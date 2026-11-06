#!/usr/bin/env python3
"""My learning path, teacher 6 November: the recommended training is every other time a review of the steps learnt before the current one
(gaps and open mistakes first), and a step session asks only the step's own topic, from Recognise to Understand to Apply.
Run against the dev server (SQLite):  php -S 127.0.0.1:8099 -t app ;  rm -f app/var/ef.sqlite* ;  python3 app/tests/path_review_test.py"""
import os, sys
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "comeback_test.py")).read()
exec(compile(src.split("def run(")[0], "helpers", "exec"), globals())


def run_session(c, s, decide):
    sid, item, seen = s["session"]["id"], s["item"], []
    while item:
        it = ITEMS[item["id"]]; seen.append((it, item))
        a = c.api("session/answer", {"session_id": sid, "item_id": it["id"], "answer": correct(it) if decide(it) else wrong(it), "time_ms": 3000})
        if a["done"]: break
        item = a["next"]
    return seen


c = login(7301, "Ruta Path")
c.api("account/profile", {"self_level": "B1"})
path = c.api("path")
check("with a level given and no test, the path starts at that level", path["placed"] == "B1" and path["placed_by"] == "self", (path["placed"], path.get("placed_by")))
cur = [s for s in path["steps"] if s["id"] == path["current"]][0]
# a few mistakes on an earlier A2 topic
s = c.api("session/start", {"mode": "practice", "skills": ["present_simple"], "level": "A2.1", "length": 4, "source": "practice_page"})
run_session(c, s, lambda it: False)
# the first recommended training: the step itself (nothing before it in the path's recommended trainings)
s = c.api("session/start", {"mode": "practice", "skills": cur["topics"], "levels": cur["levels"], "length": 10, "source": "path", "recommended": True})
seen = run_session(c, s, lambda it: True)
check("first recommended training: the step itself, only its topics", all(it["skill"] in cur["topics"] for it, _ in seen), [it["skill"] for it, _ in seen])
blooms = [min(3, it["bloom"]) for it, _ in seen]
check("from Recognise to Apply: the first tasks are not harder than the last", sum(blooms[:3]) <= sum(blooms[-3:]), blooms)
check("no review label in a step session", all(pub.get("practice_context") != "review" for _, pub in seen))
# the next recommended training: a review of what came before, with the open mistakes
s = c.api("session/start", {"mode": "practice", "skills": cur["topics"], "levels": cur["levels"], "length": 10, "source": "path", "recommended": True})
check("second recommended training: a review", s["item"].get("practice_context") == "review", s["item"].get("practice_context"))
seen = run_session(c, s, lambda it: True)
check("the review asks earlier steps (lower levels), the topic with mistakes among them", "present_simple" in {it["skill"] for it, _ in seen} and not any(it["skill"] in cur["topics"] and it["level"] in cur["levels"] for it, _ in seen), [(it["skill"], it["level"]) for it, _ in seen])
# then the step again
s = c.api("session/start", {"mode": "practice", "skills": cur["topics"], "levels": cur["levels"], "length": 10, "source": "path", "recommended": True})
check("third recommended training: the step again", s["item"].get("practice_context") != "review" and ITEMS[s["item"]["id"]]["skill"] in cur["topics"])
c.api("session/quit", {"session_id": s["session"]["id"]})
# a step chosen on purpose is never turned into a review
s = c.api("session/start", {"mode": "practice", "skills": cur["topics"], "levels": cur["levels"], "length": 10, "source": "path"})
check("a step chosen by the learner stays that step", ITEMS[s["item"]["id"]]["skill"] in cur["topics"])
c.api("session/quit", {"session_id": s["session"]["id"]})
# nothing learnt before: no review
d = login(7302, "Dina New")
s = d.api("session/start", {"mode": "practice", "skills": ["present_simple"], "levels": ["A2.1"], "length": 3, "source": "path", "recommended": True})
run_session(d, s, lambda it: True)
s = d.api("session/start", {"mode": "practice", "skills": ["present_simple"], "levels": ["A2.1"], "length": 3, "source": "path", "recommended": True})
check("nothing learnt before the current step: the step again, not a review", s["item"].get("practice_context") != "review")
print("\nALL PASS" if ok else "\nSOME FAILED")
raise SystemExit(0 if ok else 1)
