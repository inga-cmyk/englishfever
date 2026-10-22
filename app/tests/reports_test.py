#!/usr/bin/env python3
"""Report a problem: who may report, what is stored, what the teacher sees and can do, privacy, limits.
Run against the dev server (SQLite):  php -S 127.0.0.1:8099 -t app ;  rm -f app/var/ef.sqlite* ;  python3 app/tests/reports_test.py"""
import base64, csv, hashlib, hmac, io, json, os, sqlite3, time, urllib.parse, urllib.request, http.cookiejar

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

    def api(self, route, data=None, xef=True, **q):
        url = "/api.php?r=" + route + "".join(f"&{k}={urllib.parse.quote(str(v))}" for k, v in q.items())
        h = {"Content-Type": "application/json"}
        if xef: h["X-EF"] = "1"
        s, b, hd = self.raw(url, json.dumps(data).encode() if data is not None else None, h)
        try: j = json.loads(b)
        except Exception: j = {"_raw": b}
        j["_status"] = s; return j


def login(uid, name, teacher=False):
    c = C()
    c.raw("/sso.php?token=" + urllib.parse.quote(token({"uid": uid, "name": name, "teacher": teacher, "exp": int(time.time()) + 100, "n": os.urandom(6).hex()})))
    return c


ok = True
def check(n, c, x=""):
    global ok; ok &= bool(c); print(("PASS " if c else "FAIL ") + n + ("  -> " + str(x)[:240] if not c else ""))


def wrong_answer(it):
    k = it["kind"]
    if k == "mcq": return it["wrong"][0]
    if k == "gap": return ["zzz" for _ in it["answers"]]
    if k == "order": return list(reversed(it["sentence"].split(" ")))
    if k == "match": return list(reversed([p[1] for p in it["pairs"]]))
    return "zzz"


def serve(c, skill, level):
    s = c.api("session/start", {"mode": "practice", "skills": [skill], "level": level, "length": 10})
    return s["session"]["id"], s["item"]["id"]


teacher = login(9101, "Teacher Reports", True)
student = login(9102 + int(time.time()) % 500, "Rita Reporter")
g = C(); g.api("guest", {"nickname": "Report guest", "t": 5000})
check("the test-version notice is on by default", C().api("config").get("beta") is True)

# ---- who may report
sid, item_id = serve(g, "present_simple", "A2.1")
check("not logged in: refused", C().api("report", {"item_id": item_id, "reason": "unclear"})["_status"] == 401)
check("without the app header: refused", g.api("report", {"item_id": item_id, "reason": "unclear"}, xef=False)["_status"] == 400)
check("unknown reason: refused", g.api("report", {"item_id": item_id, "reason": "hate"})["_status"] == 400)
check("unknown task: refused", g.api("report", {"item_id": "nope-1", "reason": "unclear"})["_status"] == 404)
check("a guest can report a task with one tap (no reason needed)", g.api("report", {"item_id": item_id})["_status"] == 200)

# ---- the answer is stored with the report
it = ITEMS[item_id]; wa = wrong_answer(it)
a = g.api("session/answer", {"session_id": sid, "item_id": item_id, "answer": wa, "time_ms": 3000}); assert a["_status"] == 200, a
check("a wrong answer is marked wrong", a["result"]["correct"] is False)
check("reporting again (after answering) updates the same report", g.api("report", {"item_id": item_id, "comment": "<b>My answer</b> is also right =1+1"})["_status"] == 200)

# ---- a second learner, same task
sid2, _ = serve(student, "present_simple", "A2.1")
check("a registered learner reports the same task", student.api("report", {"item_id": item_id, "comment": "x" * 900})["_status"] == 200)

# ---- the teacher's page
check("students cannot read reports", student.api("teacher/reports")["_status"] == 403 and g.api("teacher/reports")["_status"] == 403)
check("nobody signed in cannot read reports", C().api("teacher/reports")["_status"] == 401)
check("students cannot change a status", student.api("teacher/report-status", {"item_id": item_id, "status": "fixed"})["_status"] == 403)
check("students cannot export", student.api("teacher/reports-export")["_status"] == 403)
t = teacher.api("teacher/reports", status="open")
check("the teacher sees one task with two reports", t["_status"] == 200 and len(t["groups"]) == 1 and t["groups"][0]["count"] == 2, t)
grp = t["groups"][0]
check("the group names the task, its key and (for multiple choice) the wrong options", grp["task"]["id"] == item_id and grp["task"]["q"] == it["q"] and grp["task"]["key"] != "", grp["task"])
check("the learner's answer and its result are kept", any(r["answer"] and r["correct"] == 0 for r in grp["reports"]), grp["reports"])
check("one report per learner and task: the guest's was updated, not added", len(grp["reports"]) == 2, grp["reports"])
check("a long comment is cut to 400 characters", any(len(r["comment"]) == 400 for r in grp["reports"]))
check("html in a comment is kept as plain text (the page shows it as text)", any("<b>My answer</b>" in r["comment"] for r in grp["reports"]))
check("the teacher's own profile counts the open reports", teacher.api("me")["user"]["reports_open"] == 1 and student.api("me")["user"]["reports_open"] == 0)

# ---- the CSV
st, body, hd = teacher.raw("/api.php?r=teacher/reports-export")
rows = list(csv.DictReader(io.StringIO(body.lstrip("﻿"))))
check("the export is a CSV download", st == 200 and "text/csv" in hd["Content-Type"] and "attachment" in hd["Content-Disposition"], (st, hd["Content-Type"]))
check("the export has the task, the key, the learner's answer and the reason", len(rows) == 2 and rows[0]["task id"] == item_id and rows[0]["task"] and rows[0]["key (accepted answers)"] and any(r["learner answered"] for r in rows), rows[:1])
check("the export holds no learner names", "Rita" not in body and "Report guest" not in body and {r["learner"] for r in rows} == {"guest", "registered"})
check("a formula in a comment cannot run in a spreadsheet", all(not c.startswith("=") for r in rows for c in r.values()))

# ---- status changes
check("mark as fixed", teacher.api("teacher/report-status", {"item_id": item_id, "status": "fixed"})["_status"] == 200)
check("fixed tasks leave the open list", teacher.api("teacher/reports", status="open")["groups"] == [] and len(teacher.api("teacher/reports", status="fixed")["groups"]) == 1)
check("a wrong status is refused", teacher.api("teacher/report-status", {"item_id": item_id, "status": "deleted"})["_status"] == 400)
check("a task with no reports cannot be marked", teacher.api("teacher/report-status", {"item_id": list(ITEMS)[-1], "status": "fixed"})["_status"] == 404)
check("a new report on a fixed task opens it again", g.api("report", {"item_id": item_id, "reason": "ambiguous"})["_status"] == 200 and len(teacher.api("teacher/reports", status="open")["groups"]) == 1)
check("dismiss", teacher.api("teacher/report-status", {"item_id": item_id, "status": "dismissed"})["_status"] == 200 and len(teacher.api("teacher/reports", status="dismissed")["groups"]) == 1)

# ---- tasks that most learners get wrong
if os.path.exists(DB):
    con = sqlite3.connect(DB); uid = g.api("me")["user"]["id"]; hard_id = "ps-A22-1a"
    for i in range(9): con.execute("INSERT INTO attempts (user_id, psession_id, item_id, skill, level, bloom, correct, answer, time_ms, xp, created_at) VALUES (?,?,?,?,?,?,?,?,?,?,?)", (uid, 0, hard_id, "present_simple", "A2.2", 1, 0 if i < 8 else 1, "zzz", 1000, 0, int(time.time())))
    con.commit(); con.close()
    hard = teacher.api("teacher/reports", status="open")["hard"]
    check("a task answered wrongly by 8 of 9 attempts is listed as 'often wrong'", any(h["task"]["id"] == hard_id and h["pct"] == 89 and h["n"] == 9 for h in hard), hard)

# ---- a reported task is paused until the teacher decides
def served_ids(c, n):
    seen = set()
    for _ in range(n):
        s = c.api("session/start", {"mode": "practice", "skills": ["past_perfect"], "level": "B1.2", "length": 12}); sid = s["session"]["id"]; item = s["item"]
        for _ in range(12):
            seen.add(item["id"]); a = c.api("session/answer", {"session_id": sid, "item_id": item["id"], "answer": wrong_answer(ITEMS[item["id"]]), "time_ms": 1000})
            if a.get("done") or not a.get("next"): break
            item = a["next"]
    return seen
pauser = login(9801 + int(time.time()) % 150, "Pause Tester"); target = [i for i in ITEMS if ITEMS[i]["skill"] == "past_perfect"][0]   # a topic with only 8 tasks: one session serves them all
check("before a report the task can be served", target in served_ids(pauser, 1))
pauser.api("report", {"item_id": target})
check("a reported task is not served to anyone while the report is open", target not in served_ids(pauser, 1) and target not in served_ids(student, 1))
teacher.api("teacher/report-status", {"item_id": target, "status": "seen"})
check("marking it 'seen' keeps it paused", target not in served_ids(pauser, 1))
teacher.api("teacher/report-status", {"item_id": target, "status": "dismissed"})
check("'Not a problem' puts it back", target in served_ids(pauser, 1))

# ---- the daily limit
flood = login(9701 + int(time.time()) % 200, "Flood Tester"); ids = [i for i in ITEMS][:40]; codes = []
for i in ids: codes.append(flood.api("report", {"item_id": i, "reason": "other"})["_status"])
check("at most 30 reports a day per person", codes.count(200) == 30 and codes[30] == 429, codes)

# ---- privacy: deleting the account deletes the reports
d = C(); d.api("guest", {"nickname": "Delete me", "t": 5000}); did = d.api("me")["user"]["id"]
d.api("report", {"item_id": ids[0], "reason": "unclear"})
before = sum(len(x["reports"]) for x in teacher.api("teacher/reports", status="all")["groups"])
d.api("account/delete", {"confirm": True})
after = sum(len(x["reports"]) for x in teacher.api("teacher/reports", status="all")["groups"])
check("deleting an account deletes its reports", after == before - 1, (before, after))

print("\nALL PASS" if ok else "\nSOME FAILED"); raise SystemExit(0 if ok else 1)
