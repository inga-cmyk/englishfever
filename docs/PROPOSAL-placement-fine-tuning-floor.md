# Proposal for the teacher: no lower level in fine-tuning for a learner with no mistakes (24 November 2026)

**Status: the teacher chose option A (26 November 2026); applied in `app/src/Engine.php` `pickNext`, zip 2026-11-26 12:25.** `placement_test.py` passed 20 of 20 runs on a fresh dev database, `placement_retake_test.php` all 11 checks, `placement_sim.py 4` full level right 92 / 98 / 98 % (12 / 24 / 40 questions).

## What was seen

The check *climbs A2 -> B1 -> B2, 3 questions per level, then more at B2* fails in about 1 of 4 to 8 runs on a fresh dev
database (5 of 20 runs on 24 November). The simulated learner answers every question right. The staircase works as
designed (A2, B1, B2, three questions each), but the 12th question is sometimes a **B1.2** task, for example
`ct-B12-3a-r2` (third conditional) after `ca-C12-4a-r4`:

    A2 A2 A2 | B1 B1 B1 | B2 B2 B2 | B2 B2 B1

## Why it happens

After the staircase, the test fine-tunes near the ability found so far (`Engine::pickNext`). After 11 right answers the
ability is about 7.6, which is above all B2 tasks (B2.2 is 6.0–6.8). Three rules then meet:

1. **Every question is about another topic** (teacher, 16 November). In the dev bank (built-in tasks only) only one unused
   topic with a B2 task is left by question 12: *Mixed conditionals*, `cm-B21-3a-r3` (B2.1, a choice task).
2. **Topics in reach** are all topics whose easiest task is at most ability + 1.0. This rule has no lower limit, so the
   unused B1 topics (third conditional, the passives, past perfect …) stay in reach. Note: the B1.2 task does *not* come
   in through the wider *half a level higher* rule (`$wider`, theta + 2.0); that rule is not used at this point.
3. **Typed first** (teacher, 6 November): a typed task costs 0.8 less, *"a choice only when no topic in reach has a typed task"*.

So the typed B1.2 task (difficulty 4.4) and the B2.1 choice task (5.4) end up almost equal: cost 2.39 against 2.44 in the
failing run. The small random part of the choice decides which one comes, about half the time. On the live server the
prepared tasks add more B2 topics, so this happens less there, but it can still happen near the end of a longer test or
a retake (a retake asks only tasks the learner has not met).

## Is it what the design wants?

Probably not, but it is your decision. The reasons it looks unintended:

- The 16 November rule moves to a topic **higher**, not lower, when the topics near the ability are used up.
- The *typed first* rule was written for the choice between tasks at about the same level. It was not written to let a
  typed task win over a level the learner has just passed.
- The result depends on a coin flip (2.39 vs 2.44), not on a rule.
- For a learner with no mistakes, a B1.2 task right after passing B2 tells the test almost nothing: the chance of a right
  answer is above 99 %. It can also feel like a step down at the end of the test.

The scoring does not change either way: the level found comes from all the answers, and a right B1.2 answer hardly moves it.

## Options

**A (recommended).** In fine-tuning, a learner who has **no mistake so far** gets no task below the **top full level passed**
in the staircase (here B2), while any unused topic still has a task at or above that level. If no such topic is left,
the test goes on as now. Learners with a mistake are not affected.

**B (wider).** The same floor for every learner: never below the top full level passed in the staircase, mistakes or not.
This changes more tests (mixed learners would no longer get fine-tuning questions from the level below the one they
passed), so it needs its own check with the simulated learners.

**C (keep it).** Lower full levels can come in fine-tuning. Then only the test changes: it would accept B1 among the
fine-tuning questions for this learner, and the check would be renamed.

## The change for option A (8 lines, ready to apply)

In `app/src/Engine.php`, `pickNext`, right after `if ($fresh) $bySkill = $fresh;` in the placement block:

```php
            // fine-tuning for a learner with no mistake so far: no task below the top full level passed, while a topic still has one at or above it
            // (an all-right learner was sometimes offered B1.2 after B2, when a typed B1.2 task outscored the last unused B2 choice task)
            $topPassed = !empty($pl['passed']) ? end($pl['passed']) : null;
            if (!$stairs && $topPassed && !in_array(0, array_map('intval', array_column($st['last'], 'correct')), true)) {
                $floor = array_search($topPassed, Content::FULL_LEVELS, true);
                $up = array_filter(array_map(fn($list) => array_values(array_filter($list, fn($it) => array_search(substr($it['level'], 0, 2), Content::FULL_LEVELS, true) >= $floor)), $bySkill));
                if ($up) $bySkill = $up;
            }
```

Checked on 24 November on a fresh dev database (the change was applied only for the check, then taken out again):

| | without the change | with option A |
|---|---|---|
| `placement_test.py`, 20 runs | 15 pass, 5 fail (all on this check) | 20 pass |
| `placement_retake_test.php` | — | all 11 checks pass |
| `placement_sim.py 4` (accuracy of the level found, 40 simulated learners per length) | full level right 95 / 98 / 90 % (12 / 24 / 40 questions) | 92 / 90 / 95 % |

The simulation differences are run-to-run noise: the server's choices are random, and option A only changes tests where
every answer so far is right. The simulated learners almost always make a mistake before fine-tuning.

## If you choose A

1. Apply the change above and keep the test as it is.
2. Add a dated line under *Changes* in `docs/RESEARCH-DATA-PLAN.md`, for example: *From the zip after (date): in the level
   test, a learner with no mistake is not given fine-tuning tasks below the top level passed in the staircase. The
   questions served change, the scoring does not.*
3. Add a line to `docs/CHANGELOG-practice-app.md`.
