# Blind check r20b-1: flags for the judge

53 tasks, 2 readers.

## r20b-1-001 · B2.1 · gap · built-in

Task: Our company will never change its fixed hours. If it ___ more flexible hours, people ___ happier. (offer / be)
Key: {"kind": "gap", "accepted": [["offered", "were to offer"], ["would be", "'d be", "might be", "could be"]]}
- reader 1: another correct answer, not accepted: [['were offering', 'would be'], ['offered', 'would feel']]
- reader 1: instruction: Only the verb-form hint; 'were to offer' / 'were offering' also fit.

## r20b-1-003 · B2.2 · gap · built-in

Task: He drove too fast just once and lost his licence. If he ___ (not / drive) so fast that day, he ___ (not / lose) it.
Key: {"kind": "gap", "accepted": [["hadn't been driving", "had not been driving", "hadn't driven", "had not driven"], ["wouldn't have lost", "would not have lost", "'d not have lost", "might not have lost", "mightn't have lost"]]}
- reader 1: instruction: (not / drive) shows negative + base verb, but tense still has to be found: fine.

## r20b-1-005 · B2.2 · mcq · built-in

Task: Which sentence is NOT correct?
options: If I am more careful, I wouldn't have lost my keys. | If she spoke French, she would have got the job in Paris. | If I hadn't eaten so much, I wouldn't feel sick now. | If he weren't so shy, he would have asked her to dance.
Key: {"kind": "mcq", "correct": "If I am more careful, I wouldn't have lost my keys.", "wrong": ["If she spoke French, she would have got the job in Paris.", "If I hadn't eaten so much, I wouldn't feel sick now.", "If he weren't so shy, he would have asked her to dance."]}
- reader 1: sense: Options 2 and 4 are mixed conditionals (present condition, past result): correct, but many learners will think they are wrong; they are not clearly marked as a trap. Option 1 is an unlikely mistake? (plausible though).
- reader 2: a wrong option that fits: Option 2 (If she spoke French, she would have got the job) is a possible mixed conditional (general ability); less usual but not wrong. Option 4 is also fine (weren't = general trait).
- reader 2: instruction: Two other options are arguably acceptable mixed conditionals, so 'NOT correct' is less clear-cut.

## r20b-1-006 · B2.2 · mcq · built-in

Task: Which sentence is NOT correct?
options: Had she known, she would have stayed. | Hadn't I moved here, I'd be in Riga now. | Were I braver, I would have said no. | Had the train been on time, we would be home by now.
Key: {"kind": "mcq", "correct": "Hadn't I moved here, I'd be in Riga now.", "wrong": ["Had she known, she would have stayed.", "Had the train been on time, we would be home by now.", "Were I braver, I would have said no."]}
- reader 1: a wrong option that fits: Were I braver, I would have said no: mixed type, acceptable (Were I braver = if I were braver, past result); borderline, some teachers would call it wrong.
- reader 1: sense: 'Hadn't I moved' is a form nobody writes; the standard negative inversion is 'Had I not moved'. A learner could pick option 3 instead because the mix of Were + would have looks odd.
- reader 2: a wrong option that fits: Option 3 (Were I braver, I would have said no) is acceptable mixed conditional.
- reader 2: sense: Negative inversion with contraction 'Hadn't I moved' is not standard (Had I not moved); but Option 3 mixing 'Were I braver' + would have said no is borderline, so two options are doubtful.

## r20b-1-007 · B2.1 · mcq · built-in

Task: Which sentence is NOT correct?
options: She told me she had lost her keys. | He said he was working from home. | She told that she would be late. | They told us the shop was closed.
Key: {"kind": "mcq", "correct": "She told that she would be late.", "wrong": ["He said he was working from home.", "They told us the shop was closed.", "She told me she had lost her keys."]}
- reader 1: level: Too easy for B2.1 (told + object, A2/B1 point).

## r20b-1-008 · B2.2 · mcq · built-in

Task: Eva's question to you: 'Where should I park?' Which sentence reports it?
options: She asked me where should she park. | She asked me where she should park. | She asked me where she should to park.
Key: {"kind": "mcq", "correct": "She asked me where she should park.", "wrong": ["She asked me where should she park.", "She asked me where she should to park."]}
- reader 1: level: Reported question word order is B1; too easy for B2.2.
- reader 1: sense: Option 1 and 2 are near-copies; option 3 'should to park' is a form few learners write.

## r20b-1-009 · B2.2 · gap · built-in

Task: 'Is the data accurate?' → The editor asked me ___.
Key: {"kind": "gap", "accepted": [["whether the data was accurate", "whether the data were accurate", "if the data was accurate", "if the data were accurate", "whether or not the data was accurate", "whether or not the data were accurate"]]}
- reader 1: another correct answer, not accepted: [['whether the data is accurate'], ['if the data is accurate']]
- reader 1: instruction: Open multi-word gap with no hint: many correct variants (if/whether, was/were/is).
- reader 2: another correct answer, not accepted: [['if the data is accurate'], ['whether the data is accurate']]
- reader 2: instruction: Gap takes several words; clue-less, many equivalents (if/whether, was/were/is).

## r20b-1-010 · B2.2 · gap · built-in

Task: 'Sorry I forgot the meeting.' → Dana apologised ___.
Key: {"kind": "gap", "accepted": [["for forgetting the meeting", "for having forgotten the meeting", "for forgetting about the meeting", "to me for forgetting the meeting", "to me for forgetting about the meeting", "for having forgotten about the meeting", "to me for having forgotten the meeting", "to me for having forgotten about the meeting"]]}
- reader 1: another correct answer, not accepted: [['that she had forgotten the meeting'], ['for missing the meeting']]
- reader 1: instruction: No structure is asked for, so several reporting patterns are correct (for + -ing, that-clause).
- reader 2: instruction: Several words in gap; many correct variants.

## r20b-1-012 · B2.2 · mcq · built-in

Task: Which sentence reports the customer's words: 'The service was terrible.'
options: The customer complained me that the service was terrible. | The customer complained that the service had been terrible. | The customer complained about the service had been terrible.
Key: {"kind": "mcq", "correct": "The customer complained that the service had been terrible.", "wrong": ["The customer complained about the service had been terrible.", "The customer complained me that the service was terrible."]}
- reader 1: a wrong option that fits: 'The customer complained that the service was terrible' is not offered; option 2 fits (and would also be fine with 'was').
- reader 1: sense: Option 1 'complained me' and option 3 are not believable-learner-level mistakes equally; fine.
- reader 2: sense: 'was terrible' would also be fine in the report, but only one option is grammatical so OK.

## r20b-1-013 · B2.2 · mcq · built-in

Task: Which sentence is correct?
options: It remains unclear who is responsible for the delay. | It remains unclear who responsible is for the delay. | It remains unclear who is the responsible for the delay.
Key: {"kind": "mcq", "correct": "It remains unclear who is responsible for the delay.", "wrong": ["It remains unclear who is the responsible for the delay.", "It remains unclear who responsible is for the delay."]}
- reader 1: level: Indirect-question word order is B1; too easy for B2.2.
- reader 1: sense: Options 2 and 3 are believable but option 2 rarely written at this level.

## r20b-1-015 · B2.2 · text · built-in

Task: Make it one sentence that starts with *Who…*: It doesn't matter who calls. Don't answer.
Key: {"kind": "text", "accepted": [["Whoever calls, don't answer.", "Whoever calls, do not answer.", "Whoever it is, don't answer.", "Whoever it is, do not answer.", "Who calls doesn't matter, so don't answer.", "Who calls does not matter, so do not answer."]]}
- reader 1: another correct answer, not accepted: [["Whoever calls, don't pick up."], ["Whoever calls, don't answer it."], ["Whoever may call, don't answer."]]
- reader 1: instruction: 'Starts with Who...' gives away Whoever.
- reader 1: sense: Instruction text 'It doesn't matter who calls. Don't answer.' is fine.
- reader 2: answer not accepted: Who calls doesn't matter, don't answer.
- reader 2: another correct answer, not accepted: ["Who calls doesn't matter; don't answer.", "Who calls doesn't matter. Don't answer.", "Who calls, don't answer."]
- reader 2: instruction: Unclear what is wanted: 'starts with Who' and 'one sentence' leaves the structure open; the natural result is 'Whoever calls, don't answer' but that is not 'Who'. Task is confusing.
- reader 2: sense: 'Who calls doesn't matter, don't answer' is a comma splice; 'Who calls, don't answer' is odd English.
- the readers disagree

## r20b-1-016 · B2.2 · order · built-in

Task: Put the words in order.
word_cards: missing | the | meeting | apologised | for | she
Key: {"kind": "order", "sentence": "she apologised for missing the meeting", "also": []}
- reader 1: instruction: Too easy: only one natural order, almost copying; no real choice.
- reader 1: level: B1 sentence at B2.2.
- reader 2: another correct answer, not accepted: ['she apologised for the missing meeting (grammatical but meaningless)']
- reader 2: instruction: No capital letter/full stop cue; fine.
- reader 2: level: Too easy for B2.2.

## r20b-1-018 · B2.1 · gap · compare-past-1.csv:53

Task: James was out of breath when he came in. He ___. (run)
Key: {"kind": "gap", "accepted": [["had been running", "had run", "'d run", "'d been running"]]}
- reader 1: another correct answer, not accepted: [['must have been running'], ['must have run']]
- reader 1: instruction: No tense is requested; 'He ran / was running / had run' all depend on context, so several answers are correct. Tense should be named or the context built (before he came in).

## r20b-1-019 · B2.1 · order · compare-past-1.csv:60

Task: Put the words in order.
word_cards: when | had | been | for | down | hours | the | we | driving | broke | car
Key: {"kind": "order", "sentence": "we had been driving for hours when the car broke down", "also": ["when the car broke down we had been driving for hours", "the car broke down when we had been driving for hours", "when we had been driving for hours the car broke down"]}
- reader 1: another correct answer, not accepted: [['when we had been driving for hours the car broke down'], ['the car broke down when we had been driving for hours'], ['when the car broke down we had been driving for hours']]
- reader 1: instruction: 'hours' without number is slightly odd but fine.

## r20b-1-023 · B2.2 · text · conjunctions-1.csv:107

Task: Rewrite with *owing to*: The flight was late because the weather was bad.
Key: {"kind": "text", "accepted": [["The flight was late owing to the bad weather.", "The flight was late owing to bad weather.", "Owing to the bad weather, the flight was late.", "Owing to bad weather, the flight was late.", "Owing to the weather being bad, the flight was late.", "The flight was late owing to the weather being bad.", "The flight was late owing to the fact that the weather was bad.", "Owing to the fact that the weather was bad, the flight was late."]]}
- reader 2: another correct answer, not accepted: ["Owing to the weather's being bad, the flight was late."]

## r20b-1-024 · B2.1 · order · conjunctions-1.csv:112

Task: Put the words in order.
word_cards: result | and | was | as | train | the | missed | concert | a | we | cancelled | the
Key: {"kind": "order", "sentence": "the train was cancelled and as a result we missed the concert", "also": ["the train was cancelled and we missed the concert as a result"]}
- reader 1: answer not accepted: we missed the train and as a result the concert was cancelled
- reader 1: another correct answer, not accepted: ['we missed the train and, as a result, the concert was cancelled', 'the concert was cancelled and we missed the train as a result', 'we missed the train and the concert was cancelled as a result', 'the concert was cancelled as a result and we missed the train']
- reader 1: sense: Illogical: missing the train does not cause the concert to be cancelled (unless they are the band). Two events with no cause link; weak model sentence.
- reader 2: another correct answer, not accepted: ['we missed the train and as a result the concert was cancelled', 'the concert was cancelled and as a result we missed the train', 'we missed the concert and as a result the train was cancelled']
- reader 2: sense: The only logical one is 'the train was cancelled and as a result we missed the concert'; 'we missed the train and as a result the concert was cancelled' is illogical (our missing a train does not cancel a concert); several orders fit all cards.
- the readers disagree

## r20b-1-025 · B2.2 · order · learn-drag-3.csv:6

Task: Put the words in order.
word_cards: would | be | we | had | on | earlier | the | we | now | beach | booked
Key: {"kind": "order", "sentence": "had we booked earlier we would be on the beach now", "also": ["we would be on the beach now had we booked earlier", "had we booked earlier we would now be on the beach", "we would now be on the beach had we booked earlier", "now we would be on the beach had we booked earlier", "had we booked earlier now we would be on the beach"]}
- reader 1: instruction: No 'if' card, so the learner must find the inversion without being told; fine for B2.2, but a learner expecting 'if' will be stuck. Duplicate card 'we' is clear.
- reader 2: answer not accepted: we would be on the beach now if we had booked earlier
- reader 2: another correct answer, not accepted: ['if we had booked earlier we would be on the beach now']
- reader 2: instruction: No capital/comma cues; many orders fit.
- the readers disagree

## r20b-1-026 · B2.1 · gap · learn-drag-3.csv:11

Task: He ___ ___ that the shop was closed.
word_cards: me | that | told | said
Key: {"kind": "gap", "accepted": [["told"], ["me"]]}
- reader 1: a wrong option that fits: said / that fit as a second answer ('He said that the shop was closed').
- reader 1: instruction: Ambiguous: two valid fillings; the cards allow both told+me and said+that.
- reader 2: level: Too easy for B2.1.

## r20b-1-027 · B2.2 · order · learn-drag-3.csv:28

Task: Put the words in order.
word_cards: the | a | quiz | gets | whoever | free | wins | dinner
Key: {"kind": "order", "sentence": "whoever wins the quiz gets a free dinner", "also": []}
- reader 1: another correct answer, not accepted: ['whoever gets a free dinner wins the quiz', 'whoever gets the quiz wins a free dinner']
- reader 1: sense: Alternatives are grammatical but silly; only the first is logical.
- reader 2: another correct answer, not accepted: ['whoever gets a free dinner wins the quiz']
- reader 2: sense: Second order is grammatical but illogical.

## r20b-1-028 · B2.2 · order · learn-drag-4.csv:23

Task: Put the words in order.
word_cards: left | I'd | traffic | about | I | if | would've | the | known | earlier
Key: {"kind": "order", "sentence": "if I'd known about the traffic I would've left earlier", "also": ["I would've left earlier if I'd known about the traffic", "if I'd known about the traffic earlier I would've left", "I would've left if I'd known about the traffic earlier", "if I'd known earlier about the traffic I would've left", "I would've left if I'd known earlier about the traffic"]}
- reader 1: level: Contracted cards (I'd, would've) fine.

## r20b-1-030 · B2.1 · order · learn-drag-4.csv:38

Task: Put the words in order.
word_cards: send | to | asked | Lena | her | the | me | invoice
Key: {"kind": "order", "sentence": "Lena asked me to send her the invoice", "also": ["Lena asked her to send me the invoice"]}
- reader 1: instruction: Another person could be asked: 'Lena asked her to send me the invoice' is also correct.
- reader 1: level: Too easy for B2.1 (ask + object + to-infinitive, A2/B1).
- reader 2: level: Too easy for B2.1.

## r20b-1-031 · B2.1 · gap · twins-1.csv:44

Task: The city has no money for cycle lanes, so it won't build any. If it ___ more cycle lanes, more people ___ by bike. (build / travel)
Key: {"kind": "gap", "accepted": [["built", "were to build"], ["would travel", "might travel", "could travel", "would be travelling"]]}
- reader 1: another correct answer, not accepted: [['built', "'d travel"], ['were building', 'would travel']]
- reader 1: instruction: Fine; 'were to build' also fits.
- reader 2: another correct answer, not accepted: [['built', "'d travel"]]

## r20b-1-033 · B2.2 · gap · twins-1.csv:57

Task: ___ it not been for the rain, the match would have finished on time.
word_cards: Were | Had | Should
Key: {"kind": "gap", "accepted": [["Had"]]}
- reader 2: a wrong option that fits: Were/Should do not fit.

## r20b-1-037 · B2.2 · order · twins-2.csv:48

Task: Put the words in order.
word_cards: she | years | when | had | for | French | learning | moved | she | been
Key: {"kind": "order", "sentence": "she had been learning French for years when she moved", "also": ["when she moved she had been learning French for years", "she moved when she had been learning French for years", "when she had been learning French for years she moved", "for years she had been learning French when she moved"]}
- reader 1: sense: The last alternative is grammatical but changes the meaning; the first is the sensible model.
- reader 2: sense: Alternatives other than the first are less natural but grammatical.

## r20b-1-038 · B2.1 · mcq · twins-3.csv:13

Task: Which sentence is correct?
options: The agent told I might need a visa. | The agent said I might need a visa. | The agent said I might to need a visa. | The agent said me I might need a visa.
Key: {"kind": "mcq", "correct": "The agent said I might need a visa.", "wrong": ["The agent told I might need a visa.", "The agent said I might to need a visa.", "The agent said me I might need a visa."]}
- reader 1: level: Too easy for B2.1 (said/told patterns, A2/B1).

## r20b-1-040 · B2.2 · text · twins-3.csv:23

Task: Join the sentences: She didn't know. Who should she ask?
Key: {"kind": "text", "accepted": [["She didn't know who to ask.", "She didn't know whom to ask.", "She didn't know who she should ask.", "She didn't know whom she should ask."]]}
- reader 1: another correct answer, not accepted: ["She didn't know who she could ask.", "She didn't know who she ought to ask."]
- reader 2: another correct answer, not accepted: ["She didn't know who she ought to ask."]

## r20b-1-041 · B2.2 · text · twins-3.csv:27

Task: Rewrite as one sentence. Start with *I'll support you*: It doesn't matter what you decide. I'll support you.
Key: {"kind": "text", "accepted": [["I'll support you whatever you decide.", "I will support you whatever you decide.", "I'll support you no matter what you decide.", "I will support you no matter what you decide.", "I'll support you whichever way you decide.", "I'll support you however you decide.", "I'll support you regardless of what you decide."]]}
- reader 1: another correct answer, not accepted: ["I'll support you whatever decision you make."]
- reader 1: instruction: 'Start with I'll support you' gives the start; the target is whatever/no matter what, not named, so several answers.

## r20b-1-042 · B2.1 · gap · typical-b2c1-1.csv:6

Task: If you had asked me, I ___ you with the move. (help)
Key: {"kind": "gap", "accepted": [["would have helped", "'d have helped", "might have helped", "could have helped"]]}
- reader 1: instruction: Open to could/might have helped (modal not fixed).

## r20b-1-043 · B2.1 · gap · typical-b2c1-1.csv:11

Task: Could you tell me what time the museum ___ on Sundays? (open)
Key: {"kind": "gap", "accepted": [["opens"]]}
- reader 1: another correct answer, not accepted: [['will open']]

## r20b-1-044 · B2.1 · gap · typical-b2c1-1.csv:14

Task: I set two alarms in order ___ my early flight. (not / miss)
Key: {"kind": "gap", "accepted": [["not to miss", "to not miss"]]}
- reader 1: another correct answer, not accepted: [["that I don't miss"], ["that I won't miss"], ["that I wouldn't miss"]]
- reader 1: instruction: (not / miss) reveals negative; 'that I won't miss' is also correct (less common).

## r20b-1-046 · B2.2 · gap · typical-b2c1-1.csv:22

Task: She was smiling when I saw her, but her eyes were red because she ___ . (cry)
Key: {"kind": "gap", "accepted": [["had been crying", "'d been crying", "had cried", "'d cried"]]}
- reader 1: instruction: No tense named; 'had cried' also correct.

## r20b-1-047 · B2.2 · gap · typical-b2c1-1.csv:25

Task: Sales fell sharply; ___ , the company cut its prices.
Key: {"kind": "gap", "accepted": [["therefore", "as a result", "consequently", "thus", "as a consequence", "accordingly", "hence", "for this reason", "in response"]]}
- reader 1: instruction: Open gap with no hint: many linkers are correct; the target is not determined.
- reader 1: sense: Cutting prices is a response, so 'in response' is also logical.
- reader 2: another correct answer, not accepted: [['because of this']]
- reader 2: instruction: Open gap: many linkers fit; only one is probably expected.

## r20b-1-048 · B2.2 · gap · typical-b2c1-1.csv:30

Task: ___ we left ten minutes earlier, we would have caught the ferry. (have)
Key: {"kind": "gap", "accepted": [["Had"]]}
- reader 1: another correct answer, not accepted: [['If']]
- reader 1: instruction: '(have)' gives it away; 'If' is marginal (If we left... would have caught: non-standard, not full alternative).
- reader 2: instruction: The hint '(have)' gives the answer away; 'Had we left' with 'left' already in the text.

## r20b-1-049 · B2.2 · gap · typical-b2c1-1.csv:33

Task: My father insisted ___ us to the airport. (drive)
Key: {"kind": "gap", "accepted": [["on driving", "that he drive", "that he should drive", "he should drive", "that he would drive", "he would drive", "that he'd drive", "he'd drive"]]}
- reader 1: instruction: 'on taking' ignores (drive) hint, so fine.

## r20b-1-051 · B2.2 · gap · typical-b2c1-1.csv:40

Task: Our holiday plans depend on ___ my boss gives me the week off.
Key: {"kind": "gap", "accepted": [["whether"]]}
- reader 1: another correct answer, not accepted: [['if'], ['whether or not']]
- reader 1: instruction: 'if' is possible after depend on in informal English.
- reader 2: another correct answer, not accepted: [['if']]
- reader 2: instruction: 'depend on if' is informal but common.

