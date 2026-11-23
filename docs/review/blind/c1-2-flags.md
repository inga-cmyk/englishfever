# Blind check c1-2: flags for the judge

9 tasks, 2 readers.

## c1-2-001 · C1 · gap · c1-pres-2.csv:2

Task: Write one word in each gap: So I ___ ___ in the queue at the bakery, and this woman suddenly ___ round and hands me her dog. (stand, turn)
Key: {"kind": "gap", "accepted": [["am", "'m"], ["standing"], ["turns"]]}
- reader 1: answer not accepted: ['was', 'standing', 'turned']
- reader 1: another correct answer, not accepted: [['was', 'standing', 'turns']]
- reader 1: instruction: Tense not signalled: past (was standing, turned) and anecdote present (am standing, turns) are both correct; three gaps although only two verbs are given.
- reader 2: another correct answer, not accepted: [['was', 'standing', 'turned'], ['was', 'standing', 'turns']]
- reader 2: instruction: Present (am standing/turns) and past (was standing/turned) both work; 'hands' is present so past is less consistent but a learner may well write it. Task does not force the anecdote present.
- reader 2: level: Anecdote present is C1 use, but 'stand' for the first gap pair needs two words; fine.
- the readers disagree

## c1-2-002 · C1 · mcq · c1-pres-2.csv:3

Task: Which sentence has a mistake?
options: I was waiting for the bus when suddenly this car stops right in front of me. | We're having dinner when all the lights go out. | In the film, a retired teacher moves to Lisbon and opens a café. | So this man is walking into a café and he orders a glass of milk.
Key: {"kind": "mcq", "correct": "So this man is walking into a café and he orders a glass of milk.", "wrong": ["I was waiting for the bus when suddenly this car stops right in front of me.", "We're having dinner when all the lights go out.", "In the film, a retired teacher moves to Lisbon and opens a café."]}
- reader 1: answer not accepted: I was waiting for the bus when suddenly this car stops right in front of me.
- reader 1: a wrong option that fits: We're having dinner when all the lights go out. (also arguable: anecdote present continuous, but acceptable)
- reader 1: sense: Option 1 mixes past and present, but mixing is common in spoken anecdotes, so the 'mistake' is debatable; option 2 is a near-twin of the model anecdote sentence.
- reader 2: answer not accepted: I was waiting for the bus when suddenly this car stops right in front of me.
- reader 2: a wrong option that fits: Option 4 ('this man is walking into a café and he orders') is borderline: joke/anecdote narration is normally 'walks', 'is walking ... and orders' is odd but possible; it could fit as a mistake too.
- reader 2: sense: Option 1 mixes past continuous with present 'stops' - a plausible learner error. Option 4 is also unnatural, so two options are arguably wrong.

## c1-2-003 · C1 · gap · c1-pres-2.csv:4

Task: Write one word in each gap: And Jones ___ the ball to Taylor, who ___ and scores! (pass, shoot)
Key: {"kind": "gap", "accepted": [["passes"], ["shoots"]]}
- reader 1: level: Too easy for C1: bare commentary present, two verbs given, only add -s.
- reader 2: another correct answer, not accepted: [['has passed', 'shoots'], ['passed', 'shot']]
- reader 2: instruction: Past forms are wrong for live commentary only if the learner knows the context; 'passes ... shoots and scores' is the intended one; 'passed ... shot' would not fit 'scores'. Task is fine.
- reader 2: level: Commentary present is nearer B1/B2 than C1; a B1 learner could solve it.

## c1-2-004 · C1 · mcq · c1-pres-2.csv:5

Task: Which sentence has a mistake?
options: It says here the museum is free on Sundays. | I'm gathering you're looking for a new flat. | Anna tells me you've started running. | I hear the bridge will be closed all summer.
Key: {"kind": "mcq", "correct": "I'm gathering you're looking for a new flat.", "wrong": ["I hear the bridge will be closed all summer.", "Anna tells me you've started running.", "It says here the museum is free on Sundays."]}
- reader 2: level: 'I gather' as stative is a good C1 point.

## c1-2-005 · C1 · mcq · c1-pres-2.csv:6

Task: Which sentence has a mistake?
options: I'm wondering could you look at my CV before Friday. | We're hoping to move in by the end of May. | I was wondering if you were free on Thursday. | I wonder whether you'd mind helping me with this.
Key: {"kind": "mcq", "correct": "I'm wondering could you look at my CV before Friday.", "wrong": ["We're hoping to move in by the end of May.", "I was wondering if you were free on Thursday.", "I wonder whether you'd mind helping me with this."]}
- reader 2: level: Missing 'if/whether' is an obvious error; closer to B1/B2 than C1.
- reader 2: sense: Believable learner mistake.

## c1-2-006 · C1 · order · c1-pres-2.csv:7

Task: Put the words in order.
word_cards: me | help | this | wondering | you | with | whether | I'm | could
Key: {"kind": "order", "sentence": "I'm wondering whether you could help me with this", "also": []}
- reader 1: instruction: Cards given in a form that nearly reveals the sentence; only one natural order.
- reader 1: level: Close to B1/B2 polite-request frame; trivial for C1.
- reader 2: instruction: Content is already near the target order (cards in order of sentence parts) and only one order is possible; low challenge for C1.
- reader 2: level: Too easy for C1; B1 learner can solve it.

## c1-2-007 · C1 · gap · c1-pres-2.csv:8

Task: The app ___ to work on my phone. Can you check it? (not / appear)
Key: {"kind": "gap", "accepted": [["doesn't appear", "does not appear"]]}
- reader 1: another correct answer, not accepted: [['appears not'], ["isn't appearing"]]
- reader 1: instruction: Gap holds two words but 'one word' style unclear; 'isn't appearing' (less natural) and 'appears not' also fit; intended form ambiguous.
- reader 1: level: Fine for C1 only if the continuous vs simple nuance is the point, which the instruction does not show.
- reader 2: another correct answer, not accepted: [["isn't appearing"], ["hasn't appeared"], ["didn't appear"]]
- reader 2: instruction: 'isn't appearing to work' is less natural but possible; 'hasn't appeared/didn't appear to' also fit 'Can you check it?'. Gap is one word per gap but answer is two words (contraction counts as one?) - unclear.
- reader 2: level: Simple/continuous with 'appear' is C1 nuance, ok.

## c1-2-008 · C1 · gap · c1-pres-2.csv:9

Task: My sister and her husband ___ their first baby in June. (expect)
Key: {"kind": "gap", "accepted": [["are expecting", "'re expecting"]]}
- reader 1: another correct answer, not accepted: [['were expecting'], ['will be expecting']]
- reader 1: instruction: No time frame: 'in June' could be past or future, so were expecting also fits.
- reader 2: another correct answer, not accepted: [['expect'], ['are going to have'], ['will be expecting']]
- reader 2: instruction: 'expect' (simple) is grammatical but less natural; 'are having' also fits ('are having their first baby in June'), though not the given verb.
- reader 2: level: Fine for C1 nuance; B2 learner could solve it.

## c1-2-009 · C1 · mcq · c1-pres-2.csv:10

Task: Which sentence has a mistake?
options: I'm not suggesting you were careless. | I'm promising I'll pay you back on Friday. | I suggest we meet at the station. | We regret that the flight has been cancelled.
Key: {"kind": "mcq", "correct": "I'm promising I'll pay you back on Friday.", "wrong": ["I suggest we meet at the station.", "We regret that the flight has been cancelled.", "I'm not suggesting you were careless."]}
- reader 2: level: 'I'm not suggesting' vs 'I'm promising' is a decent nuance point but mostly B2.

