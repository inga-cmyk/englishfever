"""Batch 4, point requests (A2.2): polite requests and permission, Could you …? Can I …? Would you …? Murphy unit 37
(A asking people to do things: Can you / Could you …?; B asking for things: Can I have / Could I have …?; C asking to do
things: Can I / Could I / May I …?, may is more formal; answers Yes, of course / Sure / Go ahead). Would you …? as a request:
Murphy 36 (Would you please be quiet?). No gap here has the modal open on its own (___ you help me? takes can / could / will /
would): every choice has only one fitting option, and the typed gaps are the verb after the modal, the person (I) or go ahead.
Not here (B1 or another point): Would you mind + -ing, Do you mind if, Would you like (point would_like), Shall I (point shall).
Word orders: lib.od() also accepts the statement (you could …), so every order was chosen so that the statement is natural too."""
from lib import gp, od, mc, tx, mt, learning_task
T = "Modal verbs"
L = "A2.2"


def base(ok, bad):
    """After the modal of a request: the base verb."""
    return (f"After *can / could / would / may* comes the base verb, without *to* or *-ing*: *{ok}* (not *{bad}*).",
            f"Aiz *can / could / would / may* ir darbības vārda pamatforma bez *to* un bez *-ing*: *{ok}* (nevis *{bad}*).")


def you(ok):
    """Can / Could / Would you …? = you do it."""
    return (f"To ask somebody to do something: *Can / Could / Would you* + base verb: *{ok}*",
            f"Lūdzot, lai cits cilvēks kaut ko izdarītu: *Can / Could / Would you* + pamatforma: *{ok}*")


def me(ok):
    """Can / Could / May I …? = I do it."""
    return (f"To ask if you may do something yourself: *Can / Could / May I* + base verb: *{ok}*",
            f"Jautājot atļauju kaut ko darīt pašam: *Can / Could / May I* + pamatforma: *{ok}*")


def lend(i_form, you_form):
    """borrow (I take it) / lend (you give it)."""
    return (f"*{i_form}* = I take it and give it back later. *{you_form}* = you give it to me for a short time. Not *borrow me*, not *Can I lend…?*",
            f"*{i_form}* = es aizņemos (paņemu uz laiku). *{you_form}* = jūs man aizdodat. Nevis *borrow me*, nevis *Can I lend…?*")


# choose (7)
mc(T, L, 2, "Choose the correct option: Could you ___ the window, please?", "open", ["to open", "opening", "opens"],
   *base("Could you open the window?", "Could you to open"))
mc(T, L, 2, "Which sentence is correct?", "Would you check my email, please?",
   ["Would you to check my email, please?", "Would you checking my email, please?", "Would you checked my email, please?"],
   *base("Would you check my email?", "Would you to check"))
mc(T, L, 2, "Which sentence is NOT correct?", "May you help me with this form?",
   ["May I use your charger?", "Could you call me back later?", "Can I try this jacket on?"],
   "*May* asks for permission with *I*: *May I use your charger?* To ask somebody to do something, say *Can / Could / Would you…?*: *Could you help me with this form?* The other sentences are correct.",
   "*May* lieto atļaujas lūgšanai ar *I*: *May I use your charger?* Lūdzot, lai cits cilvēks kaut ko izdarītu, saka *Can / Could / Would you…?*: *Could you help me with this form?* Pārējie teikumi ir bez kļūdām.")
mc(T, L, 2, "Choose the correct option: Can I ___ a coffee and a croissant, please?", "have", ["to have", "having"],
   "To ask for something: *Can I have…?* (or *Could I have…?*), with the base verb: *Can I have a coffee, please?*",
   "Lūdzot kaut ko saņemt: *Can I have…?* (vai *Could I have…?*) ar pamatformu: *Can I have a coffee, please?*")
mc(T, L, 2, "Which sentence is correct?", "Can I borrow your pen for a moment?",
   ["Can you borrow me your pen for a moment?", "Can I to borrow your pen for a moment?", "Can I lend your pen for a moment?"],
   *lend("Can I borrow your pen?", "Can you lend me your pen?"))
mc(T, L, 2, "Which sentence is correct?", "May I see your passport, please?",
   ["May I to see your passport, please?", "May I seeing your passport, please?", "May you show me your passport, please?"],
   "*May I* + base verb asks for permission politely: *May I see your passport?* There is no *May you…?* request: *Could you show me your passport?*",
   "*May I* + pamatforma pieklājīgi lūdz atļauju: *May I see your passport?* Lūgums *May you…?* nepastāv: *Could you show me your passport?*")
mc(T, L, 2, "Which sentence is correct?", "Can you give me a lift to work?",
   ["Do you can give me a lift to work?", "Can you to give me a lift to work?", "Can you giving me a lift to work?"],
   "A question with *can* needs no *do*: *Can you* + base verb: *Can you give me a lift?* (not *Do you can…?*).",
   "Jautājumā ar *can* nelieto *do*: *Can you* + pamatforma: *Can you give me a lift?* (nevis *Do you can…?*).")

# type a word (5)
gp(T, L, 3, "Could you ___ this word to me? (explain)", "explain", *base("Could you explain this word?", "Could you to explain"))
gp(T, L, 3, "Write the missing word: Can ___ borrow your charger? Mine is at home.", "I | we",
   "*Can I…?* asks if I may do something: *Can I borrow your charger?* (I take it for a short time). *Mine is at home* shows who needs it.",
   "*Can I…?* jautā, vai es drīkstu kaut ko darīt: *Can I borrow your charger?* (es aizņemos uz laiku). *Mine is at home* parāda, ka lādētājs vajadzīgs man.")
gp(T, L, 3, "Would you ___ quiet, please? I'm on the phone. (be)", "be", *base("Would you be quiet, please?", "Would you are quiet"))
gp(T, L, 3, "Write the missing word: 'Can I take a photo of your garden?' 'Yes, go ___.'", "ahead | on",
   "To say yes to *Can I…?*: *Yes, go ahead.* (also *Sure.* or *Yes, of course.*).",
   "Lai atļautu (atbilde uz *Can I…?*): *Yes, go ahead.* (arī *Sure.* vai *Yes, of course.*).")
gp(T, L, 3, "Could your sister ___ me to the airport tomorrow? (take)", "take",
   "After *could* the verb has no *-s*, also with *he / she*: *Could your sister take me?* (not *takes*).",
   "Aiz *could* darbības vārdam nav *-s* arī ar *he / she*: *Could your sister take me?* (nevis *takes*).")

# whole sentence (3)
tx(T, L, 4, "Start with *Could you*: Please wait here.",
   "Could you wait here? | Could you please wait here? | Could you wait here, please? | Could you wait here for me? | Could you please wait here for me? | Could you wait here for me, please?",
   *you("Could you wait here, please?"))
tx(T, L, 4, "Start with *May I*: I want to ask you a question.",
   "May I ask you a question? | May I ask you a question, please? | May I please ask you a question? | May I ask a question? | May I ask a question, please? | May I please ask a question?",
   *me("May I ask you a question?"))
tx(T, L, 4, "Say it another way with *Can I*: Can you lend me some money?",
   "Can I borrow some money? | Can I borrow some money from you? | Can I borrow some money, please? | Can I please borrow some money? | Can I borrow some money from you, please? | Can I please borrow some money from you?",
   *lend("Can I borrow some money?", "Can you lend me some money?"))

# word order (5); the statement that od() adds (i can pay by card) is natural English too
od(T, L, 3, "Put the words in order to make a question.", "can i pay by card", *me("Can I pay by card?"))
od(T, L, 3, "Put the words in order to make a question.", "could you speak more slowly", *you("Could you speak more slowly?"))
od(T, L, 3, "Put the words in order to make a question.", "may i sit next to you", *me("May I sit next to you?"))
od(T, L, 3, "Put the words in order to make a question.", "can you send me the link", *you("Can you send me the link?"))
od(T, L, 3, "Put the words in order to make a question.", "could you help me with my bags", *you("Could you help me with my bags?"))

# word bank (4): the wrong chips are mistakes of this point
gp(T, L, 3, "Could you ___ me your notes from the lesson?", "lend", *lend("Can I borrow your notes?", "Could you lend me your notes?"),
   bank=["lend", "borrow", "to lend"])
gp(T, L, 3, "Can I ___ your bike this afternoon?", "use", *base("Can I use your bike?", "Can I to use"), bank=["use", "to use", "using"])
gp(T, L, 3, "Would you ___ me a favour?", "do", *base("Would you do me a favour?", "Would you to do"), bank=["do", "to do", "doing"])
gp(T, L, 3, "___ you ___ the door, please?", "Would / close",
   "To ask somebody to do something: *Would / Could / Can you* + base verb: *Would you close the door?* Not *May you…?* and not *to close*.",
   "Lūdzot, lai cits cilvēks kaut ko izdarītu: *Would / Could / Can you* + pamatforma: *Would you close the door?* Nevis *May you…?* un nevis *to close*.",
   bank=["Would", "close", "May", "to close"])

# matching (1): a learning task (matching is never evidence)
mt(T, L, 2, "Match each beginning with its ending.", [("Could you lend", "me your charger?"), ("Can I borrow", "your umbrella?"),
   ("Would you help", "me with this bag?"), ("May I", "come in?")],
   "*Could you lend me…? / Would you help me…?*: you do it for me. *Can I borrow…? / May I come in?*: I ask if I may do it.",
   "*Could you lend me…? / Would you help me…?*: jūs to izdarāt manā labā. *Can I borrow…? / May I come in?*: es jautāju, vai drīkstu to darīt.")
