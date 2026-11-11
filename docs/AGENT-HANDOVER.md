# Handover: the grammar practice app (practice.englishfever.com)

For another AI agent who continues the work, and for checking afterwards what that agent added or changed.
Written 4 November 2026, last updated 11 November 2026 (end of the session: zip 2026-11-11 08:03 is live, stage 2 draft in progress; start at section 4). The owner is Inga, an English teacher (her account in the app is "Fox"; "Inga" in the app is a student).
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

**START HERE (written 11 November, end of the session).** Live on the server: **zip 2026-11-11 08:03** (Inga uploaded it; c-3394 approved). Nothing newer is packaged. The branch is clean and pushed.

**Zip link** (the `github.com/.../raw/...` link sometimes times out; this one works): `https://raw.githubusercontent.com/inga-cmyk/englishfever/claude/intelligent-albattani-2e9bfi/dist/practice-app-update.zip`

**What is live since 08:03:** topic / level / task-kind labels appear only after the answer (S1 A; teachers always see them); the account invitation no longer covers the level test result (S2 A); `unfair_wrong` column in the research export; the task gates in the packaging.

**The quality bar Inga set on 11 November (she was angry about weak drafts; read this twice):** she must not have to correct drafts by hand. You are expected to be the expert in English and in language learning. Before a task goes into a draft, answer: **what must the learner know to get this right?** Not acceptable: a pair matched by a shared word (*twice = two times*); a choice whose wrong options are in another time, so the form need not be known (wrong options must compete: *I'm meeting / I'll meet / I meet*); a long situation before an easy choice; an instruction the learner may not understand (*Report it*); an accepted word order nobody says (*before it gets dark should we leave*); a joining task that is only copying; a disputed phrase (*do the shopping*: change the sentence). Decide yourself and give reasons; bring her only what cannot be decided without her. Keep instructions short. All of this is in `app/tests/bad_examples.json` (`reader` entries) and at the end of `ITEM-WRITING-RULES.md`.

**Her decisions of 11 November (all recorded in `ITEM-WRITING-RULES.md`):**
- A wrong form may be a wrong option when it is a common learner mistake (*womans, childs, didn't used to*); forms nobody writes stay out.
- No speaker tag after a quote in any task; the rule card's example keeps its tag as an exception.
- Reported speech follows the taught rule: after a past reporting verb only the backshifted form is accepted (*liked*, not *like*), the explanation says why (the step back is always correct; Murphy unit 48 allows the present while still true; here we practise the rule). Give a situation that has changed where it is easy (*Ten years ago … Now he drinks it every day*).
- Typed reports give the start, so *said me / told to me* cannot arise: the quote and the start are shown and the learner completes it (*'Do you like jazz?' → He asked me ___.*). *said / told* is tested in separate tasks (six typed ones approved: draft section G).
- *Correct the mistake* tasks: decided by the agent, told to her, no objection yet: accept the whole corrected sentence **or** only the corrected words (96 tasks, a grader change, a dated research line).

**Agreed order of work, one zip per stage:** 0 gates (done) → 1 S1 A and S2 A (done, live) → **2 the draft (in progress, see below)** → 3 what *Learned* and C1 mean: U1, U2, U4, U3 together, one date (she has not chosen the variants) → 4 first five minutes: S3–S9 → 5 loop: C1, C2 → 6 content audits U5, U7, U6 → 7 later: C4–C8, S10, trial period for new tasks. Proposals and variants: `docs/REVIEW-2026-11.md` (page: https://claude.ai/artifact/Y9hD9dtJ4bkGz8VUbQyFJ1).

**Stage 2, exactly where it stands.** The draft is `docs/task-drafts/pending/reports-2026-11-11-draft.md`, sections A–H, reworked after her review. **Nothing of it is in the CSVs, the generators or the bank.** Contents: A reports 1, 4, 5, 6, 7 (nr. 2 `var-pp-b11-match-01`: retire, she did not object); B three rewritten matching tasks, two passive matching tasks to retire (b1-passives lines 106, 172); C two *Make a yes/no question*, one term in an instruction; D 39 reported-speech tasks without a speaker tag (16 choices / gaps, 20 typed ones in the new "complete from the start" form, 3 matching tasks); E decisions; F generated orders removed from keys; G six *said / told* tasks (approved); H four new reports: 15 conditional gaps get a situation sentence, the *Join with…* family, *Correct the mistake*, the *used to* matching task.
Still to do, in this order:
1. Rewrite the 17 *Join with…* tasks at B1 and above in the style of H.2 (list them with `tools/dump_items.php`: `q` starts with *Join with* and the answer adds at most one new word; the 15 at A2.2 stay) and add them to the draft.
2. A new gate: a typed conditional with two gaps and no situation sentence (`cond_second / cond_third / cond_mixed`, kind gap without bank, one sentence) fails; add the old task to `bad_examples.json` with `gate`.
3. Give the whole reworked draft to a **second reader** (a fresh agent; the prompt used on 11 November asked it to break every task: second correct answer, swappable pairs, starts that contradict keys; now add "what must the learner know, and do the wrong options compete?"). The first reading (before the rework) found 22 problems in 45 texts, so do not skip it.
4. Show Inga the final draft with only the points that cannot be decided without her; after her OK put everything in: built-in tasks with `report_fix` (update the retired count in `bank_update_test.php`), `var-*` by renaming to the next `-rN`, prepared rows through an overlay like `_src/bank_fixes.py` with `replaces` (a typed report that becomes a gap changes its type: `replaces` allows that). Retired prepared rows: remove the row, and tell her to press *Retire* on the server (the import does not retire a row that left the file).
5. The grader change for *Correct the mistake* (accept the corrected words alone), with tests and a line in `RESEARCH-DATA-PLAN.md`.
6. Run `item_gates_test.py --update` only for findings that were read; full suite; package; changelog; zip link; *Prepared questions → Add all → Approve all*.

**Gates:** `app/tests/item_gates_test.py` (in `run_all.sh` and in the packaging), baseline `item_gates_baseline.json` (56 known findings, list for Inga: `pending/gates-known-findings.md`; most are fixed by the draft and leave the baseline when it is applied), old mistakes `bad_examples.json`, task dump `tools/dump_items.php OUT.json` (every task with role and source: use it for counting). The gate reads `docs/task-drafts/*.csv`, not `pending/`.

**Not asked of her yet / open:** her variants for U1–U7, S3–S10, C1–C8; whether the other backshift tasks outside the draft (e.g. *'I live in Riga.' She said she ___ in Riga.*) get a changed situation; a pass over all generated alternative orders in keys (`_src/alt_orders.py`), which is U7 and now more urgent; GitHub issues #33–#43 and older are still open (#38 is fixed by draft A.7).
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
