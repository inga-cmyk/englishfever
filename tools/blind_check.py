#!/usr/bin/env python3
"""Blind check of tasks (docs/BLIND-CHECK.md).
    python3 tools/blind_check.py export NAME [--src FILE.csv ...] [--keys KEYFILE] [--limit N]
    python3 tools/blind_check.py compare NAME
    python3 tools/blind_check.py record NAME [--ids ID ...]   (records every task without an open flag, or only the ids given)
Tasks are read as the importer reads them (tools/dump_items.php). --src adds draft files that are not served yet (copied next to
the prepared files for the dump only). --keys: a file with one gate key per line (app/tests/item_gates_test.py key()).
"""
import hashlib, json, os, random, re, shutil, subprocess, sys, tempfile
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs", "review", "blind")
REC = os.path.join(OUT, "records.json")
sys.path.insert(0, os.path.join(ROOT, "app", "tests"))
from item_gates_test import key, task_hash   # noqa: E402

def dump(extra=()):
    tmp = tempfile.mkdtemp(); out = os.path.join(tmp, "items.json"); copies = []
    try:
        for f in extra:
            dst = os.path.join(ROOT, "docs", "task-drafts", "zz-blind-" + os.path.basename(f)); shutil.copy(f, dst); copies.append(dst)
        r = subprocess.run(["php", os.path.join(ROOT, "tools", "dump_items.php"), out], capture_output=True, text=True, env=dict(os.environ, EF_DEV="1"))
        if r.returncode: sys.exit(r.stdout + r.stderr)
        return json.load(open(out, encoding="utf-8"))
    finally:
        for c in copies: os.remove(c)


def as_learner(i, rnd):
    """The task as the learner sees it: no key, no explanation; options and cards shuffled."""
    t = {"id": None, "level": "B2.2" if str(i["level"]).startswith("C1") else i["level"], "kind": i["kind"], "instruction_and_task": i["q"]}
    if i["kind"] == "mcq":
        opts = [i["correct"]] + list(i["wrong"]); rnd.shuffle(opts); t["options"] = opts
    elif i["kind"] == "gap" and i.get("bank"):
        chips = list(i["bank"]); rnd.shuffle(chips); t["word_cards"] = chips; t["note"] = "the learner drags one card into each gap"
    elif i["kind"] == "gap":
        t["note"] = "the learner types the missing word(s); several gaps: one answer per gap"
    elif i["kind"] == "order":
        w = i["sentence"].split(); rnd.shuffle(w); t["word_cards"] = w; t["note"] = "the learner puts all the cards in order"
    elif i["kind"] == "match":
        left = [p[0] for p in i["pairs"]]; right = [p[1] for p in i["pairs"]]; rnd.shuffle(right); t["left"] = left; t["right"] = right
    elif i["kind"] == "text":
        t["note"] = "the learner types a whole sentence"
    elif i["kind"] == "write":
        t["note"] = "open writing; the app checks that some forms are used"
    return t


def the_key(i):
    k = {"kind": i["kind"]}
    if i["kind"] == "mcq": k["correct"] = i["correct"]; k["wrong"] = i["wrong"]
    elif i["kind"] in ("gap", "text"): k["accepted"] = i["answers"]
    elif i["kind"] == "order": k["sentence"] = i["sentence"]; k["also"] = i.get("also", [])
    elif i["kind"] == "match": k["pairs"] = i["pairs"]
    elif i["kind"] == "write": k["model"] = i.get("model"); k["must"] = [m[1] for m in i.get("must", [])]
    return k


def norm(s):
    s = str(s).lower().replace("’", "'").replace("*", "")
    s = re.sub(r"[.!?,]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def export(name, src, keys_file, limit):
    items = dump(src)
    want = None
    if keys_file: want = set(l.rstrip("\n") for l in open(keys_file, encoding="utf-8") if l.strip())
    names = {"zz-blind-" + os.path.basename(f) for f in src}
    sel = [i for i in items if (want is not None and key(i) in want) or i["src"].split(":")[0] in names or (want is None and not src)]
    if limit: sel = sel[:limit]
    rnd = random.Random(14112026)
    tasks, keyout = [], {}
    for n, i in enumerate(sel, 1):
        tid = f"{name}-{n:03d}"
        t = as_learner(i, rnd); t["id"] = tid; tasks.append(t)
        keyout[tid] = {"hash": task_hash(i), "gate_key": key(i), "src": i["src"], "point": i.get("point"), "key": the_key(i)}
    os.makedirs(OUT, exist_ok=True)
    json.dump(tasks, open(os.path.join(OUT, name + "-tasks.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump(keyout, open(os.path.join(OUT, name + "-key.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{len(tasks)} tasks: {OUT}/{name}-tasks.json (for the readers), {name}-key.json (not for the readers)")


def accepted(k, ans):
    """Is a reader's answer accepted by the key (roughly as the grader does)?"""
    if ans is None: return False
    a = ans if isinstance(ans, list) else [ans]
    if k["kind"] == "mcq": return norm(a[0]) == norm(k["correct"])
    if k["kind"] in ("gap", "text"):
        if len(k["accepted"]) == 1 and len(a) == 1: return any(norm(a[0]) == norm(x) for x in k["accepted"][0])
        if len(a) != len(k["accepted"]): a = [x for x in re.split(r"\s*/\s*", " / ".join(map(str, a)))]
        return len(a) == len(k["accepted"]) and all(any(norm(x) == norm(y) for y in alts) for x, alts in zip(a, k["accepted"]))
    if k["kind"] == "order": return norm(a[0]) in [norm(k["sentence"])] + [norm(x) for x in k.get("also", [])]
    if k["kind"] == "match":
        mine = {norm(p[0]): norm(p[1]) for p in a if isinstance(p, (list, tuple)) and len(p) == 2}
        return all(mine.get(norm(l)) == norm(r) for l, r in k["pairs"])
    return True   # open writing: no fixed answer


def compare(name):
    keyd = json.load(open(os.path.join(OUT, name + "-key.json"), encoding="utf-8"))
    tasks = {t["id"]: t for t in json.load(open(os.path.join(OUT, name + "-tasks.json"), encoding="utf-8"))}
    readers = []
    for r in (1, 2):
        p = os.path.join(OUT, f"{name}-reader{r}.json")
        if os.path.isfile(p): readers.append({x["id"]: x for x in json.load(open(p, encoding="utf-8"))})
    lines = [f"# Blind check {name}: flags for the judge", "", f"{len(keyd)} tasks, {len(readers)} readers.", ""]
    flags = {}
    for tid, k in keyd.items():
        why = []
        answers = []
        for n, r in enumerate(readers, 1):
            x = r.get(tid)
            if not x: why.append(f"reader {n}: no answer"); continue
            answers.append(norm(json.dumps(x.get("answer"), ensure_ascii=False)))
            if not accepted(k["key"], x.get("answer")): why.append(f"reader {n}: answer not accepted: {x.get('answer')}")
            for f, label in (("other_correct", "another correct answer"), ("wrong_options_that_fit", "a wrong option that fits"),
                             ("instruction_problem", "instruction"), ("level_problem", "level"), ("sense_problem", "sense")):
                v = x.get(f)
                if v and v not in ("none", "no", [], ""): why.append(f"reader {n}: {label}: {v}")
        if len(set(answers)) > 1 and k["key"]["kind"] != "write": why.append("the readers disagree")
        if why: flags[tid] = why
    for tid, why in flags.items():
        t = tasks[tid]; k = keyd[tid]
        lines += [f"## {tid} · {t['level']} · {t['kind']} · {k['src']}", "", "Task: " + t["instruction_and_task"]]
        for f in ("options", "word_cards", "left", "right"):
            if f in t: lines.append(f"{f}: " + " | ".join(map(str, t[f])))
        lines += ["Key: " + json.dumps(k["key"], ensure_ascii=False)] + ["- " + w for w in why] + [""]
    open(os.path.join(OUT, name + "-flags.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    json.dump(sorted(flags), open(os.path.join(OUT, name + "-flagged.json"), "w"), indent=0)
    print(f"{len(flags)} of {len(keyd)} flagged: {OUT}/{name}-flags.md")


def record(name, ids):
    keyd = json.load(open(os.path.join(OUT, name + "-key.json"), encoding="utf-8"))
    flagged = set(json.load(open(os.path.join(OUT, name + "-flagged.json")))) if os.path.isfile(os.path.join(OUT, name + "-flagged.json")) else set()
    rec = json.load(open(REC, encoding="utf-8")) if os.path.isfile(REC) else {}
    n = 0
    for tid, k in keyd.items():
        if ids and tid not in ids: continue
        if not ids and tid in flagged: continue
        rec[k["hash"]] = {"round": name, "task": tid, "gate_key": k["gate_key"]}; n += 1
    json.dump(rec, open(REC, "w", encoding="utf-8"), ensure_ascii=False, indent=0, sort_keys=True)
    print(f"{n} records written ({len(rec)} in all)")


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a: sys.exit(__doc__)
    cmd, name = a[0], a[1]
    opt = lambda f: [a[i + 1] for i, x in enumerate(a) if x == f]
    if cmd == "export": export(name, opt("--src"), (opt("--keys") or [None])[0], int((opt("--limit") or [0])[0]))
    elif cmd == "compare": compare(name)
    elif cmd == "record": record(name, set(a[a.index("--ids") + 1:]) if "--ids" in a else set())
    else: sys.exit(__doc__)
