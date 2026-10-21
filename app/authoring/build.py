#!/usr/bin/env python3
"""Validate the question bank and write app/content/{items,meta}.json.

    python3 app/authoring/build.py
"""
import json
import os
import re
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import dsl  # noqa: E402
import content_basic, content_perfect_future, content_passive  # noqa: E402,F401
import content_conditionals, content_reported  # noqa: E402,F401
import lv_data  # noqa: E402  (Latvian explanations up to B1.2)
from rules import SKILLS, RULES, BLOOM, AREAS  # noqa: E402

OUT = os.path.join(HERE, "..", "content")
errors = []


def err(item, msg):
    errors.append(f"{item['id']}: {msg}")


ids = Counter(i["id"] for i in dsl.ITEMS)
for k, n in ids.items():
    if n > 1:
        errors.append(f"duplicate id {k}")

skill_levels = {s[0]: s[3] for s in SKILLS}
for it in dsl.ITEMS:
    if it["skill"] not in skill_levels:
        err(it, "unknown skill")
    elif it["level"] not in skill_levels[it["skill"]]:
        err(it, f"level {it['level']} not declared for skill")
    if it["kind"] == "mcq":
        opts = [it["correct"]] + it["wrong"]
        if len(set(opts)) != len(opts):
            err(it, "duplicate options")
        if len(opts) < 3:
            err(it, "fewer than 3 options")
        for w in it["wrong_why"]:
            if w not in it["wrong"]:
                err(it, f"wrong_why key not an option: {w}")
    if it["kind"] in ("gap", "text", "order"):
        for blank in it["answers"]:
            if not blank:
                err(it, "empty answers")
    if it["kind"] == "gap" and it.get("bank"):
        firsts = [b[0] for b in it["answers"]]
        for a in firsts:
            if a not in it["bank"]:
                err(it, f"bank misses the answer {a!r}")
        if len(it["bank"]) < len(firsts) + 1:
            err(it, "bank needs at least one decoy")
        if len(set(it["bank"])) != len(it["bank"]):
            err(it, "duplicate bank cards")
        for blank in it["answers"]:
            if len(blank) > 1:
                err(it, "a bank gap takes exactly one answer per blank (alternatives cannot be dragged)")
    if it["kind"] == "order":
        toks = sorted(it["sentence"].split(" "))
        if len(toks) < 4 or len(toks) > 16:
            err(it, "word order tasks need 4 to 16 words")
        for alt in it["answers"][0][1:]:
            if sorted(alt.split(" ")) != toks:
                err(it, f"extra_accept must use exactly the same words: {alt}")
    if it["kind"] == "match":
        rights = [p[1] for p in it["pairs"]]
        if len(it["pairs"]) < 3 or len(it["pairs"]) > 6:
            err(it, "match tasks need 3 to 6 pairs")
        if len(set(rights)) != len(rights) or len({p[0] for p in it["pairs"]}) != len(it["pairs"]):
            err(it, "match cards must all differ")
    if it["kind"] == "write":
        for rx, _ in it["must"]:
            try:
                re.compile(rx)
            except re.error as e:
                err(it, f"bad regex {rx}: {e}")
        # the model answer must satisfy its own checks (Python regex ~ PCRE for these patterns)
        for rx, msg in it["must"]:
            if not re.search(rx, it["model"], re.I):
                err(it, f"model answer fails its own check: {msg}")
    for h in it.get("hints", []):
        re.compile(h[0])

# coverage: every skill-level has Bloom 1..6
cover = {}
for it in dsl.ITEMS:
    cover.setdefault((it["skill"], it["level"]), set()).add(it["bloom"])
for s in SKILLS:
    for lv in s[3]:
        missing = set(range(1, 7)) - cover.get((s[0], lv), set())
        if missing:
            errors.append(f"{s[0]} {lv}: missing Bloom levels {sorted(missing)}")
    if s[0] not in RULES:
        errors.append(f"no rule card for {s[0]}")

# Latvian explanations: every item up to B1.2 and every rule card of a topic that has such levels
LV_MAX = dsl.LEVELS.index("B1.2")
n_lv = 0
for it in dsl.ITEMS:
    if dsl.LEVELS.index(it["level"]) > LV_MAX:
        continue
    t = lv_data.LV.get(it["id"])
    if not t or not t.get("why"):
        err(it, "Latvian explanation missing")
        continue
    n_lv += 1
    it["why_lv"] = t["why"]
    if it["kind"] == "mcq" and it["wrong_why"]:
        wl = t.get("wrong", [])
        if len(wl) != len(it["wrong_why"]):
            err(it, f"Latvian 'wrong' needs {len(it['wrong_why'])} messages, has {len(wl)}")
        else:
            it["wrong_why_lv"] = dict(zip(it["wrong_why"].keys(), wl))
    key = "hints" if it["kind"] in ("gap", "text") else ("must" if it["kind"] == "write" else None)
    if key and it.get(key):
        ml = t.get("msgs", [])
        if len(ml) != len(it[key]):
            err(it, f"Latvian 'msgs' needs {len(it[key])} messages, has {len(ml)}")
        else:
            it[key] = [list(x)[:2] + [m] for x, m in zip(it[key], ml)]
for sk in SKILLS:
    if dsl.LEVELS.index(sk[3][0]) <= LV_MAX:
        t = lv_data.LV_RULES.get(sk[0])
        if not t or not all(k in t for k in ("form", "use", "signals")):
            errors.append(f"{sk[0]}: Latvian rule card missing")

if errors:
    print("\n".join(errors))
    sys.exit(1)

os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "items.json"), "w", encoding="utf-8") as f:
    json.dump(dsl.ITEMS, f, ensure_ascii=False, indent=0)
meta = {
    "levels": dsl.LEVELS,
    "areas": [{"id": a[0], "label": a[1]} for a in AREAS],
    "skills": [dict({"id": s[0], "label": s[1], "area": s[2], "levels": s[3], "rule": RULES[s[0]]},
                    **({"rule_lv": lv_data.LV_RULES[s[0]]} if s[0] in lv_data.LV_RULES else {})) for s in SKILLS],
    "bloom": {str(k): {"name": v[0], "desc": v[1]} for k, v in BLOOM.items()},
}
with open(os.path.join(OUT, "meta.json"), "w", encoding="utf-8") as f:
    json.dump(meta, f, ensure_ascii=False, indent=1)

# spreadsheet for the teachers who review the bank (docs/practice-question-bank-review.csv)
import csv
labels = {s[0]: s[1] for s in SKILLS}
bloom_names = {k: v[0] for k, v in BLOOM.items()}
rev = os.path.join(HERE, "..", "..", "docs", "practice-question-bank-review.csv")
with open(rev, "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["id", "topic", "area", "level", "thinking level", "type", "task", "correct answer", "wrong options / checks", "explanation shown to learner", "explanation in Latvian (up to B1.2)", "reviewed (ok / change)", "comment"])
    for it in dsl.ITEMS:
        voice = next(a[1] for a in AREAS if a[0] == next(s[2] for s in SKILLS if s[0] == it["skill"]))
        if it["kind"] == "mcq":
            ans, extra = it["correct"], " | ".join(it["wrong"])
        elif it["kind"] in ("gap", "text", "order"):
            ans = it["sentence"] if it["kind"] == "order" else " / ".join(b[0] for b in it["answers"])
            alts = [a for b in it["answers"] for a in b[1:]]
            extra = ("also accepted: " + " | ".join(alts)) if alts else ""
            if it.get("bank"):
                extra = ("word bank: " + " | ".join(it["bank"]) + ("; " + extra if extra else ""))
        elif it["kind"] == "match":
            ans = " ; ".join(f"{p[0]} = {p[1]}" for p in it["pairs"])
            extra = ""
        else:
            ans, extra = it["model"], "must contain: " + " ; ".join(m[1] for m in it["must"])
        w.writerow([it["id"], labels[it["skill"]], voice, it["level"], f'{it["bloom"]} {bloom_names[it["bloom"]]}', it["kind"], it["q"], ans, extra, it["why"], it.get("why_lv", ""), "", ""])

# The app reads these .php copies. A request for a .php file runs it and prints nothing, so the answers stay
# private even on a server that ignores .htaccess. (The .json files are for tests and review only; they are not packaged.)
for name in ("items", "meta"):
    with open(os.path.join(OUT, name + ".json"), encoding="utf-8") as f:
        raw = f.read()
    assert "EF_JSON_END" not in raw
    with open(os.path.join(OUT, name + ".php"), "w", encoding="utf-8") as f:
        f.write("<?php\n// generated by authoring/build.py\nreturn json_decode(<<<'EF_JSON_END'\n" + raw + "\nEF_JSON_END\n, true);\n")

print(f"OK: {len(dsl.ITEMS)} items, {len(SKILLS)} skills, {n_lv} items with Latvian explanations")
by_level = Counter(i["level"] for i in dsl.ITEMS)
by_bloom = Counter(i["bloom"] for i in dsl.ITEMS)
by_kind = Counter(i["kind"] for i in dsl.ITEMS)
print("by level:", dict(sorted(by_level.items())))
print("by bloom:", dict(sorted(by_bloom.items())))
print("by kind:", dict(by_kind))
