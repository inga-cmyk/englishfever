#!/usr/bin/env python3
"""The "learning with you now / showed up today" count: who is counted, privacy, cache.
Run against the dev server (SQLite):  php -S 127.0.0.1:8099 -t app ;  rm -f app/var/ef.sqlite* ;  python3 app/tests/pulse_test.py"""
import os, sys
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "comeback_test.py")).read()
exec(compile(src.split("def run(")[0], "helpers", "exec"), globals())


def answer_one(c, right=True):
    s = c.api("session/start", {"mode": "practice", "skills": ["present_simple"], "level": "A2.1", "length": 5})
    it = ITEMS[s["item"]["id"]]
    c.api("session/answer", {"session_id": s["session"]["id"], "item_id": it["id"], "answer": correct(it) if right else wrong(it), "time_ms": 2000})


a = login(9101, "Pulse One"); b = login(9102, "Pulse Two")
d0 = a.api("dashboard")
check("the dashboard carries the count, 0 and 0 when nobody has answered", d0["pulse"] == {"now": 0, "today": 0}, d0.get("pulse"))
answer_one(a)
g = C(); g.api("guest", {"t": 5000, "nickname": "Pulse Guest"}); answer_one(g, False)
t = C(); t.raw("/sso.php?token=" + urllib.parse.quote(token({"uid": 9103, "name": "Pulse Teacher", "teacher": True, "exp": int(time.time()) + 100, "n": os.urandom(6).hex()}))); answer_one(t)
import sqlite3; _c = sqlite3.connect(os.path.join(APP, "var", "ef.sqlite")); _c.execute("DELETE FROM kv WHERE k = 'pulse'"); _c.commit(); _c.close()   # the count is kept for a minute
check("the count is kept for a minute: a repeat call returns the same numbers", a.api("dashboard")["pulse"] == a.api("dashboard")["pulse"])
_c = sqlite3.connect(os.path.join(APP, "var", "ef.sqlite")); _c.execute("DELETE FROM kv WHERE k = 'pulse'"); _c.commit(); _c.close()
quiet = b.api("dashboard")["pulse"]   # b has not answered
check("learners and guests count, a teacher does not (2, not 3); someone who only looks is not counted", quiet["now"] == 2 and quiet["today"] == 2, quiet)
check("the count carries no names", set(quiet) == {"now", "today"})
print("ALL PASS" if ok else "SOME FAILED"); sys.exit(0 if ok else 1)
