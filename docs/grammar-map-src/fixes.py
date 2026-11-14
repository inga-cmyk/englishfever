# Corrections after the second reader (13 November) and new rows he asked for. Imported after p1-p3 and before p4.
import lib
from lib import P, AREA, POINTS
BY = {p['id']: p for p in POINTS}
def S(id, n=None, v=None, e=None, name=None, level=None, can=None, note=None, te=None):
    p = BY[id]
    if n is not None: p['needs'] = n.split()
    if v is not None: p['vs'] = v.split()
    if e is not None: p['err'] = e
    if name: p['name'] = name
    if level: p['level'] = level
    if can: p['can'] = can
    if te: p['te'] = te
    if note: p['note'] = (p['note'] + ' ' + note).strip()
def E(id, old, new=''):
    p = BY[id]; assert old in p['err'], (id, old); p['err'] = p['err'].replace(old, new).strip('; ').replace(';*', '*').replace('; *)', ')')
def C(id, old, new):
    p = BY[id]; assert old in p['can'], (id, old); p['can'] = p['can'].replace(old, new)

# missing prerequisites
S('there_is', n='be_pres was_were plural_reg')
S('demonstr', n='be_pres plural_reg', can="Points at things near and far, singular and plural, before a noun or alone, and goes on with it, not this, once the thing is known: This is my desk. It's new.",
  e='*This shoes; these book; that are my friends; A: What is this? B: This is a present* for *It is a present*')
S('cmp_adv', n='cmp_er sup adj_adv')
S('the_unique', n='a_the sup', note='Level: the A1 list names the; these uses come half a level later, with the superlative already known. The app has their tasks at A2.2-B1.1.')
S('vp_like_ing', name='Like, love, hate + -ing; want + to', can='Follows the verbs of liking with -ing and want with to: I like cooking. I want to go.', e='PATTERN: *I like cook; I want go; I want going*')
S('pas_will', n='pas_pres will_form going_to')
S('allowed_to', n='can must_have_to was_were')
S('supposed_to', n='must_have_to allowed_to pas_past')
S('q_negative', n='aux_mix')
S('fut_past', n='going_to pastc_form will_form')
S('modals_cont', n='deduction_past pc_form')
S('pas_modal_past', n='pas_modal should_have deduction_past')
S('vp_complex', n='pp_form pas_inf_ing rv_ing')
S('distancing', n='pas_report vp_complex')
S('pas_report', n='pas_past vp_to rep_say_tell', v='rep_backshift distancing', can='Reports what people say or believe without naming them, with both patterns: It is said that the firm is in trouble. The firm is said to be in trouble.')
S('caus_have', n='pas_past pc_form')
S('pas_by', n='pas_pres pas_past')
# false prerequisites
S('c3', n='pastp_form c2')
S('vp_prep_ing', n='vp_ing', v='vp_to dep_adj')
S('purpose_to', n='ps_form')
S('like_as', n='cmp_as', v='senses_like cmp_as')
S('fut_timetable', n='ps_form')
S('c2_were', n='c2')
S('have_got', n='ps_negq', v='ps_negq be_pres')
S('pp_form', n='v3 agr_basic')
S('would_like', n='')
S('could_past', n='can')
S('two_obj', n='obj_pron')
S('poss_s', n='plural_reg', v='poss_adj')
S('wish_past', n='wish_pres pastp_form', v='wish_pres should_have c3')
S('neg_inversion', n='q_yesno pastp_form')
S('vp_make_let', n='obj_pron', v='vp_obj_to allowed_to')
S('vp_see_do', n='obj_pron vp_ing', v='vp_make_let')
S('reason_result_b2', n='because_of')
S('discourse', n='link_however')
S('cmp_double', n='cmp_er')
# levels
S('rep_say_tell', level='A2.2', n='pst_irr obj_pron', note='Level: list A2 and EGP A2 for say / tell without a tense change; the app has its tasks from B1.1.')
S('prep_none', level='A2.1')
S('pas_negq', level='A2.2', note='', te='A2: Present and past simple passive; B1: Passive verb forms')
S('pp_first_time', level='B1.2')
S('vp_adj_to', note='Level: EGP B1; the A2 list line is from memory.')
S('too_to', note='Level: EGP B1-B2; the A2 list line is from memory.')
S('two_obj_pron', note='Level: one step after the basic pattern of the A2 list.')
S('two_obj_explain', note='Level: one step after the basic pattern of the A2 list.')
S('few_little', note='Level: the A2 list names little and few; the negative meaning without a is EGP B2, so it is placed with the B1 list line.')
S('link_adj', note='Level: list B1+, EGP A2; taught by the app from A2.2 on the adverbs card.')
S('q_which_subj', note='Level: taught with subject questions; the list line is from memory.')
# statements
S('c_alt', name='As long as, provided (that), even if, supposing')
C('past_seq', 'When Karen arrived, we had dinner (then) / we were having dinner (already started)', 'When Marta came in, we ate (then) / we were eating (already started)')
C('pp_ps_now', "I've worked here since 2010 / I worked there from 2010 to 2014", "I've taught here since 2015 / I taught there from 2009 to 2015")
S('pp_ps_now', e="*I've taught there from 2009 to 2015; A: I've cut my finger. B: How have you done that?; When have you arrived?* for the details after the news")
S('so_neither', can="Agrees with a positive or a negative sentence using the same helping verb, and with too / either: A: I'm tired. B: So am I. / Me too. A: I don't smoke. B: Neither do I. / I don't either.")
S('reflexive', name='Myself, yourself, themselves; by myself, on my own')
C('phr_sep', 'Turn it off. Look after her.', 'Turn it off. Look after her. Also three-word verbs: I get on with her. We ran out of milk.')
S('neednt_have', e="*We needn't hurried; We needn't have to hurry; We didn't need hurry*")
S('allowed_to', e="*We are allowed park here; It is not allowed to smoke* with it")
S('fut_timetable', e="*The train will leave at 7.15* for a timetable")
S('vp_go_ing', e="*go to shopping; go for swimming; go to home*")
S('indef_form', e="*I didn't see somebody; anybody didn't come*")
S('used_to', e="*I use to get up at seven* for a present habit; *I didn't used to* (the spelling: Murphy gives didn't use to; EGP records both); *I used to went*")
S('two_obj_pron', e="*Give me it* (heard in informal British English; the tasks practise *Give it to me*); *Show me them; I'll buy you it*")
S('c0_c1', e="*If it rains tomorrow, we stay at home*")
S('compound_nouns', e="*a driver of bus; a car's door; my sister car; a ten-years-old boy*")
S('past_seq', e="*I was going there three times; We were walking home after the concert* for a complete action")
# new rows
AREA('Nouns, articles and pronouns')
P('art_zero', 'No article: I like cats. She drinks tea. He lives in Riga.', 'A2.1', "Uses no article with plural and uncountable nouns when speaking in general and with names of people, cities and most countries.",
  n='a_the plural_reg', v='a_the', e="THE: *I like the cats* (all cats); *She drinks the tea every morning; He lives in the Riga*", m='75, 77', t='A1: A / an, the, no article', g='A1 no article',
  topic='articles', rx=r"=> —|\bRiga\b|\bLatvia\b", s='The contrast with a particular group (children / the children) is `art_general` at B1.1')
P('one_ones', 'One and ones: the red one, Which ones?', 'B1.1', "Avoids repeating a countable noun: I'd like the blue one. Which ones are yours? This one is cheaper.",
  n='a_the demonstr', v='ellipsis', e="*I'd like the blue; Which are yours ones?; a one; I need some paper. Can you give me one?* (uncountable)", m='', s='Not a Murphy EGiU unit (Hewings AGU 61). Level: EGP A2-B1; the list has it only inside B2: Ellipsis and substitution',
  t='B2: Ellipsis and substitution', g='A2 one; B1 ones, which one, this one', topic='new')
AREA('Questions')
P('what_like', "What is she like? What does he look like? How is she?", 'A2.2', "Asks for a description with What … like? and about health or mood with How …?",
  n='q_wh', v='vp_like_ing', e="*How is your new boss?* for a description; *How does he look like? What is she like?* answered *She likes tea*", m='', s='Not a Murphy EGiU unit; a standard course-book point with no list line', t='no line in the lists',
  g='A2 be like + noun or pronoun', topic='new')
AREA('Modal verbs')
P('must_vs_have_to', "Must or have to: my own view or somebody else's rule", 'B1.1', "Uses must when the speaker thinks it is necessary and have to for a rule or a situation, and prefers Do I have to …? to Must I …?",
  n='must_have_to', v='must_have_to should', e="*I must wear a uniform at work* said about the company's rule; *Must I sign here?* in everyday speech", m='31', t='B1: Have to, must, should', g='B1 must: obligation and necessity; have to',
  topic='modal_verbs', s='On the modal_verbs card as a Watch out point')
P('wont_refuse', "Won't for refusing: The door won't open", 'B1.2', "Says that a person or a thing refuses to do something now: He won't listen. My laptop won't switch on.",
  n='will_now', v='will_form', e="*My laptop doesn't want to switch on; The door isn't opening* for a refusal", m='21', t='no line of its own (returns in C1: Advanced modals: will, would, should)', g='A2 will: willingness; B1 would: willingness in the past',
  topic='future', rx=r"won't (start|open|work|listen|switch|let|close|move)", s='A Watch out point on the future card')
P('should_expect', 'Should for what we expect: She should be there by now', 'B2.1', "Says what is probably true or will probably happen because it is normal or planned: She left at six, so she should be there by now. The train should be here in five minutes.",
  n='should deduction', v='deduction likely_bound', e="*She must be there by now* where it is only an expectation; *The train should to be here*", m='33', t='C1: Advanced modals: will, would, should (page seen); no B2 line',
  g='B1 should: likelihood; B2 should: expectations', topic='new', s='Level: Murphy treats it at intermediate level and EGP at B1-B2; test-english names it only on the C1 page')
AREA('Joining ideas')
P('both_and', 'Both … and, either … or, neither … nor', 'B1.2', "Joins two things with a pair of words and keeps the verb positive after neither … nor: She speaks both French and German. You can either call or email. He neither smokes nor drinks.",
  n='all_both conj_and_but', v='so_neither all_both', e="DOUBLE-NEG / AGREE: *He doesn't neither smoke nor drink; Both she speaks French and German; Either you call or email*", m='89', t='B1: Both, either, neither',
  g='B1 either … or; both … and with nouns; B2 neither … nor', topic='new')
AREA('Reported speech')
P('rv_that', 'Reporting verbs + that: admit, explain, complain, claim, warn somebody that', 'B2.1', "Reports with a that-clause and the tense one step back: She admitted that she had lost the file. He warned us that the road was closed.",
  n='rep_backshift rep_say_tell', v='rv_ing rv_obj_to', e="SAY-TELL: *He explained me that; She complained me that; He warned that us; She admitted to lose the file*", m='34, 47, 48', t='B1+: Reporting verbs',
  g='B2 reporting verbs (increasing range)', topic='rep_verbs', rx=r"\bthat\b", s='The app has the whole topic at B2.2')
AREA('Verb patterns')
P('vp_need_help', "Need + -ing, help (to) do, can't help -ing; afraid to do / afraid of doing", 'B2.1', "Uses the patterns that do not follow the main lists: The car needs washing. She helped me (to) move. I couldn't help laughing. I'm afraid to tell him / afraid of making a mistake.",
  n='vp_meaning vp_prep_ing', v='vp_meaning', e="*The car needs to wash; She helped me moving; I couldn't help to laugh; I'm afraid of to tell him*", m='57, 66', t='no line in the lists', g='B1 help + object', topic='new',
  s='Standard point from Murphy units 57 and 66; no content and no list line')
AREA('Prepositions')
P('prep_phrases', 'Fixed phrases with a preposition: on holiday, by mistake, at the age of, in my opinion', 'B1.1', "Uses the common fixed phrases as wholes: on business, on purpose, by chance, in a hurry, at first, for sale.",
  e="DEP-PREP: *in holiday; with mistake; in the age of 20; on my opinion; by purpose*", m='127, 128', t='no line in the lists', g='A2-B1 complex prepositions', topic='new', s='Close to vocabulary, like do / make; listed because Latvian uses other prepositions')
S('art_general', n='art_zero the_unique count_unc')

# the teacher's decisions of 13 November (asked one by one)
D = ' Decided by the teacher, 13 November: '
def N(id, old, new):
    p = BY[id]; p['note'] = (p['note'].replace(old, '').strip() + new).strip()
N('pastp_form', 'See the questions for Inga', D + 'B1; the A2.2 path step is not needed.')
N('c2', 'See the questions for Inga', D + 'B1; the A2.2 path step is not needed.')
N('rep_backshift', 'See the questions for Inga', D + 'B1 for the tense change (say / tell alone is A2.2); the A2.2 path step is not needed.')
N('rel_subj', 'See the questions for Inga', D + 'A2.2, as in the list; A2.2 tasks are to be written.')
N('might', '', D + 'A2.2, as in the list; A2.2 tasks are to be written.')
N('wish_pres', '', D + 'B1.2, as in the list; B1.2 tasks are to be written.')
N('would_rather', '', D + 'B1.2, as in the list; B1.2 tasks are to be written.')
N('c_inv', 'See the questions for Inga', D + 'B2.2 is recognising the form and making it when the start is given; choosing and transforming is C1 (x_inv_cond).')
N('cleft', 'See the questions for Inga', D + 'B2.2 is recognising the form and making it when the start is given; choosing and transforming is C1 (x_cleft_adv).')
N('neg_inversion', '', D + 'B2.2 is recognising the form and making it when the start is given; the full set and transformations are C1 (x_inv_neg, x_inv_main).')
