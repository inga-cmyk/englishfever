"""Twins, batch 3 (teacher, 4 November): the nine topic-levels the batch-2 report left under 10 check / use tasks.
One twin per source task, same topic, level and task type, another setting. Written to every rule in
docs/ITEM-WRITING-RULES.md, including the lessons of batches 1 and 2 (one fitting answer; no word count that gives a
tense away; no tense names in instructions; only natural word orders; no near-identical pair; sentences that make sense).
Saved to pending/ with a review next to it until the teacher (and the reviewing agent) have seen it."""
from collections import Counter
from pathlib import Path
import csv, json, re
from lib import Topic, rows, save, italics

ROOT = Path(__file__).resolve().parents[3]
DRAFTS = ROOT / "docs/task-drafts"
META = json.loads((ROOT / "app/content/meta.json").read_text())
SKILLS = {s["id"]: s for s in META["skills"]}
ALIASES = {}
for s in SKILLS.values():
    for name in (s["id"], s["label"], re.split(r"\s*[(:]", s["label"])[0].strip()):
        ALIASES[name.lower()] = s["id"]
BUILT = {it["id"]: it for it in json.loads((ROOT / "app/content/items.json").read_text())}
SOURCES = []


def src_built(item_id):
    it = BUILT[item_id]
    key = it.get("sentence") or it.get("correct") or " / ".join(" | ".join(a) for a in it.get("answers", []))
    return dict(where="app/content/items.json · " + item_id, skill=it["skill"], level=it["level"], kind=it["kind"],
                task=it["q"], answer=key, options=" | ".join(it.get("wrong", []) or it.get("bank", [])))


def src_csv(file, task_part):
    found = [(n, r) for n, r in enumerate(csv.DictReader((DRAFTS / file).open(encoding="utf-8-sig")), 2) if task_part in r["task"] or task_part in r["correct answer"]]
    assert len(found) == 1, (file, task_part, len(found))
    n, r = found[0]
    return dict(where=f"docs/task-drafts/{file} · line {n}", skill=ALIASES[r["topic"].lower()], level=r["level"], kind=r["type"],
                task=r["task"], answer=r["correct answer"], options=r["wrong options / checks"])


def twin(source, method, *args, **kwargs):
    getattr(Topic(SKILLS[source["skill"]]["label"]), method)(source["level"], *args, **kwargs)
    assert rows[-1][2] == source["kind"] and rows[-1][1] == source["level"], (source, rows[-1][:4])
    SOURCES.append(source)


def contractions(sentences):
    """Every 'd / n't spelling the checker cannot work out by itself: had -> 'd, would -> 'd."""
    out = []
    for s in sentences:
        for a in {s, s.replace("I had ", "I'd ").replace("she had ", "she'd ").replace("he had ", "he'd "),
                  s.replace("she would ", "she'd ").replace("I would ", "I'd ").replace("he would ", "he'd "),
                  s.replace("I had ", "I'd ").replace("she had ", "she'd ").replace("he had ", "he'd ").replace("she would ", "she'd ").replace("I would ", "I'd ").replace("he would ", "he'd ")}:
            if a not in out: out.append(a)
    return out


# ── Mixed conditionals · B2.2 ─────────────────────────────────────────────────────────────────────────────
MIX = ("A quality now, a result in the past: *if* + past (*weren't*), *would have* + 3rd form.",
       "Rakstura īpašība tagad un sekas pagātnē: *if* + Past Simple (*weren't*), *would have* + 3. forma.")
twin(src_built("cm-B22-1a"), "mcq", "Complete: 'If I weren't so impatient, I ___ sold my flat so cheaply last spring.'",
     "wouldn't have", ["wouldn't", "won't have", "hadn't"], why=MIX)
twin(src_built("cm-B22-3a-r2"), "text", "Imagine it was different. Rewrite as one sentence with *if*: She didn't learn German at school, so she can't understand her new colleagues now.",
     contractions([f"If she had {v} German at school, she {r} understand her new colleagues now." for v in ("learned", "learnt") for r in ("would be able to", "could", "would")]
                  + [f"She {r} understand her new colleagues now if she had {v} German at school." for v in ("learned", "learnt") for r in ("would be able to", "could", "would")]),
     why=("Imagine a different past (*had learned*) with a result now (*would understand / could understand / would be able to understand*).", "Iztēlojamies citādu pagātni (*had learned*) un tās sekas tagad (*would understand / could understand / would be able to understand*)."))
twin(src_built("cm-B22-4a"), "mcq", "Which sentence is NOT correct?", "If she would be more patient, she wouldn't have shouted at him.",
     ["If he spoke Italian, he would have enjoyed the tour more.", "If we hadn't sold the car, we would drive to the coast now.", "If I had slept well, I wouldn't feel so tired today."],
     why=("No *would* after *if*: *If she were more patient*. A quality now, a result in the past.", "Aiz *if* nelieto *would*: *If she were more patient*. Rakstura īpašība tagad, sekas pagātnē."))
twin(src_built("cm-B22-2a-r2"), "mcq", "He isn't a confident person, so he didn't ask for a pay rise. Choose the correct sentence.",
     "If he were more confident, he would have asked for a pay rise.", ["If he were more confident, he would asked for a pay rise.", "If he would be more confident, he would have asked for a pay rise.", "If he were more confident, he will have asked for a pay rise."],
     why=("A quality now (*were more confident*), a result in the past (*would have asked*).", "Rakstura īpašība tagad (*were more confident*), sekas pagātnē (*would have asked*)."))

# ── Mixed conditionals · C1.1 ─────────────────────────────────────────────────────────────────────────────
INV = ("*Had* + subject + 3rd form = *If* + subject + *had* + 3rd form; the result is about now.", "*Had* + teikuma priekšmets + 3. forma = *If* + teikuma priekšmets + *had* + 3. forma; sekas ir par tagadni.")
twin(src_built("cm-C11-1a-r3"), "mcq", "Which sentence without *if* is correct?", "Had we booked earlier, we would be on the beach now.",
     ["Had we book earlier, we would be on the beach now.", "If had we booked earlier, we would be on the beach now.", "Did we book earlier, we would be on the beach now."], why=INV)
twin(src_built("cm-C11-3a-r2"), "text", "Rewrite starting with *Had*: If I had read the contract more carefully, I wouldn't be paying these fees now.",
     ["Had I read the contract more carefully, I wouldn't be paying these fees now.", "Had I read the contract more carefully, I'd not be paying these fees now."], why=INV)
twin(src_built("cm-C11-4a-r2"), "mcq", "Which sentence is NOT correct?", "Hadn't she missed the train, she'd be here now.",
     ["Had he trained harder, he would be in the team now.", "Were she less shy, she would have spoken up.", "Had they not moved, they would live next door now."],
     why=("In the negative, *not* comes after the subject: *Had she not missed the train*.", "Noliegumā *not* liek aiz teikuma priekšmeta: *Had she not missed the train*."))
twin(src_built("cm-C11-5a"), "mcq", "Choose the correct option.",
     "Had the software been tested earlier, we would not be fixing these errors now.",
     ["Had the software be tested earlier, we would not be fixing these errors now.", "Had the software been tested earlier, we would not fixing these errors now.",
      "Had the software been tested earlier, we will not be fixing these errors now."],
     why=("Imagine earlier testing: *had been tested* (passive). The result now: *would not be fixing*.", "Iztēlojamies agrāku programmas pārbaudi: *had been tested* (ciešamā kārta). Sekas tagad: *would not be fixing*."))

# ── Reported statements · B2.1 ────────────────────────────────────────────────────────────────────────────
twin(src_built("rs-B21-3a-r2"), "text", "Report this. Start with *The coach told us*: 'You must warm up before every match.'",
     ["The coach told us we had to warm up before every match.", "The coach told us that we had to warm up before every match.",
      "The coach told us we must warm up before every match.", "The coach told us that we must warm up before every match.", "The coach told us to warm up before every match."],
     why=("Report the obligation with *had to* or *must*, or the instruction with *told us to warm up*.", "Pienākumu atstāsta ar *had to* vai *must*, norādījumu arī ar *told us to warm up*."))
twin(src_built("rs-B21-4a"), "mcq", "Which sentence is NOT correct?", "He told that the shop was closed.",
     ["She said that the bus was full.", "They told me the film had started.", "He told us he was moving abroad."],
     why=("*tell* needs a person: *He told me / us that…*; or use *said*.", "Aiz *tell* norāda adresātu: *He told me / us that…*. Bez adresāta lieto *said*."))
twin(src_built("rs-B21-5a"), "mcq", "Choose the correct report of your sister's words to you: 'I'll call you as soon as I land.'",
     "My sister said she would call me as soon as she landed.",
     ["My sister said she would call me as soon as she would land.", "My sister said she would call me as soon as she did landed.", "My sister said she would calling me as soon as she landed."],
     why=("*will* becomes *would*; after *as soon as* no *would*: *as soon as she landed*.", "*will* kļūst par *would*; aiz *as soon as* nelieto *would*: *as soon as she landed*."))
twin(src_built("rs-B21-1a-r2"), "mcq", "Choose the correct report of the agent's words to you: 'You might need a visa.'", "The agent said I might need a visa.",
     ["The agent said I mighted need a visa.", "The agent said I might to need a visa.", "The agent said me I might need a visa."],
     why=("*might* does not change, and the base form follows it. A listener after *say* takes *to*: *said to me*, not *said me*.", "*might* nemainās, aiz tā lieto pamatformu. Adresātu aiz *say* pievieno ar *to*: *said to me*, nevis *said me*."))

# ── Reported questions and requests · B2.2 ────────────────────────────────────────────────────────────────
WORD = ("In a reported question the word order is like a statement: *how she should start* or *how to start*.", "Atstāstītā jautājumā vārdu secība ir kā apgalvojumā: *how she should start* vai *how to start*.")
twin(src_built("rq-B22-1a-r2"), "mcq", "Choose the correct report of her question to you: 'How should I start?'", "She asked me how to start.",
     ["She asked me how should she start.", "She asked me how she should starts.", "She asked me how to starting."], why=WORD)
twin(src_built("rq-B22-3a-r2"), "text", "Report this. Start with *They asked*: 'What time should we arrive?'",
     ["They asked what time they should arrive.", "They asked what time to arrive.", "They asked what time we should arrive.",
      "They asked me what time they should arrive.", "They asked us what time we should arrive.", "They asked me what time to arrive.", "They asked us what time to arrive."],
     why=("Statement order: *what time they should arrive*, or the short *what time to arrive*.", "Apgalvojuma secība: *what time they should arrive* vai īsāk *what time to arrive*."))
twin(src_built("rq-B22-4a-r2"), "mcq", "Which sentence is NOT correct?", "He asked whether or not was I coming.",
     ["She asked if the hotel had a pool.", "They asked how much the tickets cost.", "He asked whether I had finished."],
     why=("After *whether (or not)*: subject + verb: *whether or not I was coming*.", "Aiz *whether (or not)*: teikuma priekšmets + darbības vārds: *whether or not I was coming*."))
twin(src_built("rq-B22-5a"), "mcq", "Choose the correct report of Mr Ozols's question: 'Have the invoices been sent?'",
     "Mr Ozols asked whether the invoices had been sent.",
     ["Mr Ozols asked have the invoices been sent.", "Mr Ozols asked whether had the invoices been sent.", "Mr Ozols asked that the invoices had been sent."],
     why=("A yes/no question: *whether* (or *if*) + statement order; here *had been sent*.", "Jā / nē jautājumu ievada ar *whether* (vai *if*) un apgalvojuma vārdu secību; šeit *had been sent*."))

# ── Reporting verbs · C1.2 ────────────────────────────────────────────────────────────────────────────────
twin(src_built("rv-C12-1a-r2"), "mcq", "Which sentence reports this advice: 'If I were you, I'd get a second opinion before the operation.'", "She advised me to get a second opinion before the operation.",
     ["She advised me getting a second opinion before the operation.", "She suggested me to get a second opinion before the operation.", "She advised to me get a second opinion before the operation."],
     why=("*advise* + person + *to* + verb; *suggest* never takes a person + *to*.", "*advise* + persona + *to* + darbības vārds; aiz *suggest* nekad nav persona + *to*."))
twin(src_built("rv-C12-3a-r3"), "text", "My colleague told me: 'You really should have the figures checked before you submit the report.' Report it, starting with *My colleague urged me*.",
     ["My colleague urged me to have the figures checked before submitting the report.", "My colleague urged me to have the figures checked before I submitted the report.",
      "My colleague urged me to have the figures checked before I submit the report.", "My colleague urged me to get the figures checked before submitting the report.",
      "My colleague urged me to get the figures checked before I submitted the report."],
     why=("*urge* + person + *to* + verb: *urged me to have the figures checked* (= arrange for someone to check them).", "*urge* + persona + *to* + darbības vārds: *urged me to have the figures checked* (= panākt, lai skaitļus pārbauda)."))
twin(src_built("rv-C12-4a-r2"), "mcq", "Which sentence has a mistake?", "She threatened calling the police.",
     ["He promised to pay me back.", "He admitted that he had lied.", "They accused him of cheating."],
     why=("*threaten* + *to* + verb: *She threatened to call the police*.", "*threaten* + *to* + darbības vārds: *She threatened to call the police*."))
twin(src_built("rv-C12-5a-r2"), "mcq", "Which sentence reports the client's complaint: 'The delivery was three days late.'",
     "The client complained that the delivery had been three days late.",
     ["The client complained about the delivery had been three days late.", "The client complained that the delivery had be three days late.", "The client complained me that the delivery had been three days late."],
     why=("*complain that* + clause, here *had been*; a listener takes *to*: *complained to me*.", "*complain that* + palīgteikums, šeit *had been*; adresātu pievieno ar *to*: *complained to me*."))

# ── Indirect questions, more uses · B2.2 ──────────────────────────────────────────────────────────────────
TO = ("Question word + *to* + base form: *where to go* = where we should go.", "Jautājamais vārds + *to* + pamatforma: *where to go* = kur mums vajadzētu iet.")
twin(src_built("ia-B22-1a"), "mcq", "Which is correct? 'We weren't sure ___.'", "where to go", ["where to going", "where go we", "where to we go"],
     why=("Question word + *to* + base form: *where to go* = where we should go.", "Jautājamais vārds + *to* + pamatforma: *where to go* nozīmē, kur mums vajadzētu doties."))
twin(src_built("ia-B22-3a"), "text", "Join the sentences, using *to*: She didn't know. Who should she ask?",
     ["She didn't know who to ask.", "She didn't know whom to ask."],
     why=("Question word + *to* + base form: *who to ask* = who she should ask; formal *whom to ask*.", "Jautājamais vārds + *to* + pamatforma: *who to ask* nozīmē, kam viņai vajadzētu jautāt; formāli arī *whom to ask*."))
twin(src_built("ia-B22-4a"), "mcq", "Which sentence is NOT correct?", "We can't decide whether booking the hotel.",
     ["We can't decide where to stay.", "She asked how to reset the router.", "I don't know whether to laugh or cry."],
     why=("*whether* + *to* + base form: *whether to book the hotel*.", "*whether* + *to* + pamatforma: *whether to book the hotel*."))
twin(src_built("ia-B22-5a"), "mcq", "Choose the correct option.", "It remains unclear how we will pay for the repairs.",
     ["It remains unclear how will we pay for the repairs.", "It remains unclear how we will to pay for the repairs.", "It remains unclear how we do will pay for the repairs."],
     why=("Statement order in the clause: *how we will pay*, not *how will we pay*.", "Palīgteikumā apgalvojuma secība: *how we will pay*, nevis *how will we pay*."))

# ── Indirect questions, more uses · C1.2 ──────────────────────────────────────────────────────────────────
EVER = ("*whoever / whatever* = it does not matter who / what; *whoever* is the subject of its verb.", "*whoever / whatever* = nav svarīgi, kas; *whoever* ir sava darbības vārda teikuma priekšmets.")
twin(src_built("ia-C12-1a"), "mcq", "Choose the correct word: ___ arrives last has to wash the dishes.", "Whoever", ["Whomever", "Whatever", "However"],
     why=("*Whoever arrives last* = the person who arrives last; *whoever* is the subject of *arrives*.", "*Whoever arrives last* nozīmē “tas, kurš ierodas pēdējais”; *whoever* ir palīgteikuma teikuma priekšmets, tāpēc neder *whomever*."))
twin(src_built("ia-C12-3a-r3"), "text", "Write one sentence that starts with *Wh…*: It doesn't matter what you decide. I'll support you.",
     ["Whatever you decide, I'll support you.", "Whatever you decide, I will support you.", "Whatever you decide, you'll have my support.", "Whatever you decide, you will have my support."],
     why=("*Whatever you decide* = it does not matter what you decide; a comma after it.", "*Whatever you decide* nozīmē “lai ko tu izlemtu”; aiz tā raksta komatu."))
twin(src_built("ia-C12-4a"), "mcq", "Which sentence is NOT correct?", "Whomever finishes first can go home.",
     ["Invite whoever you like to the party.", "Take whichever seat is free.", "Wherever you go, call me first."],
     why=("The subject of *finishes* is *whoever*, not *whomever*.", "Darbības vārda *finishes* teikuma priekšmets ir *whoever*, nevis *whomever*."))
twin(src_built("ia-C12-5a"), "mcq", "Choose the correct option.", "Why the system failed remains to be explained.",
     ["Why did the system fail remains to be explained.", "Why the system failed it remains to be explained.", "Why failed the system remains to be explained."],
     why=("A question clause as the subject: statement order, no extra *it*.", "Viss palīgteikums *Why the system failed* ir teikuma priekšmets: apgalvojuma vārdu secība, papildu *it* nav vajadzīgs."))

# ── However, although, because of, then · B1.1 ────────────────────────────────────────────────────────────
twin(src_csv("conjunctions-1.csv", "I had dinner. After, I watched a film."), "text", "Correct the mistake: I finished work. After, I went to the gym.",
     ["I finished work. Then I went to the gym.", "I finished work. Then, I went to the gym.", "I finished work. After that, I went to the gym.",
      "I finished work. After that I went to the gym.", "I finished work. Afterwards, I went to the gym.", "I finished work. Afterwards I went to the gym.",
      "I finished work. Afterward, I went to the gym.", "I finished work. Afterward I went to the gym.", "I finished work. Later, I went to the gym.", "I finished work. Later I went to the gym."],
     why=("To introduce the next event, use *Then*, *After that* or *Afterwards*, not *After* on its own.", "Nākamo notikumu ievada ar *Then*, *After that* vai *Afterwards*, nevis ar *After* vienu pašu."))
twin(src_csv("conjunctions-1.csv", "___ she studied hard, she failed the exam."), "gap", "Complete with one word: ___ it rained all day, we enjoyed our trip.",
     "Although | Though | While", why=("*Although* + subject + verb: a contrast (rain, but we enjoyed it).", "*Although* + teikuma priekšmets + darbības vārds: pretstats (lija, tomēr mums patika)."))
twin(src_csv("conjunctions-1.csv", "Before ___ to bed"), "mcq", "Choose the correct option: After ___ the exam, we went out to celebrate.",
     "finishing", ["finish", "to finish"], why=("*before / after* + *-ing*.", "*before / after* + *-ing*."))
twin(src_csv("conjunctions-1.csv", "We cancelled the trip because of it was raining"), "mcq", "Which sentence is NOT correct?", "The match was cancelled because of it was snowing.",
     ["I always stretch before I go for a run.", "The shop was closed. However, the café was open.", "After dinner, we played cards with friends."],
     why=("*because of* + noun (*because of the snow*); *because* + subject + verb (*because it was snowing*).", "*because of* + lietvārds (*because of the snow*); *because* + teikuma priekšmets + darbības vārds (*because it was snowing*)."))

# ── The or no article · B1.2 ──────────────────────────────────────────────────────────────────────────────
twin(src_csv("articles-split-1.csv", "___ unemployed need help to find work."), "mcq", "Choose the correct option: ___ homeless often sleep in the station in winter.",
     "The", ["—", "A"], why=("*the* + adjective = a group of people: *the homeless*.", "*the* + īpašības vārds = cilvēku grupa: *the homeless*."))


def validate():
    assert len(rows) == len(SOURCES) == 33, len(rows)
    dup = [k for k, v in Counter(s["where"] for s in SOURCES).items() if v > 1]
    assert not dup, ("one twin per source", dup)
    for r, s in zip(rows, SOURCES):
        assert (r[3], r[4]) != (s["task"], s["answer"]), "unchanged source"
        assert not re.search(r"\b(past simple|past continuous|past perfect|present perfect|question word|mixed conditional)\b", r[3], re.I), ("grammar term in the task", r[3])
        assert not (re.search(r"one word", r[3], re.I) and r[2] == "gap" and "/" in r[4]), ("word count on a two-word answer", r[3])
    print(f"33 twins, one per source; {dict(Counter(r[2] for r in rows))}")


def review():
    out = list(csv.reader((DRAFTS / "twins-3.csv").open(encoding="utf-8-sig")))[1:]
    L = ["# Twins, batch 3: 33 tasks for review", "",
         "The nine topic-levels the batch-2 report left under 10 check / use tasks. One twin per source task, the same topic, level and task type, another setting. "
         "Written to docs/ITEM-WRITING-RULES.md including the lessons of batches 1 and 2. Approved by the teacher on 4 November.", "",
         "**Corrected after the review in agent/review-twins-3 (4 November):** no speaker tag after a quote (11, 12, 13, 16, 18, 20); no setting that adds nothing (8, 16, 20, 24, 28); "
         "2 asks to imagine it was different and accepts *would understand*; 3 has an unmistakable mistake (*If she would be…*); 4 is a form task with a situation instead of a meaning question; "
         "9, 14, 26, 29 accept more correct answers (*told us to…*, *asked us what time we…*, *you'll have my support*, *Afterward / Later*); 12 and 13 have cleaner wrong options; "
         "17 reports advice with *advise*, the source's skill; 18 reports with *urge* + *have something checked*, with one fitting answer and no grammar term; 24 tests word order with *how we will pay*; "
         "30 has a sentence where only a contrast fits (*___ it rained all day, we enjoyed our trip*); every explanation is about its own task; Latvian words are no longer printed as English examples.", "",
         "**Not taken over:** a 40% share of drag tasks (not a project rule: a twin keeps its source's type, and these sources are mostly choices); *She advised that I have…* for 17 (a formal subjunctive that reads oddly with *I*; *advise me to* keeps the source's skill); "
         "*Complete with one word beginning with Al* for 30 (it gives the answer away; a sentence where only a contrast fits is better); practice-only for 20 (it is a check of the form, the project's rule for evidence).", ""]
    cur = None
    for n, (r, s) in enumerate(zip(out, SOURCES), 1):
        if (r[0], r[1]) != cur: cur = (r[0], r[1]); L += ["", f"## {r[0]} · {r[1]}", ""]
        extra = (" · wrong: " + r[5].replace(" | ", " / ")) if r[2] == "mcq" else ((" · " + r[5].replace("bank: ", "words: ").replace(" | ", " / ")) if r[5] else "")
        L += [f"{n}. *{r[2]}* · {r[3]} → **{r[4].replace(' | ', ' / ')}**{extra}",
              f"   - EN: {r[6]}", f"   - LV: {r[7]}",
              f"   - original ({s['where']}): {s['task']} → {s['answer']}" + (f" · {s['options']}" if s["options"] else "")]
    (DRAFTS / "twins-3-review.md").write_text("\n".join(L) + "\n", encoding="utf-8")


validate()
save("twins-3.csv")   # approved by the teacher on 4 November
review()
