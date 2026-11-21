"""Preserve the 8 November learner-answer review when draft files regenerate."""
import json
from pathlib import Path

FIXES = json.loads(Path(__file__).with_name('learner_fixes_20261108.json').read_text())
for _name, _list in json.loads(Path(__file__).with_name('learner_fixes_20261116.json').read_text()).items():   # tester's report, 16 November
    FIXES.setdefault(_name, []).extend(_list)
for _name, _list in json.loads(Path(__file__).with_name('learner_fixes_20261121.json').read_text()).items():   # tester's report and learners' data, 21 November
    FIXES.setdefault(_name, []).extend(_list)
for _name, _list in json.loads(Path(__file__).with_name('learner_fixes_20261121_iq.json').read_text()).items():   # indirect questions, 21 November (gp6_iq_b1-notes.md)
    FIXES.setdefault(_name, []).extend(_list)


def apply(name, row):
    for fix in FIXES.get(name, []):
        if list(row[2:5]) == fix['match']:
            row = list(row) + [''] * max(0, 14 - len(row))
            for index, value in fix['set'].items():
                row[int(index)] = value
            break
    return row
