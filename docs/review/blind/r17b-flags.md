# Blind check r17b: flags for the judge

4 tasks, 2 readers.

## r17b-001 · B1.2 · mcq · built-in

Task: Choose the correct option: Could you tell me when ___ ? The guarantee may still be valid.
options: did you buy this laptop | did you bought this laptop | you have bought this laptop | you bought this laptop
Key: {"kind": "mcq", "correct": "you bought this laptop", "wrong": ["did you buy this laptop", "did you bought this laptop", "you have bought this laptop"]}
- reader 1: a wrong option that fits: you have bought this laptop is marginal: 'when' with present perfect is normally avoided, so not correct
- reader 1: instruction: The sentence 'The guarantee may still be valid.' is superfluous: without it only 'you bought this laptop' is still possible English (embedded question, no inversion). Also no 'Choose the correct option' problem otherwise.
- reader 2: sense: The sentence 'The guarantee may still be valid' is a harmless but unneeded extra; the answer is still the only possible one without it. Option 'you have bought' is a believable but wrong distractor (when + present perfect).

## r17b-002 · B2.2 · write · built-in

Task: Your team wants to launch the new app next month, but the tests are not finished, and a delay will cost money. Write a sentence that starts with *The question is whether*, *The question is how* or *The question is why*.
Key: {"kind": "write", "model": "The question is whether we can afford the delay.", "must": ["*Questions is* does not agree: one question, so *The question is*.", "Start with *The question is*.", "After *The question is* put *whether*, *how*, *why* or another question word.", "After *how*, *why* or *whether* use statement word order: *how we can…*, not *how can we…*."]}
- reader 1: instruction: Open task, so many answers fit; 'the app checks that some forms are used' is vague for the learner. Scenario is needed, OK.
- reader 2: instruction: Uses *...* markdown asterisks around the starters; the three starters are given, so only copying the form is needed. Open task: any sensible clause fits, so the check must be tolerant.

## r17b-003 · B2.2 · mcq · conjunctions-1.csv:103

Task: Choose the correct option: It was a difficult task, and ___ they finished it on time.
options: in spite of | yet | despite | although
Key: {"kind": "mcq", "correct": "yet", "wrong": ["although", "despite", "in spite of"]}
- reader 1: sense: 'and although' is odd and 'and yet' is the only fit; fine. Slight: 'and' makes 'although' look wrong for the wrong reason (clause + 'and although' is possible in other contexts).
- reader 2: sense: 'although' after 'and' is not natural (and although they ... would be illogical here), so it is a fair distractor. 'in spite of' and 'despite' fail because a clause follows.

## r17b-004 · B1.2 · gap · iq-b1-6.csv:25

Task: I'm not sure ___ ___ ___ ___ the tickets yet. Let me check my email.
word_cards: if | we | have | book | do | booked
Key: {"kind": "gap", "accepted": [["if"], ["we"], ["have"], ["booked"]]}
- reader 1: instruction: No verb of instruction (e.g. 'Complete the sentence'); the cards are not mentioned in the text. Minor.
- reader 2: sense: Distractors 'do', 'book' are believable. Check that 'whether' is not expected; 'if we have booked' is the only grammatical combination.

