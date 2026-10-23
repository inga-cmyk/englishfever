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

import glob, subprocess
APP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
ok = True
def check(n, c, x=""):
    global ok; ok &= bool(c); print(("PASS " if c else "FAIL ") + n + ("  -> " + str(x)[:600] if not c else ""))

teacher = login(9400, "Drafts Teacher", True)
files = sorted(glob.glob(os.path.join(APP, "..", "docs", "task-drafts", "*.csv")))
total = 0
for f in files:
    csvtext = open(f, encoding="utf-8-sig").read()
    res = teacher.api("teacher/items-import", {"csv": csvtext})
    check(os.path.basename(f) + ": every row passes the importer", res["bad"] == 0 and res["ok"] > 0, [(x["line"], x["errors"]) for x in res["rows"] if not x["ok"]][:6])
    warn = [(x["line"], x["warnings"]) for x in res["rows"] if x["warnings"]]
    check(os.path.basename(f) + ": no warnings (stand-out answer, instruction words)", not warn, warn[:6])
    imp = teacher.api("teacher/items-import", {"csv": csvtext, "confirm": True})
    total += imp["ok"]
drafts = [x["id"] for x in teacher.api("teacher/items")["items"]["draft"]]
teacher.api("teacher/items-status", {"ids": drafts, "status": "approved"})
check("all drafts approved for grading (%d)" % total, len(drafts) == total, (len(drafts), total))
r = subprocess.run(["php", os.path.join(APP, "tests", "grade_custom.php")], capture_output=True, text=True)
check("every listed answer is graded as expected", r.returncode == 0, r.stdout[-900:])
print(r.stdout.strip().splitlines()[-1])
learner = login(9401, "Drafts Learner")
m = learner.api("meta")
for sid, area in (("comparison", "Comparing things"), ("modal_verbs", "Modal verbs")):
    sk = [x for x in m["skills"] if x["id"] == sid]
    check(sid + ": topic is visible with its rule card (English and Latvian)", len(sk) == 1 and sk[0]["rule"]["form"] and sk[0]["rule_lv"]["form"], sk[:1])
    check(sid + ": its area is listed", area in [a["label"] for a in m["areas"]])
    st = learner.api("session/start", {"mode": "practice", "skills": [sid], "level": "A2.1", "length": 5})
    check(sid + ": a learner can practise it", st["_status"] == 200 and st["item"]["skill"] == sid, st)
# ---- every practice session has a similar mix of question types: about 3 choose, 4 drag (order / matching / word bank), 2 type a word, 1 type the whole sentence in ten
def group(it):
    return {"mcq": "choose", "order": "drag", "match": "drag", "text": "sentence"}.get(it["kind"]) or ("drag" if it.get("bank") else ("word" if it["kind"] == "gap" else "write"))
mixes = []
for k in range(4):
    mix_learner = login(9500 + k, "Mix Learner %d" % k)
    st = mix_learner.api("session/start", {"mode": "practice", "skills": ["present_simple", "past_simple"], "level": "A2.2", "length": 10})
    sid, item, groups = st["session"]["id"], st["item"], []
    while item:
        groups.append(group(item))
        a = mix_learner.api("session/answer", {"session_id": sid, "item_id": item["id"], "answer": "zzz" if item["kind"] in ("text", "write") else ([] if item["kind"] in ("order", "match") else (["zzz"] if item["kind"] == "gap" else item["options"][0])), "time_ms": 2000})
        item = a.get("next")
    mixes.append(groups)
sent = [g.count("sentence") for g in mixes]; word = [g.count("word") for g in mixes]; drag = [g.count("drag") for g in mixes]; choose = [g.count("choose") for g in mixes]
check("at most 2 whole-sentence typed questions in 10 (per session: %s)" % sent, max(sent) <= 2, sent)
check("at most 3 type-a-word questions in 10 (per session: %s)" % word, max(word) <= 3, word)
check("at least 2 drag-and-drop questions in 10 even when every answer is wrong (per session: %s); similar questions are asked again after a miss" % drag, min(drag) >= 2, drag)
check("2 to 5 multiple-choice questions in 10 (per session: %s)" % choose, 2 <= min(choose) and max(choose) <= 5, choose)
check("open writing does not appear in these sessions", all("write" not in g for g in mixes), mixes)

# ---- levels first: whole levels, with or without topics
def run_levels(levels, skills, n=10):
    lr = login(9600 + abs(hash(str(levels) + str(skills))) % 300, "Level Learner")
    st = lr.api("session/start", {"mode": "practice", "skills": skills, "levels": levels, "length": n})
    if st["_status"] != 200: return st, []
    sid, item, seen = st["session"]["id"], st["item"], []
    while item:
        full = [i for i in ITEMS if i["id"] == item["id"]]
        seen.append(item)
        a = lr.api("session/answer", {"session_id": sid, "item_id": item["id"], "answer": "zzz" if item["kind"] in ("text", "write") else ([] if item["kind"] in ("order", "match") else (["zzz"] if item["kind"] == "gap" else item["options"][0])), "time_ms": 2000})
        item = a.get("next")
    return st, seen
import json as _json
ITEMS = _json.load(open(os.path.join(APP, "content", "items.json"), encoding="utf-8"))
ITEMS = ITEMS if isinstance(ITEMS, list) else ITEMS["items"]
LEVEL_OF = {i["id"]: i["level"] for i in ITEMS}
ms = learner.api("meta")
check("meta lists the full levels and how many questions each has", ms["full_levels"] == ["A1", "A2", "B1", "B2", "C1", "C2"] and ms["level_counts"]["A2"] > 100 and ms["level_counts"]["A1"] == 0 and ms["level_counts"]["C2"] == 0, ms.get("level_counts"))
st, seen = run_levels(["A2"], ["present_simple"])
check("A2 only: every question is A2", seen and all(LEVEL_OF.get(i["id"], "A2.9").startswith("A2") or i["id"].startswith("c-") for i in seen), [i["id"] for i in seen])
st, seen = run_levels(["B1"], [])
check("B1 with no topic: a mix of several topics", len({i["skill"] for i in seen}) >= 4, len({i["skill"] for i in seen}))
check("A1 has no questions yet: said plainly", run_levels(["A1"], [])[0]["_status"] == 404)

print("\nALL PASS" if ok else "\nSOME FAILED"); raise SystemExit(0 if ok else 1)
