# Blind check r20-2: flags for the judge

60 tasks, 2 readers.

## r20-2-001 · B2.2 · mcq · built-in

Task: Which sentence expresses regret about the present?
options: I wish I had lived closer to the sea. | I wish I will live closer to the sea. | I wish I would live closer to the sea. | I wish I lived closer to the sea.
Key: {"kind": "mcq", "correct": "I wish I lived closer to the sea.", "wrong": ["I wish I had lived closer to the sea.", "I wish I will live closer to the sea.", "I wish I would live closer to the sea."]}
- reader 1: level: Easy for B2.2 (basic wish + past simple).
- reader 2: sense: 'I wish I would live' is a form nobody writes (would with I); weak distractor.

## r20-2-002 · B2.2 · mcq · built-in

Task: I wish you ___ clicking your pen. It's driving me mad.
options: to stop | would stop | would stopping | will stop
Key: {"kind": "mcq", "correct": "would stop", "wrong": ["will stop", "would stopping", "to stop"]}
- reader 1: level: Too basic for B2.2.

## r20-2-003 · B2.2 · gap · built-in

Task: I wish I ___ that email yesterday. Now everyone knows.
word_cards: hadn't sent | didn't send | wouldn't send | haven't sent
Key: {"kind": "gap", "accepted": [["hadn't sent"]]}
- reader 1: level: Too basic for B2.2.
- reader 2: instruction: Single gap but described as 'each gap'; 'yesterday' + 'Now everyone knows' both signal the answer (fine).

## r20-2-004 · B2.2 · mcq · built-in

Task: Which sentence has a mistake?
options: I wish I had saved more when I was young. | If only I would have saved more money. | If only you had told me about it earlier. | If only I earned a bit more money now.
Key: {"kind": "mcq", "correct": "If only I would have saved more money.", "wrong": ["I wish I had saved more when I was young.", "If only I earned a bit more money now.", "If only you had told me about it earlier."]}
- reader 1: level: Easy for B2.2.
- reader 2: sense: Option 2 is common in informal American speech, so learners may not see it as a mistake; no time marker to help.

## r20-2-005 · B2.2 · mcq · built-in

Task: You give a speech about a past failure. Choose the correct option.
options: If only we had listen to the warning signs, we would not be in this position. | If only we would have listened to the warning signs, we would not be in this position. | If only we had listened to the warning signs, we would not be in this position. | If only we listened to the warning signs, we would not be in this position.
Key: {"kind": "mcq", "correct": "If only we had listened to the warning signs, we would not be in this position.", "wrong": ["If only we would have listened to the warning signs, we would not be in this position.", "If only we listened to the warning signs, we would not be in this position.", "If only we had listen to the warning signs, we would not be in this position."]}
- reader 1: instruction: 'You give a speech about a past failure' is superfluous: options alone decide it. Option 1 (had listen) is a typo-type error.
- reader 1: level: Too easy for B2.2.
- reader 1: sense: Option 1 is a form nobody really chooses (missing -ed).
- reader 2: sense: Distractor 1 (had listen) is a typo-type error rather than a believable learner mistake.

## r20-2-006 · B2.2 · write · built-in

Task: Write a sentence with 'I wish' or 'If only' about something you regret from last year.
Key: {"kind": "write", "model": "I wish I had started learning Spanish last year.", "must": ["Use *I wish* or *If only.*", "For a regret about the past use the past perfect (*had / hadn't*)."]}
- reader 1: instruction: 'the app checks that some forms are used' is not clear to learner; 'I wish ... would' would also be accepted by the instruction but is wrong for past regret.
- reader 2: instruction: Open task; checker must accept 'wish/if only + had + past participle' and also 'could have'/'would have' forms.

## r20-2-007 · B2.1 · mcq · built-in

Task: Which sentence reports this: 'I might be late.'
options: She said she might to be late. | She said she might be late. | She said she might been late. | She said she might was late.
Key: {"kind": "mcq", "correct": "She said she might be late.", "wrong": ["She said she might was late.", "She said she might to be late.", "She said she might been late."]}
- reader 1: instruction: Instruction fine.
- reader 1: level: Too easy for B2.1 (A2/B1 level).
- reader 1: sense: Wrong options (might to be / might been / might was) are not mistakes real B2 learners make.
- reader 2: level: B1 content (reported statement with might), too easy for B2.1.
- reader 2: sense: Distractors (might to be / been / was) are random-ish ungrammatical strings.

## r20-2-008 · B2.1 · mcq · built-in

Task: The teacher's words: 'The Earth goes round the Sun.' Why can we report them as 'The teacher said the Earth goes round the Sun'?
options: Because goes is an irregular verb. | Because it is still true. | Because said is in the past. | Because the tense never changes.
Key: {"kind": "mcq", "correct": "Because it is still true.", "wrong": ["Because said is in the past.", "Because the tense never changes.", "Because goes is an irregular verb."]}
- reader 1: a wrong option that fits: 'Because the tense never changes' is false; none other fits. Note: 'The Earth went round the Sun' would also be correct.
- reader 1: instruction: Asks about a rule; 'Why can we' fine. Option 3 'said is in the past' is true yet is the reason you would normally backshift.
- reader 1: sense: Option 4 is odd, 'never' obviously false.
- reader 2: a wrong option that fits: 'Because said is in the past.' is true as a fact but does not explain it; 'the tense never changes' is false.
- reader 2: instruction: Natural, but options 3 and 4 are loosely worded; option 1 irrelevant.

## r20-2-009 · B2.1 · mcq · built-in

Task: Last week the client said: 'I won't sign it until the lawyer reads it.' Yesterday he signed it. Which sentence reports the client's words?
options: The client said he wouldn't sign it until the lawyer had read it. | The client said I wouldn't sign it until the lawyer reads it. | The client said he won't sign it until the lawyer will read it. | The client told he wouldn't sign it until the lawyer read it.
Key: {"kind": "mcq", "correct": "The client said he wouldn't sign it until the lawyer had read it.", "wrong": ["The client said he won't sign it until the lawyer will read it.", "The client said I wouldn't sign it until the lawyer reads it.", "The client told he wouldn't sign it until the lawyer read it."]}
- reader 1: instruction: 'Yesterday he signed it' is superfluous. Option 4 also contains 'told he' (wrong) but is not near-copy.
- reader 1: sense: The 'lawyer read it' version is acceptable but not offered as option. Option 4 'told he' is not a believable B2 error.
- reader 2: instruction: 'Yesterday he signed it' is superfluous except to justify backshift; 'The lawyer read it' also fine but is not offered as correct here.
- reader 2: sense: Option 4 differs from 1 by 'told' and 'read'; ok.

## r20-2-010 · B2.1 · write · built-in

Task: Report a warning from your doctor: 'You must drink more water.' Start with My doctor said.
Key: {"kind": "write", "model": "My doctor said I had to drink more water.", "must": ["Start with *My doctor said.*", "*must* becomes *had to* (or stays *must*).", "Change *you* to *I.*"]}
- reader 1: instruction: 'warning' is slightly odd for advice to drink water. Hint 'forms are used' unclear. Must/had to/should all correct.
- reader 2: instruction: Open task; checker must accept must/had to/should (should slightly weakens meaning).

## r20-2-011 · B2.1 · mcq · built-in

Task: Anna's question to you: 'Can you help me?' Which sentence reports it?
options: She asked can I help her. | She asked if could I help her. | She asked if I could help her. | She asked that I could help her.
Key: {"kind": "mcq", "correct": "She asked if I could help her.", "wrong": ["She asked if could I help her.", "She asked can I help her.", "She asked that I could help her."]}
- reader 1: instruction: 'Anna's question to you' and 'Which sentence reports it' fine.
- reader 1: level: Easy for B2.1.
- reader 1: sense: Option 1 and 2 are believable; option 4 'asked that' unlikely.
- reader 2: level: B1 level.

## r20-2-012 · B2.1 · mcq · built-in

Task: Which sentence reports this instruction: 'Don't touch that!'
options: The nurse said me not to touch it. | The nurse told me not touching it. | The nurse told me not to touch it. | The nurse told me not touch it.
Key: {"kind": "mcq", "correct": "The nurse told me not to touch it.", "wrong": ["The nurse told me not touch it.", "The nurse told me not touching it.", "The nurse said me not to touch it."]}
- reader 1: level: Easy for B2.1.
- reader 1: sense: Options 1,2,4 are believable.
- reader 2: level: B1 level (told + not to); easy for B2.1.

## r20-2-013 · B2.1 · gap · built-in

Task: 'Could you send me the invoice?' → Lena asked me ___.
Key: {"kind": "gap", "accepted": [["to send her the invoice", "if I could send her the invoice", "whether I could send her the invoice"]]}
- reader 1: another correct answer, not accepted: [['to send him the invoice'], ['if I could send him the invoice']]
- reader 1: instruction: 'several gaps' but only one ___ shown: unclear whether to type whole phrase or one word. 'to send her the invoice' (request report) is also correct; 'her/him' not given.
- reader 1: sense: 'Lena' gender not given by wording: her/him unclear (Lena is female name, but 'him' unnatural).
- reader 2: instruction: Number of gaps unclear ('several gaps'); 'asked me to send her the invoice' is also correct English (a request reported as an instruction) so the task accepts several structures.

## r20-2-014 · B2.1 · mcq · built-in

Task: Which sentence reports the customer's question: 'How long will the repair take?'
options: The customer asked how long would the repair take. | The customer asked how long will the repair take. | The customer asked how long did the repair take. | The customer asked how long the repair would take.
Key: {"kind": "mcq", "correct": "The customer asked how long the repair would take.", "wrong": ["The customer asked how long would the repair take.", "The customer asked how long will the repair take.", "The customer asked how long did the repair take."]}
- reader 1: instruction: Fine.
- reader 1: level: Fine.
- reader 2: level: B1/B1+; fine for B2.1 borderline.

## r20-2-015 · B2.1 · write · built-in

Task: Report a request you received at work: 'Could you call the supplier?' Start with My manager asked me.
Key: {"kind": "write", "model": "My manager asked me to call the supplier.", "must": ["Start with *My manager asked me.*", "Use *to call*, or *if / whether I could call.*"]}
- reader 1: instruction: Hint about forms is unclear; both 'to call' and 'if I could' are correct.
- reader 2: instruction: Open task; 'asked me to' gives the form away only by the starter.

## r20-2-016 · B2.2 · mcq · built-in

Task: Tom's question to you: 'What should I do?' Which sentence reports it?
options: He asked me what to doing. | He asked me what to do. | He asked me what he does. | He asked me what should he do.
Key: {"kind": "mcq", "correct": "He asked me what to do.", "wrong": ["He asked me what should he do.", "He asked me what he does.", "He asked me what to doing."]}
- reader 1: instruction: Too easy for B2.2.
- reader 1: level: Too easy for B2.2 (B1 level).
- reader 1: sense: Options 1,3,4 believable. Also 'what I should do' correct but not offered.
- reader 2: level: B1 level, too easy for B2.2.
- reader 2: sense: 'what to doing' is not a believable mistake.

## r20-2-017 · B2.2 · mcq · built-in

Task: Eva's question to you: 'Where should I park?' Which sentence reports it?
options: She asked me where does she should park. | She asked me where should she park. | She asked me where she should to park. | She asked me where she should park.
Key: {"kind": "mcq", "correct": "She asked me where she should park.", "wrong": ["She asked me where should she park.", "She asked me where she should to park.", "She asked me where does she should park."]}
- reader 1: level: Easy for B2.2.
- reader 1: sense: Option 1 (where does she should park) is a form nobody writes.
- reader 2: level: B1 level, too easy for B2.2.

## r20-2-018 · B2.2 · gap · built-in

Task: 'Where should we meet?' → They asked me ___.
Key: {"kind": "gap", "accepted": [["where they should meet", "where we should meet", "where to meet"]]}
- reader 1: another correct answer, not accepted: [['where we would meet'], ['where we were to meet'], ['where I should meet']]
- reader 1: instruction: 'several gaps' but only one ___; unclear what counts as one gap (one word? phrase?). 'where to meet' also correct.
- reader 1: level: Easy for B2.2.
- reader 2: another correct answer, not accepted: [['where they would meet']]
- reader 2: instruction: Number of gaps unclear; 'where to meet' is a valid shorter answer; we/they both defensible depending on whether the speaker includes 'me'.
- reader 2: level: B1-level.

## r20-2-019 · B2.2 · mcq · built-in

Task: Which sentence is correct?
options: Ms Novak asked whether the budget had been approved. | Ms Novak asked has the budget been approved. | Ms Novak asked whether had the budget been approved. | Ms Novak asked that the budget had been approved.
Key: {"kind": "mcq", "correct": "Ms Novak asked whether the budget had been approved.", "wrong": ["Ms Novak asked has the budget been approved.", "Ms Novak asked whether had the budget been approved.", "Ms Novak asked that the budget had been approved."]}
- reader 1: instruction: Fine.
- reader 1: sense: Option 4 'asked that' unlikely.
- reader 2: level: Fine for B2.2 (passive perfect).

## r20-2-020 · B2.2 · gap · built-in

Task: 'Is the data accurate?' → The editor asked me ___.
Key: {"kind": "gap", "accepted": [["whether the data was accurate", "whether the data were accurate", "if the data was accurate", "if the data were accurate"]]}
- reader 1: another correct answer, not accepted: [['if the data is accurate'], ['whether the data is accurate'], ['whether or not the data was accurate']]
- reader 1: instruction: 'several gaps' but only one ___. Tense (was/is) both correct; 'whether the data was accurate' vs 'if'.
- reader 2: another correct answer, not accepted: [['if the data is accurate'], ['whether the data is accurate'], ['if the data had been accurate']]
- reader 2: instruction: Many correct answers (if/whether, was/were/is); 'is' valid because data still true.
- reader 2: level: B1-level.

## r20-2-021 · B2.2 · mcq · built-in

Task: Which sentence is correct?
options: He apologised for be late. | He apologised for being late. | He apologised of being late. | He apologised to be late.
Key: {"kind": "mcq", "correct": "He apologised for being late.", "wrong": ["He apologised for be late.", "He apologised to be late.", "He apologised of being late."]}
- reader 1: instruction: Too easy for B2.2.
- reader 1: level: Too easy for B2.2.
- reader 1: sense: Option 1 'for be late' nobody writes? weak.
- reader 2: level: B1 level, too easy for B2.2.
- reader 2: sense: 'for be late' / 'of being' are believable but trivially easy.

## r20-2-022 · B2.2 · match · built-in

Task: Match each sentence with the word that says what the speaker did.
left: 'I'll definitely be there on time.' | 'Don't touch the red button!' | 'Why don't we try the new café?' | 'Yes, I broke the vase.'
right: admitted | suggested | warned | promised
Key: {"kind": "match", "pairs": [["'I'll definitely be there on time.'", "promised"], ["'Don't touch the red button!'", "warned"], ["'Why don't we try the new café?'", "suggested"], ["'Yes, I broke the vase.'", "admitted"]]}
- reader 1: instruction: Fine; 'the word that says what the speaker did' fine.
- reader 1: level: Easy for B2.2.

## r20-2-023 · B2.2 · mcq · built-in

Task: Which sentence reports Sam's answer: 'No, I won't work this weekend.'
options: Sam refused working that weekend. | Sam refused to work that weekend. | Sam refused me to work that weekend. | Sam refused that he works this weekend.
Key: {"kind": "mcq", "correct": "Sam refused to work that weekend.", "wrong": ["Sam refused working that weekend.", "Sam refused that he works this weekend.", "Sam refused me to work that weekend."]}
- reader 1: level: Easy for B2.2.
- reader 1: sense: Option 3 'refused me to work' not believable.

## r20-2-024 · B2.2 · gap · built-in

Task: 'Sorry I forgot the meeting.' → Dana apologised ___.
Key: {"kind": "gap", "accepted": [["for forgetting the meeting", "for having forgotten the meeting", "for forgetting about the meeting", "to me for forgetting the meeting", "to me for forgetting about the meeting"]]}
- reader 1: another correct answer, not accepted: [['for having forgotten about the meeting'], ['for missing the meeting']]
- reader 1: instruction: 'several gaps' but only one ___. Several correct answers.
- reader 2: another correct answer, not accepted: [['for having forgotten about the meeting'], ['that she had forgotten the meeting'], ['that he had forgotten the meeting']]
- reader 2: instruction: Number of gaps unclear; several valid answers; 'that she had forgotten' is less common after apologised.

## r20-2-025 · B2.2 · mcq · built-in

Task: Which sentence reports 'You broke the printer!' as an accusation?
options: She accused me to break the printer. | She accused me of breaking the printer. | She accused me that I broke the printer. | She accused me for breaking the printer.
Key: {"kind": "mcq", "correct": "She accused me of breaking the printer.", "wrong": ["She accused me to break the printer.", "She accused me that I broke the printer.", "She accused me for breaking the printer."]}
- reader 1: instruction: 'as an accusation' gives the verb away (accused).
- reader 1: level: Fine.

## r20-2-026 · B2.2 · mcq · built-in

Task: What is the difference? A: 'He insisted on paying.' B: 'He offered to pay.'
options: A: a polite offer. B: a strong demand. | A is about the past, B the future. | A and B mean exactly the same thing. | A: he wouldn't let others pay. B: an offer.
Key: {"kind": "mcq", "correct": "A: he wouldn't let others pay. B: an offer.", "wrong": ["A: a polite offer. B: a strong demand.", "A and B mean exactly the same thing.", "A is about the past, B the future."]}
- reader 1: instruction: Option 1 is the reverse of the truth; options differently formatted. Option 4 is correct but partly given in the second half 'an offer'.
- reader 1: sense: Option 2 (past/future) is implausible.
- reader 2: instruction: Option 4 is longest and most detailed, so it stands out; option 3 'exactly the same' is an obvious throwaway.
- reader 2: sense: Options 1 and 2 are weak distractors.

## r20-2-027 · B2.2 · mcq · built-in

Task: Which sentence reports this: 'I'm very sorry for the delay, and I will make sure it never happens again.'
options: The manager apologised for the delay and promised it not happening again. | The manager apologised the delay and promised that it would not happen again. | The manager apologised for the delay and promised to that it would not happen again. | The manager apologised for the delay and promised that it would not happen again.
Key: {"kind": "mcq", "correct": "The manager apologised for the delay and promised that it would not happen again.", "wrong": ["The manager apologised the delay and promised that it would not happen again.", "The manager apologised for the delay and promised to that it would not happen again.", "The manager apologised for the delay and promised it not happening again."]}
- reader 1: instruction: Sentence long; fine.
- reader 1: sense: Option 3 and 4 are near copies (to that / that).
- reader 2: sense: Distractors 1-3 are clearly broken.

## r20-2-028 · B2.2 · write · built-in

Task: Say what Leo did, in one sentence, without his words in quotes. Leo said: 'It wasn't me who broke it!'
Key: {"kind": "write", "model": "Leo denied breaking it.", "must": ["Use a reporting verb such as *denied* or *insisted.*"]}
- reader 1: instruction: 'what Leo did' hides the reporting verb; 'it' undefined so 'breaking it' works; many answers. 'Denied' is the target but 'said' is also what Leo did.
- reader 2: instruction: 'Say what Leo did' is vague; learner may write 'Leo said that it hadn't been him', which is also correct but may not be accepted.

## r20-2-029 · B2.2 · mcq · built-in

Task: Which sentence reports this: 'If I were you, I'd take the earlier train.'
options: She advised to me take the earlier train. | She advised me to take the earlier train. | She insisted me to take the earlier train. | She suggested me to take the earlier train.
Key: {"kind": "mcq", "correct": "She advised me to take the earlier train.", "wrong": ["She suggested me to take the earlier train.", "She insisted me to take the earlier train.", "She advised to me take the earlier train."]}
- reader 1: instruction: Fine.
- reader 1: level: Easy for B2.2.
- reader 1: sense: Option 1 'advised to me take' not believable.
- reader 2: sense: Option 3 and 4 differ in the verb only; fine.

## r20-2-030 · B2.2 · mcq · built-in

Task: The officer's words: 'I'm not going to tell you who did it.' Which word says what the officer did?
options: refused | suggested | promised | admitted
Key: {"kind": "mcq", "correct": "refused", "wrong": ["promised", "admitted", "suggested"]}
- reader 1: instruction: Fine.
- reader 1: level: Easy for B2.2.
- reader 2: instruction: 'refused' is almost given away by the sentence; easy.
- reader 2: level: Too easy for B2.2 (B1 vocabulary).

## r20-2-031 · B2.2 · mcq · built-in

Task: Which sentence reports the customer's words in formal English: 'The service was terrible.'
options: The customer complained me that the service was terrible. | The customer complained to be terrible the service. | The customer complained about the service had been terrible. | The customer complained that the service had been terrible.
Key: {"kind": "mcq", "correct": "The customer complained that the service had been terrible.", "wrong": ["The customer complained about the service had been terrible.", "The customer complained to be terrible the service.", "The customer complained me that the service was terrible."]}
- reader 1: instruction: 'in formal English' is superfluous: report structure alone decides; 'formal' is confusing.
- reader 1: sense: Option 2 is a random impossible string.
- reader 2: instruction: 'in formal English' is superfluous: only one option is possible English anyway.
- reader 2: sense: Distractors are random ungrammatical strings.

## r20-2-032 · B2.2 · write · built-in

Task: Say what Mia did, in one sentence, without her words in quotes. Mia said to the team: 'Thank you for everything you've done.'
Key: {"kind": "write", "model": "Mia thanked the team for everything they had done.", "must": ["Use *thanked* (or *expressed thanks*)."]}
- reader 1: instruction: 'Say what Mia did' does not push to 'thanked'; many answers could be right.
- reader 2: instruction: Open task; 'thank for' is not hinted, learner may write 'Mia said thank you to the team' (correct, but maybe not accepted).

## r20-2-033 · B2.1 · mcq · built-in

Task: What is the difference? A: 'Where is the manager?' B: 'Do you happen to know where the manager is?'
options: A is more polite than B. | They are the same. | B is more polite and indirect. | B asks about the past.
Key: {"kind": "mcq", "correct": "B is more polite and indirect.", "wrong": ["A is more polite than B.", "B asks about the past.", "They are the same."]}
- reader 1: instruction: 'indirect' is a grammar term; option 3 gives the explanation in its wording.
- reader 1: level: Too easy for B2.1; learner can see 'happen to know' is softer.
- reader 1: sense: Options 1,2,4 are implausible.
- reader 2: instruction: Option 1 is the reverse of option 3 and option 2 is obviously wrong.

## r20-2-034 · B2.1 · mcq · built-in

Task: Which sentence is correct?
options: I was wondering when will my order be delivered? | I was wondering if you could tell me when will my order be delivered? | I was wondering if you could tell me when my order will be delivered. | I was wondering that you could tell me when my order will be delivered.
Key: {"kind": "mcq", "correct": "I was wondering if you could tell me when my order will be delivered.", "wrong": ["I was wondering when will my order be delivered?", "I was wondering if you could tell me when will my order be delivered?", "I was wondering that you could tell me when my order will be delivered."]}
- reader 1: instruction: Fine.
- reader 1: sense: Option 2 and 3 are near copies (differ only in word order).
- reader 2: level: Fine.

## r20-2-035 · B2.1 · write · built-in

Task: Ask very politely, in one sentence, when the report will be ready.
Key: {"kind": "write", "model": "I was wondering if you could tell me when the report will be ready.", "must": ["A polite start: *I was wondering …* / *Could you tell me …*", "Ask about the time: *when the report will be ready*.", "After *when*: the subject first: *when the report will be ready*."]}
- reader 1: instruction: 'the app checks that some forms are used' unclear. Many correct answers; the instruction does not say which structure is checked.
- reader 2: instruction: Open; 'very politely' gives free choice, checker must accept many forms.

## r20-2-036 · B2.2 · mcq · built-in

Task: Which is correct? 'I don't know ___.'
options: what to doing | what to I do | what do I | what to do
Key: {"kind": "mcq", "correct": "what to do", "wrong": ["what to doing", "what do I", "what to I do"]}
- reader 1: instruction: Fine.
- reader 1: level: Too easy for B2.2.
- reader 1: sense: Wrong options are random strings (what to doing, what to I do).
- reader 2: level: A2-B1 level, too easy for B2.2.
- reader 2: sense: Distractors are impossible strings.

## r20-2-037 · B2.2 · mcq · built-in

Task: 'I have no idea how to start.' What does 'how to start' mean?
options: why I started | that I will start | when I started | how I should start
Key: {"kind": "mcq", "correct": "how I should start", "wrong": ["when I started", "why I started", "that I will start"]}
- reader 1: instruction: Fine.
- reader 1: level: Easy for B2.2.
- reader 1: sense: Distractors (why I started, when I started) are not believable.
- reader 2: level: B1 level, too easy for B2.2.

## r20-2-038 · B2.2 · text · built-in

Task: Say it shorter with *to*: Can you tell me how I can get to the museum?
Key: {"kind": "text", "accepted": [["Can you tell me how to get to the museum?"]]}
- reader 1: another correct answer, not accepted: [['Could you tell me how to get to the museum?']]
- reader 1: instruction: Fine; 'shorter' ok. Can/Could swap would be accepted? (Modal could change meaning slightly.)
- reader 1: level: Easy for B2.2.
- reader 2: another correct answer, not accepted: [['Could you tell me how to get to the museum?'], ['Can you tell me the way to the museum?']]
- reader 2: instruction: 'with to' names the form: answer is nearly given; 'Could' also fine; 'Can you tell me how I can get' only needs the swap.
- reader 2: level: B1 level.

## r20-2-039 · B2.2 · mcq · built-in

Task: Which sentence is correct?
options: It remains unclear who is the responsible for the delay. | It remains unclear who is responsible for the delay. | It remains unclear who does responsible for the delay. | It remains unclear who responsible is for the delay.
Key: {"kind": "mcq", "correct": "It remains unclear who is responsible for the delay.", "wrong": ["It remains unclear who is the responsible for the delay.", "It remains unclear who responsible is for the delay.", "It remains unclear who does responsible for the delay."]}
- reader 1: instruction: Fine.
- reader 1: level: Too easy for B2.2.
- reader 1: sense: Option 3 (who does responsible) is a form nobody writes.

## r20-2-040 · B2.2 · write · built-in

Task: Write a sentence with 'I have no idea' and a question word (how, what, where, when, who or why).
Key: {"kind": "write", "model": "I have no idea how long the meeting will take.", "must": ["Use *I have no idea* + a question word."]}
- reader 1: instruction: 'the app checks that some forms are used' unclear; any question word with clause counts.
- reader 2: instruction: Open; 'I have no idea' plus any question word with correct word order.

## r20-2-041 · B2.2 · mcq · built-in

Task: Choose the correct option: ___ remains unclear.
options: Whether will he attend | Will he attend | Whether he will attend | That will he attend
Key: {"kind": "mcq", "correct": "Whether he will attend", "wrong": ["Will he attend", "Whether will he attend", "That will he attend"]}
- reader 1: instruction: Fine.
- reader 1: sense: Option 4 and 1 plausible errors.

## r20-2-042 · B2.2 · text · built-in

Task: Combine the two sentences without changing their meaning: Who made the decision? It's not clear.
Key: {"kind": "text", "accepted": [["It's not clear who made the decision.", "It is not clear who made the decision.", "Who made the decision is not clear.", "It's unclear who made the decision.", "It is unclear who made the decision."]]}
- reader 1: another correct answer, not accepted: [['It remains unclear who made the decision.']]
- reader 1: instruction: 'Combine' is natural. Many correct sentences; 'without changing meaning' ok.
- reader 2: instruction: Combine instruction vague about which structure; many answers.

## r20-2-043 · B2.2 · mcq · built-in

Task: You write a report: 'The question is ___.' Choose the correct option.
options: whether is the project worth the cost | is the project worth the cost | whether the project is worth the cost | if is the project worth the cost
Key: {"kind": "mcq", "correct": "whether the project is worth the cost", "wrong": ["is the project worth the cost", "if is the project worth the cost", "whether is the project worth the cost"]}
- reader 1: instruction: 'You write a report' superfluous.
- reader 1: sense: Option 4 plausible but wrong.
- reader 2: level: Fine.

## r20-2-044 · B2.2 · mcq · built-in

Task: 'Whatever he says, don't sign it.' What does 'whatever' mean here?
options: it does not matter what he says | it matters a lot what he says | he says everything he thinks | he never says what he means
Key: {"kind": "mcq", "correct": "it does not matter what he says", "wrong": ["he says everything he thinks", "it matters a lot what he says", "he never says what he means"]}
- reader 1: level: Fine.
- reader 1: sense: Options 3 and 4 are not believable.
- reader 2: sense: Fine.

## r20-2-045 · B2.2 · text · built-in

Task: Write one sentence that starts with *Who…*: It doesn't matter who calls. Don't answer.
Key: {"kind": "text", "accepted": [["Whoever calls, don't answer.", "Whoever calls, do not answer."]]}
- reader 1: another correct answer, not accepted: [["Whoever it is, don't answer."], ['Whoever it is, do not answer.'], ["Who calls doesn't matter."], ["Who calls doesn't matter; don't answer."]]
- reader 1: instruction: Instruction confusing: 'starts with Who…' hides that whoever is wanted ('Who calls doesn't matter' also fits); 'one sentence' unclear with 'Don't answer'. 'Whoever' not named.
- reader 2: another correct answer, not accepted: [["Who calls doesn't matter."], ["Who calls doesn't matter, so don't answer."], ["Who calls is not important; don't answer."]]
- reader 2: instruction: Unclear: 'starts with Who...' vs 'Whoever'; unclear whether to include 'Don't answer'; two sentences given to write one. Gives no clue which structure is wanted.

## r20-2-046 · B2.2 · write · built-in

Task: Write a sentence with 'whoever', 'whatever' or 'wherever' to describe a flexible rule at your workplace.
Key: {"kind": "write", "model": "You can sit wherever you like.", "must": ["Use *whoever, whatever, wherever* or similar."]}
- reader 1: instruction: 'flexible rule' is vague; 'the app checks that some forms are used' unclear.
- reader 2: instruction: Open; 'flexible rule' vague.

## r20-2-047 · B2.1 · order · built-in

Task: Link a different past decision to a present result. Start with If I had and put now at the end.
word_cards: be | doctor | a | studied | had | would | now | I | medicine | if | I
Key: {"kind": "order", "sentence": "if I had studied medicine I would be a doctor now", "also": []}
- reader 1: instruction: 'Link a different past decision to a present result' is unnatural English. 'Start with If I had' and 'now at the end' give most of it away; only 'studied medicine, I would be a doctor' to order.
- reader 1: level: Fine for B2.1.
- reader 2: instruction: 'Link a different past decision' is confusing wording; start and end are given, so the answer is nearly given. Task needs only matching cards.
- reader 2: level: B2.1 ok (mixed conditional).

## r20-2-048 · B2.2 · order · built-in

Task: Put the words in order. Start with *Had I*.
word_cards: delay | about | you | known | have | called | would | I | had | the | I
Key: {"kind": "order", "sentence": "had I known about the delay I would have called you", "also": []}
- reader 1: another correct answer, not accepted: ['Had I called you about the delay, I would have known.']
- reader 1: instruction: Fine.
- reader 1: level: Fine.
- reader 1: sense: The alternative sentence is grammatical but illogical.
- reader 2: another correct answer, not accepted: [['Had I called you about the delay, I would have known.']]
- reader 2: instruction: Two 'I' cards; ordering ambiguous grammatically but only one makes sense.
- reader 2: level: Inverted third conditional is fine for B2.2.

## r20-2-049 · B2.2 · order · built-in

Task: Report an apology. Start with She.
word_cards: for | the | missing | meeting | she | apologised
Key: {"kind": "order", "sentence": "she apologised for missing the meeting", "also": []}
- reader 1: another correct answer, not accepted: ['She apologised for the missing meeting.']
- reader 1: instruction: 'Report an apology' with 6 cards, start given: only copying.
- reader 1: level: Too easy for B2.2 (A2/B1).
- reader 1: sense: 'the missing meeting' is grammatical but nonsense.
- reader 2: instruction: Almost nothing to decide; 6 cards, start given.
- reader 2: level: Too easy for B2.2.
- reader 2: sense: 'She apologised for the meeting missing' not possible; fine.

## r20-2-050 · B2.2 · order · built-in

Task: Put the words in order. Start with *Whether*.
word_cards: uncertain | work | whether | the | will | plan | remains
Key: {"kind": "order", "sentence": "whether the plan will work remains uncertain", "also": []}
- reader 1: instruction: Start 'Whether' given.
- reader 1: level: Fine.
- reader 2: sense: 'work' plan ambiguity ('the work'?) no; fine.

## r20-2-051 · B2.2 · gap · a2-forms-1.csv:28

Task: ___ she ___ earlier, she would have caught the train.
word_cards: Did | left | Had | leave
Key: {"kind": "gap", "accepted": [["Had"], ["left"]]}
- reader 1: instruction: Only the verb forms differ; 'Did' gives a clear wrong option but 'Had' is obvious from 'would have caught'.
- reader 1: level: Fine for B2.2.

## r20-2-052 · B2.1 · mcq · compare-past-1.csv:47

Task: Choose the correct option: The ground was wet. It ___ in the night.
options: had been raining | has been raining | had been rain
Key: {"kind": "mcq", "correct": "had been raining", "wrong": ["has been raining", "had been rain"]}
- reader 1: instruction: Fine.
- reader 1: level: Fine.
- reader 2: level: Fine.

## r20-2-053 · B2.2 · mcq · compare-past-1.csv:48

Task: Choose the correct option: When the bus finally came, we ___ in the rain for half an hour.
options: had been stand | have been standing | had been standing
Key: {"kind": "mcq", "correct": "had been standing", "wrong": ["have been standing", "had been stand"]}
- reader 1: instruction: Fine.
- reader 1: level: Fine.
- reader 1: sense: Option 1 'had been stand' is a form nobody writes.
- reader 2: level: Same grammar as 52 and 59, B2.1 not B2.2.

## r20-2-054 · B2.2 · mcq · compare-past-1.csv:49

Task: Choose the correct option: She was lying on the sofa. She was tired because she ___ hard.
options: has been working | had been working | had working
Key: {"kind": "mcq", "correct": "had been working", "wrong": ["has been working", "had working"]}
- reader 1: instruction: Fine.
- reader 1: level: Fine.
- reader 1: sense: Option 3 'had working' is not believable.
- reader 2: a wrong option that fits: 'had worked' not offered; none fit.
- reader 2: level: B2.1 level.

## r20-2-055 · B2.1 · gap · compare-past-1.csv:50

Task: We ___ tennis for half an hour when it started to rain.
word_cards: have been playing | had been playing | had been played | are playing
Key: {"kind": "gap", "accepted": [["had been playing"]]}
- reader 1: instruction: Fine.
- reader 1: level: Fine.

## r20-2-056 · B2.1 · gap · compare-past-1.csv:51

Task: Tom was tired when he got home. He ___ hard all day. (work)
Key: {"kind": "gap", "accepted": [["had been working", "had worked"]]}
- reader 1: another correct answer, not accepted: [["'d been working"], ["'d worked"], ['worked']]
- reader 1: instruction: Several tenses correct: 'had worked' fits as well.
- reader 2: another correct answer, not accepted: [["'d been working"]]
- reader 2: instruction: '(work)' only; 'had worked hard all day' is also correct.

## r20-2-057 · B2.1 · gap · compare-past-1.csv:52

Task: Yesterday was busy. By lunchtime she ___ ten emails. (write)
Key: {"kind": "gap", "accepted": [["had written"]]}
- reader 1: another correct answer, not accepted: [["'d written"]]
- reader 1: instruction: Fine.
- reader 2: another correct answer, not accepted: [['had been writing']]
- reader 2: instruction: 'had been writing ten emails' is less natural but possible; count makes simple form preferred.
- reader 2: level: Fine.

## r20-2-058 · B2.1 · gap · compare-past-1.csv:53

Task: James was out of breath when he came in. He ___. (run)
Key: {"kind": "gap", "accepted": [["had been running"]]}
- reader 1: another correct answer, not accepted: [['had run'], ["'d been running"], ["'d run"]]
- reader 1: instruction: Both 'had been running' and 'had run' are correct.
- reader 2: another correct answer, not accepted: [['had run'], ["'d been running"], ["'d run"]]
- reader 2: instruction: 'He had run' also correct; instruction does not prefer either.

## r20-2-059 · B2.2 · gap · compare-past-1.csv:54

Task: At last the bus came. I ___ for twenty minutes.
word_cards: had been waited | am waiting | have been waiting | had been waiting
Key: {"kind": "gap", "accepted": [["had been waiting"]]}
- reader 1: a wrong option that fits: have been waiting (fits in speech: 'I've been waiting for twenty minutes' said to someone after the bus came)
- reader 1: instruction: The context 'At last the bus came' allows both 'had been' and 'have been'.
- reader 2: a wrong option that fits: have been waiting (marginal: possible in direct speech to someone after the bus came, less natural narrative)
- reader 2: instruction: Instruction needs a clue; 'At last the bus came' sets past.
- reader 2: level: B1-B2.1 level, not B2.2; duplicate of 053.

## r20-2-060 · B2.2 · gap · compare-past-1.csv:55

Task: I hope the bus comes soon. I ___ for twenty minutes. (wait)
Key: {"kind": "gap", "accepted": [["have been waiting", "have waited"]]}
- reader 1: instruction: Fine; 'have waited' less natural.
- reader 2: instruction: 'have waited for twenty minutes' also correct but less natural.
- reader 2: level: B1 level (present perfect continuous), too easy for B2.2.

