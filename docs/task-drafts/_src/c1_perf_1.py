"""C1 direction 3 (The perfect tenses: forms and uses), round 1 (23 November 2026). Hewings, Advanced Grammar in Use (3rd ed.),
units 3 and 6 (exercises 3.1-3.4, 6.1); Murphy, English Grammar in Use, units 7-8, 13-14. Only places where the context leaves
one form. Contexts concrete but common; no Latvian surnames."""
from lib import gp, mc, note, tx
T = "The perfect tenses: forms and uses"
L = "C1"

# x_pp_period: the time is still going on, or it is over
gp(T, L, 3, "It's only ten o'clock, and I ___ three cups of coffee this morning. (drink)", "have drunk | 've drunk | have had | 've had",
   "*this morning* is still going on (it's ten o'clock): present perfect, *I've drunk*.",
   "*this morning* vēl turpinās (ir desmit no rīta): Present Perfect, *I've drunk*.")
gp(T, L, 3, "It's six in the evening now. I ___ much this morning because the internet was down. (not / do)", "didn't do | did not do",
   "The morning is over (it's six in the evening): past simple, *I didn't do much this morning*.",
   "Rīts ir beidzies (ir seši vakarā): Past Simple, *I didn't do much this morning*.")
# x_since_clause
mc(T, L, 3, "Choose the correct option: Since she ___ the team, sales have doubled.", "joined",
   ["had joined", "was joining", "joins"],
   "*since* + past simple for the point in the past when it started (*since she joined*), present perfect in the main part (*have doubled*).",
   "*since* + Past Simple brīdim pagātnē, kad tas sākās (*since she joined*), Present Perfect galvenajā daļā (*have doubled*).")
gp(T, L, 4, "Have you made any friends since you ___ in this city? (live)", "have lived | 've lived | have been living | 've been living",
   "Both situations go on until now (you still live here): present perfect also after *since*: *since you've lived here*.",
   "Abas situācijas turpinās līdz šim brīdim (tu joprojām te dzīvo): Present Perfect arī aiz *since*: *since you've lived here*.")
note('have been living :: Also possible: the continuous stresses that the living here still goes on. :: Arī pareizi: Continuous forma uzsver, ka tu te joprojām dzīvo.')
# x_time_perf
gp(T, L, 3, "I'll text you the moment I ___ my exam results. (get)", "'ve got | get | have got | 've gotten | have gotten | have received | 've received",
   "*the moment* about the future: present perfect (*the moment I've got my results*) or present simple (*the moment I get my results*), both correct; never *will* or the past.",
   "*the moment* par nākotni: Present Perfect (*the moment I've got my results*) vai Present Simple (*the moment I get my results*), abi pareizi; nevis *will* vai pagātne.")
note('get :: Also possible: after *the moment* the present simple has the same meaning. :: Arī pareizi: aiz *the moment* Present Simple nozīmē to pašu.')
mc(T, L, 4, "Which sentence has a mistake?", "Once you paid, the order can't be changed.",
   ["The moment we landed, I texted her.", "After she had left hospital, she went on a long holiday.",
    "I'll call you as soon as I've finished."],
   "*Once* about something that has not happened yet (*the order can't be changed*): present perfect or present simple, *Once you've paid*. "
   "*The moment we landed* is about the past, so the past simple is right there.",
   "*Once* par to, kas vēl nav noticis (*the order can't be changed*): Present Perfect vai Present Simple, *Once you've paid*. "
   "*The moment we landed* ir par pagātni, tāpēc tur Past Simple ir pareizi.")
# x_first_time
gp(T, L, 3, "This is the third time she ___ her keys this week! (lose)", "has lost | 's lost",
   "*This is the first / second / third time* + present perfect: *she has lost her keys*.",
   "*This is the first / second / third time* + Present Perfect: *she has lost her keys*.")
mc(T, L, 4, "Which sentence has a mistake?", "This is the first time I am seeing snow.",
   ["It was the first time I'd been on a plane.", "It's the second time he has missed the train this month.",
    "It won't be the first time they've voted against the plan."],
   "After *This is the first time*, the present perfect: *This is the first time I've seen snow.* After *It was the first time*, the past perfect.",
   "Aiz *This is the first time* lieto Present Perfect: *This is the first time I've seen snow.* Aiz *It was the first time* lieto Past Perfect.")
# x_ppc_adv
gp(T, L, 3, "It's only eleven, and I ___ the bank four times. Nobody's answering. (ring)", "have rung | 've rung",
   "A number of times (*four times*): present perfect simple, *I've rung*. The continuous is for the activity: *I've been ringing all morning*.",
   "Reižu skaits (*four times*): Present Perfect Simple, *I've rung*. Ilgstošā forma ir darbībai: *I've been ringing all morning*.")
mc(T, L, 3, "Which sentence has a mistake?", "I've been having this phone since May.",
   ["Rents have gone up by eight per cent this year.", "She's been learning Spanish for two years.",
    "We've been waiting for the plumber since nine."],
   "*have* meaning *own* is a state: present perfect simple, *I've had this phone since May*.",
   "*have* nozīmē *piederēt* ir stāvoklis: Present Perfect Simple, *I've had this phone since May*.")
# x_perf_cont_all
gp(T, L, 4, "By next May I ___ at this school for ten years. (teach)",
   "will have taught | 'll have taught | will have been teaching | 'll have been teaching",
   "Up to a point in the future (*by next May*): future perfect, *I'll have taught* or *I'll have been teaching*.",
   "Līdz brīdim nākotnē (*by next May*): Future Perfect, *I'll have taught* vai *I'll have been teaching*.")
note('will have been teaching :: Also possible: the continuous stresses the teaching as an activity that goes on. :: Arī pareizi: Continuous forma uzsver mācīšanu kā darbību, kas turpinās.')
# x_perf_aspect
gp(T, L, 4, "The thief is thought ___ the country last week. (leave)", "to have left",
   "*is thought* is now, the leaving was earlier (*last week*): the perfect after *to*, *to have left*.",
   "*is thought* ir tagad, aizbraukšana bija agrāk (*last week*): perfekts aiz *to*, *to have left*.")
tx(T, L, 4, "Report what she said with *deny* and *having*. Her words: 'I didn't read the letter.'",
   "She denied having read the letter. | She denied having read it. | She denied reading the letter.",
   "*deny* + *having* + 3rd form for something earlier than the denying: *She denied having read the letter.* (*She denied reading the letter* is natural too.)",
   "*deny* + *having* + 3. forma tam, kas notika pirms noliegšanas: *She denied having read the letter.* (Dabiski ir arī *She denied reading the letter*.)")
note("She denied reading the letter. :: Also correct and natural; the task asks for *having*, which shows that the reading came first. :: Arī pareizi un dabiski; uzdevums prasa *having*, kas parāda, ka lasīšana bija agrāk.")
