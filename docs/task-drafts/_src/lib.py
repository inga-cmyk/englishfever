"""Helpers that write a task CSV in the format of the Tasks tab (app/src/CustomItems.php)."""
import csv, os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "app", "authoring"))
import italics
# Latvian words without Latvian letters that the built-in list does not have yet. Kept here, not in italics.py, so the published explanations are untouched.
italics.LV_ASCII |= set('''apgriez visas diena datums punkts vieta kur gadalaiks dienas virsmas sienas piektdienas pilsēta divi filma gariem grupai ieradumam nesens notikums noliegts noteikums nulles otrais pirmais tagadnes vienas zilbes abus aizliegts atbildes
beidzas beidzies cita darba divdabi divdabis esam garums grupa ieradums izteikt jebkuru laba ideja lielu lietas likums maigs mana istaba ne nekas nelielu padomu paliek saraksta
tipiska padodas pieder latviski angliski nosauktu pateicas tos pa draugi abos viens vienam gaidu autobusu klausos draugs laikiem stingri tagadne tagadnei tam tava tur zilbe celtnieks viedoklis lielāks mazāks dod rezultatu jauns vecs vecaks gads gadu pasaule pilsetas pilseta cena cenas darbs darbi'''.split())
HEAD = ["topic", "level", "type", "task", "correct answer", "wrong options / checks", "explanation shown to learner", "explanation in Latvian", "thinking level", "replaces", "error types", "practice only", "also topics"]
ERRS = {}   # row index -> error types (docs/ERROR-TYPES.md), written in the last column; never shown to learners
# matching tasks that were corrected: the old pairs, so importing the corrected file retires the old (ambiguous) version
import json as _json
REPL = _json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "replaced_match.json"), encoding="utf-8"))
rows = []

# Latvian wording follows docs/LATVIAN-TERMS.md: English tense names are kept, "3. forma" for the participle, "ciešamā kārta", "teikuma priekšmets".
LV_SUBS = [
    (r"[Pp]asīva darbības vārdi", "ciešamās kārtas darbības vārdi"), (r"Pasīvs pagātnē:", "Ciešamā kārta, Past Simple:"), (r"Pasīvs nākotnē:", "Ciešamā kārta, Future:"), (r"Pasīvs procesā:", "Ciešamā kārta, Present Continuous:"),
    (r"Pasīva jautājums:", "Jautājums ciešamajā kārtā:"), (r"Pasīvs, ", "Ciešamā kārta, "), (r"Pasīvs:", "Ciešamā kārta:"), (r"pasīvs\b", "ciešamā kārta"), (r"Pasīvs\b", "Ciešamā kārta"),
    (r"[Vv]ienkāršo tagadni|[Vv]ienkāršā tagadne", "Present Simple"), (r"[Vv]ienkāršo pagātni|[Vv]ienkāršā pagātne", "Past Simple"),
    (r"[Tt]agadnes ilgstošā forma|[Tt]agadnes ilgstošo formu|[Tt]agadnes ilgstošā", "Present Continuous"), (r"[Pp]agātnes ilgstošā forma|[Pp]agātnes ilgstošo formu", "Past Continuous"),
    (r"[Ii]lgstošā forma", "Continuous forma"), (r"[Ss]alīdzināmā forma", "pārākā pakāpe"), (r"[Ss]alīdzināmo formu", "pārāko pakāpi"),
    (r"pagātnes divdabi\b", "3. formu"), (r"pagātnes divdabis\b", "3. forma"), (r"[Dd]ivdabi\b", "3. formu"), (r"[Dd]ivdabis\b", "3. forma"),
    (r"(?<![Tt]eikuma )(?<![Tt]eik\. )\b[Pp]riekšmets\b", "teik. priekšmets"), (r"(?<!teikuma )(?<!teik\. )\bpriekšmeta\b", "teikuma priekšmeta"), (r"(?<!teikuma )(?<!teik\. )\bpriekšmetu\b", "teikuma priekšmetu"),
]
def lv_fix(t):
    t = t.replace("*", "")
    for a, b in LV_SUBS: t = re.sub(a, b, t)
    return italics.lv_mark(t)   # every English word in a Latvian explanation is an example: the same rule the built-in explanations use
def mc(t, lv, b, q, ok, wrong, why, lvw):
    why, lvw = audit_fixes.WHY.get(q, (why, lvw))
    fx = audit_fixes.MCQ.get((q, ok)) or audit_fixes.MCQ.get(("*", ok))   # corrections from the audit (audit_fixes.py)
    old = None
    if fx:
        if fx.get("ok", ok) != ok: old = ok
        wrong, q, ok = fx.get("wrong", wrong), fx.get("q", q), fx.get("ok", ok)
    rows.append([t, lv, "mcq", q, ok, " | ".join(wrong), why, lvw, b] + ([old] if old else []))
def replaces(old):
    """The last row replaces an older version that was already imported: the old *correct option* (choose), *sentence* (word order) or *task text* (other types). The importer retires the old one."""
    rows[-1] = rows[-1][:9] + [old]

# A typed gap with a verb in brackets and nothing in the sentence that fixes the tense names the tense (teacher's decision, 25 October):
# otherwise a learner who writes another correct tense is marked wrong. Topics with several accepted forms (future) and used to are left alone.
_TENSE = {"Present simple": "the present simple", "Present continuous": "the present continuous", "Past simple": "the past simple", "Past continuous": "the past continuous",
          "Present perfect": "the present perfect", "Present perfect continuous": "the present perfect continuous", "Past perfect": "the past perfect",
          "Present simple passive": "the present simple passive", "Past simple passive": "the past simple passive", "Present continuous passive": "the present continuous passive",
          "Present perfect passive": "the present perfect passive", "Future passive (will be done)": "the future passive"}
_CUE = {
    # every / usually / how often / last / yesterday do not fix the tense: "How often did she visit…?", "I was thinking about you yesterday" (teacher, 28 October, c-1047)
    "Present simple": r"vegetarian|loves it|how much",
    "Present continuous": r"\bnow\b|at the moment|right now|\btoday\b|this (week|month)|look!|shh|be quiet|these days|tonight|tomorrow|so there is|haven't decided|\bat (six|\d)|very quiet",
    "Past simple": r"when i was|at the party|\bwere tired|didn't|after the match|the day before",
    "Past continuous": r"\bwhen\b|\bwhile\b",
    "Present perfect": r"\byet\b|since|\bfor \d|so far|\bever\b|\bnever\b|twice|lately|\bjust\b|already|how long",
    "Present perfect continuous": r"all day|for hours|lately|how long|since|all week|\bfor \d",
    "Past perfect": r"by the time",
    "Present simple passive": r"every|\bever\b|a week|a month|often|usually|in most|in many|all over|from milk|how often|\bwhere\b.*\bbuilt|by children",
    "Past simple passive": r"yesterday|\blast\b|\bago\b|\bin (1|2)\d{3}\b|at the party",
    "Present continuous passive": r"now|at the moment|right now|be quiet|this week|today",
    "Present perfect passive": r"\byet\b|so far|already|can you call|\bever\b",
    "Future passive (will be done)": r"next|tomorrow|before the test|don't worry",
}
def tense_named(topic, q):
    import re as _re
    key = next((k for k in sorted(_TENSE, key=len, reverse=True) if topic.startswith(k)), None)
    if 'have to' in q: return q
    if not key or not _re.search(r"\([a-z /\-']+\)\s*$", q) or _re.match(r"^(Use|Complete|Make|Give|Ask)", q): return q
    if _re.search(_CUE[key], q, _re.I): return q
    return "Use %s: %s" % (_TENSE[key], q)
# typed gaps: the instruction names the kind of word, never the answer (teacher, 27 October: learners do not notice the topic name)
GAP_INSTR = {
    "Prepositions after words (listen to, good at)": "Complete with the correct preposition:",
    "Prepositions of time and place (in, on, at)": "Complete with *in*, *on* or *at*:",
    "Verbs with two objects (give me, tell her)": "Complete with *to* or *for*:",
    "Subject and verb (my friend lives, my friends live)": "Complete with the correct form of *be* or *do*:",
    "Irregular plurals (children, people, men, teeth)": "Write the plural:",
    "Reported questions and requests": "Complete the reported question with a modal verb:",
    "Used to and be used to": "Complete with the correct form of *use*:",
    "Articles": "Complete with *a*, *an* or *the*:",
    "Quantity": "Complete with one word (*much, many, too, enough*…):",
    "Relative clauses": "Complete with a relative word (*who, which, whose, where*…):",
    "Question tags": "Complete the question tag:",
    "Subject and object questions": "Complete the question with one word:",
    "More modals: might, could, be able to": "Complete with a suitable modal verb:",
    "Passive with modals (must be done)": "Complete the passive form:",
    "Causative: have something done": "Complete with the correct form of *have* or *get* + past participle:",
    "Adverbs: manner, frequency, degree": "Complete with an adverb:",
    "So and such": "Complete with *so* or *such*:",
    "Someone, anything, nobody": "Complete with a word like *someone, anything, nowhere*:",
    "Comparison": "Complete the comparison with one word:",
}
def gp(t, lv, b, q, ok, why, lvw, bank=None):
    if not isinstance(ok, str): raise SystemExit("gap answer must be text like \"did\" or \"does / visit\", not a list: " + q)   # a list was written as ['did'] and no answer matched (28 October)
    why, lvw = audit_fixes.WHY.get(q, (why, lvw))   # an explanation that fitted another part of the sentence (audit_fixes.py)
    ok = extra_answers.GAP.get(q, ok)   # a gap whose other correct answers were added by hand (extra_answers.py)
    old = None
    if not bank and q in audit_fixes.NEW_BANK: bank = audit_fixes.NEW_BANK[q]
    if bank and q in audit_fixes.BANK_CHIPS: bank = audit_fixes.BANK_CHIPS[q]   # a card that also fitted the sentence is replaced (audit_fixes.py)
    if q in audit_fixes.BANK_TASK: old, q = q, audit_fixes.BANK_TASK[q]
    q2 = tense_named(t, q) if not bank else q
    if q2 != q: old, q = (old or q), q2
    if not bank and t in GAP_INSTR and not re.match(r"^[A-Z][^.?!_]*:\s", q) and not re.search(r"\([^)]+\)\s*[.?!]?$", q):
        old, q = (old or q), GAP_INSTR[t] + " " + q   # a typed gap with no instruction: say what kind of word goes in (teacher, 27 October); the importer retires the old text
    rows.append([t, lv, "gap", q, ok, ("bank: " + " | ".join(bank)) if bank else "", why, lvw, b] + ([old] if old else []))
def tx(t, lv, b, q, ok, why, lvw):
    why, lvw = audit_fixes.WHY.get(q, (why, lvw))
    ok = list(ok) if isinstance(ok, (list, tuple)) else [x.strip() for x in ok.split("|")]
    ok = ok + [x for x in extra_answers.TEXT.get(q, []) if x not in ok]       # added by hand (extra_answers.py)
    ok = auto_answers.extend(q, ok)                                            # time phrase first, that left out, me left out, polite openers (auto_answers.py)
    rows.append([t, lv, "text", q, " | ".join(ok), "", why, lvw, b])
import alt_orders, auto_answers, extra_answers, audit_fixes
_AUX = "is are was were do does did can could will would have has had shall should may might am".split()
def _is_question(sentence):
    w = sentence.lower().split()
    if len(w) < 3: return False
    if w[0] in _AUX: return True
    return w[0] in ("what", "where", "when", "why", "who", "whom", "how", "which") and (w[1] in _AUX or (len(w) > 2 and w[2] in _AUX and w[1] in ("long", "many", "much", "often", "time", "far", "old")))
_YN = re.compile(r"^(should|can|could|will|would|must|may|might|is|are|was|were|has|have|had) (i|you|we|they|he|she|it|(?:the|my|your|his|her|our|their|this|that) [a-z]+) (.+)$")
def statement_of(s):
    """A yes/no question built from cards without a question mark can also be a correct statement: should we leave → we should leave
    (learners' answers, 26 October). Not when ever / yet / any make the statement wrong, and not for joined questions (… or can I …)."""
    if re.search(r"\b(ever|yet|any|anything|anyone)\b| or ", s): return None
    if re.match(r"^(had|should|were) ", s) and re.search(r"\b(would|will|'ll)\b", s): return None   # an inverted conditional (had she left …, she would …), not a question
    m = _YN.match(s)
    return f"{m.group(2)} {m.group(1)} {m.group(3)}" if m else None
def od(t, lv, b, q, ok, why, lvw, also=None):
    also = list(also or []) + [a for a in alt_orders.alternatives(ok) if a not in (also or [])]   # other correct orders (alt_orders.py)
    if q.startswith("Put the words in order") and statement_of(ok):   # no "make a question" in the instruction: the statement is right too
        for v in [ok] + list(also):
            st = statement_of(v) or (lambda m: m and f"{m.group(1)} {statement_of(m.group(2))}" if statement_of(m.group(2)) else None)(re.match(r"^(.+?) ((?:should|can|could|will|would|must|may|might|is|are|was|were|has|have|had) .+)$", v))
            if st and st not in also and st != ok: also.append(st)
    if _is_question(ok) and "question" not in t.lower() and "question" not in why.lower() and audit_fixes.ORDER_Q[0] not in why:
        why, lvw = why.rstrip() + " " + audit_fixes.ORDER_Q[0], lvw.rstrip() + " " + audit_fixes.ORDER_Q[1]
    rows.append([t, lv, "order", q, ok, ("also accepted: " + " | ".join(also)) if also else "", why, lvw, b])
def mt(t, lv, b, q, pairs, why, lvw):
    old = " ; ".join(f"{a} = {c}" for a, c in pairs)
    fx = audit_fixes.MATCH_BY_OLD.get(old)                                  # an ambiguous matching task is replaced (audit_fixes.py)
    if fx: q, pairs = fx
    if pairs and pairs[0][0] in audit_fixes.MATCH_WHY: why, lvw = audit_fixes.MATCH_WHY[pairs[0][0]]   # a matching task whose topic explanation was about something else
    rows.append([t, lv, "match", q, " ; ".join(f"{a} = {c}" for a, c in pairs), "", why, lvw, b] + ([old] if fx else []))
def plain(task, typ):
    """Instructions stay plain: no setting in front of a question ("At work: which sentence is NOT correct?"), no hint after a word-order
    instruction, no topic after a matching instruction. The sentence, options and tiles carry the content."""
    t = task.strip()
    if typ == "mcq":
        m = re.match(r"^[^:?.]{2,45}: (which .*)$", t, re.I)
        if m: return m.group(1)[0].upper() + m.group(1)[1:]
        if re.match(r"^.* writes: '.*' Choose the correct option\.$", t): return "Which sentence is correct?"
    if typ == "order" and t.startswith("Put the words in order"): return "Put the words in order."
    if typ == "match":
        m = re.match(r"^(Match each beginning with its ending)[:.].*$", t)
        if m: return m.group(1) + "."
    return t


def en_fix(t):
    """The English explanation is English only: an earlier term replacement had put the Latvian name of the passive into it."""
    t = re.sub(r"Ciešamā kārta \(passive\):", "Passive:", t)
    t = re.sub(r"Ciešamā kārta, (Past Simple|Present Continuous|Present Perfect|Present Simple|Future):", lambda m: m.group(1) + " passive:", t)
    t = t.replace("Ciešamā kārta:", "Passive:")
    if re.search(r"[āčēģīķļņšūžĀČĒĢĪĶĻŅŠŪŽ]", t): raise SystemExit("Latvian in an English explanation: " + t)
    return t


DUP_MOVED = {"Rewrite with used to: When I was young, I played the piano every day."}   # in both Past simple and Used to: one copy
ALSO = {}   # row index -> a second topic the task compares with ("also topics" column)
def also(topic):
    ALSO[len(rows) - 1] = topic


PRACTICE_MATCH = re.compile(r"^Match each (base )?(verb|word|adjective) (with|to) its (past|past-simple|3\. form|plural|adverb|comparative)", re.I)
def practice_only(r):
    """Never in the placement test (teacher, 27 October): form-matching whose pairs can be guessed from how the words look,
    and word-order tasks whose hint gives the tested form away (Start with Had I)."""
    return bool((r[2] == "match" and PRACTICE_MATCH.match(r[3])) or (r[2] == "order" and re.search(r"Start with Had I", r[3])))


def save(name):
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", name)
    with open(out, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f); w.writerow(HEAD)
        for i, r in enumerate(rows):
            if r[0] == "Past simple" and plain(r[3], r[2]) in DUP_MOVED: continue   # the used to topic has the same task: that copy takes over
            if r[0] == "Used to and be used to" and plain(r[3], r[2]) in DUP_MOVED and len(r) > 9 and not r[9]: r = r[:9] + ["from: Past simple"] + r[10:]
            elif r[0] == "Used to and be used to" and plain(r[3], r[2]) in DUP_MOVED and len(r) <= 9: r = r + ["from: Past simple"]
            if r[0] == "Past simple" and re.search(r"\bused? to\b|___ to .*\(use\)", " ".join(str(x) for x in r[3:6]), re.I):   # used to has its own topic (teacher, 27 October)
                old = plain(r[3], r[2]); new = re.sub(r"^Use the past simple: ", "", old)
                r = r[:9] + ["from: Past simple" + (" | " + old if new != old else "")] + r[10:]; r[0] = "Used to and be used to"; r[3] = new
            if r[2] == "text" and isinstance(r[8], int) and r[8] > 3 and re.match(r"^(Make|Rewrite|Join|Ask|Add|Say|Change|Correct|Report|Write the phrase|Combine)", r[3]): r[8] = 3   # a routine transformation is Apply, not Analyse or Evaluate
            w.writerow(r[:3] + [plain(r[3], r[2])] + r[4:6] + [en_fix(r[6]), lv_fix(r[7])] + r[8:9] + [r[9] if len(r) > 9 else (REPL.get(r[4], '') if r[2] == 'match' else ''), ERRS.get(i, ''), "yes" if practice_only(r) else "", ALSO.get(i, "")])
    print(name, len(rows), "rows")


# ───────── compact builders for the big batches ─────────
LVMAP = {
    "After *did* the verb is in the base form: *stay*.": "Pēc *did* darbības vārds ir pamatformā: *stay*.",
    "*The children* = *they*, so *were*.": "*The children* = *they*, tāpēc *were*.",
    "*The guests* = *they*, so *were*.": "*The guests* = *they*, tāpēc *were*.",
    "*We* goes with *were*, not *was*.": "*We* lieto ar *were*, nevis *was*.",
    "*Wasn't listening* = she was not in the middle of listening.": "*Wasn't listening* = viņa tobrīd neklausījās.",
    "With *last week* (a finished time) we use the past simple.": "Ar *last week* (pabeigts laiks) lieto Past Simple.",
    "We can see it now, so we use *going to*.": "Mēs to redzam tagad, tāpēc lieto *going to*.",
    "After *will* we use the base verb, without *to*.": "Pēc *will* lieto pamatformu bez *to*.",
    "*Bread* is uncountable: *is baked*.": "*Bread* ir neskaitāms: *is baked*.",
    "After *was* we need the 3. form: *destroyed*.": "Pēc *was* vajag 3. formu: *destroyed*.",
    "In a general truth the *if*-part uses the Present Simple, not *will*.": "Vispārīgā patiesībā *if* daļā lieto Present Simple, nevis *will*.",
    "In this *if*-part use the Present Simple, not *will*.": "Šajā *if* daļā lieto Present Simple, nevis *will*.",
    "*Manager* is *he / she*, so *doesn't*.": "*Manager* ir *he / she*, tāpēc *doesn't*.",
    "After *doesn't* the verb has no *-s*.": "Pēc *doesn't* darbības vārdam nav *-s*.",
    "*Understand* is a state verb: *I don't understand*.": "*Understand* ir stāvokļa darbības vārds: *I don't understand*.",
    "*Know* is a state verb: *we know*.": "*Know* ir stāvokļa darbības vārds: *we know*.",
    "After *is* the verb needs *-ing*: *is having*.": "Pēc *is* darbības vārdam vajag *-ing*: *is having*.",
    "After *did* the verb is in the base form: *go*.": "Pēc *did* darbības vārds ir pamatformā: *go*.",
    "After *didn't* we use *use to*, not *used to*.": "Pēc *didn't* lieto *use to*, nevis *used to*.",
    "The Past Continuous action was already in progress when the call came.": "Past Continuous darbība jau norisinājās, kad zvans pienāca.",
    "*They* goes with *were*.": "*They* lieto ar *were*.",
    "A finished time (*last weekend*) needs the Past Simple.": "Pabeigts laiks (*last weekend*) prasa Past Simple.",
    "Use *for* with a length of time, *since* with a starting point.": "*For* lieto ar laika ilgumu, *since* ar sākuma punktu.",
    "*Know* is a state verb: *I've known*.": "*Know* ir stāvokļa darbības vārds: *I've known*.",
    "After *been* the verb needs *-ing*.": "Pēc *been* darbības vārdam vajag *-ing*.",
    "The earlier event needs *had finished*.": "Agrākajam notikumam vajag *had finished*.",
    "*Never* already makes it negative: no *n't*.": "*Never* jau ir noliegums: bez *n't*.",
    "After *when* we use the Present Simple for the future.": "Pēc *when* nākotnei lieto Present Simple.",
    "*Breakfast* is singular: *is served*.": "*Breakfast* ir vienskaitlī: *is served*.",
    "*Machines* is plural: *are checked*.": "*Machines* ir daudzskaitlī: *are checked*.",
    "After *is* we need the 3. form: *visited*.": "Pēc *is* vajag 3. formu: *visited*.",
    "After *was* we need the 3. form: *robbed*.": "Pēc *was* vajag 3. formu: *robbed*.",
    "*Trees* is plural: *were damaged*.": "*Trees* ir daudzskaitlī: *were damaged*.",
    "After *being* we need the 3. form: *written*.": "Pēc *being* vajag 3. formu: *written*.",
    "*Rooms* is plural: *are being cleaned*.": "*Rooms* ir daudzskaitlī: *are being cleaned*.",
    "After *been* we need the 3. form: *signed*.": "Pēc *been* vajag 3. formu: *signed*.",
    "*People* is plural: *have been arrested*.": "*People* ir daudzskaitlī: *have been arrested*.",
    "After *will be* we need the 3. form: *introduced*.": "Pēc *will be* vajag 3. formu: *introduced*.",
    "We need *be*: *will be announced*.": "Vajag *be*: *will be announced*.",
    "*Will* is not used after *if* or *unless* here.": "Pēc *if* vai *unless* šeit nelieto *will*.",
    "After *if* we need the Present Simple, not *will*.": "Pēc *if* vajag Present Simple, nevis *will*.",
    "*Unless* already means *if not*: no second negative.": "*Unless* jau nozīmē *if not*: otra noliegumu nevajag.",
    "In the second conditional the *if* part uses the past: *knew*, not *would know*.": "Otrajā nosacījumā *if* daļā lieto pagātni: *knew*, nevis *would know*.",
    "The result part needs *would*: *she would buy it*.": "Rezultāta daļā vajag *would*: *she would buy it*.",
    "The third conditional uses *had* in the *if* part: *had studied*, not *would have studied*.": "Trešajā nosacījumā *if* daļā ir *had*: *had studied*, nevis *would have studied*.",
    "After *wouldn't have* we need the 3. form: *missed*.": "Pēc *wouldn't have* vajag 3. formu: *missed*.",
    "*Told* needs an object: *told me*; *said* does not.": "Aiz *told* vajag papildinātāju: *told me*; aiz *said* tā nav.",
    "With *will* in the report we need *would*: *would come*.": "Netiešajā runā *will* kļūst par *would*: *would come*.",
    "In a reported question the verb follows the subject: *where I lived*.": "Netiešajā jautājumā darbības vārds ir aiz teik. priekšmeta: *where I lived*.",
    "After *asked* the question has normal word order, without *did*.": "Pēc *asked* jautājumam ir parastā vārdu secība, bez *did*.",
    "In an indirect question the verb follows the subject: *where the platform is*.": "Netiešajā jautājumā darbības vārds ir aiz teik. priekšmeta: *where the platform is*.",
    "No *does* in an indirect question: *what time breakfast starts*.": "Netiešajā jautājumā nav *does*: *what time breakfast starts*.",
}

class Topic:
    """One topic with default explanations (English, Latvian) per question type. Item-specific explanations override them."""
    def __init__(self, name, mcq_b=2, text_b=4, match_b=2, err="", **ex):
        self.t = name; self.ex = ex; self.seen = set(); self.mb = mcq_b; self.tb = text_b; self.xb = match_b; self.err = err
    def _tag(self, err=None):
        if err or self.err: ERRS[len(rows) - 1] = err or self.err
    def _why(self, kind, why):
        if isinstance(why, (tuple, list)): return why
        if why: return (why, LVMAP[why])   # an English-only explanation must have its Latvian twin in LVMAP
        return self.ex[kind]
    def _sub(self, w, why, q, ans):
        """A topic with several rules: a task that would get the topic's general line gets the line for its own rule (audit_fixes.SUBRULES)."""
        if why: return w
        text = q + " => " + (ans if isinstance(ans, str) else " / ".join(ans))
        for topic, rx, line in audit_fixes.SUBRULES:
            if self.t.startswith(topic) and re.search(rx, text, re.I): return line
        return w
    def _uniq(self, q, extra=""):
        key = (q, extra)
        if key in self.seen: raise SystemExit("duplicate in script: " + q)
        self.seen.add(key)
    def order(self, lv, sent, also=None, why=None, cue="Put the words in order.", b=3):
        self._uniq(cue, sent); w = self._sub(self._why("order", why), why, cue, sent); od(self.t, lv, b, cue, sent, w[0], w[1], also); self._tag()
    def bank(self, lv, q, ans, extra, why=None, b=3):
        self._uniq(q); w = self._why("bank", why); ans = [ans] if isinstance(ans, str) else ans; w = self._sub(w, why, q, ans)
        assert len(set(ans + extra)) == len(ans + extra) and len(extra) >= 1, q
        gp(self.t, lv, b, q, " / ".join(ans), w[0], w[1], bank=ans + extra); self._tag()
    def gap(self, lv, q, ans, why=None, b=3):
        self._uniq(q); w = self._sub(self._why("gap", why), why, q, ans); gp(self.t, lv, b, q, ans, w[0], w[1]); self._tag()
    def text(self, lv, q, ans, why=None, b=None):
        self._uniq(q)
        w = self._sub(self._why("text", why), why, q, ans if isinstance(ans, str) else " | ".join(ans))
        if not why and re.match(r"^(Make it negative|Make the sentence negative|Make a question|Make it a question)", q) and not re.search(r"Negative|Question", w[0]):
            key = next((k for k in sorted(audit_fixes.NEGQ, key=len, reverse=True) if self.t.startswith(k)), None)
            if key: w = audit_fixes.NEGQ[key]   # a negative or question task gets the negative / question line of its tense
        if not why and re.match(r"^(Question|Negative)", w[0]) and not re.match(r"^(Make (it )?(negative|a question)|Make the sentence negative|Ask|Add a question tag)", q):
            w = self.ex.get("gap") or w   # the default text explanation is about questions and negatives: a join or rewrite task gets the topic's general rule
        tx(self.t, lv, b or self.tb, q, ans, w[0], w[1]); self._tag()
    def mcq(self, lv, q, ok, wrong, why=None, b=None):
        self._uniq(q); w = self._sub(self._why("mcq", why), why, q, ok); mc(self.t, lv, b or self.mb, q, ok, wrong, w[0], w[1]); self._tag()
    def match(self, lv, q, pairs, why=None, b=None):
        self._uniq(q); w = self._why("match", why); mt(self.t, lv, b or self.xb, q, pairs, w[0], w[1]); self._tag()
