# Grammar map data, part 2: modals, passive, conditionals and wishes, reported speech, questions.
from lib import P, AREA

AREA('Modal verbs')
P('can', "Can / can't: ability, permission, requests", 'A2.1', "Says what somebody can do and asks for things: I can swim. Can I sit here? Can you help me?; no -s, no to, no do.",
  n='ps_form', v='ps_negq', e="MODAL: *I can to swim; She cans drive; Do you can swim? He doesn't can*", m='26, 37', t="A1: Can, can't", g='A1 affirmative, negative, questions; ability, requests; A2 permission',
  topic='modal_verbs', rx=r"\bcan\b|\bcan't\b|\bcannot\b")
P('could_past', "Could / couldn't: ability in the past", 'A2.2', "Talks about general ability in the past: I could swim when I was five. I couldn't sleep.",
  n='can was_were', v='can able_once', e="*I can swim when I was five; I could to swim; Did you could?*", m='26', t='A2: Have to, don\'t have to, must, mustn\'t (the card of the topic); B1: Can, could, be able to',
  g='A2 could: ability', topic='modal_verbs more_modals', rx=r"\bcould(n't)?\b.*(when (I|he|she|we|they) (was|were)|years old|as a child|in the past|at (five|six|seven|ten))|past of can")
P('requests', 'Polite requests and permission: Could you …? Can I …? Would you …?', 'A2.2', 'Asks somebody to do something and asks for permission with the right degree of politeness.',
  n='can', v='would_like', e="*Could you to help me? Can you help me, please?* said to a stranger where *Could you* fits; *May you help me?*", m='37', t='no line of its own (A1: Can; A1: Would you like)',
  g='A1 can: requests; A2 could: requests; B1 would: polite requests', topic='modal_verbs', rx=r"polite|request|please\b|\bcould you\b|\bcan you\b|\bwould you\b|\bcould I\b|\bmay I\b|permission")
P('must_have_to', 'Must and have to: obligation', 'A2.2', 'Says what is necessary; forms have to with do / does (Do you have to go? She has to work).',
  n='can ps_negq', v='should mustnt_dont', e="MODAL: *We must to go; She musts; Do you must?*; *She have to; Has she to go?*", m='31', t="A2: Have to, don't have to, must, mustn't", g='A2 must: obligation; A2 have to: affirmative, questions',
  topic='modal_verbs', d=1)
P('mustnt_dont', "Mustn't or don't have to", 'A2.2', "Separates not allowed (mustn't) from not necessary (don't have to).",
  n='must_have_to', v='must_have_to neednt', e="*You mustn't come* meaning it is not necessary; *You don't have to smoke here* meaning it is forbidden", m='31, 32', t="A2: Have to, don't have to, must, mustn't",
  g="A2 must: negative; have to: negative", topic='modal_verbs', rx=r"mustn't|must not|don't have to|doesn't have to|not necessary|not allowed|forbidden")
P('should', "Should / shouldn't: advice", 'A2.2', "Gives and asks for advice: You should see a doctor. What should I do?",
  n='can', v='must_have_to', e="MODAL: *You should to go; He shoulds; Do I should?*", m='33', t='A2: Should', g='A2 affirmative, negative, questions; advice', topic='modal_verbs', rx=r"\bshould(n't)?\b|advice")
P('had_to', 'Obligation in the past and future: had to, will have to', 'B1.1', "Moves obligation to other times, where must has no form: I had to work late yesterday. We'll have to leave early.",
  n='must_have_to pst_negq will_form', v='must_have_to', e="*I must work late yesterday; I musted; We will must leave; Did you had to?*", m='31', t='B1: Have to, must, should', g='B1 have to: infinitive',
  topic='modal_verbs', rx=r"\bhad to\b|will have to|won't have to|didn't have to|did .* have to")
P('might', 'Might and may: possibility', 'A2.2', "Says that something is possible now or in the future: It might rain. She may be late. They might not come.",
  n='will_form can', v='will_form', e="MODAL: *It might rains; It mights; It might to rain; Maybe it will might*", m='29, 30', t='A2: Might; A2: May and might', g='A2 may, might: possibility',
  topic='more_modals', rx=r"\bmight\b|\bmay\b", s='Level: test-english A2, EGP A2; the app has its tasks at B1.1-B1.2')
P('be_able', 'Be able to in other tenses', 'B1.1', "Uses be able to where can has no form: I'll be able to come. I haven't been able to call. I'd like to be able to swim.",
  n='can will_form pp_form', v='can', e="MODAL: *I will can come; I haven't could call; I'd like to can swim*", m='26', t='B1: Can, could, be able to', g='A2 will be able to; B1 modal with be able to; be able to: past',
  topic='more_modals modal_verbs', rx=r"able to", d=1)
P('able_once', 'Could or was able to / managed to: one success', 'B1.1', "Uses was able to or managed to for one achievement in the past, could for general ability, couldn't for both.",
  n='could_past be_able', v='could_past', e='COULD: *The door was locked, but I could open it; I could finish the report yesterday*', m='26', t='B1: Can, could, be able to', g='B1 be able to: past',
  topic='more_modals', rx=r"managed to|(was|were) able to|one (success|occasion|time)|succeed")
P('allowed_to', 'Permission: can, could, be allowed to', 'B1.1', "Talks about what is and was permitted, in any tense: We aren't allowed to park here. I was allowed to leave early.",
  n='can must_have_to', v='mustnt_dont', e="*We are allowed park here; It is not allowed to smoke* with it; *I could leave early yesterday* for one permission", m='26, 37', t='B2: Modals: permission, obligation, prohibition, necessity',
  g='B1 be allowed to: permission; could: permission', topic='more_modals', rx=r"allowed to", s='Level: taught by the app at B1 (EGP B1); the list names it at B2 as part of a wider set')
P('ought_to', 'Ought to and had better', 'B1.2', "Gives advice with ought to and a strong warning with had better (not) + base form: You'd better hurry.",
  n='should', v='should its_time', e="*You ought go; You had better to go; You'd better don't; You better had*", m='33, 35', t="B1: Had better, it's time", g='B1 ought to: advice (had better not found in EGP)', topic='new')
P('deduction', "Deduction about the present: must, might, could, can't + be", 'B1.2', "Says how sure a guess is: He must be at home. She might be ill. That can't be right.",
  n='might must_have_to', v='must_have_to might', e="*She mustn't be at home* for *can't be*; *He can be at home* for *might be*; *It must to be*", m='28, 29', t='B1: Modal verbs of deduction',
  g='B1 must: deductions and conclusions; could: possibility', topic='more_modals', rx=r"must be|can't be|might be|could be|may be|sure (it|he|she|that)|deduc|certain(ly)? (not )?(true|is)")
P('neednt', "Needn't and don't need to", 'B1.2', "Says that something is not necessary and separates it from a prohibition: You needn't wait. You don't need to come.",
  n='mustnt_dont', v='mustnt_dont', e="*You needn't to wait; You don't need come; You needn't park here* for a prohibition", m='32', t="B1+: Needn't, don't need to, didn't need to, needn't have",
  g="B2 need: negative; needn't: lack of obligation", topic='more_modals', rx=r"needn't(?! have)|don't need to|doesn't need to")
P('neednt_have', "Didn't need to or needn't have", 'B2.1', "Separates an action that was not necessary and probably not done (didn't need to) from one that was done for nothing (needn't have done).",
  n='neednt should_have', v='neednt should_have', e="*We needn't hurried; We didn't need to hurry* said about an unnecessary thing that was done; *We needn't have to hurry*", m='32',
  t="B1+: Needn't, don't need to, didn't need to, needn't have", g="C1 needn't have + -ed", topic='more_modals', rx=r"needn't have|didn't need to", s="Level: the list teaches it at B1+; EGP records needn't have only at C1")
P('should_have', 'Should have, could have done: criticism and regret', 'B1.2', "Says that the right thing was not done or that a chance was missed: You should have told me. We could have won.",
  n='should pp_form', v='c3 wish_past', e="*You should told me; You should have tell me; You should had told me; You must have told me* as criticism", m='27, 33', t='no line of its own (B1+: Past modals of deduction; B2: Modals, from memory)',
  g='B1 should: past affirmative, past negative, regret; B2 could: regret', topic='passive_modals', s='In the app only inside the passive (should have been closed)')
P('deduction_past', "Deduction about the past: must have, might have, can't have done", 'B2.1', "Guesses about the past with the right certainty: She must have left. He might have forgotten. They can't have seen us.",
  n='deduction should_have', v='should_have deduction', e="*She must left; He must had left; She mustn't have seen us* for *can't have*; *He can have forgotten*", m='27, 28, 29', t='B1+: Past modals of deduction; B2: Speculation and deduction',
  g='B2 must: past affirmative; could: past speculation; B1 might: past affirmative; C1 can: past negative deductions', topic='new', s='Level: the B1+ list covers B1.2-B2.1; EGP mostly B2, so the second half')
P('supposed_to', 'Be supposed to, be meant to', 'B2.1', "Talks about what is expected or arranged, and what people say: You're supposed to wear a helmet. It's supposed to be a great film.",
  n='must_have_to allowed_to', v='must_have_to', e="*You are suppose to wear; You supposed to; It supposes to be*", m='45', t='B2: Modals: permission, obligation, prohibition, necessity',
  g='B1 be supposed to: past expectation; B2 obligation, hearsay; be meant to', topic='new')
P('modals_cont', 'Modals with continuous forms: must be joking, might be working', 'B2.1', "Speculates about something in progress now or then: He must be working late. She might have been driving.",
  n='deduction pc_form', v='deduction', e="*He must working; She must be work; He might been sleeping*", m='28, 29', t='B2: Speculation and deduction', g='B2 should be + -ing', topic='new')

AREA('Passive')
P('pas_pres', 'Present simple passive: is / are + third form', 'A2.2', 'Says what is done when the doer is unknown or not important: English is spoken here. These phones are made in China.',
  n='be_pres v3', v='ps_form', e='*English is speak here; These phones make in China; The windows is cleaned*', m='42', t='A2: Present and past simple passive', g='A2 present simple, affirmative',
  topic='present_simple_passive', d=1)
P('pas_past', 'Past simple passive: was / were + third form', 'A2.2', 'Tells what was done in the past: The bridge was built in 1890. I was born in Riga.',
  n='pas_pres was_were', v='pst_reg', e='*I am born in 1990; The bridge was build; The windows was broken; I born in*', m='42', t='A2: Present and past simple passive', g='A2 past simple, affirmative',
  topic='past_simple_passive', d=1)
P('pas_by', 'The doer with by, only when it matters', 'A2.2', 'Adds by + the doer when it is new or important and leaves it out when it is not: This picture was painted by my grandfather.',
  n='pas_pres', v='pas_act', e="*It was painted from my grandfather; My bike was stolen by somebody*", m='42', t='A2: Present and past simple passive', g='A2 with by to add information; B1 giving focus with by',
  topic='present_simple_passive past_simple_passive', rx=r"\bby (my|the|a|an|his|her|our|their|some|people|\w+ \w+)\b|doer|agent")
P('pas_negq', 'Passive negatives and questions', 'B1.1', "Makes passive negatives and questions by moving be: Where are these phones made? When was the castle built? It wasn't finished.",
  n='pas_past q_wh', v='ps_negq pst_negq', e="*Where these phones are made? When the castle was built? Did the castle was built?*", m='42', t='B1: Passive verb forms', g='B1 present simple, negative; B2 past simple negative',
  topic='present_simple_passive past_simple_passive', rx=r"\?|n't\b|\bnot\b|make a (yes/no )?question|negative", s='The app has these tasks from A2.2')
P('pas_act', 'Active or passive?', 'B1.1', 'Decides by asking who does the action, turns an active sentence into a passive one and back, and knows that verbs without an object have no passive.',
  n='pas_past pas_by', v='ps_form pst_reg', e="*The accident was happened; My bike stole yesterday; The film was appeared in 2019*", m='42, 44', t='B1: Active and passive', g='B1 present simple, past simple passive (increasing range)',
  topic='present_simple_passive past_simple_passive', rx=r"active|rewrite|start with|somebody|someone|they (make|made|built|clean|speak|sell|sold|grow|use|check|stole|invite|send|sent)|happen|who does")
P('pas_cont', 'Present continuous passive: is being done', 'B1.2', 'Says that something is being done now or around now: The road is being repaired.',
  n='pas_pres pc_form', v='pas_pres pas_perf', e='*The road is repairing; Your order is been prepared; The rooms is being cleaned*', m='43', t='B1: Passive verb forms', g='B1 present continuous, affirmative',
  topic='present_continuous_passive', d=1)
P('pas_perf', 'Present perfect passive: has been done', 'B1.1', 'Gives news or a result without the doer: The email has been sent. Has the problem been solved yet?',
  n='pas_past pp_just', v='pas_past pas_cont', e='*The email has sent; The problem have been solved; The tickets have been sold yesterday; has being fixed*', m='43', t='B1: Passive verb forms',
  g='B2 present perfect simple, affirmative', topic='present_perfect_passive', d=1, s='Level: test-english B1, EGP B2')
P('pas_will', 'Future passive: will be done, is going to be done', 'B1.1', 'Says what will be done: The results will be announced on Friday.',
  n='pas_pres will_form', v='will_form', e='*The results will announced; You will be tell; Will be the meeting held online?*', m='43', t='B1: Passive verb forms', g='B2 passive with will, future reference; B1 passive infinitive after going to',
  topic='future_passive', d=1, s='Level: test-english B1, EGP B2')
P('pas_modal', 'Passive after modal verbs: must be done, can be bought', 'B1.1', 'Uses modal + be + third form for rules, advice and possibility: Tickets can be bought online.',
  n='pas_pres can must_have_to should', v='pas_will', e='*The report must finished; Tickets can be buy; It must to be done; The door should be lock*', m='43', t='B1: Passive verb forms; B1+: Passive: all tenses',
  g='B2 passive with modal verbs', topic='passive_modals', d=1, s='Level: test-english B1, EGP B2')
P('pas_modal_past', 'Passive after a past modal: should have been done', 'B2.1', 'Criticises or guesses about the past in the passive: The window should have been closed. It must have been stolen.',
  n='pas_modal should_have', v='pas_modal', e="*It should have closed; It should been closed; It must have being stolen*", m='43', t='B1+: Passive: all tenses (from memory)', g='B2 passive: modal perfect',
  topic='passive_modals', rx=r"have been \w+", s='On the passive_modals card (B1.1-B1.2 in the app)')
P('pas_other', 'Passive in other tenses: was being done, had been done', 'B2.1', 'Uses the passive in the past continuous and past perfect: The room was being cleaned. The car had been stolen before.',
  n='pas_cont pas_perf pastp_form', v='pas_cont pas_perf', e='*The room was cleaning; The car had stolen; was been cleaned*', m='43', t='B1+: Passive: all tenses', g='B2 past continuous affirmative; past perfect simple, affirmative', topic='new')
P('pas_inf_ing', 'Passive infinitive and -ing: to be told, being asked', 'B2.1', "Uses the passive after verbs and prepositions: I want to be told. Nobody likes being criticised.",
  n='pas_modal vp_to vp_ing', v='vp_to vp_ing', e="*I want to told; Nobody likes be criticised; I don't like to being asked*", m='43, 44', t='B1+: Passive: all tenses (from memory)', g='B1-B2 passive infinitive; C1 non-finite clauses', topic='new')
P('pas_two_obj', 'Passive of verbs with two objects: I was given a book', 'B2.1', 'Starts the passive with the person: I was given a ticket. She was offered the job.',
  n='pas_past two_obj', v='two_obj', e="*It was given me a ticket; To me was given; I was explained the rules*", m='44', t='B2: Passive verbs with two objects', g='B1-B2 passive with verbs taking two objects', topic='new')
P('pas_report', 'Passive with reporting verbs: It is said that … / He is said to …', 'B2.1', 'Reports what people say or believe without naming them, with both patterns.',
  n='pas_pres rep_backshift vp_to', v='rep_backshift', e="*He is said that he is rich; It is said him to be rich; He is said to being*", m='45', t='B1+: Passive with reporting verbs', g='B2 passive: summaries and evaluations; C1 summarising with it', topic='new')
P('distancing', 'Distancing: seem, appear, apparently, is believed to have done', 'B2.2', 'Reports information without taking responsibility for it: He appears to have left. There is thought to be a problem.',
  n='pas_report', v='pas_report', e="*He seems that he left; It seems him to be; He is believed to left*", m='45', t='B2: Distancing and passive of reporting verbs', g='B2 be supposed to: hearsay; C1 it + passive, summarising', topic='new')
P('caus_have', 'Have something done', 'B1.2', "Says that somebody else does a service for us, in any tense: I had my hair cut. She's having her car repaired.",
  n='pas_past', v='pas_past pastp_form', e="*I cut my hair at the hairdresser's; I had cleaned my car* (= I cleaned it); *She is having her car repair*", m='46', t='B1+: Have something done',
  g='B2 have + object + -ed', topic='causative', d=1, s='Level: test-english B1+, EGP B2; the app starts at B1.1')
P('caus_get', 'Get something done; something bad that happened: had my bag stolen', 'B2.1', "Uses get as the informal form and have for an unpleasant experience: We got the windows cleaned. She had her bag stolen.",
  n='caus_have', v='caus_have get_b2', e="*She was stolen her bag; We got cleaned the windows*", m='46', t='B1+: Have something done; B2: Get', g='C1 get + object + -ed; B2 have + object + -ed',
  topic='causative', rx=r"\b(get|got|gets|getting)\b|stolen|broken into|bad (thing|experience)|happened to")

AREA('Conditionals and wishes')
P('c0', 'Zero conditional: if + present, present', 'A2.2', 'Talks about what always happens, and gives an instruction for a situation: If you heat ice, it melts. If you feel sick, stay at home.',
  n='ps_negq imperative', v='c1', e='TIME-CLAUSE: *If you will heat ice, it melts*; 3S: *If water boil, it turns*', m='', s='Not a Murphy EGiU unit (if + present is in units 25 and 38)', t='A2: First conditional and future time clauses; B1+: Zero and first conditional, future time clauses',
  g='A2 if + present simple; if clause + imperative', topic='cond_zero', d=1)
P('c1', 'First conditional: if + present, will', 'A2.2', "Talks about a real possibility in the future and its result; either part can come first: If it rains, we'll stay at home.",
  n='will_form ps_negq', v='c0 fut_time_clause', e="TIME-CLAUSE: *If it will rain, we'll stay at home*; 3S: *If she call, I'll tell you*", m='25, 38', t='A2: First conditional and future time clauses',
  g='B1 present simple if clause + will; A2 will after if', topic='cond_first', d=1)
P('if_when', 'If or when', 'B1.1', "Uses if for something that may happen and when for something that will: If I see her, I'll tell her. When I see her, I'll tell her.",
  n='c1 fut_time_clause', v='c1 fut_time_clause', e="*When it rains tomorrow, we'll stay at home* for an uncertain event; *If I am older, I'll…*", m='25', t='B1: First conditional, future time clauses', g='A2-B1 (not a separate EGP entry)',
  topic='cond_first cond_zero time_clauses', rx=r"\bif or when\b|\bif / when\b|maybe it happens|it will happen|\bsure (it|that)\b.*when")
P('c1_unless', 'Unless = if … not', 'B1.1', "Replaces if … not with unless and keeps the verb positive: Unless you hurry, you'll miss the bus.",
  n='c1', v='c1 c_alt', e="*Unless you don't hurry; Unless you will hurry*", m='115', t='B1: First conditional, future time clauses; B2: Unless, even if, provided, as long as', g='B1 unless, exceptions',
  topic='cond_first cond_advanced', rx=r"\bunless\b")
P('c1_modal', 'First conditional with may, might, can, should or an order in the result', 'B1.1', "Varies the result: If you finish early, you can go. If it rains, we might stay in.",
  n='c1 might should', v='c1', e="*If you will finish early, you can go; If it rains, we might to stay*", m='38', t='B1: First conditional, future time clauses', g='B1 present simple if clause + modal',
  topic='cond_first', rx=r"\b(may|might|can|should|must)\b")
P('c0_c1', 'Zero or first conditional: always, or this one time?', 'B1.2', "Chooses the present for what is always true and will for one future situation: If I drink coffee late, I can't sleep. If I drink this coffee, I won't sleep tonight.",
  n='c0 c1', v='c0 c1', e="*If you heat ice, it will melt* said as a general fact; *If it rains tomorrow, we stay at home*", m='', s='Not a Murphy EGiU unit', t='B1+: Zero and first conditional, future time clauses',
  g='A2-B1', topic='cond_zero cond_first', rx=r"always true|general (fact|rule|truth)|one (future )?situation|tonight|tomorrow.*(always|every)|whenever")
P('c2', 'Second conditional: if + past, would', 'B1.1', "Imagines something that is not true now or is unlikely: If I lived by the sea, I'd swim every day. What would you do if…?",
  n='pst_irr pst_negq c1', v='c1 c3', e="IF-WOULD: *If I would have more money, I'd buy a car; If she knew, she will tell us*", m='38, 39', t='A2: Second conditional; B1: Second conditional',
  g='B1 if + past simple + would, imagined situation', topic='cond_second', d=1, s='Level: test-english A2 and again B1, EGP B1; the app starts at B1.1. See the questions for Inga')
P('c2_were', "If I were you, I'd …", 'B1.1', "Gives advice with If I were you and uses were for every person in careful English.",
  n='c2 should', v='should', e="*If I am you, I'd call her; If I would be you; If I was you, I will*", m='39', t='B1: Second conditional', g='B1 if I were you + would', topic='cond_second', rx=r"\bwere you\b|if (I|he|she|it) were\b|advice")
P('c1_c2', 'First or second conditional: real or imagined?', 'B1.2', "Chooses by how real the situation is: If it rains, I'll stay at home. If I had wings, I'd fly.",
  n='c1 c2', v='c1 c2', e="*If I win the lottery, I'll buy a house* said without a ticket; *If I had time tomorrow, I will help* (mixing the two)", m='38', t='B1: First and second conditionals',
  g='B1', topic='cond_second cond_first', rx=r"real (and|or) (possible|likely)|unreal or unlikely|first or second|possible or (imagined|unreal)|likely|unlikely")
P('c3', 'Third conditional: if + had done, would have done', 'B1.2', "Imagines a different past and its result: If I had known, I would have called.",
  n='pastp_form c2 should_have', v='c2 should_have', e="IF-WOULD: *If I would have known, I would have called; If I had known, I would have call; If we had took a taxi*", m='40', t='B1: Third conditional',
  g='B1 if + past perfect + would have + -ed', topic='cond_third', d=1)
P('c3_modal', 'Third conditional with could have, might have', 'B2.1', "Makes the imagined result less sure or about ability: If you had told me, I could have helped.",
  n='c3 should_have', v='c3', e="*If you told me, I could have helped; If you had told me, I could helped*", m='40', t='B1+: Second and third conditionals (from memory)', g='C1 if + past perfect + modal verbs',
  topic='cond_third', rx=r"could have|might have|could've|might've")
P('c2_c3', 'Second or third conditional: now or then?', 'B2.1', "Chooses by time: If I had time, I'd help (now). If I'd had time, I'd have helped (then); reads 'd as had or would.",
  n='c2 c3', v='c2 c3', e="*If I had time yesterday, I would help; If I'd have known*", m='39, 40', t='B1+: Second and third conditionals', g='B1 (both forms)',
  topic='cond_third cond_second', rx=r"second or third|now: second|the past: third|'d = (had|would)|\bnow\b.*\byesterday\b|\byesterday\b.*\bnow\b")
P('c_mixed', 'Mixed conditional: past condition, present result', 'B2.1', "Links a different past with a result now: If I had taken that job, I would be rich now.",
  n='c2_c3', v='c3', e="*If I would have taken the job, I would be rich now; If he had studied medicine, he will be a doctor now*", m='', s='Not in Murphy EGiU (units 38-40 treat the two times separately)',
  t='B2: Mixed conditionals', g='C1 if + past perfect + modal verbs, imagined situation (the nearest EGP entry)', topic='cond_mixed', d=1, s2='Level: test-english B2, EGP C1')
P('c_mixed2', 'Mixed conditional: present condition, past result', 'B2.2', "Links a lasting fact with a result in the past: If he were more confident, he would have asked for a pay rise.",
  n='c_mixed', v='c_mixed c3', e="*If she is more patient, she wouldn't have shouted; If he was more confident, he would ask* about a past chance", m='', s='Not in Murphy EGiU', t='B2: Mixed conditionals',
  g='not a separate EGP entry', topic='cond_mixed', rx=r"if (I|he|she|we|they|you|it) (were|weren't|was|wasn't|knew|spoke|had\b(?! \w+(ed|en|ne|wn|un|ght|ept|ost|aid|old)\b)|didn't|liked|lived)\b.*would(n't)? have|present condition|quality now|lasting")
P('c_alt', 'As long as, provided (that), even if, in case, supposing', 'B2.1', "Uses other words than if for a condition: You can borrow it as long as you bring it back. Even if it rains, we'll go.",
  n='c1_unless c2', v='c1_unless in_case', e="*As long as you will bring it back; Provided you would pay; Even it rains*", m='115', t='B2: Unless, even if, provided, as long as', g='B2 conditions with as long as, provided',
  topic='cond_advanced', rx=r"as long as|provided|providing|even if|supposing|on condition|only if")
P('c_inv', 'Inverted conditionals: Had I known …, Should you need …, Were she …', 'B2.2', "Recognises and forms the formal conditional without if: Should you have any questions, please contact us. Had I known, I would have helped.",
  n='c3 c2_were', v='c3', e="*If had I known; Had I knew; Hadn't she missed the train* for *Had she not missed; Would you need help, call me*", m='', s='Not in Murphy EGiU; Hewings, Advanced Grammar in Use (from memory, not checked)',
  t='B2: All conditionals, alternatives to if, inversion', g='C1 inverted conditional with should; C2 inverted past perfect; C2 inverted were + to-infinitive', topic='cond_advanced', d=1, s2='Level: test-english B2, EGP C1-C2. See the questions for Inga')
P('wish_pres', 'I wish / if only + past: a wish about now', 'B1.2', "Says that somebody would like the present to be different: I wish I had more time. If only I could drive.",
  n='c2', v='c2 wish_would', e="*I wish I have more time; I wish I would have more time; I wish I can drive*", m='39, 41', t='B1+: I wish / if only', g='B1 past simple with wish: regret that things are not different',
  topic='cond_advanced', rx=r"wish (I|he|she|we|they|you|it|my|the) (had(?! \w+(ed|en|ne|wn)\b)|were|was|could|knew|lived|didn't|spoke|weren't|wasn't)|if only (I|he|she|we|they|you|it) (had(?! \w+ed\b)|were|was|could|knew)|wish.*\bnow\b", s='The app has it at B2.2 only')
P('wish_past', 'I wish / if only + had done: regret about the past', 'B2.1', "Regrets something that happened or did not happen: I wish I had studied harder. If only we had tested the app!",
  n='wish_pres c3', v='wish_pres should_have', e="*I wish I studied harder* about a finished chance; *I wish I would have studied; I wish I have studied*", m='40, 41', t='B1+: I wish / if only; B2: Wish, rather, if only, it\'s time',
  g='B2 past perfect after if only and wish, imagined past', topic='cond_advanced', rx=r"wish.*\bhad(n't)? (\w+ly )?\w+|if only.*\bhad(n't)? \w+|regret")
P('wish_would', 'I wish … would: wanting somebody or something to change', 'B2.1', "Complains about a habit or asks for a change: I wish you would listen. I wish it would stop raining.",
  n='wish_pres', v='wish_pres', e="*I wish I would have more time* (the same subject); *I wish you will listen; I wish you listen*", m='41', t="B2: Wish, rather, if only, it's time", g='not a separate EGP entry',
  topic='cond_advanced', rx=r"wish.*\bwould(n't)?\b|annoy")
P('its_time', "It's time to go; it's time for a break", 'B1.2', "Says that the moment for something has come: It's time to leave. It's time for lunch.",
  n='vp_to', v='its_time_past', e="*It's time go; It's time for go; It's time that we go*", m='35', t="B1: Had better, it's time", g='not found in EGP', topic='new')
P('its_time_past', "It's (high / about) time + subject + past", 'B2.1', "Says that something should already be happening: It's high time we went. It's about time you called your mother.",
  n='its_time wish_pres', v='its_time', e="*It's high time we go; It's time we will go; It's high time to we went*", m='35', t="B2: Wish, rather, if only, it's time", g='not found in EGP',
  topic='unreal_time', rx=r"time\b", d=1)
P('would_rather', "Would rather, would sooner, would prefer: what I prefer to do", 'B1.2', "States a preference: I'd rather walk. I'd rather not go. I'd prefer to stay. I'd rather walk than drive.",
  n='would_like vp_to', v='would_like', e="*I'd rather to walk; I'd rather walking; I'd prefer stay; I'd rather don't go; I would rather walk that drive*", m='59', t='B1: Would rather, would sooner; B1+: Would rather, would prefer',
  g='B1 would prefer + to (would rather not found in EGP)', topic='unreal_time', rx=r"('d|would) (rather|sooner) (not )?(?!(you|he|she|we|they|it|my|the|our|his|her|people|everyone|somebody)\b)\w+|would prefer|'d prefer", s='The app has it at B2.2 only')
P('rather_you', "I'd rather you + past: what I want somebody else to do", 'B2.1', "Asks politely for different behaviour: I'd rather you came a bit earlier. I'd rather you didn't call after ten.",
  n='would_rather wish_pres', v='would_rather vp_obj_to', e="*I'd rather you come earlier; I'd rather you to come; I'd rather you don't call*", m='59', t="B2: Wish, rather, if only, it's time", g='not found in EGP',
  topic='unreal_time', rx=r"('d|would) (rather|sooner) (you|he|she|we|they|it|my|the|our|his|her|people|everyone|somebody)\b")

AREA('Reported speech')
P('rep_say_tell', 'Say or tell', 'B1.1', "Uses tell with a person and say without one: He told me (that) … / He said (that) … / He said to me …",
  n='pst_irr', v='two_obj_explain', e='SAY-TELL: *He said me that; She told that she was busy; He said, that he was tired*', m='48', t='A2: Reported speech', g='A2 reported statements with say, with tell (pronoun shift, no tense shift)',
  topic='rep_statements', rx=r"\b(say|said|tell|told)\b.*\b(tell|told|say|said)\b|said me|told that|said to (me|him|her|us|them)|\btell\b needs|needs a person")
P('rep_backshift', 'Reported statements: the tense goes one step back', 'B1.1', "Reports what somebody said after said / told: am → was, work → worked, will → would, can → could.",
  n='rep_say_tell was_were pst_irr will_form can', v='rep_stay', e='BACKSHIFT: *She said she is tired* (no longer true); *He said he will come; She said she can help*', m='47', t='A2: Reported speech; B1: Reported speech',
  g='B1 reported statements, pronoun and tense shift', topic='rep_statements', d=1, s='Level: test-english A2 and again B1; EGP A2 for say / tell with pronoun change, B1 for the tense change. See the questions for Inga')
P('rep_pron_time', 'Reported speech: pronouns, time and place words', 'B1.1', "Changes I → he / she, my → his / her, tomorrow → the next day, here → there, this → that.",
  n='rep_backshift', v='rep_backshift', e='*She said I was tired* (for she); *He said he would come tomorrow* reported a week later', m='47, 48', t='B1: Reported speech', g='B1 temporal shifts, future; B2 temporal shifts, past',
  topic='rep_statements', rx=r"the next day|the day before|the following|the previous|that day|\bthen\b|there\b.*\bhere\b|tomorrow|yesterday|pronoun|today|tonight|next week|last week")
P('rep_backshift2', 'Reported statements: past → past perfect, present perfect → past perfect', 'B1.2', "Reports a past or perfect tense: 'I lost my keys' → He said he had lost his keys. 'I've finished' → She said she had finished.",
  n='rep_backshift pastp_form', v='rep_backshift', e="*He said he lost his keys* where the order matters; *She said she has finished; He said he had went*", m='47, 48', t='B1: Reported speech', g='B2 past perfect: reports of statements',
  topic='rep_statements', rx=r"\bhad (\w+ly )?(\w+ed|been|gone|done|seen|lost|left|taken|bought|found|forgotten|met|made|told|written|broken|sold|had|won|heard|read|eaten|spent)\b")
P('rep_stay', 'When the tense can stay: still true, says, has said', 'B1.2', "Knows that after a present reporting verb nothing changes, and that a fact that is still true may keep its tense: She says she's tired. He said the Earth goes round the Sun.",
  n='rep_backshift', v='rep_backshift', e="*She says she was tired* for a present state; in our tasks the step back is the form practised (teacher, 11 November)", m='48', t='B1: Reported speech (from memory)', g='B2 citation, present simple',
  topic='rep_statements', rx=r"still true|\bsays\b|\btells\b|has (said|told)|earth|always true|still (lives|works)")
P('rep_orders', 'Reported requests and orders: told / asked somebody (not) to', 'B1.2', "Reports an order or a request with to + verb: He told me to wait. She asked me not to call.",
  n='rep_say_tell vp_obj_to', v='rep_q_yn', e="*He told me wait; She asked me don't call; He said me to wait; She told to me to wait*", m='48', t='A2: Reported speech; B1: Reported speech',
  g='B1 reported requests and commands; B2 negative', topic='rep_questions', rx=r"\b(told|asked|ordered|begged|warned|reminded) (me|him|her|us|them|\w+) (not )?to\b|request|order|imperative|don't|please")
P('rep_q_wh', 'Reported wh-questions: He asked where I lived', 'B1.2', "Reports a question with a question word: statement word order, no do / did, tense one step back.",
  n='rep_backshift q_wh', v='q_wh iq_wh', e="Q-ORDER: *He asked where did I live; She asked what was my name; He asked me where do I work*", m='50', t='B1: Reported speech', g='B1 reported wh- questions',
  topic='rep_questions', d=1)
P('rep_q_yn', 'Reported yes / no questions: She asked if / whether …', 'B1.2', "Reports a yes / no question with if or whether and statement order: She asked if I liked coffee.",
  n='rep_backshift q_yesno', v='rep_q_wh iq_yn', e="IND-YESNO: *She asked do I like coffee; He asked me that I was ready; She asked if did I like*", m='50', t='B1: Reported speech', g='B1 reported yes-no questions',
  topic='rep_questions', rx=r"\b(if|whether)\b")
P('rv_to', 'Reporting verbs + to: offer, refuse, promise, agree, threaten', 'B2.1', "Reports the meaning, not the words: 'Shall I help?' → She offered to help.",
  n='rep_orders vp_to', v='rv_ing rv_obj_to', e="*She offered helping; He refused that he would pay; She promised me to come*", m='54', t='B1+: Reporting verbs', g='B2 reporting verbs (increasing range)',
  topic='rep_verbs', rx=r"\b(offer|refus|promis|agree|threaten)\w*\b", s='The app has the whole topic at B2.2')
P('rv_obj_to', 'Reporting verbs + person + to: advise, warn, remind, invite, encourage, persuade', 'B2.1', "'Don't forget to call.' → She reminded me to call. 'You should rest.' → He advised me to rest.",
  n='rep_orders vp_obj_to', v='rv_to rv_ing', e="*He advised to rest; She reminded to me to call; He warned me to not touch; She suggested me to go*", m='55', t='B1+: Reporting verbs', g='B1 verbs + direct object + to-infinitive',
  topic='rep_verbs', rx=r"\b(advis|warn|remind|invit|encourag|persuad|urg|order|convinc)\w*\b")
P('rv_ing', 'Reporting verbs + -ing: suggest, admit, deny, recommend', 'B2.1', "'Let's take a taxi.' → He suggested taking a taxi. 'I didn't take it.' → He denied taking it.",
  n='vp_ing rep_backshift', v='rv_to rv_obj_to', e="PATTERN: *He suggested me to take a taxi; He suggested to take; She denied to take it; He admitted to took*", m='53', t='B1+: Reporting verbs', g='B2 verb + -ing form',
  topic='rep_verbs', rx=r"\b(suggest|admit|deny|denied|denies|recommend|regret)\w*\b", d=1)
P('rv_prep_ing', 'Reporting verbs + preposition + -ing: apologise for, insist on, accuse of, congratulate on', 'B2.1', "'I'm sorry I'm late.' → He apologised for being late. 'You cheated.' → They accused him of cheating.",
  n='rv_ing vp_prep_ing', v='rv_ing', e="DEP-PREP: *She insisted to pay; They accused him for cheating; He apologised to be late; congratulated me for passing*", m='62', t='B1+: Reporting verbs', g='B2 (verb + preposition + -ing, not a separate EGP entry)',
  topic='rep_verbs', rx=r"\b(apologi|insist|accus|congratulat|blam|thank|complain)\w*\b")

AREA('Questions')
P('q_yesno', 'Yes / no questions and short answers: be, do, have, can', 'A2.1', "Starts the question with the right helping verb and answers with it: Are you tired? Do you work here? Can you swim? Yes, I do.",
  n='be_pres ps_negq can', v='be_pres ps_negq', e="DO: *Are you like coffee? Do you tired? You like coffee?*; short answers *Yes, I like; Yes, I'm*", m='49', t='A1: Questions: word order and question words',
  g='A1 yes / no with modal verbs; A2 with be, do, have', topic='aux_verbs', d=1)
P('q_wh', 'Wh-questions: question word + helping verb + subject', 'A2.1', "Asks with what, where, when, who, why, how, how much / many and keeps the order: Where do you live? What are you doing?",
  n='q_yesno', v='q_subject', e="DO: *Where you live? What you are doing? Why she is late? How long you have been here?*", m='49', t='A1: Questions: word order and question words; A2: Question forms',
  g='A2 wh- with auxiliary do, be, have, modal verbs', topic='aux_verbs subject_object_q', rx=r"\b(what|where|when|why|how|which|who)\b", d=0)
P('aux_mix', 'Choosing the helping verb across tenses: do, did, be, have', 'A2.2', "Picks be for -ing and adjectives, do / does / did for the simple tenses and have for the third form, in questions and negatives.",
  n='q_wh pst_negq pp_form pc_form', v='q_yesno', e="*Did you seen it? Do she work here? Are you work? Have you see?*", m='49, 51', t='A2: Auxiliary verbs do, be, have', g='A2 auxiliary verbs have and do',
  topic='aux_verbs', dl='A2.2 B1.1')
P('so_neither', 'So am I, neither do I', 'A2.2', "Agrees with a positive or a negative sentence using the same helping verb: A: I'm tired. B: So am I. A: I don't smoke. B: Neither do I.",
  n='aux_mix', v='tag_basic', e="*So I am; So do I* after *I'm tired; Neither I do; Me too* after a negative; *Neither don't I*", m='51', t='A2: So am I, neither do I', g='not found in EGP', topic='new')
P('q_subject', 'Subject questions: Who called? What happened?', 'A2.2', "Asks about the doer without do / does / did and about the object with it: Who called you? Who did you call?",
  n='q_wh pst_negq', v='q_wh', e="DO: *What did happened? Who does live here? Who did call you?*; *What you want?*", m='49', t='A2: Subject questions, questions with a preposition',
  g='A2 wh- questions (subject questions not a separate EGP entry)', topic='subject_object_q', d=1)
P('q_which_subj', 'Which / What / How many + noun as the subject', 'B1.1', "Asks without do when the question phrase is the subject: Which bus goes to the centre? How many people came?",
  n='q_subject', v='q_subject', e="*Which bus does go to the centre? How many people did come?*", m='49', t='B1+: Questions: different types (from memory)', g='not a separate EGP entry',
  topic='subject_object_q', rx=r"\b(which|what|how many|how much|whose) (\w+ ){1,3}(goes|came|comes|won|wins|lives|live|costs|leaves|left|happened|makes|made|works|opened|opens|starts|started|belongs|took|takes)\b")
P('q_prep_end', 'Questions with a preposition at the end', 'A2.2', "Leaves the preposition after the verb: Who are you talking to? What are you looking at? Where are you from?",
  n='q_wh dep_basic', v='rel_prep', e="*To who are you talking? About what are you thinking? Who are you waiting?*", m='49', t='A2: Subject questions, questions with a preposition', g='A2 preposition stranding',
  topic='subject_object_q dep_prepositions', rx=r"\b(to|at|for|about|with|from|on|in|of)\?")
P('q_negative', "Negative questions: Don't you …? Why didn't you …?", 'B1.2', "Shows surprise, checks or suggests with a negative question, and answers about the fact: Don't you like it? Why don't we go?",
  n='q_wh', v='tag_basic', e="*Why you didn't call? Do not you like it?*; answering *Yes* to mean agreement with the negative", m='49', t='B1+: Questions: different types', g='B1 negative questions with be, auxiliary verbs, modal verbs', topic='new')
P('tag_basic', "Question tags: isn't it? don't you? did she?", 'B1.1', "Adds a tag with the opposite sign and the right helping verb and pronoun: You like tea, don't you? She isn't here, is she?",
  n='aux_mix', v='so_neither', e="*You like tea, isn't it? She isn't here, isn't she? He went home, doesn't he?*", m='52', t='B1: Question tags', g='A2 question tags (limited); B1 affirmative + negative, negative + affirmative',
  topic='question_tags', d=1, s='The app has tasks from A2.2')
P('tag_special', "Special tags: aren't I? shall we? will you? nobody … they", 'B1.2', "Uses the tags that do not follow the simple rule: I'm late, aren't I? Let's go, shall we? Nobody called, did they?",
  n='tag_basic', v='tag_basic', e="*I'm late, amn't I? Let's go, will we? Nobody called, didn't he? Nothing happened, didn't it?*", m='52', t='B1: Question tags', g='B2 tags with imperatives; C1 tags with there + be',
  topic='question_tags', rx=r"aren't I|shall we|will you|nobody|no one|nothing|everybody|everyone|somebody|let's|never|hardly|there (is|are|was|were)")
P('aux_uses', 'Auxiliaries: emphasis, echo questions, avoiding repetition', 'B1.2', "Uses the helping verb alone: I do like it! A: I've lost my keys. B: Have you? I think so. I hope not.",
  n='aux_mix so_neither', v='ellipsis', e="*I think yes; I hope no; A: I've lost my keys. B: Did you?; I do liked it*", m='51', t='B1+: Auxiliary verbs: different uses', g='B1 imperative do, emphasis; C1 past simple: emphasis with did', topic='new')
P('iq_wh', 'Indirect questions with a question word: Could you tell me where … is?', 'B1.2', "Asks politely with statement word order and no do: Could you tell me where the station is? Do you know what time the shop opens?",
  n='q_wh requests', v='q_wh rep_q_wh', e="Q-ORDER: *Could you tell me where is the station? Do you know what time does the shop open?*", m='50', t='B1+: Indirect questions', g='A2 indirect questions with Do you know + how / where / why / what',
  topic='ind_polite', d=1, s='Level: test-english B1+, EGP A2; the app starts at B1.1')
P('iq_yn', 'Indirect yes / no questions: Do you know if …?', 'B1.2', "Uses if or whether for a yes / no question inside another: Do you know if she is at home? I wonder whether it's open.",
  n='iq_wh', v='rep_q_yn', e="IND-YESNO: *Do you know is she at home? Can you tell me do you live here? I wonder does she know*", m='50', t='B1+: Indirect questions', g='B1 wonder, reported thought',
  topic='ind_polite', rx=r"\b(if|whether)\b")
P('iq_to', "Question word + to: I don't know what to do", 'B1.2', "Shortens a question about what somebody should do: I don't know what to do. Can you show me how to use it?",
  n='vp_to q_wh', v='iq_wh', e="Q-ORDER: *I don't know what should I do; I don't know what do; Show me how use it*", m='54', t='no line of its own (A2: Infinitives and gerunds; B1: Gerund or infinitive)', g='not a separate EGP entry',
  topic='ind_advanced', rx=r"\b(what|how|where|when|which|who) (\w+ )?to \w+", s='The app has it at B2.2 only')
P('iq_whether', 'Whether: after prepositions, with to, with or not', 'B2.1', "Uses whether, not if, after a preposition, before to + verb and with or not: It depends on whether the budget is approved. I can't decide whether to accept.",
  n='iq_yn iq_to', v='iq_yn', e="*It depends on if; I can't decide if to accept; It depends whether or no*", m='50', t='B1+: Indirect questions (from memory)', g='C2 whether or not, formal',
  topic='ind_advanced', rx=r"\bwhether\b|\bif\b", d=1)
P('iq_subject', 'A question clause as the subject: Why the system failed remains unclear', 'B2.2', "Starts a formal sentence with an embedded question and keeps statement order in it: How the funds were spent is not known. Whether he will come is unclear.",
  n='iq_whether', v='iq_wh', e="*Why did the system fail remains unclear; If he will come is unclear*", m='', s='Not in Murphy EGiU; no line in the lists (the app teaches it at B2.2)', t='no line in the lists', g='C1 what cleft clause as subject (the nearest EGP entry)',
  topic='ind_advanced', rx=r"^(put the words|which sentence|choose|complete|rewrite|correct)?.{0,60}\b(whether|why|how|what|where|when|who) .{3,60} (is|was|remains|depends|matters|has)\b.*(unclear|unknown|known|investigat|mystery|decided|important|matter|certain|seen)")
P('whoever', 'Whatever, whoever, whenever, wherever, however', 'B2.1', "Says 'it does not matter what / who / when': Whatever you decide, I'll help. Come whenever you like. Whoever arrives last washes up.",
  n='rel_obj', v='rel_what', e="*Whomever arrives last; Whatever you will decide; Whatever do you decide*", m='', s='Not a Murphy EGiU unit', t='B1+: Whatever, whenever…', g='C1 whatever, wherever, however as subordinating conjunctions',
  topic='ind_advanced', rx=r"\b(who|what|when|where|how|which|whom)ever\b", s2='Level: test-english B1+, EGP C1')
