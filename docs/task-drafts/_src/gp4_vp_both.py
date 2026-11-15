"""Batch 4, point vp_both (B1.1): verbs that take -ing or to + verb with (almost) the same meaning: start, begin, continue,
like, love, hate, prefer; would like / would love / would prefer take only to. Murphy unit 56 (begin, start, continue: -ing or
to, no difference; no -ing after -ing: it's starting to rain), unit 58 (like, love, hate: both; would like / would love + to),
unit 59 (prefer doing / prefer to do; would prefer to do).
Every typed gap after these verbs accepts both forms. A choice or a bank never offers the two right forms together: either the
wrong sentence is the only one (Which sentence is NOT correct?) or the other right form is not among the options."""
from lib import gp, od, mc, tx, mt, learning_task
T = "Verb patterns"
L = "B1.1"


def both(verb, a, b):
    """Both forms are right after this verb."""
    return (f"After *{verb}* both forms are correct, with the same meaning: *{a}* = *{b}*.",
            f"Aiz *{verb}* der abas formas, ar *-ing* un ar *to* + pamatformu, un nozīme ir tā pati: *{a}* = *{b}*.")


def only(verb, ok, bad, other):
    """A choice or a bank where the other right form is not offered."""
    return (f"After *{verb}* use *-ing* or *to* + base verb: *{ok}* (*{other}* is correct too). Not *{bad}*.",
            f"Aiz *{verb}* lieto formu ar *-ing* vai *to* + pamatformu: *{ok}* (der arī *{other}*). Nevis *{bad}*.")


def would(ok, bad):
    """would like / would love / would prefer + to."""
    return (f"*would like / would love / would prefer* + *to* + base verb, never *-ing*: *{ok}* Not *{bad}*.",
            f"*would like / would love / would prefer* + *to* + pamatforma, nekad ar *-ing*: *{ok}* Nevis *{bad}*.")


# ---------- choice (7) ----------
mc(T, L, 2, "Choose the correct option: My laptop is eight years old, but it continues ___ without any problems.", "to work",
   ["work", "to working"],
   *only("continue", "it continues to work", "it continues work / to working", "it continues working"))
mc(T, L, 2, "Choose the correct option: When the band came on stage, the whole crowd started ___.", "dancing",
   ["dance", "danced", "to dancing"],
   *only("start", "the crowd started dancing", "started dance / danced / to dancing", "started to dance"))
mc(T, L, 2, "Which sentence is NOT correct?", "I'd like going to the concert with you on Saturday.",
   ["My sister hates to fly, so she always takes the train.", "We started building our new website in January.",
    "He continued to work part-time after he retired."],
   "*would like* takes only *to*: *I'd like to go to the concert.* After *hate, start, continue* both forms are correct (*hates flying / hates to fly*).",
   "*would like* lieto tikai ar *to*: *I'd like to go to the concert.* Aiz *hate, start, continue* der abas formas (*hates flying / hates to fly*).")
mc(T, L, 2, "Choose the correct option: We'd love ___ to your party, but we're away that weekend.", "to come",
   ["coming", "come", "to coming"],
   *would("We'd love to come.", "We'd love coming / come / to coming"))
mc(T, L, 2, "Which sentence is NOT correct?", "She started learn Spanish when she moved to Valencia.",
   ["I love cooking for my friends at the weekend.", "They began to argue as soon as the meeting started.",
    "Would you prefer to sit by the window?"],
   "After *start* use *-ing* or *to* + base verb: *She started learning / to learn Spanish.* The base form alone is wrong.",
   "Aiz *start* lieto formu ar *-ing* vai *to* + pamatformu: *She started learning / to learn Spanish.* Tikai pamatforma ir kļūda. "
   "Tulkojot burtiski \"sāka mācīties\", sanāk *started learn*.")
mc(T, L, 2, "Which sentence is correct?", "My husband hates driving at night, so I usually drive us home.",
   ["My husband hates drive at night, so I usually drive us home.", "My husband hates to driving at night, so I usually drive us home."],
   "After *hate* use *-ing* or *to* + base verb: *hates driving* or *hates to drive*. Not the base form alone, and not *to* + *-ing*.",
   "Aiz *hate* lieto formu ar *-ing* vai *to* + pamatformu: *hates driving* vai *hates to drive*. Nevis tikai pamatformu un nevis *to* + *-ing*.")
mc(T, L, 2, "Which sentence is NOT correct?", "We like eat out on Friday evenings after a long week.",
   ["Our team began to use the new software last month.", "She prefers to cycle to work when the weather is nice.",
    "Would you like to join our book club this autumn?"],
   "After *like* use *-ing* or *to* + base verb: *We like eating out / We like to eat out.* The base form alone is wrong.",
   "Aiz *like* lieto formu ar *-ing* vai *to* + pamatformu: *We like eating out / We like to eat out.* Tikai pamatforma ir kļūda. "
   "Tulkojot burtiski \"mums patīk ēst ārpus mājas\", sanāk *we like eat out*.")

# ---------- typed gap (5): both forms accepted ----------
gp(T, L, 3, "The audience began ___ before the actor finished his joke. (laugh)", "laughing | to laugh",
   *both("begin", "began laughing", "began to laugh"))
gp(T, L, 3, "My partner loves ___ new recipes, so we often have friends over at the weekend. (try)", "trying | to try",
   *both("love", "loves trying", "loves to try"))
gp(T, L, 3, "Do you prefer ___ on holiday alone or with friends? (go)", "going | to go",
   *both("prefer", "Do you prefer going", "Do you prefer to go"))
gp(T, L, 3, "Many people continued ___ from home after the offices reopened. (work)", "working | to work",
   *both("continue", "continued working", "continued to work"))
gp(T, L, 3, "I hate ___ on the phone, so I usually send a text message instead. (talk)", "talking | to talk",
   *both("hate", "I hate talking", "I hate to talk"))

# ---------- whole sentence (3) ----------
tx(T, L, 4, "Say it another way with *to*: We started looking for a new flat as soon as I got the job.",
   "We started to look for a new flat as soon as I got the job. | As soon as I got the job, we started to look for a new flat. | We began to look for a new flat as soon as I got the job. | As soon as I got the job, we began to look for a new flat.",
   *both("start", "started looking", "started to look"))
tx(T, L, 4, "Correct the mistake: I love spend time with my cousins because they always make me laugh.",
   "I love spending time with my cousins because they always make me laugh. | I love to spend time with my cousins because they always make me laugh.",
   "After *love* use *-ing* or *to* + base verb, both are correct: *I love spending time* = *I love to spend time*. The base form alone is wrong.",
   "Aiz *love* lieto formu ar *-ing* vai *to* + pamatformu, abas ir pareizas: *I love spending time* = *I love to spend time*. Tikai pamatforma ir kļūda.")
tx(T, L, 4, "Correct the mistake: Would you like coming with us to the team lunch on Friday?",
   "Would you like to come with us to the team lunch on Friday?",
   *would("Would you like to come with us?", "Would you like coming"))

# ---------- word order (5) ----------
od(T, L, 3, "Put the words in order.", "she began to write a blog about her travels last year",
   *both("begin", "began to write", "began writing"), also=["last year she began to write a blog about her travels", "she began to write a blog last year about her travels"])
od(T, L, 3, "Put the words in order to make a question.", "would you like to have a coffee before the meeting",
   *would("Would you like to have a coffee?", "Would you like having"), also=["before the meeting would you like to have a coffee"])
od(T, L, 3, "Put the words in order.", "my father started using a smartphone when he turned seventy",
   *both("start", "started using", "started to use"),
   also=["when he turned seventy my father started using a smartphone", "when my father turned seventy he started using a smartphone"])
od(T, L, 3, "Put the words in order.", "she continued working at the hospital after her first child was born",
   *both("continue", "continued working", "continued to work"),
   also=["after her first child was born she continued working at the hospital"])
od(T, L, 3, "Put the words in order to make a question.", "do you prefer to cook at home or go to restaurants",
   *both("prefer", "prefer to cook", "prefer cooking"), also=["do you prefer to go to restaurants or cook at home"])

# ---------- word bank (4): one right chip; the other right form is not a chip ----------
gp(T, L, 3, "During the long winter my brother started ___ his own furniture, and now he sells it online.", "making",
   *only("start", "he started making", "started make / to making", "he started to make"), bank=["making", "make", "to making"])
gp(T, L, 3, "I'd like ___ a table for four at eight o'clock, please.", "to book",
   *would("I'd like to book a table.", "I'd like booking / book"), bank=["to book", "booking", "book"])
gp(T, L, 3, "My parents love ___ in the mountains, so they go there every summer.", "walking",
   *only("love", "they love walking", "love walk / to walking", "they love to walk"), bank=["walking", "walk", "to walking"])
gp(T, L, 3, "House prices will probably continue ___ next year, so this is a good time to buy.", "to rise",
   *only("continue", "prices will continue to rise", "continue rise / to rising", "continue rising"), bank=["to rise", "rise", "to rising"])

# ---------- matching (1): a learning task ----------
mt(T, L, 2, "Match each beginning with its ending.",
   [("We left the beach early because it started", "raining just after lunch."),
    ("The baby on the plane woke up and began", "to cry loudly."),
    ("My grandmother is 85, but she still loves", "working in her garden every day."),
    ("When you're back, I'd love", "to see the photos from your trip.")],
   "After *start, begin, love* both *-ing* and *to* + verb are correct (*started raining = started to rain*). *would love* takes only *to*: *I'd love to see the photos.*",
   "Aiz *start, begin, love* der abas formas (*started raining = started to rain*). *would love* lieto tikai ar *to*: *I'd love to see the photos.*")
