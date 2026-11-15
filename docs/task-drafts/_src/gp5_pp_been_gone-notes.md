# Batch 5, point `pp_been_gone` (A2.2): notes from the writer

Topic: Present perfect (`present_perfect`), level A2.2. N = 10 (the point had 0 check, 0 use, 1 learning task:
*Choose the correct meaning: 'Mum has gone to the shop.'*). Grammar checked against Murphy, *English Grammar in Use*, unit 7
(*been to* = went and came back; *gone to* = is there now or on the way; *been* for visits that are over, also counted).
Generator: `docs/task-drafts/_src/gp5_pp_been_gone.py` (10 calls, no `save()`).

Checks: `check_draft.php` 10 accepted, 0 refused (8 typed variants, 0 refused); `option_audit.py` 0 flagged;
`latvian_lint` and `draft_rules_test` on this file only: 0 problems. No model sentence repeats one in `app/content/items.json` or
`docs/task-drafts/*.csv` (checked *car wash, to the gym, cinema twice, Rita has gone*; the existing *Tom isn't here. He ___ to Spain.* is not reused).

## Mix (changed, with a reason)
3 choice, 0 word order, 4 word bank, 2 typed gaps, 1 whole sentence.
Word order was dropped: the point is a choice between two words (*been / gone*) that sit in the same place, so putting tiles in
order never needs it (the brief: a word order only where the order needs the point). The two order slots went to word banks,
where *been / gone / went* compete as chips; drag tasks stay at 40 % (rule 6 of `ITEM-WRITING-RULES.md`).
Answers are balanced: 5 x *gone*, 4 x *been*, 1 mistake task.

## Each task: what the learner must know, and why the wrong options compete
Every task gives one short situation that says whether the person is back or still away; it is needed (cover test: without it,
*been* and *gone* are both correct English in most of these sentences, e.g. a note *I've gone to the gym*).
1. *The office is empty. Everyone ___ home.* has gone: people not here now. *has been* (they would be back) is the point's mistake; *has went* the common form mistake. *went home* (correct) is not offered.
2. *I've ___ to the gym. I feel great now.* been: the speaker is back and talking. *gone* (still there) and *went* after *have*.
3. *Which sentence has a mistake?* *My parents have gone to Italy twice.* Counted visits are over, so *been* (Murphy 7; the map's typical error *He's gone to Rome twice*). The other three are correct and about different things: an *ever been* question, *has gone home* (person away), a present perfect with *this year*.
4. *Write been or gone: We have ___ to the cinema twice this month.* been: *twice* counts finished visits.
5. *Write been or gone: Dan's ___ to a football match. He'll be back at ten.* gone: not back yet.
6. Bank *Where's Oskars? He ___ ___ to the airport to meet his parents.* has / gone; chips *been* (would mean he is back) and *went* (*has went*). No other combination is a sentence.
7. Bank *Your car looks so clean! Have you ___ to the car wash?* been: said to the person, who is here. *gone*, *went* (*Have you went*).
8. Bank *I can't call Lena now. She's ___ to bed.* gone; *been*, *went* (*She's went*).
9. Bank *Our friends are back from their holiday. They ___ ___ to Greece.* have / been; *gone* (contradicts *back*), *went* (*have went*).
10. Whole sentence *Start with Rita has and use go: Rita went to Tokyo, and she is still there.* Rita has gone to Tokyo (also with *and she is still there* / *and is still there*). *go* is named so that *has moved / has left for / has travelled to* are not open; *go* does not give the answer away: the learner must choose *gone* over *went* and *been*.

## Card lines needed
None. The Present perfect card already has: *been* = was there and came back, *gone* = is still there: *She's been to Paris. She's gone to Paris.* (Watch out), and *go → gone, be → been* in the form table.

## Doubts
- Task 3: *have gone ... twice* is wrong by Murphy 7 and by the map, but some American speakers say *I've gone there twice*. A blind reader may call it acceptable; I kept it because it is the typical error the map names. If the judge disagrees, replace it with *Kate has been to the shop. She's still there.*
- Task 10: *use go* names the verb, not the form; a reader could feel it narrows the task. Without it, *Rita has moved to Tokyo* would be another correct answer.
