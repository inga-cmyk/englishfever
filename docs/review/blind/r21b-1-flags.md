# Blind check r21b-1: flags for the judge

50 tasks, 2 readers.

## r21b-1-001 · B1.1 · mcq · built-in

Task: Which sentence is correct?
options: I'm wanting a coffee. | I am want a coffee. | I want a coffee.
Key: {"kind": "mcq", "correct": "I want a coffee.", "wrong": ["I'm wanting a coffee.", "I am want a coffee."]}
- reader 1: level: Too easy for B1.1 (stative verb, basic A2 level).
- reader 1: sense: 'I am want a coffee.' is a random string, not a believable learner mistake. Note 'I'm wanting' is used informally but is wrong here.
- reader 2: level: A2 content (stative verbs) at B1.1; very easy.
- reader 2: sense: 'I'm wanting' is a believable mistake; 'I am want' is a form few learners write beyond A1 (informal 'I'm wanting' is used in some dialects/slogans).

## r21b-1-002 · B1.1 · mcq · built-in

Task: Which sentence sounds more temporary?
options: I live with my parents. | Both sound the same. | Both sound permanent. | I'm living with my parents.
Key: {"kind": "mcq", "correct": "I'm living with my parents.", "wrong": ["I live with my parents.", "Both sound the same.", "Both sound permanent."]}
- reader 1: sense: 'Both sound the same' and 'Both sound permanent' are filler distractors.
- reader 2: instruction: Option order is odd (the 'Both' options sit between); fine otherwise.

## r21b-1-003 · B1.1 · mcq · built-in

Task: Choose the correct option: Yesterday she ___ the door and walked in.
options: opened | was opening | has opened | opens
Key: {"kind": "mcq", "correct": "opened", "wrong": ["was opening", "has opened", "opens"]}
- reader 1: instruction: 'Yesterday' gives the tense away.
- reader 1: level: A2-level (simple past with 'Yesterday').
- reader 2: level: A2 level (simple past) at B1.1.

## r21b-1-004 · B1.1 · gap · built-in

Task: I ___ Tom at the party, so I called him later. (not / see)
Key: {"kind": "gap", "accepted": [["didn't see", "did not see", "hadn't seen", "had not seen"]]}
- reader 2: instruction: The hint '(not / see)' gives the verb and says negative, but not the tense; fine. Contracted and full form both must be accepted.

## r21b-1-005 · B1.1 · mcq · built-in

Task: Choose the correct option: I ___ along the street when I saw an old friend.
options: was walk | was walking | were walking | am walking
Key: {"kind": "mcq", "correct": "was walking", "wrong": ["was walk", "am walking", "were walking"]}
- reader 1: level: Easy for B1.1.
- reader 1: sense: 'was walk' is a believable error; fine.
- reader 2: level: Past continuous with 'when' is A2/B1.1; fine.

## r21b-1-007 · B1.1 · mcq · built-in

Task: I've worked here ___ five years.
options: since | for | already
Key: {"kind": "mcq", "correct": "for", "wrong": ["since", "already"]}
- reader 1: level: Easy; 'already' is a filler distractor.
- reader 1: sense: 'already' is a word of another kind, not a believable mistake.
- reader 2: level: A2-level for/since; easy for B1.1.

## r21b-1-009 · B1.2 · mcq · built-in

Task: Choose the correct option: Have you seen the new Italian film? Yes, I ___ it at the cinema last night.
options: had seen | have seen | saw | have saw
Key: {"kind": "mcq", "correct": "saw", "wrong": ["have seen", "have saw", "had seen"]}
- reader 1: instruction: 'last night' gives the answer away.
- reader 1: level: 'have saw' is not a believable error at B1.2.

## r21b-1-010 · B1.2 · mcq · built-in

Task: Choose the correct option: I ___ the email yesterday, but the client hasn't answered yet.
options: sent | have just sent | have sent
Key: {"kind": "mcq", "correct": "sent", "wrong": ["have sent", "have just sent"]}
- reader 1: instruction: 'yesterday' gives it away.

## r21b-1-011 · B1.1 · mcq · built-in

Task: Choose the correct option: I'm tired and I'm still at my desk. I ___ all day.
options: have working | have been work | have been working | had been working
Key: {"kind": "mcq", "correct": "have been working", "wrong": ["have been work", "have working", "had been working"]}
- reader 1: sense: 'have working' and 'have been work' are weak distractors.

## r21b-1-013 · B1.1 · mcq · built-in

Task: Your friend is out of breath, but she isn't running now. Why is she out of breath?
options: She is running. | She runs. | She has been running.
Key: {"kind": "mcq", "correct": "She has been running.", "wrong": ["She is running.", "She runs."]}
- reader 1: instruction: 'isn't running now' plus 'out of breath' is fine, but 'She is running' is excluded by the text; easy.
- reader 2: level: Easy for B1.1 (the three options differ obviously).

## r21b-1-014 · B1.2 · gap · built-in

Task: The children are washing their hands now. Look at the floor! They ___ with paint. (play)
Key: {"kind": "gap", "accepted": [["have been playing", "'ve been playing"]]}
- reader 1: another correct answer, not accepted: [['have played'], ['were playing'], ['had been playing']]
- reader 1: instruction: Open to several tenses; 'have played' and 'were playing' fit the context (less natural). Contraction 've allowed?
- reader 2: another correct answer, not accepted: [['have played'], ['were playing'], ['played']]
- reader 2: instruction: Not only present perfect continuous fits: 'were playing' / 'played' (past) and 'have played' (less natural) also explain the paint on the floor. Context does not force the tense; 'now' in the first sentence helps only partly.

## r21b-1-015 · B1.2 · mcq · built-in

Task: Choose the correct option: The bus left at 8.00. We got to the stop at 8.05. When we got there, the bus ___ already ___.
options: did ... leave | had ... left | was ... leaving | has ... left
Key: {"kind": "mcq", "correct": "had ... left", "wrong": ["has ... left", "was ... leaving", "did ... leave"]}
- reader 1: level: 'already' + the given times make this easy.

## r21b-1-017 · B1.2 · mcq · built-in

Task: Choose the correct option: Hurry up! The film ___ start.
options: is about to | will to | about to | is about
Key: {"kind": "mcq", "correct": "is about to", "wrong": ["will to", "about to", "is about"]}
- reader 1: sense: 'will to' and 'about to' are not believable mistakes; 'is about' is.
- reader 2: level: 'be about to' is fine for B1.2.

## r21b-1-019 · B1.2 · write · built-in

Task: The sky is full of dark clouds, and your friend has no umbrella. Write two sentences to your friend: what you expect to happen, and an offer of your umbrella.
Key: {"kind": "write", "model": "It is going to rain. I'll lend you my umbrella.", "must": ["Use *going to* + base verb in the prediction.", "Use *I'll* or *I will* for the offer."]}
- reader 1: instruction: Fine, but 'expect' could also be answered with 'might' or 'is about to': unclear which forms the app accepts.
- reader 2: instruction: 'Some forms are used' is hidden: learners may write 'will', 'going to', 'might', 'look like' and be marked wrong if only going to + will is accepted. 'What you expect' accepts will / going to / probably will.

## r21b-1-020 · B1.1 · mcq · built-in

Task: Choose the correct option: The invoices ___ every Friday, so please send me yours by Thursday.
options: are send | are sent | send
Key: {"kind": "mcq", "correct": "are sent", "wrong": ["are send", "send"]}
- reader 1: sense: 'send' is a believable error; 'are send' is fine.
- reader 2: level: Present simple passive; fine.

## r21b-1-022 · B1.1 · mcq · built-in

Task: Which sentence says the same as 'They have finished the project'?
options: The project has been finished. | The project is being finished. | The project has being finished. | The project have been finished.
Key: {"kind": "mcq", "correct": "The project has been finished.", "wrong": ["The project have been finished.", "The project has being finished.", "The project is being finished."]}
- reader 1: sense: 'has being' and 'have been' are believable.
- reader 2: level: Fine.

## r21b-1-023 · B1.1 · mcq · built-in

Task: Which sentence is correct?
options: The files check on Monday. | The files will be check on Monday. | The files will be checked on Monday. | The files will checked on Monday.
Key: {"kind": "mcq", "correct": "The files will be checked on Monday.", "wrong": ["The files will checked on Monday.", "The files will be check on Monday.", "The files check on Monday."]}
- reader 1: sense: 'The files check on Monday.' is unnatural as a learner error but acceptable.

## r21b-1-024 · B1.1 · mcq · built-in

Task: Which sentence is NOT correct?
options: If you press this button, the machine stops. | Whenever I forget my umbrella, it rains. | If the printer jams, everybody panics. | If people don't sleep enough, they would be grumpy.
Key: {"kind": "mcq", "correct": "If people don't sleep enough, they would be grumpy.", "wrong": ["Whenever I forget my umbrella, it rains.", "If the printer jams, everybody panics.", "If you press this button, the machine stops."]}
- reader 2: sense: 'would' in a zero conditional is a believable mixed-up form, but arguably possible English (habitual would); borderline.

## r21b-1-025 · B1.1 · mcq · built-in

Task: Choose the correct option: We won't finish on time ___ we start now.
options: if | when | unless
Key: {"kind": "mcq", "correct": "unless", "wrong": ["if", "when"]}
- reader 1: a wrong option that fits: 'if' is grammatical (We won't finish on time if we start now = starting now is too late), so it fits unless context excludes it.
- reader 1: instruction: Only 'unless' is logical, but 'if' also gives a possible sentence.
- reader 2: a wrong option that fits: 'if' is grammatical but gives the wrong logic ('We won't finish if we start now' = starting now is too late); only possible with an odd reading.

## r21b-1-032 · B1.2 · mcq · built-in

Task: Which sentence reports this question: 'Do you like jazz?'
options: He asked me do I like jazz. | He asked me if I liked jazz. | He asked me if did I like jazz.
Key: {"kind": "mcq", "correct": "He asked me if I liked jazz.", "wrong": ["He asked me do I like jazz.", "He asked me if did I like jazz."]}
- reader 1: sense: Wrong options are believable.
- reader 2: sense: 'if did I like' is a believable error; fine.

## r21b-1-034 · B1.2 · mcq · built-in

Task: Which sentence reports the guard's request: 'Please wait here.'
options: The guard told me waiting there. | The guard told me wait there. | The guard told me to wait there. | The guard asked if I wait there.
Key: {"kind": "mcq", "correct": "The guard told me to wait there.", "wrong": ["The guard told me wait there.", "The guard told me waiting there.", "The guard asked if I wait there."]}
- reader 1: instruction: 'asked' would be more accurate for 'please' but 'told' is acceptable.
- reader 1: sense: 'told me waiting' / 'told me wait' are weak.

## r21b-1-035 · B1.1 · mcq · built-in

Task: Choose the correct sentence.
options: Could you tell me when the next train leave? | Could you tell me when does the next train leave? | Could you tell me when the next train leaves? | Could you tell me when leaves the next train?
Key: {"kind": "mcq", "correct": "Could you tell me when the next train leaves?", "wrong": ["Could you tell me when does the next train leave?", "Could you tell me when leaves the next train?", "Could you tell me when the next train leave?"]}
- reader 2: level: Easy for B1.1.

## r21b-1-036 · B1.1 · match · built-in

Task: Match each situation with what you would say.
left: You decide now to help a colleague with a heavy bag. | You describe a confirmed appointment for tomorrow. | You predict rain because you can see dark clouds.
right: I'll carry that for you. | It's going to rain. | I'm seeing the dentist at ten.
Key: {"kind": "match", "pairs": [["You decide now to help a colleague with a heavy bag.", "I'll carry that for you."], ["You describe a confirmed appointment for tomorrow.", "I'm seeing the dentist at ten."], ["You predict rain because you can see dark clouds.", "It's going to rain."]]}
- reader 1: level: Left sentences are long/abstract for B1.1 ('confirmed appointment').
- reader 2: level: Clear; only three items.

## r21b-1-037 · B1.1 · match · built-in

Task: Match each sentence with its meaning.
left: If you help me, I'll buy you lunch. | We won't start unless everyone is here. | I'll take water in case the shop is closed.
right: A promise depending on your help. | A precaution against a possible problem. | Everyone being present is necessary for us to start.
Key: {"kind": "match", "pairs": [["If you help me, I'll buy you lunch.", "A promise depending on your help."], ["We won't start unless everyone is here.", "Everyone being present is necessary for us to start."], ["I'll take water in case the shop is closed.", "A precaution against a possible problem."]]}
- reader 1: level: Meaning descriptions are abstract and wordy for B1.1 (the learner must parse 'depending', 'precaution').
- reader 1: sense: The 'promise' meaning could also fit 'in case' loosely, but not really.
- reader 2: instruction: 'precaution' and 'necessary' are hard words for B1.1.

## r21b-1-038 · B1.1 · write · built-in

Task: Last night you had dinner at a restaurant, and this morning you can't find your scarf. You phone the restaurant. Write one polite question.
Key: {"kind": "write", "model": "Could you tell me if my scarf is still at the restaurant?", "must": ["Start politely: *Could you tell me …?*, *Do you know …?* or *I'd like to know …*", "Then *if* (or *whether*) or a question word: *… if my scarf is still there*.", "After *if* the subject comes first: *if my scarf is still there*, not *if is my scarf*; no *do / does* either."]}
- reader 1: instruction: Does not say which form is wanted; many questions are polite. Nothing says 'indirect question'.
- reader 2: instruction: The required form (indirect question) is not stated; 'polite' is the only clue. Direct polite questions (Could you look for my scarf? / Did anyone find...?) are correct English and may fail the check.

## r21b-1-039 · B1.1 · write · built-in

Task: You want to join an evening Italian course at a language school, but the website doesn't say when it begins. Write one polite question to the school.
Key: {"kind": "write", "model": "Could you tell me when the next Italian course starts?", "must": ["Start politely: *Could you tell me …?*, *Do you know …?* or *I'd like to know …*", "Then a question word or *if*: *… when the next course starts*.", "After the question word the subject comes first, with no *do / does*: *when the course starts*, not *when does the course start*."]}
- reader 2: instruction: Same: form not stated; direct 'When does the course begin, please?' is polite enough and correct.

## r21b-1-040 · B1.2 · write · built-in

Task: You ordered a printer online ten days ago, but it still hasn't arrived. Write one polite question to the shop's customer service.
Key: {"kind": "write", "model": "Could you tell me if you have sent my order yet?", "must": ["Start politely: *Could you tell me …?*, *Do you know …?* or *I'd like to know …*", "Then *if* (or *whether*) or a question word: *… if you have sent my order*, *… when my printer will arrive*.", "After *if* or the question word the subject comes first, with no *did*: *if you sent my order*, *when my printer will arrive*."]}
- reader 2: instruction: Form not stated; many polite non-indirect-question answers are correct (Could you check my order?). 'Question' + 'polite' is ambiguous.

## r21b-1-041 · B1.1 · mcq · articles-split-1.csv:5

Task: Which sentence is NOT correct?
options: We had lunch near the river. | They went skiing in the Alps. | My sister is learning Italian. | We visited the Riga last summer.
Key: {"kind": "mcq", "correct": "We visited the Riga last summer.", "wrong": ["My sister is learning Italian.", "We had lunch near the river.", "They went skiing in the Alps."]}
- reader 1: sense: 'the Riga' is a believable error for article-less L1s.

## r21b-1-042 · B1.1 · mcq · b1-cond-rep-1.csv:39

Task: Choose the correct option: If you leave milk out of the fridge all day, it ___ sour.
options: goes | went | would go
Key: {"kind": "mcq", "correct": "goes", "wrong": ["went", "would go"]}
- reader 1: a wrong option that fits: 'would go' is grammatical but unnatural (a general truth, not hypothetical).
- reader 1: level: Easy for B1.1.

## r21b-1-043 · B1.1 · mcq · b1-cond-rep-1.csv:40

Task: Choose the correct option: I get a headache if I ___ too much coffee.
options: drink | will drink | drank
Key: {"kind": "mcq", "correct": "drink", "wrong": ["will drink", "drank"]}
- reader 1: level: Easy.

## r21b-1-044 · B1.1 · mcq · b1-cond-rep-1.csv:42

Task: Which sentence is NOT correct?
options: If the battery will get low, the screen goes dark. | If people don't drink enough water, they get headaches. | We eat outside when the weather is warm. | My cat hides when it hears thunder.
Key: {"kind": "mcq", "correct": "If the battery will get low, the screen goes dark.", "wrong": ["My cat hides when it hears thunder.", "If people don't drink enough water, they get headaches.", "We eat outside when the weather is warm."]}
- reader 1: sense: Near-duplicate of 045 and 047 (will after if).

## r21b-1-045 · B1.1 · mcq · b1-cond-rep-1.csv:43

Task: Which sentence is NOT correct?
options: When I travel by bus, I always feel sick. | If the battery is low, the phone switches off. | Whenever my neighbour plays music, my dog barks. | If metal will get hot, it expands.
Key: {"kind": "mcq", "correct": "If metal will get hot, it expands.", "wrong": ["When I travel by bus, I always feel sick.", "If the battery is low, the phone switches off.", "Whenever my neighbour plays music, my dog barks."]}
- reader 1: sense: Near-duplicate of 044.

## r21b-1-046 · B1.1 · mcq · b1-cond-rep-1.csv:72

Task: Choose the correct option: They won't let you in ___ you show your ticket.
options: as soon as | when | if | unless
Key: {"kind": "mcq", "correct": "unless", "wrong": ["if", "when", "as soon as"]}
- reader 1: a wrong option that fits: 'if' is grammatical but illogical here.
- reader 2: a wrong option that fits: 'if' is grammatical but illogical ('won't let you in if you show your ticket').

## r21b-1-050 · B1.2 · match · b1-cond-rep-1.csv:140

Task: Match each sentence with its meaning.
left: If I had gone, I would have met her. | If I hadn't gone, I wouldn't have met her. | If I went, I would meet her.
right: I'm not going. | I went. | I didn't go.
Key: {"kind": "match", "pairs": [["If I had gone, I would have met her.", "I didn't go."], ["If I hadn't gone, I wouldn't have met her.", "I went."], ["If I went, I would meet her.", "I'm not going."]]}
- reader 2: sense: 'If I went, I would meet her' does not say 'I'm not going'; it is an unreal/unlikely future-or-present idea, so the pairing is by elimination only.

