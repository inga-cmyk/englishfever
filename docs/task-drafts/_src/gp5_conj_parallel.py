"""Batch 5, point conj_parallel (A2.2): 7 tasks to reach 10 counted tasks. Murphy unit: none (the map says not a Murphy EGiU unit; the rule is the card's "Join the same kind of words" and "No need to say the subject again")."""
from lib import gp, od, mc, tx
T = "And, but, or, so, because"
L = "A2.2"

ING = ("After *and* / *or* use the same form as before it: *swimming and cycling*, *-ing and -ing*.",
       "Aiz *and* / *or* lieto to pašu formu, kas ir pirms tā, piemēram, *swimming and cycling*.")
SUBJ = ("With *and* we need not say the subject again, but the second verb has the same form as the first: *I have breakfast and read the news*, *we visited … and worked*.",
        "Ar *and* teikuma priekšmetu var neatkārtot, bet otrais darbības vārds ir tādā pašā formā kā pirmais: *I have breakfast and read the news*. Arī *we visited … and worked*.")

# choice (2)
mc(T, L, 2, "Choose the correct option: My sister loves swimming and ___.", "cycling", ["cycle", "to cycle"], *ING)
mc(T, L, 2, "Which sentence has a mistake?", "I usually have breakfast and reading the news.",
   ["It was raining, so we took a taxi home.", "I'm tired today because I slept badly.", "Is the meeting today or tomorrow morning?"], *SUBJ)

# word bank (2): the wrong chips are real forms of the same verb that do not fit after this and / or
gp(T, L, 3, "Would you like to stay in tonight or ___ out?", "go",
   "*would like to stay in or go out*: after *or* the same form as before it (*to*) *stay* → *go*; *to* need not be repeated. Not *going*.",
   "*would like to stay in or go out*: aiz *or* tā pati forma kā pirms tā: *stay*, tātad *go*. *to* var neatkārtot. Nevis *going*.",
   bank=["go", "going", "went"])
gp(T, L, 3, "On Saturday we visited my parents and ___ in their garden.", "worked", *SUBJ, bank=["worked", "working", "work"])

# typed gap (2)
gp(T, L, 3, "Thanks for coming and ___ me with the move. (help)", "helping",
   "After *for* the verb takes *-ing*, and after *and* the same form again: *for coming and helping*.",
   "Aiz *for* darbības vārds ir ar *-ing*, un aiz *and* jālieto tā pati forma: *for coming and helping*.")
gp(T, L, 3, "The best parts of my job are meeting people and ___. (travel)", "travelling | traveling", *ING)

# whole sentence (1)
tx(T, L, 4, "Correct the mistake: She closed her laptop and go home.",
   "She closed her laptop and went home. | She closed her laptop and she went home. | She closes her laptop and goes home. | She closes her laptop and she goes home.",
   "Both verbs after *she* have the same form: *closed … and went* (or *closes … and goes*). The subject need not be repeated after *and*.",
   "Abos darbības vārdos ir tā pati forma: *closed … and went* (vai *closes … and goes*). Aiz *and* teikuma priekšmetu var neatkārtot.")
