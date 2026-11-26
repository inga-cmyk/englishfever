#!/usr/bin/env python3
"""Gates for task-writing rules that used to live only in docs/ITEM-WRITING-RULES.md (teacher, 11 November): a new task that
breaks one of them stops this test, and the packaging with it.
    python3 app/tests/item_gates_test.py            # every task the app can serve (built-in bank and docs/task-drafts/*.csv)
    python3 app/tests/item_gates_test.py --update   # after the teacher has read the list: write the present findings as the baseline
- item_gates_baseline.json: findings that existed when a gate was added (known debt, or read and found fine). They do not fail;
  they are counted. A finding that is not in the baseline fails.
- bad_examples.json: old faulty tasks. Every one with a "gate" must still be caught by that gate, so a gate cannot be weakened
  unnoticed. Those with "reader" cannot be caught by a script: they are the cases the second reader of a draft looks for.
A gate is a heuristic: when it flags a task that is fine, read it, then add it with --update; never loosen the task to pass."""
import hashlib, json, os, re, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
BASE = os.path.join(HERE, "item_gates_baseline.json"); BAD = os.path.join(HERE, "bad_examples.json")

TERMS = (r"\b(passive|present perfect|past simple|present simple|past perfect|future simple|continuous|conditional|modal|preposition|adverb|"
         r"adjective|noun|tense|plural|singular|gerund|infinitive|participle|article|pronoun|backshift|question tag|auxiliary|clause|"
         r"comparative|superlative|reported speech)s?\b")
# Not real forms and not typical learner mistakes. Over-regular forms that learners really write (womans, childs, buyed, didn't used to)
# may be wrong options: they are the mistake the task is about (teacher, 11 November).
NONFORM = (r"\b(wills|coulds|cans|musts|shoulds|woulds|mights|wented|boughted|childrens|gooder|badder|reliabler|beautifuler)\b|"
           r"\bhad (went|did|saw|came|took|ate|wrote|gave|knew|spoke)\b|\b(is|are|am|was|were) (get|go|make|do|have|work|play)\b|"
           r"\bwill \w+(?<!s)(s|ed|ing)\b")
AUX = r"(should|shall|can|could|will|would|must|may|might|is|are|am|was|were|have|has|had)\b"


def instruction(i):
    """The part of the task text that tells the learner what to do (not the sentence itself)."""
    q = i["q"]; m = re.match(r"^([^:]{0,90}):", q)
    if m: return m.group(1)
    if i["kind"] in ("order", "match", "write"): return q
    first = re.split(r"(?<=[.?!])\s", q)[0]
    return "" if "___" in first else first


def g_term(i):      # 29 October, 6 November: no grammar terms in an instruction
    m = re.search(TERMS, instruction(i), re.I)
    return ["grammar term in the instruction: " + m.group(0)] if m else []


def g_bank(i):      # 8 November: word-bank chips are real forms; no We has / I is
    if i["kind"] != "gap" or not i.get("bank"): return []
    out = ["chip is not a real form: " + c for c in i["bank"] if re.search(NONFORM, c, re.I)]
    if i["q"].count("___") == 1:
        m = re.search(r"(?:^|[.!?:]\s+)(We|They|You|I|He|She|It)$", i["q"].split("___")[0].strip())
        if m:
            s = m.group(1)
            for c in i["bank"]:
                w = c.split()[0].lower()
                if (s in ("We", "They", "You") and w in ("has", "is", "was", "does", "am")) or (s in ("He", "She", "It") and w in ("have", "are", "were", "do", "am")) \
                        or (s == "I" and w in ("has", "is", "are", "does", "were")):
                    out.append("chip does not agree with the subject: " + s + " " + c)
    return out


def g_order(i):     # 7 and 11 November (c-1001, c-0037): a word order that is also a correct statement needs "to make a question", a start, or both accepted
    if i["kind"] != "order" or not re.match(AUX, i["sentence"]): return []
    if re.search(r"question|Start with|Ask ", i["q"], re.I): return []
    accepted = i["answers"][0] if i.get("answers") else [i["sentence"]]
    if any(not re.match(AUX, a) and not re.match(r"(when|if|before|after|while|in|on|at)\b", a) for a in accepted): return []
    return ["question word order without 'to make a question': the statement may be correct too"]


def g_which_question(i):   # 29 October: "Make a question" says which question
    if i["kind"] == "order" or not re.search(r"Make (it )?a question\s*[:.]", i["q"], re.I) or re.search(r"Start with", i["q"], re.I): return []
    return ["'Make a question' does not say which (with What / a yes/no question)"]


SPEAKER = r"(she|he|they|we|(the|my|our|her|his) \w+|(?!She\b|He\b|They\b|We\b|I\b)[A-Z]\w+)"
def g_speaker(i):   # 29 October, 11 November: no speaker tag after a quote ('…,' she said.); who speaks is said before the quote or by "Start with"
    q = i["q"] + " " + " ".join(x[0] for x in i.get("pairs") or [])   # also the left sides of matching pairs; not a tag: 'I live in Riga.' She said she ___ (the report itself starts after the quote)
    return ["speaker tag after a quote"] if re.search(r",['’]\s+" + SPEAKER + r"\s+(said|asked|told|replied)\b", q) \
        or re.search(r"[?!]['’]\s+" + SPEAKER + r"\s+(said|asked|told|replied)( me| us| her| him)?\s*[.?]", q) else []


def g_contraction(i):   # 3 November: I'd / she'd must be accepted in a typed sentence (tools/dump_items.php asks the real checker)
    return ["the same answer with 'd is marked wrong: " + i["d_refused"]] if i.get("d_refused") else []


def g_match_labels(i):  # 6 November: matching a sentence to a category label; labels overlap easily (a plan / an arrangement), read every one
    if i["kind"] != "match": return []
    r = [p[1].strip() for p in i["pairs"]]
    if all(len(x.split()) <= 5 and not re.search(r"[.?!]$", x) and re.match(r"(an?|the|something|it|life|how|what)\b", x, re.I) for x in r):
        return ["matching with short labels on the right: check that no two can be swapped"]
    return []


def g_lv(i):        # 6 November: izglītojamie, never skolēni
    t = (i.get("why_lv") or "") + json.dumps(i.get("wrong_why_lv") or "", ensure_ascii=False) + json.dumps(i.get("anotes") or "", ensure_ascii=False)
    return ["'skolēni' in a Latvian text: say izglītojamie"] if re.search(r"skolēn", t, re.I) else []


def g_cond_situation(i):   # 11 November (c-0737): a typed conditional with both parts open and no situation sentence: real and unreal, present and past all fit
    if i["skill"] not in ("cond_second", "cond_third", "cond_mixed") or i["kind"] != "gap" or i.get("bank"): return []
    q = re.sub(r"\([^)]*\)", "", i["q"]); q = re.sub(r"^[^:]{0,90}:\s*", "", q).strip()
    if len([x for x in re.split(r"(?<=[.!?])\s+", q) if x.strip()]) != 1: return []
    m = re.search(r",\s*|\s(?=(?:if|unless)\b)", q, re.I)
    if not m or "___" not in q[:m.start()] or "___" not in q[m.end():]: return []
    return ["typed conditional with both parts open and no situation sentence: give the situation (I failed the test last week. If I ___ …)"]


FRAME = re.compile(r"^(.+?[.!?'’])\s+(Which (sentence|question|option) is (correct|right)\?|Choose the (correct|right|best|more natural|most polite) (option|sentence|answer)\.?)$")


def g_long_frame(i):   # 13 November: "Choose the correct option" needs no story; a situation only where the form depends on it, and short
    if i["kind"] != "mcq": return []
    m = re.match(r"^(.*?)\s*Choose the (correct|right|more natural) option", i["q"])
    if m and len(m.group(1).split()) > 10:
        return ["a long situation before 'Choose the correct option' (" + str(len(m.group(1).split())) + " words): keep it only if the form depends on it"]
    # 14 November (part A): the rule is not about length. A choice without a gap with any sentence before the instruction is read:
    # the situation stays only if a wrong option would be correct English in another situation (baseline = the tasks read and kept)
    m = FRAME.match(i["q"])
    if m and "___" not in i["q"]:
        return ["a situation before '" + m.group(2) + "': cover it; if only one option is still possible English, remove it"]
    return []


def g_point(i):   # 14 November (C1): the app knows the grammar point of every task (content/map.php); a new task gets its point when it is written
    return [] if i.get("point") else ["no grammar point: add the task to docs/grammar-map-src/assign_keys.json, run export.py, then app/authoring/build.py"]


BLIND_FIELDS = ("skill", "level", "kind", "q", "correct", "wrong", "answers", "bank", "sentence", "pairs", "must", "model")


def task_hash(i):
    """What makes a task this task for the learner: text, answers, options, level. A change of one word needs a new blind check."""
    level = "B2.2" if str(i.get("level", "")).startswith("C1") else i.get("level")
    body = {k: i.get(k) for k in BLIND_FIELDS if i.get(k) is not None}
    body["level"] = level
    if i.get("moved_from"): body["skill"] = i["moved_from"]   # a point moved to another topic (22 November) is the same task: no new check
    return hashlib.sha1(json.dumps(body, sort_keys=True, ensure_ascii=False).encode()).hexdigest()[:16]


_REC = os.path.join(ROOT, "docs", "review", "blind", "records.json")
BLIND = json.load(open(_REC, encoding="utf-8")) if os.path.isfile(_REC) else {}
_BH = os.path.join(ROOT, "docs", "review", "blind", "baseline_hashes.json")
BLIND_DEBT = set(json.load(open(_BH, encoding="utf-8"))) if os.path.isfile(_BH) else set()   # tasks as they were when the gate came (to be checked in rounds)


def g_blind(i):   # 14 November (docs/BLIND-CHECK.md): two readers solved the task without the key, a judge decided every flag
    # by the content hash, not the key: a task whose answers or options changed needs a new check, even with the same question
    h = task_hash(i)
    return [] if h in BLIND or h in BLIND_DEBT else ["no blind check: python3 tools/blind_check.py (docs/BLIND-CHECK.md)"]


def _words(s):
    return re.sub(r"[^a-z0-9' ]", " ", str(s).lower().replace("\u2019", "'")).split()


def g_copy(i):      # 21 November (tester: "the instruction gives the form away"): a typed sentence that is already in the instruction
    if i["kind"] not in ("text", "write"): return []
    if re.match(r"(Start with|Say it another way|Rewrite|Correct)", i["q"]): return []   # there the start or the change is the task
    cands = []
    for a in (i.get("answers") or [])[:1]: cands += a[:1] if isinstance(a, list) else [a]
    if i.get("model"): cands.append(i["model"])
    q = " ".join(_words(re.sub(r"\*[^*]+\*", " ", i["q"])))   # the words given in italics are the start, not the answer
    starts = [_words(s) for s in re.findall(r"\*([^*]+)\*", i["q"])]
    for c in cands:
        w = _words(c)
        for s in starts:
            if s and w[:len(s)] == s: w = w[len(s):]; break
        if len(w) >= 3 and " " + " ".join(w) + " " in " " + q + " ":
            return ["the answer can be copied from the instruction: " + " ".join(w)]
    return []


MISTAKE_Q = r"NOT correct|has a mistake"
OBVIOUS = (r"\b(will|would|can|could|should|must|might|may|shall) to \w+|\b(will|would|can|could|should|must|might|may) (are|is|am|was|were)\b|"
           r"\b(recommended|suggested|enjoyed?|finished|avoided?|decided|wanted|promised|hoped) to \w+ing\b")


def g_mistake(i):   # 15 and 21 November: in "Which sentence has a mistake?" no near-copy of the wrong sentence among the right ones, and no mistake nobody makes
    if i["kind"] != "mcq" or not re.search(MISTAKE_Q, i["q"]): return []
    out = []; c = _words(i.get("correct", ""))
    for o in i.get("wrong", []):
        w = _words(o)
        if abs(len(w) - len(c)) <= 2 and len(set(w) ^ set(c)) <= 3:
            out.append("a right sentence is a near-copy of the wrong one (gives the pair away): " + o); break
    m = re.search(OBVIOUS, i.get("correct", ""), re.I)
    if m: out.append("the mistake is one learners do not make (too obvious): " + m.group(0))
    return out


# 21-22 November (teacher): the wrong options are words the card of the task's topic teaches. Checked for linking words, prepositions
# and quantity words only (verb forms are judged by the readers: the card names the forms, not every verb).
CLOSED = set("""although though whereas while however nevertheless nonetheless yet despite because since so therefore consequently unless
whether until before after during without towards than once provided providing owing due instead in on at for to from with by about of into
much many few little lot some any no none every each all both either neither enough too very quite rather""".split())
_META = os.path.join(ROOT, "app", "content", "meta.json")
CARD = {s["id"]: re.sub(r"[\[\]*]", "", json.dumps(s.get("rule", {}), ensure_ascii=False).lower())
        for s in (json.load(open(_META, encoding="utf-8"))["skills"] if os.path.isfile(_META) else [])}


def g_card_words(i):
    opts = []
    if i["kind"] == "mcq" and len(str(i.get("correct", "")).split()) <= 3: opts = i.get("wrong", [])
    if i["kind"] == "gap" and i.get("bank"):
        acc = {a.lower() for g in i.get("answers", []) for a in g}; opts = [c for c in i["bank"] if c.lower() not in acc]
    out = []
    for o in opts:
        w = o.lower().strip().rstrip(".,").split()
        if not w or not all(x in CLOSED for x in w): continue
        if i.get("skill") in CARD and not re.search(r"(?<![a-z])" + re.escape(" ".join(w)) + r"(?![a-z])", CARD[i["skill"]]):
            out.append("wrong option not taught on the card of this topic: " + o)
    return out


_EX_FUNC = set("""a an the i you he she it we they me him her us them my your his its our their this that these those is are was were be been being am do does did have has had will would can could shall should may might must not no and or but if so to of in on at for with by from about as than then there here what where when who whom whose which why how whether yes also too very just only even still already yet ever never more most less some any all each every one two three first last next same other another own such don't doesn't didn't isn't aren't wasn't weren't won't can't couldn't shouldn't wouldn't haven't hasn't hadn't i'm you're he's she's it's we're they're i've you've we've they've i'd you'd he'd she'd we'd they'd i'll you'll he'll she'll we'll they'll let's someone something""".split())


def g_example(i):   # 22 November (tester): the example in an explanation is the task's own sentence, not another task's (*where Anna lives* in a task about the library)
    words = lambda t: re.findall(r"[a-z]+(?:'[a-z]+)?", t.lower())
    stem = lambda w: re.sub(r"(ies|es|s|ed|ing|'s)$", "", w)
    parts = [i.get("q", ""), i.get("correct") or "", i.get("sentence") or "", i.get("model") or ""] + list(i.get("wrong") or []) + list(i.get("bank") or [])
    for g in i.get("answers") or []: parts += g if isinstance(g, list) else [str(g)]
    for p in i.get("pairs") or []: parts += list(p)
    task = {stem(w) for w in words(" ".join(map(str, parts)))}
    out = []
    for f in re.findall(r"\*([^*]+)\*", i.get("why") or ""):
        ws = [w for w in words(f) if w not in _EX_FUNC and len(w) > 2]
        foreign = [w for w in ws if stem(w) not in task]
        if len(words(f)) >= 3 and len(foreign) >= 2 and len(foreign) * 2 >= len(ws) and not re.search(r"[+/,→…]|\.\.\.|\bverb\b|participle|-ing", f):
            out.append("the explanation's example is from another sentence: *" + f + "* (use this task's own answer)")
    return out


GATES = {"term": g_term, "bank": g_bank, "order": g_order, "which_question": g_which_question, "speaker": g_speaker,
         "contraction": g_contraction, "match_labels": g_match_labels, "lv": g_lv, "cond_situation": g_cond_situation, "long_frame": g_long_frame, "point": g_point, "blind": g_blind, "copy": g_copy, "mistake": g_mistake, "card_words": g_card_words, "example": g_example}


def key(i):
    body = i.get("correct") or i.get("sentence") or (" ; ".join(a + " = " + b for a, b in i["pairs"]) if i.get("pairs") else "") or ""
    return " | ".join([i.get("moved_from") or i["skill"], i["level"], i["kind"], i["q"], body])   # the topic the prepared file names


def main():
    tmp = os.path.join(tempfile.mkdtemp(), "items.json")
    r = subprocess.run(["php", os.path.join(ROOT, "tools", "dump_items.php"), tmp], capture_output=True, text=True, env=dict(os.environ, EF_DEV="1"))
    if r.returncode or not os.path.isfile(tmp): print("FAIL could not read the tasks: " + r.stdout + r.stderr); sys.exit(1)
    items = json.load(open(tmp, encoding="utf-8"))
    found = {g: {} for g in GATES}
    for i in items:
        for g, f in GATES.items():
            msgs = f(i)
            if msgs: found[g][key(i)] = {"src": i["src"], "why": msgs}
    if "--update" in sys.argv:
        json.dump({g: sorted(found[g]) for g in GATES}, open(BASE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print("baseline written: " + ", ".join(f"{g} {len(found[g])}" for g in GATES)); return
    base = json.load(open(BASE, encoding="utf-8")) if os.path.isfile(BASE) else {}
    ok = True
    for g in GATES:
        known = set(base.get(g, [])); new = [k for k in found[g] if k not in known]; gone = [k for k in known if k not in found[g]]
        for k in new:
            ok = False; print(f"FAIL [{g}] {found[g][k]['src']}: {'; '.join(found[g][k]['why'])}\n       {k}")
        print(f"{'PASS' if not new else 'FAIL'} {g}: {len(items)} tasks, {len(new)} new, {len(found[g]) - len(new)} known" + (f", {len(gone)} baseline entries no longer needed" if gone else ""))
    n = 0
    for ex in json.load(open(BAD, encoding="utf-8")):
        if "gate" not in ex: continue
        n += 1
        if not GATES[ex["gate"]](ex["task"]):
            ok = False; print(f"FAIL the gate '{ex['gate']}' no longer catches the old mistake: {ex['what']}")
    print(f"{'PASS' if ok else 'FAIL'} {n} old mistakes are still caught by their gates")
    print("ALL PASS" if ok else "SOME FAILED"); sys.exit(0 if ok else 1)


if __name__ == "__main__": main()
