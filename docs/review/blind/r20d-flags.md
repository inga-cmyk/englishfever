# Blind check r20d: flags for the judge

7 tasks, 2 readers.

## r20d-001 · B2.2 · text · twins-3.csv:15

Task: Report this. Start with *They asked*: 'What time should we arrive?'
Key: {"kind": "text", "accepted": [["They asked what time they should arrive.", "They asked what time to arrive.", "They asked what time we should arrive.", "They asked me what time they should arrive.", "They asked us what time we should arrive.", "They asked me what time to arrive.", "They asked us what time to arrive.", "They asked what time they ought to arrive.", "They asked what time they were to arrive.", "They asked what time we were to arrive.", "They asked what time we ought to arrive."]]}
- reader 1: another correct answer, not accepted: ['They asked what time we were supposed to arrive.', 'They asked what time we had to arrive.', 'They asked what time I should arrive.', 'They asked what time you should arrive.', 'They asked me what time we should arrive.', 'They asked what time we would have to arrive.']
- reader 1: instruction: Speaker/hearer of the quoted question is not given, so the pronoun (we/they/I/you) is open: many valid answers; the checker must accept them or the task must say who 'we' is. Back-shifting of 'should' is not needed, which a learner may not know.
- reader 2: another correct answer, not accepted: ['They asked me what time we should arrive.', 'They asked what time we had to arrive.']
- reader 2: instruction: Pronoun shift (we/they) is not specified: both 'we should' and 'they should' fit; key must accept both. 'Start with They asked' leaves 'me' optional.
- reader 2: sense: The pronoun is ambiguous: the speaker of the quote may be the same group as 'they'.

## r20d-002 · B2.2 · text · twins-3.csv:23

Task: Join the sentences: She didn't know. Who should she ask?
Key: {"kind": "text", "accepted": [["She didn't know who to ask.", "She didn't know whom to ask.", "She didn't know who she should ask.", "She didn't know whom she should ask.", "She didn't know who she ought to ask.", "She didn't know whom she ought to ask.", "She didn't know who she was to ask.", "She didn't know whom she was to ask."]]}
- reader 1: another correct answer, not accepted: ["She didn't know who she had to ask.", "She didn't know who she was supposed to ask."]
- reader 1: instruction: No hint to use a question word clause; fine, but 'who to ask' is an equally good answer and may not be what the task targets.
- reader 2: another correct answer, not accepted: ["She didn't know who she had to ask.", "She didn't know who she could ask."]
- reader 2: instruction: Fine, but 'Join' does not say how (who ... / who to); two natural answers.
- reader 2: level: Too easy for B2.2: basic embedded question (B1).

## r20d-003 · B2.2 · text · twins-3.csv:27

Task: Rewrite as one sentence. Start with *I'll support you*: It doesn't matter what you decide. I'll support you.
Key: {"kind": "text", "accepted": [["I'll support you whatever you decide.", "I will support you whatever you decide.", "I'll support you no matter what you decide.", "I will support you no matter what you decide.", "I'll support you whichever way you decide.", "I'll support you however you decide.", "I'll support you regardless of what you decide.", "I'll support you whatever decision you make.", "I will support you whatever decision you make.", "I'll support you whatever it is you decide.", "I will support you whatever it is you decide."]]}
- reader 1: another correct answer, not accepted: ["I'll support you whatever you decide to do.", "I'll support you regardless of what you decide to do."]
- reader 1: instruction: 'Rewrite as one sentence' is fine; the target (whatever / no matter what) is not hinted, so several valid structures; 'regardless of' is a different structure and may be rejected.
- reader 2: instruction: Many valid wordings; the target form (whatever / no matter what / regardless of what) is not fixed.

## r20d-004 · B2.2 · gap · typical-b2c1-1.csv:21

Task: I'm not sure what time the meeting ___ tomorrow. (start)
Key: {"kind": "gap", "accepted": [["starts", "will start", "is going to start", "is starting", "is to start", "is due to start"]]}
- reader 1: instruction: Future tense not constrained: 'starts' (timetable) is best, but will start / is starting / is going to start are all correct.
- reader 1: level: Too easy for B2.2 (simple present for a timetable is A2/B1).
- reader 2: another correct answer, not accepted: [['begins']]
- reader 2: instruction: Verb form is not constrained: present simple, present continuous, will all fit; only a timetable-type 'starts' is the likely target.
- reader 2: level: Too easy for B2.2 (embedded question word order, B1).

## r20d-005 · B2.2 · gap · typical-b2c1-1.csv:34

Task: We couldn't decide where ___ on holiday. (go)
Key: {"kind": "gap", "accepted": [["to go", "we should go", "we could go", "we would go", "we'd go", "we were going to go", "we ought to go", "we were going", "we wanted to go", "we were to go"]]}
- reader 1: instruction: Only one gap with (go): 'to go' and 'we should go' both fit; the task does not say which structure is wanted.
- reader 1: level: Wh- word + infinitive is B1; low for B2.2.
- reader 2: instruction: Several gap words may be needed: gap is one slot but 'we should go' is also correct; instruction does not say to use only one word.
- reader 2: level: Too easy for B2.2 (where + to-infinitive, B1).
- reader 2: sense: Ambiguous: 'to go' vs 'we should go'.

## r20d-006 · B2.2 · gap · typical-b2c1-1.csv:40

Task: Our holiday plans depend on ___ my boss gives me the week off or not.
Key: {"kind": "gap", "accepted": [["whether"]]}
- reader 1: another correct answer, not accepted: [['if']]
- reader 1: instruction: 'if' is common (informal, some call it non-standard after a preposition) and may be marked wrong. No hint on the word type.
- reader 1: level: whether/if is B1; low for B2.2.
- reader 2: another correct answer, not accepted: [['if']]
- reader 2: instruction: 'if' is common after depend on in informal English (prescriptively less correct); no hint for the learner.

## r20d-007 · B2.2 · text · unreal-time-1.csv:5

Task: Write one sentence that starts with *It's high time*: You should really start looking for a new job.
Key: {"kind": "text", "accepted": [["It's high time you started looking for a new job.", "It's high time you started to look for a new job.", "It's high time you looked for a new job.", "It is high time you started looking for a new job.", "It is high time you started to look for a new job.", "It is high time you looked for a new job.", "It's high time you began looking for a new job.", "It is high time you began looking for a new job.", "It's high time that you started looking for a new job.", "It is high time that you started looking for a new job.", "It's high time you were looking for a new job.", "It is high time you were looking for a new job.", "It's high time you started job-hunting.", "It is high time you started job-hunting.", "It's high time for you to start looking for a new job.", "It is high time for you to start looking for a new job.", "It's high time you started looking for a job.", "It is high time you started looking for a job.", "It's high time you started your search for a new job.", "It is high time you started your search for a new job."]]}
- reader 1: another correct answer, not accepted: ["It's high time you start looking for a new job.", "It's high time you got started looking for a new job.", "It's high time you began to look for a new job."]
- reader 1: instruction: The starter does not signal the past-tense form, which is the point, but present 'start' is also used (less formal) and 'for you to start' is correct; many answers to accept.
- reader 2: another correct answer, not accepted: ["It's high time you start looking for a new job.", "It's high time you found a new job.", "It's high time you really started looking for a new job.", "It's about high time you started looking for a new job."]
- reader 2: instruction: Too open: past subjunctive (you started) vs 'you start' (accepted by some) vs 'for you to start'; the target structure is not clear.

