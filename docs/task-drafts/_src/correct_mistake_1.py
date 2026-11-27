"""Correct the mistake, round 1 (27 November 2026; blind round cm-1 applied: docs/review/blind/cm-1-judge.md; rounds cm-2, cm-3: cm-2-judge.md, cm-3-judge.md): the learner
finds the one mistake in a sentence and types the corrected sentence (or only the corrected words: Grader::correctedPart).
The task type already exists in 33 topics; this round adds it to three of the 44 topics that had none: Present simple,
Past simple, Future (agent proposal, 27 November; the teacher asked for new task types in the existing topics, step by step,
and does not read drafts: two blind readers and a judge decide).
Every mistake is one that learners at the level really make (docs/ERROR-TYPES.md, typical errors of the point in
docs/GRAMMAR-MAP.json); never a form nobody writes (*will to*, rule of 21 November). One mistake per sentence; the rest of the
sentence fixes the time so that only one correction fits; where another correction would also fix it, the instruction says what
to keep (*Keep *going to**). No card example and no scene of another task (judge, cm-1). Murphy, English Grammar in Use.
POINT_OF gives each row its grammar point (assign_points.py)."""
from lib import tx, save, ERRS, NOTES, rows

POINT_OF = {}
C = "Correct the mistake: "


def add(t, lv, q, ok, why, lvw, point, err=""):
    tx(t, lv, 3, q if q.startswith("Correct") else C + q, ok, why, lvw)
    POINT_OF[len(rows) - 1] = point
    if err: ERRS[len(rows) - 1] = err


def note(*parts):
    NOTES[len(rows) - 1] = " || ".join(parts)


def point_of(row):
    return POINT_OF[row]


# ---------------------------------------------------------------- Present simple (Murphy 2, 3, 4, 5)
T = "Present simple"
add(T, "A2.1", "My neighbour walk her dog every morning before work.",
    "My neighbour walks her dog every morning before work.",
    "*he / she / it* + verb-*s*: *My neighbour walks*. *every morning* is a habit.",
    "*he / she / it* + darbības vārds ar *-s*: *My neighbour walks*. *every morning* rāda ieradumu.",
    "ps_form", "3S")
add(T, "A2.1", "I am agree with you about the price.",
    "I agree with you about the price.",
    "*agree* is a verb, so no *am*: *I agree*.",
    "*agree* ir darbības vārds, tāpēc bez *am*: *I agree*. Tulkojot burtiski *esmu vienisprātis*, rodas *I am agree*.",
    "ps_form", "BE-VERB")
add(T, "A2.1", "Do your brother play any sport?",
    "Does your brother play any sport?",
    "*your brother* = *he*, so the question starts with *Does*: *Does your brother play …?*",
    "*your brother* = *he*, tāpēc jautājums sākas ar *Does*: *Does your brother play …?*",
    "ps_negq", "3S")
add(T, "A2.2", "My boss doesn't drinks coffee after lunch.",
    "My boss doesn't drink coffee after lunch.",
    "After *doesn't* the verb has no *-s*: *doesn't drink*.",
    "Aiz *doesn't* darbības vārdam nav *-s*: *doesn't drink*.",
    "ps_negq", "BASE")
add(T, "A2.2", "Where you usually buy your vegetables?",
    "Where do you usually buy your vegetables?",
    "A question with *Where* needs *do*: *Where do you usually buy …?*",
    "Jautājumā ar *Where* vajag *do*: *Where do you usually buy …?* Tulkojot burtiski *Kur tu parasti pērc …?*, rodas *Where you usually buy …?*",
    "ps_negq", "DO")
add(T, "A2.2", "Sorry, I am not understanding the question. Can you say it again?",
    "Sorry, I don't understand the question. Can you say it again? | Sorry, I can't understand the question. Can you say it again? | "
    "Sorry, I didn't understand the question. Can you say it again?",
    "*understand* is a state verb: it stays simple, *I don't understand*.",
    "*understand* ir stāvokļa darbības vārds: tas paliek vienkāršajā formā, *I don't understand*.",
    "stative", "STATE-ING")
note("Sorry, I can't understand the question. Can you say it again? :: Also correct: *can't understand* says you are not able to understand it. "
     "*understand* is a state verb, so never *am not understanding*. :: Arī pareizi: *can't understand* saka, ka tu nespēj to saprast. "
     "*understand* ir stāvokļa darbības vārds, tāpēc nekad *am not understanding*.",
     "Sorry, I didn't understand the question. Can you say it again? :: Also correct: *didn't understand* is about the moment you heard it. "
     "*understand* is a state verb, so never *am not understanding*. :: Arī pareizi: *didn't understand* ir par brīdi, kad tu to dzirdēji. "
     "*understand* ir stāvokļa darbības vārds, tāpēc nekad *am not understanding*.")
add(T, "B1.1", "I'm thinking this plan is too expensive for us, so let's look for another one.",
    "I think this plan is too expensive for us, so let's look for another one. | I think that this plan is too expensive for us, so let's look for another one.",
    "*think* = have an opinion: present simple, *I think this plan is too expensive*. *I'm thinking about it* = I am considering it now.",
    "*think* = būt viedoklim: Present Simple, *I think this plan is too expensive*. *I'm thinking about it* = es par to tagad domāju, apsveru.",
    "stative2", "STATE-ING")
add(T, "B1.1", "Light is travelling faster than sound, so you see the lightning before you hear the thunder.",
    "Light travels faster than sound, so you see the lightning before you hear the thunder.",
    "A fact that is always true: present simple, *Light travels faster than sound*. *is travelling* = it is happening now.",
    "Fakts, kas vienmēr ir patiess: Present Simple, *Light travels faster than sound*. *is travelling* = tas notiek tagad.",
    "ps_pc", "NOW-HABIT")
add(T, "B1.1", "It's depend on the traffic, so I can't say what time I'll be home.",
    "It depends on the traffic, so I can't say what time I'll be home.",
    "*depend* is a verb: *It depends on*, not *It's depend*.",
    "*depend* ir darbības vārds: *It depends on*, nevis *It's depend*. Tulkojot burtiski *tas ir atkarīgs*, rodas *It's depend*.",
    "ps_form", "BE-VERB")

# ---------------------------------------------------------------- Past simple (Murphy 5, 13, App. 1)
T = "Past simple"
add(T, "A2.1", "We was very tired after the long flight.",
    "We were very tired after the long flight.",
    "*we, you, they* + *were*: *We were very tired*.",
    "*we, you, they* + *were*: *We were very tired*.",
    "was_were")
add(T, "A2.1", "I buyed a new jacket last weekend.",
    "I bought a new jacket last weekend.",
    "*buy* is irregular: *buy → bought*.",
    "*buy* ir neregulārs darbības vārds: *buy → bought*.",
    "pst_irr", "PAST-FORM")
add(T, "A2.1", "Did you went to the concert on Friday?",
    "Did you go to the concert on Friday?",
    "After *Did* the verb is in the base form: *Did you go …?*",
    "Aiz *Did* darbības vārds ir pamatformā: *Did you go …?*",
    "pst_negq", "BASE")
add(T, "A2.2", "Robert join our team two months ago.",
    "Robert joined our team two months ago.",
    "*two months ago* is a finished time: past simple, *joined*.",
    "*two months ago* ir pabeigts laiks: Past Simple, *joined*.",
    "pst_reg", "PAST-FORM")
add(T, "A2.2", "I didn't saw your message until this morning.",
    "I didn't see your message until this morning.",
    "After *didn't* the verb is in the base form: *didn't see*.",
    "Aiz *didn't* darbības vārds ir pamatformā: *didn't see*.",
    "pst_negq", "BASE")
add(T, "A2.2", "We moved to this city before three years.",
    "We moved to this city three years ago.",
    "*ago* goes after the time: *three years ago*.",
    "*ago* stāv aiz laika: *three years ago*. Tulkojot burtiski *pirms trim gadiem*, rodas *before three years*.",
    "pst_reg")
add(T, "B1.1", "Correct the mistake. Keep *yesterday*: I have seen this film yesterday, so let's watch something else tonight.",
    "I saw this film yesterday, so let's watch something else tonight. | I watched this film yesterday, so let's watch something else tonight. | "
    "I saw this film yesterday, so let us watch something else tonight. | I watched this film yesterday, so let us watch something else tonight.",
    "*yesterday* is a finished time: past simple (*I saw*, *I watched*), not *I have seen*.",
    "*yesterday* ir pabeigts laiks: Past Simple (*I saw*, *I watched*), nevis *I have seen*.",
    "pp_ps", "FINISHED-TIME")
add(T, "B1.1", "Where did you stayed when you visited Rome last spring?",
    "Where did you stay when you visited Rome last spring?",
    "After *did* the verb is in the base form: *Where did you stay …?*",
    "Aiz *did* darbības vārds ir pamatformā: *Where did you stay …?*",
    "pst_negq", "BASE")
add(T, "B1.1", "The meeting finished late, so I catched the last bus home.",
    "The meeting finished late, so I caught the last bus home.",
    "*catch* is irregular: *catch → caught*.",
    "*catch* ir neregulārs darbības vārds: *catch → caught*.",
    "pst_irr", "PAST-FORM")

# ---------------------------------------------------------------- Future: will, going to, present continuous (Murphy 19-23)
T = "Future: will, going to, present continuous"
K = "Correct the mistake. Keep *going to*: "
add(T, "A2.1", "Correct the mistake. Keep *going*: We're going get a dog next year.",
    "We're going to get a dog next year.",
    "*going to* + base verb: *We're going to get*.",
    "*going to* + pamatforma: *We're going to get*.",
    "going_to")
add(T, "A2.1", K + "She going to look for a new flat in May.",
    "She is going to look for a new flat in May. | She's going to look for a new flat in May.",
    "*going to* needs *am / is / are* before it: *She is going to look*.",
    "Pirms *going to* vajag *am / is / are*: *She is going to look*.",
    "going_to", "BE")
add(T, "A2.1", "Will I turn on the heating? It's very cold in here.",
    " | ".join(f"{m} I turn on the heating? It's very cold in here." for m in ("Shall", "Should", "Can", "Could", "May"))
    + " | " + " | ".join(f"{m} I turn the heating on? It's very cold in here." for m in ("Shall", "Should", "Can", "Could", "May")),
    "An offer: *Shall I …?* (or *Can I …?*). *Will I turn on …?* asks about the future, not what you can do for someone.",
    "Piedāvājums: *Shall I …?* (vai *Can I …?*). *Will I turn on …?* jautā par nākotni, nevis piedāvā palīdzību.",
    "shall")
add(T, "A2.2", "It's late. I walk you to the bus stop.",
    "It's late. I'll walk you to the bus stop. | It's late. I will walk you to the bus stop. | It's late. I can walk you to the bus stop. | It's late. Let me walk you to the bus stop. | "
    "It's late. Shall I walk you to the bus stop? | It's late. Should I walk you to the bus stop?",
    "An offer you decide on now: *will*, *I'll walk you*. *I can walk you …* is an offer too.",
    "Piedāvājums, ko izlem tagad: *will*, *I'll walk you*. *I can walk you …* arī ir piedāvājums.",
    "will_now", "FUTURE")
note("It's late. Let me walk you to the bus stop. :: Also correct: *Let me walk you* is an offer too. With *I*, the offer needs *will*: *I'll walk you*. "
     ":: Arī pareizi: *Let me walk you* arī ir piedāvājums. Ar *I* piedāvājumam vajag *will*: *I'll walk you*.",
     *[f"It's late. {m} I walk you to the bus stop? :: Also correct: *Shall I …?* makes the offer a question. As a statement, the offer needs *will*: *I'll walk you*. "
       ":: Arī pareizi: *Shall I …?* piedāvā ar jautājumu. Apgalvojumā piedāvājumam vajag *will*: *I'll walk you*." for m in ("Shall", "Should")])
add(T, "A2.2", "I meet a client at nine tomorrow, so I can't take the kids to school.",
    "I'm meeting a client at nine tomorrow, so I can't take the kids to school. | I'm going to meet a client at nine tomorrow, so I can't take the kids to school.",
    "An arrangement with a time and another person: present continuous, *I'm meeting a client*.",
    "Norunāta tikšanās ar laiku un citu cilvēku: Present Continuous, *I'm meeting a client*.",
    "fut_arr", "FUTURE")
note("I'm going to meet a client at nine tomorrow, so I can't take the kids to school. :: Also correct: *going to* is your plan. "
     "*I'm meeting a client* says it is already arranged. :: Arī pareizi: *going to* ir tavs plāns. *I'm meeting a client* saka, ka tikšanās jau ir norunāta.")
add(T, "A2.2", K + "What you are going to do after the course?",
    "What are you going to do after the course?",
    "In a question *are* comes before *you*: *What are you going to do?*",
    "Jautājumā *are* stāv pirms *you*: *What are you going to do?*",
    "going_to", "Q-ORDER")
add(T, "B1.1", "I promise I tell you as soon as I hear any news about the job.",
    "I promise I'll tell you as soon as I hear any news about the job. | I promise I will tell you as soon as I hear any news about the job. | I promise to tell you as soon as I hear any news about the job.",
    "A promise: *will*, *I promise I'll tell you*. After *as soon as* the present stays: *as soon as I hear*.",
    "Solījums: *will*, *I promise I'll tell you*. Aiz *as soon as* paliek tagadne: *as soon as I hear*.",
    "will_now", "FUTURE")
add(T, "B1.1", "I can't go out until the plumber will come, so could you buy some bread?",
    "I can't go out until the plumber comes, so could you buy some bread? | I can't go out until the plumber has come, so could you buy some bread? | "
    "I can't go out until the plumber arrives, so could you buy some bread? | I can't go out until the plumber gets here, so could you buy some bread? | I can't go out until the plumber has arrived, so could you buy some bread? | I can't go out until the plumber 's come, so could you buy some bread? | I can't go out until the plumber 's arrived, so could you buy some bread?",
    "After *until* we use the present, also about the future: *until the plumber comes*, not *will come*.",
    "Aiz *until* lieto tagadni, arī runājot par nākotni: *until the plumber comes*, nevis *will come*. Latviski *kamēr atnāks* ir nākotnē, tāpēc gribas *will*.",
    "fut_time_clause", "TIME-CLAUSE")
PL = "I can't go out until the plumber {}, so could you buy some bread?"
note(PL.format("has come") + " :: Also correct: *has come* says the plumber will already be here. :: Arī pareizi: *has come* saka, ka santehniķis jau būs atnācis.",
     PL.format("has arrived") + " :: Also correct: *has arrived* says the plumber will already be here. :: Arī pareizi: *has arrived* saka, ka santehniķis jau būs ieradies.",
     PL.format("'s come") + " :: Also correct: *'s come* = *has come*: the plumber will already be here. :: Arī pareizi: *'s come* = *has come*: santehniķis jau būs atnācis.",
     PL.format("'s arrived") + " :: Also correct: *'s arrived* = *has arrived*: the plumber will already be here. :: Arī pareizi: *'s arrived* = *has arrived*: santehniķis jau būs ieradies.")
add(T, "B1.2", "My phone won't charge last night, so I couldn't call you.",
    "My phone wouldn't charge last night, so I couldn't call you. | My phone didn't charge last night, so I couldn't call you. | My phone wasn't charging last night, so I couldn't call you.",
    "*won't charge* = it refuses to charge now. *last night* is past: *wouldn't charge*.",
    "*won't charge* = tas atsakās lādēties tagad. *last night* ir pagātne: *wouldn't charge*.",
    "wont_refuse")
note("My phone didn't charge last night, so I couldn't call you. :: Also correct: *didn't charge* only says what happened. *wouldn't charge* says the phone "
     "refused, although you tried. :: Arī pareizi: *didn't charge* tikai saka, kas notika. *wouldn't charge* saka, ka telefons atteicās lādēties, lai gan tu mēģināji.",
     "My phone wasn't charging last night, so I couldn't call you. :: Also correct: *wasn't charging* describes the night. *wouldn't charge* says the phone "
     "refused, although you tried. :: Arī pareizi: *wasn't charging* apraksta, kas notika naktī. *wouldn't charge* saka, ka telefons atteicās lādēties, lai gan tu mēģināji.")
add(T, "B1.2", "Correct the mistake. Keep *about*: Sorry, I can't talk now. I'm about going into a meeting.",
    "Sorry, I can't talk now. I'm about to go into a meeting.",
    "*be about to* + base verb = very soon: *I'm about to go into a meeting*.",
    "*be about to* + pamatforma = tūlīt: *I'm about to go into a meeting*.",
    "about_to")

save("correct-mistake-1.csv")
