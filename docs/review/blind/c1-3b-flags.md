# Blind check c1-3b: flags for the judge

3 tasks, 2 readers.

## c1-3b-001 · C1 · mcq · c1-past-1.csv:9

Task: Which sentence has a mistake?
options: I was meaning to call you, but the week got away from me. | I had hoped to finish the report by Friday. | They were planning to move, but they changed their minds. | We have hoped the weather would hold, but it rained all weekend.
Key: {"kind": "mcq", "correct": "We have hoped the weather would hold, but it rained all weekend.", "wrong": ["I was meaning to call you, but the week got away from me.", "I had hoped to finish the report by Friday.", "They were planning to move, but they changed their minds."]}
- reader 1: level: Sentences are short and the point (was meaning to / had hoped / were planning to for unfulfilled plans) is B2 at most; a B1-B2 learner can solve it. Not clearly C1.
- reader 1: sense: The wrong sentence is believable-ish, but 'have hoped' + 'would hold' is an obvious tense clash, so it is easy to spot.
- reader 2: level: Tense mismatch (have hoped + would) is a B1 error; the good options are B2 at most, so C1 is not really tested (no nuance of use).
- reader 2: sense: Option 4 is a believable slip but rather easy to spot; option 1 (get away from me) is idiomatic, fine.

## c1-3b-002 · C1 · mcq · c1-past-1.csv:10

Task: Choose the correct option: When we shared a flat, Tom ___ my phone charger without asking.
options: has always borrowed | was always borrowing | was always borrow | always was borrowing
Key: {"kind": "mcq", "correct": "was always borrowing", "wrong": ["always was borrowing", "was always borrow", "has always borrowed"]}
- reader 1: level: Past continuous with 'always' for annoying habit is B1-B2; distractors are easy (was always borrow is not a believable mistake). Weak for C1.
- reader 1: sense: 'was always borrow' is a form no learner at this level writes (random string). 'always was borrowing' is an odd word order, not a real error type.
- reader 2: instruction: Fine, but the annoyance meaning is only implied; clear enough. "has always borrowed" is ruled out only by "When we shared a flat" (past, finished).
- reader 2: level: Past continuous with always for annoying habit is B2 rather than C1; a B2 learner can solve it.
- reader 2: sense: "was always borrow" is a form nobody writes (bare verb after was); "always was borrowing" is a weak distractor (word order, not a real learner error).

## c1-3b-003 · C1 · gap · c1-past-1.csv:11

Task: I went back to my old school last summer and found that it ___ much. (not / change)
Key: {"kind": "gap", "accepted": [["hadn't changed", "had not changed"]]}
- reader 1: another correct answer, not accepted: [["hasn't changed"], ['has not changed']]
- reader 1: instruction: '(not / change)' names the verb and negative, leaving only the tense to choose; fine, but the contraction/full form ambiguity must be accepted. Typed answer count: 'much' is outside the gap, ok.
- reader 1: level: Past perfect after 'found that' is B1-B2; not C1 in use or nuance.
- reader 1: sense: 'hasn't changed much' is also acceptable (present-relevant reported state, esp. informal/American), so 'hadn't' is not the only correct answer; 'didn't change much' is wrong here (means something different).
- reader 2: another correct answer, not accepted: [['has not changed'], ["hasn't changed"]]
- reader 2: instruction: (not / change) names the verb and negative, so only the tense is tested; "found that" + past makes past perfect the clear target. Typed answer needs contraction/full form both accepted. Present perfect (hasn't changed) is less natural but possible if the school is still the same now.
- reader 2: level: Past perfect after found that is B1/B2; not C1 (no nuance).
- reader 2: sense: "didn't change much" is also something learners write; here it is arguably wrong (needs earlier-than-found), fine.

