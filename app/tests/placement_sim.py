#!/usr/bin/env python3
"""How accurate is the placement test? Simulated learners (known ability) take the 12/24/40 question versions.
    python3 app/tests/placement_sim.py [reps]       needs the dev server (php -S 127.0.0.1:8099 -t app)
Prints, per test length: mean error of the fitted ability (bias), mean absolute error, and how often the reported level is the true one or next to it."""
import json, math, os, random, sys, statistics as st
sys.path.insert(0, os.path.dirname(__file__))
import importlib.util
src = open(os.path.join(os.path.dirname(__file__), "sim.py")).read().split("random.seed(7)")[0]
ns = {"__file__": os.path.join(os.path.dirname(os.path.abspath(__file__)), "sim.py")}
exec(compile(src, "sim_head", "exec"), ns)
Client, ITEMS, BASEL = ns["Client"], ns["ITEMS"], ns["BASEL"]
correct_answer, wrong_answer = ns["correct_answer"], ns["wrong_answer"]

reps = int(sys.argv[1]) if len(sys.argv) > 1 else 4
random.seed(11)
ORDER = list(BASEL)
def true_level(a):  # the level whose band holds the ability (bands centred on the level bases)
    out = "A2.1"
    for lv, b in BASEL.items():
        if a >= b - 0.5: out = lv
    return out

def play(c, ability, session, first):
    item = first; seq = []
    while True:
        full = ITEMS[item["id"]]
        d = BASEL[full["level"]] + (full["bloom"] - 1) * 0.2
        ok = random.random() < 1 / (1 + math.exp(-1.7 * (ability - d)))
        r = c.call("session/answer", {"session_id": session["id"], "item_id": item["id"], "answer": correct_answer(full) if ok else wrong_answer(full), "time_ms": 3000})
        if "error" in r: print("ERROR", r); sys.exit(1)
        seq.append((full["skill"], full["level"], ok))
        if r["done"]: return r["summary"], seq
        item = r["next"]

abilities = [1.4, 2.0, 2.6, 3.2, 3.8, 4.4, 5.0, 5.6, 6.4, 7.2]
for size in (12, 24, 40):
    errs = []; exact = near = full = 0; n = 0
    for a in abilities:
        for _ in range(reps):
            for f in ("ef.sqlite", "ef.sqlite-wal", "ef.sqlite-shm"):   # a fresh database each time: guests and sessions are rate-limited per connection
                try: os.remove(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "var", f))
                except FileNotFoundError: pass
            c = Client(); c.call("guest", {"t": 5000, "nickname": f"ps{size}_{os.urandom(3).hex()}"})
            r = c.call("session/start", {"mode": "placement", "length": size})
            if "session" not in r: print("START FAILED", r); sys.exit(1)
            s, seq = play(c, a, r["session"], r["item"])
            errs.append(s["overall_theta"] - a); n += 1
            d = abs(ORDER.index(s["overall_level"]) - ORDER.index(true_level(a)))
            exact += d == 0; near += d <= 1; full += s['overall_level'][:2] == true_level(a)[:2]
    print(f"{size:>2} questions: bias {st.mean(errs):+.2f}  mean abs error {st.mean(abs(e) for e in errs):.2f}  rmse {math.sqrt(st.mean(e*e for e in errs)):.2f}  "
          f"exact half-level {100*exact/n:.0f}%  full level {100*full/n:.0f}%  within one half-level {100*near/n:.0f}%  (n={n})")
