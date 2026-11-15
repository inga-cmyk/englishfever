"""Batch 5, point link_time (A2.2): 3 tasks to reach 10 counted tasks. Not a Murphy EGiU unit (map); before / after + clause checked against Murphy 25, before / after + -ing against Murphy 60."""
from lib import gp, od, mc, tx
T = "However, although, because of, then"
L = "A2.2"

# The point already has 3 check (2 choices, 1 word order) and 4 use (2 typed gaps, 2 corrections), and no word bank:
# 2 word banks + 1 "Which sentence has a mistake?".

# word bank (1): after + subject + verb joins two actions in one sentence; Then / After that start a new sentence, so
# "Then we had dinner, we went …" and "After that we had dinner, we went …" are two sentences joined by a comma. No "Before"
# or "When" chip: both would be correct English here.
gp(T, L, 3, "___ we had dinner, we went for a walk by the sea.", "After",
   "*after* + subject + verb joins two actions in one sentence: *After we had dinner, we went for a walk.* *Then* and *after that* start a new sentence: *We had dinner. Then we went for a walk.*",
   "*after* + teik. priekšmets + darbības vārds savieno abas darbības vienā teikumā: *After we had dinner, we went for a walk.* *Then* un *after that* sāk jaunu teikumu: *We had dinner. Then we went for a walk.*",
   bank=["After", "Then", "After that"])
# word bank (2): only before can stand before a noun here; while and when need subject + verb (while the film is on,
# when the film starts). No "after" chip: "after the film" is correct English too.
gp(T, L, 3, "We always buy popcorn ___ the film.", "before",
   "*before* (and *after*) can come before a noun: *before the film*. *while* and *when* need subject + verb: *while the film is on*, *when the film starts*.",
   "*before* (un *after*) var likt pirms lietvārda: *before the film*. Aiz *while* un *when* vajag teik. priekšmetu + darbības vārdu: *while the film is on*, *when the film starts*.",
   bank=["before", "while", "when"])
# choice (1): the map's typical error "Before go to bed"; the other three are correct and about three different things
mc(T, L, 2, "Which sentence has a mistake?", "Before go to work, I walk the dog.",
   ["We had lunch. After that, we visited the old town.", "Someone called me while I was at the gym.", "When I got home, I made some soup."],
   "*before* + subject + verb (*Before I go to work*) or *before* + -ing (*Before going to work*), not *before* + the bare verb.",
   "*before* + teik. priekšmets + darbības vārds (*Before I go to work*) vai *before* + *-ing* (*Before going to work*), nevis *before go*.")
