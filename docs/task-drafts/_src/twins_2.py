"""Batch 2: 50 pending twins for 16 small topic-level banks.

Run from any directory. Sources are resolved from the checked-out bank, not copied
from memory. Every twin keeps its source's topic, level and interaction type.
The review includes the source, answer keys, alternatives and both explanations.
Nothing is moved to the prepared-question directory by this generator.
"""
from collections import Counter
from pathlib import Path
import csv
import json
import re

from lib import Topic, rows, save, LV_BY_FILE, italics

ROOT = Path(__file__).resolve().parents[3]
DRAFTS = ROOT / "docs/task-drafts"
META = json.loads((ROOT / "app/content/meta.json").read_text())
SKILLS = {s["id"]: s for s in META["skills"]}
ALIASES = {}
for skill in SKILLS.values():
    for name in (skill["id"], skill["label"], re.split(r"\s*[(:]", skill["label"])[0].strip()):
        ALIASES[name.lower()] = skill["id"]


def canonical(topic):
    return ALIASES[topic.lower()]


BUILT = {it["id"]: it for it in json.loads((ROOT / "app/content/items.json").read_text())}
for _it in list(BUILT.values()):   # a source revised later (no grammar terms, 6 November) is still found by its older id
    _base = re.sub(r"-r\d+$", "", _it["id"])
    for _k in [_base] + [f"{_base}-r{n}" for n in range(2, 10)]: BUILT.setdefault(_k, _it)
PROVENANCE = []


def original(file, key, skill=None, level=None):
    """Resolve a built-in ID or an exact, unique CSV answer. Fail on ambiguity."""
    if file == "built-in":
        it = BUILT[key]
        answer = it.get("sentence", it.get("correct", ""))
        if not answer:
            answer = " / ".join(" | ".join(a) for a in it.get("answers", []))
        return dict(path="app/content/items.json", locator=key, skill=it["skill"],
                    level=it["level"], kind=it["kind"], task=it["q"], answer=answer,
                    options=" | ".join(it.get("wrong", [])),
                    why=it.get("why", ""), why_lv=it.get("why_lv", ""))
    found = []
    for line, r in enumerate(csv.DictReader((DRAFTS / file).open(encoding="utf-8-sig")), 2):
        if (r["correct answer"] == key and (skill is None or canonical(r["topic"]) == skill)
                and (level is None or r["level"] == level)):
            found.append(dict(path="docs/task-drafts/" + file, locator="CSV line " + str(line),
                              skill=canonical(r["topic"]), level=r["level"], kind=r["type"],
                              task=r["task"], answer=r["correct answer"],
                              options=r["wrong options / checks"],
                              why=r["explanation shown to learner"], why_lv=r["explanation in Latvian"]))
    assert len(found) == 1, (file, key, len(found))
    return found[0]


def twin(source, method, *args, **kwargs):
    topic = Topic(SKILLS[source["skill"]]["label"])
    getattr(topic, method)(source["level"], *args, **kwargs)
    assert rows[-1][2] == source["kind"], (source, rows[-1])
    assert canonical(rows[-1][0]) == source["skill"]
    assert rows[-1][1] == source["level"]
    PROVENANCE.append(source)


def clause_orders(left, right, link):
    """Both clause positions and both sensible attachments of when/while."""
    return [f"{left} {link} {right}", f"{link} {right} {left}",
            f"{right} {link} {left}", f"{link} {left} {right}"]


def order(source, sentence, alternatives, why):
    def capitals(text):
        return re.sub(r"\bi\b", "I", text).replace("french", "French")
    sentence = capitals(sentence)
    twin(source, "order", sentence,
         also=[capitals(a) for a in alternatives if capitals(a) != sentence], why=why)


# Narrative tenses, B1.2: travel, work, technology, learning, hobbies.
N_ORDER = original("compare-past-1.csv", "she had already left when i arrived")
N_JUST = original("compare-past-1.csv", "had / got")
EARLIER = ("*Had* + 3rd form marks the earlier event; *when* introduces the later event.",
           "*Had* + 3. forma norāda agrāko notikumu; *when* ievada vēlāko notikumu.")
order(N_ORDER, "the sun had risen when we arrived",
      ["when we arrived the sun had risen"], EARLIER)
# one twin per source (Claude's review, 4 November): the three clones of N_ORDER became twins of other sources
N_SHINE = original("compare-past-1.csv", "looked / was shining | shone")
N_LUNCH = original("compare-past-1.csv", "had just had")
N_KATE = original("compare-past-1.csv", "was", skill="narrative", level="B1.2")
twin(N_SHINE, "gap", "Use the verbs in brackets: I opened the curtains and ___ outside. It ___ heavily. (look / snow)", "looked / was snowing",
     why=("The event: past simple (*looked*); what was going on at that time: *was* + *-ing* (*was snowing*).",
          "Notikums: Past Simple (*looked*); kas tobrīd notika: *was* + *-ing* (*was snowing*)."))
twin(N_LUNCH, "gap", "Use the verb in brackets: Tom didn't want a coffee. He ___ one. (just / drink)", "had just drunk",
     why=("Before the moment in the story: *had* + *just* + 3rd form: *had just drunk*.",
          "Pirms stāsta brīža: *had* + *just* + 3. forma: *had just drunk*."))
twin(N_JUST, "gap", "Write one word in each gap: I missed the first minute of the lesson. It ___ just ___ when I joined. (start)", "had / started",
     why=("*Had just started* places the start before the moment I joined. Each gap takes one word.",
          "*Had just started*: nodarbība bija sākusies pirms pievienošanās. Katrā tukšumā ieraksti vienu vārdu."))
twin(N_KATE, "gap", "Use the verb in brackets: Leo didn't answer my call. He ___ in a meeting at that moment. (be)", "was",
     why=("At that moment, not before it: past simple *was*.", "Tajā brīdī, nevis pirms tā: Past Simple *was*."))

# Mixed conditionals, B2.1: finance, technology, travel, learning.
M_ORDER = original("built-in", "var-cm-b21-order-01")
M_GAP = original("built-in", "cm-B21-3a")
M_MCQ = original("built-in", "cm-B21-5a")
M_BAD = original("built-in", "cm-B21-4a")
MIXED = ("The condition changes a past event; *would* + base form gives its result now.",
         "Nosacījums maina pagātnes notikumu; *would* + pamatforma izsaka tā sekas tagad.")
order(M_ORDER, "if i had saved more money i would own a flat now", [
    "i would own a flat now if i had saved more money",
    "now if i had saved more money i would own a flat",
    "now i would own a flat if i had saved more money",
    "if i had saved more money now i would own a flat",
    "if i had saved more money i would now own a flat",
    "i would now own a flat if i had saved more money",
], MIXED)
twin(M_MCQ, "mcq", "Choose the correct option: I didn't charge my phone last night. Imagine a different past and its result now.",
     "If I had charged my phone, it would be working now.", [
         "If I had charge my phone, it would be working now.",
         "If I had charged my phone, it would working now.",
         "If I had charged my phone, it would be work now."], why=MIXED)
twin(M_BAD, "mcq", "Which sentence is NOT correct?",
     "If we had caught the flight, we would are in Rome now.", [
         "If she had kept the receipt, she could return the coat now.",
         "If I had joined the course, I would know more Spanish now.",
         "If he had taken the job, he would be living in Berlin now."],
     why=("After *would* use *be*, not *are*: *we would be in Rome now*.",
          "Pēc *would* lieto *be*, nevis *are*: *we would be in Rome now*."))
twin(M_GAP, "gap", "Write one word in each gap: I did not take that course. If I ___ ___ it, I ___ ___ more about design now. (take / know)",
     "had / taken / would | could | might / know", why=(
         "*Had taken* changes the past. *Would know* gives a present result; *could/might* express possibility.",
         "*Had taken* maina pagātni. *Would know* izsaka sekas tagad; *could/might* izsaka iespējamību."))

# Reporting verbs, B2.2: travel, technology, learning, relationships.
R_ORDER = original("built-in", "var-rv-b22-order-01")
R_MCQ = original("built-in", "rv-B22-5a")
R_TEXT = original("built-in", "rv-B22-3a-r2")
APOLOGY = ("*Apologise for* + *-ing*: say sorry for an action.",
           "*Apologise for* + *-ing*: atvainoties par darbību.")
order(R_ORDER, "she apologised for losing my luggage", ["for losing my luggage she apologised"], APOLOGY)
R_BAD = original("built-in", "rv-B22-4a")
twin(R_BAD, "mcq", "Which sentence is NOT correct?", "He suggested to meet on Friday.", [
    "She offered to drive us home.", "They admitted breaking the window.", "I promised to call back later."],
    why=("*suggest* + *-ing* or *that*: *He suggested meeting on Friday*.", "*suggest* + *-ing* vai *that*: *He suggested meeting on Friday*."))
twin(R_MCQ, "mcq", "Which sentence reports this: 'No, I won't take another exam.'",
     "He refused to take another exam.", ["He refused taking another exam.",
     "He refused take another exam.", "He refused to taking another exam."],
     why=("*Refuse* + *to* + base form: *refused to take*.", "*Refuse* + *to* + pamatforma: *refused to take*."))
twin(R_TEXT, "text", "Report with *deny*: 'I didn't share the secret.' Start with *Nora denied*.", [
    "Nora denied sharing the secret.", "Nora denied having shared the secret.",
    "Nora denied that she had shared the secret.", "Nora denied she had shared the secret.",
    "Nora denied that she shared the secret.", "Nora denied she shared the secret.",
    "Nora denied that she'd shared the secret.", "Nora denied she'd shared the secret."],
    why=("*Deny* takes *-ing* or a clause, with or without *that*. *Having shared* makes the earlier time explicit.",
         "Pēc *deny* lieto *-ing* vai palīgteikumu ar *that* vai bez tā. *Having shared* uzsver agrāko darbību."))

# Embedded questions as subjects, C1.1: finance, hobbies, work, travel.
I_ORDER = original("built-in", "var-ia-c11-order-01")
I_MCQ = original("built-in", "ia-C11-5a")
I_TEXT = original("built-in", "ia-C11-3a-r6")
EMBEDDED = ("Inside the question clause, the subject comes before the verb: *whether the payment has arrived*.",
            "Jautājuma palīgteikumā teikuma priekšmets ir pirms darbības vārda: *whether the payment has arrived*.")
order(I_ORDER, "whether the payment has arrived remains unclear", [], EMBEDDED)
I_BAD = original("built-in", "ia-C11-4a")
twin(I_BAD, "mcq", "Which sentence is NOT correct?", "We discussed where should we hold the party.", [
    "Nobody knows why the train stopped.", "It depends on whether the client agrees.", "I wonder what the new boss will say."],
    why=("Inside a question clause, the subject comes before the verb: *where we should hold the party*.",
         "Jautājuma palīgteikumā teikuma priekšmets ir pirms darbības vārda: *where we should hold the party*."))
twin(I_MCQ, "mcq", "Choose the correct option: The question is ___.", "whether the supplier can meet the deadline", [
    "whether can the supplier meet the deadline", "whether the supplier can meets the deadline",
    "whether the supplier can to meet the deadline"], why=(
        "After *whether*, use subject + verb: *the supplier can meet*.",
        "Pēc *whether* lieto teikuma priekšmetu un darbības vārdu: *the supplier can meet*."))
twin(I_TEXT, "text", "Combine the sentences. Start with *It is unclear*: Which route should we take? It is unclear.", [
    "It is unclear which route we should take.", "It's unclear which route we should take.",
    "It is unclear which route to take.", "It's unclear which route to take."], why=(
        "Use *which route we should take* or the shorter *which route to take*, without question word order.",
        "Lieto *which route we should take* vai īsāk *which route to take*. Palīgteikumā teikuma priekšmets ir pirms darbības vārda."))

# Past simple or past continuous, B1.1: work, learning, hobbies, travel.
P_ORDER = original("compare-past-1.csv", "the phone rang while i was having a shower")
P_MCQ = original("compare-past-1.csv", "knew")
P_GAP = original("compare-past-1.csv", "walked")
BACKGROUND = ("*Was/were* + *-ing* gives the activity in progress; the other verb gives the event during it.",
              "*Was/were* + *-ing* izsaka darbību procesā; otrs darbības vārds norāda notikumu tās laikā.")
order(P_ORDER, "the alarm rang while i was working", clause_orders("the alarm rang", "i was working", "while"), BACKGROUND)
twin(P_MCQ, "mcq", "Choose the correct option: We ___ the answer in yesterday's lesson, so we raised our hands.",
     "knew", ["were knowing", "was knowing"], why=(
         "For a state of knowledge, use *knew*, not *was/were knowing*.",
         "Zināšanu stāvoklim lieto *knew*, nevis *was/were knowing*."))
P_ROAD = original("compare-past-1.csv", "was walking / saw")
twin(P_ROAD, "gap", "Use the verbs in brackets: I ___ to work when I ___ a strange noise from the engine. So I stopped the car. (drive / hear)", "was driving / heard", why=BACKGROUND)
twin(P_GAP, "gap", "Use the verb in brackets: Last Saturday we ___ ten kilometres along the coast. (walk)", "walked",
     why=("A finished walk with its whole distance: past simple *walked*.",
          "Pabeigta pastaiga ar visu attālumu: Past Simple *walked*."))

# Third conditional, B2.1: learning, technology, travel, relationships.
T_MCQ = original("built-in", "ct-B21-1a")
T_BAD = original("built-in", "ct-B21-4a")
T_REQUEST = original("built-in", "ct-B21-5a")
T_TEXT = original("built-in", "ct-B21-3a-r2")
THIRD = ("An unreal past: *if* + *had* + 3rd form; *would/could have* + 3rd form gives the imagined result.",
         "Iedomāta pagātne: *if* + *had* + 3. forma; *would/could have* + 3. forma izsaka iedomātās sekas.")
twin(T_MCQ, "mcq", "Choose the correct option: She would have understood the lesson if she ___ the notes.",
     "had read", ["had reading", "have read"], why=THIRD)
twin(T_BAD, "mcq", "Which sentence has a mistake?", "If I had save a copy, I wouldn't have lost my work.", [
    "If she had booked earlier, she would have paid less for the flight.",
    "If we had trained harder, we could have finished the race together.",
    "If he had checked the date, he would have attended the right meeting."], why=(
        "After *had*, use the 3rd form: *had saved*, not *had save*.",
        "Pēc *had* lieto 3. formu: *had saved*, nevis *had save*."))
twin(T_REQUEST, "mcq", "Choose the correct option: We missed the bus yesterday. If we had left earlier, we ___.",
     "could have caught it", ["could have catch it", "could had caught it"], why=THIRD)
twin(T_TEXT, "text", "Rewrite with *if* and *would*: I didn't remember her birthday, so I didn't call her.", [
    "If I had remembered her birthday, I would have called her.",
    "If I'd remembered her birthday, I would have called her.",
    "If I had remembered her birthday, I'd have called her.",
    "If I'd remembered her birthday, I'd have called her.",
    "I would have called her if I had remembered her birthday.",
    "I would have called her if I'd remembered her birthday.",
    "I'd have called her if I had remembered her birthday.",
    "I'd have called her if I'd remembered her birthday."], why=THIRD)

# Reported questions and requests, B2.1: technology, travel, relationships, work.
Q_CAN = original("built-in", "rq-B21-1a")
Q_NOT = original("built-in", "rq-B21-2a")
Q_BAD = original("built-in", "rq-B21-4a")
Q_TEXT = original("built-in", "rq-B21-3a-r2")
twin(Q_CAN, "mcq", "Which sentence reports this: 'Can you fix my laptop?'", "She asked if I could fix her laptop.", [
    "She asked if could I fix her laptop.", "She asked if I could fixed her laptop.",
    "She asked if I could to fix her laptop."], why=(
        "The reported question uses *if I could*, with subject before verb.",
        "Netiešajā jautājumā lieto *if I could*: teikuma priekšmets ir pirms darbības vārda."))
twin(Q_NOT, "mcq", "Which sentence reports this: 'Don't leave your bag here!'", "He told me not to leave my bag there.", [
    "He told me not leave my bag there.", "He told me not to leaving my bag there.",
    "He told me to not left my bag there."], why=(
        "A negative instruction: *told me not to leave*. *Here* becomes *there* when the location changes.",
        "Aizliegums: *told me not to leave*. Mainoties vietai, *here* kļūst par *there*."))
twin(Q_BAD, "mcq", "Which sentence is NOT correct?", "She asked me where did I buy the flowers.", [
    "He asked whether I had enjoyed the concert.", "They asked how long the repair would take.",
    "Mia asked if I could send the report that afternoon."], why=(
        "Use statement word order: *where I bought the flowers*, without *did*.",
        "Lieto apgalvojuma vārdu secību: *where I bought the flowers*, bez *did*."))
twin(Q_TEXT, "text", "Report this request. Start with *Omar asked me*: 'Could you check the figures?'", [
    "Omar asked me to check the figures.", "Omar asked me if I could check the figures.",
    "Omar asked me whether I could check the figures."], why=(
        "A request can be reported as *asked me to check* or *asked me if/whether I could check*.",
        "Lūgumu var atstāstīt ar *asked me to check* vai *asked me if/whether I could check*."))

# Auxiliary verbs, B1.1: lifestyle, technology, work.
A_ORDER = original("aux-verbs-1.csv", "what have you been doing all day")
A_MCQ = original("aux-verbs-1.csv", "have", "aux_verbs", "B1.1")
A_TEXT = original("aux-verbs-1.csv", "Were you late again?")
order(A_ORDER, "what have you been cooking all morning", [], (
    "Question order: *what have you been cooking*; the activity continues over a period.",
    "Jautājuma vārdu secība: *what have you been cooking*; darbība ilgst noteiktu laiku."))
twin(A_MCQ, "mcq", "Choose the correct option: How long ___ you owned this laptop?", "have", ["are", "do"],
     why=("*Have* + 3rd form: *have you owned*.", "*Have* + 3. forma: *have you owned*."))
twin(A_TEXT, "text", "Make a yes/no question: You were busy yesterday.", "Were you busy yesterday?",
     why=("Move *were* before *you*: *Were you busy yesterday?*", "Pārvieto *were* pirms *you*: *Were you busy yesterday?*"))

# Articles, B1.2: lifestyle, work, travel.
ART_ORDER = original("b1-new-1.csv", "she spent half an hour waiting for the bus")
ART_EXCL = original("b1-new-1.csv", "what a lovely surprise to see you here")


def original_task(file, task):
    matches = [r for r in csv.DictReader((DRAFTS / file).open(encoding="utf-8-sig")) if r["task"] == task]
    assert len(matches) == 1, (file, task)
    r = matches[0]
    # Reuse the same source representation, with a unique task locator.
    for line, candidate in enumerate(csv.DictReader((DRAFTS / file).open(encoding="utf-8-sig")), 2):
        if candidate == r:
            return dict(path="docs/task-drafts/" + file, locator="CSV line " + str(line),
                        skill=canonical(r["topic"]), level=r["level"], kind=r["type"], task=r["task"],
                        answer=r["correct answer"], options=r["wrong options / checks"],
                        why=r["explanation shown to learner"], why_lv=r["explanation in Latvian"])


ART_GAP = original_task("b1-new-1.csv", "Complete with *a*, *an* or *the*: It was such ___ nice day that we went swimming.")
order(ART_ORDER, "she spent half an hour choosing a jacket", [], (
    "Say *half an hour*: *hour* begins with a vowel sound.", "Lieto *half an hour*: *hour* sākas ar patskaņa skaņu."))
order(ART_EXCL, "what a useful skill to have at work", [], (
    "*What a* + adjective + singular noun: *what a useful skill*.",
    "*What a* + īpašības vārds + vienskaitļa lietvārds: *what a useful skill*."))
twin(ART_GAP, "gap", "Complete with one word: It was such ___ long journey that we stopped twice.", "a",
     why=("*Such a* + adjective + singular countable noun: *such a long journey*.",
          "*Such a* + īpašības vārds + skaitāms lietvārds vienskaitlī: *such a long journey*."))

# Past simple or past continuous, A2.2: travel, work, hobbies.
PA_ORDER = original("compare-past-1.csv", "she was reading when i arrived")
PA_MCQ = original("compare-past-1.csv", "were playing")
PA_GAP = original("compare-past-1.csv", "hurt / was working")
order(PA_ORDER, "it was snowing when we arrived", clause_orders("it was snowing", "we arrived", "when"), BACKGROUND)
twin(PA_MCQ, "mcq", "Choose the correct option: They started lunch at one and finished at two. At one thirty, they ___ lunch.",
     "were having", ["was having", "were have"], why=(
         "Lunch was in progress: *they were having lunch*.",
         "*They were having lunch* nozīmē, ka pusdienošana tobrīd vēl turpinājās."))
twin(PA_GAP, "gap", "Complete the sentence: I ___ my ankle while I ___ tennis yesterday. (hurt / play)",
     "hurt / was playing | played", why=(
         "*Hurt* is the event. *Was playing* gives the activity during it; *played* is also possible after *while*.",
         "*Hurt* ir notikums. *Was playing* izsaka darbību tā laikā; pēc *while* iespējams arī *played*."))

# Past perfect continuous, B2.1: hobbies, work, learning.
NB_ORDER = original("compare-past-1.csv", "we had been driving for hours when the car broke down")
NB_MCQ = original("compare-past-1.csv", "had been raining")
NB_GAP = original("compare-past-1.csv", "had written")
PAST_DURATION = ("*Had been* + *-ing* describes an activity continuing up to a past event.",
                 "*Had been* + *-ing* izsaka darbību, kas turpinājās līdz pagātnes notikumam.")
order(NB_ORDER, "we had been hiking for hours when the storm began", [
    "when the storm began we had been hiking for hours", "the storm began when we had been hiking for hours",
    "when we had been hiking for hours the storm began", "for hours we had been hiking when the storm began",
    "when the storm began for hours we had been hiking"], PAST_DURATION)
twin(NB_MCQ, "mcq", "Choose the correct option: The floor was wet. Water ___ from a pipe all night.",
     "had been leaking", ["had been leak", "had leaking"], why=PAST_DURATION)
twin(NB_GAP, "gap", "Use the verb in brackets: By the time the bell rang, Eva ___ all ten questions, so she left early. (answer)",
     "had answered", why=(
         "*By the time* + past event: what was finished before it takes *had* + 3rd form.",
         "*By the time* + pagātnes notikums: tam, kas jau bija pabeigts, lieto *had* + 3. formu."))

# Present perfect or past simple, B1.1: hobbies, work, learning.
PB_MCQ = original("compare-past-1.csv", "have never ridden")
PB_PAST = original("compare-past-1.csv", "worked")
PB_QUESTION = original("compare-past-1.csv", "Did / see")
twin(PB_MCQ, "mcq", "Choose the correct option: I ___ a marathon. Never in my life.", "have never run", [
    "have never ran", "has never run"], why=(
        "Experience up to now: *have never* + 3rd form, *run*.",
        "Pieredze līdz šim brīdim: *have never* + 3. forma, *run*."))
twin(PB_PAST, "gap", "Use the verb in brackets: I ___ that office from 2018 to 2021. Now I work elsewhere. (manage)", "managed",
     why=("The finished period *from 2018 to 2021* takes *managed*.",
          "Pabeigtam periodam *from 2018 to 2021* lieto *managed*."))
twin(PB_QUESTION, "gap", "Complete with one word in each gap: ___ you ___ the workshop yesterday? (enjoy)", "Did / enjoy",
     why=("For yesterday's event, ask *Did you enjoy ...?* *Did* is followed by the base form.",
          "Par vakardienas notikumu jautā *Did you enjoy ...?* Pēc *did* lieto pamatformu."))

# Present perfect or past simple, A2.2: hobbies, work.
PP_ORDER = original("compare-past-1.csv", "have you ever eaten sushi")
PP_MCQ = original("compare-past-1.csv", "has gone")
order(PP_ORDER, "have you ever tried skiing", [], (
    "*Have you ever tried ...?* asks about experience up to now.",
    "*Have you ever tried ...?* jautā par pieredzi līdz šim brīdim."))
twin(PP_MCQ, "mcq", "Choose the correct option: Sara isn't here. She ___ to a meeting.", "has gone", ["has went", "have gone"],
     why=("*Has gone* means she went there and has not returned.", "*Has gone* nozīmē, ka viņa ir aizgājusi un vēl nav atgriezusies."))

# Past perfect continuous, B2.2: learning, relationships.
NB2_ORDER = original("compare-past-1.csv", "she had been working there for ten years when she left")
NB2_TEXT = original("compare-past-1.csv", "We had known each other since school.")
order(NB2_ORDER, "she had been learning french for years when she moved", [
    "when she moved she had been learning french for years",
    "she moved when she had been learning french for years",
    "when she had been learning french for years she moved",
    "for years she had been learning french when she moved",
    "when she moved for years she had been learning french"], PAST_DURATION)
twin(NB2_TEXT, "text", "Correct the sentence. Keep *had*: We had been knowing each other for years before we married.", [
    "We had known each other for years before we married.",
    "We'd known each other for years before we married.",
    "Before we married, we had known each other for years.",
    "Before we married, we'd known each other for years.",
    "For years before we married, we had known each other.",
    "For years before we married, we'd known each other."],
    why=("*Know* describes a state, so use *had known*, not *had been knowing*.",
         "*Know* izsaka stāvokli, tāpēc lieto *had known*, nevis *had been knowing*."))

# The final one-task gaps: narrative B1.1 and comparison B1.2.
N1_ORDER = original("compare-past-1.csv", "it was raining when we left the house")
order(N1_ORDER, "the shop was closing when we got there", clause_orders("the shop was closing", "we got there", "when"), BACKGROUND)
C1_ORDER = original("comparison-1.csv", "this year was not as busy as last year")
order(C1_ORDER, "this winter was not as cold as last winter", ["last winter was not as cold as this winter"], (
    "*Not as cold as* compares two winters. Either winter can be the subject with these tiles.",
    "*Not as cold as* salīdzina divas ziemas. No šīm kartītēm var izveidot abus salīdzinājumus."))


def role(row):
    if row[2] == "order" or row[2] == "mcq":
        return "check"
    return "use"


def validate():
    assert len(rows) == len(PROVENANCE) == 50
    kinds = Counter(r[2] for r in rows)
    assert kinds == {"order": 14, "mcq": 18, "gap": 12, "text": 6}, kinds
    assert kinds["order"] / len(rows) >= .25
    sources = Counter((s["path"], s["locator"]) for s in PROVENANCE)
    assert max(sources.values()) == 1, [k for k, v in sources.items() if v > 1]   # one twin per source: no clones (Claude's review, 4 November)
    pending_one = {(canonical(r["topic"]), r["level"]) for r in
                   csv.DictReader((DRAFTS / "twins-1.csv").open(encoding="utf-8-sig"))}
    counts = Counter((canonical(r[0]), r[1]) for r in rows)
    assert len(counts) == 16
    assert not (set(counts) & pending_one)
    for row, source in zip(rows, PROVENANCE):
        assert (row[3], row[4]) != (source["task"], source["answer"]), "Unchanged source task"
        assert len(row[6]) >= 12 and len(row[7]) >= 12
        plain_lv = re.sub(r"\*[^*]+\*", " ", row[7])
        lv_words = set(re.findall(r"\b[a-zA-Z]+\b", plain_lv.lower()))
        unknown = lv_words - italics.LV_ASCII - LV_BY_FILE["twins-2.csv"]
        assert not unknown, ("Latvian words would be styled as English", unknown)
        if row[2] == "order":
            accepted = row[5].removeprefix("also accepted: ").split(" | ") if row[5] else []
            for variant in accepted:
                assert Counter(variant.split()) == Counter(row[4].split()), (row[4], variant)
        assert not (len(row) > 9 and row[9]), ("Twins must never retire a published task", row[3], row[9])
    n_order = kinds["order"]; print(f"Validated 50 source links, 16 topic-levels, {n_order} drag tasks ({n_order * 2}%), one twin per source, and all alternative tile multisets.")


def write_review():
    """Read the saved CSV so the review shows exactly what would be imported."""
    output = list(csv.DictReader((DRAFTS / "twins-2.csv").open(encoding="utf-8-sig")))
    lines = ["# Dvīņi, 2. partija: 50 uzdevumi pārskatīšanai", "",
             "Statuss: Inga apstiprināja 4. novembrī; pievienots sagatavotajiem jautājumiem (docs/task-drafts/twins-2.csv).", "",
             "**Claude labojumi (4. novembris):** katram oriģinālam tikai viens dvīnis (nr. 2, 3, 5, 11, 15 un 20 bija kloni; tagad tie ir citu oriģinālu dvīņi: tukšumi un izvēles uzdevumi); "
             "instrukcijas bez *one word*, kas izslēdza otru laiku (*Last Saturday we ___ ten kilometres*, *from 2018 to 2021*); *By the time the bell rang, Eva ___* pieņem tikai *had answered*; "
             "jauktajā nosacījuma teikumā vairs nav *should*; *If I had save a copy, I wouldn't have lost my work*; nedabiskās vārdu secības vairs netiek pieņemtas; "
             "B1.1 secības uzdevums ir cita aina (*the shop was closing when we got there*). Visas 16 tēmas joprojām sasniedz 10 uzdevumus.", "",
             "16 tēmu un līmeņu pāri; 16 izvēles, 20 vārdu secības, 8 rakstāmu tukšumu un 6 teikuma rakstīšanas uzdevumi.",
             "Vilkšanas uzdevumi: 40%. Katram dvīnim saglabāta oriģināla tēma, līmenis un uzdevuma veids.", "",
             "Oriģināli atspoguļo šī zara sākuma versiju. Tie ir salīdzināšanai, nevis jauniem uzdevumiem paredzēti paraugi bez pārbaudes.",
             "Pie nosacījuma vai laika palīgteikuma pieņemtas arī norādītās alternatīvās kartīšu secības.",
             "Tukšumu atslēgās `/` atdala tukšumus, bet `|` atdala viena tukšuma derīgās atbildes.", "",
             "## Pārklājums", "", "| Tēma | Līmenis | Jauni uzdevumi |", "|---|---|---:|"]
    for (topic, level), n in Counter((r["topic"], r["level"]) for r in output).items():
        lines.append(f"| {topic} | {level} | {n} |")
    for n, (r, src) in enumerate(zip(output, PROVENANCE), 1):
        lines += ["", f"## {n}. {r['topic']} · {r['level']} · {r['type']}", "",
                  f"**Loma:** {role(rows[n-1])}.", "",
                  f"**Oriģināls:** `{src['path']}` ({src['locator']}).",
                  f"> {src['task']}", "", f"Oriģināla atslēga: {src['answer']}"]
        if src["options"]:
            lines += ["", "Oriģināla varianti / pieņemtās secības: " + src["options"]]
        lines += ["", "**Dvīnis:** " + r["task"], "", "**Atbilde:** " + r["correct answer"]]
        if r["wrong options / checks"]:
            lines += ["", "**Varianti / citas pieņemtās secības:** " + r["wrong options / checks"]]
        lines += ["", "**EN:** " + r["explanation shown to learner"], "",
                  "**LV:** " + r["explanation in Latvian"]]
    (DRAFTS / "twins-2-review.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    validate()
    save("twins-2.csv")   # approved by the teacher on 4 November after Claude's corrections
    write_review()
