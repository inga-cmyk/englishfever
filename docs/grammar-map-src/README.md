# The source of the grammar map

`docs/GRAMMAR-MAP.md`, `docs/GRAMMAR-MAP-GAPS.md`, `docs/GRAMMAR-MAP.json`, `docs/GRAMMAR-MAP-TASKS.csv` and the two lists in `docs/review/` are generated from this folder. Do not edit them by hand: change the source here and run:

```
export GM_WORK=/tmp/grammar-map; mkdir -p $GM_WORK
php tools/dump_items.php $GM_WORK/items.json     # every task as the importer reads it
python3 docs/grammar-map-src/check.py            # ids, prerequisites, levels, cycles: must print no UNKNOWN / NEED LATER / CYCLE
python3 docs/grammar-map-src/gaps.py             # writes GRAMMAR-MAP.md and GRAMMAR-MAP-GAPS.md
python3 docs/grammar-map-src/export.py           # writes GRAMMAR-MAP.json, GRAMMAR-MAP-TASKS.csv, docs/review/*.csv
python3 docs/grammar-map-src/page.py             # writes $GM_WORK/gramatikas-karte.html (the page Inga opens)
```

| File | What it holds |
|---|---|
| `p1.py` … `p3.py` | the points A2.1 to B2.2: `P(id, name, level, can_do, n=needs, v=contrasts, e=typical errors, m=Murphy units, t=line in the reference list, g=English Grammar Profile, topic=…, rx=…)` |
| `fixes.py` | the corrections after the second reader and the teacher's five level decisions of 13 November (applied on top of p1 to p3) |
| `p4.py` | C1, the ten strands, with the sources seen for each and the task forms each strand needs |
| `assign_keys.json` | every task tied to a point: `key → [point, read / rule]`. The key is the one of `app/tests/item_gates_test.py` (topic, level, kind, question, body). A task that is new or changed has no entry and falls back to the patterns in `classify.py`; add it here after reading it |
| `classify.py`, `review.py` | the pattern sorting (fallback only) and the reader used for the hand reading (`python3 review.py <topic>` lists a topic's tasks under their points) |
| `build.py`, `gaps.py`, `export.py`, `page.py`, `check.py` | the generators |
| `questions.md`, `second_reading.md` | the texts of section 5 of the gaps document and of the second-reading record |
| `corr.txt` | the record of the 663 corrections made while reading (already inside `assign_keys.json`) |
