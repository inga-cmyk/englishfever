"""Batch 4, A2 part (teacher, 14 November): 25 tasks for each of the seven A2 grammar points that had a rule card and no task
(docs/GRAMMAR-MAP-GAPS.md 3.1): have_got, shall, art_zero (Articles A2.1, prepared tasks only), no_longer, requests,
vp_ing_subject, vp_go_ing. One module per point (gp4_<point>.py, with its notes file); written by separate writers, then
checked blind (docs/BLIND-CHECK.md)."""
import re
import lib, italics

NAME = "gap-points-a2-1.csv"
POINTS = ["have_got", "shall", "art_zero", "no_longer", "requests", "vp_ing_subject", "vp_go_ing"]

# Word-order questions keep "to make a question" (the gate wants it; plain() would shorten it). This file only.
_plain = lib.plain
lib.plain = lambda task, typ: task.strip() if typ == "order" and task.strip() == "Put the words in order to make a question." else _plain(task, typ)
# Latvian explanations: "no longer / no more" is English (Latvian "no" = from); a few Latvian words without diacritics stay plain.
italics.LV_ASCII.discard("no")
italics.AMBIGUOUS.add("no")
lib.LV_BY_FILE[NAME] = set("""tulkojot burtiski Tulkojot artikula artikulu valstu nosaukumiem nosaukumi noteikta noteikts noteiktiem visi veidiem
Sporta sporta instrumentiem Hobijs hobijs citam tikai pareizi ideju lieta atsakot""".split())

POINT_OF = []   # (first row, point) for the map
for p in POINTS:
    POINT_OF.append((len(lib.rows), p))
    __import__("gp4_" + p)

if __name__ == "__main__":
    import sys
    lib.save(sys.argv[1] if len(sys.argv) > 1 else "pending/" + NAME)
