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
    return items
