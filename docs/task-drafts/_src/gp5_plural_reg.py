"""Batch 5, point plural_reg (A2.1): 9 tasks to reach 10 counted tasks. Murphy unit Appendix 6 (spelling: -s, -es, -ies)."""
from lib import gp, od, mc, tx
T = "Irregular plurals (children, people, men, teeth)"
L = "A2.1"

ES = ("After *-s, -sh, -ch, -x* the plural adds *-es*: *bus → buses, dish → dishes, watch → watches, box → boxes*.",
      "Pēc *-s, -sh, -ch, -x* daudzskaitlī pievieno *-es*: *bus → buses, dish → dishes, watch → watches, box → boxes*.")
IES = ("Consonant + *-y*: the *y* changes to *-ies*: *city → cities, country → countries, party → parties*.",
       "Līdzskanis + *-y*: *y* pārvēršas par *-ies*: *city → cities, country → countries, party → parties*.")
VY = ("Vowel + *-y* just adds *-s*: *day → days, key → keys, boy → boys*.",
      "Patskanis + *-y*: pievieno tikai *-s*: *day → days, key → keys, boy → boys*.")

# ── choice (4) ──
# Murphy App. 6: consonant + y → -ies; "countrys" and "countryes" are the two spellings learners write; "three country" has no plural
mc(T, L, 2, "Choose the correct option: We visited three ___ on our trip.", "countries", ["countrys", "countryes", "country"], *IES)
# vowel + y: only -s; "daies / dayes" over-apply the -ies / -es rules
mc(T, L, 2, "Choose the correct option: I work late two ___ a week.", "days", ["daies", "dayes", "day"], *VY)
mc(T, L, 2, "Which sentence is correct?", "We bought two watches and three bags.",
   ["We bought two watchs and three bags.", "We bought two watches and three bages.", "We bought two watch and three bags."],
   "*watch* ends in *-ch*, so *watches*; *bag* just adds *-s*: *bags*.",
   "*watch* beidzas ar *-ch*, tāpēc *watches*; *bag* pievieno tikai *-s*: *bags*.")
# three correct sentences about three different things (a trip, housework, family), one -ies mistake
mc(T, L, 2, "Which sentence has a mistake?", "Our town has two new librarys.",
   ["We stayed in Rome for five days.", "I always wash the dishes by hand.", "Tom has two brothers and a sister."],
   "*library* ends in consonant + *-y*: *libraries*. (*days*: vowel + *-y*, only *-s*; *dishes*: *-sh* + *-es*.)",
   "*library* beidzas ar līdzskani + *-y*: *libraries*. (*days*: patskanis + *-y*, tikai *-s*; *dishes*: *-sh* + *-es*.)")

# ── word bank (2) ──
gp(T, L, 3, "We need two big ___ for the books.", "boxes", *ES, bank=["boxes", "boxs", "box"])
gp(T, L, 3, "There are lots of ___ in December.", "parties", *IES, bank=["parties", "partys", "party"])

# ── typed gap (2) ──
gp(T, L, 3, "I've got three ___ for the office. (key)", "keys", *VY)
gp(T, L, 3, "I have two English ___ a week. (class)", "classes", *ES)

# ── whole sentence (1) ──
# "busses" is a rare variant (American dictionaries list it): accepted, not taught
tx(T, L, 4, "Start with *Two*: The bus is late.", "Two buses are late. | Two busses are late.",
   "More than one: *bus → buses* (*-s* + *-es*), and the verb is plural too: *are*.",
   "Vairāk nekā viens: *bus → buses* (*-s* + *-es*), un darbības vārds arī ir daudzskaitlī: *are*.")
