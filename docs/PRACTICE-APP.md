# English Fever Practice – tenses A2.1 to B1.2

A small web app for adult learners to practise active and passive tenses. It lives in `app/`, separate from WordPress, and runs on your Hostinger Cloud plan (PHP + MySQL).

## What it does

**Learners**
- **Registered students** (Tutor LMS users) continue with their englishfever.com account in one click: no second registration, no new password. On the first visit they confirm how their name is shown (their real name or a nickname). Their results are saved.
- **Guests** can start with one click (an optional name field; without a name they appear as "Guest 4821"). No password, no registration. You see them in the teacher list, marked *guest*. Their results stay in that browser and are lost if it is cleared. After practice, a popup invites them to create a free account. When they register and press "Continue with my account" in the same browser, everything they did as a guest moves into the new account. Guests are not on the leaderboard. Guest data is deleted after 60 days without a visit.
- **Option 1 – placement test:** 24 adaptive questions, then a level estimate, the 3 tenses to start with, and a "Practise" button for each.
- **Option 2 – choose:** pick one tense or several, and a level (A2.1, A2.2, B1.1, B1.2).
- **Practice:** the first 3 tasks are a quick check at the chosen level. After that, the tasks get harder after correct answers and easier after mistakes, and the learner is told which way the next task goes.
- **Feedback after every answer:** right or wrong, the correct answer, a one-sentence reason, a specific tip for common mistakes, and a collapsible rule card.
- **Bloom's levels are built in, not a separate section.** Every tense and level has tasks at all six levels: Remember (recognise the form), Understand (explain use), Apply (gap fill, rewrite), Analyse (find the mistake), Evaluate (judge the best answer), Create (write a sentence, checked for the key grammar). The engine mixes them in each session.
- Time practised (today, total), daily streak, XP, weekly and all-time leaderboard (registered learners only; the shown name is their choice, opt-out in Profile), progress per tense and per thinking level.

**Teachers** (you and your colleague)
- Student list: level estimate, last active, minutes this week, tasks, accuracy, streak, XP. Sortable and searchable.
- Student page: 30-day activity, thinking-level accuracy, per-tense level and accuracy, placement result, last 60 answers with what the student typed.
- See guests and registered students in one list (guests are marked). A student's password is managed on englishfever.com, not in the app.
- Export all answers as CSV.

**Content now:** 13 skills (8 active, 5 passive), 241 tasks. Counts per level: A2.1 29, A2.2 56, B1.1 78, B1.2 78. Every tense and level has all six thinking levels.

| Active | Passive |
|---|---|
| Present simple, present continuous, past simple (incl. *used to*), past continuous (incl. *was going to*), present perfect, present perfect continuous, past perfect, future (*will*, *going to*, present continuous, *be about to*) | Present simple, past simple, present continuous, present perfect, future (*will be done*) |

## What is not done yet (please read)

- **B2.1 and B2.2 are not in the pilot.** Past perfect continuous, future continuous and perfect, past continuous and past perfect passive, mixed conditionals and reported speech belong there.
- **A2.1 has the fewest tasks** (4 tenses). More A2.1 and A2.2 items would make the placement more precise for beginners.
- **The question bank needs a teacher's review before learners use it.** Open `docs/practice-question-bank-review.csv` in a spreadsheet. Check the task, the answer, the wrong options and the explanation; write `ok` or `change` in the last columns. Wrong grammar feedback in a grammar app costs trust. Plan about 15–25 hours for the first pass.
- **"Create" tasks check key patterns, not meaning.** A sentence passes if it contains the target structure (for example *have/has been + -ing*). It can pass a sentence that is odd in meaning and can fail a correct sentence written in an unexpected way. The model answer is always shown. A deeper check with an AI model could be added later.
- **Tested here with:** PHP 8.3 on SQLite and on MariaDB 10.11 (including strict `ONLY_FULL_GROUP_BY` mode), a real browser (Chromium: desktop, phone width, dark mode), simulated learners, 30 API and login-handoff checks. **Not tested on a live Hostinger account or on your live WordPress site.** The plugin passed a syntax check and the token format is tested from the app side, but it has not run inside WordPress. Expect a small fix or two on first deployment.
- The leaderboard rewards points, which rise with practice. It is a motivation tool, not a measure of level.

## Setting it up on Hostinger Cloud

Build the files first (or use the ones in `dist/`):

```
python3 tools/package_practice_app.py
```

This makes `dist/practice-app.zip` (the app) and `dist/ef-practice-sso.zip` (the WordPress plugin). Menu names in hPanel change from time to time; the steps below describe what to do, not exact button labels.

### 1. Subdomain (or a folder)
**Folder option (what this install uses):** upload into `public_html/practice` so the app is at `https://englishfever.com/practice/`. Then do **not** make a WordPress page whose address is `/practice/`; name that page `practice-login`. Use `https://englishfever.com/practice` (no slash at the end) as `EF_PRACTICE_URL`.

**Subdomain option:** hPanel → Domains → Subdomains → create `practice` under englishfever.com. Note the folder it creates (for example `public_html/practice`). Turn on the free SSL certificate for it (hPanel → Security → SSL).

### 2. PHP
For the subdomain, pick PHP 8.1 or newer. The default extensions include `pdo_mysql`.

### 3. Database
hPanel → Databases → MySQL Databases → create a database and a user, and write down the database name, user and password. The app creates its own tables the first time it runs.

### 4. Upload
File Manager → open the subdomain folder → upload `practice-app.zip` → Extract. Check that `index.html`, `api.php` and the folders `assets`, `src`, `config`, `content`, `var` are directly inside the subdomain folder.

### 5. Configure
In `config/`, copy `config.sample.php` to `config.php` and edit it:
- `mysql` → host (usually `localhost`), database name, user, password
- `sso_secret` → 64 random hex characters. Make one at any password generator, or run `php -r "echo bin2hex(random_bytes(32));"` over SSH. Keep a copy: the WordPress side needs the same value.
- `wp_login_url` → the address of the WordPress page with the practice button (step 7)
- `privacy_url` → your privacy policy page
- `register_url` → optional, where people without a website account register (shown under the sign-in button), e.g. `https://englishfever.com/en/register/`
- `contact_email` → optional, shown in the footer

### 6. Check that private files are private
Open these in a browser. All must show "403 Forbidden" or "Not found", **not** file contents:
- `https://practice.englishfever.com/content/items.json` (contains the answers)
- `https://practice.englishfever.com/config/config.php`
- `https://practice.englishfever.com/src/Engine.php`

If any of them shows content, stop and tell me. The `.htaccess` files in those folders should block them (Hostinger uses LiteSpeed, which reads `.htaccess`).

Then open the app's address. You should see the welcome page. Start as a guest with a test nickname and do one task.

### 7. Website login (Tutor LMS users)
1. WordPress → Plugins → Add New → Upload → `ef-practice-sso.zip` → Activate.
2. Add to `wp-config.php`, above "That's all, stop editing!":
   ```php
   define( 'EF_PRACTICE_URL',    'https://practice.englishfever.com' );
   define( 'EF_PRACTICE_SECRET', 'the same 64 hex characters as sso_secret' );
   ```
3. Create a page `practice-login` with the shortcode `[ef_practice_button label="Start practising"]`. This page is only a bridge; learners never need to visit it. In the app's `config.php` set `'wp_login_url' => 'https://englishfever.com/practice-login/?ef_practice=go'`, so the app's "Sign in with englishfever.com" button goes straight through: logged-in users enter the app at once, others are sent to the login page.
   Optional: to use your own login page instead of `wp-login.php`, add `define( 'EF_PRACTICE_LOGIN_URL', 'https://englishfever.com/your-login-page/' );` to `wp-config.php`.
4. Test with a student account: click the button → you land in the app, confirm the name (real name or nickname), done. The second time, you go straight in.

What the website shares with the app: the WordPress user ID, display name, and whether the user is a teacher. No email, no password. The link works once and expires after 2 minutes.

**Who becomes a teacher:** WordPress administrators and Tutor LMS instructors, automatically, each time they sign in through the website. So you and your colleague need nothing else if your colleague has the instructor role.

### 8. Tell learners
Give learners the app's address (`https://practice.englishfever.com`) for your menu or the course, not the bridge page. Learners who are not registered can start as guests on the app's own page and are invited to register.

## Teacher guide

- **Students** page: click a column title to sort; click a name for details. A level estimate (≈ B1.1) appears after 5 tasks. It is an estimate, not a grade.
- Guests appear with a *guest* label. They have no password; if a guest loses their browser data, they start from zero. The **Export** file has an `account` column (guest or registered).
- **Export** gives every answer as CSV (time, student, tense, level, thinking level, answer, correct or not, seconds).
- Teachers can try the practice tasks too. Teachers are not shown on the leaderboard and do not appear in the student list.

## Draft text for your privacy policy

Adapt this and have it checked by whoever advises you on GDPR. It is not legal advice.

> **Practice app (practice.englishfever.com)**
> **What we collect.** If you sign in with your englishfever.com account: your account number and the name on your account (teachers see it) and the name you choose to show to other learners. If you use the app as a guest: only the name you type, if you type one. For everyone: your answers, scores, the tenses and levels you practise, the time you spend in the app, your daily streak, and the date you last visited.
> **Why.** To give you practice that fits your level, to show you your progress, and to let your teacher follow your learning and help you. If you choose to appear on the leaderboard, other learners see your nickname, points and minutes. You can switch this off in your profile at any time.
> **Legal basis.** Providing the course you signed up for (contract); our legitimate interest in running and improving the practice; the leaderboard is optional and based on your choice.
> **Activity in your account.** If you have an englishfever.com account, the time you spend in the practice app and the number of tasks per day also appear in your “My activity” page and to your teachers, like your other learning activity. You can turn this off at any time; then the app stops recording your practice time and the practice entries are deleted.
> **Who sees it.** Your teachers at English Fever. Our hosting provider (Hostinger) stores the data for us. We do not use advertising, analytics or tracking services, and the app loads no third-party fonts or scripts.
> **Cookies.** One cookie, `efp`, keeps you signed in. It is strictly necessary and does not track you.
> **How long.** Registered learners: until you delete your results, or [24] months after your last visit. Guests: 60 days after the last visit.
> **Your rights.** In your profile you can download your data and delete your account and all your results. You can also contact us at [email] to ask for access, correction or deletion, or to complain to the Data State Inspectorate (Datu valsts inspekcija).

## Practice time and results on the website ("My activity")

Needs plugin **ef-practice-sso 1.1.0 or newer**.

**What it does**
- A registered student's practice time is added to the existing tracker. The app sends one total per student per day. The plugin saves it in `wp_ef_aktivitate` as a row with `object_type='practice'`, `event='view'`, `course_id=0`, a `visit_key` made from the student and the day (so one row per day, updated rather than duplicated) and a label such as *Grammar practice (app): 24 tasks*. It then counts in **Time learning**, **Days active**, the streak and the calendar, and it is covered by the tracker's 12-month clean-up. It does not appear in the teacher's per-course time or in the lessons list.
- **Consent is respected.** The plugin calls `ef_priv_activity_allowed()` before every write. If the student chose "Atsakos", nothing is saved, the app is told, and the app stops recording that student's practice *time* (answers and results are still saved, because they are the learning results). When a student opts out, their practice rows in the tracker are deleted at once. Time the app had already recorded stays in the app until the student uses *Delete my results* in their profile. If an opted-out student opts in again, only the time after that is sent, never the time from before.
- Nothing is saved for administrators, Tutor instructors (the tracker ignores them too) or guests.
- **Results card:** the shortcode `[ef_practice_results]` shows the logged-in student's practice results (level estimate, accuracy, tasks, streak, time, the tenses worth practising next) and a button into the app. Use `[ef_practice_results plain="1"]` inside another card.
- **Teachers:** the app's teacher page shows a small status line "Website activity tracker: connected, last sent …" or the last error.

**Setup (after the app and plugin are installed)**
1. Upload `ef-practice-sso.zip` (Plugins → Add New → Upload → Replace current with uploaded).
2. App `config/config.php`: add `'wp_sync_url' => 'https://englishfever.com/wp-json/ef-practice/v1/activity',` (it is in `config.sample.php`).
3. Show the results card on the student Home: in the snippet "My activity on student Home", right after `echo $report;` add
   ```php
   if ( shortcode_exists( 'ef_practice_results' ) ) { echo do_shortcode( '[ef_practice_results plain="1"]' ); }
   ```
   and, if you like, put `[ef_practice_results]` below `[ef_my_activity]` on the "My activity" page.
4. Update the consent text in the "Optional activity consent" snippet and raise its `notice_version`. Suggested Latvian sentence (please have it checked): *"Mācību aktivitāšu uzskaitē tiek iekļauts arī laiks un dienas, kad izmantojat gramatikas prakses lietotni (practice.englishfever.com). Ja atsakāties no papildu mācību datu sniegšanas, lietotne jauno laiku neuzskaita, un jūsu prakses ieraksti sadaļā “Mācību aktivitātes” tiek dzēsti."*
5. Optional but recommended: a cron job every 15 minutes (hPanel → Advanced → Cron Jobs): `/usr/bin/php /home/USERNAME/domains/englishfever.com/public_html/practice/bin/sync-wp.php`. The app already sends while students practise; the cron job only makes sure the last minutes of a session are not left waiting. The exact path is shown in File Manager.
6. Check the tracker's clean-up job: it should delete old rows by date only. If it filters by `object_type`, practice rows would stay longer than 12 months.
7. The website's time zone (Settings → General) should be Europe/Riga, the same as the app, so a practice day and a tracker day are the same day.

**If the status line shows a problem:** the text is the website's answer. `403` means the secrets differ (compare `EF_PRACTICE_SECRET` and `sso_secret`) or the server clock is off by more than 2 minutes. `503 tracker snippets are not active` means the tracker snippets are switched off. A connection error usually means the address in `wp_sync_url` is wrong or a security plugin blocks the REST API for this address.

**Testing against a real WordPress.** `app/tests/wp_integration_test.py` runs the whole chain (plugin login, practice, tracker rows, opt-out, outage, results card) against a real WordPress with stand-ins for the two snippets. It needs a WordPress site with the plugin active and two test students; see the header of the file for the variables.

## Maintenance

**Add or fix questions.** Edit the files in `app/authoring/` (`content_*.py`), then:
```
python3 app/authoring/build.py              # checks everything, rewrites content/*.json and the review spreadsheet
php app/tests/grader_test.php               # every task accepts its own answers and rejects its wrong options
python3 tools/package_practice_app.py       # makes the upload files
```
Upload `practice-app.zip` over the old files (keep your `config/config.php`; the zip does not contain one). Learners' data lives in the database and is not touched.

**Add a tense or a level (for example B2).** Add the skill to `app/authoring/rules.py` (label, voice, levels, rule card), add the new levels to `LEVELS` in `app/authoring/dsl.py`, and extend the level boundaries in `Content::levelFromTheta` in `app/src/Content.php` (B2.1 and B2.2 already have a difficulty base there but no boundary yet), write items with all six thinking levels (the build refuses a skill level that misses one), and package.

**Backups.** Use hPanel's backups for the database, or phpMyAdmin → Export. Do this before each update.

**Tests you can run locally** (PHP 8 and Python 3):
```
cd app && php -S 127.0.0.1:8099 -t .         # the app on your computer, SQLite database
python3 app/tests/sim.py                      # simulated learners, placement and practice
python3 app/tests/sso_test.py                 # guests, website login, guest-to-account merge, teacher access, purge (delete app/var/ef.sqlite* before re-running)
```

**Security notes.** Answers are checked on the server and never sent to the browser. The app stores no passwords: registered students sign in with a signed, single-use link from englishfever.com that expires after 2 minutes; guests have no password. Guest creation is limited to 100 per hour per connection. All requests that change data need a custom header, and cookies are `HttpOnly`, `SameSite=Lax` and `Secure` on HTTPS. If the secret in `config.php` leaks, make a new one in both places.
