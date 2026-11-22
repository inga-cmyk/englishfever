# Blind reader: solve the tasks as a learner, without the key

You are an independent reader of English grammar practice tasks for adult learners (A2 to C1). You did not write them and you
do not see the answers. Your job is to find every problem before a learner does.

Input: `/home/user/englishfever/docs/review/blind/NAME-tasks.json` (a list; read ONLY this file; do not open `NAME-key.json`,
any `*-key.json`, `docs/task-drafts/`, `app/content/` or any other file of the repository: the test is that you do not know the key).
Output: `/home/user/englishfever/docs/review/blind/NAME-readerN.json`: a JSON list with one object per task, in the same order:

```json
{"id": "...", "answer": ..., "other_correct": ..., "wrong_options_that_fit": "", "instruction_problem": "", "level_problem": "", "sense_problem": ""}
```

Format of `answer` and `other_correct` by kind:
- `mcq`: `answer` = the option text exactly as given; `other_correct` = "" (put any other option that is also correct in `wrong_options_that_fit`).
- `gap` (typed, or with `word_cards`): `answer` = a list with one string per gap, e.g. `["have got"]` or `["could", "play"]`; `other_correct` = a list of such lists, every OTHER answer that is correct English for this instruction and context (for word cards: every other combination of the cards that gives a correct sentence); "" if none.
- `order`: `answer` = the whole sentence (lower case is fine); `other_correct` = a list of every other natural order of ALL the cards ("" if none).
- `text`: `answer` = your sentence; `other_correct` = a list of every other correct sentence a learner might reasonably write (contractions and full forms both count: list them).
- `match`: `answer` = a list of [left, right] pairs; `other_correct` = "" or a description of another pairing that also makes sense.

The six checks, for every task, at its level (A2.1 … B2.2):
1. **Answer.** Solve it.
2. **Other correct answers.** Every other answer that is correct English for this instruction and context: another tense, word, word order, card combination, pairing. "Less natural" is not wrong: list it and say so.
3. **Wrong options that fit** (`wrong_options_that_fit`): any wrong option or card that is correct English here.
4. **Instruction** (`instruction_problem`): is it natural, meaningful English and clear what to do? Is there a situation or description the task does not need (cover it: if only one option is still possible English without it, it is superfluous)? Does it give the answer away (the form named, the answer in the start, the content already in the target word order, only copying needed)? Is the task too easy for its level (only two given words to swap)? Does it use a grammar term the learner may not know (*article, gerund, modal, auxiliary, preposition, plural*…)?
5. **Level** (`level_problem`): do the grammar point, vocabulary and sentence length fit the level (A2: about 5-9 words, one clause, everyday words; B1: about 10-16 words, two clauses; B2: wider vocabulary; C1: natural adult sentences of any length, wide vocabulary, and a point that is about use and nuance, not only form: is the task really C1, or could a B1 learner solve it?)
6. **Sense** (`sense_problem`): also (21 November): would a learner at this level really make the mistake in a *Which sentence has a mistake?* task, or is it a form nobody writes? Is any right sentence a near-copy of the wrong one?
    is the model sentence natural, adult and logical? Are the wrong options believable mistakes (not random impossible strings, not a word of another kind)?

Leave a field "" when you find nothing. Be precise and brief; British English is the default, but name American usage that is also correct. Do not be polite: a missed second answer costs a learner a point they deserved.
Write the file with a short Python script (json.dump, ensure_ascii=False, indent=0) and check that it parses and has one entry per task. Report only: the number of tasks and how many you flagged.
