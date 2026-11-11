# Handover: the grammar practice app (practice.englishfever.com)

For another AI agent who continues the work, and for checking afterwards what that agent added or changed.
Written 4 November 2026, last updated 11 November 2026 (after the word-bank audit, zip 2026-11-08 17:31, uploaded by Inga). The owner is Inga, an English teacher (her account in the app is "Fox"; "Inga" in the app is a student).
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
| Drafts waiting for Inga's review (NOT packaged) | `docs/task-drafts/pending/` (only `learn-drag-4-fix-draft.md`, already applied) |
| Overlays that keep later fixes when the draft generators run again (applied in `_src/lib.py` `save()`, in this order) | `_src/term_free*.py` (no grammar terms in instructions), `screenshot_fixes.py` + `_20261107.json`, `learner_fixes.py` + `_20261108.json`, `bank_fixes.py` + `bank_fixes_20261108.json` (word-bank options). Each fix matches a row by type, task and answer; a new task text also sets `replaces` (column 9) to the old text |
| WordPress plugin (sign-in from englishfever.com, My activity, dashboard menu item) | `app/wp-plugin/ef-practice-sso/ef-practice-sso.php` (now 1.8.5) |
| Tests | `app/tests/` (PHP and Python), browser tests `app/tests/browser/` |
| Packaging | `tools/package_practice_app.py` → `dist/practice-app-update.zip` (Inga uploads it), `dist/practice-app.zip` (first install), `dist/ef-practice-sso.zip` (plugin) |
| Checking a draft file | `tools/check_draft.php FILE.csv`, `tools/option_audit.py [FILE.csv]`; small banks: `tools/small_banks.py` |
| Documentation | `docs/`: `ITEM-WRITING-RULES.md` (how tasks must be written: read first), `LEVEL-LISTS-test-english.md` (the order of the path), `RESEARCH-DATA-PLAN.md`, `CHANGELOG-practice-app.md`, `LEARNING-PATH.md`, `NEXT-SESSION.md`, `PRACTICE-APP.md` (setup), `UPLOAD-STEPS.md` |

## 2. Rules that are not negotiable

- A **Claude Code session that Inga starts on `claude/intelligent-albattani-2e9bfi`** develops and pushes on that branch. **Any other agent** (ChatGPT, Codex) works on a new branch made from it (see *How to hand the work back*). Never push to `live`, never force-push.
- **Never touch WordPress or Hostinger** (no logins, no uploads, no settings). Never deploy: Inga uploads the zip and the plugin herself.
- Never ask for, print or store the Anthropic API key or any password. The key lives in the server's `config.php` (`ai_key`), which Inga sets.
- No GitHub comments, issues or closing anything without Inga's OK. No pull request unless she asks for one.
- Learners' names are never stored in research data; never guess who an account belongs to.
- Inga reads in **Latvian**: reply to her in Latvian. Code, comments and commit messages in English. No double dash in her documents. Her `.docx` files are never committed.
- **Propose variants before changing anything she has not asked for, and show drafted tasks before adding them.**
- In Latvian texts say *izglītojamie*, never *skolēni*. Inga's account *Fox* is a teacher account (teachers do not see the welcome popup).
- The fun / feedback lines under an answer are English only.

## 3. How tasks are written (summary; the full list is `docs/ITEM-WRITING-RULES.md`)

- Exactly one answer fits the instruction and the context. In *Which sentence has a mistake?* the other options are correct; in a form task the wrong options are ungrammatical; where a tense mix could be right (mixed conditionals), give the situation that rules it out.
- Options: about the same length, all on one theme or each on its own theme, never one odd one out; no near-identical pair in *NOT correct* tasks; four different sentences there. Use "—" for "no article / no preposition".
- No open gap that several words fit (*___ you help me?*: can / could / will / would). Then use a choice or accept every correct word. Say what to change when several corrections are possible (*Correct the sentence. Keep "will"*, *Remove one unnecessary word*). Two gaps: *Write one word in each gap*.
- No grammar terms in task **instructions** (also not *the correct preposition*); explanations (*Why*), answer notes and rule cards **keep** the grammar terms; *Make a question with What*, *Make a yes/no question*. No speaker tag after a quote when the sentence already names the speaker. Writing tasks never give the answer away.
- When the context allows a second correct form, accept it and give it its own note (*answer notes* column, `answer :: EN :: LV || …`; the learner sees *Also possible:*). Never show *Correct* with the explanation of another form.
- Sentence starts and examples never contain the answer. In matching, no two pairs whose meanings could be swapped.
- **Word banks (8 November):** one word or word group per chip; the wrong chips build **real forms** that do not fit this sentence (*We ___ ___ this car since 2018* → have · had · were · having). No *We has / We is*, no forms that do not exist (*is get, wills, had went*), no bare *-ing* without a helping word, no word of another kind (*bore, rarity*). Check that no other combination of chips gives a correct sentence; where another tense would also fit, add a time word. Gaps after a fixed helping word (*has ___*, *must ___*) keep form options.
- Answer keys list the contractions the checker cannot work out (*'d*, *'s*: *If I'd known…, I'd have…*). The checker already accepts *n't = not*, *can't = cannot*, curly apostrophes, commas and the final full stop. Alternative word orders with swapped people are accepted.
- The level fits the skill: basic *unless*, *wish* + past, *apologise for* are B1–B2; at C1 use *But for*, *Had it not been for*, inversion, *It's high time*, *I'd rather you*, *wish … could have*.
- Settings: travel, work, hobbies, lifestyle, learning, relationships, technologies; current events only at B2/C1. Grammar decisions are checked against Murphy (*English Grammar in Use*). New topics follow what test-english.com teaches at that level (Inga sends screenshots: the site blocks automated access; do not try to get round it), with our own sentences.
- A Latvian explanation for every task up to B1.2 (we write one for all); a Latvian note on a typical mistake only where Latvian causes it, starting *Tulkojot burtiski…*. Learners never see error-type names.
- Task roles (`Content::role`): *learn* (matching, "Which sentence means…", practice-only) is never evidence; *check* depends on the form; *use* = the learner writes. A topic needs 10 different check / use tasks at a level before it can count as learned.

## 4. Where the work stands, and what is open

**Latest zip 2026-11-08 17:31, uploaded by Inga on 11 November.** It contains, after the 5 November zip: *My level* from the last 60 answers; first visit (level question → test sizes or *Skip the test*); level test starting at the learner's own level and asking typed forms first; My learning path alternating a review and the next step (R → U → A); welcome-back popup; research with everyone in (opt-out button under *Your data → Research*); no grammar terms in any task instruction (3 batches); answer notes; 41 typed B2/C1 tasks; ChatGPT's two commits of 7 and 8 November (phone summaries without *Skills check*, Second Chance headlines, *Also possible* for typed alternatives, 27 reported tasks, issues #44–#81); the learning drag task *We ___ ___ this car since 2018*; the word-bank audit (`docs/task-drafts/bank-options-batch1..4-review.md`, 242 tasks; three tasks had marked correct English wrong: *Coffee grows*, *Two windows broke*, the *Mr Ozols … invoices* task). Every change is in `docs/CHANGELOG-practice-app.md`.

**Zip link** (the `github.com/.../raw/...` link sometimes times out; this one works): `https://raw.githubusercontent.com/inga-cmyk/englishfever/claude/intelligent-albattani-2e9bfi/dist/practice-app-update.zip`

**FIRST TASK of the next session (Inga, 11 November): a critical evaluation, before any new work.** Look at everything built so far as an outside expert would, write the findings down, and propose improvements; change nothing until Inga has chosen. Three parts:

1. **The tasks, by role and level.** Every role we tried to cover: *learn* (matching, *Which sentence means…*, learning drag tasks, practice only), *check* (choices, word banks, typed gaps), *use* (rewrites, writing), the level test, the quick check, Second Chance, the review mixes and the *Tricky ones*. For each: does the task really do the job of its role (does a *check* task show that the learner knows the form, or can it be guessed; does a *learn* task teach; does a *use* task make the learner produce the form)? Is it on the right **CEFR level** (grammar and vocabulary of the sentence, not only the topic; compare with `docs/LEVEL-LISTS-test-english.md`, Murphy, the English Grammar Profile / CEFR descriptors)? Is there exactly one correct answer, or are second correct forms accepted with a note? Quality of the sentences: natural, adult, varied settings, no repetition. Work by sampling every topic-level (built-in `app/content/items.json` and `docs/task-drafts/*.csv`), plus scripts for what can be counted (level spread per topic, roles per level, repeated sentences, length and vocabulary level per CEFR level). Give concrete examples and numbers, not impressions.
2. **The interface, seen by a new learner (an adult Latvian learner of English, on a phone).** Go through the first visit step by step with the browser tests' tools (Playwright, phone size; screenshots for Inga at deviceScaleFactor 2): level question, level test, result, first practice, feedback, summary, Home, My learning path, return visit. Note everything that can slow down, confuse or discourage a new user, and above all: **what keeps a new user from getting immediate proof that the app is useful to them** (in the first 2–5 minutes: do they see what they already know, what they learnt, and what the next step brings?).
3. **The positive feedback loop.** What else is needed so the app starts a loop in which the learner gets confirmation of learning and progress and wants to come back (visible progress after every session, mastered topics, before / after on the same skill, streaks and the leaderboard used gently, the welcome-back message, a reason to return tomorrow). Tie it to Inga's research on **engagement** (`docs/RESEARCH-DATA-PLAN.md`: confident learners, return visits, session length) and say how each proposal would show in the data.

**Output:** a report in Latvian for Inga (`docs/REVIEW-2026-11.md`, and a page she can open: publish it as an Artifact) with, per part: what works, what is weak (with examples), and proposals ranked by benefit and effort, each with variants where there is a choice. Then wait for her to choose.

**Open, proposed to Inga on 11 November (she has not chosen yet):**
1. **5 matching tasks whose meanings could be swapped**: b1-tenses-2 line 26, b1-tenses-1 line 67, b1-passives lines 106 and 172, a2-big line 124. Draft new pairs in `pending/`, show them, then add with the `match` replacement (`_src/replaced_match.json`).
2. **Research export**: done on 11 November (`unfair_wrong` column in answers.csv, `Research::unfairWrong`); in zip 2026-11-11 07:23, not uploaded yet.
3. **GitHub issues #44–#82** are fixed in the uploaded zip but still open; close them with a short comment only after Inga's OK.
4. After her upload *Prepared questions* showed **1 new in b1-tenses-2.csv** (2829 already there). A replay of every past zip on a clean database gives 0 new, so the row is missing or retired only on the server: ask her for the task text after *Add all*.
5. **9 new reports of 11 November** (ppc-B11-5a-r2, var-pp-b11-match-01, var-fu-a22-bank-01-r2, c-3118 *Madrid*, fu-B11-5a-r3, c-0409 *the shopping*, c-0037 *should we leave*, pa-A21-5a-r2, var-pc-a21-order-01): proposals given to Inga, nothing changed yet. For item 1 she chose to see the five matching tasks first and decide which to rewrite or drop.

**Older open items (only when she asks):** learning drag tasks for every path step (*option B*: the source is always a check / use task that is not a drag task; never copy an existing order / bank / match); twins where tasks repeat most (needs her Usage → Repeats screenshot); `tools/small_banks.py` short-name map; 74 built-in explanations with *past participle / infinitive / gerund* vs *3rd form / base form* on the cards; Latvian path and summary; her review lists `task-roles-review.md` and `write-tasks-rewrite-review.md`; path circles proposal D; AI check of writing dry run (`tools/ai_dryrun.php`, the key is set by Inga in the environment settings, never asked in chat); A2.2 tasks and the missing test-english.com topics; WordPress plugin 1.8.5 icon.

**Templates to copy:** `_src/twins_3.py` for check / use tasks, `_src/learn_drag_4.py` for learning tasks (`learning_task()` marks them *practice only*), `_src/bank_fixes.py` for changing published draft rows without touching their generators.

**Rule cards:** every card is in `app/authoring/cards2_*.py` (one style: a form table, exactly three typical mistakes, two or three "When we use it" blocks, one to three "Watch out" points, EN and LV in the same structure). A new topic's card follows `cards2_h.py`. Show EN and LV phone screenshots to Inga before packaging.

**How a batch of tasks is made and approved:**
1. Write the generator in `docs/task-drafts/_src/`, ending with `save("pending/<name>.csv")` and a review file `pending/<name>-review.md` (task, answer, wrong options or words, EN and LV explanation, the source task).
2. Checks: `php tools/check_draft.php docs/task-drafts/pending/<name>.csv` (0 refused, twice), `python3 tools/option_audit.py …` (read every flag), the writing-rules and Latvian tests on `pending/` (sed the glob in `app/tests/draft_rules_test.py` and `app/tests/latvian_lint.py` to `"pending", "*.csv"` in a temporary copy), and an import next to every published CSV that must report only new tasks (no "Already added").
3. Latvian words that the italics marking takes for English (*sekas, mums, rakstura…*) go into `LV_BY_FILE["<name>.csv"]` in `_src/lib.py`; the English tense names (*Past Simple*) are the correct Latvian terms.
4. Show the review to Inga. Reviews by other agents are welcome, but weigh each point against the rules: take the sound ones, say briefly why you do not take the others.
5. After her OK: save to `docs/task-drafts/<name>.csv` (no `pending/`), move the review next to it, add lines to `CHANGELOG-practice-app.md` and `RESEARCH-DATA-PLAN.md`, run the full test suite, package, give her the zip link and the reminder *Prepared questions → Add all → Approve all*.

Correcting a task that is already on the server: built-in tasks with `report_fix(base_id, **changes)` in `app/authoring/content_review.py` (a new `-rN` version; update the expected retired count in `app/tests/bank_update_test.php`, now 337); `var-*` tasks in `content_variety.py` by renaming the id to the next `-rN` in place; prepared drafts by changing the generator and adding `replaces("old correct option / sentence / task text")` after the row, so the import retires the old one (it may change the task type).

## Working with Inga (what she expects)
- She writes in Latvian, often briefly ("A, apstiprinu, iedod zip"). Answer in Latvian: what was done, the test results, what is in the zip, what waits for her. Tables are welcome; no filler.
- She approves content herself. Nothing goes into `docs/task-drafts/*.csv` (and so into the zip) before her OK.
- Every zip answer gives the version (from the package output), the link (above), what is inside, and *Prepared questions → Add all → Approve all*.
- Say proactively how a change affects her research data.
- She remembers past corrections and expects them never to come back: read the dated sections of `ITEM-WRITING-RULES.md` before writing anything.

## 5. Build, test, package

```
python3 app/authoring/build.py                 # after any change in app/authoring
bash app/tests/browser/run_all.sh 2>&1 | tee /tmp/run_all.log   # everything, ~15 min; each line must end ALL PASS / OK / no errors
python3 tools/package_practice_app.py          # do not pipe into head (it stops the packaging); builds and tests the bank, then writes dist/*.zip with a version stamp (Riga time)
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
