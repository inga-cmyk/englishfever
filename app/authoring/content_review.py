"""Reviewed corrections to the original bank.

Applied after legacy translations/italics. Original source IDs remain stable;
every changed learner-facing item receives a new, explicit revision ID.
Reasons are exported in docs/question-bank-update.md. Do not reuse a published
revision ID when changing its content: increment it and retain the ledger.
"""
from copy import deepcopy

REASONS = {}


def revise(original):
    items = deepcopy(original)
    by_id = {i['id']: i for i in items}

    def fix(id, reason, **changes):
        it = by_id[id]
        it.update(changes)
        it['id'] = id + '-r2'
        REASONS[id] = (REASONS[id] + ' ' + reason) if id in REASONS else reason

    fix('ps-B11-1a', 'Distinguish continuous verb forms from gerunds such as knowing.',
        q='Which verb is normally NOT used in a continuous tense when it describes a state of knowledge?',
        why='When *know* describes knowledge, we normally use a simple tense: *I know the answer*, not *I am knowing the answer*.',
        why_lv='Ja *know* apzīmē zināšanas, parasti lieto vienkāršo laiku: *I know the answer*, nevis *I am knowing the answer*.')
    fix('ps-B11-2a', 'Qualify the temperature in the general-truth example, without making the correct option stand out by length.',
        correct='Water boils at 100 degrees Celsius.')
    fix('ps-B11-4a', 'Test the state-verb rule with a verb that is never continuous, instead of a typo.',
        correct='My brother is owning a small shop.',
        why='*Own* is a state verb, so we use the present simple: *My brother owns a small shop.*',
        why_lv='*Own* ir stāvokļa darbības vārds, tāpēc lieto Present Simple: *My brother owns a small shop.*')
    fix('pc-A22-3a', 'Specify the target future form for an otherwise open completion.',
        q='Ask about a future arrangement. Use the present continuous: What ___ you ___ this weekend? (do)')
    fix('pc-A22-5a', 'State the communicative criterion rather than declaring every other tense impossible.',
        q='You are staying in Riga temporarily for one month. Which sentence best emphasises your temporary situation now?')
    fix('pc-B11-4a', 'Keep the state-verb rule (want is not used in the continuous) instead of a typo.',
        correct='She is wanting a new phone.',
        why='*Want* is a state verb, so we use the present simple: *She wants a new phone.*',
        why_lv='*Want* ir stāvokļa darbības vārds, tāpēc lieto Present Simple: *She wants a new phone.*')
    fix('pa-A22-3b', 'Anchor the gap-fill sequence in the past.',
        q='Yesterday he ___ at 7 and ___ a shower. (wake up / have)')
    fix('pa-B11-2a', 'The present perfect option can also describe sequential actions; specify the target tense.',
        q='Which sentence uses the past simple to describe two completed actions in sequence?')
    fix('pac-A22-1a', 'A past-simple event can also occur at eight; specify an action already in progress.',
        q="At 8 o'clock yesterday, dinner preparation was already in progress. Complete with the past continuous: I ___ dinner.")
    fix('pac-B11-1a', 'Make the background-action requirement explicit.',
        q='Describe the action already in progress, using the past continuous: I ___ along the street when I saw an old friend.')
    fix('pac-B11-4a', 'Past continuous can describe repeated behaviour; replace the disputed error.',
        correct='When I arrived, they was having lunch.',
        why='The subject *they* needs *were*: *When I arrived, they were having lunch.* The lunch was already in progress.',
        why_lv='Ar *they* lieto *were*: *When I arrived, they were having lunch.* Pusdienošana jau bija sākusies.')
    fix('pac-B12-2a', 'A past intention does not by itself prove that the action never happened.',
        correct='I planned to call you.',
        why='*Was going to* describes a past intention. Context tells us whether it happened: *I was going to call, but I forgot* shows that it did not.',
        why_lv='*Was going to* izsaka nodomu pagātnē. Konteksts parāda, vai tas īstenojās: *I was going to call, but I forgot* nozīmē, ka zvans nenotika.')
    fix('pp-B11-5a', 'Present perfect suggests current relevance rather than guaranteeing an unresolved problem.',
        q="You cannot open the door because your keys are missing. Which sentence most directly presents the loss as a current problem?",
        why='*I have lost my keys* presents the past loss as relevant now. The past simple reports the past event; context can also connect it to a current problem.',
        why_lv='*I have lost my keys* uzsver pagātnes notikuma saistību ar tagadni. Past Simple apraksta pagātnes notikumu; arī tam konteksts var piešķirt saistību ar pašreizējo problēmu.')
    fix('pp-B12-3b', 'Specify the intended tense where past simple is also possible.',
        q='Use the present perfect to describe life experience: I ___ in three countries, so I speak a little of each language. (live)')
    fix('ppc-B11-1a', 'Specify duration continuing to now, not an ambiguous finished past event.',
        q="I'm tired and I am still at my desk. Use the present perfect continuous: I ___ all day.")
    fix('ppc-B11-3a', 'Specify the continuous target; present perfect simple can also express duration.',
        q='Use the present perfect continuous: She ___ Spanish for six months. (learn)')
    fix('ppc-B12-4a', 'A bounded number of emails does not make continuous aspect universally impossible.',
        correct="I've been written emails all morning.",
        why='The present perfect continuous uses *have/has been + verb-ing*: *I have been writing emails all morning.* Use *written* in *I have written five emails* to focus on the result.',
        why_lv='Present Perfect Continuous veido ar *have/has been +* darbības vārdu ar *-ing*: *I have been writing emails all morning.* Formu *written* lieto, piemēram, *I have written five emails*, uzsverot rezultātu.')
    fix('ppf-B12-3c', 'After does not itself require past perfect; make the exercise requirement explicit.',
        q='Join with After. Use the past perfect for the first action and the past simple for the second: I finished work. Then I went home.',
        why='Here the exercise asks for *After I had finished work, I went home.* In ordinary English, *After I finished work, I went home* is also correct because *after* makes the sequence clear.',
        why_lv='Šajā uzdevumā jālieto *After I had finished work, I went home.* Ikdienas valodā pareizs ir arī *After I finished work, I went home*, jo *after* skaidri parāda darbību secību.')
    fix('fu-A21-3a', 'Specify going to instead of rejecting other valid future forms.',
        q='Use be going to for a plan: Tom ___ a party on Saturday. (have)')
    fix('fu-A22-5a', 'Both will and going to can predict rain; state the evidence-based criterion.',
        q='You see dark clouds. Which sentence is a prediction from what you can see now?',
        why='*It is going to rain* highlights evidence visible now. *It will rain* is also a possible prediction, but does not highlight that evidence as directly.',
        why_lv='*It is going to rain* uzsver tagad redzamās pazīmes. Arī *It will rain* var izteikt prognozi, bet neuzsver redzamo pamatojumu tik tieši.')
    fix('fu-B11-1a', 'Present continuous in an if-clause can be grammatical; use a clear distractor.',
        wrong=['will rain', 'raining', 'rain'])
    fix('fu-B12-3a', 'Make the intended promise with will explicit.',
        q="Make a promise with will: Don't worry. I ___ anyone your secret. (not / tell)")
    fix('fu-B12-3b', 'Specify going to in the open future gap.',
        q='Use be going to for a prediction based on what you see: Be careful! You ___ off that chair! (fall)')
    fix('ppp-B11-3a', 'Specify the intended passive tense.',
        q='Use the present perfect passive: All the tickets ___. (sell)')
    fix('ppp-B11-5a', 'Both past and present perfect can imply that an email is available; require the relevant reporting form.',
        q='You want to announce a completed action as news now, using the present perfect passive. Which option meets both requirements?',
        why='*The email has been sent* uses *has been + past participle* to announce completion. *The email was sent* is also grammatical, but uses the past simple.',
        why_lv='*The email has been sent* izmanto *has been +* 3. formu, lai paziņotu par paveiktu darbību. Arī *The email was sent* ir pareizs teikums, bet tajā lietots Past Simple.')
    fix('fup-B11-3a', 'Specify the target future passive.',
        q='Use will in the passive: The results ___ on Friday. (announce)')
    fix('fup-B12-3a', 'Specify the target future passive.',
        q="Use will in the passive: Don't worry. Everything ___ before the guests arrive. (prepare)")
    fix('cz-A22-1a', 'Will melt is grammatical in a future prediction; require the general-rule form.',
        q='Complete the general rule using the zero conditional: If you heat ice, it ___.')
    fix('cz-A22-2a', 'Qualify the boiling-point fact.',
        pairs=[['If you heat pure water to its boiling point,', 'it boils.'],
               ["If you don't sleep enough,", 'you feel tired.'],
               ['If the traffic light is red,', 'cars stop.'],
               ['If you mix red and blue paint,', 'you get purple.']])
    fix('cz-B11-3a', 'The instruction requires when, not whenever.',
        answers=[['When you press this button, the door opens.', 'The door opens when you press this button.']])
    fix('cf-A22-1a', 'Remove a grammatical continuous alternative from the single-answer MCQ.',
        wrong=['will rain', 'rained', 'rain'])
    fix('cf-B11-1a', 'Provide the meaning that makes unless the unique answer.',
        q='Starting now is necessary to finish on time. Complete: We will not finish on time ___ we start now.')
    fix('cf-B11-3b', 'Get at/reach at do not fit the fixed sentence.',
        answers=[['arrive']])
    fix('cf-B12-4a', 'Assess the intended meaning rather than banning negatives after unless.',
        q='Which sentence does NOT express this warning: you need to hurry to avoid being late?',
        why='*Unless you hurry* means *if you do not hurry*. Adding *not* changes the condition and loses the intended warning. A negative clause after *unless* can be grammatical when that different meaning is intended.',
        why_lv='*Unless you hurry* nozīmē *if you do not hurry*. Papildu noliegums maina nosacījumu un vairs neizsaka doto brīdinājumu. Noliegums pēc *unless* var būt pareizs, ja ir domāta cita nozīme.')
    fix('ct-B12-2a', 'A cheaper alternative does not establish that the actual price was expensive.',
        correct='We did not book earlier.',
        why='The third conditional imagines a different past. We did not book earlier, and the imagined earlier booking would have been cheaper.',
        why_lv='Third conditional izsaka iedomātu pagātnes situāciju. Mēs nerezervējām agrāk; ja būtu rezervējuši agrāk, cena būtu bijusi zemāka.')
    fix('ct-B22-1a', 'Several offered combinations are valid conditional types; identify the required meaning.',
        q="Imagine a different past using the third conditional: 'If she ___ the warning, she ___ the accident.'")
    fix('ct-B22-4a', 'Distinguish formal standard usage from informal variants.',
        q='Which sentence needs editing for standard formal written English?')
    fix('ca-C11-4a', 'Do not teach that unless can never take a negative clause.',
        q='Which sentence does NOT express this warning: we need to hurry to avoid missing the flight?',
        why='*Unless you hurry* gives the intended condition. *Unless you do not hurry* changes its meaning. The issue here is the intended warning, not a universal ban on negatives after *unless*.')
    fix('rs-B11-1a', 'Backshift is not always compulsory; explicitly request it.',
        q="Report it. Move the verb one step back: 'I am tired,' she said. → She said she ___ tired.")
    fix('rs-B12-1a', 'Make backshift a task requirement.',
        q="Use backshift. Direct: 'I have finished.' Reported: He said he ___ finished.")
    fix('rs-B12-4a', 'Unshifted will may be valid in context; test the requested reporting convention.',
        q='You are reporting past statements using backshift. Which sentence has NOT backshifted its future verb?',
        why='In this exercise, *will* backshifts to *would*. Without that instruction, keeping *will* can be possible if the promise is still relevant to the future.',
        why_lv='Šajā uzdevumā *will* jāmaina uz *would*. Citā kontekstā *will* var saglabāt, ja solījums joprojām attiecas uz nākotni.')
    fix('rs-B21-1a', 'Clarify the conventional backshift question.',
        q='Which modal normally stays in the same form when we backshift a report?',
        wrong=['can', 'will', 'may'])
    fix('rq-B12-3a', 'Require backshift instead of rejecting a contextually valid present tense.',
        q="Report with backshift: 'What time does the film start?' → She asked what time the film ___. (start)")
    fix('rv-C12-4a', 'Replace the disputed recommend + object + infinitive example.',
        correct='He recommended to reading the report carefully.',
        why='Use *recommended reading* or *recommended that I read*. *Recommended to reading* is not a grammatical verb pattern.')
    fix('ia-C11-1a', 'The original what-clause was a fused relative, not an embedded question.',
        correct='Whether he will attend remains unclear.',
        wrong=['He asked whether I would attend.', 'Will he attend the meeting?', 'We do not know whether he will attend.'],
        why='*Whether he will attend* expresses an unresolved yes/no question and is the subject of *remains unclear*. In the other statements, the embedded question is not the subject.')

    fix('ps-A21-6a', 'Accept has and common adverbs in valid present-simple writing.',
        q='Write one sentence about a daily habit of your friend or colleague. Start with He or She and use an action verb in the present simple (for example, works, goes or has breakfast).',
        must=[[r'^\s*(he|she)\s+(?:(?:usually|often|always|sometimes|never)\s+)?(?!is\b|was\b)\w+s\b',
               'Use *He* or *She* with a present-simple verb, such as *works*, *goes* or *has*.',
               'Lieto *He* vai *She* ar darbības vārdu Present Simple, piemēram, *works*, *goes* vai *has*.']])
    fix('ps-B11-6a', 'Accept written times, noon and midnight, not just digits. Say whose timetable: your own plans are not a timetable.',
        q='Write two sentences about a timetable, for example a train, a class or a shop. Use the present simple with a time, as in: The train leaves at 7.45.',
        must=[[r'\b(starts?|begins?|opens?|leaves?|ends?|finish(es)?|closes?|arrives?)\b.{0,40}\bat\s+(?:\d|[a-z])',
               'Use a timetable verb with *at* and a time, such as *at nine*, *at 9.00* or *at noon*.',
               'Lieto grafika darbības vārdu ar *at* un laiku, piemēram, *at nine*, *at 9.00* vai *at noon*.'],
              [r'[.!?]\s+\S', 'Write two sentences.', 'Uzraksti divus teikumus.']])
    for id in ('ppp-B11-6a', 'ppp-B12-6a'):
        rules = deepcopy(by_id[id]['must'])
        rules[0][0] = r"(?:\b(?:has|have)|'(?:s|ve))\s+been\s+\w+"
        fix(id, 'Accept contracted has/have been in passive writing.', must=rules)
    for id in ('fup-B11-6a', 'fup-B12-6a'):
        rules = deepcopy(by_id[id]['must'])
        rules[0][0] = r"(?:\bwill|'ll)\s+be\s+\w+"
        fix(id, 'Accept contracted will in future-passive writing.', must=rules)
    for id in ('ct-B12-6a', 'ct-B21-6a'):
        fix(id, 'Make the negative result in the model consistent with the instruction.',
            q=by_id[id]['q'].replace('use would have.', "use would have or would not have (wouldn't have)."))

    # Explain why a grammatical distractor does not meet this task's criterion.
    by_id['fu-A22-5a']['wrong_why'] = {
        'It will rain.': 'This is a possible prediction. Here *going to* highlights the visible evidence more directly.',
        'It rains.': 'The present simple normally describes a general pattern here, not this evidence-based prediction.',
        'It rained.': 'This describes past rain, not the future rain you are predicting.'}
    by_id['fu-A22-5a']['wrong_why_lv'] = {
        'It will rain.': 'Tā ir iespējama prognoze. Šajā situācijā *going to* tiešāk uzsver redzamās pazīmes.',
        'It rains.': 'Present Simple šeit parasti apraksta vispārīgu parādību, nevis šo uz redzamām pazīmēm balstīto prognozi.',
        'It rained.': 'Tas apraksta lietu pagātnē, nevis prognozēto lietu nākotnē.'}
    by_id['cz-A22-1a']['wrong_why'] = {
        'will melt': 'This can express a future prediction, but the task asks for a general rule in the zero conditional.',
        'melting': '*Melting* alone cannot be the finite verb of this clause. Use *it melts*.',
        'is melt': '*Is melt* is not a grammatical form. The general rule uses *it melts*.'}
    by_id['cz-A22-1a']['wrong_why_lv'] = {
        'will melt': 'Tas var izteikt nākotnes prognozi, bet šajā uzdevumā vajadzīgs vispārīgs noteikums ar Zero conditional.',
        'melting': '*Melting* viens pats šeit nevar būt izteicējs. Lieto *it melts*.',
        'is melt': '*Is melt* nav pareiza forma. Vispārīgajā noteikumā lieto *it melts*.'}
    by_id['rs-B11-1a']['wrong_why'] = {
        'is': '*Is* can stay when the information is still true now, but this task asks you to move the verb one step back: *was*.',
        'am': '*Am* agrees with *I*, not *she*.',
        'will be': 'This changes the statement to a future meaning; it does not backshift *am*.'}
    by_id['rs-B11-1a']['wrong_why_lv'] = {
        'is': '*Is* var saglabāt, ja informācija joprojām ir aktuāla, bet šajā uzdevumā jāveic laiku saskaņošana uz *was*.',
        'am': '*Am* lieto ar *I*, nevis *she*.',
        'will be': 'Tas maina nozīmi uz nākotni, nevis saskaņo *am* pagātnē.'}
    by_id['ct-B22-1a']['wrong_why'] = {
        'heard / would avoid': 'This is a second-conditional pattern. The task asks for an unreal past condition and past result.',
        'had heard / would avoid': 'This combines a past condition with a non-past result. The task asks for both parts to refer to the past.',
        'would have heard / had avoided': 'For the standard third conditional, put the past perfect in the if-clause and *would have + past participle* in the result.'}
    by_id['ia-C11-1a']['wrong_why'] = {
        'He asked whether I would attend.': 'The embedded question complements *asked*. The subject of the main clause is *He*.',
        'Will he attend the meeting?': 'This is a direct question, not a question embedded inside another clause.',
        'We do not know whether he will attend.': 'The embedded question complements *know*. The subject of the main clause is *We*.'}
    # Typed answers: accept every correct clause order and spelling that the instruction allows.
    def more(id, reason, extra, **changes):
        have = by_id[id]['answers'][0]
        fix(id, reason, answers=[list(have) + [a for a in extra if a not in have]], **changes)

    more('cf-B12-3a', 'Accept both clause orders and the American spelling of practise.',
         ["You won't improve unless you practise.", "You won't improve unless you practice."])
    more('cs-B12-3a', 'Accept the if-clause in second position.',
         ['I could buy a new laptop if I had enough money.', 'I would buy a new laptop if I had enough money.', "I'd buy a new laptop if I had enough money."])
    more('ct-B21-3a', 'Accept the if-clause in second position.',
         ["I wouldn't have parked there if I had seen the sign.", "I wouldn't have got a fine if I had seen the sign.",
          "I would not have got a fine if I had seen the sign.", "I wouldn't have gotten a fine if I had seen the sign.",
          "I wouldn't have been fined if I had seen the sign.", "I would not have parked there if I had seen the sign."])
    more('cm-B22-3a', 'Accept the if-clause in second position.',
         ['He would be living in Paris now if he had taken the job.', "He'd be living in Paris now if he'd taken the job."])
    fix('ct-B22-3a', "The continuous form is also correct: hadn't been driving (reported by a learner).",
        answers=[["hadn't been driving", "had not been driving", "hadn't driven", "had not driven"], ["wouldn't have lost", "would not have lost", "'d not have lost"]],
        why="Negative third conditional: *hadn't been driving* (or *hadn't driven*), then *wouldn't have lost*.")
    more('rv-C12-3a', 'Reported by a learner: suggest / recommend / advise + -ing and said / told that + should are also correct reports of this sentence.',
         ['My sister suggested seeing a doctor about that cough.', 'My sister suggested I see a doctor about that cough.', 'My sister suggested I should see a doctor about that cough.',
          'My sister recommended seeing a doctor about that cough.', 'My sister recommended I see a doctor about that cough.', 'My sister recommended I should see a doctor about that cough.',
          'My sister advised seeing a doctor about that cough.', 'My sister advised that I see a doctor about that cough.', 'My sister advised that I should see a doctor about that cough.',
          'My sister said I should see a doctor about that cough.', 'My sister said that I should see a doctor about that cough.',
          'My sister told me I should see a doctor about that cough.', 'My sister told me that I should see a doctor about that cough.'],
         why='*advise / urge / tell / encourage* + person + *to* + base verb; *recommend / suggest / advise* + *-ing* or + *that* + subject + base verb; or *said / told me* + *I should* + base verb.')
    more('rs-B21-3a', 'Accept that after said / told with must.',
         ['My boss said that I must finish by Friday.', 'My boss told me that I must finish by Friday.'])
    more('cm-C11-3a', 'Accept the inverted clause in second position.',
         ["I wouldn't be in this mess now had I listened to my accountant.", "I'd not be in this mess now had I listened to my accountant."])
    more('ia-C12-3a', 'Accept the wh-ever clause after the instruction.',
         ["Don't answer, whoever calls.", 'Do not answer, whoever calls.'])
    more('ia-C11-3a', 'Accept the noun clause as the subject.',
         ['Who made the decision is not clear.'])
    more('ps-A22-3b', 'Accept travel as well as go and get.',
         ['How does she travel to work?'])
    more('rv-B22-3a', 'Say is also a reporting verb, so the task must name the verb deny. Accept the phone.',
         ['Max denied taking the phone.', 'Max denied that he had taken the phone.', 'Max denied that he took the phone.', 'Max denied having taken the phone.'],
         q="Report with the verb deny: 'I didn't take your phone,' Max said.")
    fix('ps-B11-3a', 'The present continuous can also describe this flight; ask for the timetable present simple.',
        q='Use the present simple for a timetable: Our flight ___ at 6.40 tomorrow morning. (leave)')
    fix('pc-B11-3a', 'The present simple can also describe this habit; ask for the present continuous.',
        q='Use the present continuous: These days more people ___ from home. (work)')
    fix('pac-A22-3a', 'The past simple can also complete this sentence; ask for the past continuous.',
        q='Use the past continuous: They ___ TV when I arrived. (watch)')
    # Options must not carry the rule or the verdict: the explanation is shown after the answer.
    fix('ps-A22-5a', 'The correct option explained the rule and a wrong option said it was correct.',
        correct='He goes to the gym on Mondays.',
        wrong=['He go to the gym on Mondays.', 'He is go to the gym on Mondays.', 'He going to the gym on Mondays.'])
    fix('ps-B11-5a', 'The prompt repeats the sentence the options already show; the correct option explained the rule.',
        q='Choose the correct option.', correct="'I want a coffee.'",
        wrong=["'I'm wanting a coffee.'", "'I wanted a coffee now.'", "'I am want a coffee.'"])
    fix('ps-A22-5a', 'The prompt repeats the sentence the options already show.', q='Choose the correct option.')
    fix('pp-B12-5a', 'The prompt repeats the sentence the options already show.', q='Choose the correct option.')
    fix('pc-B11-5a', 'The correct option explained the rule.', correct='Yes, it is true.')
    fix('pac-B11-2a', 'The correct option explained the answer.', correct='Cooking.')
    fix('pp-B12-5a', 'The correct option explained the rule and a wrong option said it was correct.',
        correct='I sent the email yesterday.',
        wrong=['I have sent the email yesterday.', 'I will send the email yesterday.', 'I was sending the email yesterday.'])
    fix('ppp-B12-2a', 'The continuous option can also be news that is important now; use a clearly future distractor.',
        wrong=['The road was closed in 1999.', 'The road closes every night.', 'The road will close tomorrow.'])
    fix('cf-A22-5a', 'The options repeated the word Say and one said it was correct; they are now plain sentences.',
        correct="If I have time, I'll call you.", wrong=['If I would have time, I will call you.', 'If I had time, I will call you.', 'If I will have time, I will call you.'])
    # Reported by learners and checked by the teacher (24 October). Each is a second correction of an item that was already published, so it gets the next revision id.
    def fix_again(id, reason, **changes):
        it = by_id[id]
        it.update(changes)
        import json, os
        ledger = {x['id'] for x in json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'history', 'published_items.json'), encoding='utf-8'))}
        n = 3
        while id + '-r%d' % n in ledger: n += 1     # the next revision number that no published version uses
        it['id'] = id + '-r%d' % n
        REASONS[id] = (REASONS[id] + ' ' + reason) if id in REASONS else reason
    # Open writing (25 October audit): the checks listed too few verbs, so a correct sentence was refused.
    IRR = ("went|had|saw|did|made|took|got|came|ate|bought|met|read|wrote|drank|gave|found|was|were|slept|left|ran|swam|drove|spoke|won|felt|sat|stood|heard|said|knew|"
           "thought|brought|taught|paid|sent|told|began|lost|wore|flew|sang|woke|rang|fell|broke|chose|forgot|caught")
    rules = deepcopy(by_id['ps-A21-6a']['must'])
    rules[0][0] = r'^\s*(he|she)\s+(?:(?:\w+ly|usually|often|always|sometimes|never|also|still|just)\s+)?(?!is\b|was\b)\w+s\b'
    fix_again('ps-A21-6a', 'Accept any adverb of manner or frequency before the verb (She really enjoys ...).', must=rules)
    for id, k in (('pa-A21-6a', 0), ('pa-A22-6a', 0), ('pa-B11-6a', 1), ('pac-B11-6a', 2)):
        rules = deepcopy(by_id[id]['must'])
        rules[k][0] = r'\b(\w+ed|' + IRR + r')\b'
        fix_again(id, 'Accept more irregular past verbs (swam, drove, spoke ...).', must=rules)
    # Typed tasks: every correct answer a learner can write is accepted (teacher's request, 24 October)
    def more_again(id, reason, extra):
        have = by_id[id]['answers'][0]
        fix_again(id, reason, answers=[list(have) + [a for a in extra if a not in have]])
    R = 'A correct answer that was not accepted.'
    more('pp-B11-3b', R + ' The present perfect continuous is also correct with since.', ['How long has she been working here?'])
    fix('pac-B11-3a', R + ' Both actions can be in the past continuous or the past simple, as long as the sentence is correct.',
        answers=[['was driving', 'drove'], ['rang', 'was ringing']])
    fix('pac-B12-3b', R + ' Both verbs can be continuous or simple.',
        answers=[['were arriving', 'arrived'], ['was playing', 'played']])
    more('pasp-B11-3b', R, ['My wallet was stolen by someone.'])
    more('ppp-B11-3b', R, ['My bag has been stolen by someone.'])
    more('ppp-B12-3b', R, ['The invoice has been sent already.'])
    more('rs-B12-3a', R + ' The time word may stay or go.',
         ['Kate said she was leaving now.', 'Kate said that she was leaving now.', 'Kate said she was leaving.', 'Kate said that she was leaving.'])
    more('rq-B21-3a', R + ' would is as polite as could; the invoice may follow to her.',
         ['Lena asked me to send the invoice to her.', 'Lena asked if I would send her the invoice.', 'Lena asked whether I would send her the invoice.', 'Lena asked me if I would send her the invoice.',
          'Lena asked me whether I would send her the invoice.', 'Lena asked if I could send the invoice to her.', 'Lena asked me if I could send the invoice to her.'])
    more('ip-B12-3a', R + ' please and other polite openers.',
         ['Could you please tell me what time the museum closes?', 'Could you tell me what time the museum closes please?', 'Could you tell me, please, what time the museum closes?', 'Can you please tell me what time the museum closes?',
          'Do you happen to know what time the museum closes?', "I'd like to know what time the museum closes.", 'I was wondering what time the museum closes.', 'Would you tell me what time the museum closes?'])
    more('ip-B21-3a', R + ' please and I wonder.',
         ['Could you please tell me why the order didn\'t arrive?', 'Do you happen to know why the order didn\'t arrive?', 'I wonder why the order didn\'t arrive.', 'I was wondering why the order didn\'t arrive.',
          'Could you tell me why the order did not arrive?', 'Do you know why the order did not arrive?'])
    more_again('ia-C11-3a', R + ' unclear = not clear.', ["It's unclear who made the decision.", 'It is unclear who made the decision.'])
    fix('ps-A22-3a', 'The same sentence without a time word was also a past-simple task; add usually so only the present simple fits.',
        q='What time ___ the film usually ___? (start)')
    # Audit of the whole bank (24 October): a wrong option or card that also fitted, and the double-negative key sentence once more
    fix_again('cf-B12-4a', 'Unless you don\'t hurry is not a natural structure (as in the C1 task); ask which sentence has the same meaning, with natural options.',
        q="Which sentence means the same as: 'If you don't hurry, you will be late.'?", correct='Unless you hurry, you will be late.',
        wrong=['If you hurry, you will be late.', 'Unless you hurry, you will be on time.', 'You will be on time unless you hurry.'],
        why='*Unless you hurry* means *if you do not hurry*, so the warning stays the same: you will be late. The other sentences change who must hurry or what happens.')
    fix('pasp-B11-1a', 'When is this museum opened? is also a correct question; use a form that does not fit the singular noun.',
        wrong=['did', 'were', 'has'])
    fix('cf-B11-3a', 'Unless you finish early, we will go also fitted; use a card that cannot start the sentence.',
        bank=['If', 'Until', 'will', 'would'])
    fix('cs-B11-3b', 'If I had a cat, I would sleep all day also fitted; use a card that cannot follow if.',
        bank=['were', 'would', 'will', 'being'])
    # Guest review (24 October): context, option wording, a realistic distractor, a softer backshift explanation
    fix('ppf-B12-1a', 'Was already starting is also grammatical with another meaning; give the times so only the past perfect fits.',
        q='The film began at 7.00. We arrived at 7.15. When we arrived, the film ___ already ___.')
    fix('rs-B21-2a', 'Keep the report and the reason apart so because does not look like part of the report.',
        q="'The Earth goes round the Sun,' the teacher said. Which version is also correct?",
        correct='Report: The teacher said the Earth goes round the Sun. Reason: it is always true, so the tense can stay.',
        wrong=["Report: The teacher said the Earth went round the Sun. Reason: it must go back, because said is in the past.", "Report: The teacher said the Earth had gone round the Sun. Reason: it must go back two steps.", "Report: The teacher said the Earth goes round the Sun. Reason: this is wrong, because reported speech always changes the tense."])
    fix('ia-C11-2a', 'Replace an implausible distractor with a realistic misconception.',
        wrong=['Because whether is more polite.', 'Because the sentence is in the past.', 'Because if can only start a conditional clause, never a noun clause.'])
    fix('rs-B11-2a', 'With a past reporting verb the tense often goes one step back, but it is not always needed.',
        why='With a past reporting verb the tense often goes one step back: *work → worked, am working → was working, finished → had finished, can → could.* It is not always needed, for example when the fact is still true.',
        why_lv='Pēc darbības vārda pagātnē laiks bieži iet vienu soli atpakaļ: *work → worked, am working → was working, finished → had finished, can → could*. Tas nav vienmēr vajadzīgs, piemēram, ja fakts joprojām ir patiess.')
    # Second guest review: feedback that said too much or the wrong thing
    fix_again('cf-B12-3a', 'Unless is usually followed by a positive verb, but the feedback must not say a negative can never follow.',
        why="*Unless* means *if ... not*, so the clause after it is usually positive: *Unless you practise, you won't improve.*",
        why_lv="*Unless* nozīmē *if ... not*, tāpēc teikums aiz tā parasti ir apgalvojošs: *Unless you practise, you won't improve.*",
        hints=[["unless you don't", "*Unless* already means *if ... not*, so the verb after it is normally positive: *Unless you practise, ...*", "*Unless* jau nozīmē *if ... not*, tāpēc darbības vārds aiz tā parasti ir apgalvojošā formā: *Unless you practise*, ..."]])
    fix_again('ip-B21-3a', 'The answer contains didn\'t, so the feedback must not say no did.',
        why="Polite phrase + *why* + subject + verb in statement order: *why the order didn't arrive*, not *why didn't the order arrive*.",
        hints=[["\\bdid\\b", "In the indirect part use statement order: *... why the order didn't arrive.*"]])
    fix('pasp-B11-3a', 'The verb and the noun were the same word (film); use a verb that cannot be mistaken for a noun.',
        q='Where ___ this photo ___? (take)', answers=[['was'], ['taken']])
    fix('ct-B22-2a', 'An option that says both sentences are about the past is illogical for this question; use a reversed contrast.',
        wrong=['A is about now. B is about the past.', 'A is about the future. B is about the past.', 'There is no difference.'])
    fix_again('ct-B22-4a', 'The answer that "needs editing" was arguable and showed an ungrammatical sentence as the correct answer; ask which sentence is not correct.',
        q='Which sentence is NOT correct?',
        why="In standard written English use *had + past participle* in this if-clause: *If I had known*. *Had I known* is a correct inverted alternative. *If I'd have known* occurs informally but is not the standard form.")
    fix_again('ca-C11-4a', 'The key sentence (*Unless you don\'t hurry*) is not a common structure; ask which sentence has the same meaning, with natural options.',
        q="Which sentence means the same as: 'If you don't hurry, we will miss the flight.'?",
        correct='Unless you hurry, we will miss the flight.',
        wrong=['If you hurry, we will miss the flight.', 'Unless you hurry, we will catch the flight.', 'We will catch the flight unless you hurry.'],
        why='*Unless you hurry* means *if you do not hurry*, so the warning stays the same: we will miss the flight. The other sentences change who must hurry or what happens.')
    # Every typed-sentence task also accepts the automatic variants (auto_answers.py). A published task gets the next revision id.
    import json, os, re
    from auto_answers import extend
    published = {p['id']: p for p in json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'history', 'published_items.json'), encoding='utf-8'))}

    def next_id(i):
        m = re.match(r'^(.*)-r(\d+)$', i)
        return m.group(1) + '-r' + str(int(m.group(2)) + 1) if m else i + '-r2'
    for it in items:
        if it['kind'] != 'text':
            continue
        new = extend(it['q'], it['answers'][0])
        if new != it['answers'][0]:
            it['answers'] = [new]
            if it['id'] in published and it != published[it['id']]:
                old = it['id']
                it['id'] = next_id(old)
                REASONS[old] = (REASONS[old] + ' ' if old in REASONS else '') + 'Other correct forms are accepted: time phrase first, that or me left out, polite openers.'
    # Remaining issues from the 24 October report export. Preserve every
    # published version; these are new revisions, never historical regrades.
    def report_fix(original_id, **changes):
        it = by_id[original_id]
        old = it['id']
        it.update(changes)
        it['id'] = next_id(old)

    report_fix('ps-B11-2a',
        q='Which sentence states a general fact?',
        correct='The Earth orbits the Sun.',
        why='Use the present simple for general facts and regular processes: *The Earth orbits the Sun.*',
        why_lv='Vispārīgiem faktiem un regulāriem procesiem lieto Present Simple: *The Earth orbits the Sun.*')
    report_fix('ia-C11-3a',
        q="Combine the two sentences without changing their meaning: Who made the decision? It's not clear.",
        why="Keep the meaning of *It's not clear*. *Who* is the subject of *made*, so use *who made the decision*. *I wonder who made the decision* is grammatical but changes the main idea.")
    return items
