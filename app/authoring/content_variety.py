"""48 additional drag-and-drop tasks. IDs are explicit, never position-based.

Explanations are deliberately authored with *example* markup in both languages.
All tasks keep the existing six-category taxonomy and interaction types.
"""
ITEMS = []


def add(id, skill, level, bloom, kind, q, why, lv=None, **fields):
    item = dict(id=id, skill=skill, level=level, bloom=bloom, kind=kind, q=q, why=why, **fields)
    if lv:
        item['why_lv'] = lv
    ITEMS.append(item)


def order(id, skill, level, q, sentence, why, lv=None, alternatives=()):
    punctuated = {
        'var-cz-a22-order-01': 'If you heat butter, it melts.',
        'var-cf-a22-order-01': 'If it rains, we will stay indoors.',
        'var-cs-b11-order-01': 'If I had a car, I would drive.',
        'var-ct-b12-order-01': 'If I had left earlier, I would have caught the bus.',
        'var-cm-b21-order-01': 'If I had studied medicine, I would be a doctor now.',
        'var-ca-c11-order-01-r2': 'Had I known about the delay, I would have called you.',
    }
    question = sentence.split()[0] in {'did', 'have', 'has', 'how', 'could'}
    display = punctuated.get(id, sentence[0].upper() + sentence[1:] + ('?' if question else '.'))
    add(id, skill, level, 3, 'order', q, why, lv,
        sentence=sentence, answers=[[sentence, *alternatives]], display_answer=display)


def gap(id, skill, level, q, answers, decoys, why, lv=None):
    add(id, skill, level, 3, 'gap', q, why, lv,
        answers=[[a] for a in answers], bank=[*answers, *decoys], hints=[])


def match(id, skill, level, bloom, q, pairs, why, lv=None):
    add(id, skill, level, bloom, 'match', q, why, lv, pairs=[list(p) for p in pairs])


# Word order: one additional task in each of the 24 existing topics.
order('var-ps-a21-order-01', 'present_simple', 'A2.1',
      'Put the words in order. Start with My brother.',
      'my brother works in a hospital',
      'Use *works* with *my brother* (= *he*). Put the subject before the verb: *My brother works*.',
      'Ar *my brother* (= *he*) lieto *works*. Teikuma priekšmetu liek pirms darbības vārda: *My brother works*.')
order('var-pc-a21-order-01', 'present_continuous', 'A2.1',
      'Put the words in order. Start with They.', 'they are waiting for the bus',
      'The present continuous uses *am/is/are + verb-ing*. With *they*, use *are waiting*.',
      'Present Continuous veido ar *am/is/are* un darbības vārdu ar *-ing*. Ar *they* lieto *are waiting*.')
order('var-pa-a21-order-01', 'past_simple', 'A2.1',
      'Make a question. Start with Did and put yesterday at the end.', 'did you watch the film yesterday',
      'Past-simple questions use *did + subject + base verb*: *Did you watch*, not *Did you watched*.',
      'Jautājumā lieto *did*, teikuma priekšmetu un darbības vārda pamatformu: *Did you watch*, nevis *Did you watched*.')
order('var-pac-a22-order-01', 'past_continuous', 'A2.2',
      'Put the words in order. Start with She.', 'she was reading when the phone rang',
      '*Was reading* describes the activity already in progress. *Rang* is the past-simple event that happened during it.',
      '*Was reading* apraksta darbību, kura jau norisinājās. *Rang* ir Past Simple darbība, kas notika tās laikā.')
order('var-pp-a22-order-01', 'present_perfect', 'A2.2',
      'Ask about life experience. Start with Have you ever.', 'have you ever visited this museum',
      'Use *Have you ever + past participle* to ask about experience without naming a finished past time.',
      'Lai jautātu par pieredzi, nenorādot konkrētu pabeigtu laiku pagātnē, lieto *Have you ever* un darbības vārda 3. formu.')
order('var-ppc-b11-order-01', 'present_perfect_continuous', 'B1.1',
      'Make a duration question. Start with How long and put here at the end.', 'how long have you been waiting here',
      '*How long have you been waiting?* asks about the duration of an activity continuing to now or just finished.',
      '*How long have you been waiting?* jautā par darbības ilgumu. Darbība turpinās līdz tagadnei vai tikko beigusies.')
order('var-ppf-b12-order-01', 'past_perfect', 'B1.2',
      'Put the words in order. Start with The train.', 'the train had left before we arrived',
      '*Had left* places the departure before the past arrival. *Before* also makes the sequence clear.',
      '*Had left* parāda, ka vilciens aizbrauca pirms mūsu ierašanās pagātnē. Arī *before* skaidri norāda secību.')
order('var-fu-a21-order-01', 'future', 'A2.1',
      'Describe a plan. Start with I am going to and put tonight at the end.', 'I am going to cook dinner tonight',
      'Use *am going to + base verb* for a plan: *I am going to cook*.',
      'Plānu izsaka ar *am going to* un darbības vārda pamatformu: *I am going to cook*.')
order('var-psp-a22-order-01-r2', 'present_simple_passive', 'A2.2',
      'Make a passive sentence. Start with These bicycles.', 'these bicycles are made in Italy',
      'The bicycles receive the action. A plural subject needs *are + past participle*: *are made*.',
      'Velosipēdi saņem darbību. Daudzskaitlī lieto *are* un 3. formu: *are made*.')
order('var-pasp-a22-order-01', 'past_simple_passive', 'A2.2',
      'Make a passive sentence. Start with The window.', 'the window was broken during the storm',
      'The past passive uses *was/were + past participle*. With *the window*, use *was broken*.',
      'Pagātnes ciešamo kārtu veido ar *was/were* un 3. formu. Ar *the window* lieto *was broken*.')
order('var-pcp-b12-order-01-r2', 'present_continuous_passive', 'B1.2',
      'Describe work in progress. Start with The road and put this week at the end.', 'the road is being repaired this week',
      '*Is being repaired* is the present continuous passive. The work is in progress, and the road receives the action.',
      '*Is being repaired* ir Present Continuous ciešamajā kārtā. Darbs norisinās, un ceļš saņem darbību.')
order('var-ppp-b11-order-01', 'present_perfect_passive', 'B1.1',
      'Ask whether an action is complete. Start with Has and put yet at the end.', 'has the parcel been delivered yet',
      'A present-perfect passive question uses *has/have + subject + been + past participle*.',
      'Present Perfect ciešamās kārtas jautājumā lieto *has/have*, teikuma priekšmetu, *been* un 3. formu.')
order('var-fup-b11-order-01', 'future_passive', 'B1.1',
      'Make a future passive sentence. Start with The results.', 'the results will be announced on Friday',
      'Use *will be + past participle* for a future passive: *will be announced*. The results are the focus.',
      'Nākotnes ciešamo kārtu veido ar *will be* un 3. formu: *will be announced*. Uzmanība ir pievērsta rezultātiem.')
order('var-cz-a22-order-01', 'cond_zero', 'A2.2',
      'Make a general rule. Start with If.', 'if you heat butter it melts',
      'For this general cause-and-effect rule, both clauses use the present simple. In writing: *If you heat butter, it melts.*',
      'Šajā vispārīgajā cēloņa un seku sakarībā abās daļās lieto Present Simple. Rakstot: *If you heat butter, it melts.*')
order('var-cf-a22-order-01', 'cond_first', 'A2.2',
      'Make a first conditional. Start with If.', 'if it rains we will stay indoors',
      'Use *if + present simple* and *will + base verb* for a possible future: *If it rains, we will stay indoors.*',
      'Iespējamu nākotnes situāciju izsaka ar *if +* Present Simple un *will* ar pamatformu: *If it rains, we will stay indoors.*')
order('var-cs-b11-order-01', 'cond_second', 'B1.1',
      'Imagine a different present. Start with If I.', 'if I had a car I would drive',
      '*Had* describes an imagined present condition, not a past event here. The imagined result uses *would drive*.',
      '*Had* šeit izsaka iedomātu tagadnes nosacījumu, nevis pagātnes notikumu. Iedomāto rezultātu izsaka *would drive*.')
order('var-ct-b12-order-01', 'cond_third', 'B1.2',
      'Imagine a different past. Start with If I had.', 'if I had left earlier I would have caught the bus',
      'Use *had left* for the unreal past condition and *would have caught* for its imagined past result.',
      'Nereālu pagātnes nosacījumu izsaka *had left*, bet tā iedomāto pagātnes rezultātu — *would have caught*.')
order('var-cm-b21-order-01', 'cond_mixed', 'B2.1',
      'Link a different past decision to a present result. Start with If I had and put now at the end.',
      'if I had studied medicine I would be a doctor now',
      '*Had studied* imagines a different past decision. *Would be ... now* describes the present consequence.')
order('var-ca-c11-order-01-r2', 'cond_advanced', 'C1.1',
      'Make an inverted third conditional. Start with Had I.', 'had I known about the delay I would have called you',
      '*Had I known* means *If I had known*. Inversion removes *if* and puts *had* before the subject.')
order('var-rs-b11-order-01', 'rep_statements', 'B1.1',
      'Report a past statement using backshift. Start with She said.', 'she said that she was tired',
      'When backshift is required, *I am tired* becomes *she was tired*. *That* introduces the reported statement.',
      'Ja jāveic laiku saskaņošana, *I am tired* kļūst par *she was tired*. *That* ievada atstāstīto izteikumu.')
order('var-rq-b12-order-01', 'rep_questions', 'B1.2',
      'Make a reported yes/no question. Start with He asked me.', 'he asked me whether I needed help',
      'After *whether*, use statement word order: *I needed help*, not *did I need help*.',
      'Pēc *whether* lieto apgalvojuma vārdu secību: *I needed help*, nevis *did I need help*.')
order('var-rv-b22-order-01', 'rep_verbs', 'B2.2',
      'Report an apology. Start with She.', 'she apologised for missing the meeting',
      'The pattern is *apologise for + noun or -ing form*: *apologised for missing the meeting*.')
order('var-ip-b11-order-01', 'ind_polite', 'B1.1',
      'Make a polite indirect question. Start with Could you tell me.', 'could you tell me where the bank is',
      'Inside the indirect question, put the subject before the verb: *where the bank is*.',
      'Netiešā jautājuma daļā teikuma priekšmets ir pirms darbības vārda: *where the bank is*.')
order('var-ia-c11-order-01', 'ind_advanced', 'C1.1',
      'Use an embedded yes/no question as the subject. Start with Whether.', 'whether the plan will work remains uncertain',
      '*Whether the plan will work* is the subject of *remains uncertain*. The embedded question uses statement word order.')

# Word-bank gaps: every card is a whole answer for one slot; decoys do not
# introduce a second correct answer under the stated tense requirement.
gap('var-ps-a21-bank-01', 'present_simple', 'A2.1',
    'Use the present simple. My sister ___ here, but her friends ___ in another office.',
    ['works', 'work'], ['working', 'does'],
    '*My sister* (= *she*) needs *works*. *Her friends* (= *they*) needs the base form *work*.',
    'Ar *my sister* (= *she*) lieto *works*. Ar *her friends* (= *they*) lieto pamatformu *work*.')
gap('var-pc-a21-bank-01', 'present_continuous', 'A2.1',
    'Look! Anna ___ dinner and we ___ the table.',
    ['is cooking', 'are setting'], ['is cook', 'sets'],
    'Both actions are happening now. Use *is cooking* with *Anna* and *are setting* with *we*.',
    'Abas darbības notiek tagad. Ar *Anna* lieto *is cooking*, bet ar *we* — *are setting*.')
gap('var-pa-a21-bank-01', 'past_simple', 'A2.1',
    'Yesterday I ___ a bus and ___ to the museum.', ['took', 'went'], ['take', 'go'],
    '*Yesterday* places both events in the past. The irregular past forms are *take → took* and *go → went*.',
    '*Yesterday* norāda, ka abas darbības notika pagātnē. Neregulārās formas ir *take → took* un *go → went*.')
gap('var-pac-a22-bank-01', 'past_continuous', 'A2.2',
    'Describe two activities in progress at 9 last night: I ___ while my parents ___ TV.',
    ['was studying', 'were watching'], ['study', 'watch'],
    'Use *was* with *I* and *were* with the plural subject *my parents*. Both verbs take *-ing*.',
    'Ar *I* lieto *was*, bet ar daudzskaitļa teikuma priekšmetu *my parents* — *were*. Abiem darbības vārdiem pievieno *-ing*.')
gap('var-pp-a22-bank-01', 'present_perfect', 'A2.2',
    'I have ___ my report, but I have not sent it ___.', ['already finished', 'yet'], ['finish', 'ago'],
    '*Already* says the first action is complete. *Not ... yet* says the second action has not happened up to now.',
    '*Already* norāda, ka pirmā darbība jau ir pabeigta. *Not ... yet* nozīmē, ka otrā darbība līdz šim vēl nav notikusi.')
gap('var-fu-a22-bank-01', 'future', 'A2.2',
    'I decided yesterday: I ___ a course next month. The phone is ringing — I ___ it!',
    ['am going to start', 'will answer'], ['will to start', 'answer'],
    '*Am going to start* expresses an existing plan. *I will answer* is an offer made at the moment of speaking.',
    '*Am going to start* izsaka iepriekš pieņemtu plānu. *I will answer* ir piedāvājums, kas izteikts runāšanas brīdī.')
gap('var-psp-a22-bank-01', 'present_simple_passive', 'A2.2',
    'Use the present simple passive. This room ___ every day. The windows ___ once a month.',
    ['is cleaned', 'are washed'], ['is clean', 'are wash'],
    'Use *is* for one room and *are* for several windows. The passive needs the past participles *cleaned* and *washed*.',
    'Vienai istabai lieto *is*, bet vairākiem logiem — *are*. Ciešamajā kārtā vajadzīgas 3. formas *cleaned* un *washed*.')
gap('var-pasp-a22-bank-01', 'past_simple_passive', 'A2.2',
    'Use the past simple passive. The parcel ___ yesterday, and the documents ___ this morning.',
    ['was delivered', 'were signed'], ['was deliver', 'were sign'],
    '*The parcel* is singular, so use *was delivered*. *The documents* is plural, so use *were signed*.',
    '*The parcel* ir vienskaitlī, tāpēc lieto *was delivered*. *The documents* ir daudzskaitlī, tāpēc lieto *were signed*.')
gap('var-pcp-b12-bank-01-r2', 'present_continuous_passive', 'B1.2',
    'Use the present continuous passive. Your order ___ now, and the tables ___.',
    ['is being prepared', 'are being cleaned'], ['is preparing', 'are cleaning'],
    'The order and tables receive the actions. Use *is/are being + past participle* for passive actions in progress.',
    'Pasūtījums un galdi saņem darbības. Pašlaik notiekošai darbībai ciešamajā kārtā lieto *is/are being* un 3. formu.')
gap('var-cf-a22-bank-01', 'cond_first', 'A2.2',
    'Make a first conditional: If she ___ early, we ___ the bus.',
    ['arrives', 'will catch'], ['will arrives', 'caught'],
    'After *if*, use the present simple *arrives*. The possible future result is *will catch*.',
    'Pēc *if* lieto Present Simple formu *arrives*. Iespējamo nākotnes rezultātu izsaka *will catch*.')
gap('var-cs-b11-bank-01', 'cond_second', 'B1.1',
    'Make a second conditional about an imagined present: If I ___ more free time, I ___ a new language.',
    ['had', 'would learn'], ['have', 'will learn'],
    'For this imagined present, use *had* in the condition and *would learn* in the result. *Have/will learn* would express a different, first-conditional meaning.',
    'Iedomātam tagadnes nosacījumam lieto *had*, bet rezultātam — *would learn*. *Have/will learn* izteiktu citu nozīmi — First conditional.')
gap('var-ct-b12-bank-01', 'cond_third', 'B1.2',
    'Make a third conditional about a different past: If we ___ earlier, we ___ the train.',
    ['had left', 'would have caught'], ['left', 'would catch'],
    'The unreal past condition needs *had left*. Its imagined past result needs *would have caught*.',
    'Nereālam pagātnes nosacījumam vajag *had left*. Iedomātajam pagātnes rezultātam vajag *would have caught*.')

# Matching: distinct meanings, diagnoses and communicative purposes.
match('var-ps-a21-match-01', 'present_simple', 'A2.1', 2,
      'Match each sentence to its meaning.',
      [('I walk to work every day.', 'A regular habit.'), ('I am walking to work now.', 'An action in progress now.'), ('I walked to work yesterday.', 'A finished action yesterday.')],
      '*Every day* signals the habit here. *Am walking* describes now; *walked ... yesterday* describes a finished past event.',
      '*Every day* šeit norāda uz ieradumu. *Am walking* apraksta tagadni, bet *walked ... yesterday* — pabeigtu pagātnes notikumu.')
match('var-pc-a22-match-01', 'present_continuous', 'A2.2', 2,
      'Match each sentence to what it expresses.',
      [('I work in the office every Monday.', 'My regular routine.'), ('I am working from home this week only.', 'A temporary situation around now.'), ('I am meeting Eva at the café at six tomorrow.', 'An arrangement for tomorrow.')],
      'Time expressions help distinguish the uses. The present continuous can describe a temporary situation or a future arrangement.',
      'Laika norādes palīdz atšķirt nozīmes. Present Continuous var aprakstīt pagaidu situāciju vai norunātu nākotnes darbību.')
match('var-pa-a22-match-01', 'past_simple', 'A2.2', 1,
      'Match each base verb to its past-simple form.',
      [('bring', 'brought'), ('choose', 'chose'), ('leave', 'left'), ('meet', 'met')],
      'These verbs are irregular: *bring → brought*, *choose → chose*, *leave → left*, *meet → met*. Do not add *-ed*.',
      'Šie darbības vārdi ir neregulāri: *bring → brought*, *choose → chose*, *leave → left*, *meet → met*. Nepievieno *-ed*.')
match('var-pac-b12-match-01', 'past_continuous', 'B1.2', 4,
      'Compare the verb forms and match each sentence to the timing of the cooking.',
      [('When Eva arrived, I was cooking.', 'Cooking was still in progress at her arrival.'), ('When Eva arrived, I started cooking.', 'Cooking began at her arrival.'), ('When Eva arrived, I had finished cooking.', 'Cooking was already complete at her arrival.')],
      '*Was cooking* gives background in progress; *started* marks the beginning; *had finished* places completion before the arrival.',
      '*Was cooking* apraksta notiekošu fona darbību, *started* — tās sākumu, bet *had finished* — pabeigšanu pirms ierašanās.')
match('var-pp-b11-match-01', 'present_perfect', 'B1.1', 2,
      'Match each time expression to the information it gives in its sentence.',
      [('I have worked here for three years.', 'The length of the period: three years.'), ('I have worked here since 2023.', 'The starting point: 2023.'), ('I have not finished yet.', 'The action is still incomplete now.')],
      '*For* introduces a duration; *since* introduces a starting point. *Not ... yet* describes something that has not happened up to now.',
      '*For* ievada ilgumu, bet *since* — sākuma punktu. *Not ... yet* apraksta kaut ko, kas līdz šim vēl nav noticis.')
match('var-ppc-b12-match-01-r2', 'present_perfect_continuous', 'B1.2', 4,
      'Compare what each sentence focuses on.',
      [('I have painted the wall. It is finished.', 'Completion of one wall.'), ('I have been painting the wall for an hour.', 'The duration of the painting activity.'), ('I have painted three walls today.', 'The number of completed walls.')],
      'The simple form can focus on completion or quantity. The continuous form focuses on the activity and its duration; it does not by itself say the wall is finished.',
      'Simple forma var uzsvērt pabeigšanu vai daudzumu. Continuous forma uzsver darbību un tās ilgumu; tā pati par sevi nenorāda, ka siena ir pabeigta.')
match('var-pasp-b12-match-01-r2', 'past_simple_passive', 'B1.2', 4,
      'Identify the voice and time in each sentence.',
      [('The technician repaired the printer.', 'Past active: the technician is the subject.'), ('The printer was repaired yesterday.', 'Past passive: the printer is the subject.'), ('The printer is being repaired now.', 'Present continuous passive: the repair is in progress.')],
      'In the active sentence, the subject does the action. In the passive sentences, the printer receives it. The auxiliaries distinguish past completion from work in progress.',
      'Darāmajā kārtā teikuma priekšmets veic darbību. Ciešamajā kārtā printeris saņem darbību. Palīgdarbības vārdi atšķir pagātnes darbību no pašlaik notiekoša darba.')
match('var-fu-b11-match-01', 'future', 'B1.1', 5,
      'Match each situation with the response that best fits its purpose.',
      [('You decide now to help a colleague with a heavy bag.', "I'll carry that for you."), ('You describe a confirmed appointment for tomorrow.', "I'm seeing the dentist at ten."), ('You predict rain because you can see dark clouds.', "It's going to rain.")],
      'Choose the form for the purpose: *will* for this immediate offer, present continuous for the arrangement, and *going to* to highlight visible evidence.',
      'Izvēlies formu atbilstoši nolūkam: *will* šim tūlītējam piedāvājumam, Present Continuous norunai un *going to*, lai uzsvērtu redzamās pazīmes.')
match('var-cf-b11-match-01', 'cond_first', 'B1.1', 2,
      'Match each sentence with the relationship it expresses.',
      [("If you help me, I'll buy you lunch.", 'A promise depending on your help.'), ("We won't start unless everyone is here.", 'Everyone being present is necessary for us to start.'), ("I'll take water in case the shop is closed.", 'A precaution against a possible problem.')],
      '*If* introduces the condition for the promise. *Unless* means *if not*. *In case* gives the reason for taking a precaution in advance.',
      '*If* ievada solījuma nosacījumu. *Unless* nozīmē *if not*. *In case* pamato iepriekš veiktu piesardzības pasākumu.')
match('var-cs-b12-match-01', 'cond_second', 'B1.2', 4,
      'Compare the conditionals and match each sentence to its time and meaning.',
      [("If I had enough money now, I'd buy a car.", 'An imagined present situation.'), ("If I have enough money next month, I'll buy a car.", 'A possible future situation.'), ("If I had had enough money yesterday, I'd have bought a car.", 'An imagined alternative to the past.')],
      '*Had ... would buy* imagines the present; *have ... will buy* concerns a possible future; *had had ... would have bought* imagines a different past.',
      '*Had ... would buy* izsaka iedomātu tagadni, *have ... will buy* — iespējamu nākotni, bet *had had ... would have bought* — iedomātu pagātni.')
match('var-rs-b12-match-01', 'rep_statements', 'B1.2', 3,
      'Match each statement by Eva to its report. Use backshift.',
      [("'I am busy,' Eva said.", 'Eva said she was busy.'), ("'I have finished,' Eva said.", 'Eva said she had finished.'), ("'I can help,' Eva said.", 'Eva said she could help.')],
      'In these backshifted reports, *am → was*, *have finished → had finished*, and *can → could*. Eva becomes *she*.',
      'Saskaņojot laikus šajos teikumos, *am → was*, *have finished → had finished* un *can → could*. Evas vietā lieto *she*.')
match('var-ip-b11-match-01', 'ind_polite', 'B1.1', 3,
      'Match each direct question to the indirect question with the same meaning.',
      [('Where is the meeting room?', 'Could you tell me where the meeting room is?'), ('What time does the café close?', 'Do you know what time the café closes?'), ('Does this bus stop at the station?', 'Could you tell me if this bus stops at the station?')],
      'Use statement word order in the indirect part. For a yes/no question, add *if* or *whether*. The auxiliary *does* disappears and the main verb takes *-s*.',
      'Netiešajā daļā lieto apgalvojuma vārdu secību. Jā/nē jautājumam pievieno *if* vai *whether*. Palīgdarbības vārds *does* pazūd, un pamatdarbības vārdam pievieno *-s*.')
