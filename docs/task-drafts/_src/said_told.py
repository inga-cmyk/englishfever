"""said or told (draft section G, teacher, 11-12 November): the learner types the word; the tense change is already given.
Role use: evidence for Reported statements."""
from lib import rows, save

T = "Reported statements (tense changes)"
EN = "*tell* needs a person right after it: *told me, told us*. *say* does not: *said (that)…*, or *said to me*."
LV = "Pēc *tell* uzreiz nāk persona: *told me, told us*. Pēc *say* persona nenāk: *said (that)…* vai *said to me*. Tulkojot burtiski no \"teica man\", rodas *said me*."
for lv, q, a in [
    ("B1.1", "Complete with *said* or *told*: Anna ___ me she was moving to Tallinn.", "told"),
    ("B1.1", "Complete with *said* or *told*: My neighbour ___ the parcel had arrived.", "said"),
    ("B1.1", "Complete with *said* or *told*: The doctor ___ that I needed more sleep.", "said"),
    ("B1.2", "Complete with *said* or *told*: Our manager ___ us the office would close at four.", "told"),
    ("B1.2", "Complete with *said* or *told*: The driver ___ to us that the road was closed.", "said"),
    ("B1.2", "Complete with *said* or *told*: Nobody ___ me that the meeting had been moved.", "told"),
]:
    rows.append([T, lv, "gap", q, a, "", EN, LV, 3])
save("said-told-1.csv")
