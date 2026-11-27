# Blind check cm-2: flags for the judge

15 tasks, 2 readers.

## cm-2-003 · B1.1 · text · correct-mistake-1.csv:8

Task: Correct the mistake: I'm thinking this plan is too expensive for us, so let's look for another one.
Key: {"kind": "text", "accepted": [["I think this plan is too expensive for us, so let's look for another one.", "I think that this plan is too expensive for us, so let's look for another one."]]}
- reader 2: another correct answer, not accepted: ["I do think this plan is too expensive for us, so let's look for another one."]

## cm-2-004 · B1.1 · text · correct-mistake-1.csv:9

Task: Correct the mistake: Light is travelling faster than sound, so you see the lightning before you hear the thunder.
Key: {"kind": "text", "accepted": [["Light travels faster than sound, so you see the lightning before you hear the thunder."]]}
- reader 2: another correct answer, not accepted: ['Light is faster than sound, so you see the lightning before you hear the thunder.']

## cm-2-005 · B1.1 · text · correct-mistake-1.csv:10

Task: Correct the mistake: It's depend on the traffic, so I can't say what time I'll be home.
Key: {"kind": "text", "accepted": [["It depends on the traffic, so I can't say what time I'll be home."]]}
- reader 2: another correct answer, not accepted: ["It all depends on the traffic, so I can't say what time I'll be home.", "It does depend on the traffic, so I can't say what time I'll be home."]

## cm-2-006 · B1.1 · text · correct-mistake-1.csv:17

Task: Correct the mistake: I have seen this film yesterday, so let's watch something else tonight.
Key: {"kind": "text", "accepted": [["I saw this film yesterday, so let's watch something else tonight."]]}
- reader 1: another correct answer, not accepted: ["I watched this film yesterday, so let's watch something else tonight.", "I have seen this film, so let's watch something else tonight.", "I've seen this film, so let's watch something else tonight."]
- reader 1: sense: The sentence has two valid fixes (change the tense, or delete 'yesterday'); the instruction does not say which to keep, so a correct 'I've seen this film' may be marked wrong.
- reader 2: another correct answer, not accepted: ["I watched this film yesterday, so let's watch something else tonight.", "I have seen this film, so let's watch something else tonight. (deletes 'yesterday'; correct but changes the sentence)"]

## cm-2-009 · A2.1 · text · correct-mistake-1.csv:22

Task: Correct the mistake: Will I turn on the heating? It's very cold in here.
Key: {"kind": "text", "accepted": [["Shall I turn on the heating? It's very cold in here.", "Should I turn on the heating? It's very cold in here.", "Can I turn on the heating? It's very cold in here.", "Could I turn on the heating? It's very cold in here.", "May I turn on the heating? It's very cold in here."]]}
- reader 1: another correct answer, not accepted: ["Shall I turn the heating on? It's very cold in here.", "Do you want me to turn on the heating? It's very cold in here."]
- reader 2: another correct answer, not accepted: ["Do you want me to turn on the heating? It's very cold in here.", "Would you like me to turn on the heating? It's very cold in here."]
- reader 2: level: 'Shall I' offer is fine for A2 but is a new form for A2.1; ok

## cm-2-010 · A2.2 · text · correct-mistake-1.csv:23

Task: Correct the mistake: It's late. I walk you to the bus stop.
Key: {"kind": "text", "accepted": [["It's late. I'll walk you to the bus stop.", "It's late. I will walk you to the bus stop.", "It's late. I can walk you to the bus stop."]]}
- reader 1: another correct answer, not accepted: ["It's late. I'm going to walk you to the bus stop. (less natural for an offer)", "It's late. Let me walk you to the bus stop."]
- reader 2: another correct answer, not accepted: ["It's late. I'm going to walk you to the bus stop. (less natural for a spontaneous offer)", "It's late. Let me walk you to the bus stop."]

## cm-2-013 · B1.1 · text · correct-mistake-1.csv:27

Task: Correct the mistake. Keep *going to*: Are you going to sell your old car or you are going to keep it?
Key: {"kind": "text", "accepted": [["Are you going to sell your old car or are you going to keep it?", "Are you going to sell your old car or keep it?"]]}
- reader 1: level: Very easy for B1.1: one repeated pattern, only a missing inverted auxiliary; closer to A2.
- reader 1: sense: Learners may fix it as 'or keep it' (drops the second going to); fine if 'Keep going to' only means keep the structure, but the intended mistake ('or you are') is a weak, unusual error.
- reader 2: level: Grammar (going to + word order after 'or') is A2.2 level; easy for B1.1

