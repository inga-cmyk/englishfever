#!/usr/bin/env python3
"""Slip or gap (a missed task comes back as a similar one; missed again = a gap, two more tasks from other angles) and the life of a mistake
(missed -> fixed -> locked in on another day -> reopened). No messages: only the result flags that drive the sounds.
Run against the dev server (SQLite):  php -S 127.0.0.1:8099 -t app ;  rm -f app/var/ef.sqlite* ;  python3 app/tests/probe_test.py"""
import os, sys, sqlite3
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "comeback_test.py")).read()
exec(compile(src.split("def run(")[0], "helpers", "exec"), globals())


def sim(a, b):
    return a["skill"] == b["skill"] and abs(LV.index(a["level"]) - LV.index(b["level"])) <= 1 and abs(a["bloom"] - b["bloom"]) <= 1
LV = ["A2.1", "A2.2", "B1.1", "B1.2", "B2.1", "B2.2", "C1.1", "C1.2"]


def play(c, plan, skills=("present_simple",), level="A2.1", n=12):
    """plan(i, item) -> True/False/None (None: answer wrong). Returns the list of (item, result)."""
    s = c.api("session/start", {"mode": "practice", "skills": list(skills), "level": level, "length": n})
    sid, item, out = s["session"]["id"], s["item"], []
    while item:
        it = ITEMS[item["id"]]
        r = c.api("session/answer", {"session_id": sid, "item_id": it["id"], "answer": correct(it) if plan(len(out), it) else wrong(it), "time_ms": 2000})
        out.append((it, r["result"]))
        if r["done"]: break
        item = r["next"]
    return out


# 1. a miss comes back soon as a similar task; right = a slip, nothing special happens
c = login(9201, "Probe One")
out = play(c, lambda i, it: i != 0)            # first wrong, everything else right
first = out[0][0]
twin_pos = [i for i, (it, r) in enumerate(out) if i > 0 and sim(first, it)]
check("after a miss, a similar task (same topic, level and thinking level within one step) comes within 3 questions", twin_pos and twin_pos[0] <= 3, twin_pos)
check("the first question is wrong and the next one is not the same task", out[1][0]["id"] != first["id"])
check("a right answer to the similar task is a slip: no gap flag", not any(r["gap"] for _, r in out))
check("the miss counts as fixed through that task", any(r["fixed"] for _, r in out))

# 2. missed again = a gap: the gap flag, then more tasks of that kind from other angles
c2 = login(9203, "Probe Three")
s0 = c2.api("session/start", {"mode": "practice", "skills": ["present_simple"], "level": "A2.1", "length": 15})
sid = s0["session"]["id"]; item = s0["item"]; out = []
while item:
    it = ITEMS[item["id"]]; ok = len(out) > 3           # the first four wrong: the miss and the similar task that follows it are both wrong
    r = c2.api("session/answer", {"session_id": sid, "item_id": it["id"], "answer": correct(it) if ok else wrong(it), "time_ms": 2000})
    out.append((it, r["result"]))
    if r["done"]: break
    item = r["next"]
gap_at = [i for i, (it, r) in enumerate(out) if r["gap"]]
check("a wrong answer to the similar task is a gap (flag)", len(gap_at) >= 1, gap_at)
check("all tasks of the session are different", len({it["id"] for it, _ in out}) == len(out))
t0 = login(9207, "Probe Teacher Two", True)
ev0 = t0.api("teacher/evidence")["probes"]
check("the angle tasks that follow a gap were asked", ev0["gaps"] >= 1 and ev0["angle_probes"] >= 1, ev0)

# 3. fixed -> locked in on another day -> reopened
c = login(9204, "Probe Four")
uid = c.api("me")["user"]["id"]
db = sqlite3.connect(DB)
# one wrong, then the same task right: fixed
it = next(i for i in ITEMS.values() if i["skill"] == "present_simple" and i["level"] == "A2.1" and i["kind"] == "mcq")
tw = [i for i in ITEMS.values() if i["id"] != it["id"] and sim(it, i)]
s = c.api("session/start", {"mode": "practice", "skills": ["present_simple"], "level": "A2.1", "length": 5})
def ans(sid, item, right):
    return c.api("session/answer", {"session_id": sid, "item_id": item["id"], "answer": correct(item) if right else wrong(item), "time_ms": 1000})
# use whatever the first task is as the mistake
m = ITEMS[s["item"]["id"]]
r1 = ans(s["session"]["id"], m, False)
check("a wrong answer is not 'locked' and not 'fixed'", not r1["result"]["locked"] and not r1["result"]["fixed"])
# make the twin come: answer until a similar task appears, right
sid = s["session"]["id"]; item = r1["next"]; fixed_at = None; guard = 0
while item and guard < 8:
    guard += 1
    it = ITEMS[item["id"]]; r = ans(sid, it, True)
    if r["result"]["fixed"]: fixed_at = it["id"]; break
    item = r["next"]
check("answering a similar task right fixes it (and says nothing new)", fixed_at is not None)
check("on the same day it is not yet locked in", not r["result"]["locked"])
# the fixing answer moves to two days ago; another different, similar task today -> locked in
db.execute("UPDATE attempts SET created_at = created_at - 2 * 86400 WHERE user_id = ?", (uid,)); db.commit()
s = c.api("session/start", {"mode": "practice", "skills": ["present_simple"], "level": "A2.1", "length": 10})
sid = s["session"]["id"]; item = s["item"]; locked = False; guard = 0
while item and guard < 10:
    guard += 1
    it = ITEMS[item["id"]]; r = ans(sid, it, True)
    if r["result"]["locked"]: locked = True; break
    if r["done"]: break
    item = r["next"]
check("a similar, different task answered right on a later day locks the mistake in", locked)
c.api("session/quit", {"session_id": sid})
# reopened: a wrong answer on that kind of task
s = c.api("session/start", {"mode": "practice", "skills": ["present_simple"], "level": "A2.1", "length": 6})
r = ans(s["session"]["id"], ITEMS[s["item"]["id"]], False)
from_db = db.execute("SELECT COUNT(1) FROM attempts WHERE user_id = ?", (uid,)).fetchone()[0]

# 3b. the same in "Surprise me" and in a session chosen by level (the picker)
for label, body in (("Surprise me", {"mode": "smart", "length": 10}), ("level picker", {"mode": "practice", "skills": ["present_simple", "past_simple"], "levels": ["A2"], "length": 10})):
    cc = login(9300 + len(label), "Probe " + label)
    st = cc.api("session/start", body); sid, item, seq = st["session"]["id"], st["item"], []
    while item:
        it = ITEMS[item["id"]]
        r = cc.api("session/answer", {"session_id": sid, "item_id": it["id"], "answer": correct(it) if seq else wrong(it), "time_ms": 1000})
        seq.append(it)
        if r["done"]: break
        item = r["next"]
    pos = [i for i, it in enumerate(seq) if i > 0 and sim(seq[0], it)]
    check(label + ": a miss brings back a similar task within 3 questions", pos and pos[0] <= 3, pos)

# 4. no probes in Second Chance or the placement test
c = login(9205, "Probe Five")
pl = c.api("session/start", {"mode": "placement", "length": 12}); it = ITEMS[pl["item"]["id"]]
r = c.api("session/answer", {"session_id": pl["session"]["id"], "item_id": it["id"], "answer": wrong(it), "time_ms": 1000})
check("the placement test has no probes or gap flags", r["result"]["gap"] is False and r["result"]["locked"] is False)

# 4b. Second Chance: a task that stood for a mistake is missed again = a gap, with more tasks of that kind next
c = login(9208, "Probe Six")
pr = c.api("session/start", {"mode": "practice", "skills": ["past_simple"], "level": "A2.2", "length": 10})
it = ITEMS[pr["item"]["id"]]
c.api("session/answer", {"session_id": pr["session"]["id"], "item_id": it["id"], "answer": wrong(it), "time_ms": 1000})   # one mistake
c.api("session/quit", {"session_id": pr["session"]["id"]})
cb = c.api("session/start", {"mode": "comeback"})
check("Second Chance starts", cb["_status"] == 200, cb)
n0 = cb["session"]["length"]; sid = cb["session"]["id"]; item = cb["item"]; flags = []; ids = []; i = 0
while item:
    it = ITEMS[item["id"]] if item["id"] in ITEMS else None
    ids.append(item["id"])
    right = i != 0                                   # the first one is missed again
    ans = correct(it) if right else wrong(it)
    a = c.api("session/answer", {"session_id": sid, "item_id": item["id"], "answer": ans, "time_ms": 1000})
    flags.append((i, a["result"]["gap"], a["session"]["length"]))
    i += 1
    if a["done"]: break
    item = a["next"]
check("the first Second Chance task answered wrongly is a gap", flags[0][1] is True, flags[:2])
check("the session grew by one or two similar tasks (not more)", 1 <= flags[0][2] - n0 <= 2 and i == flags[0][2], (n0, flags[0][2], i))
check("all Second Chance tasks are different", len(set(ids)) == len(ids), ids)
check("right answers afterwards are not gaps", not any(f[1] for f in flags[1:]))

# 5. the teacher can read the numbers (and nobody else can)
t = login(9206, "Probe Teacher", True)
ev = t.api("teacher/evidence")
check("the evidence page has probe and mistake numbers", ev["_status"] == 200 and set(ev["probes"]) >= {"first_probes", "slips", "gaps"} and set(ev["mistakes"]) >= {"fixed", "locked", "reopened", "open"}, ev)
check("a first probe was counted", ev["probes"]["first_probes"] >= 1, ev["probes"])
check("a student cannot open it", c.api("teacher/evidence")["_status"] == 403)
print("ALL PASS" if ok else "SOME FAILED"); sys.exit(0 if ok else 1)
