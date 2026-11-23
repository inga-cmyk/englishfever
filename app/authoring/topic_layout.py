"""How the topics are laid out for learners (teacher, 22 November). Display and grouping only, except MOVES.

CARD_LEVEL: every topic card shows one level, A2, B1 or B2: the level the topic really belongs to by its difficulty
(test-english.com and Murphy as the reference, the bulk of its tasks as a check). The tasks keep their own levels (A2.1 ... B2.2),
so which tasks a learner gets, the path and the level test do not change.

ALSO_AREAS: a topic shown in a second group too (the same card and the same topic, not a copy): indirect and reported questions
also under Question forms, where learners look for them.

MOVES: the tasks of a grammar point that belong to another topic. The time words (then, after that, before / after + -ing,
while, when / as soon as + present) were in "However, although, because of, then", which mixed contrast, reason and time; they
are now in "Time words and clauses", in the same area, Linking ideas (teacher, 22 November: not with the conditionals). Same task ids; the prepared files still name the old topic (the
import knows the task by it); the app serves and records the task in the new topic (Content::moved). Answers given before the
move stay in the old topic.

AKA: earlier names of a renamed topic, so prepared files and the "from:" / "also topics" columns that use them still work."""

CARD_LEVEL = {
    # A2
    "present_simple": "A2", "present_continuous": "A2", "past_simple": "A2", "past_continuous": "A2", "present_perfect": "A2",
    "future": "A2", "modal_verbs": "A2", "comparison": "A2", "cond_zero": "A2", "cond_first": "A2", "articles": "A2",
    "quantity": "A2", "subject_object_q": "A2", "aux_verbs": "A2", "verb_patterns": "A2", "two_objects": "A2", "adverbs": "A2",
    "indefinite_pronouns": "A2", "dep_prepositions": "A2", "agreement": "A2", "irregular_plurals": "A2", "prep_time_place": "A2",
    "cmp_ps_pc": "A2", "conj_basic": "A2", "conj_linkers": "A2",
    # B1
    "present_perfect_continuous": "B1", "past_perfect": "B1", "used_to": "B1", "cmp_pp_ps": "B1", "narrative": "B1",
    "present_simple_passive": "B1", "past_simple_passive": "B1", "present_continuous_passive": "B1", "present_perfect_passive": "B1",
    "future_passive": "B1", "passive_modals": "B1", "more_modals": "B1", "cond_second": "B1", "cond_third": "B1",
    "time_clauses": "B1", "rep_statements": "B1", "rep_questions": "B1", "ind_polite": "B1", "relative_clauses": "B1",
    "question_tags": "B1", "articles_b1": "B1", "causative": "B1", "adj_ed_ing": "B1", "adj_order": "B1", "so_such": "B1",
    "conj_clauses": "B1",
    # B2
    "narrative_b2": "B2", "cond_mixed": "B2", "cond_advanced": "B2", "unreal_time": "B2", "rep_verbs": "B2", "ind_advanced": "B2",
    "conj_b2": "B2",
    # C1 (teacher, 22 November)
    "adv_present": "C1", "adv_past": "C1", "adv_perfect": "C1", "adv_will": "C1", "adv_can": "C1", "adv_subj": "C1",
}

ALSO_AREAS = {"ind_polite": ["questions"], "rep_questions": ["questions"], "ind_advanced": ["questions"]}

MOVES = [
    {"from": "conj_linkers", "to": "time_clauses", "points": ["link_time", "fut_time_clause", "vp_prep_ing"]},
]

AKA = {
    "conj_linkers": ["However, although, because of, then"],
    "time_clauses": ["Time clauses (when, as soon as, until)"],
}
