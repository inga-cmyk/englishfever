# Batch 5, point `a_the` (A2.1), topic Articles: notes

**Murphy:** *English Grammar in Use*, unit 72 (*a* and *the*: *a* when we say something for the first time, *the* when it is clear which one, because we have already talked about it). Nothing from units 73 to 77 (the only one is used only as one correct sentence in task 1).

**What the point had:** 5 *check* tasks (2 word orders, 1 choice, 2 word banks / gaps at A2.2 to B1.1) and **no *use* task**. So 3 of the 5 new tasks are written by the learner.

**Mix (N = 5):** 1 choice, 1 word bank, 2 typed gaps, 1 whole sentence. No word order: for a single-word choice like *a / the* the brief says gaps and choices; the point already has two word orders. The second choice of the standard mix became a typed gap because the point has no *use* tasks.

**Level A2.1:** 5 to 9 words per sentence, two short sentences where the second mention needs one; only *be*, *have* and the past simple (on the app's A2.1 list).

## Task by task: what the learner must know, and why the wrong options compete
1. *Which sentence has a mistake?* → *I ordered a pizza. A pizza was cold.* The learner must see that the second time the pizza is known, so *The pizza*. The three correct sentences are about three different things: a job with *an* (*an engineer*), an uncountable noun in general with no article (*coffee*), the only one (*The sun*). Each looks like a place where a learner might suspect a mistake (*an* / no article / *the*), so they compete.
2. Bank *There was ___ wallet on my seat on the bus. ___ wallet was empty.* (a / The / A / the) → *a / The*. *There was* introduces something new, so only *a* fits the first gap (*There was the wallet* is wrong as a statement); that closes the one risky combination *the … The*. *A wallet was empty* is exactly this point's mistake (*a* at the second mention). All four chips are real words; the wrong combinations (a + A, the + The, the + A) are all wrong here.
3. Typed *Complete with a, an or the: My sister has ___ new job. ___ job is in Riga.* → *a / The*. First mention after *has* (*has the new job* has nothing to refer to), second mention *The job*. Naming the three words in the instruction stops *her job* / *This job*.
4. Typed *Complete with a, an or the: We rented ___ car in Spain. ___ car was very small.* → *a / The*. Same rule in another setting (travel; task 3 is work). Typical mistakes refused: *the car … The car* (no earlier mention), *a car … A car*.
5. *Correct the mistake: I bought a new laptop. A laptop is very fast.* → *The laptop is very fast.* Also accepted: *It is / It's very fast.* (the same correction with a pronoun; the checker cannot work out *'s*, so it is listed). There is only one mistake: *a new laptop* is the first mention and right.

Settings in order: food (restaurant), travel (bus), work, travel (car hire), technology; no two in a row the same.

## Card lines
None needed. The *use* line already says "*a / an*: one of many, or the first time we mention something" and "*the*: something both people know, something already mentioned", and the v2 card has "First time *a*, second time *the*: I saw a dog. The dog was huge." No task repeats the card example (*jacket*, *dog*, *film*).

## Checks run
`check_draft.php`: 5 accepted, 0 refused, 7 typed variants, 0 refused. `option_audit.py`: 0 flagged. `draft_rules_test.py`: 0 problems. CSV deleted.

## Doubts
- The typed instruction *Complete with a, an or the:* is the house wording for Articles (`GAP_INSTR`); I wrote it in the task so that `lib.py` does not add it and fill the *replaces* column for a task that never existed.
- Task 5 accepts *It is very fast*. If the lead wants the correction to keep the noun only, remove the two *It* answers; I think a learner who writes *It* has shown the point (the second *a* is wrong) and should not be marked wrong.
- Latvian explanations were reworded until `italics.lv_mark` marked no Latvian word as English (*pirmoreiz*, *otrreiz*, *kuru*, *nopirku* were marked), so no `LV_BY_FILE` entry is needed.
