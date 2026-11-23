# Blind check c1-12: flags for the judge

10 tasks, 2 readers.

## c1-12-001 · C1 · mcq · c1-agree-1.csv:8

Task: Which sentence has a mistake?
options: More than one guest has complained about the noise. | Neither of the answers is correct. | One in four adults has never been abroad. | Each of the rooms have a private bathroom.
Key: {"kind": "mcq", "correct": "Each of the rooms have a private bathroom.", "wrong": ["More than one guest has complained about the noise.", "Neither of the answers is correct.", "One in four adults has never been abroad."]}
- reader 2: sense: Spoken English often uses 'have' after 'each of the plural'; some learners/natives would not see it as wrong, but formal rule says 'has'. 'More than one guest has' is a tricky-looking but correct form; fine.

## c1-12-002 · C1 · mcq · c1-can-1.csv:12

Task: Choose the correct option: The forecast says snow until April, so this winter ___ unusually long.
options: may being | may be | is able to be | can be
Key: {"kind": "mcq", "correct": "may be", "wrong": ["can be", "is able to be", "may being"]}
- reader 1: level: may be for a forecast is B1; the task is not C1 (may vs can) and the clue 'The forecast says' gives it away.
- reader 2: a wrong option that fits: can be (weakly: 'can' = general possibility, odd for one specific winter; 'is able to be' is not natural)
- reader 2: sense: 'may' sits oddly after 'so' with a forecast of snow until April: 'will be/is going to be' would be the logical result; 'may' is weak. 'can be' is arguably wrong only on nuance, so the item depends on a subtle distinction.

## c1-12-003 · C1 · text · c1-order-1.csv:13

Task: Put the focus on *the noise*. Start with *What*: The noise really annoys me.
Key: {"kind": "text", "accepted": [["What really annoys me is the noise."]]}
- reader 1: another correct answer, not accepted: ['What annoys me is the noise.']
- reader 1: instruction: 'What annoys me is the noise' (dropping 'really') is also accepted by many learners; the key should say whether 'really' must be kept.
- reader 2: another correct answer, not accepted: [['What annoys me really is the noise.'], ['What annoys me is the noise.']]
- reader 2: instruction: 'Put the focus on' is vague jargon; 'Start with What' gives the structure away. The learner must know to add 'is'.

## c1-12-004 · C1 · mcq · c1-order-1.csv:14

Task: Choose the correct option: Look, there's our bus! Here ___!
options: it comes | comes it | does it come | it is coming
Key: {"kind": "mcq", "correct": "it comes", "wrong": ["comes it", "does it come", "it is coming"]}
- reader 1: level: Fixed phrase 'Here it comes' is A2/B1, not C1; no nuance or use point.
- reader 2: level: Here + subject pronoun is a basic B1 pattern; easy for C1.

## c1-12-005 · C1 · gap · c1-perf-1.csv:6

Task: I'll text you the moment I ___ my exam results. (get)
Key: {"kind": "gap", "accepted": [["'ve got", "get", "have got", "'ve gotten", "have gotten", "have received", "'ve received"]]}
- reader 1: instruction: The verb is given in brackets so only the form matters; 'have got' (the moment I've got) is also possible, less natural.
- reader 1: level: Time clause after 'the moment' with present simple is B1, too easy for C1.
- reader 2: instruction: The verb is given in brackets and no change is needed except 'get'; the trap is not visible.
- reader 2: level: Time clause with present simple is B1; too easy for C1.
- reader 2: sense: 'the moment I've got' is possible but less natural; US 'have gotten' also works.

## c1-12-006 · C1 · text · c1-perf-1.csv:14

Task: Report what she said with *deny* and *having*. Her words: 'I didn't read the letter.'
Key: {"kind": "text", "accepted": [["She denied having read the letter.", "She denied reading the letter."]]}
- reader 1: another correct answer, not accepted: ['She denied having read it.']
- reader 2: another correct answer, not accepted: [['She denied having read it.']]
- reader 2: instruction: Giving 'deny' and 'having' reveals the whole structure; only copying left.

## c1-12-007 · C1 · text · c1-prep-1.csv:12

Task: Make it more formal. Start with *The colleague with*: The colleague I share an office with is on holiday.
Key: {"kind": "text", "accepted": [["The colleague with whom I share an office is on holiday."]]}
- reader 2: another correct answer, not accepted: [['The colleague with whom I share my office is on holiday.']]
- reader 2: instruction: 'Start with The colleague with' gives away 'whom'.
- reader 2: sense: 'Make it more formal' with a fixed start leaves essentially one answer; fine.

## c1-12-008 · C1 · text · c1-prep-1.csv:13

Task: Make it less formal. End the first part with *to*: The person to whom I spoke was very helpful.
Key: {"kind": "text", "accepted": [["The person I spoke to was very helpful.", "The person who I spoke to was very helpful.", "The person that I spoke to was very helpful."]]}
- reader 1: another correct answer, not accepted: ['The person whom I spoke to was very helpful.']
- reader 1: level: Preposition stranding / dropping whom is B1-B2 rather than C1.
- reader 2: another correct answer, not accepted: [['The person who(m) I spoke to was very helpful.']]
- reader 2: instruction: 'End the first part' is unclear: the learner must guess which part is meant.
- reader 2: level: B1/B2 level point, rather easy for C1.

## c1-12-009 · C1 · gap · c1-subj-1.csv:4

Task: It's odd that she ___ ___ ___ that at yesterday's meeting. She's usually so polite.
word_cards: has | say | have | should | said
Key: {"kind": "gap", "accepted": [["should"], ["have"], ["said"]]}
- reader 2: a wrong option that fits: has (not with 3 gaps/'yesterday')
- reader 2: instruction: The 'yesterday's meeting' cue is needed; fine. Number of gaps (3) gives away a three-word form.
- reader 2: level: Putative 'should have said' is good B2/C1.

## c1-12-010 · C1 · gap · c1-subj-1.csv:13

Task: It's odd that she ___ ___ that whenever the topic comes up. She knows it isn't true.
word_cards: say | should | said | has
Key: {"kind": "gap", "accepted": [["should"], ["say"]]}
- reader 1: a wrong option that fits: 'has said' (present perfect) is possible with 'whenever', but less natural than 'should say'.
- reader 1: sense: 'whenever the topic comes up' suggests habit; a learner may reasonably expect 'says', so 'has said' is a believable but weaker alternative.
- reader 2: a wrong option that fits: has / said (as the pair 'has said': 'It's odd that she has said that whenever the topic comes up' is grammatical, though less natural)
- reader 2: instruction: The two items 009/010 share cards and sentence; learner can solve 010 by elimination from 009. Gap count (2) is a clue.
- reader 2: sense: 'has said ... whenever' competes with 'should say'; ambiguity risk.

