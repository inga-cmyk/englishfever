# Blind check c1-9: flags for the judge

12 tasks, 2 readers.

## c1-9-001 · C1 · mcq · c1-can-1.csv:11

Task: Which sentence has a mistake?
options: The flat may be small, but it's bright and quiet. | He might not be the fastest, but he never gives up. | It may well rain later, so take an umbrella. | She may not much experience, but she learns fast.
Key: {"kind": "mcq", "correct": "She may not much experience, but she learns fast.", "wrong": ["The flat may be small, but it's bright and quiet.", "He might not be the fastest, but he never gives up.", "It may well rain later, so take an umbrella."]}
- reader 1: sense: Option D reads like a missing-word typo (may not have much experience), not a mistake a C1 learner really makes; the other three are plain correct, so the task is easy to spot.
- reader 2: sense: Mistake (missing 'have') is believable. Fine.

## c1-9-002 · C1 · gap · c1-can-1.csv:12

Task: Even with my glasses on, I ___ hardly read the sign. (can)
Key: {"kind": "gap", "accepted": [["could"]]}
- reader 1: answer not accepted: ['can']
- reader 1: instruction: The cue (can) gives the answer away; only copying is needed. 'could' is also correct (and 'can' vs 'could' is not distinguished by context).
- reader 1: level: Too easy for C1: can hardly is not a C1 point.
- reader 2: answer not accepted: ['can']
- reader 2: another correct answer, not accepted: [["can't"]]
- reader 2: instruction: Second answer: 'could' is correct (Even with my glasses on, I could hardly read: past reading of the same situation, no time frame given). 'can't' also works (can't hardly is non-standard; 'can't' alone loses 'hardly' so not valid). Give a past or present cue.
- reader 2: level: Too easy for C1: 'hardly' with can is B1 level.

## c1-9-003 · C1 · gap · c1-order-1.csv:11

Task: Such ___ the noise from the party that nobody in the street could sleep.
Key: {"kind": "gap", "accepted": [["was"]]}
- reader 2: another correct answer, not accepted: [['is']]
- reader 2: instruction: 'is' is also possible as a literary/present narration, but 'could' makes past; 'was' is the only natural one. Gap gives answer away via 'Such' inversion only mildly.

## c1-9-004 · C1 · gap · c1-order-1.csv:12

Task: Write one word in each gap: Only when I got home ___ I ___ that my wallet was missing. (realise)
Key: {"kind": "gap", "accepted": [["did"], ["realise", "realize"]]}
- reader 1: instruction: Cue (realise) is the verb; 'Only when' at the start prompts inversion strongly. American spelling 'realize' is also correct.
- reader 2: instruction: American spelling 'realize' is also correct; accept both. 'Only when' at the start gives the inversion away.

## c1-9-005 · C1 · gap · c1-past-1.csv:11

Task: By the time the doctor arrived, the patient ___ for over an hour. (wait)
Key: {"kind": "gap", "accepted": [["had been waiting", "'d been waiting", "had waited", "'d waited"]]}
- reader 1: sense: 'had waited' is also correct; the task cannot tell the two apart.
- reader 2: instruction: 'had waited' is also correct with 'for over an hour'. Task needs one extra cue (e.g. 'still') to force continuous.

## c1-9-006 · C1 · gap · c1-past-1.csv:12

Task: I wish you ___ me about the party. I would have come. (tell)
Key: {"kind": "gap", "accepted": [["had told", "'d told"]]}
- reader 2: level: Possibly B2 rather than C1 (third conditional wish).

## c1-9-007 · C1 · gap · c1-subj-1.csv:9

Task: It is essential that every passenger ___ a valid ticket. (have)
Key: {"kind": "gap", "accepted": [["have", "should have", "has"]]}
- reader 1: instruction: Cue (have) is the answer given away; 'should have' (British) is also correct, and 'has' is common in informal use.
- reader 1: level: Mandative subjunctive with cue given is easy for C1.
- reader 2: instruction: 'should have' (BrE) is correct; 'has' is also acceptable informally (indicative), less formal-subjunctive. Giving '(have)' hands over the subjunctive form.

## c1-9-009 · C1 · mcq · c1-subj-1.csv:11

Task: Which sentence has a mistake?
options: I'd rather you wouldn't have sold the car. | I'd rather you didn't smoke in here. | I wish I had kept the receipt. | I'd sooner she hadn't told everyone.
Key: {"kind": "mcq", "correct": "I'd rather you wouldn't have sold the car.", "wrong": ["I'd rather you didn't smoke in here.", "I wish I had kept the receipt.", "I'd sooner she hadn't told everyone."]}
- reader 2: sense: Believable mistake.

## c1-9-010 · C1 · gap · c1-subj-1.csv:12

Task: We'll finish this project on time, come what ___.
Key: {"kind": "gap", "accepted": [["may"]]}
- reader 1: another correct answer, not accepted: [['might']]
- reader 1: instruction: 'come what might' is also possible, though rarer.
- reader 2: another correct answer, not accepted: [['will']]
- reader 2: instruction: 'come what will' is also found (rarer); 'may' is the standard idiom. Idiom with no context to help.

## c1-9-011 · C1 · mcq · c1-will-1.csv:11

Task: Choose the correct option: ___ that's about right, but let me check the figures.
options: I would to say | I'd say | I'm saying | I'd said
Key: {"kind": "mcq", "correct": "I'd say", "wrong": ["I would to say", "I'd said", "I'm saying"]}
- reader 1: level: 'I'd say' as a hedge is B1/B2; too easy for C1.
- reader 1: sense: 'I would to say' is an impossible string, not a believable mistake; 'I'd said' and 'I'm saying' are also weak distractors.
- reader 2: instruction: 'I'm saying' is grammatical in some contexts (I'm saying that's about right) so is arguably not wrong; but it does not fit the hedging sense.
- reader 2: level: Easy for C1 (B1 learner could solve it).
- reader 2: sense: 'I would to say' is a random impossible string, not a believable mistake.

## c1-9-012 · C1 · gap · c1-will-1.csv:12

Task: There's the doorbell. That ___ the courier: I'm expecting a parcel. (will / be)
Key: {"kind": "gap", "accepted": [["'ll be", "will be"]]}
- reader 1: instruction: Cue (will / be) gives the form away; only copying/joining is needed. 'must be' would also fit but is excluded by the cue.
- reader 2: another correct answer, not accepted: [['must be'], ['could be'], ['might be'], ['may be']]
- reader 2: instruction: Hint '(will / be)' forces answer but other modals (must/could/might) are correct English here; if hint is ignored many fit. Contraction 'll be' after 'That' should be accepted.
- reader 2: level: B1 level (will for prediction/deduction) not C1.

