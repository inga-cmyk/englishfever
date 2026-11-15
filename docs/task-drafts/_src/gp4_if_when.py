"""Batch 4, point if_when (B1.1): if or when about the future. Murphy unit 25 (C: when = I'm sure it will happen,
if = it is possible, it may happen; A-B: when / if + present simple for the future, not will).
Every choice between if and when has one short sentence that makes the event sure (a timetable, a plan, a date) or
not sure (might, may, perhaps, not sure): without it both are correct English, so the situation is the task.
No 'when' for something that happens every time (zero conditional): every event here is one future event.
The word orders give only one of if / when, so they practise the form (no will after if / when) and the clause order."""
from lib import gp, od, mc, tx, mt, learning_task, replaces
T = "First conditional (if + present, will)"
L = "B1.1"

SURE = ("*when* = we are sure it will happen; *if* = it may happen. After both, the present simple for the future, not *will*.",
        "*when* = esam droši, ka tas notiks; *if* = varbūt notiks. Aiz abiem nākotnei lieto Present Simple, nevis *will*.")
NOWILL = ("After *when* and *if*, use the present simple for the future, not *will*: *when I land*, not *when I will land*.",
          "Tulkojot burtiski *kad nolaidīšos*, gribas lietot *will*. Angliski aiz *when* un *if* nākotnei lieto Present Simple: *when I land*.")
ORD_WHEN = ("*when* + present simple, *will* in the other part. The *when*-part can come first (with a comma) or second.",
            "*when* + Present Simple, *will* otrā daļā. *when* daļa var būt pirmā (ar komatu) vai otrā.")
ORD_IF = ("*if* + present simple, *will* in the other part. The *if*-part can come first (with a comma) or second.",
          "*if* + Present Simple, *will* otrā daļā. *if* daļa var būt pirmā (ar komatu) vai otrā.")
ORD_Q = ("In the question *will* goes before *you*; the *when*-part keeps the present simple and can come first or second.",
         "Jautājumā *will* stāv pirms *you*. Daļā ar *when* paliek Present Simple, un tā var būt pirmā vai otrā.")

# ── choose (7) ──
# c1 travel, sure: a timetable
mc(T, L, 2, "Choose the correct option: My train gets in at six. ___, I'll call you from the station.", "When I arrive",
   ["If I arrive", "When I will arrive", "If I will arrive"],
   "The train time is fixed, so the arrival is sure: *when*. After *when*, the present simple: *When I arrive*, not *When I will arrive*.",
   "Vilciena laiks ir zināms, tātad ierašanās ir droša: *when*. Aiz *when* lieto Present Simple: *When I arrive*, nevis *When I will arrive*.")
# c2 work, not sure: may not
mc(T, L, 2, "Choose the correct option: I may not get the job, but ___, I'll move to Oslo.", "if I get it",
   ["when I get it", "if I'll get it", "when I'll get it"],
   "*I may not get the job*: it is not sure, so *if*. *when* would mean you are sure. After *if*, the present simple: *if I get it*.",
   "*I may not get the job*: tas nav droši, tāpēc *if*. *when* nozīmētu, ka esi drošs. Aiz *if* lieto Present Simple: *if I get it*.")
# c3 hobbies, sure: the film ends at nine
mc(T, L, 2, "Which sentence is correct?", "The film ends at nine, so I'll call you when it finishes.",
   ["The film ends at nine, so I'll call you if it finishes.", "The film ends at nine, so I'll call you when it will finish.",
    "The film ends at nine, so I'll call you if it will finish."],
   "The film surely ends, so *when*, and after *when* the present simple: *when it finishes*.",
   "Filma noteikti beigsies, tāpēc *when*, un aiz *when* lieto Present Simple: *when it finishes*.")
# c4 relationships, not sure: might
mc(T, L, 2, "Choose the correct option: My brother might visit us next month. ___, we'll take him to the new museum.", "If he comes",
   ["When he comes", "If he will come", "When he will come"],
   "*might visit*: the visit is not sure, so *if*. After *if*, the present simple: *If he comes*.",
   "*might visit*: ciemošanās nav droša, tāpēc *if*. Aiz *if* lieto Present Simple: *If he comes*.")
# c5 mixed: no will after when (the other three: weather / a trip next week / help with the move)
mc(T, L, 2, "Which sentence is NOT correct?", "I'll text you when I will land in Riga.",
   ["If the weather is nice tomorrow, we'll go for a walk.", "When I'm in London next week, I'll visit the new gallery.",
    "If you need help with the move, just call me."], *NOWILL)
# c6 lifestyle, sure: a wedding date
mc(T, L, 2, "Choose the correct option: We're getting married in June. ___ married, we'll look for a bigger flat.", "When we're",
   ["If we're", "When we'll be", "If we'll be"],
   "The wedding is planned, so it is sure: *when*. After *when*, the present simple: *When we're married*, not *When we'll be married*.",
   "Kāzas ir ieplānotas, tātad tas ir droši: *when*. Aiz *when* lieto Present Simple: *When we're married*, nevis *When we'll be married*.")
# c7 travel, not sure (the sentence after it decides)
mc(T, L, 2, "Choose the correct option: ___ my visa in time, I'll fly to Toronto in May. It's not certain yet.", "If I get",
   ["When I get", "If I'll get", "When I'll get"],
   "*It's not certain yet*, so *if*. After *if*, the present simple: *If I get my visa*.",
   "*It's not certain yet*: tas vēl nav droši, tāpēc *if*. Aiz *if* lieto Present Simple: *If I get my visa*.")

# ── type a word (5) ──
gp(T, L, 3, "Write *if* or *when*: I'm having lunch with Tom today. ___ I see him, I'll give him your book.", "When",
   "Lunch with Tom is planned, so you are sure to see him: *when*.",
   "Pusdienas ar Tomu ir norunātas, tātad viņu noteikti satiksi: *when*.")
gp(T, L, 3, "When the update ___, the app will restart by itself. (finish)", "finishes | has finished | 's finished | is finished",
   "After *when*, the present simple (or the present perfect) for the future, not *will*: *When the update finishes*.",
   "Aiz *when* nākotnei lieto Present Simple (vai Present Perfect), nevis *will*: *When the update finishes*.")
gp(T, L, 3, "Write *if* or *when*: The bank might be closed on Saturday. ___ it is, I'll go on Monday.", "If",
   "*might be closed*: it is not sure, so *if*.",
   "*might be closed*: tas nav droši, tāpēc *if*.")
gp(T, L, 3, "My course begins on Monday. When it ___, I'll have less free time. (start)", "starts | has started | 's started | begins | has begun",
   "After *when*, the present simple for the future: *When it starts*, not *When it will start*.",
   "Aiz *when* nākotnei lieto Present Simple: *When it starts*, nevis *When it will start*.")
replaces("My course starts on Monday. When it ___, I'll have less free time. (start)")   # tester, 15 November: the answer was in the first sentence
gp(T, L, 3, "Write *if* or *when*: The museum opens at ten. ___ it opens, we'll buy tickets for the tower.", "When",
   "The opening time is fixed, so it is sure: *when*.",
   "Atvēršanas laiks ir zināms, tātad tas ir droši: *when*.")

# ── whole sentence (3) ──
tx(T, L, 4, "Join with *if* or *when*: My contract ends in June. Then I'll take a long holiday.",
   "When my contract ends in June, I'll take a long holiday. | When my contract ends in June, I will take a long holiday. | "
   "When my contract ends, I'll take a long holiday. | When my contract ends, I will take a long holiday. | "
   "I'll take a long holiday when my contract ends in June. | I will take a long holiday when my contract ends in June. | "
   "I'll take a long holiday when my contract ends. | I will take a long holiday when my contract ends. | "
   "In June, when my contract ends, I'll take a long holiday. | In June, when my contract ends, I will take a long holiday. | "
   "I'll take a long holiday in June, when my contract ends. | I will take a long holiday in June, when my contract ends. | "
   "When my contract has ended, I'll take a long holiday. | When my contract has ended, I will take a long holiday. | "
   "I'll take a long holiday when my contract has ended. | I will take a long holiday when my contract has ended.",
   "The contract surely ends in June, so *when*, and after *when* the present simple: *When my contract ends*.",
   "Līgums jūnijā noteikti beigsies, tāpēc *when*, un aiz *when* lieto Present Simple: *When my contract ends*.")
tx(T, L, 4, "Join with *if* or *when*: Perhaps the hotel is full. In that case, we'll stay with friends.",
   "If the hotel is full, we'll stay with friends. | If the hotel is full, we will stay with friends. | "
   "If the hotel's full, we'll stay with friends. | If the hotel's full, we will stay with friends. | "
   "We'll stay with friends if the hotel is full. | We will stay with friends if the hotel is full. | "
   "We'll stay with friends if the hotel's full. | We will stay with friends if the hotel's full. | "
   "If the hotel is full, then we'll stay with friends. | If the hotel is full, we'll stay with friends instead. | "
   "We'll stay with friends instead if the hotel is full.",
   "*Perhaps*: it is not sure, so *if*, with the present simple: *If the hotel is full*.",
   "*Perhaps*: tas nav droši, tāpēc *if* un Present Simple: *If the hotel is full*.")
tx(T, L, 4, "Join with *when*: I'll finish this email. Then I'll call you back.",
   "When I finish this email, I'll call you back. | When I finish this email, I will call you back. | "
   "When I've finished this email, I'll call you back. | When I've finished this email, I will call you back. | "
   "When I have finished this email, I'll call you back. | When I have finished this email, I will call you back. | "
   "I'll call you back when I finish this email. | I will call you back when I finish this email. | "
   "I'll call you back when I've finished this email. | I will call you back when I've finished this email. | "
   "I'll call you back when I have finished this email. | I will call you back when I have finished this email.",
   "After *when*, the present simple (or the present perfect) for the future, not *will*: *When I finish this email*.",
   "Aiz *when* nākotnei lieto Present Simple (vai Present Perfect), nevis *will*: *When I finish this email*.")

# ── word order (5) ──
od(T, L, 3, "Put the words in order to make a question.", "what will you do when you finish your degree", *ORD_Q,
   also=["when you finish your degree what will you do"])
od(T, L, 3, "Put the words in order to make a question.", "will you text me when your plane lands in rome", *ORD_Q,
   also=["when your plane lands in rome will you text me"])
od(T, L, 3, "Put the words in order.", "if the meeting finishes early i'll go to the gym", *ORD_IF,
   also=["i'll go to the gym if the meeting finishes early"])
od(T, L, 3, "Put the words in order.", "i'll send you the photos of the flat when i get home", *ORD_WHEN,
   also=["when i get home i'll send you the photos of the flat"])
od(T, L, 3, "Put the words in order.", "my parents will move to the coast when they retire", *ORD_WHEN,
   also=["when they retire my parents will move to the coast", "when my parents retire they will move to the coast"])

# ── word bank (4) ──
gp(T, L, 3, "My new laptop arrives on Friday. ___ it ___, I'll set it up for you.", "When / arrives",
   "The delivery day is fixed, so it is sure: *when*. After *when*, the present simple: *When it arrives*.",
   "Piegādes diena ir zināma, tātad tas ir droši: *when*. Aiz *when* lieto Present Simple: *When it arrives*.",
   bank=["When", "If", "arrives", "will arrive"])
gp(T, L, 3, "I might not finish the report today. ___ I ___ it, I'll send it to you tonight.", "If / finish",
   "*might not finish*: it is not sure, so *if*. After *if*, the present simple: *If I finish it*.",
   "*might not finish*: tas nav droši, tāpēc *if*. Aiz *if* lieto Present Simple: *If I finish it*.",
   bank=["If", "When", "finish", "will finish"])
gp(T, L, 3, "We're moving to Riga in March. ___ there, we'll see each other more often.", "When we're",
   "The move is planned, so it is sure: *when*, with the present simple: *When we're there*.",
   "Pārcelšanās ir ieplānota, tātad tas ir droši: *when* un Present Simple: *When we're there*.",
   bank=["When we're", "If we're", "When we'll be"])
gp(T, L, 3, "I might get tickets for the concert. ___ I ___ them, I'll take you with me.", "If / get",
   "*might get*: it is not sure, so *if*. After *if*, the present simple: *If I get them*.",
   "*might get*: tas nav droši, tāpēc *if*. Aiz *if* lieto Present Simple: *If I get them*.",
   bank=["If", "When", "get", "will get"])

# ── matching (1, learning) ──
mt(T, L, 2, "Match each sentence with the one that follows it.",
   [("My flight lands at six.", "When it does, I'll text you."), ("My flight might be late.", "If it is, I'll take a taxi."),
    ("I'm not sure the hotel has parking.", "If it doesn't, we'll park at the station."),
    ("Our room will be ready at two.", "When it is, we'll take our bags up.")],
   "Something sure (*lands at six*, *will be ready*) takes *when*; something not sure (*might*, *not sure*) takes *if*.",
   "Drošam notikumam (*lands at six*, *will be ready*) lieto *when*; nedrošam (*might*, *not sure*) lieto *if*.")
