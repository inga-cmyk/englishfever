"""Preserve the 8 November learner-answer review when draft files regenerate."""
import json
from pathlib import Path

FIXES = json.loads(Path(__file__).with_name('learner_fixes_20261108.json').read_text())


def apply(name, row):
    for fix in FIXES.get(name, []):
        if list(row[2:5]) == fix['match']:
            row = list(row) + [''] * max(0, 14 - len(row))
            for index, value in fix['set'].items():
                row[int(index)] = value
            break
    return row
