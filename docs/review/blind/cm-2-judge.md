# Judge: blind round cm-2 (the 15 tasks changed after cm-1), 27 November 2026

Source: `docs/task-drafts/_src/correct_mistake_1.py` → `correct-mistake-1.csv`. Same rules and checks as in `cm-1-judge.md`
(Murphy, `ITEM-WRITING-RULES.md`, the rule cards, the grammar map, the bank and the drafts, `Grader::norm` / `correctedPart`).

**Totals (7 flags): KEEP 3 · ADD ANSWERS 2 · REWRITE 2 · DROP 0.** The 8 unflagged tasks pass. Nothing goes to the teacher.

Rejected answer kinds, as in cm-1: (b) **emphasis added** (*I do think*, *It all depends*, *It does depend*); (e) **a new
structure** around the same idea (*Light is faster than sound*, *Do you want me to …*, *Would you like me to …*).

---

## cm-2-003 · I'm thinking this plan is too expensive for us, so let's look for another one.
**KEEP.** *I do think* is kind (b). The key already has *I think* and *I think that*.

## cm-2-004 · Light is travelling faster than sound, so you see the lightning before you hear the thunder.
**KEEP.** *Light is faster than sound* is kind (e): it removes the verb instead of correcting its form. The task is about
*travels* (a fact) versus *is travelling* (now). A learner who knows the point types *travels*, and with `correctedPart` can
type only that word.

## cm-2-005 · It's depend on the traffic, so I can't say what time I'll be home.
**KEEP.** *It all depends* and *It does depend* are kind (b): both readers' answers add emphasis that the sentence did not have.

## cm-2-006 · I have seen this film yesterday, so let's watch something else tonight.
**REWRITE** (instruction only) **and one added answer.** The readers are right. Deleting *yesterday* (*I've seen this film, so
let's watch something else tonight*) fixes the same clash from the other side, and the sentence is just as natural. I called
it kind (c) in cm-1, but that was wrong here: the time word is the only thing in conflict, so both fixes are equally
reasonable. The 3 November rule says to name what to keep. *I watched this film yesterday* is the same correction (past
simple with *yesterday*) using the other everyday verb for films, so it is accepted. The point is *pp_ps* (present perfect or
past simple), not irregular forms.
- Sentence: `Correct the mistake. Keep *yesterday*: I have seen this film yesterday, so let's watch something else tonight.`
- Accepted: `I saw this film yesterday, so let's watch something else tonight. | I watched this film yesterday, so let's watch something else tonight.`
- EN: *yesterday* is a finished time: past simple (*I saw*, *I watched*), not *I have seen*.
- LV: *yesterday* ir pabeigts laiks: Past Simple (*I saw*, *I watched*), nevis *I have seen*.
- Point unchanged: `pp_ps`.

## cm-2-009 · Will I turn on the heating? It's very cold in here.
**ADD ANSWERS.** Reader 1's *Shall I turn the heating on?* only moves the particle. That is a natural second order that changes
nothing the task is about, so it is accepted with every modal already in the key. *Do you want me to …?* and *Would you like me
to …?* are kind (e): they rebuild the question instead of replacing *Will*. Reader 2's level note says the task is fine (*Shall
I* is an A2.1 point).
- Add:
  - `Shall I turn the heating on? It's very cold in here.`
  - `Should I turn the heating on? It's very cold in here.`
  - `Can I turn the heating on? It's very cold in here.`
  - `Could I turn the heating on? It's very cold in here.`
  - `May I turn the heating on? It's very cold in here.`

## cm-2-010 · It's late. I walk you to the bus stop.
**ADD ANSWERS** (with an answer note). Four readers in two rounds gave *Let me walk you to the bus stop*. It is the most natural
way to make this offer, and it changes the one word that causes the mistake (the bare *I walk*). The key already accepts *I
can*, which shows the offer without *will*, so *Let me* belongs with it. *I'm going to walk you* (both readers: "less natural")
is not accepted: *going to* is a plan made before, not an offer made now (Murphy 21, 23; the map's error *I'm going to answer
it* as an instant decision).
- Add: `It's late. Let me walk you to the bus stop.`
  - Note EN: Also correct: *Let me walk you* is an offer too. With *I*, the offer needs *will*: *I'll walk you*.
  - Note LV: Arī pareizi: *Let me walk you* arī ir piedāvājums. Ar *I* piedāvājumam vajag *will*: *I'll walk you*.

## cm-2-013 · Are you going to sell your old car or you are going to keep it?
**REWRITE** (new sentence, new point). Both readers are right. At B1.1 the only change is one inverted *are* in a long, repeated
frame, and statement order after *or* is not a mistake the grammar map lists for B1.1. *going to* already has three A2 tasks in
this round (019, 020, 024). The new task tests a real B1.1 Future error from the map instead: *will* after *until*
(fut_time_clause, TIME-CLAUSE: *I'll wait until she will come*). Not about rain: B1.2 *Let's wait here until the rain will stop*
already exists in `b1-new-2.csv`. Not *as soon as*: cm-1-025 uses it. The new sentence was checked against the bank and the
drafts with no hit, and it is not a card example (the card has *When I will get home, I'll call you*).
- Sentence: `Correct the mistake: I can't go out until the plumber will come, so could you buy some bread?`
- Accepted: `I can't go out until the plumber comes, so could you buy some bread? | I can't go out until the plumber has come, so could you buy some bread?`
- Answer note on *has come*: EN *Also correct: *has come* says the plumber's visit will be over.* · LV *Arī pareizi: *has come* saka, ka santehniķis jau būs atnācis.*
- EN: After *until* we use the present, also about the future: *until the plumber comes*, not *will come*.
- LV: Aiz *until* lieto tagadni, arī runājot par nākotni: *until the plumber comes*, nevis *will come*. Latviski *kamēr atnāks* ir nākotnē, tāpēc gribas *will*.
- Point: `fut_time_clause` (was `going_to`); error type `TIME-CLAUSE`; level B1.1 (unchanged).
- (*until the plumber arrives* changes the verb: not accepted. *won't go out* or *can go out* change a correct part.)

---

## Unflagged tasks
001, 002, 007, 008, 011, 012, 014 and 015: **KEEP** (no reader flag; the cm-1 changes work as intended).

One thing for whoever applies this (not a task problem): the key of **cm-2-007** lists the auto-generated answer *Next year
We're going to get a dog.* with a capital *W*. Grading is not affected (`Grader::norm` lowercases), but if accepted answers are
ever shown, it would display wrongly. The fronting in `auto_answers.py` should lowercase the old first word (except *I* and
names).

## Questions for the teacher
None.
