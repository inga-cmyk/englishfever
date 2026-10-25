"""Error types (docs/ERROR-TYPES.md): kinds of mistake that work in the background. Learners never see these names; the engine uses them
to choose the next task, to tell a slip from a real gap and, later, to build personal plans.

ERRORS   code -> (short name for the teacher, group)
SKILL_ERR topic -> the codes its tasks train when a task does not name its own (a first, rough link: tasks get their own codes as they are tagged)
"""

ERRORS = {
    # A. verb forms
    "3S": ("he / she / it + -s", "verb forms"),
    "DO": ("questions and negatives need do / does / did", "verb forms"),
    "BASE": ("base form after do / does / did / can / to", "verb forms"),
    "MODAL": ("no do and no to with can / should / must", "verb forms"),
    "BE": ("am / is / are left out", "verb forms"),
    "BE-VERB": ("is / am before a verb (It's depend, I'm agree)", "verb forms"),
    "NEG-INF": ("not to + verb (not don't)", "verb forms"),
    "PAST-FORM": ("past form: -ed and irregular verbs", "verb forms"),
    # B. choosing the tense
    "NOW-HABIT": ("now or always / usually", "tense choice"),
    "STATE-ING": ("know, want, like ... without -ing", "tense choice"),
    "DURATION": ("how long up to now: have done / have been doing, for / since", "tense choice"),
    "FINISHED-TIME": ("finished time: past simple, not have done", "tense choice"),
    "BACKGROUND": ("in progress at a past moment: was / were doing", "tense choice"),
    "TIME-CLAUSE": ("no will after when / if / as soon as", "tense choice"),
    "FUTURE": ("future: will / going to, not the present simple", "tense choice"),
    "BACKSHIFT": ("reported speech: the tense goes back", "tense choice"),
    "COULD": ("could / was able to / managed to", "tense choice"),
    "IF-WOULD": ("no would in the if-part", "tense choice"),
    # C. sentence structure
    "Q-ORDER": ("statement order inside a question (where the station is)", "sentence structure"),
    "IND-YESNO": ("if / whether inside a question", "sentence structure"),
    "AGREE": ("the verb agrees with the subject", "sentence structure"),
    "REL-ORDER": ("preposition at the end of a relative clause", "sentence structure"),
    "REL-WHICH": (", which for extra information and for a whole idea", "sentence structure"),
    "CONTRAST": ("although / even though / despite", "sentence structure"),
    "NP-ORDER": ("My whole section and I", "sentence structure"),
    "DOUBLE-NEG": ("one negative only", "sentence structure"),
    "IT-THERE": ("It's cold / There is a park", "sentence structure"),
    "ADV-PLACE": ("always / never before the verb, after be", "sentence structure"),
    "SAY-TELL": ("tell + person, say (to) + person", "sentence structure"),
    # D. nouns
    "ARTICLE": ("a / the / my before a noun", "nouns"),
    "THE": ("the or no article (life, the sun)", "nouns"),
    "PLURAL": ("one of the + plural", "nouns"),
    "IRR-PLURAL": ("children, people, teeth, feet, mice, police", "nouns"),
    "POSSESSIVE": ("'s (my colleague's name)", "nouns"),
    "UNCOUNT": ("uncountable nouns (news, advice, hair)", "nouns"),
    # E. word patterns
    "PATTERN": ("-ing or to after a verb", "word patterns"),
    "ED-ING": ("bored or boring", "word patterns"),
    "DEP-PREP": ("the preposition after a word (depend on, listen to)", "word patterns"),
    "TWO-OBJ": ("explain it to me, introduce you to", "word patterns"),
    "COMPARE": ("cheaper / the same as / as ... as", "word patterns"),
}

SKILL_ERR = {
    "present_simple": ["3S", "DO", "BASE"],
    "present_continuous": ["BE", "NOW-HABIT", "STATE-ING"],
    "past_simple": ["PAST-FORM", "DO", "BASE"],
    "past_continuous": ["BACKGROUND", "BE"],
    "present_perfect": ["DURATION", "FINISHED-TIME", "PAST-FORM"],
    "present_perfect_continuous": ["DURATION"],
    "future": ["FUTURE", "TIME-CLAUSE"],
    "time_clauses": ["TIME-CLAUSE"],
    "cond_first": ["TIME-CLAUSE"],
    "cond_second": ["IF-WOULD"],
    "cond_third": ["IF-WOULD"],
    "rep_statements": ["BACKSHIFT", "SAY-TELL"],
    "rep_questions": ["Q-ORDER", "IND-YESNO"],
    "ind_polite": ["Q-ORDER", "IND-YESNO"],
    "modal_verbs": ["MODAL"],
    "more_modals": ["MODAL", "COULD"],
    "subject_object_q": ["DO"],
    "indefinite_pronouns": ["DOUBLE-NEG"],
    "adverbs": ["ADV-PLACE"],
    "articles": ["ARTICLE", "THE"],
    "quantity": ["UNCOUNT"],
    "verb_patterns": ["PATTERN", "NEG-INF"],
    "adj_ed_ing": ["ED-ING"],
    "two_objects": ["TWO-OBJ"],
    "comparison": ["COMPARE"],
    "relative_clauses": ["REL-WHICH", "REL-ORDER"],
    "dep_prepositions": ["DEP-PREP"],
    "agreement": ["AGREE", "3S"],
    "irregular_plurals": ["IRR-PLURAL"],
}

assert all(c in ERRORS for codes in SKILL_ERR.values() for c in codes)
