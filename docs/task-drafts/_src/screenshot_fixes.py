"""Keep the reviewed 7 November corrections when a draft CSV is regenerated."""
import json
from pathlib import Path
FIXES=json.loads(Path(__file__).with_name('screenshot_fixes_20261107.json').read_text())
def apply(name,row):
    for fix in FIXES.get(name,[]):
        if [row[2],row[3],row[4]]==fix['match']:
            row=list(row)
            for index,value in fix['set'].items(): row[int(index)]=value
            break
    return row
