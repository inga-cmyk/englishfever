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
| source | where the session started: placement, path, path_check, surprise, second_chance, home_topic, practice_page, rule_card, summary (a button on the results page, from 3 Nov 2026) | 28 Oct 2026 (older: partly unknown) |
| lang | explanation language set for the learner then (en / lv) | 1 Nov 2026 |
| feedback_seconds | time from the feedback to Next: reading the explanation | 1 Nov 2026 |
| app_version | app version then (see docs/CHANGELOG-practice-app.md) | 1 Nov 2026 |
| task_role | learn (solvable from the meaning, not evidence) / check (depends on the form) / use (the learner writes it); computed from the task (Content::role) | 3 Nov 2026 |
| rule_card_before | 1 = the learner opened the rule card (the ? button) during this task, before answering | 2 Nov 2026 |

## Definitions (as used on the Learning evidence page)
- **Slip / gap**: a missed task is asked again later in the session; right = slip, wrong again = gap.
- **Fixed**: after a mistake, the learner answers a *different* task of the same kind correctly.
- **Locked in**: a fixed mistake answered correctly again on another day with another task of that kind.
- **Reopened**: a fixed mistake made again.

## Learning path states (from 3 Nov 2026)
- **learned**: 10+ different check/use tasks right at the step's levels, 80%+ of the last 12 right, recognise + use + one typed answer, two days. A topic with fewer than 10 check/use tasks at that level cannot be learned yet.
- **mastered**: learned, and 3+ days later three never-seen tasks right.
- **probably known**: below the placement level, right in the level test, or 80%+ on 5+ answers at a higher level of the same topic; confirmed (**known**) by 3 right answers on 3 different tasks in a row, else **strengthen the basics**.

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
- 2 Nov 2026: session mix for My learning path and Surprise me (about 60 % the step at its level, 25 % review, 15 % the same topics half a level higher; the part of each task is stored in the session state as `slot`). Surprise me now takes its topics from the path (the recommended step and the next one), not from the most mistakes. Rule C: mistakes on tasks that were later corrected (a newer version, a retired task, a report marked fixed) are left out of topic choice, Second Chance and the Learning evidence counts. Below the placement level a step counts as known unless the learner has 5+ answers there with under 70 % right.
- 2 Nov 2026: a ? button on every practice task opens the rule card; answers given after opening it are marked (rule_card_before). Compare or separate them when judging what a learner knows without help.
- 3 Nov 2026: optional AI check of open writing answers (Claude Haiku 5.5, only when an API key is set in config.php). The answer row keeps the AI verdict and the changed words (`attempts.ai`). When the AI finds a mistake the pattern check missed, the answer counts as wrong. Learner text is sent to Anthropic for this check (no names): say so in the privacy notice and the consent text before switching it on.
- 3 Nov 2026: task roles (learn / check / use). The level test no longer asks learn tasks (it skipped practice-only tasks before; matching and "Which sentence means …" tasks are now left out too). Use only check and use answers as evidence of knowing a form.
- 3 Nov 2026: mastery rule 1a and the path states above replace the earlier rule (8 of the last 10 answers right). Path statistics before and after are not comparable.
- 3 Nov 2026 (evening): choice tasks rewritten so the options are about one theme and of about the same length, and *NOT correct* tasks have no near-identical pair (109 tasks, new `-rN` versions; docs/task-drafts/option-fixes-review.md). Answers to the old versions are the "corrected task" case in *Leave out*, point 3: the old options could give the answer away.
- 3 Nov 2026 (evening): the level test asks the topics of each level in the order of My learning path (A2 first: present simple, present continuous, past simple ...) instead of a random topic; it still climbs or stops by the answers. Level tests before and after this are comparable in level, not in which topics they asked.
- 3 Nov 2026 (evening): My learning path recommends the first step from the level found, in path order, even when the level test did not ask it; such a step starts as a 5-task quick check (`source = path_check`), and passing it counts the step as known. Before, a step with a topic missed in the level test came first.
- 4 Nov 2026: new C1 topic *Unreal time and preferences* (`unreal_time`: it's high time, I'd rather / I'd sooner) and a path step for it after *Conditionals, inversion, wish*. Three tasks moved there from the twins batch (they were never served under the old topic). The C1 part of the path has one step more from this date.
- 4 Nov 2026: twins batch 1 (76 tasks, docs/task-drafts/twins-1.csv) offered as prepared questions after the teacher's two reviews: the small banks grow, so fewer tasks are served again (`served_why = again_after_right`).
- 4 Nov 2026: twins batch 2 (50 tasks for 16 topic-levels, written by another agent and corrected by Claude; docs/task-drafts/twins-2.csv) offered as prepared questions. Each of these topic-levels reaches 10 check / use tasks, so *Learned* becomes possible there; one twin per source task, so the ten are not near-copies of one sentence.
- 4 Nov 2026: 9 more tasks for *Unreal time and preferences* (docs/task-drafts/unreal-time-1.csv), so the C1 topic has 12 check / use tasks and its path step can reach *Learned*.
- 4 Nov 2026: twins batch 3 (33 tasks, docs/task-drafts/twins-3.csv) offered as prepared questions: the nine topic-levels left below 10 check / use tasks reach 10.
- 4 Nov 2026: first **learning tasks** (docs/task-drafts/learn-drag-3.csv): 33 drag tasks with the same sentences as batch 3, marked *practice only* (`Content::role` = learn). They are served in practice sessions but never in the level test or the quick check and never counted for *Learned*. In analysis, answers to learn tasks are practice, not evidence (filter by `task_role`).
