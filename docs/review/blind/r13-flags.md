# Blind check r13: flags for the judge

152 tasks, 2 readers.

## r13-002 · A2.1 · gap · zz-blind-gap-fill-a2-1.csv:3

Task: My dad loves ___ old films. (watch)
Key: {"kind": "gap", "accepted": [["watching", "to watch"]]}
- reader 2: instruction: Brackets give only the verb, so both -ing and to + verb are correct (loves watching / loves to watch).

## r13-003 · A2.1 · order · zz-blind-gap-fill-a2-1.csv:4

Task: Put the words in order to make a question.
word_cards: come | us | want | to | do | with | you
Key: {"kind": "order", "sentence": "do you want to come with us", "also": []}
- reader 1: another correct answer, not accepted: [['do you want us to come with you']]
- reader 1: instruction: Cards allow a second question with a different meaning (us to come with you).
- reader 2: another correct answer, not accepted: ['do you want us to come with you']
- reader 2: sense: Second order is correct English with a different meaning (you invite us).

## r13-007 · A2.1 · gap · zz-blind-gap-fill-a2-1.csv:8

Task: Does your partner like ___ computer games? (play)
Key: {"kind": "gap", "accepted": [["playing", "to play"]]}
- reader 2: instruction: Both -ing and to + verb are correct after like; brackets do not restrict.

## r13-009 · A2.1 · text · zz-blind-gap-fill-a2-1.csv:10

Task: Say it another way with *love*: Cooking is my favourite hobby.
Key: {"kind": "text", "accepted": [["I love cooking.", "I love to cook.", "I really love cooking.", "I really love to cook.", "I love cooking very much."]]}
- reader 1: instruction: Open: subject not given (I / my brother...), so many sentences are right.
- reader 2: instruction: Subject is not given; 'My sister loves cooking' etc. are also possible.

## r13-018 · A2.1 · text · zz-blind-gap-fill-a2-1.csv:19

Task: Start with *Two*: The bus is late.
Key: {"kind": "text", "accepted": [["Two buses are late.", "Two busses are late."]]}
- reader 1: instruction: Starting word nearly gives the plural.
- reader 2: another correct answer, not accepted: ['The two buses are late.']

## r13-021 · A2.1 · gap · zz-blind-gap-fill-a2-1.csv:22

Task: Use the words in brackets: I need two ___ for the trip. (bag / big)
Key: {"kind": "gap", "accepted": [["big bags"]]}
- reader 1: instruction: One gap needs two words; say so.
- reader 2: instruction: Order of the two bracket words not stated: learner must know to put adjective first and make plural; acceptable but slightly unclear.

## r13-024 · A2.1 · gap · zz-blind-gap-fill-a2-1.csv:25

Task: Use the words in brackets: My new headphones ___. (comfortable / very / be)
Key: {"kind": "gap", "accepted": [["are very comfortable"]]}
- reader 1: another correct answer, not accepted: [['were very comfortable'], ['are really comfortable']]
- reader 1: instruction: Tense not given: 'were' also correct; one gap needs three words.
- reader 2: instruction: Three bracket words in one gap: unclear that all must be used and in which order.

## r13-025 · A2.1 · order · zz-blind-gap-fill-a2-1.csv:26

Task: Put the words in order.
word_cards: age | her | active | grandmother | for | is | very | my
Key: {"kind": "order", "sentence": "my grandmother is very active for her age", "also": ["for her age my grandmother is very active"]}
- reader 1: level: 'very active for her age' is a B1 idiom.

## r13-027 · A2.1 · text · zz-blind-gap-fill-a2-1.csv:28

Task: Start with *Our*: We have very nice neighbours.
Key: {"kind": "text", "accepted": [["Our neighbours are very nice.", "Our neighbours are nice."]]}
- reader 1: another correct answer, not accepted: ['Our neighbours are really nice.']
- reader 2: another correct answer, not accepted: ['Our neighbours are really nice.']
- reader 2: instruction: Start-with only fixes 'Our'; result needs 'are very nice', fine. Learner may also write 'Our neighbours are very nice' only.

## r13-028 · A2.1 · mcq · zz-blind-gap-fill-a2-1.csv:29

Task: Choose the correct option: What time ___ you usually finish work?
options: are | do | —
Key: {"kind": "mcq", "correct": "do", "wrong": ["are", "—"]}
- reader 1: sense: Option '—' cannot fit; not a believable mistake.

## r13-030 · A2.1 · order · zz-blind-gap-fill-a2-1.csv:31

Task: Put the words in order.
word_cards: she | is | usually | she | running | but | swims | today
Key: {"kind": "order", "sentence": "she usually swims but today she is running", "also": ["usually she swims but today she is running", "she usually swims but she is running today", "today she is running but she usually swims", "she is running today but she usually swims"]}
- reader 1: instruction: No hint of word order or meaning; several equally good sentences.
- reader 2: another correct answer, not accepted: ['today she is running but usually she swims']
- reader 2: sense: Card list has 'she' twice; first order of the cards that is grammatical is not unique (several orders).

## r13-032 · A2.1 · gap · zz-blind-gap-fill-a2-1.csv:33

Task: Look! Dad ___ the dishes. He never ___ that! (wash / do)
Key: {"kind": "gap", "accepted": [["is washing", "'s washing"], ["does"]]}
- reader 2: another correct answer, not accepted: [['is washing', 'is doing']]
- reader 2: instruction: Brackets order wash / do matches gaps; ok.

## r13-036 · A2.1 · gap · zz-blind-gap-fill-a2-1.csv:37

Task: The shops ___ busy yesterday.
word_cards: wasn't | weren't | didn't
Key: {"kind": "gap", "accepted": [["weren't"]]}
- reader 2: instruction: Cards weren't/wasn't/didn't; wasn't wrong; no issue.

## r13-045 · A2.1 · text · zz-blind-gap-fill-a2-1.csv:46

Task: Say it another way with *a few* or *a little*: There are three or four cafés near my office.
Key: {"kind": "text", "accepted": [["There are a few cafés near my office.", "Near my office there are a few cafés.", "There are a few cafes near my office.", "Near my office there are a few cafes."]]}
- reader 1: another correct answer, not accepted: ['A few cafés are near my office.']

## r13-047 · A2.1 · gap · zz-blind-gap-fill-a2-1.csv:48

Task: There was ___ wallet on my seat on the bus. ___ wallet was empty.
word_cards: a | A | The | the
Key: {"kind": "gap", "accepted": [["a"], ["The"]]}
- reader 2: sense: Capital/lower-case duplicate cards (A/a, The/the) make the gap 2 capital the only clue; fine but cards 'A' and 'the' are not believable mistakes.

## r13-050 · A2.1 · text · zz-blind-gap-fill-a2-1.csv:51

Task: Correct the mistake: I bought a new laptop. A laptop is very fast.
Key: {"kind": "text", "accepted": [["I bought a new laptop. The laptop is very fast.", "I bought a new laptop. It is very fast.", "I bought a new laptop. It's very fast."]]}
- reader 2: instruction: Which part to fix is not clear; 'It is very fast' also corrects it.

## r13-052 · A2.1 · mcq · zz-blind-gap-fill-a2-1.csv:53

Task: Choose the correct option: Are you free ___ this weekend?
options: in | at | on | —
Key: {"kind": "mcq", "correct": "—", "wrong": ["at", "on", "in"]}
- reader 1: sense: '—' as an option is unnatural for a learner; 'on this weekend' is heard in American English only.
- reader 2: sense: Fine in British English; 'on this weekend' not natural either way.

## r13-053 · A2.1 · gap · zz-blind-gap-fill-a2-1.csv:54

Task: I check my email ___ every morning.
word_cards: — | in
Key: {"kind": "gap", "accepted": [["—"]]}
- reader 1: sense: A dash card for 'nothing' may confuse.

## r13-054 · A2.1 · gap · zz-blind-gap-fill-a2-1.csv:55

Task: The new gym opens ___ tomorrow.
word_cards: on | — | in
Key: {"kind": "gap", "accepted": [["—"]]}
- reader 1: sense: A dash card for 'nothing' may confuse.

## r13-059 · A2.2 · mcq · zz-blind-gap-fill-a2-1.csv:60

Task: Choose the correct option: I've ___ to the gym. I feel great now.
options: gone | been | went
Key: {"kind": "mcq", "correct": "been", "wrong": ["gone", "went"]}
- reader 2: a wrong option that fits: gone is wrong here (I have gone = still there)

## r13-062 · A2.2 · gap · zz-blind-gap-fill-a2-1.csv:63

Task: Write *been* or *gone*: Dan's ___ to a football match. He'll be back at ten.
Key: {"kind": "gap", "accepted": [["gone"]]}
- reader 2: sense: Note: 'been' would contradict 'He'll be back at ten'; make sure key says gone.

## r13-067 · A2.2 · text · zz-blind-gap-fill-a2-1.csv:68

Task: Start with *Rita has* and use *go*: Rita went to Tokyo, and she is still there.
Key: {"kind": "text", "accepted": [["Rita has gone to Tokyo.", "Rita has gone to Tokyo, and she is still there.", "Rita has gone to Tokyo and is still there."]]}
- reader 1: instruction: 'use go' plus 'Rita has' gives the answer away.

## r13-071 · A2.2 · order · zz-blind-gap-fill-a2-1.csv:72

Task: Put the words in order to make a question.
word_cards: advice | piece | a | can | i | you | of | give
Key: {"kind": "order", "sentence": "can i give you a piece of advice", "also": []}
- reader 2: level: Eight cards, A2.2 ok.

## r13-072 · A2.2 · gap · zz-blind-gap-fill-a2-1.csv:73

Task: My ___ ___ still at the airport.
word_cards: luggages | are | luggage | is
Key: {"kind": "gap", "accepted": [["luggage"], ["is"]]}
- reader 2: sense: Cards luggages/are form a believable plural mistake; ok.

## r13-074 · A2.2 · gap · zz-blind-gap-fill-a2-1.csv:75

Task: Thank you! Your advice about the exam ___ really helpful. (be)
Key: {"kind": "gap", "accepted": [["is", "was", "has been", "will be"]]}
- reader 1: another correct answer, not accepted: [["'s"]]
- reader 1: instruction: Tense not given: present and past both fine.
- reader 2: instruction: No time clue: was, has been and is are all correct.

## r13-084 · A2.2 · gap · zz-blind-gap-fill-a2-1.csv:85

Task: Write one word in each gap: At airport security, take your laptop ___ ___ your bag.
Key: {"kind": "gap", "accepted": [["out"], ["of"]]}
- reader 2: level: 'out of' two-word preposition phrase at airport security is a little hard for A2.2; ok.

## r13-085 · A2.2 · text · zz-blind-gap-fill-a2-1.csv:86

Task: Correct the mistake: What time did you get to home last night?
Key: {"kind": "text", "accepted": [["What time did you get home last night?"]]}
- reader 1: another correct answer, not accepted: ['What time did you arrive home last night?']
- reader 2: another correct answer, not accepted: ['What time did you arrive home last night?', 'What time did you get to your home last night?']

## r13-088 · A2.2 · order · zz-blind-gap-fill-a2-1.csv:89

Task: Put the words in order.
word_cards: new | my | like | very | flat | i | much
Key: {"kind": "order", "sentence": "i like my new flat very much", "also": ["i very much like my new flat"]}
- reader 2: sense: Second order is correct but formal/less natural.

## r13-090 · A2.2 · gap · zz-blind-gap-fill-a2-1.csv:91

Task: Complete with one word: My grandmother loves her garden very ___.
Key: {"kind": "gap", "accepted": [["much"]]}
- reader 2: instruction: 'Complete with one word' - 'well' also possible? No; only much. Fine.

## r13-100 · A2.2 · gap · zz-blind-gap-fill-a2-1.csv:101

Task: Of all my colleagues, Anna lives ___ from the office. (far)
Key: {"kind": "gap", "accepted": [["the furthest", "the farthest", "furthest", "farthest"]]}
- reader 2: instruction: Unclear whether 'the' is inside the gap ('lives furthest from' and 'lives the furthest from' are both correct); furthest/farthest both correct.

## r13-105 · A2.2 · order · zz-blind-gap-fill-a2-1.csv:106

Task: Put the words in order.
word_cards: i | i | much | was | run | younger | when | could | faster
Key: {"kind": "order", "sentence": "when i was younger i could run much faster", "also": ["i could run much faster when i was younger"]}
- reader 2: sense: Two 'i' cards; fine.

## r13-111 · A2.2 · gap · zz-blind-gap-fill-a2-1.csv:112

Task: My glasses are ___ in this room. Can you help me look?
word_cards: anywhere | somewhere | something
Key: {"kind": "gap", "accepted": [["somewhere"]]}
- reader 2: a wrong option that fits: anywhere is wrong in an affirmative statement; fine
- reader 2: sense: Distractor 'something' is not the same kind of word (believable mistake only partly).

## r13-113 · A2.2 · gap · zz-blind-gap-fill-a2-1.csv:114

Task: Complete with a word like *someone, anything, nowhere*: ___ works here on Sundays. The office is closed.
Key: {"kind": "gap", "accepted": [["Nobody", "No one"]]}
- reader 2: another correct answer, not accepted: [['No-one']]
- reader 2: instruction: Examples (someone, anything, nowhere) are given, which hints at the word family but not the answer.

## r13-115 · A2.2 · text · zz-blind-gap-fill-a2-1.csv:116

Task: Make it negative: I bought something for Anna.
Key: {"kind": "text", "accepted": [["I didn't buy anything for Anna.", "I didn't buy Anna anything.", "I bought nothing for Anna."]]}
- reader 2: sense: Last is correct but less natural.

## r13-116 · A2.2 · mcq · zz-blind-gap-fill-a2-1.csv:117

Task: Choose the correct option: My sister loves swimming and ___.
options: to cycle | cycling | cycle
Key: {"kind": "mcq", "correct": "cycling", "wrong": ["cycle", "to cycle"]}
- reader 1: sense: 'to cycle' is awkward after 'swimming and', not correct.

## r13-121 · A2.2 · gap · zz-blind-gap-fill-a2-1.csv:122

Task: The best parts of my job are meeting people and ___. (travel)
Key: {"kind": "gap", "accepted": [["travelling", "traveling"]]}
- reader 2: sense: traveling is American spelling, also correct.

## r13-122 · A2.2 · text · zz-blind-gap-fill-a2-1.csv:123

Task: Correct the mistake: She closed her laptop and go home.
Key: {"kind": "text", "accepted": [["She closed her laptop and went home.", "She closed her laptop and she went home.", "She closes her laptop and goes home.", "She closes her laptop and she goes home."]]}
- reader 1: instruction: Correction could be past or present; tense not fixed.
- reader 2: instruction: Learner may change the tense of both verbs; both are correct.

## r13-126 · A2.2 · gap · zz-blind-gap-fill-a2-1.csv:127

Task: I met an old friend ___ the tram yesterday.
word_cards: on | at | in
Key: {"kind": "gap", "accepted": [["on"]]}
- reader 1: a wrong option that fits: 'in' is possible for some speakers (in the tram) but 'on' is standard.

## r13-128 · A2.2 · gap · zz-blind-gap-fill-a2-1.csv:129

Task: Write the missing word: We went to the airport ___ a taxi.
Key: {"kind": "gap", "accepted": [["in"]]}
- reader 2: instruction: 'by' is a believable answer for a learner, but 'by a taxi' is wrong; the gap fits only 'in' (note: with 'by' it would need 'taxi' without 'a').

## r13-134 · A2.2 · gap · zz-blind-gap-fill-a2-1.csv:135

Task: Why did you call the hotel? I called ___ a room. (book)
Key: {"kind": "gap", "accepted": [["to book", "in order to book", "so as to book"]]}
- reader 2: instruction: Whether 'to' is part of the gap is not clear; 'I called to book a room' needs the word 'to' in the answer.

## r13-136 · A2.2 · mcq · zz-blind-gap-fill-a2-1.csv:137

Task: Which sentence has a mistake?
options: Our kitchen chairs were made from my uncle. | The museum is visited by thousands of tourists. | Breakfast is served from seven to ten. | My grandmother was born in a small town.
Key: {"kind": "mcq", "correct": "Our kitchen chairs were made from my uncle.", "wrong": ["Breakfast is served from seven to ten.", "My grandmother was born in a small town.", "The museum is visited by thousands of tourists."]}
- reader 1: level: Passive is B1 rather than A2.2.

## r13-137 · A2.2 · gap · zz-blind-gap-fill-a2-1.csv:138

Task: Complete with one word: Our hotel is owned ___ a Swedish company.
Key: {"kind": "gap", "accepted": [["by"]]}
- reader 1: level: Passive is B1 rather than A2.2.

## r13-138 · A2.2 · gap · zz-blind-gap-fill-a2-1.csv:139

Task: In our village, the bread is baked ___ a local family.
word_cards: of | by | from
Key: {"kind": "gap", "accepted": [["by"]]}
- reader 1: level: Passive is B1 rather than A2.2.

## r13-139 · A2.2 · gap · zz-blind-gap-fill-a2-1.csv:140

Task: The windows of our office ___ ___ a small company every month. (clean)
Key: {"kind": "gap", "accepted": [["are cleaned", "get cleaned"], ["by"]]}
- reader 1: instruction: Two gaps but three words needed (are cleaned by); 'are'+'cleaned' leaves 'by' missing. Split of gaps unclear.
- reader 1: level: Passive is B1 rather than A2.2.
- reader 2: another correct answer, not accepted: [['are', 'cleaned by']]
- reader 2: instruction: Unclear how the words split over the two gaps: 'are cleaned' + 'by' (three words in two gaps).

## r13-140 · A2.2 · text · zz-blind-gap-fill-a2-1.csv:141

Task: Start with *This bridge*: A Latvian engineer designed this bridge.
Key: {"kind": "text", "accepted": [["This bridge was designed by a Latvian engineer."]]}
- reader 1: level: Passive is B1 rather than A2.2.

## r13-144 · A2.2 · text · zz-blind-gap-fill-a2-1.csv:145

Task: Start with *These trousers*: This shirt is too expensive.
Key: {"kind": "text", "accepted": [["These trousers are too expensive."]]}
- reader 1: another correct answer, not accepted: ['These trousers are too expensive for me.']
- reader 1: instruction: Shirt becomes trousers: not a real rewrite, meaning changes.
- reader 2: instruction: Not a rewrite of the same sentence: the learner must replace 'shirt' with 'trousers'; unclear what to do, and meaning changes.
- reader 2: sense: Task is a substitution, not a paraphrase.

## r13-148 · A2.2 · gap · zz-blind-gap-fill-a2-1.csv:149

Task: Complete with *will* or *going to*: 'Did you reply to Mark's email?' 'Oh no, I forgot! I ___ to him now.' (write)
Key: {"kind": "gap", "accepted": [["'ll write", "will write"]]}
- reader 2: another correct answer, not accepted: [['am going to write'], ["'m going to write"]]
- reader 2: instruction: Instruction gives the choice but 'going to' is also acceptable for an immediate intention; 'will' is the more natural.

## r13-149 · A2.2 · gap · zz-blind-gap-fill-a2-1.csv:150

Task: Complete with *will* or *going to*: 'Why are you saving so much money?' 'I ___ a flat next year.' (buy)
Key: {"kind": "gap", "accepted": [["'m going to buy", "am going to buy"]]}
- reader 1: instruction: 'will buy' is wrong here (plan); 'I'm buying' also right but excluded.
- reader 2: instruction: 'will buy' also possible as a prediction/promise but less natural.

## r13-152 · A2.2 · text · zz-blind-gap-fill-a2-1.csv:153

Task: Say it another way with *discuss*: We talked about the new timetable at the meeting.
Key: {"kind": "text", "accepted": [["We discussed the new timetable at the meeting.", "We discussed the new timetable in the meeting."]]}
- reader 1: level: 'discuss' is slightly above A2.
- reader 2: another correct answer, not accepted: ['At the meeting we discussed the new timetable.']

