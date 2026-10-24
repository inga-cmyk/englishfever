from lib import *
# ============ Present simple (+13) ============
P = Topic("Present simple",
    order=("Subject + verb (with -s after he / she / it) + the rest.", "Teikuma priekšmets + darbības vārds (ar *-s* aiz *he / she / it*) + pārējais."),
    bank=("Present simple: *-s* after *he / she / it*; *do / does* in questions and negatives.", "Present Simple: *-s* aiz *he / she / it*; *do / does* jautājumos un noliegumos."),
    gap=("After *he / she / it* the verb takes *-s* or *-es*; questions and negatives use *do / does* + base verb.", "Aiz *he / she / it* darbības vārdam pievieno *-s* vai *-es*; jautājumos un noliegumos lieto *do / does* + pamatforma."),
    text=("Negative: *do / does* + *not* + base verb. Question: *Do / Does* + subject + base verb.", "Noliegums: *do / does* + *not* + pamatforma. Jautājums: *Do / Does* + teik. priekšmets + pamatforma."),
    mcq=("*They* takes the base verb, *he / she / it* takes *-s*.", "Aiz *they* ir pamatforma, aiz *he / she / it* ir *-s*."),
    match=("", ""))
P.order("A2.1","my sister walks to school every day")
P.order("A2.2","do your parents work in the city")
P.order("A2.1","he doesn't eat meat on fridays")
P.order("A2.2","what time does the lesson start")
P.bank("A2.1","My dad ___ the dishes after dinner.","washes",["wash","washing"])
P.bank("A2.1","___ your cousins live near you?","Do",["Does","Are"])
P.bank("A2.1","Tom ___ like spicy food.","doesn't",["don't","isn't"])
P.bank("A2.2","Ben ___ up at six, but his sisters ___ up at eight.",["gets","get"],["getting","is get"])
P.gap("A2.1","My neighbour ___ his car every Saturday. (wash)","washes")
P.gap("A2.2","How often ___ she ___ her grandmother? (visit)","does / visit")
P.gap("A2.2","I ___ coffee, but my wife loves it. (not / like)","don't like | do not like")
P.text("A2.1","Make it negative: The bus stops here.",["The bus doesn't stop here.","The bus does not stop here."])
P.mcq("A2.1","Choose the correct form: Lucy and her brother ___ to the same school.","go",["goes","going","are go"])
# ============ Present continuous (+15) ============
P = Topic("Present continuous",
    order=("Subject + *am / is / are* + verb + *-ing* + the rest.", "Teikuma priekšmets + *am / is / are* + darbības vārds + *-ing* + pārējais."),
    bank=("Now: *am / is / are* + verb + *-ing*.", "Tagad: *am / is / are* + darbības vārds + *-ing*."),
    gap=("Now: *am / is / are* + verb + *-ing*.", "Tagad: *am / is / are* + darbības vārds + *-ing*."),
    text=("Question: *am / is / are* before the subject. Negative: *not* after *am / is / are*.", "Jautājums: *am / is / are* pirms teik. priekšmeta. Noliegums: *not* aiz *am / is / are*."),
    mcq=("*Right now* shows an action in progress: *am / is / are* + verb + *-ing*.", "*Right now* parāda darbību, kas norit: *am / is / are* + darbības vārds + *-ing*."),
    match=("", ""))
P.order("A2.1","the children are playing in the garden")
P.order("A2.1","we are waiting for the bus")
P.order("A2.2","what are you reading at the moment")
P.order("A2.2","my brother isn't working today")
P.order("A2.1","is it raining in your city")
P.bank("A2.1","Look! The cat ___ on the sofa.","is sleeping",["sleeping","are sleeping","sleep"])
P.bank("A2.1","We ___ dinner at the moment.","are having",["having","has"])
P.bank("A2.2","Why ___ you ___ at me?",["are","looking"],["is","look"])
P.bank("A2.1","I ___ a letter to my friend now.","am writing",["wrote","writes"])
P.bank("A2.2","The students ___ not ___ because the teacher is late.",["are","studying"],["is","studied"])
P.gap("A2.1","Shh! My father ___ on the phone. (talk)","is talking")
P.gap("A2.1","Where ___ they ___ today? (go)","are / going")
P.gap("A2.2","She ___ her hair at the moment. (not / dry)","isn't drying | is not drying")
P.text("A2.1","Make a question: Your sister is waiting outside.","Is your sister waiting outside?")
P.mcq("A2.1","Choose the correct form: Right now my parents ___ in the garden.","are working",["work","works","is working"])
# ============ Past simple (+14) ============
P = Topic("Past simple",
    order=("Subject + past verb + the rest. Questions: *Did* + subject + base verb.", "Teikuma priekšmets + pagātnes forma + pārējais. Jautājumi: *Did* + teik. priekšmets + pamatforma."),
    bank=("Finished time: past form (*-ed* or irregular). After *did / didn't* the verb is in the base form.", "Pabeigts laiks: pagātnes forma (*-ed* vai neregulāra). Pēc *did / didn't* darbības vārds ir pamatformā."),
    gap=("Finished time: past form. After *did / didn't* use the base form.", "Pabeigts laiks: pagātnes forma. Pēc *did / didn't* lieto pamatformu."),
    text=("Negative: *didn't* + base verb. Question: *Did* + subject + base verb; *When / Where / Why* go first.", "Noliegums: *didn't* + pamatforma. Jautājums: *Did* + teik. priekšmets + pamatforma; *When / Where / Why* ir pirmajā vietā."),
    mcq=("A finished time in the past: past simple.", "Pabeigts laiks pagātnē: Past Simple."),
    match=("", ""))
P.order("A2.1","we visited our grandparents last weekend")
P.order("A2.2","did you see the match yesterday")
P.order("A2.1","she didn't answer the phone")
P.order("A2.2","where did they go on holiday")
P.bank("A2.1","Last night I ___ a good film.","watched",["watch","watching"])
P.bank("A2.2","___ you ___ your homework yesterday?",["Did","do"],["Does","done","doing"])
P.bank("A2.2","She ___ a cake and ___ it to school.",["made","took"],["make","take"])
P.bank("A2.2","They ___ at home because it ___ cold.",["stayed","was"],["stay","were"])
P.gap("A2.1","We ___ a taxi to the station. (take)","took")
P.gap("A2.1","I ___ the news on TV last night. (not / see)","didn't see | did not see")
P.gap("A2.2","What time ___ the film ___ last night? (start)","did / start")
replaces("What time ___ the film ___ ? (start)")
P.text("A2.1","Make it negative: She bought a new bag.",["She didn't buy a new bag.","She did not buy a new bag."])
P.text("A2.2","Make a question with When: They arrived.","When did they arrive?")
P.mcq("A2.1","Choose the correct form: My grandparents ___ in a small village when they were young.","lived",["live","lives","were live"])
# ============ Past continuous (+32) ============
P = Topic("Past continuous",
    order=("Subject + *was / were* + verb + *-ing* + the rest.", "Teikuma priekšmets + *was / were* + darbības vārds + *-ing* + pārējais."),
    bank=("An action in progress in the past: *was / were* + verb + *-ing*.", "Darbība, kas pagātnē norisinājās: *was / were* + darbības vārds + *-ing*."),
    gap=("An action in progress in the past: *was / were* + verb + *-ing*.", "Darbība, kas pagātnē norisinājās: *was / were* + darbības vārds + *-ing*."),
    text=("Question: *was / were* before the subject. Negative: *not* after *was / were*.", "Jautājums: *was / were* pirms teik. priekšmeta. Noliegums: *not* aiz *was / were*."),
    mcq=("The action was in progress at that moment: *was / were* + verb + *-ing*.", "Darbība tajā brīdī norisinājās: *was / were* + darbības vārds + *-ing*."),
    match=("*Was / were* + *-ing* shows what was in progress; *when* introduces the short event.", "*Was / were* + *-ing* parāda, kas norisinājās; *when* ievada īso notikumu."))
for s,l in [("it was raining when we left the house","A2.2"),("they were playing football at six","A2.2"),("what were you doing at nine last night","A2.2"),("i was cooking while my brother was watching tv","A2.2"),("she wasn't listening to the teacher","A2.2"),("were you sleeping when i called","A2.2"),("the sun was shining and the birds were singing","A2.2"),("we were walking home when it started to rain","A2.2")]: P.order(l,s)
P.bank("A2.2","At eight o'clock I ___ my homework.","was doing",["doing","am doing"])
P.bank("A2.2","They ___ lunch when the phone rang.","were having",["having","was having"])
P.bank("A2.2","While Mum ___ dinner, Dad ___ the table.",["was cooking","was setting"],["were cooking","were setting"])
P.bank("A2.2","___ you ___ when I knocked?",["Were","sleeping"],["Was","sleep"])
P.bank("A2.2","The children ___ in the garden when it started to rain.","were playing",["playing","was playing"])
P.bank("A2.2","She ___ a book when the lights went out.","was reading",["reading","were reading"])
P.bank("A2.2","We ___ for the bus when it began to snow.","were waiting",["waiting","was waiting"])
P.bank("A2.2","It ___ heavily when we left, so we took umbrellas.","was raining",["raining","were raining"])
P.gap("A2.2","At midnight they ___ . (sleep)","were sleeping")
P.gap("A2.2","What ___ she ___ at seven? (do)","was / doing")
P.gap("A2.2","I ___ TV when you called. (not / watch)","wasn't watching | was not watching")
P.gap("A2.2","The boys ___ football when it began to rain. (play)","were playing")
P.gap("A2.2","___ it ___ when you left home? (rain)","Was / raining")
P.text("A2.2","Make a question: They were waiting for a taxi.","Were they waiting for a taxi?")
P.text("A2.2","Make it negative: We were talking.",["We weren't talking.","We were not talking."])
P.text("A2.2","Join with when: I was walking home. It started to rain.",["I was walking home when it started to rain.","When it started to rain, I was walking home.","When I was walking home, it started to rain.","It started to rain when I was walking home."],b=4)
P.match("A2.2","Match each beginning with its ending.",[("I was cooking","dinner in the kitchen."),("They were playing","tennis in the park."),("She was reading","a newspaper on the sofa."),("We were watching","a film on TV.")],("*Was / were* + *-ing* shows what was in progress.","*Was / were* + *-ing* parāda, kas norisinājās."))
P.match("A2.2","Match each question with its answer.",[("What were you doing?","I was cleaning my room."),("Was it raining?","Yes, it was."),("Were they sleeping?","No, they weren't."),("Who was she talking to?","Her brother.")])
P.mcq("A2.2","Choose the correct form: While I ___ a bath, the phone rang.","was taking",["take","am taking","were taking"],b=3)
P.mcq("A2.2","Choose the correct form: ___ you ___ at ten o'clock last night?","Were / working",["Did / working","Was / work","Are / working"],b=3)
P.mcq("A2.2","About last night: which sentence is NOT correct?","We was watching a film.",["We were watching a film.","I was sleeping at midnight.","They were talking on the phone."],"*We* goes with *were*, not *was*.",b=4)
P.mcq("A2.2","Choose the correct word: She ___ listening, so she did not hear the question.","wasn't",["didn't","weren't","isn't"],"*Wasn't listening* = she was not in the middle of listening.",b=3)
P.mcq("A2.2","Which sentence describes an action in progress at a moment in the past?","At 7 p.m. I was cooking dinner.",["I cooked dinner last night.","I will cook dinner at seven.","I cook dinner every day."],b=2)
P.mcq("A2.2","Choose the correct form: The students ___ when the teacher walked in.","were talking",["talking","was talking","are talking"],b=3)
# ============ Present perfect (+28) ============
P = Topic("Present perfect",
    order=("Subject + *have / has* + 3. form + the rest.", "Teikuma priekšmets + *have / has* + 3. forma + pārējais."),
    bank=("Present perfect: *have / has* + 3. form. *Just, already, yet, ever, never* go with it.", "Present Perfect: *have / has* + 3. forma. Ar to lieto *just, already, yet, ever, never*."),
    gap=("Present perfect: *have / has* + 3. form.", "Present Perfect: *have / has* + 3. forma."),
    text=("Question: *Have / Has* + subject + 3. form. Negative: *haven't / hasn't* + 3. form.", "Jautājums: *Have / Has* + teik. priekšmets + 3. forma. Noliegums: *haven't / hasn't* + 3. forma."),
    mcq=("Present perfect: an experience or a result now, with no finished time.", "Present Perfect: pieredze vai rezultāts tagad, bez pabeigta laika."),
    match=("Short answers repeat *have / has*.", "Īsās atbildes atkārto *have / has*."))
for s in ["i have never eaten snails","she has just finished her homework","have you ever been to london","we haven't seen that film yet","my brother has already left for work","has he called you today"]: P.order("A2.2",s)
P.bank("A2.2","I have ___ a bike, but I have never ridden a horse.","ridden",["rode","ride"]) if False else None
P.bank("A2.2","She has ___ her keys, so she can't open the door.","lost",["lose","losing"])
P.bank("A2.2","___ you ___ your lunch yet?",["Have","eaten"],["Has","ate","eat"])
P.bank("A2.2","They ___ never ___ to Italy.",["have","been"],["has","was","go"])
P.bank("A2.2","He ___ just ___ a new phone.",["has","bought"],["have","buy","buys"])
P.bank("A2.2","We ___ already ___ the dishes.",["have","washed"],["has","washing"])
P.bank("A2.2","I haven't ___ my sister for a month.","seen",["saw","see"])
P.bank("A2.2","Has your teacher ever ___ you a hard test?","given",["gave","give"])
P.gap("A2.2","They ___ a lot of photos this week. (take)","have taken")
P.gap("A2.2","She ___ to Spain twice. (be)","has been")
P.gap("A2.2","I ___ my phone. Can you help me look? (lose)","have lost")
P.gap("A2.2","___ he ___ the report yet? (finish)","Has / finished")
P.gap("A2.2","We ___ here since Monday. (not / be)","haven't been | have not been")
P.text("A2.2","Make a question with ever: She has met a famous person.","Has she ever met a famous person?")
P.text("A2.2","Make it negative: He has finished his work.",["He hasn't finished his work.","He has not finished his work."])
P.text("A2.2","Make a question: They have arrived.","Have they arrived?")
P.mcq("A2.2","Choose the correct form: My brother ___ his passport, so he can't travel.","has lost",["have lost","is losing","has losing"],b=3)
P.mcq("A2.2","Choose the correct word: I have ___ been to Japan. It is on my list.","never",["ago","last","yesterday"],b=2)
P.mcq("A2.2","Choose the correct word: She has ___ cleaned the kitchen, so it looks great.","just",["ago","tomorrow","last"],b=2)
P.mcq("A2.2","About experiences: which sentence is NOT correct?","I have seen that film last week.",["I have seen that film twice.","I saw that film last week.","Have you seen that film?"],"With *last week* (a finished time) we use the past simple.",b=4)
P.mcq("A2.2","Choose the correct meaning: 'Our guests have arrived.'","They are here now.",["They will arrive tomorrow.","They arrived last year.","They are not here."],b=2)
P.mcq("A2.2","Choose the correct form: ___ your parents ever ___ to a concert?","Have / been",["Has / been","Did / be","Are / been"],b=3)
P.match("A2.2","Match each question with its answer.",[("Have you seen Tom?","No, I haven't."),("Has she called you?","Yes, she has."),("Have they finished?","No, they haven't."),("Has he ever been abroad?","Yes, he has.")],b=2)
P.match("A2.2","Match each beginning with its ending.",[("I have never tried","Indian food."),("She has just painted","the kitchen."),("We have already booked","the tickets."),("They haven't answered","our emails yet.")],("*Have / has* + 3. form: *have tried*, *has painted*, *have booked*.","*Have / has* + 3. forma: *have tried*, *has painted*, *have booked*."),b=2)
P.match("A2.2","Match each verb with its 3. form.",[("write","written"),("take","taken"),("see","seen"),("go","gone")],("Irregular verbs: learn the 3. form with the verb.","Neregulārie darbības vārdi: iemācies 3. formu kopā ar darbības vārdu."),b=1)
P.text("A2.2","Say you did not do it yet: I / not / finish / homework / yet.",["I haven't finished my homework yet.","I have not finished my homework yet."],b=4)
# ============ Future (+17) ============
P = Topic("Future: will, going to, present continuous",
    order=("Plan: *am / is / are going to* + verb. Decision now or promise: *will* + verb.", "Plāns: *am / is / are going to* + darbības vārds. Lēmums tagad vai solījums: *will* + darbības vārds."),
    bank=("*Going to* = plan or what you can see; *will* = decision now, promise or opinion; present continuous = arrangement.", "*Going to* = plāns vai redzamais; *will* = lēmums tagad, solījums vai viedoklis; Present Continuous = norunāts pasākums."),
    gap=("*Going to* = plan; *will* = decision now or opinion.", "*Going to* = plāns; *will* = lēmums tagad vai viedoklis."),
    text=("*Going to*: *am / is / are* + not + going to + verb. *Will*: *won't* + verb.", "*Going to*: *am / is / are* + not + going to + darbības vārds. *Will*: *won't* + darbības vārds."),
    mcq=("Choose by meaning: plan, decision now, prediction or arrangement.", "Izvēlies pēc nozīmes: plāns, lēmums tagad, prognoze vai norunāts pasākums."),
    match=("", ""))
for s,l in [("we are going to buy a new sofa","A2.1"),("what are you going to do tonight","A2.1"),("i'm not going to watch tv this evening","A2.1"),("it will be sunny tomorrow","A2.2"),("i'll help you with your bags","A2.2"),("she is meeting her friends at seven","A2.2")]: P.order(l,s)
P.bank("A2.1","My parents ___ a trip to Spain next month.","are going to take",["go to take","going to take"])
P.bank("A2.1","I ___ study hard for the exam.","am going to",["going to","will to"])
P.bank("A2.2","Oh, no! I forgot my wallet. I ___ go back and get it.","'ll",["am going","going to"])
P.bank("A2.2","Look at the sky! It ___ snow.","is going to",["will to","goes to"])
P.gap("A2.1","He ___ a new job next week. (start)","is going to start")
P.gap("A2.2","I think the test ___ difficult. (not / be)","won't be | will not be")
P.gap("A2.2","We ___ dinner with our friends on Friday. They are coming at eight. (have)","are having")
P.text("A2.2","Make a question with going to: What / you / do / tomorrow?","What are you going to do tomorrow?")
P.mcq("A2.2","Choose the correct option: 'The shop is closed.' 'OK, I ___ come back tomorrow.'","'ll",["am going","came","coming"],b=3)
P.mcq("A2.1","Choose the correct form: Anna ___ a doctor when she grows up.","is going to be",["going to be","will to be","is going be"],b=2)
P.mcq("A2.2","A man carries a very full cup. Which sentence is a prediction?","He's going to spill it.",["He'll make some coffee.","He's meeting Jo at six.","He hopes to drink less."],"We can see it now, so we use *going to*.",b=3)
P.match("A2.2","Match each sentence with its meaning.",[("I'll carry that for you.","an offer"),("I'm going to learn French.","a plan"),("It's going to rain.","a prediction from what I see"),("I'm seeing the dentist at 4.","an arrangement")],("*'ll* = offer, *going to* = plan or what I see, Present Continuous = arrangement.","*'ll* = piedāvājums, *going to* = plāns vai redzamais, Present Continuous = norunāts pasākums."),b=2)
P.match("A2.1","Match each beginning with its ending.",[("We are going to visit","our aunt on Sunday."),("She is going to buy","a new bike."),("They aren't going to eat","fish tonight."),("Are you going to play","football today?")],("Plan: *am / is / are* + *going to* + base verb.","Plāns: *am / is / are* + *going to* + pamatforma."),b=2)
P.text("A2.1","Make it negative: We are going to leave early.",["We aren't going to leave early.","We are not going to leave early.","We're not going to leave early."],b=4)
P.mcq("A2.2","About tomorrow: which sentence is NOT correct?","I will to call you tomorrow.",["I'll call you tomorrow.","I'm going to call you tomorrow.","I'm calling you tomorrow at five."],"After *will* we use the base verb, without *to*.",b=4)
# ============ Present simple passive (+28) ============
P = Topic("Present simple passive",
    order=("Subject + *is / are* + 3. form (+ *by* ...).", "Teikuma priekšmets + *is / are* + 3. forma (+ *by* ...)."),
    bank=("Ciešamā kārta (passive): *is / are* + 3. form.", "Ciešamā kārta: *is / are* + 3. forma."),
    gap=("Passive: *is / are* + 3. form.", "Ciešamā kārta: *is / are* + 3. forma."),
    text=("Passive: the object becomes the subject: *is / are* + 3. form.", "Ciešamā kārta: papildinātājs kļūst par teikuma priekšmetu: *is / are* + 3. forma."),
    mcq=("Passive: *is / are* + 3. form, because the action matters more than who does it.", "Ciešamā kārta: *is / are* + 3. forma, jo darbība ir svarīgāka par darītāju."),
    match=("Passive: *is / are* + 3. form.", "Ciešamā kārta: *is / are* + 3. forma."))
for s in ["milk is sold in every shop","the rooms are cleaned every morning","english is spoken all over the world","is this road used by many cars","these bananas are grown in ecuador","bread isn't made here"]: P.order("A2.2",s)
P.bank("A2.2","Pizza ___ in Italy and all over the world.","is eaten",["eats","eat"])
P.bank("A2.2","These toys ___ in China.","are made",["is made","make"])
P.bank("A2.2","___ the shops closed on Sundays?","Are",["Do","Is"])
P.bank("A2.2","Our homework ___ on the website every week.","is posted",["posts","are posted"])
P.bank("A2.2","Coffee ___ in Brazil.","is grown",["grows","are grown"])
P.bank("A2.2","The tickets ___ at the station.","are sold",["is sold","selling"])
P.gap("A2.2","The mail ___ at ten every day. (bring)","is brought")
P.gap("A2.2","Cheese ___ from milk. (make)","is made")
P.gap("A2.2","These books ___ by children. (read)","are read")
P.gap("A2.2","Where ___ the cars ___ ? (build)","are / built")
P.text("A2.2","Make it passive: They clean the streets every night.","The streets are cleaned every night.")
P.text("A2.2","Make it negative: This room is used on Sundays.",["This room isn't used on Sundays.","This room is not used on Sundays."])
P.text("A2.2","Make a question: Tea is sold here.","Is tea sold here?")
P.mcq("A2.2","Choose the correct form: Rice ___ in Asia.","is grown",["growing","is grow","are grown"],b=2)
P.mcq("A2.2","Choose the correct form: The cinema ___ every evening at ten.","is closed",["closing","are closed","is close"],b=2)
P.mcq("A2.2","Read about the shop: which sentence is passive?","Paper is made from wood.",["People make paper from wood.","Wood makes paper.","We make paper at school."],b=2)
P.mcq("A2.2","In the shop: which sentence is NOT correct?","The bread are baked every morning.",["The bread is baked every morning.","The rolls are baked every morning.","Cakes are sold here."],"*Bread* is uncountable: *is baked*.",b=4)
P.mcq("A2.2","Choose the correct question: ___ your phone made in Korea?","Is",["Does","Are","Do"],b=3)
P.match("A2.2","Match each product with where it is made.",[("Watches","Switzerland"),("Cars","Germany"),("Pasta","Italy"),("Tea","India")],("Say *Watches are made in Switzerland*: *are* + 3. form.","Saka *Watches are made in Switzerland*: *are* + 3. forma."),b=2)
P.match("A2.2","Match each beginning with its ending.",[("Letters are delivered","by the postman."),("Meals are cooked","by the chef."),("Lessons are taught","by the teachers."),("Planes are flown","by pilots.")],b=2)
P.order("A2.2","are the windows cleaned every week")
P.order("A2.2","this song is played on the radio")
P.bank("A2.2","Newspapers ___ at the corner shop.","are sold",["selling","is sold"])
P.gap("A2.2","The floors ___ twice a week. (wash)","are washed")
P.text("A2.2","Make it passive: People use phones everywhere.","Phones are used everywhere.")
P.mcq("A2.2","Choose the correct form: Many languages ___ in our school.","are taught",["teach","is taught","are teach"],b=2)
# ============ Past simple passive (+28) ============
P = Topic("Past simple passive",
    order=("Subject + *was / were* + 3. form (+ *by* ...).", "Teikuma priekšmets + *was / were* + 3. forma (+ *by* ...)."),
    bank=("Ciešamā kārta, Past Simple: *was / were* + 3. form.", "Ciešamā kārta, Past Simple: *was / were* + 3. forma."),
    gap=("Past passive: *was / were* + 3. form.", "Ciešamā kārta pagātnē: *was / were* + 3. forma."),
    text=("Past passive: the object becomes the subject: *was / were* + 3. form.", "Ciešamā kārta pagātnē: papildinātājs kļūst par teikuma priekšmetu: *was / were* + 3. forma."),
    mcq=("Past passive: *was / were* + 3. form, because the action matters more than who did it.", "Ciešamā kārta pagātnē: *was / were* + 3. forma, jo darbība ir svarīgāka par darītāju."),
    match=("Past passive: *was / were* + 3. form.", "Ciešamā kārta pagātnē: *was / were* + 3. forma."))
for s in ["the car was repaired yesterday","my phone was stolen on the bus","these pictures were painted by children","was the letter sent last week","the thieves weren't caught","the museum was opened in 1990"]: P.order("A2.2",s)
P.bank("A2.2","The cake ___ by my grandmother.","was made",["made","were made"])
P.bank("A2.2","Two windows ___ in the storm.","were broken",["was broken","breaking"])
P.bank("A2.2","___ the film shot in Spain?","Was",["Did","Were"])
P.bank("A2.2","This song ___ in 1985.","was written",["wrote","were written"])
P.bank("A2.2","The prizes ___ to the best students.","were given",["gave","was given"])
P.bank("A2.2","My bag ___ at the airport.","was found",["found","were found"])
P.gap("A2.2","The match ___ because of rain. (cancel)","was cancelled | was canceled")
P.gap("A2.2","The guests ___ at the door by the manager. (meet)","were met")
P.gap("A2.2","When ___ this bridge ___ ? (build)","was / built")
P.gap("A2.2","The letters ___ yesterday. (not / post)","weren't posted | were not posted")
P.text("A2.2","Make it passive: Someone broke the window.","The window was broken.")
P.text("A2.2","Make it negative: The door was locked.",["The door wasn't locked.","The door was not locked."])
P.text("A2.2","Make a question: The letter was sent.","Was the letter sent?")
P.mcq("A2.2","Choose the correct form: The thief ___ by the police yesterday.","was caught",["caught","is caught","were caught"],b=2)
P.mcq("A2.2","Choose the correct form: These shoes ___ in a small factory.","were made",["was made","made","are make"],b=2)
P.mcq("A2.2","Read about the news: which sentence is passive?","The shop was robbed last night.",["Someone robbed the shop last night.","The robbers took the money.","We went to the shop last night."],b=2)
P.mcq("A2.2","On the news: which sentence is NOT correct?","The bridge was destroy in the storm.",["The bridge was destroyed in the storm.","Two roads were closed.","The town was flooded."],"After *was* we need the 3. form: *destroyed*.",b=4)
P.mcq("A2.2","Choose the correct question: Where ___ this photo ___ ?","was / taken",["did / taken","is / take","were / took"],b=3)
P.match("A2.2","Match each famous thing with who made it.",[("Hamlet","was written by Shakespeare."),("The Mona Lisa","was painted by Leonardo."),("The telephone","was invented by Bell."),("Harry Potter","was written by Rowling.")],("Past passive: *was* + 3. form + *by* + the maker.","Ciešamā kārta pagātnē: *was* + 3. forma + *by* + autors."),b=2)
P.match("A2.2","Match each beginning with its ending.",[("The window","was broken by a ball."),("The cake","was baked by my mother."),("The film","was directed by a famous director."),("The bike","was stolen by a thief.")],b=2)
P.order("A2.2","the doors were locked at nine")
P.order("A2.2","this house was built in 1920")
P.bank("A2.2","The room ___ before the guests arrived.","was cleaned",["cleaned","were cleaned"])
P.gap("A2.2","The film ___ in London. (shoot)","was shot")
P.text("A2.2","Make it passive: A famous artist painted this picture.","This picture was painted by a famous artist.")
P.mcq("A2.2","Choose the correct form: The new teacher ___ to the class yesterday.","was introduced",["introduced","were introduced","is introduced"],b=2)
# ============ Zero conditional (+36) ============
P = Topic("Zero conditional (if + present, present)",
    order=("*If* + Present Simple, Present Simple: something that is always true.", "*If* + Present Simple, Present Simple: kaut kas, kas vienmēr ir patiesi."),
    bank=("Always true: Present Simple in the *if* part and in the result.", "Vienmēr patiesi: Present Simple gan *if* daļā, gan rezultātā."),
    gap=("Always true: Present Simple in both parts.", "Vienmēr patiesi: abās daļās Present Simple."),
    text=("Always true: Present Simple in both parts; *if* can start or end the sentence.", "Vienmēr patiesi: abās daļās Present Simple; *if* var būt teikuma sākumā vai beigās."),
    mcq=("Always true: Present Simple in both parts, no *will*.", "Vienmēr patiesi: abās daļās Present Simple, bez *will*."),
    match=("Always true: Present Simple in both parts.", "Vienmēr patiesi: abās daļās Present Simple."))
for s in ["if you heat ice it melts","if i drink coffee at night i can't sleep","plants die if they don't get water","if it rains the streets get wet","if you press this key the page goes down","when the sun goes down it gets cold","if you don't eat you feel hungry","if you add salt the soup tastes better"]: P.order("A2.2",s)
P.bank("A2.2","If you ___ metal, it gets hot.","heat",["will heat","heating"])
P.bank("A2.2","If I ___ too much coffee, I can't sleep.","drink",["will drink","drinking"])
P.bank("A2.2","Water ___ if the temperature goes below zero.","freezes",["will freeze","freezing"])
P.bank("A2.2","If you ___ a cold, you often feel tired.","have",["will have","having"])
P.bank("A2.2","When it ___ , the grass grows.","rains",["will rain","raining"])
P.bank("A2.2","If you ___ butter in the sun, it melts.","leave",["will leave","leaving"])
P.bank("A2.2","If people ___ enough, they get ill.","don't sleep",["won't sleep","not sleeping"])
P.bank("A2.2","The ice ___ if you put it in a warm room.","melts",["will melt","melting"])
P.gap("A2.2","If you ___ water to 100 degrees, it boils. (heat)","heat")
P.gap("A2.2","If my phone ___ hot, I turn it off. (get)","gets")
P.gap("A2.2","If I ___ my keys, I can't open the door. (lose)","lose")
P.gap("A2.2","Birds ___ south if the winter is cold. (fly)","fly")
P.gap("A2.2","If you ___ a lot, you feel better. (exercise)","exercise")
P.gap("A2.2","If the lights ___ off, the room gets dark. (go)","go")
P.text("A2.2","Join with if: You mix red and blue. You get purple.",["If you mix red and blue, you get purple.","You get purple if you mix red and blue."])
P.text("A2.2","Join with if: You don't water plants. They die.",["If you don't water plants, they die.","Plants die if you don't water them."])
P.text("A2.2","Join with if: It gets cold. Water turns into ice.",["If it gets cold, water turns into ice.","Water turns into ice if it gets cold."])
P.mcq("A2.2","Choose the correct form: If you ___ ice, it melts.","heat",["will heat","heating","would heat"],b=2)
P.mcq("A2.2","Choose the correct form: If the sun ___ , the day gets warmer.","shines",["will shine","shining","would shine"],b=2)
P.mcq("A2.2","Choose the correct form: Plants ___ if you don't give them water.","die",["will died","dying","dies"],b=2)
P.mcq("A2.2","Which sentence is always true?","If you drop a glass, it breaks.",["If you drop the glass, I will be angry.","If I drop the glass, I will buy a new one.","If I dropped the glass, I would be sorry."],b=2)
P.mcq("A2.2","In science class: which sentence is NOT correct?","If you will mix oil and water, they separate.",["If you mix oil and water, they separate.","If you heat water, it boils.","If you cool water enough, it freezes."],"No *will* after *if* in a general truth.",b=4)
P.mcq("A2.2","Choose the correct word: ___ you push the button, the door opens.","If",["Unless","Because","Until"],b=2)
P.match("A2.2","Match each beginning with its ending.",[("If you heat ice,","it melts."),("If you cool water,","it freezes."),("If you drop a glass,","it breaks."),("If you press the light switch,","the light goes on.")],b=2)
P.match("A2.2","Match each beginning with its ending: feelings and weather.",[("If I eat too much,","I feel sick."),("If it rains,","the roads are wet."),("If I don't sleep,","I'm tired all day."),("If I run fast,","I get hot.")],b=2)
P.order("A2.2","if i run fast i get hot")
P.order("A2.2","the soup gets cold if you leave it")
P.bank("A2.2","If a baby ___ hungry, it cries.","is",["will be","being"])
P.gap("A2.2","If you ___ the cat's tail, it gets angry. (pull)","pull")
P.text("A2.2","Join with when: The sun comes up. It gets warmer.",["When the sun comes up, it gets warmer.","It gets warmer when the sun comes up."])
P.mcq("A2.2","Choose the correct form: If I ___ sad, I listen to music.","feel",["will feel","feeling","would feel"],b=2)
# ============ First conditional (+31) ============
P = Topic("First conditional (if + present, will)",
    order=("*If* + Present Simple, *will* + base verb: a possible future.", "*If* + Present Simple, *will* + pamatforma: iespējama nākotne."),
    bank=("Possible future: *if* + Present Simple, *will* + base verb. No *will* after *if*.", "Iespējama nākotne: *if* + Present Simple, *will* + pamatforma. Pēc *if* nav *will*."),
    gap=("Possible future: *if* + Present Simple, *will* + base verb.", "Iespējama nākotne: *if* + Present Simple, *will* + pamatforma."),
    text=("Possible future: *if* + Present Simple, *will* + base verb.", "Iespējama nākotne: *if* + Present Simple, *will* + pamatforma."),
    mcq=("Possible future: *if* + Present Simple, *will* + base verb.", "Iespējama nākotne: *if* + Present Simple, *will* + pamatforma."),
    match=("Possible future: *if* + Present Simple, *will* + base verb.", "Iespējama nākotne: *if* + Present Simple, *will* + pamatforma."))
for s in ["if it snows we will build a snowman","i will lend you my book if you ask","if you don't hurry you will miss the train","she will be happy if you call her","if we win the game we'll celebrate","they won't come if it rains"]: P.order("A2.2",s)
P.bank("A2.2","If I ___ time tomorrow, I will call you.","have",["will have","having"])
P.bank("A2.2","We ___ late if we don't leave now.","will be",["being","would be"])
P.bank("A2.2","If you ___ the exam, your parents will be proud.","pass",["will pass","passing"])
P.bank("A2.2","If it ___ tonight, we won't go out.","rains",["will rain","raining"])
P.bank("A2.2","She ___ you if you ask her nicely.","will help",["helping","would help"])
P.bank("A2.2","If they ___ early, they will get good seats.","arrive",["will arrive","arriving"])
P.gap("A2.2","If she ___ the bus, she will be late. (miss)","misses")
P.gap("A2.2","I ___ you a message if I get there first. (send)","will send | 'll send")
P.gap("A2.2","If you ___ hard, you will succeed. (work)","work")
P.gap("A2.2","They ___ angry if we forget their birthday. (be)","will be | 'll be")
P.gap("A2.2","If he ___ his phone, he will call us. (find)","finds")
P.gap("A2.2","What ___ you do if you lose your keys? (will)","will")
P.text("A2.2","Join with if: You help me. I will help you.",["If you help me, I will help you.","I will help you if you help me."])
P.text("A2.2","Join with if: You are late. We will start without you.",["If you are late, we will start without you.","We will start without you if you are late."])
P.text("A2.2","Make it negative: If she comes, I will stay.",["If she doesn't come, I won't stay.","If she does not come, I will not stay."],b=4)
P.mcq("A2.2","Choose the correct form: If we ___ the film, we will tell you about it.","see",["will see","seeing","would see"],b=2)
P.mcq("A2.2","Choose the correct form: If you ___ now, you'll catch the early train.","leave",["will leave","leaving","would leave"],b=2)
P.mcq("A2.2","Which sentence is a promise?","If you tell me, I won't tell anyone.",["If you told me, I wouldn't tell anyone.","If I tell you, will you tell me?","I never tell anyone."],b=3)
P.mcq("A2.2","At the weekend: which sentence is NOT correct?","If it will be sunny, we will go to the beach.",["If it is sunny, we will go to the beach.","We will go to the beach if it is sunny.","If it rains, we'll stay home."],"No *will* after *if*.",b=4)
P.mcq("A2.2","Choose the correct word: ___ you hurry, you will miss the bus.","If you don't",["Unless you","If you won't","When you didn't"],b=3) if False else None
P.mcq("A2.2","Choose the best ending: If you study every day, ...","you will pass the test.",["you passed the test.","you passing the test.","you pass yesterday."],b=2)
P.match("A2.2","Match each beginning with its ending: if-sentences.",[("If it rains,","we'll take an umbrella."),("If you're thirsty,","I'll make some tea."),("If she calls,","I'll answer the phone."),("If the shop is open,","we'll buy bread.")],b=2)
P.match("A2.2","Match each promise with its if-part.",[("I'll carry your bag","if it is heavy."),("I'll take an umbrella","if it rains."),("I'll tell you the result","if I get the news."),("I'll buy you a drink","if you win.")],b=2)
P.order("A2.2","if you eat that you will feel sick")
P.order("A2.2","we won't go if it's too cold")
P.bank("A2.2","If you ___ me, I'll tell you a secret.","help",["will help","helping"])
P.gap("A2.2","If the shop ___ closed, we will try another one. (be)","is")
P.text("A2.2","Join with if: You are ill. You will stay at home.",["If you are ill, you will stay at home.","You will stay at home if you are ill."])
P.mcq("A2.2","Choose the correct form: If it ___ cold tomorrow, I'll wear a coat.","is",["will be","being","would be"],b=2)
save("a2-big-1.csv")
