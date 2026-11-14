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
    # Typed gaps with nothing in the sentence that fixes the tense name it (teacher's decision, 25 October)
    for id, q in (('ps-A21-3a', 'Use the present simple: My brother ___ football. (not / like)'),
                  ('ppf-B12-3a', 'Use the past perfect: She was upset because she ___ her phone. (lose)'),
                  ('pac-A22-3b', 'Use the past continuous: ___ you ___ at 6 pm? (work)')):
        fix_again(id, 'Name the tense: another tense would also be correct in this sentence.', q=q)
    fix_again('fu-A21-3b', 'A correct answer that was not accepted: a decision about the coat can also be going to.',
        answers=[["'ll take", 'will take', "'m going to take", 'am going to take']])
    # Latvian read-through (25 October): wording that was wrong, stiff or did not match the English
    LVFIX = {
        'cf-B12-4a': '*Unless you hurry* nozīmē *if you do not hurry*, tāpēc brīdinājums paliek tāds pats: tu nokavēsi. Pārējie teikumi maina to, kam jāsteidzas, vai to, kas notiks.',
        'pac-A22-2a': '*At nine* ir brīdis pagātnē. Past Continuous rāda, kas tad norisinājās.',
        'pac-B11-5a': 'Pēkšņai īsai darbībai, kas pārtrauc citu darbību, lieto Past Simple.',
        'pp-B11-5a': '*I have lost my keys* uzsver pagātnes notikuma saistību ar tagadni. Past Simple apraksta pagātnes notikumu; arī to konteksts var saistīt ar pašreizējo problēmu.',
        'fu-A22-3b': 'Jau sarunāts plāns: *are going* (*to*).',
        'fu-B11-2a': 'Present Continuous ar laiku rāda fiksētu vienošanos.',
        'fu-B11-5a': 'Vienošanās ar laiku bieži izsaka ar Present Continuous.',
        'pc-A22-1a': 'Pagaidu situācija šobrīd: *am/is/are* + darbības vārds ar *-ing*.',
        'pc-B11-3a': 'Tendence mūsdienās: *are* + darbības vārds ar *-ing*.',
        'psp-B11-5a': 'Ciešamā kārta uzmanību patur uz darbību, un cilvēks nav minēts.',
        'psp-B12-5a': 'Ciešamā kārta novirza uzmanību uz datiem.',
        'fup-B11-5a': 'Ciešamā kārta patur uzmanību uz failiem.',
        'pasp-B12-5a': 'Ciešamā kārta neuzsver, kas darbību veica, un skan neitrālāk.',
    }
    for id, lv in LVFIX.items():
        fix_again(id, 'Latvian wording corrected after a read-through.', why_lv=lv)
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
    fix('rq-B12-1a', 'Learners did not understand "report"; use the usual instruction (teacher, 27 October).',
        q="Choose the correct option: 'Where do you work?' She asked me ___.")
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
    # Full placement test report (25 October): an option whose report was right but whose reason was wrong made the question ambiguous
    fix_again('rs-B21-2a', 'Ask for the reason only, so no option has a correct report with a wrong reason.',
        q="'The Earth goes round the Sun,' the teacher said. Why can we report it as 'The teacher said the Earth goes round the Sun'?",
        correct='Because it is still true.',
        wrong=['Because said is in the past.', 'Because reported speech never changes the tense.', 'Because goes is an irregular verb.'],
        why='When a fact is still true, the tense does not have to go back: *The teacher said the Earth goes round the Sun.*')
    fix_again('rs-B12-4a', 'The explanation must not make the answer look arguable.',
        why='Only this sentence keeps *will*. With backshift it is: *She said she would call me the next day.*',
        why_lv='Tikai šajā teikumā paliek *will*. Ar laiku saskaņošanu tas ir: *She said she would call me the next day.*')
    # Teacher's feedback (27 October): ask about the meaning, not the name of the conditional type
    fix_again('cz-B11-2a', 'Ask about the meaning, not the name of the type.', q='Which sentence is about something that is always true?')
    fix_again('cf-B11-1b', 'Ask about the meaning, not the name of the type.', q='Which sentence about a possible future is correct?')
    fix_again('cm-B21-1a', 'Ask about the meaning, not the name of the type.', q='Which sentence imagines a different past with a result now?')
    fix_again('cm-C11-1a', 'Ask about the meaning, not the name of the type.', q='Which sentence without *if* is correct?')
    fix_again('cz-B11-1a', 'Ask about the meaning, not the name of the type.', q="Which word can replace 'if' here? 'If it rains, the street floods.'")
    # Teacher (27 October): "a suitable reporting verb" makes clear that the learner chooses the verb
    fix_again('rv-C11-6a', 'Say that the learner chooses a suitable verb.', q="Report with a suitable reporting verb. 'It wasn't me who broke it!' said Leo.")
    fix_again('rv-C12-3a', 'Say that the learner chooses a suitable verb.', q="Report with a suitable reporting verb: 'You really should see a doctor about that cough,' my sister said.")
    fix_again('rv-C12-6a', 'Say that the learner chooses a suitable verb.', q="Report with a suitable reporting verb and a noun phrase: 'Thank you for everything you've done,' Mia said to the team.")
    # Learners' answers (26 October): cards without a question mark also make a correct statement
    fix_again('ip-B11-3b', 'Without a question-mark card the statement order is correct too.',
        answers=[['could you tell me where the station is', 'you could tell me where the station is']])
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
    # what to do is not the same as what she should do (teacher, 28 October): no task may say they mean the same
    report_fix('rq-B22-1a',
        why="A reported question has statement word order, so *what should he do* is wrong. The report *what to do* is correct here; *what he should do* is also possible.")
    report_fix('rq-B22-2a',
        q="'Where should I park?' she asked me. Which report is correct?",
        correct='She asked me where she should park.',
        wrong=['She asked me where should she park.', 'She asked me where she should to park.', 'She asked me where does she should park.'],
        why='Statement word order after the question word: *where she should park*. *I* becomes *she*, because she asks about herself.')
    report_fix('rq-B22-3a',
        answers=[['They asked where they should meet.', 'They asked where to meet.']],
        why='Statement word order: *where they should meet*. They ask about themselves, so *we* becomes *they*.')
    # no "she said" after the quote (teacher, 29 October); congratulate was 70% wrong as a whole typed sentence, now only the key part
    # reported 31 October: no speaker tag, no grammatical wrong option, no guessed he; the polite question says what to ask
    report_fix('rv-C11-5a',
        q="Which sentence reports this: 'I'm very sorry for the delay, and I will make sure it never happens again.'",
        wrong=['The manager apologised the delay and promised that it would not happen again.',
               'The manager apologised for the delay and promised to that it would not happen again.',
               'The manager apologised for the delay and promised it not happening again.'])
    # open writing tasks that gave the answer away (teacher, 3 November): write_fixes.py
    import write_fixes
    for _id, _ch in write_fixes.FIX.items():
        _base = re.sub(r'-r\d+$', '', _id)   # by_id holds the original ids; the item may already be a later revision
        if _base in by_id: report_fix(_base, **_ch)
    # reported 3 November: plain wording, wrong options that are wrong, a writing task that does not give the form away
    report_fix('pc-A21-2a', q='Which sentence is about this moment?')
    report_fix('pc-A21-5a', q='Choose the correct question.', wrong=['What do you doing now?', 'What you are doing now?', 'What are you do now?'])
    report_fix('pc-A21-6a', q='Look around you. Write two sentences about what is going on around you at the moment.',
        must=[["\\b(am|is|are|'m|'s|'re)\\s+\\w+ing\\b", "Use *am / is / are* + verb-ing, for example: *My neighbour is cutting the grass.*",
               "Lieto *am / is / are* + darbības vārds ar *-ing*, piemēram: *My neighbour is cutting the grass.*"]],
        model='I am sitting at my desk. My neighbour is cutting the grass.')
    report_fix('ip-B21-5a', q="Which is the polite way to ask this: 'When will my order be delivered?'")
    report_fix('rv-C12-1a', q="Which sentence reports this: 'If I were you, I'd take the earlier train.'")
    report_fix('rv-C11-3a',
        q="Complete the report of 'Well done on winning the award, Jo!': I congratulated Jo ___ the award. (win)",
        answers=[['on winning']], hints=[],
        why='*congratulate* + person + *on* + -ing.')
    # options of equal length, one theme, no near-duplicate pair (teacher, 3 November; option_fixes.py)
    from option_fixes import FIX as _OPT
    for _id, _ch in _OPT.items():
        report_fix(_id, **_ch)
    # teacher, 3 November: a meaning question that the context gives away becomes a form task; options about one theme, the same length;
    # an instruction without a term the learner may not know; a report whose missing words were already in the quote
    report_fix('ca-C12-2a',
        q="I wish you ___ clicking your pen. It's driving me mad.",
        correct='would stop', wrong=['will stop', 'would stopping', 'to stop'], wrong_why={},
        why='*wish* + *would* + base form: something someone keeps doing that annoys us.')
    report_fix('ps-B11-2a',
        q='Water ___ at 100 degrees Celsius.',
        correct='boils', wrong=['boil', 'boiling', 'is boil'], wrong_why={},
        why='A general fact: present simple, *-s* after *he / she / it*: *Water boils at 100 °C.*',
        why_lv='Vispārīgs fakts: Present Simple, aiz *he / she / it* galotne *-s*: *Water boils at 100 °C.*')
    report_fix('ia-C12-3a',
        q="Write one sentence that starts with *Who…*: It doesn't matter who calls. Don't answer.",
        answers=[["Whoever calls, don't answer.", 'Whoever calls, do not answer.']])
    report_fix('rv-C11-3a',
        q="'Congratulations, Jo! You finally passed the exam!' I congratulated Jo ___ passing the exam.",
        kind='gap', answers=[['on']], bank=['on', 'about', 'at', 'with'], hints=[],
        why='*congratulate* + person + *on* + -ing: *I congratulated Jo on passing the exam.*')
    # Teacher reports, 4 November: test language in context, not terminology.
    report_fix('ip-B12-2a',
        q='Could you tell me ___?', correct='where the station is',
        wrong=['where is the station', 'where does the station be', 'where the station it is'],
        why='After *Could you tell me*, use *where the station is*. Do not turn the second part into a separate question.',
        why_lv='Pēc *Could you tell me* lieto *where the station is*. Otrajā daļā neveido atsevišķu jautājumu.', wrong_why={}, wrong_why_lv={})
    report_fix('cm-C11-1a',
        q='Choose the sentence that keeps the meaning: I did not take that job, so I am not rich now.',
        correct='Had I taken that job, I would be rich now.',
        wrong=['Had I taken that job, I would have been rich then.',
               'Had I not taken that job, I would be rich now.',
               'Were I rich now, I would have taken that job.'],
        why='The past decision has a result now: *Had I taken* + *I would be rich now*. The other options change the time or reverse the situation.',
        why_lv='Pagātnes lēmumam ir sekas tagad: *Had I taken* + *I would be rich now*. Pārējie varianti maina laiku vai apgriež situāciju.', wrong_why={})
    report_fix('rq-B21-2a',
        q="Which sentence reports this instruction: 'Don't touch that!'",
        wrong=['The nurse told me not touch it.', 'The nurse told me not touching it.', 'The nurse said me not to touch it.'],
        why='*told me not to touch*: after *told*, name the person, then use *not to* + base form.',
        why_lv='*told me not to touch*: pēc *told* nosauc cilvēku un lieto *not to* ar pamatformu.', wrong_why={})
    report_fix('rs-B21-1a',
        q="Which sentence reports this: 'I might be late.'",
        correct='She said she might be late.',
        wrong=['She said she might was late.', 'She said she might to be late.', 'She said she might been late.'],
        why='*might* stays the same in the report and is followed by *be*: *She said she might be late.*',
        why_lv='Atstāstījumā *might* nemainās; pēc tā lieto *be*: *She said she might be late.*', wrong_why={})
    report_fix('ia-C11-2a',
        q='The decision depends on ___ the budget is approved.', correct='whether',
        wrong=['if', 'that', 'unless'],
        why='After *on*, use *whether*: *depends on whether the budget is approved*.',
        why_lv='Pēc *on* lieto *whether*: *depends on whether the budget is approved*.', wrong_why={}, wrong_why_lv={})
    # No grammar terms in the task (teacher, 6 November; docs/task-drafts/pending/term-free-review.md and term-free-batch1-review.md):
    # the context or a start makes the form necessary; a second correct form gets its own note (answer_notes)
    report_fix('ps-B11-1a', q='Choose the correct option: Sorry, I ___ the answer.', correct="don't know", wrong=['am not knowing', 'not know', "doesn't know"],
        why="*know* (to have the answer in your head) is not used with *-ing*: *I don't know*.", why_lv="*know* (zināt) nelieto ar *-ing*: *I don't know*.", wrong_why={}, wrong_why_lv={})
    report_fix('pa-A22-2a', q='Which words fit: I visited my aunt ___.', wrong=['already, yet, just, so far', 'now, at the moment, right now', 'always, usually, never'], wrong_why={}, wrong_why_lv={})
    report_fix('pa-B11-2a', q='Which sentence says that she first opened the door and then walked in?')
    report_fix('pp-B12-2a', q='Choose the correct option: I ___ the film last night.', correct='saw', wrong=['have seen', "'ve seen", 'was see'],
        why='*Last night* is a finished time, so *saw*.', why_lv='*Last night* ir pabeigts laiks, tāpēc *saw*.', wrong_why={}, wrong_why_lv={})
    report_fix('psp-A22-2a', q='Which sentence says that people grow rice in Asia, without saying who?')
    report_fix('psp-B12-2a', q="Which sentence says the same as 'People often call him Mo'?")
    report_fix('pasp-A22-2a', q='Which sentence says that someone broke the window, without saying who?')
    report_fix('ppp-B11-2a', q="Which sentence says the same as 'They have finished the project'?")
    report_fix('fup-B12-2a', q="Which sentence says the same as 'They will announce the winner tomorrow'?")
    report_fix('rv-B22-1a', q="Which sentence correctly reports 'I'm sorry I'm late'?")
    report_fix('rv-B22-2a', q='Match each sentence with the word that says what the person did.')
    report_fix('ia-C11-1a', q='Choose the correct option: ___ remains unclear.', correct='Whether he will attend', wrong=['Will he attend', 'Whether will he attend', 'That will he attend'],
        why='A question inside a sentence has the order of a statement: *Whether he will attend* remains unclear.',
        why_lv='Jautājumam teikuma iekšienē ir apgalvojuma vārdu secība: *Whether he will attend* remains unclear.', wrong_why={}, wrong_why_lv={})
    report_fix('psp-B11-3b', q='Start with *Fresh bread*: They sell fresh bread here.')
    report_fix('psp-B12-3b', q='Start with *The rooms*, and do not say who: Someone cleans the rooms daily.')
    report_fix('pasp-B11-3b', q='Start with *My wallet*: Someone stole my wallet.')
    report_fix('pasp-B12-3b', q='Start with *Twenty new workers*: The company hired 20 new workers last year.')
    report_fix('ppp-B11-3b', q='Start with *My bag*: Someone has stolen my bag.')
    report_fix('ppp-B12-3b', q='Start with *The invoice*: They have already sent the invoice.')
    report_fix('fup-B11-3b', q='Start with *The shop*: They will open the shop at 9.', answers=[['The shop will be opened at 9.', 'The shop will open at 9.']],
        answer_notes=[['The shop will open at 9.', 'Correct English too, but it means the shop opens (its opening time). *Will be opened* says that someone will open it.',
                       'Arī pareiza angļu valoda, bet tas nozīmē, ka veikals atveras (darba laiks). *Will be opened* pasaka, ka kāds to atvērs.']])
    report_fix('fup-B12-3b', q='Start with *The tickets*: We will send the tickets by email.')
    report_fix('cs-B12-3a', q="Imagine it is different. Start with *If I*: I don't have enough money, so I can't buy a new laptop.")
    report_fix('ct-B21-3a', q="Imagine it happened differently. Start with *If I*: I didn't see the sign, so I parked there and got a fine.")
    report_fix('cm-B22-3a', q="Imagine the past was different, and say how things would be now. Start with *If he*: He didn't take the job, so he isn't living in Paris now.")
    report_fix('rs-B12-1a', q="'I have finished the report,' he said. Later he found more mistakes in it. Report it: He said he ___ finished the report.")
    report_fix('rs-B12-4a', q='All these people spoke to you last week. Which report is NOT correct?')
    report_fix('rq-B12-3a', q="Report it: 'What time does the film start?' → She asked what time the film ___. (start)", answers=[['started', 'starts']],
        answer_notes=[['starts', 'Correct too when the film has not started yet: the time is still true now.', 'Arī pareizi, ja filma vēl nav sākusies: laiks joprojām ir patiess.']])
    # batch 2 without grammar terms (teacher, 6 November; docs/task-drafts/term-free-batch2-review.md)
    report_fix('ps-A21-3a', q='My brother ___ football. He never watches it. (not / like)')   # without a time word "didn't like" would also fit
    report_fix('pac-A22-3a', q='When I arrived, they ___ TV. They were in the middle of a film. (watch)')
    report_fix('pac-A22-3b', q="I called you at 6 pm, but you didn't answer. ___ you ___? (work)")
    report_fix('ppf-B12-3a', q='She was upset because she ___ her phone. (lose)', answers=[['had lost', "'d lost", 'lost']],
        answer_notes=[['lost', 'Correct too in everyday speech. *Had lost* makes it clear that she lost it before she was upset.',
                       'Ikdienas runā arī pareizi. *Had lost* skaidri pasaka, ka viņa to pazaudēja, pirms bija bēdīga.']])
    # batch 3 without grammar terms (teacher, 6 November; docs/task-drafts/term-free-batch3-review.md)
    report_fix('rv-C12-2a', q="'I'm not going to tell you who did it,' the officer said. Which word says what he did?")
    report_fix('ct-B12-5a', q='A colleague forgot to save a file and lost two hours of work. Choose the correct comment about what could have been different.')
    report_fix('pac-A22-1a', q='At 8 o\'clock yesterday I was in the middle of making dinner. At 8 o\'clock I ___ dinner.')
    report_fix('pac-B11-1a', q='Choose the option that shows the walk was already going on: I ___ along the street when I saw an old friend.')
    report_fix('ppc-B11-1a', q="I'm tired and I'm still at my desk. I ___ all day.")
    report_fix('ct-B22-1a', q="Imagine the past was different: 'If she ___ the warning, she ___ the accident.'")
    report_fix('cz-A22-1a', q='This is always true: If you heat ice, it ___.', wrong=['melted', 'melting', 'is melt'], wrong_why={}, wrong_why_lv={})
    report_fix('rs-B11-1a', q="'I am tired,' she said last night. Now she feels fine. Report it: She said she ___ tired.")
    report_fix('rs-B12-2a', q="'I'll call you tomorrow, I'm busy now,' Ann said last week. When you report it a week later, what happens to *tomorrow* and *now*?")
    report_fix('ppp-B11-5a', q="You want to tell a colleague the news: the email is sent, and you don't say who sent it. Which sentence?",
        correct='The email has just been sent.', wrong=['The email was just send.', 'The email will be sent.', 'The email is sending.'], wrong_why={}, wrong_why_lv={})
    report_fix('pc-A22-3a', q="Ask about someone's plans: What ___ this weekend? (you / do)", answers=[['are you doing', 'will you do']],   # one gap: the two words go together
        answer_notes=[['will you do', 'Correct too. *Are you doing* asks about plans that are already made.', 'Arī pareizi. *Are you doing* jautā par plāniem, kas jau ir sarunāti.']])
    report_fix('pc-B11-3a', q='These days more people ___ from home. (work)', answers=[['are working', 'work']],
        answer_notes=[['work', 'Correct too. *Are working* stresses that this is a change happening these days.', 'Arī pareizi. *Are working* uzsver, ka tās ir pārmaiņas, kas notiek tagad.']])
    report_fix('ppc-B11-3a', q='She started six months ago and she still goes to class. She ___ Spanish for six months. (learn)', answers=[['has been learning', 'has learned', 'has learnt']],
        answer_notes=[['has learned', 'Correct too. *Has been learning* stresses that it is still going on.', 'Arī pareizi. *Has been learning* uzsver, ka tas joprojām turpinās.'],
                      ['has learnt', 'Correct too. *Has been learning* stresses that it is still going on.', 'Arī pareizi. *Has been learning* uzsver, ka tas joprojām turpinās.']])
    report_fix('ppp-B11-3a', q="Sorry, you can't buy one now. All the tickets ___. (sell)", answers=[['have been sold', 'are sold']],
        answer_notes=[['are sold', 'Correct too: *are sold* describes the situation now; *have been sold* says that it has happened.', 'Arī pareizi: *are sold* apraksta situāciju tagad; *have been sold* pasaka, ka tas ir noticis.']])
    report_fix('pp-B12-3b', q='I ___ in three countries in my life, so I speak a little of each language. (live)', answers=[['have lived', 'lived']],
        answer_notes=[['lived', 'Correct too. *Have lived* links that experience with now: you speak the languages now.', 'Arī pareizi. *Have lived* saista šo pieredzi ar tagadni: valodas tu runā tagad.']])
    report_fix('ps-B11-3a', q='Look at the ticket: our flight ___ at 6.40 tomorrow morning. (leave)', answers=[['leaves', 'is leaving', 'will leave']],
        answer_notes=[['is leaving', 'Correct too. For a timetable we usually say *leaves*.', 'Arī pareizi. Par sarakstu parasti saka *leaves*.'],
                      ['will leave', 'Correct too. For a timetable we usually say *leaves*.', 'Arī pareizi. Par sarakstu parasti saka *leaves*.']])
    report_fix('fup-B12-3a', q="Don't worry. Everything ___ before the guests arrive. (prepare)")
    report_fix('fup-B11-3a', q='Next Friday the results ___. (announce)', answers=[['will be announced', 'are going to be announced']])
    report_fix('ppf-B12-3c', q='Join with *After*, and show which came first: I finished work. Then I went home.',
        answers=[['After I had finished work, I went home.', 'I went home after I had finished work.', 'After I finished work, I went home.']],
        answer_notes=[['After I finished work, I went home.', 'Correct too: *after* already shows the order; *had finished* makes it even clearer.', 'Arī pareizi: *after* jau parāda secību; *had finished* to pasaka vēl skaidrāk.']])
    report_fix('rv-B22-3a', q="Report it with *deny*. Max said: 'I didn't take your phone.'")
    report_fix('rv-C12-3a', q="Say what my sister did, in one sentence. My sister said to me: 'You really should see a doctor about that cough.'")
    report_fix('ip-B11-6a', q='Ask a colleague politely where the meeting room is. Start with *Could you tell me* or *Do you know*.')
    report_fix('ip-B12-6a', q='Ask a stranger politely if the café takes cards. Start with *Do you know* or *Could you tell me*.')
    report_fix('ip-B21-6a', q='Ask very politely, in one sentence, when the report will be ready.')
    report_fix('rv-C12-6a', q="Say what Mia did, in one sentence, without her words in quotes. Mia said to the team: 'Thank you for everything you've done.'")
    report_fix('rv-C11-6a', q="Say what Leo did, in one sentence, without his words in quotes. Leo said: 'It wasn't me who broke it!'")
    report_fix('cm-C11-6a', q='Write one sentence about a decision in your past and how your life would be different today. Start with *Had I*.')
    report_fix('ia-C11-6a', q='Write a sentence that starts with *The question is whether*, *The question is how* or *The question is why*.')
    report_fix('pp-B12-6a', q='Write two sentences: say that you have been to a place (no time), then say when you went there.')
    report_fix('ppc-B12-6a', q='Write two sentences about this week: something you have been doing (it is still going on), and something you have finished.')
    # Phone screenshots and 27 reports, 7 November: explicit situations, no accidental option clues.
    report_fix('ps-A22-2a',
        q='Which sentence gives a scheduled departure, rather than a hope, a past event or an action happening now?',
        correct='The train leaves at 7.45 tomorrow, according to the timetable.',
        wrong=['We hope the train will leave at 7.45 tomorrow.', 'The train left at 7.45 yesterday, according to the records.', 'The train is leaving at 7.45 right now; I can see it.'],
        why='A timetable gives a fixed departure time: *The train leaves at 7.45 tomorrow*. A hope is not a timetable.',
        why_lv='Saraksts nosaka atiešanas laiku: *The train leaves at 7.45 tomorrow*. Cerība nav sarakstā noteikts laiks.')
    report_fix('fu-B12-6a',
        q='Look at those dark clouds. Your friend has no umbrella. Write two sentences: say what is about to happen, then offer to lend your umbrella.',
        model="It is going to rain. I'll lend you my umbrella.",
        why='The clouds support a prediction: *It is going to rain*. *I will lend you my umbrella* offers help now.',
        why_lv='Mākoņi pamato prognozi: *It is going to rain*. *I will lend you my umbrella* ir palīdzības piedāvājums tagad.')
    # Learner-answer audit, 8 November: unrestricted clause order and a valid
    # possession negative. Preserve published originals under their earlier IDs.
    report_fix('cf-B12-3a',
        answers=[["Unless you practise, you won't improve.", "Unless you practice, you won't improve.",
                  "You won't improve unless you practise.", "You won't improve unless you practice.",
                  "You will not improve unless you practise.", "You will not improve unless you practice."]],
        why='*Unless* means *if not*. The unless-clause can come before or after the main clause.',
        why_lv='*Unless* nozīmē *if not*. Palīgteikums ar *unless* var būt pirms vai pēc virsteikuma.')
    report_fix('ps-B11-3b',
        answers=[["She doesn't have any money.", "She does not have any money.",
                  "She hasn't any money.", "She has not any money.",
                  "She hasn't got any money.", "She has not got any money."]],
        why='For possession, both *does not have any money* and *has not got any money* are correct negatives.',
        why_lv='Runājot par to, kas kādam ir, pareizi noliegumi ir gan *does not have any money*, gan *has not got any money*.')
    # Word banks with real forms (teacher, 8 November, batch 2): wrong chips are real forms that do not fit
    report_fix('cs-B11-3b', bank=['were', 'would', 'am', 'will'])
    # Draft of 11-12 November (reports, speaker tags, situations), approved by the teacher on 12 November; read by a second reader
    BS_EN = ('After a past reporting verb (*said, told, asked*) the tense goes one step back (*am → was, will → would, have done → had done*). '
             'This is always correct. While something is still true, the present is also heard in everyday English, but here we practise the rule.')
    BS_LV = ('Pēc atstāstījuma darbības vārda pagātnē (*said, told, asked*) laiks iet soli atpakaļ (*am → was, will → would, have done → had done*). '
             'Tas vienmēr ir pareizi. Kamēr kaut kas joprojām ir patiess, sarunvalodā dzird arī tagadni, bet šeit mēs trenējam likumu.')
    def opt_that(*xs):
        out = []
        for x in xs: out += [x, 'that ' + x]
        return out
    report_fix('ppc-B11-5a', q="Your friend is out of breath, but she isn't running now. Why is she out of breath?",
        correct='She has been running.', wrong=['She is running.', 'She runs.', 'She has run.'], wrong_why={}, wrong_why_lv={},
        why='*Has been running*: an activity that has just stopped and explains how she is now. *Has run* is for a finished result (*She has run 10 km*).',
        why_lv='*Has been running*: darbība, kas nupat beigusies un izskaidro, kāda viņa ir tagad. *Has run* lieto pabeigtam rezultātam (*She has run 10 km*).')
    report_fix('fu-B11-5a', q="'Are you free this evening?' 'Sorry, ___ Anna at 6. We booked a table yesterday.'",
        correct="I'm meeting", wrong=["I'll meet", 'I meet', "I've met"],
        why='An arrangement made earlier, with a time: present continuous (*I\'m meeting*). *I\'ll meet* is a decision made now; *I meet* is for timetables.',
        why_lv='Iepriekš norunāta lieta ar laiku: Present Continuous (*I\'m meeting*). *I\'ll meet* ir lēmums runāšanas brīdī; *I meet* lieto sarakstiem un grafikiem.',
        wrong_why={"I'll meet": '*will* is for a decision made now; this was arranged yesterday.'},
        wrong_why_lv={"I'll meet": '*will* lieto lēmumam šajā brīdī; šis tika norunāts vakar.'})
    report_fix('pa-A21-3b', q='Make a yes/no question: He played football.')
    report_fix('fu-A21-3c', q='Make a yes/no question: You are going to travel by train.')
    report_fix('rs-B11-1a', q="Last night Anna said: 'I am tired.' Now she feels fine. → Anna said she ___ tired.")
    report_fix('rs-B11-3a', q="Ten years ago Mark said: 'I don't like coffee.' Now he drinks it every day. → Mark said he ___ coffee. (not / like)")
    report_fix('rs-B11-5a', q="Last month Jon said: 'I can't come to the meeting.' In the end, he came. Which sentence reports Jon's words?")
    report_fix('rs-B12-1a', q="On Monday Tom said: 'I have finished the report.' Later he found mistakes in it. → Tom said he ___ finished the report.")
    report_fix('rs-B12-2a', q="Last week Ann said: 'I'm busy now. I'll call you tomorrow.' When you report it a week later, what happens to *tomorrow* and *now*?")
    report_fix('rs-B12-5a', q="Yesterday the team said: 'We are almost ready.' Today the work is finished. Which sentence reports the team's message to you?")
    report_fix('rs-B21-2a', q="The teacher's words: 'The Earth goes round the Sun.' Why can we report them as 'The teacher said the Earth goes round the Sun'?")
    report_fix('rs-B21-5a', q="Last week the client said: 'I won't sign it until the lawyer reads it.' Yesterday he signed it. Which sentence reports the client's words?")
    report_fix('rq-B12-1b', q="Which sentence reports the guard's request: 'Please wait here.'")
    report_fix('rq-B21-1a', q="Anna's question to you: 'Can you help me?' Which sentence reports it?")
    report_fix('rq-B21-5a', q="Which sentence reports the customer's question: 'How long will the repair take?'")
    report_fix('rq-B22-1a', q="Tom's question to you: 'What should I do?' Which sentence reports it?")
    report_fix('rq-B22-2a', q="Eva's question to you: 'Where should I park?' Which sentence reports it?")
    report_fix('rv-B22-5a', q="Which sentence reports Sam's answer: 'No, I won't work this weekend.'")
    report_fix('rv-C12-2a', q="The officer's words: 'I'm not going to tell you who did it.' Which word says what the officer did?")
    report_fix('rv-C12-5a', q="Which sentence reports the customer's words in formal English: 'The service was terrible.'")
    # typed reports: the quote and the start are shown, the learner completes it (kind gap)
    report_fix('rs-B11-6a', kind='gap', q="'I'm learning Spanish.' → Elena said ___.", answers=[opt_that('she was learning Spanish')], hints=[], must=[], model=None, why=BS_EN, why_lv=BS_LV)
    report_fix('rs-B12-3a', kind='gap', q="Yesterday at five: 'I'm leaving now.' → Kate said ___.",
        answers=[opt_that('she was leaving', 'she was leaving then', 'she was leaving at that moment', 'she was leaving right then')], why=BS_EN, why_lv=BS_LV)
    report_fix('rs-B21-3a', kind='gap', q="'You must finish by Friday.' → My boss told me ___.",
        answers=[opt_that('I had to finish by Friday', 'I must finish by Friday', 'I would have to finish by Friday')],
        answer_notes=[['I would have to finish by Friday', 'Correct too: *would have to* looks at the obligation from that moment in the past.',
                       'Arī pareizi: *would have to* skatās uz pienākumu no šī brīža pagātnē.']])
    report_fix('rq-B21-3a', kind='gap', q="'Could you send me the invoice?' → Lena asked me ___.",
        answers=[['to send her the invoice', 'if I could send her the invoice', 'whether I could send her the invoice']])
    report_fix('rq-B22-3a', kind='gap', q="'Where should we meet?' → They asked me ___.",
        answers=[['where they should meet', 'where we should meet', 'where to meet']])
    report_fix('rq-B22-6a', kind='gap', q="'Is the data accurate?' → The editor asked me ___.",
        answers=[['whether the data was accurate', 'whether the data were accurate', 'if the data was accurate', 'if the data were accurate']], hints=[], must=[], model=None,
        why='A yes/no question is reported with *whether* or *if* and statement word order: *whether the data was accurate*.',
        why_lv='Jā/nē jautājumu atstāsta ar *whether* vai *if* un apgalvojuma vārdu secību: *whether the data was accurate*.')
    report_fix('rv-B22-6a', kind='gap', q="'Sorry I forgot the meeting.' → Dana apologised ___.",
        answers=[['for forgetting the meeting', 'for having forgotten the meeting', 'for forgetting about the meeting', 'to me for forgetting the meeting', 'to me for forgetting about the meeting']], hints=[], must=[], model=None,
        why='*apologise for* + *-ing*: *apologised for forgetting the meeting*.', why_lv='*apologise for* + *-ing*: *apologised for forgetting the meeting*.')
    report_fix('rs-B11-2a', q='Match what she said with the sentences that start "She said".',
        pairs=[["'I work in a bank.'", 'She said she worked in a bank.'], ["'I'm working in a bank.'", 'She said she was working in a bank.'],
               ["'I will work in a bank.'", 'She said she would work in a bank.'], ["'I have worked in a bank.'", 'She said she had worked in a bank.']],
        why='Reported later, each tense goes one step back: *work → worked, am working → was working, will work → would work, have worked → had worked*.',
        why_lv='Atstāstot vēlāk, katrs laiks iet soli atpakaļ: *work → worked, am working → was working, will work → would work, have worked → had worked*.')
    report_fix('rv-B22-2a', q='Match each sentence with the word that says what the speaker did.',
        pairs=[["'I'll definitely be there on time.'", 'promised'], ["'Don't touch the red button!'", 'warned'], ["'Why don't we try the new café?'", 'suggested'], ["'Yes, I broke the vase.'", 'admitted']])
    # typed conditionals: one situation sentence decides the type (c-0737, 11 November)
    COULD_EN = 'Correct too: *could* = would be able to. *Would* says what you would do; *could* says what would be possible.'
    COULD_LV = 'Arī pareizi: *could* = varētu. *Would* saka, ko tu darītu; *could*, kas būtu iespējams.'
    report_fix('cs-B11-3a', q="I'm not the boss. If I ___ (be) the boss, I ___ (cancel) all Monday meetings.",
        answers=[['were', 'was'], ['would cancel', "'d cancel", 'could cancel']],
        answer_notes=[['were / could cancel', COULD_EN, COULD_LV], ['was / could cancel', COULD_EN, COULD_LV]])
    report_fix('cs-B21-3a', q='Our company will never change its fixed hours. If it ___ more flexible hours, people ___ happier. (offer / be)')
    report_fix('ct-B12-3a', q='Nobody told me about the meeting, so I missed it. If you ___ me about it, I ___ there. (tell / be)',
        answers=[['had told', "'d told"], ['would have been', "'d have been"]])
    report_fix('ct-B22-3a', q='He drove too fast just once and lost his licence. If he ___ (not / drive) so fast that day, he ___ (not / lose) it.')
    report_fix('cm-B21-3a', q="I didn't learn English at school. If I ___ it then, I ___ fluent now. (learn / be)",
        answers=[['had learned', 'had learnt', "'d learned", "'d learnt"], ['would be', "'d be"]])
    report_fix('ia-B22-3a', q='Say it shorter with *to*: Can you tell me how I can get to the museum?',
        answers=[['Can you tell me how to get to the museum?']],
        why='*how* + *to* + base form: *how to get*.', why_lv='*how* + *to* + pamatforma: *how to get*.')
    # Reports of 13 November: a short instruction; the time word decides the form (teacher: context only where the form depends on it)
    report_fix('pa-B11-5a', q='Choose the correct option: I ___ my report last March.', correct='finished', wrong=['have finished', 'finish', 'am finishing'],
        why='*last March* is a finished time: past simple *finished*.', why_lv='*last March* ir pabeigts laiks: Past Simple *finished*.', wrong_why={}, wrong_why_lv={})
    report_fix('pa-B11-3b', answers=[['When did she move to London?', 'When did she move?']])
    # Part A of 14 November: the situation before a choice goes where only one option is possible English anyway
    # (teacher: Choose the correct option / Which sentence is correct? is enough); docs/review/choice-with-situation-2026-11-14.csv
    report_fix('cf-A22-5a', q='Which sentence is correct?')
    report_fix('cf-B11-5a', q='Your friend keeps forgetting his password. Choose the correct option.')
    report_fix('cf-B11-1b', q='Which sentence is correct?')
    report_fix('cm-B21-5a', q='Which sentence is correct?')
    report_fix('cm-C11-5a', q='Which sentence is correct?')
    report_fix('cs-B11-5a', q='Which sentence is correct?')
    report_fix('cs-B12-5a', q='Which sentence is correct?')
    report_fix('cs-B21-5a', q='Which sentence is correct?')
    report_fix('ct-B21-5a', q='Which sentence is correct?')
    report_fix('ct-B22-5a', q='Which sentence is correct?')
    report_fix('cz-B11-5a', q='Which sentence is correct?')
    report_fix('fup-B12-5a', q='Which sentence is correct?')
    report_fix('ia-B22-5a', q='Which sentence is correct?')
    report_fix('ia-C12-5a', q='Which sentence is correct?')
    report_fix('ip-B12-5a', q='Which sentence is correct?')
    report_fix('ip-B21-5a', q='Which sentence is correct?')
    report_fix('pac-B11-5a', q='Choose the correct option: I was walking home. Suddenly a dog ___ out of the garden.')
    report_fix('pac-B12-5a', q='Which sentence is correct?')
    report_fix('ppf-B12-5a', q='Which sentence is correct?')
    report_fix('pasp-A22-5a', q='Which sentence is correct?')
    report_fix('pasp-B11-5a', q='Which sentence is correct?')
    report_fix('pc-A22-5a', q='You are in Riga for one month only. Which sentence is correct?')
    report_fix('ppp-B11-5a', q='Tell a colleague the news: the email is now sent. Which sentence is correct?')
    report_fix('rq-B12-5a', q='Which sentence is correct?')
    report_fix('rq-B22-5a', q='Which sentence is correct?')
    # Part B of 14 November: correct answers that were refused (docs/review/typed-one-answer-2026-11-14.csv, after a second reader)
    report_fix('pp-B11-3a', q='My grandparents ___ married for 50 years, and they still go dancing together. (be)')
    report_fix('cf-B11-3b', answers=[['arrive', 'have arrived', "'ve arrived"]], answer_notes=[['have arrived', 'Correct too: *have arrived* = after you have arrived. Not *will* after *when / as soon as*.', 'Arī pareizi: *have arrived* = kad būsi ieradies. Pēc *when / as soon as* nelieto *will*.']])
    report_fix('fup-B12-3a', answers=[['will be prepared', 'will have been prepared', 'is going to be prepared']], answer_notes=[['will have been prepared', 'Correct too: *will have been prepared* = ready before they arrive.', 'Arī pareizi: *will have been prepared* = viss būs gatavs, pirms viesi ieradīsies.'], ['is going to be prepared', 'Correct too: *be going to* = it is the plan.', 'Arī pareizi: *be going to* = tā ir ieplānots.']])
    report_fix('psp-A22-3b', q='These cars ___ in Germany, and they are sold all over the world. (build)')
    # A rebuild must not allocate new IDs to unchanged published corrections.
    # Some earlier passes choose an unused revision before the final wording is
    # known; reuse the recorded final version when its content is identical.
    for it in items:
        base = re.sub(r'-r\d+$', '', it['id'])
        content = {k: v for k, v in it.items() if k != 'id'}
        same = [p for p in published.values()
                if re.sub(r'-r\d+$', '', p['id']) == base
                and {k: v for k, v in p.items() if k != 'id'} == content]
        if same:
            it['id'] = max(same, key=lambda p: int(re.search(r'-r(\d+)$', p['id']).group(1)) if re.search(r'-r(\d+)$', p['id']) else 1)['id']
    return items
