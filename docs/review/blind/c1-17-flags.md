# Blind check c1-17: flags for the judge

3 tasks, 2 readers.

## c1-17-001 · C1 · gap · c1-part-1.csv:12

Task: ___ with the other candidates, she was clearly the strongest. (compare)
Key: {"kind": "gap", "accepted": [["Compared", "When compared"]]}
- reader 1: another correct answer, not accepted: [['Being compared']]
- reader 1: instruction: Only one gap but 'when compared' (two words) would also fit; unclear whether one word is wanted. 'Being compared' is correct but less natural.
- reader 1: level: Compared with/to is B2 rather than C1; a B2 learner solves it from the given verb.
- reader 2: another correct answer, not accepted: [['If compared']]
- reader 2: instruction: Hint (compare) plus 'with' gives away the form; only one word to supply.
- reader 2: level: Reduced participle clause is fine for C1 but the task is only form-filling, B2-ish.

## c1-17-002 · C1 · text · c1-perf-1.csv:14

Task: Report what she said with *deny* and *having*. Her words: 'I didn't read the letter.'
Key: {"kind": "text", "accepted": [["She denied having read the letter.", "She denied having read it.", "She denied ever having read the letter.", "She has denied having read the letter."]]}
- reader 1: another correct answer, not accepted: ['She denies having read the letter.']
- reader 1: instruction: Naming 'having' gives the structure away; the reporting tense (denied/denies) is not specified, so both fit. Verb and 'having' in the given order make it near copy work.
- reader 1: level: deny + having done is a B2 pattern; low for C1.
- reader 2: another correct answer, not accepted: ["She denied having read the letter. (with 'that' clause not allowed by instruction)", 'She had denied having read the letter.', 'She denies having read the letter.', 'She denied having read the letter that day.']
- reader 2: instruction: Names both deny and having, so the structure is given away; only copying/transforming needed. Does not say whether the reporting verb is past or present (denied/denies both fit).
- reader 2: level: Reporting with deny + having done is B2; C1 would need a nuance choice.

## c1-17-003 · C1 · mcq · c1-pres-2.csv:3

Task: In this story, which verb gives the background, not an event that moves the story on? So I'm sitting on the train, this man opens a bag of crisps, everyone turns round, and he just smiles.
options: opens | turns round | smiles | 'm sitting
Key: {"kind": "mcq", "correct": "'m sitting", "wrong": ["opens", "turns round", "smiles"]}
- reader 1: instruction: 'gives the background, not an event that moves the story on' is abstract wording, but understandable. The narrative present makes it harder to see.
- reader 1: level: Task is about continuous vs simple in narrative; fine for C1, though quite easy once the continuous form is spotted.
- reader 2: instruction: Wording 'gives the background, not an event that moves the story on' is clear but long; 'opens' and 'smiles' are all events so fine.
- reader 2: level: Narrative present with continuous background is fine for C1 but a B1 learner could solve it (the only continuous form).

