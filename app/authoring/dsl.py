"""Tiny authoring DSL for the practice question bank.

Every item belongs to a skill (a tense + voice), a CEFR sub-level and a Bloom level (1-6).
Run `python3 app/authoring/build.py` to validate everything and write app/content/*.json.

Item kinds
  M  multiple choice   M(skill, lv, bloom, question, correct, [wrong, ...], why, wrong_why={option: message})
                       The correct option is written FIRST; the server shuffles the options.
  G  gap fill          G(skill, lv, bloom, "text with ___", "answer" | ["accepted", ...] | [[blank1 ok...], [blank2 ok...]], why, hints=[(regex, message)])
  T  typed rewrite     T(skill, lv, bloom, "instruction", "answer" | ["accepted", ...], why, hints=[...])
  O  word order        O(skill, lv, bloom, "instruction", "Correct sentence.", why, extra_accept=[...])
  W  write (create)    W(skill, lv, bloom, "prompt", must=[(regex, message)], model="Model answer.", why)
  D  match (drag)      D(skill, lv, bloom, "instruction", [("left 1", "right 1"), ("left 2", "right 2"), ...], why)
                       The learner drags each right-hand card to its left-hand partner. Right-hand cards must all differ.
  G with bank=[...]    a gap fill where the learner drags words from a word bank (the bank holds the answers plus decoys).
  O  word order (drag) is shown as cards to drag into order; extra_accept lists other correct orders (same words).

Answers are compared after the same normalisation the server uses (lower case, straight
apostrophes, contractions such as n't / 're / 'll / 've / 'm expanded, no final punctuation).
"""

ITEMS = []
_counter = {}

LEVELS = ["A2.1", "A2.2", "B1.1", "B1.2", "B2.1", "B2.2", "C1.1", "C1.2"]

ABBR = {
    "present_simple": "ps", "present_continuous": "pc", "past_simple": "pa",
    "past_continuous": "pac", "present_perfect": "pp", "present_perfect_continuous": "ppc",
    "past_perfect": "ppf", "future": "fu",
    "present_simple_passive": "psp", "past_simple_passive": "pasp",
    "present_continuous_passive": "pcp", "present_perfect_passive": "ppp", "future_passive": "fup",
    "modal_verbs": "mv", "cond_zero": "cz", "cond_first": "cf", "cond_second": "cs", "cond_third": "ct", "cond_mixed": "cm", "cond_advanced": "ca",
    "rep_statements": "rs", "rep_questions": "rq", "rep_verbs": "rv", "ind_polite": "ip", "ind_advanced": "ia",
}


def _add(kind, skill, lv, bloom, **kw):
    assert skill in ABBR, skill
    assert lv in LEVELS, lv
    assert 1 <= bloom <= 6
    key = (skill, lv, bloom)
    n = _counter.get(key, 0)
    _counter[key] = n + 1
    item = {"id": f"{ABBR[skill]}-{lv.replace('.', '')}-{bloom}{'abcdefghijkl'[n]}",
            "skill": skill, "level": lv, "bloom": bloom, "kind": kind}
    item.update(kw)
    ITEMS.append(item)


def M(skill, lv, bloom, q, correct, wrong, why, wrong_why=None):
    _add("mcq", skill, lv, bloom, q=q, correct=correct, wrong=list(wrong), why=why, wrong_why=wrong_why or {})


def _blanks(ans):
    if isinstance(ans, str):
        return [[ans]]
    if ans and isinstance(ans[0], list):
        return ans
    return [list(ans)]


def G(skill, lv, bloom, q, ans, why, hints=None, bank=None):
    blanks = _blanks(ans)
    assert q.count("___") == len(blanks), q
    extra = {"bank": list(bank)} if bank else {}
    _add("gap", skill, lv, bloom, q=q, answers=blanks, why=why, hints=[list(h) for h in (hints or [])], **extra)


def T(skill, lv, bloom, q, ans, why, hints=None):
    acc = [ans] if isinstance(ans, str) else list(ans)
    _add("text", skill, lv, bloom, q=q, answers=[acc], why=why, hints=[list(h) for h in (hints or [])])


def O(skill, lv, bloom, q, sentence, why, extra_accept=None):
    _add("order", skill, lv, bloom, q=q, sentence=sentence, answers=[[sentence] + list(extra_accept or [])], why=why)


def D(skill, lv, bloom, q, pairs, why):
    _add("match", skill, lv, bloom, q=q, pairs=[list(p) for p in pairs], why=why)


def W(skill, lv, bloom, q, must, model, why=""):
    _add("write", skill, lv, bloom, q=q, must=[list(m) for m in must], model=model,
         why=why or "Compare your sentence with the model answer.")
