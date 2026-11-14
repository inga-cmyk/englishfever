"""A2.2 tasks for two points the teacher moved to A2.2 (13 November, decision 2; docs/GRAMMAR-MAP-GAPS.md section 5):
rel_subj (who / which / that as the subject) and might (might / may: possibility). 25 each, mix of the rules (3 choose, 4 drag,
2 type a word, 1 whole sentence per 10). DRAFT: written to pending/, not packaged, until the teacher has read it.
Grammar checked against Murphy 92 (relative clauses) and 29-30 (may, might)."""
from lib import rows, save, gp, od, mc, tx, mt

REL = "Relative clauses"
R_EN = "*who* (or *that*) for people, *which* (or *that*) for things, then the verb: *the woman who lives next door*."
R_LV = "*who* (vai *that*) cilvēkiem, *which* (vai *that*) lietām, tad darbības vārds: *the woman who lives next door*."
R_AGR = ("After *who / which / that* the verb agrees with the noun before it: *the people who live*, *the bus which goes*.",
         "Aiz *who / which / that* darbības vārds saskan ar lietvārdu pirms tā: *the people who live*, *the bus which goes*.")
R_NO2 = ("*who / which / that* is already the subject: no second *he / she / it* (*the girl who lives here*, not *the girl who she lives here*).",
         "*who / which / that* jau ir teikuma priekšmets: otru *he / she / it* neliek (*the girl who lives here*, nevis *the girl who she lives here*).")
R_JOIN = ("Join with *who* (people) or *which / that* (things); the second *he / she / it* goes.",
          "Savieno ar *who* (cilvēki) vai *which / that* (lietas); otrais *he / she / it* izpaliek.")
L = "A2.2"

# choose (8)
gp(REL, L, 3, "I have a friend ___ lives in Canada.", "who", R_EN, R_LV, bank=["who", "which", "what"])
mc(REL, L, 2, "Choose the correct option: We stayed at a hotel ___ has a big pool.", "which", ["who", "what", "where"], R_EN, R_LV)
mc(REL, L, 2, "Choose the correct option: I use an app ___ makes short videos.", "that", ["who", "what", "where"], R_EN, R_LV)
mc(REL, L, 2, "Which sentence is correct?", "The man who fixed my car was very kind.",
   ["The man which fixed my car was very kind.", "The man who he fixed my car was very kind.", "The man what fixed my car was very kind."], *R_NO2)
mc(REL, L, 2, "Which sentence is correct?", "I need a laptop that is light.",
   ["I need a laptop who is light.", "I need a laptop that it is light.", "I need a laptop what is light."], *R_NO2)
mc(REL, L, 2, "Choose the correct option: The people who ___ next door are very friendly.", "live", ["lives", "living", "is living"], *R_AGR)
mc(REL, L, 2, "Choose the correct option: The bus which ___ to the airport leaves at six.", "goes", ["go", "going", "gone"], *R_AGR)
mc(REL, L, 2, "Which sentence is NOT correct?", "I know a woman which speaks five languages.",
   ["We need a teacher who can sing.", "It's a film that makes people laugh.", "The shop which sells fresh bread is closed today."], R_EN, R_LV)
# type a word (5): every correct word is accepted (that for people and things)
gp(REL, L, 3, "Write the missing word: A pilot is a person ___ flies planes.", "who | that", R_EN, R_LV)
gp(REL, L, 3, "Write the missing word: I bought a bike ___ has ten gears.", "which | that", R_EN, R_LV)
gp(REL, L, 3, "Write the missing word: The woman ___ teaches us yoga is from India.", "who | that", R_EN, R_LV)
gp(REL, L, 3, "Write the missing word: Do you like songs ___ tell a story?", "which | that", R_EN, R_LV)
gp(REL, L, 3, "Write the missing word: On our trip we met a guide ___ spoke perfect English.", "who | that", R_EN, R_LV)
# whole sentence (3)
tx(REL, L, 4, "Join with *who*: I have a cousin. He works in a hotel.", "I have a cousin who works in a hotel.", *R_JOIN)
tx(REL, L, 4, "Join the two sentences: We visited a museum. It has old cars.",
   "We visited a museum which has old cars. | We visited a museum that has old cars.", *R_JOIN)
tx(REL, L, 4, "Join the two sentences: The app helps me learn new words. It is free.",
   "The app which helps me learn new words is free. | The app that helps me learn new words is free. | The app which is free helps me learn new words. | The app that is free helps me learn new words.", *R_JOIN)
# word order (5)
od(REL, L, 3, "Put the words in order.", "i have a neighbour who plays the piano", R_EN, R_LV)
od(REL, L, 3, "Put the words in order.", "we stayed in a flat that had a garden", R_EN, R_LV)
od(REL, L, 3, "Put the words in order.", "she wants a job which pays well", R_EN, R_LV)
od(REL, L, 3, "Put the words in order.", "my uncle has a shop that sells bikes", R_EN, R_LV)
od(REL, L, 3, "Put the words in order.", "she met a man who makes furniture", R_EN, R_LV)
# word bank (3): chips are real words of this point that do not fit
gp(REL, L, 3, "I know a man ___ ___ three languages.", "who / speaks", *R_AGR, bank=["who", "speaks", "which", "speak"])
gp(REL, L, 3, "We bought a car ___ uses very little petrol.", "which", R_EN, R_LV, bank=["which", "who", "what"])
gp(REL, L, 3, "The women who ___ in the next office are my colleagues.", "work", *R_AGR, bank=["work", "works", "working"])
# matching (1): a learning task
mt(REL, L, 2, "Match each beginning with its ending.", [("A baker is a person", "who makes bread."), ("A fridge is a machine", "which keeps food cold."),
   ("A tourist is someone", "who travels for fun."), ("A map is a picture", "which shows roads and towns.")], R_EN, R_LV)

MOD = "More modals: might, could, be able to"
M_EN = "*might / may* + base verb (no *to*, no *-s*) = it is possible: *It might rain.*"
M_LV = "*might / may* + pamatforma (bez *to*, bez *-s*) = iespējams: *It might rain.*"
M_NEG = ("Negative: *might not / may not* + base verb, without *don't / doesn't*: *He might not come.*",
         "Noliegums: *might not / may not* + pamatforma, bez *don't / doesn't*: *He might not come.*")
M_MAYBE = ("*may* is the verb: *I may be late.* *maybe* means *perhaps* and needs its own verb: *Maybe I'll be late.*",
           "*may* ir darbības vārds: *I may be late.* *maybe* nozīmē *varbūt*, un tam vajag savu darbības vārdu: *Maybe I'll be late.*")
M_ANY = ("*might, may* and *could* all say that something is possible here.",
         "*might, may* un *could* šeit visi saka, ka kaut kas ir iespējams.")

# choose (8)
mc(MOD, L, 2, "Choose the correct option: Take an umbrella. It might ___ later.", "rain", ["rains", "to rain", "raining"], M_EN, M_LV)
mc(MOD, L, 2, "Which sentence is correct?", "She may be at home now.", ["She may is at home now.", "She may to be at home now.", "She may being at home now."], M_EN, M_LV)
mc(MOD, L, 2, "Choose the correct option: I'm not sure yet. We ___ go to the beach on Saturday.", "might", ["might to", "may to", "maybe"], M_EN, M_LV)
mc(MOD, L, 2, "Choose the correct option: He's very tired. He ___ not come to the party.", "might", ["doesn't", "is", "don't"], *M_NEG)
mc(MOD, L, 2, "Which sentence is NOT correct?", "Maybe it will might snow tonight.",
   ["Our flight might be late.", "They may not have time today.", "I might buy a new phone."],
   "Don't use *will* and *might* together: *It might snow.* or *Maybe it will snow.*", "Nelieto *will* un *might* kopā: *It might snow.* vai *Maybe it will snow.*")
mc(MOD, L, 2, "Which sentence is correct?", "Ask Tom. He might know the answer.",
   ["Ask Tom. He might knows the answer.", "Ask Tom. He might to know the answer.", "Ask Tom. He might knowing the answer."], M_EN, M_LV)
gp(MOD, L, 3, "The pharmacy may ___ closed on Sunday.", "be", M_EN, M_LV, bank=["be", "is", "being"])
mc(MOD, L, 2, "Choose the correct option: Don't wait for me. I ___ be late.", "may", ["maybe", "may to"], *M_MAYBE)
# type a word (5): might, may and could are all accepted
gp(MOD, L, 3, "Write the missing word: I'm not sure, but I ___ visit my aunt this weekend.", "might | may | could", *M_ANY)
gp(MOD, L, 3, "Write the missing word: The road is icy. You ___ fall, so be careful.", "might | may | could | can", *M_ANY)
gp(MOD, L, 3, "I can't see Anna's car. She might ___ at home. (not / be)", "not be", *M_NEG)
gp(MOD, L, 3, "Write the missing word: Take your laptop. I'm not sure, but we ___ need it on the trip.", "might | may | could", *M_ANY)
gp(MOD, L, 3, "Write the missing word: I'm not sure, but they ___ have a map of the town at the desk.", "might | may | could", *M_ANY)
# whole sentence (3)
tx(MOD, L, 4, "Rewrite with *might*: Perhaps the concert tickets are sold out.", "The concert tickets might be sold out.", M_EN, M_LV)
tx(MOD, L, 4, "Make it negative: We might finish the project today.", "We might not finish the project today. | We mightn't finish the project today.", *M_NEG)
tx(MOD, L, 4, "Say it another way with *may*: It's possible that she knows Anna.", "She may know Anna.", M_EN, M_LV)
# word order (5)
od(MOD, L, 3, "Put the words in order.", "the café might be busy today", M_EN, M_LV)
od(MOD, L, 3, "Put the words in order.", "i may not have time for lunch", *M_NEG)
od(MOD, L, 3, "Put the words in order.", "they might move to another city", M_EN, M_LV)
od(MOD, L, 3, "Put the words in order.", "you might need a warm jacket", M_EN, M_LV)
od(MOD, L, 3, "Put the words in order.", "my phone might not work in the mountains", *M_NEG, also=["in the mountains my phone might not work"])
# word bank (3)
gp(MOD, L, 3, "It ___ ___ tomorrow, so I'm taking my boots.", "might / snow", M_EN, M_LV, bank=["might", "snow", "snows", "to"])
gp(MOD, L, 3, "She may ___ ___ the meeting today.", "not / join", *M_NEG, bank=["not", "join", "doesn't", "joins"])
gp(MOD, L, 3, "You ___ ___ this film. It's very funny.", "might / like", M_EN, M_LV, bank=["might", "like", "likes", "liking"])
# matching (1): a learning task
mt(MOD, L, 2, "Match each sentence with its meaning.", [("It will rain.", "I'm sure about the rain."), ("She might call.", "Perhaps she will call."),
   ("He won't come.", "I'm sure he will stay at home."), ("They might not win.", "Perhaps they will lose.")],
   "*will* = sure; *might* = perhaps. *won't* and *might not* are the negatives.", "*will* = droši; *might* = varbūt. *won't* un *might not* ir nolieguma formas.")

save("pending/a2-rel-might-1.csv")
