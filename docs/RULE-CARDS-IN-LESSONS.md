# Rule cards in Tutor LMS lessons (teacher, 27 November 2026, option A)

A lesson page on englishfever.com can show the practice app's rule card of a topic, in the app's own design, with a button
that opens ten practice tasks of that topic.

## Shortcode (WordPress plugin *EF Practice*, 1.9.0 or later)

    [ef_rule_card topic="present_simple" lang="lv"]

- `topic`: the topic id from the table below.
- `lang`: `lv` (the Latvian card, button *Trenēties šajā tēmā*) or `en` (the English card, button *Practise this topic*). Default `en`.
- `height` (optional): the starting height in pixels before the card has loaded (default 700). The frame then takes the card's own height.

In the Tutor LMS lesson editor, put the shortcode on its own line (Gutenberg: a *Shortcode* block; classic editor: the text
itself). The card is the app's page `card.html` in a frame, so a corrected card shows in every lesson at once; nothing has to be
pasted again.

## The button

*Practise this topic* goes through the website (`/?ef_practice=open&ef_topic=ID`): a student who is logged in on englishfever.com
is signed in to the app on the way and lands in ten tasks of the topic. A visitor who is not logged in lands on the app's welcome
page; after *Continue as guest* or signing in, the app opens the same topic (it remembers the link in the browser tab).
A direct link without the website also works: `https://practice.englishfever.com/#/topic/ID`.

## Technical notes

- `app/card.html` + `embedCard()` in `app/assets/app.js`; route `#/topic/ID` (`viewTopicLink`, session source `lesson_link`).
- `app/.htaccess` lets only `englishfever.com` and its subdomains show `card.html` in a frame (every other page stays `SAMEORIGIN`).
- `app/sso.php` takes `topic=ID` and opens `#/topic/ID` after the sign-in.
- A topic that has no tasks on the server yet shows *Unknown topic* (the app shows only topics with tasks).

## Topic ids

| Area | Topic | id | Shortcode (Latvian card) |
|---|---|---|---|
| Active tenses | Present simple | `present_simple` | `[ef_rule_card topic="present_simple" lang="lv"]` |
| Active tenses | Present continuous | `present_continuous` | `[ef_rule_card topic="present_continuous" lang="lv"]` |
| Active tenses | Past simple | `past_simple` | `[ef_rule_card topic="past_simple" lang="lv"]` |
| Active tenses | Past continuous | `past_continuous` | `[ef_rule_card topic="past_continuous" lang="lv"]` |
| Active tenses | Present perfect | `present_perfect` | `[ef_rule_card topic="present_perfect" lang="lv"]` |
| Active tenses | Present perfect continuous | `present_perfect_continuous` | `[ef_rule_card topic="present_perfect_continuous" lang="lv"]` |
| Active tenses | Past perfect | `past_perfect` | `[ef_rule_card topic="past_perfect" lang="lv"]` |
| Active tenses | Future: will, going to, present continuous | `future` | `[ef_rule_card topic="future" lang="lv"]` |
| Passive tenses | Present simple passive | `present_simple_passive` | `[ef_rule_card topic="present_simple_passive" lang="lv"]` |
| Passive tenses | Past simple passive | `past_simple_passive` | `[ef_rule_card topic="past_simple_passive" lang="lv"]` |
| Passive tenses | Present continuous passive | `present_continuous_passive` | `[ef_rule_card topic="present_continuous_passive" lang="lv"]` |
| Passive tenses | Present perfect passive | `present_perfect_passive` | `[ef_rule_card topic="present_perfect_passive" lang="lv"]` |
| Passive tenses | Future passive (will be done) | `future_passive` | `[ef_rule_card topic="future_passive" lang="lv"]` |
| Modal verbs | Modal verbs: can, should, must, have to | `modal_verbs` | `[ef_rule_card topic="modal_verbs" lang="lv"]` |
| Comparing things | Comparison: -er, more, the most, as ... as | `comparison` | `[ef_rule_card topic="comparison" lang="lv"]` |
| Conditionals | Zero conditional (if + present, present) | `cond_zero` | `[ef_rule_card topic="cond_zero" lang="lv"]` |
| Conditionals | First conditional (if + present, will) | `cond_first` | `[ef_rule_card topic="cond_first" lang="lv"]` |
| Conditionals | Second conditional (if + past, would) | `cond_second` | `[ef_rule_card topic="cond_second" lang="lv"]` |
| Conditionals | Third conditional (if + had done, would have done) | `cond_third` | `[ef_rule_card topic="cond_third" lang="lv"]` |
| Conditionals | Mixed conditionals | `cond_mixed` | `[ef_rule_card topic="cond_mixed" lang="lv"]` |
| Conditionals | Advanced conditionals: inversion, unless, wish | `cond_advanced` | `[ef_rule_card topic="cond_advanced" lang="lv"]` |
| Reported speech | Reported statements (tense changes) | `rep_statements` | `[ef_rule_card topic="rep_statements" lang="lv"]` |
| Reported speech | Reported questions and requests | `rep_questions` | `[ef_rule_card topic="rep_questions" lang="lv"]` |
| Reported speech | Reporting verbs (suggest, admit, promise...) | `rep_verbs` | `[ef_rule_card topic="rep_verbs" lang="lv"]` |
| Questions inside sentences | Indirect questions (Could you tell me where...) | `ind_polite` | `[ef_rule_card topic="ind_polite" lang="lv"]` |
| Questions inside sentences | Indirect questions, more uses (I don't know what to do) | `ind_advanced` | `[ef_rule_card topic="ind_advanced" lang="lv"]` |
| Active tenses | Used to and be used to | `used_to` | `[ef_rule_card topic="used_to" lang="lv"]` |
| Nouns and articles | Articles: a, an, the | `articles` | `[ef_rule_card topic="articles" lang="lv"]` |
| Nouns and articles | Quantity: some, any, much, many, enough | `quantity` | `[ef_rule_card topic="quantity" lang="lv"]` |
| Linking ideas | Relative clauses (who, which, that, where) | `relative_clauses` | `[ef_rule_card topic="relative_clauses" lang="lv"]` |
| Linking ideas | Time words and clauses (then, while, when, until) | `time_clauses` | `[ef_rule_card topic="time_clauses" lang="lv"]` |
| Question forms | Question tags (isn't it? don't you?) | `question_tags` | `[ef_rule_card topic="question_tags" lang="lv"]` |
| Question forms | Subject and object questions | `subject_object_q` | `[ef_rule_card topic="subject_object_q" lang="lv"]` |
| Verb patterns | Verb patterns: -ing or to | `verb_patterns` | `[ef_rule_card topic="verb_patterns" lang="lv"]` |
| Modal verbs | More modals: might, could, be able to | `more_modals` | `[ef_rule_card topic="more_modals" lang="lv"]` |
| Passive tenses | Passive with modals (must be done) | `passive_modals` | `[ef_rule_card topic="passive_modals" lang="lv"]` |
| Verb patterns | Causative: have something done | `causative` | `[ef_rule_card topic="causative" lang="lv"]` |
| Verb patterns | Verbs with two objects (give me, tell her) | `two_objects` | `[ef_rule_card topic="two_objects" lang="lv"]` |
| Adjectives and adverbs | -ed or -ing adjectives (bored, boring) | `adj_ed_ing` | `[ef_rule_card topic="adj_ed_ing" lang="lv"]` |
| Adjectives and adverbs | Adjective order (a small old car) | `adj_order` | `[ef_rule_card topic="adj_order" lang="lv"]` |
| Adjectives and adverbs | Adverbs: manner, frequency, degree | `adverbs` | `[ef_rule_card topic="adverbs" lang="lv"]` |
| Adjectives and adverbs | So and such | `so_such` | `[ef_rule_card topic="so_such" lang="lv"]` |
| Nouns and articles | Someone, anything, nobody | `indefinite_pronouns` | `[ef_rule_card topic="indefinite_pronouns" lang="lv"]` |
| Prepositions | Prepositions after words (listen to, good at) | `dep_prepositions` | `[ef_rule_card topic="dep_prepositions" lang="lv"]` |
| Active tenses | Subject and verb (my friend lives, my friends live) | `agreement` | `[ef_rule_card topic="agreement" lang="lv"]` |
| Nouns and articles | Irregular plurals (children, people, men, teeth) | `irregular_plurals` | `[ef_rule_card topic="irregular_plurals" lang="lv"]` |
| Prepositions | Prepositions of time and place (in, on, at) | `prep_time_place` | `[ef_rule_card topic="prep_time_place" lang="lv"]` |
| Question forms | Auxiliary verbs: be, do, have (Are you…? Do you…? Have you…?) | `aux_verbs` | `[ef_rule_card topic="aux_verbs" lang="lv"]` |
| Active tenses | Past simple or past continuous | `cmp_ps_pc` | `[ef_rule_card topic="cmp_ps_pc" lang="lv"]` |
| Active tenses | Present perfect or past simple | `cmp_pp_ps` | `[ef_rule_card topic="cmp_pp_ps" lang="lv"]` |
| Active tenses | Narrative tenses: past simple, past continuous, past perfect | `narrative` | `[ef_rule_card topic="narrative" lang="lv"]` |
| Active tenses | Narrative tenses with past perfect continuous | `narrative_b2` | `[ef_rule_card topic="narrative_b2" lang="lv"]` |
| Nouns and articles | The or no article (school, the school) | `articles_b1` | `[ef_rule_card topic="articles_b1" lang="lv"]` |
| Linking ideas | And, but, or, so, because | `conj_basic` | `[ef_rule_card topic="conj_basic" lang="lv"]` |
| Linking ideas | However, although, because of | `conj_linkers` | `[ef_rule_card topic="conj_linkers" lang="lv"]` |
| Linking ideas | Contrast, purpose and reason (although, despite, so that) | `conj_clauses` | `[ef_rule_card topic="conj_clauses" lang="lv"]` |
| Linking ideas | Contrast, purpose, reason and result (whereas, in case, therefore) | `conj_b2` | `[ef_rule_card topic="conj_b2" lang="lv"]` |
| Conditionals | Unreal time and preferences (it's high time, I'd rather) | `unreal_time` | `[ef_rule_card topic="unreal_time" lang="lv"]` |
| Active tenses | Advanced present simple and continuous | `adv_present` | `[ef_rule_card topic="adv_present" lang="lv"]` |
| Active tenses | Advanced past simple, past continuous and past perfect | `adv_past` | `[ef_rule_card topic="adv_past" lang="lv"]` |
| Active tenses | The perfect tenses: forms and uses | `adv_perfect` | `[ef_rule_card topic="adv_perfect" lang="lv"]` |
| Modal verbs | Advanced modals: will, would, should | `adv_will` | `[ef_rule_card topic="adv_will" lang="lv"]` |
| Modal verbs | Advanced modals: can, be able to, may, might | `adv_can` | `[ef_rule_card topic="adv_can" lang="lv"]` |
| Conditionals | The subjunctive: I insist that he be told, if I were | `adv_subj` | `[ef_rule_card topic="adv_subj" lang="lv"]` |
| Active tenses | Subject and verb: advanced rules | `adv_agree` | `[ef_rule_card topic="adv_agree" lang="lv"]` |
| Prepositions | Prepositions: position and advanced patterns | `adv_prep` | `[ef_rule_card topic="adv_prep" lang="lv"]` |
| Linking ideas | Advanced participle clauses | `adv_part` | `[ef_rule_card topic="adv_part" lang="lv"]` |
| Linking ideas | Advanced word order: inversion and fronting | `adv_order` | `[ef_rule_card topic="adv_order" lang="lv"]` |
