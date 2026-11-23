# Blind check c1-14: flags for the judge

8 tasks, 2 readers.

## c1-14-001 · C1 · gap · c1-agree-1.csv:12

Task: The manager and two of her assistants ___ coming to the meeting. (be)
Key: {"kind": "gap", "accepted": [["are", "were"]]}
- reader 1: another correct answer, not accepted: [['will be']]
- reader 1: instruction: No time context: 'are coming' (present arrangement), 'will be coming' and 'were coming' (past) all fit. Also needs the verb form only; plural subject agreement is the whole task.
- reader 1: level: Too easy for C1: subject-verb agreement with 'be' is A2/B1.
- reader 2: another correct answer, not accepted: [['will be'], ['have been']]
- reader 2: instruction: No time context given, so are/were/will be/have been all fit; the only given word is (be). Also 'The manager ... her assistants' is a plain subject-verb agreement point.
- reader 2: level: Plain agreement; A2/B1, not C1.
- reader 2: sense: Only sense problem: no context to fix the tense.

## c1-14-002 · C1 · text · c1-order-1.csv:5

Task: Start with *So loud*: The music was so loud that we couldn't hear each other.
Key: {"kind": "text", "accepted": [["So loud was the music that we couldn't hear each other.", "So loud was the music that we could not hear each other."]]}
- reader 1: another correct answer, not accepted: ["So loud was the music that we couldn't hear one another.", 'So loud was the music that we could not hear one another.', "So loud did the music play that we couldn't hear each other."]
- reader 1: instruction: Instruction does not say to invert (So loud was the music...); a learner may write 'So loud, the music was that...' or copy the model. The model sentence nearly gives the answer (just move words and invert).
- reader 2: another correct answer, not accepted: [["so loud did the music become that we couldn't hear each other"], ["so loudly did the music play that we couldn't hear each other"]]
- reader 2: instruction: The example already gives the full sentence; instruction does not say to invert (so the learner may write 'So loud, the music was...'); the expected inversion is not signalled, and the model sentence given is the answer's content only.
- reader 2: level: Inversion after So is C1/B2+, fine.

## c1-14-003 · C1 · text · c1-part-1.csv:8

Task: Join the two sentences with an *-ing* form: The river burst its banks. It flooded the streets near the station.
Key: {"kind": "text", "accepted": [["The river burst its banks, flooding the streets near the station."]]}
- reader 1: another correct answer, not accepted: ['Bursting its banks, the river flooded the streets near the station.', 'The river, bursting its banks, flooded the streets near the station.', 'The river burst its banks and flooded the streets near the station (not an -ing form).']
- reader 1: instruction: Does not say which sentence the -ing goes in, so several answers are valid.
- reader 1: level: Borderline: -ing participle clause is B2 rather than C1.
- reader 2: another correct answer, not accepted: [['Bursting its banks, the river flooded the streets near the station.'], ['The river, bursting its banks, flooded the streets near the station.']]
- reader 2: instruction: Two possible -ing patterns (result vs. simultaneous clause) are both allowed by the instruction; 'Bursting its banks, the river flooded...' is less natural (implies simultaneity) but correct.
- reader 2: level: Fine for C1 but B2-ish.

## c1-14-004 · C1 · text · c1-part-1.csv:12

Task: Start with *Having* and join the two sentences: We checked the train times. We left for the station.
Key: {"kind": "text", "accepted": [["Having checked the train times, we left for the station."]]}
- reader 1: another correct answer, not accepted: ['We left for the station, having checked the train times.']
- reader 1: instruction: Start is given, so the form is named (only combining needed); 'We left ... having checked' ignores 'Start with' but is correct English.
- reader 1: level: Perfect participle clause is B2; fine for C1 only as easy item.
- reader 2: instruction: Instruction nearly gives the structure away (Having + past participle of the verb in sentence 1); only the participle needs to be produced.
- reader 2: level: Perfect participle clause is B2/C1; acceptable.

## c1-14-005 · C1 · gap · c1-past-1.csv:12

Task: I'm always losing receipts. I wish I ___ them more carefully. (keep)
Key: {"kind": "gap", "accepted": [["kept"]]}
- reader 1: another correct answer, not accepted: [['had kept']]
- reader 1: instruction: 'had kept' also works as regret about the past; 'I'm always losing' favours 'kept' but does not exclude it.
- reader 1: level: Easy for C1: 'wish + past simple' is B1/B2.
- reader 2: another correct answer, not accepted: [['had kept']]
- reader 2: instruction: Both fit: 'kept' (present habit) is natural; 'had kept' (regret about the past) is also correct but less natural after 'always losing'.
- reader 2: level: Wish + past is B1/B2; below C1 in difficulty.

## c1-14-006 · C1 · gap · c1-perf-1.csv:15

Task: I ___ the bank all morning, but nobody's answering. (ring)
Key: {"kind": "gap", "accepted": [["have been ringing", "'ve been ringing"]]}
- reader 1: instruction: Contraction accepted? Tell learners whether 'I've' is allowed (the gap sits after 'I').
- reader 2: another correct answer, not accepted: [['was ringing'], ['had been ringing']]
- reader 2: instruction: Contraction 'I've been ringing' should be accepted. 'was ringing' (past, narrating) is possible but less natural with 'nobody's answering'. American: 'calling' not applicable (word given).
- reader 2: level: Present perfect continuous is B1/B2; not C1.

## c1-14-007 · C1 · mcq · c1-prep-1.csv:7

Task: Choose the correct option: She took a part-time job ___ her own business.
options: with a view to start | with a view of starting | in view to starting | with a view to starting
Key: {"kind": "mcq", "correct": "with a view to starting", "wrong": ["with a view to start", "with a view of starting", "in view to starting"]}
- reader 2: sense: 'in view to' and 'with a view of' are believable errors. Fine.

## c1-14-008 · C1 · mcq · c1-pres-2.csv:9

Task: Your friend lent you money and is worried. Choose the most natural way to make a promise: ___ I'll pay you back on Friday.
options: I was promising | I promise | I'm going to promise | I'm promising
Key: {"kind": "mcq", "correct": "I promise", "wrong": ["I'm promising", "I'm going to promise", "I was promising"]}
- reader 1: instruction: The situation is partly superfluous: only 'I promise' is possible English before 'I'll pay you back' anyway.
- reader 1: level: Too easy for C1: performative 'I promise' vs continuous is B1; options are not really tempting.
- reader 2: instruction: The situation ('Your friend lent you money and is worried') is needed to justify 'most natural', but 'I'm promising' is not natural; answer is a simple performative.
- reader 2: level: I promise is A2/B1; not a C1 point of use and nuance.
- reader 2: sense: 'I'm promising' is not a believable learner error here? Mild: fine. 'I'm going to promise' is unlikely.

