"""Batch 5, point cmp_adv (A2.2): 8 tasks to reach 10 counted tasks. Murphy unit 105 (comparative adverbs: more slowly,
more carefully; harder, faster, earlier, better, worse, further) and unit 108 (the + superlative; with an adverb the is often
left out: who works hardest). The point had 2 check tasks and no use task, so 4 of the 8 are typed (3 gaps, 1 whole sentence)."""
from lib import gp, od, mc, tx
T = "Comparison: -er, more, the most, as ... as"
L = "A2.2"

LY = ("An adverb with *-ly* takes *more*: *slowly → more slowly*, *carefully → more carefully*. Not *slowlier*, and not *more* + *-er* together.",
      "Apstākļa vārds ar *-ly* veido pārāko pakāpi ar *more*: *slowly → more slowly*, *carefully → more carefully*. Nevis *slowlier* un nevis *more* kopā ar *-er*.")
SHORT = ("*fast, hard, early, late* are adverbs without *-ly*: they take *-er* like short adjectives (*faster, harder, earlier, later*). Not *more fast*.",
         "*fast, hard, early, late* ir apstākļa vārdi bez *-ly*: tie veido pārāko pakāpi ar *-er* kā īsie īpašības vārdi (*faster, harder, earlier, later*). Nevis *more fast*.")
WELL = ("*well* and *badly* are irregular: *well → better → the best*, *badly → worse → the worst*. Not *more well* or *more good*.",
        "*well* un *badly* ir nekārtni: *well → better → the best*, *badly → worse → the worst*. Nevis *more well* vai *more good*.")

# ---------- choice (2) ----------
mc(T, L, 2, "Choose the correct option: Please drive ___. The road is icy.", "more slowly",
   ["slowlier", "more slowlier", "the most slowly"],
   "*slowly* has *-ly*, so the comparative is *more slowly* (*slower* is also heard in everyday speech). Not *slowlier* or *more slowlier*; *the most slowly* compares with a whole group.",
   "*slowly* beidzas ar *-ly*, tāpēc pārākā pakāpe ir *more slowly* (sarunvalodā dzird arī *slower*). Nevis *slowlier* vai *more slowlier*; *the most slowly* salīdzina ar visu grupu.")
mc(T, L, 2, "Which sentence has a mistake?", "Tom drives more fast than his father.",
   ["We arrived later than the others.", "My new phone charges much faster.", "Who sings the best in your family?"],
   "*fast* has no *-ly*: the comparative is *faster*, not *more fast*: *Tom drives faster than his father.* The other three are correct: *later than*, *much faster*, *the best*.",
   "*fast* nav *-ly* galotnes: pārākā pakāpe ir *faster*, nevis *more fast*: *Tom drives faster than his father.* Pārējie trīs teikumi ir pareizi: *later than*, *much faster*, *the best*.")

# ---------- word order (1) ----------
od(T, L, 3, "Put the words in order.", "my sister speaks english more fluently than me",
   "The adverb comes after the verb and its object: *speaks English more fluently*, then *than* + the other person (*than me*). Not *speaks more fluently English*.",
   "Apstākļa vārds nāk aiz darbības vārda un tā papildinātāja: *speaks English more fluently*, tad *than* + otrs cilvēks (*than me*). Nevis *speaks more fluently English*. "
   "Tulkojot burtiski \"runā brīvāk angliski\", sanāk *speaks more fluently English*.")

# ---------- word bank (1) ----------
gp(T, L, 3, "She plays the guitar ___ than her brother.", "better", *WELL, bank=["better", "more well", "best"])

# ---------- typed gap (3) ----------
gp(T, L, 3, "Marta has never had an accident. She drives ___ than her brother. (careful)",
   "more carefully | much more carefully | a lot more carefully | far more carefully",
   "*drive* needs an adverb: *careful → carefully*, and with *-ly* the comparative is *more carefully*. Not *more careful* (that is the adjective).",
   "Aiz *drive* vajag apstākļa vārdu: *careful → carefully*, un ar *-ly* pārākā pakāpe ir *more carefully*. Nevis *more careful* (tas ir īpašības vārds).")
gp(T, L, 3, "Today I started work ___ than usual. (early)",
   "earlier | much earlier | a bit earlier | a lot earlier",
   "*early* is an adverb and an adjective: *early → earlier* (*y → i* + *-er*). Not *more early*.",
   "*early* ir apstākļa vārds un arī īpašības vārds: *early → earlier* (*y → i* + *-er*). Nevis *more early*.")
gp(T, L, 3, "Of all my colleagues, Anna lives ___ from the office. (far)",
   "the furthest | the farthest | furthest | farthest",
   "*Of all* compares one person with the whole group: superlative. *far* is irregular: *far → further → the furthest* (*farther, the farthest* are correct too). With an adverb, *the* is often left out.",
   "*Of all* salīdzina vienu cilvēku ar visu grupu: vispārākā pakāpe. *far* ir nekārtns: *far → further → the furthest* (der arī *farther, the farthest*). Ar apstākļa vārdu *the* bieži izlaiž.")

# ---------- whole sentence (1) ----------
tx(T, L, 4, "Start with *My brother*: I cook worse than my brother.",
   "My brother cooks better than me. | My brother cooks better than I do. | My brother cooks better than I. | My brother cooks better than I cook. | My brother cooks much better than me. | My brother cooks much better than I do. | My brother cooks a lot better than me. | My brother cooks a lot better than I do. | My brother is a better cook than me. | My brother is a better cook than I am. | My brother is a better cook than I.",
   *WELL)
