# Blind check r20b-3: flags for the judge

52 tasks, 2 readers.

## r20b-3-002 · B2.2 · mcq · built-in

Task: What is the difference? A: 'If you had asked, I would have helped.' B: 'If you asked, I would help.'
options: There is no difference in meaning. | A is about the past, B about now or the future. | A is about the future, B the past. | A is about now, B about the past.
Key: {"kind": "mcq", "correct": "A is about the past, B about now or the future.", "wrong": ["A is about now, B about the past.", "A is about the future, B the past.", "There is no difference in meaning."]}
- reader 2: level: Easy for B2.2 (B1 conditional contrast).

## r20b-3-003 · B2.2 · mcq · built-in

Task: Which sentence is correct?
options: If I had realised the impact of my decision, I would have acted differently. | If I realised the impact of my decision, I would have acted differently. | If I would have realised the impact of my decision, I would have acted differently. | If I had realised the impact of my decision, I would acted differently.
Key: {"kind": "mcq", "correct": "If I had realised the impact of my decision, I would have acted differently.", "wrong": ["If I realised the impact of my decision, I would have acted differently.", "If I would have realised the impact of my decision, I would have acted differently.", "If I had realised the impact of my decision, I would acted differently."]}
- reader 1: sense: Near-duplicate of 006, 031, 032 (third conditional); 'would acted' is a typo-like distractor nobody writes.

## r20b-3-004 · B2.2 · text · built-in

Task: Imagine the past was different, and say how things would be now. Start with *If he*: He didn't take the job, so he isn't living in Paris now.
Key: {"kind": "text", "accepted": [["If he had taken the job, he would be living in Paris now.", "If he'd taken the job, he'd be living in Paris now.", "He would be living in Paris now if he had taken the job.", "He'd be living in Paris now if he'd taken the job.", "If he had taken the job, he would live in Paris now.", "If he'd taken the job, he'd live in Paris now.", "He would live in Paris now if he had taken the job.", "If he had taken the job, he would be in Paris now.", "If he'd taken the job, he'd be in Paris now.", "He would be in Paris now if he had taken the job."]]}
- reader 1: another correct answer, not accepted: [['If he had taken the job, he might be living in Paris now.']]
- reader 2: another correct answer, not accepted: [['If he had taken the job, he might be living in Paris now.']]

## r20b-3-006 · B2.2 · mcq · built-in

Task: Which sentence is correct?
options: If only we had listened to the warning signs last year, we would not be in this position now. | If only we would have listened to the warning signs last year, we would not be in this position now. | If only we listened to the warning signs last year, we would not be in this position now.
Key: {"kind": "mcq", "correct": "If only we had listened to the warning signs last year, we would not be in this position now.", "wrong": ["If only we would have listened to the warning signs last year, we would not be in this position now.", "If only we listened to the warning signs last year, we would not be in this position now."]}
- reader 2: sense: Option 3 (past simple) and option 2 ('would have') are very similar types of error; fine but two of three wrong options are the same family.

## r20b-3-007 · B2.2 · mcq · built-in

Task: Tom's question to you: 'What should I do?' Which sentence reports it?
options: He asked me what should he do. | He asked me what to do. | He asked me what he does.
Key: {"kind": "mcq", "correct": "He asked me what to do.", "wrong": ["He asked me what should he do.", "He asked me what he does."]}
- reader 1: sense: 'what he does' changes the meaning, fine as distractor.
- reader 2: level: B1 level, easy for B2.2.

## r20b-3-009 · B2.2 · mcq · built-in

Task: Which sentence is NOT correct?
options: My doctor advised me to rest. | She suggested to go by train. | They promised that they would call back. | He denied taking the money.
Key: {"kind": "mcq", "correct": "She suggested to go by train.", "wrong": ["He denied taking the money.", "My doctor advised me to rest.", "They promised that they would call back."]}
- reader 2: level: B1 level, easy for B2.2.

## r20b-3-010 · B2.2 · gap · built-in

Task: 'Congratulations, Jo! You've finally passed the exam!' I congratulated Jo ___ passing the exam.
word_cards: to | on | for | of
Key: {"kind": "gap", "accepted": [["on"]]}
- reader 1: instruction: 'congratulate someone for' is attested but less standard; if key accepts only 'on', fine, but 'for' is not wrong.
- reader 2: a wrong option that fits: 'for' is used by some speakers (congratulate someone for) and is arguably correct; standard is 'on'.
- reader 2: level: B1 level, easy for B2.2.

## r20b-3-013 · B2.2 · text · built-in

Task: Combine the two sentences without changing their meaning: Who made the decision? It's not clear.
Key: {"kind": "text", "accepted": [["It's not clear who made the decision.", "It is not clear who made the decision.", "Who made the decision is not clear.", "It's unclear who made the decision.", "It is unclear who made the decision.", "It remains unclear who made the decision."]]}
- reader 2: another correct answer, not accepted: [['Who made the decision is unclear.']]

## r20b-3-014 · B2.2 · mcq · built-in

Task: Choose the correct word: ___ booked the meeting room should cancel it if plans change.
options: Wherever | Whatever | Whoever | Whomever
Key: {"kind": "mcq", "correct": "Whoever", "wrong": ["Whomever", "Whatever", "Wherever"]}
- reader 1: sense: Near-duplicate of 040 (whoever/whomever).
- reader 2: sense: 'Whomever booked' is wrong as it is the subject; fine.

## r20b-3-015 · B2.1 · order · built-in

Task: Put the words in order.
word_cards: would | a | doctor | be | I | if | medicine | studied | had | now | I
Key: {"kind": "order", "sentence": "if I had studied medicine I would be a doctor now", "also": ["if I had studied medicine I would now be a doctor", "I would be a doctor now if I had studied medicine", "I would now be a doctor if I had studied medicine"]}
- reader 1: another correct answer, not accepted: ['now I would be a doctor if I had studied medicine', 'if I had studied medicine now I would be a doctor']
- reader 1: instruction: No starting word or punctuation card, so many orders are possible; learner cannot know which is wanted. Also two 'I' cards are interchangeable.
- reader 2: another correct answer, not accepted: [['i would be a doctor now if i had studied medicine'], ['if i had studied medicine, i would now be a doctor'], ['i would now be a doctor if i had studied medicine'], ['now i would be a doctor if i had studied medicine'], ['if i had studied medicine, now i would be a doctor']]
- reader 2: instruction: No capital or comma cue and no hint that several orders are possible; at least two clause orders work.

## r20b-3-016 · B2.2 · mcq · compare-past-1.csv:49

Task: Choose the correct option: Mark was covered in sweat when I saw him. He ___ at the gym.
options: had been train | had been training | has been training
Key: {"kind": "mcq", "correct": "had been training", "wrong": ["has been training", "had been train"]}
- reader 1: sense: 'had been train' is a form hardly anyone writes.
- reader 2: a wrong option that fits: 'has been training' is wrong in past context (marginal).

## r20b-3-017 · B2.1 · gap · compare-past-1.csv:52

Task: The shop was busy yesterday. By eleven o'clock Mark ___ forty customers. (serve)
Key: {"kind": "gap", "accepted": [["had served", "'d served"]]}
- reader 1: another correct answer, not accepted: [['had been serving'], ['served']]
- reader 1: instruction: 'had been serving' is less natural with a count of customers; 'served' is weaker but possible.
- reader 1: sense: Near-duplicate of 036.
- reader 2: another correct answer, not accepted: [['served']]
- reader 2: instruction: 'served' (past simple with 'by') is possible, less natural.

## r20b-3-018 · B2.2 · gap · compare-past-1.csv:56

Task: When I looked outside, it ___ any more, but the roads were still wet. (not / snow)
Key: {"kind": "gap", "accepted": [["wasn't snowing", "was not snowing"]]}
- reader 1: level: Past continuous is A2/B1, too easy for B2.2.
- reader 2: level: Past continuous is A2-B1; too easy for B2.2.

## r20b-3-019 · B2.1 · text · conjunctions-1.csv:81

Task: Correct the mistake: Despite of the delays, the project was finished on time.
Key: {"kind": "text", "accepted": [["Despite the delays, the project was finished on time.", "In spite of the delays, the project was finished on time."]]}
- reader 1: instruction: Does not say whether to keep 'despite'; 'In spite of' is also a correct fix.
- reader 1: sense: Same mistake as 030 and near-identical sentence.
- reader 2: another correct answer, not accepted: [['The project was finished on time despite the delays.'], ['The project was finished on time in spite of the delays.']]
- reader 2: sense: Near-duplicate of task 30 (Despite of the delay).

## r20b-3-022 · B2.1 · text · conjunctions-1.csv:106

Task: Correct the mistake. Keep *for*: These boxes are for store old documents.
Key: {"kind": "text", "accepted": [["These boxes are for storing old documents.", "These boxes are used for storing old documents."]]}
- reader 2: another correct answer, not accepted: [['These boxes are for the storing of old documents.'], ['These boxes are for storage of old documents.']]
- reader 2: sense: Near-duplicate pattern of task 20.

## r20b-3-023 · B2.2 · order · conjunctions-1.csv:111

Task: Put the words in order.
word_cards: loan | needs | the | bank | for | go | signature | order | the | your | to | in | through
Key: {"kind": "order", "sentence": "the bank needs your signature in order for the loan to go through", "also": ["in order for the loan to go through the bank needs your signature"]}
- reader 1: instruction: Two natural orders (clause first or last); no start given or hint.
- reader 2: another correct answer, not accepted: [['the bank needs your signature in order for the loan to go through']]
- reader 2: instruction: No hint about capital/comma or that two orders work.

## r20b-3-025 · B2.1 · order · learn-drag-3.csv:10

Task: Put the words in order.
word_cards: warm | up | coach | the | before | us | every | to | match | told
Key: {"kind": "order", "sentence": "the coach told us to warm up before every match", "also": ["before every match the coach told us to warm up"]}
- reader 1: another correct answer, not accepted: ['the coach told us before every match to warm up']
- reader 1: instruction: Adverbial can go first; no start given.
- reader 2: another correct answer, not accepted: [['before every match the coach told us to warm up'], ['the coach told us before every match to warm up']]
- reader 2: instruction: 'Before every match' can start the sentence; meaning shifts slightly.

## r20b-3-027 · B2.1 · order · learn-drag-4.csv:18

Task: Put the words in order.
word_cards: would | had | the | been | won | prepared | better | if | have | team | we
Key: {"kind": "order", "sentence": "if the team had been better prepared we would have won", "also": ["we would have won if the team had been better prepared", "if we had been better prepared the team would have won", "the team would have won if we had been better prepared"]}
- reader 1: another correct answer, not accepted: ['if the team had been prepared better we would have won', 'we would have won if the team had been prepared better', 'if we had won the team would have been better prepared', 'the team would have been better prepared if we had won']
- reader 1: instruction: Many orders; no start or hint.
- reader 1: sense: 'the team' and 'we' as two different groups is odd; swapping them also works.
- reader 2: another correct answer, not accepted: [['if we had been better prepared the team would have won'], ['if the team had been better prepared we would have won'], ['we would have won if the team had been better prepared']]
- reader 2: instruction: Both 'we' and 'the team' can be subject of either clause, so four orders work; no hint given.

## r20b-3-028 · B2.1 · order · learn-drag-4.csv:28

Task: Put the words in order.
word_cards: the | the | went | despite | ahead | strike | conference
Key: {"kind": "order", "sentence": "despite the strike the conference went ahead", "also": ["the conference went ahead despite the strike"]}
- reader 1: instruction: No start hint; two orders.
- reader 1: level: Very short and easy: only the position of 'despite'.
- reader 2: another correct answer, not accepted: [['despite the strike the conference went ahead'], ['the strike went ahead despite the conference'], ['despite the conference the strike went ahead']]
- reader 2: level: Only 7 simple words, too easy for B2.1.
- reader 2: sense: Other pairing 'strike went ahead despite the conference' is grammatical but odd.

## r20b-3-029 · B2.1 · order · learn-drag-4.csv:36

Task: Put all the words in order. More than one answer is possible.
word_cards: I | asked | her | help | could | if | she
Key: {"kind": "order", "sentence": "she asked if I could help her", "also": ["I asked her if she could help", "she asked her if I could help", "I asked if she could help her"]}
- reader 1: instruction: Says more than one answer is possible, fine; but 'her' as object of 'help' gives odd sentences.
- reader 2: another correct answer, not accepted: [['she asked her if i could help'], ['i asked if she could help her']]
- reader 2: instruction: 'More than one answer is possible' tells the learner to look for alternatives; the other orders are odd (different people).

## r20b-3-030 · B2.1 · text · twins-1.csv:34

Task: Correct the mistake: Despite of the delay, we arrived on time.
Key: {"kind": "text", "accepted": [["Despite the delay, we arrived on time.", "In spite of the delay, we arrived on time.", "We arrived on time despite the delay.", "We arrived on time in spite of the delay."]]}
- reader 1: instruction: Does not say whether to keep 'despite'.
- reader 1: sense: Duplicate of 019.
- reader 2: sense: Near-duplicate of task 19.

## r20b-3-031 · B2.2 · gap · twins-1.csv:49

Task: She stayed late and missed the last bus. If she ___ (not / stay) so late, she ___ (not / miss) the last bus.
Key: {"kind": "gap", "accepted": [["hadn't stayed"], ["wouldn't have missed", "might not have missed"]]}
- reader 2: another correct answer, not accepted: [["hadn't stayed", "'d not have missed"]]

## r20b-3-033 · B2.2 · text · twins-1.csv:62

Task: Start with *I'd rather you*: Please don't park in front of my garage.
Key: {"kind": "text", "accepted": [["I'd rather you didn't park in front of my garage.", "I would rather you didn't park in front of my garage.", "I'd rather you not park in front of my garage.", "I would rather you not park in front of my garage.", "I'd rather you parked somewhere else, not in front of my garage."]]}
- reader 1: another correct answer, not accepted: [["I'd rather you wouldn't park in front of my garage."], ["Please, I'd rather you didn't park in front of my garage."]]
- reader 1: instruction: Unclear whether 'please' must be kept.
- reader 2: another correct answer, not accepted: [["I'd rather you wouldn't park in front of my garage."], ["I'd rather you don't park in front of my garage."]]
- reader 2: sense: 'wouldn't' and 'don't' are less standard (informal/US) but heard.

## r20b-3-034 · B2.1 · gap · twins-2.csv:10

Task: Write one word in each gap: I did not take that course. If I ___ ___ it, I ___ ___ more about design now. (take / know)
Key: {"kind": "gap", "accepted": [["had", "'d"], ["taken"], ["would", "could", "might"], ["know"]]}
- reader 1: instruction: Gaps '(take / know)' order is clear, but 'would'/'might'/'could' all fit the second modal.
- reader 2: instruction: 'one word in each gap' with contraction 'd not clear; 'take' form (taken) not given.

## r20b-3-036 · B2.1 · gap · twins-2.csv:42

Task: By the time the bell rang, Eva ___ all ten questions, so she left early. (answer)
Key: {"kind": "gap", "accepted": [["had answered", "'d answered"]]}
- reader 1: sense: Near-duplicate of 017.
- reader 2: another correct answer, not accepted: [['answered']]
- reader 2: instruction: 'answered' (past simple with 'by the time') is possible, less natural.

## r20b-3-038 · B2.2 · text · twins-3.csv:15

Task: Report this. Start with *They asked*: 'What time should we arrive?'
Key: {"kind": "text", "accepted": [["They asked what time they should arrive.", "They asked what time to arrive.", "They asked what time we should arrive.", "They asked me what time they should arrive.", "They asked us what time we should arrive.", "They asked me what time to arrive.", "They asked us what time to arrive.", "They asked what time they ought to arrive.", "They asked what time they were to arrive."]]}
- reader 1: another correct answer, not accepted: [['They asked what time we were to arrive.'], ['They asked what time we would arrive.']]
- reader 1: instruction: Reference of 'we' is ambiguous (we/they).
- reader 2: another correct answer, not accepted: [['They asked what time we were to arrive.']]
- reader 2: instruction: Does not say who 'we' is, so 'we' and 'they' are both right.

## r20b-3-039 · B2.2 · mcq · twins-3.csv:22

Task: Which is correct? 'We weren't sure ___.'
options: where go | where should we go | where do we go | where to go
Key: {"kind": "mcq", "correct": "where to go", "wrong": ["where should we go", "where do we go", "where go"]}
- reader 2: level: B1 level, easy for B2.2.

## r20b-3-040 · B2.2 · mcq · twins-3.csv:26

Task: Choose the correct word: ___ called the help desk this morning didn't leave a name.
options: Whomever | Whoever | Whatever | Wherever
Key: {"kind": "mcq", "correct": "Whoever", "wrong": ["Whomever", "Whatever", "Wherever"]}
- reader 1: sense: Duplicate of 014.

## r20b-3-041 · B2.1 · gap · typical-b2c1-1.csv:4

Task: I ___ more if the gym were closer to my office. (exercise)
Key: {"kind": "gap", "accepted": [["would exercise", "'d exercise", "might exercise", "could exercise"]]}
- reader 1: level: Second conditional is B1, too easy for B2.1.
- reader 2: level: Second conditional is B1; easy for B2.1.

## r20b-3-042 · B2.1 · gap · typical-b2c1-1.csv:8

Task: 'I've lived here for two years.' She told me she ___ there for two years. (live)
Key: {"kind": "gap", "accepted": [["had lived", "had been living", "'d lived", "'d been living"]]}
- reader 1: another correct answer, not accepted: [['has lived']]
- reader 1: instruction: 'has lived' is correct if she still lives there; 'had been living' also fine.
- reader 2: another correct answer, not accepted: [['has lived']]
- reader 2: instruction: 'has lived' (no backshift, still true) is possible but marginal.

## r20b-3-043 · B2.1 · gap · typical-b2c1-1.csv:13

Task: ___ her knee injury, she finished the marathon.
word_cards: Even though | Despite | Although | Despite of
Key: {"kind": "gap", "accepted": [["Despite"]]}
- reader 2: level: B1 level.

## r20b-3-045 · B2.2 · gap · typical-b2c1-1.csv:21

Task: I'm not sure what time the meeting ___ . (start)
Key: {"kind": "gap", "accepted": [["starts", "will start", "is going to start", "is starting"]]}
- reader 1: another correct answer, not accepted: [['started'], ['is to start']]
- reader 1: instruction: Context gives no time frame: past 'started' also fits; 'will start' is natural.
- reader 1: level: Indirect question is B1, too easy for B2.2.
- reader 2: another correct answer, not accepted: [['started'], ['is to start']]
- reader 2: instruction: No context (schedule or past), so several tenses fit; 'started' changes meaning.
- reader 2: level: Indirect question is B1; easy for B2.2.

## r20b-3-046 · B2.2 · gap · typical-b2c1-1.csv:24

Task: If I ___ allergic to cats, I would have stayed at Anna's place last weekend. (not / be)
Key: {"kind": "gap", "accepted": [["weren't", "wasn't", "were not", "was not", "hadn't been", "had not been"]]}
- reader 1: instruction: Both 'weren't' (mixed) and 'hadn't been' (third conditional) are correct English here.

## r20b-3-047 · B2.2 · gap · typical-b2c1-1.csv:29

Task: We'll start at nine unless the speaker ___ late. (be)
Key: {"kind": "gap", "accepted": [["is", "'s"]]}
- reader 1: level: First conditional with 'unless' is B1, too easy for B2.2.
- reader 2: level: First conditional/unless is B1; easy for B2.2.

## r20b-3-048 · B2.2 · gap · typical-b2c1-1.csv:32

Task: In future, I'd rather you ___ my phone without asking. (not / use)
Key: {"kind": "gap", "accepted": [["didn't use", "did not use"]]}
- reader 1: another correct answer, not accepted: [["wouldn't use"], ["don't use"], ['not use']]
- reader 1: instruction: 'don't use' informal; 'not use' American subjunctive.
- reader 2: another correct answer, not accepted: [["wouldn't use"], ['would not use'], ["don't use"]]
- reader 2: sense: 'wouldn't' and 'don't' are less standard.

## r20b-3-049 · B2.2 · gap · typical-b2c1-1.csv:36

Task: If it ___ for your advice, I would never have applied. (not / be)
Key: {"kind": "gap", "accepted": [["hadn't been", "had not been", "weren't", "were not", "wasn't", "was not"]]}
- reader 1: instruction: 'weren't' is less standard here but sometimes used.

## r20b-3-050 · B2.2 · gap · typical-b2c1-1.csv:39

Task: ___ wins the competition will get a trip to Lisbon. (who)
Key: {"kind": "gap", "accepted": [["Whoever", "Anyone who", "Anybody who", "The person who", "Everyone who"]]}
- reader 1: another correct answer, not accepted: [['Those who']]
- reader 1: instruction: Hint '(who)' is unclear: it does not say to add -ever; other phrases with 'who' fit.
- reader 2: instruction: '(who)' gives away the word; other answers 'Anyone who' fit.

## r20b-3-051 · B2.2 · gap · unreal-time-1.csv:3

Task: It's high time we ___ the tickets. The concert is next week.
word_cards: have booked | will book | had booked | booked
Key: {"kind": "gap", "accepted": [["booked"]]}
- reader 2: a wrong option that fits: 'had booked' is marginal, rare after 'high time'.

