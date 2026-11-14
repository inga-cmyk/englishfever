"""Batch 4, point shall (A2.1): Shall I …? (offers) and Shall we …? (suggestions), also What / Where / When shall we …?
Murphy unit 22 (will/shall 2: Shall I …? Shall we …? to ask somebody's opinion, in offers and suggestions; shall is used
with I and we) and unit 21 (I'll … for an offer as a statement). Should I …? / Can I …? / Could I …? / Do you want me to …?
are also correct offers and Let's … / Why don't we …? correct suggestions: they are never a wrong option, and no typed gap
here has shall itself as the answer (the gaps are the verb after shall or the question word, so every answer is fixed).
The word orders are all question-word questions: plain() turns 'to make a question' into 'Put the words in order.', and the
cards of a yes/no question (shall i carry your bag) would also make a correct statement (I shall carry your bag)."""
from lib import gp, od, mc, tx, mt, learning_task
T = "Future: will, going to, present continuous"
L = "A2.1"


def base(ok, bad):
    """After shall: the base verb (the Latvian line shows to / -ing in the wrong example only: a bare 'to' reads as Latvian)."""
    return (f"After *shall* comes the base verb, without *to* or *-ing*: *{ok}* (not *{bad}*).",
            f"Aiz *shall* lieto pamatformu: *{ok}* (nevis *{bad}*).")


def offer(ok):
    """Shall I …? as an offer."""
    return (f"*Shall I…?* offers to do something for somebody: *{ok}* We don't use *Will I…?* or *Do I…?* for an offer.",
            f"*Shall I…?* piedāvā palīdzību: *{ok}* Piedāvājumam nelieto *Will I…?* vai *Do I…?*.")


def sugg(ok):
    """Shall we …? as a suggestion."""
    return (f"*Shall we…?* suggests doing something together: *{ok}* *Will we…?* and *Do we…?* ask about facts or the future; they don't make a suggestion.",
            f"*Shall we…?* ir ierosinājums darīt kaut ko kopā: *{ok}* *Will we…?* un *Do we…?* jautā par faktiem vai nākotni; ierosinājumam tos nelieto.")


def wh(ok, bad):
    """Question word + shall + we / I + base verb."""
    return (f"Question word, then *shall*, then *we* or *I*, then the base verb: *{ok}* (not *{bad}*).",
            f"Jautājamais vārds, tad *shall*, tad *we* vai *I*, tad pamatforma: *{ok}* (nevis *{bad}*).")


# ---------- choice (7) ----------
mc(T, L, 2, "Choose the correct option: Your hands are full. ___ I open the door?", "Shall", ["Will", "Do"],
   *offer("Shall I open the door?"))   # Murphy 22: Shall I …? = Do you want me to …?; the situation makes it an offer (Will I …? / Do I …? are questions elsewhere)
mc(T, L, 2, "Choose the correct option: Shall we ___ a break?", "have", ["to have", "having", "had"],
   *base("Shall we have a break?", "Shall we to have / having"))
mc(T, L, 2, "Which sentence is correct?", "Shall I help you with your suitcase?",
   ["Shall I to help you with your suitcase?", "Shall I helping you with your suitcase?", "Shall I helped you with your suitcase?"],
   *base("Shall I help you with your suitcase?", "Shall I to help"))
mc(T, L, 2, "Which sentence is correct?", "Where shall we have lunch?",
   ["Where we shall have lunch?", "Where shall we to have lunch?", "Where shall have we lunch?"],
   *wh("Where shall we have lunch?", "Where we shall have lunch?"))
mc(T, L, 2, "Which sentence is NOT correct?", "Shall we to meet at six?",
   ["Shall I turn off the music?", "Where shall we sit?", "What shall we buy for Tom?"],
   "After *shall* comes the base verb, without *to*: *Shall we meet at six?* The others are correct: an offer (*Shall I…?*) and two questions with *Where / What shall we…?*.",
   "Aiz *shall* lieto pamatformu bez *to*: *Shall we meet at six?* Pārējie teikumi ir bez kļūdām: piedāvājums (*Shall I…?*) un divi jautājumi ar *Where / What shall we…?*.")
mc(T, L, 2, "Which sentence is NOT correct?", "Shall you call me later?",
   ["Shall we walk home?", "What time shall we leave?", "Shall I order a pizza?"],
   "In questions *shall* goes with *I* and *we* only. To ask somebody to do something, say *Can you…?* or *Will you…?*: *Can you call me later?*",
   "Jautājumos *shall* lieto vienīgi ar *I* un *we*. Lai kādu palūgtu kaut ko izdarīt, saka *Can you…?* vai *Will you…?*: *Can you call me later?*")   # Murphy 22: shall with I and we
mc(T, L, 2, "A friend asks: 'Shall I make you a sandwich?' Choose the correct answer.", "Yes, please.",
   ["Yes, you shall.", "Yes, I shall.", "Yes, you will."],
   "To accept an offer, say *Yes, please.* (or *No, thanks.* to say no). We don't answer *Shall I…?* with a short answer with *shall* or *will*.",
   "Pieņemot piedāvājumu, saka *Yes, please.* Īsā atbilde ar *shall* vai *will* šeit nav iespējama.")

# ---------- word order (5): question-word questions, no statement can be built from the cards ----------
od(T, L, 3, "Put the words in order to make a question.", "what shall i bring to the party",
   *wh("What shall I bring to the party?", "What I shall bring…?"))
od(T, L, 3, "Put the words in order to make a question.", "how shall we get to the airport",
   *wh("How shall we get to the airport?", "How we shall get…?"))
od(T, L, 3, "Put the words in order to make a question.", "where shall i put these boxes",
   *wh("Where shall I put these boxes?", "Where I shall put…?"))
od(T, L, 3, "Put the words in order to make a question.", "which bus shall we take",
   *wh("Which bus shall we take?", "Which bus we shall take?"))
od(T, L, 3, "Put the words in order to make a question.", "what time shall we start the meeting",
   *wh("What time shall we start the meeting?", "What time we shall start…?"))

# ---------- word bank (4): the wrong chips are the mistakes of this point ----------
gp(T, L, 3, "I'm bored. ___ we go for a walk?", "Shall",
   *sugg("Shall we go for a walk?"), bank=["Shall", "Will", "Do"])   # the situation makes it a suggestion: Will we / Do we go for a walk? are questions elsewhere
gp(T, L, 3, "Shall I ___ you a taxi?", "call",
   *base("Shall I call you a taxi?", "Shall I to call / calling"), bank=["call", "to call", "calling"])
gp(T, L, 3, "What ___ ___ watch tonight?", "shall / we",
   *wh("What shall we watch tonight?", "What we shall watch?"), bank=["shall", "we", "you"])   # shall you: shall goes with I and we only (Murphy 22)
gp(T, L, 3, "Shall we ___ ___ the beach on Sunday?", "go / to",
   *base("Shall we go to the beach on Sunday?", "Shall we going to / to go"), bank=["go", "to", "going"])

# ---------- matching (1, learning) ----------
mt(T, L, 2, "Match each question with its answer.",
   [("Shall I open the window?", "Yes, please. It's hot in here."), ("Where shall we meet?", "Outside the cinema."),
    ("What shall we have for dinner?", "Fish and rice."), ("When shall I call you?", "After six. I'm at work till then.")],
   "Answer an offer (*Shall I…?*) with *Yes, please* or *No, thanks*. *Where / What / When shall we…?* asks for an idea: answer with a place, a thing or a time.",
   "Uz piedāvājumu (*Shall I…?*) atbild ar *Yes, please*. *Where / What / When shall we…?* jautā pēc ierosinājuma: atbildē ir vieta, ēdiens vai laiks.")

# ---------- typed gap (5): the verb after shall, or the question word ----------
gp(T, L, 3, "It's raining. Shall we ___ a taxi? (take)", "take",
   *base("Shall we take a taxi?", "Shall we to take"))
gp(T, L, 3, "Your phone is dead. Shall I ___ you mine? (lend)", "lend",
   *base("Shall I lend you mine?", "Shall I to lend"))
gp(T, L, 3, "Write the missing word: ___ shall I put your coat? On the chair?", "Where",
   *wh("Where shall I put your coat?", "Where I shall put…?"))
gp(T, L, 3, "I'm going to the shop. Shall I ___ you anything? (get)", "get",
   *base("Shall I get you anything?", "Shall I to get"))
gp(T, L, 3, "We're free tonight. What shall we ___? (do)", "do",
   *base("What shall we do?", "What shall we to do"))

# ---------- whole sentence (3) ----------
tx(T, L, 4, "Say it another way with *Shall I*: Do you want me to book a table?",
   "Shall I book a table? | Shall I book a table for you? | Shall I book a table for us?",
   "*Shall I…?* means *Do you want me to…?* After *shall* comes the base verb, without *to*: *Shall I book a table?*",
   "*Shall I…?* nozīmē *Do you want me to…?* Aiz *shall* lieto pamatformu bez *to*: *Shall I book a table?*")
tx(T, L, 4, "Make a question with *Where*: Shall we go to Italy this summer?",
   "Where shall we go this summer? | Where shall we go?",
   *wh("Where shall we go this summer?", "Where we shall go…?"))
tx(T, L, 4, "Make a question with *What*: Shall we cook pasta tonight?",
   "What shall we cook tonight? | What shall we cook?",
   *wh("What shall we cook tonight?", "What we shall cook…?"))
