"""Helpers that write a task CSV in the format of the Tasks tab (app/src/CustomItems.php)."""
import csv, os, sys
HEAD = ["topic", "level", "type", "task", "correct answer", "wrong options / checks", "explanation shown to learner", "explanation in Latvian", "thinking level"]
rows = []
def mc(t, lv, b, q, ok, wrong, why, lvw): rows.append([t, lv, "mcq", q, ok, " | ".join(wrong), why, lvw, b])
def gp(t, lv, b, q, ok, why, lvw, bank=None): rows.append([t, lv, "gap", q, ok, ("bank: " + " | ".join(bank)) if bank else "", why, lvw, b])
def tx(t, lv, b, q, ok, why, lvw): rows.append([t, lv, "text", q, " | ".join(ok) if isinstance(ok, (list, tuple)) else ok, "", why, lvw, b])
def od(t, lv, b, q, ok, why, lvw, also=None): rows.append([t, lv, "order", q, ok, ("also accepted: " + " | ".join(also)) if also else "", why, lvw, b])
def mt(t, lv, b, q, pairs, why, lvw): rows.append([t, lv, "match", q, " ; ".join(f"{a} = {c}" for a, c in pairs), "", why, lvw, b])
def save(name):
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", name)
    with open(out, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f); w.writerow(HEAD); w.writerows(rows)
    print(name, len(rows), "rows")
