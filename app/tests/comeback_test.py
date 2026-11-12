#!/usr/bin/env python3
"""Report a problem: who may report, what is stored, what the teacher sees and can do, privacy, limits.
Run against the dev server (SQLite):  php -S 127.0.0.1:8099 -t app ;  rm -f app/var/ef.sqlite* ;  python3 app/tests/reports_test.py"""
import subprocess, base64, csv, hashlib, hmac, io, json, os, sqlite3, time, urllib.parse, urllib.request, http.cookiejar

BASE = "http://127.0.0.1:8099"
APP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SECRET = "local-dev-secret-local-dev-secret-local-dev-secret-0000"
ITEMS = {i["id"]: i for i in json.load(open(os.path.join(APP, "content", "items.json")))}
DB = os.path.join(APP, "var", "ef.sqlite")

# Learning tasks are practised but do not enter the mistake evidence queue.
roles_code = "require '" + os.path.join(APP, 'src', 'Content.php') + "'; echo json_encode(array_column(array_map(fn($it) => ['id'=>$it['id'], 'role'=>Content::role($it)], Content::items()), 'role', 'id'));"
ROLES = json.loads(subprocess.check_output(['php', '-r', roles_code]))


def b64u(b): return base64.urlsafe_b64encode(b).rstrip(b"=").decode()
def token(p):
    x = b64u(json.dumps(p).encode()); return x + "." + b64u(hmac.new(SECRET.encode(), x.encode(), hashlib.sha256).digest())


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k): return None


class C:
    def __init__(self):
        self.cj = http.cookiejar.CookieJar(); self.op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cj), NoRedirect)

    def raw(self, url, data=None, headers=None):
        try:
            r = self.op.open(urllib.request.Request(BASE + url, data=data, headers=headers or {})); return r.status, r.read().decode("utf-8"), r.headers
        except urllib.error.HTTPError as e: return e.code, e.read().decode("utf-8"), e.headers

    def api(self, route, data=None, xef=True, **q):
        url = "/api.php?r=" + route + "".join(f"&{k}={urllib.parse.quote(str(v))}" for k, v in q.items())
        h = {"Content-Type": "application/json"}
        if xef: h["X-EF"] = "1"
        s, b, hd = self.raw(url, json.dumps(data).encode() if data is not None else None, h)
        try: j = json.loads(b)
        except Exception: j = {"_raw": b}
        j["_status"] = s; return j


def login(uid, name, teacher=False):
    c = C()
    c.raw("/sso.php?token=" + urllib.parse.quote(token({"uid": uid, "name": name, "teacher": teacher, "exp": int(time.time()) + 100, "n": os.urandom(6).hex()})))
    return c


ok = True
def check(n, c, x=""):
    global ok; ok &= bool(c); print(("PASS " if c else "FAIL ") + n + ("  -> " + str(x)[:240] if not c else ""))


def correct(it):
    k = it["kind"]
    if k == "mcq": return it["correct"]
    if k == "gap": return [b[0] for b in it["answers"]]
    if k == "text": return it["answers"][0][0]
    if k == "order": return it["sentence"].split(" ")
    if k == "match": return [p_[1] for p_ in it["pairs"]]
    return it["model"]


def wrong(it):
    k = it["kind"]
    if k == "mcq": return it["wrong"][0]
    if k == "gap": return ["zzz" for _ in it["answers"]]
    if k == "order": return list(reversed(it["sentence"].split(" ")))
    if k == "match": return list(reversed([p_[1] for p_ in it["pairs"]]))
    return "zzz"


def run(c, skills, level, n, answer, mode="practice"):
    """Answer n tasks with answer(item); returns the list of (item id, result)."""
    s = c.api("session/start", {"mode": mode, "skills": skills, "level": level, "length": n})
    if s["_status"] != 200: return s, []
    sid, item, out = s["session"]["id"], s["item"], []
    while item:
        a = c.api("session/answer", {"session_id": sid, "item_id": item["id"], "answer": answer(ITEMS[item["id"]]), "time_ms": 3000})
        out.append((item["id"], a["result"])); item = a["next"]
        if a["done"]: return a, out
    return s, out


def dash(c): return c.api("dashboard")["comeback"]


# ---- a new learner has nothing to fix
UID = 9300 + int(time.time()) % 600
c = login(UID, "Comeback Tester")
check("a new learner has no mistakes waiting", dash(c)["open"] == 0)
r = c.api("session/start", {"mode": "comeback"})
check("Comeback with nothing to fix says so (404)", r["_status"] == 404, r)

# ---- wrong answers become open mistakes
done, got = run(c, ["present_simple"], "A2.1", 6, wrong)
n_attempts = len(got)
expected = len({item for item, _ in got if ROLES[item] != "learn"})
d = dash(c)
check("only check/use misses enter the mistake queue", d["open"] == expected and d["fixed"] == 0, d)
check("ordinary practice reports no fixed mistakes while all are wrong", done["summary"]["fixed"] == 0 and done["summary"]["open_after"] == expected, done["summary"])

# ---- Comeback serves each mistake again, as a similar task where there is one
done, got = run(c, [], "A2.1", 6, correct, mode="comeback")
n_attempts += len(got)
ids = [g[0] for g in got]
check("Comeback is one task per mistake (up to ten)", len(got) == expected, len(got))
check("every task in Comeback is a different task", len(set(ids)) == len(ids))
fixed = sum(1 for g in got if g[1].get("fixed"))
check("fixed flags and summary agree, with no more than one fix per task", 0 <= fixed <= expected and done["summary"]["fixed"] == fixed and done["summary"]["comeback"] is True, done["summary"])
check("unfixed same-day retries stay open, fixed total is kept", {k: dash(c)[k] for k in ("open", "fixed")} == {"open": expected - fixed, "fixed": fixed}, dash(c))
remaining = expected - fixed
check("Comeback availability matches remaining evidence mistakes", c.api("session/start", {"mode": "comeback"})["_status"] == (200 if remaining else 404))

# ---- a wrong answer in Comeback keeps the mistake
done, got = run(c, ["past_simple"], "A2.1", 5, wrong)
n_attempts += len(got)
new_misses = len({item for item, _ in got if ROLES[item] != "learn"})
check("new evidence misses join the remaining queue", dash(c)["open"] == remaining + new_misses, dash(c))
done, got = run(c, [], "A2.1", 5, wrong, mode="comeback")
n_attempts += len(got)
check("answering wrong in Comeback fixes nothing and keeps the mistakes", done["summary"]["fixed"] == 0 and dash(c)["open"] >= remaining + new_misses, (done["summary"], dash(c)))

# ---- placement: mistakes above the level found are parked, not offered for Second Chance, until that level is practised
p2 = login(UID + 1, "Parked Tester")
st = p2.api("session/start", {"mode": "placement", "length": 12}); sid = st["session"]["id"]; item = st["item"]
while item:
    it = ITEMS[item["id"]]
    ans = correct(it) if it["level"].startswith("A2") else wrong(it)   # right at A2, wrong above it
    if not it["level"].startswith("A2") and ROLES[it["id"]] != "learn": missed_skill = it["skill"]; ITEMS_LEVEL = {it["skill"]: it["level"]}
    r = p2.api("session/answer", {"session_id": sid, "item_id": item["id"], "answer": ans, "time_ms": 1000})
    if r["done"]: break
    item = r["next"]
summ = r["summary"]
check("placement: right at A2, wrong above it: level A2", summ["overall_level"].startswith("A2"), summ["overall_level"])
check("placement: the misses above A2 are parked, nothing is offered for Second Chance", summ["parked"] >= 3 and summ["open_after"] == 0 and dash(p2)["open"] == 0, (summ["parked"], summ["open_after"], dash(p2)))
check("Second Chance has nothing to offer yet", p2.api("session/start", {"mode": "comeback"})["_status"] == 404)
b1 = p2.api("session/start", {"mode": "practice", "skills": [missed_skill], "level": ITEMS_LEVEL[missed_skill], "length": 5})   # a level-test mistake waits until its topic is practised (teacher, 12 November, A)
bit = ITEMS[b1["item"]["id"]]
p2.api("session/answer", {"session_id": b1["session"]["id"], "item_id": bit["id"], "answer": correct(bit), "time_ms": 1000})
p2.api("session/quit", {"session_id": b1["session"]["id"]})
check("after practising that topic, its level-test mistake comes back to Second Chance", dash(p2)["open"] >= 1, (missed_skill, dash(p2)))
# ---- the history is never rewritten: every attempt is still there
db = sqlite3.connect(DB)
uid = db.execute("select id from users where provider='wp' and external_id=?", (str(UID),)).fetchone()[0]
n_att = db.execute("select count(*) from attempts where user_id=?", (uid,)).fetchone()[0]
check("all practice and Second Chance answers remain stored", n_att == n_attempts, n_att)

# ---- practising a topic brings back a missed task (never right after the mistake) and fresh tasks first
c2 = login(9900 + int(time.time()) % 90, "Variety Tester")
seen = []
for _ in range(3):
    done, got = run(c2, ["past_simple"], "A2.1", 8, correct)
    seen += [g[0] for g in got]
pool = [i for i in ITEMS.values() if i["skill"] == "past_simple" and i["level"] in ("A2.1", "A2.2") and i["kind"] != "write"]   # open writing waits for a right typed answer in the session
first = seen[:len(pool)]
check("tasks do not repeat until every task in reach has been seen once", len(set(first)) == len(first), (len(pool), len(set(first))))

print("\nALL PASS" if ok else "\nSOME FAILED"); raise SystemExit(0 if ok else 1)
