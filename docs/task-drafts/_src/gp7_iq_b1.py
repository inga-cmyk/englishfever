"""Indirect questions B1.1 and B1.2, points iq_wh / iq_yn: the learner makes the indirect question himself (teacher's tester,
22 November: all 20 B1 tasks done as a guest, 20/20; "fine as practice for early B1, but a strong B1 learner finds most of them
easy: choosing the right word order, matching cards by keywords. Replace some similar choice tasks with tasks where the learner
transforms a direct question into an indirect one himself"). Murphy unit 50 (Do you know where ...? / Could you tell me if ...?),
unit 13 for the past (What did he say? -> what he said); checked against the rule card of ind_polite.

Eight typed whole sentences: a short adult situation, the direct question in quotes, the two starts the card teaches. Each needs
a real change, mixed over the set:
  - do / does / did goes, and the verb carries the tense: does breakfast start -> breakfast starts, did the client say -> the
    client said, does this jacket come -> if this jacket comes, did the teacher give -> if the teacher gave;
  - the subject comes before can / is / has / will: how can I -> how I can, is insurance -> if insurance is, has my test result
    -> if my test result has, when will my new glasses -> when my new glasses will;
  - if / whether for a yes/no question (four of the eight).
Every answer is listed: both starts, Excuse me in front, please, Could you please tell me / Do you happen to know, if and
whether, the 's contraction, the small natural variants of the core (named in the explanations or the notes). The grader ignores
capitals, commas and the final punctuation and reads n't / 'll / 're itself; 's is listed. A question mark follows both starts.
No save() here: the lead agent adds this module to iq_b1_6.py (point_of: POINT_OF first). Notes: gp7_iq_b1-notes.md."""
import lib
from lib import tx, rows

T = "Indirect questions (Could you tell me where...)"
POINT_OF = {}


def point(p):
    POINT_OF[len(rows) - 1] = p


def ask(setting, question):
    return f"{setting} Ask politely, starting with *Could you tell me* or *Do you know*: '{question}'"


def forms(cores):
    """Every accepted sentence: the two starts (and their polite variants) + each core, with and without Excuse me."""
    out = []
    for c in cores:
        base = [f"Could you tell me {c}?", f"Do you know {c}?", f"Could you tell me {c}, please?",
                f"Could you please tell me {c}?", f"Do you happen to know {c}?", f"Do you know {c}, please?"]
        for f in base + ["Excuse me, " + b[0].lower() + b[1:] for b in base]:
            if f not in out: out.append(f)
    return out


def yn(cores):
    return [f"{w} {c}" for w in ("if", "whether") for c in cores]


# ================================ B1.1 (present, can, is, if / whether) ================================
L = "B1.1"

tx(T, L, 4, ask("You're at a hotel reception.", "What time does breakfast start?"),
   forms(["what time breakfast starts", "when breakfast starts", "what time breakfast begins", "when breakfast begins", "what time breakfast is", "when breakfast is"]),
   "*What time does breakfast start?* becomes *what time breakfast starts*: *does* goes, and the verb itself takes *-s*.",
   "*What time does breakfast start?* kļūst par *what time breakfast starts*: *does* pazūd, un *-s* ir pašam darbības vārdam.")
point("iq_wh")

tx(T, L, 4, ask("You've forgotten your work password and call the IT help desk.", "How can I reset my password?"),
   forms(["how I can reset my password", "how I could reset my password", "how I reset my password", "how to reset my password",
          "how I can reset it", "how I could reset it", "how I reset it", "how to reset it"]),
   "*How can I reset my password?* becomes *how I can reset my password*: the subject *I* comes before *can*. "
   "*how to reset my password* is correct too.",
   "*How can I reset my password?* kļūst par *how I can reset my password*: teikuma priekšmets *I* ir pirms *can*. "
   "Arī *how to reset my password* ir pareizā atbilde.")
point("iq_wh")

tx(T, L, 4, ask("In a clothes shop, the jacket you like is too small.", "Does this jacket come in a larger size?"),
   forms(yn([f"{s} in a {z} size" for s in ("this jacket comes", "it comes", "this jacket is available", "it is available", "it's available",
                                            "you have this jacket", "you have it", "you've got this jacket", "you've got it")
             for z in ("larger", "bigger")])),
   "*Does this jacket come in a larger size?* becomes *if this jacket comes in a larger size*: *if* (or *whether*), no *does*, "
   "and *comes* with *-s*.",
   "*Does this jacket come in a larger size?* kļūst par *if this jacket comes in a larger size*: *if* (vai *whether*), bez *does*, "
   "un *comes* ar *-s*.")
point("iq_yn")

tx(T, L, 4, ask("You're renting a car on holiday and talking to the agent.", "Is insurance included in the price?"),
   forms(yn([f"{s} included in the price" for s in ("insurance is", "the insurance is", "insurance's", "the insurance's")] + ["the price includes insurance"])),
   "*Is insurance included in the price?* becomes *if insurance is included in the price*: *if* (or *whether*), "
   "then the subject before *is*.",
   "*Is insurance included in the price?* kļūst par *if insurance is included in the price*: *if* (vai *whether*), "
   "tad teikuma priekšmets pirms *is*.")
point("iq_yn")

# ============== B1.2 (past without did, present perfect, will, if / whether) ==============
L = "B1.2"

tx(T, L, 4, ask("You had a blood test last week, and now you phone the doctor's surgery.", "Has my test result come back yet?"),
   forms(yn([f"{s} {v}" for s in ("my test result has", "my test result's", "my result has", "my result's", "my test results have", "my results have", "my blood test result has", "my blood test results have")
             for v in ("come back yet", "come back", "arrived yet", "arrived")])),
   "*Has my test result come back yet?* becomes *if my test result has come back yet*: *if* (or *whether*), "
   "then the subject before *has*.",
   "*Has my test result come back yet?* kļūst par *if my test result has come back yet*: *if* (vai *whether*), "
   "tad teikuma priekšmets pirms *has*.")
point("iq_yn")

tx(T, L, 4, ask("You missed yesterday's meeting with a client. Your colleague was there.", "What did the client say about our offer?"),
   forms([f"what {s} said about {o}" for s in ("the client", "they", "he", "she") for o in ("our offer", "the offer")]),
   "*What did the client say about our offer?* becomes *what the client said about our offer*: *did* goes, "
   "and the verb itself is in the past: *said*.",
   "*What did the client say about our offer?* kļūst par *what the client said about our offer*: *did* pazūd, "
   "un pagātni rāda darbības vārds: *said*.")
point("iq_wh")

tx(T, L, 4, ask("You ordered new glasses two weeks ago and now you're at the optician's.", "When will my new glasses be ready?"),
   forms([f"{w} {s} will be ready" for w in ("when", "what day") for s in ("my new glasses", "my glasses", "they")] + [f"when {s} are going to be ready" for s in ("my new glasses", "my glasses", "they")]),
   "*When will my new glasses be ready?* becomes *when my new glasses will be ready*: the subject comes before *will*.",
   "*When will my new glasses be ready?* kļūst par *when my new glasses will be ready*: teikuma priekšmets ir pirms *will*.")
point("iq_wh")

_hw = [f"{s} {v} us {h}" for s in ("the teacher", "she", "he") for v in ("gave", "has given") for h in ("any homework", "homework")] \
    + [f"we {v} {h}" for v in ("got", "have got", "have", "had") for h in ("any homework", "homework")]
tx(T, L, 4, ask("You missed your evening Spanish class, so you message a classmate.", "Did the teacher give us any homework?"),
   forms(yn(_hw)),
   "*Did the teacher give us any homework?* becomes *if the teacher gave us any homework*: *if* (or *whether*), no *did*, "
   "and the verb in the past: *gave*.",
   "*Did the teacher give us any homework?* kļūst par *if the teacher gave us any homework*: *if* (vai *whether*), bez *did*, "
   "un darbības vārds pagātnē: *gave*.")
point("iq_yn")
# *has given* is correct too (any homework until now); its own note, shown only to whoever writes it
lib.NOTES[len(rows) - 1] = " || ".join(
    a + " :: Correct too: *has given* asks about homework until now. The question asked about the class with *did*, so the closest form is *gave*. "
        ":: Arī pareizi: *has given* jautā par mājasdarbu līdz šim brīdim. Jautājumā bija *did* (par nodarbību), tāpēc tuvākā forma ir *gave*."
    for a in forms(yn([h for h in _hw if "has given" in h])))
