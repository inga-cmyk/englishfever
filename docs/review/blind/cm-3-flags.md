# Blind check cm-3: flags for the judge

4 tasks, 2 readers.

## cm-3-001 · B1.1 · text · correct-mistake-1.csv:17

Task: Correct the mistake. Keep *yesterday*: I have seen this film yesterday, so let's watch something else tonight.
Key: {"kind": "text", "accepted": [["I saw this film yesterday, so let's watch something else tonight.", "I watched this film yesterday, so let's watch something else tonight."]]}
- reader 1: another correct answer, not accepted: ['I saw this film yesterday, so let us watch something else tonight.', 'I watched this film yesterday, so let us watch something else tonight.']
- reader 2: another correct answer, not accepted: ['I saw this film yesterday, so let us watch something else tonight.', 'I watched this film yesterday, so let us watch something else tonight.']

## cm-3-002 · A2.1 · text · correct-mistake-1.csv:22

Task: Correct the mistake: Will I turn on the heating? It's very cold in here.
Key: {"kind": "text", "accepted": [["Shall I turn on the heating? It's very cold in here.", "Should I turn on the heating? It's very cold in here.", "Can I turn on the heating? It's very cold in here.", "Could I turn on the heating? It's very cold in here.", "May I turn on the heating? It's very cold in here.", "Shall I turn the heating on? It's very cold in here.", "Should I turn the heating on? It's very cold in here.", "Can I turn the heating on? It's very cold in here.", "Could I turn the heating on? It's very cold in here.", "May I turn the heating on? It's very cold in here."]]}
- reader 1: another correct answer, not accepted: ["Do you want me to turn on the heating? It's very cold in here.", "Do you want me to turn the heating on? It's very cold in here."]
- reader 2: another correct answer, not accepted: ["Do you want me to turn on the heating? It's very cold in here.", "Do you want me to turn the heating on? It's very cold in here.", "Shall I put the heating on? It's very cold in here."]
- reader 2: level: 'Shall I' offers may be above A2.1 for many learners; many would not know 'shall' and would only guess 'Do you want me to...' or 'Can I...'.

## cm-3-003 · A2.2 · text · correct-mistake-1.csv:23

Task: Correct the mistake: It's late. I walk you to the bus stop.
Key: {"kind": "text", "accepted": [["It's late. I'll walk you to the bus stop.", "It's late. I will walk you to the bus stop.", "It's late. I can walk you to the bus stop.", "It's late. Let me walk you to the bus stop."]]}
- reader 1: another correct answer, not accepted: ["It's late. Shall I walk you to the bus stop?", "It's late. I'm going to walk you to the bus stop.", "It's late. Should I walk you to the bus stop?"]
- reader 1: instruction: No clear single target: the mistake could be fixed as a spontaneous offer (I'll), a question (Shall I...?) or a plan (I'm going to); many valid answers.
- reader 2: another correct answer, not accepted: ["It's late. I'm going to walk you to the bus stop.", "It's late. Shall I walk you to the bus stop?", "It's late, so I'll walk you to the bus stop."]
- reader 2: instruction: Does not say what to keep, so rewrites like 'Let me walk you' / 'Shall I walk you...?' are open; 'I'm going to' is correct but less natural for a spontaneous offer.

## cm-3-004 · B1.1 · text · correct-mistake-1.csv:27

Task: Correct the mistake: I can't go out until the plumber will come, so could you buy some bread?
Key: {"kind": "text", "accepted": [["I can't go out until the plumber comes, so could you buy some bread?", "I can't go out until the plumber has come, so could you buy some bread?"]]}
- reader 1: another correct answer, not accepted: ["I can't go out until the plumber arrives, so could you buy some bread?", "I can't go out until the plumber has arrived, so could you buy some bread?", "I can't go out until the plumber gets here, so could you buy some bread?"]
- reader 2: another correct answer, not accepted: ["I can't go out until the plumber arrives, so could you buy some bread?", "I can't go out until the plumber has arrived, so could you buy some bread?", "I can't go out until the plumber gets here, so could you buy some bread?", "I can't go out until the plumber's come, so could you buy some bread?"]

