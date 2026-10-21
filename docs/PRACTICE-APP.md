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
Use the `?ef_practice=open` link from "Making the app easy to find" in your menu, footer and homepage, and the plain app address (`https://practice.englishfever.com`) for social media and e-mails. Learners who are not registered can start as guests on the app's own page and are invited to register.

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

## Spelling and apostrophes

This is a grammar app, so a missing apostrophe or a typo should not look like a grammar mistake, but a real grammar slip must never pass as a typo. The default (`'spelling' => 'forgiving'` in `config.php`):

| Learner writes | Result |
|---|---|
| Capital letters wrong (`they play tennis on sundays`) | Correct. A tip appears for names, days, months and "I": *Capital letter: Sundays.* |
| Missing apostrophe (`dont`, `doesnt`, `isnt`, `im`, `ive`, `youre`) | Correct, with the tip *Use an apostrophe: don't.* Only forms that cannot be anything else are accepted (not `were`, `ill`, `its`, `hes`). |
| One-letter typo **inside** a word of five or more letters that appears in the task (`tenis`, `tenins` for *tennis*) | Correct, with the tip *Spelling: tenis → tennis.* At most two such typos. |
| A typo in a short word, in a word that is not in the task, or at the **end** of a word (`plays` for `play`, `finish`/`finishes`/`finishing` for `finished`, `has` for `had`, `Sunday` for `Sundays`, `tens` for `tennis`) | Not accepted. These are grammar, or a different word. |

Accepted answers get full points and count as correct for the adaptive logic. A test (`app/tests/grader_test.php`) changes the end of every word in every text and gap answer (over a thousand variants) and checks that none is accepted. Writing tasks (Create) accept `im`, `ive` and similar the same way.

To go back to exact matching, set `'spelling' => 'strict'` (capital letters still never matter).

## From guest to registered: the return trip

1. A guest taps **Create a free account** (welcome page, the popup after practice, the banner, the leaderboard note). The link goes through `register.php`, which leaves a 30-minute marker (cookie `ef_return`) and sends them to your registration form (`register_url`).
2. They register on the website as usual.
3. As soon as they are registered and logged in, **plugin 1.3.0 sends them straight back into the app** from whatever page the form leaves them on (the Tutor dashboard, the homepage, anywhere). It does not depend on the form honouring `redirect_to`. Switch this off with `define( 'EF_PRACTICE_AUTO_RETURN', false );` in `wp-config.php`; a "Back to your practice" bar then appears instead.
4. In the app they confirm their name (their real name is suggested, or a nickname), and a **welcome message** says what moved over ("We moved your guest results over: 34 tasks and 312 XP"). The results, streak, level, tenses and the guest's avatar all move to the new account. Nothing is lost.
5. Administrators and instructors are never redirected, and the marker is used up after one return.

**Limits.** The move works when the guest registers in the **same browser** (the app recognises them by its login cookie). Registering on another device starts a fresh account. On an iPhone, an app added to the home screen keeps its own cookies, separate from Safari, so a guest who practised in the home-screen icon but registered in Safari would not be merged (the earlier "sign in with a code" idea would fix this; not built). The marker needs the app and website on the same domain (`practice.englishfever.com` and `englishfever.com`), or the same host, and `site_url` set in `config.php`.

## People who only want to practise grammar

They are first-class users. As a guest they can practise without ever visiting the website. To keep their results they need a website account, because that is the one place passwords and e-mail live, which keeps the app free of passwords. After registering, the return trip above puts them straight back, and they stay signed in for **90 days after their last visit** on that device (the sign-in renews daily). The website is only seen again when they sign in on a new device or after 90 days away; the login page then returns them to the app.

If many learners turn out to want only the app, there are two upgrades: a shorter registration form for people coming from the app, or signing in inside the app with an e-mail code (sent through the website, so the app still stores no passwords). Look at the numbers after the first weeks of testing before building either.

## Avatars

Learners choose an avatar instead of a photo: a symbol (flame, spark, bolt, sun, thermometer, wave, comet, leaf) in one of six colours, in **Profile → Your avatar**, or keep a monogram (their first initial). It shows in the top bar, on the home page, on the leaderboard and in the teacher pages. Guests can choose one too, and it moves with them when they register. There are no uploads, so there is nothing to moderate, no image files to protect and no photos to keep under GDPR. The server only accepts a fixed list of "symbol-colour" values.

## Using it like an app on a phone

The practice app is an **installable web app (PWA)**. Students can put it on the home screen of an iPhone or Android phone: it gets the EF icon, opens full screen without browser bars, and updates the moment you upload a new zip. It costs nothing and needs no app store.

**How a student installs it**
- **iPhone (Safari):** open the practice address → tap **Share** (square with an arrow) → **Add to Home Screen**.
- **Android (Chrome):** open the practice address → tap **Install the app** in the card on the home screen, or the browser menu (⋮) → **Install app** / **Add to Home screen**.
The app shows this hint itself on phones (on the home page, lower down, with "Not now") and always in **Profile**. It is hidden once the app is installed.

**What works offline:** the screens open, but practising needs a connection, so the app says "You are offline" instead of showing a blank page. Answers, results and logins are never stored on the phone by the app's service worker.

**Known limitation on iPhone.** An app added to the iPhone home screen keeps its own sign-in, separate from Safari. A guest is not affected. A registered student who installs the icon may have to tap **Continue with my account** once inside the icon, and on some iPhones the website login that follows may not return to the installed app. If students report this, the fix is a "sign in with a code" (the website shows a short code, the student types it into the app). Test with one iPhone before announcing the install option widely; Android shares the sign-in with Chrome and has no such problem.

**Real store apps (optional, later)**
| | Cost (check current prices) | Effort and caveats |
|---|---|---|
| **Google Play** | one-time developer fee, about US$25 | The same web app packaged for the store (Trusted Web Activity, for example with PWABuilder). A few hours of work. Updates still come from your server. |
| **Apple App Store** | Apple Developer Program, about US$99 per year | Needs a Mac, a native wrapper and an App Review. Apple often rejects apps that are only a website in a frame, so a store version should add something native (for example reminders by notification). Real extra work, so only worth it if you need to be in the store. |
Both would need the same sign-in solution as above. My advice: start with the home-screen install, see how many students use it, and decide about the stores after that.

## Making the app easy to find

**Use one link everywhere:** `https://englishfever.com/practice-login/?ef_practice=open` (any page of your site works as the base; the `practice-login` page is simply a stable one).
- A **logged-in student** who clicks it is signed in automatically and lands in the app.
- A **visitor** who clicks it goes to the app's welcome page, where they can start as a guest or continue with their account. They never meet a login wall.
- The other link, `?ef_practice=go`, always asks for the website login first. The app uses it only behind "Continue with my account".

Needs plugin **1.2.0 or newer**. Where to put it:

| Place | How |
|---|---|
| **Main menu** | Appearance → Menus (or Site Editor → Navigation) → Custom Link. URL as above. Label: *Gramatikas prakse* (Latvian menu) / *Grammar practice* (English menu). With a language plugin, add it to each language's menu. |
| **Homepage** | Add a **Shortcode** block under the top section: `[ef_practice_banner lang="lv"]` on the Latvian page, `[ef_practice_banner lang="en"]` on the English one. It is a black panel with a gold heading and a raspberry button, and it works on phones. Change the wording with `title=""`, `text=""`, `button=""`, `eyebrow=""`. The Latvian text is a draft: please read it. |
| **Footer** | Add a link in the MĀCIES column with the same URL (*Gramatikas prakse*). |
| **Course and lesson pages** | `[ef_practice_button label="Practise tenses"]`. |
| **Student dashboard** | The "Grammar practice" card (`[ef_practice_results]`) already has a button. |
| **Social media, e-mails, QR codes** | `https://practice.englishfever.com` |

Inside the app, the top bar and the footer have a link back to englishfever.com (`site_url` in `config.php`).

If you use a caching plugin (for example LiteSpeed Cache), exclude the query string `ef_practice` from caching (LiteSpeed Cache → Cache → Excludes → Do Not Cache Query Strings).

**Check after adding it:** (1) in a private window the menu link opens the app's welcome page; (2) while logged in as a student the same link lands in the app without a login screen; (3) the banner looks right on a phone.

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

**Security.** See [SECURITY.md](SECURITY.md): what the app protects against, its limits, and a launch checklist. Run `python3 app/tests/security_test.py` after changes (see its header).
