"""Writes docs/task-drafts/b1-new-review.md: every new B1 question in readable form (run after b1_new_1/2/3.py)."""
import csv, collections, os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
out = ["# New B1 topics: all questions to read before importing", "", "Eight topics, three files: `b1-new-1.csv`, `b1-new-2.csv`, `b1-new-3.csv`. Each line is one question as the learner sees it. **✔** = the correct answer (or all accepted answers), **✗** = the wrong options. The text after the dash is the explanation shown after the answer (the Latvian version is in the CSV). Levels are the internal half-levels: learners see A2 and B1.", ""]
by = collections.OrderedDict()
for f in ("b1-new-1.csv", "b1-new-2.csv", "b1-new-3.csv"):
    for r in csv.DictReader(open(os.path.join(D, f), encoding="utf-8-sig")):
        by.setdefault(r["topic"], []).append(r)
kind = {"mcq": "choose", "gap": "type a word", "bank": "drag the word", "text": "type the sentence", "order": "drag the words", "match": "match"}
for topic, rows in by.items():
    out += [f"## {topic} ({len(rows)} questions)", ""]
    for lv in sorted({r["level"] for r in rows}):
        sub = [r for r in rows if r["level"] == lv]
        out += [f"### {lv} ({len(sub)})", ""]
        for r in sub:
            t, q, ans, w = r["type"], r["task"], r["correct answer"], r["wrong options / checks"]
            if t == "gap" and w.startswith("bank:"): t = "bank"
            if t == "mcq": body = f"✔ {ans}   ✗ {w}"
            elif t == "bank": body = f"✔ {ans}   (chips: {w[5:].strip()})"
            elif t == "order": body = f"✔ {ans}" + (f"   ({w})" if w else "")
            elif t == "match": body = "✔ " + ans.replace(" ; ", "  ·  ")
            else: body = f"✔ {ans}"
            out.append(f"- [{kind[t]}] **{q}**   {body}  — {r['explanation shown to learner'].replace('*', '')}")
        out.append("")
open(os.path.join(D, "b1-new-review.md"), "w", encoding="utf-8").write("\n".join(out))
print(len(out), "lines")
