#!/usr/bin/env python3
"""App <-> real WordPress: login through the plugin, practice time into the tracker table, consent, summary card.

Needs (see docs/PRACTICE-APP.md, "Testing against a real WordPress"): a WordPress with the plugin active and stand-in
tracker/consent snippets (mu-plugin), the app on APP_URL using SQLite and the same secret, and:
    WP_URL (default http://127.0.0.1:8200)   APP_URL (default http://127.0.0.1:8099)
    WP_CLI  (command that runs wp-cli for that site)   MYSQL_DB (database of that WordPress, read with the mysql command)
"""
import hashlib, hmac, json, os, re, subprocess, sys, time, urllib.parse, urllib.request, http.cookiejar

WP = os.environ.get("WP_URL", "http://127.0.0.1:8200")
APP = os.environ.get("APP_URL", "http://127.0.0.1:8099")
WPCLI = os.environ["WP_CLI"].split()
DB = os.environ.get("MYSQL_DB", "wptest")
SECRET = "local-dev-secret-local-dev-secret-local-dev-secret-0000"
ITEMS = {i["id"]: i for i in json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "items.json")))}
KEY = hmac.new(SECRET.encode(), b"ef-tracker-v1", hashlib.sha256).hexdigest()
APPDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k): return None


class Br:
    """A browser: its own cookies, optional redirect following."""
    def __init__(self):
        self.cj = http.cookiejar.CookieJar()
        self.op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cj), NoRedirect)

    def req(self, url, data=None, headers=None, method=None):
        r = urllib.request.Request(url, data=data, headers=headers or {}, method=method)
        try:
            x = self.op.open(r); return x.status, x.read().decode(), x.headers
        except urllib.error.HTTPError as e:
            return e.code, e.read().decode(), e.headers

    def api(self, route, data=None, **q):
        url = APP + "/api.php?r=" + route + "".join(f"&{k}={v}" for k, v in q.items())
        s, b, _ = self.req(url, json.dumps(data).encode() if data is not None else None, {"X-EF": "1", "Content-Type": "application/json"})
        j = json.loads(b); j["_status"] = s; return j


def wp_login(user):
    b = Br()
    b.req(WP + "/wp-login.php")  # test cookie
    body = urllib.parse.urlencode({"log": user, "pwd": "pass1234", "wp-submit": "Log In", "testcookie": "1"}).encode()
    b.cj.set_cookie(http.cookiejar.Cookie(0, "wordpress_test_cookie", "WP Cookie check", None, False, "127.0.0.1", False, False, "/", True, False, None, False, None, None, {}))
    s, _, h = b.req(WP + "/wp-login.php", body, {"Content-Type": "application/x-www-form-urlencoded"})
    assert s == 302, f"wp login failed for {user}: {s}"
    return b


def via_plugin(wp_browser, app_browser):
    """Click the bridge link while logged in to WordPress, then follow it into the app."""
    s, _, h = wp_browser.req(WP + "/?ef_practice=go")
    loc = h.get("Location") or ""
    assert s == 302 and "sso.php?token=" in loc, (s, loc)
    s2, _, h2 = app_browser.req(loc)
    return s2, h2.get("Location")


def sql(q):
    out = subprocess.run(["mysql", DB, "-N", "-B", "-e", q], capture_output=True, text=True, check=True).stdout.strip()
    return [l.split("\t") for l in out.split("\n")] if out else []


def wpcli(*a):
    return subprocess.run(WPCLI + list(a), capture_output=True, text=True).stdout.strip()


def uid_of(login): return int(wpcli("user", "get", login, "--field=ID"))


def practise(app, n=6, skills=("present_simple",), level="A2.1"):
    r = app.api("session/start", {"mode": "practice", "skills": list(skills), "level": level, "length": n})
    item = r["item"]; sid = r["session"]["id"]
    while True:
        it = ITEMS[item["id"]]
        ans = it["correct"] if it["kind"] == "mcq" else ([b[0] for b in it["answers"]] if it["kind"] == "gap" else (it["answers"][0][0] if it["kind"] == "text" else (it["sentence"].split(" ") if it["kind"] == "order" else ([p[1] for p in it["pairs"]] if it["kind"] == "match" else it["model"]))))
        a = app.api("session/answer", {"session_id": sid, "item_id": it["id"], "answer": ans, "time_ms": 4000})
        if a.get("done") or not a.get("next"): return
        item = a["next"]


def signed_post(payload, tamper=False, old=False):
    body = json.dumps(payload); t = str(int(time.time()) - (500 if old else 0))
    sig = hmac.new(KEY.encode(), (t + "." + body).encode(), hashlib.sha256).hexdigest()
    if tamper: body = body.replace("seconds", "secondz")
    s, b, _ = Br().req(WP + "/wp-json/ef-practice/v1/activity", body.encode(), {"Content-Type": "application/json", "X-EF-Time": t, "X-EF-Sign": sig})
    return s, json.loads(b)


ok = True
def check(name, cond, extra=""):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name + ("  -> " + str(extra) if extra and not cond else ""))


# the app and the real site both count days in Riga time; make the stand-in WordPress do the same
# (otherwise the two disagree about the date between 21:00 and 24:00 UTC)
wpcli("option", "update", "timezone_string", "Europe/Riga")
today = wpcli("eval", "echo current_time('Y-m-d');")
maria = uid_of("maria"); optout = uid_of("optout")

# 1. login through the plugin
wpb = wp_login("maria"); app = Br()
st, loc = via_plugin(wpb, app)
check("plugin link signs the student into the app", st == 302 and "#/home" in (loc or ""), (st, loc))
me = app.api("me")["user"]
check("registered student, name suggested from the website, track_time on", me["provider"] == "wp" and me["nickname"].startswith("Maria") and "Test" not in me["nickname"] and me["track_time"] is True and not me["nick_set"], me)
check("name can be confirmed", app.api("account/profile", {"nickname": "Maria T", "show_on_board": True})["user"]["nick_set"])

# 1b. the two link kinds, the banner and the button
wpcli("post", "create", "--post_type=page", "--post_title=Banner", "--post_name=banner", "--post_status=publish",
      "--post_content=[ef_practice_banner lang=\"en\"] [ef_practice_banner lang=\"lv\"] [ef_practice_banner title=\"Own title\" text=\"Own text\" button=\"Own button\"] [ef_practice_button]")
anon = Br()
s1, _, h1 = anon.req(WP + "/?ef_practice=open")
check("visitor + open link: straight to the app's welcome page (guests can start)", s1 == 302 and (h1.get("Location") or "").rstrip("/") == APP.rstrip("/"), (s1, h1.get("Location")))
s2, _, h2 = anon.req(WP + "/?ef_practice=go")
check("visitor + go link: website login first, then back", s2 == 302 and "dashboard-login" in (h2.get("Location") or "") and "redirect_to=" in (h2.get("Location") or ""), (s2, h2.get("Location")))
s3, _, h3 = wpb.req(WP + "/?ef_practice=open")
check("logged-in student + open link: signed in and sent to the app", s3 == 302 and "sso.php?token=" in (h3.get("Location") or ""), (s3, h3.get("Location")))
page = anon.req(WP + "/banner/")[1]
check("English banner", "Practise English grammar" in page and "No registration needed" in page and "Free · A2.1 – C1" in page)
check("Latvian banner", "Trenējiet angļu valodas gramatiku" in page and "Sākt praksi" in page)
check("banner texts can be changed", "Own title" in page and "Own text" in page and "Own button" in page)
check("banner and button use the guest-friendly link", page.count("ef_practice=open") >= 4 and "ef_practice=go" not in page, page.count("ef_practice=open"))
check("banner is in the brand colours", "#020101" in page and "#D82C5E" in page and "#DEC17A" in page)
check("config offers the website link back", Br().api("config").get("site_url"), "")

# 2. practice -> tracker row
app.api("heartbeat", {"seconds": 15})
practise(app, 6)
time.sleep(1.5)
rows = sql(f"SELECT object_type,event,course_id,active_seconds,label,visit_key,DATE(started_at) FROM wp_ef_aktivitate WHERE user_id={maria}")
check("one practice row for today", len(rows) == 1 and rows[0][0] == "practice" and rows[0][1] == "view" and rows[0][2] == "0", rows)
check("row has seconds > 0 so the day counts, label shows tasks, visit_key is 32 hex", rows and int(rows[0][3]) >= 15 and "6 tasks" in rows[0][4] and re.fullmatch(r"[0-9a-f]{32}", rows[0][5]), rows)
check("started_at is today", rows and rows[0][6] == today, rows)
t1 = int(rows[0][3])
practise(app, 5); time.sleep(1.5)
rows = sql(f"SELECT COUNT(*), MAX(active_seconds), MAX(label) FROM wp_ef_aktivitate WHERE user_id={maria}")[0]
check("still one row per day, updated not duplicated", rows[0] == "1" and int(rows[1]) >= t1 and "11 tasks" in rows[2], rows)

# the tracker's own numbers (as described: time = SUM(active_seconds) of 'view' rows; active day = DATE(started_at) with seconds > 0)
tsum = int(sql(f"SELECT COALESCE(SUM(active_seconds),0) FROM wp_ef_aktivitate WHERE user_id={maria} AND event='view'")[0][0])
days = sql(f"SELECT COUNT(DISTINCT DATE(started_at)) FROM wp_ef_aktivitate WHERE user_id={maria} AND (event<>'view' OR active_seconds>0)")[0][0]
check("practice counts in Time learning and Days active", tsum >= 15 and days == "1", (tsum, days))

# 3. the signed endpoint: bad signature, old request, admins/unknown users, consent
s, j = signed_post({"user": maria, "days": [{"day": today, "seconds": 99, "answers": 1}]}, tamper=True)
check("tampered request refused", s == 403, (s, j))
s, j = signed_post({"user": maria, "days": [{"day": today, "seconds": 99, "answers": 1}]}, old=True)
check("old request refused", s == 403, (s, j))
s, j = Br().req(WP + "/wp-json/ef-practice/v1/activity", b"{}", {"Content-Type": "application/json"})[:2]
check("unsigned request refused", s == 403, s)
s, j = signed_post({"user": 1, "days": [{"day": today, "seconds": 600, "answers": 9}]})
check("administrator is skipped", s == 200 and j["results"][today] == "skipped" and not sql("SELECT 1 FROM wp_ef_aktivitate WHERE user_id=1"), (s, j))
s, j = signed_post({"user": 99999, "days": [{"day": today, "seconds": 600, "answers": 9}]})
check("unknown user is skipped", s == 200 and j["results"][today] == "skipped", (s, j))
s, j = signed_post({"user": maria, "days": [{"day": "not-a-date", "seconds": 5, "answers": 1}]})
check("bad day ignored", s == 200 and j["results"] in ([], {}), (s, j))

# 4. results card on the website
html = wpb.req(WP + "/results/")[1]
check("[ef_practice_results] shows the student's results", "Grammar practice" in html and "Level estimate" in html and "Tasks done" in html and ">11<" in html.replace(" ", ""), re.sub(r"<[^>]+>", " ", html)[-300:])
check("results card has the practise button through the bridge", "ef_practice=open" in html)
check("logged-out visitor sees nothing", "ef-practice-results" not in Br().req(WP + "/results/")[1])
wpcli("post", "create", "--post_type=page", "--post_title=Plain card", "--post_name=plain-card", "--post_status=publish", "--post_content=[ef_practice_results plain=\"1\"]")
plain = wpb.req(WP + "/plain-card/")[1]
check("plain option renders without its own card border", "Level estimate" in plain and "border-radius:16px;padding:24px" not in plain.replace(" ", "") and "border-top:1px solid" in plain, "")
bob = wp_login("optout")
html2 = bob.req(WP + "/results/")[1]
check("student without practice sees the start invitation", "have not practised yet" in html2, "")

# 5. opting out: rows deleted, app stops recording time
wpcli("user", "meta", "update", "maria", "ef_priv_activity_choice", "no")
check("opting out deletes the practice rows", sql(f"SELECT COUNT(*) FROM wp_ef_aktivitate WHERE user_id={maria} AND object_type='practice'")[0][0] == "0")
app.api("heartbeat", {"seconds": 15}); practise(app, 5); time.sleep(1.5)
check("no new rows after opting out", sql(f"SELECT COUNT(*) FROM wp_ef_aktivitate WHERE user_id={maria}")[0][0] == "0")
me = app.api("me")["user"]
check("the app learned about the opt-out from the website's answer", me["track_time"] is False, me)
before = app.api("dashboard")["today"]["seconds"]
app.api("heartbeat", {"seconds": 15}); time.sleep(0.5)
check("the app no longer records time", app.api("dashboard")["today"]["seconds"] == before)
check("answers and results are still saved", app.api("dashboard")["totals"]["answers"] >= 16)

# 6. opting in again: nothing from before is sent
seconds_before_yes = app.api("dashboard")["today"]["seconds"]
wpcli("user", "meta", "update", "maria", "ef_priv_activity_choice", "yes")
wpb2 = wp_login("maria"); via_plugin(wpb2, app)
check("track_time back on after a new login", app.api("me")["user"]["track_time"] is True)
app.api("heartbeat", {"seconds": 15}); time.sleep(1.5)
practise(app, 5); time.sleep(1.5)
rows = sql(f"SELECT active_seconds, label FROM wp_ef_aktivitate WHERE user_id={maria}")
total_app = app.api("dashboard")["today"]["seconds"]
after_yes = total_app - seconds_before_yes   # time recorded since opting in again
check("only time after opting in again is sent (30 s minimum for an active day, nothing from before)", len(rows) == 1 and int(rows[0][0]) <= max(30, after_yes + 1), (rows, total_app, seconds_before_yes))

# 7. teacher status + the website being down must not break practice
teacher = wp_login("admin"); tapp = Br(); via_plugin(teacher, tapp)
tm = tapp.api("me")["user"]
check("administrator becomes teacher in the app", tm["role"] == "teacher", tm)
stt = tapp.api("teacher/sync-status")
check("teacher sees a working link", stt["configured"] and stt["last_ok"] > 0 and not stt["last_error"], stt)
def app_sql(q):
    """Run SQL on the app's own database: SQLite by default, or MySQL/MariaDB if APP_MYSQL_DB is set."""
    if os.environ.get("APP_MYSQL_DB"):
        subprocess.run(["mysql", os.environ["APP_MYSQL_DB"], "-e", q], check=True)
    else:
        import sqlite3
        con = sqlite3.connect(os.path.join(APPDIR, "var", "ef.sqlite")); con.execute(q); con.commit(); con.close()


app_sql(f"DELETE FROM sync_wp WHERE user_id IN (SELECT id FROM users WHERE external_id='{maria}')")
cfg_path = os.path.join(APPDIR, "config", "config.php"); cfg = open(cfg_path).read()
open(cfg_path, "w").write(cfg.replace("127.0.0.1:8200/wp-json", "127.0.0.1:9/wp-json"))   # nothing listens on port 9
time.sleep(3)  # PHP's opcache re-reads a changed file after up to 2 seconds
try:
    s_ = app.api("heartbeat", {"seconds": 15}); practise(app, 5); time.sleep(2)
    check("practice works while the website is unreachable", app.api("dashboard")["totals"]["answers"] > 20)
    stt = tapp.api("teacher/sync-status")
    check("teacher sees the problem and who is waiting", bool(stt["last_error"]) and stt["students_waiting"] >= 1, stt)
finally:
    open(cfg_path, "w").write(cfg)
    time.sleep(3)
r = subprocess.run(["php", os.path.join(APPDIR, "bin", "sync-wp.php")], capture_output=True, text=True, cwd=APPDIR)
check("cron script catches up", "sent: 1" in r.stdout and r.returncode == 0, (r.stdout, r.stderr))
stt = tapp.api("teacher/sync-status")
check("status clean again", stt["last_error"] is None and stt["students_waiting"] == 0, stt)
check("tracker has exactly one practice row for the student", sql(f"SELECT COUNT(*) FROM wp_ef_aktivitate WHERE user_id={maria} AND object_type='practice'")[0][0] == "1")

# 8. guests are never sent
g = Br(); g.api("guest", {"t": 5000, "nickname": "Gast"}); g.api("heartbeat", {"seconds": 15}); practise(g, 4); time.sleep(1)
check("guests produce no tracker rows", sql("SELECT COUNT(*) FROM wp_ef_aktivitate WHERE label LIKE 'Grammar practice%'")[0][0] == "1")

# 8b. guest -> registers on the website -> straight back into the app, results moved
wpcli("user", "delete", "newbie", "--yes")
guest = Br(); guest.api("guest", {"nickname": "Soon registered", "t": 5000}); guest.api("account/profile", {"avatar": "leaf-gold"}); practise(guest, 5); time.sleep(1)
before = guest.api("dashboard")["totals"]
s_, _, h_ = guest.req(APP + "/register.php")
check("register.php: marker set and sent to the registration form", s_ == 302 and "ef_return" in " ".join(v for k, v in h_.items() if k.lower() == "set-cookie"), (s_, h_.get("Location")))
wpcli("user", "create", "newbie", "newbie@example.com", "--role=subscriber", "--user_pass=pass1234", "--display_name=New Bie")
# the registration form leaves the new user on some page of the website, logged in; the marker travels with the browser
guest.req(WP + "/wp-login.php")
guest.cj.set_cookie(http.cookiejar.Cookie(0, "wordpress_test_cookie", "WP Cookie check", None, False, "127.0.0.1", False, False, "/", True, False, None, False, None, None, {}))
guest.req(WP + "/wp-login.php", urllib.parse.urlencode({"log": "newbie", "pwd": "pass1234", "wp-submit": "Log In", "testcookie": "1"}).encode(), {"Content-Type": "application/x-www-form-urlencoded"})
s1, _, h1 = guest.req(WP + "/results/")
check("after registering, any page sends them back into the app", s1 == 302 and "ef_practice=open" in (h1.get("Location") or ""), (s1, h1.get("Location")))
s2, _, h2 = guest.req(urllib.parse.urljoin(WP + "/results/", h1.get("Location")))
check("...and the app signs them in", s2 == 302 and "sso.php?token=" in (h2.get("Location") or ""), (s2, h2.get("Location")))
guest.req(h2.get("Location"))
me = guest.api("me")
check("the guest is now a registered student, with a welcome message", me["user"]["provider"] == "wp" and me.get("welcome") and me["welcome"]["answers"] == before["answers"], me)
check("the welcome message is shown only once", guest.api("me").get("welcome") is None)
after = guest.api("dashboard")["totals"]
check("all guest results are in the new account", after["answers"] == before["answers"] and after["xp"] == before["xp"], (before, after))
check("the guest's avatar came along", me["user"]["avatar"] == "leaf-gold", me["user"].get("avatar"))
s3, _, h3 = guest.req(WP + "/results/")
check("the marker is used up (no second redirect)", s3 == 200, s3)

# banner instead of redirect when the automatic return is switched off
wpcli("config", "set", "EF_PRACTICE_AUTO_RETURN", "false", "--raw", "--type=constant"); time.sleep(3)  # opcache re-reads wp-config after up to 2 s
g2 = Br(); g2.api("guest", {"nickname": "Banner path", "t": 5000}); g2.req(APP + "/register.php")
wpcli("user", "delete", "newbie2", "--yes"); wpcli("user", "create", "newbie2", "newbie2@example.com", "--role=subscriber", "--user_pass=pass1234")
g2.req(WP + "/wp-login.php"); g2.cj.set_cookie(http.cookiejar.Cookie(0, "wordpress_test_cookie", "WP Cookie check", None, False, "127.0.0.1", False, False, "/", True, False, None, False, None, None, {}))
g2.req(WP + "/wp-login.php", urllib.parse.urlencode({"log": "newbie2", "pwd": "pass1234", "wp-submit": "Log In", "testcookie": "1"}).encode(), {"Content-Type": "application/x-www-form-urlencoded"})
s4, page4, _ = g2.req(WP + "/results/")
check("auto-return off: a 'Back to your practice' bar is shown instead", s4 == 200 and "Back to your practice" in page4 and "ef_practice=open" in page4, s4)
wpcli("config", "delete", "EF_PRACTICE_AUTO_RETURN", "--type=constant"); time.sleep(3)
# 8b2. "My students": enrolments in the teacher's Tutor courses (Tutor stores them as tutor_enrolled posts), plus marks made by hand
course = wpcli("post", "create", "--post_type=courses", "--post_title=Test course", "--post_status=publish", "--post_author=1", "--porcelain")
other_course = wpcli("post", "create", "--post_type=courses", "--post_title=Someone else's course", "--post_status=publish", "--post_author=" + str(optout), "--porcelain")
wpcli("post", "create", "--post_type=tutor_enrolled", "--post_status=completed", f"--post_parent={course}", f"--post_author={maria}", "--post_title=enrolment 1")
wpcli("post", "create", "--post_type=tutor_enrolled", "--post_status=cancelled", f"--post_parent={course}", f"--post_author={optout}", "--post_title=cancelled enrolment")
wpcli("post", "create", "--post_type=tutor_enrolled", "--post_status=completed", f"--post_parent={other_course}", f"--post_author={uid_of('newbie')}", "--post_title=enrolment elsewhere")
lst = tapp.api("teacher/students")
mine_rows = {x["nickname"]: x["mine"] for x in lst["students"]}
check("roster is known and students of the teacher's courses are marked 'course'", lst["roster_ok"] is True and any(v == "course" for v in mine_rows.values()), mine_rows)
check("a cancelled enrolment and a stranger's course do not count", sum(1 for v in mine_rows.values() if v == "course") == 1, mine_rows)
gm = Br(); gm.api("guest", {"nickname": "Mark me", "t": 5000}); gm_id = gm.api("me")["user"]["id"]
check("the teacher can add a guest to my students", tapp.api("teacher/mine", {"user_id": gm_id, "mine": True})["_status"] == 200)

# 8c. registration with an email confirmation: the person logs in hours later, maybe days later
def set_marker(br, secs_ago):
    br.cj.set_cookie(http.cookiejar.Cookie(0, "ef_return", str(int(time.time()) - secs_ago), None, False, "127.0.0.1", False, False, "/", True, False, None, False, None, None, {}))

def login_into(br, user, pwd="pass1234"):
    br.req(WP + "/wp-login.php")
    br.cj.set_cookie(http.cookiejar.Cookie(0, "wordpress_test_cookie", "WP Cookie check", None, False, "127.0.0.1", False, False, "/", True, False, None, False, None, None, {}))
    br.req(WP + "/wp-login.php", urllib.parse.urlencode({"log": user, "pwd": pwd, "wp-submit": "Log In", "testcookie": "1"}).encode(), {"Content-Type": "application/x-www-form-urlencoded"})

wpcli("user", "delete", "late", "--yes"); wpcli("user", "create", "late", "late@example.com", "--role=subscriber", "--user_pass=pass1234", "--display_name=Late One")
g3 = Br(); g3.api("guest", {"nickname": "Late confirm", "t": 5000}); practise(g3, 3); time.sleep(1)
dflt = g3.api("me")["user"]["avatar"]
g3_id = g3.api("me")["user"]["id"]; tapp.api("teacher/mine", {"user_id": g3_id, "mine": True})   # the teacher already follows this guest
check("without a chosen avatar a guest gets a symbol that stays the same", bool(re.fullmatch(r"(flame|spark|bolt|sun|thermo|wave|comet|leaf)-(raspberry|gold|ink|cream|plum|sand)", dflt or "")) and g3.api("me")["user"]["avatar"] == dflt, dflt)
g3.req(APP + "/register.php")
set_marker(g3, 2 * 3600)
login_into(g3, "late")
s5, page5, h5 = g3.req(WP + "/results/")
check("confirmed hours later: a bar with a way back, no surprise redirect", s5 == 200 and "Back to your practice" in page5 and "ef_practice_dismiss" in page5, (s5, h5.get("Location")))
s6, _, h6 = g3.req(WP + "/results/?ef_practice_dismiss=1")
check("the x forgets the marker and stays on the page", s6 == 302 and "ef_practice_dismiss" not in (h6.get("Location") or "") and "/results/" in (h6.get("Location") or ""), (s6, h6.get("Location")))
s7, page7, _ = g3.req(WP + "/results/")
check("no bar after closing it", s7 == 200 and "Back to your practice" not in page7, s7)
set_marker(g3, 4 * 86400)
s8, page8, _ = g3.req(WP + "/results/")
check("a marker older than 3 days does nothing", s8 == 200 and "Back to your practice" not in page8, s8)
set_marker(g3, 3600)
s9, _, h9 = g3.req(WP + "/results/")
check("...but within the 3 days the bar still shows", s9 == 200, s9)
sA, _, hA = g3.req(WP + "/?ef_practice=open")
sB, _, hB = g3.req(hA.get("Location") or "")   # the app's sso.php signs them in
me3 = g3.api("me")
check("signing in later moves the guest results and keeps the assigned avatar", me3["user"]["provider"] == "wp" and me3.get("welcome") and me3["user"]["avatar"] == dflt, (me3["user"], me3.get("welcome")))
after_merge = {x["id"]: x for x in tapp.api("teacher/students")["students"]}
check("the teacher's mark moved to the new account and the guest row is gone", g3_id not in after_merge and after_merge.get(me3["user"]["id"], {}).get("mine") == "added", after_merge.get(me3["user"]["id"]))
check("teacher and student views show an avatar for everyone", all(r.get("avatar") for r in tapp.api("leaderboard", period="all")["rows"]) if tapp.api("leaderboard", period="all")["rows"] else True)
# administrators are never redirected
adm = wp_login("admin"); adm.cj.set_cookie(http.cookiejar.Cookie(0, "ef_return", str(int(time.time())), None, False, "127.0.0.1", False, False, "/", True, False, None, False, None, None, {}))
check("an administrator with the marker is not redirected", adm.req(WP + "/results/")[0] == 200)

# 8d. phones: the account is created in one browser, the confirmation link opens in ANOTHER one (no cookie there).
# The plugin keeps a note on the account, so the first page after logging in still goes into the app.
wpcli("option", "update", "users_can_register", "1")
wpcli("user", "delete", "crossbrowser", "--yes")
reg = Br(); set_marker(reg, 60)                                 # the browser where "Create account" was pressed
reg.req(WP + "/wp-login.php?action=register")
reg.req(WP + "/wp-login.php?action=register", urllib.parse.urlencode({"user_login": "crossbrowser", "user_email": "crossbrowser@example.com", "wp-submit": "Register",
    "redirect_to": WP + "/practice-login/?ef_practice=go"}).encode(), {"Content-Type": "application/x-www-form-urlencoded"})
cb_id = wpcli("user", "get", "crossbrowser", "--field=ID")
note = wpcli("user", "meta", "get", cb_id, "ef_practice_pending") if cb_id else ""
check("registering from the app leaves a note on the new account", note.isdigit() and abs(int(note) - time.time()) < 120, (cb_id, note))
wpcli("user", "update", cb_id, "--user_pass=pass1234", "--display_name=Cross Browser")
other = Br()                                                     # another browser: no ef_return cookie at all
login_into(other, "crossbrowser")
sC, _, hC = other.req(WP + "/results/")
check("another browser, no cookie: the first page after logging in goes into the app", sC == 302 and "ef_practice=open" in (hC.get("Location") or ""), (sC, hC.get("Location")))
sD, _, hD = other.req(WP + "/?ef_practice=open")
check("...and it reaches the app's sign-in", sD == 302 and "sso.php?token=" in (hD.get("Location") or ""), (sD, hD.get("Location")))
check("the note is gone after that (no second redirect)", wpcli("user", "meta", "get", cb_id, "ef_practice_pending") == "" and other.req(WP + "/results/")[0] == 200)
# later than 24 hours: the bar instead of a redirect; later than 3 days: nothing
wpcli("user", "meta", "update", cb_id, "ef_practice_pending", str(int(time.time()) - 30 * 3600))
sE, pageE, _ = other.req(WP + "/results/")
check("30 hours after registering: a bar with a way back, no redirect", sE == 200 and "Back to your practice" in pageE, sE)
wpcli("user", "meta", "update", cb_id, "ef_practice_pending", str(int(time.time()) - 4 * 86400))
sF, pageF, _ = other.req(WP + "/results/")
check("4 days after registering: nothing", sF == 200 and "Back to your practice" not in pageF, sF)
# a person who did not come from the app gets no note
wpcli("user", "delete", "plainreg", "--yes")
Br().req(WP + "/wp-login.php?action=register", urllib.parse.urlencode({"user_login": "plainreg", "user_email": "plainreg@example.com", "wp-submit": "Register"}).encode(), {"Content-Type": "application/x-www-form-urlencoded"})
pr_id = wpcli("user", "get", "plainreg", "--field=ID")
check("a registration that did not start in the app leaves no note", pr_id.isdigit() and wpcli("user", "meta", "get", pr_id, "ef_practice_pending") == "", pr_id)
wpcli("option", "update", "users_can_register", "0")

# 8e. "Sign in" in the app: the website's login form may ignore redirect_to and show Tutor's dashboard; the next page leads back into the app
wpcli("user", "delete", "signin", "--yes"); wpcli("user", "create", "signin", "signin@example.com", "--role=subscriber", "--user_pass=pass1234", "--display_name=Sign In")
si = Br()
sG, _, hG = si.req(WP + "/?ef_practice=go")
check("Sign in from the app (not logged in): goes to the login form", sG == 302 and "redirect_to=" in (hG.get("Location") or ""), (sG, hG.get("Location")))
check("...and leaves the 'came from the app' marker", any(c.name == "ef_return" for c in si.cj), [c.name for c in si.cj])
login_into(si, "signin")                                          # the login form sends the person nowhere near the app
sH, _, hH = si.req(WP + "/results/")
check("logged in, on Tutor's dashboard: straight on into the app", sH == 302 and "ef_practice=open" in (hH.get("Location") or ""), (sH, hH.get("Location")))
sI, _, hI = si.req(hH.get("Location") or WP + "/?ef_practice=open")
check("...which signs the person in there", sI == 302 and "sso.php?token=" in (hI.get("Location") or ""), (sI, hI.get("Location")))
check("only once: the dashboard works afterwards", si.req(WP + "/results/")[0] != 302)
# somebody who just browses the website and logs in is not sent anywhere
plain = Br(); login_into(plain, "signin")
check("logging in on the website itself (not from the app) does not redirect", plain.req(WP + "/results/")[0] != 302)

# 9. the summary endpoint is private
s, b, _ = Br().req(APP + f"/api.php?r=wp/summary&uid={maria}")
check("summary without a signature refused", s == 403, s)
t = str(int(time.time())); sig = hmac.new(KEY.encode(), (t + f".summary:{maria}").encode(), hashlib.sha256).hexdigest()
s, b, _ = Br().req(APP + f"/api.php?r=wp/summary&uid={maria}", headers={"X-EF-Time": t, "X-EF-Sign": sig})
check("summary with a signature works and only covers that student", s == 200 and json.loads(b)["practice"] is True, (s, b[:80]))
s, b, _ = Br().req(APP + f"/api.php?r=wp/summary&uid={maria+1000}", headers={"X-EF-Time": t, "X-EF-Sign": sig})
check("signature for one student does not open another", s == 403, s)

print("\nALL PASS" if ok else "\nSOME FAILED")
sys.exit(0 if ok else 1)
