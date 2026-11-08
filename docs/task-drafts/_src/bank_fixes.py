"""Word-bank wrong options that build real forms (teacher, 8 November): kept when the draft files regenerate.
Each fix matches a row by type, task and answer and sets the bank (and, where a time word was added, the new task text
with the old text in *replaces*). Batches: docs/task-drafts/bank-options-batch*-review.md."""
import json
from pathlib import Path

FIXES = json.loads(Path(__file__).with_name('bank_fixes_20261108.json').read_text())


def apply(name, row):
    for fix in FIXES.get(name, []):
        if list(row[2:5]) == fix['match']:
            row = list(row) + [''] * max(0, 14 - len(row))
            for index, value in fix['set'].items():
                row[int(index)] = value
            break
    return row
