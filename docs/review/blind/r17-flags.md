# Blind check r17: flags for the judge

56 tasks, 2 readers.

## r17-001 · A2.2 · mcq · built-in

Task: Why do we say 'Tickets are sold here'?
options: Someone is selling tickets right now. | We want to say who sells the tickets. | The sentence is about the past. | The action matters, not who sells them.
Key: {"kind": "mcq", "correct": "The action matters, not who sells them.", "wrong": ["Someone is selling tickets right now.", "We want to say who sells the tickets.", "The sentence is about the past."]}
- reader 1: level: Metalinguistic question about passive purpose is abstract for A2.2.
- reader 2: a wrong option that fits: 'Someone is selling tickets right now.' is also true: the sentence is present simple passive, and someone does sell them here.
- reader 2: instruction: 'Why do we say' is vague; option 1 is not clearly wrong.

## r17-002 · B1.2 · match · built-in

Task: Match each sentence with its meaning.
left: If I had a car, I would drive to work. | If I had had a car, I would have driven to work. | If I borrow my dad's car, I get to work in ten minutes. | If the trains are on strike tomorrow, I'll borrow my dad's car.
right: It is possible in the future. | I have no car. | This is what usually happens. | I had no car then.
Key: {"kind": "match", "pairs": [["If I had a car, I would drive to work.", "I have no car."], ["If I had had a car, I would have driven to work.", "I had no car then."], ["If I borrow my dad's car, I get to work in ten minutes.", "This is what usually happens."], ["If the trains are on strike tomorrow, I'll borrow my dad's car.", "It is possible in the future."]]}
- reader 1: level: Third conditional is hard for B1.2 but acceptable.

## r17-003 · B2.1 · gap · built-in

Task: 'You must finish by Friday.' → My boss told me ___.
Key: {"kind": "gap", "accepted": [["I had to finish by Friday", "that I had to finish by Friday", "I must finish by Friday", "that I must finish by Friday", "I would have to finish by Friday", "that I would have to finish by Friday", "to finish by Friday"]]}
- reader 1: answer not accepted: ['(that) I had to finish by Friday']
- reader 1: instruction: Several correct reports (had to / must if still true / told me to finish); instruction does not say how many words or which structure.
- reader 2: another correct answer, not accepted: [['I should finish by Friday'], ['that I should finish by Friday']]
- reader 2: instruction: Open gap: reported 'told me to finish' and 'told me (that) I had to / must finish' are all correct; nothing says which form is wanted.
- the readers disagree

## r17-009 · B1.2 · mcq · built-in

Task: Choose the correct option: Could you tell me where ___ ?
options: you have bought that jacket | you bought that jacket | did you buy that jacket | did you bought that jacket
Key: {"kind": "mcq", "correct": "you bought that jacket", "wrong": ["did you buy that jacket", "did you bought that jacket", "you have bought that jacket"]}
- reader 1: a wrong option that fits: you have bought that jacket (grammatical, but less natural; present perfect with 'where' for a one-off purchase is odd, may be accepted by some)
- reader 2: a wrong option that fits: 'you have bought that jacket' is grammatical (present perfect), only less natural with 'where'.
- reader 2: sense: Option 1 is arguably correct English.

## r17-011 · B1.2 · write · built-in

Task: Last week you emailed your landlord about the broken heater in your flat, but he hasn't answered. Write him one polite question. Start with *Could you tell me* or *I'd like to know*.
Key: {"kind": "write", "model": "Could you tell me if you got my email about the heater?", "must": ["A polite start: *Could you tell me …?* / *I'd like to know …*", "Then *if* or a question word: *… if you got my email*, *… when someone can repair the heater*.", "After *if* or the question word the subject comes first, with no *did*: *if you got my email*, *when the heater will be repaired*."]}
- reader 1: instruction: Task does not say what to ask (when fixed or whether he got the email): many correct answers; checker may reject valid ones.

## r17-012 · B2.2 · write · built-in

Task: Write a sentence that starts with *The question is whether*, *The question is how* or *The question is why*.
Key: {"kind": "write", "model": "The question is whether we can afford the delay.", "must": ["*Questions is* does not agree: one question, so *The question is*.", "Start with *The question is*.", "After *The question is* put *whether*, *how*, *why* or another question word.", "After *how*, *why* or *whether* use statement word order: *how we can…*, not *how can we…*."]}
- reader 1: instruction: No situation or content given: any sentence with the opening is correct; unclear what is being tested.
- reader 2: instruction: Open task with no topic; fine but any sentence with the starter works.

## r17-018 · B1.1 · order · b1-new-4.csv:139

Task: Put the words in order.
word_cards: you | could | salt | the | pass | me | please
Key: {"kind": "order", "sentence": "could you pass me the salt please", "also": ["could you please pass me the salt", "please could you pass me the salt", "you could pass me the salt please"]}
- reader 2: another correct answer, not accepted: [['please could you pass me the salt'], ['could you please pass me the salt']]

## r17-019 · B1.1 · order · b1-tenses-1.csv:6

Task: Put the words in order.
word_cards: lunch | me | usually | drink | it | don't | keeps | after | coffee | because | i | awake
Key: {"kind": "order", "sentence": "i don't usually drink coffee after lunch because it keeps me awake", "also": ["because it keeps me awake i don't usually drink coffee after lunch", "i usually don't drink coffee after lunch because it keeps me awake", "because it keeps me awake i usually don't drink coffee after lunch", "usually i don't drink coffee after lunch because it keeps me awake"]}
- reader 1: another correct answer, not accepted: ["after lunch i don't usually drink coffee because it keeps me awake", "i don't usually drink coffee because it keeps me awake after lunch", "after lunch i usually don't drink coffee because it keeps me awake"]
- reader 1: instruction: Many correct orders (adverb and clause position).
- reader 1: level: 12 cards is long for B1.1.
- reader 2: another correct answer, not accepted: [["usually i don't drink coffee after lunch because it keeps me awake"], ["i usually don't drink coffee after lunch because it keeps me awake"], ["after lunch i don't usually drink coffee because it keeps me awake"], ["after lunch i usually don't drink coffee because it keeps me awake"], ["because it keeps me awake i don't usually drink coffee after lunch"], ["because it keeps me awake i usually don't drink coffee after lunch"], ["i don't usually drink coffee because it keeps me awake after lunch (odd meaning)"]]
- reader 2: level: 12 cards is too long for B1.1 (about 5-9 words); many valid orders.

## r17-020 · B1.1 · order · b1-tenses-1.csv:8

Task: Put the words in order.
word_cards: day | newspaper | news | never | but | the | a | they | parents | read | watch | every | my
Key: {"kind": "order", "sentence": "my parents never watch the news but they read a newspaper every day", "also": ["my parents read a newspaper every day but they never watch the news", "every day my parents read a newspaper but they never watch the news", "my parents never watch the news but every day they read a newspaper"]}
- reader 1: answer not accepted: my parents never read a newspaper but they watch the news every day
- reader 1: another correct answer, not accepted: ['my parents watch the news every day but they never read a newspaper', 'every day my parents watch the news but they never read a newspaper']
- reader 1: instruction: Meaning is not given, so both halves can swap; many correct orders.
- reader 1: level: 13 cards is too long for B1.1.
- reader 2: another correct answer, not accepted: [['every day my parents read a newspaper but they never watch the news'], ['my parents never read a newspaper but they watch the news every day'], ['my parents never read a newspaper but every day they watch the news'], ['every day my parents watch the news but they never read a newspaper'], ['my parents watch the news every day but they never read a newspaper']]
- reader 2: level: 13 cards is far too long for B1.1; several orders with different but correct meaning.
- the readers disagree

## r17-022 · B2.2 · gap · compare-past-1.csv:57

Task: By the time he retired, he ___ the same car for thirty years. (have)
Key: {"kind": "gap", "accepted": [["had had", "'d had"]]}
- reader 1: answer not accepted: [['had had']]
- reader 1: sense: Fine; 'had been having' is not natural.
- reader 2: level: Fine for B2.2 but 'had had' is hard to type; no problem otherwise.
- the readers disagree

## r17-023 · B2.2 · text · compare-past-1.csv:59

Task: Correct the mistake: When she sold the café, she had been owning it since 2010.
Key: {"kind": "text", "accepted": [["When she sold the café, she had owned it since 2010.", "When she sold the café, she'd owned it since 2010.", "she had owned it since 2010 when she sold the café.", "she'd owned it since 2010 when she sold the café."]]}
- reader 1: another correct answer, not accepted: ['When she sold the café, she had had it since 2010.', 'When she sold the café, she had owned it for years.']
- reader 1: sense: 'had owned it since 2010' is odd with a sale date unspecified; a 'for' period reads more naturally. Instruction does not say what to change.
- reader 2: another correct answer, not accepted: [['When she sold the café, she had had it since 2010.']]
- reader 2: instruction: Does not say which part is wrong; 'since 2010' with past perfect is fine, learner may also change 'since' to a 'for' phrase, but no number given.

## r17-024 · A2.2 · order · comparison-1.csv:26

Task: Put the words in order.
word_cards: than | one | that | cheaper | jacket | this | is
Key: {"kind": "order", "sentence": "this jacket is cheaper than that one", "also": ["that jacket is cheaper than this one"]}
- reader 1: instruction: Direction of comparison not given: both orders correct.
- reader 2: another correct answer, not accepted: [['that jacket is cheaper than this one']]
- reader 2: instruction: Both 'this...than that' and 'that...than this' fit the cards; nothing fixes which jacket is cheaper.

## r17-025 · B1.1 · text · comparison-1.csv:36

Task: Rewrite with *less*. Start with *That flat*: This flat is more expensive than that flat.
Key: {"kind": "text", "accepted": [["That flat is less expensive than this flat.", "That flat is less expensive than this one.", "That flat's less expensive than this flat.", "That flat's less expensive than this one.", "That flat is less expensive than this flat is.", "That flat is less expensive than this one is."]]}
- reader 2: another correct answer, not accepted: [['That flat is less expensive than this.']]

## r17-026 · B2.2 · gap · conjunctions-1.csv:103

Task: Complete with one word: It was a difficult task, and ___ they finished it on time.
Key: {"kind": "gap", "accepted": [["yet", "still", "nevertheless", "nonetheless"]]}
- reader 1: answer not accepted: [['yet']]
- reader 1: another correct answer, not accepted: [['somehow'], ['even so'], ['finally'], ['eventually'], ['luckily']]
- reader 1: instruction: 'One word' gap has many correct fillers; only 'yet' presumably intended. Contrast is not signalled enough.
- reader 2: another correct answer, not accepted: [['somehow'], ['finally'], ['eventually'], ['luckily'], ['fortunately'], ['surprisingly'], ['miraculously'], ['then']]
- reader 2: instruction: No contrast cue: many one-word adverbs fit ('and yet', 'still', 'somehow', 'finally', 'luckily'...). The intended word is not determined.
- reader 2: sense: Open gap with many correct answers.
- the readers disagree

## r17-029 · B1.1 · gap · iq-b1-6.csv:3

Task: Do you know where ___ ___ buy a phone charger near here?
word_cards: I | can | do
Key: {"kind": "gap", "accepted": [["I"], ["can"]]}
- reader 1: answer not accepted: [['I', 'can']]
- the readers disagree

## r17-030 · B1.1 · gap · iq-b1-6.csv:4

Task: Use the words in brackets: Can you tell me how often ___ on Sundays? (the night bus / run)
Key: {"kind": "gap", "accepted": [["the night bus runs", "the night bus is running"]]}
- reader 1: answer not accepted: [['the night bus runs']]
- reader 1: another correct answer, not accepted: [['the night bus will run']]
- reader 1: sense: 'will run' is less natural but possible.
- the readers disagree

## r17-031 · B1.1 · gap · iq-b1-6.csv:5

Task: I can't hear the guide. Do you know what ___ ___ talking about?
word_cards: is | she | does
Key: {"kind": "gap", "accepted": [["she"], ["is"]]}
- reader 1: answer not accepted: [['she', 'is']]
- the readers disagree

## r17-032 · B1.1 · text · iq-b1-6.csv:6

Task: You need to print a document at work, but you can't find the printer. Ask a colleague. Start with *Do you know where*.
Key: {"kind": "text", "accepted": [["Do you know where the printer is?", "Do you know where the printer is, please?", "Excuse me, do you know where the printer is?", "Excuse me, do you know where the printer is, please?", "Do you know where the printers are?", "Do you know where the printers are, please?", "Excuse me, do you know where the printers are?", "Excuse me, do you know where the printers are, please?", "Do you know where the nearest printer is?", "Do you know where the nearest printer is, please?", "Excuse me, do you know where the nearest printer is?", "Excuse me, do you know where the nearest printer is, please?", "Do you know where I can find the printer?", "Do you know where I can find the printer, please?", "Excuse me, do you know where I can find the printer?", "Excuse me, do you know where I can find the printer, please?", "Do you know where I can find a printer?", "Do you know where I can find a printer, please?", "Excuse me, do you know where I can find a printer?", "Excuse me, do you know where I can find a printer, please?", "Do you know where I can print?", "Do you know where I can print, please?", "Excuse me, do you know where I can print?", "Excuse me, do you know where I can print, please?", "Do you know where I can print something?", "Do you know where I can print something, please?", "Excuse me, do you know where I can print something?", "Excuse me, do you know where I can print something, please?", "Do you know where I can print a document?", "Do you know where I can print a document, please?", "Excuse me, do you know where I can print a document?", "Excuse me, do you know where I can print a document, please?", "Do you know where I can print my document?", "Do you know where I can print my document, please?", "Excuse me, do you know where I can print my document?", "Excuse me, do you know where I can print my document, please?", "Do you know where I can print this document?", "Do you know where I can print this document, please?", "Excuse me, do you know where I can print this document?", "Excuse me, do you know where I can print this document, please?", "Do you know where there is a printer?", "Do you know where there is a printer, please?", "Excuse me, do you know where there is a printer?", "Excuse me, do you know where there is a printer, please?", "Do you know where the printer is located?", "Do you know where the printer is located, please?", "Excuse me, do you know where the printer is located?", "Excuse me, do you know where the printer is located, please?", "Do you know where I can find one?", "Do you know where I can find one, please?", "Excuse me, do you know where I can find one?", "Excuse me, do you know where I can find one, please?", "Do you know where the printer room is?", "Do you know where the printer room is, please?", "Excuse me, do you know where the printer room is?", "Excuse me, do you know where the printer room is, please?"]]}
- reader 1: another correct answer, not accepted: ['Do you know where I can print this?']
- reader 2: another correct answer, not accepted: [['Do you know where I can print this?']]

## r17-038 · B1.1 · gap · iq-b1-6.csv:12

Task: Use the words in brackets. Add any missing word: I'd like to know ___ a balcony. We'd love a view of the sea. (our room / have)
Key: {"kind": "gap", "accepted": [["if our room has", "whether our room has", "if our room has got", "whether our room has got"]]}
- reader 1: answer not accepted: [['if our room has']]
- reader 1: another correct answer, not accepted: [['if our room will have']]
- the readers disagree

## r17-039 · B1.1 · gap · iq-b1-6.csv:13

Task: Can you tell me ___ ___ ___ English? I need help with the menu.
word_cards: speaks | if | speak | does | the waiter
Key: {"kind": "gap", "accepted": [["if"], ["the waiter"], ["speaks"]]}
- reader 1: answer not accepted: [['if', 'the waiter', 'speaks']]
- reader 1: a wrong option that fits: does the waiter speak (non-standard 'Can you tell me does ...')
- the readers disagree

## r17-040 · B1.2 · gap · iq-b1-6.csv:14

Task: Use the words in brackets: Do you know where ___ the car last night? It isn't in the garage. (Tom / park)
Key: {"kind": "gap", "accepted": [["Tom parked"]]}
- reader 1: answer not accepted: [['Tom parked']]
- reader 1: another correct answer, not accepted: [['Tom had parked']]
- reader 1: sense: 'had parked' is less natural.
- reader 2: another correct answer, not accepted: [['Tom had parked']]
- the readers disagree

## r17-041 · B1.2 · gap · iq-b1-6.csv:15

Task: I wonder ___ ___ ___ my email. She hasn't answered yet.
word_cards: get | did | got | Maria | if
Key: {"kind": "gap", "accepted": [["if"], ["Maria"], ["got"]]}
- reader 1: answer not accepted: [['if', 'Maria', 'got']]
- the readers disagree

## r17-044 · B1.2 · text · iq-b1-6.csv:18

Task: Your colleague has a great new laptop bag, and you would like one like it. Ask her about the shop. Start with *Could you tell me where*.
Key: {"kind": "text", "accepted": [["Could you tell me where you bought it?", "Could you tell me where you bought it, please?", "Could you tell me where you bought it from?", "Could you tell me where you bought it from, please?", "Could you tell me where you bought that bag?", "Could you tell me where you bought that bag, please?", "Could you tell me where you bought that bag from?", "Could you tell me where you bought that bag from, please?", "Could you tell me where you bought your bag?", "Could you tell me where you bought your bag, please?", "Could you tell me where you bought your bag from?", "Could you tell me where you bought your bag from, please?", "Could you tell me where you bought your new bag?", "Could you tell me where you bought your new bag, please?", "Could you tell me where you bought your laptop bag?", "Could you tell me where you bought your laptop bag, please?", "Could you tell me where you bought that laptop bag?", "Could you tell me where you bought that laptop bag, please?", "Could you tell me where you got it?", "Could you tell me where you got it, please?", "Could you tell me where you got it from?", "Could you tell me where you got it from, please?", "Could you tell me where you got that bag?", "Could you tell me where you got that bag, please?", "Could you tell me where you got that bag from?", "Could you tell me where you got that bag from, please?", "Could you tell me where you got your bag?", "Could you tell me where you got your bag, please?", "Could you tell me where you got your bag from?", "Could you tell me where you got your bag from, please?", "Could you tell me where you got your new bag?", "Could you tell me where you got your new bag, please?", "Could you tell me where you got your laptop bag?", "Could you tell me where you got your laptop bag, please?", "Could you tell me where you got that laptop bag?", "Could you tell me where you got that laptop bag, please?", "Could you tell me where I can buy one?", "Could you tell me where I can buy one, please?", "Could you tell me where I can get one?", "Could you tell me where I can get one, please?", "Could you tell me where I could buy one?", "Could you tell me where I could buy one, please?", "Could you tell me where I could get one?", "Could you tell me where I could get one, please?", "Could you tell me where I can buy one like it?", "Could you tell me where I can buy one like it, please?", "Could you tell me where I can get one like it?", "Could you tell me where I can get one like it, please?", "Could you tell me where I can buy the same bag?", "Could you tell me where I can buy the same bag, please?", "Could you tell me where I can get the same bag?", "Could you tell me where I can get the same bag, please?"]]}
- reader 1: another correct answer, not accepted: ['Could you tell me where the shop is?']
- reader 2: another correct answer, not accepted: [['Could you tell me where the shop is?']]

## r17-045 · B1.2 · gap · iq-b1-6.csv:19

Task: Do you know how long ___ ___ ___ in this company? She knows everyone.
word_cards: does | work | has | worked | Anna
Key: {"kind": "gap", "accepted": [["Anna"], ["has"], ["worked"]]}
- reader 1: answer not accepted: [['Anna', 'has', 'worked']]
- the readers disagree

## r17-046 · B1.2 · text · iq-b1-6.csv:20

Task: Correct the mistake: Dear Mr Kalns, could you tell me when did you send the invoice? We still haven't received it.
Key: {"kind": "text", "accepted": [["Dear Mr Kalns, could you tell me when you sent the invoice? We still haven't received it."]]}
- reader 1: another correct answer, not accepted: ["Dear Mr Kalns, could you tell me when you sent it? We still haven't received it."]

## r17-048 · B1.2 · gap · iq-b1-6.csv:22

Task: Use the words in brackets. Add any missing word: Can you remember ___ the back door before we left? (you / lock)
Key: {"kind": "gap", "accepted": [["if you locked", "whether you locked", "if you had locked", "whether you had locked"]]}
- reader 1: answer not accepted: [['if you locked']]
- the readers disagree

## r17-050 · B1.2 · text · iq-b1-6.csv:24

Task: You left your umbrella in the meeting room this morning, and now it isn't there. Ask the receptionist. Start with *Do you know if*.
Key: {"kind": "text", "accepted": [["Do you know if anyone has found it?", "Do you know if anyone has found an umbrella?", "Do you know if anyone has found my umbrella?", "Do you know if anyone found it?", "Do you know if anyone found an umbrella?", "Do you know if anyone found my umbrella?", "Do you know if someone has found it?", "Do you know if someone has found an umbrella?", "Do you know if someone has found my umbrella?", "Do you know if someone found it?", "Do you know if someone found an umbrella?", "Do you know if someone found my umbrella?", "Do you know if somebody has found it?", "Do you know if somebody has found an umbrella?", "Do you know if somebody has found my umbrella?", "Do you know if somebody found it?", "Do you know if somebody found an umbrella?", "Do you know if somebody found my umbrella?", "Do you know if anybody has found it?", "Do you know if anybody has found an umbrella?", "Do you know if anybody has found my umbrella?", "Do you know if anybody found it?", "Do you know if anybody found an umbrella?", "Do you know if anybody found my umbrella?", "Do you know if anyone has seen it?", "Do you know if anyone has seen my umbrella?", "Do you know if anyone saw it?", "Do you know if anyone saw my umbrella?", "Do you know if anyone has taken it?", "Do you know if anyone has taken my umbrella?", "Do you know if anyone took it?", "Do you know if anyone took my umbrella?", "Do you know if someone has seen it?", "Do you know if someone has seen my umbrella?", "Do you know if someone saw it?", "Do you know if someone saw my umbrella?", "Do you know if someone has taken it?", "Do you know if someone has taken my umbrella?", "Do you know if someone took it?", "Do you know if someone took my umbrella?", "Do you know if somebody has seen it?", "Do you know if somebody has seen my umbrella?", "Do you know if somebody saw it?", "Do you know if somebody saw my umbrella?", "Do you know if somebody has taken it?", "Do you know if somebody has taken my umbrella?", "Do you know if somebody took it?", "Do you know if somebody took my umbrella?", "Do you know if anybody has seen it?", "Do you know if anybody has seen my umbrella?", "Do you know if anybody saw it?", "Do you know if anybody saw my umbrella?", "Do you know if anybody has taken it?", "Do you know if anybody has taken my umbrella?", "Do you know if anybody took it?", "Do you know if anybody took my umbrella?", "Do you know if anyone has handed it in?", "Do you know if anyone handed it in?", "Do you know if anyone has handed in an umbrella?", "Do you know if anyone handed in an umbrella?", "Do you know if anyone has handed in my umbrella?", "Do you know if anyone handed in my umbrella?", "Do you know if someone has handed it in?", "Do you know if someone handed it in?", "Do you know if someone has handed in an umbrella?", "Do you know if someone handed in an umbrella?", "Do you know if someone has handed in my umbrella?", "Do you know if someone handed in my umbrella?", "Do you know if somebody has handed it in?", "Do you know if somebody handed it in?", "Do you know if somebody has handed in an umbrella?", "Do you know if somebody handed in an umbrella?", "Do you know if somebody has handed in my umbrella?", "Do you know if somebody handed in my umbrella?", "Do you know if anybody has handed it in?", "Do you know if anybody handed it in?", "Do you know if anybody has handed in an umbrella?", "Do you know if anybody handed in an umbrella?", "Do you know if anybody has handed in my umbrella?", "Do you know if anybody handed in my umbrella?", "Do you know if it has been found?", "Do you know if it was found?", "Do you know if it has been handed in?", "Do you know if it was handed in?", "Do you know if my umbrella has been found?", "Do you know if my umbrella was found?", "Do you know if my umbrella has been handed in?", "Do you know if my umbrella was handed in?", "Do you know if an umbrella has been found?", "Do you know if an umbrella was found?", "Do you know if an umbrella has been handed in?", "Do you know if an umbrella was handed in?"]]}
- reader 2: another correct answer, not accepted: [['Do you know if the cleaner took my umbrella?']]

## r17-051 · B1.2 · gap · iq-b1-6.csv:25

Task: I'm not sure ___ ___ ___ ___ the tickets yet. Let me check my email.
word_cards: have | book | did | we | booked | if
Key: {"kind": "gap", "accepted": [["if"], ["we"], ["have"], ["booked"]]}
- reader 1: answer not accepted: [['if', 'we', 'have', 'booked']]
- reader 1: sense: 'did book ... yet' with 'yet' is odd (emphatic, mostly American); 'if we booked' also fine but needs 3 gaps.
- reader 2: sense: Second answer ('if we did book ... yet') is awkward with 'yet' and emphatic; weak but not strictly wrong in US usage.
- the readers disagree

## r17-054 · B2.1 · text · twins-1.csv:72

Task: Ask politely, starting with *Do you know*: When does the shop close?
Key: {"kind": "text", "accepted": [["Do you know when the shop closes?", "Do you know when the shop closes today?", "Do you know what time the shop closes?", "Do you know what time the shop closes today?", "Do you happen to know when the shop closes?", "Do you happen to know when the shop closes today?", "Do you happen to know what time the shop closes?", "Do you happen to know what time the shop closes today?"]]}
- reader 1: another correct answer, not accepted: ['Do you know when the shop will close?']
- reader 1: level: Far too easy for B2.1 (B1 structure).
- reader 2: another correct answer, not accepted: [['Do you know when the shop is closing?'], ['Do you know when the shop will close?']]
- reader 2: level: Too easy for B2.1: same pattern as B1.1 tasks.

## r17-056 · B2.2 · text · twins-2.csv:49

Task: Correct the sentence. Keep *had*: The house had been belonging to my grandparents for decades before we bought it.
Key: {"kind": "text", "accepted": [["The house had belonged to my grandparents for decades before we bought it.", "Before we bought it, the house had belonged to my grandparents for decades.", "the house had belonged to my grandparents for decades before we bought it."]]}
- reader 1: another correct answer, not accepted: ['The house had been owned by my grandparents for decades before we bought it.']
- reader 2: another correct answer, not accepted: [['The house had been owned by my grandparents for decades before we bought it.']]

