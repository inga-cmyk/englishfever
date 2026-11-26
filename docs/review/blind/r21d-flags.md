# Blind check r21d: flags for the judge

10 tasks, 2 readers.

## r21d-001 · B1.1 · write · built-in

Task: You want to join an evening Italian course at a language school, but the website shows no start date. Write one polite question to the school.
Key: {"kind": "write", "model": "Could you tell me when the next Italian course starts?", "must": ["Start politely: *Could you tell me …?*, *Do you know …?* or *I'd like to know …*", "Then a question word or *if*: *… when the next course starts*.", "After the question word the subject comes first, with no *do / does*: *when the course starts*, not *when does the course start*.", "Put the subject before the verb: *when the course starts*, not *when starts the course*."]}
- reader 1: instruction: Open task: 'some forms are used' is unclear to me; an ordinary direct question (When does the course start?) is also polite and correct, so the intended form (indirect question?) is not forced by the instruction.
- reader 2: instruction: Open writing; nothing says which form is expected, so any polite question passes or the checker is unclear. Direct 'When does the course start, please?' is also polite.

## r21d-002 · B1.2 · write · built-in

Task: You ordered a printer online ten days ago, and you are still waiting. Write one polite question to the shop's customer service.
Key: {"kind": "write", "model": "Could you tell me if you have sent my order yet?", "must": ["Start politely: *Could you tell me …?*, *Do you know …?* or *I'd like to know …*", "Then *if* (or *whether*) or a question word: *… if you have sent my order*, *… when my printer will arrive*.", "After *if* or the question word the subject comes first, with no *did*: *if you sent my order*, *when my printer will arrive*.", "Put the subject before the verb: *when my printer arrives*, not *when arrives my printer*."]}
- reader 1: instruction: Instruction does not force any one form: direct questions, present perfect questions (Has it been sent yet?) are all correct. Unclear what the app checks.
- reader 2: instruction: Open writing; the target form is not clear, so many different polite questions are correct.

## r21d-003 · B1.1 · mcq · b1-cond-rep-1.csv:43

Task: Which sentence is NOT correct?
options: When I travel by bus, I always feel sick. | If you don't save your work, you lose it. | Whenever I read without my glasses, I get a headache. | If metal gets hot, it expand.
Key: {"kind": "mcq", "correct": "If metal gets hot, it expand.", "wrong": ["When I travel by bus, I always feel sick.", "If you don't save your work, you lose it.", "Whenever I read without my glasses, I get a headache."]}
- reader 1: sense: 'it expand' (missing -s) is a believable learner error.
- reader 2: sense: Missing -s is a plausible B1 mistake, but 'it expand' is very obvious. Also 'If you don't save your work, you lose it' is correct but the other three are near copies in pattern (zero conditional), so the wrong one stands out.

## r21d-004 · B1.1 · text · b1-new-3.csv:90

Task: There's a loud bang in the kitchen. Ask your flatmate. Use *What* and *make*:
Key: {"kind": "text", "accepted": [["What made that noise?", "What made the noise?", "What made that bang?", "What made the bang?", "What made that sound?", "What made the sound?", "What made that?", "What made it?", "What made that loud bang?", "What made the loud bang?", "What made that loud noise?", "What made the loud noise?", "What made that noise in the kitchen?", "What made the noise in the kitchen?", "What made that bang in the kitchen?", "What made the bang in the kitchen?", "What made that loud noise in the kitchen?", "What made the loud bang in the kitchen?"]]}
- reader 1: another correct answer, not accepted: ['What has made that loud bang?']
- reader 1: instruction: Situation says 'Ask your flatmate' but the sentence is open: 'What was that?' is excluded only by the word hint. Fine. 'Use What and make' partly gives away the form.
- reader 2: another correct answer, not accepted: ['What was it that made that bang?']
- reader 2: instruction: The instruction names the words *What* and *make*, so it gives the structure away; 'noise' vs 'bang' is also open.

## r21d-005 · B1.2 · text · b1-new-4.csv:84

Task: Start with *The problem*: Someone could have solved the problem much earlier.
Key: {"kind": "text", "accepted": [["The problem could have been solved much earlier.", "The problem could've been solved much earlier.", "The problem could have been solved much earlier by someone.", "The problem could've been solved much earlier by someone.", "The problem could have been solved by someone much earlier.", "The problem could've been solved by someone much earlier.", "The problem could have been solved much earlier by somebody.", "The problem could've been solved much earlier by somebody.", "The problem could have been solved by somebody much earlier.", "The problem could've been solved by somebody much earlier."]]}
- reader 1: instruction: Does not say 'use the passive' (good), but 'Start with The problem' strongly forces it; acceptable.
- reader 2: another correct answer, not accepted: ['The problem could have been solved earlier.']
- reader 2: instruction: 'Start with The problem' practically gives the passive away; the instruction does not say 'passive' or 'rewrite' (it is not clear that the sentence must be changed).
- reader 2: level: Passive with modal perfect is B1.2/B2-ish, borderline.

## r21d-006 · B1.1 · order · b1-new-5.csv:136

Task: Put the words in order to make a question.
word_cards: we | would | eat | like | before | to | leave | you | something
Key: {"kind": "order", "sentence": "would you like something to eat before we leave", "also": ["before we leave would you like something to eat", "would you like to eat something before we leave", "before we leave would you like to eat something", "would you like to leave before we eat something"]}
- reader 1: instruction: Cards are all lower case with no capital or punctuation hint; several natural orders exist (something to eat / to eat something; before-clause first).
- reader 2: instruction: 'Make a question' is fine, but the cards are shown lower case with no capital or question-mark hint; two cards (to, eat) allow both 'to eat something' and 'something to eat'.

## r21d-007 · B1.1 · order · b1-passives-1.csv:39

Task: Put the words in order.
word_cards: still | bridge | today | in | and | used | was | built | is | it | the | 1932
Key: {"kind": "order", "sentence": "the bridge was built in 1932 and it is still used today", "also": ["the bridge was built in 1932 and today it is still used", "in 1932 the bridge was built and it is still used today", "the bridge is still used today and it was built in 1932", "today the bridge is still used and it was built in 1932", "in 1932 the bridge was built and today it is still used"]}
- reader 1: another correct answer, not accepted: ['it was built in 1932 and the bridge is still used today', "the bridge was built in 1932 and is still used today (without it: not possible, card 'it' must be used)", 'the bridge is still used today and was built in 1932 (no)']
- reader 1: instruction: Instruction is bare; no clue whether to start with 'The bridge' or 'It'; several orders are correct.
- reader 2: another correct answer, not accepted: ['it was built in 1932 and the bridge is still used today']
- reader 2: instruction: Several orders are correct; instruction gives no clue which one is intended. All 12 cards in a long sentence with several valid orders.

## r21d-008 · B1.2 · text · b1-upgrades-1.csv:42

Task: Rewrite the sentence. Start with *The winner*: They will announce the winner on Friday.
Key: {"kind": "text", "accepted": [["The winner will be announced on Friday.", "On Friday the winner will be announced.", "The winner will be announced by them on Friday.", "The winner will be announced on Friday by them."]]}
- reader 1: instruction: Fine; passive forced by 'Start with The winner'.
- reader 2: instruction: 'They' is not in the original need; fine. 'Start with The winner' gives the passive away (but needed to fix the start).

## r21d-009 · B1.1 · gap · compare-past-1.csv:13

Task: My brother ___ a lot of books when he was off work with a broken leg last winter. (read)
Key: {"kind": "gap", "accepted": [["read", "was reading", "would read", "used to read"]]}
- reader 1: another correct answer, not accepted: [['had read']]
- reader 1: instruction: 'was reading' and 'used to read' also fit; 'had read' unlikely. Spelling 'read' is identical to present, so a learner can't be sure of the tense target; only the verb (read) is given.
- reader 1: sense: Past simple intended probably; 'a lot of books ... when he was off work' also supports habitual past (used to / would read).
- reader 2: instruction: Past simple vs past continuous: 'was reading a lot of books' is possible but less natural; 'used to read' is possible but less fitting for one winter. 'read' looks the same as the verb in brackets, so the learner may think nothing changes.

## r21d-010 · B1.1 · gap · compare-past-1.csv:40

Task: Ana: 'Did you have lunch with your colleagues yesterday?'
Tom: 'No, when I got to the café, they ___ eating.' (already / finish)
Key: {"kind": "gap", "accepted": [["had already finished", "'d already finished", "already had finished"]]}
- reader 1: another correct answer, not accepted: [['had finished already'], ['already finished']]
- reader 1: instruction: Gap 'they ___ eating' with 'already / finish' needs 'finished eating' - fine; American 'already finished' is also correct.
- reader 2: another correct answer, not accepted: [['had finished already']]
- reader 2: instruction: The answer is only one tense (past perfect); clear. 'finished eating' fits the gap grammar, but a learner could write 'were already finishing' (not correct here: 'finishing eating' is awkward).

