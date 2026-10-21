#!/usr/bin/env python3
"""Attacks the app like a bot or a malicious user would. Run against the dev server (SQLite, no config/config.php):
    php -S 127.0.0.1:8099 -t app ;  rm -f app/var/ef.sqlite* ;  python3 app/tests/security_test.py
Delete app/var/ef.sqlite* before running again (it uses up the per-connection quotas it is testing)."""
import base64, hashlib, hmac, json, os, re, sqlite3, time, urllib.parse, urllib.request, http.cookiejar

BASE = "http://127.0.0.1:8099"
APP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SECRET = "local-dev-secret-local-dev-secret-local-dev-secret-0000"
ITEMS = {i["id"]: i for i in json.load(open(os.path.join(APP, "content", "items.json")))}
DB = os.path.join(APP, "var", "ef.sqlite")


def b64u(b): return base64.urlsafe_b64encode(b).rstrip(b"=").decode()
def token(p):
    x = b64u(json.dumps(p).encode()); return x + "." + b64u(hmac.new(SECRET.encode(), x.encode(), hashlib.sha256).digest())

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k): return None

class C:
    def __init__(self, cookies=None):
        self.cj = http.cookiejar.CookieJar(); self.op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cj), NoRedirect)
    def raw(self, url, data=None, headers=None):
        try:
            r = self.op.open(urllib.request.Request(BASE + url, data=data, headers=headers or {})); return r.status, r.read().decode(), r.headers
        except urllib.error.HTTPError as e: return e.code, e.read().decode(), e.headers
    def api(self, route, data=None, **q):
        url = "/api.php?r=" + route + "".join(f"&{k}={urllib.parse.quote(str(v))}" for k, v in q.items())
        s, b, h = self.raw(url, json.dumps(data).encode() if data is not None else None, {"X-EF": "1", "Content-Type": "application/json"})
        try: j = json.loads(b)
        except Exception: j = {"_raw": b}
        j["_status"] = s; j["_headers"] = h; return j
    def guest(self, name="Sec test"): return self.api("guest", {"nickname": name, "t": 5000})

def sso(c, uid, name="Sec Student", teacher=False):
    return c.raw("/sso.php?token=" + urllib.parse.quote(token({"uid": uid, "name": name, "teacher": teacher, "exp": int(time.time()) + 100, "n": os.urandom(6).hex()})))

def dumps(r): return json.dumps({k: v for k, v in r.items() if k != "_headers"})
def correct(it): return it["correct"] if it["kind"] == "mcq" else ([b[0] for b in it["answers"]] if it["kind"] == "gap" else (it["answers"][0][0] if it["kind"] == "text" else it["model"]))

ok = True
def check(n, c, x=""):
    global ok; ok &= bool(c); print(("PASS " if c else "FAIL ") + n + ("  -> " + str(x)[:160] if not c else ""))

# ---- 1. files and headers
ht = open(os.path.join(APP, ".htaccess")).read()
for h in ["Content-Security-Policy", "X-Frame-Options", "X-Content-Type-Options", "Referrer-Policy", "Permissions-Policy", "Strict-Transport-Security"]:
    check(f".htaccess sets {h}", h in ht)
check("CSP: no inline scripts, no outside scripts, no plugins, no framing", all(x in ht for x in ["script-src 'self'", "object-src 'none'", "frame-ancestors 'self'", "default-src 'self'"]) and "unsafe-eval" not in ht and "script-src 'self' 'unsafe-inline'" not in ht)
check("camera, microphone and location are switched off", "camera=()" in ht and "microphone=()" in ht and "geolocation=()" in ht)
for d in ["src", "content", "config", "var", "bin"]:
    check(f"{d}/ is closed by its own .htaccess", "Require all denied" in open(os.path.join(APP, d, ".htaccess")).read())
check("answers are in a .php file that prints nothing when requested", open(os.path.join(APP, "content", "items.php")).read().startswith("<?php"))
s, body, h = C().raw("/content/items.php"); check("requesting the answer file shows no answers", "correct" not in body and '"why"' not in body, body[:80])
js = open(os.path.join(APP, "assets", "app.js")).read() + open(os.path.join(APP, "assets", "ui.js")).read()
inner = [l.strip() for l in js.splitlines() if "innerHTML" in l]
check("no eval / document.write in the app code", not re.search(r"eval\(|document\.write|new Function|insertAdjacentHTML", js))
check("innerHTML is only used for the built-in icon and avatar shapes (fixed strings)", len(inner) == 3 and all(re.match(r"(s|grp)\.innerHTML = (ICONS\[name\] \|\| ''|AV_GLYPHS\[parts\[0\]\];|AV_CHARS\[parts\[0\]\];)", l) for l in inner), inner)
check("no third-party hosts in the app code", not re.search(r"https?://(?!127\.0\.0\.1|www\.w3\.org)", js), re.findall(r"https?://[^'\" )]+", js)[:3])

# ---- 2. API basics
r = C().api("config"); hd = r["_headers"]
check("API: nosniff and no-store", hd.get("X-Content-Type-Options") == "nosniff" and "no-store" in (hd.get("Cache-Control") or ""))
g = C(); r = g.guest(); sc = " ".join(h for k, h in r["_headers"].items() if k.lower() == "set-cookie")
check("session cookie is HttpOnly and SameSite=Lax", "HttpOnly" in sc and "SameSite=Lax" in sc, sc)
check("POST without the custom header refused (CSRF)", C().raw("/api.php?r=guest", b'{"nickname":"x","t":5000}', {"Content-Type": "application/json"})[0] == 400)
check("unknown route is a plain 404", C().api("../../etc/passwd")["_status"] == 404)
check("no stack trace or path in an error", "/home/" not in dumps(C().api("session/current", id="x")) and "Exception" not in dumps(C().api("session/current", id="x")))
for route in ["dashboard", "leaderboard", "session/resume", "account/export", "heartbeat"]:
    check(f"{route} needs a login", C().api(route, {} if route == "heartbeat" else None)["_status"] == 401)
for route in ["teacher/students", "teacher/student", "teacher/export", "teacher/sync-status"]:
    check(f"{route}: guests are refused", g.api(route)["_status"] == 403 if route != "teacher/export" else g.raw("/api.php?r=teacher/export")[0] == 403)
check("teacher/moderate: guests are refused", g.api("teacher/moderate", {"user_id": 1, "hide": True})["_status"] == 403)

# ---- 3. injection
for payload in ["x'; DROP TABLE users;--", "' OR '1'='1", "<img src=x onerror=alert(1)>", "<script>alert(1)</script>", "../../etc/passwd", "a" * 500, "‮evil", "name\x00null"]:
    r = C().guest(payload)
    check(f"hostile name refused or made harmless: {payload[:22]!r}", r["_status"] == 400 or ("<" not in r.get("user", {}).get("nickname", "") and len(r.get("user", {}).get("nickname", "")) <= 30), r.get("user"))
con = sqlite3.connect(DB)
check("tables still there after the SQL attempts", con.execute("SELECT COUNT(1) FROM users").fetchone()[0] > 0)
r = g.api("session/start", {"mode": "practice", "skills": ["present_simple' OR 1=1 --"], "level": "A2.1' --", "length": 10}); check("hostile skill/level refused", r["_status"] == 400, r.get("error"))
r = g.api("session/start", {"mode": "practice", "skills": ["present_simple"], "level": "A2.1", "length": 10}); sid = r["session"]["id"]; iid = r["item"]["id"]
r = g.api("session/answer", {"session_id": sid, "item_id": "x' OR 1=1 --", "answer": "x", "time_ms": 1}); check("hostile item id refused", r["_status"] in (404, 409), r)
r = g.api("session/answer", {"session_id": sid, "item_id": iid, "answer": "'; DELETE FROM attempts; --", "time_ms": 1}); check("hostile answer text is just a wrong answer", r["_status"] == 200 and r["result"]["correct"] is False, r)
check("answer text is stored, not executed", con.execute("SELECT COUNT(1) FROM attempts").fetchone()[0] >= 1)
check("period is a whitelist", g.api("leaderboard", period="week'; --")["period"] == "week")

# ---- 4. bots
r = C().api("guest", {"nickname": "bot", "t": 5000, "website": "http://spam.example"}); check("bot trap: a filled hidden field is refused", r["_status"] == 400)
r = C().api("guest", {"nickname": "bot"}); check("bot trap: a form posted without the timer is refused", r["_status"] == 400)
r = C().api("guest", {"nickname": "bot", "t": 100}); check("bot trap: a form 'filled' in 0.1 s is refused", r["_status"] == 400)
b = C(); b.guest("Fast bot"); got429 = False
for _ in range(10):
    s = b.api("session/start", {"mode": "practice", "skills": ["present_simple"], "level": "A2.1", "length": 30}); item = s["item"]; sid = s["session"]["id"]
    for _ in range(30):
        a = b.api("session/answer", {"session_id": sid, "item_id": item["id"], "answer": correct(ITEMS[item["id"]]), "time_ms": 1})
        if a["_status"] == 429: got429 = True; break
        if a.get("done") or not a.get("next"): break
        item = a["next"]
    if got429: break
check("a script answering 45+ tasks a minute is slowed down", got429)
g2 = C(); g2.guest("Daily cap"); gid = g2.api("me")["user"]["id"]
con.executemany("INSERT INTO attempts (user_id, psession_id, item_id, skill, level, bloom, correct, answer, time_ms, xp, created_at) VALUES (?,?,?,?,?,?,?,?,?,?,?)", [(gid, 0, "x", "present_simple", "A2.1", 1, 1, "", 1000, 0, int(time.time()) - 3000) for _ in range(600)]); con.commit()
s = g2.api("session/start", {"mode": "practice", "skills": ["present_simple"], "level": "A2.1", "length": 10}); a = g2.api("session/answer", {"session_id": s["session"]["id"], "item_id": s["item"]["id"], "answer": correct(ITEMS[s["item"]["id"]]), "time_ms": 3000})
check("a guest's daily limit points to registering", a["_status"] == 429 and "free account" in a.get("error", ""), a.get("error"))

# ---- 5. sessions
c = C(); c.cj.set_cookie(http.cookiejar.Cookie(0, "efp", "attackerchosen123", None, False, "127.0.0.1", False, False, "/", True, False, None, False, None, None, {}))
c.guest("Fixation"); sid_after = [ck.value for ck in c.cj if ck.name == "efp"]
check("session fixation: a session id chosen by an attacker is not kept", sid_after and "attackerchosen123" not in sid_after, sid_after)
check("another browser cannot use someone else's session", C().api("me")["user"] is None)
a1 = C(); a1.guest("Alice priv"); a2 = C(); a2.guest("Bob priv")
s1 = a1.api("session/start", {"mode": "practice", "skills": ["present_simple"], "level": "A2.1", "length": 10})
r = a2.api("session/answer", {"session_id": s1["session"]["id"], "item_id": s1["item"]["id"], "answer": "x", "time_ms": 1}); check("a learner cannot answer in someone else's session", r["_status"] == 404, r.get("error"))
r = a2.api("session/summary", id=s1["session"]["id"]); check("a learner cannot read someone else's summary", r["_status"] == 404, r.get("error"))
r = a2.api("session/quit", {"session_id": s1["session"]["id"]}); check("a learner cannot end someone else's session", r["_status"] == 404, r.get("error"))
r = a2.api("session/current", id=str(s1["session"]["id"]) + " OR 1=1"); check("an injected id in the URL is read as a plain number, and still not Alice's session", r["_status"] == 404, r.get("error"))
check("guests cannot read other people's data", "Alice" not in dumps(a2.api("leaderboard")) and "Alice" not in dumps(a2.api("account/export")))

# ---- 6. website login (forged teachers)
t = C(); r = t.raw("/sso.php?token=" + urllib.parse.quote(token({"uid": 5, "teacher": True, "exp": int(time.time()) + 100, "n": "zz"}).replace("A", "B", 1))); check("a forged teacher token is refused", r[0] == 400 and not t.api("me")["user"], r[0])
tc = C(); sso(tc, 7000 + int(time.time()) % 900, "Real Teacher", True); check("a real teacher token works", tc.api("me")["user"]["role"] == "teacher")
check("the teacher can use the teacher pages", tc.api("teacher/students")["_status"] == 200)
con.execute("UPDATE users SET sso_at = ? WHERE role = 'teacher'", (int(time.time()) - 90000,)); con.commit()
check("teacher access expires after a day without a website login", tc.api("teacher/students")["_status"] == 401)
sso(tc, tc.api("me")["user"]["id"] and 7000 + int(time.time()) % 900, "Real Teacher", True)
check("signing in again from the website restores it", tc.api("teacher/students")["_status"] == 200)
sso(tc, 7000 + int(time.time()) % 900, "Real Teacher", False)
check("a teacher demoted on the website loses the role at the next login", tc.api("me")["user"]["role"] == "student" and tc.api("teacher/students")["_status"] == 403)
sso(tc, 7000 + int(time.time()) % 900, "Real Teacher", True)

# ---- 7. moderation
bad = C(); sso(bad, 8800 + int(time.time()) % 90, "Rude Person"); bad.api("account/profile", {"nickname": "Rude Person", "show_on_board": True})
practise = bad.api("session/start", {"mode": "practice", "skills": ["present_simple"], "level": "A2.1", "length": 5}); it = practise["item"]
bad.api("session/answer", {"session_id": practise["session"]["id"], "item_id": it["id"], "answer": correct(ITEMS[it["id"]]), "time_ms": 3000})
check("registered learner is on the leaderboard", any(x["nickname"] == "Rude Person" for x in bad.api("leaderboard", period="all")["rows"]))
bid = bad.api("me")["user"]["id"]
check("teacher can hide a name", tc.api("teacher/moderate", {"user_id": bid, "hide": True})["_status"] == 200 and not any(x["nickname"] == "Rude Person" for x in bad.api("leaderboard", period="all")["rows"]))
check("teacher can reset a name", tc.api("teacher/moderate", {"user_id": bid, "reset_name": True})["_status"] == 200 and bad.api("me")["user"]["nickname"].startswith("Learner "))
check("teacher can show the learner again", tc.api("teacher/moderate", {"user_id": bid, "hide": False})["_status"] == 200)
check("moderation of a missing learner is a clean 404", tc.api("teacher/moderate", {"user_id": 999999, "hide": True})["_status"] == 404)

# ---- 7b. avatars: a fixed list, nothing else
av = C(); av.guest("Avatar fan")
check("a valid avatar is saved", av.api("account/profile", {"avatar": "comet-plum"})["user"]["avatar"] == "comet-plum")
for bad_av in ['flame-raspberry"><script>alert(1)</script>', "../../etc/passwd", "flame", "flame-neon", "nope-gold", "<svg onload=alert(1)>", "a" * 300, "flame-raspberry-x"]:
    check(f"hostile avatar refused: {bad_av[:24]!r}", av.api("account/profile", {"avatar": bad_av})["_status"] == 400)
check("the avatar is unchanged after the attempts", av.api("me")["user"]["avatar"] == "comet-plum")
dflt = av.api("account/profile", {"avatar": None})["user"]["avatar"]
check("clearing the avatar gives an assigned symbol, the same every time", bool(re.fullmatch(r"(flame|spark|bolt|sun|thermo|wave|comet|leaf)-(raspberry|gold|ink|cream|plum|sand)", dflt or "")) and av.api("me")["user"]["avatar"] == dflt, dflt)
for good_av in ["fox-gold", "ada-plum", "hana-cream", "initial-ink", "ivan-sand", "ember-ink"]:
    check(f"character / initial avatar accepted: {good_av}", av.api("account/profile", {"avatar": good_av})["user"]["avatar"] == good_av)
check("a character alone (no colour) is refused", av.api("account/profile", {"avatar": "fox"})["_status"] == 400)
av.api("account/profile", {"avatar": "spark-gold"})
check("a guest's avatar shows to the teacher", any(x["avatar"] == "spark-gold" for x in tc.api("teacher/students")["students"]))
rw = C(); sso(rw, 9500 + int(time.time()) % 90, "Avatar Reg"); rw.api("account/profile", {"nickname": "Avatar Reg", "show_on_board": True, "avatar": "sun-ink"})
pr = rw.api("session/start", {"mode": "practice", "skills": ["present_simple"], "level": "A2.1", "length": 5}); it = pr["item"]
rw.api("session/answer", {"session_id": pr["session"]["id"], "item_id": it["id"], "answer": correct(ITEMS[it["id"]]), "time_ms": 3000})
check("the avatar shows on the leaderboard", any(x["nickname"] == "Avatar Reg" and x["avatar"] == "sun-ink" for x in rw.api("leaderboard", period="all")["rows"]))

# ---- 7c. the 'Create account' step and long sign-in
s_, _, hh = C().raw("/register.php")
loc = hh.get("Location") or ""; ck = " ".join(v for k, v in hh.items() if k.lower() == "set-cookie")
check("register.php sends people to the website's form", s_ == 302 and loc.startswith("http"), (s_, loc))
check("register.php leaves a short-lived marker", "ef_return=" in ck and "HttpOnly" in ck and ("Max-Age" in ck or "expires" in ck.lower()), ck)
m_ = re.search(r"Max-Age=(\d+)", " ".join(v for k, v in C().guest("Long sign in")["_headers"].items() if k.lower() == "set-cookie"))
check("people stay signed in for about 90 days", m_ and 85 * 86400 <= int(m_.group(1)) <= 91 * 86400, m_.group(1) if m_ else None)

# ---- 8. the CSV cannot carry a spreadsheet formula
fx = C(); sso(fx, 9300 + int(time.time()) % 90, "=HYPERLINK(\"http://evil\",\"x\")"); fx.api("account/profile", {"nickname": "Formula Fan", "show_on_board": False})
s, csv, _ = tc.raw("/api.php?r=teacher/export")
check("CSV export neutralises formulas", not re.search(r'(^|,)"?=HYPERLINK', csv, re.M), csv[:120])

print("\nALL PASS" if ok else "\nSOME FAILED"); raise SystemExit(0 if ok else 1)
