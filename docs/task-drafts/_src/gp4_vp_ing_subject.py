"""Batch 4, point vp_ing_subject (A2.2): -ing as the subject (Swimming is good for you). Murphy has no unit of its own:
the -ing form from Murphy 53 (verb + -ing) and 60 (preposition + -ing, the -ing form used like a noun); It's + adjective + to
(the other correct way to say it) from Murphy 65. To + verb as the subject (To learn a language takes time) is correct but
formal and rare: it is never a wrong option, and it is accepted in every typed gap where it fits (questions rule it out)."""
from lib import gp, od, mc, tx, mt, learning_task
T = "Verb patterns"
L = "A2.2"


def form(ok, bad, lv_lit=None, lit_bad=None):
    """An activity at the start takes -ing (bad: the wrong starts, e.g. ["Walk", "To walking"])."""
    en = f"An activity at the start of a sentence takes *-ing*: *{ok}* Not " + " or ".join(f"*{b}*" for b in bad) + "."
    lv = f"Ja teikums sākas ar aktivitāti, lieto formu ar *-ing*: *{ok}* Nevis " + " vai ".join(f"*{b}*" for b in bad) + "."
    if lv_lit: lv += f" Tulkojot burtiski \"{lv_lit}\", sanāk *{lit_bad}*."
    return en, lv


def agr(subj, ok, bad, extra_en="", extra_lv=""):
    """One activity = one thing: the verb after it is singular."""
    return (f"*{subj}* is one activity, so the verb is singular: *{ok}* Not *{bad}*.{extra_en}",
            f"*{subj}* ir viena aktivitāte, tāpēc darbības vārds ir vienskaitlī: *{ok}* Nevis *{bad}*.{extra_lv}")


def both(ok):
    """Word order and matching: -ing at the start, a singular verb after it."""
    return (f"An activity at the start of a sentence takes *-ing*, and the verb after it is singular: *{ok}*",
            f"Ja teikums sākas ar aktivitāti, lieto formu ar *-ing*, un darbības vārds aiz tās ir vienskaitlī: *{ok}*")


def with_to(ok, to):
    """A typed gap that also accepts to + verb: the explanation says both are correct."""
    return (f"An activity at the start of a sentence usually takes *-ing*: *{ok}* *{to}* is also correct, but formal and less common.",
            f"Ja teikums sākas ar aktivitāti, parasti lieto formu ar *-ing*: *{ok}* Arī *{to}* ir iespējams, bet tā runā retāk un oficiālāk.")


def quest(ok, note_en, note_lv):
    """The -ing activity is the subject of the question or the negative."""
    return (f"The *-ing* activity is the subject: *{ok}* {note_en}",
            f"Aktivitāte ar *-ing* ir teikuma priekšmets: *{ok}* {note_lv}")


DOES = ("One activity, so *does*, not *do*; after *does* the base verb.", "Viena aktivitāte, tāpēc *does*, nevis *do*; aiz *does* pamatforma.")

# ---------- choice (7) ----------
mc(T, L, 2, "Choose the correct option: ___ is good for your heart.", "Walking", ["Walk", "To walking"],
   *form("Walking is good for your heart.", ["Walk", "To walking"], "Staigāt ir veselīgi", "Walk is good"))
mc(T, L, 2, "Choose the correct option: Meeting new people ___ fun.", "is", ["are", "were"],
   *agr("Meeting new people", "Meeting new people is fun.", "are"))
mc(T, L, 2, "Choose the correct option: ___ a new language takes time.", "Learning", ["Learn", "To learning"],
   *form("Learning a new language takes time.", ["Learn", "To learning"], "Mācīties svešvalodu aizņem laiku", "Learn a new language takes time"))
mc(T, L, 2, "Choose the correct option: Booking flights early ___ money.", "saves", ["save", "saving"],
   *agr("Booking flights early", "Booking flights early saves money.", "save"))
mc(T, L, 2, "Which sentence is correct?", "Cooking relaxes me after work.",
   ["Cook relaxes me after work.", "Cooking relax me after work.", "To cooking relaxes me after work."],
   *both("Cooking relaxes me after work."))
mc(T, L, 2, "Choose the correct option: ___ long hours makes me tired.", "Working", ["Work", "To working"],
   *form("Working long hours makes me tired.", ["Work", "To working"]))
mc(T, L, 2, "Which sentence is NOT correct?", "Watching the news make me sad.",
   ["Driving at night is tiring.", "Is parking free at the hotel?", "Learning to cook takes time."],
   *agr("Watching the news", "Watching the news makes me sad.", "make"))

# ---------- word order (5) ----------
od(T, L, 3, "Put the words in order.", "cycling to work saves me money", *both("Cycling to work saves me money."))
od(T, L, 3, "Put the words in order.", "travelling alone is not always easy", *both("Travelling alone is not always easy."))
od(T, L, 3, "Put the words in order.", "playing the guitar helps me relax", *both("Playing the guitar helps me relax."))
od(T, L, 3, "Put the words in order to make a question.", "is learning english hard for you",
   *quest("Is learning English hard for you?", "*Is* comes first, then the activity.", "Sākumā *is*, tad aktivitāte."))
od(T, L, 3, "Put the words in order.", "charging my phone takes two hours", *both("Charging my phone takes two hours."))

# ---------- word bank (4) ----------
gp(T, L, 3, "___ is my favourite way to relax.", "Reading",
   *form("Reading is my favourite way to relax.", ["Read", "To reading"]), bank=["Reading", "Read", "To reading"])
gp(T, L, 3, "Riding a bike ___ me fit.", "keeps",
   *agr("Riding a bike", "Riding a bike keeps me fit.", "keep"), bank=["keeps", "keep", "keeping"])
gp(T, L, 3, "___ ___ English help you at work?", "Does / speaking",
   *quest("Does speaking English help you at work?", *DOES), bank=["Does", "speaking", "Do", "speak"])
gp(T, L, 3, "___ ___ not allowed in this lake.", "Swimming / is",
   *both("Swimming is not allowed in this lake."), bank=["Swimming", "is", "Swim", "are"])

# ---------- matching (1, a learning task by its type) ----------
mt(T, L, 2, "Match each beginning with its ending.", [("Brushing your teeth twice a day", "keeps them healthy."),
   ("Wearing a helmet on a bike", "protects your head."), ("Speaking English well", "helps you find a good job."),
   ("Booking a hotel early", "makes it cheaper.")],
   "Each activity at the start takes *-ing*, and the verb after it is singular: *Wearing a helmet on a bike protects your head.*",
   "Visām aktivitātēm teikuma sākumā lieto formu ar *-ing*, un darbības vārds aiz tām ir vienskaitlī: *Wearing a helmet on a bike protects your head.*")

# ---------- typed gap (5) ----------
gp(T, L, 3, "Is ___ a car expensive in Riga? (rent)", "renting",
   *quest("Is renting a car expensive in Riga?", "Not *Is rent* or *Is to rent*.", "Nevis *Is rent* vai *Is to rent*."))
gp(T, L, 3, "___ late at night is bad for you. (eat)", "Eating | To eat",
   *with_to("Eating late at night is bad for you.", "To eat late at night"))
gp(T, L, 3, "Why is ___ so popular in Denmark? (cycle)", "cycling",
   *quest("Why is cycling so popular in Denmark?", "Not *Why is cycle* or *Why is to cycle*.", "Nevis *Why is cycle* vai *Why is to cycle*."))
gp(T, L, 3, "___ to music helps me work. (listen)", "Listening | To listen",
   *with_to("Listening to music helps me work.", "To listen to music"))
gp(T, L, 3, "Getting up early ___ never easy for me. (be)", "is | was",
   *agr("Getting up early", "Getting up early is never easy for me.", "are", " (*was* for the past.)", " (*was* pagātnē.)"))

# ---------- whole sentence (3) ----------
tx(T, L, 4, "Make it negative: Flying makes me nervous.", "Flying doesn't make me nervous.",
   *quest("Flying doesn't make me nervous.", "One activity, so *doesn't*, not *don't*.", "Viena aktivitāte, tāpēc *doesn't*, nevis *don't*."))
tx(T, L, 4, "Make a yes/no question: Living in a big city is expensive.",
   "Is living in a big city expensive? | Is living expensive in a big city?",
   *quest("Is living in a big city expensive?", "*Is* goes before the whole activity: *living in a big city*.",
          "*Is* stāv pirms teikuma priekšmeta: *living in a big city*."))
tx(T, L, 4, "Make a yes/no question: Using this app saves you time.", "Does using this app save you time? | Does using this app save time?",   # r9
   *quest("Does using this app save you time?", *DOES))
