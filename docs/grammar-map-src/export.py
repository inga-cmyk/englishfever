"""Writes the machine-readable outputs of the grammar map (run after gaps.py):
docs/GRAMMAR-MAP.json, docs/GRAMMAR-MAP-TASKS.csv and the two review lists in docs/review/."""
import sys, os, json, csv, re, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build as B, review as R
C = B.C; ROOT = C.ROOT; P = B.P; LV = B.LV
out = lambda p: os.path.join(ROOT, p)

# 1. the map
json.dump({"levels": LV, "points": [dict(id=p["id"], name=p["name"], level=p["level"], area=p["area"], can_do=p["can"], needs=p["needs"],
          contrasts=p["vs"], leads_to=p["leads"], typical_errors=p["err"], sources=B.src(p), topics=[] if p["topics"] == ["new"] else p["topics"],
          card=p["card"], tasks=dict(check=p["c"].get("check", 0), use=p["c"].get("use", 0), learn=p["c"].get("learn", 0)), task_levels=p["tl"]) for p in P]},
          open(out("docs/GRAMMAR-MAP.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# 2. every task with its point; `key` is the key of app/tests/item_gates_test.py
rows = []; new = 0
for i in B.items:
    p = R.point(i); h = R.how(i); new += h.startswith("rule (new")
    rows.append([p, C.BY[p]["level"], i["skill"], i["level"], i["role"], i["kind"], h, i["id"] if i["src"] == "built-in" else "", i["src"], R.key(i)])
rows.sort(key=lambda r: (LV.index(r[1]), r[0], r[3]))
with open(out("docs/GRAMMAR-MAP-TASKS.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(["point", "point_level", "topic", "task_level", "role", "kind", "sorted_by", "built_in_id", "source", "key"]); w.writerows(rows)

# 3. choice tasks with a situation or an explanation before the options
def situation(i):
    q = i["q"]
    if "___" in q: return bool(re.match(r"^(You |A |Your |Imagine|Choose the option that|In an email|The sign|Someone)", q)) and len(q.split()) > 14
    if re.match(r"^(Which sentence is NOT correct|Which sentence is correct|Choose the correct (sentence|option|question|form)[.:]?$|Which question is (NOT )?correct|Which sentence has a mistake)", q): return False
    return len(q.split()) >= 8
MEAN = r"Which sentence (means|says|shows|is about|describes|gives|focuses|expresses|tells|puts|talks|imagines|states|keeps|reports)|What does|What is the difference|which action|Why (do|can)|What really"
def gate(i):
    m = re.match(r"^(.*?)\s*Choose the (correct|right|more natural) option", i["q"]); return "yes" if m and len(m.group(1).split()) > 10 else ""
os.makedirs(out("docs/review"), exist_ok=True)
def filled(path):   # a work list that already has verdicts is a record of the reading (14 November): never overwritten
    p = out(path)
    if os.path.isfile(p) and any(r.get("verdict") for r in csv.DictReader(open(p, encoding="utf-8"))): print("kept (verdicts filled):", path); return True
    return False
c1 = [i for i in B.items if i["kind"] == "mcq" and situation(i)]
with open(out("docs/review/choice-with-situation-2026-11-14.csv") if not filled("docs/review/choice-with-situation-2026-11-14.csv") else os.devnull, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(["group", "caught_by_long_frame_gate", "topic", "level", "role", "question", "correct", "wrong", "verdict", "new_question", "source", "key"])
    for i in sorted(c1, key=lambda i: (bool(re.search(MEAN, i["q"])), i["skill"], i["level"])):
        w.writerow(["meaning question" if re.search(MEAN, i["q"]) else "situation + choice", gate(i), i["skill"], i["level"], i["role"], i["q"], i["correct"], " / ".join(map(str, i["wrong"])), "", "", i["src"], R.key(i)])

# 4. typed tasks that accept one answer only
RISK = {"present perfect simple or continuous": r"^(have|has|haven't|hasn't) (been \w+ing|\w+(ed|en|wn|t|ne))$", "will / going to / present continuous": r"^('ll \w+|will \w+|won't \w+|(am|is|are) going to \w+|(am|is|are) \w+ing)$",
        "used to or past simple / would": r"^(used to \w+|didn't use to \w+)$", "needn't / don't have to / don't need to": r"^(needn't|don't have to|doesn't have to|don't need to)$",
        "might / may / could": r"^(might|may|could)( not)?$", "couldn't / wasn't able to": r"^(couldn't|wasn't able to|weren't able to)$", "was / were": r"^(was|were|wasn't|weren't)$",
        "until / till, as soon as / when / once, if / when": r"^(until|till|as soon as|when|once|if|whether)$", "that / which / who": r"^(that|which|who)$",
        "past simple or past perfect": r"^had (\w+ly )?\w+(ed|en|wn|t|ne)$", "past simple or past continuous": r"^(was|were) \w+ing$"}
c2 = [i for i in B.items if i["kind"] in ("gap", "text") and len(i["answers"]) == 1 and len(i["answers"][0]) == 1]
def risk(a): return next((k for k, rx in RISK.items() if re.match(rx, a.strip().lower())), "")
with open(out("docs/review/typed-one-answer-2026-11-14.csv") if not filled("docs/review/typed-one-answer-2026-11-14.csv") else os.devnull, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(["risk_group", "topic", "level", "kind", "point", "question", "accepted", "verdict", "answers_to_add", "source", "key"])
    for i in sorted(c2, key=lambda i: (not risk(i["answers"][0][0]), risk(i["answers"][0][0]), i["skill"], i["level"])):
        w.writerow([risk(i["answers"][0][0]), i["skill"], i["level"], i["kind"], R.point(i), i["q"], i["answers"][0][0], "", "", i["src"], R.key(i)])
print(len(P), "points;", len(rows), "tasks,", new, "new or changed since the reading;", len(c1), "choice tasks with a situation (", sum(1 for i in c1 if not re.search(MEAN, i["q"])), "not meaning questions,", sum(1 for i in c1 if gate(i)), "caught by the long_frame gate );", len(c2), "typed tasks with one answer (", sum(1 for i in c2 if risk(i["answers"][0][0])), "in a risk group )")
