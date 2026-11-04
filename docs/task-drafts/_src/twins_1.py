"""Twins, batch 1 (teacher, 3 November, option B): the topics and levels with fewer than 10 check / use tasks get tasks that are
very like the existing ones but in another setting (travel, work, hobbies, lifestyle, learning, relationships, technologies).
Wrong options are ungrammatical, of one length, all about one theme (or each about its own); no speaker tag before a gap that
already names the speaker. Saved to pending/ until the teacher has seen them."""
from lib import *

MV = Topic("Modal verbs")
PAST_OBL = ("A past obligation: *had to*. *Must* has no past form.", "Pagātnes pienākums: *had to*. *Must* nav pagātnes formas.")
MV.mcq("B1.1", "Choose the correct option: We ___ wait two hours at the airport last night.", "had to", ["must", "have to"], why=PAST_OBL)
MV.mcq("B1.1", "Choose the correct option: I ___ finish the report before the meeting yesterday.", "had to", ["must", "have to"], why=PAST_OBL)
MV.mcq("B1.1", "Choose the correct option: She ___ call the bank tomorrow morning.", "will have to", ["will must", "will has to"],
       why=("A future obligation: *will have to*. *Must* cannot follow *will*.", "Nākotnes pienākums: *will have to*. Aiz *will* nevar lietot *must*."))
MV.text("B1.1", "Correct the sentence. Keep *will*: We will can visit you next summer.",
        ["We will be able to visit you next summer.", "We'll be able to visit you next summer.", "Next summer we will be able to visit you.", "Next summer we'll be able to visit you."],
        why=("*Can* has no future form: *will be able to*.", "*Can* nav nākotnes formas: *will be able to*."))
MV.text("B1.1", "Remove one unnecessary word: I must to wear a uniform at work.", "I must wear a uniform at work.",
        why=("After *must* comes the base form, without *to*.", "Aiz *must* lieto darbības vārda pamatformu bez *to*."))
MV.gap("B1.1", "I'm sorry, I ___ come to your party last Saturday. I was ill. (can)", "couldn't",
       why=("The past of *can* is *could*; the negative is *couldn't*.", "*Can* pagātnē ir *could*, noliegumā *couldn't*."))
MV.gap("B1.1", "When I was ten, I ___ swim really well. (can)", "could",
       why=("An ability in the past: *could*.", "Prasme pagātnē: *could*."))
MV.order("B1.1", "you don't have to bring any food", why=("*don't have to* = it is not necessary.", "*don't have to* = nav nepieciešams."))

CM = Topic("Comparison")
ER = ("A short adjective + *-er* + *than*: *fast → faster*.", "Īss īpašības vārds + *-er* + *than*: *fast → faster*.")
CM.mcq("A2.1", "Choose the correct option: The train is ___ than the bus.", "faster", ["more fast", "fastest"], why=ER)
CM.mcq("A2.1", "Choose the correct option: This is the ___ day of my holiday.", "best", ["goodest", "most good"],
       why=("*good → better → the best*: an irregular adjective.", "*good → better → the best*: neregulārs īpašības vārds."))
CM.gap("A2.1", "My new phone is ___ than my old one. (cheap)", "cheaper", why=ER)
CM.gap("A2.1", "My suitcase is ___ than yours. (heavy)", "heavier", why=("*-y* changes to *-ier*: *heavy → heavier*.", "*-y* kļūst par *-ier*: *heavy → heavier*."))
CM.gap("A2.1", "Today is ___ than yesterday. (hot)", "hotter", why=("One vowel + one consonant: double the consonant: *hot → hotter*.", "Viens patskanis + viens līdzskanis: līdzskani dubulto: *hot → hotter*."))
CM.mcq("A2.1", "Choose the correct option: Who is the ___ person in your family?", "oldest", ["most old", "more old"],
       why=("*the* + adjective + *-est*: *the oldest*.", "*the* + īpašības vārds + *-est*: *the oldest*."))
CM.text("A2.1", "Correct the mistake: My sister is more young than me.", ["My sister is younger than me.", "My sister is younger than I am."],
        why=("A short adjective takes *-er*, not *more*.", "Īsam īpašības vārdam pievieno *-er*, nevis *more*."))
CM.mcq("B1.1", "Choose the correct option: My phone is the same ___ yours.", "as", ["like", "than"], why=("*the same as*.", "*the same as*."))
CM.mcq("B1.1", "Choose the correct option: This film is not as good ___ the book.", "as", ["than", "like"], why=("*not as ... as*.", "*not as ... as*."))
CM.gap("B1.1", "The weather is getting ___ and ___. (cold)", "colder / colder", why=("A change: comparative + *and* + comparative.", "Pārmaiņas: pārākā pakāpe + *and* + pārākā pakāpe."))
CM.gap("B1.1", "Write one word in each gap: Flights cost more every year. They are getting ___ and ___ expensive.", "more / more", why=("A long adjective: *more and more expensive*.", "Garš īpašības vārds: *more and more expensive*."))
CM.text("B1.1", "Correct the mistake: This course is more easier than the last one.", "This course is easier than the last one.",
        why=("*-er* or *more*, never both.", "Vai nu *-er*, vai *more*, ne abi kopā."))
CM.text("B1.1", "Correct the mistake: My new job is more better than my old one.", "My new job is better than my old one.",
        why=("*better* is already a comparative: no *more*.", "*better* jau ir pārākā pakāpe: bez *more*."))
CM.mcq("B1.1", "Choose the correct option: The ___ you practise, the better you get.", "more", ["most", "many"], why=("*the more ..., the better ...*.", "*the more ..., the better ...*."))

MVA = "Modal verbs"
MV.mcq("A2.1", "Choose the correct option: You ___ use your phone in the exam.", "mustn't", ["don't must", "not must"], why=("A rule: *mustn't* + base form.", "Noteikums: *mustn't* + pamatforma."))
MV.mcq("A2.1", "Choose the correct option: My son ___ ride a bike.", "can", ["cans", "can to"], why=("*can* has no *-s* and no *to* after it.", "*can* nav galotnes *-s*, un aiz tā nav *to*."))
MV.order("A2.1", "we should take an umbrella", why=("*should* + base form: advice.", "*should* + pamatforma: padoms."))
MV.mcq("A2.1", "Choose the correct option: You look tired. You ___ go to bed early.", "should", ["should to", "shoulds"], why=("*should* + base form, no *to*.", "*should* + pamatforma, bez *to*."))
MV.mcq("A2.1", "Choose the correct option: ___ you help me with this box, please?", "Can", ["Cans", "Can to"], why=("A request: *Can you* + base form. *Can* has no *-s* and no *to*.", "Lūgums: *Can you* + pamatforma. *Can* nav galotnes *-s*, un aiz tā nav *to*."))
MV.mcq("A2.1", "Choose the correct option: I ___ drive. I don't have a licence.", "can't", ["don't can", "not can"], why=("The negative of *can* is *can't*.", "*can* noliegumā ir *can't*."))
MV.order("A2.1", "you must not park here", why=("*must not* + base form: it is not allowed.", "*must not* + pamatforma: nav atļauts."))

CT = Topic("Contrast, purpose and reason")
DESP = ("*despite / in spite of* + noun or *-ing*; never *despite of*.", "*despite / in spite of* + lietvārds vai *-ing*; nekad *despite of*.")
CT.mcq("B2.1", "Which sentence is correct?", "She took the job despite the fact that the pay was low.", ["She took the job despite of the fact that the pay was low.", "She took the job in spite the fact that the pay was low."], why=DESP)
CT.mcq("B2.1", "Choose the correct option: I left early so as ___ late.", "not to be", ["to not being", "not being"], why=("*so as not to* + base form.", "*so as not to* + pamatforma."))
CT.gap("B2.1", "Complete with one word: She spoke slowly so ___ to be understood.", "as", why=("*so as to* + base form: purpose.", "*so as to* + pamatforma: nolūks."))
CT.text("B2.1", "Correct the mistake: Despite of the delay, we arrived on time.", ["Despite the delay, we arrived on time.", "In spite of the delay, we arrived on time."], why=DESP)
CT.gap("B2.1", "Complete with one word: In ___ of the cold, they went swimming.", "spite", why=DESP)
CT.mcq("B2.1", "Choose the correct option: ___ feeling ill, he went to work.", "Despite", ["Despite of", "In spite"], why=DESP)

DP = Topic("Prepositions after words (listen to, good at)")
END = ("In a question the preposition stays at the end: *Who are you talking to?*", "Jautājumā prievārds paliek beigās: *Who are you talking to?* Tulkojot burtiski 'ar ko tu runā', prievārdu liek sākumā, bet angliski tas paliek beigās.")
DP.mcq("B1.1", "Which question is correct?", "Who are you talking to?", ["Who are you talking?", "To who you are talking?"], why=END)
DP.gap("B1.1", "Complete with one word: What are you afraid ___?", "of", why=("*afraid of*.", "*afraid of*."))
DP.order("B1.1", "what are you listening to", why=END)
DP.order("B1.1", "who is she married to", why=("*married to* someone; the preposition stays at the end.", "*married to*; prievārds paliek beigās."))
DP.mcq("B1.1", "Choose the correct option: Which team do you play ___?", "for", ["at", "of"], why=("*play for* a team.", "*play for* (komandā)."))
DP.mcq("B1.1", "Choose the correct question.", "What is this book about?", ["What is about this book?", "About what this book is?"], why=END)

C2 = Topic("Second conditional (if + past, would)")
C2.mcq("B2.1", "Which is correct? 'If I ___ in your position, I'd ask for a pay rise.'", "were", ["am", "would be", "be"], why=("*If I were you / in your position* + *would*.", "*If I were you* + *would*."))
C2.gap("B2.1", "If the city ___ more cycle lanes, more people ___ by bike. (build / travel)", "built / would travel", why=("*if* + past, *would* + base form.", "*if* + pagātne, *would* + pamatforma."))
C2.mcq("B2.1", "Which sentence has a mistake?", "If I would have a car, I would drive to work.", ["If she lived nearer, she'd visit more often.", "We would travel more if flights were cheaper.", "If he knew the answer, he would tell us all."], why=("No *would* after *if*: *If I had a car*.", "Aiz *if* nelieto *would*: *If I had a car*."))
C2.mcq("B2.1", "I don't have a car, so I take the bus. Imagine it is different. Choose the correct sentence.", "If I had a car, I wouldn't take the bus.", ["If I have a car, I wouldn't take the bus.", "If I would have a car, I wouldn't take the bus.", "If I had a car, I won't take the bus."], why=("An imagined present: *if* + past, *would* + base form.", "Iedomāta tagadne: *if* + pagātne, *would* + pamatforma."))
C2.text("B2.1", "Write the sentence with if: I don't have a garden, so I don't grow vegetables.", ["If I had a garden, I would grow vegetables.", "If I had a garden, I'd grow vegetables.", "I would grow vegetables if I had a garden.", "I'd grow vegetables if I had a garden.", "If I had a garden, I could grow vegetables.", "I could grow vegetables if I had a garden."], why=("*if* + past, *would* + base form.", "*if* + pagātne, *would* + pamatforma."))

C3 = Topic("Third conditional (if + had done, would have done)")
T3 = ("*if* + *had* + 3rd form, *would have* + 3rd form.", "*if* + *had* + 3. forma, *would have* + 3. forma.")
C3.mcq("B2.2", "We got lost yesterday because we didn't check the map. Imagine the opposite: 'If we ___ the map, we ___ lost.'", "had checked / wouldn't have got", ["checked / wouldn't get", "had checked / wouldn't get", "would check / hadn't got"], why=T3)
C3.gap("B2.2", "She stayed late and missed the last bus. If she ___ (not / stay) so late, she ___ (not / miss) the last bus.", "hadn't stayed / wouldn't have missed", why=T3)
C3.mcq("B2.2", "Which sentence is NOT correct?", "If they'd have asked me, I would've helped.", ["If it had rained, we'd have stayed in.", "She would have come if you'd invited her.", "If I had known, I wouldn't have said it."], why=("No *would have* after *if*: *If they had asked me*.", "Aiz *if* nelieto *would have*: *If they had asked me*."))
C3.mcq("B2.2", "We didn't know about the problem yesterday, so we didn't call you. Choose the sentence that says the opposite.", "If we had known about the problem, we would have called you.", ["If we knew about the problem, we would have called you.", "If we would have known about the problem, we would call you.", "If we had known about the problem, we will have called you."], why=T3)
C3.text("B2.2", "Write the sentence with if: I didn't know about the sale, so I didn't buy the coat.", ["If I had known about the sale, I would have bought the coat.", "I would have bought the coat if I had known about the sale.", "If I'd known about the sale, I'd have bought the coat.", "If I'd known about the sale, I would have bought the coat.", "If I had known about the sale, I'd have bought the coat.", "I'd have bought the coat if I'd known about the sale.", "I would have bought the coat if I'd known about the sale.", "I'd have bought the coat if I had known about the sale."], why=T3)

CA = Topic("Advanced conditionals: inversion, unless, wish")
CA.mcq("C1.1", "Choose the correct option: ___ for your help, we would never have finished on time.", "But", ["Without", "Unless"], why=("*But for* + noun = *If it hadn't been for*.", "*But for* + lietvārds = *If it hadn't been for*."))
CA.text("C1.1", "Rewrite starting with *Were*: If the price were lower, more people would buy it.", ["Were the price lower, more people would buy it.", "Were the price lower, more people would buy the product."], why=("*Were* + subject = *If* + subject + *were*, in formal English.", "*Were* + teikuma priekšmets = *If* + teikuma priekšmets + *were* (formāli)."))
CA.mcq("C1.1", "Choose the most formal option.", "Should you have questions, let us know.", ["If you've got questions, just shout.", "Got any questions? Just let us know.", "Any questions, just give us a call."], why=("*Should you ...* = *If you ...*, in formal writing.", "*Should you ...* = *If you ...* formālā tekstā."))
CA.bank("C1.1", "___ he ___ harder, he would have passed the exam.", ["Had", "studied"], ["Did", "studying"], why=("*Had he studied* = *If he had studied*: *had* before the subject, then the 3rd form.", "*Had he studied* = *If he had studied*: *had* pirms teikuma priekšmeta, tad 3. forma."))
CA.bank("C1.1", "___ it not been for the rain, the match would have finished on time.", "Had", ["Were", "Did", "Has"], why=("*Had it not been for* = *If it hadn't been for*.", "*Had it not been for* = *If it hadn't been for*."))
CA.mcq("C1.2", "Choose the correct option: It's high time we ___ a decision.", "made", ["make", "have made", "making"], why=("*It's (high) time* + subject + past: something should already be happening.", "*It's (high) time* + teikuma priekšmets + pagātne: tam jau būtu jānotiek."))
CA.bank("C1.2", "I'd rather you ___ anyone about this yet.", "didn't tell", ["don't tell", "won't tell", "not to tell"], why=("*I'd rather* + another person + past: what we want someone else to do.", "*I'd rather* + cits cilvēks + pagātne: ko gribam, lai dara kāds cits."))
CA.mcq("C1.2", "I was in hospital, so I missed your wedding. Choose the correct sentence.", "I wish I could have come to your wedding.", ["I wish I could come to your wedding.", "I wish I can have come to your wedding.", "I wish I would come to your wedding."], why=("A past ability we regret: *wish* + *could have* + 3rd form.", "Nožēla par pagātnē neiespējamo: *wish* + *could have* + 3. forma."))
CA.mcq("C1.2", "You talk about a past mistake in a meeting. Choose the correct option.", "If only we had tested the app, we would not have these problems.", ["If only we would have tested the app, we would not have these problems.", "If only we tested the app, we would not have these problems.", "If only we had tested the app, we will not have these problems."], why=("*If only* + past perfect for the past; *would* for the result now.", "*If only* + Past Perfect par pagātni; *would* par sekām tagad."))
CA.text("C1.2", "Write one sentence that starts with *I'd rather*: Please don't call me after ten.", ["I'd rather you didn't call me after ten.", "I would rather you didn't call me after ten.", "I'd rather you didn't call me after ten o'clock.", "I would rather you didn't call me after ten o'clock."], why=("*I'd rather* + another person + past.", "*I'd rather* + cits cilvēks + pagātne."))

RV = Topic("Reporting verbs (suggest, admit, promise...)")
RV.mcq("C1.1", "Which sentence reports 'You lost my keys!' as an accusation?", "He accused me of losing his keys.", ["He accused me to lose his keys.", "He accused me that I lost his keys.", "He accused me for losing his keys."], why=("*accuse* someone *of* + -ing.", "*accuse* kādu *of* + -ing."))
RV.mcq("C1.1", "Choose the correct option: The lawyer advised her ___ anything.", "not to sign", ["to not signing", "not signing"], why=("*advise* someone (*not*) *to* + verb.", "*advise* kādu (*not*) *to* + darbības vārds."))
RV.mcq("C1.1", "Which sentence is NOT correct?", "She insisted to pay for dinner.", ["She offered to pay for the tickets.", "He admitted taking the money.", "They suggested going by train."], why=("*insist on* + -ing: *She insisted on paying*.", "*insist on* + -ing: *She insisted on paying*."))
RV.mcq("C1.1", "Which sentence reports this: 'We're sorry the train was late, and we'll give you a refund.'", "The company apologised for the delay and promised a refund.", ["The company apologised the delay and promised a refund.", "The company apologised for the delay and promised refunding.", "The company apologised for the delay and promised of a refund."], why=("*apologise for* something; *promise* + noun or *to* + verb.", "*apologise for*; *promise* + lietvārds vai *to* + darbības vārds."))
RV.text("C1.1", "Report with *deny*: 'I didn't take the money,' said Leo.", ["Leo denied taking the money.", "Leo denied having taken the money.", "Leo denied that he had taken the money.", "Leo denied that he took the money."], why=("*deny* + -ing (or *having* + 3rd form).", "*deny* + -ing (vai *having* + 3. forma)."))

IP = Topic("Indirect questions (Could you tell me where...)")
ORD = ("After *Could you tell me / Do you know* the word order is like a statement: subject + verb.", "Aiz *Could you tell me / Do you know* vārdu secība ir kā apgalvojumā: teikuma priekšmets + darbības vārds.")
IP.mcq("B2.1", "Which sentence is correct and polite?", "Would you mind telling me where the nearest pharmacy is?", ["Would you mind telling me where is the nearest pharmacy?", "Would you mind to tell me where the nearest pharmacy is?", "Would you mind telling me where the nearest pharmacy is it?"], why=ORD)
IP.text("B2.1", "Ask politely, starting with *Could you tell me*: Why is the flight delayed?", ["Could you tell me why the flight is delayed?", "Could you tell me why the flight's delayed?"], why=ORD)
IP.mcq("B2.1", "Which sentence is NOT correct?", "Do you know what time does it open?", ["Do you know if Anna is at home?", "I wonder how far the station is.", "Could you tell me who called me?"], why=ORD)
IP.mcq("B2.1", "Which is the polite way to ask this: 'Where is the meeting room?'", "I was wondering if you could tell me where the meeting room is.", ["I was wondering if you could tell me where is the meeting room.", "I was wondering if could you tell me where the meeting room is.", "I was wondering you could tell me where the meeting room is."], why=ORD)
IP.text("B2.1", "Ask politely, starting with *Do you know*: When does the shop close?", "Do you know when the shop closes?", why=ORD)

QY = Topic("Quantity")
QY.mcq("B1.1", "Choose the correct option: I can't concentrate. There are ___ people here.", "too many", ["too much", "enough of"], why=("*too many* + plural nouns; *too much* + uncountable nouns.", "*too many* + daudzskaitlis; *too much* + neskaitāmi lietvārdi."))
QY.mcq("B1.1", "Choose the correct option: We can't make a cake. There isn't ___ flour.", "enough", ["too many", "enough of"], why=("*enough* + noun, without *of*.", "*enough* + lietvārds, bez *of*."))
QY.gap("B1.1", "Write the missing word: Is your car big ___ for five people?", "enough", why=("adjective + *enough*: *big enough*.", "īpašības vārds + *enough*: *big enough*."))
QY.mcq("B1.1", "Choose the correct option: There was ___ much traffic, so we were late.", "too", ["many", "enough"], why=("*too much* = more than is good.", "*too much* = vairāk nekā vajag."))
QY.mcq("B1.1", "Choose the correct option: I've got ___ money, so I can't come to the cinema.", "very little", ["very few", "a few"], why=("*little* + uncountable nouns (*money*); *few* + plurals.", "*little* + neskaitāmi lietvārdi (*money*); *few* + daudzskaitlis."))

save("pending/twins-1.csv")
