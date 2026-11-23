"""C1 direction 6 (The subjunctive), round 1 (23 November 2026). Hewings, Advanced Grammar in Use (3rd ed.), units 39 and 85;
Murphy, English Grammar in Use, units 39, 41. Only places where the context leaves one form; where informal English also
allows an ordinary tense (*demanded that he resigns*, *if I was*), it is accepted."""
from lib import gp, mc, note
T = "The subjunctive: I insist that he be told, if I were"
L = "C1"

# x_subj_present
mc(T, L, 4, "Which sentence has a mistake?", "The board demanded the director to resign.",
   ["The doctor recommended that she rest for a week.", "I insist that he be told the truth.",
    "They suggested that we should leave early."],
   "*demand* is not followed by an object + *to*: *The board demanded that the director resign* (or *should resign*).",
   "Aiz *demand* nelieto papildinātāju + *to*: *The board demanded that the director resign* (vai *should resign*).")
gp(T, L, 4, "We recommend that this medicine ___ taken with alcohol. (not / be)", "not be | should not be | shouldn't be | is not | isn't",
   "Formal: *not* + base form: *that this medicine not be taken*; also *should not be*, or *is not* in less formal English.",
   "Oficiāli: *not* + pamatforma: *that this medicine not be taken*; arī *should not be* vai mazāk oficiāli *is not*.")
note('should not be :: Also correct (British English). :: Arī pareizi (britu angļu valodā). || is not :: Also correct in less formal English. :: Arī pareizi, mazāk oficiāli.')
# x_should_react
gp(T, L, 4, "It's odd that she ___ ___ ___ that at yesterday's meeting. She's usually so polite.", "should / have / said",
   "After *It's odd / surprising that*, *should* + verb shows surprise; about the past, *should have* + 3rd form: *It's odd that she should have said that.*",
   "Aiz *It's odd / surprising that* *should* + darbības vārds izsaka pārsteigumu; par pagātni *should have* + 3. forma: *It's odd that she should have said that.*",
   bank=["should", "have", "said", "say", "has"])
# x_subj_were
gp(T, L, 4, "If the bank ___ to refuse the loan, we would sell the car. (be)", "were | was",
   "*If* + *were to* for an unlikely future: *If the bank were to refuse…* (*was* is informal). Not *would* after *if*.",
   "*If* + *were to* maz ticamai nākotnei: *If the bank were to refuse…* (*was* ir sarunvalodā). Aiz *if* nelieto *would*.")
mc(T, L, 4, "Which sentence has a mistake?", "If the landlord would raise the rent, we'd move.",
   ["I wish the weekend were a little longer.", "If I were you, I'd take that job in Oslo.", "She speaks to me as if I were still a child."],
   "After *if*, not *would* for a condition: *If the landlord raised / were to raise the rent, we'd move.*",
   "Aiz *if* nosacījumam nelieto *would*: *If the landlord raised / were to raise the rent, we'd move.*")
# x_rather_perf
gp(T, L, 4, "I'd rather you ___ me yesterday, before the meeting, not after it. (tell)", "had told | 'd told",
   "Something someone did in the past that you wish were different: *I'd rather you had told me.* *I'd rather you told me* is about now or later.",
   "Kaut kas, ko kāds izdarīja pagātnē un ko gribētos citādi: *I'd rather you had told me.* *I'd rather you told me* ir par tagadni vai nākotni.")
# x_subj_fixed
mc(T, L, 4, "Choose the correct option: The plan has its problems. ___, it's the best one we have.", "Be that as it may",
   ["Being that as it may", "Come what may", "As it may be"],
   "A fixed phrase with the old subjunctive: *Be that as it may* = even so.",
   "Nemainīgs izteiciens ar seno *be* formu: *Be that as it may* = tomēr, lai kā arī būtu.")

# ── added 23 November to reach 10 counted tasks ──
# x_subj_adj
gp(T, L, 4, "It is essential that every passenger ___ a valid ticket. (have)", "have | should have | has",
   "After *It is essential / vital that*, formal English uses the base form (*have*) or *should have*; *has* is less formal.",
   "Aiz *It is essential / vital that* oficiālā valodā lieto pamatformu (*have*) vai *should have*; *has* ir mazāk oficiāli.")
note('should have :: Also correct (British English). :: Arī pareizi (britu angļu valodā). || has :: Also correct in less formal English. :: Arī pareizi, mazāk oficiāli.')
# x_subj_present
mc(T, L, 4, "Choose the correct option: The lawyer demanded that her client ___ told the whole truth.", "be",
   ["is being", "to be", "being"],
   "After *demand that*, the base form for every person: *The lawyer demanded that her client be told.* (British English also: *should be told*.)",
   "Aiz *demand that* pamatforma visām personām: *The lawyer demanded that her client be told.* (Britu angļu valodā arī: *should be told*.)")
# x_rather_perf
mc(T, L, 4, "Which sentence has a mistake?", "I'd rather you wouldn't have posted that photo.",
   ["I'd rather you didn't smoke in the kitchen.", "I wish I had listened to your advice back then.", "I'd sooner she hadn't told everyone at work."],
   "*I'd rather* + past perfect for the past: *I'd rather you hadn't posted that photo*, not *wouldn't have posted*.",
   "*I'd rather* + Past Perfect pagātnei: *I'd rather you hadn't posted that photo*, nevis *wouldn't have posted*.")
# x_subj_fixed
gp(T, L, 4, "We'll finish this project on time, come what ___.", "may | might",
   "A fixed phrase with the old subjunctive: *come what may* = whatever happens.",
   "Nemainīgs izteiciens ar seno *be* formu: *come what may* = lai kas notiktu.")
note('might :: Also possible, but rarer: *come what may* is the usual phrase. :: Arī pareizi, bet retāk: parastais izteiciens ir *come what may*.')

# teacher's tester, 23 November: the same frame about something that happens again and again
gp(T, L, 4, "It's odd that she ___ ___ that whenever the topic comes up. She knows it isn't true.", "should / say",
   "After *It's odd that*, *should* + base form shows surprise about something that keeps happening: *It's odd that she should say that.*",
   "Aiz *It's odd that* *should* + pamatforma izsaka pārsteigumu par to, kas atkārtojas: *It's odd that she should say that.*",
   bank=["should", "say", "says", "saying"])
