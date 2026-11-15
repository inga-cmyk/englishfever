# Batch 5, point `could_past` (A2.2), topic Modal verbs (`modal_verbs`)

Source file: `docs/task-drafts/_src/gp5_could_past.py` (7 calls, no `save()`).
Grammar: Murphy unit 26 (A: *could* = past of *can* for general ability, *My grandfather could speak five languages*;
C: *couldn't* for general ability and for one particular situation, *I couldn't sleep*). The one-success contrast
(*was able to / managed to*, point `able_once`) is B1 and is kept out: every affirmative *could* here is a general ability.

Topic: `modal_verbs` (has A2.2; its card teaches *could* in the past: "In the past: *could* and *had to*", *I could swim
when I was five*). `more_modals` also has A2.2, but its A2.2 tasks are *might / may*, and its typed gaps get the automatic
instruction *Complete with a suitable modal verb* (a grammar term). No sentence repeats the card's example.

## Mix (N = 7) and why
2 choice, 2 word order, 2 word bank, 0 typed gap, 1 whole sentence. The point already has 3 *use* tasks, all typed gaps
(*couldn't come*, *could swim*, *couldn't play*) and no *check* task, so the typed-gap slot of the standard mix went to the
check kinds and one whole sentence. After this batch: 6 check, 4 use.

## What the learner must know, and why the wrong options compete
1. *It was very hot, so I ___ sleep last night.* couldn't / can't / didn't could / couldn't to: *last night* needs the past
   of *can*; *can't* (present), *didn't could* (the typical *did* + modal error) and *couldn't to* (*to* after a modal) are
   the three typical mistakes of the point.
2. *Which sentence has a mistake?* *When I was ten, I can speak French.* (present *can* in a past time frame). The three
   correct ones are a particular *couldn't* (travel), *could* for a thing's ability (technology) and a *Could you …?*
   question (lifestyle); no near copy of the wrong one.
3. Order *we couldn't see the stage from our seats* (also with *from our seats* first): *couldn't* + base verb before the object.
4. Order *when i was younger i could run much faster* (also the clause second): the past time clause and *could* + base verb.
5. Bank *___ your parents ___ a car when they were young?* Could / drive (chips Can, drove): the question is *Could* +
   subject + base verb; *Can* is a real form wrong for the past (*when they were young*), *drove* is the past-form-after-*could*
   mistake. No *Did* chip, so *Did … drive* (also correct English) cannot be built.
6. Bank *As a teenager, Ben ___ ___ any song on the guitar.* could / play (chips can, played): *As a teenager* fixes the past;
   *can* and *could played* are the typical mistakes. Every chip pair other than *could play* is wrong.
7. Whole sentence *Make a yes/no question: Tom could speak German when he lived in Berlin.* → *Could Tom speak German …?*
   (typical mistake *Did Tom could speak …*). Also accepted: the clause first, and *Was Tom able to …?* (same meaning).

## Card lines needed
None: the `modal_verbs` card already has "In the past: *could* and *had to*" with *I could swim when I was five.* (EN and LV).

## Doubts
- Task 7 accepts *Was Tom able to speak German …?* although *be able to* is on the `more_modals` card, not on `modal_verbs`;
  it is correct and means the same, so refusing it would be wrong.
- Settings: lifestyle, mixed, hobbies (concert), sport, relationships, hobbies (guitar), travel; tasks 3/4 and 6 are hobbies
  but never two in a row of the same kind of scene.
- Checks: `check_draft.php` 7 accepted, 0 refused; `option_audit.py` 0 flags (a first version had the wrong sentence as the
  longest option in task 2: shortened); `draft_rules_test.py` 0 problems. Temporary CSV deleted.
