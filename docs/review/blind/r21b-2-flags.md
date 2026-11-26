# Blind check r21b-2: flags for the judge

50 tasks, 2 readers.

## r21b-2-003 · B1.1 · order · b1-cond-rep-1.csv:151

Task: Put the words in order.
word_cards: they | said | they | eaten | already | had
Key: {"kind": "order", "sentence": "they said they had already eaten", "also": ["they said they had eaten already"]}
- reader 1: another correct answer, not accepted: ['they had already eaten they said']
- reader 1: instruction: No context; fine, but 'they had already eaten, they said' is a reorder with a comma the cards lack.
- reader 2: another correct answer, not accepted: [['they said they had eaten already']]

## r21b-2-004 · B1.2 · order · b1-cond-rep-1.csv:153

Task: Put the words in order.
word_cards: he | he | was | said | come | couldn't | ill | because | he
Key: {"kind": "order", "sentence": "he said he couldn't come because he was ill", "also": ["because he was ill he said he couldn't come"]}
- reader 1: another correct answer, not accepted: ["he couldn't come because he was ill he said", "he said he was ill because he couldn't come", "he couldn't come because he said he was ill", "because he was ill he couldn't come he said"]
- reader 1: instruction: Many valid orders but the instruction does not say more than one answer is possible; the three 'he' cards allow several meanings.
- reader 2: another correct answer, not accepted: ["he said he was ill because he couldn't come", "he couldn't come because he said he was ill"]
- reader 2: instruction: Three identical 'he' cards and several grammatical orders; the intended one is not forced by the cards.

## r21b-2-005 · B1.1 · mcq · b1-cond-rep-1.csv:180

Task: Which sentence is NOT correct?
options: They said they had already eaten. | My boss told that the meeting was cancelled. | She said that she was tired. | He told me he would call later.
Key: {"kind": "mcq", "correct": "My boss told that the meeting was cancelled.", "wrong": ["She said that she was tired.", "He told me he would call later.", "They said they had already eaten."]}
- reader 1: sense: Option A is the same sentence as task 003 (near-copy across tasks).

## r21b-2-006 · B1.2 · mcq · b1-cond-rep-1.csv:181

Task: Which sentence is NOT correct?
options: They said they will come the next day. | He said he couldn't find his keys. | She said she was working from home that day. | They said they had booked a table.
Key: {"kind": "mcq", "correct": "They said they will come the next day.", "wrong": ["She said she was working from home that day.", "He said he couldn't find his keys.", "They said they had booked a table."]}
- reader 2: sense: 'will' with 'next day' can be defended as reporting a still-future event; the sentence is only marked wrong by strict backshift.

## r21b-2-007 · B1.2 · gap · b1-cond-rep-1.csv:207

Task: At school, years ago: 'Do you like jazz?' → He asked me ___.
Key: {"kind": "gap", "accepted": [["if I liked jazz", "whether I liked jazz", "if I liked jazz or not", "whether I liked jazz or not", "whether or not I liked jazz"]]}
- reader 1: another correct answer, not accepted: [['if I had liked jazz'], ['if I like jazz']]
- reader 1: instruction: Gap holds a whole clause (several words) though the note says one gap; typed answers will vary (if/whether, 'jazz music'). 'if I like jazz' is not wrong in principle but 'years ago' calls for the past; do not accept it unless intended.

## r21b-2-010 · B1.2 · gap · b1-cond-rep-1.csv:234

Task: I wonder ___ he will come.
word_cards: what | whether
Key: {"kind": "gap", "accepted": [["whether"]]}
- reader 1: instruction: Fine, but 'if' is the usual word at this level and is not offered; only one card works so the task is easy.

## r21b-2-011 · B1.1 · order · b1-new-1.csv:5

Task: Put all the words in order. More than one answer is possible.
word_cards: but | loves | it | now | cooking | she | enjoy | to | she | use | didn't
Key: {"kind": "order", "sentence": "she didn't use to enjoy cooking but now she loves it", "also": ["she didn't use to enjoy cooking but she loves it now", "she loves cooking now but she didn't use to enjoy it", "now she loves cooking but she didn't use to enjoy it"]}
- reader 1: another correct answer, not accepted: ["she didn't use to enjoy it but now she loves cooking", "she didn't use to enjoy it but she loves cooking now"]
- reader 1: level: 'used to' with didn't (use to) and two clauses are fine for B1.1 but the sentence is long (11 cards).
- reader 2: another correct answer, not accepted: [["she didn't use to enjoy it but now she loves cooking"], ["now she loves cooking but she didn't use to enjoy it"], ["now she loves it but she didn't use to enjoy cooking"], ["she loves cooking now but she didn't use to enjoy it"], ["she loves it now but she didn't use to enjoy cooking"], ["she didn't use to enjoy cooking but she loves it now"], ["she didn't use to enjoy it but she loves cooking now"]]

## r21b-2-012 · B1.2 · order · b1-new-1.csv:8

Task: Put the words in order.
word_cards: child | every | sunday | a | i | used | my | to | when | was | visit | grandparents | we
Key: {"kind": "order", "sentence": "when i was a child we used to visit my grandparents every sunday", "also": ["we used to visit my grandparents every sunday when i was a child", "every sunday we used to visit my grandparents when i was a child", "when i was a child every sunday we used to visit my grandparents"]}
- reader 1: another correct answer, not accepted: ['every sunday when i was a child we used to visit my grandparents']
- reader 1: instruction: Several correct orders, but the instruction does not say more than one answer is possible. Cards 'i' and 'sunday' are lower case (capitalisation clue lost/confusing). 13 cards is long.
- reader 2: another correct answer, not accepted: ['every sunday when i was a child we used to visit my grandparents', 'we used to visit my grandparents when i was a child every sunday']
- reader 2: level: 13 cards, long for B1.2 ordering; many valid orders.

## r21b-2-013 · B1.2 · order · b1-new-1.csv:10

Task: Put all the words in order. More than one answer is possible.
word_cards: up | getting | not | am | so | early | to | used | i
Key: {"kind": "order", "sentence": "i am not used to getting up so early", "also": ["i am used to not getting up so early", "i am not so used to getting up early"]}
- reader 1: another correct answer, not accepted: ['i am so not used to getting up early']
- reader 1: instruction: Instruction says more than one answer, ok; but 'used to' vs 'be used to' choice is signalled by 'am'. 'I am not used to getting up so early' only differs from the alternative by placing 'so'.
- reader 2: instruction: Says more than one answer is possible; second order is slightly awkward.

## r21b-2-014 · B1.1 · gap · b1-new-1.csv:20

Task: When I was a teenager, I ___ any money, so I walked everywhere. (not / have)
Key: {"kind": "gap", "accepted": [["didn't use to have", "did not use to have", "didn't have", "did not have", "used not to have", "hadn't", "had not"]]}
- reader 1: instruction: '(not / have)' gives the verb but not the tense; a learner could type ['didn't','have'] as separate gaps? only one gap. Past simple fits 'was a teenager' - fine.
- reader 2: level: Fairly easy for B1.1 unless 'used to' is intended.

## r21b-2-015 · B1.1 · mcq · b1-new-1.csv:26

Task: Which sentence is NOT correct?
options: Did you used to play chess? | Are you used to the new office yet? | My dad used to work at night. | We didn't use to have a dishwasher.
Key: {"kind": "mcq", "correct": "Did you used to play chess?", "wrong": ["My dad used to work at night.", "We didn't use to have a dishwasher.", "Are you used to the new office yet?"]}
- reader 1: sense: Fine; common learner error.
- reader 2: sense: 'Did you used to' is common in speech and some say acceptable; learners really do write it, but strict grammar says 'use to'.

## r21b-2-016 · B1.1 · gap · b1-new-1.csv:50

Task: She plays ___ violin in an orchestra.
word_cards: an | the | —
Key: {"kind": "gap", "accepted": [["the"]]}
- reader 2: instruction: Card '—' (no word) may confuse learners.

## r21b-2-022 · B1.2 · text · b1-new-2.csv:36

Task: Join the two sentences with *who*: My uncle lives in Spain. He is a chef.
Key: {"kind": "text", "accepted": [["My uncle, who lives in Spain, is a chef.", "My uncle, who is a chef, lives in Spain."]]}
- reader 1: instruction: Unclear which sentence to turn into the who-clause: both joinings are correct. Without commas the sentence implies other uncles (less natural). Needs 'use the second sentence as the who-clause' or one fixed answer.
- reader 2: instruction: Two directions possible; instruction does not say which sentence to attach 'who' to.

## r21b-2-027 · B1.2 · mcq · b1-new-3.csv:86

Task: Which sentence is NOT correct?
options: How many people signed up for the course? | Which team won the match on Saturday? | Which colleague did suggested the new plan? | What did your manager say about the report?
Key: {"kind": "mcq", "correct": "Which colleague did suggested the new plan?", "wrong": ["Which team won the match on Saturday?", "What did your manager say about the report?", "How many people signed up for the course?"]}
- reader 1: sense: Same error pattern as task 026 (did + past form); repetitive.

## r21b-2-028 · B1.1 · text · b1-new-3.csv:90

Task: There's a loud bang in the kitchen. Ask your flatmate. Use *What* and *make*:
Key: {"kind": "text", "accepted": [["What made that noise?", "What made the noise?", "What made that bang?", "What made the bang?", "What made that sound?", "What made the sound?", "What made that?", "What made it?"]]}
- reader 1: another correct answer, not accepted: ['What made that loud bang?', 'What made that loud noise?', 'What made that noise in the kitchen?', 'What was making that noise?', "What's making that noise?"]
- reader 1: instruction: Open: the learner must guess the noun (noise/bang) and the use of 'make' = cause is not obvious; 'What was that noise?' would be the natural question without 'make'.
- reader 1: level: 'make' meaning cause in a question is above B1.1 for many learners.
- reader 2: another correct answer, not accepted: ['What made that loud noise?', 'What made that loud bang?', 'What made that noise in the kitchen?']

## r21b-2-033 · B1.2 · mcq · b1-new-4.csv:77

Task: Which sentence is NOT correct?
options: The shoes ought to taken off. | The plants have to be watered every day. | The meeting might be moved to Friday. | Can this jacket be washed at home?
Key: {"kind": "mcq", "correct": "The shoes ought to taken off.", "wrong": ["The meeting might be moved to Friday.", "Can this jacket be washed at home?", "The plants have to be watered every day."]}
- reader 1: sense: 'ought to taken' (missing 'be') is a believable slip but rarer; 'should taken' in task 032 is the same error.

## r21b-2-034 · B1.2 · text · b1-new-4.csv:84

Task: Start with *The accident*: Someone could have avoided the accident.
Key: {"kind": "text", "accepted": [["The accident could have been avoided.", "The accident could have been avoided by someone.", "The accident could've been avoided.", "The accident could've been avoided by someone."]]}
- reader 1: another correct answer, not accepted: ['The accident could have been avoided by somebody.']
- reader 1: instruction: Passive is not signalled; 'Start with The accident' is the only hint (acceptable), but the learner could write 'The accident could have been avoidable' etc.
- reader 2: another correct answer, not accepted: ['The accident might have been avoided.', 'The accident could have been prevented.']
- reader 2: instruction: Instruction does not rule out other modals or synonyms.

## r21b-2-037 · B1.1 · gap · b1-new-4.csv:145

Task: She introduced her new colleague ___ the whole team.
word_cards: to | for | —
Key: {"kind": "gap", "accepted": [["to"]]}
- reader 1: sense: Near-duplicate of task 040 (to-card gap vs to-option).

## r21b-2-040 · B1.1 · mcq · b1-new-4.csv:162

Task: Choose the correct option: He lent his car ___ his neighbour.
options: — | for | to
Key: {"kind": "mcq", "correct": "to", "wrong": ["for", "—"]}
- reader 1: sense: Near-duplicate pattern of task 037.

## r21b-2-041 · B1.1 · mcq · b1-new-4.csv:200

Task: Which sentence is correct?
options: It was an amazed experience, and we were all amazed. | It was an amazed experience, and we were all amazing. | It was an amazing experience, and we were all amazed. | It was an amazing experience, and we were all amazing.
Key: {"kind": "mcq", "correct": "It was an amazing experience, and we were all amazed.", "wrong": ["It was an amazed experience, and we were all amazing.", "It was an amazing experience, and we were all amazing.", "It was an amazed experience, and we were all amazed."]}
- reader 1: instruction: Unusual: instruction asks which sentence is CORRECT while nearly all other tasks ask NOT correct (fine, but note the change).
- reader 1: sense: Wrong options are believable.
- reader 2: instruction: Question wording ('correct') differs from the usual 'NOT correct' format; fine but easy to misread.

## r21b-2-043 · B1.1 · mcq · b1-new-5.csv:25

Task: Which sentence is NOT correct?
options: He drives a small Japanese car. | I found a beautiful wooden box. | We sat at a big round table. | She wore a cotton white dress.
Key: {"kind": "mcq", "correct": "She wore a cotton white dress.", "wrong": ["We sat at a big round table.", "He drives a small Japanese car.", "I found a beautiful wooden box."]}
- reader 1: sense: Tasks 043-045 test the same adjective-order rule three times.

## r21b-2-046 · B1.2 · mcq · b1-new-5.csv:76

Task: Choose the correct option: The soup wasn't hot ___ to eat.
options: quite | too | very | enough
Key: {"kind": "mcq", "correct": "enough", "wrong": ["too", "very", "quite"]}
- reader 1: level: Very easy for B1.2 (only 'enough' with 'not ... to' is typical); 'too' fits only if the sentence were positive.

## r21b-2-049 · B1.1 · gap · b1-new-5.csv:102

Task: Thank you for your help. You've been ___ kind.
word_cards: such a | such | so
Key: {"kind": "gap", "accepted": [["so"]]}
- reader 1: sense: 'such a' could be thought to fit ('such a kind [person]') but the sentence ends in 'kind' so it is wrong; fine.
- reader 2: sense: 'such a' / 'such' only work if a noun follows; none does, so the distractors are fair but 'such a' looks tempting.

