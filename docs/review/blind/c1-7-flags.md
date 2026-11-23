# Blind check c1-7: flags for the judge

20 tasks, 2 readers.

## c1-7-001 · C1 · mcq · c1-can-1.csv:6

Task: Choose the correct option: The next bus is in an hour, so we ___ walk.
options: might as good | might so well | might well as | might as well
Key: {"kind": "mcq", "correct": "might as well", "wrong": ["might as good", "might so well", "might well as"]}
- reader 2: level: 'might as well' is B1/B2, a bit low for C1

## c1-7-002 · C1 · gap · c1-order-1.csv:2

Task: Write one word in each gap: Rarely ___ I ___ such a beautiful sunset. (have / see)
Key: {"kind": "gap", "accepted": [["have"], ["seen"]]}
- reader 1: another correct answer, not accepted: [['did', 'see']]
- reader 1: instruction: (have / see) allows 'did I see' too (correct, slightly less common than 'have I seen'); fix by giving the form or context.
- reader 2: instruction: Verbs given (have / see) reveal the form; 'Rarely' + inversion is the target, ok

## c1-7-004 · C1 · gap · c1-order-1.csv:4

Task: Write one word in each gap: Not until the guests had gone ___ we ___ the stain on the carpet. (notice)
Key: {"kind": "gap", "accepted": [["did"], ["notice"]]}
- reader 2: instruction: Verb given, only the form is tested

## c1-7-005 · C1 · gap · c1-order-1.csv:5

Task: So loud ___ the music that we couldn't hear each other.
Key: {"kind": "gap", "accepted": [["was"]]}
- reader 1: another correct answer, not accepted: [['had been']]
- reader 1: instruction: No verb given: 'had been' also fits (less natural). No 'one word' hint on the instruction line.

## c1-7-006 · C1 · text · c1-order-1.csv:6

Task: Start with *Had*: If I had known about the traffic, I would have left earlier.
Key: {"kind": "text", "accepted": [["Had I known about the traffic, I would have left earlier.", "Had I known about the traffic, I'd have left earlier."]]}
- reader 2: instruction: Start word given, so the structure is named; pure transformation, mechanical

## c1-7-007 · C1 · text · c1-order-1.csv:7

Task: Start with *Should*: If you need any help, please call reception.
Key: {"kind": "text", "accepted": [["Should you need any help, please call reception."]]}
- reader 1: another correct answer, not accepted: ['Should you need any help, call reception.']
- reader 1: instruction: Learner may drop 'please' or change words; fine. Slightly easy if 'Should' is the only change.
- reader 2: another correct answer, not accepted: ['Should you require any help, please call reception.']
- reader 2: instruction: Start word given, so structure is named; 'require' is a changed word, not needed

## c1-7-008 · C1 · gap · c1-order-1.csv:8

Task: Here ___ the bus! Quick, get your bag. (come)
Key: {"kind": "gap", "accepted": [["comes"]]}
- reader 1: instruction: Very easy and a fixed A2 pattern; the (come) hint plus 'Here' gives it away.
- reader 1: level: Too easy for C1 (A2/B1 level).
- reader 2: level: 'Here comes' is A2 vocabulary, a fixed phrase; not C1
- reader 2: sense: Fixed phrase, not really inversion nuance

## c1-7-009 · C1 · text · c1-order-1.csv:9

Task: Start with *What*: I need a long holiday.
Key: {"kind": "text", "accepted": [["What I need is a long holiday."]]}
- reader 1: another correct answer, not accepted: ['What I need is to have a long holiday', "What I need's a long holiday."]
- reader 1: instruction: Instruction only says 'Start with What': many acceptable sentences (holiday/break, to have); unclear what is wanted. American 'vacation' also correct.
- reader 2: instruction: Ambiguous: 'What a long holiday I need!' also starts with What; instruction does not say it should keep the meaning or be a cleft sentence

## c1-7-010 · C1 · gap · c1-order-1.csv:10

Task: Cold ___ it was, we went for a swim in the lake.
Key: {"kind": "gap", "accepted": [["though", "as"]]}
- reader 1: instruction: 'Cold though it was' is equally correct (and common); only 'although' is wrong.
- reader 2: instruction: No hint that the structure is 'Adjective + as/though + clause'; 'though' is also correct (Cold though it was)

## c1-7-012 · C1 · gap · c1-part-1.csv:3

Task: ___ finished the report, she went home early. (have)
Key: {"kind": "gap", "accepted": [["Having"]]}
- reader 1: instruction: The hint (have) nearly gives the form away.

## c1-7-014 · C1 · gap · c1-part-1.csv:5

Task: ___ in a cool, dry place, the seeds will keep for years. (store)
Key: {"kind": "gap", "accepted": [["Stored", "If stored", "When stored"]]}
- reader 2: level: Form is simple past participle; fairly easy for C1

## c1-7-015 · C1 · gap · c1-part-1.csv:6

Task: ___ prices going up every month, many families are struggling.
Key: {"kind": "gap", "accepted": [["With"]]}
- reader 1: another correct answer, not accepted: [['Given']]
- reader 1: instruction: No hint word: 'Given prices going up' is marginally possible but less natural; 'With' is the intended one. Open-ended, hard to guess the target.
- reader 1: sense: Meaning of 'With + noun + -ing' is hard to infer without a hint.
- reader 2: another correct answer, not accepted: [['Given']]
- reader 2: instruction: No verb given; 'Given' is marginal/odd with a bare plural noun; 'What with' is two words

## c1-7-017 · C1 · gap · c1-part-1.csv:8

Task: The river burst its banks, ___ the streets near the station. (flood)
Key: {"kind": "gap", "accepted": [["flooding"]]}
- reader 2: level: B2 rather than C1

## c1-7-018 · C1 · mcq · c1-part-1.csv:9

Task: Choose the correct option: ___ hearing the news, she burst into tears.
options: At | In | On | By
Key: {"kind": "mcq", "correct": "On", "wrong": ["In", "By", "At"]}
- reader 2: a wrong option that fits: 'At' is grammatical but rare/dated ('at hearing'); 'Upon' not offered
- reader 2: level: Fixed phrase 'on + -ing', B2-ish

## c1-7-019 · C1 · gap · c1-part-1.csv:10

Task: Keep the jar in the fridge once ___. (open)
Key: {"kind": "gap", "accepted": [["opened"]]}
- reader 2: another correct answer, not accepted: [['open']]
- reader 2: instruction: 'once open' is also correct (common on labels), although given verb suggests 'opened'
- reader 2: level: B2 level

## c1-7-020 · C1 · gap · c1-part-1.csv:11

Task: ___ by the queue outside, the new café is very popular. (judge)
Key: {"kind": "gap", "accepted": [["Judging"]]}
- reader 1: another correct answer, not accepted: [['Judged']]
- reader 1: instruction: 'Judged by the queue' is also correct English (less idiomatic than 'Judging by').
- reader 2: another correct answer, not accepted: [['Judged']]
- reader 2: sense: 'Judged by' is passive, less natural but grammatical

