"""Add the batch 5 rows of a CSV to docs/grammar-map-src/assign_keys.json with their point (POINT_OF of the generator).
usage: python3 docs/task-drafts/_src/assign_points.py GENERATOR_MODULE CSV_NAME, e.g. gap_fill_a2 gap-fill-a2-1.csv; the generator needs POINT_OF and point_of(row)   (CSV in docs/task-drafts/ or pending/)"""
import json, os, subprocess, sys, tempfile, shutil
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, "docs/task-drafts/_src")); sys.path.insert(0, os.path.join(ROOT, "app/tests"))
from item_gates_test import key
mod, name = sys.argv[1], sys.argv[2]
os.chdir(os.path.join(ROOT, "docs/task-drafts/_src"))
g = __import__(mod)
src = os.path.join(ROOT, "docs/task-drafts", name)
copied = None
if not os.path.isfile(src):
    copied = os.path.join(ROOT, "docs/task-drafts", "zz-assign-" + name); shutil.copy(os.path.join(ROOT, "docs/task-drafts/pending", name), copied)
tmp = os.path.join(tempfile.mkdtemp(), "items.json")
try:
    subprocess.run(["php", os.path.join(ROOT, "tools/dump_items.php"), tmp], check=True, env=dict(os.environ, EF_DEV="1"), capture_output=True)
finally:
    if copied: os.remove(copied)
items = json.load(open(tmp, encoding="utf-8"))
base = os.path.basename(copied or src)
A = json.load(open(os.path.join(ROOT, "docs/grammar-map-src/assign_keys.json"), encoding="utf-8"))
n = 0
for i in items:
    s = str(i.get("src", ""))
    if not s.startswith(base + ":"): continue
    row = int(s.split(":")[1]) - 2
    A[key(i)] = [g.point_of(row), "read"]; n += 1
json.dump(A, open(os.path.join(ROOT, "docs/grammar-map-src/assign_keys.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print(n, "keys")
