"""Batch 5, point dep_none (A2.2): 1 task to reach 10 counted tasks. Murphy unit 132.
discuss, call, answer, join, enter take the object directly, with no preposition (discuss the plan, not discuss about the plan).
The point had 6 check tasks (choices and one bank) and 3 use tasks (all Correct the mistake), so the one new task is a whole
sentence the learner writes: talk about -> discuss, where about must go."""
from lib import gp, od, mc, tx
T = "Prepositions after words (listen to, good at)"
L = "A2.2"

# whole sentence (1)
tx(T, L, 4, "Say it another way with *discuss*: We talked about the new timetable at the meeting.",
   "We discussed the new timetable at the meeting. | We discussed the new timetable in the meeting.",
   "*talk about* has a preposition, but *discuss* takes its object directly: *We discussed the new timetable*, not *discussed about*.",
   "*talk about* ir ar prievārdu, bet aiz *discuss* papildinātājs seko uzreiz: *We discussed the new timetable*, nevis *discussed about*.")
