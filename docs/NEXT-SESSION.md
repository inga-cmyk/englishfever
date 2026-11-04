**Handing over to another agent, or checking its work: see `docs/AGENT-HANDOVER.md`.**

# Handover for the next session (2 November 2026)

Read this first, then `docs/ITEM-WRITING-RULES.md`, `docs/LEVEL-LISTS-test-english.md`, `docs/RESEARCH-DATA-PLAN.md`
and the top of `docs/CHANGELOG-practice-app.md`. Reply to Inga in Latvian.

## Standing rules (Inga)
- Work and push only on `claude/intelligent-albattani-2e9bfi`. Never push to `live`. Never touch WordPress or Hostinger.
- Never deploy: Inga uploads `dist/practice-app-update.zip` herself
  (https://github.com/inga-cmyk/englishfever/raw/claude/intelligent-albattani-2e9bfi/dist/practice-app-update.zip),
  then imports drafts: Prepared questions → Add all → Approve all.
- Propose variants before changing anything ("Pirms kaut ko maini - iesaki variantus"); show drafted cards and tasks in chat before adding them.
- Grammar decisions: check Murphy. New topics: take the scope from test-english.com (the lesson for that level) and
  check Murphy; own examples only, never copied sentences.
- Tasks: wrong options ungrammatical; "—" for no article/preposition; one sensible answer; no grammar terms in tasks
  (no vowel/consonant/passive in a question); "Make a question with *What*" or "Make a yes/no question"; no speaker
  tag after a quote; four different sentences in "NOT correct" tasks; settings travel, work, hobbies, lifestyle,
  learning, relationships, technologies (current events only B2/C1).
- Latvian note only where Latvian causes the mistake ("Tulkojot burtiski…"); natural Latvian; learners never see
  error-type names; no learner names stored; no GitHub comments without Inga's OK; no double dash in her documents.
- Say proactively how every change affects the research data. Never guess who an account belongs to (Inga = "Fox").
- Commit footer: `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` and the Claude-Session line.

## Testing and packaging
- Local server: `php -S 127.0.0.1:8099 -t app` (from the repo root). Build content: `cd app/authoring && python3 build.py`.
- Drafts: `docs/task-drafts/_src/*.py` write `docs/task-drafts/*.csv` (`lib.py` has the helpers; `lib.save` moves the
  B1 article tasks to "The or no article").
- Tests: the `app/tests/*` suites (PHP and Python) plus the Playwright scripts; `python3 tools/package_practice_app.py`
  runs bank_update_test and builds the zip. Add a line on top of the CHANGELOG for every change.

## Last uploaded / built
- Last zip version 2026-11-01 22:15: joining ideas (3 topics, cards, path steps, 84 drafts in conjunctions-1.csv,
  review list conjunctions-1-review.md), bold `**…**` in rule cards. Inga approved the A2.1 and A2.2 card drafts
  ("der") and asked for the tasks to be done without her; she has not seen the 84 tasks or the B1 card yet.
- test-english.com answers 403 to automated requests (bot protection); do not try to get round it. Inga sends
  screenshots of the explanation pages instead. B2 "clauses of contrast, purpose, reason and result" and
  "discourse markers" not done yet (no screenshot).

## Status 2 November, morning
- Done: learning path from the level lists (app/src/Path.php), step 2 session mix 60/25/15 with variant A and rule C (zip 2026-11-02 05:08).
- Next: B2 joining-ideas topics (Inga sends screenshots), Learning evidence additions, new tasks where banks run out or a path step falls back to a lower level (C1 tenses, B2 future), A2.2 tasks for past perfect, might, second conditional, reported speech, relative clauses.

## Plan, in order (agreed with Inga)
1. Done: research data step 1 (exposure, served_why, lang, feedback time, app version per answer; test accounts).
   Inga still has to mark "Fox" as a test account after uploading.
2. **Learning path from the test-english lists** (approved "1. jā"): the path for each level follows
   `docs/LEVEL-LISTS-test-english.md` in that order. A1 list = A2.1 basics (Inga: "pamatus arī vajag"; some current A2
   tasks are really A1). Topics without tasks are skipped until they have tasks; a topic without tasks at that level
   uses the nearest lower level and goes on the "needs tasks" list. Fix: "The or no article" was put right after
   "Used to" by mistake.
3. **Session rule (step 2)**, shown to Inga with a simulation on her data: for My learning path and Surprise me
   60 % current 1-2 steps at the learner's level (path order), 25 % review (weak topics below level first: ≥5 answers
   and <70 %; then fixed mistakes after 2-7 days), 15 % the same topic half a level higher. Topics below the learner's
   placement level count as known unless the data say otherwise. Rule C: mistakes on tasks later corrected (newer -rN
   or report marked fixed) do not count. Practice of a chosen topic (Practice page, Topics) stays exactly as chosen.
   Second Chance keeps fixing mistakes up to the learner's level. Variant A (start from the placement test: missed
   topics first, quick checks for the others) was proposed; Inga has not answered it explicitly.
4. **New topic group: Conjunctions and clauses** (Inga chose to start here). Split: A2.1 and/but/or/so/because;
   A2.2 however/although/because/so + time connectors; B1-B1+ contrast, purpose, reason (although, even though,
   despite, in spite of; to, in order to, so that, for; because, because of, as, since); B2 + result and discourse
   markers. Murphy English Grammar in Use units 64, 113, 116, 119 (the PDF is on Inga's Drive, only its contents
   could be read from the cloud). A card draft for A2.1 was shown in chat (table word / what it adds / example;
   mistakes: so vs because, comma before because ("Tulkojot burtiski…"), a because-clause on its own; watch out:
   "I don't drink coffee or tea"). Before finishing it: read the test-english explanation pages for these topics
   (look at how their tables highlight the key point; use the idea, not their sentences), then show Inga the card and
   25+ tasks per level.
5. Then: Learning evidence additions (Most practised, Repeats, "checked on another day"); new tasks where banks run out
   (Modal verbs B1.1/A2.2, Present simple/continuous B1.1, the small B2/C1 banks); about 20 tasks that ask for
   grammar terms; a held-out placement set for pre/post tests; the explanation-language experiment (Inga: interesting
   but not the focus; only after her yes); the 11 cards in the old layout.

## Data looked at (1 November, attempts export without "Fox")
- 3263 answers; most practised: present simple, modal verbs, past simple, reported questions (49 % right, served often
  because the old Surprise me picks the topics with most mistakes and some tasks were faulty), irregular plurals,
  present perfect. Levels mostly A2.2 and B1.1.
- Banks nearly used up by the keenest learners: Modal verbs B1.1 (all 27), Reporting verbs C1.1, Third conditional B2.1,
  Present continuous B1.1, Present simple B1.1, Modal verbs A2.2.
