#!/usr/bin/env python3
"""Choice tasks whose options give the answer away (teacher's rule, 3 November): options of very different length, the correct one
clearly the longest, or one option on another theme while the others share one (e.g. a near-identical pair in a NOT-correct task).
    python3 tools/option_audit.py                     # the built-in bank and every file in docs/task-drafts
    python3 tools/option_audit.py FILE.csv [...]      # only these files
It is a heuristic: verb-form choices like "Were / working" are flagged as "odd-theme" although they are fine; read each one."""
import csv, glob, json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STOP = set("a an the i you he she it we they is are was were be been to of in on at for and or but not do does did have has had my your his her our their this that with will would can could no yes it's should".split())
def words(s): return set(w for w in re.findall(r"[a-z']+", s.lower()) if w not in STOP and len(w) > 2)
def check(opts):
    L = [len(o) for o in opts]; mx, mn = max(L), min(L); f = []
    if mx - mn > max(8, 0.4 * mx): f.append("uneven")
    if L[0] == mx and mx - sorted(L)[-2] >= 8: f.append("correct-longest")
    if len(opts) >= 4 and all(len(o.split()) >= 3 for o in opts):
        ws = [words(o) for o in opts]
        for i in range(len(opts)):
            others = [j for j in range(len(opts)) if j != i]
            if all(not (ws[i] & ws[j]) for j in others) and all(ws[a] & ws[b] for a in others for b in others if a < b):
                f.append("odd-theme:" + ("correct" if i == 0 else "wrong")); break
    return f
files = sys.argv[1:]
out = []
if not files:
    for it in json.load(open(os.path.join(ROOT, "app", "content", "items.json"))):
        if it["kind"] == "mcq" and (f := check([it["correct"]] + it["wrong"])): out.append(("built-in " + it["id"], it["q"], it["correct"], it["wrong"], f))
    files = sorted(glob.glob(os.path.join(ROOT, "docs", "task-drafts", "*.csv")))
for fn in files:
    for r in list(csv.reader(open(fn, encoding="utf-8-sig")))[1:]:
        if len(r) < 6 or r[2] != "mcq": continue
        wrong = [w.strip() for w in r[5].split("|") if w.strip()]
        if wrong and (f := check([r[4]] + wrong)): out.append((os.path.basename(fn) + " " + r[0], r[3], r[4], wrong, f))
for src, q, ok, wrong, f in out: print(f"{' '.join(f):28} {src[:40]:40} {q[:60]} | OK: {ok} | " + " / ".join(wrong))
print(len(out), "flagged")
