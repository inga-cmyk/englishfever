"""Indirect questions B1.1 and B1.2 (teacher, 21 November): 24 new tasks from gp6_iq_b1.py (notes gp6_iq_b1-notes.md), written
after the tester's report that the old set was too easy and gave the answer away. Points: iq_yn when the answer has if / whether,
otherwise iq_wh. Blind-checked before packaging (docs/BLIND-CHECK.md)."""
import re
import lib

NAME = "iq-b1-6.csv"
import gp6_iq_b1  # noqa: F401  (adds its rows to lib.rows)
import gp6_iq_extra  # noqa: E402  question mark after a non-question (B1.2), if vs whether (B2.2): teacher, 21 November
import gp7_iq_b1  # noqa: E402  the learner rewrites the direct question himself (tester, 22 November)


def point_of(n):
    if n in gp6_iq_extra.POINT_OF: return gp6_iq_extra.POINT_OF[n]
    if n in gp7_iq_b1.POINT_OF: return gp7_iq_b1.POINT_OF[n]
    r = lib.rows[n]
    text = " ".join(str(x) for x in r[3:6]).lower()
    return "iq_yn" if re.search(r"\b(if|whether)\b", text) else "iq_wh"


if __name__ == "__main__":
    import sys
    lib.save(sys.argv[1] if len(sys.argv) > 1 else NAME)
