#!/usr/bin/env python3
"""The writing rules for the question drafts (docs/ITEM-WRITING-RULES.md), checked on every file in docs/task-drafts.
Each check stops a mistake that was made before. Needs no server:  python3 app/tests/draft_rules_test.py"""
import csv, glob, os, re, sys, collections
APP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
bad = []
rows = []
# matching tasks that the "could the cards be swapped?" net flags but that were read and are unambiguous: the cards start or end alike, but each card's meaning decides
REVIEWED = ("If I had gone, I would have met her.", "Tom ate the pizza. (who?)", "The bridge is being repaired.", "When I arrived, she had left.", "The new phone is much faster.", "No entry", "If you don't eat,")
for f in sorted(glob.glob(os.path.join(APP, "..", "docs", "task-drafts", "*.csv"))):
    for n, r in enumerate(csv.DictReader(open(f, encoding="utf-8-sig")), 2):
        rows.append((os.path.basename(f), n, r))

def flag(f, n, why, text=""): bad.append(f"{f}:{n} {why}  {text[:90]}")

seen_content = collections.defaultdict(list)
for f, n, r in rows:
    t, q, ans, wrong = r["type"], r["task"], r["correct answer"], r["wrong options / checks"]
    # 1. plain instructions: no setting in front, no hint after a word-order instruction, no topic after a matching instruction
    if t == "mcq" and re.match(r"^[^:?.]{2,45}: which\b", q, re.I): flag(f, n, "a setting in front of the instruction", q)
    if t == "mcq" and re.search(r"\b(writes|says|asks|texts)\b[^.?]*: '.*' Choose the correct option\.$", q): flag(f, n, "'Your friend writes: ...' intro", q)
    if t == "order" and q != "Put the words in order.": flag(f, n, "a hint after the word-order instruction", q)
    if t == "match" and re.match(r"^Match each beginning with its ending[:.]", q) and q != "Match each beginning with its ending.": flag(f, n, "a topic after the matching instruction", q)
    # 2. matching: one sensible pairing. A net, not a proof: fragments that start alike or end alike are the ones that can be swapped
    if t == "match" and not ans.startswith(REVIEWED):
        pairs = [p.strip().split(" = ", 1) for p in ans.split(" ; ")]
        lefts = [p[0].lower().split() for p in pairs]; rights = [p[1].lower().split() for p in pairs if len(p) == 2]
        if len({tuple(x[:3]) for x in lefts}) < len(lefts) and all(len(x) >= 3 for x in lefts): flag(f, n, "two beginnings start with the same three words (can the endings be swapped?)", ans)
        if len({tuple(x[-3:]) for x in rights}) < len(rights) and all(len(x) >= 3 for x in rights): flag(f, n, "two endings end with the same three words (can they be swapped?)", ans)
        if len(pairs) < 3 or len(pairs) > 6: flag(f, n, "3 to 6 pairs", ans)
    # 3. a second copy of a task under another wording would overwrite the first one when the corrected file is imported again
    if t in ("mcq", "order", "match") and "___" not in q:
        key = (r["topic"], r["level"], t, ans.lower(), "|".join(sorted(x.strip().lower() for x in wrong.split("|"))) if t == "mcq" else "")
        seen_content[key].append((f, n))
    # 4. every question has both explanations, and the English one is a sentence (an earlier bug cut explanations to one character)
    if len(r["explanation shown to learner"].strip()) < 12: flag(f, n, "English explanation too short", r["explanation shown to learner"])
    if len(r["explanation in Latvian"].strip()) < 12: flag(f, n, "Latvian explanation missing", q)
    # 5. multiple-choice: the options are different and the correct one is not repeated
    if t == "mcq":
        opts = [ans] + [x.strip() for x in wrong.split("|")]
        if len({o.lower() for o in opts}) != len(opts): flag(f, n, "two options are the same", q)
        if len(opts) < 3: flag(f, n, "fewer than 3 options", q)
for k, v in seen_content.items():
    if len(v) > 1: bad.append(f"same task twice under different wording: {k[2]} / {k[3][:60]}  {v}")
for b in bad[:40]: print("FAIL", b)
print(f"{len(rows)} questions checked, {len(bad)} problems")
sys.exit(1 if bad else 0)
