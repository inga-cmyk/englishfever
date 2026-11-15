"""Batch 5, point pas_by (A2.2): 5 tasks to reach 10 counted tasks. Murphy unit 42."""
from lib import gp, od, mc, tx
T = "Present simple passive"
T2 = "Past simple passive"
L = "A2.2"

BY = ("*by* + the doer tells us who does the action: *The hotel is owned by a Swedish company.* Not *from* or *of*.",
      "*by* + darītājs norāda, kurš izdarīja darbību: *The hotel is owned by a Swedish company.* Nevis *from* vai *of*.")

# Murphy 42: who did it = by; "made from" is for the material (made from wood), so "from my uncle" is the believable mistake.
# The three correct sentences: no doer (times), no doer (born), by + doer that matters.
mc(T2, L, 2, "Which sentence has a mistake?", "Our kitchen chairs were made from my uncle.",
   ["Breakfast is served from seven to ten.", "My grandmother was born in a small town.", "The museum is visited by thousands of tourists."],
   "The person who did it comes after *by*: *made by my uncle*. *made from* is for the material: *made from wood*.",
   "Cilvēks, kas to izdarīja, nāk aiz *by*: *made by my uncle*. *made from* lieto materiālam: *made from wood*.")
# "owned for / with" are not English, so only "by" fits the open gap
gp(T, L, 3, "Complete with one word: Our hotel is owned ___ a Swedish company.", "by", *BY)
# chips: from (material: baked from flour), of (Latvian genitive: vietējās ģimenes cepta)
gp(T, L, 3, "In our village, the bread is baked ___ a local family.", "by",
   "Who bakes it? A local family, so *by a local family*. *from* is for what it is made of: *baked from rye flour*.",
   "Darītājs ir vietējā ģimene, tāpēc *by a local family*. *from* lieto materiālam: *baked from rye flour*.",
   bank=["by", "from", "of"])
# every month = present; are (plural windows) + 3rd form, then by + the doer
gp(T, L, 3, "The windows of our office ___ ___ a small company every month. (clean)", "are cleaned | get cleaned / by",
   "*every month* = Present Simple; *the windows* = plural, so *are cleaned*. The doer comes after *by*: *by a small company*.",
   "*every month* = Present Simple; *the windows* ir daudzskaitlis, tāpēc *are cleaned*. Darītājs nāk aiz *by*: *by a small company*.")
# the doer is new information, so it stays, after by
tx(T2, L, 4, "Start with *This bridge*: A Latvian engineer designed this bridge.",
   "This bridge was designed by a Latvian engineer.",
   "*This bridge* first, then *was* + 3rd form; the engineer is important here, so *by a Latvian engineer* stays: *This bridge was designed by a Latvian engineer.*",
   "Sākumā *This bridge*, tad *was* + 3. forma; inženieris šeit ir svarīgs, tāpēc *by a Latvian engineer* paliek: *This bridge was designed by a Latvian engineer.*")
