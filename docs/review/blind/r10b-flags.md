# Blind check r10b: flags for the judge

2 tasks, 2 readers.

## r10b-001 · B1.1 · order · zz-blind-gap-points-b11-1.csv:85

Task: Put the words in order to make a question.
word_cards: passes | our | to | boarding | do | we | have | print
Key: {"kind": "order", "sentence": "do we have to print our boarding passes", "also": []}
- reader 1: level: Order-only task with 8 cards is fine, but have to is a bit light for B1.1 (it is common at A2/B1.1 border); acceptable.

## r10b-002 · B1.1 · order · zz-blind-gap-points-b11-1.csv:86

Task: Put the words in order to make a question.
word_cards: to | the | latvian | new | speak | have | does | manager
Key: {"kind": "order", "sentence": "does the new manager have to speak latvian", "also": []}
- reader 1: sense: Card 'latvian' is lower case; the correct sentence needs a capital L, so check the checker is case-insensitive and that learners are not confused.
- reader 2: another correct answer, not accepted: ['does the new latvian manager have to speak']
- reader 2: sense: Second order (Latvian manager, verb 'speak' without object) is grammatical but incomplete in meaning/less natural; consider changing a card (e.g. 'Latvian' as adjective is ambiguous). Card 'latvian' is lower case, so the capital clue is lost.

