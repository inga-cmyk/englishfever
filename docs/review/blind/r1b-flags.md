# Blind check r1b: flags for the judge

14 tasks, 2 readers.

## r1b-001 · B2.1 · text · built-in

Task: Imagine it happened differently. Start with *If I*: I didn't see the sign, so I parked there and got a fine.
Key: {"kind": "text", "accepted": [["If I had seen the sign, I wouldn't have parked there.", "If I had seen the sign, I wouldn't have got a fine.", "If I had seen the sign, I would not have got a fine.", "If I had seen the sign, I wouldn't have gotten a fine.", "If I had seen the sign, I wouldn't have been fined.", "If I had seen the sign, I would not have parked there.", "I wouldn't have parked there if I had seen the sign.", "I wouldn't have got a fine if I had seen the sign.", "I would not have got a fine if I had seen the sign.", "I wouldn't have gotten a fine if I had seen the sign.", "I wouldn't have been fined if I had seen the sign.", "I would not have parked there if I had seen the sign.", "If I had seen the sign, I wouldn't have parked there and I wouldn't have got a fine.", "If I had seen the sign, I wouldn't have parked there and I wouldn't have gotten a fine.", "If I had seen the sign, I wouldn't have parked there and wouldn't have got a fine.", "If I had seen the sign, I wouldn't have parked there and wouldn't have gotten a fine.", "If I had seen the sign, I wouldn't have parked there or got a fine.", "If I had seen the sign, I wouldn't have parked there or gotten a fine.", "If I had seen the sign, I wouldn't have parked there and got a fine.", "If I had seen the sign, I wouldn't have parked there and gotten a fine.", "If I had seen the sign, I would have parked somewhere else."]]}
- reader 1: another correct answer, not accepted: ["If I had seen the sign, I wouldn't have parked there and (wouldn't have) gotten a fine. (American)", "If I had noticed the sign, I wouldn't have parked there and got a fine."]
- reader 2: another correct answer, not accepted: ["If I had seen the sign, I wouldn't have parked there and (wouldn't have) gotten a fine.", "If I had seen the sign, I wouldn't have parked there, so I wouldn't have got a fine."]
- reader 2: instruction: Two results (parked / got a fine) and the instruction does not say whether one or both must go into the result clause, so many answers are possible; 'and got a fine' after a negative clause reads oddly ('or got' / 'wouldn't have got').

## r1b-002 · B2.1 · gap · built-in

Task: I didn't learn English at school. If I ___ it then, I ___ fluent now. (learn / be)
Key: {"kind": "gap", "accepted": [["had learned", "had learnt", "'d learned", "'d learnt"], ["would be", "'d be", "might be", "could be"]]}
- reader 2: instruction: No instruction line (e.g. 'Complete with the correct form'); does not say gaps may need two words.

## r1b-003 · B1.2 · mcq · built-in

Task: Choose the correct option: 'Where do you work?' She asked me ___.
options: where did I work | where do I work | if I worked | where I worked
Key: {"kind": "mcq", "correct": "where I worked", "wrong": ["where did I work", "where do I work", "if I worked"]}
- reader 1: sense: 'if I worked' is not a believable answer for a wh-question (more a distractor from yes/no questions), but acceptable.

## r1b-004 · B2.2 · gap · built-in

Task: 'Congratulations, Jo! You've finally passed the exam!' I congratulated Jo ___ passing the exam.
word_cards: with | on | at | about
Key: {"kind": "gap", "accepted": [["on"]]}
- reader 1: instruction: No explicit instruction (e.g. 'Complete the sentence'); the quoted line is fine as context.
- reader 1: level: 'congratulate on' is a fairly basic collocation for B2.2.
- reader 2: instruction: No instruction line; the direct quote already contains 'passed the exam', so the frame is longer than needed for a one-preposition gap.
- reader 2: level: 'congratulate on' is a B1 collocation; easy for B2.2.
- reader 2: sense: 'with' and 'at' are weak distractors; 'for' (a real learner error) is missing.

## r1b-005 · B2.2 · text · built-in

Task: Say what my sister did, in one sentence. My sister said to me: 'You really should see a doctor about that cough.'
Key: {"kind": "text", "accepted": [["My sister advised me to see a doctor about that cough.", "My sister urged me to see a doctor about that cough.", "My sister told me to see a doctor about that cough.", "My sister encouraged me to see a doctor about that cough.", "My sister recommended that I see a doctor about that cough.", "My sister recommended that I should see a doctor about that cough.", "My sister suggested that I see a doctor about that cough.", "My sister suggested that I should see a doctor about that cough.", "My sister suggested seeing a doctor about that cough.", "My sister suggested I see a doctor about that cough.", "My sister suggested I should see a doctor about that cough.", "My sister recommended seeing a doctor about that cough.", "My sister recommended I see a doctor about that cough.", "My sister recommended I should see a doctor about that cough.", "My sister advised seeing a doctor about that cough.", "My sister advised that I see a doctor about that cough.", "My sister advised that I should see a doctor about that cough.", "My sister said I should see a doctor about that cough.", "My sister said that I should see a doctor about that cough.", "My sister told me I should see a doctor about that cough.", "My sister told me that I should see a doctor about that cough.", "My sister advised me to see a doctor about my cough.", "My sister urged me to see a doctor about my cough.", "My sister told me to see a doctor about my cough.", "My sister encouraged me to see a doctor about my cough.", "My sister recommended that I see a doctor about my cough.", "My sister recommended that I should see a doctor about my cough.", "My sister suggested that I see a doctor about my cough.", "My sister suggested that I should see a doctor about my cough.", "My sister suggested seeing a doctor about my cough.", "My sister suggested I see a doctor about my cough.", "My sister suggested I should see a doctor about my cough.", "My sister recommended seeing a doctor about my cough.", "My sister recommended I see a doctor about my cough.", "My sister recommended I should see a doctor about my cough.", "My sister advised seeing a doctor about my cough.", "My sister advised that I see a doctor about my cough.", "My sister advised that I should see a doctor about my cough.", "My sister said I should see a doctor about my cough.", "My sister said that I should see a doctor about my cough.", "My sister told me I should see a doctor about my cough.", "My sister told me that I should see a doctor about my cough.", "My sister said I really should see a doctor about that cough.", "My sister said I really should see a doctor about my cough.", "My sister said that I really should see a doctor about that cough.", "My sister said that I really should see a doctor about my cough.", "My sister told me I really should see a doctor about that cough.", "My sister told me I really should see a doctor about my cough.", "My sister told me that I really should see a doctor about that cough.", "My sister told me that I really should see a doctor about my cough."]]}
- reader 1: another correct answer, not accepted: ['My sister told me (that) I really should see a doctor about my cough.', 'My sister said (that) I really should see a doctor about my cough.', 'My sister recommended that I (should) see a doctor about my cough.', 'My sister suggested (that) I (should) see a doctor about my cough.']
- reader 1: instruction: 'Say what my sister did' is vague: it does not say clearly that a reporting verb (advise/urge) is expected, so plain 'said I should...' is equally valid.
- reader 2: another correct answer, not accepted: ['My sister recommended that I (should) see a doctor about my cough.', 'My sister suggested that I (should) see a doctor about my cough.', 'My sister told me (that) I really should see a doctor about my cough.', 'My sister advised me to go to the doctor about my cough.']
- reader 2: instruction: 'Say what my sister did' is vague: it does not signal that a reporting verb (advise/urge) is wanted, so 'told me I should...' is equally valid; many correct answers to accept.

## r1b-006 · B2.1 · text · built-in

Task: Ask politely. Start with *Could you tell me*: Why hasn't the order arrived?
Key: {"kind": "text", "accepted": [["Could you tell me why the order hasn't arrived?", "Could you please tell me why the order hasn't arrived?", "Could you tell me why the order hasn't arrived, please?", "Could you tell me why the order hasn't arrived yet?", "Could you tell me why the order has not arrived?"]]}
- reader 1: another correct answer, not accepted: ["Could you tell me why my order hasn't arrived?"]
- reader 2: another correct answer, not accepted: ["Could you tell me why my order hasn't arrived?"]

## r1b-008 · A2.2 · text · a2-rel-might-1.csv:16

Task: Join with *which*: We visited a museum. It has old cars.
Key: {"kind": "text", "accepted": [["We visited a museum which has old cars.", "We visited a museum that has old cars.", "We visited a museum which had old cars.", "We visited a museum that had old cars."]]}
- reader 1: sense: 'a museum which has old cars' is a little unnatural; 'which has a collection of old cars' / 'with old cars' would sound better.
- reader 2: sense: 'a museum which has old cars' is slightly unnatural; 'a museum with old cars' / 'a car museum' is what a native would say.

## r1b-009 · A2.2 · text · a2-rel-might-1.csv:17

Task: Join with *which*: The app helps me learn new words. It is free.
Key: {"kind": "text", "accepted": [["The app which helps me learn new words is free.", "The app that helps me learn new words is free.", "The app which is free helps me learn new words.", "The app that is free helps me learn new words.", "The app which helps me to learn new words is free.", "The app that helps me to learn new words is free.", "The app, which is free, helps me learn new words."]]}
- reader 1: instruction: Unclear which sentence should become the relative clause; both orders are correct. Since 'The app' is already identified, a non-defining clause with commas is arguably more natural.
- reader 1: level: Embedding the relative clause in the subject is a step harder than A2.2 object-end joining; acceptable but demanding.
- reader 2: instruction: Two different embeddings are correct (which helps... is free / which is free helps...), plus comma vs no-comma variants; the instruction does not say which sentence becomes the clause.
- reader 2: level: Embedding a relative clause in the middle of the sentence is harder than A2.2 end-position joining.

## r1b-010 · A2.2 · match · a2-rel-might-1.csv:26

Task: Match each beginning with its ending.
left: A baker is a person | A fridge is a machine | A tourist is someone | A map is a drawing
right: which keeps food cold. | who makes bread. | which shows roads and towns. | who travels for fun.
Key: {"kind": "match", "pairs": [["A baker is a person", "who makes bread."], ["A fridge is a machine", "which keeps food cold."], ["A tourist is someone", "who travels for fun."], ["A map is a drawing", "which shows roads and towns."]]}
- reader 1: instruction: Matching is solved by meaning alone; who/which never has to be chosen, so the grammar point is not really tested.
- reader 2: sense: Solvable purely by meaning (general knowledge); the who/which grammar is never tested, since each ending fits only one beginning logically. 'A tourist is someone who travels for fun' is a loose definition.

## r1b-012 · A2.2 · text · a2-rel-might-1.csv:40

Task: Rewrite with *might*: Perhaps the concert tickets are sold out.
Key: {"kind": "text", "accepted": [["The concert tickets might be sold out.", "The tickets for the concert might be sold out.", "The concert tickets might have sold out."]]}
- reader 1: another correct answer, not accepted: ['The concert tickets might already be sold out.']
- reader 2: another correct answer, not accepted: ['The concert tickets might already be sold out.', 'The concert might be sold out.']

## r1b-013 · A2.2 · match · a2-rel-might-1.csv:51

Task: Match each sentence with its meaning.
left: She'll call. | She might call. | She won't call. | She might not call.
right: No, I'm sure. | Yes, I'm sure. | Perhaps not. | Yes, perhaps.
Key: {"kind": "match", "pairs": [["She'll call.", "Yes, I'm sure."], ["She might call.", "Yes, perhaps."], ["She won't call.", "No, I'm sure."], ["She might not call.", "Perhaps not."]]}
- reader 1: sense: 'No, I'm sure.' as a meaning is slightly odd wording ('No, definitely not' would be clearer), but understandable.
- reader 2: sense: 'No, I'm sure.' is odd as a 'meaning' (reads like a reply contradicting someone); 'I'm sure she won't' / 'Definitely not' would be clearer.

## r1b-014 · A2.2 · text · b1-new-3.csv:144

Task: Make a sentence with *decide*: I will go home early.
Key: {"kind": "text", "accepted": [["I decided to go home early.", "I have decided to go home early.", "I've decided to go home early.", "I've decided I'll go home early.", "I've decided that I'll go home early.", "I have decided that I will go home early.", "I have decided I will go home early.", "I decided that I would go home early.", "I decided I would go home early."]]}
- reader 1: another correct answer, not accepted: ["I've decided (that) I'll go home early.", 'I decided (that) I would go home early.']
- reader 1: instruction: Unclear what to do: no tense or form is indicated, so present perfect and past simple are both acceptable; 'Make a sentence with decide' does not signal the target 'decide + to-infinitive' clearly.
- reader 2: instruction: 'Make a sentence with decide' is unclear: tense of 'decide' is not given, and it is not explained that 'will' (spontaneous decision) should become 'decide to'; 'I will decide to go home early' would follow the instruction literally but is wrong.

