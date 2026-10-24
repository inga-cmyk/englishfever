"""Other correct answers for typed-sentence tasks (teacher's request, 24 October: no correct answer marked wrong).
Used for the question drafts (docs/task-drafts/_src/lib.py) and for the built-in typed tasks (content_review.py).
  time_front  - a closing time phrase may come first        (The streets are cleaned every night. / Every night the streets are cleaned.)
  drop_that   - so / such ... that: that may be left out    (It was so cold we stayed inside.)
  drop_me     - asked me if / whether: me may be left out   (He asked if I liked jazz.)
  polite      - Make it polite: please, I wonder, Would you mind ...
Contractions ('d = would / had, 's = is / has) are read both ways by the grader, and the other clause order of an if / when / because sentence
is added when a task is imported, so neither is listed here."""
import re

TIME = ["every day", "every morning", "every evening", "every night", "every week", "every weekend", "every year", "every sunday", "on fridays", "on sundays", "on mondays", "on weekdays", "on weekends",
        "yesterday", "last weekend", "last week", "last night", "last year", "last month", "last summer", "today", "tomorrow", "this morning", "this evening", "this afternoon", "this year",
        "tonight", "next week", "next month", "next year", "at nine", "at six", "at seven", "in 1990", "in 1950", "in 1920", "in july", "at night", "at the weekend", "at the moment", "these days",
        "right now", "soon", "lately", "twice a week", "all day", "the next day", "at the end of the month", "on friday evening", "on friday", "within an hour", "within two days",
        "by the end of june", "since last september", "since march", "for hours", "for twenty minutes", "before noon", "after a few lessons", "later this afternoon", "before bed",
        "after the long day", "at sea level", "in the morning", "in the evening", "in the afternoon"]
QUESTION_START = {"what", "who", "where", "why", "how", "which", "when", "is", "are", "do", "does", "did", "can", "could", "will", "would", "has", "have", "had", "was", "were",
                  "should", "may", "might", "must", "shall", "whom"}
STOP = (" as ", " than ", " the one ", " and ", " but ", " so ", " because ", " when ", " while ", " if ", " until ", " that ", " before ", " after ", " unless ", " as soon as ", " which ", " who ", " where ")
STARTERS = {"the", "a", "an", "my", "your", "his", "her", "our", "their", "this", "that", "these", "those", "we", "you", "they", "he", "she", "it", "there", "people", "nobody", "everyone",
            "someone", "somebody", "everybody", "phones", "tea", "cars", "all", "most", "some", "no", "one", "many", "i"}


def _lead(sentence):
    w = sentence.split()[0]
    return sentence[0].lower() + sentence[1:] if w.lower() in STARTERS and w != "I" else sentence


def time_front(sentence):
    """The same statement with its closing time phrase first, or None."""
    body = sentence.rstrip(".!?")
    low = " " + body.lower() + " "
    toks = body.split()
    if len(toks) < 4 or toks[0].lower() in QUESTION_START or "," in body or any(x in low for x in STOP): return None
    for ph in sorted(TIME, key=lambda p: -len(p.split())):
        n = len(ph.split())
        if len(toks) > n + 2 and " ".join(toks[-n:]).lower() == ph:
            rest = " ".join(toks[:-n])
            return ph[0].upper() + ph[1:] + " " + _lead(rest) + sentence[len(body):]
    return None


def drop_that(sentence):
    m = re.search(r"\b(so|such)\b(.*?)\bthat\b ", sentence)
    return (sentence[:m.start()] + m.group(0).replace(" that ", " ", 1) + sentence[m.end():]) if m and " that " in m.group(0) + " " else None


def drop_me(sentence):
    return re.sub(r"\b(asked|told) me (if|whether)\b", lambda m: m.group(1) + " " + m.group(2), sentence, count=1) if re.search(r"\basked me (if|whether)\b", sentence) else None


def polite(sentence):
    """From 'Could you tell me what time the museum closes?' (or Do you know / Can you tell me) the other polite openers."""
    m = re.match(r"^(?:Could you tell me|Can you tell me|Do you know)\s+(.*?)[.?]?$", sentence)
    if not m: return []
    core = m.group(1)
    return ["Could you please tell me %s?" % core, "Could you tell me %s, please?" % core, "Can you please tell me %s?" % core, "Would you mind telling me %s?" % core,
            "Do you happen to know %s?" % core, "I wonder %s." % core, "I was wondering %s." % core, "I'd like to know %s." % core, "Would you tell me %s?" % core]


def extend(task, answers):
    out = list(answers)
    def add(x):
        if x and x not in out: out.append(x)
    for a in list(answers):
        add(time_front(a)); add(drop_that(a)); add(drop_me(a))
    if re.match(r"^(Make it polite|Make it indirect)\b", task):
        for a in list(answers):
            for x in polite(a): add(x)
    return out
