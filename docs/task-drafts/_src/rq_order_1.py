"""Word order in reported and indirect questions (teacher, 14 November): the learner must make the word order, not only one verb.
Every scene gives four tasks with slightly different sentences: typed (the start up to the question word: She asked me where …),
a word bank with the subject and a helping verb (I · lived · did · live), a choice of word orders (I lived / did I live …) and the
whole sentence in order. The old tasks where only one verb is put in are learning tasks now (rq_learning in _src/draft_fixes).
Reported questions follow the taught rule: one step back in time (teacher, 11 November). Indirect questions keep the tense."""
from lib import rows, save, gp, od, mc, tx, learning_task

RQ = "Reported questions and requests"
IQ = "Indirect questions (Could you tell me where...)"
R_EN = ("In a reported question the word order is like a statement: subject + verb (*where I lived*), with no *do / does / did*, and the verb goes one step back.",
        "Atstāstītā jautājumā vārdu secība ir kā apgalvojumā: teikuma priekšmets + darbības vārds (*where I lived*), bez *do / does / did*, un laiks pāriet vienu soli atpakaļ.")
R_YN = ("A reported yes/no question: *if* + subject + verb, one step back in time (*if I had finished*), not *if had I finished*.",
        "Atstāstīts jautājums ar atbildi jā / nē: *if* + teikuma priekšmets + darbības vārds, laiks soli atpakaļ (*if I had finished*), nevis *if had I finished*.")
I_EN = ("Inside *Do you know…? / Could you tell me…?* the word order is like a statement: *where Anna lives*, with no *does*; the tense stays.",
        "Pēc *Do you know…? / Could you tell me…?* vārdu secība ir kā apgalvojumā: *where Anna lives*, bez *does*; laiks nemainās.")
I_YN = ("A yes/no question inside *Do you know…?*: *if* + subject + verb: *if there is*, not *if is there*.",
        "Jautājums ar atbildi jā / nē pēc *Do you know…?*: *if* + teikuma priekšmets + darbības vārds: *if there is*, nevis *if is there*.")
F = "Finish the sentence: "


def typed(t, lv, quote, start, conts, why):
    """The quote on the first line, then 'Finish the sentence: start …'; the continuation or the whole sentence is accepted."""
    ans = []
    for c in conts:
        for a in (f"{start} {c}.", f"{c}."):
            if a not in ans: ans.append(a)
    tx(t, lv, 3, f"'{quote}'\n{F}{start} …", " | ".join(ans), *why)


def order(t, lv, quote, sentence, why, question=False, also=None):
    """Only 'Put the words in order.': the direct question is not shown in a word-order task (teacher, 14 November)."""
    od(t, lv, 3, "Put the words in order" + (" to make a question." if question else "."), sentence, *why, also=also)


# ---- reported questions (B1.2; how long B2.1) ----
L = "B1.2"
typed(RQ, L, "Where do you live?", "She asked me where", ["I lived"], R_EN)
gp(RQ, L, 3, "'Where do you work?'\nHe asked me where ___ ___ .", "I / worked", *R_EN, bank=["I", "worked", "did", "work"])
mc(RQ, L, 2, "'Where do you study?'\nChoose the correct option: She asked him where ___.", "he studied", ["did he study", "does he study", "he did study"], *R_EN)
order(RQ, L, "Where is your office?", "she asked me where my office was", R_EN)

typed(RQ, L, "What time does the film start?", "He asked what time", ["the film started"], R_EN)
gp(RQ, L, 3, "'What time does the train leave?'\nShe asked me what time ___ ___ .", "the train / left", *R_EN, bank=["the train", "left", "did", "leave"])
mc(RQ, L, 2, "'What time does the shop close?'\nChoose the correct option: He asked what time ___.", "the shop closed", ["did the shop close", "does the shop close", "the shop did close"], *R_EN)
order(RQ, L, "What time does the bus arrive?", "she asked me what time the bus arrived", R_EN)   # an everyday situation, no extra usually (teacher, 14 November)

typed(RQ, L, "Have you finished?", "He asked me if", ["I had finished", "I'd finished"], R_YN)
gp(RQ, L, 3, "'Have you eaten?'\nShe asked me if ___ ___ ___ .", "I / had / eaten", *R_YN, bank=["I", "had", "eaten", "did", "eat"])
mc(RQ, L, 2, "'Have you seen the film?'\nChoose the correct option: He asked me if ___ the film.", "I had seen", ["had I seen", "did I see", "I did see"], *R_YN)
order(RQ, L, "Has the parcel arrived?", "she asked if the parcel had arrived", R_YN)

typed(RQ, L, "Can you help me?", "She asked me if", ["I could help her", "I could help"], R_YN)
gp(RQ, L, 3, "'Can you drive?'\nHe asked me if ___ ___ drive.", "I / could", *R_YN, bank=["I", "could", "can"])
mc(RQ, L, 2, "'Can you swim?'\nChoose the correct option: She asked me if ___.", "I could swim", ["could I swim", "can I swim", "I could to swim"], *R_YN)
order(RQ, L, "Can the shop deliver on Sunday?", "he asked if the shop could deliver on sunday", R_YN, also=["he asked on sunday if the shop could deliver", "on sunday he asked if the shop could deliver"])

typed(RQ, L, "Where is the manager?", "She asked where", ["the manager was"], R_EN)
gp(RQ, L, 3, "'Where is the station?'\nHe asked me where ___ ___ .", "the station / was", *R_EN, bank=["the station", "was", "did"])
mc(RQ, L, 2, "'Where is the lift?'\nChoose the correct option: He asked where ___.", "the lift was", ["was the lift", "is the lift"], *R_EN)
order(RQ, L, "Where are my keys?", "she asked where her keys were", R_EN)

typed(RQ, "B2.1", "How long have you been learning English?", "She asked me how long", ["I had been learning English", "I'd been learning English"], R_EN)
gp(RQ, "B2.1", 3, "'How long have you lived here?'\nHe asked me how long ___ ___ ___ there.", "I / had / lived", *R_EN, bank=["I", "had", "lived", "have"])
mc(RQ, "B2.1", 2, "'How long have you worked here?'\nChoose the correct option: She asked how long ___ there.", "I had worked", ["had I worked", "have I worked", "did I work"], *R_EN)
order(RQ, "B2.1", "How long has the shop been open?", "she asked how long the shop had been open", R_EN)

typed(RQ, L, "Why are you late?", "The teacher asked us why", ["we were late"], R_EN)
gp(RQ, L, 3, "'Why is he angry?'\nShe asked me why ___ ___ angry.", "he / was", *R_EN, bank=["he", "was", "did"])
mc(RQ, L, 2, "'Why are you tired?'\nChoose the correct option: He asked me why ___ tired.", "I was", ["was I", "am I", "did I"], *R_EN)
order(RQ, L, "Why is the shop closed?", "he asked why the shop was closed", R_EN)

# ---- indirect questions (B1.1, B1.2): the tense stays ----
# 21 November (teacher: too easy, the answer is given away; gp6_iq_b1-notes.md): the direct question is quoted and the frame is given,
# so only two words change places. Practice only now; the word order about 'Is there a café' stays a check. New checks: gp6_iq_b1.py.
L = "B1.1"
typed(IQ, L, "Where does Anna live?", "Do you know where", ["Anna lives"], I_EN); learning_task()
gp(IQ, L, 3, "'Where does Tom work?'\nDo you know where ___ ___ ?", "Tom / works", *I_EN, bank=["Tom", "works", "does", "work"]); learning_task()
mc(IQ, L, 2, "'Where does your teacher live?'\nChoose the correct option: Do you know where ___?", "your teacher lives", ["does your teacher live", "your teacher does live", "lives your teacher"], *I_EN); learning_task()
order(IQ, L, "Where does Mark work?", "do you know where mark works", I_EN, question=True); learning_task()

typed(IQ, L, "What time does the bus leave?", "Could you tell me what time", ["the bus leaves"], I_EN); learning_task()
gp(IQ, L, 3, "'What time does the museum open?'\nCould you tell me what time ___ ___ ?", "the museum / opens", *I_EN, bank=["the museum", "opens", "does", "open"]); learning_task()
mc(IQ, L, 2, "'What time does the concert start?'\nChoose the correct option: Do you know what time ___?", "the concert starts", ["does the concert start", "the concert does start", "starts the concert"], *I_EN); learning_task()
order(IQ, L, "What time does the bank close?", "could you tell me what time the bank closes", I_EN, question=True); learning_task()

L = "B1.2"
typed(IQ, L, "How much is this jacket?", "Could you tell me how much", ["this jacket is", "this jacket costs", "it is", "it costs"], I_EN); learning_task()
gp(IQ, L, 3, "'How much does this lamp cost?'\nI'd like to know how much ___ ___ .", "this lamp / costs", *I_EN, bank=["this lamp", "costs", "does", "cost"]); learning_task()
mc(IQ, L, 2, "'How much is the ticket?'\nChoose the correct option: Can you tell me how much ___?", "the ticket is", ["is the ticket", "does the ticket cost"], *I_EN); learning_task()
order(IQ, L, "How much are the tickets?", "do you know how much the tickets are", I_EN, question=True); learning_task()

typed(IQ, L, "Is there a pharmacy near here?", "Can you tell me if", ["there is a pharmacy near here", "there's a pharmacy near here"], I_YN); learning_task()
gp(IQ, L, 3, "'Is there a bank near here?'\nDo you know if ___ ___ a bank near here?", "there / is", *I_YN, bank=["there", "is", "are"]); learning_task()
mc(IQ, L, 2, "'Is there a lift in this building?'\nChoose the correct option: Do you know if ___ a lift in this building?", "there is", ["is there", "there are"], *I_YN); learning_task()
order(IQ, L, "Is there a café near the station?", "do you know if there is a café near the station", I_YN, question=True)

typed(IQ, L, "Where is the post office?", "Do you know where", ["the post office is"], I_EN); learning_task()
gp(IQ, L, 3, "'Where is the toilet?'\nCould you tell me where ___ ___ ?", "the toilet / is", *I_EN, bank=["the toilet", "is", "does"]); learning_task()
mc(IQ, L, 2, "'Where is the library?'\nChoose the correct option: Can you tell me where ___?", "the library is", ["is the library", "is there the library"], *I_EN); learning_task()
order(IQ, L, "Where is the car park?", "do you know where the car park is", I_EN, question=True); learning_task()

save("rq-order-1.csv")
