"""Rule cards, new layout (teacher, 28 October): a form table, typical mistakes, and each use with its own
signal words and examples. [[x]] marks the part of the form to notice (coloured); *x* is an example in italics.
Timelines (tl): repeat, always, now, point, experience, recent, upto, future.
Topics not listed here keep the old card (form / use / signals / example)."""

CARDS2 = {
    "present_simple": {
        "en": {
            "table": {"cols": ["Positive", "Negative", "Question"],
                      "rows": [["I / you / we / they", "[[work]]", "[[don't]] work", "[[Do]] you work?"],
                               ["he / she / it", "work[[s]]", "[[doesn't]] work", "[[Does]] she work?"]],
                      "short": "Short answers: *Yes, I [[do]]. / No, she [[doesn't]].*"},
            "mistakes": [["He doesn't works.", "He doesn't work."],
                         ["Does she works?", "Does she work?"],
                         ["She work every day.", "She works every day."]],
            "watch": ["Spelling: *watch → watches, go → goes, study → studies, play → plays; have → has*.", "State verbs (*know, like, want, need, believe*) stay simple: *I know* (not *I'm knowing*).", "*Who* as the subject: no *do*: *Who lives here?* (not *Who does live here?*)"],
            "uses": [{"t": "Habits and routines", "s": ["every day", "usually", "often", "never", "on Mondays"],
                      "ex": ["I [[go]] to the gym on Mondays.", "She never [[drinks]] coffee."]},
                     {"t": "Facts and permanent situations",
                      "ex": ["Water [[boils]] at 100 degrees.", "I [[live]] in Riga."]},
                     {"t": "Timetables", "s": ["at 7.15", "on Friday"],
                      "ex": ["The train [[leaves]] at 7.15.", "The film [[starts]] at eight."]}],
        },
        "lv": {
            "table": {"cols": ["Apstiprinājums", "Noliegums", "Jautājums"],
                      "rows": [["I / you / we / they", "[[work]]", "[[don't]] work", "[[Do]] you work?"],
                               ["he / she / it", "work[[s]]", "[[doesn't]] work", "[[Does]] she work?"]],
                      "short": "Īsās atbildes: *Yes, I [[do]]. / No, she [[doesn't]].*"},
            "mistakes": [["He doesn't works.", "He doesn't work."],
                         ["Does she works?", "Does she work?"],
                         ["She work every day.", "She works every day."]],
            "watch": ["Rakstība: *watch → watches, go → goes, study → studies, play → plays; have → has*.", "Stāvokļa darbības vārdi (*know, like, want, need, believe*) paliek Present Simple: *I know* (nevis *I'm knowing*).", "Ja *Who* ir teikuma priekšmets, *do* nevajag: *Who lives here?* (nevis *Who does live here?*)"],
            "uses": [{"t": "Ieradumi un rutīna", "s": ["every day", "usually", "often", "never", "on Mondays"],
                      "ex": ["I [[go]] to the gym on Mondays.", "She never [[drinks]] coffee."]},
                     {"t": "Fakti un pastāvīgas situācijas",
                      "ex": ["Water [[boils]] at 100 degrees.", "I [[live]] in Riga."]},
                     {"t": "Saraksti", "s": ["at 7.15", "on Friday"],
                      "ex": ["The train [[leaves]] at 7.15.", "The film [[starts]] at eight."]}],
        },
    },
    "present_perfect": {
        "en": {
            "table": {"cols": ["Positive", "Negative", "Question"],
                      "rows": [["I / you / we / they", "[[have]] seen", "[[haven't]] seen", "[[Have]] you seen it?"],
                               ["he / she / it", "[[has]] seen", "[[hasn't]] seen", "[[Has]] she seen it?"]],
                      "short": "Past participle: regular verbs *-ed* (*work[[ed]]*), irregular verbs: learn them (*see - [[seen]], go - [[gone]], be - [[been]]*)."},
            "mistakes": [["I have seen him yesterday.", "I saw him yesterday."],
                         ["I live here since 2020.", "I have lived here since 2020."],
                         ["She has went home.", "She has gone home."]],
            "watch": ["*been* (went and came back) and *gone* (is still there): *She's been to Paris. She's gone to Paris.*", "*already* before the main verb, *yet* at the end: *I've already eaten. Have you eaten yet?*", "*for* + a period, *since* + a starting point: *for five years* (not *since five years*).", "*How long have you lived here?* (not *How long do you live here?*)"],
            "uses": [{"t": "Experience: we don't say when", "s": ["ever", "never", "before", "three times"], "tl": "experience",
                      "ex": ["Have you ever [[been]] to Rome?", "I've [[seen]] this film three times."]},
                     {"t": "Recent news, a result now", "s": ["just", "already", "yet", "recently"], "tl": "recent",
                      "ex": ["I've just [[finished]].", "She hasn't [[called]] yet."]},
                     {"t": "Started in the past, still true now", "s": ["for", "since", "how long", "all my life"], "tl": "upto",
                      "ex": ["We've [[been]] married for 20 years.", "I've [[lived]] here since 2020."]},
                     {"t": "A time that is not finished", "s": ["today", "this week", "this year"], "tl": "upto",
                      "ex": ["I haven't [[seen]] Ted today."]}],
        },
        "lv": {
            "table": {"cols": ["Apstiprinājums", "Noliegums", "Jautājums"],
                      "rows": [["I / you / we / they", "[[have]] seen", "[[haven't]] seen", "[[Have]] you seen it?"],
                               ["he / she / it", "[[has]] seen", "[[hasn't]] seen", "[[Has]] she seen it?"]],
                      "short": "3. forma: kārtnie darbības vārdi ar -ed (*work[[ed]]*), nekārtnie jāiemācās (*see - [[seen]], go - [[gone]], be - [[been]]*)."},
            "mistakes": [["I have seen him yesterday.", "I saw him yesterday."],
                         ["I live here since 2020.", "I have lived here since 2020."],
                         ["She has went home.", "She has gone home."]],
            "watch": ["*been* (aizgāja un atgriezās) un *gone* (joprojām ir tur): *She's been to Paris. She's gone to Paris.*", "*already* pirms pamatdarbības vārda, *yet* beigās: *I've already eaten. Have you eaten yet?*", "*for* + laika posms, *since* + sākuma brīdis: *for five years* (nevis *since five years*). Latviski \"jau piecus gadus\", tāpēc rodas *since*.", "*How long have you lived here?* (nevis *How long do you live here?*). Latviski \"Cik ilgi tu te dzīvo?\" ir tagadnē."],
            "uses": [{"t": "Pieredze: nesakām, kad", "s": ["ever", "never", "before", "three times"], "tl": "experience",
                      "ex": ["Have you ever [[been]] to Rome?", "I've [[seen]] this film three times."]},
                     {"t": "Jaunumi, rezultāts tagad", "s": ["just", "already", "yet", "recently"], "tl": "recent",
                      "ex": ["I've just [[finished]].", "She hasn't [[called]] yet."]},
                     {"t": "Sākās pagātnē, joprojām turpinās", "s": ["for", "since", "how long", "all my life"], "tl": "upto",
                      "ex": ["We've [[been]] married for 20 years.", "I've [[lived]] here since 2020."]},
                     {"t": "Laiks vēl nav beidzies", "s": ["today", "this week", "this year"], "tl": "upto",
                      "ex": ["I haven't [[seen]] Ted today."]}],
        },
    },
    "prep_time_place": {
        "en": {
            "choice": {"cols": ["at", "on", "in"],
                       "rows": [["Time", "clock time, night: *at 7, at night*", "days and dates: *on Monday, on 5 May, on Friday evening*",
                                 "months, years, seasons, parts of the day: *in May, in 2020, in winter, in the morning*"],
                                ["Place", "a point, a place where you do something: *at the bus stop, at work, at home*",
                                 "a surface: *on the table, on the wall, on the third floor*", "inside, a town or a country: *in the fridge, in my bag, in Riga*"]],
                       "note": "No preposition: *tomorrow, yesterday, next Monday, last week, this year, every day*."},
            "mistakes": [["I was born at 1990.", "I was born in 1990."],
                         ["See you on next Monday.", "See you next Monday."],
                         ["The keys are at the table.", "The keys are on the table."]],
            "watch": ["*in the morning*, but *on Monday morning, on Friday evening*.", "*at the weekend* (British), *on the weekend* (American).", "*at home, at work, at school*, but *in the house, in the office*.", "*on the bus / train / plane*, but *in a car / taxi*.", "*arrive in* + a city or country, *arrive at* + a place, never *arrive to*: *We arrived in Riga. We arrived at the station.*"],
            "uses": [{"t": "Ask yourself: a clock time, a day or a longer period? A point, a surface or inside?",
                      "ex": ["I start work [[at]] 9 [[on]] Mondays, but [[in]] summer I work from home."]}],
        },
        "lv": {
            "choice": {"cols": ["at", "on", "in"],
                       "rows": [["Laiks", "pulksteņa laiks, nakts: *at 7, at night*", "dienas un datumi: *on Monday, on 5 May, on Friday evening*",
                                 "mēneši, gadi, gadalaiki, dienas daļas: *in May, in 2020, in winter, in the morning*"],
                                ["Vieta", "punkts, vieta, kur kaut ko dara: *at the bus stop, at work, at home*",
                                 "uz virsmas: *on the table, on the wall, on the third floor*", "iekšā, pilsēta vai valsts: *in the fridge, in my bag, in Riga*"]],
                       "note": "Bez prievārda: *tomorrow, yesterday, next Monday, last week, this year, every day*."},
            "mistakes": [["I was born at 1990.", "I was born in 1990."],
                         ["See you on next Monday.", "See you next Monday."],
                         ["The keys are at the table.", "The keys are on the table."]],
            "watch": ["*in the morning*, bet *on Monday morning, on Friday evening*. Latviski \"piektdienas vakarā\", angliski ar dienu *on*.", "*at the weekend* (britu), *on the weekend* (amerikāņu).", "*at home, at work, at school*, bet *in the house, in the office*.", "*on the bus / train / plane*, bet *in a car / taxi*. Latviski \"autobusā\", angliski *on the bus*.", "*arrive in* + pilsēta vai valsts, *arrive at* + vieta, nekad *arrive to*: *We arrived in Riga. We arrived at the station.*"],
            "uses": [{"t": "Pajautā sev: pulksteņa laiks, diena vai ilgāks laiks? Punkts, virsma vai iekšā?",
                      "ex": ["I start work [[at]] 9 [[on]] Mondays, but [[in]] summer I work from home."]}],
        },
    },
}


import cards2_a2  # noqa: E402
CARDS2.update(cards2_a2.CARDS)
import cards2_rest  # noqa: E402   (reworked after the Adverbs review; replaces the versions above)
CARDS2.update(cards2_rest.CARDS)
import cards2_b  # noqa: E402   (A2 batch 2 and auxiliary verbs)
CARDS2.update(cards2_b.CARDS)
import cards2_c  # noqa: E402   (A2 batch 3)
CARDS2.update(cards2_c.CARDS)
import cards2_d  # noqa: E402   (A2 batch 4)
CARDS2.update(cards2_d.CARDS)
import cards2_e  # noqa: E402   (B1 batch 1)
CARDS2.update(cards2_e.CARDS)
import cards2_f  # noqa: E402   (comparing past tenses)
CARDS2.update(cards2_f.CARDS)

# The form to learn is green in every example (teacher, 28 October): in the italic parts of table cells, notes and
# Watch out, these words get [[ ]]. Parts after "not" / "nevis" (the wrong version) stay as they are.
HL = {
    "present_simple": r"watches|goes|studies|plays|has|know|lives",
    "present_perfect": r"been|gone|already|yet|for|since|lived|eaten",
    "prep_time_place": r"at|on|in|tomorrow|yesterday|next|last|this|every",
    "irregular_plurals": r"days|boys|advice",
    "articles": r"an|a|the",
    "quantity": r"a lot of|a few|a little|How many|How much|some|any|many|much|few|little|no",
    "adverbs": r"\w+ly|well|fast|hard|always|usually|often|sometimes|never|very|really|quite|too|extremely|enough",
    "verb_patterns": r"\w+ing|to \w+|go|laugh|swim",
    "past_simple": r"ago|lived|since",
    "past_continuous": r"went|was going to",
    "agreement": r"",
}


def _mark(sid, text):
    import re
    pat = HL.get(sid)
    if not pat or "*" not in text:
        return text
    rx = re.compile(r"(?<![\w\[])(?:" + pat + r")(?![\w\]])", re.I if sid != "articles" else 0)
    parts = text.split("*")
    for i in range(1, len(parts), 2):
        before = parts[i - 1].rstrip()
        if "[[" in parts[i] or before.endswith("not") or before.endswith("nevis") or before.endswith("(not") or before.endswith("(nevis"):
            continue
        parts[i] = rx.sub(lambda m: "[[" + m.group(0) + "]]", parts[i])
    return "*".join(parts)


def marked(sid, v):
    """A copy of one language's card with the forms in the examples marked green."""
    import copy
    v = copy.deepcopy(v)
    for k in ("choice", "table"):
        if k in v:
            v[k]["rows"] = [[r[0]] + [_mark(sid, c) for c in r[1:]] for r in v[k]["rows"]]
            for n in ("note", "short"):
                if v[k].get(n): v[k][n] = _mark(sid, v[k][n])
    if v.get("watch"): v["watch"] = [_mark(sid, w) for w in v["watch"]]
    return v
