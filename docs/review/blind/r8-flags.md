# Blind check r8: flags for the judge

50 tasks, 2 readers.

## r8-011 · B1.2 · gap · wish-rather-1.csv:12

Task: I wish my sister ___ nearer. (live)
Key: {"kind": "gap", "accepted": [["lived"]]}
- reader 1: another correct answer, not accepted: [['could live']]
- reader 2: another correct answer, not accepted: [['could live']]
- reader 2: instruction: The gap takes 'missing word(s)', so 'could live' (fully correct and natural: she can't live nearer, e.g. because of work) must be accepted or the cue should force one word.

## r8-012 · B1.2 · gap · wish-rather-1.csv:13

Task: I can't dance. I wish I ___ dance.
Key: {"kind": "gap", "accepted": [["could"]]}
- reader 2: another correct answer, not accepted: [['was able to'], ['were able to']]
- reader 2: instruction: No bracketed cue (unlike the other typed gaps); 'was/were able to' is also correct in a 'word(s)' gap.

## r8-013 · B1.2 · text · wish-rather-1.csv:14

Task: Start with *I wish*: I don't speak French.
Key: {"kind": "text", "accepted": [["I wish I spoke French.", "I wish I could speak French."]]}
- reader 1: another correct answer, not accepted: ['I wish I knew French.']
- reader 2: another correct answer, not accepted: ['I wish I knew French.']
- reader 2: instruction: 'I wish I could speak French' is at least as natural as 'spoke' and must be accepted.

## r8-014 · B1.2 · text · wish-rather-1.csv:15

Task: Start with *If only*: I don't have enough time.
Key: {"kind": "text", "accepted": [["If only I had enough time.", "If only I had more time."]]}
- reader 2: instruction: Learners will naturally end 'If only...' with '!'; make sure the checker accepts it. 'more time' is an equally natural rewrite.

## r8-015 · B1.2 · text · wish-rather-1.csv:16

Task: Start with *I wish*: My job is boring.
Key: {"kind": "text", "accepted": [["I wish my job wasn't boring.", "I wish my job weren't boring.", "I wish my job was more interesting.", "I wish my job were more interesting.", "I wish my job was not boring.", "I wish my job were not boring."]]}
- reader 1: another correct answer, not accepted: ["I wish my job wasn't so boring.", 'I wish my job was interesting.', 'I wish my job was more exciting.', 'I wish I had a more interesting job.', 'I wish I had a different job.']
- reader 1: instruction: Very open: no target wording, so many correct sentences (wasn't/weren't boring, was/were more interesting, had a better job...); checker must accept all of them.
- reader 2: another correct answer, not accepted: ['I wish my job was less boring.', 'I wish my job were less boring.', "I wish my job wasn't so boring.", 'I wish I had a more interesting job.']
- reader 2: instruction: Very open: many correct rewrites (wasn't/weren't/was not, more interesting, less boring, so boring, I had a more interesting job). The key must list them all or the task should give more guidance (e.g. 'use interesting').

## r8-023 · B1.2 · gap · wish-rather-1.csv:24

Task: If only it ___ sunny today!
word_cards: is | were | will
Key: {"kind": "gap", "accepted": [["were"]]}
- reader 1: sense: Card 'will' alone gives 'If only it will sunny today', which no learner would build; 'will be' would be the believable mistake but needs two words in a one-gap task.

## r8-025 · B1.2 · match · wish-rather-1.csv:26

Task: Match each fact with the wish.
left: I don't have a car. | I can't sing. | My room is small. | I don't know her name.
right: I wish I knew it. | I wish it were bigger. | I wish I had one. | I wish I could sing.
Key: {"kind": "match", "pairs": [["I don't have a car.", "I wish I had one."], ["I can't sing.", "I wish I could sing."], ["My room is small.", "I wish it were bigger."], ["I don't know her name.", "I wish I knew it."]]}
- reader 2: sense: 'I wish I knew it.' is a little stiff; a native would more likely say 'I wish I knew it' only in context, or 'I wish I knew her name.' Minor.

## r8-037 · B1.2 · gap · wish-rather-1.csv:38

Task: I'd prefer ___ by the window. (sit)
Key: {"kind": "gap", "accepted": [["to sit"]]}
- reader 1: another correct answer, not accepted: [['sitting']]

## r8-041 · B1.2 · text · wish-rather-1.csv:42

Task: Ask with *Would you rather*: go to the beach or to the mountains?
Key: {"kind": "text", "accepted": [["Would you rather go to the beach or to the mountains?", "Would you rather go to the beach or the mountains?"]]}
- reader 1: instruction: Gives the answer away: the learner only adds 'Would you rather' in front of the given words; no grammar decision is needed.

## r8-042 · B1.2 · order · wish-rather-1.csv:43

Task: Put the words in order.
word_cards: rather | i'd | in | stay | tonight
Key: {"kind": "order", "sentence": "i'd rather stay in tonight", "also": []}
- reader 2: instruction: Two valid orders: 'tonight' can also go first.

## r8-043 · B1.2 · order · wish-rather-1.csv:44

Task: Put the words in order to make a question.
word_cards: rather | you | would | have | coffee | or | tea
Key: {"kind": "order", "sentence": "would you rather have tea or coffee", "also": []}
- reader 1: instruction: Two equally correct orders (coffee or tea / tea or coffee); both must be accepted.
- reader 2: instruction: Two valid orders: 'coffee or tea' and 'tea or coffee' are both correct; the checker must accept both.

