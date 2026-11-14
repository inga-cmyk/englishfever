# Blind check r8b: flags for the judge

7 tasks, 2 readers.

## r8b-001 · B1.2 · gap · wish-rather-1.csv:12

Task: I wish my sister ___ nearer. (live)
Key: {"kind": "gap", "accepted": [["lived", "could live"]]}
- reader 2: another correct answer, not accepted: ["would live (possible if the speaker means the sister's choice, but weaker with a state verb)"]

## r8b-004 · B1.2 · gap · wish-rather-1.csv:16

Task: My boss is very strict. I wish he ___ more relaxed. (be)
Key: {"kind": "gap", "accepted": [["were", "was"]]}
- reader 2: another correct answer, not accepted: ['could be', 'would be (wish about his behaviour)']

## r8b-007 · B1.2 · text · wish-rather-1.csv:42

Task: Start with *I'd rather*: I don't want to go to the beach. I want to go to the mountains.
Key: {"kind": "text", "accepted": [["I'd rather go to the mountains than to the beach.", "I'd rather go to the mountains than go to the beach.", "I would rather go to the mountains than to the beach.", "I would rather go to the mountains than go to the beach.", "I'd rather go to the mountains.", "I would rather go to the mountains.", "I'd rather not go to the beach.", "I would rather not go to the beach."]]}
- reader 1: another correct answer, not accepted: ["I'd rather go to the mountains than the beach."]
- reader 1: instruction: The instruction does not say that one sentence must cover both ideas, so 'I'd rather go to the mountains.' or 'I'd rather not go to the beach.' are reasonable responses. Say 'Make one sentence with I'd rather ... than ...' if the than-form is the target.
- reader 2: another correct answer, not accepted: ["I'd rather go to the mountains than the beach.", "I'd rather not go to the beach. I'd rather go to the mountains.", "I'd rather go to the mountains, not to the beach."]
- reader 2: instruction: Two input sentences but the instruction does not say to make ONE sentence or to use 'than', so the learner cannot know which of many correct outputs is expected ('I'd rather not go to the beach.', 'I'd rather go to the mountains.', '... than the beach', '... than to the beach', '... than go to the beach'). The key must accept all of these, or the instruction should say 'one sentence with than'.

