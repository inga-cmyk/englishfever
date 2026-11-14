# Grammar map data, part 1: present, past, perfect, future.
# P(id, name, level, can_do, n=needs, v=contrasts, e=typical errors, m=Murphy units (5th ed., checked against the contents list),
#   t=line in LEVEL-LISTS-test-english.md, g=English Grammar Profile (checked in the EGP Online table, 13 Nov 2026),
#   topic=app topic id(s) or 'new', rx=pattern that sorts the topic's tasks to this point, d=1 the topic's default point, s=other source note)
from lib import P, AREA

AREA('Present')
P('be_pres', 'Be: am / is / are', 'A2.1', 'Says who or what somebody is, how they feel and where they are; makes the negative and the question by moving or negating be.',
  e='BE: *I really happy*; *Do you tired?* for *Are you tired?*', m='', s='Not in Murphy EGiU (intermediate); Essential Grammar in Use units 1-2 (from memory, not checked)',
  t='A1: Present simple of be', g='A1 (be + complement; negation of main verb be)', topic='new')
P('ps_form', 'Present simple: I work, she works', 'A2.1', 'Talks about habits, routines and facts; adds -s / -es / -ies for he, she, it.',
  v='be_pres pc_form', e='3S: *She work here*; BE-VERB: *I am agree, I am live in Riga*', m='2', t='A1: Present simple', g='A1 (affirmative; habits and general facts)',
  topic='present_simple', d=1)
P('ps_negq', "Present simple: don't / doesn't, Do / Does …?", 'A2.1', 'Makes negatives and questions with do / does and keeps the main verb in the base form.',
  n='ps_form', v='be_pres', e="DO: *You like coffee? I not like it*; BASE: *She doesn't likes, Does she works?*", m='2', t='A1: Present simple',
  g='A1 negative; A2 questions', topic='present_simple', rx=r"\b(don't|doesn't|do not|does not)\b|^(do|does)\b|\b(do|does) (you|he|she|it|they|we|your|the|my|his|her)\b|negative|make a (yes/no )?question|make it a question")
P('pc_form', 'Present continuous: am / is / are + -ing', 'A2.1', 'Says what is happening at the moment of speaking, with negatives, questions and short answers; spells the -ing form.',
  n='be_pres', v='ps_form', e="BE: *I working now, She is work*; short answer *Yes, I'm*", m='1', t='A1: Present continuous', g='A1 affirmative, events in progress; A2 negative, questions',
  topic='present_continuous', d=1)
P('ps_pc', 'Present simple or continuous: habit or now', 'A2.1', 'Chooses between a habit (every day, usually) and an action in progress (now, at the moment, Look!).',
  n='ps_negq pc_form', v='ps_form pc_form', e='NOW-HABIT: *Look! It rains. I am going to the gym every day*', m='3', t='A1: Present simple or continuous; A2: Present simple vs present continuous',
  g='A1-A2 (both forms)', topic='present_simple present_continuous', rx=r"every (day|week|morning|evening|year|month|summer|sunday|monday|friday|saturday)|usually|at the moment|right now|\bnow\b|look!|listen!|today")
P('pc_temp', 'Present continuous: temporary situations and changes', 'A2.2', 'Talks about something temporary around now (this week, these days) and about a change in progress (is getting better).',
  n='ps_pc', v='ps_form', e='NOW-HABIT: *I work from home this week* for a temporary situation', m='1, 3', t='A2: Present simple vs present continuous',
  g='A2 temporary situations; B1 temporary repeated actions', topic='present_continuous', rx=r"this (week|month|year|term|summer)|these days|at present|for a few (days|weeks)|temporar|more and more|getting (better|worse|colder|warmer|more|bigger|harder|dark)|going up|increasing|changing")
P('stative', 'State verbs stay simple: know, like, want, need', 'A2.2', 'Uses the simple form with verbs of knowing, liking, wanting and needing, also for something true right now.',
  n='ps_pc', v='pc_form', e='STATE-ING: *I am knowing, I am wanting, I am needing help*', m='4', t='A2: Stative vs dynamic verbs', g='A2 mental process verbs with the present simple',
  topic='present_continuous present_simple', rx=r"state verb|\b(know|knows|want|wants|need|needs|believe|believes|understand|understands|belong|belongs|prefer|prefers|agree|agrees|mean|means|remember|hate|hates|own|owns|seem|seems)\b.*(right now|now|at the moment)|am (knowing|wanting|needing|liking|understanding)|is (knowing|wanting|needing)|are (knowing|wanting|needing)|stāvokļa")
P('stative2', 'Verbs with two meanings: think, have, see, taste, be', 'B1.1', "Chooses simple or continuous by meaning: I think it's good (opinion) / I'm thinking about it (considering); She has a car / She's having lunch; He's being rude.",
  n='stative', v='stative pc_temp', e='*I am thinking it is a good idea*; *I have a shower* for now', m='4', t='B1: Present simple or present continuous', g='B1 mental process verbs',
  topic='present_continuous present_simple', rx=r"\b(think|thinking|thinks)\b.*(opinion|consider)|opinion|is having|are having|am having|is being|are being|is seeing|am seeing|tastes|is tasting|smells|is smelling|looks .*(appear)|have = |= own")
P('pc_always', "Always + continuous: an annoying habit", 'B1.2', "Shows irritation about something that happens too often: He's always losing his keys.",
  n='pc_temp', v='ps_form', e='*He always loses his keys!* is correct but neutral; the continuous adds the annoyance', m='3', t='B1: Present simple or present continuous (from memory); returns in C1: Advanced present simple and continuous',
  g='A2 present continuous with adverbs of indefinite frequency (form only)', topic='present_continuous', rx=r"(am|is|are|'s|'re|'m) (always|constantly|forever) \w+ing|annoy|irritat|complain")
P('have_got', 'Have got and have', 'A2.1', "Talks about possession with have got / have; makes the negative and question of each (I haven't got / I don't have).",
  n='be_pres ps_negq', v='ps_negq', e="*Do you have got? I haven't a car*; *I'm having a car*", m='17', t='A1: Have got', g='A2 (auxiliary have; have got to)',
  topic='aux_verbs', rx=r"have got|has got|haven't got|hasn't got|got a|got any")
P('imperative', "The imperative: Open the door. Don't worry. Let's go.", 'A2.1', "Gives instructions, directions and suggestions with the base form, don't + base form and let's.",
  e="*Don't to worry; No smoke here; Let's to go*", m='', s='Not a Murphy EGiU unit', t='A1: The imperative', g="A2 affirmative, negative, let's", topic='new')
P('would_like', "Would like: I'd like …, Would you like …?", 'A2.1', 'Asks for things and offers them politely; follows would like with a noun or to + verb.',
  n='ps_negq', v='vp_like_ing', e="*I would like go; Do you like a coffee?* as an offer; *I like to order* for *I'd like to order*", m='37, 58', t="A1: Would you like…? I'd like…",
  g='A1 would like: wishes, invitations', topic='new')
P('there_is', 'There is / are, there was / were', 'A2.1', 'Says that something exists or is somewhere; chooses is or are by the noun; asks Is there…? Are there…?',
  n='be_pres', v='there_it', e='IT-THERE: *In my town is a park. There is two cafés. It is a park near here*', m='84', t='A1: There is / are, there was / were',
  g='A1 there is, there are; A2 + uncountable, a lot of', topic='new', s='Mentioned on the agreement card (there is + one, there are + more than one)')
P('there_it', 'There or it', 'A2.1', "Uses there to introduce something new and it to talk about it again, or for weather, time and distance: There's a café. It's very good. It's cold.",
  n='there_is', v='there_is', e='IT-THERE: *Is cold today. There is cold. It is a problem with my phone*', m='84', t='A1: There or it', g='A1-A2 (there is / are)', topic='new')
P('demonstr', 'This, that, these, those', 'A2.1', 'Points at things near and far, singular and plural, before a noun or alone.',
  n='be_pres', e='*This shoes; these book; that are my friends*', m='', s='Not a Murphy EGiU unit', t='A1: This, that, these, those; A1: This or it', g='A1 determiners; A2 pronouns', topic='new')

AREA('Past')
P('was_were', 'Was / were', 'A2.1', 'Talks about where somebody was and how things were; makes negatives and questions without did.',
  n='be_pres', v='pst_negq', e='*Did you were there? I were tired. They was late*', m='5', t='A1: Was / were', g='A1 past simple affirmative (be)', topic='past_simple',
  rx=r"\b(was|were|wasn't|weren't)\b(?!.*\b\w+ing\b)")
P('pst_reg', 'Past simple: regular verbs (-ed)', 'A2.1', 'Tells about finished actions at a finished time (yesterday, last week, two days ago); spells -ed forms.',
  n='ps_form', v='ps_form', e='PAST-FORM: *Robert join us last week*; spelling *stoped, studyed*; *before two days* for *two days ago*', m='5, App. 1, App. 6', t='A1: Past simple: regular and irregular',
  g='A1 affirmative (limited range); A2 increasing range', topic='past_simple', d=1)
P('pst_irr', 'Past simple: irregular verbs', 'A2.1', 'Uses the past forms of the common irregular verbs (went, saw, had, bought, took …).',
  n='pst_reg', e='PAST-FORM: *I buyed, she goed, he taked*', m='5, App. 1', t='A1: Past simple: regular and irregular', g='A2 affirmative', topic='past_simple',
  rx=r"\b(went|saw|had|bought|took|came|got|made|gave|told|said|met|left|found|ate|drank|wrote|read|knew|thought|felt|heard|spent|lost|forgot|broke|sold|paid|ran|sat|slept|spoke|swam|taught|won|wore|flew|drove|began|brought|built|caught|chose|cost|fell|grew|kept|sent|stood|understood)\b|irregular")
P('pst_negq', "Past simple: didn't, Did …?", 'A2.1', "Makes negatives and questions with did and returns the main verb to the base form.",
  n='pst_reg ps_negq', v='was_were', e="BASE: *Did you went? I didn't saw it*; DO: *Where you went?*", m='5', t='A1: Past simple: negatives and questions', g='A2 questions, negative',
  topic='past_simple', rx=r"\bdidn't\b|\bdid not\b|\bdid\b|make a (yes/no )?question|negative")
P('used_to', 'Used to + verb: past habits and states', 'A2.2', "Talks about what was true or regular in the past and is not now; didn't use to, Did you use to…?",
  n='pst_negq', v='pst_reg be_used_to', e="*I use to get up at seven* for a present habit; *I didn't used to*; *I used to went*", m='18', t='A2: Used to',
  g="B1 (no longer true; negative didn't use to / didn't used to)", topic='used_to', d=1, s='Level: test-english A2, EGP B1 (learners use it one level later than the list teaches it)')
P('used_to_ps', 'Used to or past simple; usually for the present', 'B1.1', 'Keeps used to for repeated or lasting past situations, the past simple for one finished event, and usually + present simple for a present habit.',
  n='used_to', v='used_to pst_reg', e='*We used to go to Rome last year; I use to drink coffee every morning*', m='18', t='B1: Usually, used to, be used to, get used to', g='B1',
  topic='used_to', rx=r"usually|last (year|week|month|summer|night)|once\b|one finished|in 20\d\d|yesterday")
P('be_used_to', 'Be used to and get used to + noun / -ing', 'B1.1', "Says that something is normal for somebody now, or is becoming normal: I'm used to getting up early. You'll get used to it.",
  n='used_to vp_prep_ing', v='used_to', e="*I'm used to get up early; I used to getting up early; I'm use to it*", m='61', t='B1: Usually, used to, be used to, get used to; B1+: Used to, be used to, get used to',
  g='B1-B2 (not a separate EGP entry)', topic='used_to', rx=r"\b(am|is|are|was|were|'m|'s|'re|be|been|get|gets|got|getting) (not )?used to\b|n't used to\b.*ing|accustomed")
P('would_habit', 'Would for past habits (not states)', 'B1.2', 'Uses would + verb for repeated past actions in a story and used to for past states: We would play outside every day. I used to have a dog.',
  n='used_to', v='used_to c2', e='*I would have a dog when I was a child; I would live in Riga*', m='36', t='B1+: Would and used to; B2: Narrative tenses, used to, would', g='B2 would: habitual past',
  topic='used_to', rx=r"\bwould\b", s='On the used_to card only as a Watch out point')
P('no_longer', 'No longer, any more, any longer', 'A2.2', "Says that a situation has ended: I no longer smoke. I don't smoke any more.",
  n='ps_negq', v='still_yet', e="*I don't smoke no more; I no longer don't work there; I any more live there*", m='111', t='A2: No longer, anymore', g='B1 negation with adverbs',
  topic='used_to', rx=r"any more|anymore|no longer|any longer", s='On the used_to card only as a Watch out point')
P('pastc_form', 'Past continuous: was / were + -ing', 'A2.2', 'Says what was in progress at a time in the past: At eight I was having breakfast.',
  n='was_were pc_form', v='pst_reg', e='BE: *I was work*; *They was waiting*; STATE-ING: *I was knowing her*', m='6', t='A2: Past continuous and past simple', g='A2 affirmative, events in progress, background',
  topic='past_continuous cmp_ps_pc', d=1)
P('pastc_when', 'Past continuous with past simple: when, while', 'A2.2', 'Tells that a short action happened in the middle of a longer one: I was cooking when he called. He called while I was cooking.',
  n='pastc_form pst_irr pst_negq', v='pst_reg past_seq', e='BACKGROUND: *When you called, I watched TV*; *While I cooked, he was calling*', m='6', t='A2: Past continuous and past simple',
  g='A2 past simple with when; past continuous background events', topic='past_continuous cmp_ps_pc narrative', rx=r"\b(when|while)\b")
P('past_seq', 'One after another or in the middle? When + past simple / continuous', 'B1.1', 'Hears the difference: When Karen arrived, we had dinner (then) / we were having dinner (already started); uses the past simple for complete and repeated actions.',
  n='pastc_when', v='pastc_when pastp_form', e='*I was going there three times; We were walking home after the party* for a complete action', m='6', t='B1: Past simple, past continuous, past perfect',
  g='B1 ordering of past events; past continuous: repeated events', topic='cmp_ps_pc past_continuous', rx=r"three times|twice|many times|a lot when|complete|repeated|one after|and then|first .* then")
P('pastc_two', 'Two actions in progress; the background of a story', 'B1.1', 'Sets the scene of a story and describes two things going on at the same time: It was raining, and people were hurrying home.',
  n='pastc_when', v='pst_reg', e='*While I was cooking, he watched TV* where both were in progress', m='6', t='B1: Past simple, past continuous, past perfect', g='A2 background events; B1 past continuous: reason',
  topic='past_continuous narrative', rx=r"while .*\b(was|were)\b.*\b(was|were)\b|background|were \w+ing and|was \w+ing,? and .* (was|were) \w+ing|the sun was")

AREA('Present perfect')
P('v3', 'The third form (past participle) of regular and irregular verbs', 'A2.2', 'Knows the third form of the common verbs (done, seen, gone, written, made, built) and that regular verbs repeat -ed.',
  n='pst_irr', v='pst_irr', e='PAST-FORM: *I have went, she has saw, it was build, it is speak*', m='App. 1', t='A2: Present perfect; A2: Present and past simple passive',
  g='A2 (present perfect affirmative; passive affirmative)', topic='present_perfect present_simple_passive past_simple_passive', rx=r"3rd form|third form|past participle|irregular|\bwent\b.*gone|has went|have went|is speak|was build")
P('pp_form', 'Present perfect: have / has + third form', 'A2.2', "Forms the present perfect with negatives, questions and short answers: I've finished. She hasn't called. Have you seen it?",
  n='v3 have_got', v='pst_reg', e="*She have finished; I has seen; Did you have seen?*", m='7', t='A2: Present perfect', g='A2 affirmative, negative, questions', topic='present_perfect', d=1)
P('pp_exp', 'Present perfect for experience: ever, never, before', 'A2.2', 'Asks and tells about life experience without saying when: Have you ever been to Rome? I have never tried it.',
  n='pp_form', v='pp_ps', e="FINISHED-TIME: *I have been there in 2019*; *Did you ever be…?*; *I never have seen*", m='8', t='A2: Present perfect', g='A2 experiences', topic='present_perfect',
  rx=r"\bever\b|\bnever\b|\bbefore\b|times\b|\btwice\b|\bonce\b|experience")
P('pp_been_gone', 'Been or gone', 'A2.2', "Uses been for a visit that is over and gone for somebody who is still away: She's been to Paris. She's gone to Paris.",
  n='pp_exp', v='pp_exp', e="*He's gone to Rome twice; She's been to the shop* for somebody still out", m='7', t='A2: Present perfect', g='A2 (not a separate EGP entry)', topic='present_perfect',
  rx=r"\bgone\b.*\bbeen\b|\bbeen\b.*\bgone\b|been to|gone to|still there|came back|come back")
P('pp_just', 'Present perfect with just, already, yet', 'A2.2', "Gives news and says whether something has happened: I've just finished. She's already left. Have you eaten yet?",
  n='pp_form', v='pp_ps still_yet', e="*I already have eaten; I didn't finish yet; Have you yet eaten?*", m='7', t='A2: Present perfect', g='A2 with yet; B1 with already; B1 recent past',
  topic='present_perfect', rx=r"\bjust\b|\balready\b|\byet\b|recently")
P('pp_for_since', 'Present perfect with for and since: up to now', 'A2.2', "Says how long a state has lasted up to now: I've known her for ten years / since school; asks How long have you…?",
  n='pp_form', v='ps_form pp_ps for_since_from', e="DURATION: *I live here for 10 years. I know him since 2015. I've lived here from 2015. How long are you here?*", m='11, 12', t='A2: Present perfect; B1: For, since, from',
  g='A2 time with for; B1 duration with since; B1 unfinished', topic='present_perfect', rx=r"\bfor\b.*(year|month|week|day|hour|minute|long time|ages)|\bsince\b|how long|all my life")
P('pp_ps', 'Present perfect or past simple: is the time finished?', 'A2.2', 'Uses the past simple with a finished time (yesterday, in 2019, ago, When…?) and the present perfect when the time is not said or not finished.',
  n='pp_form pst_irr pst_negq', v='pp_form pst_reg', e='FINISHED-TIME: *I have seen him yesterday. When have you arrived? Who has invented the telephone?*', m='13, 14', t='A2: Present perfect or past simple; B1: Past simple or present perfect',
  g='A2 present perfect: experiences; past simple with time adjuncts', topic='cmp_pp_ps present_perfect past_simple', rx=r"yesterday|last (week|year|night|month|summer|weekend|monday|friday)|\bago\b|in (19|20)\d\d|\bwhen (did|have)\b|finished time", d=1)
P('pp_ps_now', 'Still true or finished? News and details; today, this week', 'B1.1', "Chooses by the link with now: I've worked here since 2010 / I worked there from 2010 to 2014; gives news in the present perfect and the details in the past simple; uses the present perfect with a period that is not over (today, this week).",
  n='pp_ps pp_for_since', v='pp_ps', e="*I've worked there from 2010 to 2014; A: I've burnt myself. B: How have you done that?; Have you seen Anna this morning?* said in the afternoon", m='13, 14',
  t='B1: Past simple or present perfect', g='B1 unfinished; recent past', topic='cmp_pp_ps present_perfect', rx=r"from (19|20)\d\d to|this (morning|week|month|year)|\btoday\b|so far|still (work|live)|not .* now|any more|news|detail|how did")
P('sup_ever', "Superlative + present perfect: the best film I've ever seen", 'B1.1', "Combines a superlative with ever and the present perfect to rank an experience.",
  n='sup pp_exp', e="*It's the best film I ever saw; the best film I've never seen*", m='8, 108', t='B1: Comparative and superlative adjectives and adverbs (from memory)', g='B1 present perfect with superlative; superlative: the best with noun and present perfect',
  topic='comparison present_perfect', rx=r"(est|most \w+|best|worst)\b.{0,40}\b(I|we|she|he|they|you)('ve|'s| have| has) ever")
P('ppc_form', 'Present perfect continuous: have been + -ing', 'B1.1', "Talks about an activity that started in the past and is still going on, with for, since and How long: I've been waiting for an hour.",
  n='pp_for_since pc_form', v='pc_form pp_form', e='DURATION: *I am waiting for an hour. How long are you learning English?*; *She has been work all day*', m='9, 11', t='B1: Present perfect simple and continuous',
  g='B1 affirmative, questions; single continuing event', topic='present_perfect_continuous present_perfect', d=1, rx=r"been \w+ing")
P('ppc_result', 'Present perfect continuous: a recent activity you can see', 'B1.1', "Explains a present situation by a recent activity: You're out of breath. Have you been running?",
  n='ppc_form', v='pp_just', e='*You are out of breath. Did you run? / Have you run?* where the activity, not its completion, is meant', m='9', t='B1: Present perfect simple and continuous', g='B2 present perfect continuous: recent past',
  topic='present_perfect_continuous', rx=r"out of breath|dirty|wet|tired because|red eyes|eyes are red|covered in|smell|result|recent activity|that's why|you look")
P('pp_ppc', 'Present perfect simple or continuous: how much or how long?', 'B1.2', "Chooses the simple form for a finished amount or result (I've read three chapters) and the continuous for the activity and its length (I've been reading all afternoon); keeps state verbs simple (I've known him for years).",
  n='ppc_form pp_just stative', v='pp_form ppc_form', e="*I've been reading three chapters. I've been knowing him for years. How long have you had been…?*", m='10, 11', t='B1: Present perfect simple and continuous; B1+: Present perfect simple or continuous',
  g='B1 present perfect continuous: repeated continuing events', topic='present_perfect_continuous present_perfect', rx=r"how (much|many)|three|four|five|six|ten|twenty|\b\d+ (emails|pages|chapters|cups|times|letters|calls)|state verb|known|had this|belonged|all (day|morning|afternoon|week)")
P('pp_first_time', "It's the first time I've …", 'B2.1', "Uses the present perfect after It's the first / second time: It's the first time I've driven a car.",
  n='pp_exp', e="*It's the first time I drive a car; It's the first time I am here*", m='8', t='no line in the lists', g='not found in EGP', topic='new', s='Standard point from Murphy unit 8; no content and no list line')
P('still_yet', 'Already, still, yet', 'B1.2', "Places and chooses the three words: She still hasn't called. He's already here. Is it ready yet? I'm still waiting.",
  n='pp_just pc_form', v='pp_just no_longer', e="*I still didn't finish* for *I still haven't finished; She yet hasn't called; He is here already?* as surprise", m='111', t='B1+: Already, still, yet',
  g='B2 present perfect with still; B1 with already', topic='new')

AREA('Past perfect and narrative tenses')
P('pastp_form', 'Past perfect: had + third form, the earlier past', 'B1.1', 'Shows which of two past actions happened first: When I got to the station, the train had left.',
  n='pp_form pst_irr', v='pst_reg pp_form', e='*When I arrived, the film has already started; She had went home; I have never seen snow before I moved*', m='15', t='A2: Past perfect; B1: Past simple, past continuous, past perfect',
  g='B1 affirmative, negative; time up to then', topic='past_perfect narrative', d=1, s='Level: test-english A2, EGP B1, the app teaches it at B1.2. See the questions for Inga')
P('pastp_order', 'Past perfect or past simple: is the order already clear?', 'B1.2', 'Uses the past simple for actions told in the order they happened and with before / after when the order is clear; keeps the past perfect for stepping back.',
  n='pastp_form', v='pastp_form pst_reg', e='*She had opened the door and had gone in; After I had breakfast I had gone to work*', m='15', t='B1: Past simple, past continuous, past perfect',
  g='B1 past simple: ordering of past events', topic='past_perfect narrative', rx=r"in the order|order they happened|one after|\band (then )?(went|left|opened|closed|sat|took|got)\b|soon afterwards|after that")
P('pastp_by', 'By the time, already, just, never … before with the past perfect', 'B1.2', 'Uses the time words that go with the earlier past: By the time we arrived, the shop had closed. I had never seen snow before.',
  n='pastp_form pp_just pp_exp', v='pp_exp', e="*By the time we arrived, the shop closed / has closed; I never saw snow before I moved*", m='15, 120', t='B1: Past simple, past continuous, past perfect', g='B1 past perfect with adverbs',
  topic='past_perfect narrative', rx=r"by the time|\bnever\b.*before|\balready\b|\bjust\b|\byet\b")
P('narr_mix', 'Narrative tenses: past simple, past continuous, past perfect together', 'B1.2', 'Tells a story with events (past simple), background (past continuous) and what had happened before (past perfect), choosing all three in one text.',
  n='pastc_two past_seq pastp_form', v='pastc_when pastp_form', e='*When I have got home, I found the door open; I didn\'t go to the cinema. I have already seen the film*', m='6, 15', t='B1: Past simple, past continuous, past perfect; B1+: Narrative tenses',
  g='B1 (all three forms)', topic='narrative', d=1)
P('pastpc', 'Past perfect continuous: had been + -ing', 'B2.1', "Says how long an activity had been going on before a moment in the past: We'd been playing for half an hour when it started to rain.",
  n='pastp_form ppc_form', v='ppc_form pastc_form', e='*When it started to rain, we have been playing for half an hour; She had been work all day; We had been knowing each other*', m='16', t='B1+: Narrative tenses; B2: Narrative tenses, used to, would',
  g='B1 affirmative, continuing events in the past; B2 negative, results', topic='narrative_b2', d=1)
P('pastpc_vs', 'Had been doing, was doing or had done?', 'B2.1', 'Chooses between an activity in progress at that moment (was doing), an activity before it (had been doing) and a finished amount before it (had done).',
  n='pastpc narr_mix pp_ppc', v='pastpc pastp_form pastc_form', e="*The ground was wet because it was raining* (it had stopped); *By lunchtime she'd been writing ten emails*", m='16', t='B2: Narrative tenses, used to, would',
  g='B2 past perfect continuous: results, background information', topic='narrative_b2', rx=r"wet|had stopped|how (much|many)|by (lunchtime|noon|then|six|the end)|\b(ten|three|five|twenty|\d+) (emails|pages|calls|reports)|was \w+ing or|wasn't \w+ing|were \w+ing")

AREA('Future')
P('will_form', "Will / won't + verb: predictions and what I think will happen", 'A2.1', "Talks about the future with will and won't, often after I think / I'm sure / probably; asks Will you…?",
  n='ps_form', v='going_to', e="MODAL: *I will to help; It will rains; She wills*; *I think I won't* for *I don't think I'll*", m='21, 22', t='A1: Will and shall', g='A1 affirmative; A2 negative, questions; B1 predictions',
  topic='future', d=1)
P('shall', 'Shall I …? Shall we …?', 'A2.1', 'Offers help and suggests doing something together: Shall I open the window? Shall we go?',
  n='will_form', v='will_now', e='*Will I open the window?* as an offer; *Shall we to go?*', m='21, 22', t='A1: Will and shall', g='A2 offers and suggestions with shall', topic='future', rx=r"\bshall\b")
P('going_to', 'Be going to: plans and intentions', 'A2.1', "Says what somebody has decided to do: I'm going to visit my aunt this weekend; negatives and questions.",
  n='be_pres', v='will_form', e="BE: *She going to call you; I'm going visit; I going to*", m='20', t='A1: Be going to', g='A2 affirmative, questions, intentions', topic='future', rx=r"going to")
P('will_now', "Will for a decision made now: offers, promises, requests", 'A2.2', "Reacts at the moment of speaking: I'm thirsty. I'll have some water. I'll help you. I won't tell anyone.",
  n='will_form', v='going_to fut_arr', e="FUTURE: *I call you tomorrow* as a promise; *I'm going to answer it* as an instant decision; *I help you*", m='21, 23', t='A2: Will vs be going to',
  g='A2 willingness, offers; requests with will', topic='future', rx=r"decid|promise|offer|\bI'll (help|get|carry|open|call|answer|have|take|pay|do it|show|lend)\b|instant|at the moment of speaking|just now")
P('will_going', 'Will or going to', 'A2.2', "Chooses going to for a plan made before and for a prediction from what we can see now (Look at those clouds. It's going to rain), will for a decision made now and for what we think.",
  n='will_now going_to', v='will_now going_to', e="*I will visit my aunt this weekend* for an existing plan; *Look out! You will fall* with present evidence", m='23', t='A2: Will vs be going to', g='A2 going to: intentions, predictions; B1 will: predictions',
  topic='future', rx=r"look at|look out|clouds|evidence|already decided|decided (last|yesterday|before)|plan made")
P('fut_arr', 'Present continuous for arrangements', 'A2.2', "Talks about a fixed arrangement with a time and usually other people: I'm meeting Anna at six tomorrow.",
  n='pc_form', v='going_to will_now', e="FUTURE: *I meet Anna tomorrow at six; I will meet the dentist at ten* for an appointment", m='19', t='A2: Present continuous for arrangements', g='A2 future arrangements',
  topic='future present_continuous', rx=r"arrange|appointment|(am|is|are|'m|'s|'re) (meeting|seeing|flying|leaving|having|coming|going|playing|visiting|starting|moving|taking)\b.*(tomorrow|tonight|next|on (friday|monday|saturday|sunday|tuesday|wednesday|thursday)|at \d|this (evening|weekend|afternoon))")
P('fut_timetable', 'Present simple for timetables and programmes', 'B1.1', 'Uses the present simple for a fixed timetable: The train leaves at 7.15. The film starts at eight.',
  n='ps_form fut_arr', v='fut_arr', e="*The train will leave at 7.15* for a timetable; *I leave tomorrow* for a personal plan", m='19', t='B1: Future forms (from memory)', g='A2 present simple: timetables and plans',
  topic='present_simple future', rx=r"timetable|(train|bus|flight|plane|film|concert|lesson|class|course|shop|museum|match|meeting|ferry|show|conference|exam) (leaves|starts|begins|opens|closes|arrives|departs|ends|finishes|lands|takes off)|what time does")
P('fut_time_clause', 'Future time clauses: when, as soon as, until, before, after + present', 'A2.2', "Keeps the present simple after the time word when talking about the future: I'll call you when I arrive.",
  n='will_form ps_form', v='c1 if_when', e="TIME-CLAUSE: *When I will come home, I'll call you. I'll wait until she will come*", m='25', t='A2: First conditional and future time clauses; B1: First conditional, future time clauses',
  g='A2 present simple with when; B1 with as soon as', topic='time_clauses future conj_linkers', rx=r"\b(when|as soon as|until|till|before|after|once)\b", d=1)
P('when_done', "When I do or when I've done; if and when", 'B1.2', "Uses the present perfect after when / after / as soon as / until to show that one action will be complete first: I'll call you when I've finished.",
  n='fut_time_clause pp_form', v='fut_time_clause', e="*When I will have finished; I'll call you when I finished*", m='25', t='B1+: When I do / when I have done', g='not found in EGP', topic='time_clauses',
  rx=r"(when|after|as soon as|until|once) (I|you|he|she|we|they)('ve|'s| have| has)\b")
P('fut_mix', 'Future forms: choosing among will, going to, present continuous, present simple', 'B1.1', 'Chooses the right future form in one conversation: plan, arrangement, timetable, prediction, instant decision.',
  n='will_going fut_arr fut_timetable', v='will_going fut_arr', e='FUTURE: one form (will, or the present) for every future meaning', m='19, 20, 21, 22, 23', t='B1: Future forms', g='B1 (all forms)', topic='future',
  dl='B1.1 B1.2')
P('fut_cont', 'Future continuous: will be doing', 'B1.2', "Says what will be in progress at a future time: This time tomorrow I'll be flying to Rome.",
  n='will_form pc_form', v='will_form fut_perf', e="*This time tomorrow I will fly; I will be fly; I will flying*", m='24', t='B1+: Future continuous and future perfect', g='A2 affirmative with will; B1 negative; B2 questions, politeness', topic='new')
P('fut_perf', 'Future perfect: will have done', 'B2.1', "Says what will be complete before a future time: By Friday I'll have finished the report.",
  n='will_form pp_form', v='fut_cont', e="*By Friday I will finish* where completion before then is meant; *I will have finish; Until Friday I'll have finished*", m='24', t='B1+: Future continuous and future perfect',
  g='B2 affirmative, negative; events completed in the future', topic='new', s='Level: the B1+ list covers B1.2-B2.1; EGP B2, so the second half')
P('fut_perf_cont', 'Future perfect continuous: will have been doing', 'B2.2', "Says how long something will have lasted at a future time: In May I'll have been working here for ten years.",
  n='fut_perf ppc_form', v='fut_perf', e="*In May I will work here for ten years; I'll have been work*", m='', s='Not in Murphy EGiU; Hewings, Advanced Grammar in Use (from memory, not checked)', t='B2: Future forms (from memory)',
  g='B2 affirmative, negative; looking back from a point in the future', topic='new')
P('about_to', 'Be about to, be due to, be to', 'B2.1', 'Talks about the immediate future (about to), a scheduled event (due to) and an official arrangement or instruction (is to).',
  n='going_to', v='going_to fut_timetable', e="*I'm about leaving; The train is due arrive; I'm about to leave tomorrow*", m='', s='be about to is in Murphy Appendix 3 (from memory); be due to / be to are not in EGiU',
  t='B2: Be about to, be due to', g='B2 be about to, be due to, be to', topic='future', rx=r"about to|due to|\b(is|are|was|were) to\b")
P('fut_past', 'Future in the past: was going to, would, was about to', 'B2.1', "Talks about a plan or expectation seen from a past moment: I was going to call you, but I forgot. I knew it would rain.",
  n='going_to pastc_form', v='going_to pastc_form', e="*I was going to called; I thought it will rain; I knew he is going to be late*", m='20', t='B2: Future in the past', g='B1 be going to, would: future in the past; B2 be about to, be on the point of',
  topic='past_continuous', rx=r"(was|were|wasn't|weren't) going to", s='On the past_continuous card (form line and Watch out). Level: test-english B2, EGP B1')
P('likely_bound', 'Likely, bound, sure to; probably and definitely with will', 'B2.1', "Says how sure a future event is: She's likely to win. It's bound to rain. He'll probably come. He probably won't come.",
  n='will_form', v='deduction', e="*She is likely win; It's probably that; He won't probably come; It is bound raining*", m='', s='Not a Murphy EGiU unit', t='B1+: Likely, bound, probably',
  g='B2 be likely to: probability; be bound to: certainty; be sure / certain to', topic='new')
