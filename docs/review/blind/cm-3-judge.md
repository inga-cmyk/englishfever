# Judge: blind round cm-3 (the 4 tasks changed after cm-2), 27 November 2026

Same rules and checks as in `cm-1-judge.md` and `cm-2-judge.md`.

**Totals (4 flags): KEEP 1 · ADD ANSWERS 3 · REWRITE 0 · DROP 0.** No full rewrite is needed. Nothing goes to the teacher.

---

## cm-3-001 · Correct the mistake. Keep *yesterday*: I have seen this film yesterday, so let's watch something else tonight.
**ADD ANSWERS.** `Grader::norm` does not treat *let's* and *let us* as equal. It expands only *n't, 'm, 're, 've, 'll*, and
*Grader.php* has no *let's* rule. *let us* in a suggestion is formal but correct ("less natural is not wrong"), and it changes
nothing the task is about. I add it here rather than in `norm`: a general *let's = let us* rule would also join *let us* in
the sense of *allow us* (*They let us stay*), which is not my file to change.
- Add:
  - `I saw this film yesterday, so let us watch something else tonight.`
  - `I watched this film yesterday, so let us watch something else tonight.`

## cm-3-002 · Will I turn on the heating? It's very cold in here.
**KEEP.**
- *Do you want me to …?* (both readers, and in cm-2 too) rebuilds the question instead of replacing *Will*. Every one-word fix
  (*Shall / Should / Can / Could / May*, both particle orders) is accepted, so a learner who knows the point is never marked
  wrong.
- *put the heating on* changes a correct word (*turn*), so it is not accepted.
- **Level.** *Shall I …?* for offers is an A2.1 point in `GRAMMAR-MAP.json` (Murphy 21-22, test-english A1, English Grammar
  Profile A2). It has its own A2.1 card and 16 check tasks, so learners meet it before this task. A learner who does not know
  *shall* can still answer with *Can I …?*, which is accepted.

## cm-3-003 · It's late. I walk you to the bus stop.
**ADD ANSWERS** (with an answer note); **no rewrite.** The readers are right that the key covers some offers but not all of
them. The fix is to accept every correct offer, not to narrow the instruction:
- *Keep *I*:* would not help. *Shall I walk you …?* and *I'm going to walk you* both keep *I*.
- *Add one word:* would bring in *I could / should / must walk you*.

*Shall I / Should I walk you to the bus stop?* fix the same mistake (a bare *I walk* as an offer) as a question offer. They
join *I can* and *Let me*, which are already accepted.

**Still not accepted:**
- *I'm going to walk you*. For this point it is the mistake itself. *It's late* shows a decision made now, Murphy 21 and 23
  give *will* for that, and the grammar map lists *I'm going to answer it* as an instant decision as this point's typical
  error.
- Reader 2's *It's late, so I'll walk you …* adds a word to a correct part. A learner who types only *I'll walk* is accepted
  by `correctedPart`.

Add:
- `It's late. Shall I walk you to the bus stop?`
  - Note EN: Also correct: *Shall I …?* makes the offer a question. As a statement, the offer needs *will*: *I'll walk you*.
  - Note LV: Arī pareizi: *Shall I …?* piedāvā ar jautājumu. Apgalvojumā piedāvājumam vajag *will*: *I'll walk you*.
- `It's late. Should I walk you to the bus stop?`
  - Note: the same EN / LV note as for *Shall I*.

## cm-3-004 · I can't go out until the plumber will come, so could you buy some bread?
**ADD ANSWERS**, and **one note corrected.**
- *will come* is the wrong word itself, so replacing it with another present verb of the same meaning (*arrives*, *gets here*)
  fixes the same mistake the same way. This is the same reasoning as *I watched* in cm-2-006.
- *the plumber's come* is *has come* with *'s*, which `norm` does not expand, so it must be listed.
- **The existing EN note for *has come* is wrong.** It says *the plumber's visit will be over*, but *until he has come* means
  until he is here, not until he has left. The LV note was right.

Add:
- `I can't go out until the plumber arrives, so could you buy some bread?`
- `I can't go out until the plumber gets here, so could you buy some bread?`
- `I can't go out until the plumber has arrived, so could you buy some bread?`
  - Note EN: Also correct: *has arrived* says the plumber will already be here.
  - Note LV: Arī pareizi: *has arrived* saka, ka santehniķis jau būs ieradies.
- `I can't go out until the plumber's come, so could you buy some bread?`
  - Note EN: Also correct: *'s come* = *has come*: the plumber will already be here.
  - Note LV: Arī pareizi: *'s come* = *has come*: santehniķis jau būs atnācis.
- `I can't go out until the plumber's arrived, so could you buy some bread?`
  - Note EN: Also correct: *'s arrived* = *has arrived*: the plumber will already be here.
  - Note LV: Arī pareizi: *'s arrived* = *has arrived*: santehniķis jau būs ieradies.

Change the note on the existing answer *… until the plumber has come …*:
- EN: Also correct: *has come* says the plumber will already be here.
- LV: unchanged (Arī pareizi: *has come* saka, ka santehniķis jau būs atnācis.)

---

## Small things seen in the key (not flags, no new round needed)
The LV pass formats some italics in a way that is untidy but not wrong:
- 001: *I have seen.* has the full stop inside the italics.
- 003: *will, I'll walk you* is one italic run.
- 002: *Shall I* …? leaves the dots outside the italics.

Whoever maintains `lv_fix` may want to look. The tasks are fine.

## For whoever records this
- 001 only adds accepted answers, so it can be recorded with `record-current` under the 14 November exception.
- 003 and 004 also add or change answer notes, so they may need a check under the same exception. The answers themselves only
  widen the key.

## Questions for the teacher
None.
