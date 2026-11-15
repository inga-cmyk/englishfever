"""Batch 5, point will_going (A2.2): 2 tasks to reach 10 counted tasks. Murphy unit 23.
will for a decision made at the moment of speaking (Oh, I forgot. I'll call her now); going to for something decided
before (Why are you filling that bucket? I'm going to wash the car). The point had 6 check tasks and 2 use tasks, both at
B1.2; it had no typed task at A2.2, so both new tasks are typed gaps (use), one for each side of the contrast.
The instruction names both forms (*will* or *going to*): choosing between them is the task, and naming them keeps
can / must / want to / the present continuous out of the gap."""
from lib import gp, od, mc, tx
T = "Future: will, going to, present continuous"
L = "A2.2"

# typed gap (2)
gp(T, L, 3, "Complete with *will* or *going to*: 'Did you reply to Mark's email?' 'Oh no, I forgot! I ___ to him now.' (write)",
   "'ll write | will write",
   "The speaker decides now, at the moment of speaking (*Oh no, I forgot!*), so *will* + base verb: *I'll write to him now.* *going to* is for something decided before.",
   "Runātājs pieņem lēmumu tagad, runāšanas brīdī (*I forgot!*), tāpēc *will* + pamatforma: *I'll write to him now.* *going to* lieto, ja lēmums pieņemts jau iepriekš.")
gp(T, L, 3, "Complete with *will* or *going to*: 'Why are you saving so much money?' 'I ___ a flat next year.' (buy)",
   "'m going to buy | am going to buy",
   "The decision was made before (that is why the speaker is saving), so *going to*: *I'm going to buy a flat next year.* *will* is for a decision made at the moment of speaking.",
   "Lēmums pieņemts jau iepriekš (tāpēc runātājs jau krāj), tāpēc *going to*: *I'm going to buy a flat next year.* *will* lieto lēmumam, ko pieņem runāšanas brīdī.")
