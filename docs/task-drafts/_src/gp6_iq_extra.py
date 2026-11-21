"""Indirect questions, two gaps the teacher pointed out (21 November; scope from her summary, our own sentences):
A. B1.2, ind_polite: four *Which sentence has a mistake?* where the mistake is a question mark after a sentence that is not a
   question (I'd like to know / I'm not sure / I have no idea / I wonder ...?). Each task has right sentences WITH a question mark
   (Could you tell me / Do you know / Can you remember ...?) and one with a full stop, so the learner must judge the start, not
   spot "?". Card ind_polite: "A question mark after Could you tell me...? / Do you know...?; a full stop after I wonder... /
   I'd like to know...". Murphy unit 50.
B. B2.2, ind_advanced, point iq_whether: if = a condition (only in that case) vs whether = yes or no, in either case; only
   whether after a preposition, before to + verb and directly before or not. Swan, Practical English Usage, "if and whether";
   Murphy unit 50. Postposed if after tell / let me know is avoided where it could be an indirect question (Let me know if ...
   has both readings): the condition is always a fronted if-clause or a request that only makes sense in one case.
No save() here: the lead agent adds this module to the batch iq_b1_6.py. POINT_OF gives each row's grammar point (row index in
lib.rows -> point), because iq_b1_6.point_of() would read the if in a right option as iq_yn. Notes: gp6_iq_extra-notes.md."""
import lib
from lib import gp, mc, rows

POINT_OF = {}
# The Latvian texts use only words the italics marking knows as Latvian (no LV_BY_FILE entry needed), and never quote
# *I have no idea* (the Latvian "no" would break the italics).


def point(p):
    POINT_OF[len(rows) - 1] = p


# ===================== A. B1.2: a question mark only after a question (Could you tell me ...? / I wonder ... .) =====================
T = "Indirect questions (Could you tell me where...)"
L = "B1.2"

mc(T, L, 3, "Which sentence has a mistake?", "I'd like to know why the meeting was moved?",
   ["Could you tell me when the last bus leaves?", "I wonder what she bought for her brother.", "Do you know if Tom has finished the report?"],
   "*I'd like to know…* is not a question, so it ends with a full stop: *I'd like to know why the meeting was moved.* "
   "*Could you tell me…?* and *Do you know…?* are questions, so they keep the question mark.",
   "*I'd like to know…* nav jautājums, tāpēc beigās ir punkts: *I'd like to know why the meeting was moved.* "
   "*Could you tell me…?* un *Do you know…?* ir jautājumi, tāpēc tiem ir jautājuma zīme.")
point("iq_wh")

mc(T, L, 3, "Which sentence has a mistake?", "I'm not sure which gate our flight leaves from?",
   ["Can you remember where we parked the car?", "I have no idea who sent me these flowers.", "Do you know if the hotel serves breakfast?"],
   "*I'm not sure…* is not a question, so it ends with a full stop: "
   "*I'm not sure which gate our flight leaves from.* *Can you remember…?* and *Do you know…?* are questions: question mark.",
   "*I'm not sure…* nav jautājums, tāpēc beigās ir punkts: "
   "*I'm not sure which gate our flight leaves from.* *Can you remember…?* un *Do you know…?* ir jautājumi: jautājuma zīme.")
point("iq_wh")

mc(T, L, 3, "Which sentence has a mistake?", "I have no idea why my phone keeps switching off?",
   ["Could you tell me how long the course lasts?", "I'm not sure whether I locked the front door.", "Do you know who won the match last night?"],
   "*I have no idea…* is a statement, not a question, so it ends with a full stop: *I have no idea why my phone keeps switching off.* "
   "Only a sentence that asks (*Could you tell me…?*, *Do you know…?*) has a question mark.",
   "Teikums par *phone* nav jautājums, tāpēc beigās ir punkts: *… why my phone keeps switching off.* "
   "Jautājuma zīme ir vajadzīga, kad teikums jautā: *Could you tell me…?*, *Do you know…?*")
point("iq_wh")

mc(T, L, 3, "Which sentence has a mistake?", "I wonder how Anna's job interview went?",
   ["Could you tell me which room the exam is in?", "I'm not sure how many people are coming.", "Can you tell me how you made this soup?"],
   "*I wonder…* is not a question, so it ends with a full stop: *I wonder how Anna's job interview went.* "
   "*Could you tell me…?* and *Can you tell me…?* are questions, so they keep the question mark.",
   "*I wonder…* nav jautājums, tāpēc beigās ir punkts: *I wonder how Anna's job interview went.* "
   "*Could you tell me…?* un *Can you tell me…?* ir jautājumi, tāpēc tiem ir jautājuma zīme.")
point("iq_wh")

# ===================== B. B2.2: if (a condition, only in that case) vs whether (yes or no, in either case) =====================
T = "Indirect questions, more uses (I don't know what to do)"
L = "B2.2"

# 1. meaning: either case (learn). The if-sentences are fronted conditions, so they cannot be read as indirect questions.
mc(T, L, 2, "Which sentence means you give your manager an answer in either case?", "Tell your manager whether you can work on Saturday.",
   ["If you can work on Saturday, tell your manager.", "If you can't work on Saturday, tell your manager.", "Tell your manager that you can work on Saturday."],
   "*whether* = yes or no: you give your manager the answer in either case. *If* at the start is a condition: you tell your manager only in that one case. "
   "*that you can work* gives only one answer.",
   "*whether* nozīmē *vai*: vadītājam atbildi saki jebkurā gadījumā. *If* teikuma sākumā ir nosacījums (*ja*): saki to vienīgi tajā vienā gadījumā. "
   "*that you can work* dod vienu atbildi.")
point("iq_whether")

# 2. meaning: only in one case (learn). "ask if / ask whether" both report a question: you call anyway.
mc(T, L, 2, "Which sentence means you call the airline only when there is a problem?", "If your bag doesn't arrive, call the airline.",
   ["Call the airline to ask whether your bag has arrived.", "Whether or not your bag arrives, call the airline.", "Call the airline and ask if your bag has arrived."],
   "*If* + a condition at the start: you call only in that case. *ask whether* and *ask if* report a question, so you call anyway to get the answer; "
   "*whether or not* = in both cases.",
   "*If* teikuma sākumā ir nosacījums (*ja*): zvanīt vajag vienīgi tad. *ask whether* un *ask if* nozīmē *pajautāt, vai*, tāpēc zvanīt vajag jebkurā gadījumā; "
   "*whether or not* nozīmē *jebkurā gadījumā*.")
point("iq_whether")

# 3. (removed after blind r18: the only believable second wrong option, *Whether or not*, is grammatical, and the importer needs two)

# 4. if before to + verb (the typical mistake; blind r18: *depends on if* is common in informal English, so not used as the mistake).
mc(T, L, 3, "Which sentence has a mistake?", "We still haven't decided if to rent a car in Crete.",
   ["Everything now depends on whether the bank approves our loan.", "If the train is delayed, I'll take a taxi.", "Could you check whether the hotel has a lift?"],
   "Before *to* + verb only *whether* is possible: *We still haven't decided whether to rent a car*. *If* needs a subject and a verb: *if we should rent a car*.",
   "Pirms *to* + darbības vārds var būt tikai *whether*: *We still haven't decided whether to rent a car*. Aiz *if* vajag teikuma priekšmetu un darbības vārdu: *if we should rent a car*.")
point("iq_whether")

# 5. both in one sentence: whether before to + verb, if for the condition (unless is illogical: keeping the room until midnight only matters when we are late).
gp(T, L, 3, "The hotel wants to know ___ to expect us before ten, and ___ we're late, they'll keep the room for us until midnight.", "whether / if",
   "Before *to* + verb only *whether* is possible: *whether to expect us*. *if we're late* is a condition: they keep the room for us only in that case.",
   "Saka *whether to expect us*, nevis *if to expect us*. *if we're late* ir nosacījums (*ja*): viesnīca gaidīs vienīgi tad.",
   bank=["whether", "if", "unless"])
point("iq_whether")

# 6. whether or not: *if or not* is the mistake.
gp(T, L, 3, "Complete with one word: The caterer needs to know ___ or not you're coming to the wedding.", "whether",
   "Directly before *or not* only *whether* is possible: *whether or not you're coming*. *if or not* is a mistake.",
   "Tieši pirms *or not* var būt vienīgi *whether*: *whether or not you're coming*. *if or not* ir kļūda.")
point("iq_whether")
