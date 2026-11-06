"""Typed forms for B2 and C1 with the typical mistakes of Latvian adults (teacher, 6 November): the level test asks the learner to type
the form, and B2 had only 23 such tasks, C1 none. Every task is one gap with the verb or word in brackets; only one answer fits the
sentence. A Latvian note ("Tulkojot burtiski") only where Latvian causes the mistake. Approved by the teacher on 6 November."""
import csv
from pathlib import Path
from lib import Topic, rows, save

ROOT = Path(__file__).resolve().parents[3]
MISTAKE = []   # the typical wrong answer each task is there to catch (for the review only)


def g(topic, lv, q, ans, mistake, why):
    Topic(topic).gap(lv, q, ans, why=why); MISTAKE.append(mistake)


C2 = "Second conditional (if + past, would)"
C3 = "Third conditional (if + had done, would have done)"
CM = "Mixed conditionals"
CA = "Advanced conditionals: inversion, unless, wish"
RS = "Reported statements (tense changes)"
RQ = "Reported questions and requests"
RV = "Reporting verbs (suggest, admit, promise...)"
IP = "Indirect questions (Could you tell me where...)"
IA = "Indirect questions, more uses (I don't know what to do)"
NB = "Narrative tenses with past perfect continuous"
CC = "Contrast, purpose and reason (although, despite, so that)"
CB = "Contrast, purpose, reason and result (whereas, in case, therefore)"
UT = "Unreal time and preferences (it's high time, I'd rather)"

IFPAST = ("An imagined present: *if* + past (*knew*), not *would*.", "Iedomāta tagadne: *if* + pagātne (*knew*), nevis *would*. Tulkojot burtiski \"ja es zinātu\", gribas *would*, bet aiz *if* tā nav.")
IFHAD = ("An imagined past: *if* + *had* + 3rd form, not *would have*.", "Iedomāta pagātne: *if* + *had* + 3. forma, nevis *would have*.")
WOULDHAVE = ("The result in an imagined past: *would have* + 3rd form.", "Sekas iedomātā pagātnē: *would have* + 3. forma.")

# ── B2.1 ──
g(C2, "B2.1", "If I ___ her number, I would call her right now. (know)", "knew", "would know", IFPAST)
g(C2, "B2.1", "If the train ___ faster, more people would use it for work. (be)", "was | were", "would be", IFPAST)
g(C2, "B2.1", "I ___ more if the gym were closer to my office. (exercise)", "would exercise | 'd exercise", "will exercise",
  ("The result of an imagined present: *would* + base form.", "Iedomātas tagadnes sekas: *would* + pamatforma."))
g(C3, "B2.1", "If we ___ earlier, we wouldn't have missed the flight. (leave)", "had left | 'd left", "would have left", IFHAD)
g(C3, "B2.1", "If you had asked me, I ___ you with the move. (help)", "would have helped | 'd have helped", "would helped", WOULDHAVE)
g(RS, "B2.1", "Tom said he ___ the report the next day. (send)", "would send | 'd send", "will send",
  ("Reported later: *will* becomes *would*.", "Atstāstot vēlāk, *will* kļūst par *would*. Tulkojot burtiski \"teica, ka nosūtīs\", gribas *will*."))
g(RS, "B2.1", "She told me she ___ in Riga for two years. (live)", "had lived | had been living | 'd lived | 'd been living", "has lived",
  ("Reported later: *has lived* becomes *had lived*.", "Atstāstot vēlāk, *has lived* kļūst par *had lived*."))
g(RQ, "B2.1", "The receptionist asked me where I ___ from. (be)", "was", "am",
  ("A reported question: statement order and one step back in time: *where I was from*.", "Atstāstītā jautājumā: apgalvojuma secība un laiks soli atpakaļ: *where I was from*."))
g(RQ, "B2.1", "She asked me how long I ___ English. (study)", "had been studying | had studied | 'd been studying | 'd studied", "have been studying",
  ("A reported question: one step back in time: *had been studying*.", "Atstāstītā jautājumā laiks soli atpakaļ: *had been studying*."))
g(IP, "B2.1", "Could you tell me what time the museum ___? (open)", "opens", "does open",
  ("After *Could you tell me* the word order is like a statement, without *does*.", "Aiz *Could you tell me* vārdu secība ir kā apgalvojumā, bez *does*."))
g(NB, "B2.1", "When I finally got through, I ___ on hold for forty minutes. (wait)", "had been waiting | 'd been waiting", "was waiting",
  ("How long something went on before a moment in the past: *had been* + *-ing*.", "Cik ilgi kaut kas notika līdz kādam brīdim pagātnē: *had been* + *-ing*."))
g(CC, "B2.1", "___ the rain, we finished the hike.", "Despite | In spite of", "Although",
  ("*Despite / In spite of* + noun (*the rain*); *although* needs subject + verb.", "*Despite / In spite of* + lietvārds (*the rain*); aiz *although* vajag teikuma priekšmetu un darbības vārdu."))
g(CC, "B2.1", "She wrote everything down so as ___ anything. (not / forget)", "not to forget", "to not forget",
  ("Purpose, negative: *so as not to* + base form.", "Nolūks noliegumā: *so as not to* + pamatforma."))
g(CB, "B2.1", "Take an umbrella in case it ___ later. (rain)", "rains", "will rain",
  ("After *in case* the present, not *will*.", "Aiz *in case* tagadne, nevis *will*. Tulkojot burtiski \"ja nu līs\", gribas *will*."))

# ── B2.2 ──
g(C3, "B2.2", "I would have gone to the concert if I ___ about it. (know)", "had known | 'd known", "would have known", IFHAD)
g(C3, "B2.2", "If she hadn't checked the code, the app ___ . (crash)", "would have crashed | 'd have crashed", "would crash", WOULDHAVE)
g(RQ, "B2.2", "The doctor told me ___ anything heavy for a week. (not / lift)", "not to lift", "don't lift",
  ("A reported instruction: *told me not to* + base form.", "Atstāstīts norādījums: *told me not to* + pamatforma."))
g(RV, "B2.2", "He apologised ___ late for the meeting. (be)", "for being", "to be",
  ("*apologise for* + *-ing*.", "*apologise for* + *-ing*."))
g(RV, "B2.2", "My colleague suggested ___ a taxi to the airport. (take)", "taking", "to take",
  ("*suggest* + *-ing* (or *suggest that we take*), never *suggest to*.", "*suggest* + *-ing* (vai *suggest that we take*), nekad *suggest to*. Tulkojot burtiski \"ieteica paņemt\", gribas *to take*."))
g(IA, "B2.2", "I'm not sure what time the meeting ___ . (start)", "starts | will start", "does start",
  ("Inside a sentence the question has statement order, without *does*.", "Teikuma iekšienē jautājumam ir apgalvojuma secība, bez *does*."))
g(NB, "B2.2", "Her eyes were red because she ___ . (cry)", "had been crying | 'd been crying", "was crying",
  ("The result we see, from an activity before: *had been* + *-ing*.", "Redzams rezultāts no agrākas darbības: *had been* + *-ing*."))
g(CM, "B2.2", "If I had studied medicine, I ___ a doctor now. (be)", "would be | 'd be", "would have been",
  ("A past choice with a result now: *would* + base form, because of *now*.", "Pagātnes izvēle ar sekām tagad: *would* + pamatforma, jo ir *now*."))
g(CM, "B2.2", "If I ___ so shy, I would have spoken to her at the party. (not / be)", "weren't | wasn't | were not | was not", "hadn't been",
  ("A quality now (*so shy*) with a result in the past: *if* + past.", "Īpašība tagad (*so shy*) ar sekām pagātnē: *if* + pagātne."))
g(CB, "B2.2", "Sales fell sharply; ___ , the company cut its prices.", "therefore | as a result | consequently | thus", "because",
  ("A result as a new step after a semicolon: *therefore*, *as a result*.", "Rezultāts kā jauns solis aiz semikola: *therefore*, *as a result*."))

# ── C1.1 ──
g(CM, "C1.1", "If she ___ the job in London, she would be living there now. (accept)", "had accepted | 'd accepted", "accepted",
  ("A past event with a result now: *if* + *had* + 3rd form.", "Pagātnes notikums ar sekām tagad: *if* + *had* + 3. forma."))
g(CA, "C1.1", "I wish I ___ more time to travel this year. (have)", "had", "would have",
  ("A wish about now: *wish* + past.", "Vēlēšanās par tagadni: *wish* + pagātne. Tulkojot burtiski \"es gribētu, lai man būtu\", gribas *would have*."))
g(CA, "C1.1", "I wish I ___ that comment in the meeting yesterday. (not / make)", "hadn't made | had not made", "didn't make",
  ("Regret about the past: *wish* + *had* + 3rd form.", "Nožēla par pagātni: *wish* + *had* + 3. forma."))
g(CA, "C1.1", "We'll start at nine unless the speaker ___ late. (be)", "is", "isn't",
  ("*unless* already means *if … not*: no second *not*.", "*unless* jau nozīmē *if … not*: otru noliegumu neliek. Tulkojot burtiski \"ja vien nekavēsies\", iznāk divi noliegumi."))
g(CA, "C1.1", "___ I known about the strike, I would have booked another flight. (have)", "Had", "If",
  ("Formal, without *if*: *Had I known*.", "Formāli, bez *if*: *Had I known*."))
g(UT, "C1.1", "It's high time the government ___ something about housing. (do)", "did", "does",
  ("*It's (high) time* + subject + past: it should already happen.", "*It's (high) time* + teikuma priekšmets + pagātne: tam jau vajadzētu notikt."))
g(UT, "C1.1", "I'd rather you ___ my phone without asking. (not / use)", "didn't use | did not use", "don't use",
  ("*I'd rather* + another person + past.", "*I'd rather* + cits cilvēks + pagātne."))
g(RV, "C1.1", "She insisted ___ for the whole dinner. (pay)", "on paying", "to pay",
  ("*insist on* + *-ing*.", "*insist on* + *-ing*."))
g(IA, "C1.1", "We couldn't decide where ___ on holiday. (go)", "to go", "should we go",
  ("Not knowing what to do: question word + *to* + base form.", "Nezinot, ko darīt: jautājamais vārds + *to* + pamatforma. Tulkojot burtiski \"kur mums braukt\", iznāk jautājuma secība."))

# ── C1.2 ──
g(CA, "C1.2", "___ I in your position, I would ask for a pay rise. (be)", "Were", "Was",
  ("Formal, without *if*: *Were I* (not *Was I*).", "Formāli, bez *if*: *Were I* (nevis *Was I*)."))
g(CA, "C1.2", "If it ___ for your advice, I would never have applied. (not / be)", "hadn't been | had not been", "wasn't",
  ("*If it hadn't been for* + noun = without it, in the past.", "*If it hadn't been for* + lietvārds = bez tā, pagātnē."))
g(RV, "C1.2", "The minister denied ___ the report before it was published. (see)", "having seen | seeing", "to see",
  ("*deny* + *-ing* (or *having* + 3rd form).", "*deny* + *-ing* (vai *having* + 3. forma)."))
g(RV, "C1.2", "They accused the company ___ the data of its users. (sell)", "of selling", "for selling",
  ("*accuse someone of* + *-ing*.", "*accuse someone of* + *-ing*. Tulkojot burtiski \"apsūdzēja par\", gribas *for*."))
g(IA, "C1.2", "___ wins the competition will get a trip to Lisbon. (who)", "Whoever", "Who",
  ("*Whoever* = it does not matter who: the person who.", "*Whoever* = nav svarīgi, kurš: tas, kurš."))
g(IA, "C1.2", "It depends on ___ the budget is approved.", "whether", "if",
  ("After a preposition use *whether*, not *if*.", "Aiz prievārda lieto *whether*, nevis *if*."))
g(UT, "C1.2", "It's about time you ___ to the dentist. (go)", "went", "go",
  ("*It's about time* + subject + past.", "*It's about time* + teikuma priekšmets + pagātne."))
g(CA, "C1.2", "If only I ___ my passport at home! (not / leave)", "hadn't left | had not left", "didn't leave",
  ("Regret about the past: *If only* + *had* + 3rd form.", "Nožēla par pagātni: *If only* + *had* + 3. forma."))

assert len(rows) == len(MISTAKE) == 41, len(rows)
save("typical-b2c1-1.csv")   # approved by the teacher on 6 November

out = list(csv.reader((ROOT / "docs/task-drafts/typical-b2c1-1.csv").open(encoding="utf-8-sig")))[1:]
L = ["# Typed forms for B2 and C1: typical mistakes (41)", "",
     "For the level test (type the form, nothing to guess) and for practice. Each task has one gap; the word in brackets is the base. "
     "*catches* = the typical wrong answer the task is there to find. Approved by the teacher on 6 November.", ""]
cur = None
for n, (r, m) in enumerate(zip(out, MISTAKE), 1):
    if r[1] != cur: cur = r[1]; L += ["", f"## {cur}", ""]
    L += [f"{n}. *{r[3]}* → **{r[4]}** · catches: *{m}* · {r[0]}", f"   - EN: {r[6]}", f"   - LV: {r[7]}"]
(ROOT / "docs/task-drafts/typical-b2c1-1-review.md").write_text("\n".join(L) + "\n", encoding="utf-8")
