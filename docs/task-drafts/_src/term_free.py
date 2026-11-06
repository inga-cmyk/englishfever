"""Tasks without grammar terms (teacher, 6 November; docs/ITEM-WRITING-RULES.md "No grammar terms, precise prompts").
lib.save() passes every row through fix(): a task whose text names a form gets a prompt that makes the form necessary instead,
the old text goes into "replaces" (so the import retires the published version), and a second correct form can get its own note
("answer notes": the explanation shown only to whoever wrote that form)."""
import re

PREFIX = [   # old start of the task -> new start ("" = no instruction: the sentence does the work)
    ("Use the present perfect or the past simple: ", ""),
    ("Use the past simple, past continuous or past perfect: ", ""),
    ("Complete the question tag: ", "Complete the short question at the end: "),
    ("Add a question tag: ", "Add a short question at the end to check you are right: "),
    ("Complete with the correct preposition: ", "Write the missing word: "),
    ("Write the preposition: ", "Write the missing word: "),
    ("Complete with a suitable modal verb: ", "Write the missing word or words: "),
    ("Complete the reported question with a modal verb: ", "Report the question: "),
    ("Write the plural: ", "Complete: "),
    ("Rewrite with an adverb: She is a careful driver.", "Say the same with *drives*: She is a careful driver."),
]
WHOLE = {   # exact old task text -> new text (and, where the answer changes, new correct / wrong)
    "Change to the passive: Someone stole my wallet.": {"task": "Start with *My wallet*: Someone stole my wallet."},
    "Mozart ___ more than 600 pieces of music. (write)": {"task": "Mozart, who died in 1791, ___ more than 600 pieces of music. (write)"},
    "Complete with an adverb: I ___ drink coffee in the evening because it keeps me awake.": {"task": "Write one word that fits: I ___ drink coffee in the evening because it keeps me awake."},
    "Complete with an adverb: This coffee is ___ hot to drink. I can't drink it.": {"task": "Complete: This coffee is ___ hot to drink. I can't drink it."},
    "Match each verb with its 3. form.": {"task": "Match each word with the form that fits 'I have ___ it.'"},
    "Match each verb with its past form.": {"task": "Match each word with the form that fits 'Yesterday I ___.'"},
    "Match each word with its plural.": {"task": "Match each word with the word for more than one."},
    "Match each sentence with the reporting verb.": {"task": "Match each sentence with its report."},
    "Which sentence has the correct tag?": {"task": "Which sentence is correct?"},
    "Match each sentence with its tag.": {"task": "Match each beginning with its ending."},
    "Match each short sentence with its tag.": {"task": "Match each beginning with its ending."},
    "Which question asks about the object?": {"task": "She said something. Which question asks what it was?"},
    "Match each sentence with its passive version.": {"task": "Match each sentence with the one that means the same, without saying who."},
    "Match each active sentence with its passive.": {"task": "Match each sentence with the one that means the same, without saying who."},
    "Match each active sentence with its passive: past.": {"task": "Match each sentence with the one that means the same, without saying who."},
    "Match each active sentence with its passive: now.": {"task": "Match each sentence with the one that means the same, without saying who."},
    "Match each active sentence with its passive: recent.": {"task": "Match each sentence with the one that means the same, without saying who."},
    "Match each active sentence with its passive: future.": {"task": "Match each sentence with the one that means the same, without saying who."},
    "Match each description with its adjective.": {"task": "Match each description with the right word."},
    "Match each adjective with its kind.": {"task": "Match each word with what it tells us."},
    "Match each adjective with its adverb.": {"task": "Match each word with the form that fits 'He drives ___.'"},
    "Match each adverb with its meaning.": {"task": "Match each word with its meaning."},
    "Which sentence is passive and does not say who does it?": {"task": "Which sentence says that someone empties the bins on Mondays, without saying who?"},
    "Which sentence is passive and does not say who did it?": {"task": "Which sentence says that someone stole my phone, without saying who?"},
    "Which sentence is future passive?": {"task": "Choose the correct option: Tomorrow the shop ___ by the owner for repairs.", "correct": "will be closed", "wrong": "will close | was closed | has closed"},
    "Which sentence uses the Present Simple for a timetable?": {"task": "Which sentence gives the time in the concert programme?"},
    "Match each adjective with its comparative.": {"task": "Match each word with the form that fits 'This one is ___ than that one.'"},
    "Match each adjective with its superlative.": {"task": "Match each word with the form that fits 'It is ___ of all.'"},
}
PASSIVE_BY_ANSWER = {   # "Which sentence is passive?" twice in a2-big-1: told apart by the answer
    "Paper is made from wood.": "Which sentence says that people make paper from wood, without saying who?",
    "The shop was robbed last night.": "Which sentence says what happened to the shop, without saying who did it?",
}
ALREADY_NEW = {"Start with *My wallet*: Someone stole my wallet.": "Change to the passive: Someone stole my wallet."}   # a2-relabelled-1: copied from pasp-B11-3b
ADVERB_SAME = "Complete the second sentence so that it means the same: "
NOTES = {   # new task text -> (extra accepted answer added to the correct answer, English note, Latvian note)
    "Tom ___ his key. He can't get into the house now. (lose)": ("lost",
        "Correct too. *Tom lost his key* only tells what happened; *has lost* also says that he still hasn't got it now.",
        "Arī pareizi. *Tom lost his key* tikai pasaka, kas notika; *has lost* pasaka arī to, ka atslēgas viņam joprojām nav."),
    "I ___ here since 2010. I still work here. (work)": ("have been working",
        "Correct too. *Have been working* puts more weight on the work going on all this time.",
        "Arī pareizi. *Have been working* vairāk uzsver, ka darbs turpinās visu šo laiku."),
    "When Sarah arrived at the party, Paul wasn't there. He ___ home. (go)": ("went",
        "Correct too in everyday speech. *Had gone* makes it clear that he left before Sarah arrived.",
        "Ikdienas runā arī pareizi. *Had gone* skaidri pasaka, ka viņš aizgāja, pirms Sāra atnāca."),
    "I got up and ___ out of the window. The sun ___. (look / shine)": ("looked / shone",
        "Correct too. *The sun shone* just states the fact; *was shining* paints the scene you saw at that moment.",
        "Arī pareizi. *The sun shone* tikai konstatē faktu; *was shining* uzbur ainu, ko tajā brīdī redzēji."),
    "The house was dirty. They ___ it for weeks. (not / clean)": ("hadn't been cleaning",
        "Correct too. *Hadn't been cleaning* stresses the weeks without cleaning, not just the result.",
        "Arī pareizi. *Hadn't been cleaning* uzsver nedēļas bez tīrīšanas, ne tikai rezultātu."),
}


def _cond(text):
    m = re.match(r"^Rewrite as a (second|third) conditional: (.+)$", text)
    if not m: return None
    first = m.group(2).split()[0]
    subj = {"I": "I", "He": "he", "She": "she", "We": "we", "They": "they"}.get(first, first.lower())
    lead = "Imagine it is different" if m.group(1) == "second" else "Imagine it happened differently"
    return f"{lead}. Start with *If {subj}*: {m.group(2)}"


def fix(task, typ, correct, wrong, line_no=None):
    """-> (task, correct, wrong, replaces or None, notes string)"""
    if task in ALREADY_NEW: return task, correct, wrong, ALREADY_NEW[task], ""   # a copy that takes its new text from the built-in task
    new, c, w = task, correct, wrong
    if task in WHOLE:
        d = WHOLE[task]; new = d["task"]; c = d.get("correct", c); w = d.get("wrong", w)
    elif task == "Which sentence is passive?" and correct in PASSIVE_BY_ANSWER:
        new = PASSIVE_BY_ANSWER[correct]
    elif task.startswith("Complete with an adverb: "):
        new = ADVERB_SAME + task[len("Complete with an adverb: "):]
    elif _cond(task):
        new = _cond(task)
    else:
        for old, rep in PREFIX:
            if task.startswith(old):
                new = rep + task[len(old):]; break
        if new in WHOLE: new = WHOLE[new]["task"]   # Mozart: the prefix goes, then the sentence gets "who died in 1791"
    notes = ""
    if new in NOTES:
        alt, en, lv = NOTES[new]
        groups = [g.strip() for g in c.split(" / ")]
        parts = [p.strip() for p in alt.split(" / ")]
        if len(parts) == len(groups):   # add the second form to each blank that needs it
            groups = [g if p in [x.strip() for x in g.split("|")] else f"{g} | {p}" for g, p in zip(groups, parts)]
            c = " / ".join(groups)
        notes = f"{alt} :: {en} :: {lv}"
    if new == task and c == correct and w == wrong: return task, correct, wrong, None, ""
    rep = None if typ == "match" else (correct if typ == "mcq" and c != correct else task)   # a choice task whose answer changes is found by its old answer
    return new, c, w, rep, notes
