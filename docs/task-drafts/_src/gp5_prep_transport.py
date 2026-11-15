"""Batch 5, point prep_transport (A2.2): 7 tasks to reach 10 counted tasks. Murphy unit 128 (by car / by bus, no article; in my car; on foot), with unit 127 / the in-on-at units for in a car or taxi, on a bus, train, tram or plane."""
from lib import gp, od, mc, tx
T = "Prepositions of time and place (in, on, at)"
L = "A2.2"

BY = ("*by* + a kind of transport, with no *a / the / my*: *by bus, by car, by train*. Not *with bus*.",
      "*by* + transportlīdzeklis bez *a / the / my*: *by bus, by car, by train*. Latviski ar autobusu, bet angliski *by bus*, nevis *with bus*.")
FOOT = ("Walking is *on foot*, not *by foot*: *We went there on foot.*",
        "Kājām = *on foot*, nevis *by foot*: *We went there on foot.*")
IN = ("*in* + a car or a taxi: *in a taxi, in my car*. With *a / the / my* in front of the noun, *by* is not possible.",
      "Latviski taksometrā, bet angliski *in a taxi*; tāpat *in my car*. Ja pirms lietvārda ir *a / the / my*, tad *by* nelieto.")
ON = ("*on* + a bus, train, tram or plane: *on the tram, on the bus*.",
      "Latviski tramvajā, bet angliski *on the tram*; tāpat *on the bus, on the train, on the plane*.")

# choice (2)
mc(T, L, 2, "Choose the correct option: Is it cheaper to travel to Tallinn ___ bus?", "by", ["with", "on", "in"], *BY)
mc(T, L, 2, "Which sentence has a mistake?", "My daughter goes to school by foot.",
   ["We travelled around Italy by train.", "I fell asleep on the plane.", "He picked me up in his car."], *FOOT)
# word bank (2): no "by" chip before "the tram", because "by the tram" (= next to it) is correct English
gp(T, L, 3, "Today I'm going to work ___ Tom's car.", "in", *IN, bank=["in", "by", "on", "with"])
gp(T, L, 3, "I met an old friend ___ the tram yesterday.", "on", *ON, bank=["on", "in", "at"])
# typed gap (2): own instruction, so the topic's "Complete with in, on or at" is not added (it would give "on foot" a wrong hint)
gp(T, L, 3, "Write the missing word: The museum isn't far. Let's go ___ foot.", "on", *FOOT)
gp(T, L, 3, "Write the missing word: We went to the airport ___ a taxi.", "in", *IN)
# whole sentence (1): both corrections are right (in my car / by car)
tx(T, L, 4, "Correct the mistake: I go to work by my car.", "I go to work in my car. | I go to work by car.",
   "*by* + transport with no *my*: *by car*. With *my*: *in my car*.",
   "*by* + transportlīdzeklis bez *my*: *by car*. Ar *my*: *in my car*.")
