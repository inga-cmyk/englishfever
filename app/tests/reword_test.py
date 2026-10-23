#!/usr/bin/env python3
"""Importing a corrected CSV again: unchanged rows are left alone, a task with the same content and new wording is updated where it is
(same id, same status, learners' answers stay with it), real duplicates and built-in duplicates are still refused.
Run against the dev server (SQLite):  php -S 127.0.0.1:8099 -t app ;  rm -f app/var/ef.sqlite* ;  python3 app/tests/reword_test.py"""
import os, sys
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "comeback_test.py")).read()
exec(compile(src.split("def run(")[0], "helpers", "exec"), globals())
HEAD = "topic,level,type,task,correct answer,wrong options / checks,explanation shown to learner,explanation in Latvian,thinking level\n"
def row(task, correct, wrong, lv="A2.1"): return f'Comparison,{lv},mcq,"{task}",{correct},{wrong},*Good* is irregular.,*Good* ir neregulārs.,2\n'
OLD = HEAD + row("At home: which sentence is NOT correct?", "She is more tall than her brother.", "She is taller than her brother. | He is the youngest. | This bag is lighter.") \
    + row("On the news: which sentence is NOT correct?", "It is the more cold day of the year.", "It is the coldest day of the year. | It is colder than yesterday. | It is very cold.") \
    + row("Choose the correct word: This film is ___ than the book.", "better", "gooder | more good | best")
NEW = HEAD + row("Which sentence is NOT correct?", "She is more tall than her brother.", "She is taller than her brother. | He is the youngest. | This bag is lighter.") \
    + row("Which sentence is NOT correct?", "It is the more cold day of the year.", "It is the coldest day of the year. | It is colder than yesterday. | It is very cold.") \
    + row("Choose the correct word: This film is ___ than the book.", "better", "gooder | more good | best")

t = login(9601, "Reword Teacher", True)
r = t.api("teacher/items-import", {"csv": OLD})
check("the first file: 3 new", r["ok"] == 3 and r["bad"] == 0 and r.get("updated", 0) == 0, r)
r = t.api("teacher/items-import", {"csv": OLD, "confirm": True}); check("saved as drafts", r["ok"] == 3)
items = t.api("teacher/items")["items"]
ids = [x["id"] for x in items["draft"]]
t.api("teacher/items-status", {"ids": ids[:2], "status": "approved"})      # two approved, one still a draft
before = {x["id"]: x["q"] for k in ("draft", "approved") for x in t.api("teacher/items")["items"][k]}

# the same file again: nothing is added, nothing is a problem
r = t.api("teacher/items-import", {"csv": OLD})
check("the same file again: all 3 already there, none new, no problems", r["ok"] == 0 and r["bad"] == 0 and r["same"] == 3, r)

# the corrected file: 2 reworded in place, 1 already there
r = t.api("teacher/items-import", {"csv": NEW})
check("the corrected file: 2 reworded, 1 already there, none new, no problems", r["updated"] == 2 and r["same"] == 1 and r["ok"] == 0 and r["bad"] == 0, r)
r = t.api("teacher/items-import", {"csv": NEW, "confirm": True})
now = {x["id"]: x for k in ("draft", "approved") for x in t.api("teacher/items")["items"][k]}
check("same ids, nothing added", set(now) == set(before), (set(now), set(before)))
check("the wording changed in place", sorted(x["q"] for x in now.values()) == sorted(["Which sentence is NOT correct?", "Which sentence is NOT correct?", "Choose the correct word: This film is ___ than the book."]), [x["q"] for x in now.values()])
check("approved stays approved, draft stays draft", len([x for x in t.api("teacher/items")["items"]["approved"]]) == 2 and len(t.api("teacher/items")["items"]["draft"]) == 1)
# two tasks may share a plain instruction when their content differs, but the same content twice is a duplicate
r = t.api("teacher/items-import", {"csv": HEAD + row("Which sentence is NOT correct?", "They is happy.", "They are happy. | We are happy. | I am happy.") + row("Which sentence is NOT correct?", "They is happy.", "They are happy. | We are happy. | I am happy.")})
check("a new task with the plain instruction is fine, the same twice is refused", r["ok"] == 1 and r["bad"] == 1, r)
# a corrected matching task retires the older, ambiguous version
HEADR = HEAD.strip() + ",replaces\n"
def mrow(pairs, repl=""):
    return 'Comparison,B1.1,match,"Match each sentence with its meaning.","%s",,Explanation.,Skaidrojums.,3,"%s"\n' % (pairs, repl)
OLDM = "The new phone is much = faster than the old one. ; The new phone is a bit = heavier than the old one. ; The new phone is not as = cheap as the old one. ; The new phone is the = best one in the shop."
NEWM = "The new phone is much faster. = a big difference ; The new phone is a bit faster. = a small difference ; The new phone is not as fast. = the old one is faster ; The new phone is the fastest. = no other phone is faster"
t.api("teacher/items-import", {"csv": HEADR + mrow(OLDM), "confirm": True})
st0 = {x["id"]: x["q"] for k in ("draft", "approved") for x in t.api("teacher/items")["items"][k]}
r = t.api("teacher/items-import", {"csv": HEADR + mrow(NEWM, OLDM)})
check("the corrected matching task says it replaces the older one", r["ok"] == 1 and any("Replaces an older" in w for x in r["rows"] for w in x["warnings"]), r)
r = t.api("teacher/items-import", {"csv": HEADR + mrow(NEWM, OLDM), "confirm": True})
lst = t.api("teacher/items")["items"]
active = [x for k in ("draft", "approved") for x in lst[k]]
check("afterwards the old ambiguous version is retired and only the new one is active", len(lst["retired"]) >= 1 and sum(1 for x in active if "much faster" in json.dumps(x)) == 1 and not any("heavier than the old one" in json.dumps(x) for x in active), (len(lst["retired"]), len(active)))
print("ALL PASS" if ok else "SOME FAILED"); sys.exit(0 if ok else 1)
