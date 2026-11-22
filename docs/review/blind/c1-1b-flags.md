# Blind check c1-1b: flags for the judge

12 tasks, 2 readers.

## c1-1b-001 · C1 · gap · zz-blind-zz-c1-pres-1.csv:2

Task: What are you doing with that tape measure? I ___ the kitchen for the new cupboards. (measure)
Key: {"kind": "gap", "accepted": [["am measuring", "'m measuring"]]}
- reader 1: another correct answer, not accepted: [['am going to measure'], ['will measure']]
- reader 1: level: Present continuous for an action in progress is A2/B1; not C1.

## c1-1b-002 · C1 · gap · zz-blind-zz-c1-pres-1.csv:3

Task: Our kitchen is tiny: it ___ only three metres by four. (measure)
Key: {"kind": "gap", "accepted": [["measures"]]}
- reader 1: level: State-verb contrast (measure = be in size) is a good C1 point, fine.

## c1-1b-003 · C1 · gap · zz-blind-zz-c1-pres-1.csv:4

Task: We're eating out all week because they ___ a new kitchen in our flat. (fit)
Key: {"kind": "gap", "accepted": [["are fitting", "'re fitting"]]}
- reader 1: another correct answer, not accepted: [['are going to fit'], ['will fit'], ['are having']]
- reader 1: instruction: Hint (fit) gives the verb; 'are having ... fitted' is not one gap but 'are going to fit' is possible, so the continuous-for-arrangement point is not forced.
- reader 1: level: Grammar point is B1; not C1.
- reader 2: another correct answer, not accepted: [['have fitted'], ['are putting in']]
- reader 2: sense: 'have fitted' also fits (less natural with 'all week'); 'are going to fit' is not one word-gap but also possible

## c1-1b-004 · C1 · gap · zz-blind-zz-c1-pres-1.csv:5

Task: Write one word in each gap: Why ___ you ___ so difficult about this? It's only a small change.
Key: {"kind": "gap", "accepted": [["are", "were"], ["being", "getting"]]}
- reader 1: another correct answer, not accepted: [['have', 'been'], ['do', 'be']]
- reader 1: instruction: 'Write one word in each gap' with no hint is clear, but the two gaps are the whole point (are being), very standard B1/B2 form.
- reader 1: level: 'Why are you being difficult' is B1/B2, too easy for C1.
- reader 1: sense: ['have','been'] works but changes the sense (a habit); ['do','be'] is wrong.
- reader 2: another correct answer, not accepted: [['must', 'be'], ['can', 'be']]
- reader 2: instruction: 'Write one word in each gap' does not say which verb; 'must be' / 'can be' (less natural) also work, so more than one answer.

## c1-1b-005 · C1 · gap · zz-blind-zz-c1-pres-1.csv:6

Task: It's nearly ten o'clock. I ___ the pharmacy is still open, but we can try. (doubt)
Key: {"kind": "gap", "accepted": [["doubt"]]}
- reader 1: instruction: The verb is given in brackets and no form change is needed: only copying, gives the answer away.
- reader 1: level: Too easy for C1: A2/B1 stative verb, no change of form.

## c1-1b-006 · C1 · gap · zz-blind-zz-c1-pres-1.csv:7

Task: My manager ___ taking early retirement, but she hasn't made up her mind yet. (consider)
Key: {"kind": "gap", "accepted": [["is considering", "'s considering"]]}
- reader 1: another correct answer, not accepted: [['has been considering'], ['was considering']]
- reader 1: level: 'is considering' vs 'considers' is a fair B2 point; borderline C1.
- reader 2: another correct answer, not accepted: [['has been considering']]

## c1-1b-007 · C1 · gap · zz-blind-zz-c1-pres-1.csv:8

Task: OK, I ___ you now. I'm sorry I didn't take your story seriously. (believe)
Key: {"kind": "gap", "accepted": [["believe"]]}
- reader 1: another correct answer, not accepted: [['do believe']]
- reader 1: instruction: The verb is given and no change is needed: only copying; 'now' does not force simple present over 'am believing' for a learner who has just studied the continuous.
- reader 1: level: Too easy for C1 (A2/B1 stative verb).
- reader 2: another correct answer, not accepted: [['do believe']]
- reader 2: level: Stative vs progressive contrast is well below C1 (B1/B2 point); a B1 learner solves it by instinct.

## c1-1b-008 · C1 · mcq · zz-blind-zz-c1-pres-1.csv:9

Task: Which sentence has a mistake?
options: I'm finding the new routine quite tiring. | I suggest you book a table in advance. | This dress doesn't fit me any more. | He considers taking early retirement next year.
Key: {"kind": "mcq", "correct": "He considers taking early retirement next year.", "wrong": ["I'm finding the new routine quite tiring.", "I suggest you book a table in advance.", "This dress doesn't fit me any more."]}
- reader 1: instruction: No sentence is clearly wrong: the question assumes a mistake exists.
- reader 1: sense: Option 4 is correct English (consider + -ing is fine; 'considers' for a plan is acceptable, only 'is considering' is more usual). Options 1-3 are also correct. A learner cannot tell which is meant; this is a form nobody would call a mistake.
- reader 2: sense: Option 4 is not clearly wrong: 'considers' in simple present is possible in some contexts (habitual/general), so the 'mistake' depends on reading it as a plan; ambiguous.

## c1-1b-009 · C1 · text · zz-blind-zz-c1-pres-1.csv:10

Task: Answer with *constantly* and *change your mind*: "Actually, I'll have the fish, not the pasta."
Key: {"kind": "text", "accepted": [["You're constantly changing your mind.", "You are constantly changing your mind."]]}
- reader 1: another correct answer, not accepted: [['You constantly change your mind.'], ["You're changing your mind constantly."], ["I'm constantly changing my mind."], ['I am constantly changing my mind.']]
- reader 1: instruction: Unclear who is speaking and what the answer should do ('Answer' to a statement is odd): reply to the speaker or about oneself? Neither tense is forced either; the annoyance meaning is not stated.
- reader 1: sense: The reply is natural only as a complaint; without saying so, the simple present is also correct.
- reader 2: another correct answer, not accepted: [['You constantly change your mind.'], ["You've constantly changed your mind."]]
- reader 2: instruction: Unclear who speaks and what to say: 'Answer with' does not say the answer is a comment/complaint about the speaker; tense not specified so simple present is also correct. Learner cannot know a progressive is wanted.
- reader 2: level: Fine for C1 only if the annoyed-habit nuance is clear; as worded it is guesswork.

## c1-1b-010 · C1 · gap · zz-blind-zz-c1-pres-1.csv:11

Task: Don't phone me at half past eight: I ___ usually ___ to work then. (drive)
Key: {"kind": "gap", "accepted": [["am", "'m"], ["driving"]]}
- reader 1: another correct answer, not accepted: [['do', 'drive']]
- reader 1: level: 'I'm usually driving' (continuous with usually, for a regular activity at a given time) is a good C1 point.
- reader 1: sense: ['do','drive'] is grammatical but emphatic and odd here; less natural.
- reader 2: another correct answer, not accepted: [['will', 'be driving']]
- reader 2: instruction: 'will usually be driving' is also correct (two words in the second gap).

## c1-1b-011 · C1 · mcq · zz-blind-zz-c1-pres-1.csv:12

Task: Which sentence has a mistake?
options: She constantly checks her phone in meetings. | My neighbour forever is borrowing my tools. | At eight I'm usually driving to work. | He's always offering to help with the shopping.
Key: {"kind": "mcq", "correct": "My neighbour forever is borrowing my tools.", "wrong": ["He's always offering to help with the shopping.", "At eight I'm usually driving to work.", "She constantly checks her phone in meetings."]}
- reader 1: sense: The wrong order (forever is borrowing) is a believable learner slip, but options 1, 3 and 4 are all correct, which is fine.
- reader 2: sense: Word-order error 'forever is borrowing' is a form few learners would write at C1; the wrong sentence is easy to spot.

## c1-1b-012 · C1 · order · zz-blind-zz-c1-pres-1.csv:13

Task: Put the words in order.
word_cards: constantly | you're | I'm | interrupting | speaking | when | me
Key: {"kind": "order", "sentence": "you're constantly interrupting me when I'm speaking", "also": ["when I'm speaking you're constantly interrupting me"]}
- reader 1: another correct answer, not accepted: ["you're interrupting me constantly when I'm speaking", "when I'm speaking you're interrupting me constantly", "I'm speaking when you're constantly interrupting me"]
- reader 1: instruction: Several orders are correct (adverb after you're or after me, when-clause first or last).
- reader 1: level: Fine for C1 content, but the task is only word order, with cards giving contractions: fairly easy for C1.
- reader 2: another correct answer, not accepted: ["you're interrupting me constantly when I'm speaking", "constantly you're interrupting me when I'm speaking"]
- reader 2: instruction: Task is just ordering seven given words; the meaning is already in the cards and the 'when' clause order is open, so several orders are correct. No hint which clause starts.
- reader 2: level: Too easy for C1: only word order, no choice of form.

