# Blind check r21b-3: flags for the judge

50 tasks, 2 readers.

## r21b-3-004 · B1.1 · mcq · b1-new-5.csv:116

Task: Choose the correct option: It was ___ surprise to see him at the party.
options: so | such a | so a | such
Key: {"kind": "mcq", "correct": "such a", "wrong": ["so", "such", "so a"]}
- reader 1: sense: 'so a' is a form learners hardly ever write; weak distractor.

## r21b-3-006 · B1.1 · order · b1-new-5.csv:136

Task: Put the words in order.
word_cards: like | would | something | you | drink | to
Key: {"kind": "order", "sentence": "would you like something to drink", "also": ["you would like something to drink", "would you like to drink something"]}
- reader 1: instruction: No capital letter or question mark on the cards, so the statement 'you would like something to drink' is also correct English; question not forced.
- reader 1: level: Very basic (A1-A2); too easy for B1.1.
- reader 2: instruction: Both 'would you like something to drink' and 'would you like to drink something' use all cards.

## r21b-3-010 · B1.1 · order · b1-passives-1.csv:39

Task: Put the words in order.
word_cards: and | still | used | it | 1932 | the | in | built | is | was | today | bridge
Key: {"kind": "order", "sentence": "the bridge was built in 1932 and it is still used today", "also": ["the bridge was built in 1932 and today it is still used", "in 1932 the bridge was built and it is still used today", "the bridge is still used today and it was built in 1932"]}
- reader 1: another correct answer, not accepted: [['the bridge was built in 1932 and today it is still used'], ['the bridge is still used today and it was built in 1932'], ['in 1932 the bridge was built and it is still used today'], ['today the bridge is still used and it was built in 1932'], ['the bridge was built in 1932 and it is used still today (less natural)']]
- reader 1: instruction: No capitals/punctuation, so several orders work; ambiguous about which clause comes first.
- reader 1: level: 12 cards is long for B1.1.
- reader 2: another correct answer, not accepted: ['today the bridge is still used and it was built in 1932', 'it was built in 1932 and the bridge is still used today']
- reader 2: instruction: Many valid orders (clauses can swap, 'in 1932' can start); key must accept them. 12 cards is long for B1.1.
- reader 2: level: 12 cards, two clauses with passive in two tenses: above B1.1 length.

## r21b-3-011 · B1.1 · text · b1-passives-1.csv:62

Task: Rewrite the sentence. Start with *My laptop*: Someone stole my laptop yesterday.
Key: {"kind": "text", "accepted": [["My laptop was stolen yesterday.", "My laptop was stolen by someone yesterday.", "Yesterday my laptop was stolen.", "Yesterday my laptop was stolen by someone.", "My laptop got stolen yesterday.", "Yesterday my laptop got stolen."]]}
- reader 1: another correct answer, not accepted: ['My laptop was stolen yesterday by someone.']
- reader 2: another correct answer, not accepted: ['My laptop was stolen yesterday by someone.']

## r21b-3-012 · B1.1 · text · b1-passives-1.csv:63

Task: Start with *This factory*: The company built this factory in 1990.
Key: {"kind": "text", "accepted": [["This factory was built by the company in 1990.", "This factory was built in 1990.", "In 1990 this factory was built by the company.", "In 1990 this factory was built.", "This factory was built in 1990 by the company."]]}
- reader 1: instruction: No 'Rewrite' verb (inconsistent with other text tasks); learner may not know the sentence must stay passive-equivalent; leaving out 'by the company' is also acceptable.

## r21b-3-016 · B1.1 · text · b1-passives-1.csv:131

Task: Start with *My umbrella*: Someone has taken my umbrella.
Key: {"kind": "text", "accepted": [["My umbrella has been taken.", "My umbrella has been taken by someone.", "My umbrella's been taken.", "My umbrella's been taken by someone."]]}
- reader 2: another correct answer, not accepted: ['My umbrella has been stolen.']

## r21b-3-021 · B1.1 · order · b1-tenses-1.csv:3

Task: Put the words in order.
word_cards: to | eats | rarely | prefers | she | at | out | she | because | home | cook
Key: {"kind": "order", "sentence": "she rarely eats out because she prefers to cook at home", "also": ["because she prefers to cook at home she rarely eats out", "she eats out rarely because she prefers to cook at home", "because she prefers to cook at home she eats out rarely"]}
- reader 1: another correct answer, not accepted: [['she prefers to cook at home because she rarely eats out'], ['because she prefers to cook at home she rarely eats out'], ['because she rarely eats out she prefers to cook at home'], ['she eats out rarely because she prefers to cook at home'], ['she eats out rarely because she prefers to cook at home']]
- reader 1: instruction: No capitals or comma; many orders are possible (clauses can swap; 'rarely' can move).
- reader 1: level: 11 cards, two clauses; long for B1.1.
- reader 2: another correct answer, not accepted: ['she prefers to cook at home because she rarely eats out', 'she prefers to cook at home because she eats out rarely', 'because she rarely eats out she prefers to cook at home']
- reader 2: instruction: Two clauses can swap; many valid orders. 11 cards is long for B1.1.
- reader 2: level: 11 cards, two clauses: long for B1.1.

## r21b-3-022 · B1.1 · order · b1-tenses-1.csv:5

Task: Put the words in order.
word_cards: work | the | same | does | for | company | still | brother | your
Key: {"kind": "order", "sentence": "does your brother still work for the same company", "also": ["does your brother work for the same company still"]}
- reader 1: another correct answer, not accepted: [['does your brother work for the same company still (less natural)']]
- reader 1: level: Present simple question, A2; easy for B1.1.
- reader 2: another correct answer, not accepted: ['your brother does still work for the same company']
- reader 2: instruction: Only a question; 'does ... still' order is the only natural one (the statement 'your brother does still work...' is emphatic, not natural).

## r21b-3-023 · B1.1 · order · b1-tenses-1.csv:9

Task: Put the words in order.
word_cards: in | what | word | your | language | mean | this | does
Key: {"kind": "order", "sentence": "what does this word mean in your language", "also": ["in your language what does this word mean"]}
- reader 1: another correct answer, not accepted: [['what does this word in your language mean'], ['in your language what does this word mean']]
- reader 1: level: A2-level question; easy for B1.1.
- reader 2: another correct answer, not accepted: ['what does your word mean in this language', 'in this language what does your word mean']
- reader 2: sense: Alternatives 'what does your word mean in this language' are grammatical but odd.

## r21b-3-024 · B1.1 · gap · b1-tenses-1.csv:24

Task: How much ___ a ticket to the capital ___ ? (cost)
Key: {"kind": "gap", "accepted": [["does", "did", "will", "would"], ["cost"]]}
- reader 1: instruction: No time word, so past, present and future all fit.
- reader 1: level: A1-A2; too easy for B1.1.
- reader 2: instruction: No time or context given: does/did/will/would all fit.

## r21b-3-025 · B1.1 · text · b1-tenses-1.csv:28

Task: Make a question with What time: The bank opens at nine.
Key: {"kind": "text", "accepted": [["What time does the bank open?", "What time does the bank open at?", "At what time does the bank open?"]]}
- reader 1: level: A1-A2; too easy for B1.1.

## r21b-3-026 · B1.1 · mcq · b1-tenses-1.csv:36

Task: Which sentence is NOT correct?
options: Does your company pay for training? | My colleagues often work from home on Fridays. | Our manager don't like long meetings. | The office opens at eight.
Key: {"kind": "mcq", "correct": "Our manager don't like long meetings.", "wrong": ["My colleagues often work from home on Fridays.", "Does your company pay for training?", "The office opens at eight."]}
- reader 1: level: Third-person -s is A1-A2; too easy for B1.1.

## r21b-3-027 · B1.1 · mcq · b1-tenses-1.csv:40

Task: Which sentence is NOT correct?
options: The shop closes at six on Saturdays. | Does your sister still live in Berlin? | He doesn't goes to the gym on Sundays. | I usually cycle to work in summer.
Key: {"kind": "mcq", "correct": "He doesn't goes to the gym on Sundays.", "wrong": ["Does your sister still live in Berlin?", "I usually cycle to work in summer.", "The shop closes at six on Saturdays."]}
- reader 1: level: Doesn't + base verb is A1-A2; too easy for B1.1.

## r21b-3-028 · B1.1 · order · b1-tenses-1.csv:47

Task: Put the words in order.
word_cards: this | you | it | take | can | are | using | chair | or | i
Key: {"kind": "order", "sentence": "are you using this chair or can i take it", "also": ["can i take this chair or are you using it", "are you using it or can i take this chair", "can i take it or are you using this chair"]}
- reader 1: another correct answer, not accepted: [['can i take this chair or are you using it'], ['are you using it or can i take this chair'], ['can i take it or are you using this chair'], ['this chair, are you using it or can i take it (less natural)']]
- reader 1: instruction: Many orders possible; lower-case 'i' card and no punctuation.
- reader 2: instruction: Several valid orders.

## r21b-3-029 · B1.1 · gap · b1-tenses-1.csv:58

Task: Anna ___ for a new flat at the moment because her rent is too high.
word_cards: is looking | looks | was looking
Key: {"kind": "gap", "accepted": [["is looking"]]}
- reader 1: level: Present continuous with 'at the moment' is A2; easy for B1.1.

## r21b-3-030 · B1.1 · gap · b1-tenses-1.csv:60

Task: My neighbour ___ his house this month, so there is a lot of noise. (paint)
Key: {"kind": "gap", "accepted": [["is painting", "has been painting", "'s painting", "'s been painting"]]}
- reader 1: another correct answer, not accepted: [['is going to paint']]
- reader 1: instruction: 'is going to paint' fits grammatically but not the noise now; 'this month' is ambiguous (could suit present perfect continuous 'has been painting').
- reader 1: level: A2; easy for B1.1.
- reader 2: instruction: Contraction possible.

## r21b-3-031 · B1.1 · mcq · b1-tenses-1.csv:74

Task: Which sentence is NOT correct?
options: I'm not understanding the instructions. | I'm reading a great book at the moment. | Is your brother still looking for a job? | I need a new charger for my phone.
Key: {"kind": "mcq", "correct": "I'm not understanding the instructions.", "wrong": ["I need a new charger for my phone.", "I'm reading a great book at the moment.", "Is your brother still looking for a job?"]}
- reader 1: sense: Informal English does sometimes use 'I'm not understanding'; arguably not wrong enough, and learners rarely make this particular mistake.

## r21b-3-033 · B1.1 · mcq · b1-tenses-1.csv:79

Task: Which sentence is NOT correct?
options: I'm not using the car today. | Our team is growing fast this year. | Are you still looking for a flat? | The manager is have a meeting with a client.
Key: {"kind": "mcq", "correct": "The manager is have a meeting with a client.", "wrong": ["Are you still looking for a flat?", "Our team is growing fast this year.", "I'm not using the car today."]}
- reader 1: sense: 'is have' is a rare learner error.

## r21b-3-034 · B1.1 · order · b1-tenses-1.csv:81

Task: Put the words in order.
word_cards: she | read | answered | it | and | letter | opened | she | the | twice | before
Key: {"kind": "order", "sentence": "she opened the letter and read it twice before she answered", "also": ["before she answered she opened the letter and read it twice", "she opened and read the letter twice before she answered it", "before she answered it she opened and read the letter twice"]}
- reader 1: another correct answer, not accepted: [['before she answered she opened the letter and read it twice'], ['she opened it and read the letter twice before she answered']]
- reader 1: instruction: Only one 'it' card, so 'answered' has no object; sounds incomplete ('answered it' / 'answered the letter' not possible). Several orders possible; no capitals or comma.
- reader 1: level: 11 cards, long for B1.1.
- reader 2: another correct answer, not accepted: ['she opened it and read the letter twice before she answered']
- reader 2: instruction: 'answered' has no object (only one 'it' card); second order is odd but grammatical.
- reader 2: level: 11 cards.
- reader 2: sense: 'before she answered' without object is slightly unnatural.

## r21b-3-035 · B1.1 · order · b1-tenses-1.csv:82

Task: Put the words in order.
word_cards: why | me | job | that | lost | your | you | didn't | tell | you
Key: {"kind": "order", "sentence": "why didn't you tell me that you lost your job", "also": []}
- reader 2: instruction: Two 'you' cards; fine.
- reader 2: level: 10 cards, indirect clause: top of B1.1.

## r21b-3-037 · B1.2 · mcq · b1-tenses-1.csv:111

Task: Which sentence is NOT correct?
options: He used to work as a taxi driver. | I didn't used to like olives. | I'm slowly getting used to the early starts. | Are you used to driving on the left yet?
Key: {"kind": "mcq", "correct": "I didn't used to like olives.", "wrong": ["Are you used to driving on the left yet?", "He used to work as a taxi driver.", "I'm slowly getting used to the early starts."]}
- reader 1: sense: 'didn't used to' is common in informal writing, though not standard; fine for a B1.2 exam-style point.
- reader 2: sense: Formal standard is 'didn't use to'; but 'didn't used to' is a form learners and many natives do write; borderline.

## r21b-3-040 · B1.1 · text · b1-tenses-2.csv:22

Task: Rewrite with *since*: I started learning English in 2019, and I'm still learning it.
Key: {"kind": "text", "accepted": [["I have been learning English since 2019.", "I have learned English since 2019.", "I have learnt English since 2019."]]}
- reader 1: another correct answer, not accepted: ["Since 2019 I've been learning English."]
- reader 1: instruction: Learner may use present perfect simple or continuous; both correct.
- reader 2: another correct answer, not accepted: ["I've been learning it since 2019.", 'Since 2019 I have been learning English.']
- reader 2: instruction: Many correct answers; 'I started...' already contains 2019.

## r21b-3-041 · B1.1 · text · b1-tenses-2.csv:24

Task: Make it negative: We have visited that museum.
Key: {"kind": "text", "accepted": [["We haven't visited that museum.", "We have not visited that museum.", "We have never visited that museum."]]}
- reader 1: another correct answer, not accepted: ["We haven't visited that museum yet."]
- reader 1: instruction: 'never' also makes it negative; instruction does not say whether to use not.
- reader 2: instruction: 'never' is not strictly 'negative' form but fits.

## r21b-3-042 · B1.1 · mcq · b1-tenses-2.csv:29

Task: Choose the correct option: She has worked here ___ 2019.
options: in | for | since
Key: {"kind": "mcq", "correct": "since", "wrong": ["for", "in"]}
- reader 1: level: Near-duplicate of 043; A2-B1.

## r21b-3-043 · B1.1 · mcq · b1-tenses-2.csv:30

Task: Choose the correct option: I've worked here ___ 2015.
options: for | since | already
Key: {"kind": "mcq", "correct": "since", "wrong": ["for", "already"]}
- reader 1: level: Near-duplicate of 042.
- reader 2: level: Almost identical to task 42.

## r21b-3-046 · B1.1 · text · b1-tenses-2.csv:55

Task: Make a question with How long: She has been learning Chinese.
Key: {"kind": "text", "accepted": [["How long has she been learning Chinese?", "How long has she been learning Chinese for?"]]}
- reader 1: another correct answer, not accepted: ['How long has she learned Chinese?', 'How long has she learnt Chinese?']
- reader 2: another correct answer, not accepted: ['How long has she learned Chinese?']

## r21b-3-047 · B1.1 · mcq · b1-tenses-2.csv:62

Task: Which sentence says how long?
options: I'm learning French with a teacher. | I've learned some French at school. | I've been learning French at evening classes. | I've been learning French for two years.
Key: {"kind": "mcq", "correct": "I've been learning French for two years.", "wrong": ["I've learned some French at school.", "I've been learning French at evening classes.", "I'm learning French with a teacher."]}
- reader 1: instruction: 'says how long' is unnatural; better 'Which sentence gives a length of time?'. Options 2 and 3 might be read as 'how long' by weaker learners.
- reader 2: instruction: 'says how long' is vague, but only one gives a duration.

