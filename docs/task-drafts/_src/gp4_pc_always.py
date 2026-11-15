"""Batch 4, point pc_always (B1.2): always / constantly / forever + continuous for an annoying habit. Murphy unit 3.
Murphy 3: *I'm always losing things* = it happens too often, and the speaker is annoyed; *I always lose* is correct but neutral.
So the simple form is never a wrong option: the choices test the form (*is always losing*, not *always is losing / is always lose /
always losing*), the position of *always* (between *be* and *-ing*), the agreement and the past (*was always complaining*).
The meaning (which sentence complains) is only tested in learning tasks. Typed tasks accept the simple form wherever it is correct,
unless the instruction asks for the complaint (*Complain with *always*:*)."""
from lib import gp, od, mc, tx, mt, learning_task
T = "Present continuous"
L = "B1.2"

FORM = ("A complaint about a habit: *am / is / are* + *always* + verb-ing: *He's always losing his keys!*",
        "Īgnums par ieradumu: *am / is / are* + *always* + darbības vārds ar *-ing*: *He's always losing his keys!*")
POS = ("*always* goes between *am / is / are* and the verb-ing: *They're always arguing*, not *always are arguing*.",
       "*always* liek starp *am / is / are* un darbības vārdu ar *-ing*: *They're always arguing*, nevis *always are arguing*.")
PAST = ("About the past: *was / were* + *always* + verb-ing: *She was always complaining.*",
        "Par pagātni: *was / were* + *always* + darbības vārds ar *-ing*: *She was always complaining.*")
CONST = ("*constantly* and *forever* work like *always*: *is constantly* / *is forever* + verb-ing.",
         "*constantly* un *forever* lieto tāpat kā *always*: *is constantly* / *is forever* + darbības vārds ar *-ing*.")

# choose (7). Murphy 3: the simple form (always borrows) is correct English, so it is never a wrong option.
mc(T, L, 2, "Choose the correct option: My flatmate ___ my phone charger without asking, and it drives me mad.", "is always borrowing",
   ["always is borrowing", "is always borrow", "always borrowing"],
   "*is* + *always* + verb-ing: *is always borrowing*. *always* goes after *is*, and the verb needs *-ing*.",
   "*is* + *always* + darbības vārds ar *-ing*: *is always borrowing*. *always* liek aiz *is*, un darbības vārdam vajag *-ing*.")
mc(T, L, 2, "Which sentence is correct?", "My neighbours are always parking in front of our garage, so I can't get out.",
   ["My neighbours always are parking in front of our garage, so I can't get out.",
    "My neighbours are always park in front of our garage, so I can't get out.",
    "My neighbours are parking always in front of our garage, so I can't get out."], *POS)
mc(T, L, 2, "Choose the correct option: When we worked together, Lisa ___ about the air conditioning.", "was always complaining",
   ["always was complaining", "was always complain", "is always complaining"],
   "*When we worked together* is the past, so *was* + *always* + verb-ing: *Lisa was always complaining.*",
   "*When we worked together* ir pagātne, tāpēc *was* + *always* + darbības vārds ar *-ing*: *Lisa was always complaining.*")
mc(T, L, 2, "Which sentence is NOT correct?", "My dad is always lose his glasses somewhere in the house.",
   ["She's always checking her phone when we're having dinner.", "They were always arguing about money when they were married.",
    "My brother always forgets my birthday, but he calls the next day."],
   "After *is always* the verb needs *-ing*: *My dad is always losing his glasses.* *My brother always forgets* is correct too: it is neutral, without the complaint.",
   "Aiz *is always* darbības vārdam vajag *-ing*: *My dad is always losing his glasses.* Arī *My brother always forgets* ir pareizi: tas ir neitrāli, bez īgnuma.")
mc(T, L, 2, "Choose the correct option: My teenage sons ___ always leaving wet towels on the bathroom floor, and I'm tired of it.", "are",
   ["do", "have", "is"],
   "*sons* = *they*, so *are*: *are always leaving*. The continuous needs *be*, not *do* or *have*.",
   "*sons* = *they*, tāpēc *are*: *are always leaving*. Continuous formai vajag *be*, nevis *do* vai *have*.")
mc(T, L, 2, "Choose the correct option: My manager is constantly ___ us emails late at night, even at weekends.", "sending",
   ["send", "sends", "sent"], *CONST)
# meaning: a learning task (Content::role = learn), as the lead asked
mc(T, L, 2, "Which sentence is a complaint?", "My partner is always leaving the lights on.",
   ["My partner is leaving the office now.", "My partner leaves for work at seven.", "My partner is going to leave early tomorrow."],
   "*is always* + verb-ing says that something happens too often and annoys the speaker. The other sentences only give facts or plans.",
   "*is always* + darbības vārds ar *-ing* saka, ka kaut kas notiek pārāk bieži un runātāju kaitina. Pārējie teikumi tikai min faktus vai plānus.")
learning_task()

# type a word (5)
gp(T, L, 3, "Complain with *always*: My flatmates ___ (leave) their muddy shoes in the hall and never clean up.",
   "are always leaving | 're always leaving", *FORM)
gp(T, L, 3, "Complain with *always*: When we shared an office, Mark ___ (hum) along to his music.", "was always humming | would always hum | 'd always hum", *PAST)   # would + always is a correct annoyed past habit too: accepted
gp(T, L, 3, "Complete with one word in each gap: We need a new printer: ours ___ always ___ in the middle of big jobs. (jam)", "is / jamming", *POS)
gp(T, L, 3, "Complete with one word in each gap: My old car ___ constantly ___ down, so in the end I sold it. (break)", "was / breaking",
   "*so in the end I sold it* is the past, so *was* + *constantly* + verb-ing: *was constantly breaking down*.",
   "*so in the end I sold it* ir pagātne, tāpēc *was* + *constantly* + darbības vārds ar *-ing*: *was constantly breaking down*.")
# both forms are correct here: the simple form is neutral, the continuous adds the complaint
gp(T, L, 3, "Use the words in brackets: My brother ___ (always / forget) my birthday, but every year he calls the next day.",
   "always forgets | is always forgetting | 's always forgetting",
   "*always forgets* (neutral) or *is always forgetting* (a complaint): both are correct. *always* goes before *forgets*, or after *is*.",
   "*always forgets* (neitrāli) vai *is always forgetting* (īgnums): abi ir pareizi. *always* liek pirms *forgets* vai aiz *is*.")

# whole sentence (3)
tx(T, L, 4, "Complain with *constantly*: My boss calls me during my lunch break.",
   "My boss is constantly calling me during my lunch break. | My boss's constantly calling me during my lunch break.", *CONST)
tx(T, L, 4, "Complain with *always*: When we were students, my flatmate borrowed my notes.",
   "When we were students, my flatmate was always borrowing my notes. | My flatmate was always borrowing my notes when we were students. | When we were students, my flatmate would always borrow my notes. | My flatmate would always borrow my notes when we were students. | When we were students, my flatmate'd always borrow my notes.", *PAST)
tx(T, L, 4, "Make a question with *Why*: You're always interrupting me in meetings.",
   "Why are you always interrupting me in meetings? | Why do you always interrupt me in meetings? | Why are you always interrupting me? | Why do you always interrupt me?",
   "*Why are you always interrupting me?*: *are* goes before *you*, *always* stays before the verb-ing. *Why do you always interrupt me?* is correct too.",
   "*Why are you always interrupting me?*: *are* liek pirms *you*, *always* paliek pirms darbības vārda ar *-ing*. Arī *Why do you always interrupt me?* ir pareizi.")

# word order (5): subjects with a contraction, so the cards do not also make a yes/no question
od(T, L, 3, "Put the words in order.", "my sister's always borrowing my clothes without asking", *POS)
od(T, L, 3, "Put the words in order.", "it's always raining when i want to go cycling", *POS, also=["when i want to go cycling it's always raining"])
od(T, L, 3, "Put the words in order to make a question.", "why are you always checking your phone at dinner",
   "A question: *Why* + *are* + *you* + *always* + verb-ing.", "Jautājums: *Why* + *are* + *you* + *always* + darbības vārds ar *-ing*.")
od(T, L, 3, "Put the words in order.", "he's forever telling us how busy he is", *CONST)
od(T, L, 3, "Put the words in order.", "you're always making plans for the weekend without telling me", *POS)

# word bank (4): the wrong chips are real forms (takes, does, is, drop, have, ask, reminds, has) that do not fit here
gp(T, L, 3, "My colleague ___ ___ ___ my yoghurt from the office fridge, and it drives me mad.", "is / always / taking", *POS,
   bank=["is", "always", "taking", "takes", "does"])
gp(T, L, 3, "When I was a student, my landlord ___ always ___ round without calling first.", "was / dropping", *PAST,
   bank=["was", "dropping", "is", "drop"])
gp(T, L, 3, "My parents ___ always ___ me when I'm going to find a better job.", "are / asking", *FORM,
   bank=["are", "asking", "have", "ask"])
gp(T, L, 3, "My phone ___ constantly ___ me to update my apps, and I keep ignoring it.", "is / reminding", *CONST,
   bank=["is", "reminding", "reminds", "has"])

# matching (1): a learning task; the verb is in the beginning and its object in the ending
mt(T, L, 2, "Match each beginning with its ending.",
   [("My flatmate is always leaving", "the front door unlocked."), ("Our manager is constantly changing", "the meeting times."),
    ("My cousin is forever borrowing", "my phone charger."), ("The neighbours' dogs are always barking", "at the postman.")],
   "*always / constantly / forever* + verb-ing complains about something that happens too often.",
   "*always / constantly / forever* + darbības vārds ar *-ing* izsaka īgnumu par to, kas notiek pārāk bieži.")
