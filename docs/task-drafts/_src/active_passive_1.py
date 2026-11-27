"""Active or passive? Present and past, round 1 (27 November 2026). The teacher's request of 27 November: the present and past
simple passive are A2 topics; the B1 topic mixes the present and the past, and in every task the learner has to decide whether
the sentence needs the active or the passive. One point, pas_act (GRAMMAR-MAP.json, B1.1). The sentence decides the voice
(who does the action, or a verb with no object) and a time word decides the tense, so only one answer fits.
No card example and no scene of a card (cards2_b1p.py); the teacher does not read drafts: two blind readers and a judge decide.
Murphy, English Grammar in Use, units 42 and 44."""
from lib import mc, gp, od, tx, save, NOTES, rows

POINT_OF = {}
T = "Active or passive? Present and past"
L = "B1.1"


def pt(point="pas_act"):
    POINT_OF[len(rows) - 1] = point


def point_of(row):
    return POINT_OF[row]


def note(*parts):
    NOTES[len(rows) - 1] = " || ".join(parts)


C = "Choose the correct option: "
W = "Which sentence has a mistake?"

# ---------------------------------------------------------------- choose
mc(T, L, 3, C + "In our office, the computers ___ by an IT company every Friday.", "are checked",
   ["check", "were checked", "are checking"],
   "The computers do not check anything: someone checks them, so passive. *every Friday* is a habit now: *are checked*.",
   "Datori neko nepārbauda: tos kāds pārbauda, tāpēc ciešamā kārta. *every Friday* ir ieradums tagad: *are checked*.")
pt()
mc(T, L, 3, C + "My grandfather ___ this cottage with his own hands in 1965.", "built",
   ["was built", "is built", "builds"],
   "My grandfather did the building himself, so active. *in 1965* is past: *built*.",
   "Vectēvs pats būvēja, tāpēc darāmā kārta. *in 1965* ir pagātne: *built*.")
pt()
mc(T, L, 3, C + "The parcel ___ to the wrong address, so it came back to me a week later.", "was sent",
   ["sent", "is sent", "has sent"],
   "A parcel does not send anything: someone sent it, so passive. *came back* is past: *was sent*.",
   "Paka neko nesūta: to kāds nosūtīja, tāpēc ciešamā kārta. *came back* ir pagātne: *was sent*.")
pt()
mc(T, L, 3, C + "Every summer, thousands of tourists ___ the old town.", "visit",
   ["are visited", "were visited", "is visited"],
   "The tourists do the visiting, so active. *Every summer* is a habit now: *visit*.",
   "Tūristi paši apmeklē, tāpēc darāmā kārta. *Every summer* ir ieradums tagad: *visit*.")
pt()
mc(T, L, 3, C + "I ___ by a bee while I was working in the garden.", "was stung",
   ["stung", "am stung", "was stinging"],
   "The bee did it to me, so passive: *I was stung by a bee*. *while I was working* is past: *was stung*.",
   "Bite to izdarīja ar mani, tāpēc ciešamā kārta: *I was stung by a bee*. *while I was working* ir pagātne: *was stung*.")
pt()
mc(T, L, 3, C + "This pasta sauce is my mum's recipe. She ___ it every Sunday.", "makes",
   ["is made", "was made", "is making"],
   "My mum does the cooking, so active. *every Sunday* is a habit: present simple, *makes*.",
   "Mamma pati gatavo, tāpēc darāmā kārta. *every Sunday* ir ieradums: Present Simple, *makes*.")
pt()
mc(T, L, 3, C + "The writer ___ in 1999, but his books are still popular.", "died",
   ["was died", "is died", "dies"],
   "*die* has no object, so it has no passive: *died*. *in 1999* is past.",
   "*die* nav papildinātāja, tāpēc tam nav ciešamās kārtas: *died*. *in 1999* ir pagātne.")
pt()
mc(T, L, 4, W, "The fire was happened just after midnight.",
   ["The firefighters arrived within ten minutes.", "The fire was put out by two in the morning.", "Nobody was hurt in the fire."],
   "*happen* has no object, so it has no passive: *The fire happened*. *was put out* and *was hurt* are correct passives: someone did it to the fire, something hurt people.",
   "*happen* nav papildinātāja, tāpēc tam nav ciešamās kārtas: *The fire happened*. *was put out* un *was hurt* ir pareiza ciešamā kārta.")
pt()
mc(T, L, 4, W, "Our guests were arrived late because of the snow.",
   ["The roads were cleared in the morning.", "Some flights were cancelled because of the snow.", "We stayed at home all weekend."],
   "*arrive* has no object, so it has no passive: *Our guests arrived late*.",
   "*arrive* nav papildinātāja, tāpēc tam nav ciešamās kārtas: *Our guests arrived late*.")
pt()
mc(T, L, 3, "Which sentence is correct?", "This song was written by my best friend.",
   ["This song wrote by my best friend.", "This song was wrote by my best friend.", "My best friend was written this song."],
   "The song does not write: my best friend wrote it. Passive: *was* + 3rd form, *was written*, and *by* + who did it.",
   "Dziesma neraksta: to uzrakstīja draugs. Ciešamā kārta: *was* + 3. forma, *was written*, un *by* + darītājs.")
pt()

# ---------------------------------------------------------------- word order
od(T, L, 3, "Put the words in order.", "the rubbish is collected every tuesday",
   "Passive: *is* + 3rd form. The rubbish does not collect anything; someone collects it.",
   "Ciešamā kārta: *is* + 3. forma. Atkritumi neko nesavāc; tos kāds savāc.",
   also=["every tuesday the rubbish is collected"])
pt()
gp(T, L, 3, "When ___ your house ___? It looks very old. (build)", "was / built",
   "A house does not build anything: someone built it, and long ago. A passive question: *When was your house built?*",
   "Māja neko nebūvē: to kāds uzbūvēja, un sen. Jautājums ciešamajā kārtā: *When was your house built?*")
pt()

# ---------------------------------------------------------------- word bank
gp(T, L, 3, "This hotel ___ ___ by a famous architect in the 1930s.", "was / designed",
   "The hotel did not design anything: an architect designed it. *in the 1930s* is past: *was designed*.",
   "Viesnīca neko neprojektēja: to projektēja arhitekts. *in the 1930s* ir pagātne: *was designed*.",
   bank=["was", "designed", "is", "design"])
pt()
gp(T, L, 3, "Our flight ___ ___ because of the storm, so we stayed another night at the hotel.", "was / cancelled",
   "A flight does not cancel anything: the airline cancelled it. *stayed* is past: *was cancelled*.",
   "Reiss neko neatceļ: to atcēla aviokompānija. *stayed* ir pagātne: *was cancelled*.",
   bank=["was", "cancelled", "is", "cancel"])
pt()
gp(T, L, 3, "These days, in many Spanish families, dinner ___ ___ quite late, often after nine.", "is / eaten",
   "Dinner does not eat: people eat it, so passive. A habit now: *is eaten*.",
   "Vakariņas neēd: tās ēd cilvēki, tāpēc ciešamā kārta. Ieradums tagad: *is eaten*.",
   bank=["is", "eaten", "ate", "was"])
pt()
gp(T, L, 3, "The police ___ the thief two hours after the robbery.", "caught",
   "The police did the catching, so active. The robbery is past: *caught*.",
   "Policija pati noķēra, tāpēc darāmā kārta. Laupīšana ir pagātnē: *caught*.",
   bank=["caught", "was caught", "were caught", "catch"])
pt()

# ---------------------------------------------------------------- typed gaps
gp(T, L, 3, "The first email ___ in 1971. (send)", "was sent",
   "An email does not send anything: someone sent it. *in 1971* is past: *was sent*.",
   "Pirmo elektronisko vēstuli kāds nosūtīja; tā pati neko nesūta. *in 1971* ir pagātne: *was sent*.")
pt()
gp(T, L, 3, "I ___ my husband at a friend's wedding twelve years ago. (meet)", "met",
   "I did the meeting, so active. *twelve years ago* is past: *met*.",
   "Es pati satiku, tāpēc darāmā kārta. *twelve years ago* ir pagātne: *met*.")
pt()
gp(T, L, 3, "In this café, breakfast ___ until eleven every day. (serve)", "is served",
   "Breakfast does not serve: the staff serve it, so passive. *every day* is a habit now: *is served*.",
   "Brokastis neko nepasniedz: tās pasniedz darbinieki, tāpēc ciešamā kārta. *every day* ir ieradums tagad: *is served*.")
pt()
gp(T, L, 3, "What ___ at the meeting yesterday? (happen)", "happened | was happening",
   "*happen* has no object, so it has no passive: *happened*. *yesterday* is past.",
   "*happen* nav papildinātāja, tāpēc tam nav ciešamās kārtas: *happened*. *yesterday* ir pagātne.")
pt()
note("was happening :: Also correct: it asks what was going on during the meeting. Not *was happened*: *happen* has no passive. :: Arī pareizi: jautā, kas notika sapulces laikā. Nevis *was happened*: *happen* nav ciešamās kārtas.")
gp(T, L, 3, "All our bread ___ by hand in a small kitchen behind the shop. (make)", "is made",
   "Bread does not make anything: the bakers make it, so passive. It is how the shop works now: *is made*.",
   "Maize neko netaisa: to taisa maiznieki, tāpēc ciešamā kārta. Tā veikals strādā tagad: *is made*.")
pt()
gp(T, L, 3, "Our teacher ___ us homework every Friday, and today is Friday! (give)", "gives",
   "The teacher does the giving, so active. *every Friday* is a habit now: *gives*.",
   "Skolotājs pats uzdod, tāpēc darāmā kārta. *every Friday* ir ieradums tagad: *gives*.")
pt()

# ---------------------------------------------------------------- correct the mistake
tx(T, L, 3, "Correct the mistake: My phone repaired in only twenty minutes yesterday.",
   "My phone was repaired in only twenty minutes yesterday. | My phone got repaired in only twenty minutes yesterday.",
   "A phone does not repair anything: someone repaired it. Passive past: *was repaired*.",
   "Telefons neko neremontē: to kāds salaboja. Ciešamā kārta pagātnē: *was repaired*. Latviski \"telefonu salaboja\" ir bez *was*, tāpēc, tulkojot burtiski, to izlaiž.")
pt()
note("My phone got repaired in only twenty minutes yesterday. :: Also correct: *got* + 3rd form is the passive of everyday speech. :: Arī pareizi: *got* + 3. forma ir sarunvalodas ciešamā kārta.")
tx(T, L, 3, "Correct the mistake: Our train was arrived forty minutes late, so we missed the start of the concert.",
   "Our train arrived forty minutes late, so we missed the start of the concert.",
   "*arrive* has no object, so it has no passive: *Our train arrived*.",
   "*arrive* nav papildinātāja, tāpēc tam nav ciešamās kārtas: *Our train arrived*.")
pt()
tx(T, L, 3, "Correct the mistake: Cars aren't allowing in the city centre on Sundays.",
   "Cars aren't allowed in the city centre on Sundays. | Cars are not allowed in the city centre on Sundays.",
   "Cars do not allow anything: the city does not allow them. Passive: *aren't allowed*.",
   "Mašīnas neko neatļauj: pilsēta tās neatļauj. Ciešamā kārta: *aren't allowed*.")
pt()

# ---------------------------------------------------------------- rewrite
tx(T, L, 3, "Start with *My keys*: Someone found my keys in the car.",
   "My keys were found in the car. | My keys were found in the car by someone. | My keys were found by someone in the car. | My keys have been found in the car.",
   "*Someone* says nothing new, so the passive leaves it out: *My keys were found*. *found* is past: *were* + 3rd form.",
   "*Someone* neko jaunu nepasaka, tāpēc ciešamajā kārtā to izlaiž: *My keys were found*. *found* ir pagātne: *were* + 3. forma.")
pt()
note("My keys were found in the car by someone. :: Also correct, but *by someone* adds nothing: leave it out. :: Arī pareizi, bet *by someone* neko nepievieno: to izlaiž.",
     "My keys were found by someone in the car. :: Also correct, but *by someone* adds nothing: leave it out. :: Arī pareizi, bet *by someone* neko nepievieno: to izlaiž.",
     "My keys have been found in the car. :: Also correct: news now. *found* in the task is past: *were found*. :: Arī pareizi: jaunums tagad. *found* uzdevumā ir pagātne: *were found*.")
tx(T, L, 3, "Start with *A lot of rice*: They grow a lot of rice in this region.",
   "A lot of rice is grown in this region. | A lot of rice grows in this region.",
   "*They* here means people in general, so the passive leaves it out. *grow* is present: *is grown*.",
   "*They* šeit nozīmē cilvēkus vispār, tāpēc ciešamajā kārtā to izlaiž. *grow* ir tagadne: *is grown*.")
pt()
note("A lot of rice grows in this region. :: Also correct: here the rice does the growing. *is grown* says that people grow it. :: Arī pareizi: te rīsi paši aug. *is grown* saka, ka to audzē cilvēki.")
tx(T, L, 3, "Start with *A boy from our street*: The window was broken by a boy from our street.",
   "A boy from our street broke the window.",
   "The boy did it, so the sentence that starts with him is active: *broke*. *was broken* is past, so *broke* is past too.",
   "Zēns to izdarīja, tāpēc teikums, kas sākas ar viņu, ir darāmajā kārtā: *broke*. *was broken* ir pagātne, tāpēc arī *broke*.")
pt()

save("active-passive-1.csv")
