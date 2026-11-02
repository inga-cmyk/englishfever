# Research data plan (practice app)

What the app records for the study, what each field means, and what has to be left out before analysis.
Written 1 November 2026. Every change to a definition or to how tasks are chosen gets a dated line in *Changes* below,
so results before and after it are not mixed.

## Where the data come from
- **Research export** (teacher: Research): `people.csv`, `days.csv`, `answers.csv`, `events.csv`, `codebook.txt`.
  Pseudonymised (a code per learner). Only learners who joined the study, from the moment they joined. This is the file for the thesis.
- **Teacher exports** (answers of all learners, Usage): with nicknames. For checking the app, not for the thesis.

## One row per answer (answers.csv)
| Field | Meaning | Since |
|---|---|---|
| item | task id; `-r2`, `-r3` = a corrected version | start |
| correct | 1 / 0 (a skip counts as 0) | start |
| skipped | 1 = "I don't know" | 1 Nov 2026 |
| exposure | 1 = first time this learner meets this task, 2 = second ... | 1 Nov 2026 |
| served_why | new, again_after_wrong, again_after_right (no new task left), second_chance, bonus | 1 Nov 2026 |
| source | where the session started: placement, path, path_check, surprise, second_chance, home_topic, practice_page, rule_card | 28 Oct 2026 (older: partly unknown) |
| lang | explanation language set for the learner then (en / lv) | 1 Nov 2026 |
| feedback_seconds | time from the feedback to Next: reading the explanation | 1 Nov 2026 |
| app_version | app version then (see docs/CHANGELOG-practice-app.md) | 1 Nov 2026 |

## Definitions (as used on the Learning evidence page)
- **Slip / gap**: a missed task is asked again later in the session; right = slip, wrong again = gap.
- **Fixed**: after a mistake, the learner answers a *different* task of the same kind correctly.
- **Locked in**: a fixed mistake answered correctly again on another day with another task of that kind.
- **Reopened**: a fixed mistake made again.

## Leave out before analysis
1. Test accounts (`is_test`; the teacher marks them on the student's page). Already left out of the research export,
   Learning evidence and Usage.
2. Answers with `served_why = again_after_right` when measuring learning: the learner may remember the sentence.
   For learning curves use `exposure = 1` only.
3. Answers to a task version that was later corrected because it was faulty (a newer `-rN` exists, or the teacher marked
   its report fixed), when judging a topic.
4. Answers under 2 seconds (guessing) and over 10 minutes (away from the screen). Report how many were removed.
5. Topics or tasks with fewer than 8 answers: describe, do not compare.

## Threats to the conclusions, and the answer to each
- **Repeated tasks** look like learning: exposure and served_why (above); the Repeats table shows where a bank runs out.
- **Regression to the mean**: a missed task is often right the second time by chance. Compare with the learner's success on
  tasks they had not missed before, and use new tasks of the same kind (*fixed* is defined that way).
- **Self-selection**: keen learners practise more and improve more anyway. Compare a learner with themselves over time,
  or use the randomised conditions; do not compare heavy with light users as proof of effect.
- **Practice and test with the same tasks**: a held-out set of placement tasks that never appears in practice is planned
  for the pre / post test (plan step 5).
- **The app changes during the study**: app_version on every answer; changes listed below.
- **Guessing differs by task type** (choose from 3 = 33 %, typing ~ 0 %): compare topics with the task type taken into account.
- **Model**: a mixed-effects logistic model (learner and task as random effects) instead of plain percentages.
- **Hypotheses written down before looking**: 2-3 main questions, the rest is exploration.

## Changes
- 28 Oct 2026: session source recorded.
- 28 Oct 2026: faulty reported-questions tasks corrected (rq-B22-1a/2a/3a); topic numbers for reported questions
  before this date are inflated (wrong tasks made the app serve the topic more often).
- 1 Nov 2026: exposure, served_why, lang, feedback time, app version recorded; test accounts can be marked.
- 2 Nov 2026: My learning path rebuilt from the test-english level lists; a path step now asks only the tasks of its level (A2.1, A2.2, B1, B1+, B2, C1), and mastery of a step counts only answers at those levels. Path sessions before and after this date are not comparable.
