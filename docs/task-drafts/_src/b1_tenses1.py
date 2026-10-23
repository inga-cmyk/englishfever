from lib import *
B = dict(mcq_b=3, text_b=4, match_b=3)
# ============ Present simple (B1.1) +39 ============
P = Topic("Present simple", **B,
    order=("Subject + verb (with *-s* after *he / she / it*) + the rest; questions and negatives use *do / does*.", "Teikuma priekšmets + darbības vārds (ar *-s* aiz *he / she / it*) + pārējais; jautājumos un noliegumos lieto *do / does*."),
    bank=("Habits, facts and timetables: Present Simple. *-s* after *he / she / it*; *do / does* in questions and negatives.", "Ieradumi, fakti un saraksti: Present Simple. *-s* aiz *he / she / it*; *do / does* jautājumos un noliegumos."),
    gap=("Habits, facts and timetables: Present Simple.", "Ieradumi, fakti un saraksti: Present Simple."),
    text=("Present Simple: *do / does* for questions and negatives; adverbs like *never* go before the verb.", "Present Simple: *do / does* jautājumiem un noliegumiem; apstākļa vārdi, piemēram, *never*, ir pirms darbības vārda."),
    mcq=("Habits, facts and timetables use the Present Simple.", "Ieradumiem, faktiem un sarakstiem lieto Present Simple."),
    match=("Present Simple covers habits, facts, timetables and permanent situations.", "Present Simple lieto ieradumiem, faktiem, sarakstiem un pastāvīgām situācijām."))
for s in ["the shop opens at nine on weekdays but closes early on sundays","she rarely eats out because she prefers to cook at home","our train leaves at half past seven so we must hurry","does your brother still work for the same company","water boils at one hundred degrees at sea level","i don't usually drink coffee after lunch because it keeps me awake","he teaches maths at a school near the station","my parents never watch the news but they read a newspaper every day","what does this word mean in your language","the museum doesn't open on mondays during the winter"]: P.order("B1.1",s)
P.bank("B1.1","My sister ___ in a hospital, but she ___ to move to the countryside.",["works","wants"],["working","want","is wanting"])
P.bank("B1.1","The lesson ___ at 9.30, so we ___ to be there early.",["starts","need"],["starting","needs"])
P.bank("B1.1","He never ___ his phone during a meeting because it ___ rude.",["uses","is"],["use","are"])
P.bank("B1.1","Your sister speaks Italian, but ___ she speak French?","does",["do","is"])
P.bank("B1.1","Most people ___ tired when they ___ enough sleep.",["feel","don't get"],["feels","doesn't get"])
P.bank("B1.1","This bus ___ to the airport every twenty minutes.","goes",["go","going"])
P.bank("B1.1","I ___ understand why she ___ always late.",["don't","is"],["doesn't","does"])
P.bank("B1.1","The company ___ over two hundred people and ___ offices in five countries.",["employs","has"],["employ","have"])
P.bank("B1.1","The sun ___ in the east and ___ in the west.",["rises","sets"],["rise","set"])
P.gap("B1.1","He ___ his emails first thing in the morning, before he ___ a coffee. (check / make)","checks / makes")
P.gap("B1.1","The film ___ at eight, so we ___ leave before seven. (start / have to)","starts / have to")
P.gap("B1.1","She ___ meat because she is a vegetarian. (not / eat)","doesn't eat | does not eat")
P.gap("B1.1","How much ___ a ticket to the capital ___ ? (cost)","does / cost")
P.text("B1.1","Make it negative: My colleagues work from home on Fridays.",["My colleagues don't work from home on Fridays.","My colleagues do not work from home on Fridays."])
P.text("B1.1","Make a question with How often: He visits his parents.","How often does he visit his parents?")
P.text("B1.1","Rewrite with never: I don't eat fast food.","I never eat fast food.")
P.text("B1.1","Make a question with What time: The bank opens at nine.","What time does the bank open?")
P.match("B1.1","Match each sentence with its use.",[("The sun rises in the east.","a general truth"),("I go to the gym on Tuesdays.","a habit"),("The bus leaves at 6.15.","a timetable"),("She works in a bank.","a permanent situation")])
P.match("B1.1","Match each beginning with its ending: routines.",[("My brother always forgets","his keys."),("The shops never open","on Sundays."),("Our teacher usually gives","us homework."),("They sometimes eat","out on Fridays.")])
P.match("B1.1","Match each question with its answer.",[("What does she do?","She's a nurse."),("How often do you swim?","Twice a week."),("Where does he live?","In a small town."),("Do they speak German?","Yes, they do.")])
P.mcq("B1.1","Choose the correct option: My brother ___ much television because he prefers reading.","doesn't watch",["not watch","don't watch","doesn't watches"])
P.mcq("B1.1","Choose the correct option: The shop ___ at six on weekdays, so we should hurry.","closes",["closing","close","has close"])
P.mcq("B1.1","Choose the best option: Our teacher ___ us a lot of homework, but we enjoy it.","gives",["giving","give","gaves"])
P.mcq("B1.1","Which sentence uses the Present Simple for a timetable?","The concert starts at eight.",["The concert is starting now.","The concert started at eight.","The concert will have started."])
P.mcq("B1.1","In the office: which sentence is NOT correct?","Our manager don't like long meetings.",["Our manager doesn't like long meetings.","Our colleagues don't like long meetings.","Does your manager like long meetings?"],"*Manager* is *he / she*, so *doesn't*.",b=4)
P.mcq("B1.1","Choose the correct option: ___ you usually take the bus to work?","Do",["Does","Are","Is"])
P.mcq("B1.1","Choose the correct option: Mina ___ at the bank, but today she is working from home.","usually works",["usually working","usually work","works usual"])
P.mcq("B1.1","Choose the correct option: What ___ this sign mean?","does",["is","do","does it"])
P.mcq("B1.1","About routines: which sentence is NOT correct?","He doesn't goes to the gym on Sundays.",["He doesn't go to the gym on Sundays.","He goes to the gym on Saturdays.","Does he go to the gym every day?"],"After *doesn't* the verb has no *-s*.",b=4)
# ============ Present continuous (B1.1) +41 ============
P = Topic("Present continuous", **B,
    order=("Subject + *am / is / are* + verb + *-ing*; for the future, add a time.", "Teikuma priekšmets + *am / is / are* + darbības vārds + *-ing*; nākotnei pievieno laiku."),
    bank=("Now, around now and arranged plans: *am / is / are* + verb + *-ing*.", "Tagad, ap šo laiku un norunāti plāni: *am / is / are* + darbības vārds + *-ing*."),
    gap=("Now, around now and arranged plans: *am / is / are* + verb + *-ing*.", "Tagad, ap šo laiku un norunāti plāni: *am / is / are* + darbības vārds + *-ing*."),
    text=("Question: *am / is / are* before the subject. Negative: *not* after *am / is / are*.", "Jautājums: *am / is / are* pirms teik. priekšmeta. Noliegums: *not* aiz *am / is / are*."),
    mcq=("Present Continuous: an action now, a temporary situation, a change, or an arrangement.", "Present Continuous: darbība tagad, pagaidu situācija, pārmaiņa vai norunāts pasākums."),
    match=("Present Continuous: now, temporary, changing, or arranged.", "Present Continuous: tagad, pagaidu, mainīgs vai norunāts."))
for s in ["i'm sorry but the manager is talking to a client at the moment","prices are rising faster than wages these days","we are flying to rome on friday so i'm packing tonight","why is she wearing a coat when it is so warm","my sister is staying with us until the end of the month","more and more people are working from home","he isn't answering his phone because he is driving","are you using this chair or can i take it","the weather is getting colder and the days are getting shorter","what are you looking for in that drawer"]: P.order("B1.1",s)
P.bank("B1.1","Please don't call now. I ___ a very important meeting.","am having",["having","had"])
P.bank("B1.1","Our company ___ a new office, so everything ___ chaotic this week.",["is opening","is"],["opening","are"])
P.bank("B1.1","We ___ to Madrid on Saturday, so we ___ our flight yet.",["are flying","haven't changed"],["fly","don't change"]) if False else None
P.bank("B1.1","Children ___ taller than their parents these days.","are growing",["growing","grows"])
P.bank("B1.1","I can't talk. I ___ for an exam tomorrow.","am studying",["studying","studied"])
P.bank("B1.1","Look! They ___ the old bridge with a new one.","are replacing",["replacing","replaces"])
P.bank("B1.1","Right now the traffic ___ worse, and the drivers ___ at each other.",["is getting","are shouting"],["gets","shout"])
P.bank("B1.1","Why ___ you ___ so quietly today? Is something wrong?",["are","speaking"],["did","speaks"])
P.bank("B1.1","Anna ___ for a new flat because her rent is too high.","is looking",["looking","look"])
P.bank("B1.1","Which film ___ they ___ at the cinema tonight?",["are","watching"],["did","watched"])
P.gap("B1.1","My neighbour ___ his house this month, so there is a lot of noise. (paint)","is painting")
P.gap("B1.1","I ___ my brother at the airport at six, so I can't come to the meeting. (meet)","am meeting | 'm meeting")
P.gap("B1.1","They ___ to move to the coast, but they haven't decided yet. (think)","are thinking")
P.gap("B1.1","What ___ the children ___ in the garden? They are very quiet. (do)","are / doing")
P.text("B1.1","Make a question with Why: She is crying.","Why is she crying?")
P.text("B1.1","Make it negative: We are staying at a hotel.",["We aren't staying at a hotel.","We are not staying at a hotel.","We're not staying at a hotel."])
P.text("B1.1","Make a question: Your parents are visiting you this weekend.","Are your parents visiting you this weekend?")
P.text("B1.1","Rewrite for a change in progress: The weather gets warmer. (it is)","It is getting warmer.",b=5) if False else None
P.match("B1.1","Match each sentence with its meaning.",[("I'm waiting for a call.","an action now"),("She's staying with us this week.","a temporary situation"),("It's getting darker.","a change"),("We're flying to Rome on Friday.","an arrangement")])
P.match("B1.1","Match each beginning with its ending: this week.",[("Our neighbours are building","a new garage."),("The students are preparing","for their exams."),("My boss is travelling","to Berlin."),("I'm learning","to drive.")])
P.match("B1.1","Match each question with its answer: what is happening.",[("What are you doing?","I'm sorting my emails."),("Why are they shouting?","They're watching the match."),("Who is he talking to?","His new neighbour."),("Is it raining?","Not now, it has stopped.")])
P.mcq("B1.1","Choose the correct option: Please be quiet. The baby ___ and I don't want to wake her.","is sleeping",["sleeping","sleep","has sleeping"])
P.mcq("B1.1","Choose the correct option: ___ you ___ anything special this weekend, or can we meet?","Are / doing",["Have / done","Will / doing","Were / do"])
P.mcq("B1.1","Choose the correct option: I ___ to find a better job at the moment, so I'm reading the adverts every day.","am trying",["trying","tried","has trying"])
P.mcq("B1.1","Which sentence describes a change that is happening in society now?","More people are choosing electric cars.",["More people choose electric cars every year.","More people chose electric cars.","More people will choose electric cars."])
P.mcq("B1.1","Choose the correct option: This week my sister ___ at a friend's house while her flat is painted.","is staying",["staying","are staying","stay"])
P.mcq("B1.1","At the meeting: which sentence is NOT correct?","I'm not understanding the instructions.",["I don't understand the instructions.","I'm reading the instructions now.","Are you following the instructions?"],"*Understand* is a state verb: *I don't understand*.",b=4)
P.mcq("B1.1","In the lesson: which sentence is NOT correct?","We're knowing the answer, but we can't say it.",["We know the answer, but we can't say it.","We're working on the answer.","They are thinking about the answer."],"*Know* is a state verb: *we know*.",b=4)
P.mcq("B1.1","Choose the correct option: At the moment the prices ___ because of the shortage.","are going up",["going up","went up","goes up"])
P.mcq("B1.1","Which sentence is a fixed arrangement?","I'm seeing my dentist at four tomorrow.",["I often see my dentist.","I see my dentist when I have toothache.","I saw my dentist yesterday."])
P.mcq("B1.1","Choose the correct option: I usually walk to work, but this week I ___ the bus because of the snow.","am taking",["taking","took","has taken"])
P.mcq("B1.1","About a meeting: which sentence is NOT correct?","The manager is have a meeting with a client.",["The manager is having a meeting with a client.","The managers are having a meeting.","Is the manager having a meeting?"],"After *is* the verb needs *-ing*: *is having*.",b=4)
# ============ Past simple (B1.1 / B1.2) +33 ============
P = Topic("Past simple", **B,
    order=("Subject + past verb + the rest; *did* + base verb in questions and negatives.", "Teikuma priekšmets + pagātnes forma + pārējais; jautājumos un noliegumos *did* + pamatforma."),
    bank=("Finished events: past form (*-ed* or irregular). After *did / didn't* the base form. Past habits: *used to*.", "Pabeigti notikumi: pagātnes forma (*-ed* vai neregulāra). Pēc *did / didn't* pamatforma. Pagātnes ieradumi: *used to*."),
    gap=("Finished events: past form; *did / didn't* + base form.", "Pabeigti notikumi: pagātnes forma; *did / didn't* + pamatforma."),
    text=("Past Simple: *did / didn't* + base verb; *because* gives a reason; *after* and *before* order events.", "Past Simple: *did / didn't* + pamatforma; *because* dod iemeslu; *after* un *before* sakārto notikumus."),
    mcq=("A finished event at a finished time: Past Simple. A past habit that stopped: *used to*.", "Pabeigts notikums pabeigtā laikā: Past Simple. Pagātnes ieradums, kas beidzies: *used to*."),
    match=("Past Simple: events one after the other; *used to* for past habits.", "Past Simple: notikumi cits pēc cita; *used to* pagātnes ieradumiem."))
for s,l in [("we missed the last train so we took a taxi home","B1.1"),("she opened the letter and read it twice before she answered","B1.1"),("why didn't you tell me that you had lost your job","B1.1"),("the film was so boring that half of the audience left early","B1.1"),("when did you start learning english","B1.1"),("he didn't see the sign so he drove straight past the turning","B1.1"),("we used to play in the street until it got dark","B1.2"),("did you use to walk to school when you were young","B1.2")]: P.order(l,s)
P.bank("B1.1","I ___ the report on Monday, but I ___ it to my boss until Friday.",["finished","didn't send"],["finish","sent","don't send"])
P.bank("B1.1","The thieves ___ through the window and ___ the jewellery.",["climbed","stole"],["climbing","stealing"])
P.bank("B1.1","___ you ___ my message last night?",["Did","get"],["Do","got","Does"])
P.bank("B1.1","She ___ in London for two years before she ___ to Paris.",["lived","moved"],["live","move"])
P.bank("B1.1","We ___ a great meal, but the service ___ very slow.",["had","was"],["having","being"])
P.bank("B1.2","When I was a child, we ___ to the lake every summer.","used to go",["use to go","were used to go"])
P.bank("B1.2","He ___ to like fish, but now he eats it every week.","didn't use",["didn't used","wasn't used"]) if False else None
P.gap("B1.1","I ___ him at the party, so I didn't say hello. (not / recognise)","didn't recognise | did not recognise | didn't recognize | did not recognize")
P.gap("B1.1","After the match, the players ___ the fans and ___ into the bus. (thank / climb)","thanked / climbed")
P.gap("B1.1","How long ___ you ___ for the bus yesterday? (wait)","did / wait")
P.gap("B1.2","We ___ to have a dog when I was young. (use)","used")
P.text("B1.1","Join with after: I finished work. I went to the gym.",["After I finished work, I went to the gym.","I went to the gym after I finished work."])
P.text("B1.1","Make a question with How long: They stayed in Rome for a week.","How long did they stay in Rome?")
P.text("B1.1","Make it negative: He told me the truth.",["He didn't tell me the truth.","He did not tell me the truth."])
P.text("B1.2","Rewrite with used to: When I was young, I played the piano every day.",["When I was young, I used to play the piano every day.","I used to play the piano every day when I was young."],b=5)
P.match("B1.1","Match each beginning with its ending: yesterday.",[("I missed the bus","so I walked to work."),("She lost her phone","and called me from a friend's."),("We got to the cinema late","because the traffic was bad."),("He didn't study","so he failed the test.")])
P.match("B1.2","Match each past habit with the person.",[("He used to smoke,","but he gave it up."),("She used to live abroad,","but she moved back."),("We used to argue a lot,","but now we get on well."),("They used to have a dog,","but it died.")])
P.mcq("B1.1","Choose the correct option: She ___ the door, looked around and then walked in.","opened",["opens","has opened","opening"])
P.mcq("B1.1","Choose the correct option: We ___ the concert because the tickets were too expensive.","didn't go to",["didn't going to","don't go to","didn't went to"],b=3)
P.mcq("B1.1","Choose the correct option: Where ___ you ___ your last holiday?","did / spend",["do / spend","did / spent","are / spending"])
P.mcq("B1.1","Which sentence tells a story in the correct order?","He woke up, got dressed and left the house.",["He woke up, getting dressed and leaving the house.","He wakes up, got dressed and left.","He woke up, got dressed and leave the house."])
P.mcq("B1.1","Reading an email: which sentence is NOT correct?","Why did you stayed at home yesterday?",["Why did you stay at home yesterday?","Why did she leave early yesterday?","When did you get home yesterday?"],"After *did* the verb is in the base form: *stay*.",b=4)
P.mcq("B1.2","Choose the correct option: When I was young, I ___ in a small flat above a bakery.","used to live",["use to live","am used to live","was used to live"])
P.mcq("B1.2","Choose the correct option: We ___ much money when we were students, so we cooked at home.","didn't use to have",["didn't used to have","weren't used to have","don't use to have"],b=3)
P.mcq("B1.2","What does 'I used to play tennis' tell us?","I played in the past, but I don't now.",["I play now and I played before.","I will play tennis soon.","I am playing tennis."])
P.mcq("B1.2","About the past: which sentence is NOT correct?","I didn't used to like olives.",["I didn't use to like olives.","I used to hate olives.","Did you use to like olives?"],"After *didn't* we use *use to*, not *used to*.",b=4)
# ============ Past continuous (B1.1 / B1.2) +31 ============
P = Topic("Past continuous", **B,
    order=("Subject + *was / were* + verb + *-ing* + the rest; the short event is in the Past Simple.", "Teikuma priekšmets + *was / were* + darbības vārds + *-ing* + pārējais; īsais notikums ir Past Simple."),
    bank=("The long action in progress: *was / were* + verb + *-ing*; the short event that interrupts: Past Simple.", "Garā darbība, kas norisinājās: *was / were* + darbības vārds + *-ing*; īsais notikums, kas pārtrauc: Past Simple."),
    gap=("The long action: *was / were* + verb + *-ing*; the interruption: Past Simple.", "Garā darbība: *was / were* + darbības vārds + *-ing*; pārtraukums: Past Simple."),
    text=("The long action uses *was / were* + verb + *-ing*; *while* goes with the long action, *when* with the short event.", "Garajai darbībai lieto *was / were* + darbības vārds + *-ing*; *while* ir ar garo darbību, *when* ar īso notikumu."),
    mcq=("An action in progress when something else happened: Past Continuous for the long action, Past Simple for the short one.", "Darbība, kas norisinājās, kad notika kaut kas cits: garajai darbībai Past Continuous, īsajai Past Simple."),
    match=("Past Continuous for the long action; Past Simple for the short event.", "Garajai darbībai Past Continuous; īsajam notikumam Past Simple."))
for s,l in [("while i was walking to work i met an old friend","B1.1"),("the phone rang while we were having dinner","B1.1"),("what were you doing when the lights went out","B1.1"),("they were arguing loudly when the teacher walked in","B1.1"),("she was driving home when she saw the accident","B1.1"),("i was going to call you but i lost your number","B1.2"),("we weren't expecting visitors so the house was a mess","B1.2")]: P.order(l,s)
P.bank("B1.1","I ___ the shopping when I ___ my old teacher.",["was doing","saw"],["doing","seeing"])
P.bank("B1.1","While we ___ for the train, it ___ to snow.",["were waiting","began"],["waiting","beginning"])
P.bank("B1.1","The guests ___ when the power ___ off.",["were dancing","went"],["dancing","going"])
P.bank("B1.1","___ you ___ when the doorbell rang?",["Were","sleeping"],["Have","slept"])
P.bank("B1.2","I ___ to phone you, but I lost your number.","was going",["going","am going"])
P.bank("B1.2","We ___ to move, but then we found a better flat.","were planning",["planning","are planning"])
P.gap("B1.1","He ___ his bike when he ___ off. (ride / fall)","was riding / fell")
P.gap("B1.1","While she ___ the report, her colleagues ___ the room. (write / leave)","was writing / left")
P.gap("B1.1","What ___ you ___ when I called you last night? (do)","were / doing")
P.gap("B1.2","I ___ to tell you, but you were busy. (try)","was trying")
P.text("B1.1","Join with when: I was cooking. The smoke alarm went off.",["I was cooking when the smoke alarm went off.","When the smoke alarm went off, I was cooking."])
P.text("B1.1","Join with while: We were waiting. A man asked us for directions.",["While we were waiting, a man asked us for directions.","A man asked us for directions while we were waiting."])
P.text("B1.2","Make it negative: I was planning to come.",["I wasn't planning to come.","I was not planning to come."],b=4)
P.match("B1.1","Match each long action with the short event.",[("I was reading in bed","when the lights went out."),("We were crossing the road","when a cyclist hit us."),("She was painting the wall","when she fell off the ladder."),("They were driving home","when the engine stopped.")])
P.match("B1.2","Match each past plan with what happened.",[("I was going to call you,","but my phone died."),("We were planning to travel,","but the flights were cancelled."),("She was hoping to win,","but she came second."),("He was meant to meet us,","but he overslept.")])
P.mcq("B1.1","Choose the correct option: At ten o'clock last night we ___ a film at home.","were watching",["was watching","are watching","watching"])
P.mcq("B1.1","Choose the correct option: I ___ in the garden when it started to rain.","was working",["were working","am working","was work"])
P.mcq("B1.1","In the story 'When Mia called, I was cooking', which action started first?","Cooking.",["Calling.","Both started together.","We cannot tell."],"The Past Continuous action was already in progress when the call came.",b=3)
P.mcq("B1.1","Choose the correct option: While my brother ___ a shower, I ___ breakfast.","was taking / made",["took / made","was taking / was making","took / was making"],"Both options 'was making' and 'made' can fit, but only one pair is given here.",b=3) if False else None
P.mcq("B1.1","On the phone: which sentence is NOT correct?","When I came in, the children was watching TV.",["When I came in, the children were watching TV.","When I came in, my son was watching TV.","When I came in, we were watching TV."],"*The children* = *they*, so *were*.",b=4)
P.mcq("B1.1","Choose the correct option: What ___ at nine o'clock last night?","were you doing",["you were doing","are you doing","have you done"])
P.mcq("B1.2","Choose the correct option: We ___ about moving house when we got the news.","were thinking",["thinking","think","have thought"])
P.mcq("B1.2","What does 'We were going to call you' tell us?","We planned to call you.",["We called you.","We will call you.","We are calling you."])
P.mcq("B1.2","In the newspaper: which sentence is NOT correct?","The guests was going to stay, but they were tired.",["The guests were going to stay, but they were tired.","We were going to leave, but it rained.","I was going to ask you."],"*The guests* = *they*, so *were*.",b=4)
P.mcq("B1.2","You want to say you planned something but did not do it. Choose the best option.","I was going to buy a car, but I changed my mind.",["I am going to buy a car, but I changed my mind.","I went to buy a car, but I changed my mind.","I will buy a car, but I changed my mind."])
save("b1-tenses-1.csv")
