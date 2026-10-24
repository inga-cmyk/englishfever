"""Copies of built-in B1 tasks that are really A2 level, as an import file at A2.2. The originals leave the B1 pool once the copies are approved."""
import json, os
from lib import *
APP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "app")
raw = json.load(open(os.path.join(APP, "content", "items.json"), encoding="utf-8"))
items = {i["id"]: i for i in (raw if isinstance(raw, list) else raw["items"])}
meta = json.load(open(os.path.join(APP, "content", "meta.json"), encoding="utf-8"))
label = {s["id"]: s["label"] for s in meta["skills"]}
IDS = "pc-B11-1a pc-B11-3b pa-B11-1a pa-B12-3a pp-B11-1a pp-B11-3a pp-B12-1a pp-B12-3a fu-B11-1a-r2 fu-B11-3a fu-B11-3b psp-B11-1a psp-B11-3a psp-B12-1a psp-B12-3a pasp-B11-1a pasp-B11-3a-r2 pasp-B11-3b pasp-B12-1a cf-B11-3a".split()
def _cur(i): return next(c for c in (i, i + "-r2", i + "-r3") if c in items)   # the id the task has now (a corrected task has a new revision id)
IDS = [_cur(i) for i in IDS]
for i in IDS:
    x = items[i]; t = label[x["skill"]]
    if x["kind"] == "mcq": mc(t, "A2.2", x["bloom"], x["q"], x["correct"], x["wrong"], x["why"], x.get("why_lv", ""))
    elif x["kind"] == "text": tx(t, "A2.2", x["bloom"], x["q"], [a for a in x["answers"][0]], x["why"], x.get("why_lv", ""))
    elif x["kind"] == "gap": gp(t, "A2.2", x["bloom"], x["q"], " / ".join(" | ".join(g) for g in x["answers"]), x["why"], x.get("why_lv", ""), x.get("bank"))
    else: raise SystemExit("unexpected kind " + i)
for _i, _r in enumerate(rows):
    if _r[3] == "Where ___ this photo ___? (take)": rows[_i] = _r[:9] + ["Where ___ the film ___? (film)"]
save("a2-relabelled-1.csv")
open(os.path.join(APP, "content", "relabelled.php"), "w").write("<?php\n// Built-in tasks that were copied to a lower level (docs/task-drafts/a2-relabelled-1.csv). They leave the active pool when the approved copy exists.\nreturn " + json.dumps(IDS) + ";\n")
