from lib import *
B = dict(mcq_b=3, text_b=4, match_b=3)
# ============ Present perfect (B1.1 / B1.2) +35 ============
P = Topic("Present perfect", **B,
    order=("Subject + *have / has* + 3. form + the rest. *For / since* give the length of time.", "Teikuma priekšmets + *have / has* + 3. forma + pārējais. *For / since* parāda laika ilgumu."),
    bank=("Present Perfect: *have / has* + 3. form. It links the past with now (experience, result, time up to now).", "Present Perfect: *have / has* + 3. forma. Tas savieno pagātni ar tagadni (pieredze, rezultāts, laiks līdz tagadnei)."),
    gap=("Present Perfect: *have / has* + 3. form.", "Present Perfect: *have / has* + 3. forma."),
    text=("Question: *Have / Has* + subject + 3. form. Negative: *haven't / hasn't* + 3. form. *How long* asks about time up to now.", "Jautājums: *Have / Has* + teik. priekšmets + 3. forma. Noliegums: *haven't / hasn't* + 3. forma. *How long* jautā par laiku līdz tagadnei."),
    mcq=("Present Perfect with *for / since*, *ever / never*, *just / already / yet*. A finished time (*last week, in 2019, ago*) needs the Past Simple.", "Present Perfect lieto ar *for / since*, *ever / never*, *just / already / yet*. Pabeigts laiks (*last week, in 2019, ago*) prasa Past Simple."),
    match=("Present Perfect: *for / since*, *just / already / yet*, experiences.", "Present Perfect: *for / since*, *just / already / yet*, pieredze."))
for s,l in [("i have lived in this city since i was a child","B1.1"),("she hasn't answered my email yet so i will call her","B1.1"),("how long have you known your best friend","B1.1"),("we have never seen such a beautiful sunset","B1.1"),("has the manager already signed the contract","B1.1"),("they have just announced the results of the competition","B1.1"),("it's the first time that i have tried sushi","B1.2"),("my brother has been to australia twice but i have never been","B1.2"),("i have worked here for ten years and i still enjoy it","B1.2")]: P.order(l,s)
P.bank("B1.1","I ___ my keys, so I can't get into the flat.","have lost",["losing","has lost"])
P.bank("B1.1","She ___ here since 2018, but she ___ to move next year.",["has worked","plans"],["work","planning"])
P.bank("B1.1","We ___ for an hour, and the bus still ___ .",["have waited","hasn't come"],["waiting","come"])
P.bank("B1.1","How many countries ___ you ___ ?",["have","visited"],["did","visiting"])
P.bank("B1.1","He ___ never ___ a horse.",["has","ridden"],["have","rode"])
P.bank("B1.1","I ___ this film three times, and I want to see it again.","have seen",["seeing","has seen"])
P.bank("B1.2","They ___ just ___ the final exam.",["have","passed"],["has","pass"])
P.bank("B1.2","It ___ rained for a week, so the river is very high.","has",["have","is"])
P.gap("B1.1","I ___ my passport, so I need a new one. (lose)","have lost")
P.gap("B1.1","How long ___ you ___ for this company? (work)","have / worked")
P.gap("B1.2","She ___ her homework yet. (not / finish)","hasn't finished | has not finished")
P.text("B1.1","Rewrite with since: I started learning English in 2019 and I still learn it.",["I have been learning English since 2019.","I have learned English since 2019."],b=5)
P.text("B1.1","Make a question with How long: She has lived in Spain.","How long has she lived in Spain?")
P.text("B1.1","Make it negative: We have visited that museum.",["We haven't visited that museum.","We have not visited that museum."])
P.text("B1.2","Make a question with ever: Your parents have travelled abroad.",["Have your parents ever travelled abroad?","Have your parents ever traveled abroad?"])
P.match("B1.1","Match each sentence with its meaning.",[("I've lost my keys.","a result now"),("I've lived here for ten years.","something that continues"),("I've been to Italy twice.","life experience"),("I've just finished.","a very recent action")])
P.match("B1.1","Match each time word with its sentence.",[("for","I have studied here for two years."),("since","I have studied here since 2022."),("already","I have already studied this."),("yet","I haven't studied this yet.")])
P.match("B1.2","Match each beginning with its ending: experiences.",[("I have never","tried scuba diving."),("She has twice","won a national prize."),("They have often","stayed in that hotel."),("We have never","been so tired.")])
P.mcq("B1.1","Choose the correct option: We ___ each other since we were at school.","have known",["knew","know","are knowing"])
P.mcq("B1.1","Choose the correct option: She has worked here ___ five years.","for",["since","ago","from"])
P.mcq("B1.1","Choose the correct option: I've worked here ___ 2015.","since",["for","ago","during"])
P.mcq("B1.1","Choose the correct option: They moved to Rome three years ___ .","ago",["for","since","before"])
P.mcq("B1.2","Between colleagues: which sentence is NOT correct?","I have visited that museum last weekend.",["I visited that museum last weekend.","I have visited that museum twice.","Have you visited that museum?"],"A finished time (*last weekend*) needs the Past Simple.",b=4)
P.mcq("B1.2","In a CV: which sentence is NOT correct?","She has lived in Paris since five years.",["She has lived in Paris for five years.","She has lived in Paris since 2019.","She lived in Paris for five years."],"Use *for* with a length of time, *since* with a starting point.",b=4)
P.mcq("B1.2","Choose the correct option: He ___ in a few different jobs, so he has a lot of experience.","has worked",["have worked","working","work"])
P.mcq("B1.2","Which sentence means the same as 'I have lost my keys'?","I don't have my keys now.",["I lost my keys yesterday and found them.","I will lose my keys.","I have found my keys."])
# ============ Present perfect continuous (B1.1 / B1.2) +31 ============
P = Topic("Present perfect continuous", **B,
    order=("Subject + *have / has been* + verb + *-ing* + the rest.", "Teikuma priekšmets + *have / has been* + darbības vārds + *-ing* + pārējais."),
    bank=("Present Perfect Continuous: *have / has been* + verb + *-ing*: an activity up to now, and its length or result.", "Present Perfect Continuous: *have / has been* + darbības vārds + *-ing*: darbība līdz tagadnei, tās ilgums vai sekas."),
    gap=("*Have / has been* + verb + *-ing*.", "*Have / has been* + darbības vārds + *-ing*."),
    text=("Question: *Have / Has* + subject + *been* + *-ing*. Negative: *haven't / hasn't been* + *-ing*. *How long* asks about the length.", "Jautājums: *Have / Has* + teik. priekšmets + *been* + *-ing*. Noliegums: *haven't / hasn't been* + *-ing*. *How long* jautā par ilgumu."),
    mcq=("Present Perfect Continuous shows the activity and how long. State verbs (*know, like*) do not take it.", "Present Perfect Continuous parāda darbību un cik ilgi. Stāvokļa darbības vārdiem (*know, like*) to nelieto."),
    match=("Continuous = the activity or how long; simple = the result or how many.", "Continuous = darbība vai cik ilgi; simple = rezultāts vai cik daudz."))
for s,l in [("i have been waiting for the bus for twenty minutes","B1.1"),("she has been learning spanish since last september","B1.1"),("how long have you been working here","B1.1"),("it has been raining all day so we stayed in","B1.1"),("they have been talking on the phone for hours","B1.1"),("he hasn't been feeling well lately","B1.2"),("what have you been doing all morning","B1.2"),("we have been looking for a flat since march","B1.2")]: P.order(l,s)
P.bank("B1.1","My eyes hurt because I ___ at the screen all day.","have been looking",["looking","has been looking"])
P.bank("B1.1","How long ___ they ___ for the results?",["have","been waiting"],["did","waiting"])
P.bank("B1.1","They ___ been ___ here since June.",["have","living"],["has","lived"])
P.bank("B1.1","He ___ been ___ the guitar since he was ten.",["has","playing"],["have","played"])
P.bank("B1.2","I ___ all morning, so I'm tired.","have been working",["working","has been working"])
P.bank("B1.2","It ___ snowing since midnight.","has been",["have been","is"])
P.bank("B1.2","We ___ for you for ages!","have been waiting",["been waiting","has been waiting"])
P.gap("B1.1","I ___ all day, so I need a break. (work)","have been working")
P.gap("B1.1","How long ___ you ___ English? (learn)","have / been learning")
P.gap("B1.2","She ___ well lately, so she's seeing a doctor. (not / sleep)","hasn't been sleeping | has not been sleeping")
P.gap("B1.2","They ___ for hours, but they haven't found it. (look)","have been looking")
P.text("B1.1","Make a question with How long: She has been learning Chinese.","How long has she been learning Chinese?")
P.text("B1.1","Make it negative: I have been sleeping well.",["I haven't been sleeping well.","I have not been sleeping well."])
P.text("B1.2","Join with because: She is tired. She has been running.","She is tired because she has been running.")
P.match("B1.1","Match each sentence with its focus.",[("I've been reading all day.","the activity"),("I've read three chapters.","the result"),("I've been waiting for an hour.","how long"),("I've written five emails.","how many")])
P.match("B1.2","Match each situation with the sentence.",[("Your hands are dirty.","I've been working in the garden."),("You are very tired.","I've been studying all night."),("Your hair is wet.","I've been swimming."),("Your eyes are red.","I've been crying.")])
P.match("B1.2","Match each beginning with its ending: for or since.",[("We've been living here","since 2019."),("She has been working","for six hours."),("They have been dating","since last summer."),("I have been learning","for a year.")])
P.mcq("B1.1","Choose the correct option: Her hands are covered in paint. She ___ the kitchen.","has been painting",["painting","have been painting","has paint"])
P.mcq("B1.1","Which sentence says how long?","I've been learning French for two years.",["I've learned French.","I learned French at school.","I'm learning French."])
P.mcq("B1.1","Choose the correct option: How long ___ you ___ for a new flat?","have / been looking",["did / looking","are / looked","has / been looking"])
P.mcq("B1.2","About a long wait: which sentence is NOT correct?","I've been knowing him for years.",["I've known him for years.","I've been waiting for him for years.","I've been seeing him a lot lately."],"*Know* is a state verb: *I've known*.",b=4)
P.mcq("B1.2","Reading a diary: which sentence is NOT correct?","She has been work here since June.",["She has been working here since June.","She has worked here since June.","She has been working here for months."],"After *been* the verb needs *-ing*.",b=4)
P.mcq("B1.2","Choose the correct option: I ___ English for ten years, and I still love it.","have been learning",["have learning","am learning","learning"])
# ============ Past perfect (B1.2) +38 ============
P = Topic("Past perfect", **B,
    order=("Subject + *had* + 3. form: the first of two past events.", "Teikuma priekšmets + *had* + 3. forma: pirmais no diviem pagātnes notikumiem."),
    bank=("Past Perfect: *had* + 3. form for the earlier event; the later event is in the Past Simple.", "Past Perfect: *had* + 3. forma agrākajam notikumam; vēlākais notikums ir Past Simple."),
    gap=("Past Perfect: *had* + 3. form for the earlier event.", "Past Perfect: *had* + 3. forma agrākajam notikumam."),
    text=("Past Perfect: *had* + 3. form for the earlier event; *after* and *because* link the two events.", "Past Perfect: *had* + 3. forma agrākajam notikumam; *after* un *because* savieno abus notikumus."),
    mcq=("The Past Perfect shows which of two past events happened first.", "Past Perfect parāda, kurš no diviem pagātnes notikumiem notika pirmais."),
    match=("Past Perfect = the earlier event; Past Simple = the later one.", "Past Perfect = agrākais notikums; Past Simple = vēlākais."))
for s in ["when i arrived the film had already started","she was tired because she had worked all night","they had left before we got to the party","had you ever visited london before that trip","he realised that he had forgotten his wallet","by the time the police came the thieves had escaped","we had finished dinner when our guests arrived","i didn't recognise her because she had changed her hair","after she had read the letter she burst into tears","the train had already gone when we reached the station"]: P.order("B1.2",s)
P.bank("B1.2","When we got to the station, the train ___ already ___ .",["had","left"],["has","leave"])
P.bank("B1.2","She ___ the report before the meeting started.","had finished",["has finished","finishing"])
P.bank("B1.2","I ___ never ___ snow before that day.",["had","seen"],["has","saw"])
P.bank("B1.2","He was angry because someone ___ his car.","had damaged",["damaging","has damaged"])
P.bank("B1.2","By the time I called, they ___ .","had gone",["has gone","go"])
P.bank("B1.2","After they ___ dinner, they watched a film.","had eaten",["eating","has eaten"])
P.bank("B1.2","___ you ___ the news before I told you?",["Had","heard"],["Has","hear"])
P.bank("B1.2","We ___ the house when it started to rain.","had left",["leaving","has left"])
P.bank("B1.2","She ___ her keys, so she couldn't get in.","had lost",["losing","has lost"])
P.gap("B1.2","By the time we arrived, the concert ___ . (already / start)","had already started")
P.gap("B1.2","I ___ my homework before dinner, so I watched TV. (finish)","had finished")
P.gap("B1.2","She was upset because she ___ her ticket. (lose)","had lost")
P.gap("B1.2","Before he became a pilot, he ___ in a bank. (work)","had worked")
P.text("B1.2","Join with after: She finished her coffee. She left the café.",["After she had finished her coffee, she left the café.","She left the café after she had finished her coffee."])
P.text("B1.2","Join with because: He was late. He missed the bus.",["He was late because he had missed the bus.","Because he had missed the bus, he was late."])
P.text("B1.2","Make it negative: I had seen the film before.",["I hadn't seen the film before.","I had not seen the film before."],b=4)
P.text("B1.2","Make a question: They had already left.","Had they already left?")
P.match("B1.2","Match each result with its cause.",[("She was tired because","she had slept badly."),("He was hungry because","he hadn't eaten all day."),("They were late because","they had missed the train."),("I was nervous because","I had never flown before.")])
P.match("B1.2","Match each beginning with its ending: before and after.",[("By the time I got up,","everyone had left."),("After he had read the book,","he returned it."),("She hadn't met him before","the party."),("We had just arrived","when the rain started.")])
P.match("B1.2","Match each sentence with the event that came first.",[("When I arrived, she had left.","she left first"),("When I arrived, she left.","I arrived first"),("When I got up, it had stopped raining.","the rain stopped first"),("When I got up, it stopped raining.","I got up first")],b=4)
P.mcq("B1.2","Choose the correct option: When I got home, my sister ___ dinner.","had already cooked",["already cook","has already cooked","was already cooks"])
P.mcq("B1.2","Which sentence shows that the film started first?","When we arrived, the film had started.",["When we arrived, the film started.","When we arrived, the film starts.","When we arrived, the film will start."])
P.mcq("B1.2","Choose the correct option: She wasn't hungry because she ___ lunch an hour before.","had eaten",["has eaten","eating","is eating"])
P.mcq("B1.2","In a story: which sentence is NOT correct?","After he has finished work, he went home.",["After he had finished work, he went home.","He went home after he had finished work.","He went home after work."],"The earlier event needs *had finished*.",b=4)
P.mcq("B1.2","In a diary: which sentence is NOT correct?","I hadn't never seen it before.",["I hadn't seen it before.","I had never seen it before.","I had seen it once before."],"*Never* already makes it negative: no *n't*.",b=4)
P.mcq("B1.2","Choose the correct option: I could not get in because I ___ my keys at home.","had left",["lefting","have left","leave"])
P.mcq("B1.2","What does 'I had finished before she arrived' tell us?","I finished first.",["She arrived first.","We finished together.","I have not finished."])
P.mcq("B1.2","Choose the correct option: ___ he ever ___ abroad before he moved to Spain?","Had / lived",["Has / lived","Did / lived","Had / live"])
# ============ Future (B1.1 / B1.2) +33 ============
P = Topic("Future: will, going to, present continuous", **B,
    order=("*Will* = decision now, promise, opinion; *going to* = plan or what you see; Present Continuous = arrangement; Present Simple = timetable.", "*Will* = lēmums tagad, solījums, viedoklis; *going to* = plāns vai redzamais; Present Continuous = norunāts pasākums; Present Simple = saraksts."),
    bank=("After *when / as soon as / until / before* we use the Present Simple for the future.", "Pēc *when / as soon as / until / before* nākotnei lieto Present Simple."),
    gap=("After *when / as soon as / until* use the Present Simple; the main part takes *will*.", "Pēc *when / as soon as / until* lieto Present Simple; galvenajā daļā *will*."),
    text=("*Will*: *won't* + base verb. *Going to*: *Are / Is / Am* before the subject in questions.", "*Will*: *won't* + pamatforma. *Going to*: jautājumos *Are / Is / Am* ir pirms teik. priekšmeta."),
    mcq=("Choose by meaning: decision now, plan, prediction, arrangement or timetable.", "Izvēlies pēc nozīmes: lēmums tagad, plāns, prognoze, norunāts pasākums vai saraksts."),
    match=("Future forms by meaning.", "Nākotnes formas pēc nozīmes."))
for s,l in [("i'll call you as soon as i get there","B1.1"),("we're meeting at the station at six so don't be late","B1.1"),("the train leaves at seven so we should go now","B1.1"),("she says she will probably come to the party","B1.1"),("i think it's going to rain later","B1.1"),("they are going to open a new shop next year","B1.2"),("i'm going to ask my boss for a day off","B1.2"),("we won't be able to come if it snows heavily","B1.2"),("will you be at home when the parcel arrives","B1.2")]: P.order(l,s)
P.bank("B1.1","I ___ you when I get to the airport.","will text",["texting","am text"])
P.bank("B1.1","Don't worry, I ___ you with the luggage.","'ll help",["helping","helps"])
P.bank("B1.1","The sky is very dark. Look! It ___ rain very soon.","is going to",["will going","goes to"])
P.bank("B1.1","We ___ in Rome next week; the tickets are booked.","are staying",["staying","stays"])
P.bank("B1.2","I don't think the team ___ the match.","will win",["wins to","winning"])
P.bank("B1.2","As soon as she ___ the news, she will call you.","hears",["will hear","hearing"])
P.bank("B1.2","He ___ to see the doctor tomorrow at ten.","is going",["go","going"])
P.gap("B1.1","Don't worry. I ___ you the answer tomorrow. (send)","will send | 'll send")
P.gap("B1.1","The film ___ at eight, so let's meet at seven. (start)","starts")
P.gap("B1.2","Call me when you ___ . (arrive)","arrive")
P.gap("B1.2","We ___ the kitchen next month. We've already chosen the colour. (paint)","are going to paint | are painting")
P.text("B1.1","Make it negative: I will call you tonight.",["I won't call you tonight.","I will not call you tonight."])
P.text("B1.1","Make a question with going to: They / buy / a car?","Are they going to buy a car?")
P.text("B1.2","Join with when: I'll finish the report. Then I'll call you.",["I'll call you when I finish the report.","I'll call you when I've finished the report.","When I finish the report, I'll call you.","When I've finished the report, I'll call you."],b=5)
P.match("B1.1","Match each sentence with its use.",[("I'll help you with that.","an offer"),("I'm going to learn to drive.","a plan"),("It's going to rain.","a prediction from evidence"),("I'm meeting Jo at five.","an arrangement")])
P.match("B1.2","Match each beginning with its ending: time clauses.",[("I'll call you when","I get home."),("We'll leave as soon as","everyone is ready."),("Wait here until","I come back."),("I'll tell you after","I have spoken to her.")])
P.match("B1.2","Match each question with its answer: plans.",[("What are you doing tonight?","I'm seeing a film."),("Will you be late?","I might be."),("Are you going to apply?","Yes, I've decided."),("When does it start?","At half past six.")])
P.mcq("B1.1","Choose the correct option: My plane ___ at ten tomorrow, so I must leave early.","leaves",["leaving","left","is leave"])
P.mcq("B1.1","At the airport: which sentence is NOT correct?","I will to meet you at the gate.",["I'll meet you at the gate.","I'm meeting you at the gate.","I'm going to meet you at the gate."],"After *will* we use the base verb, without *to*.",b=4)
P.mcq("B1.2","Before the trip: which sentence is NOT correct?","When I will arrive, I'll text you.",["When I arrive, I'll text you.","I'll text you as soon as I arrive.","I'll text you when I arrive."],"After *when* we use the Present Simple for the future.",b=4)
P.mcq("B1.2","Choose the correct option: We ___ some friends for dinner on Saturday, so I need to go shopping.","are having",["had","are have","will having"])
P.mcq("B1.2","Which sentence is a promise?","I'll always be there for you.",["I'm always there for you.","I was there for you.","I'm going there for you."])
P.mcq("B1.2","Which sentence is a prediction based on what you can see?","Look out! That tree is going to fall!",["I think that tree will fall.","That tree fell.","That tree falls."],"We can see it now, so we use *going to*.",b=3)
save("b1-tenses-2.csv")
