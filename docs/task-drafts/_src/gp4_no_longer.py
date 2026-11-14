"""Batch 4, point no_longer (A2.2): no longer, any more, any longer (a situation has ended). Murphy unit 111.
no longer goes before the main verb (I no longer smoke) and after be (She is no longer my boss); the verb stays positive.
not ... any more / any longer go at the end, after a negative verb. We do not use no more in this way (Murphy 111).
anymore (one word, American) is accepted wherever any more is typed."""
from lib import gp, od, mc, tx, mt, learning_task
T = "Used to and be used to"
L = "A2.2"

NL_POS = ("*no longer* goes before the main verb, and the verb stays positive: *He no longer plays the guitar.*",
          "*no longer* liek pirms darbības vārda, un darbības vārds nav noliegumā: *He no longer plays the guitar.*")
NL_BE = ("With *be*, *no longer* goes after it: *We're no longer in the same team.*",
         "Ja teikumā ir *be*, *no longer* liek aiz tā: *We're no longer in the same team.*")
AM = ("*any more* (or *any longer*) goes at the end, after a negative verb: *I don't drive to work any more.*",
      "*any more* (vai *any longer*) liek teikuma beigās, ja darbības vārds ir noliegumā: *I don't drive to work any more.*")
ONE_NEG = ("Only one negative: *no longer* + a positive verb, or *don't* ... *any more* at the end. Not *don't ... no more*.",
           "Tulkojot burtiski *vairs ne...*, sanāk divkāršs noliegums (*I don't live there no more*). Angliski lieto vienu noliegumu: *I no longer live there* vai *I don't live there any more*.")

# choose (7). Murphy 111: no longer in the middle, any more / any longer at the end, not no more.
mc(T, L, 2, "Choose the correct option: I ___ eat meat.", "no longer", ["no more", "any more", "don't any more"],
   "*no longer* goes before the verb: *I no longer eat meat.* *any more* goes at the end, after *don't*: *I don't eat meat any more.*",
   "*no longer* liek pirms darbības vārda: *I no longer eat meat.* *any more* liek beigās, aiz *don't*: *I don't eat meat any more.*")
mc(T, L, 2, "Choose the correct option: She doesn't work here ___.", "any more", ["no more", "no longer", "more"],
   "After a negative verb, use *any more* at the end: *She doesn't work here any more.* *no more* and *no longer* would add a second negative.",
   "Tulkojot burtiski *vairs* kā *more* vai *no more*, sanāk kļūda. Ja darbības vārds ir noliegumā, teikuma beigās liek *any more*: *She doesn't work here any more.*")
mc(T, L, 2, "Which sentence is correct?", "We are no longer friends.",
   ["We are no more friends.", "We aren't no longer friends.", "We aren't friends no more."],
   "*no longer* goes after *be*, and *be* stays positive: *We are no longer friends.* Not *no more*, and not two negatives.",
   "Tulkojot burtiski, sanāk *no more* vai divkāršs noliegums. Angliski: *We are no longer friends*: aiz *are* liek *no longer*, un *are* nav noliegumā.")
mc(T, L, 2, "Which sentence is correct?", "He no longer plays the guitar.",
   ["He plays no longer the guitar.", "He no longer doesn't play the guitar.", "He doesn't no longer play the guitar."], *NL_POS)
mc(T, L, 2, "Which sentence is NOT correct?", "I don't live there no more.",
   ["My phone no longer works.", "She isn't my boss any more.", "We don't go to that gym any longer."], *ONE_NEG)
mc(T, L, 2, "Choose the correct option: The bank ___ open on Saturdays.", "is no longer", ["is no more", "no longer", "is any more"],
   "Keep *is* and put *no longer* after it: *The bank is no longer open.* Not *no more*; *any more* goes at the end, after *isn't*.",
   "Teikumā vajag *is*, un *no longer* liek aiz tā: *The bank is no longer open.* Nevis *no more*; *any more* liek beigās, aiz *isn't*.")
# the situation is needed here: without it, He still lives in Riga is correct English
mc(T, L, 2, "Choose the correct option: Tom moved to Oslo. He ___ lives in Riga.", "no longer", ["still", "any more", "no more"],
   "*still* = it continues; *no longer* = it has ended. Tom moved, so he *no longer* lives in Riga.",
   "*still* = joprojām turpinās; *no longer* = ir beidzies. Viņš pārcēlās, tāpēc: *He no longer lives in Riga.*")

# type a word (5): every correct word is accepted; anymore = any more
gp(T, L, 3, "Complete with one word: My sister doesn't live with us any ___.", "more | longer",
   "*any more* or *any longer*: both go at the end, after a negative verb.",
   "*any more* vai *any longer*: abi liek teikuma beigās, ja darbības vārds ir noliegumā.")
gp(T, L, 3, "Complete with one word: I no ___ use this app.", "longer",
   "*no longer* goes before the verb: *I no longer use this app.* We don't say *no more* here.",
   "*no longer* liek pirms darbības vārda: *I no longer use this app.* Šeit nelieto *no more*.")
gp(T, L, 3, "Write *no longer* or *any more*: The airline ___ flies to Riga.", "no longer",
   "*flies* is positive, so *no longer* goes before it. *any more* needs a negative verb and goes at the end.",
   "*flies* nav noliegumā, tāpēc pirms tā liek *no longer*. *any more* vajag noliegumu, un to liek beigās.")
gp(T, L, 3, "Write *no longer* or *any more*: We don't go camping ___.", "any more | anymore | any longer",
   "*don't* is already negative, so *any more* goes at the end: *We don't go camping any more.*",
   "*don't* jau ir noliegums, tāpēc beigās liek *any more*: *We don't go camping any more.*")
gp(T, L, 3, "Complete with one word: They're ___ longer married.", "no",
   "*no longer*, not *not longer*: *They're no longer married.* (= *They aren't married any more.*)",
   "*no longer*, nevis *not longer*: *They're no longer married.* (= *They aren't married any more.*)")

# whole sentence (3): every correct position and form
tx(T, L, 4, "Say it another way with *no longer*: I don't work there any more.",
   "I no longer work there. | I am no longer working there. | I'm no longer working there.",
   "*don't ... any more* = *no longer* before a positive verb: *I no longer work there.*",
   "*don't ... any more* = *no longer* + darbības vārds, kas nav noliegumā: *I no longer work there.*")
tx(T, L, 4, "Say it another way with *no longer*: The museum isn't free any more.",
   "The museum is no longer free. | The museum's no longer free.",
   "*isn't ... any more* = *is no longer*: *no longer* goes after *is*, and *is* stays positive.",
   "*isn't ... any more* = *is no longer*: *no longer* liek aiz *is*, un *is* nav noliegumā.")
tx(T, L, 4, "Say it another way with *any more*: Ben no longer studies Spanish.",
   "Ben doesn't study Spanish any more. | Ben doesn't study Spanish anymore. | Ben isn't studying Spanish any more. | Ben isn't studying Spanish anymore. | Ben's not studying Spanish any more. | Ben's not studying Spanish anymore.",
   "*no longer studies* = *doesn't study* ... *any more*: the verb becomes negative and *any more* goes at the end.",
   "*no longer studies* = *doesn't study* ... *any more*: darbības vārds ir noliegumā, un *any more* liek beigās.")

# word order (5): no longer at the end (I drink coffee no longer) is literary, not accepted; any more only at the end
# subjects with a contraction or I, so the cards do not also make a question (is this app no longer free?)
od(T, L, 3, "Put the words in order.", "i no longer drink coffee", *NL_POS)
od(T, L, 3, "Put the words in order.", "we're no longer in the same team", *NL_BE)
od(T, L, 3, "Put the words in order.", "my old printer no longer works", *NL_POS)
od(T, L, 3, "Put the words in order.", "i don't drive to work any more", *AM)
od(T, L, 3, "Put the words in order.", "he's not my neighbour any longer", *AM)

# word bank (4): the wrong chips are the mistakes of this point (no more, any more in the wrong place, a positive verb)
gp(T, L, 3, "She is ___ my teacher.", "no longer",
   "After *is*, use *no longer*: *She is no longer my teacher.* *any more* goes at the end after *isn't*; *no more* is not used here.",
   "Tulkojot burtiski *vairs* kā *no more*, sanāk kļūda. Aiz *is* liek *no longer*: *She is no longer my teacher.* *any more* liek beigās aiz *isn't*.",
   bank=["no longer", "no more", "any more"])
gp(T, L, 3, "We don't use cash ___ ___.", "any / more",
   "*don't* is already negative, so the end is *any more*, not *no more*.",
   "*don't* jau ir noliegums, tāpēc beigās ir *any more*, nevis *no more*.",
   bank=["any", "no", "more"])
gp(T, L, 3, "This bus ___ goes to the airport.", "no longer",
   "Before a positive verb, use *no longer*: *This bus no longer goes to the airport.* *any more* goes at the end, after *doesn't*.",
   "Ja darbības vārds nav noliegumā, pirms tā liek *no longer*: *This bus no longer goes to the airport.* *any more* liek beigās, aiz *doesn't*.",
   bank=["no longer", "any more", "no more"])
gp(T, L, 3, "These shoes ___ comfortable ___.", "aren't / any more",
   "*any more* needs a negative verb: *These shoes aren't comfortable any more.*",
   "*any more* lieto ar noliegumu: *These shoes aren't comfortable any more.*",
   bank=["aren't", "are", "any more"])

# matching (1): a learning task; the grammar decides each pair (a verb after no longer, a noun after be, any more after a negative)
mt(T, L, 2, "Match each beginning with its ending.",
   [("He no longer", "plays football."), ("She is no longer", "our manager."),
    ("They don't live here", "any more."), ("We aren't", "neighbours any longer.")],
   "*no longer* before the verb (*He no longer plays*) or after *be* (*She is no longer*); *any more / any longer* at the end, after a negative verb.",
   "*no longer* pirms darbības vārda (*He no longer plays*) vai aiz *be* (*She is no longer*); *any more / any longer* beigās, ja darbības vārds ir noliegumā.")
