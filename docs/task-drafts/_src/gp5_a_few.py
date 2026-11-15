"""Batch 5, point a_few (A2.1): 6 tasks to reach 10 counted tasks. Murphy unit 87.
a few + plural noun (a few minutes, a few cafés) = a small number; a little + uncountable noun (a little milk, a little Spanish)
= a small amount. The point had 4 check tasks (2 choice, 2 word order) and no use task, so 4 of the 6 are typed."""
from lib import gp, od, mc, tx
T = "Quantity"
L = "A2.1"

FEW = ("*a few* + plural noun = a small number: *a few minutes, a few times.* *a little* goes with uncountable nouns: *a little milk.*",
       "*a few* lieto ar daudzskaitļa lietvārdiem: *a few minutes, a few times.* *a little* lieto ar neskaitāmiem lietvārdiem: *a little milk.*")
LITTLE = ("*a little* + uncountable noun = a small amount: *a little milk, a little salt.* *a few* goes with plural nouns: *a few eggs.*",
          "*a little* lieto ar neskaitāmiem lietvārdiem: *a little milk, a little salt.* *a few* lieto ar daudzskaitļa lietvārdiem: *a few eggs.*")
BOTH = ("*a few* + plural noun (*a few words, a few shops*), *a little* + uncountable noun (*a little Spanish*): both mean a small number or amount.",
        "*a few* lieto ar daudzskaitļa lietvārdiem (*a few words, a few shops*), *a little* ar neskaitāmiem lietvārdiem (*a little Spanish*).")

# choice (1)
mc(T, L, 2, "Which sentence has a mistake?", "I put a few salt in the soup.",
   ["I speak a little German.", "There are a few museums in our town.", "How much water do you drink every day?"],
   "*salt* is uncountable, so *a little salt*, not *a few salt*. *a few* goes with plural nouns: *a few museums*.",
   "*salt* ir neskaitāms lietvārds, tāpēc *a little salt*, nevis *a few salt*. *a few* lieto ar daudzskaitļa lietvārdiem: *a few museums*.")
# word bank (1)
gp(T, L, 3, "Can you wait ___ minutes, please?", "a few", *FEW, bank=["a few", "a little", "much"])
# typed gap (2)
gp(T, L, 3, "Write *a few* or *a little*: I go to the gym ___ times a week.", "a few", *FEW)
gp(T, L, 3, "Write *a few* or *a little*: Can I have ___ milk in my tea?", "a little", *LITTLE)
# whole sentence (2)
tx(T, L, 4, "Say it another way with *a few* or *a little*: I speak some Spanish, but not much.",
   "I speak a little Spanish. | I can speak a little Spanish. | I know a little Spanish. | I speak a little Spanish, but not much. | "
   "I speak a few words of Spanish. | I know a few words of Spanish. | I can speak a few words of Spanish. | "
   "I speak a little bit of Spanish. | I can speak a little bit of Spanish. | I only speak a little Spanish. | I can only speak a little Spanish.", *BOTH)
tx(T, L, 4, "Say it another way with *a few* or *a little*: There are three or four cafés near my office.",
   "There are a few cafés near my office. | Near my office there are a few cafés. | There are a few cafes near my office. | Near my office there are a few cafes.", *BOTH)
