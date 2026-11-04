# Handover: the grammar practice app (practice.englishfever.com)

For another AI agent who continues the work, and for checking afterwards what that agent added or changed.
Written 4 November 2026. The owner is Inga, an English teacher (her account in the app is "Fox"; "Inga" in the app is a student).
The app is part of her master's research, so every change that affects what learners see or how answers are counted is logged
(see *Research* below).

## 1. Where everything is

Repository: `github.com/inga-cmyk/englishfever`, working branch **`claude/intelligent-albattani-2e9bfi`**.
Everything for the grammar practice app is in this repository; nothing lives only on the server except the settings
(`config.php`) and the learners' data.

| What | Where |
|---|---|
| The app (PHP back end, plain JS front end) | `app/` |
| Front end: all screens | `app/assets/app.js`, styles `app/assets/app.css`, small helpers and the avatars `app/assets/ui.js`, drag and drop `app/assets/dnd.js` |
| API entry point | `app/api.php` (routes `?r=...`) |
| Server logic | `app/src/`: `Engine.php` (sessions, task choice, level test), `Path.php` (My learning path, mastery rule), `Content.php` (bank, task roles), `Grader.php` (checking typed answers), `CustomItems.php` (importing teacher / prepared questions), `Stats.php`, `Usage.php`, `Research.php`, `Reports.php`, `Mistakes.php`, `AiGrader.php` (optional AI check of writing) |
| The built-in question bank (source) | `app/authoring/*.py` (topics `content_*.py`, `b1_topics.py`, `cards2_*.py`); corrections of published tasks in `content_review.py` (`report_fix`), choice-option fixes `option_fixes.py`, writing-task fixes `write_fixes.py` |
| The built-in bank (built, used by the app) | `app/content/` (made by `app/authoring/build.py`; do not edit by hand) |
| Prepared questions (imported on the server: Questions → Prepared questions → Add all → Approve all) | `docs/task-drafts/*.csv`, made by the scripts in `docs/task-drafts/_src/*.py` with the helpers in `_src/lib.py` |
| Drafts waiting for Inga's review (NOT packaged) | `docs/task-drafts/pending/` (now: `twins-1.csv` + `twins-1-review.md`, 76 tasks, corrected after her review, still waiting for her OK) |
| WordPress plugin (sign-in from englishfever.com, My activity, dashboard menu item) | `app/wp-plugin/ef-practice-sso/ef-practice-sso.php` (now 1.8.5) |
| Tests | `app/tests/` (PHP and Python), browser tests `app/tests/browser/` |
| Packaging | `tools/package_practice_app.py` → `dist/practice-app-update.zip` (Inga uploads it), `dist/practice-app.zip` (first install), `dist/ef-practice-sso.zip` (plugin) |
| Checking a draft file | `tools/check_draft.php FILE.csv`, `tools/option_audit.py [FILE.csv]`; small banks: `tools/small_banks.py` |
| Documentation | `docs/`: `ITEM-WRITING-RULES.md` (how tasks must be written: read first), `LEVEL-LISTS-test-english.md` (the order of the path), `RESEARCH-DATA-PLAN.md`, `CHANGELOG-practice-app.md`, `LEARNING-PATH.md`, `NEXT-SESSION.md`, `PRACTICE-APP.md` (setup), `UPLOAD-STEPS.md` |

## 2. Rules that are not negotiable

- Work only on a **new branch made from `claude/intelligent-albattani-2e9bfi`** (see *How to hand the work back*). Never push to `live`, never to the working branch itself, never force-push.
- **Never touch WordPress or Hostinger** (no logins, no uploads, no settings). Never deploy: Inga uploads the zip and the plugin herself.
- Never ask for, print or store the Anthropic API key or any password. The key lives in the server's `config.php` (`ai_key`), which Inga sets.
- No GitHub comments, issues or closing anything without Inga's OK. No pull request unless she asks for one.
- Learners' names are never stored in research data; never guess who an account belongs to.
- Inga reads in **Latvian**: reply to her in Latvian. Code, comments and commit messages in English. No double dash in her documents. Her `.docx` files are never committed.
- **Propose variants before changing anything she has not asked for, and show drafted tasks before adding them.**

## 3. How tasks are written (summary; the full list is `docs/ITEM-WRITING-RULES.md`)

- Exactly one answer fits the instruction and the context. In *Which sentence has a mistake?* the other options are correct; in a form task the wrong options are ungrammatical; where a tense mix could be right (mixed conditionals), give the situation that rules it out.
- Options: about the same length, all on one theme or each on its own theme, never one odd one out; no near-identical pair in *NOT correct* tasks; four different sentences there. Use "—" for "no article / no preposition".
- No open gap that several words fit (*___ you help me?*: can / could / will / would). Then use a choice or accept every correct word. Say what to change when several corrections are possible (*Correct the sentence. Keep "will"*, *Remove one unnecessary word*). Two gaps: *Write one word in each gap*.
- No grammar terms in instructions (also not *the correct preposition*); *Make a question with What*, *Make a yes/no question*. No speaker tag after a quote when the sentence already names the speaker. Writing tasks never give the answer away.
- Answer keys list the contractions the checker cannot work out (*'d*, *'s*: *If I'd known…, I'd have…*). The checker already accepts *n't = not*, *can't = cannot*, curly apostrophes, commas and the final full stop. Alternative word orders with swapped people are accepted.
- The level fits the skill: basic *unless*, *wish* + past, *apologise for* are B1–B2; at C1 use *But for*, *Had it not been for*, inversion, *It's high time*, *I'd rather you*, *wish … could have*.
- Settings: travel, work, hobbies, lifestyle, learning, relationships, technologies; current events only at B2/C1. Grammar decisions are checked against Murphy (*English Grammar in Use*). New topics follow what test-english.com teaches at that level (Inga sends screenshots: the site blocks automated access; do not try to get round it), with our own sentences.
- A Latvian explanation for every task up to B1.2 (we write one for all); a Latvian note on a typical mistake only where Latvian causes it, starting *Tulkojot burtiski…*. Learners never see error-type names.
- Task roles (`Content::role`): *learn* (matching, "Which sentence means…", practice-only) is never evidence; *check* depends on the form; *use* = the learner writes. A topic needs 10 different check / use tasks at a level before it can count as learned.

## 4. The open job: twins for small banks (Inga chose option B)

43 topic-levels have fewer than 10 check / use tasks (about 177 tasks missing): `python3 tools/small_banks.py` lists them,
`--tasks` also prints the existing tasks of each one to write twins from. Batch 1 (13 topic-levels,
76 tasks) is in `docs/task-drafts/pending/` and waits for Inga's OK. Next batches: the remaining topic-levels under 10, then the
topics whose tasks repeat most (Usage → Repeats on the server). A twin is very like an existing task (same grammar, same type)
in another setting. Next to every twin, write the original task it copies, so the review can compare them (Inga asked for this).

How to make a batch:
1. Write `docs/task-drafts/_src/twins_N.py` like `twins_1.py` (Topic(...).mcq / gap / bank / text / order with an English and a Latvian explanation each), ending with `save("pending/twins-N.csv")`. Topic names are the ones the existing CSV files use (first column).
2. `cd docs/task-drafts/_src && python3 twins_N.py`
3. `php tools/check_draft.php docs/task-drafts/pending/twins-N.csv` (must say 0 refused twice) and `python3 tools/option_audit.py docs/task-drafts/pending/twins-N.csv` (read every flag).
4. The writing rules test on the pending file: `sed 's#"task-drafts", "\*.csv"#"task-drafts", "pending", "*.csv"#' app/tests/draft_rules_test.py > /tmp/drt.py && cp /tmp/drt.py app/tests/_drt.py && python3 app/tests/_drt.py; rm app/tests/_drt.py`
5. Write `pending/twins-N-review.md` (task, answer, wrong options or words, EN and LV explanation, and the original) for Inga.
6. Only after her OK: move the CSV from `pending/` to `docs/task-drafts/` (it is then packaged and offered under Prepared questions).

Correcting a task that is already on the server: built-in tasks with `report_fix(base_id, **changes)` in `app/authoring/content_review.py` (a new `-rN` version; update the expected count in `app/tests/bank_update_test.php`); prepared drafts by changing the generator and adding `replaces("old correct option / sentence / task text")` after the row, so the import retires the old one.

## 5. Build, test, package

```
python3 app/authoring/build.py                 # after any change in app/authoring
bash app/tests/browser/run_all.sh 2>&1 | tee /tmp/run_all.log   # everything, ~15 min; each line must end ALL PASS / OK / no errors
python3 tools/package_practice_app.py          # builds and tests the bank, then writes dist/*.zip with a version stamp (Riga time)
```
Before packaging: add a line at the top of `docs/CHANGELOG-practice-app.md` (under "Fixes and polish"), and bump `?v=` in
`app/index.html` and `app/assets/app.js` when the front end changed. Commit messages end with the attribution lines the session gives.

## 6. Research: say how a change affects the data

Every change to grading, to which tasks are served, to the path or to the level test gets a dated line in
`docs/RESEARCH-DATA-PLAN.md` → *Changes*, and you tell Inga in one sentence what it means for her data. Display-only changes
need no line, but say so.

## 7. How to hand the work back (so it can be checked)

1. Start: `git fetch origin claude/intelligent-albattani-2e9bfi && git checkout -b agent/<short-name> origin/claude/intelligent-albattani-2e9bfi`
2. Small commits, one subject each, with a clear message. Run the checks above before each push.
3. `git push -u origin agent/<short-name>`; do not merge, do not open a pull request.
4. Leave a short report in `docs/AGENT-REPORT-<short-name>.md`: what was added or changed, which files, which checks ran and their result, what is open.

Checking afterwards (what the reviewer runs):
```
git fetch origin agent/<short-name>
git log --oneline origin/claude/intelligent-albattani-2e9bfi..origin/agent/<short-name>     # the commits
git diff --stat origin/claude/intelligent-albattani-2e9bfi...origin/agent/<short-name>      # the files
git diff origin/claude/intelligent-albattani-2e9bfi...origin/agent/<short-name> -- docs/task-drafts   # the tasks themselves
php tools/check_draft.php <each new or changed CSV>; python3 tools/option_audit.py <same>
bash app/tests/browser/run_all.sh
```
