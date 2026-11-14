# Brief: the quality pass and the map in the app (Inga, 14 November 2026)

For the agent who works on the app on `claude/intelligent-albattani-2e9bfi`. Written by the session that made the grammar map (documents only; it changed nothing in `app/`, the task files or the tests). Read `docs/AGENT-HANDOVER.md` (sections 2 to 4) and `docs/ITEM-WRITING-RULES.md` first; everything there still holds.

## What Inga asked for (13 and 14 November)

- She wants what learners see to be meaningful **as soon as possible**, and she wants the new grammar map to run in the app.
- Two faults keep coming back in the tasks, and she is tired of finding them herself:
  1. **A situation or explanation in front of a choice that does not need it.** Her words: the added explanation of the context is superfluous when the correct answer is recognised by where the grammar form is correct; for such questions a short instruction is enough: *Choose the correct option.* The length of an instruction is not the main problem.
  2. **Correct answers that are not accepted** in typed tasks.
- **How she wants to be asked:** one question at a time, the most important one for the step, with a recommendation (two or three short options work well; she answers with one click). Seven questions in one message made her lose track of what was still needed from her. Do not show her a draft before a second reader has seen it; bring her only what cannot be decided without her.

## What exists now (all generated; do not edit by hand, see `docs/grammar-map-src/README.md`)

| File | What it is |
|---|---|
| `docs/GRAMMAR-MAP.md` | the map for reading: 387 grammar points A2.1 to C1, each with can-do, prerequisites (`needs`), contrasts, typical errors, sources, topic, content |
| `docs/GRAMMAR-MAP.json` | the same map for programs: `points[]` with `id, level, needs, contrasts, leads_to, topics, tasks, task_levels` |
| `docs/GRAMMAR-MAP-TASKS.csv` | all 3314 tasks, each tied to one point. `key` is the key of `app/tests/item_gates_test.py` (topic, level, kind, question, body); `built_in_id` is filled for built-in tasks. 3041 tasks were read one by one, 273 sorted by rule (`sorted_by`) |
| `docs/GRAMMAR-MAP-GAPS.md` | Latvian: points with no content, level differences, points with fewer than 10 tasks, contrast pairs without choice tasks, and in section 5 **Inga's five level decisions of 13 November** |
| `docs/review/choice-with-situation-2026-11-14.csv` | the work list for part A (204 choice tasks); the columns `verdict` and `new_question` are empty for you to fill |
| `docs/review/typed-one-answer-2026-11-14.csv` | the work list for part B (808 typed tasks that accept exactly one answer); `verdict` and `answers_to_add` are empty |
| `docs/grammar-map-src/` | the source and the generators of all of the above |

The page Inga opens: https://claude.ai/artifact/JqFNfweQ3WyobBA9QvpRLh (republish it from `page.py` output only if the map changes).

## Part A. A situation before a choice (start here: no code, improves what learners see today)

**The test, for every choice task:** cover the situation. If exactly one option is still possible English on its own, the situation is superfluous: remove it and use *Choose the correct option.* (a gap sentence) or *Which sentence is correct?* (whole sentences). If a wrong option would be correct English in another situation, the situation is what makes the task: keep it, in one short sentence.

Two tasks from the bank that show the difference:
- Superfluous: *Your brother has a bad cough. Which sentence is correct?* with *He should see a doctor / He should sees a doctor / He shoulds see a doctor / He should to see a doctor.* Three options are impossible anywhere.
- Needed: *A colleague asks: 'What did you do at the weekend?'* with *I went hiking … / I go hiking … / I am going hiking … / I have gone hiking …* The others are correct sentences elsewhere; without the question there is no answer.

**The list** (`choice-with-situation-2026-11-14.csv`): 204 of the 1081 choice tasks have a situation or an explanation in the question.
- 105 are *situation + choice* (93 count as *check*). On a first reading about 40 of them fail the test; the exact number comes from reading each with its full options. Give every row one verdict: `remove` (write the new short question in `new_question`), `keep` (and shorten the situation there if it is long), or `rebuild` (the task is weak either way: say why).
- 99 are *meaning questions* (*Which sentence is a plan made before now?*). There the situation is the task, so the test does not apply; 35 of them still count as *check*, which contradicts decision U2 A of 12 November (meaning questions are *learn*). Check those 35 against `Content::role` and report the ones that should change.
- The existing `long_frame` gate (13 November) catches only 16 of the 105: it looks for more than ten words before *Choose the correct option*. The rule is not about length. After the pass, widen the gate: a choice task without a gap whose question has a sentence before *Which sentence is correct? / Choose the correct …* is listed for reading (baseline = the rows you marked `keep`).

When the situation goes, read the options once more: the wrong options must still be believable mistakes of this point, not three random impossible sentences (rules of 3 and 11 November).

## Part B. Correct answers that are refused

**The list** (`typed-one-answer-2026-11-14.csv`): 808 of the 1476 typed tasks accept exactly one answer. 120 are in a *risk group* (the accepted answer is a form that usually has a rival) and come first in the file; the other 688 follow by topic.

Three that were found while reading for the map, as models of what to look for:
- *We ___ for an hour, and the bus still ___.* accepts *have waited*; *have been waiting* is the more natural answer and is refused.
- *We ___ to the same café every Friday when we were students.* accepts *used to go*; *went* and *would go* are refused.
- *You ___ wait. The shop is open all night.* accepts *needn't*; *don't have to* and *don't need to* are refused.

Also seen: model sentences that are not natural English (*They are thinking to move to the coast*; *The cinema is closed every evening at ten* as a routine). Mark such rows `rebuild`.

For every row decide one of two things, as the rules of 4 and 6 November say:
1. The task is **about that form**: then add a time word or a situation that rules the rival out, and keep one answer.
2. The task is not about choosing that form: then **accept the rival** and give it its own answer note where the meaning differs.

**The most precise source is the learners themselves.** Ask Inga (one question) for the research export with the wrong answers that at least two learners typed for the same task, and the `unfair_wrong` column that exists since 11 November. Read those first: they show exactly where the app is wrong. `docs/AGENT-REPORT-learner-answers-2026-11-08.md` is the earlier round.

Widening a key changes grading: a dated line in `docs/RESEARCH-DATA-PLAN.md`, and tell Inga in one sentence what it means for her data.

## Part C. The map in the app

Inga's decisions that the path must follow (full text: `GRAMMAR-MAP-GAPS.md`, section 5.1):
1. Past perfect, second conditional and reported speech with the tense change are **B1**: the A2.2 path steps `a2_pap`, `a2_c2`, `a2_rep` are not needed.
2. Defining relative clauses (`rel_subj`) and might / may (`might`) are **A2.2**: the steps stay, and about 25 A2.2 tasks each must be written (now 6 and 9 tasks that count, none at A2.2).
3. *I wish* + past (`wish_pres`) and *would rather* + verb (`would_rather`) are **B1.2**: about 25 B1.2 tasks each (now 1 and 3, all B2.2).
4. Inversion and cleft sentences are **split**: B2.2 is recognising the form and making it with the start given; choosing and transforming is C1.
5. **C1 is one level**, no C1.1 / C1.2: the level list is A2.1, A2.2, B1.1, B1.2, B2.1, B2.2, C1.

Steps, smallest first; propose each to Inga before building it (handover rule), one question each:

| Step | What | Done when |
|---|---|---|
| C1 | **The app knows the point of every task.** Build `GRAMMAR-MAP.json` and the task table into `app/content/` (in `app/authoring/build.py`), joined by the gate key or the built-in id. Add a gate: a task without a point stops the packaging | every served task has a point; the gate baseline is empty |
| C2 | **After a wrong answer the next task comes from the same point** with another sentence; after a second wrong answer in that point, one task from a point in its `needs` that has tasks at the learner's level or below | new `served_why` values in the research export; a dated line in `RESEARCH-DATA-PLAN.md`; a test with a fixed seed |
| C3 | **The path follows the map:** decision 1 applied; a point without tasks is skipped, not shown as an empty step; *Learned* stays per topic and level as now | `Path.php` tests; Inga has seen the new A2.2 and B1 step lists |
| C4 | The level test walks the map | not now: only after C1 to C3 have run with learners |

C2 is the step with the largest effect for a learner and the smallest change in code: today a mistake in *been / gone* is followed by any present perfect task.

**Do not** wait for tasks for all 387 points (211 have tasks, the path can run on those), do not write C1 content yet (24 points below C1 that it stands on have no content: the table at the end of `GRAMMAR-MAP.md`), and do not relabel existing tasks beyond the five decisions.

**Tasks to draft, in this order** (each batch through the gates and a second reader, then to Inga):
1. `rel_subj` A2.2 and `might` A2.2 (decision 2).
2. Choice tasks for the form pairs that have almost none (`GRAMMAR-MAP-GAPS.md`, section 4.2): *must be / can't be* 0, *during / while* 0, *by / until* 0, *would rather + verb / would rather you + past* 1, *could / was able to* 2, *although / despite* 3, *because / because of* 3. Here the situation is needed, by the test of part A.
3. `wish_pres` and `would_rather` B1.2 (decision 3).
4. Points that have a rule card and no task at all (section 3.1 of the gaps document: 18 points, among them *have got*, *Shall I …?*, *should have done*, *no / none*).

## Keeping the map true while you work

- A task's key contains its question. **When you change a question (part A) or replace a task, carry its point over:** copy its entry in `docs/grammar-map-src/assign_keys.json` to the new key. `python3 docs/grammar-map-src/export.py` prints how many tasks have no entry (*new or changed since the reading*): keep it at 0, reading each new task before you give it a point.
- New tasks get their point when they are written: add a `point` to the review file of the batch and to `assign_keys.json`.
- If a point itself must change (level, prerequisite, a new point), change `p1.py` to `p4.py` or `fixes.py`, run `check.py`, regenerate, and say so to Inga: the map is hers.
- Sources behind the map, so that nobody quotes from memory: Murphy unit numbers were checked against the contents list; the English Grammar Profile levels against the online table (1222 statements); all ten C1 strands against the test-english pages Inga sent as screenshots (three pages only in part: marked in the map). Her screenshots and PDFs are not in the repository and must not be.

## Suggested order

A and B first, together in one zip: they need no new code and change what every learner sees. Then C1 and C2 in one zip. Then the first task batch with C3. Confirm this order with Inga in your first message, as one question.
