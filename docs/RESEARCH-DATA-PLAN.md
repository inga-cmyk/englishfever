# Research data plan (practice app)

What the app records for the study, what each field means, and what has to be left out before analysis.
Written 1 November 2026. Every change to a definition or to how tasks are chosen gets a dated line in *Changes* below,
so results before and after it are not mixed.

## Where the data come from
- **Research export** (teacher: Research): `people.csv`, `days.csv`, `answers.csv`, `events.csv`, `codebook.txt`.
  Pseudonymised (a code per learner). Every registered learner (not guests, teachers or test accounts) with all their data from registration,
  except those who pressed *I do not agree to take part in the study* (since 5 Nov 2026; before that: only those who joined, from joining). This is the file for the thesis.
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
| unfair_wrong | 1 = marked wrong although the answer is correct English (a faulty key, fixed 8 Nov 2026): *Coffee grows in Brazil*, *Two windows broke in the storm*, *…whether the invoices have been sent*. `correct` stays 0; leave these rows out or count them as right | all rows (computed at export) |

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
- 11 Nov 2026 (zip of this date, `app_version` from 2026-11-11): the topic, level and task-kind labels above a task are hidden until the answer is given (before: always visible, also in the level test, where *Present simple* above *our flight ___ at 6.40 tomorrow* gave the form away). Expect lower right-answer rates and lower placements from this version; do not compare levels or accuracy across this date without `app_version`. The account invitation for guests no longer covers the level test result (it comes after a practice): display only.
- From the zip of 12 Nov 2026 (date of upload): a level-test mistake enters Second Chance only after the learner has practised that topic (before: every level-test mistake at or below the level found). Open / fixed mistake counts drop for learners who took the level test and have not practised those topics; compare Second Chance figures before and after separately.
- From the zip after 12 Nov 2026 (date of upload): 42 prepared and 38 built-in tasks are new versions (reported speech without a speaker tag and with the start given, only backshifted forms accepted; typed conditionals with a situation sentence; *Join with…* tasks that need a change; rewritten matching). Several typed reports became gaps with the start shown (kind text/write → gap): compare them before and after separately. 6 new *said / told* tasks (role use). Retired without a replacement: 5 prepared matching tasks and `var-pp-b11-match-01` (learning tasks, no evidence).
- From the zip after 12 Nov 2026 (date of upload = date of the change): the 96 *Correct the mistake* tasks also accept the corrected words alone (*help me*, *work*, *used to*), not only the whole sentence. Before, a correct correction with a typing slip elsewhere in the rewritten sentence, or the corrected words alone, was marked wrong. Right-answer rates in these tasks can rise from that date: compare before and after separately.
- 11 Nov 2026: answers.csv has a new column `unfair_wrong`. It marks the answers *grows* (*Coffee ___ in Brazil.*), *broke* (*Two windows ___ in the storm.*) and *have been* (*Mr Ozols asked whether the invoices ___ ___ sent.*, a practice-only task) that were marked wrong before the keys were fixed on 8 November. Stored results, levels and XP are not rewritten; the flag is worked out from the old task text and the stored answer at export. Leave these rows out of right-answer rates or count them as right.
- 6 Nov 2026 (later): the welcome-back message also appears when the app or tab comes back from the background after 30+ minutes, at most every 3 hours (before: only when the app was opened). More `welcome` events per learner from this time on.
- 6 Nov 2026: batch 3 without grammar terms: 66 tasks (43 built-in get new versions, 23 prepared tasks are replaced on import). From now no task instruction names a grammar form. 8 accept a second form; *ppp-B11-5a* gets *just* in its answer; *pc-A22-3a* becomes one gap (*are you doing / will you do*). Compare by task version.
- 6 Nov 2026: batch 2 without grammar terms: 120 tasks (6 built-in get new versions, 114 prepared tasks are replaced on import); time words added where another tense would also fit; 9 accept a second form (*lost*, *left*, *worked*, *finished*, *has got*, *will open* …). Compare by task version.
- 6 Nov 2026: *My level* on Home comes from the answers (last 60 check / use answers, ability fitted to task difficulty), not from the latest level test; `practice_level` added to people.csv (the same value on the day of export). Welcome-back messages for everyone (no random conditions): events `welcome` (detail = situation : set + variant, e.g. `gap3:b1`; set a = plain English for A2, b = the others) and `welcome_ok` (closed with its button). Return behaviour before and after this date can be compared; it is a change for everyone, not an experiment.
- 6 Nov 2026: 133 tasks reworded without grammar terms (27 built-in tasks get new versions; 106 prepared tasks are replaced or reworded on import). Some accept a second correct form (*lost* / *has lost*, *shone* / *was shining*, *went* / *had gone*, *will open* / *will be opened*, *starts* / *started* …), so their right-answer rates may rise; compare by task version. Role changes: 12 rewritten choice tasks that need the form count as *check* (evidence), `rs-B12-2a` too; `var-pa-a22-match-01` (matching verb forms) is now *learn* like the other form-matching tasks.
- 6 Nov 2026: 41 typed B2 / C1 tasks with typical mistakes added (`typical-b2c1-1.csv`): from their approval the level test asks typed forms at B2 and C1 as well, so B2 / C1 placements before and after are not comparable.
- 6 Nov 2026: My learning path sessions changed. The recommended training alternates between a review of earlier steps (`source` = path_review) and the next step (`source` = path). A step session asks only the step's topics at its levels, ordered Recognise → Understand → Apply; the 60 / 25 / 15 mix (step, review, a step up) is gone for path sessions (Surprise me keeps it). A weak earlier step is no longer the recommended one; it starts the next review. Path sessions before and after this date are not comparable.
- 6 Nov 2026: new learners are asked their own level first (`self_level` in people.csv: A2, B1, B2, C1 or unknown; empty = registered before this date). The level test now starts at that level (going down a level when it is too hard; before: always from A2), asks typed forms wherever a topic has them (choices only where it has none, at present B2 and C1) and puts the topics with typical mistakes first. Placement levels before and after this date are not comparable; earlier placements were mostly choice tasks and may be too high (the teacher saw a pre-intermediate learner placed at B2). Simulation, built-in tasks only: a learner at about A2+ who says B2 is placed A2.2 to B1.2 (1 of 60 at B2.1).
- 5 Nov 2026: session screen changed (display only, answers and grading unchanged): *Skip* small on the left of a long *Check*; *Continue* in the same place after checking; no question count at the top; *Stop* renamed *Quit*; the feedback no longer has the rule reminder and the language flags under it (the rule card is still the ? on the task, recorded as `rule_card_before`; the language is now changed only in Profile). Skip and rule-card rates before and after this date may differ because of the layout.
- 5 Nov 2026: the study no longer asks for consent and has no random conditions (teacher's decision). Every registered learner is in the export with all data from registration (study day 0 = registration day); a learner can opt out under Profile → Your data → Research, and is then left out of the next export. Everyone sees the streak counter and the leaderboard (a learner can leave the leaderboard in Profile). `people.csv` has no `cond_*` columns; `consent_week` = `join_week`. Learners who had said no to the earlier invitation stay left out.
- 5 Nov 2026: *used to do* and *be / get used to doing* tasks no longer stand in for each other when a mistake is fixed, locked in or reopened (also in Second Chance and `for_item`). Learn tasks are left out of this count; meaning questions *What does it / this / that say / mean?* are now learn tasks. Answer rows and XP are not rewritten, but mistake summaries worked out from history can change (more conservative). Five built-in tasks get new versions; two B2 typed tasks (narrative tenses: tennis, bus) become word banks, so their results are not evidence of writing the form unaided; the *It's time* task becomes *It's high time* with better wrong options. The import retires the old versions of these three prepared tasks. Compare results by app version, task version and help given. Review / Next step labels, the reason line for a topic to strengthen, answer counts in the Skills check and the phone layout change only the display; topic order and placement are unchanged.
- 5 Nov 2026: seven typed narrative-tense tasks (B2.1 / B2.2) lose the instruction that named the tenses; they stay typed (use). One accepts a second form (*had worked*), so its right-answer rate may rise; compare by task version.
- 28 Oct 2026: session source recorded.
- 28 Oct 2026: faulty reported-questions tasks corrected (rq-B22-1a/2a/3a); topic numbers for reported questions
  before this date are inflated (wrong tasks made the app serve the topic more often).
- 1 Nov 2026: exposure, served_why, lang, feedback time, app version recorded; test accounts can be marked.
- 2 Nov 2026: My learning path rebuilt from the test-english level lists; a path step now asks only the tasks of its level (A2.1, A2.2, B1, B1+, B2, C1), and mastery of a step counts only answers at those levels. Path sessions before and after this date are not comparable.
- 2 Nov 2026: session mix for My learning path and Surprise me (about 60 % the step at its level, 25 % review, 15 % the same topics half a level higher; the part of each task is stored in the session state as `slot`). Surprise me now takes its topics from the path (the recommended step and the next one), not from the most mistakes. Rule C: mistakes on tasks that were later corrected (a newer version, a retired task, a report marked fixed) are left out of topic choice, Second Chance and the Learning evidence counts. Below the placement level a step counts as known unless the learner has 5+ answers there with under 70 % right.
- 2 Nov 2026: a ? button on every practice task opens the rule card; answers given after opening it are marked (rule_card_before). Compare or separate them when judging what a learner knows without help.
- 3 Nov 2026: optional AI check of open writing answers (Claude Haiku 5.5, only when an API key is set in config.php). The answer row keeps the AI verdict and the changed words (`attempts.ai`). When the AI finds a mistake the pattern check missed, the answer counts as wrong. Learner text is sent to Anthropic for this check (no names): say so in the privacy notice and the consent text before switching it on.
- 3 Nov 2026: task roles (learn / check / use). The level test no longer asks learn tasks (it skipped practice-only tasks before; matching and "Which sentence means …" tasks are now left out too). Use only check and use answers as evidence of knowing a form.
- 4 Nov 2026: rule cards of 12 topics rewritten in the new layout (passives: present continuous, present perfect, future, modals; causative; mixed and advanced conditionals; reporting verbs; advanced indirect questions; adjective order; so / such; unreal time). Four C1 cards (cond_mixed, cond_advanced, rep_verbs, ind_advanced) are now shown in Latvian to learners who chose Latvian; before this date they saw the English card. Tasks and grading did not change. Compare rule_card_before answers on these topics before and after this date with care.
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
- 4 Nov 2026: 40 more learning tasks (docs/task-drafts/learn-drag-4.csv), five drag tasks for each topic-level that had none; *practice only*, never evidence.
