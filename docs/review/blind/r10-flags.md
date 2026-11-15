# Blind check r10: flags for the judge

101 tasks, 2 readers.

## r10-001 · B1.1 · mcq · zz-blind-gap-points-b11-1.csv:2

Task: Choose the correct option: My train gets in at six. ___, I'll call you from the station.
options: If I arrive | When I will arrive | If I will arrive | When I arrive
Key: {"kind": "mcq", "correct": "When I arrive", "wrong": ["If I arrive", "When I will arrive", "If I will arrive"]}
- reader 1: a wrong option that fits: If I arrive: correct English but illogical, the arrival is timetabled (weak).
- reader 2: a wrong option that fits: If I arrive (grammatical, but odd because the train certainly arrives at six)

## r10-003 · B1.1 · mcq · zz-blind-gap-points-b11-1.csv:4

Task: Which sentence is correct?
options: The film ends at nine, so I'll call you when it finishes. | The film ends at nine, so I'll call you if it finishes. | The film ends at nine, so I'll call you when it will finish. | The film ends at nine, so I'll call you if it will finish.
Key: {"kind": "mcq", "correct": "The film ends at nine, so I'll call you when it finishes.", "wrong": ["The film ends at nine, so I'll call you if it finishes.", "The film ends at nine, so I'll call you when it will finish.", "The film ends at nine, so I'll call you if it will finish."]}
- reader 1: a wrong option that fits: 'if it finishes' is grammatical but odd/illogical (the film ends at nine) (weak).
- reader 2: a wrong option that fits: 'if it finishes' is grammatical but odd: the film certainly finishes

## r10-004 · B1.1 · mcq · zz-blind-gap-points-b11-1.csv:5

Task: Choose the correct option: My brother might visit us next month. ___, we'll take him to the new museum.
options: When he comes | If he comes | When he will come | If he will come
Key: {"kind": "mcq", "correct": "If he comes", "wrong": ["When he comes", "If he will come", "When he will come"]}
- reader 1: a wrong option that fits: 'When he comes' is grammatical but contradicts 'might visit' (weak).

## r10-006 · B1.1 · mcq · zz-blind-gap-points-b11-1.csv:7

Task: Choose the correct option: We're getting married in June. ___ married, we'll look for a bigger flat.
options: When we'll be | When we're | If we'll be | If we're
Key: {"kind": "mcq", "correct": "When we're", "wrong": ["If we're", "When we'll be", "If we'll be"]}
- reader 1: a wrong option that fits: 'If we're' is grammatical but illogical as the wedding is fixed (weak).
- reader 2: a wrong option that fits: If we're (grammatical, but odd because the wedding is certain)

## r10-007 · B1.1 · mcq · zz-blind-gap-points-b11-1.csv:8

Task: Choose the correct option: ___ my visa in time, I'll fly to Toronto in May. It's not certain yet.
options: When I'll get | If I get | When I get | If I'll get
Key: {"kind": "mcq", "correct": "If I get", "wrong": ["When I get", "If I'll get", "When I'll get"]}
- reader 1: instruction: 'It's not certain yet' is needed, but then 'When I get' is the only wrong-ish fit; fine.

## r10-008 · B1.1 · gap · zz-blind-gap-points-b11-1.csv:9

Task: Write *if* or *when*: I'm having lunch with Tom today. ___ I see him, I'll give him your book.
Key: {"kind": "gap", "accepted": [["When"]]}
- reader 1: another correct answer, not accepted: [['If']]
- reader 1: instruction: 'If' is grammatical but odd: lunch is arranged, so the meeting is certain (weak).
- reader 2: another correct answer, not accepted: [['if']]
- reader 2: instruction: 'if' is grammatical but less natural (lunch is planned); a learner may type it

## r10-010 · B1.1 · gap · zz-blind-gap-points-b11-1.csv:11

Task: Write *if* or *when*: The bank might be closed on Saturday. ___ it is, I'll go on Monday.
Key: {"kind": "gap", "accepted": [["If"]]}
- reader 1: level: 'When' is grammatical but contradicts 'might be closed'.

## r10-011 · B1.1 · gap · zz-blind-gap-points-b11-1.csv:12

Task: My course starts on Monday. When it ___, I'll have less free time. (start)
Key: {"kind": "gap", "accepted": [["starts", "has started", "'s started"]]}
- reader 1: another correct answer, not accepted: [['begins']]

## r10-012 · B1.1 · gap · zz-blind-gap-points-b11-1.csv:13

Task: Write *if* or *when*: The museum opens at ten. ___ it opens, we'll buy tickets for the tower.
Key: {"kind": "gap", "accepted": [["When"]]}
- reader 1: another correct answer, not accepted: [['If']]
- reader 1: instruction: 'If' is grammatical but odd: the opening time is fixed (weak).
- reader 2: another correct answer, not accepted: [['if']]
- reader 2: instruction: 'if' is grammatical but less natural (the museum certainly opens)

## r10-013 · B1.1 · text · zz-blind-gap-points-b11-1.csv:14

Task: Join with *if* or *when*: My contract ends in June. Then I'll take a long holiday.
Key: {"kind": "text", "accepted": [["When my contract ends in June, I'll take a long holiday.", "When my contract ends in June, I will take a long holiday.", "When my contract ends, I'll take a long holiday.", "When my contract ends, I will take a long holiday.", "I'll take a long holiday when my contract ends in June.", "I will take a long holiday when my contract ends in June.", "I'll take a long holiday when my contract ends.", "I will take a long holiday when my contract ends.", "In June, when my contract ends, I'll take a long holiday.", "In June, when my contract ends, I will take a long holiday.", "I'll take a long holiday in June, when my contract ends.", "I will take a long holiday in June, when my contract ends.", "When my contract has ended, I'll take a long holiday.", "When my contract has ended, I will take a long holiday.", "I'll take a long holiday when my contract has ended.", "I will take a long holiday when my contract has ended."]]}
- reader 1: another correct answer, not accepted: ["When my contract has ended in June, I'll take a long holiday."]
- reader 1: instruction: 'with if or when' leaves a choice; only when fits (fine, but 'in June' is certain so the choice is easy).

## r10-014 · B1.1 · text · zz-blind-gap-points-b11-1.csv:15

Task: Join with *if* or *when*: Perhaps the hotel is full. In that case, we'll stay with friends.
Key: {"kind": "text", "accepted": [["If the hotel is full, we'll stay with friends.", "If the hotel is full, we will stay with friends.", "If the hotel's full, we'll stay with friends.", "If the hotel's full, we will stay with friends.", "We'll stay with friends if the hotel is full.", "We will stay with friends if the hotel is full.", "We'll stay with friends if the hotel's full.", "We will stay with friends if the hotel's full.", "If the hotel is full, then we'll stay with friends.", "If the hotel is full, we'll stay with friends instead.", "We'll stay with friends instead if the hotel is full.", "we'll stay with friends if the hotel is full.", "we will stay with friends if the hotel is full.", "we'll stay with friends if the hotel's full.", "we will stay with friends if the hotel's full.", "then we'll stay with friends if the hotel is full.", "we'll stay with friends instead if the hotel is full."]]}
- reader 1: instruction: 'Perhaps' and 'In that case' are the trigger; fine.

## r10-016 · B1.1 · order · zz-blind-gap-points-b11-1.csv:17

Task: Put the words in order to make a question.
word_cards: you | will | what | do | finish | you | when | degree | your
Key: {"kind": "order", "sentence": "what will you do when you finish your degree", "also": ["when you finish your degree what will you do"]}
- reader 2: a wrong option that fits: Second order also correct: 'When you finish your degree, what will you do?'

## r10-017 · B1.1 · order · zz-blind-gap-points-b11-1.csv:18

Task: Put the words in order to make a question.
word_cards: lands | your | rome | when | in | plane | will | me | you | text
Key: {"kind": "order", "sentence": "will you text me when your plane lands in rome", "also": ["when your plane lands in rome will you text me"]}
- reader 1: another correct answer, not accepted: ['will you text me in rome when your plane lands', 'when your plane lands, will you text me in rome']

## r10-018 · B1.1 · order · zz-blind-gap-points-b11-1.csv:19

Task: Put the words in order.
word_cards: the | gym | finishes | early | meeting | i'll | go | the | to | if
Key: {"kind": "order", "sentence": "if the meeting finishes early i'll go to the gym", "also": ["i'll go to the gym if the meeting finishes early"]}
- reader 1: another correct answer, not accepted: ["i'll go to the meeting if the gym finishes early (odd meaning, grammatical)"]
- reader 1: sense: Card 'i'll' lower case/apostrophe fine.

## r10-020 · B1.1 · order · zz-blind-gap-points-b11-1.csv:21

Task: Put the words in order.
word_cards: to | retire | will | when | they | coast | the | parents | move | my
Key: {"kind": "order", "sentence": "my parents will move to the coast when they retire", "also": ["when they retire my parents will move to the coast", "when my parents retire they will move to the coast"]}
- reader 2: another correct answer, not accepted: ['they will move to the coast when my parents retire']

## r10-021 · B1.1 · gap · zz-blind-gap-points-b11-1.csv:22

Task: My new laptop arrives on Friday. ___ it ___, I'll set it up for you.
word_cards: When | will arrive | If | arrives
Key: {"kind": "gap", "accepted": [["When"], ["arrives"]]}
- reader 1: a wrong option that fits: 'If ... arrives' is grammatical but illogical (arrival on Friday is fixed) (weak); 'will arrive' fits no gap correctly.
- reader 2: instruction: 'If' is grammatical but less natural (arrival on Friday is certain)

## r10-022 · B1.1 · gap · zz-blind-gap-points-b11-1.csv:23

Task: I might not finish the report today. ___ I ___ it, I'll send it to you tonight.
word_cards: will finish | finish | When | If
Key: {"kind": "gap", "accepted": [["If"], ["finish"]]}
- reader 1: a wrong option that fits: 'When ... finish' is grammatical but contradicts 'might not finish' (weak).

## r10-023 · B1.1 · gap · zz-blind-gap-points-b11-1.csv:24

Task: We're moving to Riga in March. ___ there, we'll see each other more often.
word_cards: When we'll be | When we're | If we're
Key: {"kind": "gap", "accepted": [["When we're"]]}
- reader 1: a wrong option that fits: 'If we're' is correct English but illogical: the move is fixed (weak).
- reader 2: a wrong option that fits: 'If we're' is grammatical but odd (the move is certain)
- reader 2: instruction: Task is one gap; 'If we're' is odd rather than wrong

## r10-024 · B1.1 · gap · zz-blind-gap-points-b11-1.csv:25

Task: I might get tickets for the concert. ___ I ___ them, I'll take you with me.
word_cards: get | If | will get | When
Key: {"kind": "gap", "accepted": [["If"], ["get"]]}
- reader 1: a wrong option that fits: 'When ... get' is grammatical but contradicts 'might get' (weak).

## r10-025 · B1.1 · match · zz-blind-gap-points-b11-1.csv:26

Task: Match each sentence with the one that follows it.
left: My flight lands at six. | My flight might be late. | I'm not sure the hotel has parking. | Our room will be ready at two.
right: When it is, we'll take our bags up. | If it doesn't, we'll park at the station. | When it does, I'll text you. | If it is, I'll take a taxi.
Key: {"kind": "match", "pairs": [["My flight lands at six.", "When it does, I'll text you."], ["My flight might be late.", "If it is, I'll take a taxi."], ["I'm not sure the hotel has parking.", "If it doesn't, we'll park at the station."], ["Our room will be ready at two.", "When it is, we'll take our bags up."]]}
- reader 1: sense: Item 2 'If it is, I'll take a taxi' is slightly odd (taxi to where?) but fits.

## r10-026 · B1.1 · mcq · zz-blind-gap-points-b11-1.csv:27

Task: Choose the correct option: My laptop is eight years old, but it continues ___ without any problems.
options: to working | work | to work
Key: {"kind": "mcq", "correct": "to work", "wrong": ["work", "to working"]}
- reader 1: level: 'work' fits no..: fine. Note 'continues working' (correct) is not offered; fine.

## r10-033 · B1.1 · gap · zz-blind-gap-points-b11-1.csv:34

Task: The audience began ___ before the actor finished his joke. (laugh)
Key: {"kind": "gap", "accepted": [["laughing", "to laugh"]]}
- reader 1: instruction: Two answers possible (to laugh / laughing); the task does not limit it.

## r10-034 · B1.1 · gap · zz-blind-gap-points-b11-1.csv:35

Task: My partner loves ___ new recipes, so we often have friends over at the weekend. (try)
Key: {"kind": "gap", "accepted": [["trying", "to try"]]}
- reader 1: instruction: Two answers possible (trying / to try).

## r10-035 · B1.1 · gap · zz-blind-gap-points-b11-1.csv:36

Task: Do you prefer ___ on holiday alone or with friends? (go)
Key: {"kind": "gap", "accepted": [["going", "to go"]]}
- reader 1: instruction: Two answers possible (going / to go).

## r10-036 · B1.1 · gap · zz-blind-gap-points-b11-1.csv:37

Task: Many people continued ___ from home after the offices reopened. (work)
Key: {"kind": "gap", "accepted": [["working", "to work"]]}
- reader 1: instruction: Two answers possible (to work / working).

## r10-037 · B1.1 · gap · zz-blind-gap-points-b11-1.csv:38

Task: I hate ___ on the phone, so I usually send a text message instead. (talk)
Key: {"kind": "gap", "accepted": [["talking", "to talk"]]}
- reader 1: instruction: Two answers possible (talking / to talk).

## r10-038 · B1.1 · text · zz-blind-gap-points-b11-1.csv:39

Task: Say it another way with *to*: We started looking for a new flat as soon as I got the job.
Key: {"kind": "text", "accepted": [["We started to look for a new flat as soon as I got the job.", "As soon as I got the job, we started to look for a new flat.", "we started to look for a new flat as soon as I got the job."]]}
- reader 1: another correct answer, not accepted: ['We began to look for a new flat as soon as I got the job.']
- reader 1: instruction: 'with to' is slightly vague (change what?) but workable.

## r10-040 · B1.1 · text · zz-blind-gap-points-b11-1.csv:41

Task: Correct the mistake: Would you like coming with us to the team lunch on Friday?
Key: {"kind": "text", "accepted": [["Would you like to come with us to the team lunch on Friday?"]]}
- reader 1: another correct answer, not accepted: ['Would you like to join us for the team lunch on Friday?']

## r10-041 · B1.1 · order · zz-blind-gap-points-b11-1.csv:42

Task: Put the words in order.
word_cards: her | year | she | to | write | last | travels | about | blog | began | a
Key: {"kind": "order", "sentence": "she began to write a blog about her travels last year", "also": ["last year she began to write a blog about her travels"]}
- reader 1: another correct answer, not accepted: ['she began to write a blog last year about her travels', 'last year she began a blog to write about her travels (odd)']

## r10-042 · B1.1 · order · zz-blind-gap-points-b11-1.csv:43

Task: Put the words in order to make a question.
word_cards: before | coffee | would | a | have | meeting | like | you | the | to
Key: {"kind": "order", "sentence": "would you like to have a coffee before the meeting", "also": []}
- reader 1: another correct answer, not accepted: ['before the meeting, would you like to have a coffee']
- reader 2: another correct answer, not accepted: ['before the meeting, would you like to have a coffee']

## r10-044 · B1.1 · order · zz-blind-gap-points-b11-1.csv:45

Task: Put the words in order.
word_cards: first | she | after | child | continued | hospital | working | was | the | born | at | her
Key: {"kind": "order", "sentence": "she continued working at the hospital after her first child was born", "also": ["after her first child was born she continued working at the hospital"]}
- reader 1: another correct answer, not accepted: ['she continued working after her first child was born at the hospital', 'after her first child was born at the hospital she continued working']

## r10-046 · B1.1 · gap · zz-blind-gap-points-b11-1.csv:47

Task: During the long winter my brother started ___ his own furniture, and now he sells it online.
word_cards: to making | make | making
Key: {"kind": "gap", "accepted": [["making"]]}
- reader 1: a wrong option that fits: 'to making' and 'make' are wrong; correct 'to make' is not offered (fine).

## r10-056 · B1.1 · mcq · zz-blind-gap-points-b11-1.csv:57

Task: Choose the correct option: 'How many tickets are left for tonight's concert?' '___. They're all sold out.'
options: None | No one | Any | No
Key: {"kind": "mcq", "correct": "None", "wrong": ["No", "Any", "No one"]}
- reader 1: sense: 'No' alone is wrong for 'How many'; fine.

## r10-062 · B1.1 · gap · zz-blind-gap-points-b11-1.csv:63

Task: Complete with one word: There ___ any direct flights, so we had to change planes in Frankfurt.
Key: {"kind": "gap", "accepted": [["weren't", "aren't"]]}
- reader 1: instruction: 'Complete with one word' does not fix the tense; 'aren't' is arguably fine, and 'were not' is two words.
- reader 2: another correct answer, not accepted: [["wasn't"]]
- reader 2: instruction: Does not say the sentence is negative; 'aren't' (present) is also possible, 'were not' is two words, 'wasn't' is non-standard with plural 'flights'

## r10-063 · B1.1 · text · zz-blind-gap-points-b11-1.csv:64

Task: Say it another way with *no*: There aren't any vegetarian dishes on the menu.
Key: {"kind": "text", "accepted": [["There are no vegetarian dishes on the menu.", "On the menu there are no vegetarian dishes."]]}
- reader 1: another correct answer, not accepted: ['The menu has no vegetarian dishes.', 'The menu has no vegetarian options.', 'There are no vegetarian options on the menu.']
- reader 2: another correct answer, not accepted: ["There's no vegetarian dish on the menu.", 'The menu has no vegetarian dishes.', 'No vegetarian dishes are on the menu.']

## r10-064 · B1.1 · text · zz-blind-gap-points-b11-1.csv:65

Task: Say it another way with *any*: I've got no plans for the weekend.
Key: {"kind": "text", "accepted": [["I haven't got any plans for the weekend.", "I don't have any plans for the weekend.", "I've not got any plans for the weekend.", "I haven't any plans for the weekend."]]}
- reader 1: another correct answer, not accepted: ["I haven't got any plans at the weekend."]

## r10-066 · B1.1 · order · zz-blind-gap-points-b11-1.csv:67

Task: Put the words in order.
word_cards: to | have | for | time | test | revise | any | didn't | the | i
Key: {"kind": "order", "sentence": "i didn't have any time to revise for the test", "also": []}
- reader 1: another correct answer, not accepted: ["for the test i didn't have any time to revise"]

## r10-067 · B1.1 · order · zz-blind-gap-points-b11-1.csv:68

Task: Put the words in order.
word_cards: my | that | was | meeting | colleagues | knew | cancelled | the | none | of
Key: {"kind": "order", "sentence": "none of my colleagues knew that the meeting was cancelled", "also": []}
- reader 1: another correct answer, not accepted: ['none of my colleagues knew the meeting that was cancelled (grammatical, odd)']

## r10-069 · B1.1 · order · zz-blind-gap-points-b11-1.csv:70

Task: Put the words in order.
word_cards: weekends | cars | at | old | town | allowed | in | the | no | are
Key: {"kind": "order", "sentence": "no cars are allowed in the old town at weekends", "also": ["at weekends no cars are allowed in the old town", "in the old town no cars are allowed at weekends"]}
- reader 1: another correct answer, not accepted: ['no cars are allowed at weekends in the old town']

## r10-070 · B1.1 · order · zz-blind-gap-points-b11-1.csv:71

Task: Put the words in order.
word_cards: were | married | idea | that | had | no | getting | we | they
Key: {"kind": "order", "sentence": "we had no idea that they were getting married", "also": []}
- reader 1: another correct answer, not accepted: ['they had no idea that we were getting married']
- reader 2: another correct answer, not accepted: ['they had no idea that we were getting married']

## r10-084 · B1.1 · order · zz-blind-gap-points-b11-1.csv:85

Task: Put the words in order to make a question.
word_cards: do | we | boarding | to | passes | have | airport | before | our | get | to | we | print | the
Key: {"kind": "order", "sentence": "do we have to print our boarding passes before we get to the airport", "also": []}
- reader 1: another correct answer, not accepted: ['before we get to the airport, do we have to print our boarding passes', 'do we have to get to the airport before we print our boarding passes (grammatical, illogical)']
- reader 1: level: 14 cards is long for B1.1 and the card-count is heavy.
- reader 2: another correct answer, not accepted: ['before we get to the airport, do we have to print our boarding passes', 'do we have to get to the airport before we print our boarding passes (all cards, correct grammar but illogical)']
- reader 2: level: 14 cards: long for B1.1 order task

## r10-085 · B1.1 · order · zz-blind-gap-points-b11-1.csv:86

Task: Put the words in order to make a question.
word_cards: latvian | the | speak | new | english | to | manager | is | enough | does | or | have
Key: {"kind": "order", "sentence": "does the new manager have to speak latvian or is english enough", "also": ["does the new manager have to speak english or is latvian enough"]}
- reader 1: another correct answer, not accepted: ['is english enough or does the new manager have to speak latvian', 'is latvian enough or does the new manager have to speak english']
- reader 1: level: 12 cards with 'X or is Y enough' structure is heavy for B1.1; two clauses in one question.
- reader 2: another correct answer, not accepted: ['is latvian enough or does the new manager have to speak english', 'is english enough or does the new manager have to speak latvian']
- reader 2: level: 12 cards, two-clause question; at the upper edge for B1.1

## r10-086 · B1.1 · order · zz-blind-gap-points-b11-1.csv:87

Task: Put the words in order.
word_cards: work | cancel | i | i | was | because | stuck | my | appointment | dentist | at | to | had
Key: {"kind": "order", "sentence": "i had to cancel my dentist appointment because i was stuck at work", "also": ["because i was stuck at work i had to cancel my dentist appointment"]}
- reader 1: another correct answer, not accepted: ['i was stuck at work because i had to cancel my dentist appointment (grammatical, illogical)']

## r10-088 · B1.1 · order · zz-blind-gap-points-b11-1.csv:89

Task: Put the words in order.
word_cards: hire | staff | to | keep | to | we're | if | more | going | have | sales | growing
Key: {"kind": "order", "sentence": "we're going to have to hire more staff if sales keep growing", "also": ["if sales keep growing we're going to have to hire more staff"]}
- reader 1: level: 'going to have to' with 12 cards is heavy for B1.1.
- reader 2: level: 'going to have to' with 12 cards is heavy for B1.1

## r10-089 · B1.1 · gap · zz-blind-gap-points-b11-1.csv:90

Task: We ___ find a hotel near the station because the last train had already left.
word_cards: have to | must | had to
Key: {"kind": "gap", "accepted": [["had to"]]}
- reader 2: a wrong option that fits: 'have to' is possible in present-tense narration but clashes with 'had already left'; 'must' less likely

## r10-096 · B1.1 · gap · zz-blind-gap-points-b11-1.csv:97

Task: My sister works as a pilot, so she ___ have a medical check every year. (have to)
Key: {"kind": "gap", "accepted": [["has to", "must", "has got to", "'s got to"]]}
- reader 1: another correct answer, not accepted: [['needs to']]
- reader 1: instruction: Cue '(have to)' makes 'has to' the aim, but 'must' also gives correct English.
- reader 2: instruction: 'must' also gives a correct sentence but ignores the hint (have to)

## r10-097 · B1.1 · gap · zz-blind-gap-points-b11-1.csv:98

Task: ___ you ___ show your passport when you crossed the border last weekend? (have to)
Key: {"kind": "gap", "accepted": [["Did"], ["have to"]]}
- reader 1: instruction: Gap 2 'have to' (two words) in one gap while the stem shows 'show' after; fine.

## r10-100 · B1.1 · text · zz-blind-gap-points-b11-1.csv:101

Task: Make a yes/no question: Anna has to take the medicine twice a day while she is ill.
Key: {"kind": "text", "accepted": [["Does Anna have to take the medicine twice a day while she is ill?", "Must Anna take the medicine twice a day while she is ill?", "Has Anna got to take the medicine twice a day while she is ill?", "Does Anna have to take the medicine twice a day?", "While she is ill, must Anna take the medicine twice a day?", "While she is ill, has Anna got to take the medicine twice a day?"]]}
- reader 1: another correct answer, not accepted: ['While she is ill, does Anna have to take the medicine twice a day?']

## r10-101 · B1.1 · text · zz-blind-gap-points-b11-1.csv:102

Task: Say it another way with *might*: Perhaps we will have to sleep at the airport if the strike continues.
Key: {"kind": "text", "accepted": [["We might have to sleep at the airport if the strike continues.", "If the strike continues, we might have to sleep at the airport.", "Perhaps we might have to sleep at the airport if the strike continues.", "We might need to sleep at the airport if the strike continues.", "If the strike continues, we might need to sleep at the airport.", "we might have to sleep at the airport if the strike continues.", "we might need to sleep at the airport if the strike continues.", "If the strike continues, perhaps we might have to sleep at the airport."]]}
- reader 2: another correct answer, not accepted: ['We may have to sleep at the airport if the strike continues.']

