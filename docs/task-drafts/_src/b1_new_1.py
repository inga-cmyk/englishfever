from lib import *
import b1_topics
italics.LV_ASCII |= b1_topics.LV_WORDS
B = dict(mcq_b=3, text_b=4, match_b=3)

# ============ Used to and be used to (A2.2 / B1.1 / B1.2) ============
P = Topic("Used to and be used to", **B,
    order=("Subject + *used to* + base verb + the rest. Negative: *didn't use to*.", "Teikuma priekšmets + *used to* + pamatforma + pārējais. Noliegums: *didn't use to*."),
    bank=("*used to* + base verb: a past habit or state that is not true now.", "*used to* + pamatforma: ieradums vai stāvoklis pagātnē, kas tagad vairs nav spēkā."),
    gap=("*used to* + base verb: a past habit or state that is not true now.", "*used to* + pamatforma: ieradums vai stāvoklis pagātnē, kas tagad vairs nav spēkā."),
    text=("Question: *Did* + subject + *use to* + base verb? Negative: *didn't use to* (no *-d*).", "Jautājums: *Did* + teik. priekšmets + *use to* + pamatforma? Noliegums: *didn't use to* (bez *-d*)."),
    mcq=("*used to* + base verb = a past habit. *be used to* + *-ing* = it is normal for me now.", "*used to* + pamatforma = ieradums pagātnē. *be used to* + *-ing* = man tas tagad ir ierasts."),
    match=("*used to* is about the past; *be used to* and *get used to* are about now.", "*used to* attiecas uz pagātni; *be used to* un *get used to* — uz tagadni."))
for s, l, al in [("we used to live in a small flat", "A2.2", None), ("my grandfather used to work on a farm", "A2.2", None), ("did you use to play football as a child", "A2.2", ["as a child did you use to play football"]),
                 ("she didn't use to enjoy cooking but now she loves it", "B1.1", None), ("where did you use to go on holiday as a child", "B1.1", ["as a child where did you use to go on holiday"]),
                 ("my brother used to be shy but now he talks to everyone", "B1.1", None),
                 ("when i was a child we used to visit my grandparents every sunday", "B1.2", ["we used to visit my grandparents every sunday when i was a child"]),
                 ("it took me a long time to get used to the cold weather", "B1.2", None), ("i am not used to getting up so early", "B1.2", None)]:
    P.order(l, s, also=al)
    if s.startswith("when i was a child we used to"): replaces("when i was a child we would visit my grandparents every sunday")   # the topic is used to / be used to: no would
P.bank("A2.2", "My mother ___ cook every evening, but now she is too busy.", "used to", ["use to", "is used to"])
P.bank("A2.2", "I ___ like fish, but now I love it.", "didn't use to", ["didn't used to", "don't use to"])
P.bank("B1.1", "We ___ to the same café every Friday when we were students.", "used to go", ["use to go", "are used to go"])
P.bank("B1.1", "___ you ___ to live near the sea?", ["Did", "use"], ["Do", "used"])
P.bank("B1.2", "After a month I got ___ to the noise.", "used", ["use", "using"])
P.bank("B1.2", "She isn't ___ to ___ in a big city yet.", ["used", "living"], ["use", "live"])
P.gap("A2.2", "We ___ to go to the beach every summer.", "used")
P.gap("A2.2", "Did you ___ to walk to school?", "use")
P.gap("A2.2", "When I was young, I ___ the piano every day. (play)", "used to play | would play | played")
P.gap("B1.1", "When I was a teenager, I ___ any money, so I walked everywhere. (not / have)", "didn't use to have | did not use to have | didn't have | did not have")
P.gap("B1.2", "I'm not used to ___ so early. (get up)", "getting up")
P.gap("B1.2", "It took her a week to get used to ___ the new software. (use)", "using")
P.mcq("A2.2", "Choose the correct option: She ___ have long hair, but now it is short.", "used to", ["use to", "is used to", "was used to"])
P.mcq("A2.2", "Which sentence is about a past habit?", "We used to play cards on Sundays.", ["We played cards last Sunday.", "We are playing cards now.", "We will play cards on Sunday."], b=2)
P.mcq("B1.1", "Choose the correct option: He ___ smoke, but he gave up five years ago.", "used to", ["uses to", "is used to", "use to"])
P.mcq("B1.1", "At home: which sentence is NOT correct?", "Did you used to play chess?", ["Did you use to play chess?", "I used to play chess.", "She didn't use to play chess."], b=4)
P.mcq("B1.1", "Which sentence is correct?", "There didn't use to be a supermarket here.", ["There didn't used to be a supermarket here.", "There not used to be a supermarket here.", "There wasn't use to be a supermarket here."], b=3)
P.mcq("B1.2", "Choose the correct option: At first I hated the food, but now I ___ it.", "am used to", ["used to", "am use to", "use to"])
P.mcq("B1.2", "Which sentence means the same as 'It is normal for me to live alone'?", "I'm used to living alone.", ["I used to live alone.", "I'm used to live alone.", "I get used to live alone."], b=3)
P.mcq("B1.2", "At work: which sentence is NOT correct?", "She is used to get up early.", ["She used to get up early.", "She is used to getting up early.", "She got used to getting up early."], b=4)
P.mcq("B1.2", "Choose the correct option: When we were children, we ___ play in the river every summer.", "used to", ["are used to", "get used to", "use to"], b=3)
replaces("would")
P.mcq("B1.2", "In a text: which sentence is correct?", "I used to have a bike when I was ten.", ["I used have a bike when I was ten.", "I am used to have a bike when I was ten.", "I use to have a bike when I was ten."], b=4)
P.text("A2.2", "Rewrite with used to: When I was young, I played the piano every day.", ["When I was young, I used to play the piano every day.", "I used to play the piano every day when I was young."], b=4)
P.text("B1.1", "Make it negative with didn't use to: We used to have a car.", ["We didn't use to have a car.", "We did not use to have a car."])
P.text("B1.1", "Make the sentence negative: She used to play tennis.", ["She didn't use to play tennis.", "She did not use to play tennis.", "She never used to play tennis."])
P.text("B1.1", "Make a question with *Where*: She used to live in London.", ["Where did she use to live?"])
replaces("Make a question: She used to live in London.")
P.text("B1.2", "Rewrite with used to: When I was little, we visited the zoo every spring.", ["When I was little, we used to visit the zoo every spring.", "We used to visit the zoo every spring when I was little."], b=5)
replaces("Rewrite with would: When I was little, we used to visit the zoo every spring.")
P.text("B1.2", "Correct the mistake: When I was little, we use to visit the zoo every spring.", ["When I was little, we used to visit the zoo every spring.", "We used to visit the zoo every spring when I was little."], b=5)
replaces("Say it another way and keep the meaning: When I was little, we used to visit the zoo every spring.")
P.match("B1.2", "Match each form with its meaning.", [("used to", "a past habit that has stopped"), ("be used to", "something is normal for me"), ("get used to", "something is becoming normal"), ("didn't use to", "this was not true in the past")])

# ============ Articles (A2.2 / B1.1 / B1.2) ============
P = Topic("Articles", **B,
    order=("*a / an* = one of many or the first time. *the* = known or the only one. Names of most cities and countries have no article.", "*a / an* = viens no daudziem vai pirmoreiz. *the* = zināms vai vienīgais. Lielākajai daļai pilsētu un valstu nosaukumu artikula nav."),
    bank=("*a / an* before one countable noun (*an* before a vowel sound). *the* for something known. No article for general plurals and uncountable nouns.", "*a / an* pirms viena skaitāma lietvārda (*an* pirms patskaņa skaņas). *the* — zināmam. Bez artikula — vispārīgs daudzskaitlis un neskaitāmi lietvārdi."),
    gap=("*a / an* before one countable noun (*an* before a vowel sound). *the* for something known or the only one.", "*a / an* pirms viena skaitāma lietvārda (*an* pirms patskaņa skaņas). *the* — zināmam vai vienīgajam."),
    text=("Use *a / an* for one of many, *the* for something known, no article for general plurals.", "*a / an* — viens no daudziem, *the* — zināms, bez artikula — vispārīgs daudzskaitlis."),
    mcq=("*a / an* before one countable noun (*an* before a vowel sound). *the* for something known or the only one. No article for general plurals.", "*a / an* pirms viena skaitāma lietvārda (*an* pirms patskaņa skaņas). *the* — zināmam vai vienīgajam. Bez artikula — vispārīgs daudzskaitlis."),
    match=("*a / an* = first mention. *the* = known or the only one. No article = general plural or uncountable.", "*a / an* = pirmoreiz. *the* = zināms vai vienīgais. Bez artikula = vispārīgs daudzskaitlis vai neskaitāms lietvārds."))
for s, l, al in [("my sister has an old bike", "A2.2", None), ("the sun is hot in july", "A2.2", None), ("i have a cat and a dog", "A2.2", None),
                 ("i saw a man and the man waved to me", "B1.1", None), ("the moon goes around the earth", "B1.1", None), ("she is the best singer in our school", "B1.1", None),
                 ("what a lovely surprise to see you here", "B1.2", None), ("she spent half an hour waiting for the bus", "B1.2", None)]:
    P.order(l, s, also=al)
P.bank("A2.2", "I eat ___ apple every day.", "an", ["a", "some"])
P.bank("A2.2", "My brother is ___ doctor.", "a", ["an", "some"])
P.bank("B1.1", "She plays ___ violin in an orchestra.", "the", ["an", "many"])
P.bank("B1.1", "I'd like ___ glass of water, please.", "a", ["an", "many"])
P.bank("B1.1", "We stayed at ___ hotel near the station. ___ hotel was clean.", ["a", "The"], ["an", "Some"])
P.bank("B1.2", "He gives money to ___ poor.", "the", ["a", "an"])
P.gap("A2.2", "She is ___ honest woman. (a / an)", "an")
P.gap("A2.2", "My cousin lives in ___ small house near the sea. (a / an)", "a")
P.gap("B1.1", "My sister works as ___ nurse in a hospital.", "a")
P.gap("B1.1", "We visited ___ United States last year.", "the")
P.gap("B1.2", "It was such ___ nice day that we went swimming.", "a")
P.gap("B1.2", "She is one of ___ most talented musicians I know.", "the")
P.gap("B1.2", "I have never been to ___ Alps, but I'd love to go skiing there.", "the")
P.mcq("A2.2", "Choose the correct option: She is ___ engineer.", "an", ["a", "some", "many"])
P.mcq("A2.2", "Choose the correct option: I'd like ___ water, please.", "some", ["a", "an", "many"])
P.mcq("A2.2", "Choose the correct option: We have ___ hour before the train.", "an", ["a", "some", "many"])
P.mcq("A2.2", "At breakfast: which sentence is correct?", "I have breakfast at seven.", ["I have a breakfast at seven.", "I have an breakfast at seven.", "I have breakfasts at seven."], b=2)
P.mcq("B1.1", "Choose the correct option: Mount Everest is ___ highest mountain in the world.", "the", ["a", "an", "—"])
P.mcq("B1.1", "Choose the correct option: He is ___ honest man.", "an", ["a", "some", "—"])
P.mcq("B1.1", "Choose the correct option: ___ Baltic Sea is cold in winter.", "The", ["A", "An", "—"])
P.mcq("B1.1", "Choose the correct option: She goes to ___ work by bus.", "(no article)", ["a", "the", "an"])
P.mcq("B1.1", "At home: which sentence is NOT correct?", "I go to the bed at eleven.", ["My son is at school.", "She is in bed.", "We eat breakfast at eight."], b=4)
P.mcq("B1.1", "Which sentence is correct?", "Dogs are loyal animals.", ["A dogs are loyal animals.", "Dog are loyal animals.", "An dogs are loyal animals."], b=3)
P.mcq("B1.2", "Choose the correct option: What ___ beautiful view!", "a", ["an", "the", "—"])
P.mcq("B1.2", "In a text: which sentence is correct?", "She spent half an hour waiting for the bus.", ["She spent half hour waiting for the bus.", "She spent an half hour waiting for the bus.", "She spent a half an hour waiting for the bus."], b=3)
P.mcq("B1.2", "In a travel blog: which sentence is NOT correct?", "He lives in the Latvia.", ["She works in Riga.", "He lives in the Netherlands.", "They live in the UK."], b=4)
P.mcq("B1.2", "Choose the correct option: He is quite ___ good player.", "a", ["an", "—", "some"], b=3)
P.text("B1.2", "Rewrite with the elderly: Old people need more care.", ["The elderly need more care.", "The elderly need more care in hospitals."], b=5)
P.gap("B1.2", "In this town, ___ elderly get free bus tickets.", "the | The", b=4)
# (removed, teacher 29 October: a task must not test whether the learner knows the words vowel and consonant; c-1661 is retired by hand)
P.match("B1.1", "Match each rule with its example.", [("first mention", "I bought a jacket."), ("already mentioned", "The jacket was cheap."), ("general plural", "Jackets are expensive."), ("the best of all", "It is the best jacket in the shop.")])
P.match("B1.2", "Match each pattern with its example.", [("what + a / an", "What a view!"), ("the + nationality", "the Swiss"), ("half + a / an", "half an hour"), ("the + adjective", "the rich")])

# ============ Quantity (A2.2 / B1.1) ============
P = Topic("Quantity", **B,
    order=("*many* + plural, *much* + uncountable. *a few* + plural, *a little* + uncountable.", "*many* + daudzskaitlis, *much* + neskaitāms lietvārds. *a few* + daudzskaitlis, *a little* + neskaitāms lietvārds."),
    bank=("*many / a few* + plural nouns. *much / a little* + uncountable nouns. *some* in positive sentences, *any* in questions and negatives.", "*many / a few* + daudzskaitļa lietvārdi. *much / a little* + neskaitāmi lietvārdi. *some* apgalvojumos, *any* jautājumos un noliegumos."),
    gap=("*many / a few* + plural nouns. *much / a little* + uncountable nouns.", "*many / a few* + daudzskaitļa lietvārdi. *much / a little* + neskaitāmi lietvārdi."),
    text=("*any* in negatives and questions. *enough* after an adjective: *big enough*.", "*any* noliegumos un jautājumos. *enough* aiz īpašības vārda: *big enough*."),
    mcq=("*many / a few* + plural nouns. *much / a little* + uncountable nouns. *a lot of* + both. *too much / too many* = more than we need.", "*many / a few* + daudzskaitļa lietvārdi. *much / a little* + neskaitāmi lietvārdi. *a lot of* + abi veidi. *too much / too many* = vairāk, nekā vajag."),
    match=("*many / a few* go with countable nouns, *much / a little* with uncountable nouns.", "*many / a few* lieto ar skaitāmiem lietvārdiem, *much / a little* — ar neskaitāmiem."))
for s, l in [("there is not much milk in the fridge", "A2.2"), ("how many brothers and sisters do you have", "A2.2"), ("we need a few more chairs", "A2.2"),
             ("there are too many cars on the road today", "B1.1"), ("i don't have enough time to finish the report", "B1.1"), ("she has only a few friends in this city", "B1.1")]:
    P.order(l, s)
P.bank("A2.2", "Would you like ___ tea?", "some", ["two", "many"])
P.bank("A2.2", "Is there ___ bread left?", "any", ["a", "many"])
P.bank("A2.2", "I need ___ eggs for the cake.", "some", ["a", "much"])
P.bank("B1.1", "We didn't take ___ photos on holiday.", "many", ["much", "a little"])
P.bank("B1.1", "Hurry up! There is very ___ time left.", "little", ["few", "many"])
P.bank("B1.1", "The room isn't big ___ for twenty people.", "enough", ["too", "very"])
P.gap("A2.2", "There are too ___ cars in the city centre.", "many")
P.gap("A2.2", "There is too ___ traffic in the city centre.", "much")
P.gap("B1.1", "There is ___ much sugar in this coffee. I can't drink it.", "too | so | far too")
P.gap("B1.1", "How ___ homework do you have today?", "much")
P.mcq("A2.2", "Choose the correct option: We don't have ___ milk.", "any", ["a", "many", "a few"])
P.mcq("A2.2", "Choose the correct option: How ___ people are in the room?", "many", ["much", "a lot", "a little"])
P.mcq("A2.2", "Choose the correct option: There isn't ___ sugar in my tea.", "much", ["many", "a few", "few"])
P.mcq("A2.2", "Choose the correct option: I have ___ friends in this city, so I'm never alone.", "a lot of", ["much", "a little", "little"])
P.mcq("B1.1", "Choose the correct option: There were ___ people at the concert, so we couldn't find seats.", "too many", ["too much", "a little", "much"])
P.mcq("B1.1", "Choose the correct option: We haven't got ___ money to buy a car.", "enough", ["many", "a few", "few"])
P.mcq("B1.1", "At work: which sentence is NOT correct?", "I have many time for hobbies.", ["I have a lot of time for hobbies.", "I don't have much time for hobbies.", "I have a little time for hobbies."], b=4)
P.mcq("B1.1", "Which sentence is correct?", "There is little traffic at night, so the drive is quick.", ["There are little traffic at night, so the drive is quick.", "There is few traffic at night, so the drive is quick.", "There is a few traffic at night, so the drive is quick."], b=3)
P.mcq("B1.1", "Choose the correct option: She has ___ experience, so the company hired her at once.", "a lot of", ["many", "a few", "few"])
P.text("A2.2", "Make it negative with any: She has some money.", ["She doesn't have any money.", "She does not have any money.", "She hasn't any money."], b=3)
P.text("A2.2", "Make the sentence negative: There is some milk.", ["There isn't any milk.", "There is no milk.", "There's no milk.", "There is not any milk."], b=3)
P.text("B1.1", "Rewrite with enough: The soup is too cold.", ["The soup isn't hot enough.", "The soup is not hot enough."], b=5)
P.gap("B1.1", "We can't swim today. The water isn't warm ___ .", "enough", b=3)
P.match("A2.2", "Match each word with its use.", [("many", "with a plural noun: many people"), ("much", "with an uncountable noun: much time"), ("a few", "a small number: a few friends"), ("a little", "a small amount: a little water")])
P.match("B1.1", "Match each phrase with its meaning.", [("too many", "more than we need (things we can count)"), ("not enough", "less than we need"), ("enough", "as much as we need"), ("very little", "almost nothing")])
save("b1-new-1.csv")
