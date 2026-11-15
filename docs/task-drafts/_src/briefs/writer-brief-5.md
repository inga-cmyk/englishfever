# Brief for a task writer: batch 5 (points with 1-9 counted tasks, filled up to 10), 15 November 2026

Read `docs/task-drafts/_src/briefs/writer-brief.md` first and follow ALL of it (the reading list, the hard rules, the checks).
This file changes only what is different in batch 5. Where the two disagree, this file wins.

## What is different
1. **How many.** Your point already has some tasks that count (*check* + *use*). You write exactly **N** new tasks (N is given
   in your prompt) so that the point reaches 10. Every one of them must count: no matching, no `learning_task()`, no
   *Which sentence means …* / *What does … mean?* questions (those are learning tasks), no word order where only one verb is put in.
2. **Read what the point already has.** `grep "^POINT," docs/GRAMMAR-MAP-TASKS.csv` lists the existing tasks with role and kind
   (the last column is the task's key: topic, level, kind, question, answer). Do not repeat a sentence, and fill what is missing:
   when the point has no *use* tasks, most of yours are typed gaps and whole sentences; when it has no *check* tasks, most are
   choices, word banks and orders.
3. **The mix** (out of N; change it only with a reason in the notes): about 3 in 10 choice (`mc`), 2 word order (`od`),
   2 word bank (`gp(..., bank=[…])`), 2 typed gap (`gp` without bank), 1 whole sentence (`tx`). With N ≤ 3 choose the kinds the point
   lacks. Use a kind only if it tests the point: a word order only where putting the words in order needs the point (where the
   words go, which form follows which word); for a spelling or a single-word choice (plurals, *a / the*), use gaps and choices.
4. **The wording.** Write *Which sentence has a mistake?* (not *… is NOT correct?*): four sentences, three correct and about
   three different things, one with a mistake of THIS point.
5. **The level** is the point's level on the map (given in your prompt), also where the topic did not have that level in the app
   before (the teacher decided on 15 November to add it with prepared tasks only). A2.1 means short, everyday sentences (5-8
   words) and only grammar a beginner of A2 knows; do not use a tense or a form that is taught later.
6. **Files** (the only two you create):
   - `docs/task-drafts/_src/gp5_POINT.py`, starting
     ```python
     """Batch 5, point POINT (LEVEL): N tasks to reach 10 counted tasks. Murphy unit N."""
     from lib import gp, od, mc, tx
     T = "TOPIC SHORT NAME"
     L = "LEVEL"
     ```
     then the N calls, no `save()`.
   - `docs/task-drafts/_src/gp5_POINT-notes.md`: the mix and why; the Murphy unit; per task one line *what must the learner know
     to get this right, and why the wrong options compete*; card lines needed (EN and LV), if any; doubts.
7. **Check** exactly as in the batch 4 brief, with `gp5_POINT` and `pending/zz5-POINT.csv` (delete the CSV afterwards).

Report back (short): the file names, N and the mix, the card lines needed, doubts.
