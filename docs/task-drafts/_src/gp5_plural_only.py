"""Batch 5, point plural_only (A2.2): 4 tasks to reach 10 counted tasks. Murphy unit 79 (nouns that are always plural:
jeans, trousers, glasses, scissors take a plural verb; a pair of jeans / scissors to count them).
The six tasks the point has are all about *the police*; these four use the two-part nouns on the card (jeans, trousers,
glasses, scissors) and one uses *a pair of* (card line requested in the notes)."""
from lib import gp, od, mc, tx
T = "Irregular plurals (children, people, men, teeth)"
L = "A2.2"

VERB = ("*jeans, trousers, glasses, scissors* are always plural (they have two parts), so the verb is plural: *are*, *have*, verb without *-s*.",
        "*jeans, trousers, glasses, scissors* vienmēr ir daudzskaitlī (tiem ir divas daļas), tāpēc darbības vārds ir daudzskaitlī: *are*, *have*, darbības vārds bez *-s*.")

# 1 choice (check), travel: the mistake is a singular verb after glasses. The three correct sentences are about three
# other things: a correct always-plural noun (scissors, kitchen), an irregular plural (feet, lifestyle), people (travel),
# so the learner cannot pick the odd one out just by spotting a two-part noun.
mc(T, L, 2, "Which sentence has a mistake?", "My glasses is in the car.",
   ["These kitchen scissors are very sharp.", "My feet hurt after the long walk.", "People in this town are very friendly."],
   "*glasses* (for your eyes) is always plural: *My glasses are in the car.* *scissors* too: *are*. *feet* and *people* are plural: *hurt*, *are*.",
   "*glasses* vienmēr ir daudzskaitlī: *My glasses are in the car.* Arī *scissors*: *are*. *feet* un *people* ir daudzskaitlī: *hurt*, *are*.")

# 2 word bank (check), work: to count a two-part noun, a pair of + the plural noun. a scissors / a scissor / a pair of scissor
# are the learner mistakes; no chip pair other than a pair of + scissors gives a correct phrase.
gp(T, L, 3, "Can I borrow ___ ___ for a minute?", "a pair of / scissors",
   "*scissors* is always plural: no *a scissors*, no *a scissor*. To say one, use *a pair of scissors*.",
   "*scissors* vienmēr ir daudzskaitlī: nav *a scissors*, nav *a scissor*. Par vienām šķērēm saka *a pair of scissors*. "
   "Tulkojot burtiski, *vienas šķēres* dod *a scissors*.",
   bank=["a pair of", "a", "scissors", "scissor"])

# 3 typed gap (use), lifestyle / health: now fixes the time, so only are fits (were is ruled out by now)
gp(T, L, 3, "My jeans ___ too big for me now. (be)", "are", *VERB)

# 4 whole sentence (use), clothes: the verb after trousers has no -s (blind check r13: the old "Start with These trousers:
# This shirt is too expensive." only swapped the noun, so it was not a rewrite)
tx(T, L, 4, "Correct the mistake: Your trousers looks great with that jacket.", "Your trousers look great with that jacket.",
   "*trousers* is always plural, so the verb has no *-s*: *Your trousers look great*, not *looks*.",
   "*trousers* vienmēr ir daudzskaitlī, tāpēc darbības vārds ir bez *-s*: *Your trousers look great*, nevis *looks*.")
