"""Writes c1_retired_texts.json from the git history of docs/task-drafts/c1-*.csv (24 November 2026).

Every older version of a C1 task (rewritten or dropped) is named in the first row's *replaces* of its file (lib.save), so
*Add all* retires it on the server. An older version is found by what the importer matches (CustomItems::oldKey / qKey):
the correct option of a multiple-choice task, and also its question when the question has a gap; the task text of a gap or
a typed task; the sentence of a word order. A text that is still the key of a task in the current file is never named,
or the import would retire a task that is in use.
    python3 c1_retired_from_history.py      # then regenerate the c1 files with lib.save
Run it after the changed generators are committed, so the history holds the last version."""
import csv, io, json, os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
OUT = os.path.join(HERE, "c1_retired_texts.json")


def keys(rows):
    out = set()
    for r in rows:
        kind, q, ok = r.get("type", ""), r.get("task", "").strip(), r.get("correct answer", "").strip()
        if kind == "mcq":
            if ok: out.add(ok.split(" | ")[0].strip())
            if "___" in q or len(q) > 60: out.add(q)   # the importer matches such a question too (CustomItems::qKey)
        elif kind == "order":
            if ok: out.add(ok.split(" | ")[0].strip())
        elif q:
            out.add(q)
    return out


def read(text):
    return list(csv.DictReader(io.StringIO(text.lstrip("﻿"))))


def main():
    git = lambda *a: subprocess.run(["git", "-C", ROOT] + list(a), capture_output=True, text=True).stdout
    files = sorted(f for f in os.listdir(os.path.join(ROOT, "docs", "task-drafts")) if f.startswith("c1-") and f.endswith(".csv"))
    old = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    res = {}
    # a text that is a task in any current C1 file is never named (two files may share a topic: c1-pres-1 and c1-pres-2)
    current = set()
    for f in files: current |= keys(read(open(os.path.join(ROOT, "docs", "task-drafts", f), encoding="utf-8-sig").read()))
    for f in files:
        path = "docs/task-drafts/" + f
        seen = set(old.get(f, []))
        for h in git("log", "--format=%h", "--", path).split():
            seen |= keys(read(git("show", f"{h}:{path}")))
        gone = sorted(t for t in seen if t not in current)
        if gone: res[f] = gone
    json.dump(res, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print({k: len(v) for k, v in res.items()})


if __name__ == "__main__":
    main()
