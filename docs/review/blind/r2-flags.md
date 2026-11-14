# Blind check r2: flags for the judge

5 tasks, 2 readers.

## r2-001 · B2.2 · text · built-in

Task: Start with *Max denied*: 'I didn't take your phone.'
Key: {"kind": "text", "accepted": [["Max denied taking my phone.", "Max denied taking your phone.", "Max denied that he had taken my phone.", "Max denied having taken my phone.", "Max denied that he took my phone.", "Max denied that he had taken your phone.", "Max denied taking the phone.", "Max denied that he had taken the phone.", "Max denied that he took the phone.", "Max denied having taken the phone."]]}
- reader 1: another correct answer, not accepted: ['Max denied taking her phone.', 'Max denied taking his phone.']
- reader 1: instruction: Who 'your' refers to is not said, so 'my/her/his/the phone' are all possible; the checker must accept them.
- reader 2: another correct answer, not accepted: ['Max denied he had taken my phone.', 'Max denied taking her phone.', 'Max denied taking his phone.']
- reader 2: instruction: Not clear who 'your' is (me? someone else?), so the possessive could be my / her / his / the phone; the checker must accept all, or the task should say Max was speaking to you.

## r2-002 · B2.2 · text · built-in

Task: Start with *My sister advised*: 'You really should see a doctor about that cough.'
Key: {"kind": "text", "accepted": [["My sister advised me to see a doctor about that cough.", "My sister advised seeing a doctor about that cough.", "My sister advised that I see a doctor about that cough.", "My sister advised that I should see a doctor about that cough.", "My sister advised me to see a doctor about my cough.", "My sister advised seeing a doctor about my cough.", "My sister advised that I see a doctor about my cough.", "My sister advised that I should see a doctor about my cough.", "My sister advised me to see a doctor about the cough.", "My sister advised me to go to the doctor about that cough.", "My sister advised me to go to the doctor about my cough.", "My sister advised me that I should see a doctor about that cough.", "My sister advised me that I should really see a doctor about that cough.", "My sister advised me to really see a doctor about that cough.", "My sister advised me to go and see a doctor about that cough.", "My sister advised me that I should see a doctor about my cough.", "My sister advised me that I should really see a doctor about my cough.", "My sister advised me to really see a doctor about my cough.", "My sister advised me to go and see a doctor about my cough."]]}
- reader 1: another correct answer, not accepted: ['My sister advised that I (should) see a doctor about my cough.', 'My sister advised him/her/us to see a doctor about his/her/our cough.']
- reader 1: instruction: The listener is not named, so the object (me/him/her) and possessive (my/his/her/that) are open; many variants must be accepted.
- reader 2: another correct answer, not accepted: ['My sister advised me that I really should see a doctor about my cough.', 'My sister strongly advised me to see a doctor about my cough.']
- reader 2: instruction: Addressee unclear (me vs. him/her), and nothing says whether 'really' must be kept or how 'that cough' should change; many valid answers (my/the/that cough, to-infinitive vs. that-clause vs. -ing) must all be accepted.

## r2-005 · B2.2 · text · twins-1.csv:67

Task: Start with *Leo denied*: 'It wasn't me who sent that email to the whole company.'
Key: {"kind": "text", "accepted": [["Leo denied sending that email to the whole company.", "Leo denied having sent that email to the whole company.", "Leo denied that he had sent that email to the whole company.", "Leo denied he had sent that email to the whole company.", "Leo denied that he sent that email to the whole company.", "Leo denied he sent that email to the whole company.", "Leo denied sending the email to the whole company.", "Leo denied having sent the email to the whole company."]]}
- reader 1: another correct answer, not accepted: ['Leo denied that he sent the email to the whole company.', 'Leo denied being the one who sent that email to the whole company.', 'Leo denied that it was him who had sent that email to the whole company.', 'Leo denied that it had been him who sent the email to the whole company.']
- reader 1: instruction: The cleft 'It wasn't me who...' allows many correct reports (gerund, perfect gerund, that-clause, 'being the one who'); the checker must accept them.
- reader 2: another correct answer, not accepted: ['Leo denied that he sent the email to the whole company.', 'Leo denied being the one who sent that email to the whole company.', 'Leo denied that it was him who had sent that email to the whole company.', 'Leo denied it had been him who sent the email to the whole company.']

