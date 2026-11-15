"""Batch 5, point a_the (A2.1): 5 tasks to reach 10 counted tasks. Murphy unit 72."""
from lib import gp, od, mc, tx
T = "Articles"
L = "A2.1"

AGAIN = ("*a / an* the first time we talk about something; *the* the second time, when we both know which one.",
         "*a / an* lieto, kad par kaut ko runā pirmajā reizē; *the* lieto otrajā reizē, kad abi jau zinām, kurš tas ir.")

# ── choice (1): the mistake is "a" at the second mention; the three correct sentences are a job (an), a general
#    uncountable noun (no article) and the only one (the sun), so each is about a different thing
mc(T, L, 2, "Which sentence has a mistake?", "I ordered a pizza. A pizza was cold.",
   ["My aunt is an engineer in Riga.", "I never drink coffee after six.", "The sun is very strong today."],
   "The second time we talk about the pizza, both people know which one: *I ordered a pizza. The pizza was cold.*",
   "Otrajā reizē abi zinām, kurš ēdiens domāts: *I ordered a pizza. The pizza was cold.*")

# ── word bank (1): "There was ___" allows only a / an, so "the" cannot go in the first gap; "A" in the second gap is the
#    mistake of this point. Combinations: a + The (right), a + A, the + The, the + A (all wrong).
gp(T, L, 3, "There was ___ wallet on my seat on the bus. ___ wallet was empty.", "a / The", *AGAIN,
   bank=["a", "The", "A", "the"])

# ── typed gap (2): the instruction names the three words, so "her" or "this" is not a second answer
gp(T, L, 3, "Complete with *a*, *an* or *the*: My sister has ___ new job. ___ job is in Riga.", "a / The", *AGAIN)
gp(T, L, 3, "Complete with *a*, *an* or *the*: We rented ___ car in Spain. ___ car was very small.", "a / The", *AGAIN)

# ── whole sentence (1): replacing "A laptop" with "It" is also a correction of the same mistake
tx(T, L, 4, "Correct the mistake: I bought a new laptop. A laptop is very fast.",
   "I bought a new laptop. The laptop is very fast. | I bought a new laptop. It is very fast. | I bought a new laptop. It's very fast.",
   "We already know which laptop (the new one), so the second time it is *the laptop* (or *it*).",
   "Mēs jau zinām, kurš klēpjdators domāts, tāpēc otrajā reizē ir *the laptop* (vai *it*).")
