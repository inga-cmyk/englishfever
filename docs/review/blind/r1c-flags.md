# Blind check r1c: flags for the judge

8 tasks, 2 readers.

## r1c-001 · B2.1 · text · built-in

Task: Imagine it happened differently. Start with *If I*: I didn't see the sign, so I got a parking fine.
Key: {"kind": "text", "accepted": [["If I had seen the sign, I wouldn't have got a parking fine.", "If I had seen the sign, I wouldn't have gotten a parking fine.", "If I had seen the sign, I wouldn't have got a fine.", "If I had seen the sign, I wouldn't have gotten a fine.", "If I had seen the sign, I wouldn't have been fined.", "If I had noticed the sign, I wouldn't have got a parking fine.", "If I had noticed the sign, I wouldn't have got a fine."]]}
- reader 1: another correct answer, not accepted: ["If I had seen the sign, I wouldn't have gotten a parking fine. (US, common usage)", "If I had seen the sign, I wouldn't have been given a parking fine.", "If I had seen the sign, I wouldn't have had to pay a parking fine."]

## r1c-002 · B2.2 · text · built-in

Task: Report it with *advise*: My sister said to me: 'You really should see a doctor about that cough.'
Key: {"kind": "text", "accepted": [["My sister advised me to see a doctor about that cough.", "My sister advised seeing a doctor about that cough.", "My sister advised that I see a doctor about that cough.", "My sister advised that I should see a doctor about that cough.", "My sister advised me to see a doctor about my cough.", "My sister advised seeing a doctor about my cough.", "My sister advised that I see a doctor about my cough.", "My sister advised that I should see a doctor about my cough.", "My sister advised me to see a doctor about the cough.", "My sister advised me to go to the doctor about that cough.", "My sister advised me to go to the doctor about my cough."]]}
- reader 1: another correct answer, not accepted: ['My sister advised me that I should see a doctor about my cough.', 'My sister advised me to go and see a doctor about my cough.']
- reader 1: instruction: The source keeps 'that cough'; in reported speech 'my cough' is the natural shift, so the key should accept my/the/that cough.
- reader 1: level: advise + object + to-infinitive is B1/B2.1 material; a bit easy for B2.2.
- reader 2: another correct answer, not accepted: ['My sister advised me to really see a doctor about my cough.', 'My sister advised me that I should see a doctor about my cough.', 'My sister advised me that I should really see a doctor about my cough.']
- reader 2: sense: 'that cough' may be kept or changed to 'my cough', and 'really' may be dropped or kept; the checker must accept all of these.

## r1c-003 · B2.1 · text · built-in

Task: Ask politely. Start with *Could you tell me*: Why hasn't the order arrived?
Key: {"kind": "text", "accepted": [["Could you tell me why the order hasn't arrived?", "Could you please tell me why the order hasn't arrived?", "Could you tell me why the order hasn't arrived, please?", "Could you tell me why the order hasn't arrived yet?", "Could you tell me why the order has not arrived?", "Could you tell me why my order hasn't arrived?", "Could you please tell me why my order hasn't arrived?", "Could you tell me why my order hasn't arrived, please?", "Could you tell me why my order hasn't arrived yet?"]]}
- reader 1: another correct answer, not accepted: ["Could you tell me why my order hasn't arrived? (only if the learner changes the article; not strictly required)"]
- reader 2: level: Indirect questions are usually taught at B1. This is quite easy for B2.1 but acceptable as revision.

## r1c-004 · A2.2 · text · a2-rel-might-1.csv:16

Task: Join with *which*: We visited a museum. It has a collection of old cars.
Key: {"kind": "text", "accepted": [["We visited a museum which has a collection of old cars.", "We visited a museum that has a collection of old cars.", "We visited a museum which had a collection of old cars.", "We visited a museum that had a collection of old cars."]]}
- reader 1: level: Joining with a relative clause makes it a two-clause sentence, which is more B1 than A2.2.
- reader 2: another correct answer, not accepted: ['The museum which we visited has a collection of old cars.']
- reader 2: instruction: The instruction does not say which sentence should become the relative clause, so 'The museum which we visited has...' is also a valid join.

## r1c-005 · A2.2 · text · a2-rel-might-1.csv:17

Task: Join with *which*: The app helps me learn new words. It is free.
Key: {"kind": "text", "accepted": [["The app which helps me learn new words is free.", "The app that helps me learn new words is free.", "The app which is free helps me learn new words.", "The app that is free helps me learn new words.", "The app which helps me to learn new words is free.", "The app that helps me to learn new words is free.", "The app, which is free, helps me learn new words.", "The app, which helps me learn new words, is free.", "The app, which helps me to learn new words, is free.", "The app, which is free, helps me to learn new words."]]}
- reader 1: instruction: Unclear which sentence should become the relative clause; both embeddings are correct, so the key must accept both.
- reader 1: level: A relative clause embedded in the middle of the subject is hard for A2.2; the commas question (defining vs non-defining) is beyond the level.
- reader 1: sense: Without context, 'The app which helps me learn new words is free' sounds as if there are several apps; the non-defining version with commas is more natural.
- reader 2: instruction: This is ambiguous. Either sentence can become the relative clause ('The app which is free helps me learn new words' is equally correct), and the learner has no way to tell which one is expected.

## r1c-007 · A2.2 · match · a2-rel-might-1.csv:51

Task: Match each sentence with its meaning.
left: She'll call. | She might call. | She won't call. | She might not call.
right: Perhaps. | Definitely not. | Perhaps not. | Definitely.
Key: {"kind": "match", "pairs": [["She'll call.", "Definitely."], ["She might call.", "Perhaps."], ["She won't call.", "Definitely not."], ["She might not call.", "Perhaps not."]]}
- reader 1: sense: Minor: 'will' is a prediction rather than a certainty, so 'Definitely.' slightly overstates it, but it is a usual teaching simplification.
- reader 2: sense: 'She'll call' = 'Definitely' overstates it, because 'will' is a confident prediction, not a certainty. This is acceptable as an A2 simplification.

## r1c-008 · A2.2 · text · b1-new-3.csv:144

Task: Start with *I've decided*: I will go home early.
Key: {"kind": "text", "accepted": [["I decided to go home early.", "I have decided to go home early.", "I've decided to go home early.", "I've decided I'll go home early.", "I've decided that I'll go home early.", "I have decided that I will go home early.", "I have decided I will go home early.", "I decided that I would go home early.", "I decided I would go home early."]]}
- reader 1: instruction: The checker does not expand 've, so 'I have decided to go home early.' may be rejected; it is correct and should be accepted. 'I've decided I'll go home early' is also correct, so the task does not force the to-infinitive.
- reader 2: instruction: The instruction does not mention the target structure (decide + to-infinitive), so a correct 'that'-clause with 'will' cannot be ruled out. Adding 'Use to + verb' or giving a gap '(go)' would fix it.

