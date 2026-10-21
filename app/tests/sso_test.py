#!/usr/bin/env python3
"""Website-login handoff, teacher access and password reset against the dev server (php -S 127.0.0.1:8099 -t app)."""
import base64, hashlib, hmac, json, time, os, urllib.request, urllib.parse, http.cookiejar

BASE = "http://127.0.0.1:8099"
SECRET = "local-dev-secret-local-dev-secret-local-dev-secret-0000"


def b64u(b): return base64.urlsafe_b64encode(b).rstrip(b"=").decode()


def token(payload, secret=SECRET):
    p = b64u(json.dumps(payload).encode())
    return p + "." + b64u(hmac.new(secret.encode(), p.encode(), hashlib.sha256).digest())


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k): return None


class C:
    def __init__(self):
        self.cj = http.cookiejar.CookieJar()
        self.op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cj), NoRedirect)

    def raw(self, url, data=None, headers=None):
        req = urllib.request.Request(BASE + url, data=data, headers=headers or {})
        try:
            r = self.op.open(req); return r.status, r.read().decode(), r.headers
        except urllib.error.HTTPError as e:
            return e.code, e.read().decode(), e.headers

    def api(self, route, data=None, **q):
        url = "/api.php?r=" + route + "".join(f"&{k}={v}" for k, v in q.items())
        s, body, _ = self.raw(url, json.dumps(data).encode() if data is not None else None,
                               {"X-EF": "1", "Content-Type": "application/json"})
        j = json.loads(body); j["_status"] = s; return j


def sso(c, **kw):
    p = {"uid": 777, "name": "Maria Test", "teacher": False, "exp": int(time.time()) + 120, "n": os.urandom(6).hex()}
    p.update(kw)
    return c.raw("/sso.php?token=" + urllib.parse.quote(token(p, kw.get("secret", SECRET)) if "secret" not in kw else token({k: v for k, v in p.items() if k != "secret"}, kw["secret"])))


ok = True
def check(name, cond, extra=""):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name + (" " + str(extra) if extra and not cond else ""))

# 1. valid token -> signed in as a student, asked to choose a nickname
s = C()
st, _, hd = sso(s, uid=777 + int(time.time()) % 1000)
check("valid token redirects to the app", st == 302 and "#/home" in (hd.get("Location") or ""), st)
me = s.api("me")["user"]
check("signed in as student with nick_set false", me and me["role"] == "student" and me["provider"] == "wp" and not me["nick_set"], me)
r = s.api("account/profile", {"nickname": "Maria_W" + str(int(time.time()) % 1000), "show_on_board": True})
check("can choose a nickname", r["_status"] == 200 and r["user"]["nick_set"], r)
check("wp user cannot change a local password", s.api("account/password", {"old": "x", "new": "yyyy"})["_status"] == 400)

# 2. replay, forgery, expiry
n = os.urandom(6).hex()
tk = urllib.parse.quote(token({"uid": 901, "name": "X", "teacher": False, "exp": int(time.time()) + 100, "n": n}))
a = C().raw("/sso.php?token=" + tk); b = C().raw("/sso.php?token=" + tk)
check("token works once", a[0] == 302, a[0]); check("replayed token refused", b[0] == 400, b[0])
check("wrong secret refused", C().raw("/sso.php?token=" + urllib.parse.quote(token({"uid": 902, "exp": int(time.time()) + 100, "n": "zz1"}, "x" * 40)))[0] == 400)
check("expired token refused", C().raw("/sso.php?token=" + urllib.parse.quote(token({"uid": 903, "exp": int(time.time()) - 5, "n": "zz2"})))[0] == 400)
check("far-future token refused", C().raw("/sso.php?token=" + urllib.parse.quote(token({"uid": 904, "exp": int(time.time()) + 99999, "n": "zz3"})))[0] == 400)
check("garbage refused", C().raw("/sso.php?token=abc")[0] == 400)
check("tampered payload refused", C().raw("/sso.php?token=" + urllib.parse.quote(token({"uid": 905, "teacher": False, "exp": int(time.time()) + 100, "n": "zz4"}).replace(".", "x.", 1)))[0] == 400)

# 3. teacher via website (administrator / Tutor instructor)
t = C()
sso(t, uid=1, name="Inga Teacher", teacher=True)
tm = t.api("me")["user"]
check("teacher role from website", tm and tm["role"] == "teacher", tm)
lst = t.api("teacher/students")
check("teacher sees student list", lst["_status"] == 200 and len(lst["students"]) >= 1, lst.get("error"))
sid = lst["students"][0]["id"]
det = t.api("teacher/student", id=sid)
check("teacher sees student detail", det["_status"] == 200 and "dashboard" in det and "recent" in det, det.get("error"))
st_, csv, hd = t.raw("/api.php?r=teacher/export")
check("teacher can export CSV", st_ == 200 and csv.lstrip("﻿").startswith("time,nickname"), st_)
check("teacher not on leaderboard", t.api("leaderboard")["hidden"] is True)
check("student cannot see teacher routes", s.api("teacher/students")["_status"] == 403)
check("student cannot see other students", s.api("teacher/student", id=sid)["_status"] == 403)

# 4. password reset for a local student
c = C()
nick = "reset" + os.urandom(3).hex()
c.api("register", {"nickname": nick, "password": "oldpw"})
uid = c.api("me")["user"]["id"]
rr = t.api("teacher/reset-password", {"user_id": uid})
check("teacher can reset a local password", rr["_status"] == 200 and len(rr["temp_password"]) == 6, rr)
c2 = C()
lg = c2.api("login", {"nickname": nick, "password": rr["temp_password"]})
check("student can sign in with the temporary password and must change it", lg["_status"] == 200 and lg["user"]["must_change"], lg)
check("old password no longer works", C().api("login", {"nickname": nick, "password": "oldpw"})["_status"] == 401)
ch = c2.api("account/password", {"old": rr["temp_password"], "new": "brandnew"})
check("student sets a new password", ch["_status"] == 200)
check("must_change cleared", c2.api("me")["user"]["must_change"] is False)
wpid = [x for x in lst["students"] if x["provider"] == "wp"][0]["id"]
check("cannot reset a website account's password here", t.api("teacher/reset-password", {"user_id": wpid})["_status"] == 400)

# 5. rate limit and CSRF header
bad = C(); nn = "rl" + os.urandom(3).hex(); bad.api("register", {"nickname": nn, "password": "abcd"})
codes = [C().api("login", {"nickname": nn, "password": "wrong"})["_status"] for _ in range(10)]
check("login is rate limited", 429 in codes, codes)
s_, body, _ = C().raw("/api.php?r=logout", b"{}", {"Content-Type": "application/json"})
check("POST without X-EF header refused", s_ == 400, s_)

# 6. data export and delete
d = C(); dn = "del" + os.urandom(3).hex(); d.api("register", {"nickname": dn, "password": "abcd"})
check("export my data", d.api("account/export")["user"]["nickname"] == dn)
check("delete needs the nickname", d.api("account/delete", {"confirm": "nope"})["_status"] == 400)
check("delete works", d.api("account/delete", {"confirm": dn})["_status"] == 200)
check("deleted user cannot sign in", C().api("login", {"nickname": dn, "password": "abcd"})["_status"] == 401)

print("\nALL PASS" if ok else "\nSOME FAILED")
raise SystemExit(0 if ok else 1)
