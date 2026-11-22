"""The draft of 11-12 November (reports, speaker tags, situation sentences, Join with…), approved by the teacher on 12 November
after a second reader: kept when the draft files regenerate. Each fix matches a row by type, task and answer (as the earlier
overlays leave it) and sets columns, or drops the row ("drop": the task is retired; the teacher presses Retire on the server).
Review: docs/task-drafts/reports-2026-11-11-review.md."""
import json
from pathlib import Path

FIXES = json.loads(Path(__file__).with_name('draft_fixes_20261112.json').read_text())
_P2 = Path(__file__).with_name('draft_fixes_20261122.json')   # the B2 recheck of 22 November (blind round r20, judge notes docs/review/blind/r20-*-judge.md)
FIXES2 = json.loads(_P2.read_text()) if _P2.exists() else {}
_P3 = Path(__file__).with_name('draft_fixes_20261122b.json')   # its second blind round (r20b)
FIXES3 = json.loads(_P3.read_text()) if _P3.exists() else {}
_P4 = Path(__file__).with_name('draft_fixes_20261122c.json')   # and its third (r20c)
FIXES4 = json.loads(_P4.read_text()) if _P4.exists() else {}
_P5 = Path(__file__).with_name('draft_fixes_20261122d.json')   # and its last look (r20d: answers only)
FIXES5 = json.loads(_P5.read_text()) if _P5.exists() else {}


def apply(name, row):
    row = _apply(FIXES, name, row)
    for fixes in (FIXES2, FIXES3, FIXES4, FIXES5):
        if row is not None: row = _apply(fixes, name, row)
    return row


def _apply(fixes, name, row):
    for fix in fixes.get(name, []):
        if list(row[2:5]) == fix['match']:
            if fix.get('drop'): return None
            row = list(row) + [''] * max(0, 14 - len(row))
            for index, value in fix['set'].items():
                row[int(index)] = value
            break
    return row
