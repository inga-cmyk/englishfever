# Blind check r20-4: flags for the judge

60 tasks, 2 readers.

## r20-4-001 · B2.1 · gap · learn-drag-4.csv:15

Task: I would be grateful if you ___ send me the report by Friday.
word_cards: can to | would to | could
Key: {"kind": "gap", "accepted": [["could"]]}
- reader 1: sense: Cards 'can to' and 'would to' are not believable mistakes (the gap has no 'to'; they are not real word groups). Also 'would' alone would be the natural second answer but is not offered.
- reader 2: sense: Cards 'can to' and 'would to' are impossible strings, not believable mistakes; bare 'would' (correct: 'if you would send') is not offered, so the set is odd.

## r20-4-002 · B2.1 · order · learn-drag-4.csv:16

Task: Put the words in order.
word_cards: would | I | had | garden | grow | vegetables | I | a | if
Key: {"kind": "order", "sentence": "if I had a garden I would grow vegetables", "also": ["I would grow vegetables if I had a garden"]}
- reader 1: another correct answer, not accepted: [['if i had a garden i would grow vegetables']]
- reader 1: instruction: Cards are all lower case and no punctuation, so both clause orders are open; nothing says which. Fine, but both must be accepted.
- reader 2: another correct answer, not accepted: [['if i had a garden i would grow vegetables']]
- reader 2: instruction: No sentence start or comma is given, so both clause orders are possible.

## r20-4-003 · B2.1 · gap · learn-drag-4.csv:17

Task: She would have passed the exam if she ___ ___ harder.
word_cards: has | was | studied | had
Key: {"kind": "gap", "accepted": [["had"], ["studied"]]}
- reader 1: level: B2.1 is too low-level for a basic third conditional with two obvious cards (B1).
- reader 2: sense: Distractors 'has'/'was' are believable but 'was studied' is random.

## r20-4-004 · B2.1 · order · learn-drag-4.csv:18

Task: Put the words in order.
word_cards: parked | I | I | there | had | sign | if | the | seen | have | wouldn't
Key: {"kind": "order", "sentence": "if I had seen the sign I wouldn't have parked there", "also": ["I wouldn't have parked there if I had seen the sign"]}
- reader 1: another correct answer, not accepted: [["if i had seen the sign i wouldn't have parked there"]]
- reader 2: instruction: No sentence start or comma is given, so both clause orders are possible.

## r20-4-005 · B2.1 · order · learn-drag-4.csv:19

Task: Put the words in order.
word_cards: have | better | had | prepared | the | team | if | won | been | would | we
Key: {"kind": "order", "sentence": "if the team had been better prepared we would have won", "also": ["we would have won if the team had been better prepared"]}
- reader 1: answer not accepted: if we had been better prepared the team would have won
- reader 1: another correct answer, not accepted: [['the team would have won if we had been better prepared'], ['if the team had been better prepared we would have won'], ['we would have won if the team had been better prepared'], ['the team would have won if we had been better prepared']]
- reader 1: instruction: Several correct orders (swapping 'we' and 'the team', clause order). 'We' and 'the team' interchangeable is odd.
- reader 1: sense: Mixing 'we' and 'the team' as different subjects is illogical; sentences with both are strange.
- reader 2: another correct answer, not accepted: ['the team would have won if we had been better prepared', 'if we had been better prepared the team would have won']
- reader 2: instruction: No sentence start or comma is given, so both clause orders are possible. Also the subject can be 'the team' or 'we'.
- the readers disagree

## r20-4-006 · B2.1 · gap · learn-drag-4.csv:20

Task: If you had told us earlier, we ___ ___ adjusted the schedule.
word_cards: have | can | had | could
Key: {"kind": "gap", "accepted": [["could"], ["have"]]}
- reader 1: level: B2.1: basic third conditional (B1).
- reader 2: sense: 'would' is the obvious answer and is not offered; ok but 'could' adjusted is a slightly odd meaning.

## r20-4-007 · B2.1 · order · learn-drag-4.csv:21

Task: Put the words in order.
word_cards: I | have | birthday | her | had | remembered | I | would | her | if | called
Key: {"kind": "order", "sentence": "if I had remembered her birthday I would have called her", "also": ["I would have called her if I had remembered her birthday"]}
- reader 1: another correct answer, not accepted: [['if i had remembered her birthday i would have called her']]
- reader 2: instruction: No sentence start or comma is given, so both clause orders are possible.

## r20-4-008 · B2.2 · gap · learn-drag-4.csv:22

Task: If she ___ ___ the warning, she would have avoided the accident.
word_cards: was | has | heard | had
Key: {"kind": "gap", "accepted": [["had"], ["heard"]]}
- reader 1: level: Too easy for B2.2 (B1 third conditional, two obvious cards).
- reader 2: sense: Only two real choices; easy for B2.2 (same pattern as 3 and 9).

## r20-4-009 · B2.2 · gap · learn-drag-4.csv:23

Task: If he hadn't been driving so fast, he ___ ___ lost his licence.
word_cards: have | wouldn't | hadn't | won't
Key: {"kind": "gap", "accepted": [["wouldn't"], ["have"]]}
- reader 1: level: Too easy for B2.2 (B1 third conditional).
- reader 2: instruction: Cards 'hadn't' and 'won't' cannot fit; trivial for B2.2.
- reader 2: level: B2.2 too easy: basic third conditional.

## r20-4-010 · B2.2 · order · learn-drag-4.csv:24

Task: Put the words in order.
word_cards: would've | the | known | traffic | I'd | if | earlier | about | I | left
Key: {"kind": "order", "sentence": "if I'd known about the traffic I would've left earlier", "also": ["I would've left earlier if I'd known about the traffic"]}
- reader 1: another correct answer, not accepted: [["if i'd known about the traffic i would've left earlier"], ["if i'd known earlier about the traffic i would've left"], ["i would've left if i'd known about the traffic earlier"], ["i would've known about the traffic if i'd left earlier"], ["if i'd left earlier i would've known about the traffic"]]
- reader 1: instruction: 'earlier' can attach to 'known' or 'left', so several orders; the last two are logically odd but grammatical.
- reader 2: answer not accepted: i would've known about the traffic if i'd left earlier
- reader 2: another correct answer, not accepted: ["if i'd left earlier i would've known about the traffic"]
- reader 2: instruction: No sentence start or comma is given, so both clause orders are possible. Both meanings work (known/left swap).
- reader 2: sense: Contracted cards only fit one pattern; fine.
- the readers disagree

## r20-4-011 · B2.2 · gap · learn-drag-4.csv:25

Task: If I had ___ the impact of my decision, I would have ___ differently.
word_cards: act | realised | realise | acted
Key: {"kind": "gap", "accepted": [["realised"], ["acted"]]}
- reader 1: level: Too easy for B2.2 (past participle choice from base forms).
- reader 1: sense: Wrong cards are bare base forms, believable.
- reader 2: level: B2.2 too easy: past participle choice only.

## r20-4-012 · B2.2 · order · learn-drag-4.csv:26

Task: Put the words in order.
word_cards: had | called | we | problem | known | if | have | we | the | about | you | would
Key: {"kind": "order", "sentence": "if we had known about the problem we would have called you", "also": ["we would have called you if we had known about the problem"]}
- reader 1: another correct answer, not accepted: [['we would have called you if we had known about the problem'], ['if we had called you we would have known about the problem'], ['we would have known about the problem if we had called you']]
- reader 2: answer not accepted: if you had called we would have known about the problem
- reader 2: another correct answer, not accepted: ['we would have known about the problem if you had called']
- reader 2: instruction: No sentence start or comma is given, so both clause orders are possible. Two meanings are possible.
- the readers disagree

## r20-4-013 · B2.1 · order · learn-drag-4.csv:27

Task: Put the words in order.
word_cards: on | delay | despite | arrived | time | we | the
Key: {"kind": "order", "sentence": "despite the delay we arrived on time", "also": ["we arrived on time despite the delay"]}
- reader 1: another correct answer, not accepted: [['despite the delay we arrived on time']]
- reader 1: instruction: Too easy; 'despite' is B1 and only 7 cards.
- reader 1: level: Below B2.1 (despite + noun is B1).
- reader 2: instruction: No sentence start or comma is given, so both clause orders are possible.
- reader 2: level: Too easy/short for B2.1 (7 words, B1).

## r20-4-014 · B2.1 · gap · learn-drag-4.csv:28

Task: In ___ ___ the cold, they went swimming.
word_cards: despite | for | of | spite
Key: {"kind": "gap", "accepted": [["spite"], ["of"]]}
- reader 1: instruction: 'in despite of' is archaic, not standard: should not be accepted.
- reader 1: level: 'in spite of' is B1.
- reader 2: instruction: Copying a fixed phrase; 'despite' distractor easily excluded; near-duplicate of 31.
- reader 2: level: Fixed phrase, low level for B2.1.

## r20-4-015 · B2.1 · order · learn-drag-4.csv:29

Task: Put the words in order.
word_cards: the | the | went | despite | ahead | rain | match
Key: {"kind": "order", "sentence": "despite the rain the match went ahead", "also": ["the match went ahead despite the rain"]}
- reader 1: another correct answer, not accepted: [['despite the rain the match went ahead']]
- reader 1: level: Despite + noun is B1, short sentence: too easy for B2.1.
- reader 2: instruction: No sentence start or comma is given, so both clause orders are possible.
- reader 2: level: Short and easy for B2.1.

## r20-4-016 · B2.1 · order · learn-drag-4.csv:31

Task: Put the words in order.
word_cards: that | out | raining | the | despite | it | we | was | fact | went
Key: {"kind": "order", "sentence": "we went out despite the fact that it was raining", "also": ["despite the fact that it was raining we went out"]}
- reader 1: another correct answer, not accepted: [['we went out despite the fact that it was raining']]
- reader 2: instruction: No sentence start or comma is given, so both clause orders are possible.

## r20-4-017 · B2.1 · order · learn-drag-4.csv:32

Task: Put the words in order.
word_cards: the | will | repair | telling | mind | long | take | you | me | would | how
Key: {"kind": "order", "sentence": "would you mind telling me how long the repair will take", "also": ["you would mind telling me how long the repair will take"]}
- reader 1: instruction: Does not say it is a polite request; fine. Natural.

## r20-4-019 · B2.1 · gap · learn-drag-4.csv:34

Task: I'd like to know where you ___ last night.
word_cards: went | did go | did you go
Key: {"kind": "gap", "accepted": [["went"]]}
- reader 1: instruction: Gap is trivially solved from 'where you ___'; distractor 'did you go' is a standard mistake, 'did go' is not believable.
- reader 1: level: Indirect question is B1; fine for review at B2.1 but easy.
- reader 2: level: B1 indirect question; low for B2.1.
- reader 2: sense: Distractors are believable.

## r20-4-020 · B2.1 · order · learn-drag-4.csv:35

Task: Put the words in order.
word_cards: know | the | when | shop | do | you | closes
Key: {"kind": "order", "sentence": "do you know when the shop closes", "also": []}
- reader 1: level: B1 (or lower): indirect question, 7 words. Too easy for B2.1.
- reader 2: instruction: Content already in a near-normal order; easy.
- reader 2: level: B1, too low for B2.1.

## r20-4-021 · B2.1 · order · learn-drag-4.csv:36

Task: Put the words in order.
word_cards: opens | time | do | you | what | know | it
Key: {"kind": "order", "sentence": "do you know what time it opens", "also": []}
- reader 1: level: B1 or lower; too easy for B2.1.
- reader 2: instruction: Too easy (7 words).
- reader 2: level: B1, too low for B2.1.

## r20-4-022 · B2.1 · order · learn-drag-4.csv:37

Task: Put all the words in order. More than one answer is possible.
word_cards: could | help | she | if | her | asked | I
Key: {"kind": "order", "sentence": "she asked if I could help her", "also": ["I asked her if she could help"]}
- reader 1: another correct answer, not accepted: [['she asked if i could help her'], ['i asked if she could help her'], ['she asked her if i could help']]
- reader 1: instruction: Instruction says several answers are possible, which gives away that it is not one fixed sentence; fine.
- reader 2: another correct answer, not accepted: [['she asked if i could help her'], ['i asked if she could help her']]
- reader 2: instruction: 'More than one answer' is stated; fine.
- reader 2: sense: 'asked her' vs 'she asked' both use all cards.

## r20-4-023 · B2.1 · gap · learn-drag-4.csv:38

Task: The nurse told me ___ ___ touch it.
word_cards: don't | not | no | to
Key: {"kind": "gap", "accepted": [["not"], ["to"]]}
- reader 1: level: Reported command is B1, easy for B2.1.
- reader 2: level: A2/B1 level, too low for B2.1.

## r20-4-024 · B2.1 · order · learn-drag-4.csv:39

Task: Put the words in order.
word_cards: send | the | Lena | me | invoice | her | to | asked
Key: {"kind": "order", "sentence": "Lena asked me to send her the invoice", "also": []}
- reader 1: another correct answer, not accepted: [['lena asked her to send me the invoice']]
- reader 2: another correct answer, not accepted: [['lena asked her to send me the invoice']]
- reader 2: sense: Second answer is ambiguous but grammatical.

## r20-4-025 · B2.1 · gap · learn-drag-4.csv:40

Task: He asked me what time ___ ___.
word_cards: it | was | did | does
Key: {"kind": "gap", "accepted": [["it"], ["was"]]}
- reader 1: level: Reported question with 'what time' is B1; easy for B2.1.
- reader 2: level: B1 reported question, low for B2.1.

## r20-4-029 · B2.1 · gap · twins-1.csv:33

Task: Complete with one word: She spoke slowly so ___ to be understood.
Key: {"kind": "gap", "accepted": [["as"]]}
- reader 1: instruction: Gives away 'so as' only by 'so'; fine.
- reader 2: instruction: 'Complete with one word' fine.

## r20-4-030 · B2.1 · text · twins-1.csv:34

Task: Correct the mistake: Despite of the delay, we arrived on time.
Key: {"kind": "text", "accepted": [["Despite the delay, we arrived on time.", "In spite of the delay, we arrived on time."]]}
- reader 1: another correct answer, not accepted: ['We arrived on time despite the delay.', 'We arrived on time in spite of the delay.', 'Despite being delayed, we arrived on time.']
- reader 2: another correct answer, not accepted: ['We arrived on time despite the delay.', 'We arrived on time in spite of the delay.']
- reader 2: instruction: 'Correct the mistake' allows the in spite of fix too.

## r20-4-031 · B2.1 · gap · twins-1.csv:35

Task: Complete with one word: In ___ of the cold, they went swimming.
Key: {"kind": "gap", "accepted": [["spite"]]}
- reader 1: another correct answer, not accepted: [['despite']]
- reader 1: instruction: Nearly identical to r20-4-014 (same sentence); 'of' given away. 'In despite of' archaic, should not be accepted.
- reader 1: sense: Duplicate of 014.
- reader 2: instruction: Near-duplicate of 14.

## r20-4-033 · B2.1 · mcq · twins-1.csv:43

Task: Which is correct? 'If I ___ in your position, I'd ask for a pay rise.'
options: were | be | would be | am
Key: {"kind": "mcq", "correct": "were", "wrong": ["am", "would be", "be"]}
- reader 2: level: B1 (second conditional with were); low for B2.1.

## r20-4-034 · B2.1 · gap · twins-1.csv:44

Task: The city has no money for cycle lanes, so it won't build any. If it ___ more cycle lanes, more people ___ by bike. (build / travel)
Key: {"kind": "gap", "accepted": [["built"], ["would travel"]]}
- reader 1: another correct answer, not accepted: [['built', 'might travel'], ['were to build', 'would travel'], ['were to build', 'might travel'], ['were to build', 'could travel']]
- reader 1: instruction: The given verbs (build / travel) are base forms; fine.
- reader 2: another correct answer, not accepted: [['built', 'might travel'], ['were to build', 'would travel'], ['built', 'would be travelling']]
- reader 2: instruction: The first sentence is only context; ok.

## r20-4-035 · B2.1 · mcq · twins-1.csv:45

Task: Which sentence has a mistake?
options: If she lived nearer, she'd visit more often. | If he knew the answer, he would tell us all. | If I would have a car, I would drive to work. | We would travel more if flights were cheaper.
Key: {"kind": "mcq", "correct": "If I would have a car, I would drive to work.", "wrong": ["If she lived nearer, she'd visit more often.", "We would travel more if flights were cheaper.", "If he knew the answer, he would tell us all."]}
- reader 1: sense: Common learner error, believable. Duplicates the pattern in 036.
- reader 2: level: B1.
- reader 2: sense: Believable learner mistake; fine.

## r20-4-036 · B2.1 · mcq · twins-1.csv:46

Task: Which sentence is correct?
options: If I have a car, I wouldn't take the bus. | If I had a car, I wouldn't take the bus. | If I would have a car, I wouldn't take the bus. | If I had a car, I won't take the bus.
Key: {"kind": "mcq", "correct": "If I had a car, I wouldn't take the bus.", "wrong": ["If I have a car, I wouldn't take the bus.", "If I would have a car, I wouldn't take the bus.", "If I had a car, I won't take the bus."]}
- reader 1: sense: Option 3 duplicates the wrong form from 035.
- reader 2: level: B1.
- reader 2: sense: Option 3 repeats the mistake of 35.

## r20-4-037 · B2.1 · text · twins-1.csv:47

Task: Write the sentence with if: I don't have a garden, so I don't grow vegetables.
Key: {"kind": "text", "accepted": [["If I had a garden, I would grow vegetables.", "If I had a garden, I'd grow vegetables.", "I would grow vegetables if I had a garden.", "I'd grow vegetables if I had a garden."]]}
- reader 1: another correct answer, not accepted: ['If I had a garden, I might grow vegetables.', "If I had a garden, I'd grow my own vegetables."]
- reader 1: instruction: Does not say second conditional; fine.
- reader 2: another correct answer, not accepted: ['If I were to have a garden, I would grow vegetables.']
- reader 2: level: B1.

## r20-4-038 · B2.2 · mcq · twins-1.csv:48

Task: We got lost yesterday because we didn't check the map. Imagine the opposite: 'If we ___ the map, we ___ lost.'
options: had checked / wouldn't have got | checked / wouldn't get | would check / hadn't got | had checked / wouldn't get
Key: {"kind": "mcq", "correct": "had checked / wouldn't have got", "wrong": ["checked / wouldn't get", "had checked / wouldn't get", "would check / hadn't got"]}
- reader 1: level: B2.2: basic third conditional (B1); too easy.
- reader 2: sense: Distractor 4 'wouldn't get' is wrong but close; American 'gotten' not offered.

## r20-4-039 · B2.2 · gap · twins-1.csv:49

Task: She stayed late and missed the last bus. If she ___ (not / stay) so late, she ___ (not / miss) the last bus.
Key: {"kind": "gap", "accepted": [["hadn't stayed"], ["wouldn't have missed"]]}
- reader 1: another correct answer, not accepted: [["hadn't stayed", 'might not have missed']]
- reader 1: level: B2.2: basic third conditional.
- reader 2: instruction: No form is hinted; fine.

## r20-4-040 · B2.2 · mcq · twins-1.csv:50

Task: Which sentence is NOT correct?
options: If they'd have asked me, I would've helped. | If I had known, I wouldn't have said it. | She would have come if you'd invited her. | If it had rained, we'd have stayed in.
Key: {"kind": "mcq", "correct": "If they'd have asked me, I would've helped.", "wrong": ["If it had rained, we'd have stayed in.", "She would have come if you'd invited her.", "If I had known, I wouldn't have said it."]}
- reader 1: sense: Very common learner/native error, believable. 'd ambiguity is the point.
- reader 2: sense: 'If they'd have asked' is common in informal speech, so some learners may call it acceptable.

## r20-4-041 · B2.2 · mcq · twins-1.csv:51

Task: Which sentence is correct?
options: If we would have known about the problem, we would call you. | If we had known about the problem, we will have called you. | If we had known about the problem, we would have called you. | If we had knew about the problem, we would have called you.
Key: {"kind": "mcq", "correct": "If we had known about the problem, we would have called you.", "wrong": ["If we had knew about the problem, we would have called you.", "If we would have known about the problem, we would call you.", "If we had known about the problem, we will have called you."]}
- reader 1: sense: Option 4 'had knew' is a believable slip but easy.

## r20-4-042 · B2.2 · text · twins-1.csv:52

Task: Write the sentence with if: I didn't know about the sale, so I didn't buy the coat.
Key: {"kind": "text", "accepted": [["If I had known about the sale, I would have bought the coat.", "I would have bought the coat if I had known about the sale.", "If I'd known about the sale, I'd have bought the coat.", "If I'd known about the sale, I would have bought the coat.", "If I had known about the sale, I'd have bought the coat.", "I'd have bought the coat if I'd known about the sale.", "I would have bought the coat if I'd known about the sale.", "I'd have bought the coat if I had known about the sale."]]}
- reader 1: another correct answer, not accepted: ['Had I known about the sale, I would have bought the coat.']
- reader 1: level: B2.2: basic third conditional.
- reader 2: another correct answer, not accepted: ['Had I known about the sale, I would have bought the coat.']

## r20-4-043 · B2.2 · mcq · twins-1.csv:53

Task: Choose the correct option: ___ for your help, we would never have finished on time.
options: Without | Unless | But
Key: {"kind": "mcq", "correct": "But", "wrong": ["Without", "Unless"]}
- reader 1: answer not accepted: Without
- reader 1: a wrong option that fits: But
- reader 1: sense: 'But for' is also correct (more formal): 'But' fits.
- reader 2: instruction: 'Without for' is impossible; 'but for' is a formal phrase B2.2 may not know.
- reader 2: sense: Options 'Without' and 'Unless' + 'for' are not believable errors.
- the readers disagree

## r20-4-044 · B2.2 · text · twins-1.csv:54

Task: Rewrite starting with *Were*: If the price were lower, more people would buy it.
Key: {"kind": "text", "accepted": [["Were the price lower, more people would buy it.", "Were the price lower, more people would buy the product."]]}
- reader 1: another correct answer, not accepted: ['Were the price to be lower, more people would buy it.', 'More people would buy it were the price lower.', 'Were the price to fall, more people would buy it.']
- reader 1: instruction: Asterisks around Were show as markup.
- reader 2: another correct answer, not accepted: ['Were the price to be lower, more people would buy it.']
- reader 2: instruction: Gives away the form; mostly copying.

## r20-4-046 · B2.2 · gap · twins-1.csv:56

Task: ___ he ___ harder, he would have passed the exam.
word_cards: study | Did | studied | Had
Key: {"kind": "gap", "accepted": [["Had"], ["studied"]]}
- reader 1: sense: 'Did' + 'study' is a believable-looking distractor pair but gap 1 and 2 are tied; easy.
- reader 2: level: B2.2 slightly easy; 'Did' and 'study' not believable.

## r20-4-047 · B2.2 · gap · twins-1.csv:57

Task: ___ it not been for the rain, the match would have finished on time.
word_cards: Did | Were | Has | Had
Key: {"kind": "gap", "accepted": [["Had"]]}
- reader 1: instruction: Task says 'each gap' but there is only one gap; very easy (the only card that makes sense).
- reader 2: instruction: Instruction has one gap; the note says 'each gap'.
- reader 2: level: B2.2 fixed phrase; fine.

## r20-4-048 · B2.2 · mcq · twins-1.csv:58

Task: Choose the correct option: It's high time we ___ a decision.
options: made | making | have made | make
Key: {"kind": "mcq", "correct": "made", "wrong": ["make", "have made", "making"]}
- reader 1: a wrong option that fits: make: heard informally (esp. US) but non-standard

## r20-4-049 · B2.2 · gap · twins-1.csv:59

Task: I'd rather you ___ anyone about this yet.
word_cards: won't tell | not to tell | didn't tell | don't tell
Key: {"kind": "gap", "accepted": [["didn't tell"]]}
- reader 1: a wrong option that fits: don't tell (informal; 'I'd rather you don't' is used)
- reader 2: a wrong option that fits: 'don't tell' (informal, some speakers; usually judged less correct)

## r20-4-052 · B2.2 · text · twins-1.csv:62

Task: Write one sentence that starts with *I'd rather*: Please don't call me after ten.
Key: {"kind": "text", "accepted": [["I'd rather you didn't call me after ten.", "I would rather you didn't call me after ten.", "I'd rather you didn't call me after ten o'clock.", "I would rather you didn't call me after ten o'clock.", "I'd rather you not call me after ten.", "I would rather you not call me after ten.", "After ten, I'd rather you didn't call me.", "After ten, I would rather you didn't call me.", "After ten o'clock, I'd rather you didn't call me.", "After ten o'clock, I would rather you didn't call me.", "After ten, I'd rather you not call me.", "After ten, I would rather you not call me."]]}
- reader 1: another correct answer, not accepted: ["I'd rather you didn't phone me after ten.", "I'd rather you didn't ring me after ten.", "I'd rather you wouldn't call me after ten.", "I'd rather not be called after ten."]
- reader 1: instruction: 'I'd rather' + 'you' is not stated; learners may write 'I'd rather not'/'I'd rather you not' etc. Many answers.
- reader 2: another correct answer, not accepted: ["I'd rather you didn't phone me after ten.", "I'd rather not be called after ten.", "I'd rather you wouldn't call me after ten."]
- reader 2: instruction: 'Write one sentence' open; many answers.

## r20-4-053 · B2.2 · mcq · twins-1.csv:63

Task: Which sentence reports 'You lost my keys!' as an accusation?
options: He accused me that I lost his keys. | He accused me for losing his keys. | He accused me of losing his keys. | He accused me to lose his keys.
Key: {"kind": "mcq", "correct": "He accused me of losing his keys.", "wrong": ["He accused me to lose his keys.", "He accused me that I lost his keys.", "He accused me for losing his keys."]}
- reader 1: instruction: 'accused' appears in the instruction, giving the verb away.
- reader 2: instruction: 'as an accusation' hints the verb accuse.

## r20-4-054 · B2.2 · gap · twins-1.csv:64

Task: 'Don't sign anything until you've read it.' → The lawyer advised her ___.
Key: {"kind": "gap", "accepted": [["not to sign anything until she had read it", "not to sign anything until she'd read it", "not to sign anything until she read it", "against signing anything until she had read it", "not to sign anything before reading it", "not to sign anything before she had read it", "not to sign anything before she read it"]]}
- reader 1: another correct answer, not accepted: [['not to sign anything until she has read it'], ['not to sign anything until she had read it carefully']]
- reader 1: instruction: Single long gap: how many words is not stated; far too open for typed marking. Hard to judge what counts.
- reader 2: instruction: No word count given; many wordings.

## r20-4-058 · B2.1 · text · twins-1.csv:69

Task: Ask politely, starting with *Could you tell me*: Why is the flight delayed?
Key: {"kind": "text", "accepted": [["Could you tell me why the flight is delayed?", "Could you tell me why the flight's delayed?"]]}
- reader 1: another correct answer, not accepted: ['Could you tell me why the flight has been delayed?', 'Could you tell me why the flight is late?', 'Could you tell me why the flight was delayed?', 'Could you tell me why the flight is so late?']
- reader 2: another correct answer, not accepted: ['Could you tell me why the flight has been delayed?', 'Could you tell me why the flight was delayed?']

## r20-4-059 · B2.1 · mcq · twins-1.csv:70

Task: Which sentence is NOT correct?
options: I wonder how far the station is. | Could you tell me who called me? | Do you know if Anna is at home? | Do you know what time does it open?
Key: {"kind": "mcq", "correct": "Do you know what time does it open?", "wrong": ["Do you know if Anna is at home?", "I wonder how far the station is.", "Could you tell me who called me?"]}
- reader 1: sense: Option 2 'who called me' is a subject question: fine.

