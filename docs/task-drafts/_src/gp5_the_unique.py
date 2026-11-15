"""Batch 5, point the_unique (A2.2): 2 tasks to reach 10 counted tasks. Murphy unit 73."""
from lib import gp, od, mc, tx
T = "Articles"
L = "A2.2"

# ── typed gap (1): "same" always takes "the" (Murphy 73 A: the same); "a same" is the typical mistake, and "this / our"
#    are ruled out because the instruction names the three words
gp(T, L, 3, "Complete with *a*, *an* or *the*: We always sit at ___ same table in this café.", "the",
   "*same* always has *the* before it: *the same table, the same day*.",
   "Pirms *same* vienmēr lieto *the*: *the same table, the same day*.")

# ── whole sentence (1): the superlative needs "the" (Murphy 73 C); "Maria's" is listed because the checker cannot work out 's
tx(T, L, 4, "Correct the mistake: Maria is best driver in our family.",
   "Maria is the best driver in our family. | Maria's the best driver in our family.",
   "Before a superlative (*best, biggest, most expensive*) we use *the*: *the best driver*.",
   "Pirms vispārākās pakāpes formas (*best, biggest, most expensive*) lieto *the*: *the best driver*.")
