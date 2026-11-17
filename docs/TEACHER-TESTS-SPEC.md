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

## Decided by the teacher (17 November, second round)

- **Test answers count** for *My level* and for *Learned* (a dated research line is needed).
- **Notices only inside the app.** E-mail is the teacher's own matter on the WordPress side; the app sends none.
- **Groups:** the teacher must be able to choose learners by group, and the groups are the ones of the **WordPress course** the
  learners are in. Half of this exists: the app already asks the website which students are enrolled in the Tutor LMS courses a teacher
  wrote or teaches (`Wp::roster`, plugin route `/wp-json/ef-practice/v1/roster`, used for *My students*), but it gets one flat list of
  WordPress user IDs, not the course of each. The route would have to return the students per course, with the course title
  (plugin `app/wp-plugin/ef-practice-sso/`; agents change the plugin code in the repository only, the teacher installs it; never touch
  WordPress itself). Ask her which plugin holds the courses (Tutor LMS) and whether one learner can be in several courses.
- **Attempts:** the teacher sets how many attempts a test allows (for example 2). **The last attempt counts.** The reason: a learner
  whose test broke off for a technical or private reason can take it again. Every attempt is kept and shown to the teacher.

## Decided by the teacher (17 November, third round)

- **One timer for the whole test**, not a time per question.
- The learner sees their **mistakes with the explanations at once after their own test** (not only after the deadline).
- The **pass mark is shown before the test** starts.
- **After the deadline the test can still be taken**, and the attempt is marked **late** (shown to the teacher).
- **Replacing a single question: the teacher picks from a list** (tasks of the same topic and level that are check / use tasks; show
  the kind and the full text so she can judge).

## Still open: ask the teacher

1. Can one learner be in **several WordPress courses** at once (then a learner belongs to several groups)?
2. What happens to a saved test when one of its tasks is **paused (reported) or corrected** later: keep the old version for that test
   (recommended, results stay comparable) or swap in the corrected one?
3. Whether a **late** attempt counts the same as one in time for the pass mark (recommended: yes, only the mark *late* is added).

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
