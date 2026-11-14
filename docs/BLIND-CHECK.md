# Blind check: every task is solved by readers who do not see the key (teacher, 14 November)

Goal: the teacher should not have to read tasks to find mistakes. Every task the app can serve is checked by independent
readers who see it **as the learner sees it** (no key, no explanation), and a script compares what they found with the key.
Only what a third reader cannot decide goes to the teacher.

## What every reader checks (the teacher's criteria, 14 November)
For each task, at its level (A2.1 … B2.2; C1 tasks are B2.2):
1. **Answer.** Solve it. Write the answer you would give.
2. **Other correct answers.** Every other answer that is correct English for this instruction and context (another tense, word,
   word order, chip combination, matching). "Less natural" is not wrong; say so.
3. **Wrong options that fit.** Any wrong option or chip that is correct English here.
4. **Instruction.** Is it natural and meaningful English? Is there a description or situation the task does not need (cover it:
   if only one option is still possible English, it is superfluous)? Does it give the answer away (the form named, the words
   given, a hint that only needs copying)? Is it clear what to do?
5. **Level.** Do the grammar point, the vocabulary and the sentence length fit the level (A2: about 5-9 words, one clause,
   everyday words; B1: about 10-16 words, two clauses; B2: wider vocabulary)? Is the form taught at that level?
6. **Sense.** Is the model sentence natural, adult and logical? Do the wrong options make sense as believable mistakes?

## How it runs
1. `python3 tools/blind_check.py export NAME [--hard] [--src FILE.csv ...] [--keys KEY ...]` writes
   `docs/review/blind/NAME-tasks.json` (what the readers see: no answers) and `NAME-key.json` (kept from the readers).
2. Two readers (agents that did not write the tasks) each read `NAME-tasks.json` and write `NAME-reader1.json`,
   `NAME-reader2.json`: one object per task id with the fields of the list above.
3. `python3 tools/blind_check.py compare NAME` compares both readers with the key and writes `NAME-flags.md`: a task is flagged
   when a reader's answer is not accepted, a reader finds another correct answer or a wrong option that fits, a reader marks the
   instruction or the level, or the two readers disagree.
4. A third reader (the judge) decides every flag against Murphy and the rules (`docs/ITEM-WRITING-RULES.md`): fix the task, or
   say why it is right. Only flags the judge cannot decide go to the teacher, as one question each.
5. `python3 tools/blind_check.py record NAME` writes a record for every task that passed or was fixed
   (`docs/review/blind/records.json`, keyed by a hash of the task's content: text, answers, options, level).

## The gate
`app/tests/item_gates_test.py`, gate `blind`: a task without a record stops the packaging. The tasks that existed when the gate
was added are its baseline (to be checked in rounds, the most served first); a new or changed task has a new hash and needs
its own record. Changing a task after its check (even one word) means checking it again.

## Learner data (the second mechanism)
Tasks that learners answer wrongly in the same way, or far below their level, are found from the research export and checked
first (`--hard`). The app pauses a reported task until it is decided (`Reports::pausedIds`).
