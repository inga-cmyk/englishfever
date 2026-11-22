# Blind check r20-3: flags for the judge

60 tasks, 2 readers.

## r20-3-001 · B2.2 · gap · compare-past-1.csv:56

Task: It ___ when we went out. The sun was shining. (not / rain)
Key: {"kind": "gap", "accepted": [["wasn't raining", "was not raining", "hadn't been raining", "had not been raining"]]}
- reader 1: another correct answer, not accepted: [["didn't rain"], ['did not rain']]
- reader 1: instruction: Tense not fixed by the instruction: 'didn't rain' is also correct (less natural with the sun shining).
- reader 2: another correct answer, not accepted: [["didn't rain"]]
- reader 2: instruction: Tense is not signalled: 'hadn't been raining' and 'didn't rain' also work (less natural with the sun shining). Learner cannot tell which contrast is wanted.
- reader 2: level: Simple past continuous is far too easy for B2.2.

## r20-3-002 · B2.1 · gap · compare-past-1.csv:58

Task: When I first met her, she ___ in Madrid very long, but she already knew the city well. (not / live)
Key: {"kind": "gap", "accepted": [["hadn't been living", "had not been living", "hadn't lived", "had not lived"]]}
- reader 1: instruction: Perfect simple and continuous both correct.
- reader 2: instruction: 'hadn't lived' is equally correct; task cannot distinguish them.

## r20-3-003 · B2.1 · order · compare-past-1.csv:60

Task: Put the words in order.
word_cards: when | down | broke | for | the | car | hours | driving | we | been | had
Key: {"kind": "order", "sentence": "we had been driving for hours when the car broke down", "also": ["when the car broke down we had been driving for hours"]}
- reader 1: another correct answer, not accepted: ['when we had been driving for hours the car broke down', 'the car broke down when we had been driving for hours']
- reader 1: instruction: Several orders work; the learner is not told.
- reader 2: another correct answer, not accepted: ['the car broke down when we had been driving for hours', 'when we had been driving for hours the car broke down']
- reader 2: instruction: 'when' card shows clause order is free; several orders accepted.

## r20-3-004 · B2.2 · order · compare-past-1.csv:61

Task: Put all the words in order. More than one answer is possible.
word_cards: been | years | ten | had | when | there | working | left | for | she | she
Key: {"kind": "order", "sentence": "she had been working there for ten years when she left", "also": ["when she left she had been working there for ten years"]}
- reader 1: another correct answer, not accepted: ['she left when she had been working there for ten years', 'she had been working for ten years there when she left (less natural)', 'when she had been working there for ten years she left']
- reader 2: another correct answer, not accepted: ['she left when she had been working there for ten years', 'when she had been working there for ten years she left', 'she had been working for ten years there when she left (less natural)']

## r20-3-008 · B2.1 · text · conjunctions-1.csv:81

Task: Correct the mistake: Despite of the rain, the match went ahead.
Key: {"kind": "text", "accepted": [["Despite the rain, the match went ahead.", "In spite of the rain, the match went ahead."]]}
- reader 1: instruction: Two fixes possible (delete 'of' or use 'in spite of').
- reader 2: instruction: Instruction does not say whether to keep 'despite' or may change to 'in spite of'.

## r20-3-011 · B2.1 · mcq · conjunctions-1.csv:90

Task: Choose the correct option: This app is used ___ tracking your spending.
options: for | to | so that
Key: {"kind": "mcq", "correct": "for", "wrong": ["to", "so that"]}
- reader 2: a wrong option that fits: 'to': 'used to tracking' is grammatical (be used to + -ing) though odd in meaning.
- reader 2: sense: 'to' fits formally as 'be used to tracking', a real trap but the sentence then means something silly.

## r20-3-012 · B2.2 · mcq · conjunctions-1.csv:91

Task: Choose the correct option: The project was over budget. The board has ___ decided to cancel it.
options: in case | as a result of | therefore
Key: {"kind": "mcq", "correct": "therefore", "wrong": ["as a result of", "in case"]}
- reader 1: sense: 'as a result of' would not fit; fine.

## r20-3-016 · B2.1 · mcq · conjunctions-1.csv:95

Task: Which sentence is NOT correct?
options: Take a map in case your phone dies. | The shop closed early owing the strike. | Rent is high here. For this reason, we moved. | She stayed at home because she felt ill.
Key: {"kind": "mcq", "correct": "The shop closed early owing the strike.", "wrong": ["She stayed at home because she felt ill.", "Rent is high here. For this reason, we moved.", "Take a map in case your phone dies."]}
- reader 2: sense: Fine; 'owing the' is a believable slip.

## r20-3-017 · B2.2 · mcq · conjunctions-1.csv:96

Task: Which sentence is correct?
options: He studied hard; nevertheless he, failed the test. | He studied hard nevertheless, he failed the test. | He studied hard; nevertheless, he failed the test.
Key: {"kind": "mcq", "correct": "He studied hard; nevertheless, he failed the test.", "wrong": ["He studied hard nevertheless, he failed the test.", "He studied hard; nevertheless he, failed the test."]}
- reader 1: sense: Option 1 ('nevertheless he, failed') is a comma slip nobody writes; option 2 is believable.
- reader 2: sense: Option 1 (comma after 'he') is a form nobody writes; option 2 is a believable comma splice mistake.

## r20-3-025 · B2.1 · text · conjunctions-1.csv:105

Task: Correct the mistake: Take an umbrella in case it will rain.
Key: {"kind": "text", "accepted": [["Take an umbrella in case it rains."]]}
- reader 1: another correct answer, not accepted: ['Take an umbrella if it rains. (meaning changes, but correct)']
- reader 1: instruction: Alternative with 'if' is correct English.
- reader 2: another correct answer, not accepted: [['Take an umbrella in case it should rain.'], ['Take an umbrella in case it rained.']]
- reader 2: instruction: Does not say what is wrong; 'in case it should rain' is also correct.

## r20-3-026 · B2.1 · text · conjunctions-1.csv:106

Task: Correct the mistake: This tool is for cut metal.
Key: {"kind": "text", "accepted": [["This tool is for cutting metal.", "This tool is used for cutting metal."]]}
- reader 1: another correct answer, not accepted: ['This tool is used to cut metal.', 'This tool is to cut metal. (less natural)']
- reader 1: instruction: Several correct fixes.
- reader 2: instruction: Rewrite also possible as 'This tool is for cutting metals' / added 'used'; fine but open.

## r20-3-027 · B2.2 · text · conjunctions-1.csv:107

Task: Rewrite with *owing to*: The flight was late because the weather was bad.
Key: {"kind": "text", "accepted": [["The flight was late owing to the bad weather.", "The flight was late owing to bad weather.", "Owing to the bad weather, the flight was late.", "Owing to bad weather, the flight was late."]]}
- reader 1: another correct answer, not accepted: ['Owing to the weather being bad, the flight was late.', 'The flight was late owing to the fact that the weather was bad.']
- reader 1: instruction: Many correct answers; tell the learner what to keep.
- reader 2: another correct answer, not accepted: ['Owing to the weather being bad, the flight was late.', 'The flight was late owing to the fact that the weather was bad.']
- reader 2: instruction: Very open: many valid rewrites; 'owing to the fact that' also correct.

## r20-3-028 · B2.1 · order · conjunctions-1.csv:110

Task: Put the words in order.
word_cards: hurt | legs | though | kept | her | running | even | she
Key: {"kind": "order", "sentence": "she kept running even though her legs hurt", "also": ["even though her legs hurt she kept running"]}
- reader 1: another correct answer, not accepted: ['her legs hurt even though she kept running (odd logic)']
- reader 1: instruction: Two main orders.
- reader 2: level: Easy for B2.1 (B1 structure).

## r20-3-029 · B2.2 · order · conjunctions-1.csv:111

Task: Put the words in order.
word_cards: for | order | more | need | the | on | in | sundays | we | staff | shop | open | to
Key: {"kind": "order", "sentence": "we need more staff in order for the shop to open on sundays", "also": ["in order for the shop to open on sundays we need more staff", "on sundays we need more staff in order for the shop to open"]}
- reader 1: instruction: 'in order to open' is the obvious answer but 'for' would be left over, so it is a trap.
- reader 1: level: 'in order for X to' with all cards used is hard to see; 13 cards is long.
- reader 2: another correct answer, not accepted: ['we need more staff on sundays in order for the shop to open', 'in order for the shop to open we need more staff on sundays']
- reader 2: instruction: 'in order for ... to' is hard to see from the cards; many orders possible.

## r20-3-030 · B2.1 · order · conjunctions-1.csv:112

Task: Put the words in order.
word_cards: was | the | train | a | cancelled | the | missed | result | as | and | meeting | we
Key: {"kind": "order", "sentence": "the train was cancelled and as a result we missed the meeting", "also": ["the train was cancelled and we missed the meeting as a result"]}
- reader 1: another correct answer, not accepted: ['the meeting was cancelled and as a result we missed the train', 'we missed the meeting and as a result the train was cancelled (illogical)']
- reader 1: instruction: Train and meeting can swap; two logical sentences.
- reader 2: another correct answer, not accepted: ['the meeting was cancelled and as a result we missed the train', 'we missed the train and as a result the meeting was cancelled', 'we missed the meeting and as a result the train was cancelled', 'the meeting was cancelled and we missed the train as a result']
- reader 2: instruction: Cards are symmetric (train/meeting): two sensible sentences, both logical.
- reader 2: sense: Both main sentences are logical.

## r20-3-032 · B2.2 · gap · learn-drag-3.csv:2

Task: If I weren't so impatient, I ___ ___ sold my flat so cheaply last spring.
word_cards: had | won't | wouldn't | have
Key: {"kind": "gap", "accepted": [["wouldn't"], ["have"]]}
- reader 2: level: Mixed conditional is fine for B2.2.

## r20-3-035 · B2.2 · gap · learn-drag-3.csv:5

Task: If he ___ more confident, he ___ asked for a pay rise.
word_cards: were | would be | would have | will have
Key: {"kind": "gap", "accepted": [["were"], ["would have"]]}
- reader 1: a wrong option that fits: 'would be' fits the second gap as a passive ('he would be asked for a pay rise'), though odd.

## r20-3-036 · B2.2 · order · learn-drag-3.csv:6

Task: Put the words in order.
word_cards: on | beach | the | earlier | booked | be | now | we | we | had | would
Key: {"kind": "order", "sentence": "had we booked earlier we would be on the beach now", "also": ["we would be on the beach now had we booked earlier"]}
- reader 1: answer not accepted: we would be on the beach now if we had booked earlier
- reader 1: another correct answer, not accepted: ['if we had booked earlier we would be on the beach now', 'now we would be on the beach if we had booked earlier']
- reader 2: another correct answer, not accepted: ['had we booked earlier now we would be on the beach', 'now we would be on the beach had we booked earlier']
- the readers disagree

## r20-3-038 · B2.2 · order · learn-drag-3.csv:8

Task: Put the words in order.
word_cards: would | she | had | train | the | here | not | now | be | missed | she
Key: {"kind": "order", "sentence": "had she not missed the train she would be here now", "also": ["she would be here now had she not missed the train"]}
- reader 1: answer not accepted: she would be here now if she had not missed the train
- reader 1: another correct answer, not accepted: ['if she had not missed the train she would be here now', 'she would not be here now if she had missed the train', 'had she missed the train she would not be here now']
- reader 1: instruction: 'not' can go in either clause: opposite meanings, no context to decide.
- reader 1: sense: Both meanings are logical without context.
- reader 2: another correct answer, not accepted: ['now she would be here had she not missed the train', 'had she not missed the train now she would be here']
- the readers disagree

## r20-3-040 · B2.1 · order · learn-drag-3.csv:10

Task: Put the words in order.
word_cards: match | coach | warm | before | told | the | every | us | up | to
Key: {"kind": "order", "sentence": "the coach told us to warm up before every match", "also": []}
- reader 1: another correct answer, not accepted: ['before every match the coach told us to warm up', 'the coach told us before every match to warm up (less natural)']
- reader 1: level: Easy for B2.1.
- reader 2: another correct answer, not accepted: ['before every match the coach told us to warm up', 'the coach told us before every match to warm up (less natural)']
- reader 2: level: Easy for B2.1.

## r20-3-042 · B2.1 · order · learn-drag-3.csv:13

Task: Put the words in order.
word_cards: visa | need | might | the | agent | I | a | said
Key: {"kind": "order", "sentence": "the agent said I might need a visa", "also": []}
- reader 1: another correct answer, not accepted: ['I said the agent might need a visa']
- reader 1: instruction: Subject can swap.
- reader 2: another correct answer, not accepted: ['I said the agent might need a visa']
- reader 2: sense: Second reading is odd but correct.

## r20-3-043 · B2.2 · order · learn-drag-3.csv:14

Task: Put the words in order.
word_cards: how | to | start | she | asked | me
Key: {"kind": "order", "sentence": "she asked me how to start", "also": []}
- reader 1: level: Too easy for B2.2 (6 words, one possible order).
- reader 2: level: Too easy for B2.2 (six cards, one obvious order).

## r20-3-044 · B2.2 · order · learn-drag-3.csv:15

Task: Put the words in order.
word_cards: asked | arrive | time | should | they | what | they
Key: {"kind": "order", "sentence": "they asked what time they should arrive", "also": []}
- reader 1: level: Too easy for B2.2.
- reader 2: another correct answer, not accepted: ['what time should they arrive they asked (direct speech)']
- reader 2: level: Easy for B2.2.

## r20-3-045 · B2.2 · gap · learn-drag-3.csv:16

Task: He asked whether or not ___ ___ coming.
word_cards: I | did | was | am
Key: {"kind": "gap", "accepted": [["I"], ["was"]]}
- reader 1: instruction: 'am' is also correct if the coming is still future/true now.
- reader 2: instruction: Backshift is optional: 'whether or not I am coming' is also correct.

## r20-3-049 · B2.2 · order · learn-drag-3.csv:20

Task: Put the words in order.
word_cards: police | the | call | threatened | she | to
Key: {"kind": "order", "sentence": "she threatened to call the police", "also": []}
- reader 1: level: Too easy for B2.2 (6 words, one order).
- reader 2: level: Too easy for B2.2.

## r20-3-050 · B2.2 · order · learn-drag-3.csv:22

Task: Put the words in order.
word_cards: we | to | go | weren't | where | sure
Key: {"kind": "order", "sentence": "we weren't sure where to go", "also": []}
- reader 1: level: Too easy for B2.2.
- reader 2: level: Too easy for B2.2.

## r20-3-051 · B2.2 · order · learn-drag-3.csv:23

Task: Put the words in order.
word_cards: ask | know | to | who | she | didn't
Key: {"kind": "order", "sentence": "she didn't know who to ask", "also": []}
- reader 1: level: Too easy for B2.2.
- reader 2: level: Too easy for B2.2.

## r20-3-052 · B2.2 · order · learn-drag-3.csv:24

Task: Put the words in order.
word_cards: to | can't | the | decide | book | we | whether | hotel
Key: {"kind": "order", "sentence": "we can't decide whether to book the hotel", "also": []}
- reader 1: level: Easy for B2.2.

## r20-3-056 · B2.2 · order · learn-drag-3.csv:28

Task: Put the words in order.
word_cards: go | home | can | first | whoever | finishes
Key: {"kind": "order", "sentence": "whoever finishes first can go home", "also": []}
- reader 1: another correct answer, not accepted: ['whoever finishes can go home first (different meaning, correct)']
- reader 2: another correct answer, not accepted: ['whoever finishes can go home first (different meaning)']

## r20-3-057 · B2.2 · order · learn-drag-3.csv:29

Task: Put the words in order.
word_cards: explained | to | the | system | remains | why | failed | be
Key: {"kind": "order", "sentence": "why the system failed remains to be explained", "also": []}
- reader 1: level: Passive 'remains to be explained' is high B2; fine for B2.2.

## r20-3-058 · B2.1 · order · learn-drag-4.csv:12

Task: Put the words in order.
word_cards: I'd | twice | offer | were | that | about | I | you | think | if
Key: {"kind": "order", "sentence": "if I were you I'd think twice about that offer", "also": ["I'd think twice about that offer if I were you"]}
- reader 2: level: Fixed expression, easy for B2.1.

## r20-3-059 · B2.1 · gap · learn-drag-4.csv:13

Task: If the company ___ more flexible hours, people ___ happier.
word_cards: would offer | will be | would be | offered
Key: {"kind": "gap", "accepted": [["offered"], ["would be"]]}
- reader 1: a wrong option that fits: 'would offer' in gap 1 is accepted by some speakers (informal/US) but not standard here.
- reader 2: level: Second conditional, B1 level.

## r20-3-060 · B2.1 · order · learn-drag-4.csv:14

Task: Put the words in order.
word_cards: the | I | if | tell | would | knew | I | you | answer
Key: {"kind": "order", "sentence": "if I knew the answer I would tell you", "also": ["I would tell you if I knew the answer"]}
- reader 1: answer not accepted: i would tell you the answer if i knew
- reader 1: another correct answer, not accepted: ['if i knew i would tell you the answer']
- reader 1: instruction: 'the answer' can sit in either clause: several orders.
- reader 2: answer not accepted: I would tell you the answer if I knew
- reader 2: level: Easy for B2.1.

