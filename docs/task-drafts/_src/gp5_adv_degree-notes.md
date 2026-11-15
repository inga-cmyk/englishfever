# Batch 5, point `adv_degree` (A2.2): notes

Source: `docs/task-drafts/_src/gp5_adv_degree.py`, topic *Adverbs: manner, frequency, degree*, level A2.2, N = 8.
The point already has 1 *use* (A2.2 text, *Correct the mistake: I very like this song.*) and 1 *check* (B1.2 word bank, *The test was ___ easy.*).
Grammar: Murphy, *English Grammar in Use*, unit 104 (*very / quite / really* + adjective, as the map gives), unit 109 (verb + object
stay together, *I like my job very much*, not *I like very much my job*), unit 110 (*really* in mid position, before the verb).

## Mix (8)
2 choice, 2 word order, 2 word bank, 1 typed gap, 1 whole sentence. One choice fewer than the brief's 3 in 10, one drag more:
together with the existing tasks the point then has 2 choice, 2 order, 3 bank, 1 typed gap, 2 typed sentences, and 50 % of
my tasks are drag tasks (rule 6: at least 40 %). Word order is used only where the order is the point (*very much* after the object,
*a very nice*).

## Decisions
- The point's core is where the degree word goes: before an adjective (*very nice, too heavy, quite small*), *really* before a verb,
  *very much* at the end. Every wrong option is one of the map's typical errors: *very* before a verb, *much very*, *too much / very much* + adjective.
- *quite* is only in a correct sentence of the *mistake* task: in a gap it competes with *very / really* and would make the gap open.
- *too* vs *very* (meaning) is the `too_enough` point and is not tested here; the bank task with *too* has no *very* chip.
- *I very much like my new flat* is correct (British, a little formal), so it is accepted in the word order.
- No card line needed: the card has *very, really, quite, too* + adjective and the mistake *I very like it → I like it very much*.

## Task by task: what the learner must know, and why the wrong options compete
1. *We enjoyed the cooking class ___.* very much / very / much / much very: *very* alone cannot follow a verb; *much* alone is not used
   in a positive sentence; *much very* is the wrong order. All three are what Latvian *ļoti* leads to.
2. *Which sentence has a mistake?* *We very enjoyed the concert.* (very before a verb); the others are correct and about three different
   things: *quite* + adjective (hotel), *really* + adverb (boss), *too* + adjective (soup).
3. Order *i like my new flat very much* (also *i very much like my new flat*): the learner must put *very much* after the object, not
   *like very much my flat*.
4. Bank *This suitcase is ___ heavy for me.* too / too much / very much: *too much heavy* and *very much heavy* are the map's typical errors; only
   *too* goes straight before an adjective.
5. Typed *My grandmother loves her garden very ___.* much: the learner must know the fixed *very much* after the verb and object (no other word fits).
6. Order *we had a very nice holiday*: degree word between *a* and the adjective (not *very a nice*, *a nice very*); no other order is correct.
7. Bank *I ___ like this podcast.* really / very / much: before a verb only *really*; *I very like* and *I much like* are the Latvian-driven
   mistakes. (*very much* is not a chip because *I very much like* is correct.)
8. Whole sentence *Say it another way with *really*: We liked the new restaurant very much.* → *We really liked the new restaurant.*
   The learner must move the degree to the front of the verb and drop *very much*.

## Card lines needed
None.

## Latvian marking
`lv_mark` marks *Tulkojot burtiski* as English unless the output file has it in `LV_BY_FILE` (as done for `gap-points-*.csv` in `lib.py`).
The lead agent should add `Tulkojot burtiski` to `LV_BY_FILE["<batch-5 file>.csv"]`. I avoided *tikai* (also marked).

## Doubts
- Task 1: a reader may call *We enjoyed the class much* "only less natural". Murphy (unit 87) says *much* is unusual in positive
  sentences; it stays as a wrong option. If the judge disagrees, replace *much* with *very well*.
- Task 3: accepting *I very much like my new flat*: correct, but less common; if the judge rejects it, remove it from `also`.
