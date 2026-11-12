#!/usr/bin/env python3
"""Placement test: the level staircase (blocks of 3, retry block, ceiling), gaps, ladder, the lengths, a lot of simulated learners.
Run against the dev server (SQLite):  php -S 127.0.0.1:8099 -t app ;  rm -f app/var/ef.sqlite* ;  python3 app/tests/placement_test.py"""
import os, sys
sys.argv = [sys.argv[0]]
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "comeback_test.py")).read()
head = src.split("def run(")[0]   # shared helpers (client, login, check, correct, wrong)
exec(compile(head, "helpers", "exec"), globals())
FULL = lambda it: it["level"][:2]


def play(c, size, decide):
    """decide(item, n) -> True (answer right) / False. Returns the list of items served and the final summary."""
    s = c.api("session/start", {"mode": "placement", "length": size}); sid, item, seen = s["session"]["id"], s["item"], []
    while item:
        it = ITEMS[item["id"]]; seen.append(it)
        ok = decide(it, len(seen))
        a = c.api("session/answer", {"session_id": sid, "item_id": it["id"], "answer": correct(it) if ok else wrong(it), "time_ms": 3000})
        if "done" not in a: print("ERR", a, it["id"]); raise SystemExit(1)
        if a["done"]: return seen, a["summary"]
        item = a["next"]
    return seen, None


# a learner who knows everything climbs the ladder: A2, B1, B2, C1, three questions each, three different topics in a block
c = login(7001, "Aija Strong")
seen, s = play(c, 12, lambda it, n: True)
check("strong learner: 12 questions", len(seen) == 12, len(seen))
check("climbs A2 -> B1 -> B2, 3 questions per level, then more at B2 (the top since 12 November)", [FULL(i) for i in seen] == ["A2"] * 3 + ["B1"] * 3 + ["B2"] * 6, [FULL(i) for i in seen])
check("a block uses different topics", all(len({i["skill"] for i in seen[k:k + 3]}) == 3 for k in (0, 3, 6, 9)), [i["skill"] for i in seen])
check("strong learner is placed at B2 or C1", s["overall_level"][:2] in ("B2", "C1"), s["overall_level"])
check("summary has the level ladder", [l["level"] for l in s["ladder"]] == ["A2", "B1", "B2"] and all(l["correct"] == l["n"] for l in s["ladder"]), s["ladder"])   # no C1 since 12 November
check("no gaps when nothing was missed", s["gaps"] == [], s["gaps"])
check("a strong learner gets no basics message", s["basics"] is False, s.get("basics"))
check("confidence is reported", s["sure"] in ("rough", "good", "high"), s["sure"])

# a learner who misses everything: a second block at the same level, then fine-tuning
c = login(7002, "Baiba Weak")
seen, s = play(c, 24, lambda it, n: False)
check("weak learner: 24 questions", len(seen) == 24, len(seen))
check("after a failed block there is another block at the same level (6 at A2)", [FULL(i) for i in seen[:6]] == ["A2"] * 6, [FULL(i) for i in seen[:6]])
check("weak learner is placed at A2.1", s["overall_level"] == "A2.1", s["overall_level"])
check("ceiling reached: no climbing above B1 for someone who misses all", all(FULL(i) in ("A2", "B1") for i in seen[6:]), [FULL(i) for i in seen])
check("gaps are found, at most 3, with a level", 1 <= len(s["gaps"]) <= 3 and all(g["level"] in ("A2", "B1") for g in s["gaps"]), s["gaps"])
check("failing the first level twice gives the A2 basics message", s["basics"] is True, s.get("basics"))
check("level-test mistakes wait until their topic is practised (teacher, 12 November, A)", s["open_after"] == 0 and s.get("parked", 0) > 0, (s.get("open_after"), s.get("parked")))

# 2 of 3 right moves up; 1 of 3 gives a second block whose misses come back as the same topics
c = login(7003, "Cilda Mixed")
def second(it, n): return n in (1, 2, 4)          # A2: 2/3 up; B1: 1/3 -> second block
seen, s = play(c, 24, second)
check("2 of 3 right goes up to B1", [FULL(i) for i in seen[:3]] == ["A2"] * 3 and FULL(seen[3]) == "B1", [FULL(i) for i in seen[:5]])
check("1 of 3 right stays at B1 for another block", [FULL(i) for i in seen[3:9]] == ["B1"] * 6, [FULL(i) for i in seen[3:9]])
missed = {i["skill"] for i in seen[5:6] + seen[3:4] if True}
check("the second block re-checks a topic missed in the first", len({i["skill"] for i in seen[3:6]} & {i["skill"] for i in seen[6:9]}) >= 1, [i["skill"] for i in seen[3:9]])

# the learner's own level (teacher, 6 November): the test starts there and goes down when it is too hard
c = login(7150, "Dace Says B2"); c.api("account/profile", {"self_level": "B2"})
seen, s = play(c, 24, lambda it, n: FULL(it) == "A2")
check("says B2: the test starts at B2", FULL(seen[0]) == "B2", [FULL(i) for i in seen])
check("misses B2 and B1: it comes down to A2", [FULL(i) for i in seen].index("A2") > [FULL(i) for i in seen].index("B1") > 0, [FULL(i) for i in seen])
check("placed at A2, not above", s["overall_level"][:2] == "A2", s["overall_level"])
c = login(7151, "Edgars Says B1"); c.api("account/profile", {"self_level": "B1"})
seen, s = play(c, 12, lambda it, n: True)
check("says B1 and knows everything: starts at B1 and climbs", FULL(seen[0]) == "B1" and "A2" not in [FULL(i) for i in seen] and s["overall_level"][:2] in ("B2", "C1"), ([FULL(i) for i in seen], s["overall_level"]))
c = login(7152, "Gints Unknown"); c.api("account/profile", {"self_level": "unknown"})
seen, s = play(c, 12, lambda it, n: True)
check("\"I don't know\": starts at A2", FULL(seen[0]) == "A2")
check("typed forms first where a topic has them", sum(1 for i in seen if i["kind"] == "gap" and not i.get("bank")) >= len(seen) // 3, [i["kind"] for i in seen])

# no repeats inside one test, the three lengths
for size in (12, 24, 40):
    c = login(7010 + size, f"Length {size}")
    seen, s = play(c, size, lambda it, n: n % 3 != 0)
    check(f"{size}-question test has {size} different questions", len(seen) == size and len({i["id"] for i in seen}) == size, len(seen))

# all topics are shown, practise levels come from the ladder, and the report can be read again from the dashboard
d = c.api("dashboard")
check("the report is kept for the dashboard", d["placement"] and d["placement"]["report"]["ladder"], d.get("placement"))
print("ALL PASS" if ok else "SOME FAILED")
sys.exit(0 if ok else 1)
