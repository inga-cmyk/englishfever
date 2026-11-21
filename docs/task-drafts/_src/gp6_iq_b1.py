"""Indirect questions B1.1 and B1.2, points iq_wh / iq_yn (teacher, 21 November: "probably too easy; in places the answer is given
away; meaningful tasks with understandable instructions that make the learner think"). Murphy unit 50 (Do you know where ...?
Could you tell me ...? if / whether), checked against the rule card of ind_polite.

What changed against the old set (notes: gp6_iq_b1-notes.md):
- no task quotes the direct question and then gives the frame: the learner gets a situation, a frame with a gap that holds
  the subject AND the verb, or a sentence to correct;
- B1.1: present, can, is / are, present continuous, if; B1.2 adds the past (where did he park -> where he parked; did she get
  -> if she got), the present perfect, was, if / whether after I wonder / I'm not sure / Can you remember;
- frames vary (Could you tell me, Do you know, Can you tell me, I wonder, I'd like to know, I'm not sure, Can you remember,
  Could you check) and so do the settings (work, travel, learning, technology, home, shopping, relationships);
- the wrong options and chips are the real mistakes: inversion (where can I), do / does / did kept (what does it mean,
  did Maria get), did removed but the past forgotten (if Maria get, where Mark is yesterday), if left out (are there).
No save() here: the lead agent adds this module to a batch file (check: see the notes)."""
import lib
from lib import gp, od, mc, tx, rows

T = "Indirect questions (Could you tell me where...)"

# Word orders keep "to make a question" (lib.plain would shorten it); the same patch as gap_fill_a2.py, harmless elsewhere.
_plain = lib.plain
lib.plain = lambda task, typ: task.strip() if typ == "order" and task.strip() == "Put the words in order to make a question." else _plain(task, typ)
QORDER = "Put the words in order to make a question."


def oq(lv, sentence, why, lvw):
    """A question in word order: only the question is accepted (od() adds the statement 'you could tell me ...' for a bare instruction)."""
    od(T, lv, 3, QORDER, sentence, why, lvw)
    r = rows[-1]
    if r[5].startswith("also accepted: "):
        keep = [a for a in r[5][len("also accepted: "):].split(" | ") if a.split()[0] in ("could", "can", "do", "would")]
        r[5] = ("also accepted: " + " | ".join(keep)) if keep else ""


def wrap(start, cores, excuse=True, please=True):
    """Every answer to a need-based question: start + each core, with Excuse me in front and please at the end where natural."""
    out = []
    for c in cores:
        base = f"{start} {c}"
        forms = [base + "?"]
        if please: forms.append(base + ", please?")
        if excuse: forms += ["Excuse me, " + f[0].lower() + f[1:] for f in list(forms)]
        for f in forms:
            if f not in out: out.append(f)
    return out


# ================================ B1.1 (present, can, is / are, present continuous, if) ================================
L = "B1.1"

mc(T, L, 2, "Choose the correct option: Could you tell me what this word ___ ?", "means",
   ["mean", "does it mean", "it means"],
   "There is no *does* in an indirect question, so the verb itself takes *-s*: *what this word means*.",
   "Netiešajā jautājumā nav *does*, tāpēc *-s* ir pašam darbības vārdam: *what this word means*.")

gp(T, L, 3, "Do you know where ___ ___ buy a phone charger near here?", "I / can",
   "After *where* the order is like a statement: *I can buy*, not *can I buy*.",
   "Pēc *where* vārdu secība ir kā apgalvojumā: *I can buy*, nevis *can I buy*.",
   bank=["I", "can", "do"])

gp(T, L, 3, "Use the words in brackets: Can you tell me how often ___ on Sundays? (the night bus / run)",
   "the night bus runs | the night bus is running | the night bus will run",
   "*How often does the night bus run?* becomes *how often the night bus runs*: no *does*, and the verb takes *-s*.",
   "*How often does the night bus run?* kļūst par *how often the night bus runs*: bez *does*, un darbības vārdam ir *-s*.")
# blind round r17 (judge): *will run* is correct too (a timetable that starts later); its own note
lib.NOTES[len(rows) - 1] = ("the night bus will run :: Correct too: *will run* asks about the future, for example a new timetable. For a timetable that runs now, use *runs*. "
                            ":: Arī pareizi: *will run* jautā par nākotni, piemēram, par jaunu sarakstu. Par sarakstu, kas darbojas tagad, saka *runs*.")

gp(T, L, 3, "I can't hear the guide. Do you know what ___ ___ talking about?", "she / is",
   "In an indirect question the subject comes before *is*: *what she is talking about*, not *what is she*.",
   "Netiešajā jautājumā teikuma priekšmets ir pirms *is*: *what she is talking about*, nevis *what is she*.",
   bank=["she", "is", "does"])

tx(T, L, 4, "You need to print a document at work, but you can't find the printer. Ask a colleague. Start with *Do you know where*.",
   wrap("Do you know where", ["the printer is", "the printers are", "the nearest printer is", "I can find the printer", "I can find a printer",
                              "I can print", "I can print something", "I can print a document", "I can print my document",
                              "I can print this document", "I can print this", "there is a printer", "the printer is located", "I can find one", "the printer room is"]),
   "After *Do you know where* the order is like a statement: *where the printer is*, *where I can print*, not *where is the printer*.",
   "Pēc *Do you know where* vārdu secība ir kā apgalvojumā: *where the printer is*, *where I can print*, nevis *where is the printer*.")

tx(T, L, 4, "Correct the mistake: Hi Eva, could you tell me how much does the course cost? I'd like to sign up.",
   ["Hi Eva, could you tell me how much the course costs? I'd like to sign up."],
   "No *does* after *how much* in an indirect question, and the verb takes *-s*: *how much the course costs*.",
   "Netiešajā jautājumā pēc *how much* nav *does*, un darbības vārdam ir *-s*: *how much the course costs*.")

od(T, L, 3, "Put the words in order.", "i wonder why my laptop is so slow",
   "After *I wonder why* the order is like a statement: *why my laptop is so slow*. It is not a question, so it ends with a full stop.",
   "Pēc *I wonder why* vārdu secība ir kā apgalvojumā: *why my laptop is so slow*. Tas nav jautājums, tāpēc beigās ir punkts.")

oq(L, "can you tell me how the coffee machine works",
   "*How does the coffee machine work?* inside *Can you tell me*: no *does*, and *works* with *-s*.",
   "*How does the coffee machine work?* pēc *Can you tell me*: bez *does*, un *works* ar *-s*.")

mc(T, L, 2, "Choose the correct option: I'd like to know ___ any free tables for tonight.", "if there are",
   ["are there", "if are there", "there are"],
   "A yes/no question inside another sentence needs *if* and the order of a statement: *if there are*.",
   "Jautājumam ar atbildi jā / nē cita teikuma iekšā vajag *if* un vārdu secību kā apgalvojumā: *if there are*.")

tx(T, L, 4, "You are visiting a new city and want to see the old town, but you don't know the way. Ask someone in the street. Start with *Could you tell me how*.",
   wrap("Could you tell me how", ["I can get to the old town", "I get to the old town", "we can get to the old town", "we get to the old town",
                                   "I can find the old town", "I can walk to the old town", "to get to the old town", "far the old town is",
                                   "far it is to the old town", "long it takes to get to the old town", "long it takes to walk to the old town",
                                   "I can get to the old town from here", "I get to the old town from here", "to get to the old town from here"]),
   "After *how* the order is like a statement: *how I can get to the old town*, *how far the old town is*. *How to get to the old town* is correct too.",
   "Pēc *how* vārdu secība ir kā apgalvojumā: *how I can get to the old town*, *how far the old town is*. Arī *how to get to the old town* ir pareizā atbilde.")

gp(T, L, 3, "Use the words in brackets. Add any missing word: I'd like to know ___ a balcony. We'd love a view of the sea. (our room / have)",
   "if our room has | whether our room has | if our room has got | whether our room has got | if our room will have | whether our room will have",
   "A yes/no question inside another sentence: *if* (or *whether*) + subject + verb: *if our room has a balcony*.",
   "Jautājums ar atbildi jā / nē cita teikuma iekšā: *if* (vai *whether*) + teikuma priekšmets + darbības vārds: *if our room has a balcony*.")
# blind round r17 (judge): *will have* is correct too (the room is not given yet); its own note
lib.NOTES[len(rows) - 1] = " || ".join(a + " :: Correct too: *will have* asks about the room you will get. About the room as it is, use *has*: *if our room has a balcony*. "
                                       ":: Arī pareizi: *will have* jautā par istabu, ko jūs saņemsiet. Par istabu, kāda tā ir, saka *has*: *if our room has a balcony*."
                                       for a in ("if our room will have", "whether our room will have"))

gp(T, L, 3, "Can you tell me ___ ___ ___ English? I need help with the menu.", "if / the waiter / speaks",
   "*Does the waiter speak English?* becomes *if the waiter speaks English*: *if*, no *does*, and *speaks* with *-s*.",
   "*Does the waiter speak English?* kļūst par *if the waiter speaks English*: *if*, bez *does*, un *speaks* ar *-s*.",
   bank=["if", "the waiter", "speaks", "does", "speak"])

# ============== B1.2 (past simple without did, was, present perfect, if / whether, other frames) ==============
L = "B1.2"

gp(T, L, 3, "Use the words in brackets: Do you know where ___ the car last night? It isn't in the garage. (Tom / park)",
   "Tom parked",
   "*Where did Tom park?* becomes *where Tom parked*: *did* goes, and the verb itself shows the past.",
   "*Where did Tom park?* kļūst par *where Tom parked*: *did* pazūd, un pagātni rāda darbības vārds.")

gp(T, L, 3, "I wonder ___ ___ ___ my email. She hasn't answered yet.", "if / Maria / got",
   "*Did Maria get my email?* becomes *if Maria got my email*: *if*, no *did*, and the verb in the past.",
   "*Did Maria get my email?* kļūst par *if Maria got my email*: *if*, bez *did*, un darbības vārds pagātnē.",
   bank=["if", "Maria", "got", "get", "did"])

mc(T, L, 2, "Choose the correct option: Could you check ___ the parcel yet?", "if they have sent",
   ["have they sent", "if have they sent", "did they send"],
   "A yes/no question inside *Could you check*: *if* + subject + verb: *if they have sent*.",
   "Jautājums ar atbildi jā / nē pēc *Could you check*: *if* + teikuma priekšmets + darbības vārds: *if they have sent*.")

od(T, L, 3, "Put the words in order.", "i'd like to know where you learned to cook like that",
   "After *I'd like to know where* the order is like a statement and there is no *did*: *where you learned*.",
   "Pēc *I'd like to know where* vārdu secība ir kā apgalvojumā, un *did* nav: *where you learned*.")

tx(T, L, 4, "Your colleague has a great new laptop bag, and you would like one like it. Ask her about the shop. Start with *Could you tell me where*.",
   wrap("Could you tell me where", [f"you {v} {o}" for v in ("bought", "got") for o in ("it", "it from", "that bag", "that bag from", "your bag", "your bag from", "your new bag", "your laptop bag", "that laptop bag")]
        + [f"I {m} {v} one" for m in ("can", "could") for v in ("buy", "get")] + ["I can buy one like it", "I can get one like it", "I can buy the same bag", "I can get the same bag", "the shop is", "that shop is"],
        excuse=False),
   "*Where did you buy it?* becomes *where you bought it*: no *did*, and the verb in the past. *Where I can buy one* is correct too.",
   "*Where did you buy it?* kļūst par *where you bought it*: bez *did*, un darbības vārds pagātnē. Arī *where I can buy one* ir pareizā atbilde.")

gp(T, L, 3, "Do you know how long ___ ___ ___ in this company? She knows everyone.", "Anna / has / worked",
   "After *how long* the order is like a statement: *Anna has worked*, not *has Anna worked* or *does Anna work*.",
   "Pēc *how long* vārdu secība ir kā apgalvojumā: *Anna has worked*, nevis *has Anna worked* vai *does Anna work*.",
   bank=["Anna", "has", "worked", "does", "work"])

tx(T, L, 4, "Correct the mistake: Dear Mr Kalns, could you tell me when did you send the invoice? We still haven't received it.",
   ["Dear Mr Kalns, could you tell me when you sent the invoice? We still haven't received it."],
   "No *did* in an indirect question; the verb itself is in the past: *when you sent the invoice*.",
   "Netiešajā jautājumā nav *did*; pagātnē ir darbības vārds: *when you sent the invoice*.")

oq(L, "do you know why the meeting was cancelled",
   "*Why was the meeting cancelled?* inside *Do you know*: the subject comes before *was*: *why the meeting was cancelled*.",
   "*Why was the meeting cancelled?* pēc *Do you know*: teikuma priekšmets ir pirms *was*: *why the meeting was cancelled*.")

gp(T, L, 3, "Use the words in brackets. Add any missing word: Can you remember ___ the back door before we left? (you / lock)",
   "if you locked | whether you locked | if you had locked | whether you had locked",
   "*Did you lock the back door?* becomes *if you locked the back door*: *if*, no *did*, and the verb in the past.",
   "*Did you lock the back door?* kļūst par *if you locked the back door*: *if*, bez *did*, un darbības vārds pagātnē.")

mc(T, L, 2, "Choose the correct option: Do you know where ___ yesterday? He didn't come to work.", "Mark was",
   ["was Mark", "Mark is", "Mark has been"],
   "*Where was Mark yesterday?* becomes *where Mark was yesterday*: the subject first, and the past stays because of *yesterday*.",
   "*Where was Mark yesterday?* kļūst par *where Mark was yesterday*: sākumā teikuma priekšmets, un pagātne paliek *yesterday* dēļ.")

tx(T, L, 4, "You left your umbrella in the meeting room this morning, and now it isn't there. Ask the receptionist. Start with *Do you know if*.",
   wrap("Do you know if", [f"{p} {v} {o}" for p in ("anyone", "someone", "somebody", "anybody") for v in ("has found", "found") for o in ("it", "an umbrella", "my umbrella")]
        + [f"{p} {v} {o}" for p in ("anyone", "someone", "somebody", "anybody") for v in ("has seen", "saw", "has taken", "took") for o in ("it", "my umbrella")]
        + [f"{p} {v}" for p in ("anyone", "someone", "somebody", "anybody") for v in ("has handed it in", "handed it in", "has handed in an umbrella", "handed in an umbrella", "has handed in my umbrella", "handed in my umbrella")]
        + [f"{s} {v}" for s in ("it", "my umbrella", "an umbrella") for v in ("has been found", "was found", "has been handed in", "was handed in")]
        + [f"the {p} {v} {o}" for p, h in (("cleaner", "has"), ("cleaners", "have")) for v in (h + " found", "found", h + " taken", "took") for o in ("it", "my umbrella")],   # blind round r17
        excuse=False, please=False),
   "*Has anyone found it?* / *Did anyone find it?* become *if anyone has found it* / *if anyone found it*: *if* + subject + verb, no *did*.",
   "*Has anyone found it?* / *Did anyone find it?* kļūst par *if anyone has found it* / *if anyone found it*: *if* + teikuma priekšmets + darbības vārds, bez *did*.")

gp(T, L, 3, "I'm not sure ___ ___ ___ ___ the tickets yet. Let me check my email.", "if / we / have / booked",
   "A yes/no question after *I'm not sure*: *if* + subject + verb: *if we have booked*, not *if have we booked*.",
   "Jautājums ar atbildi jā / nē pēc *I'm not sure*: *if* + teikuma priekšmets + darbības vārds: *if we have booked*, nevis *if have we booked*.",
   bank=["if", "we", "have", "booked", "do", "book"])   # blind round r17: *did* also built *if we did book … yet* (emphatic, American); *do* keeps the question mistake (*if do we book*)
