#!/usr/bin/env python3
"""The topic-levels with fewer than 10 check / use tasks (built-in bank + every prepared draft in docs/task-drafts), i.e. where a
topic cannot reach "Learned" yet. The role rule copies Content::role (app/src/Content.php) closely enough for planning.
    python3 tools/small_banks.py            # the list with the number of tasks and how many are missing
    python3 tools/small_banks.py --tasks    # also the existing tasks of each (to write twins from)"""
import csv, glob, json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
meta = json.load(open(os.path.join(ROOT, "app", "content", "meta.json")))
lab = {s["label"]: s["id"] for s in meta["skills"]}
LEARN = re.compile(r"^(Which sentence (means|is about|tells|is a |describes|shows|imagines|expresses|uses|does NOT express|has a finished|is passive)|What is the difference|What usually happens|Which (words|word) usually|Which verb is normally)", re.I)
def role(kind, q, po, bank):
    if po or kind == "match": return "learn"
    if kind in ("text", "write") or (kind == "gap" and not bank): return "use"
    return "learn" if kind == "mcq" and LEARN.match(q) else "check"
T = {}
for it in json.load(open(os.path.join(ROOT, "app", "content", "items.json"))):
    if role(it["kind"], it["q"], it.get("practice_only"), it.get("bank")) == "learn": continue
    key = it.get("sentence") if it["kind"] == "order" else (it.get("correct") or (it.get("answers") or [[""]])[0][0])
    T.setdefault((it["skill"], it["level"]), []).append(("built-in " + it["id"], it["kind"], it["q"], str(key)))
for fn in sorted(glob.glob(os.path.join(ROOT, "docs", "task-drafts", "*.csv"))):
    for r in list(csv.reader(open(fn, encoding="utf-8-sig")))[1:]:
        if len(r) < 6: continue
        po = len(r) > 11 and r[11].strip() not in ("", "0", "no")
        if role(r[2], r[3], po, r[5].startswith("bank:")) == "learn": continue
        T.setdefault((lab.get(r[0], r[0]), r[1]), []).append((os.path.basename(fn), r[2], r[3], r[4]))
short = sorted(((k, v) for k, v in T.items() if len(v) < 10), key=lambda x: len(x[1]))
print(f"{len(short)} topic-levels under 10, {sum(10 - len(v) for k, v in short)} tasks missing")
for (skill, level), v in short:
    print(f"{skill:28} {level:5} has {len(v):2}, needs {10 - len(v)}")
    if "--tasks" in sys.argv:
        for src, kind, q, key in v: print(f"    {kind:5} {q}  →  {key}   [{src}]")
