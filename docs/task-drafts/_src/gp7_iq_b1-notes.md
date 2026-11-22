# Indirect questions B1: the learner makes the form (tester, 22 November)

The tester did all 20 B1 *Indirect questions* tasks as a guest: 20/20. Her verdict: fine as practice for early B1, but a
strong B1 learner finds most of them easy, because they mean choosing the right word order or matching cards by keywords.
She asked for tasks where the learner (1) turns a direct question into an indirect one himself, or (2) writes his own
polite question in a situation, with no start given. Grammar: Murphy unit 50 (*Do you know where …? / Could you tell me
if …?*), unit 13 for the past (*What did he say?* → *what he said*). Card: `ind_polite`. Every form used is on that card
(statement order, no *do / does / did*, *if / whether*, the question mark after *Could you tell me…? / Do you know…?*).

## A. `gp7_iq_b1.py`: 8 typed whole sentences (`tx`), 4 B1.1 + 4 B1.2
Each task gives a short adult situation and the direct question in quotes, with *Could you tell me* or *Do you know* as the
start. The learner has to change something real every time. The sets below spread the changes:

| Level | Setting | Direct question | What changes | Point |
|---|---|---|---|---|
| B1.1 | hotel reception | What time does breakfast start? | *does* goes, *-s* on the verb | iq_wh |
| B1.1 | IT help desk | How can I reset my password? | subject before *can* | iq_wh |
| B1.1 | clothes shop | Does this jacket come in a larger size? | *if / whether*, *does* goes, *-s* | iq_yn |
| B1.1 | car rental | Is insurance included in the price? | *if / whether*, subject before *is* | iq_yn |
| B1.2 | doctor's surgery | Has my test result come back yet? | *if / whether*, subject before *has* | iq_yn |
| B1.2 | work, client meeting | What did the client say about our offer? | *did* goes, past on the verb (*said*) | iq_wh |
| B1.2 | optician's | When will my new glasses be ready? | subject before *will* | iq_wh |
| B1.2 | evening class | Did the teacher give us any homework? | *if / whether*, *did* goes, *gave* | iq_yn |

- **Accepted answers** (72 to 768 a task, 2556 in all; `check_draft.php`: 0 refused) are built by `forms()`. That covers
  both starts, *Could you please tell me*, *Do you happen to know*, *…, please?*, *Excuse me,* in front, *if* and *whether*,
  the *'s* contraction (the grader reads *n't / 'll / 're* itself but not *'s*), and the small natural variants of the core:
  *when / what time breakfast starts / begins / is*, *how to reset my password*, *if it comes / you have it in a bigger size*,
  *if the price includes insurance*, *my test results have*, *what they said*, *when my glasses are going to be ready*,
  *if we got / have any homework*. The grader ignores capitals, commas and the final punctuation, so the question mark is
  shown in every answer but a full stop does not fail. *if the teacher has given us any homework* is accepted too. Like
  *will run* in gp6, it has its own answer note: correct, it asks about homework until now, but *gave* is closest to *did*.
- **Not in the bank:** grep for each core in `app/content/items.json`, `docs/task-drafts/*.csv` and `app/authoring`. *How long
  will the repair take?* was already in two tasks (reported and polite), so the optician's glasses replaced it.
- **The 21 November rule says to use situations instead of quoted questions in writing tasks.** That rule was about tasks where
  the instruction already gave the indirect order (*Ask … where the meeting room is*). Here the quote is the direct question,
  and a rewrite is what the tester asked for. The `copy` gate passes, because no answer can be copied from the instruction. Two
  tasks only move the verb (*can*, *will*). Unlike the bad example *'Where is the toilet?' Could you tell me where ___ ___?*,
  the learner types the whole sentence with no frame.
- `POINT_OF` maps each row to its point (`iq_yn` if the answer has *if / whether*, otherwise `iq_wh`). **For the lead:** add
  `import gp7_iq_b1` to `iq_b1_6.py`, and in `point_of()` also check `gp7_iq_b1.POINT_OF` (its row indexes are absolute in
  `lib.rows`, as with gp6_iq_extra). Then add the tasks to `assign_keys.json` and run a blind round. Those two are the only
  gate failures, as expected for new tasks.
- Checks I ran on a temporary CSV, deleted afterwards: `check_draft.php` 8 accepted, 0 refused. `option_audit.py` 0 flagged.
  `draft_rules_test.py` 0 problems. `latvian_lint.py` found nothing new. `item_gates_test.py` failed only `point` and `blind`.

## B. `/tmp/claude-0/iq7_write.json`: 3 open writing tasks, `ind_polite`
Each has the fields of the built-in `ip-B12-6a` (`q`, `must`, `model`, `why`, `why_lv`) plus `level`, `skill`, `tests_ok`
and `tests_bad`. None gives a start. The instruction is the situation + *Write one polite question.*
- B1.1: a scarf left at a restaurant (model *Could you tell me if my scarf is still at the restaurant?*)
- B1.1: when an evening Italian course starts (model *Could you tell me when the next Italian course starts?*)
- B1.2: a printer ordered ten days ago that has not arrived (model *Could you tell me if you have sent my order yet?*)

The three `must` regexes are the same for all three tasks. Only the hints differ.
1. A polite opener: *Could / Can / Would you (please) tell me / let me know / check / find out / confirm*, *Would you mind
   telling me / checking*, *Do you (happen to) know*, *I'd / I would like to know*, *I wonder / I was wondering*.
2. Right after the opener verb (an optional *, please,* may come between), *if / whether* or a question word.
3. Statement order: no *if / whether / question word* (also *what time*, *how long*, *which day*, *how many days* …) directly
   followed by an auxiliary (also *hasn't, didn't, won't* …) and then a subject word (*you, it, the, my, there, anyone* …).

Tested in Python (`re.I`) and in PHP (`preg_match` with `~…~iu`, as `Grader::rx`), curly apostrophe included. All 28 correct
sentences pass and all 30 wrong ones fail. They are in the JSON. Known limits: a wrong tense after removing *did* (*if anyone
find my scarf*) is not caught, like in ip-B12-6a. A subject question with *has + my* (*who has my scarf*) would be refused
(rare). These tasks are meant to replace or sit next to the built-ins, so the lead decides the ids and how they go into
`content_review.py` / `write_fixes.py`.

## Card lines
None needed: every form a task requires is on the `ind_polite` card. Optional: the write tasks also accept *I was wondering if…*
and *Could you check if…*, which the card does not name. The hints name only card forms (*Could you tell me / Do you know /
I'd like to know*).
