# Blind check r21-4: flags for the judge

60 tasks, 2 readers.

## r21-4-001 · B1.1 · mcq · built-in

Task: Is this statement true? 'I'm living with my parents at the moment' sounds more temporary than 'I live with my parents.'
options: No, the two mean the same. | No, 'live' sounds more temporary. | No, both sound permanent. | Yes, it sounds more temporary.
Key: {"kind": "mcq", "correct": "Yes, it sounds more temporary.", "wrong": ["No, the two mean the same.", "No, 'live' sounds more temporary.", "No, both sound permanent."]}
- reader 1: instruction: Three options start with 'No' and only one with 'Yes': the odd one out gives the answer away. 'No, live sounds more temporary' contradicts the statement and is not a believable choice.

## r21-4-003 · B1.2 · mcq · built-in

Task: Choose the correct option.
options: I sent the email yesterday. | I have sent the email yesterday. | I will send the email yesterday. | I was sending the email yesterday.
Key: {"kind": "mcq", "correct": "I sent the email yesterday.", "wrong": ["I have sent the email yesterday.", "I will send the email yesterday.", "I was sending the email yesterday."]}
- reader 1: a wrong option that fits: I was sending the email yesterday. (correct English, only less natural)
- reader 1: instruction: No context at all; 'was sending' is grammatical, so the task relies on 'simple past is the normal choice'.
- reader 2: a wrong option that fits: I was sending the email yesterday. (grammatical, only less natural without context)
- reader 2: instruction: No situation given; 'was sending' also fits.

## r21-4-004 · B1.1 · mcq · built-in

Task: Which sentence is an arrangement (fixed time and place in your diary)?
options: I'll probably see the dentist on Friday. | I'm seeing the dentist at 3 pm on Friday. | I saw the dentist at 3 pm on Friday. | I see the dentist every year in May.
Key: {"kind": "mcq", "correct": "I'm seeing the dentist at 3 pm on Friday.", "wrong": ["I'll probably see the dentist on Friday.", "I see the dentist every year in May.", "I saw the dentist at 3 pm on Friday."]}
- reader 1: instruction: The definition in brackets contains the key ('fixed time and place'): '3 pm on Friday' answers it.

## r21-4-006 · B1.2 · mcq · built-in

Task: You see a colleague with heavy boxes. Choose the correct option.
options: I'm carrying one of those for you. | I'll carry one of those for you. | I carried one of those for you. | I carry one of those for you.
Key: {"kind": "mcq", "correct": "I'll carry one of those for you.", "wrong": ["I carry one of those for you.", "I'm carrying one of those for you.", "I carried one of those for you."]}
- reader 1: sense: Wording 'carry one of those' is odd but fine.

## r21-4-007 · B1.1 · mcq · built-in

Task: You want to write a neutral email and not blame anyone. Choose the correct option.
options: I think you send the invoices on Fridays. | The invoices are sent on Fridays. | You send the invoices on Fridays. | The invoices are send on Fridays.
Key: {"kind": "mcq", "correct": "The invoices are sent on Fridays.", "wrong": ["You send the invoices on Fridays.", "The invoices are send on Fridays.", "I think you send the invoices on Fridays."]}
- reader 1: a wrong option that fits: 'You send the invoices on Fridays.' and 'I think you send the invoices on Fridays.' are correct English; only the situation (not blaming) excludes them. Passive hint given in the situation.
- reader 1: instruction: The situation is needed, but the neutral/no-blame idea is vague; option 1 is not clearly blaming.
- reader 2: a wrong option that fits: 'You send the invoices on Fridays.' and 'I think you send...' are correct English, only not neutral.
- reader 2: instruction: Learner may not know the passive is what is wanted; task never names it (ok), but 'neutral/not blame' is a style judgement, not grammar.

## r21-4-008 · B1.2 · mcq · built-in

Task: Which sentence means: the work is in progress now?
options: The road is being repaired. | The road is repaired every year. | The road was repaired. | The road will be repaired.
Key: {"kind": "mcq", "correct": "The road is being repaired.", "wrong": ["The road was repaired.", "The road is repaired every year.", "The road will be repaired."]}
- reader 1: sense: 'The road is repaired every year' etc. clearly wrong for 'now'; good.

## r21-4-011 · B1.1 · mcq · built-in

Task: Your friend keeps forgetting his password. Choose the correct option.
options: If you will forget it again, you'll be locked out. | If you forgot it again, you'll be locked out. | If you forget it again, you locked out. | If you forget it again, you'll be locked out.
Key: {"kind": "mcq", "correct": "If you forget it again, you'll be locked out.", "wrong": ["If you will forget it again, you'll be locked out.", "If you forgot it again, you'll be locked out.", "If you forget it again, you locked out."]}
- reader 1: sense: Option 3 ('you locked out') is a missing-word slip, easy to spot.
- reader 2: instruction: Situation sentence is not needed: only one option is correct without it.

## r21-4-012 · B1.1 · match · built-in

Task: Match each sentence with the relationship it expresses.
left: If you help me, I'll buy you lunch. | We won't start unless everyone is here. | I'll take water in case the shop is closed.
right: Everyone being present is necessary for us to start. | A promise depending on your help. | A precaution against a possible problem.
Key: {"kind": "match", "pairs": [["If you help me, I'll buy you lunch.", "A promise depending on your help."], ["We won't start unless everyone is here.", "Everyone being present is necessary for us to start."], ["I'll take water in case the shop is closed.", "A precaution against a possible problem."]]}
- reader 1: instruction: Right-hand items are in a different order from the left (good). 'Relationship' is a vague word.

## r21-4-013 · B1.1 · order · b1-cond-rep-1.csv:151

Task: Put the words in order.
word_cards: had | said | they | eaten | they | already
Key: {"kind": "order", "sentence": "they said they had already eaten", "also": []}
- reader 1: answer not accepted: ['they said they had already eaten']
- reader 1: another correct answer, not accepted: [['they said they had eaten already']]
- reader 1: instruction: Mixed-case/no capital; the two 'they' cards give the structure away somewhat.
- reader 2: answer not accepted: ['they said they had already eaten']
- reader 2: another correct answer, not accepted: [['they said they had eaten already']]

## r21-4-014 · B1.2 · order · b1-cond-rep-1.csv:155

Task: Put the words in order.
word_cards: said | i | i | didn't | that | know | the | answer
Key: {"kind": "order", "sentence": "i said that i didn't know the answer", "also": []}
- reader 1: answer not accepted: ["i said that i didn't know the answer"]
- reader 1: instruction: Sentence has no context; only one natural order. Fine.
- reader 2: answer not accepted: ["i said that i didn't know the answer"]

## r21-4-015 · B1.2 · gap · b1-cond-rep-1.csv:197

Task: I asked her ___ quiet.
word_cards: be | to be | being
Key: {"kind": "gap", "accepted": [["to be"]]}
- reader 1: level: Too easy/near A2 for B1.2.

## r21-4-016 · B1.2 · gap · b1-cond-rep-1.csv:200

Task: The teacher asked why we ___ late.
word_cards: were | did we | were we
Key: {"kind": "gap", "accepted": [["were"]]}
- reader 1: level: Too easy for B1.2 (A2-B1 indirect question word order); 'did we'/'were we' are clear distractors.

## r21-4-017 · B1.2 · match · b1-cond-rep-1.csv:212

Task: Match each request with its report.
left: 'Please sit down.' | 'Don't touch it!' | 'You should see a doctor.' | 'I'll help you.'
right: She warned me not to touch it. | She asked me to sit down. | She offered to help me. | She advised me to see a doctor.
Key: {"kind": "match", "pairs": [["'Please sit down.'", "She asked me to sit down."], ["'Don't touch it!'", "She warned me not to touch it."], ["'You should see a doctor.'", "She advised me to see a doctor."], ["'I'll help you.'", "She offered to help me."]]}
- reader 1: instruction: Instruction says 'request' but 'You should see a doctor' and 'I'll help you' are not requests.
- reader 1: level: Reporting verbs are easily matched by the verb stem alone; easy for B1.2.

## r21-4-018 · B1.2 · order · b1-new-1.csv:9

Task: Put the words in order.
word_cards: the | cold | me | get | long | took | time | it | a | weather | to | to | used
Key: {"kind": "order", "sentence": "it took me a long time to get used to the cold weather", "also": []}
- reader 1: answer not accepted: ['it took me a long time to get used to the cold weather']
- reader 1: instruction: 'used to' vs 'get used to' is not helped; fine. 13 cards, quite long to arrange but fine.
- reader 2: another correct answer, not accepted: ['to get used to the cold weather took me a long time (grammatical, unnatural)']
- the readers disagree

## r21-4-019 · B1.2 · order · b1-new-1.csv:10

Task: Put all the words in order. More than one answer is possible.
word_cards: used | i | am | getting | so | up | to | early | not
Key: {"kind": "order", "sentence": "i am not used to getting up so early", "also": ["i am used to not getting up so early"]}
- reader 1: answer not accepted: ['i am not used to getting up so early']
- reader 1: another correct answer, not accepted: [['i am not so used to getting up early'], ['i am so not used to getting up early']]
- reader 1: instruction: Says 'more than one answer is possible' but the main alternatives are marginal or colloquial.
- reader 2: another correct answer, not accepted: [['i am not so used to getting up early'], ['i am so not used to getting up early (informal)']]
- the readers disagree

## r21-4-020 · B1.1 · order · b1-new-2.csv:44

Task: Put the words in order.
word_cards: calls | doctor | your | here | wait | until | the | name
Key: {"kind": "order", "sentence": "wait here until the doctor calls your name", "also": ["until the doctor calls your name wait here"]}
- reader 1: answer not accepted: ['wait here until the doctor calls your name']
- reader 1: another correct answer, not accepted: [['until the doctor calls your name wait here'], ['wait until the doctor calls your name here']]
- reader 1: instruction: Imperative without capital/punctuation; 'your name' and 'doctor' ok.
- reader 2: another correct answer, not accepted: ['wait until the doctor calls your name here (grammatical, different meaning, less natural)']
- the readers disagree

## r21-4-022 · B1.1 · gap · b1-new-3.csv:114

Task: She refused ___ the contract.
word_cards: signing | to sign | sign
Key: {"kind": "gap", "accepted": [["to sign"]]}
- reader 1: level: Easy for B1.1 but acceptable.

## r21-4-023 · B1.1 · match · b1-new-4.csv:213

Task: Match each description with the right word.
left: It makes me feel bored. | I feel bored. | It makes me feel tired. | I feel tired.
right: tiring | tired | bored | boring
Key: {"kind": "match", "pairs": [["It makes me feel bored.", "boring"], ["I feel bored.", "bored"], ["It makes me feel tired.", "tiring"], ["I feel tired.", "tired"]]}
- reader 1: level: A2 vocabulary and -ed/-ing; easy for B1.1.
- reader 2: level: Very easy for B1.1 (A2 level vocabulary, one rule, 4 near-identical pairs).

## r21-4-024 · B1.1 · gap · b1-new-5.csv:145

Task: Nothing ___ changed since last year.
word_cards: hasn't | has | have | isn't
Key: {"kind": "gap", "accepted": [["has"]]}
- reader 1: a wrong option that fits: 'hasn't' is wrong (double negative: Nothing hasn't changed), though a learner might think of it.

## r21-4-025 · B1.1 · gap · b1-passives-1.csv:15

Task: The shop ___ by two sisters, and the products ___ locally.
word_cards: runs | are made | is run | make
Key: {"kind": "gap", "accepted": [["is run"], ["are made"]]}
- reader 1: sense: 'is run by two sisters' fine; 'products' plural ok.

## r21-4-028 · B1.1 · order · b1-passives-1.csv:40

Task: Put the words in order.
word_cards: still | bridge | built | and | today | is | was | the | used | in | 1932 | it
Key: {"kind": "order", "sentence": "the bridge was built in 1932 and it is still used today", "also": []}
- reader 1: answer not accepted: ['the bridge was built in 1932 and it is still used today']
- reader 1: another correct answer, not accepted: [['the bridge was built in 1932 and today it is still used'], ['in 1932 the bridge was built and it is still used today'], ['the bridge is still used today and it was built in 1932'], ['it was built in 1932 and the bridge is still used today']]
- reader 1: instruction: Several orders possible but the instruction does not say so.
- reader 2: another correct answer, not accepted: ['the bridge was built in 1932 and today it is still used', 'in 1932 the bridge was built and it is still used today', 'the bridge is still used today and it was built in 1932', "it was built in 1932 and the bridge is still used today (odd, 'it' before noun)"]
- reader 2: instruction: Many valid orders for 12 cards; no 'more than one answer' note.
- the readers disagree

## r21-4-029 · B1.1 · text · b1-passives-1.csv:63

Task: Start with *My laptop*: Someone stole my laptop yesterday.
Key: {"kind": "text", "accepted": [["My laptop was stolen yesterday.", "My laptop was stolen by someone yesterday.", "Yesterday my laptop was stolen.", "Yesterday my laptop was stolen by someone."]]}
- reader 1: another correct answer, not accepted: [['My laptop got stolen yesterday.']]
- reader 1: instruction: No instruction to rewrite or to use the passive; the learner must guess the task.
- reader 2: another correct answer, not accepted: ['my laptop got stolen yesterday']
- reader 2: instruction: Does not say to rewrite the sentence with the same meaning; 'Start with' alone is unclear (the passive is not named).

## r21-4-030 · B1.1 · order · b1-tenses-1.csv:3

Task: Put the words in order.
word_cards: out | home | cook | she | rarely | to | at | she | because | prefers | eats
Key: {"kind": "order", "sentence": "she rarely eats out because she prefers to cook at home", "also": ["because she prefers to cook at home she rarely eats out"]}
- reader 1: answer not accepted: ['she rarely eats out because she prefers to cook at home']
- reader 1: another correct answer, not accepted: [['she prefers to cook at home because she rarely eats out'], ['because she prefers to cook at home she rarely eats out']]
- reader 1: instruction: Several orders are possible but the instruction does not say so.
- reader 2: another correct answer, not accepted: ['she eats out rarely because she prefers to cook at home', 'she prefers to cook at home because she rarely eats out (grammatical, reversed cause)']
- reader 2: instruction: Several valid orders but no 'more than one answer' note.
- the readers disagree

## r21-4-031 · B1.1 · order · b1-tenses-1.csv:4

Task: Put the words in order.
word_cards: must | past | hurry | seven | half | at | train | our | leaves | so | we
Key: {"kind": "order", "sentence": "our train leaves at half past seven so we must hurry", "also": []}
- reader 1: answer not accepted: ['our train leaves at half past seven so we must hurry']
- reader 1: sense: 'we must hurry so our train leaves...' is grammatical but illogical; fine as a distractor but learners may see both.
- reader 2: another correct answer, not accepted: ['so we must hurry our train leaves at half past seven (illogical)']
- the readers disagree

## r21-4-032 · B1.1 · order · b1-tenses-1.csv:5

Task: Put the words in order.
word_cards: work | your | for | same | brother | does | company | still | the
Key: {"kind": "order", "sentence": "does your brother still work for the same company", "also": []}
- reader 1: answer not accepted: ['does your brother still work for the same company']
- reader 1: another correct answer, not accepted: [['does your brother work for the same company still']]
- reader 2: another correct answer, not accepted: ['does your brother work for the same company still (less natural)']
- the readers disagree

## r21-4-033 · B1.1 · order · b1-tenses-1.csv:7

Task: Put the words in order.
word_cards: station | he | near | the | teaches | school | maths | at | a
Key: {"kind": "order", "sentence": "he teaches maths at a school near the station", "also": []}
- reader 1: answer not accepted: ['he teaches maths at a school near the station']
- reader 1: another correct answer, not accepted: [['at a school near the station he teaches maths']]
- reader 2: another correct answer, not accepted: ['at a school near the station he teaches maths', 'he teaches maths at the school near a station (odd)']
- reader 2: instruction: Several valid orders, no 'more than one answer' note.
- the readers disagree

## r21-4-034 · B1.1 · gap · b1-tenses-1.csv:12

Task: My sister ___ in a hospital, but she ___ to move to the countryside.
word_cards: is wanting | wants | works
Key: {"kind": "gap", "accepted": [["works"], ["wants"]]}
- reader 1: level: Easy for B1.1 (A2 simple present).

## r21-4-035 · B1.1 · gap · b1-tenses-1.csv:13

Task: The lesson ___ at 9.30, so we ___ to be there early.
word_cards: started | starts | are needing | need
Key: {"kind": "gap", "accepted": [["starts"], ["need"]]}
- reader 1: instruction: 'started ... need' is grammatical, only the logic of the timetable makes it wrong.
- reader 2: a wrong option that fits: 'started' fits grammatically but is illogical with 'need'.

## r21-4-036 · B1.1 · gap · b1-tenses-1.csv:18

Task: I ___ understand why she ___ always late.
word_cards: does | is | am | don't
Key: {"kind": "gap", "accepted": [["don't"], ["is"]]}
- reader 1: level: Easy for B1.1.
- reader 1: sense: 'is always late' (annoyance) fine; cards 'does'/'am' are random distractors.

## r21-4-037 · B1.1 · gap · b1-tenses-1.csv:23

Task: She ___ meat because she is a vegetarian. (not / eat)
Key: {"kind": "gap", "accepted": [["doesn't eat", "does not eat"]]}
- reader 1: level: A1-A2 level; too easy for B1.1.
- reader 2: another correct answer, not accepted: [["isn't eating"]]
- reader 2: level: A2 level (basic present simple negative); too easy for B1.1.

## r21-4-038 · B1.1 · gap · b1-tenses-1.csv:24

Task: How much ___ a ticket to the capital ___ ? (cost)
Key: {"kind": "gap", "accepted": [["does"], ["cost"]]}
- reader 1: another correct answer, not accepted: [['did', 'cost'], ['will', 'cost'], ['would', 'cost']]
- reader 1: instruction: Past/future questions are also correct; no time context given.
- reader 2: another correct answer, not accepted: [['did', 'cost'], ['will', 'cost']]
- reader 2: instruction: No time context: past and future also fit.
- reader 2: level: A2 level, too easy for B1.1.

## r21-4-039 · B1.1 · text · b1-tenses-1.csv:25

Task: Make it negative: My colleagues work from home on Fridays.
Key: {"kind": "text", "accepted": [["My colleagues don't work from home on Fridays.", "My colleagues do not work from home on Fridays.", "On fridays my colleagues don't work from home.", "On fridays my colleagues do not work from home."]]}
- reader 1: level: A2 level; too easy for B1.1.
- reader 2: level: A2 level, too easy for B1.1.

## r21-4-040 · B1.1 · gap · b1-tenses-1.csv:57

Task: Why ___ you ___ so quietly today? Is something wrong?
word_cards: spoke | speaking | are | did
Key: {"kind": "gap", "accepted": [["are"], ["speaking"]]}
- reader 1: sense: 'did ... speak' would fit but the card 'speak' is not given; fine.

## r21-4-041 · B1.1 · gap · b1-tenses-1.csv:58

Task: Anna ___ for a new flat because her rent is too high.
word_cards: looks | is looking | was looking
Key: {"kind": "gap", "accepted": [["is looking"]]}
- reader 1: a wrong option that fits: 'was looking' is correct English with no time context (past); 'looks' is grammatical but odd/less natural.
- reader 1: instruction: No time marker; 'is looking' vs 'was looking' depends on context only.
- reader 1: level: A2 present continuous vs simple.
- reader 2: a wrong option that fits: 'looks' is grammatical but less natural; 'was looking' does not fit 'is too high'.

## r21-4-042 · B1.1 · gap · b1-tenses-1.csv:60

Task: My neighbour ___ his house this month, so there is a lot of noise. (paint)
Key: {"kind": "gap", "accepted": [["is painting", "has been painting"]]}
- reader 1: another correct answer, not accepted: [['is going to paint']]
- reader 2: another correct answer, not accepted: [["'s painting"]]

## r21-4-043 · B1.1 · order · b1-tenses-1.csv:80

Task: Put all the words in order. More than one answer is possible.
word_cards: we | last | taxi | train | missed | the | we | a | so | home | took
Key: {"kind": "order", "sentence": "we missed the last train so we took a taxi home", "also": ["we missed the last train home so we took a taxi"]}
- reader 1: answer not accepted: ['we missed the last train so we took a taxi home']
- reader 1: instruction: Says more than one answer is possible, but I find only one sensible order ('we took a taxi home so we missed the last train' is illogical).
- reader 2: another correct answer, not accepted: ['we took a taxi home so we missed the last train (illogical)']
- reader 2: instruction: 'More than one answer is possible' hint: only an illogical alternative exists.
- the readers disagree

## r21-4-044 · B1.1 · order · b1-tenses-1.csv:81

Task: Put the words in order.
word_cards: twice | it | she | letter | opened | before | she | and | read | the | answered
Key: {"kind": "order", "sentence": "she opened the letter and read it twice before she answered", "also": ["before she answered she opened the letter and read it twice"]}
- reader 1: answer not accepted: ['she opened the letter and read it twice before she answered']
- reader 1: another correct answer, not accepted: [['she opened and read the letter twice before she answered it']]
- reader 1: instruction: Two orders are possible; the instruction does not say so.
- reader 2: another correct answer, not accepted: ['she opened it and read the letter twice before she answered', 'she opened the letter and read it before she answered twice (different meaning)']
- reader 2: instruction: Several valid orders, no 'more than one answer' note.
- reader 2: sense: 'answered' without an object ('answered it') is slightly odd.
- the readers disagree

## r21-4-046 · B1.1 · gap · b1-tenses-2.csv:12

Task: She ___ here since 2018, but she ___ to move next year.
word_cards: has worked | is working | works | plans
Key: {"kind": "gap", "accepted": [["has worked"], ["plans"]]}
- reader 1: sense: 'plans to move next year' fine.

## r21-4-047 · B1.1 · gap · b1-tenses-2.csv:13

Task: We ___ for an hour, and the bus still ___ .
word_cards: are waiting | wasn't coming | have waited | hasn't come
Key: {"kind": "gap", "accepted": [["have waited"], ["hasn't come"]]}
- reader 1: a wrong option that fits: 'are waiting' is wrong with 'for an hour' (needs have been waiting); 'wasn't coming' is wrong with 'still'.
- reader 1: sense: 'have waited for an hour' is correct but 'have been waiting' would be more natural.

## r21-4-048 · B1.1 · gap · b1-tenses-2.csv:45

Task: How long ___ they ___ for the results?
word_cards: been waiting | are | did | have
Key: {"kind": "gap", "accepted": [["have"], ["been waiting"]]}
- reader 1: instruction: Two gaps with 'been waiting' as a single card; 'are/did' distractors easy.

## r21-4-050 · B1.1 · gap · b1-upgrades-1.csv:4

Task: My cousin ___ in a bank, but at the weekend he ___ as a volunteer at the zoo. (work / help)
Key: {"kind": "gap", "accepted": [["works"], ["helps"]]}
- reader 1: another correct answer, not accepted: [['is working', 'helps']]
- reader 1: instruction: 'is working' is not impossible without time context.
- reader 2: another correct answer, not accepted: [['is working', 'helps'], ['works', 'is helping'], ['worked', 'helped']]
- reader 2: instruction: No time context: past tense also fits; continuous variants are possible but less natural.

## r21-4-051 · B1.2 · text · b1-upgrades-1.csv:38

Task: Start with *The road*: They are repairing the road.
Key: {"kind": "text", "accepted": [["The road is being repaired."]]}
- reader 1: another correct answer, not accepted: [["The road's being repaired."], ['The road is being repaired by them.']]
- reader 1: instruction: No instruction: the task does not say 'rewrite in the passive'.
- reader 2: another correct answer, not accepted: ['the road is being repaired by them']
- reader 2: instruction: Does not say to rewrite with the same meaning; the passive is not named.

## r21-4-052 · B1.1 · gap · compare-past-1.csv:13

Task: Kate ___ TV a lot when she was ill last year. (watch)
Key: {"kind": "gap", "accepted": [["watched", "was watching"]]}
- reader 1: another correct answer, not accepted: [['would watch']]

## r21-4-053 · B1.1 · gap · compare-past-1.csv:24

Task: I ___ here since 2010. I still work here. (work)
Key: {"kind": "gap", "accepted": [["have worked", "have been working"]]}
- reader 1: level: Easy for B1.1; the second sentence gives the tense away.

## r21-4-055 · B1.1 · mcq · compare-past-1.csv:34

Task: Choose the correct option: I didn't recognise her. She ___ a lot.
options: had changed | has changed | had change
Key: {"kind": "mcq", "correct": "had changed", "wrong": ["has changed", "had change"]}
- reader 1: a wrong option that fits: 'has changed' is wrong in the past context.
- reader 2: a wrong option that fits: 'has changed' is also correct (present result, acceptable in speech).

## r21-4-056 · B1.2 · order · comparison-1.csv:47

Task: Put the words in order.
word_cards: busy | was | last | as | as | year | not | this | year
Key: {"kind": "order", "sentence": "this year was not as busy as last year", "also": ["last year was not as busy as this year"]}
- reader 1: answer not accepted: ['this year was not as busy as last year']
- reader 1: another correct answer, not accepted: [['last year was not as busy as this year']]
- reader 1: instruction: Two opposite-meaning sentences are correct; the instruction does not say so.
- reader 2: another correct answer, not accepted: ['last year was not as busy as this year (opposite meaning, also correct)']
- reader 2: instruction: Two valid answers with opposite meanings; nothing in the task fixes which.
- the readers disagree

## r21-4-057 · B1.1 · gap · comparison-1.csv:51

Task: The new model is much ___ than the old one. (reliable)
word_cards: most reliable | more reliable | reliable
Key: {"kind": "gap", "accepted": [["more reliable"]]}
- reader 1: level: A2 comparative; too easy for B1.1.
- reader 2: level: Easy for B1.1 (one cue, basic comparative).

## r21-4-058 · B1.2 · match · comparison-1.csv:52

Task: Match each comparison with its meaning.
left: twice as expensive as | not as big as | slightly cheaper than | by far the best
right: smaller | costs double | much better than all the others | a little less money
Key: {"kind": "match", "pairs": [["twice as expensive as", "costs double"], ["not as big as", "smaller"], ["slightly cheaper than", "a little less money"], ["by far the best", "much better than all the others"]]}
- reader 1: sense: 'slightly cheaper than' and 'a little less money' are near paraphrases.

## r21-4-060 · B1.1 · mcq · modal-verbs-1.csv:34

Task: Choose the correct question: ___ speak English at work?
options: Have you to | Are you have to | Do you have to | Must you to
Key: {"kind": "mcq", "correct": "Do you have to", "wrong": ["Have you to", "Must you to", "Are you have to"]}
- reader 1: level: A2-B1 level; easy.
- reader 2: a wrong option that fits: 'Have you to' is old-fashioned British, rare but grammatical.

