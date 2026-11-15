"""Batch 5, A2 part (teacher, 15 November): the 25 A2 grammar points with 1-9 counted tasks (docs/GRAMMAR-MAP-GAPS.md 3.2)
filled up to 10 each, 152 tasks. One module per point (gp5_<point>.py, with its notes file, brief briefs/writer-brief-5.md); written
by separate writers, then checked blind (docs/BLIND-CHECK.md). Levels as on the map (teacher, 15 November): Verb patterns,
Adjective order and Quantity get A2.1, Clauses A2.2, prepared tasks only."""
import re
import lib

NAME = "gap-fill-a2-1.csv"
POINTS = ["vp_like_ing", "plural_reg", "adj_basic", "ps_pc", "was_were", "a_few", "a_the", "prep_none", "count_unc",
          "pp_been_gone", "unc_nouns", "prep_move", "adv_degree", "cmp_adv", "could_past", "indef_form", "conj_parallel",
          "prep_transport", "purpose_to", "pas_by", "plural_only", "link_time", "will_going", "the_unique", "dep_none"]

# Word-order questions keep "to make a question" (the gate wants it; plain() would shorten it). This file only.
_plain = lib.plain
lib.plain = lambda task, typ: task.strip() if typ == "order" and task.strip() == "Put the words in order to make a question." else _plain(task, typ)

POINT_OF = []   # (first row, point) for the map
for p in POINTS:
    POINT_OF.append((len(lib.rows), p))
    __import__("gp5_" + p)


def point_of(n):
    """The grammar point of row n."""
    return [p for start, p in POINT_OF if start <= n][-1]


# A word order that says "to make a question" accepts only questions: od() adds the statement for a bare "Put the words in order."
_AUXQ = re.compile(r"^(is|are|am|was|were|do|does|did|can|could|will|would|shall|should|may|might|must|have|has|had|what|where|when|why|who|whom|how|which|whose)\b")
for r in lib.rows:
    if r[2] == "order" and r[3].strip() == "Put the words in order to make a question." and r[5].startswith("also accepted: "):
        keep = [a for a in r[5][len("also accepted: "):].split(" | ") if _AUXQ.match(a)]
        r[5] = ("also accepted: " + " | ".join(keep)) if keep else ""

# plural_only (blind check r13b): *Your pair of trousers looks…* is correct too; it gets its own note (the explanation says *not looks*)
for n, r in enumerate(lib.rows):
    if r[2] == "text" and r[3].startswith("Correct the mistake: Your trousers looks great"):
        lib.NOTES[n] = (lib.NOTES[n] + " || " if n in lib.NOTES else "") + "Your pair of trousers looks great with that jacket. :: Correct too: here the subject is *pair* (one pair), so the verb has *-s*. With *trousers* alone: *Your trousers look great*. :: Arī pareizi: te teikuma priekšmets ir *pair* (viens pāris), tāpēc darbības vārdam ir *-s*. Tikai ar *trousers*: *Your trousers look great*."

if __name__ == "__main__":
    import sys
    lib.save(sys.argv[1] if len(sys.argv) > 1 else NAME)   # blind-checked (r13, r13b)
