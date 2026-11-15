# Blind check r11b: flags for the judge

4 tasks, 2 readers.

## r11b-001 · B1.2 · gap · zz-blind-gap-points-b12-1.csv:11

Task: We need a new printer: ours ___ always ___ in the middle of big jobs.
word_cards: is | jams | jamming | was
Key: {"kind": "gap", "accepted": [["is"], ["jamming"]]}
- reader 1: a wrong option that fits: 'was' fits as a second answer (was always jamming), less natural after 'We need a new printer' (present problem).
- reader 1: instruction: No instruction at all: only a sentence with gaps; learner is not told to choose cards or what to complete. Also 'always + continuous' complaint is only signalled by 'always'; fine.
- reader 1: sense: 'was ... jamming' being possible makes the item ambiguous; 'ours' present need strongly favours 'is'.
- reader 2: a wrong option that fits: was (with jamming): 'ours was always jamming' is correct English, though less logical beside 'ours' still being the printer in use and 'We need'; arguably acceptable if the printer is already replaced/described as past.
- reader 2: instruction: No instruction line: the learner is not told what to do beyond the dragging note (minor). 'always' + continuous is the target and is not named, fine.
- reader 2: sense: Distractor 'jams' cannot fit any gap pair (is/was + jams is ungrammatical) so it is a weak distractor; 'was' only fits marginally.

## r11b-002 · B1.2 · gap · zz-blind-gap-points-b12-1.csv:12

Task: My old car ___ constantly ___ down, so in the end I sold it.
word_cards: is | breaks | was | breaking
Key: {"kind": "gap", "accepted": [["was"], ["breaking"]]}
- reader 1: instruction: No instruction at all: only a sentence with gaps; learner is not told to choose cards or what to complete. 'so in the end I sold it' is what forces past; fine.
- reader 2: instruction: No instruction line (minor). 'so in the end I sold it' makes past obvious, so only 'was' is possible; fine.
- reader 2: sense: Distractors 'is'/'breaks' are believable; 'breaks' pairs with no auxiliary so is a weak distractor.

## r11b-003 · B1.2 · order · zz-blind-gap-points-b12-1.csv:18

Task: Put the words in order.
word_cards: neighbour | loud | always | late | at | night | music | my | playing | is
Key: {"kind": "order", "sentence": "my neighbour is always playing loud music late at night", "also": ["late at night my neighbour is always playing loud music", "at night my neighbour is always playing loud music late"]}
- reader 1: another correct answer, not accepted: [['late at night my neighbour is always playing loud music'], ['is my neighbour always playing loud music late at night']]
- reader 1: instruction: Does not say statement or question: the 'is my neighbour always playing ...?' question also uses all cards. Cards are all lower case with no capital or full stop/question mark to show which. Say 'make a sentence'.
- reader 1: sense: Fine, natural. Starting with 'late at night' also natural (less usual).
- reader 2: another correct answer, not accepted: ['is my neighbour always playing loud music late at night', 'my neighbour is playing loud music always late at night (less natural)', 'my neighbour is always playing music loud late at night (less natural)']
- reader 2: instruction: 'Put the words in order.' does not say statement or question, so the question 'Is my neighbour always playing ...' is also valid; no capital letters or full stop to guide. Specify 'to make a sentence'.
- reader 2: sense: Fine; a natural complaint.

## r11b-004 · B1.2 · order · zz-blind-gap-points-b12-1.csv:63

Task: Put the words in order to make a question.
word_cards: to | have | should | i | what | said | my | boss
Key: {"kind": "order", "sentence": "what should i have said to my boss", "also": []}
- reader 1: instruction: 'to make a question' is clear; 'should have' structure is not named. Fine.
- reader 1: sense: Natural. 'i' lower case card is fine.
- reader 2: instruction: 'to make a question' gives away the word order start (what should...); mild. Otherwise clear.

