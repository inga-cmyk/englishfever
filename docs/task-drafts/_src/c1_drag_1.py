"""C1 drag-and-drop round 1 (26 November 2026): word banks and word orders for all ten C1 topics, so that at least 40% of the
C1 tasks are drag-and-drop (ITEM-WRITING-RULES 6; C1 full review C4). Teacher, 26 November: write them, have them checked by
independent readers, no samples for her. Hewings, Advanced Grammar in Use (3rd ed.); Murphy, English Grammar in Use.
Points not covered before are preferred (x_mental_cont, x_i_hear, x_pastc_always, x_past_polite, x_will_crit, x_can_could,
x_allowed_once, x_subj_should, x_agr_rel, x_agr_there, x_of_which, x_part_own, x_part_rel, x_inv_place ...).
Blind round c1-18 (26 November): the judge's decisions (docs/review/blind/c1-18-judge.md) are applied here: 41 tasks rewritten,
5 with added orders, the chef demonstration dropped.
Blind round c1-19 (26 November): docs/review/blind/c1-19-judge.md applied: orders added to 5 tasks, the
allowed-once task rewritten, the heatwave task dropped."""
from lib import gp, od

ORD = "Put the words in order."

# ---------------------------------------------------------------- 1. Advanced present simple and continuous
T = "Advanced present simple and continuous"; L = "C1"
gp(T, L, 3, "You ___ ___ very difficult today. That's not like you.", "are / being",
   "*be* about how someone behaves at the moment is continuous: *You're being difficult* (today, not always).",
   "*be* par to, kā kāds uzvedas šobrīd, ir ilgstošajā formā: *You're being difficult* (šodien, ne vienmēr).",
   bank=["are", "being", "be", "been"])
od(T, L, 3, ORD, "i'm wondering whether you'd mind swapping seats with me",
   "*I'm wondering whether …* (present continuous) is a softer, more polite request than *Would you swap …?*",
   "*I'm wondering whether …* (ilgstošā forma) ir maigāks, pieklājīgāks lūgums nekā *Would you swap …?*")
gp(T, L, 3, "I ___ ___ more and more how much I miss the sea.", "am / realising",
   "A growing awareness now: the continuous, *I'm realising more and more*.",
   "Apziņa, kas tagad pieaug: ilgstošā forma, *I'm realising more and more*.",
   bank=["am", "realising", "realise", "was"])
gp(T, L, 4, "Your brother ___ ___ you've decided to sell the flat. Is that right?", "tells / me",
   "News we have heard: present simple, *Your brother tells me …*. *say* takes no person straight after it.",
   "Ziņa, ko esam dzirdējuši: Present Simple, *Your brother tells me …*. Aiz *say* cilvēks uzreiz nestāv.",
   bank=["tells", "me", "is", "telling", "says"])
od(T, L, 3, ORD, "i'm already regretting my decision to move to the countryside",
   "*regret* about a feeling that is new and growing now can be continuous: *I'm already regretting*.",
   "*regret* par sajūtu, kas ir jauna un tagad pieaug, var būt ilgstošajā formā: *I'm already regretting*.",
   also=["i'm regretting my decision to move to the countryside already",
         "already i'm regretting my decision to move to the countryside"])
gp(T, L, 4, "OK, OK, I ___ ___: I forgot to book the restaurant.", "admit / it",
   "Saying *I admit it* is the act of admitting, so the present simple: not *I'm admitting it*.",
   "Pasakot *I admit it*, cilvēks jau atzīstas, tāpēc Present Simple: nevis *I'm admitting it*.",
   bank=["admit", "it", "am", "admitting"])

# ---------------------------------------------------------------- 2. Advanced past simple, past continuous and past perfect
T = "Advanced past simple, past continuous and past perfect"
gp(T, L, 3, "I ___ ___ to retire at sixty, but with prices the way they are, I'll have to keep working.", "had / planned",
   "*had planned to*: a plan that will not happen now. *have planned* would mean the plan still stands, but the second half says it does not.",
   "*had planned to*: plāns, kas tagad neīstenosies. *have planned* nozīmētu, ka plāns joprojām ir spēkā, bet teikuma otrā daļa saka pretējo.",
   bank=["had", "planned", "have", "plan"])
od(T, L, 3, ORD, "we were wondering if you might be able to help us with the move",
   "*We were wondering if …* (past continuous) is a softer, more polite request than *We wonder if …*. After *if* the words keep statement order: *if you might be able to*.",
   "*We were wondering if …* (Past Continuous) ir maigāks, pieklājīgāks lūgums nekā *We wonder if …*. Aiz *if* vārdu secība ir kā apgalvojumā: *if you might be able to*.")
gp(T, L, 4, "When we were teenagers, my sister ___ ___ ___ my clothes without asking.", "was / always / borrowing",
   "*was always* + *-ing*: an annoying habit in the past. *always* goes between *was* and the *-ing* form.",
   "*was always* + darbības vārds ar *-ing*: kaitinošs ieradums pagātnē. *always* stāv starp *was* un formu ar *-ing*.",
   bank=["was", "always", "borrowing", "had", "borrow"])
gp(T, L, 4, "When we got back from holiday, the heating was on and there were dirty cups in the sink. Someone ___ ___ ___ in the flat.", "had / been / staying",
   "A conclusion about what had been going on before a past moment (*when we got back*): *had been staying*. *has been staying* would be about now.",
   "Secinājums par to, kas bija noticis pirms brīža pagātnē (*when we got back*): *had been staying*. *has been staying* būtu par tagadni.",
   bank=["had", "been", "staying", "has", "stayed"])
gp(T, L, 4, "By the time I found my phone, she ___ ___ ___ me four times.", "had / already / texted",
   "*four times* is a number of times, so the simple form: *had already texted*. *had been texting me four times* is wrong: the continuous does not count.",
   "*four times* ir reižu skaits, tāpēc vienkāršā forma: *had already texted*. *had been texting me four times* ir nepareizi: ilgstošo formu neizmanto, kad skaita reizes.",
   bank=["had", "already", "texted", "been", "texting"])
od(T, L, 3, ORD, "i had expected the interview to be much harder than it was",
   "*had expected*: what I thought before; it turned out differently (*than it was*, *than I had expected it to be*).",
   "*had expected*: ko domāju iepriekš; iznāca citādi (*than it was*, *than I had expected it to be*).",
   also=["the interview was much harder than i had expected it to be",
         "it was much harder than i had expected the interview to be",
         "i had expected it to be much harder than the interview was"])

# ---------------------------------------------------------------- 3. The perfect tenses: forms and uses
T = "The perfect tenses: forms and uses"
gp(T, L, 4, "She is said ___ ___ ___ a fortune on the house.", "to / have / spent",
   "*is said* + perfect infinitive for an earlier action: *is said to have spent*.",
   "*is said* + Perfect nenoteiksme par agrāku darbību: *is said to have spent*.",
   bank=["to", "have", "spent", "spend", "having"])
gp(T, L, 4, "It was the first time she ___ ___ on the left, so she was very nervous.", "had / driven",
   "*It was the first time* + past perfect: *had driven*. With *It's the first time* it would be *has driven*.",
   "*It was the first time* + Past Perfect: *had driven*. Ar *It's the first time* būtu *has driven*.",
   bank=["had", "driven", "has", "drove"])
gp(T, L, 4, "By the end of this month, I ___ ___ ___ this car for exactly ten years.", "will / have / had",
   "*by* + a future moment + *for ten years*: future perfect, *will have had*. *have* (= own) is a state, so not *will be having*.",
   "*by* + nākotnes brīdis + *for ten years*: Future Perfect, *will have had*. *have* (= piederēt) ir stāvokļa darbības vārds, tāpēc nevis *will be having*.",
   bank=["will", "have", "had", "be", "having"])
gp(T, L, 3, "Once the paint ___ ___, you can put the furniture back.", "has / dried",
   "After *once* about the future we use the present perfect (or the present), not *will*: *once the paint has dried*.",
   "Aiz *once*, runājot par nākotni, lieto Present Perfect (vai Present Simple), nevis *will*: *once the paint has dried*.",
   bank=["has", "dried", "will", "dry"])
gp(T, L, 4, "I don't remember ___ ___ this film before, but I know how it ends.", "having / seen",
   "*remember having seen* = remember an earlier experience. *remember to see* means \"not forget to do it\" and does not fit.",
   "*remember having seen* = atcerēties agrāku pieredzi. *remember to see* nozīmē \"neaizmirst izdarīt\", un tas te neder.",
   bank=["having", "seen", "to", "see"])
gp(T, L, 4, "She told the boss he was wrong in front of everyone? I'd love ___ ___ ___ his face!", "to / have / seen",
   "*I'd love to have seen*: a wish about the past that cannot come true now (*to have* + 3rd form).",
   "*I'd love to have seen*: vēlēšanās par pagātni, kas vairs nevar piepildīties (*to have* + 3. forma).",
   bank=["to", "have", "seen", "saw", "having"])
od(T, L, 4, ORD, "the house is thought to have been built in the 1890s",
   "*is thought* + perfect passive infinitive for an earlier action: *to have been built*.",
   "*is thought* + Perfect ciešamās kārtas nenoteiksme par agrāku darbību: *to have been built*.",
   also=["is the house thought to have been built in the 1890s"])

# ---------------------------------------------------------------- 4. Advanced modals: will, would, should
T = "Advanced modals: will, would, should"
gp(T, L, 4, "If you ___ ___ any problems with the app, just email us.", "should / have",
   "*If you should* + verb: a polite condition that is not very likely.",
   "*If you should* + darbības vārds: pieklājīgs nosacījums, kas nav īpaši ticams.",
   bank=["should", "have", "had", "will", "would"])
od(T, L, 3, ORD, "she would spend hours in the garden when she was a child",
   "*would* + verb for a repeated action in the past.",
   "*would* + darbības vārds atkārtotai darbībai pagātnē.",
   also=["when she was a child she would spend hours in the garden"])
gp(T, L, 4, "If you ___ ___ to bed at two every night, of course you're tired!", "will / go",
   "*If you will* + verb: criticism of a habit the person keeps.",
   "*If you will* + darbības vārds: kritika par ieradumu, ko cilvēks nemaina.",
   bank=["will", "go", "would", "went"])
gp(T, L, 4, "I ___ ___ ___ the shops would be open on a Sunday.", "would / have / thought",
   "*I would have thought* gives an opinion politely, with some distance.",
   "*I would have thought* izsaka viedokli pieklājīgi, ar distanci.",
   bank=["would", "have", "thought", "will", "think"])
od(T, L, 3, ORD, "i'm afraid i'd have to disagree with you on that",
   "*I'd have to disagree* is a softer, more polite way to say *I disagree*: *would* adds distance.",
   "*I'd have to disagree* ir maigāks, pieklājīgāks veids, kā pateikt *I disagree*: *would* rada distanci.",
   also=["i'd have to disagree with you on that i'm afraid",
         "i'm afraid i'd have to disagree on that with you",
         "i'd have to disagree on that with you i'm afraid",
         "on that i'm afraid i'd have to disagree with you",
         "on that i'd have to disagree with you i'm afraid",
         "i'm afraid on that i'd have to disagree with you"])
gp(T, L, 4, "Please allow extra time for your journey in case the roads ___ ___ busy.", "should / be",
   "*in case* + *should*: a formal way to talk about a possible situation. Not *will* or *would* after *in case*.",
   "*in case* + *should*: oficiāls veids, kā runāt par iespējamu situāciju. Aiz *in case* nelieto *will* vai *would*.",
   bank=["should", "be", "would", "will"])
od(T, L, 3, ORD, "you should have told me you were going to be late",
   "*should have* + 3rd form: criticism of something that did not happen.",
   "*should have* + 3. forma: pārmetums par to, kas netika izdarīts.")

# ---------------------------------------------------------------- 5. Advanced modals: can, be able to, may, might
T = "Advanced modals: can, be able to, may, might"
gp(T, L, 4, "We ___ ___ well take a taxi: the last bus has gone.", "might / as",
   "*might as well* = the sensible thing to do, as there is nothing better.",
   "*might as well* = saprātīga izvēle, jo nekā labāka nav.",
   bank=["might", "as", "good", "so"])
od(T, L, 3, ORD, "he can't have been at home last night",
   "*can't have* + 3rd form: we are sure something did not happen.",
   "*can't have* + 3. forma: esam pārliecināti, ka tas nenotika.",
   also=["last night he can't have been at home"])
gp(T, L, 4, "I've rung the bell twice and nobody's answering. They ___ ___ out in the garden.", "might / be",
   "A guess about this situation now: *might be* (or *may / could be*). *can be* is only for what is sometimes true in general.",
   "Minējums par šo situāciju tagad: *might be* (vai *may / could be*). *can be* lieto tikai tam, kas vispār mēdz būt.",
   bank=["might", "be", "can", "being"])
gp(T, L, 4, "My name was missing from the passenger list, but after an hour of phone calls, I ___ ___ onto the plane.", "was / allowed",
   "Permission on one particular occasion in the past: *was allowed* (onto the plane). *could* is for general permission or ability, not for one thing that happened on one occasion: not *I could go onto the plane*.",
   "Atļauja vienā konkrētā reizē pagātnē: *was allowed* (onto the plane). *could* lieto vispārējai atļaujai vai spējai, nevis vienam notikumam vienā reizē: nevis *I could go onto the plane*.",
   bank=["was", "allowed", "could", "go"])
od(T, L, 3, ORD, "she may be clever but she has no common sense",
   "*may … but*: we admit one point before we say something against it.",
   "*may … but*: atzīstam vienu lietu, pirms sakām kaut ko pretī.",
   also=["clever she may be but she has no common sense"])
gp(T, L, 4, "With this much snow, the match ___ ___ be cancelled, so check the website before you set off.", "may / well",
   "*may well* = it is quite likely. Not *may good*, and not *can* for a guess about one event.",
   "*may well* = diezgan iespējams. Nevis *may good*, un nevis *can*, minot par vienu notikumu.",
   bank=["may", "well", "can", "good"])
od(T, L, 3, ORD, "they might have been delayed by the snow",
   "*might have been* + 3rd form: a possible explanation of something in the past.",
   "*might have been* + 3. forma: iespējams izskaidrojums tam, kas notika pagātnē.",
   also=["might they have been delayed by the snow"])

# ---------------------------------------------------------------- 6. The subjunctive
T = "The subjunctive: I insist that he be told, if I were"
gp(T, L, 4, "The coach advised that the captain ___ ___ to journalists before the final.", "not / speak",
   "*advise that* + subject + base form; the negative is *not* + base form: *that the captain not speak*. No *to* after *that*.",
   "*advise that* + teikuma priekšmets + pamatforma; noliegumā *not* + pamatforma: *that the captain not speak*. Aiz *that* nelieto *to*.",
   bank=["not", "speak", "to", "speaks"])
od(T, L, 4, ORD, "i'd rather we had booked somewhere with a pool",
   "*I'd rather* + subject + past perfect: a wish about the past (*we booked somewhere else*).",
   "*I'd rather* + teikuma priekšmets + Past Perfect: vēlēšanās par pagātni (*mēs rezervējām citu vietu*).")
gp(T, L, 4, "It is vital that the patient ___ ___ left alone tonight.", "not / be",
   "*It is vital that* + subject + base form; the negative is *not be*.",
   "*It is vital that* + teikuma priekšmets + pamatforma; noliegumā *not be*.",
   bank=["not", "be", "being", "been"])
gp(T, L, 4, "If the factory ___ ___ close, two hundred people would lose their jobs.", "were / to",
   "*If* … *were to* + verb: an imagined future situation.",
   "*If* … *were to* + darbības vārds: iedomāta situācija nākotnē.",
   bank=["were", "to", "is", "has"])
od(T, L, 4, ORD, "the committee insisted that the decision be announced to all staff",
   "*insist that* + subject + base form: *the decision be announced* (for every person, also in the past).",
   "*insist that* + teikuma priekšmets + pamatforma: *the decision be announced* (visām personām, arī pagātnē).",
   also=["all staff insisted that the decision be announced to the committee",
         "the committee insisted to all staff that the decision be announced",
         "all staff insisted to the committee that the decision be announced",
         "the staff insisted that the committee decision be announced to all",
         "the committee insisted that the staff decision be announced to all",
         "all the committee insisted that the decision be announced to staff", "the committee all insisted that the decision be announced to staff"])
gp(T, L, 4, "My colleagues may think I'm rude for leaving at five, but so ___ ___.", "be / it",
   "A fixed phrase that keeps the old form: *so be it* (= I accept it). Not *so is it*.",
   "Nemainīgs izteiciens, kas saglabā seno formu: *so be it* (= es to pieņemu). Nevis *so is it*.",
   bank=["be", "it", "is", "was"])
od(T, L, 4, ORD, "the captain requested that passengers should remain in their seats",
   "*request that* + *should* + verb: the British way, less formal than the base form alone.",
   "*request that* + *should* + darbības vārds: britu variants, mazāk oficiāls nekā tikai pamatforma.")

# ---------------------------------------------------------------- 7. Subject and verb: advanced rules
T = "Subject and verb: advanced rules"
gp(T, L, 4, "This pair of glasses ___ ___ me over two hundred euros.", "has / cost",
   "The subject is *pair* (singular), so *has cost*. The past form of *cost* is *cost*.",
   "Teikuma priekšmets ir *pair* (vienskaitlis), tāpēc *has cost*. *cost* pagātnes forma ir *cost*.",
   bank=["has", "cost", "have", "costed"])
gp(T, L, 4, "Our biggest expense ___ ___ ___ the rent and the heating bills.", "has / always / been",
   "The subject is *expense* (singular); what comes after the verb does not change it: *has always been*.",
   "Teikuma priekšmets ir *expense* (vienskaitlis); tas, kas seko darbības vārdam, to nemaina: *has always been*.",
   bank=["has", "always", "been", "have", "being"])
gp(T, L, 4, "She is one of the few doctors who ___ ___ home visits.", "still / make",
   "*who* refers to *doctors* (plural), so the verb is plural: *who still make*.",
   "*who* attiecas uz *doctors* (daudzskaitlis), tāpēc darbības vārds ir daudzskaitlī: *who still make*.",
   bank=["still", "make", "makes"])
gp(T, L, 4, "There ___ ___ three cars parked outside your house all morning.", "have / been",
   "After *there* the verb agrees with the noun that follows: *three cars*, so *have been*.",
   "Aiz *there* darbības vārds saskan ar lietvārdu, kas seko: *three cars*, tāpēc *have been*.",
   bank=["have", "been", "has", "was"])
gp(T, L, 4, "Two thirds of the money ___ ___ spent on salaries.", "has / been",
   "A fraction + *of* + an uncountable noun takes a singular verb: *two thirds of the money has been spent*.",
   "Daļa + *of* + neskaitāms lietvārds: darbības vārds vienskaitlī, *two thirds of the money has been spent*.",
   bank=["has", "been", "have", "being"])
gp(T, L, 4, "The cost of the repairs ___ ___ higher than we thought.", "was / much",
   "The main noun is *cost* (singular), not *repairs*: *The cost … was*.",
   "Galvenais lietvārds ir *cost* (vienskaitlis), nevis *repairs*: *The cost … was*.",
   bank=["was", "much", "were", "more"])
od(T, L, 4, ORD, "neither the teacher nor the students were happy with the results",
   "With *neither … nor* the verb agrees with the nearer noun: *the students were*.",
   "Ar *neither … nor* darbības vārds saskan ar tuvāko lietvārdu: *the students were*.")

# ---------------------------------------------------------------- 8. Prepositions: position and advanced patterns
T = "Prepositions: position and advanced patterns"
gp(T, L, 4, "The manager ___ ___ I worked in my first job taught me everything I know.", "for / whom",
   "In formal English the preposition goes before *whom* (people) or *which* (things), never before *who* or *that*: *the manager for whom I worked*.",
   "Oficiālā valodā prievārds stāv pirms *whom* (cilvēki) vai *which* (lietas), nekad pirms *who* vai *that*: *the manager for whom I worked*.",
   bank=["for", "whom", "who", "that", "which"])
od(T, L, 3, ORD, "it's not the kind of job you can walk away from",
   "In everyday English the preposition stays at the end, with its verb: *a job you can walk away from*.",
   "Ikdienas valodā prievārds paliek beigās pie sava darbības vārda: *a job you can walk away from*.",
   also=["it's the kind of job you can not walk away from"])
gp(T, L, 4, "She has two brothers, both ___ ___ live abroad.", "of / whom",
   "*both of whom* joins the two parts: after *of* we use *whom* for people.",
   "*both of whom* savieno abas daļas: aiz *of* par cilvēkiem lieto *whom*.",
   bank=["of", "whom", "who", "them"])
gp(T, L, 3, "The course is open to everyone, ___ ___ age.", "regardless / of",
   "*regardless of* + noun = it does not matter what the age is.",
   "*regardless of* + lietvārds = nav svarīgi, kāds ir vecums.",
   bank=["regardless", "of", "despite", "from"])
od(T, L, 4, ORD, "the matter is being looked into by the police",
   "In the passive the preposition stays with its verb: *is being looked into*.",
   "Ciešamajā kārtā prievārds paliek pie sava darbības vārda: *is being looked into*.",
   also=["is the matter being looked into by the police"])
gp(T, L, 4, "Two goals down with five minutes left, there's little hope ___ ___ the match now.", "of / winning",
   "The noun *hope* takes *of* + *-ing*: *little hope of winning* (not *hope to win* after the noun).",
   "Lietvārdam *hope* seko *of* + darbības vārds ar *-ing*: *little hope of winning* (aiz lietvārda nevis *hope to win*).",
   bank=["of", "winning", "to", "win"])
od(T, L, 3, ORD, "she's not an easy person to work with",
   "The preposition stays at the end of the infinitive: *an easy person to work with*.",
   "Prievārds paliek nenoteiksmes beigās: *an easy person to work with*.")

# ---------------------------------------------------------------- 9. Advanced participle clauses
T = "Advanced participle clauses"
gp(T, L, 4, "Unpacking my suitcase at the hotel, ___ ___ that my passport was missing.", "I / noticed",
   "The *-ing* part tells us about the subject of the main clause: I was unpacking, so *I noticed*. *it seemed* would mean that \"it\" was unpacking.",
   "Daļa ar *-ing* ir par galvenā teikuma priekšmetu: koferi izsaiņoju es, tāpēc *I noticed*. *it seemed* nozīmētu, ka izsaiņoja \"it\".",
   bank=["I", "noticed", "it", "seemed"])
od(T, L, 4, ORD, "not wanting to wake the children we spoke in whispers",
   "*Not* + *-ing* gives the reason: *Not wanting to wake the children, …*",
   "*Not* + *-ing* izsaka iemeslu: *Not wanting to wake the children, …*",
   also=["we spoke in whispers not wanting to wake the children"])
gp(T, L, 4, "All flights ___ ___ ___, passengers were offered rooms at a nearby hotel.", "having / been / cancelled",
   "A participle clause with its own subject (*All flights*), formal: *All flights having been cancelled, …* (= because all flights had been cancelled). *were being cancelled* would join two sentences with only a comma.",
   "Teiciens ar savu teikuma priekšmetu (*All flights*), oficiāli: *All flights having been cancelled, …* (= tā kā visi reisi bija atcelti). *were being cancelled* savienotu divus teikumus tikai ar komatu.",
   bank=["having", "been", "cancelled", "were", "being"])
gp(T, L, 4, "___ ___, he refused to go to bed until the match was over.", "Though / exhausted",
   "Conjunction + 3rd form with no subject and no verb: *Though exhausted* (= although he was exhausted). *exhausting* describes what makes someone tired.",
   "Saiklis + 3. forma bez teikuma priekšmeta un darbības vārda: *Though exhausted* (= lai gan viņš bija ļoti noguris). *exhausting* raksturo to, kas nogurdina.",
   bank=["Though", "exhausted", "If", "exhausting"])
gp(T, L, 4, "The flats ___ ___ near the station will be ready next spring.", "being / built",
   "The flats do not build anything; they are being built: the short form of *which are being built* is *being built*.",
   "Dzīvokļi paši neko neceļ, tos ceļ: īsā forma no *which are being built* ir *being built*.",
   bank=["being", "built", "building", "are", "have"])
gp(T, L, 4, "The storm brought down power lines, ___ thousands of homes ___ electricity.", "leaving / without",
   "An *-ing* clause after the main clause for its result: *leaving thousands of homes without electricity*.",
   "*-ing* teiciens aiz galvenā teikuma izsaka sekas: *leaving thousands of homes without electricity*.",
   bank=["leaving", "without", "left", "with"])
gp(T, L, 4, "___ ___, the job isn't mine until I've signed the contract.", "Strictly / speaking",
   "*Strictly speaking* is a fixed comment phrase (= if we are exact): adverb + *speaking*.",
   "*Strictly speaking* ir nemainīgs komentāra izteiciens (= ja runājam precīzi): apstākļa vārds + *speaking*.",
   bank=["Strictly", "speaking", "Strict", "spoken"])

# ---------------------------------------------------------------- 10. Advanced word order: inversion and fronting
T = "Advanced word order: inversion and fronting"
gp(T, L, 4, "Not only ___ ___ late, but he also forgot the tickets.", "was / he",
   "After *Not only* at the start, the verb comes before the subject: *Not only was he late*.",
   "Pēc *Not only* teikuma sākumā darbības vārds stāv pirms teikuma priekšmeta: *Not only was he late*.",
   bank=["was", "he", "is", "did"])
od(T, L, 4, ORD, "no sooner had the film started than the power went off",
   "*No sooner had* + subject + 3rd form … *than*.",
   "*No sooner had* + teikuma priekšmets + 3. forma … *than*.",
   also=["the film had no sooner started than the power went off"])
gp(T, L, 4, "___ ___ to resign, who would replace her?", "Were / she",
   "*Were* + subject + *to*: a formal conditional without *if* (= If she were to resign).",
   "*Were* + teikuma priekšmets + *to*: oficiāls nosacījums bez *if* (= If she were to resign).",
   bank=["Were", "she", "Did", "If"])
gp(T, L, 4, "___ ___ I like him, I can't agree with him on this.", "Much / as",
   "*Much as* + clause = although: *Much as I like him, …*",
   "*Much as* + teikums = lai gan: *Much as I like him, …*",
   bank=["Much", "as", "So", "that"])
gp(T, L, 4, "Opposite our office ___ two new cafés, so lunch is never a problem.", "are",
   "A place phrase first, then the verb, then the subject. The subject is *two new cafés* (plural), so *are*.",
   "Vietas apzīmētājs pirmais, tad darbības vārds, tad teikuma priekšmets. Teikuma priekšmets ir *two new cafés* (daudzskaitlis), tāpēc *are*.",
   bank=["are", "is", "stands", "there"])
gp(T, L, 4, "Not once ___ ___ thank us for looking after his dog.", "did / he",
   "After *Not once* at the start, *did* comes before the subject: *Not once did he thank us*.",
   "Pēc *Not once* teikuma sākumā *did* stāv pirms teikuma priekšmeta: *Not once did he thank us*.",
   bank=["did", "he", "has", "was"])
gp(T, L, 4, "What she did ___ ___ out of the meeting without a word.", "was / walk",
   "*What she did was* + base form puts the focus on the action: *What she did was walk out*. Not *was walked*.",
   "*What she did was* + pamatforma izceļ darbību: *What she did was walk out*. Nevis *was walked*.",
   bank=["was", "walk", "walked", "is"])
