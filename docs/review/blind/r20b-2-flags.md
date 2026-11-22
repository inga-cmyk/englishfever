# Blind check r20b-2: flags for the judge

53 tasks, 2 readers.

## r20b-2-002 · B2.1 · mcq · built-in

Task: Which sentence is correct?
options: If you would tell us earlier, we could have adjusted the schedule. | If you had told us earlier, we could have adjusted the schedule. | If you had told us earlier, we could have adjust the schedule. | If you told us earlier, we could have adjusted the schedule.
Key: {"kind": "mcq", "correct": "If you had told us earlier, we could have adjusted the schedule.", "wrong": ["If you told us earlier, we could have adjusted the schedule.", "If you had told us earlier, we could have adjust the schedule.", "If you would tell us earlier, we could have adjusted the schedule."]}
- reader 2: sense: Option C ('could have adjust') is a typo-type slip, not a believable learner mistake.

## r20b-2-003 · B2.2 · mcq · built-in

Task: Which sentence is NOT correct?
options: If I'd have known about the traffic, I would've left earlier. | Had we checked the forecast, we wouldn't have gone sailing. | If she'd asked me, I'd have helped her. | They wouldn't have got lost if they had taken a map.
Key: {"kind": "mcq", "correct": "If I'd have known about the traffic, I would've left earlier.", "wrong": ["Had we checked the forecast, we wouldn't have gone sailing.", "If she'd asked me, I'd have helped her.", "They wouldn't have got lost if they had taken a map."]}
- reader 1: sense: Option A ('If I'd have known') is a common native-speaker form, so some learners may hear it as fine; defensible as a B2.2 mistake but the task should say it is about standard written English.
- reader 2: sense: 'If I'd have known' is common in speech; 'NOT correct' is fine but learners may doubt it. Okay.

## r20b-2-004 · B2.1 · mcq · built-in

Task: Which sentence is correct?
options: If I didn't stay up so late, I wouldn't have been so tired now. | If I hadn't stayed up so late, I wouldn't be so tired now. | If I wouldn't have stayed up so late, I wouldn't be so tired now. | If I hadn't stayed up so late, I wouldn't have been so tired now.
Key: {"kind": "mcq", "correct": "If I hadn't stayed up so late, I wouldn't be so tired now.", "wrong": ["If I didn't stay up so late, I wouldn't have been so tired now.", "If I hadn't stayed up so late, I wouldn't have been so tired now.", "If I wouldn't have stayed up so late, I wouldn't be so tired now."]}
- reader 2: sense: Option A is an odd mixture nobody writes.

## r20b-2-005 · B2.2 · mcq · built-in

Task: A colleague says: 'If I had a better memory, I would have remembered your birthday.' What does the sentence say?
options: It is a general fact that is always true. | Both parts are about the past. | A quality now caused a result in the past. | Both parts are about the future.
Key: {"kind": "mcq", "correct": "A quality now caused a result in the past.", "wrong": ["Both parts are about the past.", "Both parts are about the future.", "It is a general fact that is always true."]}
- reader 1: instruction: Options are abstract and wordy ('A quality now caused a result in the past'); a learner may not parse them. 'a better memory' is a general trait, not clearly 'now'.
- reader 1: sense: The model sentence is odd: 'If I had a better memory, I would have remembered' is a weak mixed conditional; adult-natural but borderline.
- reader 2: a wrong option that fits: Option B (both parts about the past) fits loosely: 'had a better memory' could be read as past.
- reader 2: instruction: Options are abstract and clumsy ('A quality now caused a result'); a B2 learner may not follow. The sentence is odd: 'If I had a better memory' is a general trait.
- reader 2: sense: Meta-linguistic question, not a grammar-use task.

## r20b-2-006 · B2.2 · mcq · built-in

Task: Which sentence has a mistake?
options: If only I had a bit more free time now. | If only I would have saved more money. | If only you had told me about it earlier. | I wish I had chosen a different course at university.
Key: {"kind": "mcq", "correct": "If only I would have saved more money.", "wrong": ["I wish I had chosen a different course at university.", "If only I had a bit more free time now.", "If only you had told me about it earlier."]}
- reader 1: sense: Mistake is believable (would have after if only).

## r20b-2-008 · B2.2 · gap · built-in

Task: 'Where should we meet?' → They asked me ___.
Key: {"kind": "gap", "accepted": [["where they should meet", "where we should meet", "where to meet", "where we were to meet", "where they were to meet"]]}
- reader 1: another correct answer, not accepted: [['where we ought to meet'], ['where we would meet']]
- reader 1: instruction: Unclear how many words to type and whether to start with 'where' (already printed in the quote only). Many correct answers: should/ought to/were to/would, 'they' vs 'we' (pronoun ambiguity), and 'where to meet'. A typed key will miss some.
- reader 2: another correct answer, not accepted: [['where we would meet']]
- reader 2: instruction: 'We' is ambiguous after 'They asked me': 'where to meet' and 'where they should meet' also fit; the learner cannot know which is expected.

## r20b-2-011 · B2.2 · mcq · built-in

Task: Which sentence reports this: 'I'm very sorry for the delay, and I will make sure it never happens again.'
options: The manager apologised the delay and promised that it would not happen again. | The manager apologised for the delay and promised it not to happen again. | The manager apologised for the delay and promised that it would not happen again.
Key: {"kind": "mcq", "correct": "The manager apologised for the delay and promised that it would not happen again.", "wrong": ["The manager apologised the delay and promised that it would not happen again.", "The manager apologised for the delay and promised it not to happen again."]}
- reader 1: instruction: Only three options, others obviously fail; fine.

## r20b-2-012 · B2.2 · mcq · built-in

Task: Which is correct? 'The instructions don't explain ___ the new printer.'
options: how should we set up | how set up | how to set up
Key: {"kind": "mcq", "correct": "how to set up", "wrong": ["how should we set up", "how set up"]}
- reader 2: a wrong option that fits: 'how should we set up' is not correct (direct-question order); none fit.

## r20b-2-013 · B2.2 · mcq · built-in

Task: The decision depends on ___ the budget is approved.
options: if | that | what | whether
Key: {"kind": "mcq", "correct": "whether", "wrong": ["if", "that", "what"]}
- reader 1: a wrong option that fits: 'if' is accepted by many speakers after 'depends on' in informal English ('depends on if'), though 'whether' is the standard form.
- reader 1: instruction: The learner may argue 'if' is also correct; consider adding 'or not' or a different frame.
- reader 2: a wrong option that fits: 'if' is used after 'depends on' informally and is accepted by many speakers.
- reader 2: instruction: Two options fit (whether; informal if).

## r20b-2-015 · B2.2 · mcq · built-in

Task: Which sentence is NOT correct?
options: Whomever wins the contract will celebrate. | Whatever you decide, I'll support you. | You can sit wherever you like. | I'll talk to whoever is at the front desk.
Key: {"kind": "mcq", "correct": "Whomever wins the contract will celebrate.", "wrong": ["Whatever you decide, I'll support you.", "You can sit wherever you like.", "I'll talk to whoever is at the front desk."]}
- reader 1: sense: Overlaps with 041 (same whoever/whomever idea); 'whomever' is a trap many learners (and natives) overuse, acceptable but rule is formal.
- reader 2: sense: Near-duplicate of task 041 (whomever as subject).

## r20b-2-016 · B2.1 · mcq · compare-past-1.csv:47

Task: Choose the correct option: Her feet were sore. She ___ around the city all day.
options: had been walk | had been walking | has been walking
Key: {"kind": "mcq", "correct": "had been walking", "wrong": ["has been walking", "had been walk"]}
- reader 1: a wrong option that fits: 'has been walking' does not fit the past 'were sore' (not a good fit); none.
- reader 2: sense: 'had been walk' is a typo-type distractor.

## r20b-2-017 · B2.1 · gap · compare-past-1.csv:51

Task: Anna's hands were dirty when she came in. She ___ in the garden all afternoon. (work)
Key: {"kind": "gap", "accepted": [["had been working", "'d been working", "had worked", "'d worked"]]}
- reader 1: another correct answer, not accepted: [['was working']]
- reader 1: instruction: 'was working' and 'had worked' are also correct English here; only 'had been working' is clearly best (less natural variants).
- reader 2: another correct answer, not accepted: [['was working']]
- reader 2: instruction: 'Her hands were dirty' + all afternoon: 'had worked' and 'was working' also correct.

## r20b-2-019 · B2.2 · order · compare-past-1.csv:61

Task: Put all the words in order. More than one answer is possible.
word_cards: she | been | she | had | years | left | there | ten | when | working | for
Key: {"kind": "order", "sentence": "she had been working there for ten years when she left", "also": ["when she left she had been working there for ten years", "she left when she had been working there for ten years", "when she had been working there for ten years she left"]}
- reader 1: another correct answer, not accepted: ['she had been working for ten years there when she left (less natural)']
- reader 2: another correct answer, not accepted: ['when she left there, she had been working for ten years', 'she had been working for ten years there when she left']

## r20b-2-020 · B2.1 · mcq · conjunctions-1.csv:89

Task: Choose the correct option: The concert was cancelled ___ the singer's illness.
options: as a result | owing | on account | owing to
Key: {"kind": "mcq", "correct": "owing to", "wrong": ["owing", "on account", "as a result"]}
- reader 1: instruction: Distractors 'owing' and 'on account' are fragments of the same phrase, not real alternatives; easy for B2.1.
- reader 2: sense: Options 'owing' and 'on account' are incomplete fragments, weak distractors.

## r20b-2-022 · B2.1 · text · conjunctions-1.csv:105

Task: Correct the mistake: Save a copy on a USB stick in case your laptop will crash.
Key: {"kind": "text", "accepted": [["Save a copy on a USB stick in case your laptop crashes.", "Save a copy on a USB stick in case your laptop should crash."]]}
- reader 1: another correct answer, not accepted: ['Save a copy on a USB stick in case your laptop were to crash.', 'Save a copy on a USB stick in case your laptop does crash.']
- reader 1: instruction: Several corrections possible (crashes, should crash, were to crash); a typed key must accept them.
- reader 2: another correct answer, not accepted: ['Save a copy on a USB stick in case your laptop does crash.']

## r20b-2-023 · B2.2 · gap · conjunctions-1.csv:108

Task: The company lost its biggest client. ___, it had to cut twenty jobs.
word_cards: Therefore | Whereas | Owing to | On account of
Key: {"kind": "gap", "accepted": [["Therefore"]]}
- reader 1: instruction: Easy for B2.2: the two preposition cards need a noun and 'Whereas' is not causal, so only 'Therefore' fits at a glance.

## r20b-2-024 · B2.2 · gap · iq-b1-6.csv:33

Task: The hotel wants to know ___ to expect us before ten, and ___ we're late, they'll keep the room for us until midnight.
word_cards: if | whether | what
Key: {"kind": "gap", "accepted": [["whether"], ["if"]]}
- reader 1: instruction: Second gap: 'whether we're late' without 'or not' is marginal; 'if' is the natural choice. First gap: 'if to expect' is wrong. Third card 'what' is a trivial distractor.
- reader 1: sense: 'know whether to expect us before ten' is slightly awkward.
- reader 2: a wrong option that fits: 'whether' in gap 2 is possible but incomplete without 'or not' (less natural). 'if' in gap 1 does not fit ('if to expect' is wrong).
- reader 2: instruction: No hint of the infinitive, so the difference rests on 'whether to'; OK.

## r20b-2-025 · B2.2 · order · learn-drag-3.csv:8

Task: Put the words in order.
word_cards: train | not | had | be | here | missed | already | she | the | she | would
Key: {"kind": "order", "sentence": "had she not missed the train she would be here already", "also": ["she would be here already had she not missed the train", "had she not missed the train she would already be here", "she would already be here had she not missed the train"]}
- reader 1: another correct answer, not accepted: ['she would not be here already had she missed the train', 'had she missed the train, she would not be here already']
- reader 1: instruction: No 'More than one answer is possible' note although several correct orders exist; inversion without 'if' also hard to infer.

## r20b-2-026 · B2.1 · order · learn-drag-3.csv:13

Task: Put the words in order.
word_cards: need | the | I | a | visa | might | said | agent
Key: {"kind": "order", "sentence": "the agent said I might need a visa", "also": ["I said the agent might need a visa"]}
- reader 1: instruction: Two correct sentences (agent/I swap); too easy for B2.1 (8 cards).
- reader 2: another correct answer, not accepted: ['I might need a visa, the agent said', 'the agent might need a visa, I said']
- reader 2: instruction: Only one real choice of order; the sentence is too easy for B2.1.
- reader 2: level: Too easy for B2.1 (short, simple reported speech).

## r20b-2-027 · B2.1 · order · learn-drag-4.csv:14

Task: Put the words in order.
word_cards: the | I | tell | I | answer | knew | if | would | you
Key: {"kind": "order", "sentence": "if I knew the answer I would tell you", "also": ["I would tell you if I knew the answer", "I would tell you the answer if I knew", "if I knew I would tell you the answer"]}
- reader 1: instruction: Many correct orders but no note saying more than one answer is possible.
- reader 2: level: Second conditional is B1, low for B2.1.

## r20b-2-028 · B2.2 · order · learn-drag-4.csv:25

Task: Put the words in order.
word_cards: have | we | known | problem | you | would | had | if | called | about | the | we
Key: {"kind": "order", "sentence": "if we had known about the problem we would have called you", "also": ["we would have called you if we had known about the problem", "if we had called you we would have known about the problem", "we would have known about the problem if we had called you"]}
- reader 1: answer not accepted: we would have known about the problem if you had called
- reader 1: another correct answer, not accepted: ['if you had called we would have known about the problem', 'if you had called about the problem we would have known', 'we would have known if you had called about the problem']
- reader 1: instruction: Many correct orders (including a different sentence with 'we had known ... we would have called you'); no note about multiple answers.
- reader 2: answer not accepted: we would have known about the problem if you had called
- reader 2: another correct answer, not accepted: ['if you had called we would have known about the problem', 'we would have known if you had called about the problem', 'if you had called about the problem we would have known']
- reader 2: instruction: Instruction does not say more than one answer is possible although several exist.

## r20b-2-029 · B2.1 · order · learn-drag-4.csv:31

Task: Put the words in order to make a question.
word_cards: telling | take | repair | how | you | the | will | would | me | long | mind
Key: {"kind": "order", "sentence": "would you mind telling me how long the repair will take", "also": []}
- reader 1: another correct answer, not accepted: ['will you mind telling me how long the repair would take (wrong/unnatural)']
- reader 1: instruction: Grammar fine; 'Put in order to make a question' fits.
- reader 2: instruction: Instruction 'to make a question' fine; 'mind' and 'telling' cards give the frame away, acceptable.

## r20b-2-032 · B2.2 · text · twins-1.csv:54

Task: Rewrite starting with *Were*: If the price were lower, more people would buy it.
Key: {"kind": "text", "accepted": [["Were the price lower, more people would buy it.", "Were the price lower, more people would buy the product.", "Were the price to be lower, more people would buy it."]]}
- reader 1: another correct answer, not accepted: ['More people would buy it were the price lower.']
- reader 1: instruction: Starting word is given and the rest is mostly copying.

## r20b-2-035 · B2.2 · mcq · twins-2.csv:17

Task: Choose the correct option: The question is ___.
options: whether is the supplier able to meet the deadline | whether the supplier can meet the deadline | whether can the supplier meet the deadline | if can the supplier meet the deadline
Key: {"kind": "mcq", "correct": "whether the supplier can meet the deadline", "wrong": ["whether can the supplier meet the deadline", "if can the supplier meet the deadline", "whether is the supplier able to meet the deadline"]}
- reader 1: instruction: Near duplicate of 014 (same frame 'The question is ___').
- reader 2: sense: Near-duplicate of task 014.

## r20b-2-036 · B2.1 · order · twins-2.csv:40

Task: Put the words in order.
word_cards: storm | we | hours | when | been | hiking | began | the | for | had
Key: {"kind": "order", "sentence": "we had been hiking for hours when the storm began", "also": ["when the storm began we had been hiking for hours", "the storm began when we had been hiking for hours", "when we had been hiking for hours the storm began", "for hours we had been hiking when the storm began"]}
- reader 1: instruction: Several orders correct; no note about it.

## r20b-2-037 · B2.2 · mcq · twins-3.csv:8

Task: Which sentence is NOT correct?
options: Had he trained harder, he would be in the team now. | Hadn't she missed the train, she'd be here now. | If she weren't so shy, she would have spoken up at the meeting. | Had they not moved, they would live next door now.
Key: {"kind": "mcq", "correct": "Hadn't she missed the train, she'd be here now.", "wrong": ["Had he trained harder, he would be in the team now.", "If she weren't so shy, she would have spoken up at the meeting.", "Had they not moved, they would live next door now."]}
- reader 1: sense: Option B is a form hardly any learner writes ('Hadn't she'); the mistake is somewhat exotic. Option C is a correct mixed conditional that some may wrongly mark.
- reader 2: sense: Option B ('Hadn't she missed') is a form hardly any learner writes; wrong answer more likely guessed than noticed.

## r20b-2-038 · B2.2 · mcq · twins-3.csv:14

Task: Which sentence is correct?
options: She asked me how do I start. | She asked to me how to start. | She asked me how should she start. | She asked me how to start.
Key: {"kind": "mcq", "correct": "She asked me how to start.", "wrong": ["She asked me how should she start.", "She asked me how do I start.", "She asked to me how to start."]}
- reader 1: sense: Option 'asked to me' is a random preposition error, not a very believable one.

## r20b-2-039 · B2.2 · mcq · twins-3.csv:21

Task: Which sentence reports the client's complaint: 'The delivery was three days late.'
options: The client complained that the delivery has been three days late. | The client complained me that the delivery had been three days late. | The client complained that the delivery had been three days late. | The client complained that the delivery had be three days late.
Key: {"kind": "mcq", "correct": "The client complained that the delivery had been three days late.", "wrong": ["The client complained that the delivery has been three days late.", "The client complained that the delivery had be three days late.", "The client complained me that the delivery had been three days late."]}
- reader 2: sense: 'had be' is a typo-type distractor.

## r20b-2-040 · B2.2 · mcq · twins-3.csv:25

Task: Choose the correct option.
options: It remains unclear how we will pay for the repairs. | It remains unclear how will we pay for the repairs. | It remains unclear how are we going to pay for the repairs. | It remains unclear how do we pay for the repairs.
Key: {"kind": "mcq", "correct": "It remains unclear how we will pay for the repairs.", "wrong": ["It remains unclear how will we pay for the repairs.", "It remains unclear how are we going to pay for the repairs.", "It remains unclear how do we pay for the repairs."]}
- reader 1: sense: Wrong options are believable.

## r20b-2-041 · B2.2 · mcq · twins-3.csv:28

Task: Which sentence is NOT correct?
options: Wherever you go, call me first. | Invite whoever you like to the party. | Whatever happens, stay calm. | Whomever gets home first should start dinner.
Key: {"kind": "mcq", "correct": "Whomever gets home first should start dinner.", "wrong": ["Invite whoever you like to the party.", "Whatever happens, stay calm.", "Wherever you go, call me first."]}
- reader 1: a wrong option that fits: Option B 'Invite whoever you like' is accepted in everyday English (formal 'whomever'); a pedantic learner may mark it wrong.
- reader 1: instruction: Overlaps with 015.
- reader 2: sense: Near-duplicate of task 015.

## r20b-2-042 · B2.1 · gap · typical-b2c1-1.csv:7

Task: 'I'll send the report tomorrow.' Tom said he ___ the report the next day. (send)
Key: {"kind": "gap", "accepted": [["would send", "'d send"]]}
- reader 1: another correct answer, not accepted: [['was going to send']]
- reader 2: another correct answer, not accepted: [['was going to send']]

## r20b-2-043 · B2.1 · gap · typical-b2c1-1.csv:12

Task: When I finally got through, I ___ on hold for forty minutes. (wait)
Key: {"kind": "gap", "accepted": [["had been waiting", "'d been waiting", "had waited", "'d waited"]]}
- reader 1: instruction: 'had waited' is also correct; only 'had been waiting' stresses duration.

## r20b-2-044 · B2.1 · gap · typical-b2c1-1.csv:15

Task: I'll leave you my number in case you ___ any problems with the flat. (have)
Key: {"kind": "gap", "accepted": [["have", "should have"]]}
- reader 1: another correct answer, not accepted: [['had'], ['happen to have'], ['do have'], ['are having'], ["'re having"]]
- reader 1: instruction: Several forms fit ('in case you had' is less natural in this context); typed key must accept variants.
- reader 2: another correct answer, not accepted: [['happen to have'], ['had']]
- reader 2: instruction: 'had' (in case you had) is a less natural alternative.

## r20b-2-045 · B2.2 · gap · typical-b2c1-1.csv:20

Task: Our guide suggested ___ the museum early to avoid the queues. (visit)
Key: {"kind": "gap", "accepted": [["visiting", "that we visit", "we visit", "that we should visit", "we should visit", "that we visited", "we visited"]]}
- reader 1: another correct answer, not accepted: [['our visiting']]
- reader 1: instruction: The gap can hold a whole clause as well as -ing; the verb hint '(visit)' does not say which.
- reader 2: another correct answer, not accepted: [['going to visit']]
- reader 2: instruction: The gap can hold a clause ('that we visit'), not only the -ing form.

## r20b-2-047 · B2.2 · gap · typical-b2c1-1.csv:27

Task: I wish I ___ closer to my office; the commute takes hours. (live)
Key: {"kind": "gap", "accepted": [["lived", "could live", "was living", "were living"]]}
- reader 1: instruction: 'could live' and 'were living' are also correct with '(live)'.
- reader 2: instruction: 'could live' is not from the given verb form but correct.

## r20b-2-048 · B2.2 · gap · typical-b2c1-1.csv:31

Task: It's high time the government ___ something about housing. (do)
Key: {"kind": "gap", "accepted": [["did", "was doing"]]}
- reader 1: another correct answer, not accepted: [['should do'], ['were to do']]
- reader 1: instruction: 'should do' is also correct (less common).
- reader 2: another correct answer, not accepted: [['should do'], ['were to do']]
- reader 2: instruction: 'should do' is formal and rare.

## r20b-2-049 · B2.2 · gap · typical-b2c1-1.csv:34

Task: We couldn't decide where ___ on holiday. (go)
Key: {"kind": "gap", "accepted": [["to go", "we should go", "we could go", "we would go", "we'd go", "we were going to go"]]}
- reader 1: another correct answer, not accepted: [['we ought to go'], ['we were going']]
- reader 1: instruction: Open gap: many clauses fit; should say 'one word' or give a frame.
- reader 2: instruction: Not clear whether a to-infinitive or a clause is wanted.

## r20b-2-050 · B2.2 · gap · typical-b2c1-1.csv:38

Task: They accused the company ___ the data of its users. (sell)
Key: {"kind": "gap", "accepted": [["of selling", "of having sold"]]}
- reader 1: instruction: Gap includes the preposition 'of', which the learner must supply; instruction doesn't say so.

## r20b-2-052 · B2.2 · text · unreal-time-1.csv:5

Task: Write one sentence that starts with *It's high time*: You should really start looking for a new job.
Key: {"kind": "text", "accepted": [["It's high time you started looking for a new job.", "It's high time you started to look for a new job.", "It's high time you looked for a new job.", "It is high time you started looking for a new job.", "It is high time you started to look for a new job.", "It is high time you looked for a new job.", "It's high time you began looking for a new job.", "It is high time you began looking for a new job.", "It's high time that you started looking for a new job.", "It is high time that you started looking for a new job.", "It's high time you were looking for a new job.", "It is high time you were looking for a new job.", "It's high time you started job-hunting.", "It is high time you started job-hunting.", "It's high time for you to start looking for a new job.", "It is high time for you to start looking for a new job."]]}
- reader 1: another correct answer, not accepted: ["It's high time you started looking for a job.", "It's high time to start looking for a new job."]
- reader 1: instruction: Many answers; a typed key must be tolerant.
- reader 2: another correct answer, not accepted: ["It's high time you start looking for a new job."]
- reader 2: instruction: Many correct answers; unclear if 'you' is required.

## r20b-2-053 · B2.2 · text · unreal-time-1.csv:10

Task: Write one sentence that starts with *I'd rather you*: Please don't bring your dog to the office.
Key: {"kind": "text", "accepted": [["I'd rather you didn't bring your dog to the office.", "I would rather you didn't bring your dog to the office.", "I'd rather you not bring your dog to the office.", "I would rather you not bring your dog to the office.", "I'd rather you didn't bring your dog into the office.", "I would rather you didn't bring your dog into the office.", "I'd rather you didn't bring your dog to work.", "I would rather you didn't bring your dog to work.", "I'd rather you left your dog at home.", "I would rather you left your dog at home.", "I'd rather you kept your dog at home.", "I would rather you kept your dog at home."]]}
- reader 1: another correct answer, not accepted: ["I'd rather you wouldn't bring your dog to the office."]
- reader 1: instruction: Many variants including American subjunctive; 'Please' dropped.

