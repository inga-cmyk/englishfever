#!/usr/bin/env python3
"""Guests, website login (signed token), guest -> account merge, teacher access, privacy functions.
Run against the dev server:   php -S 127.0.0.1:8099 -t app    then    python3 app/tests/sso_test.py
Needs the SQLite config (no config/config.php) so it can age a guest for the purge check.
Delete app/var/ef.sqlite* before running again: the last check uses up this connection's hourly guest quota."""
import base64, hashlib, hmac, json, os, sqlite3, subprocess, time, urllib.request, urllib.parse, http.cookiejar

BASE = "http://127.0.0.1:8099"
APP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SECRET = "local-dev-secret-local-dev-secret-local-dev-secret-0000"
ITEMS = {i["id"]: i for i in json.load(open(os.path.join(APP, "content", "items.json")))}


def b64u(b): return base64.urlsafe_b64encode(b).rstrip(b"=").decode()


def token(payload, secret=SECRET):
    p = b64u(json.dumps(payload).encode())
    return p + "." + b64u(hmac.new(secret.encode(), p.encode(), hashlib.sha256).digest())


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k): return None


class C:
    def __init__(self):
        self.cj = http.cookiejar.CookieJar()
        self.op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cj), NoRedirect)

    def raw(self, url, data=None, headers=None):
        req = urllib.request.Request(BASE + url, data=data, headers=headers or {})
        try:
            r = self.op.open(req); return r.status, r.read().decode(), r.headers
        except urllib.error.HTTPError as e:
            return e.code, e.read().decode(), e.headers

    def api(self, route, data=None, **q):
        url = "/api.php?r=" + route + "".join(f"&{k}={v}" for k, v in q.items())
        s, body, _ = self.raw(url, json.dumps(data).encode() if data is not None else None, {"X-EF": "1", "Content-Type": "application/json"})
        j = json.loads(body); j["_status"] = s; return j


def sso(c, uid, name="Maria Test", teacher=False, **kw):
    p = {"uid": uid, "name": name, "teacher": teacher, "exp": int(time.time()) + 120, "n": os.urandom(6).hex()}
    p.update(kw)
    return c.raw("/sso.php?token=" + urllib.parse.quote(token(p)))


def answer_some(c, n=4, skills=("present_simple",), level="A2.1", correct=True):
    r = c.api("session/start", {"mode": "practice", "skills": list(skills), "level": level, "length": 10})
    item = r["item"]; sid = r["session"]["id"]
    for _ in range(n):
        it = ITEMS[item["id"]]
        ans = it["correct"] if it["kind"] == "mcq" else ([b[0] for b in it["answers"]] if it["kind"] == "gap" else (it["answers"][0][0] if it["kind"] == "text" else (it["sentence"].split(" ") if it["kind"] == "order" else ([p[1] for p in it["pairs"]] if it["kind"] == "match" else it["model"]))))
        if not correct: ans = it["wrong"][0] if it["kind"] == "mcq" else ("zzz" if it["kind"] != "gap" else ["zzz"] * len(it["answers"]))
        a = c.api("session/answer", {"session_id": sid, "item_id": it["id"], "answer": ans, "time_ms": 3000})
        if a.get("done") or not a.get("next"): break
        item = a["next"]


ok = True
def check(name, cond, extra=""):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name + ("  -> " + str(extra) if extra and not cond else ""))


uniq = os.urandom(3).hex()

# 1. guests
g = C()
r = g.api("guest", {"t": 5000, "nickname": "Anna K. " + uniq})
check("guest can start with a nickname with spaces", r["_status"] == 200 and r["user"]["guest"] and r["user"]["provider"] == "guest", r)
check("guest is a student", r["user"]["role"] == "student")
nn = C().api("guest", {"t": 5000, "nickname": "   "})
check("guest without a name gets a number", nn["_status"] == 200 and nn["user"]["nickname"].startswith("Guest ") and nn["user"]["guest"], nn)
check("1-letter nickname refused", C().api("guest", {"t": 5000, "nickname": "A"})["_status"] == 400)
check("html in nickname refused", C().api("guest", {"t": 5000, "nickname": "<b>x</b>"})["_status"] == 400)
check("reserved nickname refused", C().api("guest", {"t": 5000, "nickname": "teacher"})["_status"] == 400)
g2 = C()
check("two guests may use the same nickname", g2.api("guest", {"t": 5000, "nickname": "Anna K. " + uniq})["_status"] == 200)
answer_some(g, 5, ("present_simple",), "A2.1")
dash = g.api("dashboard")
check("guest practice is recorded", dash["totals"]["answers"] >= 3, dash["totals"])
lb = g.api("leaderboard")
check("guest sees a guest note and is not on the leaderboard", lb["guest"] is True and not any(x["me"] for x in lb["rows"]), lb)
check("guest cannot turn the leaderboard on", g.api("account/profile", {"show_on_board": True})["user"]["show_on_board"] is False)
check("old password routes are gone", C().api("register", {"nickname": "xx", "password": "yyyy"})["_status"] == 404 and C().api("login", {})["_status"] == 404)
check("POST without X-EF header refused", C().raw("/api.php?r=guest", b"{}", {"Content-Type": "application/json"})[0] == 400)

# 2. website login: valid / replay / forged / expired
wp_uid = 8000 + int(time.time()) % 900
s = C()
st, _, hd = sso(s, wp_uid, name="Maria Test " + uniq)
check("valid token redirects to the app", st == 302 and "#/home" in (hd.get("Location") or ""), st)
me = s.api("me")["user"]
check("website user starts as a student who has not confirmed the name", me and me["role"] == "student" and me["provider"] == "wp" and not me["nick_set"] and not me["guest"], me)
check("suggested name is the first name only, never the surname", me["nickname"].startswith("Maria") and "Test" not in me["nickname"], me["nickname"])
check("a new registered learner is on the leaderboard by default", me["show_on_board"] is True, me)
r = s.api("account/profile", {"nickname": "Maria " + uniq, "show_on_board": True})
check("name can be changed and confirmed", r["_status"] == 200 and r["user"]["nick_set"] and r["user"]["nickname"] == "Maria " + uniq, r)
check("same name is refused for another registered user", C().api("me")["user"] is None)
n = os.urandom(6).hex()
tk = urllib.parse.quote(token({"uid": 901, "name": "X", "teacher": False, "exp": int(time.time()) + 100, "n": n}))
a_ = C().raw("/sso.php?token=" + tk); b_ = C().raw("/sso.php?token=" + tk)
check("token works once", a_[0] == 302, a_[0]); check("replayed token refused", b_[0] == 400, b_[0])
check("wrong secret refused", C().raw("/sso.php?token=" + urllib.parse.quote(token({"uid": 902, "exp": int(time.time()) + 100, "n": "zz1"}, "x" * 40)))[0] == 400)
check("expired token refused", C().raw("/sso.php?token=" + urllib.parse.quote(token({"uid": 903, "exp": int(time.time()) - 5, "n": "zz2"})))[0] == 400)
check("far-future token refused", C().raw("/sso.php?token=" + urllib.parse.quote(token({"uid": 904, "exp": int(time.time()) + 99999, "n": "zz3"})))[0] == 400)
check("garbage refused", C().raw("/sso.php?token=abc")[0] == 400)

# 3. guest -> registered: results move over
cg = C()
cg.api("guest", {"t": 5000, "nickname": "Guesty" + uniq})
answer_some(cg, 6, ("past_simple",), "A2.1")
before = cg.api("dashboard")
check("guest has results before registering", before["totals"]["answers"] >= 3, before["totals"])
st, _, _ = sso(cg, 9000 + int(time.time()) % 900, name="New Student " + uniq)
after = cg.api("dashboard")
check("results moved into the new account", after["totals"]["answers"] == before["totals"]["answers"] and after["totals"]["xp"] == before["totals"]["xp"], (before["totals"], after["totals"]))
check("tenses moved too", any(s_["n"] > 0 for s_ in after["skills"] if s_["id"] == "past_simple"))
me2 = cg.api("me")["user"]
check("now a registered user, not a guest", me2["provider"] == "wp" and not me2["guest"], me2)

# 4. teacher via website
t = C()
sso(t, 1, name="Inga Teacher " + uniq, teacher=True)
tm = t.api("me")["user"]
check("teacher role from website", tm and tm["role"] == "teacher", tm)
lst = t.api("teacher/students")
check("teacher sees the list", lst["_status"] == 200 and len(lst["students"]) >= 3, lst.get("error"))
provs = {x["provider"] for x in lst["students"]}
check("list shows guests and registered students", {"guest", "wp"} <= provs, provs)
check("merged guest is gone from the list", not any(x["nickname"] == "Guesty" + uniq for x in lst["students"]))
sid = [x for x in lst["students"] if x["provider"] == "wp"][0]["id"]
det = t.api("teacher/student", id=sid)
check("teacher sees student detail", det["_status"] == 200 and "dashboard" in det and "recent" in det, det.get("error"))
st_, csv, hd = t.raw("/api.php?r=teacher/export")
check("CSV export has an account column", st_ == 200 and csv.lstrip("﻿").startswith("time,nickname,name,account"), csv[:60])
check("teacher not on leaderboard", t.api("leaderboard")["hidden"] is True)
check("student cannot see teacher routes", s.api("teacher/students")["_status"] == 403)
check("guest cannot see teacher routes", g.api("teacher/students")["_status"] == 403)
check("reset-password route is gone", t.api("teacher/reset-password", {"user_id": sid})["_status"] == 404)

# 5. leaderboard shows registered learners, not guests
answer_some(s, 3, ("present_simple",), "A2.1")
lb2 = s.api("leaderboard", period="all")
names = [x["nickname"] for x in lb2["rows"]]
check("registered learner on the leaderboard", ("Maria " + uniq) in names, names)
check("no guests on the leaderboard", not any(n.startswith("Anna K.") or n.startswith("Guesty") for n in names), names)

# 6. data export and delete
d = C(); dn = "Del " + uniq; d.api("guest", {"t": 5000, "nickname": dn})
check("export my data", d.api("account/export")["user"]["nickname"] == dn)
check("delete needs confirmation", d.api("account/delete", {})["_status"] == 400)
check("delete works", d.api("account/delete", {"confirm": True})["_status"] == 200)
check("deleted guest is signed out", d.api("me")["user"] is None)

# 7. guests who stay away for 60 days are purged, active ones are not
old = C(); old.api("guest", {"t": 5000, "nickname": "OldGuest" + uniq}); answer_some(old, 2, ("present_simple",), "A2.1")
new = C(); new.api("guest", {"t": 5000, "nickname": "NewGuest" + uniq})
db = sqlite3.connect(os.path.join(APP, "var", "ef.sqlite"))
db.execute("UPDATE users SET last_seen = ? WHERE nickname = ?", (int(time.time()) - 61 * 86400, "OldGuest" + uniq)); db.commit()
php = "putenv('EF_DEV=1');require 'src/Db.php';require 'src/Auth.php';Config::load();Db::connect(Config::all());Auth::purgeGuests();"
subprocess.run(["php", "-r", php], cwd=APP, check=True)
left = [r[0] for r in db.execute("SELECT nickname FROM users WHERE nickname IN (?, ?)", ("OldGuest" + uniq, "NewGuest" + uniq))]
orphans = db.execute("SELECT COUNT(1) FROM attempts WHERE user_id NOT IN (SELECT id FROM users)").fetchone()[0]
check("inactive guest purged, active guest kept", left == ["NewGuest" + uniq], left)
check("purge leaves no orphaned answers", orphans == 0, orphans)

# 8. (last, because it uses up this connection's guest quota) guest creation is limited per connection
codes = [C().api("guest", {"t": 5000, "nickname": "Bulk" + str(i)})["_status"] for i in range(110)]
check("guest creation is rate limited", 429 in codes, sorted(set(codes)))


print("\nALL PASS" if ok else "\nSOME FAILED")
raise SystemExit(0 if ok else 1)
