# Blind check r20c: flags for the judge

30 tasks, 2 readers.

## r20c-001 · B2.1 · gap · built-in

Task: Our company will never change its fixed hours. If it ___ more flexible hours, people ___ happier. (offer / be)
Key: {"kind": "gap", "accepted": [["offered", "were to offer", "were offering"], ["would be", "'d be", "might be", "could be"]]}
- reader 2: instruction: 'never change' plus the verbs in brackets make the tense very easy to guess; fine otherwise

## r20c-002 · B2.2 · mcq · built-in

Task: Which sentence is correct?
options: If I realised the impact of my decision, I would have acted differently. | If I would have realised the impact of my decision, I would have acted differently. | If I had realised the impact of my decision, I would have acted differently.
Key: {"kind": "mcq", "correct": "If I had realised the impact of my decision, I would have acted differently.", "wrong": ["If I realised the impact of my decision, I would have acted differently.", "If I would have realised the impact of my decision, I would have acted differently."]}
- reader 2: sense: Options 1 and 2 are believable mistakes. Option 1 is not a form nobody writes, fine.

## r20c-003 · B2.2 · text · built-in

Task: Imagine the past was different, and say how things would be now. Start with *If he*: He didn't take the job, so he isn't living in Paris now.
Key: {"kind": "text", "accepted": [["If he had taken the job, he would be living in Paris now.", "If he'd taken the job, he'd be living in Paris now.", "He would be living in Paris now if he had taken the job.", "He'd be living in Paris now if he'd taken the job.", "If he had taken the job, he would live in Paris now.", "If he'd taken the job, he'd live in Paris now.", "He would live in Paris now if he had taken the job.", "If he had taken the job, he would be in Paris now.", "If he'd taken the job, he'd be in Paris now.", "He would be in Paris now if he had taken the job.", "If he had taken the job, he might be living in Paris now.", "If he'd taken the job, he might be living in Paris now."]]}
- reader 1: another correct answer, not accepted: ['If he had accepted the job, he would be living in Paris now.']
- reader 2: instruction: 'Start with If he' plus the given facts nearly gives the whole sentence; 'say how things would be now' is the only real hint to the mixed form. Several correct variants (contractions, would live / would be living).

## r20c-004 · B2.2 · mcq · built-in

Task: A colleague says: 'If I had a better memory, I would have remembered your birthday.' What does the sentence say?
options: The colleague's memory was poor in the past, but it is fine now. | The colleague remembered your birthday. | The colleague will remember your birthday next year. | The colleague's memory is poor, and that is why they forgot your birthday.
Key: {"kind": "mcq", "correct": "The colleague's memory is poor, and that is why they forgot your birthday.", "wrong": ["The colleague's memory was poor in the past, but it is fine now.", "The colleague remembered your birthday.", "The colleague will remember your birthday next year."]}
- reader 1: a wrong option that fits: The first option is partly defensible (memory poor then) but 'fine now' is not stated, so wrong.
- reader 1: sense: Mixed conditional with a general trait ('better memory') is odd; 'If I had a better memory' is a permanent trait, so the sentence sounds unnatural; most speakers would say 'If I had remembered...' or 'I wish I had a better memory'.
- reader 2: instruction: The sentence is an odd mixed conditional ('had a better memory' for a general state); a learner may read it as past (option 1). Strongly depends on knowing the mixed conditional.
- reader 2: sense: Model sentence is slightly unnatural: 'If I had a better memory' + 'would have remembered' is rare; most people say 'If I had a better memory, I'd have remembered' only informally. Option 1 is a plausible rival reading.

## r20c-005 · B2.2 · gap · built-in

Task: 'Where should we meet?' → They asked me ___.
Key: {"kind": "gap", "accepted": [["where they should meet", "where we should meet", "where to meet", "where we were to meet", "where they were to meet", "where we ought to meet", "where they ought to meet"]]}
- reader 1: instruction: Gap has several words but 'several gaps' note suggests one word each; unclear how many words go in the gap.
- reader 2: instruction: Gap needs the whole clause including 'where'; instruction gives no hint how many words. 'where to meet' is also correct. 'they' vs 'we' ambiguous.
- reader 2: level: Too easy for B2.2 (B1 reported question).

## r20c-006 · B2.2 · gap · built-in

Task: 'Congratulations, Jo! You've finally passed the exam!' I congratulated Jo ___ passing the exam.
word_cards: on | to | of
Key: {"kind": "gap", "accepted": [["on"]]}
- reader 1: instruction: The direct speech is not needed: 'I congratulated Jo ___ passing' already allows only 'on'.
- reader 2: level: Easy for B2.2; 'congratulate on' is B1/B2.1.

## r20c-007 · B2.2 · mcq · built-in

Task: Which sentence reports the customer's words: 'The service was terrible.'
options: The customer complained that the service had been terrible. | The customer complained that the service has been terrible. | The customer complained me that the service was terrible.
Key: {"kind": "mcq", "correct": "The customer complained that the service had been terrible.", "wrong": ["The customer complained that the service has been terrible.", "The customer complained me that the service was terrible."]}
- reader 1: a wrong option that fits: 'has been' (option 2) is possible only if the service is still terrible; from 'was terrible' it is a wrong backshift, so not correct.
- reader 2: a wrong option that fits: 'has been' (option 2) is possible if the service is still bad now / complaint is recent, but weaker than 'had been'. Strictly 'was' would also be right but is not offered.
- reader 2: level: Too easy for B2.2.

## r20c-008 · B2.2 · text · built-in

Task: Combine the two sentences without changing their meaning: Who made the decision? It's not clear.
Key: {"kind": "text", "accepted": [["It's not clear who made the decision.", "It is not clear who made the decision.", "Who made the decision is not clear.", "It's unclear who made the decision.", "It is unclear who made the decision.", "It remains unclear who made the decision.", "Who made the decision is unclear."]]}
- reader 1: level: Easy for B2.2: just a swap of two parts, only 'who' word order.
- reader 2: level: Too easy for B2.2 (B1 embedded question).

## r20c-009 · B2.2 · text · built-in

Task: Make it one sentence that starts with *Who…*: It doesn't matter who calls. Don't answer.
Key: {"kind": "text", "accepted": [["Whoever calls, don't answer.", "Whoever calls, do not answer.", "Whoever it is, don't answer.", "Whoever it is, do not answer.", "Who calls doesn't matter, so don't answer.", "Who calls does not matter, so do not answer.", "Whoever may call, don't answer.", "Whoever may call, do not answer.", "Who calls doesn't matter; don't answer.", "Who calls does not matter; do not answer."]]}
- reader 1: another correct answer, not accepted: ["Don't answer, whoever calls.", "Don't answer whoever calls.", "Who(ever) it is that calls, don't answer."]
- reader 1: instruction: 'Starts with Who...' is ambiguous (Who? Whoever?) and gives a hint; a learner may write 'Who calls doesn't matter' or 'Who calls, don't answer'. 'No matter who calls' does not start with Who.
- reader 1: level: 'whoever' structure is a stretch but OK for B2.2.
- reader 2: another correct answer, not accepted: ["Who(ever) it is that calls, don't answer.", "Don't answer, whoever calls."]
- reader 2: instruction: 'starts with Who…' is unclear: 'Who calls doesn't matter' is also a sentence starting with Who. 'Whoever' is not obviously what is wanted; 'No matter who calls' does not start with Who. The two given sentences do not make clear it should be one imperative sentence.

## r20c-010 · B2.1 · gap · compare-past-1.csv:53

Task: James was out of breath when he came in. He ___. (run)
Key: {"kind": "gap", "accepted": [["had been running", "had run", "'d run", "'d been running", "must have been running", "must have run"]]}
- reader 1: instruction: 'had run' is also correct (less natural: stresses the completed run, not the continuing effect); the task allows both.
- reader 2: instruction: 'had run' is also correct; a learner has no way to know the continuous is wanted.

## r20c-011 · B2.2 · order · compare-past-1.csv:61

Task: Put all the words in order. More than one answer is possible.
word_cards: been | years | ten | had | when | there | working | left | for | she | she
Key: {"kind": "order", "sentence": "she had been working there for ten years when she left", "also": ["when she left she had been working there for ten years", "she left when she had been working there for ten years", "when she had been working there for ten years she left", "when she left there she had been working for ten years", "she had been working for ten years when she left there"]}
- reader 1: another correct answer, not accepted: ['she had been working for ten years there when she left (less natural)']
- reader 1: level: Fine, but cards give no capital letter or punctuation, so the clause order is ambiguous (this is flagged by 'more than one answer').
- reader 2: instruction: No capital letters or punctuation shown, so both clause orders look possible; 'More than one answer is possible' is fine.
- reader 2: sense: Two 'she' cards: fine.

## r20c-012 · B2.1 · text · conjunctions-1.csv:81

Task: Correct the mistake: Despite of the delays, the project was finished on time.
Key: {"kind": "text", "accepted": [["Despite the delays, the project was finished on time.", "In spite of the delays, the project was finished on time.", "The project was finished on time despite the delays.", "The project was finished on time in spite of the delays."]]}
- reader 1: instruction: Does not say how to fix; both 'Despite' without 'of' and 'In spite of' are correct.
- reader 2: sense: Very common mistake, believable. Near-duplicate of 16.

## r20c-013 · B2.1 · text · conjunctions-1.csv:105

Task: Correct the mistake: Save a copy on a USB stick in case your laptop will crash.
Key: {"kind": "text", "accepted": [["Save a copy on a USB stick in case your laptop crashes.", "Save a copy on a USB stick in case your laptop should crash.", "Save a copy on a USB stick in case your laptop does crash."]]}
- reader 2: another correct answer, not accepted: ['Save a copy on a USB stick in case your laptop crashed.']
- reader 2: sense: Believable mistake.

## r20c-014 · B2.2 · text · conjunctions-1.csv:107

Task: Rewrite with *owing to*: The flight was late because the weather was bad.
Key: {"kind": "text", "accepted": [["The flight was late owing to the bad weather.", "The flight was late owing to bad weather.", "Owing to the bad weather, the flight was late.", "Owing to bad weather, the flight was late.", "Owing to the weather being bad, the flight was late.", "The flight was late owing to the weather being bad.", "The flight was late owing to the fact that the weather was bad.", "Owing to the fact that the weather was bad, the flight was late.", "Owing to the weather's being bad, the flight was late.", "The flight was late owing to the weather's being bad."]]}
- reader 2: instruction: 'owing to' needs a noun phrase; a learner may write 'owing to the weather was bad' (not an instruction fault).

## r20c-015 · B2.1 · order · learn-drag-4.csv:18

Task: Put the words in order.
word_cards: would | the | have | team | won | had | prepared | we | if | better | been
Key: {"kind": "order", "sentence": "if the team had been better prepared we would have won", "also": ["we would have won if the team had been better prepared", "if we had been better prepared the team would have won", "the team would have won if we had been better prepared", "if the team had been prepared better we would have won", "we would have won if the team had been prepared better", "if we had been prepared better the team would have won", "the team would have won if we had been prepared better"]}
- reader 1: another correct answer, not accepted: ['We would have been better prepared if the team had won (illogical but grammatical).']
- reader 1: instruction: Does not say more than one order is possible, and nothing says who was unprepared; at least four sensible answers exist.
- reader 1: sense: 'we' and 'the team' make two logical versions; ambiguous.
- reader 2: instruction: No punctuation/capitals; the cards contain 'won' and 'been' so only the third conditional works; fine. Several correct orders but no note that more than one is possible.

## r20c-016 · B2.1 · text · twins-1.csv:34

Task: Correct the mistake: She got the job despite of having no experience.
Key: {"kind": "text", "accepted": [["She got the job despite having no experience.", "She got the job in spite of having no experience.", "Despite having no experience, she got the job.", "In spite of having no experience, she got the job."]]}
- reader 1: instruction: Does not say how to fix; 'in spite of' is also correct.
- reader 2: sense: Near-duplicate of 12 (despite of); also level-wise similar.

## r20c-017 · B2.1 · gap · twins-1.csv:44

Task: The city has no money for cycle lanes, so it won't build any. If it ___ more cycle lanes, more people ___ by bike. (build / travel)
Key: {"kind": "gap", "accepted": [["built", "were to build"], ["would travel", "might travel", "could travel", "would be travelling", "'d travel"]]}
- reader 2: instruction: 'won't build any' makes the unreal reading clear; fine.

## r20c-018 · B2.2 · gap · twins-1.csv:49

Task: She stayed late and missed the last bus. If she ___ (not / stay) so late, she ___ (not / miss) the last bus.
Key: {"kind": "gap", "accepted": [["hadn't stayed"], ["wouldn't have missed", "might not have missed", "'d not have missed"]]}
- reader 2: instruction: The brackets give the verbs and polarity; learners only need to build the third conditional (little gap left).

## r20c-019 · B2.2 · text · twins-3.csv:15

Task: Report this. Start with *They asked*: 'What time should we arrive?'
Key: {"kind": "text", "accepted": [["They asked what time they should arrive.", "They asked what time to arrive.", "They asked what time we should arrive.", "They asked me what time they should arrive.", "They asked us what time we should arrive.", "They asked me what time to arrive.", "They asked us what time to arrive.", "They asked what time they ought to arrive.", "They asked what time they were to arrive.", "They asked what time we were to arrive."]]}
- reader 1: another correct answer, not accepted: ['They asked what time we would arrive.', 'They asked what time we ought to arrive.']
- reader 2: instruction: 'Start with They asked' plus quote makes it almost copying; 'they/we' ambiguous.
- reader 2: level: Easy for B2.2.

## r20c-020 · B2.2 · text · twins-3.csv:23

Task: Join the sentences: She didn't know. Who should she ask?
Key: {"kind": "text", "accepted": [["She didn't know who to ask.", "She didn't know whom to ask.", "She didn't know who she should ask.", "She didn't know whom she should ask.", "She didn't know who she ought to ask.", "She didn't know whom she ought to ask."]]}
- reader 1: another correct answer, not accepted: ["She didn't know who she was to ask."]
- reader 2: instruction: Instruction does not say how to join; 'who to ask' also correct.
- reader 2: level: Easy for B2.2.

## r20c-021 · B2.2 · text · twins-3.csv:27

Task: Rewrite as one sentence. Start with *I'll support you*: It doesn't matter what you decide. I'll support you.
Key: {"kind": "text", "accepted": [["I'll support you whatever you decide.", "I will support you whatever you decide.", "I'll support you no matter what you decide.", "I will support you no matter what you decide.", "I'll support you whichever way you decide.", "I'll support you however you decide.", "I'll support you regardless of what you decide.", "I'll support you whatever decision you make.", "I will support you whatever decision you make."]]}
- reader 1: another correct answer, not accepted: ["I'll support you whatever it is you decide."]
- reader 2: another correct answer, not accepted: ["I'll support you whatever it is you decide."]
- reader 2: instruction: Start 'I'll support you' is given, so only the ending is needed; 'it doesn't matter what' leads to whatever/no matter what - fine.

## r20c-022 · B2.1 · gap · typical-b2c1-1.csv:14

Task: I set two alarms in order ___ my early flight. (not / miss)
Key: {"kind": "gap", "accepted": [["not to miss", "to not miss", "that I don't miss", "that I do not miss", "that I won't miss", "that I will not miss", "that I wouldn't miss", "that I would not miss"]]}
- reader 1: instruction: '(not / miss)' in brackets half-gives the answer; split infinitive 'to not miss' is accepted by many speakers.
- reader 2: instruction: '(not / miss)' nearly gives the answer; level fine.

## r20c-023 · B2.1 · gap · typical-b2c1-1.csv:15

Task: I'll leave you my number in case you ___ any problems with the flat. (have)
Key: {"kind": "gap", "accepted": [["have", "should have", "happen to have", "do have"]]}
- reader 1: another correct answer, not accepted: [['might have'], ['had']]
- reader 1: instruction: 'had' (in case you had any problems) is also possible but less common.
- reader 2: another correct answer, not accepted: [['might have']]
- reader 2: instruction: '(have)' gives the verb; 'should have' also correct (more formal).

## r20c-024 · B2.2 · gap · typical-b2c1-1.csv:20

Task: Our guide suggested ___ the museum early to avoid the queues. (visit)
Key: {"kind": "gap", "accepted": [["visiting", "that we visit", "we visit", "that we should visit", "we should visit", "that we visited", "we visited", "our visiting", "going to visit"]]}
- reader 1: instruction: Verb given as (visit) hides that 'we visit/should visit' also fits before 'the museum'; the gap invites one word but several correct answers exist.
- reader 1: level: OK for B2.2.
- reader 2: instruction: Gap is ambiguous: 'we visit / (that) we should visit' also fit the sentence; the hint '(visit)' makes both -ing and 'we visit' possible. 'visiting' is the intended answer.
- reader 2: level: B1 level for B2.2 (suggest + -ing).

## r20c-025 · B2.2 · gap · typical-b2c1-1.csv:21

Task: I'm not sure what time the meeting ___ tomorrow. (start)
Key: {"kind": "gap", "accepted": [["starts", "will start", "is going to start", "is starting", "is to start"]]}
- reader 1: another correct answer, not accepted: [['begins']]
- reader 1: instruction: No hint that a timetable present is wanted; 'will start', 'is going to start', 'is starting' are all correct.
- reader 2: another correct answer, not accepted: [['is due to start'], ['begins']]
- reader 2: instruction: Several tenses fit; (start) is the only hint, and 'starts' is the timetable use. Wrong/other answers 'will start' are fully correct.
- reader 2: level: Easy for B2.2.

## r20c-026 · B2.2 · gap · typical-b2c1-1.csv:25

Task: Sales fell sharply; ___ , the company cut its prices.
Key: {"kind": "gap", "accepted": [["therefore", "as a result", "consequently", "thus", "as a consequence", "accordingly", "hence", "for this reason", "in response", "because of this"]]}
- reader 1: another correct answer, not accepted: [['so']]
- reader 1: instruction: No instruction: open gap with many correct linkers; space before comma suggests a one- or two-word linker but 'so' (no comma) is also possible.
- reader 1: sense: Too many fits; the item tests nothing specific.
- reader 2: another correct answer, not accepted: [['so']]
- reader 2: instruction: No hint at all: any result linker fits (open gap); 'so' with a comma is poor but 'so' without comma would be fine. Too open for a typed gap.

## r20c-027 · B2.2 · gap · typical-b2c1-1.csv:32

Task: In future, I'd rather you ___ my phone without asking. (not / use)
Key: {"kind": "gap", "accepted": [["didn't use", "did not use", "not use"]]}
- reader 2: another correct answer, not accepted: [["wouldn't use"], ['would not use']]
- reader 2: instruction: 'wouldn't use' is also accepted by many speakers; 'not use' is American subjunctive.

## r20c-028 · B2.2 · gap · typical-b2c1-1.csv:34

Task: We couldn't decide where ___ on holiday. (go)
Key: {"kind": "gap", "accepted": [["to go", "we should go", "we could go", "we would go", "we'd go", "we were going to go", "we ought to go", "we were going"]]}
- reader 1: another correct answer, not accepted: [['we wanted to go']]
- reader 1: instruction: Gap of one or several words: 'to go' and a full clause with 'we' both fit.
- reader 2: another correct answer, not accepted: [['we were to go']]
- reader 2: instruction: '(go)' hints 'to go' but 'we should/could go' also correct.
- reader 2: level: B1 level for B2.2.

## r20c-029 · B2.2 · gap · typical-b2c1-1.csv:40

Task: Our holiday plans depend on ___ my boss gives me the week off.
Key: {"kind": "gap", "accepted": [["whether", "whether or not"]]}
- reader 1: another correct answer, not accepted: [['if'], ['when']]
- reader 1: instruction: 'if' after a preposition is informal; some accept it. 'when' also gives correct English with a different meaning (no meaning cue given).
- reader 2: another correct answer, not accepted: [['if'], ['when'], ['how'], ['what time'], ['how soon']]
- reader 2: instruction: No hint: 'if' (informal), 'when' and 'whether' all fit; 'when my boss gives me the week off' is perfectly correct and sensible.

## r20c-030 · B2.2 · text · unreal-time-1.csv:5

Task: Write one sentence that starts with *It's high time*: You should really start looking for a new job.
Key: {"kind": "text", "accepted": [["It's high time you started looking for a new job.", "It's high time you started to look for a new job.", "It's high time you looked for a new job.", "It is high time you started looking for a new job.", "It is high time you started to look for a new job.", "It is high time you looked for a new job.", "It's high time you began looking for a new job.", "It is high time you began looking for a new job.", "It's high time that you started looking for a new job.", "It is high time that you started looking for a new job.", "It's high time you were looking for a new job.", "It is high time you were looking for a new job.", "It's high time you started job-hunting.", "It is high time you started job-hunting.", "It's high time for you to start looking for a new job.", "It is high time for you to start looking for a new job.", "It's high time you started looking for a job.", "It is high time you started looking for a job."]]}
- reader 1: another correct answer, not accepted: ["It's high time you started your search for a new job."]
- reader 1: sense: 'You should really start' with 'really' is a near copy; fine.
- reader 2: instruction: Instruction does not say 'you' must follow; fine. Sentence repeats 'should really' content.

