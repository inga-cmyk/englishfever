# Teacher's test generator: decisions and open points

Recorded 17 November 2026 from the teacher (Inga), for the session that will build it. **Nothing is built yet.** Read
`docs/AGENT-HANDOVER.md` first (rules, how to package, research lines), then this.

## What it is

A teacher makes a test from the existing tasks, gives it to learners who are already registered, and sees the results. Every test is
saved.

## Decided by the teacher (17 November)

**Making a test.** The teacher chooses: level, topic or topics, number of questions, pass mark, time limit, deadline. The app draws
the tasks. Before the test is given, the teacher can **regenerate the whole test** or **replace single questions**.

**Tasks.** Only *check* and *use* tasks (`Content::role`), never *learn* (matching, "Which sentence means…", practice only). Test tasks
**may also appear in practice**: no separate pool.

**Giving it.** To learners who are already registered. Both sides get a notice: the learner *new test*, the teacher *test handed in*.

**Taking it.**
- The same questions for everyone, **in a different order for each learner**.
- A time limit. A test that was interrupted can be continued while the time has not run out. Unanswered questions count as wrong.
- **No rule cards** during a test (the *?* button and the Rules page must not be reachable from it).
- No explanations during the test: the learner sees their mistakes **after the whole test is finished**.
- Test mode **looks different** from practice, and the progress through the questions is visible.

**After it.**
- The mistakes of a test go to **Second Chance**.
- The teacher can let the **same test be taken again**; the order of the questions changes again.
- The teacher sees the results; every test and every attempt is kept.

## Open: ask the teacher (one question each, with a recommendation)

1. **Notices:** inside the app only (a card on Home, a badge in the teacher view), or also by e-mail? The app sends no e-mail today
   (learners sign in through englishfever.com); e-mail would need the WordPress side, which agents never touch. Recommended: in the app.
2. **Does a test answer count** for *My level* and for *Learned*? Recommended: yes (no help, timed: the cleanest evidence), with a dated
   research line.
3. **One timer for the whole test** (recommended) or a time per question?
4. **What the learner sees at the end:** score and pass / fail, then their mistakes with the explanations. At once, or only after the
   deadline (so answers cannot be passed on)? She said "after the whole test"; confirm that this means at once for that learner.
5. **Is the pass mark shown** to the learner before the test?
6. **Who can be chosen:** single learners from the list, or also saved groups? There are no groups in the app today.
7. **A retake:** does the teacher open it per learner or for everyone; which attempt counts (best, last, all shown)?
8. **After the deadline:** closed, or still possible and marked late?
9. **Replacing a question:** the app proposes another task of the same topic, level and kind, or the teacher picks from a list?

## What is already there to build on

- Sessions and answers: `app/src/Engine.php` (`start`, `answer`, `pickNext`), tables `psessions`, `attempts`. The level test
  (`mode = placement`) is the closest existing mode: no feedback, no skip, no rule card button, a report link only.
- Checking answers: `app/src/Grader.php`. Task roles: `Content::role`. Reported tasks are paused: `Reports::pausedIds` (a test should
  not draw a paused task; decide what happens when a task in a saved test is paused or retired later).
- Teacher views and the learner list: `app/assets/app.js` (`#/teacher`), `app/src/Stats.php`.
- Second Chance: `app/src/Mistakes.php` (a mistake is fixed only by another task of the same grammar point).
- Research export: `app/src/Research.php`. Usage events: `app/src/Usage.php`.

## Things the builder must not miss

- **Research:** test answers need their own mark in the export (a `mode` value, e.g. `test`, and the test id), a dated line in
  `docs/RESEARCH-DATA-PLAN.md` → *Changes*, and one sentence to the teacher on what it means for her data. A teacher-set test with a
  deadline is a new engagement factor (an external cue to return): say so.
- **Fixed content:** a saved test stores its task ids and the content version of each task (ids get `-rN` when a task is corrected),
  so results stay readable after a task changes.
- **Equal difficulty:** tasks of one level differ a lot, and a typed answer is about half a level harder than a choice
  (`docs/THESIS-ASSESSMENT.md`, learner model check). Keep the mix of task kinds fixed per test, and the same in a regenerated test.
- **Timing on the server:** the time limit and the deadline are checked on the server, not only in the page.
- **Order per learner:** derive it from the test id and the attempt, so a reload shows the same order and a retake a new one.
- Texts the learner sees: English, short, no grammar terms in instructions; test the phone layout (390 px) with screenshots for the
  teacher before packaging.
- Known failing test before this work: browser test `comeback_ui` (Second Chance summary); it is not caused by the test generator.
