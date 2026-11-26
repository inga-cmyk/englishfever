# Blind check r21c: flags for the judge

27 tasks, 2 readers.

## r21c-001 · B1.1 · mcq · built-in

Task: Choose the correct option: I ___ what you mean, but I don't agree with you.
options: am knowing | knows | know
Key: {"kind": "mcq", "correct": "know", "wrong": ["am knowing", "knows"]}
- reader 1: level: Present simple of a state verb at B1.1 is easy (nearly A2).

## r21c-003 · B1.2 · write · built-in

Task: The sky is full of dark clouds, and your friend has no umbrella. Write two sentences to your friend: what you expect to happen, and an offer of your umbrella.
Key: {"kind": "write", "model": "It is going to rain. I'll lend you my umbrella.", "must": ["Say what the clouds show with *going to* (or *about to*) + base verb.", "Offer your umbrella with *I'll* (or *Shall I …?*)."]}
- reader 1: instruction: Open task, fine; 'the app checks that some forms are used' but the learner is not told which forms (will / going to / offer), so many correct answers may be marked wrong.
- reader 2: instruction: Forms not named, so any future form (will, going to, might, may) is correct; fine for open writing but the app check may reject valid answers like 'might' or 'is about to'.

## r21c-006 · B1.1 · write · built-in

Task: You want to join an evening Italian course at a language school, but the website shows no start date. Write one polite question to the school.
Key: {"kind": "write", "model": "Could you tell me when the next Italian course starts?", "must": ["Start politely: *Could you tell me …?*, *Do you know …?* or *I'd like to know …*", "Then a question word or *if*: *… when the next course starts*.", "After the question word the subject comes first, with no *do / does*: *when the course starts*, not *when does the course start*.", "Put the subject before the verb: *when the course starts*, not *when starts the course*."]}
- reader 1: instruction: Open; 'polite question' is the only constraint, so direct 'When does the course start?' is also fine. Learner cannot know which forms the app wants (indirect question?).
- reader 2: instruction: Direct question 'When does the course start?' is also correct; 'polite' is the only push to an indirect question. Which forms the app checks is not clear to the learner.

## r21c-007 · B1.2 · write · built-in

Task: You ordered a printer online ten days ago, and you are still waiting. Write one polite question to the shop's customer service.
Key: {"kind": "write", "model": "Could you tell me if you have sent my order yet?", "must": ["Start politely: *Could you tell me …?*, *Do you know …?* or *I'd like to know …*", "Then *if* (or *whether*) or a question word: *… if you have sent my order*, *… when my printer will arrive*.", "After *if* or the question word the subject comes first, with no *did*: *if you sent my order*, *when my printer will arrive*.", "Put the subject before the verb: *when my printer arrives*, not *when arrives my printer*."]}
- reader 1: instruction: Open; the forms the app checks are not stated (present perfect? indirect question?), so many valid questions may be rejected. 'One polite question' but a statement plus question is also natural.
- reader 2: instruction: Open: several tenses/structures fit (present perfect, passive, indirect question); the learner cannot know which forms are checked.
- reader 2: level: Fine for B1.2 but nothing in the task needs B1.2 over B1.1 (same as r21c-006).

## r21c-008 · B1.1 · mcq · b1-cond-rep-1.csv:43

Task: Which sentence is NOT correct?
options: When I travel by bus, I always feel sick. | If metal gets hot, it expand. | Whenever my neighbour plays music, my dog barks. | If you don't save your work, you lose it.
Key: {"kind": "mcq", "correct": "If metal gets hot, it expand.", "wrong": ["When I travel by bus, I always feel sick.", "If you don't save your work, you lose it.", "Whenever my neighbour plays music, my dog barks."]}
- reader 1: sense: Missing -s after 'it' is a believable mistake. Fine.
- reader 2: sense: Missing -s on 'expand' is a believable mistake. Fine.

## r21c-009 · B1.2 · match · b1-cond-rep-1.csv:140

Task: Match each sentence with its meaning.
left: If I had gone, I would have met her. | If I hadn't gone, I wouldn't have met her. | If I went, I would meet her.
right: I probably won't go. | I didn't go. | I went.
Key: {"kind": "match", "pairs": [["If I had gone, I would have met her.", "I didn't go."], ["If I hadn't gone, I wouldn't have met her.", "I went."], ["If I went, I would meet her.", "I probably won't go."]]}
- reader 1: instruction: Possibly unclear which pairing; 'meaning' is clear enough.
- reader 1: sense: 'If I went, I would meet her' = unreal/unlikely, 'I probably won't go' is a loose fit (it could also mean 'I don't go'); acceptable but not exact.

## r21c-010 · B1.2 · order · b1-cond-rep-1.csv:153

Task: Put the words in order.
word_cards: ill | said | because | come | he | he | he | couldn't | was
Key: {"kind": "order", "sentence": "he said he couldn't come because he was ill", "also": ["because he was ill he said he couldn't come", "he said he was ill because he couldn't come"]}
- reader 1: another correct answer, not accepted: ["he couldn't come because he said he was ill", "because he said he was ill he couldn't come"]
- reader 1: instruction: No capital or full stop on cards so 'he' x3 cards are identical; gives little away. Many orders possible.
- reader 1: level: B1.2 is a bit easy (reported speech, 9 cards, obvious order).
- reader 1: sense: The alternatives are grammatical but illogical; the intended one is the only natural one.
- reader 2: another correct answer, not accepted: ["he couldn't come because he said he was ill", "because he said he was ill he couldn't come"]
- reader 2: instruction: No context, so meaning is open: several orders are correct English with different meanings (only the first is the natural one). Three identical 'he' cards and no capital/comma cue.
- reader 2: sense: Alternatives are correct but change meaning; the task does not say which meaning is wanted.

## r21c-011 · B1.1 · mcq · b1-cond-rep-1.csv:180

Task: Which sentence is NOT correct?
options: My boss told that the meeting was cancelled. | She said that she was tired. | He told me he would call later. | They said they had missed the last train.
Key: {"kind": "mcq", "correct": "My boss told that the meeting was cancelled.", "wrong": ["She said that she was tired.", "He told me he would call later.", "They said they had missed the last train."]}
- reader 1: sense: Missing object after 'told' is a believable B1 error.

## r21c-012 · B1.2 · order · b1-new-1.csv:8

Task: Put the words in order.
word_cards: a | sunday | visit | used | we | grandparents | every | i | was | child | when | to | my
Key: {"kind": "order", "sentence": "when i was a child we used to visit my grandparents every sunday", "also": ["we used to visit my grandparents every sunday when i was a child", "every sunday we used to visit my grandparents when i was a child", "when i was a child every sunday we used to visit my grandparents", "every sunday when i was a child we used to visit my grandparents"]}
- reader 1: instruction: Very many correct orders; the learner cannot know which one the key holds.
- reader 1: sense: 'a child' without 'a' capital is fine. Several orders are equally natural.
- reader 2: instruction: Many valid orders (time clauses and 'every Sunday' move freely); no comma/capital cue. 'sunday' is given lower case.
- reader 2: level: 13 cards, long for a card task, though within B1.2.

## r21c-013 · B1.1 · text · b1-new-3.csv:90

Task: There's a loud bang in the kitchen. Ask your flatmate. Use *What* and *make*:
Key: {"kind": "text", "accepted": [["What made that noise?", "What made the noise?", "What made that bang?", "What made the bang?", "What made that sound?", "What made the sound?", "What made that?", "What made it?", "What made that loud bang?", "What made the loud bang?", "What made that loud noise?", "What made the loud noise?", "What made that noise in the kitchen?", "What made the noise in the kitchen?", "What made that bang in the kitchen?", "What made the bang in the kitchen?"]]}
- reader 1: another correct answer, not accepted: ['What has made that noise?']
- reader 1: instruction: Open: any noun works (bang/noise/sound); 'Ask your flatmate' ok. 'make' is the word to use but the learner may also think 'What makes ...'. Uses markdown asterisks.
- reader 1: sense: 'make' for a cause (What made...) is not obvious at B1.1.
- reader 2: another correct answer, not accepted: ['What made that loud noise in the kitchen?', 'What made the loud bang in the kitchen?', "What's making that noise?"]
- reader 2: instruction: 'Use What and make' nearly gives the structure away but is needed; fine. 'What was that?' does not use make.

## r21c-014 · B1.2 · text · b1-new-4.csv:84

Task: Start with *The accident*: Someone could have avoided the accident.
Key: {"kind": "text", "accepted": [["The accident could have been avoided.", "The accident could have been avoided by someone.", "The accident could've been avoided.", "The accident could've been avoided by someone.", "The accident could have been avoided by somebody.", "The accident could've been avoided by somebody."]]}
- reader 1: another correct answer, not accepted: ['The accident could have been prevented.']
- reader 1: instruction: 'Start with The accident' makes passive obvious; 'avoid' should be kept (prevented changes the word). Fine.
- reader 2: another correct answer, not accepted: ['The accident might have been avoided.', 'The accident could have been prevented.']
- reader 2: instruction: 'might/should have been avoided' change the meaning slightly; 'could' is expected but the instruction does not say to keep it.
- reader 2: level: Passive with a perfect modal is B2 rather than B1.2.

## r21c-016 · B1.1 · order · b1-new-5.csv:136

Task: Put the words in order to make a question.
word_cards: something | would | before | you | to | leave | like | eat | we
Key: {"kind": "order", "sentence": "would you like something to eat before we leave", "also": ["before we leave would you like something to eat", "would you like to eat something before we leave", "before we leave would you like to eat something"]}
- reader 1: a wrong option that fits: would you like to leave before we eat something is grammatical but odd (cards).
- reader 1: instruction: 'to make a question' fine; question word order is given by 'would' only.
- reader 1: sense: Cards allow odd but grammatical combos (like to leave / eat something).
- reader 2: instruction: Both 'eat something' and 'something to eat' use all the cards; also starting with 'Before we leave'. Task is not a single-answer order.

## r21c-017 · B1.1 · order · b1-passives-1.csv:39

Task: Put the words in order.
word_cards: is | was | the | bridge | today | still | used | and | built | 1932 | in | it
Key: {"kind": "order", "sentence": "the bridge was built in 1932 and it is still used today", "also": ["the bridge was built in 1932 and today it is still used", "in 1932 the bridge was built and it is still used today", "the bridge is still used today and it was built in 1932", "today the bridge is still used and it was built in 1932"]}
- reader 1: another correct answer, not accepted: ['it was built in 1932 and the bridge is still used today', 'it was built in 1932 and today the bridge is still used']
- reader 1: instruction: Many orders possible; the learner cannot know the key.
- reader 1: sense: Sentence is natural though 'it' after 'the bridge' is a bit repetitive.
- reader 2: another correct answer, not accepted: ['in 1932 the bridge was built and today it is still used']
- reader 2: instruction: No context, so several orders are correct; the last two are less natural (chronology reversed).
- reader 2: sense: 'it' after 'and' is natural but the bridge/it repetition is slightly clumsy.

## r21c-018 · B1.1 · text · b1-passives-1.csv:62

Task: Rewrite the sentence. Start with *My laptop*: Someone stole my laptop yesterday.
Key: {"kind": "text", "accepted": [["My laptop was stolen yesterday.", "My laptop was stolen by someone yesterday.", "Yesterday my laptop was stolen.", "Yesterday my laptop was stolen by someone.", "My laptop got stolen yesterday.", "Yesterday my laptop got stolen.", "My laptop was stolen yesterday by someone."]]}
- reader 2: instruction: Passive is not named, but 'Start with My laptop' makes it obvious.

## r21c-020 · B1.1 · order · b1-tenses-1.csv:5

Task: Put the words in order.
word_cards: work | does | brother | same | still | the | for | your | company
Key: {"kind": "order", "sentence": "does your brother still work for the same company", "also": ["does your brother work for the same company still", "your brother does still work for the same company"]}
- reader 1: instruction: Answer is almost fixed; question order with 'does' is easy to see.
- reader 1: level: B1.1 is fairly easy.
- reader 1: sense: 'Does your brother still work for the same company' is the only natural order (lower-case 'still' position fixed).
- reader 2: sense: Cards contain 'does': the question form is given away; easy for B1.1.

## r21c-021 · B1.1 · gap · b1-tenses-1.csv:58

Task: Anna ___ for a new flat at the moment because her rent is too high.
word_cards: is looking | looks | looking
Key: {"kind": "gap", "accepted": [["is looking"]]}
- reader 1: a wrong option that fits: 'looking' alone does not fit.
- reader 1: level: Too easy for B1.1 (present continuous with 'at the moment').

## r21c-022 · B1.1 · text · b1-tenses-2.csv:22

Task: Rewrite with *since*: I started learning English in 2019, and I'm still learning it.
Key: {"kind": "text", "accepted": [["I have been learning English since 2019.", "I have learned English since 2019.", "I have learnt English since 2019.", "Since 2019 I've been learning English.", "Since 2019 I have been learning English.", "I've been learning it since 2019."]]}
- reader 1: sense: Rewrite instruction is clear.
- reader 2: instruction: 'Rewrite with since' does not say how to change the verb; the present perfect (simple or continuous) is expected but not stated. Answer may be marked wrong if only continuous is accepted.

## r21c-023 · B1.1 · text · b1-tenses-2.csv:24

Task: Make it negative: We have visited that museum.
Key: {"kind": "text", "accepted": [["We haven't visited that museum.", "We have not visited that museum.", "We have never visited that museum.", "We haven't visited that museum yet."]]}
- reader 1: instruction: 'Negative' might not accept 'never'; learners may write it.
- reader 2: another correct answer, not accepted: ["We haven't been to that museum."]
- reader 2: level: Very easy for B1.1: add 'not' to an A2 form.

## r21c-025 · B1.1 · gap · b1-upgrades-1.csv:34

Task: Every week, the cheese ___ in small villages and then ___ to shops around the country. (make / send)
Key: {"kind": "gap", "accepted": [["is made", "gets made"], ["is sent", "sent", "gets sent"]]}
- reader 1: instruction: The passive is not stated; learner must work out it from 'make / send' with a singular noun 'cheese'. Whether 'is ... and then sent' (one 'is') is accepted is unclear.
- reader 1: level: Passive present at B1.1 is acceptable.
- reader 1: sense: Fine.
- reader 2: instruction: Passive is not hinted by '(make / send)'; the learner must find it from context (acceptable at B1.1 but the active 'makes/sends' is wrong, 'cheese' as subject saves it). Gap 2 'sent' alone is correct after 'and then'.

## r21c-026 · B1.2 · text · b1-upgrades-1.csv:42

Task: Rewrite the sentence. Start with *The winner*: They will announce the winner on Friday.
Key: {"kind": "text", "accepted": [["The winner will be announced on Friday.", "On Friday the winner will be announced.", "The winner will be announced by them on Friday."]]}
- reader 1: another correct answer, not accepted: ['The winner will be announced on Friday by them.']

## r21c-027 · B1.1 · gap · compare-past-1.csv:40

Task: Ana: 'Did you have lunch with your colleagues yesterday?'
Tom: 'No, when I got to the café, they ___ eating.' (already / finish)
Key: {"kind": "gap", "accepted": [["had already finished", "'d already finished"]]}
- reader 1: another correct answer, not accepted: [['had finished'], ['already finished'], ['already had finished']]
- reader 1: instruction: Unclear whether 'already' belongs in the gap or is a hint word; the gap sits before 'eating' only, so 'had finished' could also be wanted. Past simple 'finished' is also acceptable in American English.
- reader 2: another correct answer, not accepted: [['had finished already']]
- reader 2: instruction: Two verb hints in one gap; the learner must type the whole 'had already finished'. Past perfect with 'when' is not signalled.
- reader 2: level: Past perfect is B1.2/B2 at the very least; B1.1 is too low.
- reader 2: sense: 'No, ...' answer is a little odd as a reply to 'Did you have lunch with your colleagues'; Tom may have had lunch elsewhere.

