"""Batch 4, point should_have (B1.2): should have / could have done, criticism and regret. Murphy unit 27 (could and could have)
and unit 33 (should, section C: should have done). Topic More modals (teacher's decision, 15 November: not the passive topic).
The check / use tasks keep the meaning fixed by the sentence (the modal is given in the sentence or in the brackets) and test the FORM:
should / could + have + 3rd form (not should told, should have tell, should had told, should of told, should have took).
could have is never a wrong option: You could have called me is a reproach too. must have (deduction, B2.1) is a wrong option only in
one task, where the sentence says the action did not happen (Why didn't you tell me?). ought to have is accepted in typed tasks."""
from lib import gp, od, mc, tx, mt, learning_task
T = "More modals: might, could, be able to"
L = "B1.2"

SH = ("*should have* + 3rd form = it was the right thing to do, but it did not happen: *You should have told me.*",
      "*should have* + 3. forma = tā būtu bijis pareizi, bet tas netika izdarīts: *You should have told me.* (Tev vajadzēja man pateikt.)")
SHNEG = ("*shouldn't have* + 3rd form = it happened, but it was wrong: *You shouldn't have shouted.*",
         "*shouldn't have* + 3. forma = tas notika, bet tas bija nepareizi: *You shouldn't have shouted.* (Tev nevajadzēja kliegt.)")
CO = ("*could have* + 3rd form = it was possible, but it did not happen: *We could have won.*",
      "*could have* + 3. forma = tas bija iespējams, bet nenotika: *We could have won.* (Mēs varējām uzvarēt.) "
      "Tulkojot burtiski, *varējām uzvarēt* šķiet *could win*, bet par iespēju, kas nenotika, angliski saka *could have won*.")
COREP = ("*could have* + 3rd form can also criticise: it was possible, and the person did not do it: *You could have called me.*",
         "*could have* + 3. forma var arī pārmest: tas bija iespējams, bet cilvēks to neizdarīja: *You could have called me.* (Tu varēji man piezvanīt.)")
FORM = ("After *should / could* comes *have* + 3rd form: *should have told*, not *should told*, *should have tell* or *should had told*.",
        "Aiz *should / could* nāk *have* + 3. forma: *should have told*, nevis *should told*, *should have tell* vai *should had told*. "
        "Tulkojot burtiski, *vajadzēja pateikt* šķiet *should told*, bet angliski pagātni rāda *have* + 3. forma.")

# ── choose (7) ──
# 1. form after should: taken (took is the past, not the 3rd form)
mc(T, L, 2, "Choose the correct option: We ___ a taxi to the airport, because the bus was so slow that we missed our flight.",
   "should have taken", ["should took", "should have took", "should had taken"],
   "*should have* + 3rd form: *taken*, not the past *took*. The taxi was the right choice, but we did not take it.",
   "*should have* + 3. forma: *taken*, nevis pagātnes forma *took*. Taksometrs būtu bijis pareizā izvēle, bet mēs to neņēmām.")
# 2. negative: shouldn't have shouted
mc(T, L, 2, "Choose the correct option: You ___ at the waiter, because it wasn't his fault that the kitchen was slow.",
   "shouldn't have shouted", ["shouldn't shouted", "shouldn't have shout", "didn't should have shouted"],
   "*shouldn't have* + 3rd form: you shouted, and that was wrong. The negative is *shouldn't have*, never *didn't should*.",
   "*shouldn't have* + 3. forma: tu kliedzi, un tas bija nepareizi. Noliegums ir *shouldn't have*, nekad *didn't should*.")
# 3. could have been: a chance that was missed
mc(T, L, 2, "Choose the correct option: She ___ a great doctor, but she decided to study music instead.",
   "could have been", ["could been", "could have be", "could had been"], *CO)
# 4. criticism, not a guess: must have told would mean I am sure you told me
mc(T, L, 2, "Choose the correct option: Why didn't you tell me about the delay? You ___ me before I left home.",
   "should have told", ["must have told", "should have tell", "should had told"],
   "You did not tell me, and that was wrong: *should have told*. *must have told* would mean 'I am sure you told me', and the first sentence says you did not.",
   "Tu man nepateici, un tas bija nepareizi: *should have told*. *must have told* nozīmētu 'esmu pārliecināts, ka tu pateici', bet pirmais teikums saka, ka nepateici.")
# 5. have, not of or had (should've sounds like should of)
mc(T, L, 2, "Choose the correct option: Sorry, I should ___ called you last night, but my phone battery was dead.",
   "have", ["of", "had"],
   "*should have* + 3rd form. In speech *should've* sounds like *should of*, but we always write *have*. *should had* is not English.",
   "*should have* + 3. forma. Runā *should've* izklausās pēc *should of*, bet raksta vienmēr *have*. *should had* angliski nesaka.")
# 6. whole sentences: the form after should have
mc(T, L, 2, "Which sentence is correct?", "You should have checked the figures before you sent the report.",
   ["You should checked the figures before you sent the report.", "You should have check the figures before you sent the report.",
    "You should had checked the figures before you sent the report."],
   "After *should* comes *have* + 3rd form: *should have checked*, not *should checked*, *should have check* or *should had checked*.",
   "Aiz *should* nāk *have* + 3. forma: *should have checked*, nevis *should checked*, *should have check* vai *should had checked*.")
# 7. NOT correct: should of; the other three are a regret, a missed chance and 'you missed something good'
mc(T, L, 2, "Which sentence is NOT correct?", "You should of booked the tickets much earlier.",
   ["I shouldn't have eaten so much last night.", "We could have driven, but we took the train.", "You should have seen the view from the top."],
   "*should of* is a spelling mistake: in speech *should've* sounds like *should of*, but we write *should have booked*.",
   "*should of* ir pareizrakstības kļūda: runā *should've* izklausās pēc *should of*, bet raksta *should have booked*.")

# ── word order (5) ──
od(T, L, 3, "Put the words in order.", "you should have told me that the train was cancelled", *SH)
od(T, L, 3, "Put the words in order.", "i shouldn't have bought these shoes without trying them on", *SHNEG)
od(T, L, 3, "Put the words in order.", "she could have got the job but she didn't apply in time", *CO)
od(T, L, 3, "Put the words in order.", "you could have asked me for help instead of doing it alone", *COREP,
   also=["instead of doing it alone you could have asked me for help"])
od(T, L, 3, "Put the words in order to make a question.", "what should i have said when my boss asked about the delay",
   "Question: question word + *should* + subject + *have* + 3rd form: *What should I have said?*",
   "Jautājums: jautājamais vārds + *should* + teik. priekšmets + *have* + 3. forma: *What should I have said?*",
   also=["when my boss asked about the delay what should i have said"])

# ── word bank (4): the wrong chips are the typical mistakes of this point ──
gp(T, L, 3, "You shouldn't ___ ___ the oven on when you went out this morning.", "have / left", *SHNEG,
   bank=["have", "left", "had", "leave"])
gp(T, L, 3, "We could ___ ___ the earlier ferry, but we decided to stay another night.", "have / taken", *CO,
   bank=["have", "taken", "took", "had"])
gp(T, L, 3, "Sorry, I should ___ you that the office was closed on Monday.", "have told", *FORM,
   bank=["have told", "told", "had told"])
gp(T, L, 3, "I ___ ___ studied for the exam, but I spent the whole weekend watching TV series.", "should / have",
   "I did not study, and that was a mistake: *should have studied*. *must have studied* would be a guess that I studied; *should had* is not English.",
   "Es nemācījos, un tā bija kļūda: *should have studied*. *must have studied* būtu minējums, ka es mācījos; *should had* angliski nesaka.",
   bank=["should", "have", "must", "had"])

# ── matching (1): a learning task; each comment fits only its own situation ──
mt(T, L, 2, "Match each situation with the comment.",
   [("You didn't wear a coat, and now you've got a cold.", "You should have worn one."),
    ("You laughed at his new haircut, and he was upset.", "You shouldn't have laughed."),
    ("We missed the last bus and walked home in the rain.", "We could have taken a taxi."),
    ("You knew about the problem but said nothing.", "You should have told someone.")],
   "*should have* + 3rd form = it did not happen, and that was a mistake. *shouldn't have* = it happened, and that was a mistake. *could have* = it was possible, but it did not happen.",
   "*should have* + 3. forma = tas nenotika, un tā bija kļūda. *shouldn't have* = tas notika, un tā bija kļūda. *could have* = tas bija iespējams, bet nenotika.")

# ── typed gap (5): the modal is in the brackets, so the form is tested ──
gp(T, L, 3, "You ___ me about the party. I would have loved to come! (should / tell)",
   "should have told | should've told | ought to have told", *SH)
gp(T, L, 3, "I ___ so much at the wedding. I felt terrible the next morning. (should / not / drink)",
   "shouldn't have drunk | should not have drunk | oughtn't to have drunk | ought not to have drunk", *SHNEG)
gp(T, L, 3, "We ___ the final, but we missed two penalties in the last ten minutes. (could / win)",
   "could have won | could've won", *CO)
gp(T, L, 3, "We ___ the whole day at the beach yesterday, but we stayed in the hotel because of the clouds. (could / spend)",
   "could have spent | could've spent", *CO)
gp(T, L, 3, "You ___ me back last night. Your phone was with you all evening! (could / call)",
   "could have called | could've called", *COREP)

# ── whole sentence (3) ──
tx(T, L, 4, "Make it negative: I should have told Anna what you said about her new boyfriend.",
   "I shouldn't have told Anna what you said about her new boyfriend. | I should not have told Anna what you said about her new boyfriend. | "
   "I oughtn't to have told Anna what you said about her new boyfriend. | I ought not to have told Anna what you said about her new boyfriend. | "
   "I shouldn't've told Anna what you said about her new boyfriend.", *SHNEG)
tx(T, L, 4, "Start with *You shouldn't*: It was wrong of you to lend him your car for the whole weekend.",
   "You shouldn't have lent him your car for the whole weekend. | You shouldn't have lent your car to him for the whole weekend. | "
   "You shouldn't have lent him your car. | You shouldn't have lent your car to him.",
   "It was wrong, and you did it: *You shouldn't have lent …* (*have* + 3rd form *lent*, not *lend* or *lended*).",
   "Tas bija nepareizi, un tu to izdarīji: *You shouldn't have lent …* (*have* + 3. forma *lent*, nevis *lend* vai *lended*).")
tx(T, L, 4, "Make a yes/no question: I should have told the manager about the mistake in the invoice.",
   "Should I have told the manager about the mistake in the invoice? | Ought I to have told the manager about the mistake in the invoice? | "
   "Should I have told the manager about the mistake?",
   "Question: *Should* + subject + *have* + 3rd form: *Should I have told the manager …?*",
   "Jautājums: *Should* + teik. priekšmets + *have* + 3. forma: *Should I have told the manager …?*")
