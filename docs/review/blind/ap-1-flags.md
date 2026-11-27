# Blind check ap-1: flags for the judge

28 tasks, 2 readers.

## ap-1-005 · B1.1 · mcq · zz-blind-active-passive-1.csv:6

Task: Choose the correct option: Sorry, I can't hold the pen properly. I ___ by a bee while I was working in the garden.
options: was stinging | stung | was stung | am stung
Key: {"kind": "mcq", "correct": "was stung", "wrong": ["stung", "am stung", "was stinging"]}
- reader 1: instruction: 'Sorry, I can't hold the pen properly' is superfluous: without it only 'was stung' is still possible.

## ap-1-011 · B1.1 · order · zz-blind-active-passive-1.csv:12

Task: Put the words in order.
word_cards: once | are | our | the | a | cleaned | building | in | month | windows
Key: {"kind": "order", "sentence": "the windows in our building are cleaned once a month", "also": ["once a month the windows in our building are cleaned"]}
- reader 1: another correct answer, not accepted: ['our windows in the building are cleaned once a month', 'once a month our windows in the building are cleaned', 'in our building the windows are cleaned once a month', 'once a month in our building the windows are cleaned', 'in the building our windows are cleaned once a month']
- reader 1: instruction: Several natural orders use all cards (the/our swap, adverbial first); no hint which is wanted. Words are already in target order mostly.
- reader 2: another correct answer, not accepted: [['in our building the windows are cleaned once a month'], ['once a month in our building the windows are cleaned'], ['the windows are cleaned in our building once a month'], ['in our building once a month the windows are cleaned']]
- reader 2: instruction: Many natural orders possible (adverbial can go at start, middle or end); the task has no single answer unless the checker accepts all.

## ap-1-012 · B1.1 · order · zz-blind-active-passive-1.csv:13

Task: Put the words in order.
word_cards: built | when | was | this | church
Key: {"kind": "order", "sentence": "when was this church built", "also": []}
- reader 1: instruction: No capital letter or question mark shown: 'when' could start a statement; only a swap of two words.
- reader 1: level: Too easy for B1.1: five cards, A2-level question order.
- reader 2: another correct answer, not accepted: [['when this church was built']]
- reader 2: instruction: Only five cards and the question word starts the sentence: very easy, almost no reordering. Without punctuation 'when this church was built' (a clause) also uses all cards.
- reader 2: level: Easy for B1.1 (A2-level word order).

## ap-1-015 · B1.1 · gap · zz-blind-active-passive-1.csv:16

Task: In many Spanish families, dinner ___ ___ quite late, often after nine.
word_cards: eaten | is | ate | was
Key: {"kind": "gap", "accepted": [["is"], ["eaten"]]}
- reader 1: sense: 'was eaten' is grammatical (past habit) though 'often' suggests present; weak distractor risk.
- reader 2: instruction: No tense cue: 'was eaten' is grammatical (past habit/history) though less natural; learner cannot tell which is wanted.

## ap-1-016 · B1.1 · gap · zz-blind-active-passive-1.csv:17

Task: The police ___ the thief two hours after the robbery.
word_cards: was caught | catch | were caught | caught
Key: {"kind": "gap", "accepted": [["caught"]]}
- reader 1: level: Very easy: only an active verb in the past; one gap though the note says cards go in each gap.

## ap-1-020 · B1.1 · gap · zz-blind-active-passive-1.csv:21

Task: What ___ at the meeting yesterday? Nobody tells me anything! (happen)
Key: {"kind": "gap", "accepted": [["happened"]]}
- reader 1: instruction: 'Nobody tells me anything!' is superfluous: without it only 'happened' is possible.
- reader 2: instruction: 'Nobody tells me anything!' is not needed: 'What ___ at the meeting yesterday? (happen)' already gives only 'happened'.

## ap-1-022 · B1.1 · gap · zz-blind-active-passive-1.csv:23

Task: Our teacher ___ us homework every Friday, and today is Friday! (give)
Key: {"kind": "gap", "accepted": [["gives"]]}
- reader 1: instruction: 'and today is Friday!' is superfluous: only 'gives' fits without it.

## ap-1-023 · B1.1 · text · zz-blind-active-passive-1.csv:24

Task: Correct the mistake: My phone repaired in only twenty minutes yesterday.
Key: {"kind": "text", "accepted": [["My phone was repaired in only twenty minutes yesterday.", "Yesterday my phone was repaired in only twenty minutes."]]}
- reader 1: another correct answer, not accepted: ['My phone got repaired in only twenty minutes yesterday.']
- reader 1: instruction: Does not say what kind of mistake; fine, but 'got repaired' is a correct colloquial fix.
- reader 2: another correct answer, not accepted: ['My phone got repaired in only twenty minutes yesterday.']

## ap-1-026 · B1.1 · text · zz-blind-active-passive-1.csv:27

Task: Start with *My keys*: Someone found my keys in the car.
Key: {"kind": "text", "accepted": [["My keys were found in the car."]]}
- reader 1: another correct answer, not accepted: ['My keys were found in the car by someone.']
- reader 1: instruction: '*My keys*' shows asterisks; the start gives away the passive.
- reader 2: another correct answer, not accepted: ['My keys were found in the car by someone.', 'My keys have been found in the car.']
- reader 2: instruction: 'by someone' is optional; answer with or without it is correct.

## ap-1-027 · B1.1 · text · zz-blind-active-passive-1.csv:28

Task: Start with *A lot of rice*: They grow a lot of rice in this region.
Key: {"kind": "text", "accepted": [["A lot of rice is grown in this region."]]}
- reader 1: another correct answer, not accepted: ['A lot of rice grows in this region.']
- reader 1: instruction: Instruction does not say passive: 'A lot of rice grows in this region' is correct English too (active, intransitive).

