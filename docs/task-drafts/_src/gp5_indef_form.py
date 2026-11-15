"""Batch 5, point indef_form (A2.2): 7 tasks to reach 10 counted tasks. Murphy units 85 (some and any) and 86 (no / none / any; nothing, nobody, nowhere).
some- in positive sentences, any- in questions and negatives, no- with a positive verb, every- = all; -one / -body for people,
-thing for things, -where for places. No word order: the cards would give the word, so ordering them does not test the choice."""
from lib import gp, od, mc, tx
T = "Someone, anything, nobody"
L = "A2.2"

# choose (2)
mc(T, L, 2, "Choose the correct option: The party was great. ___ had a good time.", "Everybody", ["Anybody", "Nobody"],
   "*every-* = all the people: *Everybody had a good time.* *any-* is for questions and negatives, and *Nobody* would mean that no person had a good time.",
   "*every-* = visi cilvēki: *Everybody had a good time.* *any-* lieto jautājumos un noliegumos, bet *Nobody* nozīmētu, ka neviens nav labi pavadījis laiku.")
mc(T, L, 2, "Which sentence has a mistake?", "I heard anybody in the garden last night.",
   ["Did anyone call me this morning?", "Everybody in my office drives to work.", "Nobody in my family can cook."],
   "In a positive sentence use *some-*: *I heard somebody in the garden.* *any-* is for questions and negatives. The other three are correct: *Did anyone…?* (a question), *Everybody … drives* (all the people), *Nobody … can cook* (*no-* with a positive verb).",
   "Apgalvojumā lieto *some-*: *I heard somebody in the garden.* *any-* lieto jautājumos un noliegumos. Pārējie trīs ir pareizi: *Did anyone…?* (jautājums), *Everybody … drives* (visi cilvēki), *Nobody … can cook* (*Nobody* ar apgalvojuma formu).")

# word bank (2): the wrong chips are the any- form and the wrong ending (thing / place)
gp(T, L, 3, "My glasses are ___ in this room. Can you help me look?", "somewhere",
   "A place we don't know, in a positive sentence: *somewhere*. *anywhere* is for questions and negatives; *something* is a thing, not a place.",
   "Vieta, ko nezinām, apgalvojumā: *somewhere*. *anywhere* lieto jautājumos un noliegumos; *something* ir lieta, nevis vieta.",
   bank=["somewhere", "anywhere", "something"])
gp(T, L, 3, "There's ___ in my wallet. It's empty.", "nothing",
   "*There's* is a positive verb, so the word itself says no: *There's nothing in my wallet.* *anything* needs a negative (*There isn't anything*); *something* does not fit an empty wallet.",
   "*There's* ir apgalvojuma forma, tāpēc noliegumu izsaka pats vārds: *There's nothing in my wallet.* *anything* vajag noliegumu (*There isn't anything*); *something* neder tukšam makam.",
   bank=["nothing", "anything", "something"])

# typed gap (2): lib adds "Complete with a word like *someone, anything, nowhere*:" (the answers are not among those three words)
gp(T, L, 3, "___ works here on Sundays. The office is closed.", "Nobody | No one",
   "*Nobody / No one* already makes the sentence negative, so the verb stays positive: *Nobody works here on Sundays.*",
   "*Nobody* (arī *No one*) jau ir noliegums, tāpēc darbības vārds paliek apgalvojumā: *Nobody works here on Sundays.*")
gp(T, L, 3, "There are trees ___: in the streets, in the parks, by the river.", "everywhere",
   "*every-* = all: *everywhere* = in all places. The list after the colon shows that the trees are in all the places.",
   "*every-* = visi: *everywhere* = visur, visās vietās. Uzskaitījums aiz kola rāda, ka koki ir visās vietās.")

# whole sentence (1)
tx(T, L, 4, "Make it negative: I bought something for Anna.",
   "I didn't buy anything for Anna. | I didn't buy Anna anything. | I bought nothing for Anna.",
   "In a negative sentence *something* becomes *anything*: *I didn't buy anything for Anna.* With a positive verb, *nothing* says the same: *I bought nothing for Anna.*",
   "Noliegumā *something* kļūst par *anything*: *I didn't buy anything for Anna.* Ar apgalvojuma formu to pašu saka *nothing*: *I bought nothing for Anna.*")
