"""Batch 5, point unc_nouns (A2.2): 9 tasks to reach 10 counted tasks. Murphy unit 69 (countable and uncountable 1:
advice, information, furniture, luggage, news are uncountable: no a / an, no plural, a singular verb; a piece of advice,
some furniture) and unit 70 (countable and uncountable 2: a piece of + uncountable; How much luggage / How many bags).
The point has one typed gap (The news ___ good), so most new tasks are check tasks (choices, banks, orders).
Wrong options and chips are the learner mistakes the map lists: an information / a useful information, advices,
furnitures / a furniture, luggages, a good news, a plural verb (are)."""
from lib import gp, od, mc, tx
T = "Quantity"
L = "A2.2"

UNC = ("*advice, information, furniture, news, luggage* are uncountable: no *a / an*, no plural *-s*, and a singular verb: *some news, The furniture is new.*",
       "*advice, information, furniture, news, luggage* ir neskaitāmi lietvārdi: bez *a / an*, bez daudzskaitļa *-s*, un darbības vārds vienskaitlī: *some news, The furniture is new.*")
VERB = ("An uncountable noun takes a singular verb: *is*, *has*, verb + *-s*. *luggage* has no plural: *My luggage is …*",
        "Neskaitāmam lietvārdam darbības vārds ir vienskaitlī: *is*, *has*, darbības vārds + *-s*. *luggage* nav daudzskaitļa: *My luggage is …*")
ADV = ("*advice* is uncountable: *some advice*, *a piece of advice*, never *an advice* or *advices*; the verb is singular: *Your advice is…*",
       "*advice* ir neskaitāms lietvārds: *some advice*, *a piece of advice*, nekad *an advice* vai *advices*; darbības vārds vienskaitlī: *Your advice is…* "
       "Tulkojot burtiski, latviešu *padoms, padomi* dod *an advice, advices*.")
PIECE = ("To count an uncountable noun, use *a piece of / two pieces of*: *a piece of advice*, *How many pieces of luggage?*",
         "Lai saskaitītu neskaitāmu lietvārdu, lieto *a piece of / two pieces of*: *a piece of advice*, *How many pieces of luggage?*")

# 1 choice (check), relationships: news is uncountable, no a / an. Learners write "a good news" (Latvian "laba ziņa")
# and "a good new"; "good news" without some would also be correct, so it is not an option.
mc(T, L, 2, "Choose the correct option: I have ___ for you!", "some good news", ["a good news", "a good new"],
   "*news* is uncountable and always ends in *-s*: *some good news*, *the news*, never *a news* or *a new*.",
   "*news* ir neskaitāms lietvārds un vienmēr beidzas ar *-s*: *some good news*, *the news*, nekad *a news* vai *a new*. "
   "Tulkojot burtiski, *laba ziņa* dod *a good news*.")

# 2 word bank (check), technology: some + information; a useful information and informations are the two typical mistakes.
gp(T, L, 3, "I found ___ useful ___ on this website.", "some / information", *UNC,
   bank=["some", "a", "information", "informations"])

# 3 choice (check), work: the mistake is an advice; the three correct sentences are about three other things:
# a singular verb after furniture (home), much + luggage in a negative (travel), some + information in a question (learning)
mc(T, L, 2, "Which sentence has a mistake?", "My boss gave me a useful advice.",
   ["Our new furniture is very comfortable.", "We haven't got much luggage.", "Can I ask you for some information?"], *ADV)

# 4 word order (check), relationships: the order needs the pattern a piece of + advice (not an advice, not a advice piece)
od(T, L, 3, "Put the words in order to make a question.", "can i give you a piece of advice", *PIECE)

# 5 word bank (check), travel: no plural luggages and a singular verb; every other chip pair is wrong
gp(T, L, 3, "My ___ ___ still at the airport.", "luggage / is", *VERB,
   bank=["luggage", "luggages", "is", "are"])

# 6 choice (check), work: some furniture; a furniture, furnitures and some furnitures are the learner mistakes
mc(T, L, 2, "Choose the correct option: We need ___ for our new office.", "some furniture",
   ["a furniture", "furnitures", "some furnitures"], *UNC)

# 7 typed gap (use), learning: a singular verb after advice. Thank you! rules out would be (a polite request);
# was, has been and will be are correct English with it and are accepted: the task is about singular / plural, not the time
gp(T, L, 3, "Thank you! Your advice about the exam ___ really helpful. (be)", "is | was | has been | will be | 's", *ADV)

# 8 word order (check), travel: How many + pieces of luggage (not How much luggages, not How many luggage)
od(T, L, 3, "Put the words in order to make a question.", "how many pieces of luggage do you have", *PIECE)

# 9 whole sentence (use), lifestyle: the learner must turn a plural subject and are into furniture + is
tx(T, L, 4, "Rewrite with *furniture*: The chairs and tables in this café are new.",
   "The furniture in this café is new. | The furniture in this café is all new. | All the furniture in this café is new. | "
   "All of the furniture in this café is new. | The furniture in the café is new. | This café's furniture is new. | "
   "The café's furniture is new. | This café has new furniture. | The café has new furniture.",
   "*furniture* (chairs, tables, beds…) is uncountable: no plural, and a singular verb: *The furniture is new.*",
   "*furniture* (mēbeles) ir neskaitāms lietvārds: bez daudzskaitļa, un darbības vārds vienskaitlī: *The furniture is new.* "
   "Tulkojot burtiski, *mēbeles ir* dod *furnitures are*.")
