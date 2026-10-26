"""Comparison tasks (teacher, 27 October): when a learner chooses two tenses, some questions compare them instead of testing one at a
time. Each task names the second topic in the "also topics" column; the app gives about a third of a session to such tasks when both
topics are chosen. Meaning questions have options that are all correct English with different meanings; form questions have wrong
options that are not correct in that sentence."""
from lib import *

DEF = ("Compare the two forms.", "Salīdzini abas formas.")

# ============ Past simple / Past continuous (Murphy, units 5-6) ============
PC = Topic("Past continuous", mcq=DEF, match=DEF, bank=DEF, text=DEF)
PC.mcq("A2.2", "Which sentence means the phone rang in the middle of dinner?", "We were having dinner when the phone rang.",
       ["We had dinner when the phone rang.", "We had had dinner when the phone rang."],
       ("*were having* = dinner had already started. *had dinner when* = after the call; *had had* = dinner was over.",
        "*were having* = vakariņas jau bija sākušās. *had dinner when* = pēc zvana; *had had* = vakariņas jau bija beigušās."), b=2)
also("Past simple")
PC.mcq("A2.2", "Which sentence means she started cooking after you arrived?", "When I arrived, she cooked dinner.",
       ["When I arrived, she was cooking dinner.", "When I arrived, she had cooked dinner."],
       ("Past simple after *when* = first I arrived, then she cooked. *was cooking* = she had already started.",
        "Past Simple pēc *when* = vispirms es atnācu, tad viņa gatavoja. *was cooking* = viņa jau bija sākusi."), b=4)
also("Past simple")
PC.match("B1.1", "Match each sentence with its meaning.",
         [("I was making tea when Tom came.", "Already in progress"),
          ("When Tom came, I made tea.", "Started after his arrival"),
          ("I had made tea before Tom came.", "Ready before he arrived")],
         ("*was making* = already in progress; *made* = after; *had made* = finished before.",
          "*was making* = jau notika; *made* = pēc tam; *had made* = pabeigts pirms tam."), b=4)
also("Past simple")
PC.bank("A2.2", "I ___ my leg while I ___.", ["broke", "was skiing"], ["was breaking", "breaking"],
        ("The short event: past simple (*broke*). The longer action in progress: past continuous (*was skiing*).",
         "Īsais notikums: Past Simple (*broke*). Ilgākā darbība, kas notika: Past Continuous (*was skiing*)."), b=3)
also("Past simple")
PC.text("A2.2", "Join with when: She was reading. The lights went out.",
        ["She was reading when the lights went out.", "When the lights went out, she was reading."],
        ("The longer action: *was reading*. The short event: *went out*.", "Ilgākā darbība: *was reading*. Īsais notikums: *went out*."), b=3)
also("Past simple")

# ============ Present simple / Present continuous (Murphy, units 1-4) ============
PR = Topic("Present continuous", mcq=DEF, match=DEF, bank=DEF, text=DEF)
PR.mcq("A2.1", "Which sentence is about now, not a habit?", "She's working from home today.",
       ["She works from home on Fridays.", "She usually works from home."],
       ("Now or today: present continuous. A habit: present simple.", "Tagad vai šodien: Present Continuous. Ieradums: Present Simple."), b=2)
also("Present simple")
PR.mcq("A2.1", "Which sentence is about a habit?", "I take the bus to work.",
       ["I'm taking the bus this week.", "I'm taking the bus right now."],
       ("A habit: present simple. *This week, right now*: present continuous.", "Ieradums: Present Simple. *This week, right now*: Present Continuous."), b=2)
also("Present simple")
PR.bank("A2.2", "Tom usually ___ to work, but today he ___ the bus.", ["walks", "is taking"], ["is walking", "take"],
        ("*usually* = a habit: *walks*. *today* = for now: *is taking*.", "*usually* = ieradums: *walks*. *today* = šobrīd: *is taking*."), b=3)
also("Present simple")
PR.match("A2.2", "Match each sentence with its meaning.",
         [("I live in Riga.", "This is my permanent home."),
          ("I'm living with my aunt.", "This is for a short time."),
          ("I'm moving on Saturday.", "This is a plan for the future.")],
         ("Present simple: permanent. Present continuous: for a short time, or a plan.",
          "Present Simple: pastāvīgi. Present Continuous: uz īsu laiku vai plāns."), b=4)
also("Present simple")
PR.text("A2.2", "Correct the mistake: I'm knowing the answer.", "I know the answer.",
        ("*know* is a state verb: present simple, not *-ing*.", "*know* ir stāvokļa darbības vārds: Present Simple, nevis *-ing*."), b=3)
also("Present simple")

# ============ Present perfect / Past simple (Murphy, units 7-14) ============
PP = Topic("Present perfect", mcq=DEF, match=DEF, bank=DEF, text=DEF)
PP.mcq("A2.2", "Which sentence is correct?", "I saw that film last week.",
       ["I have seen that film last week.", "I have saw that film last week."],
       ("A finished time (*last week*): past simple.", "Pabeigts laiks (*last week*): Past Simple."), b=2)
also("Past simple")
PP.mcq("A2.2", "Which sentence does not say when?", "I've lost my keys.",
       ["I lost my keys yesterday.", "I lost my keys at the station on Monday."],
       ("Present perfect: the result now, no time. Past simple: a finished time.", "Present Perfect: rezultāts tagad, bez laika. Past Simple: pabeigts laiks."), b=2)
also("Past simple")
PP.bank("B1.1", "I ___ to Paris twice, and I ___ there again last May.", ["have been", "went"], ["have gone", "been"],
        ("Experience up to now: *have been*. A finished time (*last May*): *went*.", "Pieredze līdz šim: *have been*. Pabeigts laiks (*last May*): *went*."), b=3)
also("Past simple")
PP.text("A2.2", "Correct the mistake: I have finished the report yesterday.", "I finished the report yesterday.",
        ("*yesterday* is a finished time: past simple.", "*yesterday* ir pabeigts laiks: Past Simple."), b=3)
also("Past simple")
PP.match("B1.1", "Match each sentence with its meaning.",
         [("I have lived here for ten years.", "I still live here."),
          ("I lived here for ten years.", "I don't live here now."),
          ("I have just moved here.", "The move happened a moment ago.")],
         ("*have lived* = up to now; *lived* = finished; *have just moved* = a moment ago.",
          "*have lived* = līdz šim; *lived* = beidzies; *have just moved* = tikko."), b=4)
also("Past simple")

save("contrast-1.csv")
