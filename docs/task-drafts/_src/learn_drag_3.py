"""Learning tasks for twins batch 3 (teacher, 4 November): for every sentence of batch 3 a new drag task with the same
sentence, a word order or a word bank (the right words and two extra ones), marked "practice only". They are practised in
learning mode but are never evidence: not in the level test, not in the quick check, not in the count for "Learned" (the
check / use task with the same sentence is the evidence). The same principle can later be applied to every topic.
Each keeps the explanation of the batch-3 task with the same sentence. Saved to pending/ with batch 3."""
import csv
from pathlib import Path
from lib import Topic, rows, save, learning_task

ROOT = Path(__file__).resolve().parents[3]
SRC = list(csv.reader((ROOT / "docs/task-drafts/pending/twins-3.csv").open(encoding="utf-8-sig")))[1:]
LINKS = []


def why(n):
    r = SRC[n - 1]
    return (r[6], r[7].replace("*", "*"))


def order(n, sentence, also=()):
    r = SRC[n - 1]
    Topic(r[0]).order(r[1], sentence, also=list(also) or None, why=why(n)); learning_task(); LINKS.append(n)


def bank(n, q, ans, extra):
    r = SRC[n - 1]
    Topic(r[0]).bank(r[1], q, ans, extra, why=why(n)); learning_task(); LINKS.append(n)


bank(1, "If I weren't so impatient, I ___ ___ sold my flat so cheaply last spring.", ["wouldn't", "have"], ["won't", "had"])
bank(2, "If she ___ ___ German at school, she would be able to understand her new colleagues now.", ["had", "learned"], ["has", "learning"])
order(3, "if she were more patient she wouldn't have shouted at him", ["she wouldn't have shouted at him if she were more patient"])
bank(4, "If he ___ more confident, he ___ asked for a pay rise.", ["were", "would have"], ["would be", "will have"])
order(5, "had we booked earlier we would be on the beach now", ["we would be on the beach now had we booked earlier"])
bank(6, "___ I ___ the contract more carefully, I wouldn't be paying these fees now.", ["Had", "read"], ["Did", "reading"])
order(7, "had she not missed the train she would be here now", ["she would be here now had she not missed the train"])
bank(8, "Had the software ___ ___ earlier, we would not be fixing these errors now.", ["been", "tested"], ["be", "testing"])
order(9, "the coach told us to warm up before every match")
bank(10, "He ___ ___ that the shop was closed.", ["told", "me"], ["said", "to"])
bank(11, "My sister said she ___ call me as soon as she ___.", ["would", "landed"], ["will", "would land"])
order(12, "the agent said I might need a visa")
order(13, "she asked me how to start")
order(14, "they asked what time they should arrive")
bank(15, "He asked whether or not ___ ___ coming.", ["I", "was"], ["did", "am"])
bank(16, "Mr Ozols asked whether the invoices ___ ___ sent.", ["had", "been"], ["have", "being"])
bank(17, "She advised me ___ ___ a second opinion before the operation.", ["to", "get"], ["getting", "for"])
bank(18, "My colleague urged me ___ have the figures ___ before submitting the report.", ["to", "checked"], ["for", "checking"])
order(19, "she threatened to call the police")
bank(20, "The client complained ___ the delivery ___ been three days late.", ["that", "had"], ["about", "have"])
order(21, "we weren't sure where to go")
order(22, "she didn't know who to ask")
order(23, "we can't decide whether to book the hotel")
order(24, "it remains unclear how we will pay for the repairs")
bank(25, "___ arrives last has to wash the dishes.", "Whoever", ["Whomever", "Whatever"])
order(26, "whatever you decide I'll support you", ["I'll support you whatever you decide"])
order(27, "whoever finishes first can go home")
order(28, "why the system failed remains to be explained")
bank(29, "I finished work. ___, I went to the gym.", "After that", ["After", "Since then"])
bank(30, "___ it rained all day, we enjoyed our trip.", "Although", ["Because of", "Despite"])
order(31, "after finishing the exam we went out to celebrate", ["we went out to celebrate after finishing the exam"])
order(32, "the match was cancelled because it was snowing", ["because it was snowing the match was cancelled"])
bank(33, "___ homeless often sleep in the station in winter.", "The", ["A", "An"])

assert LINKS == list(range(1, 34)), LINKS
save("pending/learn-drag-3.csv")

out = list(csv.reader((ROOT / "docs/task-drafts/pending/learn-drag-3.csv").open(encoding="utf-8-sig")))[1:]
L = ["# Learning drag tasks for twins batch 3 (33)", "",
     "One new drag task for every sentence of batch 3: the same sentence as a word order, or as a word bank with the right words and two extra ones. "
     "Marked *practice only*: practised in learning mode, never evidence (not in the level test, the quick check or the count for *Learned*). "
     "Only natural word orders are accepted (both clause orders around *if / when / because / whatever*). Each keeps the explanation of its batch-3 task.", ""]
cur = None
for n, r in enumerate(out, 1):
    if (r[0], r[1]) != cur: cur = (r[0], r[1]); L += ["", f"## {r[0]} · {r[1]}", ""]
    s = SRC[n - 1]
    extra = (" · " + r[5].replace("bank: ", "words: ").replace(" | ", " / ")) if r[5] else ""
    L += [f"{n}. *{r[2]}* · {r[3]} → **{r[4].replace(' | ', ' / ')}**{extra}" + (" · practice only" if r[11] == "yes" else " · NOT practice only!"),
          f"   - same sentence as batch 3, no. {n}: {s[3]} → {s[4].split(' | ')[0]}"]
(ROOT / "docs/task-drafts/pending/learn-drag-3-review.md").write_text("\n".join(L) + "\n", encoding="utf-8")
print("33 learning tasks:", sum(1 for r in out if r[2] == "order"), "word orders,", sum(1 for r in out if r[2] == "gap"), "word banks; practice only:", sum(1 for r in out if r[11] == "yes"))
