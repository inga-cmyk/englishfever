# Blind check r20-5: flags for the judge

60 tasks, 2 readers.

## r20-5-001 · B2.1 · order · twins-2.csv:7

Task: Put the words in order.
word_cards: would | a | money | flat | I | more | own | now | saved | if | had | I
Key: {"kind": "order", "sentence": "if I had saved more money I would own a flat now", "also": ["I would own a flat now if I had saved more money", "now if I had saved more money I would own a flat", "now I would own a flat if I had saved more money", "if I had saved more money now I would own a flat", "if I had saved more money I would now own a flat", "I would now own a flat if I had saved more money"]}
- reader 2: instruction: No capital letter or comma cue, fine.

## r20-5-002 · B2.1 · mcq · twins-2.csv:8

Task: Choose the correct option: I didn't charge my phone last night. Imagine a different past and its result now.
options: If I would have charged my phone, it would be working now. | If I charged my phone, it would be working now. | If I had charged my phone, it would be working now. | If I had charged my phone, it would have been working now.
Key: {"kind": "mcq", "correct": "If I had charged my phone, it would be working now.", "wrong": ["If I charged my phone, it would be working now.", "If I had charged my phone, it would have been working now.", "If I would have charged my phone, it would be working now."]}
- reader 1: instruction: 'Imagine a different past and its result now' gives away the mixed form; fine but telling.

## r20-5-003 · B2.1 · gap · twins-2.csv:10

Task: Write one word in each gap: I did not take that course. If I ___ ___ it, I ___ ___ more about design now. (take / know)
Key: {"kind": "gap", "accepted": [["had"], ["taken"], ["would", "could", "might"], ["know"]]}
- reader 1: answer not accepted: ['had taken', 'would know']
- reader 1: another correct answer, not accepted: [['had taken', 'could know'], ['had taken', 'might know'], ["'d taken", 'would know']]
- reader 1: instruction: Gaps need 2 words each but 'had taken' = one gap of two words: unclear whether 'had' and 'taken' go in separate gaps (3 gaps vs 4 shown: 4 blanks, so answers are single words: had / taken / would / know). Clear only if split by word.
- reader 2: instruction: Hints (take / know) are bare infinitives for four gaps; learner must guess would/could/might. Tense cues given by 'now'.
- the readers disagree

## r20-5-004 · B2.2 · order · twins-2.csv:11

Task: Put the words in order.
word_cards: for | she | losing | apologised | luggage | my
Key: {"kind": "order", "sentence": "she apologised for losing my luggage", "also": ["for losing my luggage she apologised"]}
- reader 1: instruction: Only one order; too easy.
- reader 1: level: Far too easy for B2.2: 6 cards, A2/B1 sentence, apologise for + -ing is B1.
- reader 2: level: Far too easy for B2.2: 6 cards, B1 structure, one possible order.

## r20-5-005 · B2.2 · mcq · twins-2.csv:12

Task: Which sentence is NOT correct?
options: I promised to call back later. | He suggested to meet on Friday. | She offered to drive us home. | They admitted breaking the window.
Key: {"kind": "mcq", "correct": "He suggested to meet on Friday.", "wrong": ["She offered to drive us home.", "They admitted breaking the window.", "I promised to call back later."]}
- reader 2: level: Too easy for B2.2 (basic verb patterns, B1).

## r20-5-006 · B2.2 · mcq · twins-2.csv:13

Task: Which sentence reports this: 'No, I won't take another exam.'
options: He refused to take another exam. | He refused take another exam. | He refused taking another exam. | He refused to taking another exam.
Key: {"kind": "mcq", "correct": "He refused to take another exam.", "wrong": ["He refused taking another exam.", "He refused take another exam.", "He refused to taking another exam."]}
- reader 1: level: Easy for B2.2 (B1 pattern).
- reader 1: sense: Distractors 'refused take / taking / to taking' are weak.
- reader 2: level: Too easy for B2.2 (A2/B1 pattern).

## r20-5-007 · B2.2 · text · twins-2.csv:14

Task: Report with *deny*: 'I didn't share the secret.' Start with *Nora denied*.
Key: {"kind": "text", "accepted": [["Nora denied sharing the secret.", "Nora denied having shared the secret.", "Nora denied that she had shared the secret.", "Nora denied she had shared the secret.", "Nora denied that she shared the secret.", "Nora denied she shared the secret.", "Nora denied that she'd shared the secret.", "Nora denied she'd shared the secret."]]}
- reader 2: instruction: Several correct forms; key must accept all.

## r20-5-008 · B2.2 · order · twins-2.csv:15

Task: Put the words in order.
word_cards: the | remains | unclear | payment | whether | has | arrived
Key: {"kind": "order", "sentence": "whether the payment has arrived remains unclear", "also": []}
- reader 1: instruction: Capital W is not visible, but only one order is possible; fine.
- reader 2: instruction: Starts with a word that needs a capital letter only in the answer; fine.

## r20-5-010 · B2.2 · mcq · twins-2.csv:17

Task: Choose the correct option: The question is ___.
options: whether the supplier can to meet the deadline | whether the supplier can meet the deadline | whether the supplier can meets the deadline | whether can the supplier meet the deadline
Key: {"kind": "mcq", "correct": "whether the supplier can meet the deadline", "wrong": ["whether can the supplier meet the deadline", "whether the supplier can meets the deadline", "whether the supplier can to meet the deadline"]}
- reader 1: level: Too easy for B2.2: wrong options are basic errors (can to / meets).
- reader 2: level: Too easy for B2.2 (modal + bare infinitive).

## r20-5-011 · B2.2 · text · twins-2.csv:18

Task: Combine the sentences. Start with *It is unclear*: Which route should we take? It is unclear.
Key: {"kind": "text", "accepted": [["It is unclear which route we should take.", "It's unclear which route we should take.", "It is unclear which route to take.", "It's unclear which route to take."]]}
- reader 1: another correct answer, not accepted: ['It is unclear which route we ought to take.', 'It is unclear which route we are to take.']
- reader 1: instruction: 'Combine the sentences' with only a question and 'It is unclear' is fine, but 'to take' (should dropped) is also correct.
- reader 2: another correct answer, not accepted: ['It is unclear which route we ought to take.']
- reader 2: instruction: Instruction does not say whether 'to take' is allowed; both fine.

## r20-5-012 · B2.1 · mcq · twins-2.csv:23

Task: Choose the correct option: She would have understood the lesson if she ___ the notes.
options: had reading | had read | have read
Key: {"kind": "mcq", "correct": "had read", "wrong": ["had reading", "have read"]}
- reader 1: level: Too easy for B2.1: 3 options, basic third conditional form (A2/B1).
- reader 2: level: B1 content for B2.1.

## r20-5-013 · B2.1 · mcq · twins-2.csv:24

Task: Which sentence has a mistake?
options: If he had checked the date, he would have attended the right meeting. | If she had booked earlier, she would have paid less for the flight. | If we had trained harder, we could have finished the race together. | If I had save a copy, I wouldn't have lost my work.
Key: {"kind": "mcq", "correct": "If I had save a copy, I wouldn't have lost my work.", "wrong": ["If she had booked earlier, she would have paid less for the flight.", "If we had trained harder, we could have finished the race together.", "If he had checked the date, he would have attended the right meeting."]}
- reader 1: level: Basic form check, B1 level.
- reader 1: sense: 'had save' is possible for weak learners but a bit unlikely at B2.1.
- reader 2: sense: Mistake is a bare 'save' for 'saved': more a typo than a real learner error.

## r20-5-014 · B2.1 · mcq · twins-2.csv:25

Task: Choose the correct option: We missed the bus yesterday. If we had left earlier, we ___.
options: could have caught it | could had caught it | could have catch it
Key: {"kind": "mcq", "correct": "could have caught it", "wrong": ["could have catch it", "could had caught it"]}
- reader 1: level: Too easy for B2.1: B1 third conditional form, obvious wrong forms.
- reader 2: level: B1 content for B2.1.

## r20-5-015 · B2.1 · text · twins-2.csv:26

Task: Rewrite with *if* and *would*: I didn't remember her birthday, so I didn't call her.
Key: {"kind": "text", "accepted": [["If I had remembered her birthday, I would have called her.", "If I'd remembered her birthday, I would have called her.", "If I had remembered her birthday, I'd have called her.", "If I'd remembered her birthday, I'd have called her.", "I would have called her if I had remembered her birthday.", "I would have called her if I'd remembered her birthday.", "I'd have called her if I had remembered her birthday.", "I'd have called her if I'd remembered her birthday."]]}
- reader 1: another correct answer, not accepted: ['If I had remembered her birthday, I would have phoned her.', 'If I had remembered her birthday, I would have rung her.']
- reader 2: another correct answer, not accepted: ['If I had remembered her birthday, I would have phoned her.', 'If I had remembered her birthday, I would have rung her.']
- reader 2: instruction: Names 'if' and 'would' (partly gives form).

## r20-5-016 · B2.1 · mcq · twins-2.csv:27

Task: Which sentence reports this: 'Can you fix my laptop?'
options: She asked if could I fix her laptop. | She asked if I could fix her laptop. | She asked if I could to fix her laptop. | She asked if I could fixed her laptop.
Key: {"kind": "mcq", "correct": "She asked if I could fix her laptop.", "wrong": ["She asked if could I fix her laptop.", "She asked if I could fixed her laptop.", "She asked if I could to fix her laptop."]}
- reader 1: level: B1 content at B2.1.
- reader 2: level: A2/B1 reported question for B2.1; too easy.

## r20-5-017 · B2.1 · mcq · twins-2.csv:28

Task: Which sentence reports this: 'Don't leave your bag here!'
options: He told me to not left my bag there. | He told me not to leaving my bag there. | He told me not leave my bag there. | He told me not to leave my bag there.
Key: {"kind": "mcq", "correct": "He told me not to leave my bag there.", "wrong": ["He told me not leave my bag there.", "He told me not to leaving my bag there.", "He told me to not left my bag there."]}
- reader 1: level: B1 content at B2.1.
- reader 2: level: B1 pattern for B2.1; too easy.

## r20-5-018 · B2.1 · mcq · twins-2.csv:29

Task: Which sentence is NOT correct?
options: He asked whether I had enjoyed the concert. | She asked me where did I buy the flowers. | Mia asked if I could send the report that afternoon. | They asked how long the repair would take.
Key: {"kind": "mcq", "correct": "She asked me where did I buy the flowers.", "wrong": ["He asked whether I had enjoyed the concert.", "They asked how long the repair would take.", "Mia asked if I could send the report that afternoon."]}
- reader 1: level: B1 content at B2.1.

## r20-5-019 · B2.1 · text · twins-2.csv:30

Task: Report this request. Start with *Omar asked me*: 'Could you check the figures?'
Key: {"kind": "text", "accepted": [["Omar asked me to check the figures.", "Omar asked me if I could check the figures.", "Omar asked me whether I could check the figures.", "Omar asked if I could check the figures.", "Omar asked whether I could check the figures.", "If I could check the figures, omar asked me.", "If I could check the figures, omar asked."]]}
- reader 1: instruction: Instruction does not say whether to use to-infinitive or if-clause; both are correct.
- reader 2: instruction: 'Report this request' with 'asked me' allows both a reported question and 'to check'; both correct.

## r20-5-020 · B2.1 · order · twins-2.csv:40

Task: Put the words in order.
word_cards: the | for | been | hours | had | we | began | hiking | when | storm
Key: {"kind": "order", "sentence": "we had been hiking for hours when the storm began", "also": ["when the storm began we had been hiking for hours", "the storm began when we had been hiking for hours", "when we had been hiking for hours the storm began", "for hours we had been hiking when the storm began", "when the storm began for hours we had been hiking"]}
- reader 1: instruction: 'began' + 'hiking' suggest 'began hiking' as a trap but not possible with had been; fine.
- reader 2: instruction: No capital or comma cue; fine.

## r20-5-021 · B2.1 · mcq · twins-2.csv:41

Task: Choose the correct option: The floor was wet. Water ___ from a pipe all night.
options: had been leak | had leaking | had been leaking
Key: {"kind": "mcq", "correct": "had been leaking", "wrong": ["had been leak", "had leaking"]}
- reader 1: level: Too easy for B2.1: 3 options, basic form.
- reader 2: level: B1/B2.1 border, fine.

## r20-5-022 · B2.1 · gap · twins-2.csv:42

Task: By the time the bell rang, Eva ___ all ten questions, so she left early. (answer)
Key: {"kind": "gap", "accepted": [["had answered"]]}
- reader 1: another correct answer, not accepted: [['answered'], ["'d answered"]]
- reader 1: instruction: 'answered' (simple past after 'by the time') is acceptable informally; 'had answered' two words in one gap: say so. Hint '(answer)' fine.
- reader 1: level: B1 past perfect.
- reader 2: another correct answer, not accepted: [["'d answered"], ['answered']]
- reader 2: instruction: '(answer)' is an odd label: unclear whether to type the base verb or the full verb phrase; two words in one gap. Simple past 'answered' is also possible after 'by the time' (less precise).

## r20-5-023 · B2.2 · order · twins-2.csv:48

Task: Put the words in order.
word_cards: for | years | had | she | when | learning | been | French | moved | she
Key: {"kind": "order", "sentence": "she had been learning French for years when she moved", "also": ["when she moved she had been learning French for years", "she moved when she had been learning French for years", "when she had been learning French for years she moved", "for years she had been learning French when she moved", "when she moved for years she had been learning French"]}
- reader 1: sense: Last variant is odd in meaning but grammatical.
- reader 2: instruction: Two 'she' cards, fine.

## r20-5-025 · B2.2 · text · twins-3.csv:3

Task: Imagine it was different. Rewrite as one sentence with *if*: She didn't learn German at school, so she can't understand her new colleagues now.
Key: {"kind": "text", "accepted": [["If she'd learned German at school, she'd be able to understand her new colleagues now.", "If she'd learned German at school, she would be able to understand her new colleagues now.", "If she had learned German at school, she would be able to understand her new colleagues now.", "If she had learned German at school, she'd be able to understand her new colleagues now.", "If she had learned German at school, she could understand her new colleagues now.", "If she'd learned German at school, she could understand her new colleagues now.", "If she had learned German at school, she'd understand her new colleagues now.", "If she had learned German at school, she would understand her new colleagues now.", "If she'd learned German at school, she'd understand her new colleagues now.", "If she'd learned German at school, she would understand her new colleagues now.", "If she'd learnt German at school, she would be able to understand her new colleagues now.", "If she had learnt German at school, she'd be able to understand her new colleagues now.", "If she'd learnt German at school, she'd be able to understand her new colleagues now.", "If she had learnt German at school, she would be able to understand her new colleagues now.", "If she had learnt German at school, she could understand her new colleagues now.", "If she'd learnt German at school, she could understand her new colleagues now.", "If she had learnt German at school, she would understand her new colleagues now.", "If she had learnt German at school, she'd understand her new colleagues now.", "If she'd learnt German at school, she'd understand her new colleagues now.", "If she'd learnt German at school, she would understand her new colleagues now.", "She'd be able to understand her new colleagues now if she had learned German at school.", "She would be able to understand her new colleagues now if she had learned German at school.", "She'd be able to understand her new colleagues now if she'd learned German at school.", "She would be able to understand her new colleagues now if she'd learned German at school.", "She could understand her new colleagues now if she'd learned German at school.", "She could understand her new colleagues now if she had learned German at school.", "She would understand her new colleagues now if she'd learned German at school.", "She'd understand her new colleagues now if she had learned German at school.", "She would understand her new colleagues now if she had learned German at school.", "She'd understand her new colleagues now if she'd learned German at school.", "She'd be able to understand her new colleagues now if she'd learnt German at school.", "She would be able to understand her new colleagues now if she had learnt German at school.", "She'd be able to understand her new colleagues now if she had learnt German at school.", "She would be able to understand her new colleagues now if she'd learnt German at school.", "She could understand her new colleagues now if she'd learnt German at school.", "She could understand her new colleagues now if she had learnt German at school.", "She'd understand her new colleagues now if she'd learnt German at school.", "She would understand her new colleagues now if she had learnt German at school.", "She would understand her new colleagues now if she'd learnt German at school.", "She'd understand her new colleagues now if she had learnt German at school.", "she'd be able to understand her new colleagues now if she'd learned German at school.", "she would be able to understand her new colleagues now if she'd learned German at school.", "she would be able to understand her new colleagues now if she had learned German at school.", "she'd be able to understand her new colleagues now if she had learned German at school.", "she could understand her new colleagues now if she had learned German at school.", "she could understand her new colleagues now if she'd learned German at school.", "she'd understand her new colleagues now if she had learned German at school.", "she would understand her new colleagues now if she had learned German at school.", "she'd understand her new colleagues now if she'd learned German at school.", "she would understand her new colleagues now if she'd learned German at school.", "she would be able to understand her new colleagues now if she'd learnt German at school.", "she'd be able to understand her new colleagues now if she had learnt German at school.", "she'd be able to understand her new colleagues now if she'd learnt German at school.", "she would be able to understand her new colleagues now if she had learnt German at school.", "she could understand her new colleagues now if she had learnt German at school.", "she could understand her new colleagues now if she'd learnt German at school.", "she would understand her new colleagues now if she had learnt German at school.", "she'd understand her new colleagues now if she had learnt German at school.", "she'd understand her new colleagues now if she'd learnt German at school.", "she would understand her new colleagues now if she'd learnt German at school."]]}
- reader 2: instruction: Instruction 'Imagine it was different' fine.

## r20-5-026 · B2.2 · mcq · twins-3.csv:4

Task: Which sentence is NOT correct?
options: If he spoke Italian, he would have enjoyed the tour more. | If we hadn't sold the car, we would drive to the coast now. | If she would be more patient, she wouldn't have shouted at him. | If I had slept well, I wouldn't feel so tired today.
Key: {"kind": "mcq", "correct": "If she would be more patient, she wouldn't have shouted at him.", "wrong": ["If he spoke Italian, he would have enjoyed the tour more.", "If we hadn't sold the car, we would drive to the coast now.", "If I had slept well, I wouldn't feel so tired today."]}
- reader 1: a wrong option that fits: A ('If he spoke Italian, he would have enjoyed the tour more') is arguably correct (habitual/state hypothetical with past result); weak distractor.
- reader 1: sense: Option A is a real, acceptable sentence: two options may be judged wrong.
- reader 2: sense: Option A (If he spoke Italian, he would have enjoyed the tour more) is grammatical as a mixed conditional (he does not speak Italian in general); if the key is A, C is also wrong.

## r20-5-027 · B2.2 · mcq · twins-3.csv:5

Task: Which sentence is correct?
options: If he were more confident, he would asked for a pay rise. | If he were more confident, he will have asked for a pay rise. | If he would be more confident, he would have asked for a pay rise. | If he were more confident, he would have asked for a pay rise.
Key: {"kind": "mcq", "correct": "If he were more confident, he would have asked for a pay rise.", "wrong": ["If he were more confident, he would asked for a pay rise.", "If he would be more confident, he would have asked for a pay rise.", "If he were more confident, he will have asked for a pay rise."]}
- reader 1: sense: Mixed-time sentence is a little odd in meaning (were = general trait, fine).

## r20-5-030 · B2.2 · mcq · twins-3.csv:8

Task: Which sentence is NOT correct?
options: Had he trained harder, he would be in the team now. | Hadn't she missed the train, she'd be here now. | Had they not moved, they would live next door now. | Were she less shy, she would have spoken up.
Key: {"kind": "mcq", "correct": "Hadn't she missed the train, she'd be here now.", "wrong": ["Had he trained harder, he would be in the team now.", "Were she less shy, she would have spoken up.", "Had they not moved, they would live next door now."]}
- reader 1: sense: Option D 'Were she less shy, she would have spoken up' is mixed and fine; but unusual; B is clearly the wrong one.
- reader 2: sense: Option D (Were she less shy, she would have spoken up) is a grammatical mixed conditional, but borderline; B is clearly wrong.

## r20-5-031 · B2.2 · mcq · twins-3.csv:9

Task: Choose the correct option.
options: Had the software been tested earlier, we would not fixing these errors now. | Had the software be tested earlier, we would not be fixing these errors now. | Had the software been tested earlier, we would not be fixing these errors now. | Had the software been tested earlier, we will not be fixing these errors now.
Key: {"kind": "mcq", "correct": "Had the software been tested earlier, we would not be fixing these errors now.", "wrong": ["Had the software be tested earlier, we would not be fixing these errors now.", "Had the software been tested earlier, we would not fixing these errors now.", "Had the software been tested earlier, we will not be fixing these errors now."]}
- reader 1: instruction: No stem question; ok.

## r20-5-032 · B2.1 · text · twins-3.csv:10

Task: Report this. Start with *The coach told us*: 'You must warm up before every match.'
Key: {"kind": "text", "accepted": [["The coach told us we had to warm up before every match.", "The coach told us that we had to warm up before every match.", "The coach told us we must warm up before every match.", "The coach told us that we must warm up before every match.", "The coach told us to warm up before every match.", "Before every match, the coach told us we had to warm up.", "Before every match, the coach told us that we had to warm up.", "Before every match, the coach told us we must warm up.", "Before every match, the coach told us that we must warm up.", "Before every match, the coach told us to warm up."]]}
- reader 1: another correct answer, not accepted: ['The coach told us that we have to warm up before every match.']
- reader 1: level: B1 content at B2.1.
- reader 2: answer not accepted: The coach told us (that) we had to warm up before every match.
- reader 2: instruction: Direct speech 'must' allows 'must' or 'had to' and 'to warm up'.
- the readers disagree

## r20-5-033 · B2.1 · mcq · twins-3.csv:11

Task: Which sentence is NOT correct?
options: He told us he was moving abroad. | She said that the bus was full. | He told that the shop was closed. | They told me the film had started.
Key: {"kind": "mcq", "correct": "He told that the shop was closed.", "wrong": ["She said that the bus was full.", "They told me the film had started.", "He told us he was moving abroad."]}
- reader 1: level: B1 content at B2.1.

## r20-5-034 · B2.1 · mcq · twins-3.csv:12

Task: Which sentence is correct?
options: My sister said she would call me as soon as she landed. | My sister said she would call me as soon as she did landed. | My sister said she would call me as soon as she would land. | My sister said she would calling me as soon as she landed.
Key: {"kind": "mcq", "correct": "My sister said she would call me as soon as she landed.", "wrong": ["My sister said she would call me as soon as she would land.", "My sister said she would call me as soon as she did landed.", "My sister said she would calling me as soon as she landed."]}
- reader 1: level: B1 content at B2.1.
- reader 1: sense: 'did landed' / 'would calling' are rare mistakes.

## r20-5-035 · B2.1 · mcq · twins-3.csv:13

Task: Which sentence is correct?
options: The agent said me I might need a visa. | The agent said I mighted need a visa. | The agent said I might need a visa. | The agent said I might to need a visa.
Key: {"kind": "mcq", "correct": "The agent said I might need a visa.", "wrong": ["The agent said I mighted need a visa.", "The agent said I might to need a visa.", "The agent said me I might need a visa."]}
- reader 1: level: B1 content at B2.1.
- reader 1: sense: 'mighted' is a form nobody writes; 'might to need' is rare.

## r20-5-036 · B2.2 · mcq · twins-3.csv:14

Task: Which sentence is correct?
options: She asked me how to starting. | She asked me how should she start. | She asked me how she should starts. | She asked me how to start.
Key: {"kind": "mcq", "correct": "She asked me how to start.", "wrong": ["She asked me how should she start.", "She asked me how she should starts.", "She asked me how to starting."]}
- reader 1: level: B1/B2.1 content at B2.2.
- reader 1: sense: 'how to starting' unlikely.
- reader 2: instruction: Too easy for B2.2.
- reader 2: level: Wrong options 'how to starting' and 'how she should starts' are random-looking; 'how should she start' is the believable error.

## r20-5-037 · B2.2 · text · twins-3.csv:15

Task: Report this. Start with *They asked*: 'What time should we arrive?'
Key: {"kind": "text", "accepted": [["They asked what time they should arrive.", "They asked what time to arrive.", "They asked what time we should arrive.", "They asked me what time they should arrive.", "They asked us what time we should arrive.", "They asked me what time to arrive.", "They asked us what time to arrive."]]}
- reader 1: another correct answer, not accepted: ['They asked what time they had to arrive.', 'They asked what time they would have to arrive.']
- reader 1: instruction: Pronoun 'we'/'they' depends on who is speaking: not defined, so both are right.
- reader 2: another correct answer, not accepted: ['They asked what time they were to arrive.', 'They asked what time they ought to arrive.']

## r20-5-039 · B2.2 · mcq · twins-3.csv:17

Task: Which sentence is correct?
options: Mr Ozols asked whether had the invoices been sent. | Mr Ozols asked whether the invoices had been sent. | Mr Ozols asked have the invoices been sent. | Mr Ozols asked that the invoices had been sent.
Key: {"kind": "mcq", "correct": "Mr Ozols asked whether the invoices had been sent.", "wrong": ["Mr Ozols asked have the invoices been sent.", "Mr Ozols asked whether had the invoices been sent.", "Mr Ozols asked that the invoices had been sent."]}
- reader 1: sense: 'asked have the invoices been sent' is a form few write.

## r20-5-040 · B2.2 · mcq · twins-3.csv:18

Task: Which sentence reports this advice: 'If I were you, I'd get a second opinion before the operation.'
options: She advised me getting a second opinion before the operation. | She suggested me to get a second opinion before the operation. | She advised to me get a second opinion before the operation. | She advised me to get a second opinion before the operation.
Key: {"kind": "mcq", "correct": "She advised me to get a second opinion before the operation.", "wrong": ["She advised me getting a second opinion before the operation.", "She suggested me to get a second opinion before the operation.", "She advised to me get a second opinion before the operation."]}
- reader 1: sense: 'advised to me get' is an unlikely error.

## r20-5-041 · B2.2 · text · twins-3.csv:19

Task: My colleague told me: 'You really should have the figures checked before you submit the report.' Report it, starting with *My colleague urged me*.
Key: {"kind": "text", "accepted": [["My colleague urged me to have the figures checked before submitting the report.", "My colleague urged me to have the figures checked before I submitted the report.", "My colleague urged me to have the figures checked before I submit the report.", "My colleague urged me to get the figures checked before submitting the report.", "My colleague urged me to get the figures checked before I submitted the report.", "Before submitting the report, my colleague urged me to have the figures checked.", "Before I submitted the report, my colleague urged me to have the figures checked.", "Before I submit the report, my colleague urged me to have the figures checked.", "Before submitting the report, my colleague urged me to get the figures checked.", "Before I submitted the report, my colleague urged me to get the figures checked."]]}
- reader 1: instruction: 'urged' is stronger than 'should'; fine.

## r20-5-043 · B2.2 · mcq · twins-3.csv:21

Task: Which sentence reports the client's complaint: 'The delivery was three days late.'
options: The client complained me that the delivery had been three days late. | The client complained that the delivery had be three days late. | The client complained that the delivery had been three days late. | The client complained about the delivery had been three days late.
Key: {"kind": "mcq", "correct": "The client complained that the delivery had been three days late.", "wrong": ["The client complained about the delivery had been three days late.", "The client complained that the delivery had be three days late.", "The client complained me that the delivery had been three days late."]}
- reader 1: sense: 'complained me that' is a rare error.
- reader 2: level: Also 'complained that the delivery was three days late' would be fine but not offered.

## r20-5-044 · B2.2 · mcq · twins-3.csv:22

Task: Which is correct? 'We weren't sure ___.'
options: where to going | where to go | where go we | where to we go
Key: {"kind": "mcq", "correct": "where to go", "wrong": ["where to going", "where go we", "where to we go"]}
- reader 1: level: Too easy for B2.2.
- reader 1: sense: 'where go we' is an unlikely error.
- reader 2: sense: Wrong options 'where to going' and 'where to we go' are unlikely errors; 'where we go' would be the believable one.

## r20-5-045 · B2.2 · text · twins-3.csv:23

Task: Join the sentences, using *to*: She didn't know. Who should she ask?
Key: {"kind": "text", "accepted": [["She didn't know who to ask.", "She didn't know whom to ask."]]}
- reader 1: instruction: 'using to' names the form.
- reader 2: instruction: 'using to' tells the form; acceptable but partly gives answer.

## r20-5-047 · B2.2 · mcq · twins-3.csv:25

Task: Choose the correct option.
options: It remains unclear how we do will pay for the repairs. | It remains unclear how we will to pay for the repairs. | It remains unclear how will we pay for the repairs. | It remains unclear how we will pay for the repairs.
Key: {"kind": "mcq", "correct": "It remains unclear how we will pay for the repairs.", "wrong": ["It remains unclear how will we pay for the repairs.", "It remains unclear how we will to pay for the repairs.", "It remains unclear how we do will pay for the repairs."]}
- reader 1: sense: 'how we do will pay' is a form nobody writes.
- reader 2: level: Too easy for B2.2; 'how we do will pay' is an impossible string.

## r20-5-048 · B2.2 · text · twins-3.csv:27

Task: Write one sentence that starts with *Wh…*: It doesn't matter what you decide. I'll support you.
Key: {"kind": "text", "accepted": [["Whatever you decide, I'll support you.", "Whatever you decide, I will support you.", "Whatever you decide, you'll have my support.", "Whatever you decide, you will have my support."]]}
- reader 1: another correct answer, not accepted: ["Whichever way you decide, I'll support you.", "Whatever you decide, I'll back you."]
- reader 1: instruction: 'Wh…' gives away the first letters and tells the learner to find the form; also 'What you decide doesn't matter, I'll support you' is a comma splice.
- reader 2: another correct answer, not accepted: ["Whatever you decide doesn't matter; I'll support you.", "What you decide doesn't matter; I'll support you.", "What you decide doesn't matter to me: I'll support you."]
- reader 2: instruction: 'Wh…' is an unclear cue and not a normal way to give a hint; 'Wh' also allows What/Whatever/Whichever.

## r20-5-049 · B2.2 · mcq · twins-3.csv:28

Task: Which sentence is NOT correct?
options: Whomever finishes first can go home. | Take whichever seat is free. | Wherever you go, call me first. | Invite whoever you like to the party.
Key: {"kind": "mcq", "correct": "Whomever finishes first can go home.", "wrong": ["Invite whoever you like to the party.", "Take whichever seat is free.", "Wherever you go, call me first."]}
- reader 1: a wrong option that fits: D 'Invite whoever you like' is accepted in modern English (whomever is formal), so D may seem wrong to some.
- reader 1: sense: Whom/who is a subtle, formal point for adult learners.
- reader 2: sense: Learners rarely write 'whomever' there; D 'whoever you like' is correct (whomever also formal-correct), fine but pair of who/whom is a formal-register trap.

## r20-5-051 · B2.1 · gap · typical-b2c1-1.csv:2

Task: If I ___ her number, I would call her right now. (know)
Key: {"kind": "gap", "accepted": [["knew"]]}
- reader 1: another correct answer, not accepted: [['were to know']]
- reader 1: level: Too easy for B2.1: A2/B1 second conditional.
- reader 2: another correct answer, not accepted: [['had known']]

## r20-5-052 · B2.1 · gap · typical-b2c1-1.csv:3

Task: If the train ___ faster, more people would use it for work. (be)
Key: {"kind": "gap", "accepted": [["was", "were"]]}
- reader 1: level: Too easy for B2.1.
- reader 2: instruction: 'was' is acceptable informally, 'were' formal.

## r20-5-053 · B2.1 · gap · typical-b2c1-1.csv:4

Task: I ___ more if the gym were closer to my office. (exercise)
Key: {"kind": "gap", "accepted": [["would exercise", "'d exercise"]]}
- reader 1: another correct answer, not accepted: [['might exercise']]
- reader 1: instruction: Gap is one gap of two words 'would exercise'.
- reader 1: level: B1 second conditional.
- reader 2: another correct answer, not accepted: [['might exercise'], ['would work out']]

## r20-5-054 · B2.1 · gap · typical-b2c1-1.csv:5

Task: If we ___ earlier, we wouldn't have missed the flight. (leave)
Key: {"kind": "gap", "accepted": [["had left", "'d left"]]}
- reader 1: level: B1 third conditional.

## r20-5-055 · B2.1 · gap · typical-b2c1-1.csv:6

Task: If you had asked me, I ___ you with the move. (help)
Key: {"kind": "gap", "accepted": [["would have helped", "'d have helped"]]}
- reader 1: another correct answer, not accepted: [['might have helped']]
- reader 1: level: B1 third conditional.
- reader 2: another correct answer, not accepted: [['might have helped']]

## r20-5-056 · B2.1 · gap · typical-b2c1-1.csv:7

Task: Tom said he ___ the report the next day. (send)
Key: {"kind": "gap", "accepted": [["would send", "'d send"]]}
- reader 1: another correct answer, not accepted: [['was going to send'], ['would be sending'], ['was sending'], ['will send']]
- reader 1: instruction: 'will send' acceptable if the next day is still in the future.
- reader 1: level: B1 content at B2.1.
- reader 2: another correct answer, not accepted: [['was going to send'], ['was sending']]

## r20-5-057 · B2.1 · gap · typical-b2c1-1.csv:8

Task: She told me she ___ in Riga for two years. (live)
Key: {"kind": "gap", "accepted": [["had lived", "had been living", "'d lived", "'d been living"]]}
- reader 1: another correct answer, not accepted: [['lived']]
- reader 1: level: B1 content at B2.1.
- reader 2: another correct answer, not accepted: [['lived'], ['has lived'], ['has been living']]
- reader 2: instruction: 'lived' and present perfect (if she still lives there) are acceptable.

## r20-5-058 · B2.1 · gap · typical-b2c1-1.csv:9

Task: The receptionist asked me where I ___ from. (be)
Key: {"kind": "gap", "accepted": [["was"]]}
- reader 1: another correct answer, not accepted: [['am'], ['came']]
- reader 1: instruction: 'am' correct if still true; 'came' is another correct verb but ignores the hint.
- reader 1: level: B1 content at B2.1.
- reader 2: another correct answer, not accepted: [['am']]
- reader 2: instruction: 'am' is acceptable if the situation is still true.

## r20-5-059 · B2.1 · gap · typical-b2c1-1.csv:10

Task: She asked me how long I ___ English. (study)
Key: {"kind": "gap", "accepted": [["had been studying", "had studied", "'d been studying", "'d studied"]]}
- reader 1: another correct answer, not accepted: [['have been studying'], ['was studying']]
- reader 1: level: B1 content at B2.1.
- reader 2: another correct answer, not accepted: [['have studied'], ['have been studying']]
- reader 2: instruction: Present perfect is acceptable without backshift.

## r20-5-060 · B2.1 · gap · typical-b2c1-1.csv:11

Task: Could you tell me what time the museum ___? (open)
Key: {"kind": "gap", "accepted": [["opens", "will be open", "will open", "is opening", "is going to open"]]}
- reader 1: another correct answer, not accepted: [['opened']]
- reader 1: instruction: 'opened' is possible in the past sense but ill fits; 'opens' main.
- reader 1: level: B1 content at B2.1.
- reader 2: instruction: 'will open' is also correct (e.g. opening time tomorrow).

