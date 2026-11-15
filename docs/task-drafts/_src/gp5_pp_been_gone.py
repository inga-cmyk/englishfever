"""Batch 5, point pp_been_gone (A2.2): 10 tasks to reach 10 counted tasks. Murphy unit 7."""
from lib import gp, od, mc, tx
T = "Present perfect"
L = "A2.2"

GONE = ("The person is not here now, so *gone*: *has / have gone* = went and is still there. *been* would mean they are back. After *have / has* use the 3rd form, not *went*.",
        "Cilvēks tagad nav šeit, tāpēc *gone*: *has / have gone* = aizgāja un vēl ir tur. *been* nozīmētu, ka viņš jau ir atpakaļ. Aiz *have / has* lieto 3. formu, nevis *went*.")
BEEN = ("The person is back (or is here and speaking), so *been*: *have / has been to* = went and came back. *gone* would mean they are still there. After *have / has* use the 3rd form, not *went*.",
        "Cilvēks ir atpakaļ (vai ir šeit un runā), tāpēc *been*: *have / has been to* = aizgāja un atgriezās. *gone* nozīmētu, ka viņš vēl ir tur. Aiz *have / has* lieto 3. formu, nevis *went*.")

# choose (3)
mc(T, L, 2, "Choose the correct option: The office is empty. Everyone ___ home.", "has gone", ["has been", "has went"], *GONE)
mc(T, L, 2, "Choose the correct option: I've ___ to the gym. I feel great now.", "been", ["gone", "went"], *BEEN)
mc(T, L, 2, "Which sentence has a mistake?", "My parents have gone to Italy twice.",
   ["Have you ever been to a jazz concert?", "Ivo has gone home. He felt ill.", "I haven't seen my cousin this year."],
   "Visits that are over can be counted (*twice, three times*): *My parents have been to Italy twice.* *gone* means they are still there, so it cannot happen twice.",
   "Apmeklējumus, kas jau beigušies, var saskaitīt (*twice, three times*): *My parents have been to Italy twice.* *gone* nozīmē, ka viņi vēl ir tur, tāpēc ar *twice* jālieto *been*.")
# typed gap (2)
gp(T, L, 3, "Write *been* or *gone*: We have ___ to the cinema twice this month.", "been",
   "*twice* counts visits that are over: we went and came back, so *been*.",
   "*twice* norāda uz apmeklējumiem, kas jau beigušies: aizgājām un atgriezāmies, tāpēc *been*.")
gp(T, L, 3, "Write *been* or *gone*: Dan's ___ to a football match. He'll be back at ten.", "gone",
   "He is not back yet (*He'll be back at ten*), so he is still at the match: *gone*.",
   "Viņš vēl nav atpakaļ (*He'll be back at ten*), tātad viņš vēl ir mačā: *gone*.")
# word bank (4): the wrong chips are the other participle and the learner mistake went
gp(T, L, 3, "Where's Oskars? He ___ ___ to the airport to meet his parents.", "has / gone", *GONE, bank=["has", "gone", "been", "went"])
gp(T, L, 3, "Your car looks so clean! Have you ___ to the car wash?", "been", *BEEN, bank=["been", "gone", "went"])
gp(T, L, 3, "I can't call Lena now. She's ___ to bed.", "gone", *GONE, bank=["gone", "been", "went"])
gp(T, L, 3, "Our friends are back from their holiday. They ___ ___ to Greece.", "have / been", *BEEN, bank=["have", "been", "gone", "went"])
# whole sentence (1)
tx(T, L, 4, "Start with *Rita has* and use *go*: Rita went to Tokyo, and she is still there.",
   "Rita has gone to Tokyo. | Rita has gone to Tokyo, and she is still there. | Rita has gone to Tokyo and is still there.",
   "She went and is still there: *has gone to*. *has been to* would mean she is back.",
   "Viņa aizgāja un vēl ir tur: *has gone to*. *has been to* nozīmētu, ka viņa ir atpakaļ.")
