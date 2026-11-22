# Blind check r20-1: flags for the judge

60 tasks, 2 readers.

## r20-1-001 · B2.1 · mcq · built-in

Task: Which is correct? 'If I ___ you, I'd think twice about that offer.'
options: am | would be | had been | were
Key: {"kind": "mcq", "correct": "were", "wrong": ["am", "would be", "had been"]}
- reader 1: level: Second conditional with 'If I were you' is A2/B1, too easy for B2.1.
- reader 2: level: Second conditional with 'were' is B1 at most; too easy for B2.1.
- reader 2: sense: 'am' is a believable mistake. ('was' would be fine informally but is not offered.)

## r20-1-002 · B2.1 · mcq · built-in

Task: What is the difference? A: 'If I had time, I would help.' B: 'If I had time, I might help.'
options: They mean the same. | B is less certain than A. | A is past, B is future. | A is less certain than B.
Key: {"kind": "mcq", "correct": "B is less certain than A.", "wrong": ["A is less certain than B.", "A is past, B is future.", "They mean the same."]}
- reader 1: level: Too easy/basic for B2.1 (would vs might).

## r20-1-003 · B2.1 · gap · built-in

Task: Our company will never change its fixed hours. If it ___ more flexible hours, people ___ happier. (offer / be)
Key: {"kind": "gap", "accepted": [["offered", "were to offer"], ["would be", "'d be"]]}
- reader 1: another correct answer, not accepted: [['offered', 'might be']]
- reader 1: instruction: Given verbs (offer / be) plus the 'will never change' context make the second conditional obvious; ok, but 'might/could be' also fit, so key must accept them.
- reader 2: another correct answer, not accepted: [['offered', 'might be']]
- reader 2: instruction: 'will never change' is useful context but the verbs are given in brackets; gap 2 accepts might/could be too, so answer is not unique.

## r20-1-004 · B2.1 · mcq · built-in

Task: Which sentence has a mistake?
options: If I would know the answer, I would tell you. | If I knew the answer, I would tell you. | If I knew the answer, I'd tell you. | I would tell you if I knew the answer.
Key: {"kind": "mcq", "correct": "If I would know the answer, I would tell you.", "wrong": ["If I knew the answer, I would tell you.", "If I knew the answer, I'd tell you.", "I would tell you if I knew the answer."]}
- reader 1: level: B1 grammar at B2.1.
- reader 2: level: Basic second conditional, B1; too easy for B2.1.

## r20-1-005 · B2.1 · mcq · built-in

Task: Which sentence is correct?
options: I would be grateful if you will send me the report by Friday. | I would be grateful if you could send me the report by Friday. | I would be grateful if you could to send me the report by Friday. | I would grateful if you could send me the report by Friday.
Key: {"kind": "mcq", "correct": "I would be grateful if you could send me the report by Friday.", "wrong": ["I would be grateful if you will send me the report by Friday.", "I would grateful if you could send me the report by Friday.", "I would be grateful if you could to send me the report by Friday."]}
- reader 1: level: Easy for B2.1.
- reader 1: sense: 'if you will send' is wrong here but 'if you will' (polite, 'if you will be so kind') exists; fine.
- reader 2: a wrong option that fits: Option 1 ('if you will send') is awkward/non-standard but some formal writers accept 'if you will'; arguably also fits.

## r20-1-006 · B2.1 · write · built-in

Task: A colleague works 12 hours a day. Give them advice in one sentence, from your own point of view.
Key: {"kind": "write", "model": "If I were you, I would switch off my phone after seven.", "must": ["Advice from your point of view: *If I were you, …*", "Then: *I would …*"]}
- reader 1: instruction: Does not say which form to use; a learner may write 'You should/must...' (correct advice) and fail the form check. 'from your own point of view' is unclear.
- reader 2: instruction: 'the app checks that some forms are used' is not stated to the learner; learner does not know which form is required (second conditional/advice).

## r20-1-007 · B2.1 · mcq · built-in

Task: Choose the correct form: She would have passed the exam if she ___ harder.
options: has studied | studied | had studied | would study
Key: {"kind": "mcq", "correct": "had studied", "wrong": ["studied", "would study", "has studied"]}
- reader 1: level: Basic third conditional, B1 not B2.1.

## r20-1-008 · B2.1 · mcq · built-in

Task: 'If he hadn't been so rude, we might have signed the deal.' What does 'might have' show?
options: The deal was impossible from the start. | The deal was possible, not certain. | The deal was signed in the end. | The deal was certain, not possible.
Key: {"kind": "mcq", "correct": "The deal was possible, not certain.", "wrong": ["The deal was certain, not possible.", "The deal was impossible from the start.", "The deal was signed in the end."]}
- reader 2: sense: Option 4 'certain, not possible' is self-contradictory, a weak distractor.

## r20-1-009 · B2.1 · mcq · built-in

Task: Which sentence has a mistake?
options: If the team hadn't been so tired, we might have won. | If the team has been better prepared, we would have won. | If the team had been better prepared, we would have won. | We would have won if the team had been better prepared.
Key: {"kind": "mcq", "correct": "If the team has been better prepared, we would have won.", "wrong": ["If the team had been better prepared, we would have won.", "We would have won if the team had been better prepared.", "If the team hadn't been so tired, we might have won."]}
- reader 1: sense: 'has been' for 'had been' is a believable slip.

## r20-1-010 · B2.1 · mcq · built-in

Task: Which sentence is correct?
options: If you had told us earlier, we could have adjusted the schedule. | If you had told us earlier, we could adjust have the schedule. | If you told us earlier, we could have adjusted the schedule. | If you would tell us earlier, we could have adjusted the schedule.
Key: {"kind": "mcq", "correct": "If you had told us earlier, we could have adjusted the schedule.", "wrong": ["If you told us earlier, we could have adjusted the schedule.", "If you had told us earlier, we could adjust have the schedule.", "If you would tell us earlier, we could have adjusted the schedule."]}
- reader 2: sense: Option 2 is a word-order slip nobody makes at B2; weak distractor.

## r20-1-011 · B2.1 · write · built-in

Task: Write one sentence about a decision that changed your life: imagine you had not made it.
Key: {"kind": "write", "model": "If I hadn't joined that course, I wouldn't have met my best friend.", "must": ["The decision you did not make: *If I hadn't …*", "The result: *would have* + 3rd form."]}
- reader 1: instruction: Unclear which structure is wanted (past/mixed); fine as open task.
- reader 2: instruction: Not stated which grammar is needed; the instruction should name the situation form (e.g. third conditional) or learner may write other tenses.

## r20-1-012 · B2.2 · mcq · built-in

Task: Imagine the past was different: 'If she ___ the warning, she ___ the accident.'
options: had heard / would avoid | heard / would avoid | had heard / would have avoided | would have heard / had avoided
Key: {"kind": "mcq", "correct": "had heard / would have avoided", "wrong": ["heard / would avoid", "had heard / would avoid", "would have heard / had avoided"]}
- reader 1: instruction: 'Imagine the past was different' gives the third conditional away.
- reader 1: level: Basic third conditional for B2.2.
- reader 2: sense: Options 1 and 4 fine as distractors.

## r20-1-013 · B2.2 · mcq · built-in

Task: What is the difference? A: 'If you had asked, I would have helped.' B: 'If you asked, I would help.'
options: There is no difference in meaning. | A is about the future, B the past. | A is about the past, B about now. | A is about now, B about the past.
Key: {"kind": "mcq", "correct": "A is about the past, B about now.", "wrong": ["A is about now, B about the past.", "A is about the future, B the past.", "There is no difference in meaning."]}
- reader 1: level: Easy for B2.2 (B1 contrast).
- reader 1: sense: Option 'A is about the future, B the past' is not a believable wrong option, it is just reversed.
- reader 2: a wrong option that fits: Option 3 only; but B ('If you asked, I would help') can also refer to the future, so 'about now' is imprecise.
- reader 2: sense: Imprecise: B is present/future hypothetical.

## r20-1-014 · B2.2 · gap · built-in

Task: He drove too fast just once and lost his licence. If he ___ (not / drive) so fast that day, he ___ (not / lose) it.
Key: {"kind": "gap", "accepted": [["hadn't been driving", "had not been driving", "hadn't driven", "had not driven"], ["wouldn't have lost", "would not have lost", "'d not have lost"]]}
- reader 1: another correct answer, not accepted: [["hadn't driven", 'might not have lost']]
- reader 1: instruction: 'just once' and 'that day' give the third conditional away; (not / drive) is given so only a plain third conditional is needed: easy for B2.2.
- reader 1: level: Too easy for B2.2.
- reader 2: instruction: 'just once' and 'that day' are redundant; verbs are given in brackets already, so answer is mechanical.

## r20-1-015 · B2.2 · mcq · built-in

Task: Which sentence is NOT correct?
options: If I'd known about the traffic, I would've left earlier. | If I had known about the traffic, I would have left earlier. | Had I known about the traffic, I would have left earlier. | If I'd have known about the traffic, I would've left earlier.
Key: {"kind": "mcq", "correct": "If I'd have known about the traffic, I would've left earlier.", "wrong": ["If I'd known about the traffic, I would've left earlier.", "If I had known about the traffic, I would have left earlier.", "Had I known about the traffic, I would have left earlier."]}
- reader 1: sense: 'If I'd have known' is very common in speech; labelling it NOT correct is fine for exam English but note it is widely used informally.
- reader 2: sense: 'If I'd have known' is common in speech and US usage; some learners may regard it as acceptable. Standard grammar says not correct.

## r20-1-016 · B2.2 · mcq · built-in

Task: Which sentence is correct?
options: If I had realise the impact of my decision, I would have acted differently. | If I had realised the impact of my decision, I would have acted differently. | If I would have realised the impact of my decision, I acted differently. | If I realised the impact of my decision, I would have acted differently.
Key: {"kind": "mcq", "correct": "If I had realised the impact of my decision, I would have acted differently.", "wrong": ["If I realised the impact of my decision, I would have acted differently.", "If I would have realised the impact of my decision, I acted differently.", "If I had realise the impact of my decision, I would have acted differently."]}
- reader 1: level: Easy for B2.2.
- reader 1: sense: Option 1 (had realise) is a typo-level error; option 3 and 4 fine.
- reader 2: a wrong option that fits: Option 1 'had realise' is a typo-level slip, weak distractor.

## r20-1-017 · B2.2 · write · built-in

Task: Write one sentence about what would have happened in history if one thing had been different.
Key: {"kind": "write", "model": "If Alexander Fleming hadn't left his dish uncovered, penicillin might not have been discovered.", "must": ["Use *if.*", "Use the past perfect (*had / hadn't*) in the if-part.", "Use *would / might / could have* + past participle in the result."]}
- reader 1: instruction: Does not require a particular form; a learner could write a non-conditional sentence ('Rome might have...').
- reader 2: instruction: Required form not stated.

## r20-1-018 · B2.1 · mcq · built-in

Task: Which sentence imagines a different past with a result now?
options: If I take that job, I will be rich. | If I took that job, I would be rich. | If I had taken that job, I would have been rich. | If I had taken that job, I would be rich now.
Key: {"kind": "mcq", "correct": "If I had taken that job, I would be rich now.", "wrong": ["If I took that job, I would be rich.", "If I had taken that job, I would have been rich.", "If I take that job, I will be rich."]}
- reader 1: a wrong option that fits: If I had taken that job, I would have been rich.
- reader 1: instruction: 'a result now' is the key; option 3 also imagines a different past and a result that could continue to now, so it partly fits.
- reader 2: level: Fine, but options 3 and 4 differ by one phrase; B2.1 hints.
- reader 2: sense: Option 3 is a near-copy of the right sentence; only 'result now' tells them apart.

## r20-1-020 · B2.1 · mcq · built-in

Task: Which sentence is NOT correct?
options: If I had studied medicine, I would be a doctor now. | If I would have studied medicine, I would be a doctor now. | I would be a doctor now if I had studied medicine. | If I'd studied medicine, I'd be a doctor now.
Key: {"kind": "mcq", "correct": "If I would have studied medicine, I would be a doctor now.", "wrong": ["If I had studied medicine, I would be a doctor now.", "If I'd studied medicine, I'd be a doctor now.", "I would be a doctor now if I had studied medicine."]}
- reader 1: level: Easy.

## r20-1-021 · B2.1 · mcq · built-in

Task: Which sentence is correct?
options: If I wouldn't have stayed up so late, I wasn't so tired now. | If I hadn't stayed up so late, I wouldn't have been so tired now. | If I didn't stay up so late, I wouldn't have been so tired now. | If I hadn't stayed up so late, I wouldn't be so tired now.
Key: {"kind": "mcq", "correct": "If I hadn't stayed up so late, I wouldn't be so tired now.", "wrong": ["If I didn't stay up so late, I wouldn't have been so tired now.", "If I hadn't stayed up so late, I wouldn't have been so tired now.", "If I wouldn't have stayed up so late, I wasn't so tired now."]}
- reader 2: sense: Option 1 is garbled (wasn't); option 2 is a near-copy of 4.

## r20-1-022 · B2.1 · write · built-in

Task: How does a past decision still affect you today? Imagine you had decided differently. Write one sentence.
Key: {"kind": "write", "model": "If I had gone to bed earlier, I would feel better now.", "must": ["The past that was different: *If I had …*", "The result now: *would* + verb (not *would have*)."]}
- reader 1: instruction: Question and imperative mix; 'affect you today' plus 'imagine you had decided differently' gives the mixed form away.
- reader 2: instruction: Required form not stated; duplicate of 011/028 style.

## r20-1-023 · B2.2 · mcq · built-in

Task: Complete: 'If I weren't so shy, I ___ asked her out last year.'
options: would | would have | had | will have
Key: {"kind": "mcq", "correct": "would have", "wrong": ["would", "will have", "had"]}
- reader 1: level: Mixed conditional is fine for B2.2.
- reader 1: sense: Slightly odd: 'weren't so shy' (present) with a single past event is plausible. OK.
- reader 2: level: 'asked her out last year' with 'weren't' is mixed conditional; fine for B2.2 but rather B2.1.
- reader 2: sense: Natural sentence.

## r20-1-025 · B2.2 · text · built-in

Task: Imagine the past was different, and say how things would be now. Start with *If he*: He didn't take the job, so he isn't living in Paris now.
Key: {"kind": "text", "accepted": [["If he had taken the job, he would be living in Paris now.", "If he'd taken the job, he'd be living in Paris now.", "He would be living in Paris now if he had taken the job.", "He'd be living in Paris now if he'd taken the job."]]}
- reader 1: another correct answer, not accepted: [['If he had taken the job, he would live in Paris now.'], ["If he had taken the job, he'd live in Paris now."], ['If he had taken the job, he would be in Paris now.'], ["If he'd taken the job, he'd be in Paris now."]]
- reader 1: instruction: The prompt contains the facts and 'now', so it is a mechanical transformation; the *asterisks* show raw markdown. Learner must add 'had taken'.
- reader 2: another correct answer, not accepted: [['If he had taken the job, he would live in Paris now.'], ["If he'd taken the job, he'd live in Paris now."], ['If he had taken the job, he would be in Paris now.']]
- reader 2: instruction: Content is already given in the instruction (copy-and-transform only). '*If he*' markup visible.

## r20-1-026 · B2.2 · mcq · built-in

Task: Which sentence is NOT correct?
options: If I were more careful, I wouldn't have lost my keys. | If I hadn't been so careless, I wouldn't be searching now. | If I had been more careful, I wouldn't have lost my keys. | If I am more careful, I wouldn't have lost my keys.
Key: {"kind": "mcq", "correct": "If I am more careful, I wouldn't have lost my keys.", "wrong": ["If I were more careful, I wouldn't have lost my keys.", "If I had been more careful, I wouldn't have lost my keys.", "If I hadn't been so careless, I wouldn't be searching now."]}
- reader 1: sense: Option 1 is mixed and correct but arguably odd (lost keys needs present trait): fine.

## r20-1-027 · B2.2 · mcq · built-in

Task: A colleague says: 'If I had a better memory, I would have remembered your birthday.' Choose the correct comment about the grammar.
options: Third: both parts are in the past. | First conditional: about the future. | Zero conditional: a general fact. | Mixed: a present quality, a past result.
Key: {"kind": "mcq", "correct": "Mixed: a present quality, a past result.", "wrong": ["First conditional: about the future.", "Zero conditional: a general fact.", "Third: both parts are in the past."]}
- reader 1: level: Terms 'Third', 'Zero', 'Mixed conditional' may be unknown; grammar terms in options.
- reader 1: sense: 'If I had a better memory' then 'remembered your birthday': natural.
- reader 2: sense: Option 1 vs sentence: 'had a better memory' is simple past form, so 'Third' fails. Fine. Uses terms 'Zero/First/Mixed' which learner may not know.

## r20-1-028 · B2.2 · write · built-in

Task: Write one sentence about how a quality of yours (patient, brave, organised …) would have changed something in the past.
Key: {"kind": "write", "model": "If I were more patient, I wouldn't have shouted at the printer yesterday.", "must": ["Use *if.*", "Use *would have* + past participle for the past result."]}
- reader 1: instruction: Does not specify the form; learner may write unchecked structures.
- reader 2: instruction: Required form not stated.

## r20-1-029 · B2.2 · mcq · built-in

Task: Choose the sentence that keeps the meaning: I did not take that job, so I am not rich now.
options: Were I rich now, I would have taken that job. | Had I taken that job, I would be rich now. | Had I not taken that job, I would be rich now. | Had I taken that job, I would have been rich then.
Key: {"kind": "mcq", "correct": "Had I taken that job, I would be rich now.", "wrong": ["Had I taken that job, I would have been rich then.", "Had I not taken that job, I would be rich now.", "Were I rich now, I would have taken that job."]}
- reader 1: level: Inversion + meaning transformation is fine for B2.2.
- reader 1: sense: Option 4 'would have been rich then' is also a correct conditional but does not keep the 'now' meaning; fine. Sentence is near-duplicate of 018 and 032.
- reader 2: level: Meaning-keeping with inversion is B2.2: fine.
- reader 2: sense: Option 1 is odd; option 4 ('rich then') is a plausible distractor. Note: option 2 means the opposite of the given sentence's facts but matches the meaning as a counterfactual; correct.

## r20-1-030 · B2.2 · mcq · built-in

Task: 'Were I more experienced, I would have applied for the director role last year.' What does 'Were I' replace?
options: If I were | Unless I was | If I had been | If I will be
Key: {"kind": "mcq", "correct": "If I were", "wrong": ["If I had been", "If I will be", "Unless I was"]}
- reader 1: sense: The model sentence is a mixed conditional that is odd to analyse; 'Were I' replacing 'If I were' is clear.
- reader 2: sense: Sentence is mixed conditional; 'Were I' = 'If I were'. Fine.

## r20-1-031 · B2.2 · text · built-in

Task: Rewrite with inversion: If I had listened to my accountant, I wouldn't be in this mess now.
Key: {"kind": "text", "accepted": [["Had I listened to my accountant, I wouldn't be in this mess now.", "Had I listened to my accountant, I'd not be in this mess now.", "I wouldn't be in this mess now had I listened to my accountant.", "I'd not be in this mess now had I listened to my accountant."]]}
- reader 1: instruction: Everything is given; 'inversion' is a grammar term some learners may not know.
- reader 2: instruction: 'inversion' is a grammar term the learner may not know.

## r20-1-032 · B2.2 · mcq · built-in

Task: Which sentence is NOT correct?
options: Were I braver, I would have said no. | Had I taken that job, I would be rich now. | Had she known, she would have stayed. | Hadn't I moved here, I'd be in Riga now.
Key: {"kind": "mcq", "correct": "Hadn't I moved here, I'd be in Riga now.", "wrong": ["Had she known, she would have stayed.", "Had I taken that job, I would be rich now.", "Were I braver, I would have said no."]}
- reader 1: sense: Option D is a form nobody writes except as a deliberate trap; correct is 'Had I not moved'. Option 2 duplicates tasks 018/029.
- reader 2: sense: Contracted negative inversion is not standard; 'Had I not moved' is. Good B2.2 error.

## r20-1-034 · B2.2 · write · built-in

Task: Write one sentence about a decision in your past and how your life would be different today. Start with *Had I*.
Key: {"kind": "write", "model": "Had I saved more when I was young, I would be more relaxed about money today.", "must": ["Start with *Had I.*", "Use *would* in the second part."]}
- reader 1: instruction: Fine, but learner may write third conditional in main clause; unclear whether mixed is needed ('today' hints).

## r20-1-036 · B2.2 · mcq · built-in

Task: What does 'unless' mean in 'We'll start unless it rains'?
options: if it rains | although it rains | because it rains | if it does not rain
Key: {"kind": "mcq", "correct": "if it does not rain", "wrong": ["if it rains", "because it rains", "although it rains"]}
- reader 1: level: B1 level for 'unless'; easy for B2.2.
- reader 2: level: B1 meaning of 'unless'; too easy for B2.2.

## r20-1-037 · B2.2 · text · built-in

Task: Rewrite with unless: You will not get a refund if you don't have a receipt.
Key: {"kind": "text", "accepted": [["You will not get a refund unless you have a receipt.", "Unless you have a receipt, you will not get a refund."]]}
- reader 1: level: B1 level for B2.2.
- reader 2: level: B1 level for B2.2.

## r20-1-038 · B2.2 · mcq · built-in

Task: Which sentence means the same as: 'If you don't hurry, we will miss the flight.'?
options: Unless you hurry, we will catch the flight. | We will catch the flight unless you hurry. | If you hurry, we will miss the flight. | Unless you hurry, we will miss the flight.
Key: {"kind": "mcq", "correct": "Unless you hurry, we will miss the flight.", "wrong": ["If you hurry, we will miss the flight.", "Unless you hurry, we will catch the flight.", "We will catch the flight unless you hurry."]}
- reader 1: level: B1 level for B2.2.
- reader 2: level: B1 level for B2.2.
- reader 2: sense: Option 2 is the opposite meaning; fine.

## r20-1-040 · B2.2 · write · built-in

Task: Write a sentence with 'provided that' or 'as long as' to give a condition for a favour.
Key: {"kind": "write", "model": "You can borrow my laptop as long as you bring it back by Friday.", "must": ["Use *provided that* or *as long as.*"]}
- reader 1: instruction: Fine; 'a favour' ok.
- reader 2: instruction: 'the app checks that some forms are used' not visible to the learner.

## r20-1-041 · B2.1 · mcq · built-in

Task: Which sentence is NOT correct?
options: She told me that she would be late. | She said that she would be late. | She told that she would be late. | She told us she would be late.
Key: {"kind": "mcq", "correct": "She told that she would be late.", "wrong": ["She said that she would be late.", "She told me that she would be late.", "She told us she would be late."]}
- reader 1: level: Basic say/tell; B1 not B2.1.
- reader 2: level: B1 level for B2.1; too easy.

## r20-1-042 · B2.1 · mcq · built-in

Task: Which sentence is NOT correct?
options: He asked me if I knew the way. | He asked me what time it was. | He asked me what time was it. | He asked me when the train left.
Key: {"kind": "mcq", "correct": "He asked me what time was it.", "wrong": ["He asked me what time it was.", "He asked me when the train left.", "He asked me if I knew the way."]}
- reader 1: level: Basic reported questions; A2/B1 not B2.1.
- reader 2: level: B1 level for B2.1; too easy.

## r20-1-045 · B2.2 · gap · built-in

Task: 'Congratulations, Jo! You've finally passed the exam!' I congratulated Jo ___ passing the exam.
word_cards: with | about | at | on
Key: {"kind": "gap", "accepted": [["on"]]}
- reader 1: instruction: Quote in front is superfluous: 'I congratulated Jo ___ passing the exam' is enough; also the four cards are all prepositions (a collocation test only).
- reader 1: level: Easy for B2.2 (congratulate on).
- reader 2: sense: 'congratulated Jo on' correct; 'about'/'with'/'at' wrong. Single gap but note says 'each gap'.

## r20-1-046 · B2.2 · mcq · built-in

Task: Which sentence is NOT correct?
options: He blamed me for losing the file. | He blamed me for to lose the file. | He accused me of losing the file. | He admitted losing the file.
Key: {"kind": "mcq", "correct": "He blamed me for to lose the file.", "wrong": ["He blamed me for losing the file.", "He accused me of losing the file.", "He admitted losing the file."]}
- reader 1: level: Easy for B2.2.

## r20-1-048 · B2.2 · mcq · built-in

Task: The decision depends on ___ the budget is approved.
options: if | that | unless | whether
Key: {"kind": "mcq", "correct": "whether", "wrong": ["if", "that", "unless"]}
- reader 1: a wrong option that fits: if (informal: 'depends on if' is widely used, esp. US/spoken; prescriptively wrong after a preposition)
- reader 1: instruction: Key hinges on a prescriptive rule; 'if' fits informally.
- reader 2: a wrong option that fits: 'if' is commonly used after 'depends on' in informal and US English.
- reader 2: sense: 'if' fits informally; learners may defensibly choose it.

## r20-1-050 · B2.2 · mcq · built-in

Task: Choose the correct word: ___ finishes first wins a prize.
options: However | Whatever | Whoever | Whomever
Key: {"kind": "mcq", "correct": "Whoever", "wrong": ["Whomever", "Whatever", "However"]}
- reader 1: sense: Near duplicate of task 060.
- reader 2: sense: Duplicates 060 almost exactly.

## r20-1-051 · B2.2 · mcq · built-in

Task: Which sentence is NOT correct?
options: Whoever wins the contract will celebrate. | Whomever wins the contract will celebrate. | Give it to whomever you trust. | Give it to whoever wants it.
Key: {"kind": "mcq", "correct": "Whomever wins the contract will celebrate.", "wrong": ["Whoever wins the contract will celebrate.", "Give it to whomever you trust.", "Give it to whoever wants it."]}
- reader 1: sense: 'Give it to whomever you trust' is correct formal English, 'whoever you trust' also used: fine. Rule is prescriptive; many natives accept 'whoever' everywhere.
- reader 2: a wrong option that fits: 'Give it to whomever you trust' is correct (object), very formal.
- reader 2: sense: Option 3 with 'whomever' is correct formal English but many native speakers prefer whoever; debatable. Overlaps 050/060.

## r20-1-052 · B2.1 · mcq · conjunctions-1.csv:86

Task: Choose the correct option: The roads were flooded. ___, many schools closed.
options: As a result | Despite | Whereas
Key: {"kind": "mcq", "correct": "As a result", "wrong": ["Despite", "Whereas"]}
- reader 1: level: Easy for B2.1 (A2/B1 connectors); only 3 options.
- reader 2: level: Only three options; fine.

## r20-1-053 · B2.1 · mcq · conjunctions-1.csv:89

Task: Choose the correct option: The match was postponed ___ the heavy rain.
options: since | owing to | owing
Key: {"kind": "mcq", "correct": "owing to", "wrong": ["owing", "since"]}
- reader 1: level: Fine.

## r20-1-054 · B2.2 · mcq · conjunctions-1.csv:103

Task: Choose the correct option: It was a difficult task, and ___ they finished it on time.
options: in spite of | despite | although | yet
Key: {"kind": "mcq", "correct": "yet", "wrong": ["although", "despite", "in spite of"]}
- reader 1: sense: 'and yet' is correct but a rarer pattern; distractors all fail because of 'and'. Fine.
- reader 2: sense: 'and yet' natural; others do not fit after 'and'.

## r20-1-055 · B2.2 · gap · conjunctions-1.csv:108

Task: Sales fell. ___, we have decided to close the shop.
word_cards: Therefore | Despite | In case | Whereas
Key: {"kind": "gap", "accepted": [["Therefore"]]}
- reader 1: level: Easy for B2.2.

## r20-1-056 · B2.2 · gap · iq-b1-6.csv:33

Task: The hotel wants to know ___ to expect us before ten, and ___ we're late, they'll keep the room for us until midnight.
word_cards: unless | if | whether
Key: {"kind": "gap", "accepted": [["whether"], ["if"]]}
- reader 1: a wrong option that fits: unless (does not fit logically: 'unless we're late they'll keep the room' makes no sense)
- reader 1: instruction: Sentence is awkward ('know whether to expect us'); 'if to expect' is wrong so only one order works. Cards number three for two gaps.
- reader 1: sense: Slightly unnatural: a hotel wanting to know whether to expect guests.
- reader 2: instruction: Three cards for two gaps; 'unless' fits no gap sensibly.

## r20-1-057 · B2.1 · gap · learn-drag-3.csv:11

Task: He ___ ___ that the shop was closed.
word_cards: said | told | to | me
Key: {"kind": "gap", "accepted": [["told"], ["me"]]}
- reader 1: instruction: Only 'told me' works with these cards; 'said' and 'to' are distractors that cannot combine ('said to me' needs three words).
- reader 1: level: Say/tell is A2/B1, too easy for B2.1.
- reader 2: instruction: No grammar needed beyond choosing told+me; 'said' and 'to' are obvious distractors.
- reader 2: level: Too easy for B2.1 (told me / said).

## r20-1-058 · B2.2 · gap · learn-drag-3.csv:21

Task: The client complained ___ the delivery ___ been three days late.
word_cards: about | have | had | that
Key: {"kind": "gap", "accepted": [["that"], ["had"]]}
- reader 1: instruction: 'about' leaves the sentence incorrect; the gap structure is clear.
- reader 1: level: Easy for B2.2.
- reader 2: sense: Only possible combination; 'about' is a distractor that is absolutely wrong in gap 1 with 'had been'.

## r20-1-059 · B2.1 · gap · learn-drag-4.csv:30

Task: They walked quietly so as ___ ___ wake the baby.
word_cards: to | don't | not | no
Key: {"kind": "gap", "accepted": [["not"], ["to"]]}
- reader 1: level: Fine.
- reader 2: level: 'so as not to' is B2 but easy with cards.

## r20-1-060 · B2.2 · mcq · twins-3.csv:26

Task: Choose the correct word: ___ arrives last has to wash the dishes.
options: Whoever | Whomever | Whatever | However
Key: {"kind": "mcq", "correct": "Whoever", "wrong": ["Whomever", "Whatever", "However"]}
- reader 1: sense: Near duplicate of task 050.
- reader 2: sense: Duplicate of 050.

