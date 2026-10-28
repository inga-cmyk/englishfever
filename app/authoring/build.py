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
import italics, italics_en  # noqa: E402  (examples in italics)
from rules import SKILLS, RULES, BLOOM, AREAS  # noqa: E402

OUT = os.path.join(HERE, "..", "content")
errors = []


def err(item, msg):
    errors.append(f"{item['id']}: {msg}")


# used to has its own topic (teacher, 27 October): the Past simple B1.2 tasks were all about used to. They leave the bank;
# learners' earlier answers to them stay readable (retired.json), and the used to topic has its own tasks.
dsl.ITEMS = [it for it in dsl.ITEMS if not (it["skill"] == "past_simple" and it["level"] == "B1.2")]
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
has_items = {it["skill"] for it in dsl.ITEMS}
for s in SKILLS:
    for lv in s[3]:
        if s[0] not in has_items:
            continue   # a topic whose tasks the teacher adds on the Tasks page
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

# Examples in explanations are marked *like this* (the app shows them in italics). English lines are hand-marked
# (italics_en.py), Latvian ones are marked by rule (italics.py). Marking may only add * (and drop the quote marks it replaces).
EN_INDEX = italics.index(italics_en.WHY, italics_en.MSGS, italics_en.RULECARDS)
en_used = set()


def mk_en(text):
    key = italics.norm(text)
    if key in EN_INDEX:
        en_used.add(key)
        return EN_INDEX[key]
    return text


def mk_lv(text):
    out = italics.lv_mark(text)
    assert italics.norm(out) == italics.norm(text), (text, out)
    return out


for src in [it for it in dsl.ITEMS] + list(RULES.values()) + list(lv_data.LV_RULES.values()):
    pass
for it in dsl.ITEMS:
    for k in ("why", "why_lv", "wrong_why", "wrong_why_lv", "hints", "must"):
        v = it.get(k)
        if isinstance(v, str) and "*" in v:
            errors.append(f"{it['id']}: '*' is reserved for italics but is in the {k} text")
    it["why"] = mk_en(it["why"])
    if it.get("why_lv"):
        it["why_lv"] = mk_lv(it["why_lv"])
    if it.get("wrong_why"):
        it["wrong_why"] = {a: mk_en(m) for a, m in it["wrong_why"].items()}
    if it.get("wrong_why_lv"):
        it["wrong_why_lv"] = {a: mk_lv(m) for a, m in it["wrong_why_lv"].items()}
    for key in ("hints", "must"):
        if it.get(key):
            it[key] = [[h[0], mk_en(h[1])] + ([mk_lv(h[2])] if len(h) > 2 else []) for h in it[key]]
import watch  # noqa: E402
RULES_MARKED = {}
for sid, r in RULES.items():
    RULES_MARKED[sid] = {"form": [mk_en(x) for x in r["form"]], "use": [mk_en(x) for x in r["use"]],
                         "signals": mk_en(r["signals"]), "example": mk_en(r["example"]) if r.get("example") else r.get("example")}
    _w = r.get("watch") or watch.WATCH.get(sid, {}).get("en")
    if _w: RULES_MARKED[sid]["watch"] = [mk_en(x) for x in _w]   # "Watch out": the other rules worth knowing (teacher, 28 October; watch.py)
import b1_topics  # noqa: E402
LV_RULES_MARKED = {}
for sid, r in lv_data.LV_RULES.items():
    _saved = set(italics.LV_ASCII)
    if sid in b1_topics.LV_CARDS:   # the new topics: a few more Latvian words without Latvian letters, only for their own cards
        italics.LV_ASCII |= b1_topics.LV_WORDS
    try:
        LV_RULES_MARKED[sid] = {"form": [mk_lv(x) for x in r["form"]], "use": [mk_lv(x) for x in r["use"]], "signals": mk_lv(r["signals"])}
        _w = r.get("watch") or watch.WATCH.get(sid, {}).get("lv")
        if _w: LV_RULES_MARKED[sid]["watch"] = [mk_lv(x) for x in _w]
    finally:
        italics.LV_ASCII.clear(); italics.LV_ASCII.update(_saved)
for key, line in EN_INDEX.items():
    if key not in en_used:
        errors.append("italics_en.py: this line matches no explanation text: " + line)

if errors:
    print("\n".join(errors))
    sys.exit(1)

# Apply reviewed revisions only after the legacy translations/formatting have
# been resolved. Each revision has a new ID; the published original is immutable.
from content_review import revise
from bank_integrity import validate, history
dsl.ITEMS = revise(dsl.ITEMS)
from content_variety import ITEMS as VARIETY
dsl.ITEMS.extend(VARIETY)
validate(dsl.ITEMS, SKILLS, dsl.LEVELS)
retired = history(dsl.ITEMS, os.path.join(HERE, 'history', 'published_items.json'),
                  record='--record-release' in sys.argv)

# practice only (teacher, 27 October): easy first steps whose answer can be guessed from the cards, and tasks whose hint gives the
# answer away. Never in the placement test, still in practice. A flag, not content, so it is set after the immutability check.
PRACTICE_ONLY = {"var-pa-a22-match-01", "var-ca-c11-order-01-r2", "ip-B12-1a"}   # ip-B12-1a: the wrong options miss the typical mistake (is the shop open); an easy practice task (teacher, 27 October)
for it in dsl.ITEMS:
    if it["id"] in PRACTICE_ONLY:
        it["practice_only"] = True

os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "items.json"), "w", encoding="utf-8") as f:
    json.dump(dsl.ITEMS, f, ensure_ascii=False, indent=0)
with open(os.path.join(OUT, "retired.json"), "w", encoding="utf-8") as f:
    json.dump(retired, f, ensure_ascii=False, indent=0)
import error_types
assert all(k in {s[0] for s in SKILLS} for k in error_types.SKILL_ERR), 'error_types.SKILL_ERR names a topic that does not exist'
meta = {
    "levels": dsl.LEVELS,
    "areas": [{"id": a[0], "label": a[1]} for a in AREAS],
    "skills": [dict({"id": s[0], "label": s[1], "area": s[2], "levels": s[3], "rule": RULES_MARKED[s[0]]},
                    **({"rule_lv": LV_RULES_MARKED[s[0]]} if s[0] in LV_RULES_MARKED else {})) for s in SKILLS],
    "bloom": {str(k): {"name": v[0], "desc": v[1]} for k, v in BLOOM.items()},
    # error types work in the background (authoring/error_types.py, docs/ERROR-TYPES.md); learners never see them
    "errors": {c: {"name": v[0], "group": v[1]} for c, v in error_types.ERRORS.items()},
    "skill_err": error_types.SKILL_ERR,
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
            alts = [(f"blank {n + 1}: " if len(it['answers']) > 1 else "") + " | ".join(b[1:])
                    for n, b in enumerate(it["answers"]) if len(b) > 1]
            extra = ("also accepted: " + "; ".join(alts)) if alts else ""
            if it.get("bank"):
                extra = ("word bank: " + " | ".join(it["bank"]) + ("; " + extra if extra else ""))
        elif it["kind"] == "match":
            ans = " ; ".join(f"{p[0]} = {p[1]}" for p in it["pairs"])
            extra = ""
        else:
            ans, extra = it["model"], "must contain: " + " ; ".join(m[1] for m in it["must"])
        w.writerow([it["id"], labels[it["skill"]], voice, it["level"], f'{it["bloom"]} {bloom_names[it["bloom"]]}', it["kind"], it["q"], ans, extra, italics.strip(it["why"]), italics.strip(it.get("why_lv", "")), "", ""])

# The app reads these .php copies. A request for a .php file runs it and prints nothing, so the answers stay
# private even on a server that ignores .htaccess. (The .json files are for tests and review only; they are not packaged.)
for name in ("items", "meta", "retired"):
    with open(os.path.join(OUT, name + ".json"), encoding="utf-8") as f:
        raw = f.read()
    assert "EF_JSON_END" not in raw
    with open(os.path.join(OUT, name + ".php"), "w", encoding="utf-8") as f:
        f.write("<?php\n// generated by authoring/build.py\nreturn json_decode(<<<'EF_JSON_END'\n" + raw + "\nEF_JSON_END\n, true);\n")

n_lv = sum(bool(it.get('why_lv')) for it in dsl.ITEMS)
print(f"OK: {len(dsl.ITEMS)} active items, {len(retired)} retired versions, {len(SKILLS)} skills, {n_lv} items with Latvian explanations")
by_level = Counter(i["level"] for i in dsl.ITEMS)
by_bloom = Counter(i["bloom"] for i in dsl.ITEMS)
by_kind = Counter(i["kind"] for i in dsl.ITEMS)
print("by level:", dict(sorted(by_level.items())))
print("by bloom:", dict(sorted(by_bloom.items())))
print("by kind:", dict(by_kind))
