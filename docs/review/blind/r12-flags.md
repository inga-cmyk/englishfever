# Blind check r12: flags for the judge

4 tasks, 2 readers.

## r12-001 · A2.1 · text · gap-points-a2-1.csv:46

Task: Your guest has just come in with a heavy coat. Offer to take it. Start with *Shall I*:
Key: {"kind": "text", "accepted": [["Shall I take your coat?", "Shall I take your coat for you?", "Shall I hang up your coat?", "Shall I hang your coat up?", "Shall I take it?", "Shall I take that for you?", "Shall I take your coat, please?"]]}
- reader 1: another correct answer, not accepted: ['Shall I take it for you?', 'Shall I take your heavy coat?', 'Shall I take the coat?', 'Shall I put your coat away?']
- reader 1: instruction: Open task: many correct endings, the checker must accept all. 'it' is unclear (which noun?) but fine. 'heavy' is not needed.
- reader 2: another correct answer, not accepted: ['Shall I take it for you?', 'Shall I take your coat from you?', 'Shall I take your jacket?', 'Shall I take that coat for you?', 'Shall I put your coat away?']
- reader 2: instruction: 'Heavy' is not needed; 'Offer to take it' is clear but open: many offers are possible (take, hang up), so the model answer is not unique. 'it' in the instruction gives 'take' away.

## r12-002 · B1.1 · gap · gap-points-b11-1.csv:12

Task: My course begins on Monday. When it ___, I'll have less free time. (start)
Key: {"kind": "gap", "accepted": [["starts", "has started", "'s started"]]}
- reader 1: another correct answer, not accepted: [['begins'], ['has begun']]
- reader 1: instruction: The cue (start) gives the verb but not the form; fine. 'has started' is possible English but odd after 'begins on Monday' (less natural). 'begins' also fits though the cue says start.
- reader 2: another correct answer, not accepted: [['begins'], ['has begun']]
- reader 2: instruction: The hint '(start)' gives the base form but the learner must change it (starts); 'begins' also fits if the hint is ignored. The grammar point (present after 'when' for future) is not named, which is good. 'it' and 'My course' are clear.
- reader 2: sense: 'begins ... When it starts' repeats the idea, fine and natural.

## r12-003 · B1.1 · text · gap-points-b11-1.csv:100

Task: Rewrite the sentence about last month. Start with *Last month*: I have to work every Saturday to cover for a sick colleague.
Key: {"kind": "text", "accepted": [["Last month I had to work every Saturday to cover for a sick colleague."]]}
- reader 1: another correct answer, not accepted: ['Last month I had to work every Saturday to cover for a colleague who was sick.', 'Last month I had to work every Saturday to cover for an ill colleague.', 'Last month I had to work every Saturday to cover for a colleague who was ill.', 'Last month I worked every Saturday to cover for a sick colleague.', 'Last month I had to work every Saturday to cover a sick colleague.']
- reader 1: instruction: Does not say which tense change is needed, but 'last month' makes it clear; 'Rewrite the sentence about last month' is slightly redundant. 'Last month I worked every Saturday' loses 'have to' (meaning changes a little) but is correct English.
- reader 1: sense: 'sick colleague' is fine in American English; British usually 'ill' (both accepted).
- reader 2: another correct answer, not accepted: ['Last month I had to work every Saturday to cover for a colleague who was sick.', 'Last month I had to work every Saturday to cover for a colleague who was ill.', 'Last month I had to work every Saturday to cover for an ill colleague.', 'Last month I had to work every Saturday to cover a sick colleague.', 'Last month I had to work every Saturday to cover for a colleague who was off sick.', 'Last month I had to work all Saturdays to cover for a sick colleague.', 'Last month I had to work every Saturday in order to cover for a sick colleague.']
- reader 2: instruction: 'Rewrite' does not say to change the tense; learner may only copy with 'Last month' and keep 'have to' (wrong). Needs to be clear that the verb must change (e.g. 'Say it about the past'). Also 'Last month I worked every Saturday ...' is a plausible rewrite that loses 'had to' - ambiguous whether 'had to' is required.

## r12-004 · B1.2 · mcq · gap-points-b12-1.csv:77

Task: Choose the correct option: ___ at the conference gets a name badge and a free lunch.
options: Every guest | Each of guest | All guest | Every guests
Key: {"kind": "mcq", "correct": "Every guest", "wrong": ["Every guests", "All guest", "Each of guest"]}
- reader 1: level: Quite easy for B1.2 (singular after every); more A2/B1.1.
- reader 2: sense: Distractors are believable. 'Each of guest' is a bit random (missing 'the'); fine otherwise. 'Each guest' / 'Every guest' both would work, but only Every is offered.

