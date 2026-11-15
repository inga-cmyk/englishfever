"""Batch 5, point prep_none (A2.1): 5 tasks to reach 10 counted tasks. Murphy unit 121."""
from lib import gp, od, mc, tx
T = "Prepositions of time and place (in, on, at)"
L = "A2.1"

# Murphy 121 C (and 121 D): no at / on / in before last / next / this / every and before tomorrow / yesterday

# choice (2)
# has a mistake: the three correct sentences are about three different things (clock time, month, date)
mc(T, L, 2, "Which sentence has a mistake?", "I started a new job on last Monday.",
   ["The shop opens at nine.", "We often go skiing in February.", "My birthday is on 3 June."],
   "No preposition before *last / next / this / every*: *I started a new job last Monday.* But *on Monday* without *last*.",
   "Pirms *last / next / this / every* prievārdu nelieto: *I started a new job last Monday.* Bet *on Monday* bez *last*.")
# "at the weekend" is the competing form
mc(T, L, 2, "Choose the correct option: Are you free ___ this weekend?", "—", ["at", "on", "in"],
   "With *this* there is no preposition: *this weekend*. Without *this* we say *at the weekend*.",
   "Ar *this* prievārdu nelieto: *this weekend*. Bez *this* saka *at the weekend*.")

# word bank (2): the wrong chip is the preposition the noun takes without every / tomorrow
gp(T, L, 3, "I check my email ___ every morning.", "—",
   "With *every* there is no preposition: *every morning*. Without *every* we say *in the morning*.",
   "Ar *every* prievārdu nelieto: *every morning*. Bez *every* saka *in the morning*.", bank=["—", "in"])
gp(T, L, 3, "The new gym opens ___ tomorrow.", "—",
   "No preposition before *tomorrow* and *yesterday*: *The gym opens tomorrow.*",
   "Pirms *tomorrow* un *yesterday* prievārdu nelieto: *The gym opens tomorrow.*", bank=["—", "on", "in"])

# whole sentence (1)
tx(T, L, 4, "Correct the mistake: We arrived in Rome on yesterday.", "We arrived in Rome yesterday. | Yesterday we arrived in Rome.",
   "No preposition before *yesterday* and *tomorrow*: *We arrived in Rome yesterday.*",
   "Pirms *yesterday* un *tomorrow* prievārdu nelieto: *We arrived in Rome yesterday.*")
