# Blind check r21-6: flags for the judge

59 tasks, 2 readers.

## r21-6-001 · B1.1 · write · built-in

Task: What is changing in your life or your city these days? Write one sentence.
Key: {"kind": "write", "model": "More people are working from home these days.", "must": ["Use *am/is/are* + verb-ing."]}
- reader 1: instruction: Open task; fine.
- reader 2: instruction: Does not say which structure is expected (present continuous?); learner does not know what the app checks, so a correct sentence in present simple (e.g. 'Prices have risen') may be marked wrong.

## r21-6-002 · B1.1 · gap · built-in

Task: I ___ Tom at the party, so I called him later. (not / see)
Key: {"kind": "gap", "accepted": [["didn't see", "did not see"]]}
- reader 2: another correct answer, not accepted: [["hadn't seen"], ['had not seen']]
- reader 2: instruction: '(not / see)' gives no tense; 'hadn't seen' is also acceptable though less natural.

## r21-6-003 · B1.1 · mcq · built-in

Task: In 'When Mia called, I was cooking', which action started first?
options: The calling. | Both together. | We can't know. | The cooking.
Key: {"kind": "mcq", "correct": "The cooking.", "wrong": ["The calling.", "Both together.", "We can't know."]}
- reader 1: level: Fine.

## r21-6-004 · B1.2 · mcq · built-in

Task: Which sentence is NOT correct?
options: We were going to stay longer. | They was going to meet us, but they were late. | She was going to leave when he arrived. | I was going to call you, but I lost your number.
Key: {"kind": "mcq", "correct": "They was going to meet us, but they were late.", "wrong": ["I was going to call you, but I lost your number.", "She was going to leave when he arrived.", "We were going to stay longer."]}
- reader 1: sense: 'They was' is a rare slip for B1 learners; mild.
- reader 2: sense: 'They was' is a rare error for B1 learners (subject-verb agreement, A1 level).

## r21-6-005 · B1.1 · write · built-in

Task: Write two sentences about how long you have lived in your city or worked in your job. Use for in one and since in the other.
Key: {"kind": "write", "model": "I have lived in Riga for ten years. I have worked here since 2020.", "must": ["Use *have/has* + past participle.", "Use *for* + a period of time.", "Use *since* + a start time."]}
- reader 2: instruction: Learner must also know present perfect is wanted; 'I lived here since...' is wrong but the app check is unknown. Fine otherwise.

## r21-6-007 · B1.1 · mcq · built-in

Task: Your friend is out of breath, but she isn't running now. Why is she out of breath?
options: She is running. | She has been running. | She has run. | She runs.
Key: {"kind": "mcq", "correct": "She has been running.", "wrong": ["She is running.", "She runs.", "She has run."]}
- reader 1: a wrong option that fits: She has run. (also correct: result of running)
- reader 1: sense: 'She has run' also fits; option too close.
- reader 2: a wrong option that fits: She has run. (also fits: she has just finished running)
- reader 2: instruction: 'She has run' is also possible; the task does not say continuous/recent activity is the point.

## r21-6-009 · B1.2 · gap · built-in

Task: Look at the floor! The children ___ with paint. (play)
Key: {"kind": "gap", "accepted": [["have been playing"]]}
- reader 1: another correct answer, not accepted: [['have played'], ['are playing']]
- reader 1: instruction: No tense hint; 'are playing' and 'have played' also fit.
- reader 2: another correct answer, not accepted: [['are playing'], ['have played']]
- reader 2: instruction: Tense not given; 'are playing' also fits (children still playing, floor dirty). 'have played' possible too.

## r21-6-011 · B1.2 · mcq · built-in

Task: Which sentence is NOT correct?
options: It's going to rain, look at the sky. | He is going to be arrive soon. | She is about to leave the office. | Will you help me with this box?
Key: {"kind": "mcq", "correct": "He is going to be arrive soon.", "wrong": ["She is about to leave the office.", "Will you help me with this box?", "It's going to rain, look at the sky."]}
- reader 1: sense: 'going to be arrive' is an odd, rarely written error.
- reader 2: sense: 'going to be arrive' is an unlikely learner error; a form few write.

## r21-6-012 · B1.2 · write · built-in

Task: Look at those dark clouds. Your friend has no umbrella. Write two sentences: say what is about to happen, then offer to lend your umbrella.
Key: {"kind": "write", "model": "It is going to rain. I'll lend you my umbrella.", "must": ["Use *going to* + base verb in the prediction.", "Use *I'll* or *I will* for the offer."]}
- reader 1: instruction: 'about to' in the task partly gives the form away; 'offer' could be done with Shall I / Would you like.
- reader 2: instruction: 'Look at those dark clouds' is addressed to the learner, mixing scene and task. 'About to' with rain is less natural than 'going to'; offer form not specified (will / shall I / you can have).
- reader 2: sense: 'It is about to rain' is slightly odd; natural English would use going to.

## r21-6-014 · B1.1 · mcq · built-in

Task: Which sentence is NOT correct?
options: The bridge was built in 1998. | The thieves were arrested. | She was gave a prize at school. | I was told the news by Tom.
Key: {"kind": "mcq", "correct": "She was gave a prize at school.", "wrong": ["The thieves were arrested.", "The bridge was built in 1998.", "I was told the news by Tom."]}
- reader 1: sense: 'was gave' is rare for B1 learners.
- reader 2: sense: Believable mistake.

## r21-6-015 · B1.2 · gap · built-in

Task: The rooms ___ right now. (clean)
Key: {"kind": "gap", "accepted": [["are being cleaned"]]}
- reader 1: instruction: No hint that passive is needed except the subject; fine.
- reader 2: instruction: Nothing signals passive; learners will type 'are cleaning'/'are cleaned'. '(clean)' alone is misleading.
- reader 2: level: Present continuous passive is B2, not B1.2.

## r21-6-018 · B1.2 · mcq · built-in

Task: Which sentence is correct?
options: Could you let me know whether has been the contract signed? | Could you let me know whether the contract has been signed? | Could you let me know if has the contract been signed? | Could you let me know has the contract been signed?
Key: {"kind": "mcq", "correct": "Could you let me know whether the contract has been signed?", "wrong": ["Could you let me know has the contract been signed?", "Could you let me know if has the contract been signed?", "Could you let me know whether has been the contract signed?"]}
- reader 2: level: Embedded question with passive present perfect is hard for B1.2.

## r21-6-019 · B1.1 · match · built-in

Task: Match each situation with the response that best fits its purpose.
left: You decide now to help a colleague with a heavy bag. | You describe a confirmed appointment for tomorrow. | You predict rain because you can see dark clouds.
right: It's going to rain. | I'm seeing the dentist at ten. | I'll carry that for you.
Key: {"kind": "match", "pairs": [["You decide now to help a colleague with a heavy bag.", "I'll carry that for you."], ["You describe a confirmed appointment for tomorrow.", "I'm seeing the dentist at ten."], ["You predict rain because you can see dark clouds.", "It's going to rain."]]}
- reader 2: instruction: 'fits its purpose' is vague wording; the tasks are easily solved by keywords (dark clouds / rain).

## r21-6-020 · B1.2 · match · b1-cond-rep-1.csv:140

Task: Match each sentence with its meaning.
left: If I had gone, I would have met her. | If I go, I will meet her. | If I went, I would meet her. | If I go, I meet her.
right: I didn't go. | I may go. | I'm imagining it now. | this always happens
Key: {"kind": "match", "pairs": [["If I had gone, I would have met her.", "I didn't go."], ["If I go, I will meet her.", "I may go."], ["If I went, I would meet her.", "I'm imagining it now."], ["If I go, I meet her.", "this always happens"]]}
- reader 1: sense: 'I may go' is a weak paraphrase of a first conditional; 'I'm imagining it now' is awkward. Capitalisation differs between right-side items.
- reader 2: instruction: 'I'm imagining it now' and 'I may go' are odd paraphrases; right-hand cards inconsistent in capitals/full stops ('this always happens').
- reader 2: level: Four conditional types in one task is B2 level rather than B1.2.

## r21-6-022 · B1.2 · gap · b1-cond-rep-1.csv:202

Task: 'Have you finished?' He asked if I ___ . (finish)
Key: {"kind": "gap", "accepted": [["had finished"]]}
- reader 1: another correct answer, not accepted: [['have finished'], ['finished']]
- reader 1: instruction: 'have finished' is correct if reported soon; 'finished' is informal/less natural.
- reader 2: another correct answer, not accepted: [['finished'], ['have finished']]
- reader 2: instruction: 'finished' and 'have finished' also acceptable (informal / same-day report); no cue for backshift.

## r21-6-023 · B1.2 · gap · b1-cond-rep-1.csv:207

Task: At school, years ago: 'Do you like jazz?' → He asked me ___.
Key: {"kind": "gap", "accepted": [["if I liked jazz", "whether I liked jazz"]]}
- reader 1: another correct answer, not accepted: [['if I like jazz'], ['whether I like jazz'], ['if I did like jazz']]
- reader 1: instruction: Whole clause in one gap; many correct versions, unclear whether if/whether needed.
- reader 2: another correct answer, not accepted: [['if I liked jazz or not'], ['whether I liked jazz or not']]
- reader 2: instruction: Learner types a whole clause; if/whether both correct; 'years ago' needed for liked.

## r21-6-024 · B1.2 · gap · b1-cond-rep-1.csv:210

Task: A week ago: 'What did you do last night?' → She asked me ___.
Key: {"kind": "gap", "accepted": [["what I had done the night before", "what I had done the previous night", "what I 'd done the night before", "what I 'd done the previous night"]]}
- reader 1: another correct answer, not accepted: [['what I did the night before'], ['what I did the previous night'], ['what I had done that night'], ['what I did that night'], ['what I had done last night']]
- reader 1: instruction: Open clause with many valid forms; 'last night' after a week is tense/time shift ambiguity.
- reader 2: another correct answer, not accepted: [['what I did the night before'], ['what I did the previous night'], ['what I had done that night'], ['what I did last night']]
- reader 2: instruction: Many correct variants (time phrase and past simple/past perfect); hard for an exact-match app.

## r21-6-025 · B1.2 · gap · b1-cond-rep-1.csv:234

Task: I wonder ___ he will come.
word_cards: that | whether | what
Key: {"kind": "gap", "accepted": [["whether"]]}
- reader 1: a wrong option that fits: what? no. 'that' no.
- reader 2: a wrong option that fits: 'that' is grammatical in archaic 'I wonder that he will come' (= I am surprised), but a different meaning
- reader 2: instruction: Fine.

## r21-6-026 · B1.1 · order · b1-new-1.csv:5

Task: Put all the words in order. More than one answer is possible.
word_cards: she | use | she | didn't | but | it | loves | to | cooking | enjoy | now
Key: {"kind": "order", "sentence": "she didn't use to enjoy cooking but now she loves it", "also": ["she didn't use to enjoy cooking but she loves it now"]}
- reader 1: another correct answer, not accepted: ["she loves cooking now but she didn't use to enjoy it", "now she loves it but she didn't use to enjoy cooking", "now she loves cooking but she didn't use to enjoy it", "she didn't use to enjoy it but now she loves cooking"]
- reader 1: level: 'didn't use to' is hard for B1.1; 11 words.
- reader 2: another correct answer, not accepted: [["now she loves it but she didn't use to enjoy cooking"], ["she loves cooking now but she didn't use to enjoy it"], ["now she loves cooking but she didn't use to enjoy it"], ["she loves it now but she didn't use to enjoy cooking"], ["she didn't use to enjoy it but now she loves cooking"], ["she didn't use to enjoy it but she loves cooking now"], ["she loves cooking but she didn't use to enjoy it now"]]
- reader 2: instruction: 'use' as a separate card is a trap but fine; last variant in list is odd English.

## r21-6-029 · B1.1 · mcq · b1-tenses-1.csv:74

Task: Which sentence is NOT correct?
options: Are you following the instructions? | I'm not understanding the instructions. | I'm reading the instructions now. | I don't understand the instructions.
Key: {"kind": "mcq", "correct": "I'm not understanding the instructions.", "wrong": ["I don't understand the instructions.", "I'm reading the instructions now.", "Are you following the instructions?"]}
- reader 1: sense: Some speakers accept 'I'm not understanding' informally; fine as a B1 rule.
- reader 2: sense: 'I'm not understanding' is used informally and by some speakers (e.g. 'I'm not understanding this'), so it is arguably not wrong.

## r21-6-030 · B1.1 · order · b1-tenses-1.csv:82

Task: Put the words in order.
word_cards: had | you | didn't | you | why | your | tell | that | me | job | lost
Key: {"kind": "order", "sentence": "why didn't you tell me that you had lost your job", "also": []}
- reader 1: instruction: No instruction hint; fine.
- reader 1: level: Past perfect plus 11 words is more B1.2.
- reader 2: another correct answer, not accepted: [["why didn't you tell me that you had lost your job"]]
- reader 2: instruction: No punctuation/question mark cue; fine.

## r21-6-031 · B1.1 · order · b1-tenses-1.csv:83

Task: Put the words in order.
word_cards: audience | so | early | boring | half | that | the | the | left | of | was | film
Key: {"kind": "order", "sentence": "the film was so boring that half of the audience left early", "also": []}
- reader 1: level: so...that and 12 words is B1.2 rather than B1.1.
- reader 2: another correct answer, not accepted: [['so boring was the film that half of the audience left early']]
- reader 2: level: Twelve cards with so...that is long but OK.

## r21-6-033 · B1.1 · gap · b1-tenses-1.csv:96

Task: How long ___ you ___ for the bus yesterday? (wait)
Key: {"kind": "gap", "accepted": [["did"], ["wait"]]}
- reader 1: another correct answer, not accepted: [['were', 'waiting']]
- reader 1: instruction: Both past simple and past continuous fit; no hint.
- reader 2: answer not accepted: ['were', 'waiting']
- reader 2: instruction: Both past continuous and past simple are correct; '(wait)' gives no form.
- the readers disagree

## r21-6-034 · B1.1 · order · b1-tenses-2.csv:2

Task: Put the words in order.
word_cards: in | i | city | i | a | this | lived | have | since | child | was
Key: {"kind": "order", "sentence": "i have lived in this city since i was a child", "also": ["since i was a child i have lived in this city"]}
- reader 2: another correct answer, not accepted: [['since i was a child i have lived in this city']]

## r21-6-037 · B1.1 · gap · b1-tenses-2.csv:20

Task: How long ___ you ___ for this company? (work)
Key: {"kind": "gap", "accepted": [["have"], ["worked", "been working"]]}
- reader 1: another correct answer, not accepted: [['did', 'work']]
- reader 1: instruction: Tense not fixed; 'did ... work' fits a past job.
- reader 2: another correct answer, not accepted: [['did', 'work']]
- reader 2: instruction: '(work)' allows present perfect simple and continuous; 'did you work' also if he left (less natural).

## r21-6-039 · B1.1 · text · b1-tenses-2.csv:55

Task: Make a question with How long: She has been learning Chinese.
Key: {"kind": "text", "accepted": [["How long has she been learning Chinese?"]]}
- reader 1: another correct answer, not accepted: ['How long has she learned Chinese?', 'How long has she been learning Chinese for?']
- reader 1: instruction: Almost only reordering/copying; easy.
- reader 2: another correct answer, not accepted: ['How long has she been learning Chinese for?', 'How long has she learned Chinese?', 'How long has she learnt Chinese?']
- reader 2: instruction: Statement is already in present perfect continuous; only a word swap needed (nearly copying), easy.

## r21-6-040 · B1.1 · mcq · b1-tenses-2.csv:62

Task: Which sentence says how long?
options: I've learned some French at school. | I've been learning French for two years. | I learned French at school in Riga. | I'm learning French with a teacher.
Key: {"kind": "mcq", "correct": "I've been learning French for two years.", "wrong": ["I've learned some French at school.", "I learned French at school in Riga.", "I'm learning French with a teacher."]}
- reader 2: instruction: 'Which sentence says how long?' is unnatural wording; 'duration' unclear.

## r21-6-042 · B1.2 · order · b1-tenses-2.csv:112

Task: Put the words in order.
word_cards: it | if | we | come | to | snows | be | heavily | able | won't
Key: {"kind": "order", "sentence": "we won't be able to come if it snows heavily", "also": ["if it snows heavily we won't be able to come"]}
- reader 2: another correct answer, not accepted: [["if it snows heavily we won't be able to come"], ["if it snows heavily, we won't be able to come"]]

## r21-6-044 · B1.1 · gap · b1-upgrades-1.csv:34

Task: The cheese ___ in small villages and then ___ to shops around the country. (make / send)
Key: {"kind": "gap", "accepted": [["is made"], ["is sent"]]}
- reader 1: answer not accepted: ['is made', 'sent']
- reader 1: another correct answer, not accepted: [['was made', 'was sent'], ['was made', 'sent']]
- reader 1: instruction: No time context: present and past both fit.
- reader 2: answer not accepted: ['is made', 'sent']
- reader 2: another correct answer, not accepted: [['was made', 'sent'], ['was made', 'was sent'], ['are made', 'sent']]
- reader 2: instruction: Tense and voice not given; present and past both fit, 'is sent' vs 'sent' (and 'is then sent' would not fit).

## r21-6-045 · B1.1 · mcq · b1-upgrades-1.csv:39

Task: Choose the correct option: The new library ___ , so you can borrow books from tomorrow.
options: has been opened | have been opened | is opened | has open
Key: {"kind": "mcq", "correct": "has been opened", "wrong": ["has open", "is opened", "have been opened"]}
- reader 1: instruction: 'Choose the correct option:' is redundant.
- reader 1: sense: 'has been opened' with 'from tomorrow' is logically odd (opening already happened, borrowing starts tomorrow); 'will be opened' / 'opens tomorrow' expected.
- reader 2: sense: Logic problem: if the library has already been opened, 'from tomorrow' is odd; 'will be opened' is missing. 'has been opened' also sounds like a ceremony (natural: 'has opened').

## r21-6-046 · B1.2 · gap · b1-upgrades-1.csv:46

Task: Unless you ___ harder, you won't pass the final exam. (study)
Key: {"kind": "gap", "accepted": [["study"]]}
- reader 2: another correct answer, not accepted: [['are studying']]
- reader 2: instruction: 'are studying harder' possible but unnatural.

## r21-6-047 · B1.1 · order · compare-past-1.csv:16

Task: Put all the words in order. More than one answer is possible.
word_cards: i | phone | was | a | rang | the | shower | while | having
Key: {"kind": "order", "sentence": "the phone rang while i was having a shower", "also": ["while i was having a shower the phone rang"]}
- reader 1: another correct answer, not accepted: ['i was having a shower while the phone rang', 'while the phone rang i was having a shower (less natural)']
- reader 2: another correct answer, not accepted: [['i was having a shower while the phone rang'], ['while i was having a shower the phone rang'], ['while the phone rang i was having a shower']]
- reader 2: level: Nine cards, very easy for B1.1 (A2-level).

## r21-6-048 · B1.1 · gap · compare-past-1.csv:30

Task: It ___ this week. Everything is very dry. (not / rain)
Key: {"kind": "gap", "accepted": [["hasn't rained", "has not rained"]]}
- reader 1: another correct answer, not accepted: [["hasn't been raining"], ['has not been raining']]
- reader 2: another correct answer, not accepted: [["hasn't been raining"], ['has not been raining']]
- reader 2: instruction: '(not / rain)' gives no form; contraction/full form both count.

## r21-6-050 · B1.2 · gap · compare-past-1.csv:38

Task: I got up and ___ out of the window. The sun ___. (look / shine)
Key: {"kind": "gap", "accepted": [["looked"], ["was shining", "shone"]]}
- reader 1: instruction: 'shone' is possible, less natural for a background description.
- reader 2: instruction: Gap 2: 'was shining' and 'shone' both fit; no cue for tense.

## r21-6-051 · B1.1 · gap · compare-past-1.csv:40

Task: A: Was Tom there when you arrived? B: No, he ___. (already / leave)
Key: {"kind": "gap", "accepted": [["had already left"]]}
- reader 1: another correct answer, not accepted: [['had left already']]
- reader 2: another correct answer, not accepted: [["'d already left"], ['had left already'], ['had not left']]
- reader 2: instruction: 'already' placement: 'had already left' and 'had left already' both correct; 'was already gone' not allowed.

## r21-6-052 · B1.1 · mcq · comparison-1.csv:29

Task: Choose the correct option: Travelling by train is a bit ___ than driving, but it is more relaxing.
options: the slower | more slow | slower | slowest
Key: {"kind": "mcq", "correct": "slower", "wrong": ["more slow", "slowest", "the slower"]}
- reader 1: level: Comparatives are A2, too easy for B1.1.
- reader 2: level: Simple comparative is A2, too easy for B1.1.

## r21-6-053 · B1.1 · gap · comparison-1.csv:34

Task: Prices in the city centre are far ___ than in the suburbs. (high)
Key: {"kind": "gap", "accepted": [["higher"]]}
- reader 1: level: Basic comparative, A2.
- reader 2: level: Simple comparative with 'far' is A2.

## r21-6-054 · B1.2 · order · comparison-1.csv:50

Task: Put the words in order.
word_cards: get | better | the | the | more | practise | you | you
Key: {"kind": "order", "sentence": "the more you practise the better you get", "also": []}
- reader 1: another correct answer, not accepted: ['the better you get the more you practise']
- reader 2: another correct answer, not accepted: [['the better you get the more you practise']]
- reader 2: instruction: Second order is grammatical but means the opposite relation; 'get better' collocation tempting.

## r21-6-056 · B1.1 · order · learn-drag-4.csv:11

Task: Put all the words in order. More than one answer is possible.
word_cards: yesterday | you | see | Anna | did
Key: {"kind": "order", "sentence": "did you see Anna yesterday", "also": ["did Anna see you yesterday"]}
- reader 1: another correct answer, not accepted: ['yesterday did you see Anna (less natural)']
- reader 1: level: A1/A2 question word order; too easy for B1.1. Only five cards.
- reader 2: another correct answer, not accepted: [['did anna see you yesterday'], ['yesterday did you see anna'], ['yesterday did anna see you']]
- reader 2: instruction: Only five cards; too easy. Two natural answers (Anna as subject or object) — instruction admits more than one.
- reader 2: level: A2 level, not B1.1.

## r21-6-058 · B1.2 · gap · said-told-1.csv:5

Task: Complete with *said* or *told*: Our manager ___ us the office would close at four.
Key: {"kind": "gap", "accepted": [["told"]]}
- reader 1: instruction: Raw asterisks around said/told show in the text; two-choice gap is easy.
- reader 2: instruction: Markdown asterisks around said/told show in the text. The answer is only 'told' (with an object 'us').

## r21-6-059 · B1.2 · gap · twins-2.csv:5

Task: Write one word in each gap: I missed the first minute of the lesson. It ___ just ___ when I joined. (start)
Key: {"kind": "gap", "accepted": [["had"], ["started"]]}
- reader 1: another correct answer, not accepted: [['was', 'starting']]
- reader 2: another correct answer, not accepted: [['was', 'starting']]
- reader 2: instruction: 'It was just starting' also correct; 'Write one word' fine.

