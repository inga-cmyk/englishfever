# Blind check c1-15: flags for the judge

4 tasks, 2 readers.

## c1-15-001 · C1 · gap · c1-agree-1.csv:12

Task: We need two more chairs: the manager and two of her assistants ___ coming to the meeting tomorrow. (be)
Key: {"kind": "gap", "accepted": [["are", "'re", "will be"]]}
- reader 1: instruction: 'We need two more chairs' and 'two of her assistants' make the plural obvious; the single (be) gap with 'coming' is too easy. 'will be' also fits (less natural than 'are' for an arrangement).
- reader 1: level: Too easy for C1: compound subject + are is A2/B1. No nuance (e.g. notional agreement) tested.
- reader 2: instruction: 'two more chairs' and a plural subject make the form obvious; nothing to decide.
- reader 2: level: Far too easy for C1: basic present continuous with a plural subject (A2).

## c1-15-002 · C1 · text · c1-order-1.csv:5

Task: Start with *So loud*: The music was so loud that we couldn't hear each other.
Key: {"kind": "text", "accepted": [["So loud was the music that we couldn't hear each other.", "So loud was the music that we could not hear each other.", "So loud was the music that we couldn't hear one another.", "So loud was the music that we could not hear one another."]]}
- reader 1: instruction: The task shows the already-correct non-inverted sentence, so the learner only has to move 'was' and 'the music' (copying/reordering); the instruction does not say what to do (invert after the fronted phrase) and it is unclear whether the shown sentence is the model or the base. Starting words give away much of the answer.
- reader 2: instruction: Original sentence is given in full; only the inversion pattern has to be recalled, but the instruction does not say inversion is wanted (a learner might write 'So loud, the music ...'). Asterisks around So loud look like stray markup.
- reader 2: sense: Natural, formal/literary register; fine.

## c1-15-003 · C1 · text · c1-part-1.csv:8

Task: Join the two sentences: make the second one an *-ing* form. The river burst its banks. It flooded the streets near the station.
Key: {"kind": "text", "accepted": [["The river burst its banks, flooding the streets near the station."]]}
- reader 1: another correct answer, not accepted: ['The river burst its banks, thereby flooding the streets near the station.', 'The river burst its banks, thus flooding the streets near the station.', 'The river burst its banks and flooded the streets near the station. (not -ing: breaks the instruction)', 'Bursting its banks, the river flooded the streets near the station. (makes the FIRST an -ing form: breaks the instruction)']
- reader 1: instruction: Pretty much dictates the structure; mostly copying with a comma. 'make the second one an -ing form' is clear but the answer is nearly given.
- reader 1: level: Participle clause of result is B2 rather than C1; a B1+ learner could solve it.
- reader 2: another correct answer, not accepted: ['The river burst its banks, thus flooding the streets near the station.', 'The river burst its banks, thereby flooding the streets near the station.', 'The river burst its banks, so flooding the streets near the station.', "Bursting its banks, the river flooded the streets near the station. (does not follow 'second one an -ing form'; first sentence becomes -ing)"]
- reader 2: instruction: '-ing form' is a grammar term; a learner may not know it means a participle clause. Clear enough otherwise.
- reader 2: level: Closer to B2 than C1; a B1/B2 learner can solve it.

## c1-15-004 · C1 · gap · c1-past-1.csv:12

Task: I'm always losing receipts. I wish I ___ them all in one folder, but I never do. (keep)
Key: {"kind": "gap", "accepted": [["kept"]]}
- reader 1: another correct answer, not accepted: [['would keep']]
- reader 1: level: wish + past simple is B1/B2; too easy for C1 (single gap, no nuance).
- reader 1: sense: 'I wish I would keep' (about oneself) is accepted by some speakers but less natural than 'kept'; otherwise sentence is natural.
- reader 2: another correct answer, not accepted: [['would keep'], ['could keep']]
- reader 2: instruction: 'wish I would keep' (own behaviour) is marginal and 'could keep' is odd with 'never do'; 'kept' is the intended one but the gap allows alternatives. 'had kept' does not fit habit.
- reader 2: level: wish + past simple is B1/B2, not C1.

