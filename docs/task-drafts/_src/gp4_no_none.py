"""Batch 4, point no_none (B1.1): no, none, not any. Murphy unit 86.
no + noun (There's no milk) = not any + noun (There isn't any milk); none alone (How many? None.) or none of + the / my / them
(None of my friends came); only one negative in the sentence. After none of + plural noun Murphy 86 allows a singular or a plural
verb: no task here makes the learner choose between them (past verbs and modals are used instead)."""
from lib import gp, od, mc, tx, mt, learning_task
T = "Quantity"
L = "B1.1"

NO_N = ("*no* + noun = *not any* + noun: *There's no milk.* = *There isn't any milk.* The verb stays positive.",
        "*no milk* = *not any milk*: *There's no milk.* = *There isn't any milk.* Darbības vārds nav noliegumā.")
NONE = ("*none* stands alone, without a noun: *There was none left.* Before a noun use *no*: *There was no bread.*",
        "*none* lieto bez lietvārda: *There was none left.* Ar lietvārdu: *There was no bread.*")
NONE_OF = ("Before *the / my / them* use *none of*: *None of my friends came.* Not *No of*, not *None my friends*.",
           "Pirms *the / my / them* lieto *none of*: *None of my friends came.* Nevis *No of* un nevis *None my friends*.")
ONE_NEG = ("Only one negative: *There isn't any milk* or *There's no milk*, not *There isn't no milk*.",
           "Tulkojot burtiski *Nav nekāda piena*, sanāk divi noliegumi (*There isn't no milk*). Angliski lieto tikai vienu: *There isn't any milk* vai *There's no milk*.")
ANY = ("After a negative verb (*didn't, haven't, aren't*) use *any*, not *no*: *We haven't got any coffee.*",
       "Ja darbības vārds ir noliegumā (*didn't, haven't, aren't*), lieto *any*: *We haven't got any coffee*, nevis *haven't got no coffee*.")

# choose (7)
mc(T, L, 2, "Choose the correct option: The hotel was nice, but there was ___ hot water in our room.", "no", ["none", "any", "none of"],
   "*was* is positive and a noun follows, so use *no*: *there was no hot water*. *none* is used without a noun.",
   "*was* nav noliegumā, un aiz tukšās vietas ir lietvārds: *there was no hot water*. *none* lieto bez lietvārda.")
mc(T, L, 2, "Choose the correct option: I needed paper for the printer, but there was ___ left.", "none", ["no", "any", "none of"], *NONE)
mc(T, L, 2, "Which sentence is correct?", "There aren't any shops in our village, so we drive to town.",
   ["There aren't no shops in our village, so we drive to town.", "There are any shops in our village, so we drive to town.",
    "There are none shops in our village, so we drive to town."], *ONE_NEG)
mc(T, L, 2, "Which sentence is correct?", "None of my friends could come to my party, so I cancelled it.",
   ["No of my friends could come to my party, so I cancelled it.", "None my friends could come to my party, so I cancelled it.",
    "None of my friends couldn't come to my party, so I cancelled it."],
   "*None of* + *my friends*, and the verb stays positive: *None of my friends could come.* *None ... couldn't* is a double negative.",
   "*None of* + *my friends*, un darbības vārds nav noliegumā: *None of my friends could come.* *None ... couldn't* ir divi noliegumi.")
# nothing is the neighbouring point (indefinite pronouns): here only as the double negative to find (Murphy 86)
mc(T, L, 2, "Which sentence is NOT correct?", "I don't have nothing to wear to my cousin's wedding.",
   ["There's no time to cook tonight, so let's order a pizza.", "None of the shops opened before ten on Sunday.",
    "I haven't got any cash, so can I pay by card?"],
   "Only one negative: *I don't have anything to wear* or *I have nothing to wear*, not *don't ... nothing*.",
   "Tulkojot burtiski *Man nav nekā, ko vilkt*, sanāk divi noliegumi. Angliski lieto vienu: *I don't have anything to wear* vai *I have nothing to wear*.")
mc(T, L, 2, "Choose the correct option: 'How many tickets are left for tonight's concert?' '___. They're all sold out.'", "None",
   ["No", "Any", "No one"],
   "A short answer without a noun is *None*: *How many are left? None.* *No* needs a noun, and *no one* is for people.",
   "Īsa atbilde bez lietvārda ir *None*: *How many are left? None.* Ar lietvārdu saka *no tickets*, un *no one* attiecas uz cilvēkiem.")
mc(T, L, 2, "Choose the correct option: We asked five language schools about evening courses, but ___ them had a free place.", "none of",
   ["no", "none", "any of"], *NONE_OF)

# type a word (5): the instruction names the two words to choose from where several words could fit
gp(T, L, 3, "Write *no* or *any*: My new phone has ___ headphone jack, so I use wireless earbuds.", "no",
   "*has* is positive, so use *no*: *It has no headphone jack.* (= *It doesn't have a headphone jack.*)",
   "*has* nav noliegumā: *It has no headphone jack.* (= *It doesn't have a headphone jack.*)")
gp(T, L, 3, "Write *no* or *any*: Our teacher didn't give us ___ homework over the holidays.", "any", *ANY)
gp(T, L, 3, "Write *no* or *none*: I wanted to buy fresh bread after work, but there was ___ left.", "none", *NONE)
gp(T, L, 3, "Write *no* or *none*: ___ of the photos I took at the concert came out well. It was too dark.", "None | none", *NONE_OF)
gp(T, L, 3, "Complete with one word: There ___ any direct flights, so we had to change planes in Frankfurt.", "weren't | aren't",
   "*any* goes with a negative verb: *There weren't any direct flights.* (= *There were no direct flights.*)",
   "*any* lieto ar darbības vārdu noliegumā: *There weren't any direct flights.* (= *There were no direct flights.*)")

# whole sentence (3)
tx(T, L, 4, "Say it another way with *no*: There aren't any vegetarian dishes on the menu.",
   "There are no vegetarian dishes on the menu. | On the menu there are no vegetarian dishes. | The menu has no vegetarian dishes.", *NO_N)
tx(T, L, 4, "Say it another way with *any*: I've got no plans for the weekend.",
   "I haven't got any plans for the weekend. | I don't have any plans for the weekend. | I've not got any plans for the weekend. | I haven't any plans for the weekend.", *ANY)
tx(T, L, 4, "Correct the mistake: We didn't get no answer from the bank, so I called them again.",
   "We didn't get any answer from the bank, so I called them again. | We got no answer from the bank, so I called them again. | We didn't get an answer from the bank, so I called them again.",
   "Only one negative: *We didn't get any answer* or *We got no answer*, not *didn't get no answer*.",
   "Tulkojot burtiski *Mēs nesaņēmām nekādu atbildi*, sanāk divi noliegumi. Angliski lieto vienu: *We didn't get any answer* vai *We got no answer*.")

# word order (5)
od(T, L, 3, "Put the words in order.", "i didn't have any time to revise for the test", *ANY)
od(T, L, 3, "Put the words in order.", "none of my colleagues knew that the meeting was cancelled", *NONE_OF)
od(T, L, 3, "Put the words in order to make a question.", "why are there no taxis at the station", *NO_N)
od(T, L, 3, "Put the words in order.", "no cars are allowed in the old town at weekends",
   "*no* + noun can start a sentence, and the verb stays positive: *No cars are allowed.*",
   "Teikums var sākties ar *No cars*, un darbības vārds nav noliegumā: *No cars are allowed.*",
   also=["at weekends no cars are allowed in the old town", "in the old town no cars are allowed at weekends", "no cars are allowed at weekends in the old town"])
od(T, L, 3, "Put the words in order.", "we had no idea that they were getting married", *NO_N, also=["they had no idea that we were getting married"])

# word bank (4): the wrong chips make the mistakes of this point (double negative, none + noun, No of, any in a positive sentence)
gp(T, L, 3, "Sorry, there ___ ___ seats left on the morning train.", "are / no", *ONE_NEG, bank=["are", "no", "aren't", "none"])
gp(T, L, 3, "___ ___ the students passed the first test, so the teacher explained it again.", "None / of", *NONE_OF, bank=["None", "of", "No", "Any"])
gp(T, L, 3, "Our phones had ___ signal in the mountains, so we used a paper map.", "no", *NO_N, bank=["no", "any", "none"])
gp(T, L, 3, "We haven't got ___ coffee left, so I'll buy some on the way home.", "any", *ANY, bank=["any", "no", "none"])

# matching (1): a learning task automatically. Each beginning takes only its own ending (plural noun / of + them / uncountable noun / no noun)
mt(T, L, 2, "Match each beginning with its ending.", [
   ("The hotel was full, so there were no", "rooms for us."),
   ("I sent my CV to four companies, but none of", "them replied."),
   ("I can't pay for the taxi. I don't have any", "cash on me."),
   ("I wanted more coffee, but there was", "none left in the pot.")],
   "*no* + noun (*no rooms*), *none of* + *them*, *not any* + noun (*don't have any cash*), *none* without a noun (*there was none left*).",
   "Ar lietvārdu: *there were no rooms* un *don't have any cash*; pirms *them*: *none of them*; bez lietvārda: *there was none left*.")
