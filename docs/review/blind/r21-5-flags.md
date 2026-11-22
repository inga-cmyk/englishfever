# Blind check r21-5: flags for the judge

60 tasks, 2 readers.

## r21-5-001 · B1.1 · mcq · built-in

Task: Which sentence is NOT correct?
options: I'm having a great time here. | We're meeting at six. | The prices are going up. | She is wanting a new phone.
Key: {"kind": "mcq", "correct": "She is wanting a new phone.", "wrong": ["I'm having a great time here.", "We're meeting at six.", "The prices are going up."]}
- reader 2: sense: Learners do write 'is wanting', fine. 'I'm having a great time' is a possible trap but all others are correct.

## r21-5-003 · B1.1 · mcq · built-in

Task: Choose the option that shows the walk was already going on: I ___ along the street when I saw an old friend.
options: were walking | was walking | am walking | walked
Key: {"kind": "mcq", "correct": "was walking", "wrong": ["walked", "am walking", "were walking"]}
- reader 1: a wrong option that fits: walked (grammatical alone, but does not show the walk was already going on)
- reader 1: instruction: The instruction names the idea (already going on), so it gives the tense away.
- reader 2: instruction: 'shows the walk was already going on' names the meaning and gives the answer away (continuous); also hints 'were walking' is a number slip only.

## r21-5-004 · B1.1 · mcq · built-in

Task: What does 'I've been waiting for an hour' tell us?
options: I started an hour ago and I'm still waiting. | I waited for an hour last week, then left. | I will start waiting in an hour from now. | I waited an hour, but that was years ago.
Key: {"kind": "mcq", "correct": "I started an hour ago and I'm still waiting.", "wrong": ["I waited for an hour last week, then left.", "I will start waiting in an hour from now.", "I waited an hour, but that was years ago."]}
- reader 2: level: Easy for B1; two distractors are obviously nonsense ('will start in an hour from now').

## r21-5-005 · B1.1 · text · built-in

Task: Make a question with How long: They have been waiting.
Key: {"kind": "text", "accepted": [["How long have they been waiting?"]]}
- reader 1: another correct answer, not accepted: [['How long have they waited?']]
- reader 2: another correct answer, not accepted: [['How long have they waited?']]
- reader 2: instruction: Second answer 'How long have they waited?' is correct English (less natural for the given tense).

## r21-5-007 · B1.1 · mcq · built-in

Task: Which sentence says the same as 'They have finished the project'?
options: The project is being finished. | The project have been finished. | The project has been finished. | The project has finished.
Key: {"kind": "mcq", "correct": "The project has been finished.", "wrong": ["The project have been finished.", "The project has finished.", "The project is being finished."]}
- reader 1: a wrong option that fits: The project has finished. (also correct and means the same)
- reader 2: a wrong option that fits: The project has finished.
- reader 2: instruction: 'says the same' is ambiguous: 'The project has finished' is also close in meaning (no agent); 'has been finished' is only the passive match.

## r21-5-008 · B1.1 · mcq · built-in

Task: You do not want to say who will do the action. Choose the correct option.
options: The files check on Monday. | The files will be checked on Monday. | The files will checking on Monday. | Someone checks the files on Monday.
Key: {"kind": "mcq", "correct": "The files will be checked on Monday.", "wrong": ["Someone checks the files on Monday.", "The files check on Monday.", "The files will checking on Monday."]}
- reader 2: a wrong option that fits: Someone checks the files on Monday. (does not state who, arguably fits the instruction but is active and present tense)
- reader 2: instruction: 'say who will do the action' is unclear: option D names 'someone'; the instruction should say 'use the passive'.

## r21-5-009 · B1.2 · mcq · built-in

Task: ___ the new rules be explained to us?
options: Have | Will | Do | Are
Key: {"kind": "mcq", "correct": "Will", "wrong": ["Do", "Are", "Have"]}
- reader 1: level: Very easy for B1.2 (one obvious auxiliary).
- reader 2: sense: Only 'Will' fits before 'be explained'; distractors Do/Have/Are are easy to rule out.

## r21-5-013 · B1.2 · mcq · built-in

Task: 'If we had booked earlier, we would have got a cheaper flight.' What really happened?
options: We booked early. | We will book early. | We booked it early. | We didn't book early.
Key: {"kind": "mcq", "correct": "We didn't book early.", "wrong": ["We booked early.", "We will book early.", "We booked it early."]}
- reader 2: level: 'We booked early' vs 'We booked it early' are near-duplicates, both wrong; fine.

## r21-5-014 · B1.1 · order · b1-cond-rep-1.csv:9

Task: Put the words in order.
word_cards: leaves | alarm | the | the | everyone | if | off | goes | building
Key: {"kind": "order", "sentence": "if the alarm goes off everyone leaves the building", "also": ["everyone leaves the building if the alarm goes off"]}
- reader 1: instruction: No capital letter or comma on cards, so both orders are possible.
- reader 2: answer not accepted: ['the alarm goes off if everyone leaves the building']
- reader 2: another correct answer, not accepted: [['if everyone leaves the building the alarm goes off'], ['everyone leaves the building if the alarm goes off'], ['if the alarm goes off everyone leaves the building']]
- reader 2: instruction: No meaning clue and no capital/comma: four orders are correct English, so the learner cannot know the intended one.
- the readers disagree

## r21-5-015 · B1.2 · order · b1-cond-rep-1.csv:153

Task: Put the words in order.
word_cards: come | was | said | couldn't | he | ill | he | he | because
Key: {"kind": "order", "sentence": "he said he couldn't come because he was ill", "also": []}
- reader 1: another correct answer, not accepted: ["he couldn't come because he was ill he said (unnatural without comma)"]
- reader 1: sense: Unusual sentence: three 'he' cards.
- reader 2: answer not accepted: ["he said he couldn't come because he was ill"]
- reader 2: another correct answer, not accepted: [["because he was ill he said he couldn't come"], ["he said he was ill because he couldn't come"], ["he couldn't come because he said he was ill"], ["he said because he was ill he couldn't come"]]
- reader 2: instruction: Several orders are grammatical; only the logical one is intended but nothing in the task says so.
- the readers disagree

## r21-5-016 · B1.2 · order · b1-cond-rep-1.csv:154

Task: Put the words in order.
word_cards: week | us | she | told | the | was | she | leaving | next | that
Key: {"kind": "order", "sentence": "she told us that she was leaving the next week", "also": []}
- reader 1: instruction: The 'the' card forces 'the next week'; a learner expects 'next week' and cannot place 'the'.
- reader 1: sense: 'the next week' is correct only in reported speech; 'next week' is the more natural wording, so the extra card feels wrong.
- reader 2: answer not accepted: ['she told us that she was leaving the next week']
- reader 2: instruction: Card 'the' forces 'the next week'; 'next week' alone is the natural phrase and a learner may think a card is extra or search for another place for 'the'.
- reader 2: sense: 'the next week' after 'was leaving' is rare; 'the following week' is normal. Natural sentence 'she told us that she was leaving next week' cannot use the card 'the'.
- the readers disagree

## r21-5-017 · B1.2 · mcq · b1-cond-rep-1.csv:215

Task: Choose the correct option: 'Are you ready?' He asked me ___ ready.
options: I was if | was I | that I was | if I was
Key: {"kind": "mcq", "correct": "if I was", "wrong": ["was I", "that I was", "I was if"]}
- reader 2: sense: 'Are you ready?' reported with 'if I was' is fine; 'whether' not offered.

## r21-5-018 · B1.2 · order · b1-new-1.csv:8

Task: Put the words in order.
word_cards: we | used | i | when | to | a | grandparents | child | every | visit | sunday | my | was
Key: {"kind": "order", "sentence": "when i was a child we used to visit my grandparents every sunday", "also": ["we used to visit my grandparents every sunday when i was a child"]}
- reader 1: another correct answer, not accepted: ['every sunday we used to visit my grandparents when i was a child', 'when i was a child every sunday we used to visit my grandparents']
- reader 1: instruction: Many valid orders; check must accept all.
- reader 2: answer not accepted: ['when i was a child we used to visit my grandparents every sunday']
- reader 2: another correct answer, not accepted: [['we used to visit my grandparents every sunday when i was a child'], ['every sunday we used to visit my grandparents when i was a child'], ['when i was a child every sunday we used to visit my grandparents']]
- reader 2: instruction: 13 cards, many correct orders; only a long task with no clue to the intended one.
- the readers disagree

## r21-5-019 · B1.1 · gap · b1-new-1.csv:14

Task: ___ you ___ to live near the sea?
word_cards: use | used | Did | Do
Key: {"kind": "gap", "accepted": [["Did"], ["use"]]}
- reader 1: instruction: Did + used ('Did you used to') is common but non-standard; 'Do ... use' wrong.
- reader 2: level: A2-B1 border; typical B1.1 trap, ok.

## r21-5-022 · B1.1 · mcq · b1-new-1.csv:27

Task: Which sentence is correct?
options: There didn't used to be a supermarket here. | There wasn't use to be a supermarket here. | There not used to be a supermarket here. | There didn't use to be a supermarket here.
Key: {"kind": "mcq", "correct": "There didn't use to be a supermarket here.", "wrong": ["There didn't used to be a supermarket here.", "There not used to be a supermarket here.", "There wasn't use to be a supermarket here."]}
- reader 1: a wrong option that fits: There didn't used to be a supermarket here. (common informal usage, non-standard)
- reader 2: a wrong option that fits: There didn't used to be a supermarket here. (non-standard but very widely written; some speakers/dictionaries accept it)
- reader 2: sense: 'didn't used to' is a common real mistake, believable distractor.

## r21-5-023 · B1.1 · order · b1-new-2.csv:43

Task: Put the words in order.
word_cards: as | we | as | leave | ready | is | everyone | soon | will
Key: {"kind": "order", "sentence": "we will leave as soon as everyone is ready", "also": ["as soon as everyone is ready we will leave"]}
- reader 2: answer not accepted: ['as soon as everyone is ready we will leave']
- reader 2: another correct answer, not accepted: [['we will leave as soon as everyone is ready']]
- reader 2: instruction: Two orders correct (clause first or last).
- the readers disagree

## r21-5-024 · B1.1 · gap · b1-new-3.csv:61

Task: ___ phoned you this morning?
word_cards: Who | Who did | What did
Key: {"kind": "gap", "accepted": [["Who"]]}
- reader 1: level: Easy for B1.1 (subject question; wrong cards obviously odd).
- reader 2: level: Too easy for B1.1 (A2 question); instruction empty.

## r21-5-025 · B1.1 · gap · b1-new-4.csv:12

Task: She will ___ to help us next week.
word_cards: could | can | be able
Key: {"kind": "gap", "accepted": [["be able"]]}
- reader 2: level: Too easy: only 'be able' follows 'will'; B1.1 borderline A2/B1.

## r21-5-026 · B1.2 · text · b1-new-4.csv:84

Task: Start with *The accident*: Someone could have avoided the accident.
Key: {"kind": "text", "accepted": [["The accident could have been avoided."]]}
- reader 1: another correct answer, not accepted: ['The accident could have been avoided by someone.', 'The accident could have been prevented.']
- reader 1: sense: Passive with 'could have been avoided' is B1.2/B2 but fine.
- reader 2: another correct answer, not accepted: [['The accident could have been avoided by someone.'], ["The accident could've been avoided by someone."]]
- reader 2: instruction: Task does not say to use the passive; learner must guess from 'Start with The accident'.

## r21-5-028 · B1.1 · mcq · b1-new-4.csv:200

Task: Choose the correct option: It was an ___ experience.
options: amazes | amazed | amaze | amazing
Key: {"kind": "mcq", "correct": "amazing", "wrong": ["amazed", "amaze", "amazes"]}
- reader 2: level: Too easy for B1 (-ing/-ed adjective at A2-B1 border); 'an' before the gap is a minor give-away: 'amazed' still wrong.

## r21-5-029 · B1.2 · order · b1-new-5.csv:10

Task: Put the words in order.
word_cards: beautiful | a | live | they | old | stone | in | cottage
Key: {"kind": "order", "sentence": "they live in a beautiful old stone cottage", "also": []}
- reader 2: answer not accepted: ['they live in a beautiful old stone cottage']
- reader 2: another correct answer, not accepted: [['in a beautiful old stone cottage they live']]
- reader 2: sense: Second order is poetic and unlikely; adjective order is also demanding for B1.2.
- the readers disagree

## r21-5-030 · B1.1 · match · b1-new-5.csv:129

Task: Match each word with what follows it.
left: so | such a | so many | so much
right: tired | long film | noise | people
Key: {"kind": "match", "pairs": [["so", "tired"], ["such a", "long film"], ["so many", "people"], ["so much", "noise"]]}
- reader 2: level: Easy for B1.1: keyword matching, 'so many/much' pair is the only challenge.

## r21-5-031 · B1.1 · order · b1-new-5.csv:136

Task: Put the words in order.
word_cards: like | would | to | something | you | drink
Key: {"kind": "order", "sentence": "would you like something to drink", "also": ["you would like something to drink"]}
- reader 1: another correct answer, not accepted: ['would you like to drink something']
- reader 2: answer not accepted: ['would you like something to drink']
- reader 2: another correct answer, not accepted: [['you would like something to drink']]
- reader 2: instruction: No question mark or capital clue: the statement 'you would like something to drink' is also correct English.
- the readers disagree

## r21-5-033 · B1.1 · gap · b1-passives-1.csv:22

Task: How often ___ the machines ___ ? (check)
Key: {"kind": "gap", "accepted": [["are"], ["checked"]]}
- reader 2: another correct answer, not accepted: [['do', 'check']]
- reader 2: instruction: 'do the machines check' is grammatical (machines check something) though illogical; (check) does not say passive.

## r21-5-034 · B1.1 · match · b1-passives-1.csv:29

Task: Match each product with how it is made.
left: Cheese | Glass | Paper | Bread
right: is made from milk. | is baked in an oven. | is made from sand. | is made from wood.
Key: {"kind": "match", "pairs": [["Cheese", "is made from milk."], ["Glass", "is made from sand."], ["Paper", "is made from wood."], ["Bread", "is baked in an oven."]]}
- reader 1: level: Bread is also made from flour; only elimination works. Easy.
- reader 2: level: Very easy: content-word matching only; A2.

## r21-5-035 · B1.1 · order · b1-passives-1.csv:43

Task: Put the words in order.
word_cards: heavy | of | rain | the | because | cancelled | match | the | was
Key: {"kind": "order", "sentence": "the match was cancelled because of the heavy rain", "also": ["because of the heavy rain the match was cancelled"]}
- reader 2: answer not accepted: ['the match was cancelled because of the heavy rain']
- reader 2: another correct answer, not accepted: [['because of the heavy rain the match was cancelled']]
- reader 2: instruction: Two orders correct (because-clause first or last).
- the readers disagree

## r21-5-038 · B1.1 · text · b1-passives-1.csv:132

Task: Start with *My umbrella*: Someone has taken my umbrella.
Key: {"kind": "text", "accepted": [["My umbrella has been taken.", "My umbrella has been taken by someone."]]}
- reader 1: another correct answer, not accepted: ['My umbrella has been stolen.']
- reader 2: another correct answer, not accepted: [["My umbrella's been taken."]]
- reader 2: instruction: Does not say to use the passive; 'Start with' is the only hint.

## r21-5-039 · B1.1 · match · b1-passives-1.csv:169

Task: Match each sentence with the one that means the same, without saying who.
left: They will build a new school. | Someone will repair the road. | They will announce the winner. | We will send the tickets.
right: A new school will be built. | The winner will be announced. | The tickets will be sent. | The road will be repaired.
Key: {"kind": "match", "pairs": [["They will build a new school.", "A new school will be built."], ["Someone will repair the road.", "The road will be repaired."], ["They will announce the winner.", "The winner will be announced."], ["We will send the tickets.", "The tickets will be sent."]]}
- reader 2: level: Easy: nouns match each pair.

## r21-5-040 · B1.1 · order · b1-tenses-1.csv:9

Task: Put the words in order.
word_cards: mean | what | your | language | does | in | this | word
Key: {"kind": "order", "sentence": "what does this word mean in your language", "also": []}
- reader 1: another correct answer, not accepted: ['in your language what does this word mean', 'what does this word in your language mean']
- reader 2: answer not accepted: ['what does this word mean in your language']
- reader 2: another correct answer, not accepted: [['in your language what does this word mean'], ['what does this word in your language mean'], ['what does your word mean in this language']]
- reader 2: instruction: Several orders correct; no clue.
- the readers disagree

## r21-5-041 · B1.1 · gap · b1-tenses-1.csv:19

Task: The company ___ over two hundred people and ___ offices in five countries.
word_cards: is having | has | employs
Key: {"kind": "gap", "accepted": [["employs"], ["has"]]}
- reader 2: sense: 'has over two hundred people' is also natural for the first gap but only one 'has' card, so no conflict.

## r21-5-042 · B1.1 · gap · b1-tenses-1.csv:20

Task: The sun ___ in the east and ___ in the west.
word_cards: is rising | rises | has set | sets
Key: {"kind": "gap", "accepted": [["rises"], ["sets"]]}
- reader 1: instruction: Very easy; is rising/has set clearly wrong.
- reader 2: level: Too easy for B1.1 (A1-A2 present simple).

## r21-5-043 · B1.1 · gap · b1-tenses-1.csv:21

Task: He usually ___ his emails first thing in the morning, before he ___ a coffee. (check / make)
Key: {"kind": "gap", "accepted": [["checks"], ["makes"]]}
- reader 2: another correct answer, not accepted: [['checks', 'has made']]
- reader 2: level: Easy for B1.1 (present simple).

## r21-5-044 · B1.1 · text · b1-tenses-1.csv:26

Task: Make a question with How often: He visits his parents.
Key: {"kind": "text", "accepted": [["How often does he visit his parents?"]]}
- reader 2: level: A2 level.

## r21-5-045 · B1.1 · match · b1-tenses-1.csv:30

Task: Match each beginning with its ending.
left: My brother always forgets | The shops never open | Our teacher usually gives | They sometimes eat
right: out on Fridays. | on Sundays. | us homework. | his keys.
Key: {"kind": "match", "pairs": [["My brother always forgets", "his keys."], ["The shops never open", "on Sundays."], ["Our teacher usually gives", "us homework."], ["They sometimes eat", "out on Fridays."]]}
- reader 1: level: Easy for B1.
- reader 2: level: A2: simple keyword matching.

## r21-5-046 · B1.1 · match · b1-tenses-1.csv:31

Task: Match each question with its answer.
left: What does she do? | How often do you swim? | Where does he live? | Do they speak German?
right: Yes, they do. | Twice a week. | She's a nurse. | In a small town.
Key: {"kind": "match", "pairs": [["What does she do?", "She's a nurse."], ["How often do you swim?", "Twice a week."], ["Where does he live?", "In a small town."], ["Do they speak German?", "Yes, they do."]]}
- reader 1: level: Too easy: A1/A2 content.
- reader 2: level: A2, too easy for B1.1.

## r21-5-047 · B1.1 · order · b1-tenses-1.csv:47

Task: Put the words in order.
word_cards: it | chair | this | or | are | can | using | take | i | you
Key: {"kind": "order", "sentence": "are you using this chair or can i take it", "also": []}
- reader 1: answer not accepted: can i take this chair or are you using it
- reader 1: another correct answer, not accepted: ['can i take it or are you using this chair', 'are you using it or can i take this chair']
- reader 1: instruction: Many valid orders.
- reader 2: answer not accepted: ['can i take this chair or are you using it']
- reader 2: another correct answer, not accepted: [['are you using this chair or can i take it'], ['are you using it or can i take this chair'], ['can i take it or are you using this chair']]
- reader 2: instruction: Four orders correct; no clue which.
- the readers disagree

## r21-5-048 · B1.1 · gap · b1-tenses-1.csv:52

Task: Our company ___ a new office, so everything ___ chaotic this week.
word_cards: is opening | opens | was opening | is
Key: {"kind": "gap", "accepted": [["is opening"], ["is"]]}
- reader 1: a wrong option that fits: opens (marginal, scheduled-event reading); was opening (tense mismatch, less natural)
- reader 2: a wrong option that fits: opens (less natural, present simple for a scheduled event)

## r21-5-049 · B1.2 · gap · b1-tenses-2.csv:21

Task: She ___ her homework yet. (not / finish)
Key: {"kind": "gap", "accepted": [["hasn't finished", "has not finished"]]}
- reader 1: another correct answer, not accepted: [["didn't finish"]]
- reader 1: instruction: Gap answers should accept both contracted and full forms; American: didn't finish yet.

## r21-5-050 · B1.2 · match · b1-tenses-2.csv:27

Task: Match each beginning with its ending.
left: I have never tried | She has twice won | They have often stayed | We have never felt
right: scuba diving. | so tired. | in that hotel. | a national prize.
Key: {"kind": "match", "pairs": [["I have never tried", "scuba diving."], ["She has twice won", "a national prize."], ["They have often stayed", "in that hotel."], ["We have never felt", "so tired."]]}
- reader 1: level: Two correct pairings: I/We interchangeable.
- reader 2: level: Easy: keyword matching.

## r21-5-052 · B1.1 · mcq · compare-past-1.csv:4

Task: Which sentence means 'we had already started dinner'?
options: When Karen arrived, we have dinner. | When Karen arrived, we were having dinner. | When Karen arrived, we had dinner.
Key: {"kind": "mcq", "correct": "When Karen arrived, we were having dinner.", "wrong": ["When Karen arrived, we had dinner.", "When Karen arrived, we have dinner."]}
- reader 1: instruction: 'we had dinner' could also mean dinner began on her arrival; instruction gives 'already started' hint.
- reader 2: level: Only three options, two plainly wrong; easy.

## r21-5-053 · B1.1 · gap · compare-past-1.csv:11

Task: I ___ along the road when I ___ Dan. So I stopped, and we talked. (walk / see)
Key: {"kind": "gap", "accepted": [["was walking"], ["saw"]]}
- reader 1: another correct answer, not accepted: [['walked', 'saw']]
- reader 1: instruction: 'walked' is less natural but correct.
- reader 2: instruction: 'So I stopped' is superfluous; the story word 'when' already forces past continuous + simple past.

## r21-5-055 · B1.1 · gap · compare-past-1.csv:44

Task: The house was dirty. They ___ it for weeks. (not / clean)
Key: {"kind": "gap", "accepted": [["hadn't cleaned", "had not cleaned", "hadn't been cleaning"]]}
- reader 2: another correct answer, not accepted: [["didn't clean"], ["haven't cleaned"]]
- reader 2: instruction: 'didn't clean ... for weeks' and 'haven't cleaned' are also acceptable English; 'The house was dirty' suggests past perfect only weakly.

## r21-5-056 · B1.2 · order · compare-past-1.csv:45

Task: Put the words in order.
word_cards: she | already | arrived | had | when | i | left
Key: {"kind": "order", "sentence": "she had already left when i arrived", "also": ["when i arrived she had already left", "i had already left when she arrived", "when she arrived i had already left"]}
- reader 1: instruction: Meaning of who left is not fixed; all four valid.
- reader 2: answer not accepted: ['when i arrived she had already left']
- reader 2: another correct answer, not accepted: [['she had already left when i arrived'], ['when she arrived i had already left'], ['i had already left when she arrived']]
- reader 2: instruction: Meaning reversed (who arrived/left) is also correct; no clue.
- the readers disagree

## r21-5-057 · B1.1 · order · compare-past-1.csv:46

Task: Put all the words in order. More than one answer is possible.
word_cards: house | we | the | it | was | raining | left | when
Key: {"kind": "order", "sentence": "it was raining when we left the house", "also": ["when we left the house it was raining", "we left the house when it was raining"]}
- reader 1: another correct answer, not accepted: ['when it was raining we left the house']
- reader 2: answer not accepted: ['we left the house when it was raining']
- reader 2: another correct answer, not accepted: [['when it was raining we left the house'], ['it was raining when we left the house'], ['when we left the house it was raining']]
- the readers disagree

## r21-5-058 · B1.1 · mcq · twins-1.csv:3

Task: Choose the correct option: I ___ finish the report before the meeting yesterday.
options: must | have to | had to
Key: {"kind": "mcq", "correct": "had to", "wrong": ["must", "have to"]}
- reader 1: level: Easy for B1.
- reader 2: level: Too easy for B1.1 (time word 'yesterday').

## r21-5-059 · B1.1 · gap · twins-1.csv:7

Task: I'm sorry, I ___ come to your party last Saturday. I was ill. (can)
Key: {"kind": "gap", "accepted": [["couldn't"]]}
- reader 1: another correct answer, not accepted: [["wasn't able to"], ['was not able to']]
- reader 1: instruction: With (can) hint, 'wasn't able to' is equally correct.
- reader 2: another correct answer, not accepted: [["wasn't able to"], ['was not able to']]
- reader 2: instruction: Verb in brackets is 'can' but answer is a negative past: not stated ('couldn't'); learners may write 'could' only.

## r21-5-060 · B1.2 · gap · twins-2.csv:6

Task: Leo didn't answer my call. He ___ in a meeting at that moment. (be)
Key: {"kind": "gap", "accepted": [["was"]]}
- reader 1: level: Trivial for B1.2.
- reader 2: level: Too easy for B1.2.

