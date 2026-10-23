#!/usr/bin/env python3
"""Latvian wording in the question drafts and the new rule cards must follow docs/LATVIAN-TERMS.md.
Flags: terms the glossary replaced, 'priekšmets' without 'teikuma' / 'teik.', and English words that are not marked as examples with *...*."""
import csv, glob, os, re, sys
APP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.insert(0, os.path.join(APP, "authoring"))
sys.path.insert(0, os.path.join(APP, "..", "docs", "task-drafts", "_src"))
import lib  # noqa: F401  (extends the Latvian word list the same way the drafts were written)
BANNED = [r"\bpasīv", r"\baktīv", r"divdabi", r"jautājuma vārd", r"tagadnes ilgstoš", r"pagātnes ilgstoš", r"ilgstošā forma", r"salīdzināmā", r"vienkāršā tagadne", r"vienkāršā pagātne", r"vienkāršo tagadni", r"vienkāršo pagātni",
          r"(?<!teikuma )(?<!teik\. )\bpriekšmet"]
ALLOWED = {"Present", "Past", "Simple", "Continuous", "Perfect", "Future", "Passive", "Conditional", "Zero", "First", "Second", "Third"}
bad = []

def check(where, text):
    for pat in BANNED:
        if re.search(pat, text): bad.append((where, "term not in the glossary: /" + pat + "/", text[:110]))
    import italics
    if italics.lv_mark(text.replace("*", "")) != text: bad.append((where, "English words not marked as examples (run the drafts through lib.save)", text[:110]))

for f in sorted(glob.glob(os.path.join(APP, "..", "docs", "task-drafts", "*.csv"))):
    for n, r in enumerate(list(csv.reader(open(f, encoding="utf-8-sig")))[1:], 2):
        if len(r[6].strip()) < 12: bad.append((os.path.basename(f) + ":" + str(n), "English explanation too short", r[6]))
        if r[7].strip(): check(os.path.basename(f) + ":" + str(n), r[7])
        else: bad.append((os.path.basename(f) + ":" + str(n), "no Latvian explanation", r[3][:80]))
import lv_rules
for sid in ("modal_verbs", "comparison"):
    card = lv_rules.LV_RULES[sid]
    for k in ("form", "use"):
        for i, line in enumerate(card[k]):
            # cards are marked automatically by the build (every English word in a Latvian card is an example), so only the terms are checked
            for pat in BANNED:
                if re.search(pat, line): bad.append(("card " + sid + "." + k + str(i), "term not in the glossary: /" + pat + "/", line[:110]))
for b in bad[:60]: print("FAIL", *b)
print(len(bad), "problems")
sys.exit(1 if bad else 0)
