#!/usr/bin/env python3
"""Tasks uploaded by the teacher (CSV): checks row by row, drafts, approval, serving, grading, privacy.
Run against the dev server (SQLite):  php -S 127.0.0.1:8099 -t app ;  rm -f app/var/ef.sqlite* ;  python3 app/tests/tasks_test.py"""
import base64, csv, hashlib, hmac, io, json, os, time, urllib.parse, urllib.request, http.cookiejar

BASE = "http://127.0.0.1:8099"
SECRET = "local-dev-secret-local-dev-secret-local-dev-secret-0000"


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


def login(uid, name, teacher=False):
    c = C()
    c.raw("/sso.php?token=" + urllib.parse.quote(token({"uid": uid, "name": name, "teacher": teacher, "exp": int(time.time()) + 100, "n": os.urandom(6).hex()})))
    return c


ok = True
def check(n, c, x=""):
    global ok; ok &= bool(c); print(("PASS " if c else "FAIL ") + n + ("  -> " + str(x)[:300] if not c else ""))


def make_csv(rows, delim=","):
    out = io.StringIO(); w = csv.writer(out, delimiter=delim)
    w.writerow(["topic", "level", "type", "task", "correct answer", "wrong options / checks", "explanation shown to learner", "explanation in Latvian"])
    for r in rows: w.writerow(r)
    return out.getvalue()


teacher = login(9301, "Teacher Tasks", True)
student = login(9302 + int(time.time()) % 400, "Tina Tasks")
T = "Past perfect"   # a topic with only 8 tasks and one level (B1.2): a session serves them all
GOOD = [
    [T, "B1", "mcq", "Choose the correct form: She was upset because she ___ her phone.", "had lost", "lost | has lost | was losing", "Earlier action: had + past participle."],
    [T, "B1.2", "gap", "By the time I arrived, he ___ already ___. (leave)", "had / left", "", "Past perfect: had + past participle."],
    [T, "B1", "text", "Join with After: I finished work. Then I went home.", "After I had finished work, I went home.", "", "After + past perfect, then past simple."],
    [T, "B1", "order", "Put the words in order.", "they had already left when we arrived", "also accepted: when we arrived they had already left", "Past perfect for the earlier action."],
    [T, "B1", "match", "Match each beginning with the right ending.", "She had eaten = before he arrived. ; We had finished = when the bell rang. ; They had left = before the rain started.", "", "Had + past participle shows the earlier action."],
]
BAD = [
    ["Nonsense topic", "B1", "mcq", "x ___", "a", "b | c", "why"],
    [T, "A2", "mcq", "Choose: He ___ home.", "went", "go | goes", "why"],
    [T, "B1", "mcq", "Choose the correct form: ___ ", "a", "a | b", "same option"],
    [T, "B1", "mcq", "Choose the correct form: only one wrong ___", "a", "b", "needs two wrong"],
    [T, "B1", "gap", "No blank here", "x", "", "why"],
    [T, "B1", "gap", "Two blanks ___ and ___", "one", "", "why"],
    [T, "B1", "order", "Order", "too short", "", "why"],
    [T, "B1", "match", "Match", "a = b ; c = d", "", "only 2 pairs"],
    [T, "B1", "write", "Write one sentence", "model", "", "why"],
    [T, "B1", "mcq", "Choose the correct form: no explanation ___", "a", "b | c", ""],
]

check("students cannot use the Tasks routes", all(student.api(r)["_status"] == 403 for r in ("teacher/items",)) and student.api("teacher/items-import", {"csv": "x"})["_status"] == 403)
check("nobody signed in cannot either", C().api("teacher/items")["_status"] == 401)
st, body, hd = teacher.raw("/api.php?r=teacher/items-template")
tmpl = list(csv.DictReader(io.StringIO(body.lstrip("﻿"))))
check("the template is a CSV with one example per type", st == 200 and "text/csv" in hd["Content-Type"] and {r["type"] for r in tmpl} == {"mcq", "gap", "text", "order", "match"}, (st, tmpl[:1]))
t = teacher.api("teacher/items-import", {"csv": body.lstrip("﻿")})
check("the template itself passes every check", t["ok"] == 6 and t["bad"] == 0, t)
check("a check run saves nothing", sum(len(v) for v in teacher.api("teacher/items")["items"].values()) == 0)

r = teacher.api("teacher/items-import", {"csv": make_csv(GOOD + BAD)})
check("good rows pass, bad rows fail, each with a message", r["ok"] == len(GOOD) and r["bad"] == len(BAD) and all(x["errors"] for x in r["rows"] if not x["ok"]), [(x["line"], x["errors"]) for x in r["rows"]])
msgs = " ".join(" ".join(x["errors"]) for x in r["rows"])
for needle in ("Unknown topic", "no A2", "same", "at least 2 wrong", "needs ___", "2 blanks", "4 to 16", "3 to 6", "not supported", "explanation is empty"):
    check(f"message: {needle}", needle.lower() in msgs.lower() or needle in msgs, msgs[:200])
check("a semicolon file (Excel in Latvia) is read too", teacher.api("teacher/items-import", {"csv": make_csv(GOOD[:1], ";")})["ok"] == 1)

r = teacher.api("teacher/items-import", {"csv": make_csv(GOOD + BAD), "confirm": True})
check("importing saves only the good rows, as drafts", r["ok"] == len(GOOD) and r["saved"] and sum(1 for x in r["rows"] if x.get("id")) == len(GOOD), r)
lst = teacher.api("teacher/items")["items"]
check("they are listed as drafts", len(lst["draft"]) == len(GOOD) and not lst["approved"], {k: len(v) for k, v in lst.items()})
ids = [x["id"] for x in lst["draft"]]
check("ids look like c-0001", all(i.startswith("c-") for i in ids), ids)
again = teacher.api("teacher/items-import", {"csv": make_csv(GOOD)})
check("uploading the same file again adds nothing: every row is already there, none is a problem", again["ok"] == 0 and again["bad"] == 0 and again["same"] == len(GOOD), again)
text_item = [x for x in lst["draft"] if x["kind"] == "text"][0]
check("a typed answer gets the other clause order added automatically", "I went home after I had finished work" in text_item["key"], text_item["key"])


_uid = [9500 + int(time.time()) % 300]
def fresh():
    _uid[0] += 1
    return login(_uid[0], "Fresh Learner")   # the app limits one person to 45 answers a minute


def junk(item):
    k = item["kind"]
    if k == "mcq": return item["options"][0]
    if k == "gap": return ["zzz"] * item.get("blanks", 1)
    if k == "order": return item["tokens"]
    if k == "match": return item["rights"]
    return "zzz zzz"


def served(c):
    c = fresh()
    seen = set()
    s = c.api("session/start", {"mode": "practice", "skills": ["past_perfect"], "level": "B1.2", "length": 20}); sid = s["session"]["id"]; item = s["item"]
    for _ in range(20):
        seen.add(item["id"]); a = c.api("session/answer", {"session_id": sid, "item_id": item["id"], "answer": junk(item), "time_ms": 500})
        if a.get("done") or not a.get("next"): break
        item = a["next"]
    return seen

check("drafts are not served to learners", not (served(student) & set(ids)))
check("a student cannot approve", student.api("teacher/items-status", {"ids": ids, "status": "approved"})["_status"] == 403)
check("a wrong status is refused", teacher.api("teacher/items-status", {"ids": ids, "status": "deleted"})["_status"] == 400)
check("approve all", teacher.api("teacher/items-status", {"ids": ids, "status": "approved"})["changed"] == len(ids))
check("approved tasks are served", set(ids) <= served(student), served(student))

# grading each type with the real grader
def answer_item(c, iid, ans):
    c = fresh()
    s = c.api("session/start", {"mode": "practice", "skills": ["past_perfect"], "level": "B1.2", "length": 20}); sid = s["session"]["id"]; item = s["item"]
    for _ in range(20):
        if item["id"] == iid:
            r = c.api("session/answer", {"session_id": sid, "item_id": iid, "answer": ans(item), "time_ms": 500})["result"]
            c.api("session/quit", {"session_id": sid})   # finish the session so the next one can start
            return r
        a = c.api("session/answer", {"session_id": sid, "item_id": item["id"], "answer": junk(item), "time_ms": 500})
        if a.get("done") or not a.get("next"): break
        item = a["next"]
    return None

by = {x["kind"]: x["id"] for x in lst["draft"]}
check("mcq: the right option is right", (answer_item(student, by["mcq"], lambda it: "had lost") or {}).get("correct") is True)
check("mcq: a wrong option is wrong", (answer_item(student, by["mcq"], lambda it: "lost") or {}).get("correct") is False)
check("gap: both blanks", (answer_item(student, by["gap"], lambda it: ["had", "left"]) or {}).get("correct") is True)
check("text: the first clause order", (answer_item(student, by["text"], lambda it: "After I had finished work, I went home.") or {}).get("correct") is True)
check("text: the other clause order (added automatically)", (answer_item(student, by["text"], lambda it: "I went home after I had finished work.") or {}).get("correct") is True)
check("text: a wrong answer", (answer_item(student, by["text"], lambda it: "After I finished work, I go home.") or {}).get("correct") is False)
check("order: the right order", (answer_item(student, by["order"], lambda it: "they had already left when we arrived".split(" ")) or {}).get("correct") is True)
check("order: the other accepted order", (answer_item(student, by["order"], lambda it: "when we arrived they had already left".split(" ")) or {}).get("correct") is True)
check("match: the right pairs", (answer_item(student, by["match"], lambda it: ["before he arrived.", "when the bell rang.", "before the rain started."]) or {}).get("correct") is True)

# reports and pausing work with these tasks
student.api("report", {"item_id": by["mcq"]})
check("a reported custom task is paused", by["mcq"] not in served(student))
check("the teacher's Reports page can describe it", any(g["task"]["id"] == by["mcq"] for g in teacher.api("teacher/reports", status="open")["groups"]))
teacher.api("teacher/report-status", {"item_id": by["mcq"], "status": "dismissed"})
check("retire takes tasks out", teacher.api("teacher/items-status", {"ids": [by["match"]], "status": "retired"})["changed"] == 1 and by["match"] not in served(student))
check("a retired task still opens for old answers", student.api("report", {"item_id": by["match"]})["_status"] == 200)
# every draft file in docs/task-drafts must pass the checks as it is, and a new topic stays hidden until it has approved tasks
import glob
for f in sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "docs", "task-drafts", "*.csv"))):
    res = teacher.api("teacher/items-import", {"csv": open(f, encoding="utf-8-sig").read()})
    check("draft file passes every check: " + os.path.basename(f), res["bad"] == 0 and res["ok"] > 0, [(x["line"], x["errors"]) for x in res["rows"] if not x["ok"]])
pp = teacher.api("teacher/items-import-prepared", {})
check("prepared questions: all draft files are checked at once, without problems", pp["_status"] == 200 and len(pp["files"]) >= 15 and pp["bad"] == 0 and pp["ok"] > 2000, {k: pp.get(k) for k in ("ok", "updated", "same", "bad")})
pa = teacher.api("teacher/items-import-prepared", {"confirm": True})
pp2 = teacher.api("teacher/items-import-prepared", {})
check("Add all saves them; checking again finds nothing new or changed", pa["ok"] == pp["ok"] and pp2["ok"] == 0 and pp2["updated"] == 0 and pp2["bad"] == 0, ({k: pa.get(k) for k in ("ok", "updated")}, {k: pp2.get(k) for k in ("ok", "updated", "same", "bad")}))
check("students cannot use it", student.api("teacher/items-import-prepared", {})["_status"] == 403)
check("a topic with no approved tasks is hidden from learners", not any(s["id"] == "modal_verbs" for s in C().api("meta")["skills"]))
mv = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "docs", "task-drafts", "modal-verbs-1.csv"), encoding="utf-8-sig").read()
imp = teacher.api("teacher/items-import", {"csv": mv, "confirm": True})
mids = [x["id"] for x in teacher.api("teacher/items")["items"]["draft"]]
check("drafts alone do not show the topic", not any(s["id"] == "modal_verbs" for s in C().api("meta")["skills"]))
teacher.api("teacher/items-status", {"ids": mids, "status": "approved"})
m = C().api("meta"); sk = [s for s in m["skills"] if s["id"] == "modal_verbs"]
check("after approval the topic and its area appear, with the grammar card", len(sk) == 1 and sk[0]["rule"]["form"] and sk[0]["rule_lv"]["form"] and "Modal verbs" in [a["label"] for a in m["areas"]], sk[:1])
sm = student.api("session/start", {"mode": "practice", "skills": ["modal_verbs"], "level": "A2.1", "length": 10})
check("a learner can practise the new topic", sm["_status"] == 200 and sm["item"]["skill"] == "modal_verbs", sm)
# practice only: the column is read and kept with the task (never in the placement test)
import sqlite3
cmp = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "docs", "task-drafts", "comparison-1.csv"), encoding="utf-8-sig").read()
teacher.api("teacher/items-import", {"csv": cmp, "confirm": True})
db = sqlite3.connect(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "var", "ef.sqlite"))
po = [json.loads(d) for (d,) in db.execute("select data from custom_items where data like '%practice_only%'")]
check("a CSV row marked practice only keeps the mark", any(x.get("practice_only") is True and x["q"].startswith("Match each adjective with its comparative") for x in po), [x.get("q") for x in po])
# a task moved to another topic ("from: Past simple" in the replaces column): the old copy is retired, results stay
HEAD2 = ["topic", "level", "type", "task", "correct answer", "wrong options / checks", "explanation shown to learner", "explanation in Latvian", "thinking level", "replaces"]
def csv2(rows):
    out = io.StringIO(); w = csv.writer(out); w.writerow(HEAD2); [w.writerow(r) for r in rows]; return out.getvalue()
oldrow = ["Past simple", "B1.1", "mcq", "Choose the correct option: As a child I ___ milk every morning.", "used to drink", "use to drink | was used to drink", "Used to + base verb.", "", "2", ""]
teacher.api("teacher/items-import", {"csv": csv2([oldrow]), "confirm": True})
oldid = [r[0] for r in db.execute("select item_id from custom_items where data like '%milk every morning%' and status <> 'retired'")]
mv2 = teacher.api("teacher/items-import", {"csv": csv2([["Used to and be used to"] + oldrow[1:9] + ["from: Past simple"]]), "confirm": True})
st2 = dict(db.execute("select item_id, status from custom_items where data like '%milk every morning%'").fetchall())
check("a moved task retires its old copy and adds the new one", len(oldid) == 1 and st2.get(oldid[0]) == "retired" and sum(1 for v in st2.values() if v != "retired") == 1, (oldid, st2, mv2["rows"][0].get("warnings")))
# comparison tasks: two topics chosen -> some questions compare them ("also topics" column)
ct = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "docs", "task-drafts", "contrast-1.csv"), encoding="utf-8-sig").read()
teacher.api("teacher/items-import", {"csv": ct, "confirm": True})
cids = [r[0] for r in db.execute("select item_id from custom_items where data like '%\"also\"%'")]
teacher.api("teacher/items-status", {"ids": cids, "status": "approved"})
seen_c = 0
for _ in range(3):
    ss = student.api("session/start", {"mode": "practice", "skills": ["past_simple", "past_continuous"], "levels": ["A2", "B1"], "length": 9})
    sid3, cur = ss["session"]["id"], ss["item"]
    while cur:
        seen_c += cur["id"] in cids
        rr = student.api("session/answer", {"session_id": sid3, "item_id": cur["id"], "answer": "x", "time_ms": 1000})
        if rr["done"]: break
        cur = rr["next"]
check("comparison tasks are served when both topics are chosen", len(cids) == 15 and seen_c >= 3, (len(cids), seen_c))
print("\nALL PASS" if ok else "\nSOME FAILED"); raise SystemExit(0 if ok else 1)
