"""Comparing past tenses (teacher, 29 October), following Murphy, English Grammar in Use: Unit 6 (past continuous / past
simple), Units 13-14 (present perfect / past simple), Unit 15 (past perfect / past simple), Unit 16 (past perfect
continuous). The context always decides the tense: where a second tense would also be correct, the task is changed
or both are accepted. Typed gaps name the two tenses to choose from."""
from lib import *

def ex(en, lv): return (en, lv)

# ── Past simple or past continuous (Murphy, Unit 6) ──
PC_MID = ex("Past continuous: in the middle of an action at that time. Past simple: the short action that happened in the middle.",
            "Past Continuous: darbības vidū tajā brīdī. Past Simple: īsā darbība, kas notika tās vidū.")
PC_AT = ex("At a time in the past, the action had started and had not finished: past continuous.", "Kādā brīdī pagātnē darbība bija sākusies, bet nebija beigusies: Past Continuous.")
PC_SEQ = ex("One thing after another: past simple. Already going on: past continuous.", "Viens pēc otra: Past Simple. Jau notika: Past Continuous.")
PC_STATE = ex("*know, want, like* are not continuous: *We knew each other well.*", "*know, want, like* nelieto Continuous formā: *We knew each other well.*")
PC_DONE = ex("A complete action, or a repeated one: past simple.", "Pabeigta vai atkārtota darbība: Past Simple.")
I_PC = "Use the past simple or the past continuous: "
T = Topic("Past simple or past continuous", mcq_b=2, text_b=3, mcq=PC_MID, bank=PC_MID, gap=PC_MID, text=PC_MID, order=PC_MID, match=PC_MID)
T.mcq("A2.2", "They started playing at 10 and finished at 11.30. At 10.30 they ___ tennis.", "were playing", ["played", "was playing"], PC_AT)
T.mcq("A2.2", "I waved to Helen, but she ___. She didn't see me.", "wasn't looking", ["wasn't look", "weren't looking"], PC_MID)
T.mcq("B1.1", "Which sentence means 'we had already started dinner'?", "When Karen arrived, we were having dinner.", ["When Karen arrived, we had dinner.", "When Karen arrived, we have dinner."], PC_SEQ)
T.mcq("B1.1", "Which sentence means 'first she arrived, then we had dinner'?", "When Karen arrived, we had dinner.", ["When Karen arrived, we were having dinner.", "When Karen arrived, we have dinner."], PC_SEQ)
T.mcq("B1.1", "Choose the correct option: We ___ each other well. We were good friends.", "knew", ["were knowing", "was knowing"], PC_STATE)
T.gap("A2.2", I_PC + "We ___ home when I ___ Dan. (walk / meet)", "were walking / met", PC_MID)
T.gap("A2.2", I_PC + "It ___ when I ___ up this morning. (rain / get)", "was raining / got", PC_MID)
T.gap("A2.2", I_PC + "Matt ___ while we ___ dinner. We were in the middle of it. (phone / have)", "phoned / were having", PC_MID)
T.gap("A2.2", I_PC + "I ___ my back while I ___ in the garden. (hurt / work)", "hurt / was working", PC_MID)
T.gap("B1.1", I_PC + "I ___ along the road when I ___ Dan. So I stopped, and we talked. (walk / see)", "was walking / saw", PC_SEQ)
T.gap("B1.1", I_PC + "I ___ the party, but Chris ___ to go home. (enjoy / want)", "was enjoying | enjoyed / wanted", PC_STATE)   # enjoyed is right too
T.gap("B1.1", I_PC + "Kate ___ TV a lot when she was ill last year. (watch)", "watched", PC_DONE)
T.gap("B1.1", I_PC + "We ___ all the way home after the party last night. (walk)", "walked", PC_DONE)
T.order("A2.2", "she was reading when i arrived", why=PC_MID)
T.order("B1.1", "the phone rang while i was having a shower", why=PC_MID)

# ── Present perfect or past simple (Murphy, Units 13-14) ──
PP_NOW = ex("Present perfect: it tells us about the situation now. Past simple: only about the past.", "Present Perfect stāsta par situāciju tagad. Past Simple: tikai par pagātni.")
PP_FIN = ex("A finished time (*yesterday, ago, last…, When…?*): past simple.", "Pabeigts laiks (*yesterday, ago, last…, When…?*): Past Simple.")
PP_UP = ex("A time up to now (*today, this week, since…*): present perfect.", "Laiks līdz šim brīdim (*today, this week, since…*): Present Perfect.")
PP_NEWS = ex("New information: present perfect; the details after it: past simple.", "Jaunums: Present Perfect; sīkāk pēc tam: Past Simple.")
PP_OLD = ex("Not new or recent: past simple: *Mozart wrote…*", "Nav jaunums un nav nesen: Past Simple: *Mozart wrote…*")
I_PP = "Use the present perfect or the past simple: "
T = Topic("Present perfect or past simple", mcq_b=2, text_b=3, mcq=PP_NOW, bank=PP_NOW, gap=PP_NOW, text=PP_NOW, order=PP_NOW, match=PP_NOW)
T.mcq("A2.2", "Choose the correct option: Tom isn't here. He ___ to Spain.", "has gone", ["has went", "was go"], PP_NOW)
replaces("They've gone away.")
T.mcq("A2.2", "Choose the correct option: Who ___ the telephone?", "invented", ["has invented", "have invented"], PP_OLD)
T.mcq("B1.1", "Choose the correct option: I ___ a horse. Never in my life.", "have never ridden", ["have never rode", "has never ridden"], PP_UP)
T.gap("A2.2", I_PP + "It ___ very cold yesterday. (be)", "was", PP_FIN)
T.gap("A2.2", I_PP + "Paul and Lucy ___ ten minutes ago. (arrive)", "arrived", PP_FIN)
T.gap("A2.2", I_PP + "Tom ___ his key. He can't get into the house now. (lose)", "has lost", PP_NOW)
T.gap("A2.2", I_PP + "When ___ your friends ___? (arrive)", "did / arrive", PP_FIN)
T.gap("B1.1", I_PP + "I ___ here since 2010. I still work here. (work)", "have worked", PP_UP)
T.gap("B1.1", I_PP + "I ___ there from 2010 to 2014. Now I work in Riga. (work)", "worked", PP_FIN)
T.gap("B1.1", I_PP + "A: I've burnt myself. B: How ___ you ___ that? (do)", "did / do", PP_NEWS)
T.gap("B1.1", I_PP + "___ you ___ Anna yesterday? (see)", "Did / see", PP_FIN)
replaces(I_PP + "___ you ___ Anna this morning? It's four o'clock now. (see)")
T.gap("B1.1", I_PP + "___ you ___ Anna this morning? It's only ten o'clock. (see)", "Have / seen", PP_UP)
T.gap("A2.2", I_PP + "Mozart ___ more than 600 pieces of music. (write)", "wrote", PP_OLD)
T.gap("B1.1", I_PP + "It ___ this week. Everything is very dry. (not / rain)", "hasn't rained | has not rained", PP_UP)
T.order("A2.2", "have you ever eaten sushi", why=PP_UP, cue="Put the words in order to make a question.")

# ── Narrative tenses: past simple, past continuous, past perfect (Murphy, Units 6 and 15) ──
N_BEFORE = ex("The story is in the past simple; what happened before that: past perfect.", "Stāsts ir Past Simple; kas notika pirms tam: Past Perfect.")
N_BG = ex("The background, what was going on: past continuous; the events: past simple.", "Fons, kas notika apkārt: Past Continuous; notikumi: Past Simple.")
N_SIMPLE = ex("After that, or at that time: past simple. Before that: past perfect.", "Pēc tam vai tajā brīdī: Past Simple. Pirms tam: Past Perfect.")
I_N = "Use the past simple, past continuous or past perfect: "
T = Topic("Narrative tenses: past simple, past continuous, past perfect", mcq_b=2, text_b=3, mcq=N_BEFORE, bank=N_BEFORE, gap=N_BEFORE, text=N_BEFORE, order=N_BEFORE, match=N_BEFORE)
T.mcq("B1.1", "Choose the correct option: When I arrived, the film ___. I missed the beginning.", "had already started", ["has already started", "had already start"], N_BEFORE)
T.mcq("B1.2", "Which sentence means 'Paul left before Sarah came'?", "When Sarah arrived, Paul had left.", ["When Sarah arrived, Paul left.", "When Sarah arrived, Paul has left."], N_BEFORE)
T.mcq("B1.1", "Choose the correct option: I didn't recognise her. She ___ a lot.", "had changed", ["has changed", "had change"], N_BEFORE)
T.gap("B1.1", I_N + "When Sarah arrived at the party, Paul wasn't there. He ___ home. (go)", "had gone | had already gone", N_BEFORE)
T.gap("B1.1", I_N + "When we got home, we found that somebody ___ into the flat. (break)", "had broken", N_BEFORE)
T.gap("B1.1", I_N + "Karen didn't come to the cinema with us. She ___ the film. (already / see)", "had already seen", N_BEFORE)
T.gap("B1.2", I_N + "I got up and ___ out of the window. The sun ___. (look / shine)", "looked / was shining", N_BG)
T.gap("B1.2", I_N + "We weren't hungry. We ___ lunch. (just / have)", "had just had", N_BEFORE)
T.gap("B1.1", I_N + "Was Tom there when you arrived? No, he ___. (already / leave)", "had already left", N_BEFORE)
T.gap("B1.1", I_N + "Was Tom there when you arrived? Yes, but he ___ soon afterwards. (leave)", "left", N_SIMPLE)
T.gap("B1.2", I_N + "Kate wasn't at home when I phoned. She ___ at her mother's house at that moment. (be)", "was", N_SIMPLE)
T.gap("B1.2", I_N + "Kate ___ just ___ home when I phoned. (get)", "had / got", N_BEFORE)
T.gap("B1.1", I_N + "The house was dirty. They ___ it for weeks. (not / clean)", "hadn't cleaned | had not cleaned", N_BEFORE)
T.order("B1.2", "she had already left when i arrived", why=N_BEFORE)
T.order("B1.1", "it was raining when we left the house", why=N_BG)

# ── Narrative tenses with the past perfect continuous (Murphy, Unit 16) ──
P_ACT = ex("*had been* + *-ing*: an activity that went on before a moment in the past, often with a result you can see.", "*had been* + *-ing*: darbība, kas ilga pirms kāda brīža pagātnē, bieži ar redzamu rezultātu.")
P_NOW = ex("Before now: *have been -ing*. Before a moment in the past: *had been -ing*.", "Pirms tagad: *have been -ing*. Pirms kāda brīža pagātnē: *had been -ing*.")
P_COUNT = ex("How much or how many: *had done*. How long: *had been doing*.", "Cik daudz: *had done*. Cik ilgi: *had been doing*.")
P_STATE = ex("*know, have* (= own), *like* are not continuous: *We'd known each other for years.*", "*know, have* (= piederēt), *like* nelieto Continuous formā: *We'd known each other for years.*")
P_PC = ex("At that moment: *was -ing*. Before that moment: *had been -ing*.", "Tajā brīdī: *was -ing*. Pirms tā brīža: *had been -ing*.")
I_B2 = "Use a past tense or the present perfect continuous: "
T = Topic("Narrative tenses with past perfect continuous", mcq_b=2, text_b=3, mcq=P_ACT, bank=P_ACT, gap=P_ACT, text=P_ACT, order=P_ACT, match=P_ACT)
T.mcq("B2.1", "Choose the correct option: The ground was wet. It ___ in the night.", "had been raining", ["has been raining", "had been rain"], P_ACT)
T.mcq("B2.2", "Which sentence tells us what happened before the bus came?", "I'd been waiting for 20 minutes.", ["I've been waiting for 20 minutes.", "I was been waiting for 20 minutes."], P_NOW)
T.mcq("B2.2", "Choose the correct option: She was lying on the sofa. She was tired because she ___ hard.", "had been working", ["has been working", "had working"], P_ACT)
T.gap("B2.1", I_B2 + "We ___ tennis for half an hour when it started to rain. (play)", "had been playing", P_ACT)
T.gap("B2.1", I_B2 + "Tom was tired when he got home. He ___ hard all day. (work)", "had been working", P_ACT)
T.gap("B2.1", I_B2 + "By lunchtime she ___ ten emails. (write)", "had written", P_COUNT)
T.gap("B2.1", I_B2 + "James was out of breath when he came in. He ___. (run)", "had been running", P_ACT)
T.gap("B2.2", I_B2 + "At last the bus came. I ___ for twenty minutes. (wait)", "had been waiting", P_NOW)
T.gap("B2.2", I_B2 + "I hope the bus comes soon. I ___ for twenty minutes. (wait)", "have been waiting", P_NOW)
T.gap("B2.2", I_B2 + "It ___ when we went out. The sun was shining. (not / rain)", "wasn't raining | was not raining", P_PC)
T.gap("B2.2", I_B2 + "We ___ each other for years before we got married. (know)", "had known", P_STATE)
T.gap("B2.1", I_B2 + "She ___ in Madrid very long, but she knew the city well. (not / live)", "hadn't been living | had not been living | hadn't lived | had not lived", P_ACT)
T.text("B2.2", "Correct the mistake: We had been knowing each other since school.", "We had known each other since school.", P_STATE)
T.order("B2.1", "we had been driving for hours when the car broke down", why=P_ACT)
T.order("B2.2", "she had been working there for ten years when she left", why=P_ACT)

save("compare-past-1.csv")
