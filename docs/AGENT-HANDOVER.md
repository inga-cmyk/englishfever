# Handover: the grammar practice app (practice.englishfever.com)

For another AI agent who continues the work, and for checking afterwards what that agent added or changed.
Written 4 November 2026, updated the same day after twins batch 3 and the first learning tasks. The owner is Inga, an English teacher (her account in the app is "Fox"; "Inga" in the app is a student).
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
| Drafts waiting for Inga's review (NOT packaged) | `docs/task-drafts/pending/` (empty now: everything she saw is approved and published) |
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

## 4. Where the work stands, and what is open

**Latest zip 2026-11-05 22:04** (Duolingo-like buttons, research without a consent card, fun line under the feedback, ChatGPT's reported-task fixes, seven B2 instructions without tense names; before that 2026-11-04 23:02: all 58 rule cards in the new layout). **Done and published (zip 2026-11-04 08:52):** twins batches 1–3 (76 + 50 + 33 tasks; every topic-level with fewer than
10 check / use tasks now has 10, except C1 topics whose two levels together already have 10 or more); the C1 topic
*Unreal time and preferences* (12 tasks, rule card, path step); learning drag tasks `learn-drag-3.csv` (33) and `learn-drag-4.csv`
(40): every topic-level has at least one drag task. Each batch has a `*-review.md` next to its CSV and a generator in `_src/`.

**Templates to copy:** `_src/twins_3.py` for check / use tasks (sources linked with `src_built` / `src_csv`, one twin per source,
checks for grammar terms and word counts, a review with the original next to each twin); `_src/learn_drag_4.py` for learning
tasks (`learning_task()` marks them *practice only*).

**Open, in the order Inga is likely to want them (propose before starting; she decides):**
1. *Learning drag tasks for every path step* (her "option B"): about five per step. **The source is always a check / use task that is not a drag task** (a choice, a typed gap, a rewrite), and the learning task turns its sentence into a word order or a word bank. Never copy an existing word order, word bank or matching task: same sentence + same type = the same task. Same process as `learn_drag_4.py`; every learning task must import as **new** (the last rules in `ITEM-WRITING-RULES.md`).
2. *Twins where tasks repeat most*: needs the Usage → Repeats table from the server (ask Inga for a screenshot or export; never log in yourself).
3. `tools/small_banks.py` does not map some short topic names to their skill ids (found in the batch-2 review); `twins_3.py` has a correct `ALIASES` map to reuse.
4. Done 5 November (ChatGPT): *What does it / this / that say / mean?* is a learn task.
10. 74 built-in explanations use *past participle / infinitive / gerund*; the rule cards say *3rd form / base form*. Ask Inga whether to make them the same.
11. The path and the session summary are English only (Latvian learners see English there): a full Latvian version only if Inga asks.
5. Inga's review lists still open: `docs/task-drafts/task-roles-review.md` (236 learn tasks) and `docs/task-drafts/write-tasks-rewrite-review.md` (40 writing tasks).
6. My learning path: the empty circles of steps not started. Proposal waiting for her choice: D = a green ring for progress, a grey ✓ for "probably known", a green ✓ / ★ when learned / mastered.
7. The optional AI check of writing (`AiGrader.php`, model `claude-haiku-5-5`): a dry run with `tools/ai_dryrun.php` needs `ANTHROPIC_API_KEY` set by Inga in the cloud environment settings and an answers export from her.
8. Later (only when she asks): A2.2 tasks for past perfect, might, second conditional, reported speech, relative clauses; about 50 topics from the test-english.com lists not yet in the app (`docs/LEVEL-LISTS-test-english.md`); a held-out set of level-test tasks for the pre / post test; the language experiment.
9. WordPress plugin 1.8.5 (Grammar practice in the Tutor menu with Tutor's `edit-2` icon): Inga uploads it and checks that the icon shows; change the icon name in `ef-practice-sso.php` if she prefers another (`book`, `lesson`, `feather`, `font`).

**Rule cards:** every card is in `app/authoring/cards2_*.py` (one style: a form table, exactly three typical mistakes, two or three "When we use it" blocks, one to three "Watch out" points, EN and LV in the same structure). A new topic's card follows `cards2_h.py`. Show EN and LV phone screenshots to Inga before packaging.

**How a batch of tasks is made and approved:**
1. Write the generator in `docs/task-drafts/_src/`, ending with `save("pending/<name>.csv")` and a review file `pending/<name>-review.md` (task, answer, wrong options or words, EN and LV explanation, the source task).
2. Checks: `php tools/check_draft.php docs/task-drafts/pending/<name>.csv` (0 refused, twice), `python3 tools/option_audit.py …` (read every flag), the writing-rules and Latvian tests on `pending/` (sed the glob in `app/tests/draft_rules_test.py` and `app/tests/latvian_lint.py` to `"pending", "*.csv"` in a temporary copy), and an import next to every published CSV that must report only new tasks (no "Already added").
3. Latvian words that the italics marking takes for English (*sekas, mums, rakstura…*) go into `LV_BY_FILE["<name>.csv"]` in `_src/lib.py`; the English tense names (*Past Simple*) are the correct Latvian terms.
4. Show the review to Inga. Reviews by other agents are welcome, but weigh each point against the rules: take the sound ones, say briefly why you do not take the others.
5. After her OK: save to `docs/task-drafts/<name>.csv` (no `pending/`), move the review next to it, add lines to `CHANGELOG-practice-app.md` and `RESEARCH-DATA-PLAN.md`, run the full test suite, package, give her the zip link and the reminder *Prepared questions → Add all → Approve all*.

Correcting a task that is already on the server: built-in tasks with `report_fix(base_id, **changes)` in `app/authoring/content_review.py` (a new `-rN` version; update the expected count in `app/tests/bank_update_test.php`); prepared drafts by changing the generator and adding `replaces("old correct option / sentence / task text")` after the row, so the import retires the old one (it may change the task type).

## Working with Inga (what she expects)
- She writes in Latvian, often briefly ("A, apstiprinu, iedod zip"). Answer in Latvian: what was done, the test results, what is in the zip, what waits for her. Tables are welcome; no filler.
- She approves content herself. Nothing goes into `docs/task-drafts/*.csv` (and so into the zip) before her OK.
- Every zip answer gives the version (from the package output), the link `https://github.com/inga-cmyk/englishfever/raw/claude/intelligent-albattani-2e9bfi/dist/practice-app-update.zip` and what to do after uploading.
- Say proactively how a change affects her research data.
- She remembers past corrections and expects them never to come back: read the dated sections of `ITEM-WRITING-RULES.md` before writing anything.

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
