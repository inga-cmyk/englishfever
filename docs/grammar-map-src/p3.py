# Grammar map data, part 3: verb patterns, nouns and determiners, adjectives and adverbs, joining ideas, relative clauses, prepositions, B2 sentence structures.
from lib import P, AREA

AREA('Verb patterns')
P('vp_like_ing', 'Like, love, hate + -ing; want, would like + to', 'A2.1', "Follows the verbs of liking with -ing and want / would like with to: I like cooking. I want to go.",
  n='ps_form', v='would_like', e="PATTERN: *I like cook; I want go; I want going; I'd like going*", m='53, 58', t='A1: Verb + to + infinitive, verb + -ing', g='A1 verb + to-infinitive; like + to-infinitive or -ing; A2 enjoy + -ing',
  topic='verb_patterns', rx=r"\b(like|likes|love|loves|hate|hates|liked|loved)\b (\w+ing|to \w+|___)", s='The app starts the topic at A2.2')
P('vp_to', 'Verb + to: want, need, decide, hope, plan, learn, promise', 'A2.2', "Uses to + base form after these verbs, with not before to in the negative: He decided to stay. She promised not to tell.",
  n='vp_like_ing', v='vp_ing', e="PATTERN: *I want going home; He decided stay; She promised to not tell; I hope see you*", m='54', t='A2: Infinitives and gerunds', g='A2 verbs + to-infinitive (limited range); B1 increasing range',
  topic='verb_patterns', rx=r"\b(want|wants|wanted|need|needs|needed|decid\w+|hop\w+|plan\w*|learn\w*|agree\w*|promis\w+|manag\w+|refus\w+|offer\w*|expect\w*|afford|seem\w*|tend\w*|fail\w*|arrang\w+|pretend\w*|threaten\w*|would like|'d like)\b")
P('vp_ing', 'Verb + -ing: enjoy, finish, mind, avoid, keep, suggest', 'A2.2', "Uses the -ing form after these verbs: I enjoy reading. Would you mind waiting?",
  n='vp_like_ing', v='vp_to', e="PATTERN: *I enjoy to read; She finished to work; Do you mind to wait? He suggested to go*", m='53', t='A2: Infinitives and gerunds', g='A2 enjoy + -ing; B1 verb + -ing form',
  topic='verb_patterns', d=1)
P('vp_ing_subject', '-ing as the subject: Swimming is good for you', 'A2.2', "Starts a sentence with an activity: Learning a language takes time. Smoking is not allowed.",
  n='vp_ing', e="*Learn a language takes time; To smoking is not allowed; Swim is good*", m='', s='Not a Murphy EGiU unit', t='A2: Infinitives and gerunds (from memory)', g='A2 -ing forms as object; B2 -ing forms as subject',
  topic='verb_patterns', rx=r"^\W*(\w+: )?\W*\w+ing\b (\w+ )?(is|are|was|takes|makes|helps|can)\b|as the subject")
P('vp_go_ing', 'Go + -ing, go to, go for: go shopping, go for a walk', 'A2.2', "Uses the fixed patterns with go for activities: go swimming, go to the gym, go for a run, go on holiday.",
  n='vp_like_ing', e="*go to shopping; go for swimming; go to home; go on a walk*", m='', s='Not a Murphy EGiU unit', t='A2: Go', g='not found in EGP', topic='verb_patterns', rx=r"\bgo(es|ing)? (shopping|swimming|running|skiing|fishing|dancing|cycling|camping|jogging|sailing|hiking)|went (shopping|swimming|skiing|fishing|running)")
P('vp_adj_to', "Adjective + to: It's easy to …, I'm glad to …", 'B1.1', "Uses to + base form after adjectives: It's difficult to understand him. I was sorry to hear that. It's too cold to swim.",
  n='vp_to', v='too_to', e="*It's easy understand; It's difficult for understand; I'm glad seeing you*", m='65', t='A2: Infinitives and gerunds (from memory)', g='B1 it + be + adjective + infinitive; too + to-infinitive', topic='new')
P('vp_prep_ing', 'Preposition + -ing: interested in learning, before leaving', 'B1.1', "Uses -ing after every preposition: I'm good at cooking. Thank you for helping. She left without saying goodbye.",
  n='vp_ing dep_adj', v='vp_to', e="PATTERN: *interested in learn; before to leave; without say; thank you for help; instead of to talk*", m='60', t='B1: Gerund or infinitive', g='A2 preposition + -ing',
  topic='verb_patterns dep_prepositions', rx=r"\b(in|at|for|about|of|before|after|without|by|on|instead of|from|with) (\w+ing|___ \(|___\b)|preposition \+ \*?-ing")
P('vp_obj_to', 'Verb + person + to: I want you to come', 'B1.1', "Says what one person wants, asks or tells another to do: I want you to come. She asked me to help. They told us not to wait.",
  n='vp_to', v='rep_orders vp_make_let', e="PATTERN: *I want that you come; She asked me help; He told to me to wait; I'd like you coming*", m='55', t='B2: Verb + object + infinitive / gerund (first met in A2-B1: Reported speech)',
  g='B1 verbs + direct object + to-infinitive', topic='verb_patterns', rx=r"\b(want|wants|wanted|ask|asked|tell|told|expect\w*|allow\w*|teach|taught|help\w*|would like|'d like|need\w*|advis\w+|invit\w+|persuad\w+|remind\w*|encourag\w+|warn\w*) (me|you|him|her|us|them|my \w+|the \w+|\w+) (not )?to\b|want that")
P('vp_make_let', 'Make and let + person + base form', 'B1.2', "Uses the base form without to: She made me laugh. Let me help. My parents didn't let me go.",
  n='vp_obj_to', v='vp_obj_to allowed_to', e="*She made me to laugh; Let me to help; They didn't let me going*", m='55', t='B2: Verb + object + infinitive / gerund', g='B1 make, let + infinitive without to',
  topic='verb_patterns', rx=r"\b(make|makes|made|let|lets)\b (me|you|him|her|us|them|my \w+|the \w+)\b")
P('vp_both', 'Verbs with both forms and the same meaning: start, begin, continue, like', 'B1.1', "Knows that both forms are right after these verbs and that would like takes only to.",
  n='vp_to vp_ing', v='vp_meaning', e="*I like work with him* (base form); *I would like going*", m='56, 58', t='B1: Gerund or infinitive', g='A2 verbs + to-infinitive or -ing',
  topic='verb_patterns', rx=r"\b(start|starts|started|begin|begins|began|continu\w+)\b|both (forms|are)")
P('vp_meaning', 'Stop, remember, forget, try, regret + -ing or to: a different meaning', 'B1.2', "Chooses the form by meaning: I stopped smoking / I stopped to smoke. Remember to call / I remember calling. Try to sleep / Try drinking tea.",
  n='vp_both', v='vp_to vp_ing', e="*I stopped to smoke* meaning I quit; *Remember calling her* as a reminder; *I forgot locking the door* meaning I did not lock it", m='56, 57', t='B1: Gerund or infinitive; B1+: Gerund or infinitive',
  g='B2 to-infinitive or -ing form, meaning', topic='verb_patterns', rx=r"\b(stop|stops|stopped|remember|remembers|remembered|forget|forgets|forgot|forgotten|try|tries|tried|regret\w*)\b", s='Level: test-english B1, EGP B2')
P('vp_to_ing', 'To + -ing: look forward to, be used to, object to', 'B1.2', "Recognises to as a preposition: I look forward to seeing you. I'm used to driving on the left.",
  n='vp_prep_ing', v='vp_to be_used_to', e="*I look forward to see you; I'm looking forward to hear from you; I object to pay*", m='60, 62', t='B1: Gerund or infinitive (from memory)', g='not a separate EGP entry',
  topic='verb_patterns', rx=r"look(ing|s|ed)? forward")
P('vp_worth', "It's worth -ing, there's no point in -ing, it's no use -ing", 'B2.1', "Uses -ing after these expressions: It's worth trying. There's no point in waiting. I had difficulty finding it.",
  n='vp_prep_ing', e="*It's worth to try; There's no point to wait; I had difficulty to find it*", m='63', t='no line in the lists', g='not found in EGP', topic='new', s='Standard point from Murphy unit 63; no content and no list line')
P('vp_obj_ing', 'Verb + person + -ing: I can\'t imagine him doing that', 'B2.1', "Puts a new subject before -ing: Do you mind me opening the window? I remember her saying so.",
  n='vp_ing vp_obj_to', v='vp_obj_to', e="*Do you mind that I open; I can't imagine him to do that; I remember she saying*", m='53', t='B2: Verb + object + infinitive / gerund', g='B2 verb + new subject + -ing form', topic='new')
P('vp_see_do', 'See, hear, watch somebody do / doing', 'B2.1', "Uses the base form for the whole action and -ing for part of it: I saw him cross the road. I saw him crossing the road.",
  n='vp_make_let', v='vp_make_let', e="*I saw him to cross; I heard her sang; I saw him crossed*", m='67', t='B2: Verbs of the senses (from memory)', g='B2 verbs of senses + object + -ing; C1 + infinitive', topic='new')
P('vp_complex', 'Complex gerunds and infinitives: having done, to have done, being told', 'B2.2', "Uses perfect and passive forms after verbs: He denied having seen it. She seems to have left. I hate being told what to do.",
  n='vp_meaning pas_inf_ing rv_ing', v='pas_inf_ing', e="*He denied to have seen; She seems to left; He admitted have taken*", m='53, 54', t='B2: Complex gerunds and infinitives', g='C1-C2 non-finite perfect clauses and complements', topic='new')
P('vp_reduced', "Reduced infinitives: I'd love to. I didn't mean to.", 'B2.2', "Stops at to instead of repeating the verb: A: Are you coming? B: I'd like to, but I can't.",
  n='vp_to aux_uses', v='ellipsis', e="*I'd like, but I can't; I didn't mean; Yes, I want*", m='', s='Not a Murphy EGiU unit', t='B2: Reduced infinitives', g='not a separate EGP entry (B2 used to: ellipsis)', topic='new')
P('two_obj', 'Verbs with two objects: give me a present / give a present to me', 'A2.2', "Uses both orders and chooses to or for: She sent her mother a letter. He bought a gift for his mother.",
  n='obj_pron pst_irr', v='two_obj_explain', e="TWO-OBJ: *I bought a present to my sister; She gave to me a book; He sent to his mother a letter*", m='', s='Not a Murphy EGiU unit (the passive side is unit 44)', t='A2: Verbs with two objects',
  g='B1 (verbs taking two objects, in the passive)', topic='two_objects', d=1)
P('two_obj_pron', 'Give it to me: a pronoun as the thing', 'B1.1', "Puts a pronoun thing first and adds to / for: Show it to me. I'll buy them for you.",
  n='two_obj', v='two_obj', e="*Give me it; Show me them; I'll buy you it*", m='', s='Not a Murphy EGiU unit', t='A2: Verbs with two objects', g='not a separate EGP entry', topic='two_objects', rx=r"\b(it|them) (to|for) (me|you|him|her|us|them|my|the)\b|me it\b|pronoun")
P('two_obj_explain', 'Explain, describe, suggest, say: the thing first, then to + person', 'B1.1', "Never puts the person directly after these verbs: Can you explain the rules to me? He suggested a plan to us.",
  n='two_obj', v='two_obj rep_say_tell', e="TWO-OBJ: *Can you explain me the problem? She said me the truth; Describe me the man; introduce my colleague for you*", m='132', t='A2: Verbs with two objects (the exceptions)', g='not a separate EGP entry',
  topic='two_objects', rx=r"\b(explain|explained|explains|describe|described|suggest|suggested|say|said|introduce|introduced|mention|mentioned|report|announce)\w*\b")
P('do_make', 'Do or make', 'A2.2', "Uses the fixed combinations: do homework, do the dishes, do business; make a mistake, make a decision, make dinner.",
  e="*do a mistake; make homework; do a decision; make business*", m='', s='Vocabulary, not a Murphy EGiU unit', t='A2: Do vs make; B1+: Do or make', g='not in EGP (vocabulary)', topic='new')
P('get_uses', 'Get: get tired, get home, get a letter', 'A2.2', "Uses get for become (get cold), arrive (get home, get to work), receive and fetch.",
  e="*get to home; I got tired* confused with *I was tired; get in the bus*", m='', s='Vocabulary, not a Murphy EGiU unit', t='A2: Get', g='B1 get + -ed', topic='new')
P('get_b2', 'Get in grammar patterns: get married, get somebody to do, get something done', 'B2.1', "Uses get for the passive and for causing: They got married. I got him to help. Get your hair cut.",
  n='get_uses caus_have vp_obj_to', v='caus_get vp_make_let', e="*I got him help; I got him helping* for persuading; *They got marry*", m='44, 46', t='B2: Get', g='B1 get + -ed; B2 get + object + to-infinitive; C1 get + object + -ed', topic='new')
P('phr_intro', 'Phrasal verbs: get up, turn on, look for', 'A2.2', "Understands and uses the most common verb + particle combinations as single meanings.",
  e="*I stand up at seven* for *get up; put off the light; look the keys*", m='137', t='A2: Phrasal verbs', g='A2 phrasal verbs: no object; verb + pronoun + particle', topic='new')
P('phr_sep', 'Phrasal verbs and the object: turn it off, look after her', 'B1.1', "Puts a pronoun between the verb and the particle when the verb can be separated and after the preposition when it cannot: Turn it off. Look after her.",
  n='phr_intro obj_pron', e="*Turn off it; Pick up me at six; Look her after*", m='137, 138, 139, 140, 141, 142, 143, 144, 145', t='B1: Phrasal verbs 1-3', g='B1 verb + pronoun + particle; verb + particle + object', topic='new')

AREA('Nouns, articles and pronouns')
P('plural_reg', 'Regular plurals: -s, -es, -ies', 'A2.1', "Forms and spells regular plurals: books, buses, cities, days.",
  e="*two bus; citys; dayes; a books*", m='App. 6', t='A1: A / an, plurals', g='A1 plural -s; A2 -es, -ies', topic='irregular_plurals', rx=r"\b(days|boys|keys|toys|cities|buses|boxes|watches|babies|parties|countries|stories|glasses|dishes|classes|families)\b|vowel \+")
P('plural_irr', 'Irregular plurals: children, people, men, women, teeth, feet', 'A2.1', "Uses the plurals that do not add -s, with a plural verb: The children are tired.",
  n='plural_reg', v='plural_reg', e="IRR-PLURAL: *childs, childrens, peoples, tooths, foots, mouses, womans*", m='79', t='A1: A / an, plurals', g='A2 irregular plural nouns', topic='irregular_plurals', d=1)
P('plural_only', 'Always plural: jeans, glasses, scissors; the police are', 'A2.2', "Uses a plural verb and some / a pair of with these nouns: My jeans are new. The police are here.",
  n='plural_irr agr_basic', v='unc_nouns', e="IRR-PLURAL: *The police is here; a jeans; My trousers is; a scissors*", m='79', t='no line of its own (A1: A / an, plurals)', g='A2 nouns only used in the plural; B1 collective nouns',
  topic='irregular_plurals agreement', rx=r"\b(jeans|trousers|glasses|scissors|shorts|police|pyjamas|clothes)\b")
P('agr_basic', 'Subject and verb: my friend lives, my friends live', 'A2.1', "Makes the verb agree with a noun subject, also after and: My sister works. Tom and Anna live here. The shops are open.",
  n='ps_form be_pres', v='ps_form', e="3S / AGREE: *My sister work; Tom and Anna lives here; The shops is open; My parents has*", m='2, 79', t='A1: Present simple (no line of its own)', g='A1 present simple affirmative',
  topic='agreement', d=1)
P('agr_head', 'The verb agrees with the main noun: one of my friends lives …', 'B1.1', "Finds the real subject in a longer phrase: One of my friends lives in Oslo. The people in this office are nice.",
  n='agr_basic', v='agr_basic', e="AGREE / PLURAL: *One of my friends live; one of the local bank; The people in this office is; a person who prefer*", m='79, 88', t='no line in A2-B2 (returns in C1: Subject-verb agreement)',
  g='B1 superlative one of the', topic='agreement', rx=r"\bone of\b|each of|the (people|students|shops|rooms|children|price|quality|number|list) (in|of|at|on|for)\b|main noun", s='The app teaches it at A2.1-A2.2')
P('count_unc', 'Countable and uncountable: a / an, some, any', 'A2.1', "Knows which nouns can be counted and uses a / an with one, some in positive sentences, any in negatives and questions.",
  n='plural_reg a_an', v='a_an', e="*a water; an advice; I have any friends; There aren't some eggs; a money*", m='69, 71, 85', t='A1: A, some, any: countable and uncountable', g='A2 uncountable nouns; some and any',
  topic='quantity', rx=r"\b(some|any)\b", s='The app starts the topic at A2.2')
P('some_offers', 'Some in offers and requests; any = it does not matter which', 'B1.1', "Uses some in a question that offers or asks for something, and any in a positive sentence: Would you like some tea? Take any seat.",
  n='count_unc', v='count_unc', e="*Would you like any coffee?* as an offer; *Can I have any water?*", m='85', t='B1: Much, many, a lot, little, few, some, any, no', g='A2 some as subject and object; B1 quantity determiners (increasing range)',
  topic='quantity indefinite_pronouns', rx=r"would you like|can I have|could I have|offer|request|doesn't matter|any (seat|time|day|bus|colour|of them)|anyone can|anywhere you|anything you (like|want)")
P('much_many', 'Much, many, a lot of; How much? How many?', 'A2.1', "Chooses by countable or uncountable and by sentence type: How many people? Not much time. A lot of friends.",
  n='count_unc', v='count_unc', e="*How much people? many money; I have much time* (positive)", m='87', t='A1: Much, many, a lot of, a little, a few', g='A2 much, many with negative; B1 interrogative',
  topic='quantity', rx=r"\b(much|many|a lot of|lots of)\b", d=1)
P('a_few', 'A few, a little', 'A2.1', "Says 'a small number' and 'a small amount': a few friends, a little time.",
  n='much_many', v='much_many few_little', e="*a few money; a little friends; few of time*", m='87', t='A1: Much, many, a lot of, a little, a few', g='A2 quantity with plural / uncountable nouns',
  topic='quantity', rx=r"\ba (few|little)\b")
P('few_little', 'Few and little without a: almost none', 'B1.1', "Hears the negative meaning: I have few friends here (not enough) / I have a few friends (some).",
  n='a_few', v='a_few', e="*I have little friends; I have a few friends* meaning almost none", m='87', t='B1: Much, many, a lot, little, few, some, any, no', g='B2 little / few',
  topic='quantity', rx=r"(?<!\ba )\b(few|little)\b (\w+ )?(friends|people|time|money|hope|chance|information|interest|students|days)|almost none|without \*?a\*?")
P('too_enough', 'Too, too much, too many, enough', 'A2.2', "Says 'more than is good' and 'as much as is needed' and puts enough after an adjective and before a noun: too expensive, too many cars, big enough, enough chairs.",
  n='much_many adj_basic', v='so_such_basic adv_degree', e="*too much expensive; enough big; too many traffic; very expensive* meaning too expensive", m='103', t='A2: Too, too much, enough', g='A2 too with adjectives; B1 with enough; so much, too much',
  topic='quantity adverbs', rx=r"\btoo\b|\benough\b")
P('too_to', 'Too … to, … enough to', 'B1.1', "Adds what is impossible or possible: It's too cold to swim. She isn't old enough to drive. It's too heavy for me to carry.",
  n='too_enough vp_adj_to', v='so_that', e="*too cold for swim; It's too heavy that I carry; enough old to drive; too cold to swimming*", m='103', t='A2: Too, too much, enough (from memory)', g='B1 too + to-infinitive; B2 enough + to-infinitive', topic='new')
P('no_none', 'No, none, not any', 'B1.1', "Uses no before a noun, none alone or with of, and only one negative: There's no milk = There isn't any milk. None of them came.",
  n='count_unc indef_neg', v='count_unc', e="DOUBLE-NEG: *There isn't no milk; None people came; No of them; I don't have nothing*", m='86', t='B1: Any, no, none', g='A2 determiner no; B2 none of + pronoun',
  topic='quantity', rx=r"\bno\b|\bnone\b", s='On the quantity card only as a Watch out point')
P('most_of', 'Most, most of, the most', 'A2.2', "Separates most people (in general), most of the people (a known group) and the most (superlative).",
  n='much_many sup', v='sup', e="*Most of people; The most people think; most of my the friends*", m='88', t='A2: Most, most of, the most', g='A2 determiner + of + determiner', topic='new')
P('all_both', 'All, both, either, neither (+ of)', 'B1.2', "Talks about two or more things: Both films are good. Neither of them is cheap. All (of) my friends came. Either day is fine.",
  n='most_of agr_basic', v='no_none', e="AGREE: *Both of films; Neither of them are* (formal: is); *All of people; The both; Neither didn't come*", m='88, 89', t='B1: All, both; B1: Both, either, neither; B1+: All, most, both, either, neither, any, no, none',
  g='B1 both, a few as pronouns; C1 either, neither + of / with singular nouns', topic='new')
P('each_every', 'Each, every, all, whole', 'B1.2', "Uses a singular noun and verb after each and every, and separates all day from every day, all the book from the whole book.",
  n='agr_basic all_both', v='all_both', e="AGREE / NP-ORDER: *Every students have; all the day; my all section; each of student*", m='90, 91', t='B1+: All, most, both, either, neither, any, no, none (from memory)', g='B2 each as pronoun',
  topic='agreement', rx=r"\b(every|each)\b (?!one|body|thing|where)", s='On the agreement card (every + singular verb), A2 in the app')
P('another_other', 'Another, other, others, the other', 'B1.1', "Chooses by number and by whether the thing is known: another coffee, other people, the other shoe, the others.",
  n='a_the plural_reg', e="*another people; others students; the another one; other one*", m='', s='Not a Murphy EGiU unit', t='B1: Another, other, others', g='B1 another; the other', topic='new')
P('indef_form', 'Someone, anything, nobody, everywhere', 'A2.2', "Uses some- in positive sentences, any- in questions and negatives, no- with a positive verb, every- for all.",
  n='count_unc', v='count_unc', e="*I didn't see somebody; Is there someone?* (neutral question); *anybody didn't come*", m='85, 86', t='A2: Something, anything, nothing', g='A2 indefinite pronouns as subject, object',
  topic='indefinite_pronouns', d=1)
P('indef_neg', 'One negative only: I didn\'t see anybody / I saw nobody', 'A2.2', "Avoids the double negative: I don't know anything. Nobody called.",
  n='indef_form ps_negq', v='indef_form', e="DOUBLE-NEG: *I didn't see nobody; I don't know nothing; Nobody didn't call*", m='86', t='A2: Something, anything, nothing; B1+: Double negatives', g='A2 negative + anything',
  topic='indefinite_pronouns', rx=r"n't .*\b(any|no)(one|body|thing|where)\b|double negative|\b(nobody|nothing|no one|nowhere)\b")
P('indef_sing', 'Everybody is, nobody knows: singular verb, they / their', 'A2.2', "Uses a singular verb after these words and they / their to refer back: Everybody knows. Somebody left their bag.",
  n='indef_form agr_basic', v='agr_basic', e="AGREE: *Everybody are here; Everyone know him; Nobody have*", m='86, 90', t='A2: Something, anything, nothing', g='A2 indefinite pronouns as subject; B2 generic their',
  topic='indefinite_pronouns agreement', rx=r"\b(every|some|any|no)(one|body|thing)\b (is|are|was|were|has|have|knows|know|likes|like|wants|want|does|do|works|work|needs|need)\b|\b(their|they)\b|singular verb")
P('indef_adj', 'Something nice, anyone else, nothing to do', 'B1.1', "Puts the adjective, else or to + verb after the word: somewhere quiet, nothing interesting, something to drink.",
  n='indef_form', e="NP-ORDER: *I have nice something; else somebody; nothing for do*", m='', s='Not a Murphy EGiU unit', t='B1: Any, no, none (from memory)', g='A2 with adjective; with else; with to-infinitive',
  topic='indefinite_pronouns', rx=r"\b(some|any|no|every)(one|body|thing|where) (else|to \w+|nice|quiet|interesting|new|special|important|cold|hot|warm|good|wrong|cheap|different|useful|strange|funny|better|sweet)\b|adjective goes after")
P('a_an', 'A / an with a singular noun; jobs', 'A2.1', "Uses a or an by the first sound and never leaves a singular countable noun bare: a book, an hour, She is a nurse.",
  v='a_the', e="ARTICLE: *She is teacher; We have new colleague; a apple; an university*", m='71, 72', t='A1: A / an, plurals', g='A1 articles with nouns; a + adjectives', topic='articles',
  rx=r"\ban\b|\ba\b.*\b(nurse|doctor|teacher|engineer|student|driver|job)\b|vowel|sound", s='The app starts the topic at A2.2')
P('a_the', 'A or the: first mention, then known', 'A2.1', "Uses a for something new to the listener and the when both know which one: I saw a dog. The dog was huge.",
  n='a_an', v='a_an art_general', e="ARTICLE / THE: *I saw dog; Can you open a window?* for the only window; *The dog* at first mention", m='72', t='A1: A / an, the, no article', g='A1 articles with nouns', topic='articles', d=1)
P('the_unique', 'The: the sun, the same, the best, the first; play the piano', 'A2.2', "Uses the when there is only one, with superlatives and ordinals, the same, and with musical instruments.",
  n='a_the', v='art_general', e="THE: *Sun is hot today; She is best student; We live in same street; play piano*", m='72, 73', t='A1: A / an, the, no article; B1: A(n), the, no article', g='A2 the + superlatives; the + adjectives, specifying',
  topic='articles articles_b1', rx=r"\bthe (sun|moon|sky|sea|world|same|first|second|last|next|best|worst|most|biggest|tallest|only|internet|piano|guitar|violin|cinema|radio)\b|only one|superlative")
P('art_general', 'No article for things in general: Life is short. I like coffee.', 'B1.1', "Leaves out the with plural and uncountable nouns in general and uses it for a particular one: Children love games / the children in my class.",
  n='the_unique count_unc', v='a_the', e="THE: *The life is beautiful; I like the dogs* (in general); *He prefers an action instead of a talking*", m='75', t='B1: A(n), the, no article', g='A1 no article; B2 uncountable nouns: no article',
  topic='articles_b1 articles', d=1)
P('art_places', 'School or the school: places used for their purpose; meals; by bus', 'B1.1', "Leaves out the article in go to bed / school / work / hospital / prison, at home, have lunch, by car.",
  n='the_unique', v='art_general', e="THE: *I go to the bed at eleven; She is at the work; have a lunch; by the bus; go to home*", m='74', t='B1: A(n), the, no article', g='A1 preposition + no article; B1 preposition + no article',
  topic='articles_b1', rx=r"\b(bed|school|work|home|hospital|prison|university|church|college|breakfast|lunch|dinner)\b|by (car|bus|train|plane|bike)")
P('art_names', 'Names with and without the: Latvia, the Netherlands, the Daugava', 'B1.2', "Uses no article with most countries, cities, streets and lakes, and the with rivers, seas, oceans, plural names, republics and kingdoms.",
  n='the_unique', e="THE: *He lives in the Latvia; I'm learning the Spanish; Daugava is long; in United States*", m='77, 78', t='B1: A(n), the, no article', g='not a separate EGP entry',
  topic='articles_b1 articles', rx=r"\b(Latvia|Spain|France|Italy|Germany|Riga|London|Paris|Europe|Asia|Africa|Netherlands|United (States|Kingdom)|USA|UK|Alps|Daugava|Baltic|Atlantic|Pacific|Thames|Nile|Lake|Mount|Street|Spanish|English|French|German|Latvian)\b")
P('the_adj', 'The + adjective: the rich, the elderly, the unemployed', 'B1.2', "Talks about a group of people with the + adjective and a plural verb: The elderly need more care.",
  n='art_general', v='art_general', e="AGREE: *The elderly needs; the riches; the poors; riches have*", m='76', t='B1+: Adjectives without a noun', g='B2 (not a separate EGP entry)',
  topic='articles_b1', rx=r"\bthe (rich|poor|elderly|young|old|unemployed|homeless|sick|blind|deaf|disabled|injured|dead|French|British|Dutch|English)\b (\w+ ){0,2}(are|need|have|were|do|live|often|should|pay)")
P('poss_adj', 'My, your, his, her, its, our, their; I, you, he, she', 'A2.1', "Uses the subject pronoun before the verb and the possessive word before the noun: She is my sister. Their car is new.",
  n='be_pres', v='obj_pron', e="*He is me brother; she book; they car; it's colour* for *its*; *your* / *you're*", m='', s='Not a Murphy EGiU unit', t='A1: Possessive adjectives and subject pronouns', g='A1 possessive determiners with nouns; subject pronouns', topic='new')
P('obj_pron', 'Object pronouns: me, him, her, us, them', 'A2.1', "Uses the object form after a verb or a preposition: Call me. I know them. This is for her.",
  n='poss_adj', v='poss_adj', e="*I know they; Call I; for she; I like he*", m='', s='Not a Murphy EGiU unit', t='A1: Object pronouns', g='A1 object pronouns', topic='new')
P('poss_s', "Possessive 's and Whose …?", 'A2.1', "Shows who something belongs to: my sister's name, my parents' house; Whose bag is this?",
  n='poss_adj plural_reg', v='poss_adj', e="POSSESSIVE: *My new colleague name is Marta; the name of my sister; Who's bag is this?; my parent's house* for two parents", m='81', t="A1: Whose, possessive 's",
  g="A2 singular noun + 's; B1 irregular plural + 's; B2 plural noun + s'", topic='new')
P('poss_pron', 'Mine, yours, hers, ours, theirs; a friend of mine', 'A2.2', "Uses the possessive pronoun without a noun: This is mine. Is that yours? She's a friend of mine.",
  n='poss_adj', v='poss_adj', e="*This is my; It's the mine; a friend of me; hers book; your's*", m='83', t='A2: Pronouns and possessives', g='A2 mine, yours; + of mine', topic='new')
P('reflexive', 'Myself, yourself, themselves; by myself', 'B1.1', "Uses a reflexive pronoun when the subject and the object are the same, and by myself for alone: I cut myself. She lives by herself.",
  n='obj_pron', v='obj_pron reciprocal', e="*I cut me; He hurt hisself; They enjoyed theirselves; I feel myself good; We met ourselves at six* for each other", m='82, 83', t='B1: Reflexive pronouns',
  g='A2 same subject and object; B1 by + singular; after prepositions; for emphasis', topic='new')
P('reciprocal', 'Each other, one another; reflexive for emphasis; verbs without myself', 'B2.1', "Separates themselves from each other, adds emphasis (I did it myself) and leaves out the pronoun after feel, relax, concentrate, meet.",
  n='reflexive', v='reflexive', e="*They looked at themselves* for each other; *I feel myself tired; Relax yourself; We know us for years*", m='82', t='B2: Reflexive and reciprocal pronouns', g='B1 each other; B2 one another; reflexive plural, for emphasis', topic='new')
P('generic_pron', 'Generic pronouns: you, one, we, they', 'B2.1', "Talks about people in general: You never know. One should be careful. They say it will snow.",
  n='poss_adj', e="*One never know; You never knows; It says that* for *They say*", m='', s='Not a Murphy EGiU unit', t='B2: Generic pronouns', g='A2 you, general; B1 one, general, formal; B2 we, us; gender-neutral they', topic='new')
P('unc_nouns', 'Uncountable in English: advice, information, furniture, news, luggage', 'A2.2', "Uses these nouns with no plural, no a / an and a singular verb: some advice, a piece of furniture, The news is good.",
  n='count_unc agr_basic', v='plural_only', e="UNCOUNT: *The news are good; Your advices; an information; My hairs; furnitures; a luggage*", m='69, 70', t='A2: Much, many, little, few, some, any (no line of its own)',
  g='A2 uncountable nouns; with determiners, quantity; containers, quantity expressions', topic='quantity irregular_plurals agreement', rx=r"\b(advice|advices|information|informations|furniture|news|luggage|hair|homework|money|weather|traffic|bread|equipment|knowledge|progress|research)\b")
P('compound_nouns', "Noun + noun, 's or of: a bus driver, my sister's car, the end of the film", 'B2.1', "Chooses the right way to join two nouns: noun + noun for a kind of thing, 's for people, of for things.",
  n='poss_s', v='poss_s', e="*a driver of bus; the film's end; a car's door; my sister car; a ten-years-old boy*", m='80, 81', t='B2: Compound nouns and possessives', g="B1 noun + of + possessive; B2 of + noun phrase 's", topic='new')
P('poss_time', "'s with time and distance: two hours' walk, yesterday's news", 'B2.1', "Uses the possessive with time expressions: a week's holiday, in three days' time, today's paper.",
  n='poss_s', v='compound_adj_num', e="*two hours walk; a two hour's walk; yesterday news; three day's time*", m='81', t="B2: Possessive 's with time (two hours' walk)", g="B2 plural noun + s'", topic='new')

AREA('Adjectives, adverbs and comparison')
P('adj_basic', 'Adjectives: before the noun, after be, no plural', 'A2.1', "Puts the adjective before the noun or after be and never adds -s to it: a big house, The houses are big.",
  n='be_pres', e="*a house big; two smalls boxes; the news interesting; She is a girl tall*", m='99', t='A1: Adjectives', g='A1 attributive, predicative with be', topic='adj_order', rx=r"\bsmalls\b|no plural|bigs\b|olds\b|news\b", s='On the adj_order card as one form line')
P('adj_adv', 'Adjective or adverb: quick / quickly, good / well', 'A2.1', "Uses an adjective for a noun and an adverb for a verb, with -ly spelling and the irregular well: a careful driver, She drives carefully.",
  n='adj_basic ps_form', v='link_adj', e="*She speaks English very good; He drives careful; She sings beautiful; easyly, happyly*", m='100', t='A1: Adverbs of manner or adjectives', g='A2 adverbs of manner, end position',
  topic='adverbs', d=1, s='The app starts the topic at A2.2')
P('adv_irreg', 'Fast, hard, late; hardly, lately', 'B1.1', "Uses fast, hard and late without -ly and knows that hardly means almost not and lately means recently.",
  n='adj_adv', v='adj_adv', e="*He drives fastly; She works hardly* meaning a lot; *I arrived lately*", m='101', t='no line of its own (A1: Adverbs of manner or adjectives)', g='not a separate EGP entry',
  topic='adverbs', rx=r"\b(fast|hard|late|hardly|lately|fastly)\b")
P('adv_freq', 'Always, usually, often, sometimes, never: where they go', 'A2.1', "Puts the frequency word before the main verb and after be: She often walks. He is always late.",
  n='ps_form be_pres', v='adv_position', e="ADV-PLACE: *I go always by bus; She always is late; He never doesn't come; Always I get up at seven*", m='110', t='A1: Adverbs of frequency', g='A1 frequency, mid position',
  topic='adverbs', rx=r"\b(always|usually|often|sometimes|never|rarely|seldom|hardly ever|once a|twice a|every day)\b")
P('adv_degree', 'Very, really, quite, too + adjective; I like it very much', 'A2.2', "Makes an adjective stronger or weaker and puts very much at the end: quite cold, really good, I like it very much.",
  n='adj_basic', v='too_enough adv_extreme', e="*I very like it; I like very much it; too much cold; very much good*", m='104', t='no line of its own (A1: Adjectives; A2: Too, too much, enough)', g='A1 very; A2 degree adverbs',
  topic='adverbs', rx=r"\b(very|really|quite|extremely|so)\b (?!amazing|perfect|exhausted|delicious|terrible|awful|fantastic|freezing|huge|tiny|brilliant)\w+|very much")
P('adv_extreme', 'Absolutely amazing, very good: strong and normal adjectives', 'B1.2', "Uses absolutely / completely with strong adjectives and very / extremely with normal ones: absolutely exhausted, very tired.",
  n='adv_degree', v='adv_degree quite_rather', e="*very amazing; absolutely good; very exhausted; completely tired*", m='', s='Not a Murphy EGiU unit', t='B1+: Pretty, rather, quite, fairly (from memory)', g='C1 with extreme adverbs',
  topic='adverbs', rx=r"\b(absolutely|completely|totally|utterly)\b|strong adjective|\bvery (amazing|perfect|exhausted|delicious|terrible|awful|fantastic|freezing|huge|tiny|brilliant)")
P('quite_rather', 'Quite, pretty, rather, fairly', 'B1.2', "Grades an opinion and places the word: quite a good film, a rather long day, pretty tired; quite right = completely.",
  n='adv_degree a_an', v='adv_degree so_such_basic', e="*a quite good film; rather a bit; a pretty much; quite a tired*", m='104', t='B1+: Pretty, rather, quite, fairly', g='B1 quite a; B2 rather a', topic='new')
P('link_adj', 'Look, sound, feel, seem, taste + adjective', 'B1.1', "Uses an adjective, not an adverb, after these verbs: That sounds good. You look tired. I feel well / good.",
  n='adj_adv', v='adj_adv senses_like', e="*That sounds well; You look tiredly; It smells badly; She seems happily*", m='99, 101', t='B1+: Verbs of the senses', g='A2 linking verbs + adjective',
  topic='adverbs', rx=r"\b(look|looks|looked|sound|sounds|sounded|feel|feels|felt|seem|seems|seemed|taste|tastes|tasted|smell|smells|smelled)\b")
P('senses_like', 'Look like + noun, look as if + clause', 'B1.2', "Separates the three patterns: You look tired. You look like your father. It looks as if it's going to rain.",
  n='link_adj', v='link_adj like_as', e="*You look like tired; It looks like to rain; She looks as her mother; It sounds as a good idea*", m='118', t='B1+: Verbs of the senses; B2: Verbs of the senses',
  g='B1 sense verbs + as if / as though; linking verb + like; B2 as if / as though + finite clause', topic='new')
P('adv_position', 'Position of adverbs: verb + object, place before time, mid-position', 'B1.2', "Keeps the verb and its object together and puts place before time: I like coffee very much. We went to Rome last year. I've already seen it. She probably won't come.",
  n='adv_freq pp_just', v='adv_freq', e="ADV-PLACE: *I like very much coffee; We went last year to Rome; I have seen already it; She won't probably come*", m='109, 110', t='B1+: Position of adverbs; A1: Basic word order',
  g='A2 adverbs: mid position, end position (manner, degree)', topic='adverbs', rx=r"put the words in order|position|goes after the (verb|object)|after the object")
P('eding', 'Bored or boring: -ed and -ing adjectives', 'B1.1', "Uses -ed for how a person feels and -ing for the thing or person that causes it: I'm bored. The film is boring.",
  n='adj_basic', e="ED-ING: *I am boring* (= I feel bored); *The lesson was very interested; It was a tired day; I'm very interesting in history*", m='98', t='B1: -ed / -ing adjectives; B1+: -ed / -ing adjectives',
  g='not a separate EGP entry (C1 past participle as adjective)', topic='adj_ed_ing', d=1, s='The app starts at A2.2; the list has it at B1')
P('adj_order', 'Adjective order: a lovely old house, a big red car', 'B1.2', "Puts opinion before fact and facts in the usual order (size, age, shape, colour, origin, material), with at most two or three adjectives.",
  n='adj_basic', e="NP-ORDER: *an old lovely house; a red big car; a wooden nice new table*", m='99', t='B1+: Adjective order', g='B1 combining adjectives before the noun; B2 complex noun phrases with adjectives',
  topic='adj_order', d=1, s='The app starts at B1.1')
P('compound_adj_num', 'Compound adjectives with numbers: a five-star hotel, a ten-minute walk', 'B1.2', "Joins number and noun with a hyphen and keeps the noun singular: a two-hour film, a 20-year-old student.",
  n='adj_basic plural_reg', v='poss_time', e="*a five-stars hotel; a ten minutes walk; a 20-years-old student; a two hours film*", m='80', t='B1: Compound adjectives with numbers', g='B1 compound adjectives', topic='new')
P('compound_adj', 'Compound adjectives: well-known, good-looking, part-time', 'B2.1', "Forms and understands adjectives made of two words: a well-paid job, a hard-working student, a last-minute change.",
  n='compound_adj_num eding', e="*a good-looked man; a hard-worked student; a well-pay job*", m='', s='Not a Murphy EGiU unit', t='B2: Compound adjectives', g='B2 compound adjectives (increasing range); C1 wide range', topic='new')
P('cmp_er', 'Comparatives: -er, more … than; better, worse', 'A2.1', "Compares two things with the right form and spelling: bigger, easier, more expensive than, better, worse, further.",
  n='adj_basic', v='sup cmp_as', e="COMPARE: *more tall; more bigger; more better; older that me; gooder; expensiver*", m='105', t='A1: Comparative adjectives', g='A2 comparatives: -er, with more, irregular, with than',
  topic='comparison', d=1)
P('sup', 'Superlatives: the -est, the most …; the best, the worst', 'A2.1', "Compares one with all the others and adds in / of: the tallest in the class, the most expensive, the best.",
  n='cmp_er', v='cmp_er', e="COMPARE: *the most good; the most tallest; the tallest of the class; she is tallest; the more expensive of all*", m='108', t='A1: Superlative adjectives', g='A2 superlatives: with -est, the most, with in / of + noun',
  topic='comparison', rx=r"\bthe (most|least|best|worst|\w+est)\b|superlative")
P('cmp_as', 'As … as, not as … as; the same as, different from', 'A2.2', "Says that two things are equal or not: as fast as, not as heavy as, the same as mine, different from yours.",
  n='cmp_er', v='cmp_er', e="COMPARE: *as fast than; the same age like; not so heavy than; the same that; different than* (US) / *different of*", m='107', t='A2: Comparative and superlative adjectives and adverbs',
  g='B1 as … as; the same (+ noun) + as', topic='comparison', rx=r"\bas \w+ as\b|as ___ as|not as\b|the same|different from|\bas\b.*\bas\b")
P('cmp_adv', 'Comparing adverbs: more slowly, faster, better, the most carefully', 'A2.2', "Compares how things are done: She drives more carefully than me. He runs faster. Who works the hardest?",
  n='cmp_er adj_adv', v='cmp_er', e="*more fast; more quicklier; he speaks English gooder; more well*", m='105', t='A2: Comparative and superlative adjectives and adverbs', g='B1 (comparative clauses with adverbs)',
  topic='comparison', rx=r"more (\w+ly)\b|\b(faster|harder|earlier|later)\b.*\b(runs|run|works|work|drives|drive|arrive|arrived|gets up|speak|speaks|sing|sings|play|plays|type|types)\b|adverb")
P('cmp_less', 'Less … than, the least; than me / than I am', 'B1.1', "Compares downwards and finishes the comparison naturally: less expensive than, the least interesting; She's taller than me / than I am.",
  n='cmp_as sup', v='cmp_as', e="*lesser expensive; the less interesting of all; taller than I* (very formal); *less cheaper*", m='105, 107', t='B1: Comparative and superlative adjectives and adverbs', g='B1 comparative clauses: finite after than',
  topic='comparison', rx=r"\bless\b|\bleast\b|than (me|him|her|us|them)\b|than I (am|do|did|was)")
P('cmp_modify', 'How big is the difference: much, a lot, far, a bit, slightly + comparative', 'B1.2', "Strengthens or softens a comparison: much cheaper, a lot more expensive, a bit colder, slightly better; never very + comparative.",
  n='cmp_er', v='adv_degree', e="COMPARE: *very cheaper; more cheaper; much more cheap; a lot of better*", m='106', t='B2: Modifying comparatives', g='B1 with (so) much, with a (little) bit, with even; B2 with slightly, with a lot',
  topic='comparison', rx=r"\b(much|a lot|far|a bit|a little|slightly|even|way) (more|less|\w+er|better|worse)\b|how big the difference", s='Level: taught by the app from B1 (EGP B1); the list names it at B2')
P('cmp_modify_b2', 'By far the best, nowhere near as … as, twice as … as, not nearly as', 'B2.1', "Modifies superlatives and as … as: by far the biggest, easily the best, nearly as good as, three times as expensive as.",
  n='cmp_modify cmp_as sup', v='cmp_modify', e="*by far better; twice more expensive than; not near as good; three times so expensive*", m='106, 107', t='B2: Modifying comparatives', g='B2 superlatives with by far', topic='new')
P('cmp_double', 'The sooner, the better; more and more', 'B1.2', "Shows that two things change together, or that something keeps changing: The more you practise, the easier it gets. It's getting colder and colder.",
  n='cmp_er pc_temp', v='cmp_er', e="*More you practise, easier it gets; The more you practise, it gets easier; more and more cold; the more sooner*", m='106', t='B1+: The … the … comparatives',
  g='B1 combining comparative adjectives with and; B2 the more … the more …', topic='comparison', rx=r"\bthe (more|less|sooner|\w+er|better|worse)\b.{2,40}\bthe (more|less|better|worse|\w+er)\b|(\w+er|more) and (\w+er|more)\b")
P('so_such_basic', 'So + adjective, such (a) + noun', 'B1.1', "Makes a description stronger with the right word: so long, so quickly; such a long film, such nice people, such bad weather.",
  n='adj_basic a_an count_unc', v='adv_degree too_enough', e="*so a long film; such long; such a nice people; a such good idea; so nice people*", m='102', t='B1: So, such, so much, so many', g="B1 such (a) + adjective + noun",
  topic='so_such', d=1)
P('so_much_many', 'So much, so many', 'B1.1', "Uses so much with uncountable and so many with plural nouns: so much noise, so many people.",
  n='so_such_basic much_many', v='much_many too_enough', e="*so much people; so many traffic; such many people; so much of noise*", m='102', t='B1: So, such, so much, so many', g='A2 so many with plural nouns; B1 so much, too much with uncountable nouns',
  topic='so_such', rx=r"so (much|many)|such (much|many)")
P('so_that', 'So … that, such … that: the result', 'B1.2', "Adds the result of a strong quality: It was so cold that we stayed inside. It was such a cold day that we stayed inside.",
  n='so_such_basic', v='too_to', e="*It was too cold that we stayed inside; so cold as we stayed; such cold that*", m='102', t='B1+: So, such', g='B1 so + adjective + that clause; subordinated clauses: purpose, result',
  topic='so_such', rx=r"\bthat (I|we|he|she|they|it|you|nobody|everyone|the|my|no one)\b|result|join|one sentence", s='The app has these tasks from B1.1')

AREA('Joining ideas')
P('word_order', 'Basic word order: subject, verb, object, place, time', 'A2.1', "Builds a statement in the fixed English order: I play tennis in the park on Sundays.",
  n='ps_form', v='adv_position', e="ADV-PLACE: *In my town is a park; I like very much tennis; Plays he tennis; Yesterday went I to work*", m='109', t='A1: Basic word order', g='A1 declarative clauses; adverbs: time, place, end position', topic='new')
P('conj_and_but', 'And, but, or', 'A2.1', "Joins words and sentences that add, contrast or give a choice; uses or after a negative: I don't eat meat or fish.",
  n='ps_form', v='conj_so_bec', e="*I don't eat meat and fish; I like tea but coffee; and too I like*", m='', s='Not a Murphy EGiU unit', t='A1: And, but, or, so, because', g='A1 coordinating: word + word, clause + clause; but, concessive',
  topic='conj_basic', d=1)
P('conj_so_bec', 'So or because: result or reason', 'A2.1', "Gives the result with so and the reason with because: It was late, so we left. We left because it was late.",
  n='conj_and_but', v='conj_and_but reason_b1', e="*I went home so the shop was closed; Because it was late, so we left; We left, because it was late*", m='', s='Not a Murphy EGiU unit', t='A1: And, but, or, so, because',
  g='A1 because, reasons; A2 so', topic='conj_basic', rx=r"\bso\b|\bbecause\b")
P('conj_parallel', 'The same kind of words on both sides: cooking and reading', 'A2.2', "Keeps the forms equal after and / or and leaves out the repeated subject: She got up and left. I like cooking and reading.",
  n='conj_and_but vp_ing', e="*I like cooking and read; She got up and she leaving; to walk or taking the bus*", m='', s='Not a Murphy EGiU unit', t='A2: However, although, because, so, time connectors (no line of its own)',
  g='A1 clause + clause, ellipted subject; B1 combining clauses of the same type', topic='conj_basic', rx=r"\w+ing (and|or) \w+|same kind|subject again|and (left|went|sat|took|closed|opened)\b")
P('link_however', 'However, although, but', 'A2.2', "Contrasts two ideas in one sentence (although, but) or in two (However, …) with the right punctuation.",
  n='conj_and_but', v='contrast_b1', e="CONTRAST: *Although, it was late, we stayed; Although it was late, but we stayed; I'd love a dog, however my flat is small*", m='113', t='A2: However, although, because, so, time connectors',
  g='A2 subordinating conjunctions, simple; B1 discourse markers: contrasting', topic='conj_linkers', d=1)
P('link_time', 'Time connectors: then, after that, before, after, while, when', 'A2.2', "Orders the events of a story and puts a comma after a time clause that comes first: Before I go to bed, I read. Then I made breakfast.",
  n='conj_and_but pst_reg', v='fut_time_clause', e="*I had a shower. After, I made breakfast; After I made breakfast; Before go to bed, I read*", m='', s='Not a Murphy EGiU unit', t='A2: However, although, because, so, time connectors',
  g='A2 subordinated clauses: time; B1 discourse markers: sequencing', topic='conj_linkers', rx=r"\b(then|after that|afterwards|before|after|while|when|first|finally|next|as soon as)\b")
P('purpose_to', 'Purpose: to + verb, for + noun', 'A2.2', "Says why somebody does something: I went to the bank to get some money. We stopped for a coffee.",
  n='vp_to', v='purpose_so_that', e="*I went to the bank for get some money; for to get; for getting money* (purpose of an action)", m='64', t='A2: Purpose with to and for', g='A2 subordinated clauses: purpose',
  topic='conj_clauses', rx=r"\bto (get|buy|see|learn|ask|meet|help|pay|find|make|take|catch|save|study|improve|check|pick|tell|visit|book|talk|speak|keep|have|send|do|be)\b|\bfor (a|an|some|the|my) \w+|purpose", s='The app has it at B1.1 and above')
P('because_of', 'Because or because of; due to + noun', 'B1.1', "Uses because before a clause and because of / due to before a noun: because it snowed / because of the snow.",
  n='conj_so_bec', v='conj_so_bec contrast_b1', e="CONTRAST: *The flight was late because the snow; because of it snowed; He was late because the traffic*", m='113', t='B1: Clauses of contrast, purpose and reason',
  g='B1 subordinated clauses: reason', topic='conj_linkers conj_clauses', rx=r"because of|due to|\bbecause\b")
P('contrast_b1', 'Although, even though + clause; despite, in spite of + noun / -ing', 'B1.1', "Chooses the word by what follows: Although it was raining, we went out. Despite the rain / Despite feeling ill, …",
  n='link_however vp_prep_ing', v='link_however because_of', e="CONTRAST: *Despite it was raining; Despite of the rain; even she has a lot to do; In spite the rain; Although the rain*", m='113', t='B1: Clauses of contrast, purpose and reason; B1+: Clauses of contrast and purpose',
  g='B1 subordinated clauses: contrast; B2 complex subordinating conjunctions (despite)', topic='conj_clauses', d=1)
P('purpose_so_that', 'So that + can / could / would', 'B1.2', "Gives a purpose with its own subject: I wrote it down so that I wouldn't forget. Speak slowly so that everyone can understand.",
  n='purpose_to can will_form', v='purpose_to so_that', e="*so that I don't forgot; for that everyone understands; so everyone to understand; so that to understand*", m='64', t='B1: Clauses of contrast, purpose and reason; B1+: Clauses of contrast and purpose',
  g='B1 subordinated clauses: purpose, result', topic='conj_clauses', rx=r"so that")
P('reason_b1', 'As and since for a reason', 'B1.2', "Gives a reason the listener already knows: As it was late, we took a taxi. Since you're here, let's start.",
  n='conj_so_bec', v='because_of pp_for_since', e="*As it was late, so we took a taxi; Since it was late, that we took*", m='116', t='B1: Clauses of contrast, purpose and reason', g='B1 subordinated clauses: reason',
  topic='conj_clauses', rx=r"\b(as|since)\b (it|he|she|we|they|you|I|the|there|my)\b")
P('during_while', 'During, for, while', 'B1.1', "Uses during + noun (when), for + a period (how long), while + clause: during the film, for two hours, while we were watching.",
  n='pastc_when pp_for_since', v='pp_for_since by_until', e="*During I was cooking; during two hours; while the film; for the film I fell asleep*", m='119', t='B1: During, for, while', g='B1 subordinating conjunctions, simple',
  topic='time_clauses', rx=r"\bduring\b|\bwhile\b")
P('by_until', 'By or until; by the time', 'B1.1', "Uses until for something that continues up to a moment and by for something that happens not later than it: Stay until five. Finish it by five.",
  n='fut_time_clause', v='during_while', e="*Finish it until five; Wait here since I come back; I'll be home until six* meaning not later", m='120', t='no line of its own (B1: During, for, while)', g='C1 present simple with by the time',
  topic='time_clauses', rx=r"\bby (five|six|seven|eight|nine|ten|noon|midnight|friday|monday|tomorrow|the end|then|next|\d)|\bby\b.*\buntil\b|\buntil\b.*\bby\b|not later than|up to a moment")
P('for_since_from', 'For, since, from … to', 'B1.1', "Uses for + a length of time, since + a starting point up to now, from … to for a finished period: from 2010 to 2014.",
  n='pp_for_since', v='pp_for_since during_while', e="DURATION: *I've lived here from 2015; since three years; for 2015; I worked there since 2010 to 2014*", m='12', t='B1: For, since, from', g='A2 for; B1 since', topic='new', s='Overlaps the present perfect points; listed because the list has it as a lesson')
P('on_time', 'On time / in time, at the end / in the end', 'A2.2', "Separates punctual (on time) from early enough (in time), and the last part (at the end of) from finally (in the end).",
  n='prep_time', e="*in the end of the film; at the end we decided; I arrived on time to catch* for *in time*", m='122', t='A2: On time / in time, at the end / in the end', g='not found in EGP', topic='new')
P('in_case', 'In case', 'B2.1', "Takes a precaution: I'll take some cash in case the card machine isn't working; separates it from if.",
  n='c1 fut_time_clause', v='c1 c_alt', e="TIME-CLAUSE: *in case it will rain; in case of it rains; I'll take an umbrella if it rains* (= only then)", m='114', t='B2: Clauses of contrast, purpose, reason and result', g='B2 complex subordinating conjunctions',
  topic='conj_b2', rx=r"in case")
P('contrast_b2', 'Whereas, while, nevertheless, yet, even so', 'B2.1', "Compares two facts (whereas, while) and concedes a point between sentences (Nevertheless, …).",
  n='contrast_b1', v='contrast_b1', e="*Whereas it was late, we stayed* for although; *It was late, nevertheless we stayed* (punctuation); *Despite, we stayed*", m='113', t='B2: Clauses of contrast, purpose, reason and result',
  g='B2 discourse markers: comparing; C1 yet, concessive', topic='conj_b2', d=1)
P('purpose_b2', 'In order to, so as not to, in order for … to, for + -ing', 'B2.1', "Gives a purpose formally, in the negative and with a new subject: so as not to wake her; in order for the plan to work; a tool for cutting metal.",
  n='purpose_so_that vp_prep_ing', v='purpose_so_that purpose_to', e="*for not to wake her; in order to not; This tool is for cut metal; in order that the plan to work*", m='64', t='B2: Clauses of contrast, purpose, reason and result',
  g='B2 complex subordinating conjunctions (in order that)', topic='conj_b2 conj_clauses', rx=r"in order|so as|\bfor \w+ing\b")
P('reason_result_b2', 'Owing to, on account of; therefore, consequently, as a result', 'B2.2', "Gives reasons and results in formal writing with the right structure and punctuation.",
  n='because_of contrast_b2', v='because_of', e="*owing the fog; due to it was foggy; Sales fell, therefore we closed* (comma splice); *as a result of we closed*", m='', s='Not a Murphy EGiU unit', t='B2: Clauses of contrast, purpose, reason and result; B2: Discourse markers',
  g='B2 discourse markers: summarising, formal', topic='conj_b2', rx=r"owing to|on account of|therefore|consequently|as a result|thus|hence")
P('like_as', 'Like or as', 'B2.1', "Uses like + noun for similarity and as + noun for a role, as + clause: She works as a teacher. She sings like a professional. Do as I say.",
  n='senses_like', v='senses_like cmp_as', e="*She works like a teacher* (that is her job); *as my brother, I love football; Do like I say* (informal)", m='117', t='no line in the lists', g='A2 be like + noun; B1 linking verb + like', topic='new', s='Standard point from Murphy unit 117; no list line')
P('discourse', 'Discourse markers: in fact, on the other hand, as far as I know, anyway', 'B2.2', "Organises speech and writing: adding, contrasting, giving an opinion, changing the subject.",
  n='contrast_b2', e="*In the other hand; According to me; At the end* for finally; *As far I know*", m='', s='Not a Murphy EGiU unit', t='B2: Discourse markers', g='B1 organising: adding, contrasting, sequencing; B2 summarising, formal', topic='new')

AREA('Relative clauses')
P('rel_subj', 'Defining relative clauses: who, which, that as the subject', 'A2.2', "Says which person or thing is meant: the woman who lives next door, a phone that takes good photos.",
  n='ps_form pst_reg', v='rel_obj', e="REL-WHICH: *the woman which lives; the book what I bought; the man who he called; the people who lives*", m='92', t='A2: Defining relative clauses', g='A2 defining, subject, with who / which',
  topic='relative_clauses', d=1, s='Level: test-english A2, EGP A2; the app has the topic at B1.1-B1.2. See the questions for Inga')
P('rel_obj', 'Who, which, that as the object; leaving the word out', 'B1.1', "Leaves out the relative word when it is the object and never repeats the object: the film (that) we saw.",
  n='rel_subj', v='rel_subj', e="*The book that I bought it is great; the man who I met him; the film what we saw*", m='93', t='B1: Defining and non-defining relative clauses', g='A2 defining, object, with that; defining, without pronoun',
  topic='relative_clauses', rx=r"left out|leave out|without (who|which|that)|\b(I|we|you|they|he|she) (bought|saw|met|read|made|wrote|told|gave|found|like|liked|need|want|recommended|ordered|borrowed|lost|watched|chose|sent) it\b|object")
P('rel_where_whose', 'Where, whose, when', 'B1.1', "Adds a place, an owner or a time: the restaurant where we met, a driver whose car was stolen, the day when we met.",
  n='rel_subj poss_s', v='rel_subj', e="*the man who's car was stolen; the restaurant which we met; the man that his car; the city where I was born in*", m='94', t='B1: Defining and non-defining relative clauses',
  g='B1 with where, place; with whose name; B2 defining with whose', topic='relative_clauses', rx=r"\b(where|whose|who's|when)\b")
P('rel_what', 'What = the thing that', 'B1.2', "Uses what without a noun before it and that / which after a noun: I didn't hear what he said. Everything that he said was true.",
  n='rel_obj', v='rel_obj whoever', e="REL-WHICH: *The book what I bought; Everything what he said; I didn't hear that he said*", m='93', t='no line of its own (B1: Defining and non-defining relative clauses)', g='not a separate EGP entry',
  topic='relative_clauses', rx=r"\bwhat\b")
P('rel_nondef', 'Non-defining relative clauses: commas, who / which, never that', 'B1.2', "Adds extra information between commas: My brother, who lives in Berlin, is a nurse.",
  n='rel_obj rel_where_whose', v='rel_subj', e="REL-WHICH: *My brother, that lives in Berlin; My brother who lives in Berlin, is a nurse* (one comma); *a presentation, that made*", m='95', t='B1: Defining and non-defining relative clauses',
  g='A2 non-defining, subject, with who / which; B1 non-defining, object, with who', topic='relative_clauses', rx=r",\s*(who|which|whose|where)\b|, that\b|comma|extra information|non-defining")
P('rel_which_all', ', which = the whole idea before it', 'B2.1', "Comments on a whole sentence: He didn't call, which was strange.",
  n='rel_nondef', v='rel_what', e="REL-WHICH: *He didn't call, what was strange; She worked in a hospital, what means; …, that was strange*", m='96', t='B2: Defining and non-defining relative clauses', g='B2 sentence relative, evaluative',
  topic='relative_clauses', rx=r", which (was|is|means|meant|made|makes|surprised|annoyed|explains|shows|proved)\b|whole (sentence|idea)", s='On the relative_clauses card only as a Watch out point')
P('rel_prep', 'Prepositions in relative clauses: the man I was talking to / to whom', 'B2.1', "Puts the preposition at the end in everyday English and before whom / which in formal English.",
  n='rel_obj q_prep_end', v='q_prep_end', e="REL-ORDER: *the man who about I was telling you; the house I live; the man to who I spoke; the hotel which we stayed*", m='93, 96', t='B2: Defining and non-defining relative clauses',
  g='A2-B1 preposition stranding; B2 pronoun + preposition; preposition + wh- word', topic='relative_clauses', rx=r"\b(in|to|about|with|for|at|on|of|from)\b[.?!]?$|\b(to|with|for|about|in|from|of) (whom|which)\b|live in\b|preposition", s='On the relative_clauses card only as a Watch out point')
P('rel_quant', 'All of whom, most of which, neither of whom', 'B2.2', "Adds a quantity to a non-defining clause: She has three brothers, all of whom live abroad.",
  n='rel_nondef rel_prep all_both', e="*all of them live abroad* (joined with a comma); *all of who; most of that*", m='96', t='B2: Defining and non-defining relative clauses (from memory)', g='C1 quantity pronouns with relative pronouns', topic='new')
P('part_reduced', '-ing and -ed clauses after a noun: the woman talking to Tom, the boy injured in the accident', 'B2.1', "Shortens a relative clause with a participle: active → -ing, passive → third form.",
  n='rel_subj pas_past pc_form', v='rel_subj eding', e="*the woman talked to Tom; the boy injuring in the accident; the people who waiting*", m='97', t='B2: Participle clauses', g='B1-B2 subordinated: non-finite with -ing; C1 non-finite with -ed clauses', topic='new')
P('part_adv', 'Participle clauses for time and reason: Feeling tired, I went to bed. Having finished, …', 'B2.2', "Replaces a clause with when / because / after by a participle, with the same subject in both parts.",
  n='part_reduced vp_complex', v='part_reduced', e="*Walking down the street, a car hit me* (different subjects); *Having finish; Being tired, so I went to bed*", m='68', t='B2: Participle clauses',
  g='B2 -ing clause; C1 not + -ing clause; C1 non-finite -ed clauses, focus', topic='new', s='Level: test-english B2 and again C1 (Advanced participle clauses)')

AREA('Prepositions')
P('prep_time', 'At, in, on: time', 'A2.1', "Uses at with clock times, on with days and dates, in with months, years, seasons and parts of the day; at night, at the weekend.",
  e="PREP-TIME: *in Monday; on 2020; at the morning; in night; on May*", m='121', t='A1: At, in, on: time', g='A1 simple prepositions', topic='prep_time_place', d=1)
P('prep_none', 'No preposition: next Monday, last year, tomorrow, every day', 'A2.2', "Leaves out the preposition before next / last / this / every and tomorrow / yesterday.",
  n='prep_time', v='prep_time', e="*on next Monday; in last year; at this weekend; in every day; on tomorrow*", m='121', t='A1: At, in, on: time', g='not a separate EGP entry',
  topic='prep_time_place', rx=r"\b(next|last|this|every) (monday|tuesday|wednesday|thursday|friday|saturday|sunday|week|year|month|weekend|summer|morning|evening|day|time)\b|tomorrow|yesterday|—")
P('prep_place', 'At, in, on: place', 'A2.1', "Uses in for inside and areas, on for surfaces, at for a point or a place of activity: in the fridge, on the wall, at the bus stop, at work.",
  v='prep_time', e="*The keys are at the table; in the wall; on the fridge; in the bus stop; in work*", m='123, 124, 125', t='A1: At, in, on: place', g='A1 simple prepositions',
  topic='prep_time_place', rx=r"\b(table|wall|floor|fridge|bag|box|pocket|shelf|bus stop|station|airport|home|work|school|page|street|kitchen|garden|room|door|corner|car|taxi|train|bus|plane|cinema|hospital|picture|photo|sky|world|ceiling|desk)\b")
P('prep_place2', 'Next to, under, between, behind, in front of, opposite', 'A2.1', "Describes where things are in relation to each other.",
  n='prep_place', e="*in front the house; between of; opposite of the bank; near of; behind of*", m='', s='Not a Murphy EGiU unit', t='A1: Next to, under, between…', g='A2 complex prepositions', topic='new')
P('prep_move', 'Movement: to, into, out of, across, through, along, past; arrive in / at', 'A2.2', "Describes direction and says arrive in a city, arrive at a place, get to, go home: She walked into the room. We arrived in Riga.",
  n='prep_place', v='prep_place', e="*We arrived to Riga; go to home; enter into the room; I've been in Paris twice* (visit)", m='126', t='A2: Prepositions of movement', g='A2 simple prepositions (increasing range)',
  topic='prep_time_place dep_prepositions', rx=r"\barriv\w+\b|\b(into|out of|across|through|along|past|towards)\b|go(es|ing)? (to )?home")
P('prep_transport', 'By car, on the bus, in a taxi, on foot', 'A2.2', "Says how somebody travels: by bus, by train; on the bus, in the car; on foot.",
  n='prep_place', e="*with bus; by foot; in the bus; on a taxi; by my car*", m='127, 128', t='no line of its own (A2: Prepositions of movement)', g='A1 preposition + no article', topic='prep_time_place', rx=r"\bby (car|bus|train|plane|taxi|bike|tram|boat)\b|on foot|(in|on) (a|the|my|his|her) (car|taxi|bus|train|plane|tram|bike)")
P('dep_basic', 'Everyday verbs with their prepositions: listen to, look at, wait for, talk to', 'A2.1', "Uses the fixed preposition after the most common verbs and puts the object pronoun after it: Listen to me. I'm waiting for you.",
  n='obj_pron', v='dep_none', e="DEP-PREP: *I'm waiting you; Listen me; Look me; She talked with me about* (fine) but *She told with me*", m='132, 133', t='no line in A1-A2 (B1: Verb + preposition)', g='A1 prepositional verbs: verb + preposition + object',
  topic='dep_prepositions', rx=r"\b(listen\w*|look\w*|wait\w*|talk\w*|speak\w*|ask\w*|pay\w*|paid) (___|to|at|for|—)", s='Taught by the app from A2.1; the list has verb + preposition only at B1')
P('dep_none', 'Verbs with no preposition: call me, discuss it, answer the question, join the team', 'A2.2', "Puts the object directly after these verbs: We discussed the plan. She married a doctor. Enter the room.",
  n='dep_basic', v='dep_basic', e="DEP-PREP: *discuss about the plan; call to me; join to our group; answer to the question; helped to other workers; married with*", m='132', t='no line of its own (B1: Verb + preposition)',
  g='not a separate EGP entry', topic='dep_prepositions', rx=r"—|\b(discuss\w*|call\w*|phone\w*|join\w*|answer\w*|help\w*|meet|met|enter\w*|reach\w*|marr\w+|contact\w*|attend\w*)\b|no preposition")
P('dep_verb', 'Verb + preposition: depend on, belong to, apologise for, think about / of', 'B1.1', "Uses the right preposition after a wider range of verbs, also before -ing: It depends on the weather. She succeeded in passing.",
  n='dep_basic vp_prep_ing', v='dep_adj noun_prep', e="DEP-PREP: *It depends from the weather; I dreamt with you; consists from; think on; Hope to hear you soon*", m='132, 133, 134, 135, 136', t='B1: Verb + preposition',
  g='B1 prepositional verbs (increasing range)', topic='dep_prepositions', d=1)
P('dep_adj', 'Adjective + preposition: good at, afraid of, interested in, married to', 'B1.1', "Uses the right preposition after an adjective, also before -ing: I'm tired of waiting. She's good at maths.",
  n='dep_basic', v='dep_verb eding', e="DEP-PREP / ED-ING: *responsible about; interested about; good in; married with; afraid from; different of; I'm very interesting in*", m='130, 131', t='B1: Adjective + preposition',
  g='A2 adjectives with prepositional phrase', topic='dep_prepositions adj_ed_ing', rx=r"\b(good|bad|afraid|interested|proud|different|married|keen|fond|tired|angry|annoyed|worried|excited|surprised|bored|famous|responsible|similar|full|aware|capable|sorry|kind|nice|scared|frightened|pleased|disappointed|crazy|ready|late|sure|typical|short|addicted|jealous|ashamed|fed up|happy|engaged|related|used)\b (___|at|of|in|to|about|with|for|from|on|by)\b")
P('noun_prep', 'Noun + preposition: a reason for, an increase in, a solution to', 'B2.1', "Uses the right preposition after a noun: the cause of, a rise in prices, a need for, an answer to.",
  n='dep_verb dep_adj', v='dep_verb', e="DEP-PREP: *the reason of; an increase of prices* (amount aside); *a solution of the problem; the cause for; an answer on*", m='129', t='B2: Noun + preposition', g='B1 noun + prepositional phrases', topic='new')

AREA('B2 sentence structures')
P('there_it_prep', 'There and it as preparatory subjects', 'B2.1', "Starts a sentence with it for a clause and with there for existence: It's no use complaining. It's a pity that … There seems to be a problem. There's no point in waiting.",
  n='there_it vp_adj_to', v='there_it', e="IT-THERE: *Is important to check; It seems to be a problem; There is important to; It is no point in waiting*", m='84', t='B2: There and it as preparatory subjects',
  g='B1 it + be + adjective + that clause; there + modal verbs; B2 there + verbs with modal meaning', topic='new')
P('have_aux', 'Have: auxiliary or main verb', 'B2.1', "Uses do with have as a main verb and have got for possession; separates have a shower (action) from have a car (state): Do you have …? I didn't have time. I'm having lunch.",
  n='have_got pp_form stative2', v='have_got', e="*Had you a good time? I hadn't breakfast; I haven't time* (old-fashioned); *I'm having a car; Have you got a shower every day?*", m='17', t='B2: Have: auxiliary or main verb', g='A2 auxiliary verbs have and do', topic='new')
P('ellipsis', 'Ellipsis and substitution: I think so, I hope not, do so, one / ones', 'B2.2', "Leaves out or replaces repeated words: A: Is it open? B: I think so. She said she would call, and she did. I prefer the red ones.",
  n='aux_uses vp_reduced', v='aux_uses', e="*I think yes; I hope no; I don't think it* for *I don't think so; She said she would call and she called it*", m='51', t='B2: Ellipsis and substitution',
  g='B1 one, ones; B1 must, should: ellipsis; C1 none, substitution', topic='new')
P('cleft', 'Cleft sentences: It was Tom who …, What I need is …', 'B2.2', "Moves the important part forward for emphasis: It was the price that surprised me. What I need is a holiday. The thing that worries me is …",
  n='rel_obj rel_what', v='rel_what', e="*It was Tom which called; What I need it is a holiday; It was yesterday when did I see him; What I need are a holiday*", m='', s='Not in Murphy EGiU; Hewings, Advanced Grammar in Use (from memory, not checked)',
  t='B2: Cleft sentences', g='B2 the thing / fact / point / problem is (that); C1 what cleft clause; C2 it cleft', topic='new', s2='Level: test-english B2, EGP C1-C2. See the questions for Inga')
P('neg_inversion', 'Inversion after negative adverbials: Never have I seen …, Not only … but also', 'B2.2', "Uses question word order after a fronted negative expression in formal style: Never have I seen such a mess. No sooner had we left than it started to rain.",
  n='q_yesno pastp_form c_inv', v='c_inv', e="*Never I have seen; Not only he came but also; No sooner we had left than; Hardly had we left than* (when)", m='', s='Not in Murphy EGiU; Hewings, Advanced Grammar in Use (from memory, not checked)',
  t='B2: Inversion with negative adverbials', g='B2 never, inverted front position; past perfect: inversion with no sooner … than; C1 not only … but also with inversion; C2 hardly … when', topic='new', s2='Level: test-english B2; EGP B2 for never and no sooner, C1-C2 for the rest. Returns in C1: Advanced word order')
