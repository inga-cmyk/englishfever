# Blind check r1: flags for the judge

105 tasks, 2 readers.

## r1-002 · B1.1 · write · built-in

Task: Write two sentences about a timetable: a train, a class, a shop or a film.
Key: {"kind": "write", "model": "My class starts at 9.00. It finishes at 11.30.", "must": ["Use a timetable verb with *at* and a time, such as *at nine*, *at 9.00* or *at noon*.", "Write two sentences."]}
- reader 1: instruction: The instruction does not say what grammar is wanted (present simple for timetabled future); a learner could write e.g. 'The shop was open until six' and still meet the instruction. 'A timetable ... a shop' is slightly odd (a shop has opening hours, not a timetable).
- reader 2: instruction: Does not say which form to use (present simple for timetables), yet the app checks forms. 'A shop' has opening hours, not a timetable.

## r1-003 · B2.1 · text · built-in

Task: Imagine it happened differently. Start with *If I*: I didn't see the sign, so I parked there and got a fine.
Key: {"kind": "text", "accepted": [["If I had seen the sign, I wouldn't have parked there.", "If I had seen the sign, I wouldn't have got a fine.", "If I had seen the sign, I would not have got a fine.", "If I had seen the sign, I wouldn't have gotten a fine.", "If I had seen the sign, I wouldn't have been fined.", "If I had seen the sign, I would not have parked there.", "I wouldn't have parked there if I had seen the sign.", "I wouldn't have got a fine if I had seen the sign.", "I would not have got a fine if I had seen the sign.", "I wouldn't have gotten a fine if I had seen the sign.", "I wouldn't have been fined if I had seen the sign.", "I would not have parked there if I had seen the sign."]]}
- reader 1: answer not accepted: If I had seen the sign, I wouldn't have parked there and I wouldn't have got a fine.
- reader 1: another correct answer, not accepted: ["If I'd seen the sign, I wouldn't have parked there. / If I had seen the sign, I wouldn't have got a fine. / If I had seen the sign, I wouldn't have parked there or got a fine. / ...and wouldn't have got a fine. / (AmE) ...gotten a fine."]
- reader 1: instruction: The source has two results (parked, got a fine); it is unclear whether one or both must appear in the answer, so many forms should be accepted.
- reader 2: answer not accepted: If I had seen the sign, I wouldn't have parked there and I wouldn't have got a fine.
- reader 2: another correct answer, not accepted: ["If I had seen the sign, I wouldn't have parked there and got a fine.", "... wouldn't have gotten a fine (American)", 'If I had seen the sign, I would have parked somewhere else.']
- reader 2: instruction: 'Imagine it happened differently' is vague, and the prompt has two results (parked, got a fine), so many valid sentences are possible. A typed checker must accept all of them.

## r1-004 · B2.2 · mcq · built-in

Task: Which sentence is NOT correct?
options: If I'd known about the traffic, I would've left earlier. | If I had known about the traffic, I would have left earlier. | Had I known about the traffic, I would have left earlier. | If I'd have known about the traffic, I would've left earlier.
Key: {"kind": "mcq", "correct": "If I'd have known about the traffic, I would've left earlier.", "wrong": ["If I'd known about the traffic, I would've left earlier.", "If I had known about the traffic, I would have left earlier.", "Had I known about the traffic, I would have left earlier."]}
- reader 1: sense: Note: 'If I'd have known' is very common in informal spoken English (also AmE), so some learners hear it; still non-standard, so the key is fine.

## r1-005 · B2.1 · gap · built-in

Task: I didn't learn English at school. If I ___ it then, I ___ fluent now. (learn / be)
Key: {"kind": "gap", "accepted": [["had learned", "had learnt", "'d learned", "'d learnt"], ["would be", "'d be"]]}
- reader 1: another correct answer, not accepted: ['["had learned", "would be"]; ["\'d learnt"/"\'d learned", "\'d be"]']
- reader 2: another correct answer, not accepted: [['had learned', 'might be']]

## r1-006 · B1.2 · mcq · built-in

Task: Choose the correct option: 'Where do you work?' She asked me ___.
options: where I work did | where I worked | where do I work | where did I work
Key: {"kind": "mcq", "correct": "where I worked", "wrong": ["where did I work", "where do I work", "where I work did"]}
- reader 1: sense: 'where I work did' is a random, unbelievable distractor. ('where I work' without backshift would also be correct if still true, but it is not offered, so no ambiguity.)
- reader 2: sense: 'where I work did' is not a believable learner mistake.

## r1-008 · B2.2 · gap · built-in

Task: 'Congratulations, Jo! You finally passed the exam!' I congratulated Jo ___ passing the exam.
word_cards: about | on | with | at
Key: {"kind": "gap", "accepted": [["on"]]}
- reader 1: sense: 'You finally passed the exam!' is AmE-flavoured; BrE (Murphy) would say 'You've finally passed'. ('congratulated Jo for' is used informally but not offered.)

## r1-009 · B2.2 · text · built-in

Task: Say what my sister did, in one sentence. My sister said to me: 'You really should see a doctor about that cough.'
Key: {"kind": "text", "accepted": [["My sister advised me to see a doctor about that cough.", "My sister urged me to see a doctor about that cough.", "My sister told me to see a doctor about that cough.", "My sister encouraged me to see a doctor about that cough.", "My sister recommended that I see a doctor about that cough.", "My sister recommended that I should see a doctor about that cough.", "My sister suggested that I see a doctor about that cough.", "My sister suggested that I should see a doctor about that cough.", "My sister suggested seeing a doctor about that cough.", "My sister suggested I see a doctor about that cough.", "My sister suggested I should see a doctor about that cough.", "My sister recommended seeing a doctor about that cough.", "My sister recommended I see a doctor about that cough.", "My sister recommended I should see a doctor about that cough.", "My sister advised seeing a doctor about that cough.", "My sister advised that I see a doctor about that cough.", "My sister advised that I should see a doctor about that cough.", "My sister said I should see a doctor about that cough.", "My sister said that I should see a doctor about that cough.", "My sister told me I should see a doctor about that cough.", "My sister told me that I should see a doctor about that cough."]]}
- reader 1: answer not accepted: My sister advised me to see a doctor about my cough.
- reader 1: another correct answer, not accepted: ['My sister told me (that) I really should see a doctor about my cough. / My sister said (that) I should see a doctor about my cough. / My sister recommended/suggested that I (should) see a doctor about my cough. / My sister urged me to see a doctor about my cough. / My sister told me to see a doctor about my cough.']
- reader 1: instruction: 'Say what my sister did' is vague: it hints at a reporting verb (advised) but does not name it, so many verbs and patterns are possible; key must accept them.
- reader 2: answer not accepted: My sister advised me to see a doctor about my cough.
- reader 2: another correct answer, not accepted: ['My sister told me (that) I really should see a doctor about my cough.', 'My sister said (that) I should see a doctor about my cough.', 'My sister urged me to see a doctor about my cough.', 'My sister recommended that I (should) see a doctor about my cough.', 'My sister told me to see a doctor about my cough.']
- reader 2: instruction: 'Say what my sister did' is vague: it does not say a reporting verb (advise) is wanted, so many different correct sentences are possible for a typed answer.

## r1-011 · B2.1 · text · built-in

Task: Make it indirect: Why didn't the order arrive?
Key: {"kind": "text", "accepted": [["Could you tell me why the order didn't arrive?", "Do you know why the order didn't arrive?", "Can you tell me why the order didn't arrive?", "I'd like to know why the order didn't arrive.", "Would you mind telling me why the order didn't arrive?", "Could you please tell me why the order didn't arrive?", "Do you happen to know why the order didn't arrive?", "I wonder why the order didn't arrive.", "I was wondering why the order didn't arrive.", "Could you tell me why the order did not arrive?", "Do you know why the order did not arrive?", "Could you tell me why the order didn't arrive, please?", "Can you please tell me why the order didn't arrive?", "Would you tell me why the order didn't arrive?", "Could you please tell me why the order did not arrive?", "Could you tell me why the order did not arrive, please?", "Can you please tell me why the order did not arrive?", "Would you mind telling me why the order did not arrive?", "Do you happen to know why the order did not arrive?", "I wonder why the order did not arrive.", "I was wondering why the order did not arrive.", "I'd like to know why the order did not arrive.", "Would you tell me why the order did not arrive?"]]}
- reader 1: another correct answer, not accepted: ["Can you tell me why the order didn't arrive? / Do you know why the order didn't arrive? / I'd like to know why the order didn't arrive. / I wonder why the order didn't arrive. / Could you tell me why the order did not arrive? / reported: She asked why the order hadn't arrived."]
- reader 1: instruction: 'Make it indirect' gives no opening phrase, so there are many correct answers (Can/Could you tell me, Do you know, I wonder, I'd like to know...) and 'indirect' could also be read as reported speech. Give the opening (e.g. 'Start with Could you tell me').
- reader 1: sense: 'Why didn't the order arrive?' is slightly unnatural for a still-missing order; BrE would say 'Why hasn't the order arrived?'.
- reader 2: another correct answer, not accepted: ["Can you tell me why the order hasn't arrived?"]
- reader 2: instruction: 'Make it indirect' gives no opening phrase, so the answer is completely open for a typed task.

## r1-013 · A2.2 · mcq · a2-big-1.csv:149

Task: Which sentence is NOT correct?
options: Cakes are sold at the market. | The bread are baked every morning. | Milk is delivered every morning. | The rolls are baked in the oven.
Key: {"kind": "mcq", "correct": "The bread are baked every morning.", "wrong": ["Milk is delivered every morning.", "The rolls are baked in the oven.", "Cakes are sold at the market."]}
- reader 1: sense: The wrong sentence tests uncountable-noun agreement, not the passive form itself; acceptable but the target may be unclear.

## r1-016 · A2.2 · mcq · a2-rel-might-1.csv:3

Task: Choose the correct option: We stayed at a hotel ___ has a big pool.
options: which | who | where | what
Key: {"kind": "mcq", "correct": "which", "wrong": ["who", "what", "where"]}
- reader 1: sense: 'that' (also correct) is not offered, fine.

## r1-017 · A2.2 · mcq · a2-rel-might-1.csv:4

Task: Choose the correct option: I use an app ___ makes short videos.
options: what | where | who | that
Key: {"kind": "mcq", "correct": "that", "wrong": ["who", "what", "where"]}
- reader 1: sense: 'an app that makes short videos' is a little odd (the user makes the videos); 'an app that lets me make / edits short videos' is more natural.

## r1-023 · A2.2 · gap · a2-rel-might-1.csv:10

Task: Write the missing word: A pilot is a person ___ flies planes.
Key: {"kind": "gap", "accepted": [["who", "that"]]}
- reader 1: another correct answer, not accepted: ['["that"]']

## r1-024 · A2.2 · gap · a2-rel-might-1.csv:11

Task: Write the missing word: I bought a bike ___ has ten gears.
Key: {"kind": "gap", "accepted": [["which", "that"]]}
- reader 1: another correct answer, not accepted: ['["which"]']

## r1-025 · A2.2 · gap · a2-rel-might-1.csv:12

Task: Write the missing word: The woman ___ teaches us yoga is from India.
Key: {"kind": "gap", "accepted": [["who", "that"]]}
- reader 1: another correct answer, not accepted: ['["that"]']

## r1-026 · A2.2 · gap · a2-rel-might-1.csv:13

Task: Write the missing word: Do you like songs ___ tell a story?
Key: {"kind": "gap", "accepted": [["which", "that"]]}
- reader 1: another correct answer, not accepted: ['["which"]']

## r1-027 · A2.2 · gap · a2-rel-might-1.csv:14

Task: Write the missing word: On our trip we met a guide ___ spoke perfect English.
Key: {"kind": "gap", "accepted": [["who", "that"]]}
- reader 1: another correct answer, not accepted: ['["that"]']

## r1-028 · A2.2 · text · a2-rel-might-1.csv:15

Task: Join with *who*: I have a cousin. He works in a hotel.
Key: {"kind": "text", "accepted": [["I have a cousin who works in a hotel."]]}
- reader 1: another correct answer, not accepted: ['I have a cousin that works in a hotel.']

## r1-029 · A2.2 · text · a2-rel-might-1.csv:16

Task: Join the two sentences: We visited a museum. It has old cars.
Key: {"kind": "text", "accepted": [["We visited a museum which has old cars.", "We visited a museum that has old cars."]]}
- reader 1: another correct answer, not accepted: ['We visited a museum that has old cars. / We visited a museum which/that had old cars. / We visited a museum, which has old cars.']
- reader 1: instruction: No joining word is named (cf. r1-028 'Join with who'); 'We visited a museum and it has old cars' also joins the sentences.
- reader 2: another correct answer, not accepted: ['We visited a museum which had old cars.', 'We visited a museum that had old cars.', 'We visited a museum with old cars.', 'We visited a museum, and it has old cars.']
- reader 2: instruction: Does not say how to join (with which/that), so 'and' or 'with' also joins the sentences correctly.

## r1-030 · A2.2 · text · a2-rel-might-1.csv:17

Task: Join the two sentences: The app helps me learn new words. It is free.
Key: {"kind": "text", "accepted": [["The app which helps me learn new words is free.", "The app that helps me learn new words is free.", "The app which is free helps me learn new words.", "The app that is free helps me learn new words."]]}
- reader 1: another correct answer, not accepted: ['The app that helps me learn new words is free. / The app, which is free, helps me learn new words. / The app which/that is free helps me learn new words. / The app that helps me to learn new words is free.']
- reader 1: instruction: No joining word or structure is named; the learner may also use 'and' ('The app helps me learn new words and it is free'). Embedding the clause mid-sentence is harder than r1-028/029 without a hint.
- reader 2: another correct answer, not accepted: ['The app helps me learn new words, and it is free.']
- reader 2: instruction: Does not say how to join or which sentence becomes the relative clause; several structures are correct.
- reader 2: level: Relative clause inside the subject is a step harder than the other A2.2 items (all others add the clause at the end).

## r1-031 · A2.2 · order · a2-rel-might-1.csv:18

Task: Put the words in order.
word_cards: piano | the | who | have | plays | a | neighbour | i
Key: {"kind": "order", "sentence": "i have a neighbour who plays the piano", "also": []}
- reader 1: another correct answer, not accepted: ['(marginal, odd) I have the neighbour who plays a piano.']
- reader 2: another correct answer, not accepted: ['I have the neighbour who plays a piano. (grammatical but unnatural)']

## r1-039 · A2.2 · match · a2-rel-might-1.csv:26

Task: Match each beginning with its ending.
left: A baker is a person | A fridge is a machine | A tourist is someone | A map is a picture
right: who travels for fun. | which keeps food cold. | who makes bread. | which shows roads and towns.
Key: {"kind": "match", "pairs": [["A baker is a person", "who makes bread."], ["A fridge is a machine", "which keeps food cold."], ["A tourist is someone", "who travels for fun."], ["A map is a picture", "which shows roads and towns."]]}
- reader 1: instruction: Who/which halves the choices (people vs things), so only 2 x 2 pairing is needed; easy but acceptable at A2.
- reader 1: sense: 'A map is a picture' is a bit loose ('a drawing' or 'a plan' is more accurate).
- reader 2: sense: 'A map is a picture' is a slightly odd definition (a drawing/plan).

## r1-043 · A2.2 · mcq · a2-rel-might-1.csv:30

Task: Choose the correct option: He's very tired. He ___ not come to the party.
options: don't | doesn't | is | might
Key: {"kind": "mcq", "correct": "might", "wrong": ["doesn't", "is", "don't"]}
- reader 1: sense: Because 'not' follows the gap, the distractors give 'don't not / doesn't not / is not come', which are not believable learner mistakes; the task is solvable by elimination.

## r1-048 · A2.2 · gap · a2-rel-might-1.csv:35

Task: Write the missing word: I'm not sure, but I ___ visit my aunt this weekend.
Key: {"kind": "gap", "accepted": [["might", "may", "could"]]}
- reader 1: another correct answer, not accepted: ['["may"]; ["could"] (possible, more like an option/plan)']

## r1-049 · A2.2 · gap · a2-rel-might-1.csv:36

Task: Write the missing word: The road is icy. You ___ fall, so be careful.
Key: {"kind": "gap", "accepted": [["might", "may", "could", "can"]]}
- reader 1: another correct answer, not accepted: ['["may"]; ["could"]']

## r1-051 · A2.2 · gap · a2-rel-might-1.csv:38

Task: Write the missing word: Take your laptop. I'm not sure, but we ___ need it on the trip.
Key: {"kind": "gap", "accepted": [["might", "may", "could"]]}
- reader 1: another correct answer, not accepted: ['["may"]; ["could"]']

## r1-052 · A2.2 · gap · a2-rel-might-1.csv:39

Task: Write the missing word: I'm not sure, but they ___ have a map of the town at the desk.
Key: {"kind": "gap", "accepted": [["might", "may", "could"]]}
- reader 1: another correct answer, not accepted: ['["may"]; ["could"]']

## r1-053 · A2.2 · text · a2-rel-might-1.csv:40

Task: Rewrite with *might*: Perhaps the concert tickets are sold out.
Key: {"kind": "text", "accepted": [["The concert tickets might be sold out."]]}
- reader 1: another correct answer, not accepted: ['The concert tickets might have sold out. / The tickets for the concert might be sold out.']
- reader 2: another correct answer, not accepted: ['The concert tickets might have sold out.']

## r1-054 · A2.2 · text · a2-rel-might-1.csv:41

Task: Make it negative: We might finish the project today.
Key: {"kind": "text", "accepted": [["We might not finish the project today.", "We mightn't finish the project today.", "Today we might not finish the project.", "Today we mightn't finish the project."]]}
- reader 1: another correct answer, not accepted: ["We mightn't finish the project today. (BrE, informal)"]
- reader 2: another correct answer, not accepted: ["We mightn't finish the project today. (British, rare)"]

## r1-064 · A2.2 · match · a2-rel-might-1.csv:51

Task: Match each sentence with its meaning.
left: It will rain. | She might call. | He won't come. | They might not win.
right: Perhaps they will lose. | I'm sure he will stay at home. | Perhaps she will call. | I'm sure about the rain.
Key: {"kind": "match", "pairs": [["It will rain.", "I'm sure about the rain."], ["She might call.", "Perhaps she will call."], ["He won't come.", "I'm sure he will stay at home."], ["They might not win.", "Perhaps they will lose."]]}
- reader 1: sense: 'I'm sure he will stay at home' is not the same meaning as 'He won't come' (he could go somewhere else); 'I'm sure he will not come' / 'I'm sure he'll stay away' is closer. 'I'm sure about the rain' is a slightly unnatural paraphrase.
- reader 2: sense: 'I'm sure about the rain' is unnatural; 'He won't come' does not mean 'he will stay at home' (he may go elsewhere); 'might not win' = 'perhaps they will lose' ignores a draw.

## r1-065 · B1.2 · mcq · b1-cond-rep-1.csv:219

Task: Which sentence is NOT correct?
options: He asked if I had liked the job. | He asked me did I like the job. | He asked me if I liked the job. | He asked me whether I liked the job.
Key: {"kind": "mcq", "correct": "He asked me did I like the job.", "wrong": ["He asked me if I liked the job.", "He asked me whether I liked the job.", "He asked if I had liked the job."]}
- reader 1: sense: Note: 'He asked me did I like the job' is normal in Irish English and informal speech; 'He asked if I had liked the job' is correct but means something different, which may confuse learners looking for the error.

## r1-067 · A2.2 · text · b1-new-3.csv:144

Task: Make a sentence with decide: I will go home early.
Key: {"kind": "text", "accepted": [["I decided to go home early.", "I have decided to go home early."]]}
- reader 1: another correct answer, not accepted: ["I've decided to go home early. / I have decided to go home early. / I've decided I will go home early."]
- reader 1: instruction: The instruction gives no tense or form; 'Make a sentence with decide' is vague (should it be 'I decided to...', 'I've decided to...'?). 'decide' is not marked as the word to use (no italics, unlike other tasks).
- reader 2: another correct answer, not accepted: ['I decided that I would go home early.']
- reader 2: instruction: Unclear what to do: no tense or pattern is given ('decide' could be used in many ways), and 'decide' is not marked like other key words.

## r1-068 · B1.1 · text · b1-tenses-1.csv:64

Task: Make a question with Why: She is crying.
Key: {"kind": "text", "accepted": [["Why is she crying?"]]}
- reader 2: level: Too easy for B1.1: a present continuous Why-question is A1/A2.

## r1-070 · B1.2 · mcq · zz-blind-pairs-1.csv:2

Task: Choose the correct option: The lights are off and nobody answers the door. They ___ be at home.
options: mustn't | can't | must
Key: {"kind": "mcq", "correct": "can't", "wrong": ["must", "mustn't"]}
- reader 2: a wrong option that fits: ["mustn't is only marginal: American English uses 'must not' for negative deduction (e.g. 'They must not be home'); fine for a British-English course, but a careful AmE speaker might accept it"]

## r1-072 · B1.2 · mcq · zz-blind-pairs-1.csv:4

Task: Choose the correct option: That ___ be Tom's car. He sold it last month.
options: mustn't | can't | must
Key: {"kind": "mcq", "correct": "can't", "wrong": ["must", "mustn't"]}
- reader 2: a wrong option that fits: ["mustn't is only marginal: American English uses 'must not' for negative deduction (e.g. 'They must not be home'); fine for a British-English course, but a careful AmE speaker might accept it"]

## r1-074 · B1.2 · mcq · zz-blind-pairs-1.csv:6

Task: Choose the correct option: This ___ be the right address. There's no number 52 on this street.
options: mustn't | must | can't
Key: {"kind": "mcq", "correct": "can't", "wrong": ["must", "mustn't"]}
- reader 2: a wrong option that fits: ["mustn't is only marginal: American English uses 'must not' for negative deduction (e.g. 'They must not be home'); fine for a British-English course, but a careful AmE speaker might accept it"]

## r1-075 · B1.2 · mcq · zz-blind-pairs-1.csv:7

Task: Choose the correct option: Mark works at two jobs and has three small children. He ___ be bored at home.
options: must | mustn't | can't
Key: {"kind": "mcq", "correct": "can't", "wrong": ["must", "mustn't"]}
- reader 2: a wrong option that fits: ["mustn't is only marginal: American English uses 'must not' for negative deduction (e.g. 'They must not be home'); fine for a British-English course, but a careful AmE speaker might accept it"]

## r1-088 · B1.1 · mcq · zz-blind-pairs-1.csv:20

Task: Choose the correct option: The fire was big, but everyone ___ get out of the building.
options: was able | was able to | could
Key: {"kind": "mcq", "correct": "was able to", "wrong": ["could", "was able"]}
- reader 1: a wrong option that fits: could (only in informal use; Murphy 26: not for a single achievement in a positive sentence)

## r1-089 · B1.1 · mcq · zz-blind-pairs-1.csv:21

Task: Choose the correct option: The main road was closed, but we ___ find another way home.
options: were able | could | were able to
Key: {"kind": "mcq", "correct": "were able to", "wrong": ["could", "were able"]}
- reader 1: a wrong option that fits: could (only in informal use; Murphy 26: not for a single achievement in a positive sentence)

## r1-091 · B1.1 · mcq · zz-blind-pairs-1.csv:23

Task: Choose the correct option: Our flight was cancelled, but luckily we ___ get seats on the next one.
options: were able to | could to | could
Key: {"kind": "mcq", "correct": "were able to", "wrong": ["could", "could to"]}
- reader 1: a wrong option that fits: could (only in informal use; Murphy 26: not for a single achievement in a positive sentence)

## r1-092 · B1.1 · mcq · zz-blind-pairs-1.csv:24

Task: Choose the correct option: The sofa was very heavy, but the two of us ___ carry it upstairs.
options: could to | could | managed to
Key: {"kind": "mcq", "correct": "managed to", "wrong": ["could", "could to"]}
- reader 1: a wrong option that fits: could (only in informal use; Murphy 26: not for a single achievement in a positive sentence)

