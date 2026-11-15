"""Batch 4, B1.2 part (teacher, 14 November): 25 tasks for each of the six B1.2 grammar points that had no task
(docs/GRAMMAR-MAP-GAPS.md 3.1): pc_always (Present continuous B1.2), would_habit, should_have (More modals),
each_every (Subject and verb B1.2), rel_what, wont_refuse (teacher, 15 November: the two new levels are prepared tasks only). One module per point (gp4_<point>.py, with its notes file); written by separate writers, then
checked blind (docs/BLIND-CHECK.md)."""
import re
import lib

NAME = "gap-points-b12-1.csv"
POINTS = ["pc_always", "would_habit", "should_have", "each_every", "rel_what", "wont_refuse"]

# Word-order questions keep "to make a question" (the gate wants it; plain() would shorten it). This file only.
_plain = lib.plain
lib.plain = lambda task, typ: task.strip() if typ == "order" and task.strip() == "Put the words in order to make a question." else _plain(task, typ)

POINT_OF = []   # (first row, point) for the map
for p in POINTS:
    POINT_OF.append((len(lib.rows), p))
    __import__("gp4_" + p)

# A word order that says "to make a question" accepts only questions: od() adds the statement for a bare "Put the words in order."
_AUXQ = re.compile(r"^(is|are|am|was|were|do|does|did|can|could|will|would|shall|should|may|might|must|have|has|had|what|where|when|why|who|whom|how|which|whose)\b")
for r in lib.rows:
    if r[2] == "order" and r[3].strip() == "Put the words in order to make a question." and r[5].startswith("also accepted: "):
        keep = [a for a in r[5][len("also accepted: "):].split(" | ") if (_AUXQ.match(a) or re.search(r"\b(will|would|can|could|should|must|shall|is|are|am|was|were|have|has|do|does|did) (i|you|we|they|he|she|it|the|my|your|our|his|her|their)\b", a)) and not (re.search(r"\b(i|you|we|they|he|she|it) (will|would|can|could|should|must|shall|is|are|am|was|were|have|has)\b", a) and not re.search(r"\b(will|would|can|could|should|must|shall|is|are|am|was|were|have|has|do|does|did) (i|you|we|they|he|she|it)\b", a))]
        r[5] = ("also accepted: " + " | ".join(keep)) if keep else ""

if __name__ == "__main__":
    import sys
    lib.save(sys.argv[1] if len(sys.argv) > 1 else "pending/" + NAME)
