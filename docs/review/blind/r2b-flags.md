# Blind check r2b: flags for the judge

2 tasks, 2 readers.

## r2b-001 · B2.2 · text · built-in

Task: Max said to you: 'I didn't take your phone.' Start with *Max denied*.
Key: {"kind": "text", "accepted": [["Max denied taking my phone.", "Max denied taking your phone.", "Max denied that he had taken my phone.", "Max denied having taken my phone.", "Max denied that he took my phone.", "Max denied that he had taken your phone.", "Max denied taking the phone.", "Max denied that he had taken the phone.", "Max denied that he took the phone.", "Max denied having taken the phone.", "Max denied he had taken my phone.", "Max denied he took my phone."]]}
- reader 2: instruction: Many correct forms are possible (gerund, perfect gerund, that-clause with past or past perfect), so the checker must accept all of them. The prompt does not say which pattern is being practised. 'your phone' must become 'my phone'. Learners who keep 'your' will be marked wrong, but that shift is a reasonable thing to test.

## r2b-002 · B2.2 · text · built-in

Task: My sister said to me: 'You really should see a doctor about that cough.' Start with *My sister advised*.
Key: {"kind": "text", "accepted": [["My sister advised me to see a doctor about that cough.", "My sister advised seeing a doctor about that cough.", "My sister advised that I see a doctor about that cough.", "My sister advised that I should see a doctor about that cough.", "My sister advised me to see a doctor about my cough.", "My sister advised seeing a doctor about my cough.", "My sister advised that I see a doctor about my cough.", "My sister advised that I should see a doctor about my cough.", "My sister advised me to see a doctor about the cough.", "My sister advised me to go to the doctor about that cough.", "My sister advised me to go to the doctor about my cough.", "My sister advised me that I should see a doctor about that cough.", "My sister advised me that I should really see a doctor about that cough.", "My sister advised me to really see a doctor about that cough.", "My sister advised me to go and see a doctor about that cough.", "My sister advised me that I should see a doctor about my cough.", "My sister advised me that I should really see a doctor about my cough.", "My sister advised me to really see a doctor about my cough.", "My sister advised me to go and see a doctor about my cough.", "My sister strongly advised me to see a doctor about that cough.", "My sister advised me that I really should see a doctor about that cough.", "My sister strongly advised me to see a doctor about my cough.", "My sister advised me that I really should see a doctor about my cough.", "My sister strongly advised me to see a doctor about the cough.", "My sister advised me that I should see a doctor about the cough.", "My sister advised me that I really should see a doctor about the cough."]]}
- reader 1: another correct answer, not accepted: ['My sister advised me I should see a doctor about my cough.']
- reader 2: another correct answer, not accepted: ['My sister advised that I (should) see a doctor about my cough.']
- reader 2: instruction: The prompt does not say what to do with 'that cough' (my / the / that). All three are acceptable and the checker must accept each one. It also does not say whether 'really' should stay ('strongly advised' or 'really advised' would capture it). With the given start, 'advised me to' is the obvious pattern, but 'advised that I should' and 'advised seeing' are also correct and must be accepted.
- reader 2: level: Fairly easy for B2.2 (advise + object + to-infinitive is B1).

