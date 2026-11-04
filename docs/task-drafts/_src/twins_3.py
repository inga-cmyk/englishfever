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
       "Īpašība tagad, sekas pagātnē: *if* + pagātne (*weren't*), *would have* + 3. forma.")
twin(src_built("cm-B22-1a"), "mcq", "Complete: 'If I weren't so impatient, I ___ sold my flat so cheaply last spring.'",
     "wouldn't have", ["wouldn't", "won't have", "hadn't"], why=MIX)
twin(src_built("cm-B22-3a-r2"), "text", "Rewrite as one sentence with *if*: She didn't learn German at school, so she can't understand her new colleagues now.",
     contractions([f"If she had {v} German at school, she {r} understand her new colleagues now." for v in ("learned", "learnt") for r in ("would be able to", "could")]
                  + [f"She {r} understand her new colleagues now if she had {v} German at school." for v in ("learned", "learnt") for r in ("would be able to", "could")]),
     why=("A past event changed (*had learned*), a result now (*would be able to / could*).", "Mainīts pagātnes notikums (*had learned*), sekas tagad (*would be able to / could*)."))
twin(src_built("cm-B22-4a"), "mcq", "Which sentence is NOT correct?", "If she is more patient, she wouldn't have shouted at him.",
     ["If he spoke Italian, he would have enjoyed the tour more.", "If we hadn't sold the car, we would drive to the coast now.", "If I had slept well, I wouldn't feel so tired today."],
     why=("A quality that is not true now: *If she were more patient*, not *is*.", "Īpašība, kas tagad nav patiesa: *If she were more patient*, nevis *is*."))
twin(src_built("cm-B22-2a-r2"), "mcq", "'If he were more confident, he would have asked for a pay rise.' What does it say?",
     "He isn't confident, so he didn't ask.", ["He is confident, but he didn't ask.", "He will be more confident next year.", "He isn't confident, but he asked."],
     why=("*were more confident* = he is not confident (now, in general); *would have asked* = he did not ask.", "*were more confident* = viņš nav pārliecināts (tagad, kopumā); *would have asked* = viņš nepajautāja."))

# ── Mixed conditionals · C1.1 ─────────────────────────────────────────────────────────────────────────────
INV = ("*Had* + subject + 3rd form = *If* + subject + *had* + 3rd form; the result is about now.", "*Had* + teikuma priekšmets + 3. forma = *If* + teikuma priekšmets + *had* + 3. forma; sekas ir par tagadni.")
twin(src_built("cm-C11-1a-r3"), "mcq", "Which sentence without *if* is correct?", "Had we booked earlier, we would be on the beach now.",
     ["Had we book earlier, we would be on the beach now.", "If had we booked earlier, we would be on the beach now.", "Did we book earlier, we would be on the beach now."], why=INV)
twin(src_built("cm-C11-3a-r2"), "text", "Rewrite starting with *Had*: If I had read the contract more carefully, I wouldn't be paying these fees now.",
     ["Had I read the contract more carefully, I wouldn't be paying these fees now.", "Had I read the contract more carefully, I'd not be paying these fees now."], why=INV)
twin(src_built("cm-C11-4a-r2"), "mcq", "Which sentence is NOT correct?", "Hadn't she missed the train, she'd be here now.",
     ["Had he trained harder, he would be in the team now.", "Were she less shy, she would have spoken up.", "Had they not moved, they would live next door now."],
     why=("In the negative, *not* comes after the subject: *Had she not missed the train*.", "Noliegumā *not* liek aiz teikuma priekšmeta: *Had she not missed the train*."))
twin(src_built("cm-C11-5a"), "mcq", "You write a formal report about a past decision with an effect today. Choose the correct option.",
     "Had the software been tested earlier, we would not be fixing these errors now.",
     ["If the software had tested earlier, we would not be fixing these errors now.", "Had the software tested earlier, we would not be fixing these errors now.",
      "Had the software been tested earlier, we will not be fixing these errors now."],
     why=("The software was tested by someone: *had been tested*; the result now: *would not be fixing*.", "Programmu kāds pārbaudīja: *had been tested*; sekas tagad: *would not be fixing*."))

# ── Reported statements · B2.1 ────────────────────────────────────────────────────────────────────────────
twin(src_built("rs-B21-3a-r2"), "text", "Report this. Start with *The coach told us*: 'You must warm up before every match.'",
     ["The coach told us we had to warm up before every match.", "The coach told us that we had to warm up before every match.",
      "The coach told us we must warm up before every match.", "The coach told us that we must warm up before every match."],
     why=("*must* becomes *had to* (or stays *must*); *you* becomes *we*.", "*must* kļūst par *had to* (vai paliek *must*); *you* kļūst par *we*."))
twin(src_built("rs-B21-4a"), "mcq", "Which sentence is NOT correct?", "He told that the shop was closed.",
     ["She said that the bus was full.", "They told me the film had started.", "He told us he was moving abroad."],
     why=("*tell* needs a person: *He told me / us that…*; or use *said*.", "Aiz *tell* jābūt personai: *He told me / us that…*; vai lieto *said*."))
twin(src_built("rs-B21-5a"), "mcq", "Report this naturally: 'I'll call you as soon as I land,' my sister said.",
     "My sister said she would call me as soon as she landed.",
     ["My sister said she will call me as soon as she will land.", "My sister said I would call her as soon as I landed.", "My sister said she would calling me as soon as she landed."],
     why=("*will* becomes *would*; after *as soon as* no *will*; *I* becomes *she* and *you* becomes *me*.", "*will* kļūst par *would*; aiz *as soon as* nav *will*; *I* kļūst par *she*, *you* par *me*."))
twin(src_built("rs-B21-1a-r2"), "mcq", "Report this: 'You might need a visa,' the agent said.", "The agent said I might need a visa.",
     ["The agent said I might needed a visa.", "The agent said I might to need a visa.", "The agent said me I might need a visa."],
     why=("*might* stays *might* + base form; *say* without a person.", "*might* paliek *might* + pamatforma; *say* bez personas."))

# ── Reported questions and requests · B2.2 ────────────────────────────────────────────────────────────────
WORD = ("In a reported question the word order is like a statement: *how she should start* or *how to start*.", "Atstāstītā jautājumā vārdu secība ir kā apgalvojumā: *how she should start* vai *how to start*.")
twin(src_built("rq-B22-1a-r2"), "mcq", "Which report is correct? 'How should I start?' she asked me.", "She asked me how to start.",
     ["She asked me how should she start.", "She asked me how she starts.", "She asked me how to starting."], why=WORD)
twin(src_built("rq-B22-3a-r2"), "text", "Report this. Start with *They asked*: 'What time should we arrive?'",
     ["They asked what time they should arrive.", "They asked what time to arrive."], why=WORD)
twin(src_built("rq-B22-4a-r2"), "mcq", "Which sentence is NOT correct?", "He asked whether or not was I coming.",
     ["She asked if the hotel had a pool.", "They asked how much the tickets cost.", "He asked whether I had finished."],
     why=("After *whether (or not)*: subject + verb: *whether or not I was coming*.", "Aiz *whether (or not)*: teikuma priekšmets + darbības vārds: *whether or not I was coming*."))
twin(src_built("rq-B22-5a"), "mcq", "You write meeting minutes: 'Have the invoices been sent?' Mr Ozols asked. Choose the correct option.",
     "Mr Ozols asked whether the invoices had been sent.",
     ["Mr Ozols asked have the invoices been sent.", "Mr Ozols asked whether had the invoices been sent.", "Mr Ozols asked that the invoices had been sent."],
     why=("A yes/no question: *whether* + statement order, one tense back: *had been sent*.", "Jā / nē jautājums: *whether* + apgalvojuma secība, laiks vienu soli atpakaļ: *had been sent*."))

# ── Reporting verbs · C1.2 ────────────────────────────────────────────────────────────────────────────────
twin(src_built("rv-C12-1a-r2"), "mcq", "Which sentence reports this: 'Why don't we take a taxi?'", "She suggested taking a taxi.",
     ["She suggested us to take a taxi.", "She suggested to take a taxi.", "She suggested take a taxi."],
     why=("*suggest* + *-ing* (or *that* + clause), never *suggest (someone) to*.", "*suggest* + *-ing* (vai *that* + palīgteikums), nekad *suggest (someone) to*."))
twin(src_built("rv-C12-3a-r3"), "text", "Report with a suitable reporting verb: 'Don't forget to bring your passport,' my mother said.",
     ["My mother reminded me to bring my passport.", "My mother told me to bring my passport.", "My mother reminded me not to forget my passport.",
      "My mother told me not to forget my passport.", "My mother warned me not to forget my passport."],
     why=("*remind / tell* someone *to* do something; *warn* someone *not to*.", "*remind / tell* kādu *to* + darbības vārds; *warn* kādu *not to*."))
twin(src_built("rv-C12-4a-r2"), "mcq", "Which sentence has a mistake?", "She threatened calling the police.",
     ["He promised to pay me back.", "He admitted that he had lied.", "They accused him of cheating."],
     why=("*threaten* + *to* + verb: *She threatened to call the police*.", "*threaten* + *to* + darbības vārds: *She threatened to call the police*."))
twin(src_built("rv-C12-5a-r2"), "mcq", "You report in formal English: 'The delivery was three days late,' the client said. Choose the correct option.",
     "The client complained that the delivery had been three days late.",
     ["The client complained about the delivery had been three days late.", "The client complained to be three days late the delivery.", "The client complained me that the delivery was three days late."],
     why=("*complain (to someone) that* + clause, one tense back: *had been*.", "*complain (to someone) that* + palīgteikums, laiks vienu soli atpakaļ: *had been*."))

# ── Indirect questions, more uses · B2.2 ──────────────────────────────────────────────────────────────────
TO = ("Question word + *to* + base form: *where to go* = where we should go.", "Jautājamais vārds + *to* + pamatforma: *where to go* = kur mums vajadzētu iet.")
twin(src_built("ia-B22-1a"), "mcq", "Which is correct? 'We weren't sure ___.'", "where to go", ["where to going", "where go we", "where to we go"], why=TO)
twin(src_built("ia-B22-3a"), "text", "Join the sentences, using *to*: She didn't know. Who should she ask?",
     ["She didn't know who to ask.", "She didn't know whom to ask."], why=TO)
twin(src_built("ia-B22-4a"), "mcq", "Which sentence is NOT correct?", "We can't decide whether booking the hotel.",
     ["We can't decide where to stay.", "She asked how to reset the router.", "I don't know whether to laugh or cry."],
     why=("*whether* + *to* + base form: *whether to book the hotel*.", "*whether* + *to* + pamatforma: *whether to book the hotel*."))
twin(src_built("ia-B22-5a"), "mcq", "You write a formal email. Choose the correct option.", "It remains unclear who will pay for the repairs.",
     ["It remains unclear who will be pay for the repairs.", "It remains unclear who pay will for the repairs.", "It remains unclear who does will pay for the repairs."],
     why=("Inside the clause, normal order: *who will pay*.", "Palīgteikumā parastā secība: *who will pay*."))

# ── Indirect questions, more uses · C1.2 ──────────────────────────────────────────────────────────────────
EVER = ("*whoever / whatever* = it does not matter who / what; *whoever* is the subject of its verb.", "*whoever / whatever* = nav svarīgi, kas; *whoever* ir sava darbības vārda teikuma priekšmets.")
twin(src_built("ia-C12-1a"), "mcq", "Choose the correct word: ___ arrives last has to wash the dishes.", "Whoever", ["Whomever", "Whatever", "However"], why=EVER)
twin(src_built("ia-C12-3a-r3"), "text", "Write one sentence that starts with *Wh…*: It doesn't matter what you decide. I'll support you.",
     ["Whatever you decide, I'll support you.", "Whatever you decide, I will support you."], why=EVER)
twin(src_built("ia-C12-4a"), "mcq", "Which sentence is NOT correct?", "Whomever finishes first can go home.",
     ["Invite whoever you like to the party.", "Take whichever seat is free.", "Wherever you go, call me first."],
     why=("The subject of *finishes* is *whoever*, not *whomever*.", "Darbības vārda *finishes* teikuma priekšmets ir *whoever*, nevis *whomever*."))
twin(src_built("ia-C12-5a"), "mcq", "You write a formal report. Choose the correct option.", "Why the system failed remains to be explained.",
     ["Why did the system fail remains to be explained.", "Why the system failed it remains to be explained.", "Why failed the system remains to be explained."],
     why=("A question clause as the subject: statement order, no extra *it*.", "Jautājuma palīgteikums kā teikuma priekšmets: apgalvojuma secība, bez lieka *it*."))

# ── However, although, because of, then · B1.1 ────────────────────────────────────────────────────────────
twin(src_csv("conjunctions-1.csv", "I had dinner. After, I watched a film."), "text", "Correct the mistake: I finished work. After, I went to the gym.",
     ["I finished work. Then I went to the gym.", "I finished work. Then, I went to the gym.", "I finished work. After that, I went to the gym.",
      "I finished work. After that I went to the gym.", "I finished work. Afterwards, I went to the gym.", "I finished work. Afterwards I went to the gym."],
     why=("*After* alone does not start a sentence: *Then*, *After that* or *Afterwards*.", "Ar *After* vienu pašu teikumu nesāk: *Then*, *After that* vai *Afterwards*."))
twin(src_csv("conjunctions-1.csv", "___ she studied hard, she failed the exam."), "gap", "Complete with one word: ___ the hotel was expensive, we stayed there for a week.",
     "Although | Though | While", why=("*Although* + subject + verb: a contrast.", "*Although* + teikuma priekšmets + darbības vārds: pretstats."))
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
    out = list(csv.reader((DRAFTS / "pending/twins-3.csv").open(encoding="utf-8-sig")))[1:]
    L = ["# Twins, batch 3: 33 tasks for review", "",
         "The nine topic-levels the batch-2 report left under 10 check / use tasks. One twin per source task, the same topic, level and task type, another setting. "
         "Written to docs/ITEM-WRITING-RULES.md including the lessons of batches 1 and 2. Not added yet: pending/ until the teacher's OK.", ""]
    cur = None
    for n, (r, s) in enumerate(zip(out, SOURCES), 1):
        if (r[0], r[1]) != cur: cur = (r[0], r[1]); L += ["", f"## {r[0]} · {r[1]}", ""]
        extra = (" · wrong: " + r[5].replace(" | ", " / ")) if r[2] == "mcq" else ((" · " + r[5].replace("bank: ", "words: ").replace(" | ", " / ")) if r[5] else "")
        L += [f"{n}. *{r[2]}* · {r[3]} → **{r[4].replace(' | ', ' / ')}**{extra}",
              f"   - EN: {r[6]}", f"   - LV: {r[7]}",
              f"   - original ({s['where']}): {s['task']} → {s['answer']}" + (f" · {s['options']}" if s["options"] else "")]
    (DRAFTS / "pending/twins-3-review.md").write_text("\n".join(L) + "\n", encoding="utf-8")


validate()
save("pending/twins-3.csv")
review()
