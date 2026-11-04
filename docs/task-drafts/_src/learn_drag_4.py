"""Learning drag tasks, set 2 (teacher, 4 November, option A): the topic-levels that had no drag task at all get five each.
Every task uses the sentence of an existing check / use task of that topic-level (named in the review), as a word order
(only natural orders: both clause orders around if / despite) or a word bank (the right words and two that do not fit).
All are *practice only* (learning tasks, never evidence). Saved to pending/ until the teacher has seen them."""
import csv
from pathlib import Path
from lib import Topic, rows, save, learning_task

ROOT = Path(__file__).resolve().parents[3]
LINKS = []


def order(topic, lv, src, sentence, why, also=()):
    Topic(topic).order(lv, sentence, also=list(also) or None, why=why); learning_task(); LINKS.append(src)


def bank(topic, lv, src, q, ans, extra, why):
    Topic(topic).bank(lv, q, ans, extra, why=why); learning_task(); LINKS.append(src)


def both(a, b):
    """The two natural clause orders."""
    return f"{b} {a}"


# ── Auxiliary verbs · A2.1 ──
AUX = "Auxiliary verbs: be, do, have (Are you…? Do you…? Have you…?)"
Q = ("A question: the helping verb (*do / does / are*) comes before the subject.", "Jautājumā palīgdarbības vārds (*do / does / are*) ir pirms teikuma priekšmeta.")
SHORT = ("A short answer repeats the helping verb of the question: *Did you…? Yes, I did.*", "Īsajā atbildē atkārto jautājuma palīgdarbības vārdu: *Did you…? Yes, I did.*")
order(AUX, "A2.1", "aux-verbs-1.csv · line 19", "does your brother play football", Q)
order(AUX, "A2.1", "aux-verbs-1.csv · line 20", "are you at work now", Q)
order(AUX, "A2.1", "aux-verbs-1.csv · line 27", "when does she work", ("A question with *When*: *When* + *does* + subject + base form.", "Jautājums ar *When*: *When* + *does* + teikuma priekšmets + pamatforma."))
bank(AUX, "A2.1", "aux-verbs-1.csv · line 38", "'Did you enjoy the film?' 'Yes, I ___.'", "did", ["do", "enjoyed"], SHORT)
bank(AUX, "A2.1", "aux-verbs-1.csv · line 44", "'Is it raining?' 'Yes, it ___.'", "is", ["does", "raining"], SHORT)

# ── Present perfect or past simple · B1.1 ──
PPS = "Present perfect or past simple"
NOW = ("Up to now (*since 2010*, *this morning* while it is still morning): *have* + 3rd form.", "Līdz šim brīdim (*since 2010*, *this morning*, kamēr vēl ir rīts): *have* + 3. forma.")
DONE = ("A finished time (*from 2010 to 2014*, *yesterday*): past simple.", "Pabeigts laiks (*from 2010 to 2014*, *yesterday*): Past Simple.")
bank(PPS, "B1.1", "compare-past-1.csv · line 28", "___ you ___ Anna this morning? It's only ten o'clock.", ["Have", "seen"], ["Did", "saw"], NOW)
bank(PPS, "B1.1", "compare-past-1.csv · line 25", "I ___ there from 2010 to 2014. Now I work in Riga.", "worked", ["have worked", "work"], DONE)
bank(PPS, "B1.1", "compare-past-1.csv · line 24", "I ___ here since 2010. I still work here.", "have worked", ["worked", "work"], NOW)
order(PPS, "B1.1", "compare-past-1.csv · line 19", "I have never ridden a horse", ("Your whole life up to now: *have never* + 3rd form.", "Visa dzīve līdz šim: *have never* + 3. forma."))
order(PPS, "B1.1", "compare-past-1.csv · line 27", "did you see Anna yesterday", DONE)

# ── Second conditional · B2.1 ──
C2 = "Second conditional (if + past, would)"
SEC = ("An imagined present: *if* + past, *would* + base form.", "Iedomāta tagadne: *if* + pagātne, *would* + pamatforma.")
order(C2, "B2.1", "app/content/items.json · cs-B21-1a", "if I were you I'd think twice about that offer", ("Advice: *If I were you, I'd…*", "Padoms: *If I were you, I'd…*"), ["I'd think twice about that offer if I were you"])
bank(C2, "B2.1", "app/content/items.json · cs-B21-3a", "If the company ___ more flexible hours, people ___ happier.", ["offered", "would be"], ["would offer", "will be"], SEC)
order(C2, "B2.1", "app/content/items.json · cs-B21-4a", "if I knew the answer I would tell you", SEC, ["I would tell you if I knew the answer"])
bank(C2, "B2.1", "app/content/items.json · cs-B21-5a", "I would be grateful if you ___ send me the report by Friday.", "could", ["can to", "would to"],
     ("A polite request: *I would be grateful if you could…*", "Pieklājīgs lūgums: *I would be grateful if you could…*"))
order(C2, "B2.1", "twins-1.csv · line 47", "if I had a garden I would grow vegetables", SEC, ["I would grow vegetables if I had a garden"])

# ── Third conditional · B2.1 ──
C3 = "Third conditional (if + had done, would have done)"
THIRD = ("An imagined past: *if* + *had* + 3rd form, *would / could have* + 3rd form.", "Iedomāta pagātne: *if* + *had* + 3. forma, *would / could have* + 3. forma.")
bank(C3, "B2.1", "app/content/items.json · ct-B21-1a", "She would have passed the exam if she ___ ___ harder.", ["had", "studied"], ["has", "studying"], THIRD)
order(C3, "B2.1", "app/content/items.json · ct-B21-3a-r2", "if I had seen the sign I wouldn't have parked there", THIRD, ["I wouldn't have parked there if I had seen the sign"])
order(C3, "B2.1", "app/content/items.json · ct-B21-4a", "if the team had been better prepared we would have won", THIRD, ["we would have won if the team had been better prepared"])
bank(C3, "B2.1", "app/content/items.json · ct-B21-5a", "If you had told us earlier, we ___ ___ adjusted the schedule.", ["could", "have"], ["can", "had"], THIRD)
order(C3, "B2.1", "twins-2.csv · line 26", "if I had remembered her birthday I would have called her", THIRD, ["I would have called her if I had remembered her birthday"])

# ── Third conditional · B2.2 ──
bank(C3, "B2.2", "app/content/items.json · ct-B22-1a-r2", "If she ___ ___ the warning, she would have avoided the accident.", ["had", "heard"], ["has", "hearing"], THIRD)
bank(C3, "B2.2", "app/content/items.json · ct-B22-3a-r2", "If he hadn't been driving so fast, he ___ ___ lost his licence.", ["wouldn't", "have"], ["won't", "hadn't"], THIRD)
order(C3, "B2.2", "app/content/items.json · ct-B22-4a-r5", "if I'd known about the traffic I would've left earlier",
      ("*If I'd known* = *If I had known*; no *would have* after *if*.", "*If I'd known* = *If I had known*; aiz *if* nelieto *would have*."), ["I would've left earlier if I'd known about the traffic"])
bank(C3, "B2.2", "app/content/items.json · ct-B22-5a", "If I had ___ the impact of my decision, I would have ___ differently.", ["realised", "acted"], ["realise", "act"], THIRD)
order(C3, "B2.2", "twins-1.csv · line 51", "if we had known about the problem we would have called you", THIRD, ["we would have called you if we had known about the problem"])

# ── Contrast, purpose and reason · B2.1 ──
CT = "Contrast, purpose and reason"
DESP = ("*despite / in spite of* + noun or *-ing*; *despite the fact that* + subject + verb.", "*despite / in spite of* + lietvārds vai *-ing*; *despite the fact that* + teikuma priekšmets + darbības vārds.")
order(CT, "B2.1", "twins-1.csv · line 34", "despite the delay we arrived on time", DESP, ["we arrived on time despite the delay"])   # "despite feeling ill" is already a word order at B1.2
bank(CT, "B2.1", "twins-1.csv · line 35", "In ___ ___ the cold, they went swimming.", ["spite", "of"], ["despite", "for"], DESP)
order(CT, "B2.1", "conjunctions-1.csv · line 81", "despite the rain the match went ahead", DESP, ["the match went ahead despite the rain"])
bank(CT, "B2.1", "conjunctions-1.csv · line 70", "They walked quietly so as ___ ___ wake the baby.", ["not", "to"], ["no", "don't"], ("Purpose, negative: *so as not to* + base form.", "Nolūks noliegumā: *so as not to* + pamatforma."))
order(CT, "B2.1", "conjunctions-1.csv · line 69", "we went out despite the fact that it was raining", DESP, ["despite the fact that it was raining we went out"])

# ── Indirect questions (Could you tell me where…) · B2.1 ──
IP = "Indirect questions (Could you tell me where...)"
ORD = ("After *Could you tell me / Do you know / Would you mind telling me* the word order is like a statement.", "Aiz *Could you tell me / Do you know / Would you mind telling me* vārdu secība ir kā apgalvojumā.")
order(IP, "B2.1", "app/content/items.json · ip-B21-1a", "would you mind telling me how long the repair will take", ORD)
order(IP, "B2.1", "app/content/items.json · ip-B21-3a-r3", "could you tell me why the order didn't arrive", ORD)
bank(IP, "B2.1", "app/content/items.json · ip-B21-4a-r2", "I'd like to know where you ___ last night.", "went", ["did go", "did you go"], ORD)
order(IP, "B2.1", "twins-1.csv · line 72", "do you know when the shop closes", ORD)
order(IP, "B2.1", "twins-1.csv · line 70", "do you know what time it opens", ORD)

# ── Reported questions and requests · B2.1 ──
RQ = "Reported questions and requests"
REP = ("A reported question has statement order (*if I could help her*); a request: *ask / tell* + person + (*not*) *to*.", "Atstāstītā jautājumā ir apgalvojuma secība (*if I could help her*); lūgumam: *ask / tell* + persona + (*not*) *to*.")
order(RQ, "B2.1", "app/content/items.json · rq-B21-1a", "she asked if I could help her", REP)
bank(RQ, "B2.1", "app/content/items.json · rq-B21-2a", "The nurse told me ___ ___ touch it.", ["not", "to"], ["don't", "no"], REP)
order(RQ, "B2.1", "app/content/items.json · rq-B21-3a-r2", "Lena asked me to send her the invoice", REP)
bank(RQ, "B2.1", "app/content/items.json · rq-B21-4a", "He asked me what time ___ ___.", ["it", "was"], ["did", "does"], REP)
order(RQ, "B2.1", "app/content/items.json · rq-B21-5a", "the customer asked how long the repair would take", REP)

assert len(rows) == len(LINKS) == 40, len(rows)
save("pending/learn-drag-4.csv")

out = list(csv.reader((ROOT / "docs/task-drafts/pending/learn-drag-4.csv").open(encoding="utf-8-sig")))[1:]
L = ["# Learning drag tasks, set 2 (40)", "",
     "Option A: the eight topic-levels that had no drag task get five learning tasks each. Each uses the sentence of an existing check / use task of that topic-level (named below), "
     "as a word order (only natural orders) or a word bank (the right words and two that do not fit). All are *practice only*: practised, never counted as evidence. Not added yet.", ""]
cur = None
for n, (r, src) in enumerate(zip(out, LINKS), 1):
    if (r[0], r[1]) != cur: cur = (r[0], r[1]); L += ["", f"## {r[0]} · {r[1]}", ""]
    extra = (" · " + r[5].replace("bank: ", "words: ").replace(" | ", " / ")) if r[5] else ""
    L += [f"{n}. *{r[2]}* · {r[3]} → **{r[4].replace(' | ', ' / ')}**{extra}" + ("" if r[11] == "yes" else " · NOT practice only!"),
          f"   - EN: {r[6]}", f"   - LV: {r[7]}", f"   - sentence from: {src}"]
(ROOT / "docs/task-drafts/pending/learn-drag-4-review.md").write_text("\n".join(L) + "\n", encoding="utf-8")
print("40 learning tasks:", sum(1 for r in out if r[2] == "order"), "word orders,", sum(1 for r in out if r[2] == "gap"), "word banks; practice only:", sum(1 for r in out if r[11] == "yes"))
