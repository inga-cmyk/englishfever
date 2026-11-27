# Blind check ap-2: flags for the judge

8 tasks, 2 readers.

## ap-2-002 · B1.1 · order · zz-blind-active-passive-1.csv:12

Task: Put the words in order.
word_cards: collected | every | is | rubbish | tuesday | the
Key: {"kind": "order", "sentence": "the rubbish is collected every tuesday", "also": ["every tuesday the rubbish is collected"]}
- reader 1: sense: Card 'tuesday' is lower case; a day name needs a capital, and a learner may hesitate.

## ap-2-004 · B1.1 · gap · zz-blind-active-passive-1.csv:16

Task: These days, in many Spanish families, dinner ___ ___ quite late, often after nine.
word_cards: eaten | is | was | ate
Key: {"kind": "gap", "accepted": [["is"], ["eaten"]]}
- reader 2: instruction: Cards make it a choice of is/was; 'These days' is a clear cue, so very easy.

## ap-2-005 · B1.1 · gap · zz-blind-active-passive-1.csv:21

Task: What ___ at the meeting yesterday? (happen)
Key: {"kind": "gap", "accepted": [["happened"]]}
- reader 1: another correct answer, not accepted: [['was happening']]
- reader 1: instruction: Task has an active verb in a passive-voice exercise, so it is a trap/unclear why it is here; two answers (happened / was happening, the latter less natural).
- reader 1: sense: Not a passive item; sits oddly among passive tasks.
- reader 2: another correct answer, not accepted: [['was happening']]
- reader 2: sense: Active verb in a passive set; 'was happening' is also correct English (less natural for a single event).

## ap-2-006 · B1.1 · text · zz-blind-active-passive-1.csv:24

Task: Correct the mistake: My phone repaired in only twenty minutes yesterday.
Key: {"kind": "text", "accepted": [["My phone was repaired in only twenty minutes yesterday.", "My phone got repaired in only twenty minutes yesterday.", "Yesterday my phone was repaired in only twenty minutes.", "Yesterday my phone got repaired in only twenty minutes."]]}
- reader 2: another correct answer, not accepted: ['My phone was fixed in only twenty minutes yesterday.', 'My phone has been repaired in only twenty minutes.']

## ap-2-007 · B1.1 · text · zz-blind-active-passive-1.csv:27

Task: Start with *My keys*: Someone found my keys in the car.
Key: {"kind": "text", "accepted": [["My keys were found in the car.", "My keys were found in the car by someone.", "My keys have been found in the car."]]}
- reader 1: another correct answer, not accepted: ['My keys were found by someone in the car.']
- reader 1: instruction: Instruction shows markdown asterisks around 'My keys'. 'by someone' is optional, so learners may disagree on whether to include it.
- reader 2: another correct answer, not accepted: ['My keys were found by someone in the car.']
- reader 2: instruction: Does not say to use the passive; the learner must guess. Other tenses/by-agent versions are acceptable.

## ap-2-008 · B1.1 · text · zz-blind-active-passive-1.csv:28

Task: Start with *A lot of rice*: They grow a lot of rice in this region.
Key: {"kind": "text", "accepted": [["A lot of rice is grown in this region.", "A lot of rice grows in this region."]]}
- reader 1: another correct answer, not accepted: ['A lot of rice is grown in this region by them.', 'A lot of rice is grown by them in this region.']
- reader 1: instruction: Asterisks shown in instruction. 'by them' is unnecessary but a learner may add it.
- reader 2: another correct answer, not accepted: ['A lot of rice has been grown in this region.', 'A lot of rice is grown in this region by them.']
- reader 2: instruction: 'Start with' does not require the passive; 'A lot of rice grows in this region' is correct English and avoids the target grammar.

