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

# Top-up, 16 November (2 more counted tasks; the topic needs 12 at A2.1)
# typed gap (use): a + one countable thing (toaster), any + uncountable in a negative (bread; a bread is the map's error).
# The instruction names the three words, so no / much do not arise; some fits neither gap.
gp(T, L, 3, "Write *a*, *some* or *any*: There's ___ toaster, but there isn't ___ bread.", "a / any",
   "*toaster* is one thing we can count: *a toaster*. *bread* is uncountable, and in a negative sentence we use *any*: *there isn't any bread*, never *a bread*.",
   "*toaster* ir skaitāms lietvārds: *a toaster*. *bread* ir neskaitāms lietvārds, un noliegumā lieto *any*: *there isn't any bread*, nekad *a bread*.")
# whole sentence (use): some in the statement becomes any in a plain question for information (Murphy 85).
tx(T, L, 4, "Make a yes/no question: There are some yoga classes on Sunday.", "Are there any yoga classes on Sunday? | Are there any yoga classes on Sundays? | Are there yoga classes on Sunday? | Are there yoga classes on Sundays? | Are there some yoga classes on Sunday? | Are there some yoga classes on Sundays?",   # blind check r14: the other correct questions accepted, *some* with its own note (gap_fill_a2.py)
   "In a question we usually use *any*, not *some*: *Are there any yoga classes on Sunday?* *some* is for positive sentences.",
   "Jautājumā parasti lieto *any*, nevis *some*: *Are there any yoga classes on Sunday?* *some* lieto apgalvojumā.")
