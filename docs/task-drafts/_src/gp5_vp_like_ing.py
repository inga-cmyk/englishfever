"""Batch 5, point vp_like_ing (A2.1): 9 tasks to reach 10 counted tasks. Murphy unit 53, 54, 58."""
from lib import gp, od, mc, tx
T = "Verb patterns"
L = "A2.1"

LIKE = ("*like, love, hate* + *-ing* (or *to* + verb): *I like cooking.* Not the base verb: not *I like cook*.",
        "*like, love, hate* + darbības vārds ar *-ing* (vai *to* + pamatforma): *I like cooking.* Nevis pamatforma: nevis *I like cook*.")
LIKE_LV = ("*like, love, hate* + *-ing* (or *to* + verb): *Ben likes playing tennis.* Not the base verb: not *likes play*.",
           "Tulkojot burtiski *Benam patīk spēlēt* → *Ben likes play*. Angļu valodā pēc *like, love, hate* lieto darbības vārdu ar *-ing* (vai *to* + pamatforma): *Ben likes playing tennis.*")
WANT = ("*want* + *to* + base verb: *I want to go.* Not *I want go* or *I want going*.",
        "*want* + *to* + pamatforma: *I want to go.* Nevis *I want go* vai *I want going*.")
WANT_LV = ("*want* + *to* + base verb: *Maria wants to take a taxi.* Not *wants take*.",
           "Tulkojot burtiski *gribu iet* → *I want go*. Angļu valodā pēc *want* vajag *to* + pamatforma: *Maria wants to take a taxi.*")

# choose (2): Murphy 58 (like / love / hate + -ing or to: to is not a wrong option), Murphy 54 (want + to)
mc(T, L, 2, "Choose the correct option: My brother hates ___ early.", "getting up", ["get up", "gets up", "to getting up"], *LIKE)
# typed gap (3)
gp(T, L, 3, "My dad loves ___ old films. (watch)", "watching | to watch", *LIKE)
# word order (1): where to goes (want to come, not want come to)
od(T, L, 3, "Put the words in order to make a question.", "do you want to come with us", *WANT)
gp(T, L, 3, "I want ___ my own café one day. (open)", "to open", *WANT)
# word bank (1): real forms of the verb that do not fit after want
gp(T, L, 3, "My parents want ___ ___ a dog.", "to / get", *WANT, bank=["to", "get", "getting", "gets"])
mc(T, L, 2, "Which sentence has a mistake?", "Ben likes play tennis on Sundays.",
   ["I want to visit Prague in May.", "We love walking in the forest.", "Do you like working from home?"], *LIKE_LV)
gp(T, L, 3, "Does your partner like ___ computer games? (play)", "playing | to play", *LIKE)
# whole sentence (2)
tx(T, L, 4, "Correct the mistake: Maria wants take a taxi to the airport.", "Maria wants to take a taxi to the airport.", *WANT_LV)
tx(T, L, 4, "Say it another way with *love*: Cooking is my favourite hobby.",
   "I love cooking. | I love to cook. | I really love cooking. | I really love to cook. | I love cooking very much.", *LIKE)
