#!/usr/bin/env python3
"""Word-order tasks accept every correct order (docs/task-drafts/_src/alt_orders.py). Needs no server:  python3 app/tests/orders_test.py
A learner who writes "my boss is the man who called you" must not be marked wrong for "the man who called you is my boss"."""
import csv, glob, os, sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
sys.path.insert(0, os.path.join(ROOT, "docs", "task-drafts", "_src"))
import alt_orders as A
ok = True
def check(n, c, x=""):
    global ok; ok &= bool(c); print(("PASS " if c else "FAIL ") + n + ("  -> " + str(x)[:500] if not c else ""))
orders = {}
for f in sorted(glob.glob(os.path.join(ROOT, "docs", "task-drafts", "*.csv"))):
    for r in csv.DictReader(open(f, encoding="utf-8-sig")):
        if r["type"] == "order":
            also = [x.strip() for x in r["wrong options / checks"].replace("also accepted:", "").split("|") if x.strip()]
            orders[r["correct answer"]] = also
check("every entry of the table belongs to a word-order task (in one of its orders)", all(any(e in orders for e in g) for g in A.GROUPS), [g for g in A.GROUPS if not any(e in orders for e in g)])
check("every other order uses exactly the same words", all(sorted(a.split()) == sorted(k.split()) for k, v in orders.items() for a in v), [(k, a) for k, v in orders.items() for a in v if sorted(a.split()) != sorted(k.split())][:3])
check("the three reported orders are accepted",
      "my boss is the man who called you" in orders["the man who called you is my boss"]
      and "the police called the woman whose car was stolen" in orders["the woman whose car was stolen called the police"]
      and "she didn't use to enjoy cooking but she loves it now" in orders["she didn't use to enjoy cooking but now she loves it"])
check("an if-sentence is accepted in both orders", "it melts if you heat ice" in orders["if you heat ice it melts"] and "if they don't get water plants die" in orders["plants die if they don't get water"])
check("a closing time phrase may come first", "every day my sister walks to school" in orders["my sister walks to school every day"])
check("a question does not get a fronted time phrase", orders["did you see the match yesterday"] == [])
# typed "Join with when / while" tasks: either clause may follow the conjunction when the meaning stays (report: "when I was walking home, it started to rain")
texts = {}
for f in sorted(glob.glob(os.path.join(ROOT, "docs", "task-drafts", "*.csv"))):
    for r in csv.DictReader(open(f, encoding="utf-8-sig")):
        if r["type"] == "text": texts[r["task"]] = [x.strip().lower() for x in r["correct answer"].split("|")]
for task, want in (("Join with when: I was walking home. It started to rain.", "when I was walking home, it started to rain."), ("Join with when: I was cooking. The smoke alarm went off.", "when I was cooking, the smoke alarm went off."),
                   ("Join with while: I was cooking. My brother was setting the table.", "while my brother was setting the table, I was cooking.")):
    check("accepted: " + want, want.lower().rstrip(".") in [a.rstrip(".") for a in texts[task]], texts[task])
print("\nALL PASS" if ok else "\nSOME FAILED"); sys.exit(0 if ok else 1)
