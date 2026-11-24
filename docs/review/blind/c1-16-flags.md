# Blind check c1-16: flags for the judge

13 tasks, 2 readers.

## c1-16-001 · C1 · gap · c1-agree-1.csv:2

Task: The number of applicants ___ fallen sharply this year. (have)
Key: {"kind": "gap", "accepted": [["has", "'s"]]}
- reader 1: level: The number of... + has is B2 at most; fine for C1 only if the point is the contrast with 'A number of' (see 002).

## c1-16-002 · C1 · gap · c1-agree-1.csv:3

Task: A number of applicants ___ already withdrawn, so there are still places left. (have)
Key: {"kind": "gap", "accepted": [["have", "'ve"]]}
- reader 1: level: A number of + plural verb is B2, borderline C1.

## c1-16-003 · C1 · gap · c1-agree-1.csv:5

Task: Politics ___ never interested me much, but this election is different. (have)
Key: {"kind": "gap", "accepted": [["has", "'s"]]}
- reader 1: instruction: '(have)' tells which verb; fine, but gives away the verb so only has/have is tested.
- reader 1: level: Politics + singular verb is B1-B2, not really C1.
- reader 1: sense: Fine.
- reader 2: another correct answer, not accepted: [['have']]
- reader 2: sense: 'Politics have' is rare/non-standard; mostly fine. Ambiguity only if learner treats politics as plural.

## c1-16-004 · C1 · gap · c1-agree-1.csv:6

Task: The criteria for the award ___ changed this year, so please read them again. (have)
Key: {"kind": "gap", "accepted": [["have", "'ve"]]}
- reader 1: level: Plural 'criteria' is a good C1 point, though a B2 learner could solve it.

## c1-16-005 · C1 · gap · c1-agree-1.csv:12

Task: Write one word in the gap: We need two more chairs, because the manager and two of her assistants ___ coming to the meeting tomorrow.
Key: {"kind": "gap", "accepted": [["are"]]}
- reader 1: instruction: 'Write one word' is fine. Does not need 'tomorrow' for a tense choice but it is harmless; 'will be' is two words so blocked. 'are' vs 'is' is the only issue.
- reader 1: level: Subject-verb agreement with 'and' is A2-B1; too easy for C1.
- reader 1: sense: The two-chairs context is natural.
- reader 2: instruction: Fine; 'will be' would be two words, so excluded by 'one word'.

## c1-16-006 · C1 · mcq · c1-can-1.csv:2

Task: Which sentence has a mistake?
options: I could hear the neighbours arguing all night. | We couldn't find a parking space anywhere. | After three tries, she managed to open the jar. | Despite the traffic, we could catch the last bus.
Key: {"kind": "mcq", "correct": "Despite the traffic, we could catch the last bus.", "wrong": ["I could hear the neighbours arguing all night.", "We couldn't find a parking space anywhere.", "After three tries, she managed to open the jar."]}
- reader 1: sense: Believable mistake (could for one specific past success; should be managed to / were able to). Note 'couldn't find' in option 2 is correct because negatives are allowed.

## c1-16-007 · C1 · gap · c1-part-1.csv:12

Task: ___ with the other candidates, she was clearly the strongest. (compare)
Key: {"kind": "gap", "accepted": [["Compared"]]}
- reader 1: another correct answer, not accepted: [['When compared'], ['Once compared']]
- reader 1: instruction: Gap before 'with' invites 'Compared'; the verb in brackets is not enough to tell it is a participle clause, but it is not wrong.
- reader 1: level: Participle clause, fine for B2-C1.
- reader 2: instruction: Fairly easy for C1 (participle clause is B2); verb is given in base form so only -ed needed.
- reader 2: level: B2 rather than C1.

## c1-16-008 · C1 · gap · c1-past-1.csv:5

Task: Show that the shouting went on for a long time: His voice was hoarse because he ___ all afternoon at the match. (shout)
Key: {"kind": "gap", "accepted": [["had been shouting", "'d been shouting"]]}
- reader 1: another correct answer, not accepted: [['had shouted']]
- reader 1: instruction: The first sentence gives away the form (long duration = continuous). Also the instruction does not say it is the past perfect continuous. 'Show that...' is slightly odd instruction wording.
- reader 1: level: Past perfect continuous is B2, not C1.
- reader 1: sense: 'had shouted' is possible but less good for duration.
- reader 2: another correct answer, not accepted: [['had shouted'], ['was shouting']]
- reader 2: instruction: Gives the answer away: 'went on for a long time' names the continuous form. 'had shouted' is also correct English (less natural/less emphatic); 'was shouting' fits less well.
- reader 2: level: Past perfect continuous is B2, not C1.

## c1-16-009 · C1 · text · c1-perf-1.csv:14

Task: Report what she said with *deny* and *having*. Her words: 'I didn't read the letter.'
Key: {"kind": "text", "accepted": [["She denied having read the letter.", "She denied having read it."]]}
- reader 1: another correct answer, not accepted: [['She denied ever having read the letter.']]
- reader 1: instruction: Gives away the answer: 'deny' and 'having' are named, leaving only copying. 'She' is not defined (the sentence says 'Her words' but no name).
- reader 1: level: Good C1 structure, but the instruction does the work.
- reader 2: another correct answer, not accepted: [['She denies having read the letter.'], ['She has denied having read the letter.'], ['She denied ever having read the letter.'], ['She denied not having read the letter.']]
- reader 2: instruction: 'Report what she said' with the structure named (deny + having) gives the form away; 'having' may be unclear. The speaker is just 'she' with no context for sense. 'denied not having read' is wrong (double negative), listed only as a possible learner answer.
- reader 2: sense: 'Her words' are 'I didn't read the letter' (simple past) - fine, but 'having read' also covers 'had read'; OK.

## c1-16-010 · C1 · mcq · c1-prep-1.csv:7

Task: Choose the correct option: She took a bookkeeping course ___ her own business.
options: in view to starting | with a view to starting | with a view of starting | with a view to start
Key: {"kind": "mcq", "correct": "with a view to starting", "wrong": ["with a view to start", "with a view of starting", "in view to starting"]}
- reader 1: level: Fixed phrase, fine for C1.
- reader 1: sense: Wrong options 'in view to', 'with a view of', 'with a view to start' are believable.

## c1-16-011 · C1 · mcq · c1-pres-2.csv:3

Task: In this story, which verb gives the background, not an event that moves the story on? So I'm sitting on the train, this man opens a bag of crisps, and the whole carriage turns round.
options: 'm sitting | opens | turns round | all three
Key: {"kind": "mcq", "correct": "'m sitting", "wrong": ["opens", "turns round", "all three"]}
- reader 1: instruction: Question is long and a bit awkward ('gives the background, not an event that moves the story on'); uses undefined grammar idea. 'all three' is an odd option.
- reader 1: level: Narrative present with background continuous is C1-ish but the task is more about reading than grammar; B1-B2 learners could solve it.
- reader 1: sense: Model sentence is natural spoken anecdote.
- reader 2: instruction: 'verb gives the background' is a bit unclear; 'all three' is a trivially wrong distractor. 'turns round' is not clearly an event vs. reaction.
- reader 2: level: B2 rather than C1 (present narrative); fairly easy.
- reader 2: sense: 'all three' is not a believable option.

## c1-16-012 · C1 · text · c1-subj-1.csv:10

Task: Report the lawyer's words with *demanded that*. Her words: 'My client must be told the whole truth.'
Key: {"kind": "text", "accepted": [["The lawyer demanded that her client be told the whole truth.", "The lawyer demanded that her client should be told the whole truth.", "She demanded that her client be told the whole truth.", "She demanded that her client should be told the whole truth."]]}
- reader 1: another correct answer, not accepted: [['She demanded that her client was told the whole truth.'], ['She demanded that her client is told the whole truth.']]
- reader 1: instruction: 'demanded that' is given; only the subjunctive form is left to produce, but that is the point. The speaker is 'the lawyer' and 'Her words': 'she' is clear.
- reader 1: level: Good C1 point.
- reader 1: sense: 'was told' / 'is told' are not formal but acceptable in less formal use; list them.
- reader 2: another correct answer, not accepted: [['The lawyer demanded that her client was told the whole truth.'], ['The lawyer demanded that her client is told the whole truth.']]
- reader 2: instruction: 'be told' (subjunctive) is American/formal; British 'should be told' also correct; 'was told' informal. Task does not state which is wanted; 'demanded that' given in the instruction gives the structure away.
- reader 2: sense: Her words are quoted but the lawyer is 'her' in both instruction and speech: 'my client' -> 'her client' vs 'their/his client' is ambiguous.

## c1-16-013 · C1 · mcq · c1-will-1.csv:3

Task: Which sentence has a mistake?
options: Whenever we visited my uncle, we would play in his garden. | Years ago, the factory would be where the car park is now. | We visited Switzerland four times in the nineties. | Didn't you use to have red hair?
Key: {"kind": "mcq", "correct": "Years ago, the factory would be where the car park is now.", "wrong": ["Whenever we visited my uncle, we would play in his garden.", "Didn't you use to have red hair?", "We visited Switzerland four times in the nineties."]}
- reader 1: sense: Believable mistake (would for a state). Option 4 'Didn't you use to' is correct (also 'Didn't you used to' is common but non-standard).

