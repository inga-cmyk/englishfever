"""Batch 5, point adj_basic (A2.1): 9 tasks to reach 10 counted tasks. Murphy unit 99."""
from lib import gp, od, mc, tx
T = "Adjective order (a small old car)"
L = "A2.1"

# Murphy 99: adjectives go before a noun (a good job) or after be (The shops are expensive); they have no plural form (big bags, not bigs bags).
POS = ("An adjective goes before the noun: *a very good job* (not *a job very good*).",
       "Īpašības vārds stāv pirms lietvārda: *a very good job* (nevis *a job very good*).")
BE = ("After a noun the adjective needs *be*: *The shops are expensive.* The adjective never takes *-s*: not *expensives*.",
      "Aiz lietvārda īpašības vārdam vajag *be*: *The shops are expensive.* Īpašības vārdam nekad nepievieno *-s*: nevis *expensives*.")
PL = ("Only the noun takes *-s*; the adjective stays the same and goes first: *two big bags* (not *two bigs bags*, *two bags big*).",
      "Tulkojot burtiski, *divas lielas somas*: latviešu valodā īpašības vārdam ir daudzskaitlis, angļu valodā nav. *-s* saņem tikai lietvārds, un īpašības vārds ir pirms tā: *two big bags* (nevis *two bigs bags*, *two bags big*).")

# 1. choice: be + adjective, no -s (2 x 2 options)
mc(T, L, 2, "Choose the correct option: The shops here ___.", "are very expensive",
   ["very expensive", "are very expensives", "very expensives"], *BE)
# 2. word order: the adjective before the noun
od(T, L, 3, "Put the words in order.", "she has a very good job", *POS)
# 3. typed gap: adjective first, -s only on the noun
gp(T, L, 3, "Use the words in brackets: I need two ___ for the trip. (bag / big)", "big bags", *PL)
# 4. word bank: -s on the noun only
gp(T, L, 3, "We have two ___ ___ in our garden.", "big / trees", *PL, bank=["big", "bigs", "trees", "tree"])
# 5. choice: one mistake of this point, three correct sentences about three different things
mc(T, L, 2, "Which sentence has a mistake?", "We rented a car small for the week.",
   ["The lesson was short and useful.", "I need two new batteries for my camera.", "Her flat has big windows."],
   "The adjective goes before the noun: *a small car*. After *be* it can stand alone (*The lesson was short*), and it has no *-s* (*new batteries*).",
   "Īpašības vārds stāv pirms lietvārda: *a small car*. Aiz *be* tas var stāvēt viens (*The lesson was short*), un tam nav *-s* (*new batteries*).")
# 6. typed gap: be + adjective, no -s
gp(T, L, 3, "Use the words in brackets: My new headphones ___. (comfortable / very / be)", "are very comfortable | were very comfortable", *BE)   # r13: no time word, the past is correct too
# 7. word order: be + adjective
od(T, L, 3, "Put the words in order.", "my grandmother is very active for her age",
   "After *be* the adjective comes alone, without a noun: *My grandmother is very active.*",
   "Aiz *be* īpašības vārds var stāvēt viens, bez lietvārda: *My grandmother is very active.*",
   also=["for her age my grandmother is very active"])
# 8. word bank: be + adjective, no -s
gp(T, L, 3, "The rooms in this hotel ___ very ___.", "are / clean", *BE, bank=["are", "clean", "cleans", "have"])
# 9. whole sentence: from before the noun to after be
tx(T, L, 4, "Start with *Our*: We have very nice neighbours.", "Our neighbours are very nice. | Our neighbours are nice. | Our neighbours are really nice.",
   "The adjective moves after *be* and stays without *-s*: *Our neighbours are very nice.* (not *very nices*).",
   "Īpašības vārds pāriet aiz *be* un paliek bez *-s*: *Our neighbours are very nice.* (nevis *very nices*).")
