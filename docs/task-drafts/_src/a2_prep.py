"""Prepositions of time and place: in, on, at (teacher, 28 October: the most frequent A2 mistake that had no topic yet).
Murphy, English Grammar in Use (at / on / in for time and for place). Only sentences with one natural answer: no "at / on the weekend"
(British / American), no "in / at the park", no "in / on the bus", no "works in / at a bank". Where no preposition is right, one option
is "—". A Latvian comparison only where Latvian leads to the mistake (piektdienas vakarā, pie sienas); otherwise a short rule."""
from lib import *
NONE = "—"

def ex(en, lv): return (en, lv)
AT = ex("*at* + a clock time: *at 9 o'clock*.", "*at* + pulksteņa laiks: *at 9 o'clock*.")
ON = ex("*on* + a day or a date: *on Monday, on 5 May*.", "*on* + diena vai datums: *on Monday, on 5 May*.")
IN = ex("*in* + a month, year, season or part of the day: *in May, in 1995, in the evening*.", "*in* + mēnesis, gads, gadalaiks vai dienas daļa: *in May, in 1995, in the evening*.")
NIGHT = ex("*at night*, but *in the morning, in the evening*.", "*at night*, bet *in the morning, in the evening*.")
DAYPART = ex("A day + part of the day: *on*: *on Friday evening, on Sunday mornings*.", "Latviski *piektdienas vakarā*, bet angliski ar dienu lieto *on*: *on Friday evening*.")
NO = ex("No preposition before *tomorrow, yesterday* and *next / last / this / every* + time: *see you tomorrow, last Friday*.",
        "Bez prievārda pirms *tomorrow, yesterday* un *next / last / this / every* + laiks: *see you tomorrow, last Friday*.")
P_ON = ex("*on* + a surface: *on the wall, on the table, on the third floor*.", "Latviski *pie sienas*, bet angliski *on the wall*: *on* = uz virsmas (*on the table, on the third floor*).")
P_IN = ex("*in* = inside or in an area: *in the fridge, in my bag, in London*.", "*in* = iekšā vai teritorijā: *in the fridge, in my bag, in London*.")
P_AT = ex("*at* + a point or a place where you do something: *at work, at home, at school, at the bus stop*.", "*at* + punkts vai vieta, kur kaut ko dara: *at work, at home, at school, at the bus stop*.")

T = Topic("Prepositions of time and place (in, on, at)", mcq_b=2, text_b=3, err="PREP-TP",
          mcq=IN, bank=IN, gap=IN, text=IN, order=IN, match=IN)

# ── choose ──
T.mcq("A2.1", "Choose the correct option: I have English ___ Monday.", "on", ["in", "at"], ON, b=1)
T.mcq("A2.1", "Choose the correct option: The lesson starts ___ 9 o'clock.", "at", ["in", "on"], AT, b=1)
T.mcq("A2.1", "Choose the correct option: My birthday is ___ May.", "in", ["on", "at"], IN, b=1)
T.mcq("A2.1", "Choose the correct option: I was born ___ 1995.", "in", ["on", "at"], IN)
T.mcq("A2.1", "Choose the correct option: We have dinner ___ the evening.", "in", ["at", "on"], NIGHT)
T.mcq("A2.2", "Choose the correct option: I often can't sleep ___ night.", "at", ["in", "on"], NIGHT)
T.mcq("A2.2", "Choose the correct option: The shop is closed ___ Sunday mornings.", "on", ["in", "at"], DAYPART)
T.mcq("A2.2", "Choose the correct option: I'll call you ___ tomorrow.", NONE, ["on", "in", "at"], NO)
T.mcq("A2.2", "Choose the correct option: We met ___ last Friday.", NONE, ["on", "in", "at"], NO)
T.mcq("A2.1", "Choose the correct option: There's a picture ___ the wall.", "on", ["in", NONE], P_ON, b=1)
T.mcq("A2.1", "Choose the correct option: My mum is ___ work now.", "at", ["in", "on"], P_AT, b=1)
T.mcq("A2.1", "Choose the correct option: The milk is ___ the fridge.", "in", ["on", "at"], P_IN)
T.mcq("A2.2", "Choose the correct option: We live ___ the third floor.", "on", ["in", "at"], P_ON)
T.mcq("A2.2", "Choose the correct option: She's waiting ___ the bus stop.", "at", ["in", "on"], P_AT)
T.mcq("A2.2", "Choose the correct option: My keys are ___ my bag.", "in", ["on", "at"], P_IN)

# ── word bank (two gaps) ──
T.bank("A2.1", "The film starts ___ 8 o'clock ___ Friday.", ["at", "on"], ["in"], ex("*at* + a clock time, *on* + a day: *at 8 o'clock on Friday*.", "*at* + pulksteņa laiks, *on* + diena: *at 8 o'clock on Friday*."))
T.bank("A2.2", "I get up early ___ the morning, but ___ Saturdays I sleep late.", ["in", "on"], ["at"], ex("*in the morning*, but *on* + a day: *on Saturdays*.", "*in the morning*, bet ar dienu *on*: *on Saturdays*."))
T.bank("A2.2", "My brother lives ___ London, and his flat is ___ the fifth floor.", ["in", "on"], ["at"], ex("*in* + a city, *on* + a floor: *in London, on the fifth floor*.", "*in* + pilsēta, *on* + stāvs: *in London, on the fifth floor*."))
T.bank("A2.1", "Put the cups ___ the table and the milk ___ the fridge.", ["on", "in"], ["at"], ex("*on* + a surface, *in* = inside: *on the table, in the fridge*.", "*on* = uz virsmas, *in* = iekšā: *on the table, in the fridge*."))

# ── type the word (no clue) ──
T.gap("A2.1", "We always have a holiday ___ July.", "in", IN)
T.gap("A2.2", "The meeting is ___ 10 March.", "on", ON)
T.gap("A2.2", "I'm not ___ home now. I'm ___ school.", "at / at", P_AT)
T.gap("A2.1", "Anna is cooking ___ the kitchen.", "in", P_IN)
T.gap("A2.2", "Our office is ___ the second floor.", "on", P_ON)
T.gap("A2.2", "The concert starts ___ half past seven.", "at", AT)

# ── word order ──
T.order("A2.1", "we have lunch at one o'clock", why=AT)
T.order("A2.2", "my sister lives in a small flat in Riga", why=P_IN)

# ── correct the mistake (whole sentence) ──
T.text("A2.1", "Correct the mistake: I'll see you in Friday evening.", "I'll see you on Friday evening.", DAYPART)
T.text("A2.1", "Correct the mistake: My birthday is in 5 May.", ["My birthday is on 5 May.", "My birthday is on May 5.", "My birthday is on the 5th of May."], ON)
T.text("A2.2", "Correct the mistake: I always drink coffee at the morning.", ["I always drink coffee in the morning.", "In the morning I always drink coffee."], NIGHT)
T.text("A2.2", "Correct the mistake: See you on next Monday!", "See you next Monday!", NO)
T.text("A2.2", "Correct the mistake: She is in work now.", "She is at work now.", P_AT)
T.text("A2.2", "Correct the mistake: There is a clock in the wall.", "There is a clock on the wall.", P_ON)

save("a2-prepositions-1.csv")
