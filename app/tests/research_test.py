#!/usr/bin/env python3
"""Learning study: consent, random conditions, features hidden by condition, anonymised export.
Run against the dev server (SQLite; config.local.php has research_enabled and both experiments):
    php -S 127.0.0.1:8099 -t app ;  rm -f app/var/ef.sqlite* ;  python3 app/tests/research_test.py
With a MariaDB database instead (config/config.php pointing at it): EF_MYSQL_DB=<database name> python3 app/tests/research_test.py"""
import base64, csv, hashlib, hmac, io, json, os, sqlite3, subprocess, time, urllib.parse, urllib.request, http.cookiejar

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
    def __init__(self):
        self.cj = http.cookiejar.CookieJar(); self.op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cj), NoRedirect)

    def raw(self, url, data=None, headers=None):
        try:
            r = self.op.open(urllib.request.Request(BASE + url, data=data, headers=headers or {})); return r.status, r.read().decode("utf-8"), r.headers
        except urllib.error.HTTPError as e: return e.code, e.read().decode("utf-8"), e.headers

    def api(self, route, data=None, **q):
        url = "/api.php?r=" + route + "".join(f"&{k}={urllib.parse.quote(str(v))}" for k, v in q.items())
        s, b, h = self.raw(url, json.dumps(data).encode() if data is not None else None, {"X-EF": "1", "Content-Type": "application/json"})
        try: j = json.loads(b)
        except Exception: j = {"_raw": b}
        j["_status"] = s; return j

    def file(self, name):
        s, b, h = self.raw("/api.php?r=teacher/research-export&file=" + name); return s, b, h


def login(uid, name, teacher=False):
    c = C()
    c.raw("/sso.php?token=" + urllib.parse.quote(token({"uid": uid, "name": name, "teacher": teacher, "exp": int(time.time()) + 100, "n": os.urandom(6).hex()})))
    return c


def correct(it):
    k = it["kind"]
    if k == "mcq": return it["correct"]
    if k == "gap": return [b[0] for b in it["answers"]]
    if k == "text": return it["answers"][0][0]
    if k == "order": return it["sentence"].split(" ")
    if k == "match": return [p_[1] for p_ in it["pairs"]]
    return it["model"]


def practise(c, n):
    s = c.api("session/start", {"mode": "practice", "skills": ["present_simple"], "level": "A2.1", "length": 10}); item = s["item"]; sid = s["session"]["id"]
    for _ in range(n):
        a = c.api("session/answer", {"session_id": sid, "item_id": item["id"], "answer": correct(ITEMS[item["id"]]), "time_ms": 4000})
        assert a["_status"] == 200, a
        if a.get("done") or not a.get("next"): break
        item = a["next"]


def rows(text):
    return list(csv.DictReader(io.StringIO(text.lstrip("﻿"))))


ok = True
def check(n, c, x=""):
    global ok; ok &= bool(c); print(("PASS " if c else "FAIL ") + n + ("  -> " + str(x)[:200] if not c else ""))


MYSQL = os.environ.get("EF_MYSQL_DB")
con = None if MYSQL else sqlite3.connect(DB)


def dbq(sql, *p):
    """Read from the app database, whichever it is."""
    if MYSQL:
        for x in p: sql = sql.replace("?", str(int(x)) if isinstance(x, int) else "'" + str(x) + "'", 1)
        out = subprocess.run(["mysql", MYSQL, "-N", "-B", "-e", sql], capture_output=True, text=True, check=True).stdout.strip()
        return [tuple(int(v) if v.lstrip("-").isdigit() else v for v in l.split("\t")) for l in out.split("\n")] if out else []
    return con.execute(sql, p).fetchall()


teacher = login(9001, "Teacher Test", True)
check("config says the study is on", C().api("config")["research"] is True)

# ---- who can join
g = C(); g.api("guest", {"nickname": "Study guest", "t": 5000})
check("guests cannot join (no person to follow)", g.api("account/research", {"join": True})["_status"] == 403)
check("a guest's profile shows no study state or conditions", g.api("me")["user"]["research"] == 0 and dict(g.api("me")["user"]["cond"]) == {})
check("teachers cannot join", teacher.api("account/research", {"join": True})["_status"] == 403)
check("not logged in: refused", C().api("account/research", {"join": True})["_status"] == 401)

# ---- random conditions: eight people join one after the other
people = [login(8100 + i, f"Studyperson{i} Surname") for i in range(8)]
before = [p.api("me")["user"] for p in people]
check("before consent: not asked, no conditions", all(u["research"] == 0 and dict(u["cond"]) == {} for u in before), before[0])
conds = []
for p in people:
    r = p.api("account/research", {"join": True}); conds.append(r["user"]["cond"]); assert r["user"]["research"] == 1, r
check("every participant gets a condition for both factors", all(set(c) == {"streak", "leaderboard"} and all(v in ("on", "off") for v in c.values()) for c in conds), conds)
for f in ("streak", "leaderboard"):
    seq = [c[f] for c in conds]
    check(f"{f}: each block of four has two 'on' and two 'off'", seq[:4].count("on") == 2 and seq[4:].count("on") == 2, seq)
check("the two factors are not simply the same sequence", [c["streak"] for c in conds] != [c["leaderboard"] for c in conds], conds)
again = [p.api("me")["user"]["cond"] for p in people]
check("the condition stays the same on later visits", again == conds)
check("assignments are stored once per person and factor", dbq("SELECT COUNT(1) FROM conditions")[0][0] == 16, dbq("SELECT * FROM conditions"))
check("sequence numbers are 1..8 per factor", sorted(r[0] for r in dbq("SELECT seq FROM conditions WHERE factor = 'streak'")) == list(range(1, 9)))

# ---- leaving and joining again
leaver = login(8301, "Study Leaver"); r = leaver.api("account/research", {"join": True}); first = dict(r["user"]["cond"])
practise(leaver, 2)
r = leaver.api("account/research", {"join": False})
check("leaving: back to the normal app, no conditions", r["user"]["research"] == 2 and dict(r["user"]["cond"]) == {}, r)
r = leaver.api("account/research", {"join": True})
check("joining again gives the same conditions", dict(r["user"]["cond"]) == first, (r["user"]["cond"], first))
leaver.api("account/research", {"join": False})
decliner = login(8302, "Study Decliner"); r = decliner.api("account/research", {"join": False})
check("saying no is stored and gives no conditions", r["user"]["research"] == 2 and dict(r["user"]["cond"]) == {})

# ---- the leaderboard follows the condition
for p in people: practise(p, 2)
off = [i for i, c in enumerate(conds) if c["leaderboard"] == "off"]; on = [i for i, c in enumerate(conds) if c["leaderboard"] == "on"]
check("leaderboard 'off': refused by the server", all(people[i].api("leaderboard")["_status"] == 403 for i in off))
board = people[on[0]].api("leaderboard", period="all")
names = {r["nickname"] for r in board["rows"]}
check("leaderboard 'on': works", board["_status"] == 200 and f"Studyperson{on[0]}" in names, board)
check("people in the 'off' condition are not listed on it", not any(f"Studyperson{i}" in names for i in off), names)
check("people in the 'on' condition are listed", all(f"Studyperson{i}" in names for i in on), names)
check("the teacher still sees the leaderboard", teacher.api("leaderboard", period="all")["_status"] == 200)

# ---- consent date: earlier answers are not part of the study
q = login(8201, "Study Early"); practise(q, 2); q.api("heartbeat", {"seconds": 12}); time.sleep(1.2)
q.api("account/research", {"join": True}); practise(q, 3); time.sleep(3); q.api("heartbeat", {"seconds": 5})
qid = q.api("me")["user"]["id"]
seed = dbq("SELECT v FROM kv WHERE k = 'research_seed'")[0][0]
qpid = hmac.new(seed.encode(), f"pid:{qid}".encode(), hashlib.sha256).hexdigest()[:12]

# ---- export
s, people_csv, h = teacher.file("people"); P = rows(people_csv)
check("people.csv: teacher can download it as a CSV", s == 200 and "text/csv" in h["Content-Type"] and "attachment" in h["Content-Disposition"], (s, h["Content-Type"]))
check("people.csv: one row per participant (9), none for the person who left, the one who said no, the guest or the teacher", len(P) == 9, len(P))
check("people.csv: ids are 12 hex characters and different", len({r["pid"] for r in P}) == 9 and all(len(r["pid"]) == 12 and int(r["pid"], 16) >= 0 for r in P))
check("people.csv: the id is the keyed hash (so it can be rebuilt from the stored key and is not the user number)", qpid in {r["pid"] for r in P} and str(qid) not in {r["pid"] for r in P})
mine = [r for r in P if r["pid"] == qpid][0]
check("people.csv: only answers after the consent count (3, not 5)", mine["answers"] == "3", mine)
total = dbq("SELECT seconds FROM activity WHERE user_id = ?", qid)[0][0]
check("people.csv: time recorded before the consent is not counted (the day's total minus the 12 s already there)", dbq("SELECT research_base FROM users WHERE id = ?", qid)[0][0] == 12 and total > 12 and mine["seconds"] == str(total - 12), (mine["seconds"], total))
check("people.csv: one active day, day 0, observed 1 day", mine["active_days"] == "1" and mine["first_active_day"] == "0" and mine["last_active_day"] == "0" and mine["observed_days"] == "1" and mine["longest_streak"] == "1" and mine["active_day1"] == "0", mine)
check("people.csv: the conditions are in the file", all(r["cond_streak"] in ("on", "off") and r["cond_leaderboard"] in ("on", "off") for r in P))
check("people.csv: conditions match what the learners saw", sorted((r["cond_streak"], r["cond_leaderboard"]) for r in P if r["pid"] != qpid) == sorted((c["streak"], c["leaderboard"]) for c in conds), [(r["cond_streak"], r["cond_leaderboard"]) for r in P])
check("people.csv: no calendar dates, only weeks", all(len(r["join_week"]) == 8 and "W" in r["join_week"] for r in P), P[0])
s, days_csv, h = teacher.file("days"); D = rows(days_csv)
check("days.csv: that learner has one row: study day 0, 3 answers, the same seconds", [(r["study_day"], r["answers"], r["seconds"]) for r in D if r["pid"] == qpid] == [("0", "3", str(total - 12))], [r for r in D if r["pid"] == qpid])
s, ans_csv, h = teacher.file("answers"); A = rows(ans_csv)
check("answers.csv: 3 rows for that learner", len([r for r in A if r["pid"] == qpid]) == 3)
check("answers.csv: has no answer text column", "answer" not in A[0] and set(A[0]) == {"pid", "study_day", "weekday", "hour", "mode", "skill", "area", "level", "bloom", "correct", "seconds", "item"}, list(A[0]))
check("answers.csv: area is filled", all(r["area"] == "active" for r in A), A[0])
s, readme, h = teacher.file("readme")
check("readme.txt: explains pseudonymisation and the conditions", s == 200 and "pseudonymised" in readme and "study_day" in readme and "cond_streak" in readme and "streak, leaderboard" in readme, readme[:200])
blob = people_csv + days_csv + ans_csv + readme
check("no names, nicknames or typed answers anywhere in the export", not any(x in blob for x in ["Studyperson", "Study Early", "Study Leaver", "Teacher Test", "Study Decliner", "@"]))
check("the export contains nobody who left or declined", len(A) > 0 and all(r["pid"] in {x["pid"] for x in P} for r in A + D))
check("students cannot download", people[0].file("people")[0] == 403 and people[0].api("teacher/research")["_status"] == 403)
check("not logged in cannot download", C().file("people")[0] == 401)
check("unknown file is a plain 404", teacher.file("../../config/config")[0] == 404 and teacher.file("x")[0] == 404)
sm = teacher.api("teacher/research")
check("teacher summary: 9 joined, 1 said no, both factors balanced to within one", sm["joined"] == 9 and sm["declined"] == 2 and len(sm["factors"]) == 2 and all(abs(f["on"] - f["off"]) <= 1 and f["on"] + f["off"] == 9 for f in sm["factors"]), sm)

# ---- the person's own copy of the data shows the study state
ex = people[0].api("account/export")
check("'Download my data' includes the study state and conditions", ex["study"]["status"] == "taking part" and ex["study"]["conditions"] == conds[0], ex.get("study"))

# ---- deleting an account removes it from the export and the conditions table
q.api("account/delete", {"confirm": True})
check("deleted account: conditions removed", dbq("SELECT COUNT(1) FROM conditions WHERE user_id = ?", qid)[0][0] == 0)
P2 = rows(teacher.file("people")[1])
check("deleted account: gone from the export", qpid not in {r["pid"] for r in P2} and len(P2) == 8, len(P2))

# ---- the codes stay the same between exports
P3 = rows(teacher.file("people")[1])
check("ids are the same in the next export", [r["pid"] for r in P3] == [r["pid"] for r in P2])

print("\nALL PASS" if ok else "\nSOME FAILED")
raise SystemExit(0 if ok else 1)
