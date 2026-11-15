"""Batch 5, point ps_pc (A2.1): 6 tasks to reach 10 counted tasks. Murphy unit 3.
Murphy 3 (I do and I am doing): the present simple for things that happen in general or repeatedly (usually, never, every day),
the present continuous for something happening now (Look!, at the moment, right now). In every task the signal word or the
short situation decides, and the wrong option of the other form competes. No sentence with a temporary situation (this week,
these days) or a plan: those are pc_temp (A2.2) and the future."""
from lib import gp, od, mc, tx
T = "Present continuous"
S = "Present simple"   # the one task whose answer is the habit form
L = "A2.1"

# choice (2)
mc(S, L, 2, "Choose the correct option: What time ___ you usually finish work?", "do", ["are", "—"],
   "*usually* shows a habit, so the present simple: *What time do you usually finish work?* *Are you finishing* is about now or a plan; without *do* the question is not correct.",
   "*usually* norāda uz ieradumu, tāpēc Present Simple: *What time do you usually finish work?* *Are you finishing* ir par tagadni vai plānu; bez *do* jautājums ir kļūdains.")
mc(T, L, 2, "Which sentence has a mistake?", "Look! Our bus comes round the corner.",
   ["We usually have dinner at seven.", "My brother is sleeping at the moment.", "Does your shop open on Sundays?"],
   "*Look!* shows it is happening now: *Look! Our bus is coming round the corner.* The other three are correct: a habit, an action now, a question about a regular time.",
   "*Look!* norāda, ka tas notiek tagad: *Look! Our bus is coming round the corner.* Pārējie trīs teikumi ir bez kļūdām: ieradums, darbība tagad, jautājums par regulāru laiku. Tulkojot burtiski, latviešu tagadne dod *Our bus comes*; angļu valodā tagad notiekošam vajag *is coming*.")
# word order (1): usually goes with the simple form, today with the continuous one
od(T, L, 3, "Put the words in order.", "she usually swims but today she is running",
   "*usually* + present simple (*she usually swims*), *today* + present continuous (*today she is running*).",
   "*usually* + Present Simple (*she usually swims*), *today* + Present Continuous (*today she is running*).",
   also=["usually she swims but today she is running", "she usually swims but she is running today",
         "today she is running but she usually swims", "she is running today but she usually swims",
         "today she is running but usually she swims"])   # r13: a reader's order, correct English
# word bank (1)
gp(T, L, 3, "Can I call you back? I ___ dinner.", "am having",
   "The person is eating dinner at this moment, so *I am having dinner*. *I have dinner* is a habit (*I have dinner at seven*).",
   "Cilvēks šobrīd ēd vakariņas, tāpēc *I am having dinner*. *I have dinner* ir ieradums (*I have dinner at seven*).",
   bank=["am having", "have", "had"])
# typed gap (1): two gaps, now and a habit
gp(T, L, 3, "Look! Dad ___ the dishes. He never ___ that! (wash / do)", "is washing | 's washing / does",
   "*Look!*: happening now, *is washing*. *never*: a habit, present simple with *he*: *does*.",
   "*Look!*: notiek tagad, *is washing*. *never*: ieradums, Present Simple ar *he*: *does*.")
# whole sentence (1)
tx(T, L, 4, "Rewrite the sentence about this moment. Start with *Right now*: My sister reads the news on her phone.",
   "Right now my sister is reading the news on her phone. | Right now my sister's reading the news on her phone.",
   "*Right now*: an action in progress, *is reading*. *She reads the news* is a habit.",
   "*Right now*: darbība norisinās, *is reading*. *She reads the news* ir ieradums.")
