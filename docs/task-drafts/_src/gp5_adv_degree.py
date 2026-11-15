"""Batch 5, point adv_degree (A2.2): 8 tasks to reach 10 counted tasks. Murphy unit 104 (very / quite / really + adjective),
with 109 (verb + object order: I like my job very much) and 110 (really before the verb)."""
from lib import gp, od, mc, tx
T = "Adverbs: manner, frequency, degree"
L = "A2.2"

VM = ("*very much* goes at the end, after the verb and its object: *We enjoyed the class very much.* Not *very* or *much* alone, and not *much very*.",
      "*very much* ir teikuma beigās, aiz darbības vārda un tā papildinātāja: *We enjoyed the class very much.* Nevis *very*, *much* vai *much very*.")
VERB = ("*very* goes before an adjective or an adverb (*very good, very fast*), never before a verb. With a verb: *I really like it* or *I like it very much*.",
        "Tulkojot burtiski ļoti patīk, sanāk *I very like it*. Angliski *very* liek pirms īpašības vārda vai apstākļa vārda (*very good*); ar darbības vārdu saka *I really like it* vai *I like it very much*.")
ADJ = ("A degree word goes right before the adjective: *a very nice holiday*, *really good*, *quite small*.",
       "Pakāpes apstākļa vārds ir tieši pirms īpašības vārda: *a very nice holiday*, *really good*, *quite small*.")
TOO = ("*too* + adjective = more than is good: *too heavy*. Not *too much heavy* or *very much heavy*; *too much* goes with a noun (*too much luggage*).",
       "*too* + īpašības vārds = vairāk, nekā vajag: *too heavy*. Nevis *too much heavy* vai *very much heavy*; *too much* lieto ar lietvārdu (*too much luggage*).")

# choose (2)
mc(T, L, 2, "Choose the correct option: We enjoyed the cooking class ___.", "very much", ["very", "much", "much very"], *VM)
mc(T, L, 2, "Which sentence has a mistake?", "We very enjoyed the concert.",
   ["The hotel was quite small.", "My boss speaks really fast.", "This soup is too salty."], *VERB)
# word order (2)
od(T, L, 3, "Put the words in order.", "i like my new flat very much", *VM, also=["i very much like my new flat"])
# word bank (1 of 2)
gp(T, L, 3, "This suitcase is ___ heavy for me.", "too", *TOO, bank=["too", "too much", "very much"])
# typed gap (1)
gp(T, L, 3, "Complete with one word: My grandmother loves her garden very ___.", "much", *VM)
# word order (2 of 2)
od(T, L, 3, "Put the words in order.", "we had a very nice holiday", *ADJ)
# word bank (2 of 2)
gp(T, L, 3, "I ___ like this podcast.", "really", *VERB, bank=["really", "very", "much"])
# whole sentence (1)
tx(T, L, 4, "Say it another way with *really*: We liked the new restaurant very much.", "We really liked the new restaurant.", *VERB)
