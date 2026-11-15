# Batch 5, point `was_were` (A2.1): notes from the writer

Topic: Past simple (`past_simple`), level A2.1. Grammar checked against Murphy, *English Grammar in Use*, unit 10 (*was / were*)
and unit 12 (*did* is not used with *be*: *Were you …?*, not *Did you be …?*). Generator: `docs/task-drafts/_src/gp5_was_were.py` (6 calls, no `save()`).

## Mix and why
The point had 2 choices and 2 typed gaps (all A2.2). To make the ten follow the house mix (3 choice, 2 order, 2 bank, 2 typed gap, 1 sentence)
the 6 new tasks are: **1 choice, 2 word order, 2 word bank, 1 whole sentence**, no typed gap (the point already has two).
The point says "makes negatives and questions without *did*", and the existing four are all agreement (*we were*, *it was*, *Were you*):
so the new ones put the weight on questions and negatives (Did / didn't as the competing mistake) and keep one agreement task.

Checks: `check_draft.php` 6 accepted, 0 refused (2 typed variants, 0 refused); `option_audit.py` 0 flagged; `latvian_lint` 0 problems in this file.
No sentence repeats one in `app/content/items.json` or `docs/task-drafts/` (grep for each). The temporary CSV is deleted.

## Each task: what the learner must know, and why the wrong options compete
1. *Which sentence has a mistake?* **The concert tickets was expensive.** A plural noun takes *were* (*They was late* is the map's typical error). The three correct
   sentences are about three different things: a *Were you …?* question, a *weren't* negative, a *were* statement with *we*.
2. Bank *___ your parents at the wedding?* **Were**. *Was* is the agreement mistake (*your parents* = *they*), *Did* the typical *did* + *be* mistake (*Did you were there?*). Neither gives a correct sentence.
3. Bank *The shops ___ busy yesterday.* **weren't**. *wasn't* is the agreement mistake, *didn't* the *didn't* + *be* mistake (*The shops didn't busy* / *didn't be busy*). *were* is not in the bank, so only one chip fits.
4. Order *where were you at lunchtime*: question word + *were* + subject. No other natural order (*at lunchtime where were you* is not said; no fronting accepted).
5. Order *why was your phone off*: question word + *was* + subject; the statement order *why your phone was off* is the mistake. No other order.
6. Sentence *Make a yes/no question: The exam was difficult.* **Was the exam difficult?** (also *Was it difficult?*). The learner must move *was* to the front and not add *did* (*Did the exam be difficult?*).

## Decisions
- Both word orders are question-word questions on purpose. `lib.plain()` makes every word-order instruction *Put the words in order.* and `od()` then accepts the
  statement of a yes/no question (a first draft *was the hotel near the beach* also accepted *the hotel was near the beach*), so a yes/no order would not test the question form.
  A question-word question has no correct statement order with these cards.
- Settings in order: mixed (choice), relationships (wedding), shopping, work / daily life (lunchtime), technology (phone), learning (exam). 5-7 words each, A2.1 grammar only (no past continuous: *the lift wasn't working* avoided).
- *Did / didn't* chips: real words and the common learner mistake of this point (rule of 11 November), as in the existing choice *We ___ very tired* (wrong option *did*).

## Card lines needed
None. The Past simple card already has *was / wasn't / Was she there?* and *were / weren't / Were they late?* and the mistake *Did you were there?*. No task repeats a card example.

## Doubts
- The gate on bank chips that agree with the subject may list *Was* (task 2) and *wasn't* (task 3): here the agreement is the point, so they are believable mistakes, not chips rejected without the grammar.
- Task 6 also accepts *Was it difficult?* (pronoun for the noun); if the lead wants only the copied noun, remove that answer.
