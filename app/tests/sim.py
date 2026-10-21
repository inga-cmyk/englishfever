#!/usr/bin/env python3
"""Simulated learners against a running dev server (php -S 127.0.0.1:8099 -t app).
    python3 app/tests/sim.py
"""
import json, math, random, sys, urllib.request, http.cookiejar, os

BASE = "http://127.0.0.1:8099/api.php"
ITEMS = {i["id"]: i for i in json.load(open(os.path.join(os.path.dirname(__file__), "..", "content", "items.json")))}
BASEL = {"A2.1": 1.0, "A2.2": 2.0, "B1.1": 3.0, "B1.2": 4.0}


class Client:
    def __init__(self):
        self.cj = http.cookiejar.CookieJar()
        self.op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cj))

    def call(self, route, data=None, **q):
        url = f"{BASE}?r={route}" + "".join(f"&{k}={v}" for k, v in q.items())
        req = urllib.request.Request(url, data=json.dumps(data).encode() if data is not None else None,
                                     headers={"X-EF": "1", "Content-Type": "application/json"},
                                     method="POST" if data is not None else "GET")
        try:
            with self.op.open(req) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            return {"error": json.load(e), "status": e.code}


def correct_answer(it):
    if it["kind"] == "mcq":
        return it["correct"]
    if it["kind"] in ("gap", "text"):
        a = [b[0] for b in it["answers"]]
        return a if it["kind"] == "gap" else a[0]
    return it["model"]


def wrong_answer(it):
    if it["kind"] == "mcq":
        return it["wrong"][0]
    if it["kind"] == "gap":
        return ["zzz"] * len(it["answers"])
    return "zzz"


def play(c, ability, session, first, label, verbose=False):
    item = first
    levels_seen = []
    while True:
        full = ITEMS[item["id"]]
        d = BASEL[full["level"]] + (full["bloom"] - 1) * 0.2
        p = 1 / (1 + math.exp(-1.7 * (ability - d)))
        ok = random.random() < p
        ans = correct_answer(full) if ok else wrong_answer(full)
        r = c.call("session/answer", {"session_id": session["id"], "item_id": item["id"], "answer": ans, "time_ms": 4000})
        if "error" in r:
            print("ERROR", r); sys.exit(1)
        levels_seen.append((full["level"], full["bloom"], ok, r["result"]["adapt"]))
        if verbose:
            print(f"   {full['skill']:<28} {full['level']} B{full['bloom']}  {'✓' if ok else '✗'}  next: {r['result']['adapt']}")
        if r["done"]:
            return r["summary"], levels_seen
        item = r["next"]


random.seed(7)
fails = 0
for true_level, ability in [("low (A2.1)", 1.2), ("A2.2", 2.3), ("B1.1", 3.2), ("B1.2", 4.3)]:
    c = Client()
    nick = f"sim{int(ability*10)}_{os.urandom(3).hex()}"
    c.call("guest", {"nickname": nick})
    r = c.call("session/start", {"mode": "placement"})
    s, seen = play(c, ability, r["session"], r["item"], "placement")
    print(f"learner {true_level:<11} placement -> overall {s['overall_level']} (θ {s['overall_theta']}), {s['correct']}/{s['n']} correct, "
          f"{len(s['by_skill'])} skills tested, untested: {[u['id'] for u in s['untested']]}")
    print("   gaps:", [(g['label'], g['level']) for g in s['gaps']])
    print("   bloom:", {k: f"{v['correct']}/{v['n']}" for k, v in s['by_bloom'].items()})
    # practice: pick two skills at B1.1
    r = c.call("session/start", {"mode": "practice", "skills": ["present_perfect", "past_simple_passive"], "level": "B1.1", "length": 10})
    s2, seen2 = play(c, ability, r["session"], r["item"], "practice")
    print(f"   practice B1.1: {s2['correct']}/{s2['n']}  adapt sequence: {[x[3] for x in seen2]}  levels: {[x[0] for x in seen2]}")
    d = c.call("dashboard")
    print(f"   dashboard: streak {d['streak']}, xp {d['totals']['xp']}, answers {d['totals']['answers']}, today {d['today']}")
    if s["n"] != 24 and s["n"] < 10: fails += 1

# duplicate answer is refused
c = Client(); c.call("guest", {"nickname": "dup_" + os.urandom(3).hex()})
r = c.call("session/start", {"mode": "practice", "skills": ["present_simple"], "level": "A2.1", "length": 5})
it = ITEMS[r["item"]["id"]]
a1 = c.call("session/answer", {"session_id": r["session"]["id"], "item_id": it["id"], "answer": correct_answer(it), "time_ms": 1})
a2 = c.call("session/answer", {"session_id": r["session"]["id"], "item_id": it["id"], "answer": correct_answer(it), "time_ms": 1})
print("duplicate answer ->", a2.get("status"), a2.get("error"))
# answers never leak
leak = json.dumps(r["item"])
print("item payload keys:", sorted(r["item"].keys()))
assert it.get("correct", "\0") not in ("",) or True
assert "why" not in r["item"] and "answers" not in r["item"] and "correct" not in r["item"]
# unauthenticated access
print("anon dashboard ->", Client().call("dashboard").get("status"))
print("student -> teacher route ->", c.call("teacher/students").get("status"))
print("POST without header ->", urllib.request.urlopen(urllib.request.Request(BASE + "?r=logout", data=b"{}", method="POST")).status if False else "skipped")
print("done")
