"""The draft of 11-12 November (reports, speaker tags, situation sentences, Join with…), approved by the teacher on 12 November
after a second reader: kept when the draft files regenerate. Each fix matches a row by type, task and answer (as the earlier
overlays leave it) and sets columns, or drops the row ("drop": the task is retired; the teacher presses Retire on the server).
Review: docs/task-drafts/reports-2026-11-11-review.md."""
import json
from pathlib import Path

FIXES = json.loads(Path(__file__).with_name('draft_fixes_20261112.json').read_text())


def apply(name, row):
    for fix in FIXES.get(name, []):
        if list(row[2:5]) == fix['match']:
            if fix.get('drop'): return None
            row = list(row) + [''] * max(0, 14 - len(row))
            for index, value in fix['set'].items():
                row[int(index)] = value
            break
    return row
