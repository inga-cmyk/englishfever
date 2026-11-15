"""Batch 5, point count_unc (A2.1): 2 tasks to reach 10 counted tasks. Murphy unit 69 (countable and uncountable 1: a / an
with a singular countable noun, never with an uncountable one), 71 (a / an and some) and 85 (some and any)."""
from lib import gp, od, mc, tx
T = "Quantity"
L = "A2.1"

# typed gap (use): the point has no typed gap and no task on a / an against some. umbrella = one thing, starts with a vowel
# sound (an); money = uncountable (some, never a money). The instruction names the three words, so any / much do not arise.
gp(T, L, 3, "Write *a*, *an* or *some*: I need ___ umbrella and ___ money.", "an / some",
   "*umbrella* is one thing we can count, so *an* (it starts with a vowel sound). *money* is uncountable: *some money*, never *a money*.",
   "*umbrella* ir skaitāms lietvārds, tāpēc *an* (sākas ar patskaņa skaņu). *money* ir neskaitāms lietvārds: *some money*, nekad *a money*.")

# choice (check): the mistake is some in a negative; the three correct sentences are about three different things:
# a / an + some in a positive sentence (food), any in a question (travel), some + plural in a positive sentence (work)
mc(T, L, 2, "Which sentence has a mistake?", "I don't have some free time this week.",
   ["I'd like a sandwich and some water.", "Are there any shops near your hotel?", "Our office has some new computers."],
   "In a negative sentence we use *any*, not *some*: *I don't have any free time this week.* *some* is for positive sentences, *any* for negatives and questions.",
   "Noliegumā lieto *any*, nevis *some*: *I don't have any free time this week.* *some* lieto apgalvojumā, *any* noliegumā un jautājumā.")
