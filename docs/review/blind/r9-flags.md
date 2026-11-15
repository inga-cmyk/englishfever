# Blind check r9: flags for the judge

175 tasks, 2 readers.

## r9-004 · A2.1 · mcq · zz-blind-gap-points-a2-1.csv:5

Task: Choose the correct short answer: 'Have you got a bike?'
options: Yes, I have got. | Yes, I have. | Yes, I've. | Yes, I do.
Key: {"kind": "mcq", "correct": "Yes, I have.", "wrong": ["Yes, I have got.", "Yes, I do.", "Yes, I've."]}
- reader 1: a wrong option that fits: Yes, I do. (a normal answer to 'Have you got...?' in everyday British and American English)

## r9-011 · A2.1 · order · zz-blind-gap-points-a2-1.csv:12

Task: Put the words in order.
word_cards: today | have | don't | time | lunch | we | for
Key: {"kind": "order", "sentence": "we don't have time for lunch today", "also": []}
- reader 2: another correct answer, not accepted: ["we don't have time today for lunch"]

## r9-012 · A2.1 · order · zz-blind-gap-points-a2-1.csv:13

Task: Put the words in order.
word_cards: got | my | sauna | gym | a | new | has
Key: {"kind": "order", "sentence": "my gym has got a new sauna", "also": []}
- reader 1: another correct answer, not accepted: ['my new gym has got a sauna']
- reader 2: another correct answer, not accepted: ['my new gym has got a sauna']

## r9-017 · A2.1 · match · zz-blind-gap-points-a2-1.csv:18

Task: Match each question with its short answer.
left: Have you got a pen? | Do you have a ticket? | Has Mark got a job? | Does Anna have a sister?
right: No, I don't. | Yes, she does. | No, he hasn't. | Yes, I have.
Key: {"kind": "match", "pairs": [["Have you got a pen?", "Yes, I have."], ["Do you have a ticket?", "No, I don't."], ["Has Mark got a job?", "No, he hasn't."], ["Does Anna have a sister?", "Yes, she does."]]}
- reader 1: sense: Pairing is ambiguous: have got / do have short answers are interchangeable in everyday English
- reader 2: sense: 'Do you have a ticket?' - 'Yes, I have.' is also heard, so the two have/do pairs are not fully exclusive; 'Have you got a pen?' - 'No, I don't.' is odd but understandable.

## r9-018 · A2.1 · gap · zz-blind-gap-points-a2-1.csv:19

Task: My sister ___ three cats. (have got)
Key: {"kind": "gap", "accepted": [["has got", "'s got"]]}
- reader 1: instruction: The brackets give the verb form; only conjugation is tested

## r9-019 · A2.1 · gap · zz-blind-gap-points-a2-1.csv:20

Task: We ___ a car, so we cycle to work. (not / have got)
Key: {"kind": "gap", "accepted": [["haven't got", "have not got"]]}
- reader 1: another correct answer, not accepted: [["don't have"]]
- reader 1: instruction: Hint '(not / have got)' gives the form away; 'don't have' also fits the sentence

## r9-020 · A2.1 · gap · zz-blind-gap-points-a2-1.csv:21

Task: 'Has the new library got a café?' 'Yes, it ___.'
Key: {"kind": "gap", "accepted": [["has"]]}
- reader 1: another correct answer, not accepted: [['has got']]

## r9-022 · A2.1 · gap · zz-blind-gap-points-a2-1.csv:23

Task: My grandparents ___ a computer. (not / have)
Key: {"kind": "gap", "accepted": [["don't have", "haven't got", "haven't", "have no"]]}
- reader 1: instruction: Hint is '(not / have)' but 'haven't got' also fits; learner may be unsure whether 'got' is allowed
- reader 2: instruction: Cue '(not / have)' is ambiguous: 'haven't got' is also correct English though it does not use the cue verb exactly.

## r9-025 · A2.1 · text · zz-blind-gap-points-a2-1.csv:26

Task: Make a question with *How many*: She has got two children.
Key: {"kind": "text", "accepted": [["How many children has she got?", "How many children does she have?", "How many children has she?"]]}
- reader 1: another correct answer, not accepted: ['How many kids has she got?', 'How many kids does she have?']
- reader 2: another correct answer, not accepted: ['How many kids has she got?', 'How many kids does she have?']

## r9-038 · A2.1 · gap · zz-blind-gap-points-a2-1.csv:39

Task: I'm bored. ___ we go for a walk?
word_cards: Will | Shall | Do
Key: {"kind": "gap", "accepted": [["Shall"]]}
- reader 2: a wrong option that fits: 'Will' makes a grammatical question (prediction) but not a suggestion; not fitting here.

## r9-040 · A2.1 · gap · zz-blind-gap-points-a2-1.csv:41

Task: What ___ ___ watch tonight?
word_cards: we | you | shall
Key: {"kind": "gap", "accepted": [["shall"], ["we"]]}
- reader 1: a wrong option that fits: 'you' (What shall you watch tonight?) is grammatical but archaic and odd as a suggestion; not a real problem
- reader 2: sense: 'What shall you watch' is grammatical but archaic/odd; only 'we' is natural.

## r9-048 · A2.1 · text · zz-blind-gap-points-a2-1.csv:49

Task: Say it another way with *Shall I*: Do you want me to book a table?
Key: {"kind": "text", "accepted": [["Shall I book a table?", "Shall I book a table for you?", "Shall I book a table for us?"]]}
- reader 1: another correct answer, not accepted: ['Shall I reserve a table?', 'Shall I book you a table?']
- reader 2: another correct answer, not accepted: ['Shall I reserve a table?', 'Shall I book us a table?', 'Shall I book you a table?']

## r9-049 · A2.1 · text · zz-blind-gap-points-a2-1.csv:50

Task: Make a question with *Where*: Shall we go to Italy this summer?
Key: {"kind": "text", "accepted": [["Where shall we go this summer?", "Where shall we go?"]]}
- reader 1: another correct answer, not accepted: ['Where shall we go in the summer?', 'Where shall we go in Italy this summer?']
- reader 1: sense: Learners may keep 'Italy' (e.g. 'Where shall we go in Italy...') which is also fine
- reader 2: another correct answer, not accepted: ['Where shall we go in the summer?']

## r9-050 · A2.1 · text · zz-blind-gap-points-a2-1.csv:51

Task: Make a question with *What*: Shall we cook pasta tonight?
Key: {"kind": "text", "accepted": [["What shall we cook tonight?", "What shall we cook?"]]}
- reader 1: another correct answer, not accepted: ['What shall we cook for dinner tonight?']
- reader 2: another correct answer, not accepted: ['What shall we cook for dinner tonight?']

## r9-051 · A2.1 · mcq · zz-blind-gap-points-a2-1.csv:52

Task: Choose the correct option: We went to ___ Croatia last summer.
options: the | a | —
Key: {"kind": "mcq", "correct": "—", "wrong": ["the", "a"]}
- reader 1: instruction: '—' as an option is not explained to the learner (means no word)

## r9-052 · A2.1 · mcq · zz-blind-gap-points-a2-1.csv:53

Task: Choose the correct option: My sister teaches ___ maths in Riga.
options: a | the | —
Key: {"kind": "mcq", "correct": "—", "wrong": ["the", "a"]}
- reader 1: instruction: '—' option not explained

## r9-053 · A2.1 · mcq · zz-blind-gap-points-a2-1.csv:54

Task: Choose the correct option: I'm vegetarian. I don't eat ___ meat.
options: the | — | a
Key: {"kind": "mcq", "correct": "—", "wrong": ["the", "a"]}
- reader 1: instruction: '—' option not explained

## r9-060 · A2.1 · order · zz-blind-gap-points-a2-1.csv:61

Task: Put the words in order.
word_cards: met | in | paris | i | my | wife | and
Key: {"kind": "order", "sentence": "my wife and i met in paris", "also": []}
- reader 1: answer not accepted: i met my wife in paris
- reader 2: another correct answer, not accepted: ['i and my wife met in paris (poor style, not natural)']
- the readers disagree

## r9-063 · A2.1 · gap · zz-blind-gap-points-a2-1.csv:64

Task: Our new manager is from ___ Sweden.
word_cards: the | —
Key: {"kind": "gap", "accepted": [["—"]]}
- reader 1: instruction: '—' card not explained

## r9-064 · A2.1 · gap · zz-blind-gap-points-a2-1.csv:65

Task: I usually listen to ___ jazz in the car.
word_cards: the | —
Key: {"kind": "gap", "accepted": [["—"]]}
- reader 1: instruction: '—' card not explained

## r9-065 · A2.1 · gap · zz-blind-gap-points-a2-1.csv:66

Task: I think ___ dogs are better pets than cats.
word_cards: — | the
Key: {"kind": "gap", "accepted": [["—"]]}
- reader 1: instruction: '—' card not explained

## r9-066 · A2.1 · gap · zz-blind-gap-points-a2-1.csv:67

Task: My kids spend hours on ___ social media.
word_cards: the | —
Key: {"kind": "gap", "accepted": [["—"]]}
- reader 1: instruction: '—' card not explained

## r9-069 · A2.1 · gap · zz-blind-gap-points-a2-1.csv:70

Task: In big cities, ___ are often faster than cars. (bike)
Key: {"kind": "gap", "accepted": [["bikes"]]}
- reader 1: another correct answer, not accepted: [['bicycles']]
- reader 2: another correct answer, not accepted: [['bicycles']]

## r9-083 · A2.2 · gap · zz-blind-gap-points-a2-1.csv:84

Task: Complete with one word: My sister doesn't live with us any ___.
Key: {"kind": "gap", "accepted": [["more", "longer"]]}
- reader 2: instruction: 'any more' and 'any longer' both fit; the instruction does not say which.

## r9-086 · A2.2 · gap · zz-blind-gap-points-a2-1.csv:87

Task: Write *no longer* or *any more*: We don't go camping ___.
Key: {"kind": "gap", "accepted": [["any more", "anymore", "any longer"]]}
- reader 2: instruction: Only the two named phrases are offered, but 'any longer' is also correct (will a learner be marked wrong?).

## r9-090 · A2.2 · text · zz-blind-gap-points-a2-1.csv:91

Task: Say it another way with *any more*: Ben no longer studies Spanish.
Key: {"kind": "text", "accepted": [["Ben doesn't study Spanish any more.", "Ben doesn't study Spanish anymore.", "Ben isn't studying Spanish any more.", "Ben isn't studying Spanish anymore.", "Ben's not studying Spanish any more.", "Ben's not studying Spanish anymore."]]}
- reader 1: another correct answer, not accepted: ["Ben doesn't study Spanish any longer."]
- reader 2: another correct answer, not accepted: ["Ben doesn't study Spanish any longer."]

## r9-095 · A2.2 · order · zz-blind-gap-points-a2-1.csv:96

Task: Put the words in order.
word_cards: any | not | my | he's | longer | neighbour
Key: {"kind": "order", "sentence": "he's not my neighbour any longer", "also": []}
- reader 1: sense: Cards use 'any longer' while the set teaches 'any more'; fine

## r9-115 · A2.2 · text · zz-blind-gap-points-a2-1.csv:116

Task: Say it another way with *Can I*: Can you lend me some money?
Key: {"kind": "text", "accepted": [["Can I borrow some money?", "Can I borrow some money from you?", "Can I borrow some money, please?", "Can I please borrow some money?", "Can I borrow some money from you, please?", "Can I please borrow some money from you?"]]}
- reader 2: another correct answer, not accepted: ['Can I have some money?']

## r9-143 · A2.2 · gap · zz-blind-gap-points-a2-1.csv:144

Task: Is ___ a car expensive in Riga? (rent)
Key: {"kind": "gap", "accepted": [["renting"]]}
- reader 1: another correct answer, not accepted: [['to rent']]

## r9-150 · A2.2 · text · zz-blind-gap-points-a2-1.csv:151

Task: Make a yes/no question: Using this app saves you time.
Key: {"kind": "text", "accepted": [["Does using this app save you time?"]]}
- reader 2: another correct answer, not accepted: ['Does using this app save time?']

## r9-151 · A2.2 · mcq · zz-blind-gap-points-a2-1.csv:152

Task: Choose the correct option: We often go ___ fishing at the lake.
options: — | for | to
Key: {"kind": "mcq", "correct": "—", "wrong": ["to", "for"]}
- reader 1: instruction: '—' option not explained

## r9-165 · A2.2 · text · zz-blind-gap-points-a2-1.csv:166

Task: Say it another way with *for*: I took a short walk after lunch.
Key: {"kind": "text", "accepted": [["I went for a short walk after lunch.", "After lunch, I went for a short walk.", "I went out for a short walk after lunch.", "After lunch, I went out for a short walk."]]}
- reader 2: another correct answer, not accepted: ['I went for a walk after lunch.']

