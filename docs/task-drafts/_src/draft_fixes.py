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
_P6 = Path(__file__).with_name('draft_fixes_20261122e.json')   # explanations use the task's own sentence (tester, 22 November)
FIXES6 = json.loads(_P6.read_text()) if _P6.exists() else {}
_P7 = Path(__file__).with_name('draft_fixes_20261122f.json')   # the B1 recheck (blind round r21, judge notes docs/review/blind/r21-*-judge.md)
FIXES7 = json.loads(_P7.read_text()) if _P7.exists() else {}
_P8 = Path(__file__).with_name('draft_fixes_20261122g.json')   # easy B1 indirect questions practice only (tester, 22 November)
FIXES8 = json.loads(_P8.read_text()) if _P8.exists() else {}
_P9 = Path(__file__).with_name('draft_fixes_20261122h.json')   # second look at the B1 recheck (blind round r21b, judge notes docs/review/blind/r21b-*-judge.md)
FIXES9 = json.loads(_P9.read_text()) if _P9.exists() else {}


def apply(name, row):
    row = _apply(FIXES, name, row)
    for fixes in (FIXES2, FIXES3, FIXES4, FIXES5, FIXES6, FIXES7, FIXES8, FIXES9):
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
