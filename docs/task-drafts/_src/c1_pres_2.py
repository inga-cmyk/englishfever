"""C1 direction 1 (Advanced present simple and continuous), round 2 (23 November 2026): points x_pres_story, x_pres_comment,
x_i_hear, x_polite_cont, x_state_cont (appear, expect), x_performative. Hewings, Advanced Grammar in Use (3rd ed.), units 1-2
(exercises 1.1, 1.2, 2.1, 2.2). Contexts concrete but common; no Latvian surnames (teacher, 22 November).
Headlines (x_headline) are left out: round c1-1c showed that *has resigned* and *resigned* are real headline forms too, so a
choice has no single answer."""
from lib import gp, od, mc
T = "Advanced present simple and continuous"
L = "C1"

# ── x_pres_story: an anecdote told in the present ──
# st1 lifestyle: background continuous, main event simple; "hands" fixes the present
gp(T, L, 4, "Write one word in each gap: So I ___ ___ in the queue at the bakery, and this woman suddenly ___ round and hands me her dog. (stand, turn)",
   "am | 'm / standing / turns",
   "In a story told in the present, the background is in the present continuous "
   "(*I'm standing in the queue*) and the main events in the present simple (*turns, hands*).",
   "Stāstā tagadnē fons ir Present Continuous (*I'm standing in the queue*), bet galvenie notikumi Present Simple (*turns, hands*).")
# st2 the main event is not continuous
mc(T, L, 4, "Which sentence has a mistake?", "So this man is walking into a café and he orders a glass of milk.",
   ["I was waiting for the bus when suddenly this car stops right in front of me.",
    "We're having dinner when all the lights go out.",
    "In the film, a retired teacher moves to Lisbon and opens a café."],
   "In a joke or a story told in the present, the main events are in the present simple: *So this man walks into a café and orders…* "
   "After a past background, a sudden event can be in the present simple (*I was waiting … when suddenly this car stops*): that is correct.",
   "Jokā vai stāstā tagadnē galvenie notikumi ir Present Simple: *So this man walks into a café and orders…* "
   "Pēc pagātnes fona pēkšņs notikums var būt Present Simple (*I was waiting … when suddenly this car stops*): tas ir pareizi.")

# ── x_pres_comment: live commentary ──
gp(T, L, 4, "Write one word in each gap: And Jones ___ the ball to Taylor, who ___ and scores! (pass, shoot)", "passes / shoots",
   "In a live commentary, quick actions that are over as you speak are in the present simple: *passes, shoots, scores*. "
   "*is passing* would describe a longer action in progress.",
   "Tiešraides komentārā ātras darbības, kas beidzas runāšanas brīdī, ir Present Simple: *passes, shoots, scores*. "
   "*is passing* aprakstītu ilgāku darbību, kas vēl notiek.")

# ── x_i_hear: news we have heard ──
mc(T, L, 4, "Which sentence has a mistake?", "I'm gathering you're looking for a new flat.",
   ["I hear the bridge will be closed all summer.", "Anna tells me you've started running.",
    "It says here the museum is free on Sundays."],
   "To pass on news we have heard or read, we use the present simple: *I gather, I hear, Anna tells me, It says here*. "
   "Not *I'm gathering*: *I gather you're looking for a new flat.*",
   "Lai nodotu dzirdētu vai izlasītu ziņu, lieto Present Simple: *I gather, I hear, Anna tells me, It says here*. "
   "Nevis *I'm gathering*: *I gather you're looking for a new flat.*")

# ── x_polite_cont: I'm wondering whether … ──
mc(T, L, 4, "Which sentence has a mistake?", "I'm wondering could you look at my CV before Friday.",
   ["We're hoping to move in by the end of May.", "I was wondering if you were free on Thursday.",
    "I wonder whether you'd mind helping me with this."],
   "After *I'm wondering*, the question becomes *if / whether* + statement order: *I'm wondering whether you could look at my CV.*",
   "Aiz *I'm wondering* jautājums kļūst par *if / whether* + apgalvojuma vārdu secību: *I'm wondering whether you could look at my CV.*")
od(T, L, 4, "Put the words in order.", "I'm wondering whether you could help me with this",
   "A polite request: *I'm wondering whether* + statement order (*you could*), not question order (*could you*).",
   "Pieklājīgs lūgums: *I'm wondering whether* + apgalvojuma vārdu secība (*you could*), nevis jautājuma secība (*could you*).")

# ── x_state_cont: one verb, two meanings ──
gp(T, L, 4, "The app ___ to work on my phone. Can you check it? (not / appear)", "doesn't appear | does not appear",
   "*appear* = seem is a state: present simple, *doesn't appear to work*. In the meaning *take part* it can be continuous "
   "(*She's appearing in a musical*).",
   "*appear* = šķist ir stāvoklis: Present Simple, *doesn't appear to work*. Nozīmē *piedalīties, uzstāties* var būt ilgstošā forma "
   "(*She's appearing in a musical*).")
gp(T, L, 3, "My sister and her husband ___ their first baby in June. (expect)", "are expecting | 're expecting",
   "*be expecting a baby* = she is pregnant, always continuous. In the meaning *think something will happen*, *expect* is simple "
   "(*I expect it will rain*).",
   "*be expecting a baby* = gaida bērnu, vienmēr ilgstošā forma. Nozīmē *domāt, ka kaut kas notiks* *expect* ir vienkāršajā formā "
   "(*I expect it will rain*).")

# ── x_performative: saying it is doing it ──
mc(T, L, 4, "Which sentence has a mistake?", "I'm promising I'll pay you back on Friday.",
   ["I suggest we meet at the station.", "We regret that the flight has been cancelled.",
    "I'm not suggesting you were careless."],
   "When saying the words is the act itself (promising, suggesting, regretting), use the present simple: *I promise I'll pay you back.* "
   "In the negative, *I'm not suggesting* is also correct.",
   "Ja paši vārdi ir darbība (apsolīt, ieteikt, izteikt nožēlu), lieto Present Simple: *I promise I'll pay you back.* "
   "Noliegumā pareizi ir arī *I'm not suggesting*.")
