# Blind check cm-1: flags for the judge

28 tasks, 2 readers.

## cm-1-001 · A2.1 · text · zz-blind-correct-mistake-1.csv:2

Task: Correct the mistake: My sister work in a hotel and she loves it.
Key: {"kind": "text", "accepted": [["My sister works in a hotel and she loves it."]]}
- reader 1: another correct answer, not accepted: ['My sister is working in a hotel and she loves it.']
- reader 2: another correct answer, not accepted: ['My sisters work in a hotel and they love it.']

## cm-1-002 · A2.1 · text · zz-blind-correct-mistake-1.csv:3

Task: Correct the mistake: I am agree with you about the price.
Key: {"kind": "text", "accepted": [["I agree with you about the price."]]}
- reader 2: another correct answer, not accepted: ['I do agree with you about the price.']

## cm-1-003 · A2.1 · text · zz-blind-correct-mistake-1.csv:4

Task: Correct the mistake: Do your brother play any sport?
Key: {"kind": "text", "accepted": [["Does your brother play any sport?"]]}
- reader 1: another correct answer, not accepted: ['Do your brothers play any sport?']
- reader 2: another correct answer, not accepted: ['Do your brothers play any sport?']

## cm-1-006 · A2.2 · text · zz-blind-correct-mistake-1.csv:7

Task: Correct the mistake: Sorry, I am not understanding the question. Can you say it again?
Key: {"kind": "text", "accepted": [["Sorry, I don't understand the question. Can you say it again?"]]}
- reader 1: another correct answer, not accepted: ["Sorry, I don't understand the question. Could you say it again?"]
- reader 2: another correct answer, not accepted: ["Sorry, I can't understand the question. Can you say it again?", "Sorry, I didn't understand the question. Can you say it again?"]

## cm-1-007 · B1.1 · text · zz-blind-correct-mistake-1.csv:8

Task: Correct the mistake: I'm thinking this plan is too expensive for us, so let's look for another one.
Key: {"kind": "text", "accepted": [["I think this plan is too expensive for us, so let's look for another one."]]}
- reader 1: another correct answer, not accepted: ["I think that this plan is too expensive for us, so let's look for another one."]
- reader 2: another correct answer, not accepted: ["I thought this plan is too expensive for us, so let's look for another one.", "I do think this plan is too expensive for us, so let's look for another one."]
- reader 2: sense: Not clearly wrong: 'I'm thinking (that) this plan is too expensive' is acceptable in informal English (opinion forming now). A learner who leaves it unchanged has a defensible sentence; the 'mistake' is only a stative-verb rule of thumb.

## cm-1-008 · B1.1 · text · zz-blind-correct-mistake-1.csv:9

Task: Correct the mistake: Water is boiling at 100 degrees Celsius, so the thermometer will show 100 when it starts to bubble.
Key: {"kind": "text", "accepted": [["Water boils at 100 degrees Celsius, so the thermometer will show 100 when it starts to bubble."]]}
- reader 2: another correct answer, not accepted: ['Water always boils at 100 degrees Celsius, so the thermometer will show 100 when it starts to bubble.']

## cm-1-009 · B1.1 · text · zz-blind-correct-mistake-1.csv:10

Task: Correct the mistake: It's depend on the weather, so we'll decide about the picnic tomorrow morning.
Key: {"kind": "text", "accepted": [["It depends on the weather, so we'll decide about the picnic tomorrow morning."]]}
- reader 2: another correct answer, not accepted: ["It all depends on the weather, so we'll decide about the picnic tomorrow morning.", "It will depend on the weather, so we'll decide about the picnic tomorrow morning."]

## cm-1-016 · B1.1 · text · zz-blind-correct-mistake-1.csv:17

Task: Correct the mistake: I have lost my keys yesterday, so I had to call a locksmith.
Key: {"kind": "text", "accepted": [["I lost my keys yesterday, so I had to call a locksmith."]]}
- reader 2: another correct answer, not accepted: ['I lost my keys, so I had to call a locksmith.']

## cm-1-019 · A2.1 · text · zz-blind-correct-mistake-1.csv:20

Task: Correct the mistake: I'm going visit my parents this weekend.
Key: {"kind": "text", "accepted": [["I'm going to visit my parents this weekend."]]}
- reader 1: another correct answer, not accepted: ["I'm visiting my parents this weekend.", 'I am visiting my parents this weekend.', "I'll visit my parents this weekend. (less natural for a plan)"]
- reader 2: another correct answer, not accepted: ["I'm visiting my parents this weekend.", 'I am visiting my parents this weekend.', "I'll visit my parents this weekend.", 'I will visit my parents this weekend.']

## cm-1-020 · A2.1 · text · zz-blind-correct-mistake-1.csv:21

Task: Correct the mistake: She going to look for a new flat in May.
Key: {"kind": "text", "accepted": [["She is going to look for a new flat in May.", "She's going to look for a new flat in May."]]}
- reader 1: another correct answer, not accepted: ['She is looking for a new flat in May.', "She's looking for a new flat in May.", 'She will look for a new flat in May. (less natural)']
- reader 2: another correct answer, not accepted: ['She is looking for a new flat in May.', "She's looking for a new flat in May.", 'She will look for a new flat in May.', "She'll look for a new flat in May."]

## cm-1-021 · A2.1 · text · zz-blind-correct-mistake-1.csv:22

Task: Correct the mistake: Will I open the window? It's very hot in here.
Key: {"kind": "text", "accepted": [["Shall I open the window? It's very hot in here.", "Should I open the window? It's very hot in here."]]}
- reader 1: another correct answer, not accepted: ["Can I open the window? It's very hot in here.", "May I open the window? It's very hot in here."]
- reader 1: sense: Two corrections fit equally (Shall/Should/Can I); the mistake is only 'Will I' and the fix is not unique in meaning (Can I asks permission).
- reader 2: another correct answer, not accepted: ["Can I open the window? It's very hot in here.", "Could I open the window? It's very hot in here.", "May I open the window? It's very hot in here.", "Do you want me to open the window? It's very hot in here."]

## cm-1-022 · A2.2 · text · zz-blind-correct-mistake-1.csv:23

Task: Correct the mistake: Your bag looks heavy. I carry it for you.
Key: {"kind": "text", "accepted": [["Your bag looks heavy. I'll carry it for you.", "Your bag looks heavy. I will carry it for you."]]}
- reader 1: another correct answer, not accepted: ['I can carry it for you.']
- reader 2: another correct answer, not accepted: ['Your bag looks heavy. I can carry it for you.', 'Your bag looks heavy. Let me carry it for you.', "Your bag looks heavy. I'm going to carry it for you. (less natural)"]

## cm-1-023 · A2.2 · text · zz-blind-correct-mistake-1.csv:24

Task: Correct the mistake: I meet Anna for lunch tomorrow, so I can't help you then.
Key: {"kind": "text", "accepted": [["I'm meeting Anna for lunch tomorrow, so I can't help you then.", "I'm going to meet Anna for lunch tomorrow, so I can't help you then."]]}
- reader 1: another correct answer, not accepted: ["I will meet Anna for lunch tomorrow, so I can't help you then. (less natural for an arrangement)"]
- reader 2: another correct answer, not accepted: ["I'll meet Anna for lunch tomorrow, so I can't help you then. (less natural)"]
- reader 2: sense: Possibly not a clear mistake: present simple 'I meet Anna for lunch tomorrow' is acceptable for a fixed arrangement/routine in some usage; a learner may reasonably leave it. Typical L1 slip, but not unambiguously wrong.

## cm-1-024 · A2.2 · text · zz-blind-correct-mistake-1.csv:25

Task: Correct the mistake: What you are going to do after the course?
Key: {"kind": "text", "accepted": [["What are you going to do after the course?", "After the course, what are you going to do?"]]}
- reader 1: another correct answer, not accepted: ['What are you doing after the course?', 'What will you do after the course?']
- reader 2: another correct answer, not accepted: ['What will you do after the course?', 'What are you doing after the course?']

## cm-1-025 · B1.1 · text · zz-blind-correct-mistake-1.csv:26

Task: Correct the mistake: I promise I tell you as soon as I hear any news about the job.
Key: {"kind": "text", "accepted": [["I promise I'll tell you as soon as I hear any news about the job.", "I promise I will tell you as soon as I hear any news about the job.", "I promise to tell you as soon as I hear any news about the job.", "As soon as I hear any news about the job, I promise I'll tell you.", "As soon as I hear any news about the job, I promise I will tell you.", "As soon as I hear any news about the job, I promise to tell you."]]}
- reader 1: another correct answer, not accepted: ["I promise I'm going to tell you as soon as I hear any news about the job. (less natural)"]
- reader 2: another correct answer, not accepted: ["I promise I'm going to tell you as soon as I hear any news about the job. (less natural)"]

## cm-1-026 · B1.1 · text · zz-blind-correct-mistake-1.csv:27

Task: Correct the mistake: Are you going to sell your old car or you are going to keep it?
Key: {"kind": "text", "accepted": [["Are you going to sell your old car or are you going to keep it?", "Are you going to sell your old car or keep it?"]]}
- reader 1: another correct answer, not accepted: ['Are you going to sell your old car or will you keep it?', 'Are you going to sell your old car or are you keeping it?']
- reader 2: another correct answer, not accepted: ['Are you going to sell your old car or are you keeping it?', 'Are you going to sell or keep your old car?']

## cm-1-027 · B1.2 · text · zz-blind-correct-mistake-1.csv:28

Task: Correct the mistake: The car won't start this morning, so I took the bus to work.
Key: {"kind": "text", "accepted": [["The car wouldn't start this morning, so I took the bus to work.", "The car didn't start this morning, so I took the bus to work."]]}
- reader 1: another correct answer, not accepted: ["The car won't start this morning, so I'll take the bus to work."]
- reader 1: sense: Fix is not unique: change won't to wouldn't/didn't, or change took to 'I'll take' (present reading of 'this morning'). Also the point (wouldn't = refused to) is rather subtle for a plain 'correct the mistake' task.
- reader 2: another correct answer, not accepted: ["The car won't start this morning, so I'll take the bus to work.", 'The car will not start this morning, so I will take the bus to work.']
- reader 2: sense: Ambiguous target: the mistake can be fixed in either clause (won't->wouldn't/didn't, or took->'ll take). Both repairs are correct English; 'wouldn't' (refusal) is also a nuance beyond plain B1.2 for some learners.

## cm-1-028 · B1.2 · text · zz-blind-correct-mistake-1.csv:29

Task: Correct the mistake: Hurry up! The film is about starting.
Key: {"kind": "text", "accepted": [["Hurry up! The film is about to start."]]}
- reader 1: another correct answer, not accepted: ['Hurry up! The film is going to start.', 'Hurry up! The film is starting.', 'Hurry up! The film is just about to start.']
- reader 2: another correct answer, not accepted: ['Hurry up! The film is starting.', 'Hurry up! The film is going to start.', 'Hurry up! The film is about to begin.', 'Hurry up! The film is just about to start.', 'Hurry up! The film starts soon.']

