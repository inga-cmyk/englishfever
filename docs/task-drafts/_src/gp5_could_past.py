"""Batch 5, point could_past (A2.2): 7 tasks to reach 10 counted tasks. Murphy unit 26."""
from lib import gp, od, mc, tx
T = "Modal verbs"
L = "A2.2"

C_EN = "Ability in the past: *could* + base verb (no *to*, no past form): *I could read at four.*"
C_LV = "Spēja pagātnē: *could* + darbības vārda pamatforma (bez *to*, bez pagātnes formas): *I could read at four.*"
NEG = ("Past: *couldn't* + base verb. *can't* is the present, and *could* never goes with *did / didn't*.",
       "Pagātnē: *couldn't* + pamatforma. *can't* ir tagadne, un *could* nekad nelieto ar *did / didn't*.")
Q = ("Question about the past: *Could* + subject + base verb? No *did*: *Could you swim at six?*",
     "Jautājums par pagātni: *Could* + teik. priekšmets + pamatforma? Bez *did*: *Could you swim at six?*")

# choose (2)
mc(T, L, 2, "Choose the correct option: It was very hot, so I ___ sleep last night.", "couldn't", ["can't", "didn't could", "couldn't to"], *NEG)
# Murphy 26: couldn't for a general and for a particular situation
mc(T, L, 2, "Which sentence has a mistake?", "When I was ten, I can speak French.",
   ["We couldn't find a taxi at the airport.", "My first phone could only make calls.", "Could you cook when you were a student?"],
   "*When I was ten* is the past: *I could speak French*, not *I can*.", "*When I was ten* ir pagātne: *I could speak French*, nevis *I can*.")
# word order (2)
od(T, L, 3, "Put the words in order.", "we couldn't see the stage from our seats", *NEG, also=["from our seats we couldn't see the stage"])
od(T, L, 3, "Put the words in order.", "when i was younger i could run much faster", C_EN, C_LV, also=["i could run much faster when i was younger"])
# word bank (2): can is a real form that is wrong in the past, the past form is the typical mistake after could
gp(T, L, 3, "___ your parents ___ a car when they were young?", "Could / drive", *Q, bank=["Could", "drive", "Can", "drove"])
gp(T, L, 3, "As a teenager, Ben ___ ___ any song on the guitar.", "could / play", C_EN, C_LV, bank=["could", "play", "can", "played"])
# whole sentence (1)
tx(T, L, 4, "Make a yes/no question: Tom could speak German when he lived in Berlin.",
   "Could Tom speak German when he lived in Berlin? | When he lived in Berlin, could Tom speak German? | Was Tom able to speak German when he lived in Berlin? | When he lived in Berlin, was Tom able to speak German?", *Q)
