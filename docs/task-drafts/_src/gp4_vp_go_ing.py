"""Batch 4, point vp_go_ing (A2.2): go + -ing (go shopping, go skiing), go for a + noun (go for a walk, a coffee),
go to + place (go to the gym, to work, to bed), go on holiday / a trip, go home (no to).
Murphy, Essential Grammar in Use, the unit "go to ... / go on ... / go for ... / go + -ing" (unit 56 as named by the lead;
the number was not checked against the contents list), and English Grammar in Use unit 126 (to / at / in / into: go home, no to).
Never a wrong option that is correct English somewhere: no *on* before a walk / a run / a swim (go on a walk is used, US and UK),
no *on* before -ing (go on shopping = continue shopping), no *to* + verb (went to ski = purpose)."""
from lib import gp, od, mc, tx, mt, learning_task
T = "Verb patterns"
L = "A2.2"

ING = ("*go* + *-ing* for activities, with nothing in between: *go fishing, go skiing, go camping*. Not *go to fishing* or *go for fishing*.",
       "*go* + *-ing* nodarbēm, bez nekā starp tiem: *go fishing, go skiing, go camping*. Nevis *go to fishing* vai *go for fishing*.")
SHOP = ("*go shopping*, not *go to shopping*. *go to* + a place: *go to the shops, go to the gym*.",
        "*go shopping*, nevis *go to shopping*. *go to* + vieta: *go to the shops, go to the gym*.")
FOR = ("*go for a* + noun for a short activity: *go for a coffee, a drink, a walk, a run*.",
       "*go for a* + lietvārds īsām nodarbēm: *go for a coffee, a drink, a walk, a run*.")
SWIM = ("*go for a swim* (*a* + noun) = *go swimming* (*-ing*, no *for*). Not *go for swimming* or *go for a swimming*.",
        "*go for a swim* (*a* + lietvārds) = *go swimming* (*-ing*, bez *for*). Nevis *go for swimming* vai *go for a swimming*.")
RUN = ("*go running* (*-ing*, no *for*) = *go for a run* (*a* + noun). Not *go for running*.",
       "*go running* (*-ing*, bez *for*) = *go for a run* (*a* + lietvārds). Nevis *go for running*.")
WALK = ("*go for a walk*: *for a* + noun. *go on a walk* is also used, especially in American English.",
        "*go for a walk*: *for a* + lietvārds. Lieto arī *go on a walk*, īpaši amerikāņu angļu valodā.")
TO = ("*go to* + a place: *go to the gym, go to the cinema, go to work, go to bed*.",
      "*go to* + vieta: *go to the gym, go to the cinema, go to work, go to bed*.")
BED = ("*go to* + a place: *go to bed* (with no *the*), *go to work*, *go to the gym*.",
       "*go to* + vieta: *go to bed* (bez *the*), *go to work*, *go to the gym*.")
WORK = ("*go to work*: *go to* + a place, with no *the*. In British English *go into work* is also said.",
        "*go to work*: *go to* + vieta, bez *the*. Lielbritānijā saka arī *go into work*.")
ON = ("*go on* + *holiday* or *a trip*: *go on holiday, go on a trip*. Not *go to holiday* or *go for holiday*.",
      "*go on* + *holiday* vai *a trip*: *go on holiday, go on a trip*. Nevis *go to holiday* vai *go for holiday*.")
HOME = ("*go home*, not *go to home* or *go at home*: *I'm going home.*",
        "Saka *go home*, nevis *go to home* vai *go at home*: *I'm going home.*")
ALL = ("*go* + *-ing* (*go fishing*), *go for a* + noun (*go for a coffee*), *go to* + place (*go to the gym*), *go on holiday*, *go home*.",
       "*go* + *-ing* (*go fishing*), *go for a* + lietvārds (*go for a coffee*), *go to* + vieta (*go to the gym*), *go on holiday*, *go home*.")

# choose (7)
mc(T, L, 2, "Choose the correct option: We often go ___ fishing at the lake.", "—", ["to", "for"], *ING)
mc(T, L, 2, "Choose the correct option: Let's go ___ a coffee after the meeting.", "for", ["to", "on", "—"], *FOR)
mc(T, L, 2, "Choose the correct option: They're going ___ holiday to Greece in May.", "on", ["to", "for", "in"], *ON)
mc(T, L, 2, "Choose the correct option: Do you want to go ___ before breakfast?", "for a swim",
   ["for swimming", "to swimming", "for a swimming"], *SWIM)
mc(T, L, 2, "Which sentence is correct?", "We went skiing in Austria last winter.",
   ["We went to skiing in Austria last winter.", "We went for skiing in Austria last winter.", "We went for a skiing in Austria last winter."], *ING)
mc(T, L, 2, "Which sentence is NOT correct?", "Shall we go to shopping on Saturday?",
   ["I go to the gym after work.", "Let's go for a walk by the river.", "We're going on a trip next month."], *SHOP)
mc(T, L, 2, "Which sentence is NOT correct?", "I went to home early yesterday.",
   ["She goes running every morning.", "We went for a drink after work.", "He goes to bed very late."], *HOME)

# type a word (5): every correct word is accepted
gp(T, L, 3, "Write the missing word: I usually go ___ bed at eleven.", "to", *BED)
gp(T, L, 3, "Write the missing word: Where are you going ___ holiday this year?", "on", *ON)
gp(T, L, 3, "Write the missing word: What time do you go ___ work?", "to | into", *WORK)
gp(T, L, 3, "Write the missing word: We went ___ a long walk on the beach.", "for | on", *WALK)
gp(T, L, 3, "She goes ___ in the park every morning. (run)", "running | for a run", *RUN)

# whole sentence (3)
tx(T, L, 4, "Say it another way with *for*: Let's go swimming after work.",
   "Let's go for a swim after work. | After work, let's go for a swim. | Shall we go for a swim after work? | Let's go out for a swim after work.", *SWIM)
tx(T, L, 4, "Say it another way with *shopping*: Let's go to the shops this afternoon.",
   "Let's go shopping this afternoon. | This afternoon, let's go shopping. | Shall we go shopping this afternoon? | Let's do some shopping this afternoon. | Let's do the shopping this afternoon. | Shall we do some shopping this afternoon? | Let's go and do some shopping this afternoon.", *SHOP)
tx(T, L, 4, "Say it another way with *for*: I took a short walk after lunch.",
   "I went for a short walk after lunch. | After lunch, I went for a short walk. | I went out for a short walk after lunch. | After lunch, I went out for a short walk. | I went for a walk after lunch. | After lunch, I went for a walk.", *FOR)

# word order (5)
od(T, L, 3, "Put the words in order.", "we go cycling every saturday", *ING, also=["every saturday we go cycling"])
od(T, L, 3, "Put the words in order.", "my dad goes for a bike ride every sunday", *FOR, also=["every sunday my dad goes for a bike ride"])
od(T, L, 3, "Put the words in order.", "she goes to the gym before work", *TO, also=["before work she goes to the gym"])
od(T, L, 3, "Put the words in order.", "we're going on holiday next week", *ON, also=["next week we're going on holiday"])
od(T, L, 3, "Put the words in order.", "he went home after the meeting", *HOME, also=["after the meeting he went home"])

# word bank (4): the extra chips are the typical mistakes of this point
gp(T, L, 3, "We went ___ a boat trip on the river.", "on", *ON, bank=["on", "to", "—"])
gp(T, L, 3, "Last summer we went ___ in the forest.", "camping", *ING, bank=["camping", "to camping", "for camping"])
gp(T, L, 3, "It's late, so I'm going ___.", "home", *HOME, bank=["home", "to home", "at home"])
gp(T, L, 3, "Let's go ___ a ___ before dinner.", "for / run", *RUN, bank=["for", "run", "to", "running"])

# matching (1): a learning task automatically
mt(T, L, 2, "Match each beginning with its ending.", [("Let's go for", "a coffee after work."), ("She goes to", "the gym every morning."),
   ("We're going on", "holiday in July."), ("They often go", "fishing at the weekend.")], *ALL)
