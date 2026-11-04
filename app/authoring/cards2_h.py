"""Rule cards, new layout: the last twelve cards that still had the old layout (teacher, 4 November, option B).
One style for all of them: passives with the Positive / Negative / Question table like the other passives; every other
topic with one Form · Example table; three typical mistakes; two blocks in "When we use it"; one Watch out point that says
something the card does not say yet. A Latvian note on a mistake only where Latvian causes it ("Tulkojot burtiski…").
Grammar checked against Murphy, English Grammar in Use, and the British Council LearnEnglish pages for B1–C1."""

EN_COLS = ["Positive", "Negative", "Question"]
LV_COLS = ["Apstiprinājums", "Noliegums", "Jautājums"]
FE = ["Form", "Example"]
FP = ["Forma", "Piemērs"]


def card(en_choice, lv_choice, mistakes_en, mistakes_lv, uses_en, uses_lv, watch_en, watch_lv, table=False):
    k = "table" if table else "choice"
    return {"en": {k: en_choice, "mistakes": mistakes_en, "uses": uses_en, "watch": watch_en},
            "lv": {k: lv_choice, "mistakes": mistakes_lv, "uses": uses_lv, "watch": watch_lv}}


PCP = [["I", "[[am being]] [[checked]]", "[[am not being]] [[checked]]", "[[Am]] I [[being checked]]?"],
       ["he / she / it", "[[is being]] [[repaired]]", "[[isn't being]] [[repaired]]", "[[Is]] it [[being repaired]]?"],
       ["you / we / they", "[[are being]] [[painted]]", "[[aren't being]] [[painted]]", "[[Are]] they [[being painted]]?"]]
PPP = [["I / you / we / they", "[[have been]] [[sent]]", "[[haven't been]] [[sent]]", "[[Have]] they [[been sent]]?"],
       ["he / she / it", "[[has been]] [[solved]]", "[[hasn't been]] [[solved]]", "[[Has]] it [[been solved]]?"]]
FUP = [["will (everyone)", "[[will be]] [[told]]", "[[won't be]] [[told]]", "[[Will]] you [[be told]]?"],
       ["be going to", "[[is going to be]] [[built]]", "[[isn't going to be]] [[built]]", "[[Is]] it [[going to be built]]?"]]

CARDS = {
    "present_continuous_passive": card(
        {"cols": EN_COLS, "rows": PCP, "short": "*am / is / are* + *being* + 3rd form."},
        {"cols": LV_COLS, "rows": PCP, "short": "*am / is / are* + *being* + 3. forma."},
        [["The road [[is repairing]] now.", "The road [[is being repaired]] now."],
         ["Your order [[is been]] prepared.", "Your order [[is being]] prepared."],
         ["The rooms [[is being]] cleaned.", "The rooms [[are being]] cleaned."]],
        [["The road [[is repairing]] now.", "The road [[is being repaired]] now.", "Tulkojot burtiski \"ceļu remontē\", iznāk darāmā kārta *is repairing*; ceļš pats sevi neremontē."],
         ["Your order [[is been]] prepared.", "Your order [[is being]] prepared."],
         ["The rooms [[is being]] cleaned.", "The rooms [[are being]] cleaned."]],
        [{"t": "An action in progress now; who does it is not important", "s": ["now", "at the moment", "right now"],
          "ex": ["The road [[is being repaired]] at the moment.", "Your order [[is being prepared]]."]},
         {"t": "Something in progress around now", "s": ["this week", "these days"], "ex": ["A new school [[is being built]] in our town."]}],
        [{"t": "Darbība notiek tagad; nav svarīgi, kas to dara", "s": ["now", "at the moment", "right now"],
          "ex": ["The road [[is being repaired]] at the moment.", "Your order [[is being prepared]]."]},
         {"t": "Kaut kas notiek šajā laikā", "s": ["this week", "these days"], "ex": ["A new school [[is being built]] in our town."]}],
        ["Already finished: *has been* + 3rd form: *The road [[has been repaired]].*"],
        ["Jau pabeigts: *has been* + 3. forma: *The road [[has been repaired]].*"], table=True),

    "present_perfect_passive": card(
        {"cols": EN_COLS, "rows": PPP, "short": "*has / have* + *been* + 3rd form."},
        {"cols": LV_COLS, "rows": PPP, "short": "*has / have* + *been* + 3. forma."},
        [["The email [[has sent]].", "The email [[has been sent]]."],
         ["The problem [[have been]] solved.", "The problem [[has been]] solved."],
         ["The tickets [[have been sold]] yesterday.", "The tickets [[were sold]] yesterday."]],
        [["The email [[has sent]].", "The email [[has been sent]]."],
         ["The problem [[have been]] solved.", "The problem [[has been]] solved."],
         ["The tickets [[have been sold]] yesterday.", "The tickets [[were sold]] yesterday."]],
        [{"t": "News or a result now; who did it is not important", "s": ["just", "already", "yet"],
          "ex": ["The email [[has just been sent]].", "[[Has]] the problem [[been solved]] yet?"]},
         {"t": "Up to now", "s": ["so far", "recently"], "ex": ["Ten new shops [[have been opened]] so far this year."]}],
        [{"t": "Jaunums vai rezultāts tagad; nav svarīgi, kas to izdarīja", "s": ["just", "already", "yet"],
          "ex": ["The email [[has just been sent]].", "[[Has]] the problem [[been solved]] yet?"]},
         {"t": "Līdz šim brīdim", "s": ["so far", "recently"], "ex": ["Ten new shops [[have been opened]] so far this year."]}],
        ["*been*, not *being*: *The car [[has been]] fixed.*"],
        ["*been*, nevis *being*: *The car [[has been]] fixed.*"], table=True),

    "future_passive": card(
        {"cols": EN_COLS, "rows": FUP, "short": "*will be* + 3rd form; *be going to be* + 3rd form."},
        {"cols": LV_COLS, "rows": FUP, "short": "*will be* + 3. forma; *be going to be* + 3. forma."},
        [["The results [[will announced]] on Friday.", "The results [[will be announced]] on Friday."],
         ["You [[will be tell]] soon.", "You [[will be told]] soon."],
         ["[[Will be the meeting]] held online?", "[[Will the meeting be]] held online?"]],
        [["The results [[will announced]] on Friday.", "The results [[will be announced]] on Friday."],
         ["You [[will be tell]] soon.", "You [[will be told]] soon."],
         ["[[Will be the meeting]] held online?", "[[Will the meeting be]] held online?"]],
        [{"t": "A future event; who does it is unknown or not important", "s": ["tomorrow", "next week", "soon"],
          "ex": ["The results [[will be announced]] on Friday."]},
         {"t": "Announcements and plans", "s": ["by Friday", "next year"], "ex": ["All passengers [[will be asked]] to show their passports.", "A new bridge [[is going to be built]] next year."]}],
        [{"t": "Nākotnes notikums; nav zināms vai nav svarīgi, kas to darīs", "s": ["tomorrow", "next week", "soon"],
          "ex": ["The results [[will be announced]] on Friday."]},
         {"t": "Paziņojumi un plāni", "s": ["by Friday", "next year"], "ex": ["All passengers [[will be asked]] to show their passports.", "A new bridge [[is going to be built]] next year."]}],
        ["After *will*, *be* never changes: *They [[will be]] invited.*"],
        ["Aiz *will* forma *be* nemainās: *They [[will be]] invited.*"], table=True),

    "cond_mixed": card(
        {"stack": "rows", "cols": FE, "rows": [
            ["Past → now", "*If* + past perfect, *would* + base form: a past event changes the present", "*If I [[had taken]] that job, I [[would be]] rich now.*"],
            ["Now → past", "*If* + past simple, *would have* + 3rd form: a present quality changes a past event", "*If I [[weren't]] so shy, I [[would have asked]] her out.*"],
            ["Formal", "*Had* + subject + 3rd form, then the result now", "*[[Had]] I [[listened]], I [[wouldn't be]] in this mess now.*"]]},
        {"stack": "rows", "cols": FP, "rows": [
            ["Pagātne → tagadne", "*If* + Past Perfect, *would* + pamatforma: pagātnes notikums maina tagadni", "*If I [[had taken]] that job, I [[would be]] rich now.*"],
            ["Tagadne → pagātne", "*If* + Past Simple, *would have* + 3. forma: īpašība tagad maina pagātnes notikumu", "*If I [[weren't]] so shy, I [[would have asked]] her out.*"],
            ["Formāli", "*Had* + teikuma priekšmets + 3. forma, tad sekas tagad", "*[[Had]] I [[listened]], I [[wouldn't be]] in this mess now.*"]]},
        [["If I [[would have taken]] the job, I would be rich now.", "If I [[had taken]] the job, I would be rich now."],
         ["If she [[is]] more patient, she wouldn't have shouted.", "If she [[were]] more patient, she wouldn't have shouted."],
         ["If he had studied medicine, he [[will be]] a doctor now.", "If he had studied medicine, he [[would be]] a doctor now."]],
        [["If I [[would have taken]] the job, I would be rich now.", "If I [[had taken]] the job, I would be rich now."],
         ["If she [[is]] more patient, she wouldn't have shouted.", "If she [[were]] more patient, she wouldn't have shouted."],
         ["If he had studied medicine, he [[will be]] a doctor now.", "If he had studied medicine, he [[would be]] a doctor now."]],
        [{"t": "A past event with a result now", "s": ["now", "today", "still"], "ex": ["If I [[hadn't missed]] the train, I [[would be]] home now."]},
         {"t": "A quality now with a result in the past", "s": ["at the time", "yesterday"], "ex": ["If he [[were]] more confident, he [[would have asked]] for a pay rise."]}],
        [{"t": "Pagātnes notikums ar sekām tagad", "s": ["now", "today", "still"], "ex": ["If I [[hadn't missed]] the train, I [[would be]] home now."]},
         {"t": "Īpašība tagad ar sekām pagātnē", "s": ["at the time", "yesterday"], "ex": ["If he [[were]] more confident, he [[would have asked]] for a pay rise."]}],
        ["Look at the time words: *now, today* go with *would* + base form; *yesterday, last year* go with *had* + 3rd form: *If I [[had saved]] last year, I [[would have]] a car now.*"],
        ["Skaties laika vārdus: *now, today* iet kopā ar *would* + pamatformu; *yesterday, last year* ar *had* + 3. formu: *If I [[had saved]] last year, I [[would have]] a car now.*"]),

    "cond_advanced": card(
        {"stack": "rows", "cols": FE, "rows": [
            ["Inversion", "*Had / Were / Should* + subject, without *if* (formal)", "*[[Had]] I [[known]], I would have helped. [[Should]] you [[need]] help, call me.*"],
            ["But for", "*But for* + noun = *If it hadn't been for*", "*[[But for]] your help, we would have failed.*"],
            ["unless, as long as", "*unless* = *if … not*; *as long as / provided that* = only if", "*We'll start at ten [[unless]] it [[rains]].*"],
            ["wish, if only", "+ past (now), + past perfect (the past), + *would* (something that annoys us)", "*I [[wish]] I [[had]] more time. [[If only]] I [[had listened]]!*"]]},
        {"stack": "rows", "cols": FP, "rows": [
            ["Inversija", "*Had / Were / Should* + teikuma priekšmets bez *if* (formāli)", "*[[Had]] I [[known]], I would have helped. [[Should]] you [[need]] help, call me.*"],
            ["But for", "*But for* + lietvārds = *If it hadn't been for*", "*[[But for]] your help, we would have failed.*"],
            ["unless, as long as", "*unless* = *if … not*; *as long as / provided that* = tikai ja", "*We'll start at ten [[unless]] it [[rains]].*"],
            ["wish, if only", "+ pagātne (tagad), + Past Perfect (pagātne), + *would* (kas kaitina)", "*I [[wish]] I [[had]] more time. [[If only]] I [[had listened]]!*"]]},
        [["[[If had I known]], I would have helped.", "[[Had I known]], I would have helped."],
         ["We'll start [[unless it doesn't rain]].", "We'll start [[unless it rains]]."],
         ["I wish I [[would have]] more time.", "I wish I [[had]] more time."]],
        [["[[If had I known]], I would have helped.", "[[Had I known]], I would have helped."],
         ["We'll start [[unless it doesn't rain]].", "We'll start [[unless it rains]].", "Tulkojot burtiski \"ja vien nelīs\", iznāk divi noliegumi; *unless* jau ietver *not*."],
         ["I wish I [[would have]] more time.", "I wish I [[had]] more time."]],
        [{"t": "Formal writing and speaking", "s": ["Had I…", "Should you…", "Were she…"], "ex": ["[[Should]] you have any questions, please contact us."]},
         {"t": "Regret and wishes", "s": ["I wish", "if only"], "ex": ["[[If only]] we [[had tested]] the app!"]}],
        [{"t": "Formāls teksts un runa", "s": ["Had I…", "Should you…", "Were she…"], "ex": ["[[Should]] you have any questions, please contact us."]},
         {"t": "Nožēla un vēlēšanās", "s": ["I wish", "if only"], "ex": ["[[If only]] we [[had tested]] the app!"]}],
        ["In the negative, *not* comes after the subject: *[[Had she not]] missed the train, she would be here.*"],
        ["Noliegumā *not* ir aiz teikuma priekšmeta: *[[Had she not]] missed the train, she would be here.*"]),

    "rep_verbs": card(
        {"stack": "rows", "cols": FE, "rows": [
            ["+ that", "*admit, explain, complain, promise, insist* + *that* + clause", "*She [[admitted that]] she had lied.*"],
            ["+ person + to", "*advise, warn, remind, urge, encourage* + person + *to*", "*He [[advised me to]] see a doctor.*"],
            ["+ to", "*offer, refuse, agree, threaten* + *to*", "*She [[refused to]] sign the contract.*"],
            ["+ -ing", "*suggest, deny, recommend* + *-ing*", "*He [[suggested taking]] a taxi.*"],
            ["+ preposition + -ing", "*apologise for, insist on, accuse someone of*", "*She [[apologised for]] being late.*"]]},
        {"stack": "rows", "cols": FP, "rows": [
            ["+ that", "*admit, explain, complain, promise, insist* + *that* + palīgteikums", "*She [[admitted that]] she had lied.*"],
            ["+ persona + to", "*advise, warn, remind, urge, encourage* + persona + *to*", "*He [[advised me to]] see a doctor.*"],
            ["+ to", "*offer, refuse, agree, threaten* + *to*", "*She [[refused to]] sign the contract.*"],
            ["+ -ing", "*suggest, deny, recommend* + *-ing*", "*He [[suggested taking]] a taxi.*"],
            ["+ prievārds + -ing", "*apologise for, insist on, accuse someone of*", "*She [[apologised for]] being late.*"]]},
        [["He [[suggested me to]] take a taxi.", "He [[suggested taking]] a taxi."],
         ["She [[insisted to pay]].", "She [[insisted on paying]]."],
         ["They [[accused him for]] cheating.", "They [[accused him of]] cheating."]],
        [["He [[suggested me to]] take a taxi.", "He [[suggested taking]] a taxi.", "Tulkojot burtiski \"viņš man ieteica paņemt taksi\", iznāk *suggested me to*; aiz *suggest* nav persona + *to*."],
         ["She [[insisted to pay]].", "She [[insisted on paying]]."],
         ["They [[accused him for]] cheating.", "They [[accused him of]] cheating."]],
        [{"t": "To say what the person meant, not only the words", "s": ["admitted", "denied", "promised", "warned"],
          "ex": ["'I didn't take it.' → He [[denied taking]] it."]},
         {"t": "Shorter and more natural than *said that…*", "ex": ["'Shall I help?' → She [[offered to help]]."]}],
        [{"t": "Lai pateiktu, ko cilvēks ar to domāja, ne tikai vārdus", "s": ["admitted", "denied", "promised", "warned"],
          "ex": ["'I didn't take it.' → He [[denied taking]] it."]},
         {"t": "Īsāk un dabiskāk nekā *said that…*", "ex": ["'Shall I help?' → She [[offered to help]]."]}],
        ["Some verbs take two patterns with the same meaning: *He admitted [[taking]] the money.* = *He admitted [[that he had taken]] the money.*"],
        ["Dažiem darbības vārdiem ir divas uzbūves ar vienu nozīmi: *He admitted [[taking]] the money.* = *He admitted [[that he had taken]] the money.*"]),

    "ind_advanced": card(
        {"stack": "rows", "cols": FE, "rows": [
            ["Question word + to", "*what / how / where / who* + *to* + base form", "*I don't know [[what to do]].*"],
            ["whether", "*whether* + clause, or *whether to* + base form", "*I can't decide [[whether to accept]].*"],
            ["As the subject", "the whole question clause is the subject, in statement order", "*[[Whether he will come]] is still unclear.*"],
            ["-ever words", "*whoever / whatever / wherever* = it does not matter who / what / where", "*[[Whoever]] finishes first can go home.*"]]},
        {"stack": "rows", "cols": FP, "rows": [
            ["Jautājamais vārds + to", "*what / how / where / who* + *to* + pamatforma", "*I don't know [[what to do]].*"],
            ["whether", "*whether* + palīgteikums vai *whether to* + pamatforma", "*I can't decide [[whether to accept]].*"],
            ["Kā teikuma priekšmets", "viss jautājuma palīgteikums ir teikuma priekšmets, apgalvojuma secībā", "*[[Whether he will come]] is still unclear.*"],
            ["-ever vārdi", "*whoever / whatever / wherever* = nav svarīgi, kas / ko / kur", "*[[Whoever]] finishes first can go home.*"]]},
        [["I don't know [[what should I]] do.", "I don't know [[what to]] do."],
         ["[[Why did the system fail]] remains unclear.", "[[Why the system failed]] remains unclear."],
         ["[[Whomever]] arrives last washes up.", "[[Whoever]] arrives last washes up."]],
        [["I don't know [[what should I]] do.", "I don't know [[what to]] do.", "Tulkojot burtiski \"nezinu, ko man darīt\", iznāk jautājuma secība; angliski: *what to do*."],
         ["[[Why did the system fail]] remains unclear.", "[[Why the system failed]] remains unclear."],
         ["[[Whomever]] arrives last washes up.", "[[Whoever]] arrives last washes up."]],
        [{"t": "Not knowing or not being sure", "s": ["no idea", "not sure", "it depends on", "the question is"],
          "ex": ["I have [[no idea how long]] the meeting [[will take]]."]},
         {"t": "Formal writing", "ex": ["[[How the funds were spent]] remains to be investigated."]}],
        [{"t": "Kad nezinām vai neesam pārliecināti", "s": ["no idea", "not sure", "it depends on", "the question is"],
          "ex": ["I have [[no idea how long]] the meeting [[will take]]."]},
         {"t": "Formāls teksts", "ex": ["[[How the funds were spent]] remains to be investigated."]}],
        ["After a preposition use *whether*, not *if*: *It depends on [[whether]] the budget is approved.*"],
        ["Aiz prievārda lieto *whether*, nevis *if*: *It depends on [[whether]] the budget is approved.*"]),

    "passive_modals": card(
        {"stack": "rows", "cols": FE, "rows": [
            ["Positive", "modal + *be* + 3rd form", "*Tickets [[can be bought]] online.*"],
            ["Negative", "modal + *not* + *be* + 3rd form", "*Shoes [[mustn't be worn]] inside.*"],
            ["Question", "modal + subject + *be* + 3rd form?", "*[[Can]] this [[be repaired]]?*"],
            ["Past", "modal + *have been* + 3rd form", "*The accident [[could have been avoided]].*"]]},
        {"stack": "rows", "cols": FP, "rows": [
            ["Apstiprinājums", "modālais darbības vārds + *be* + 3. forma", "*Tickets [[can be bought]] online.*"],
            ["Noliegums", "modālais darbības vārds + *not* + *be* + 3. forma", "*Shoes [[mustn't be worn]] inside.*"],
            ["Jautājums", "modālais darbības vārds + teikuma priekšmets + *be* + 3. forma?", "*[[Can]] this [[be repaired]]?*"],
            ["Pagātne", "modālais darbības vārds + *have been* + 3. forma", "*The accident [[could have been avoided]].*"]]},
        [["The report [[must finished]] today.", "The report [[must be finished]] today."],
         ["Tickets [[can be buy]] online.", "Tickets [[can be bought]] online."],
         ["The door [[should be lock]] at night.", "The door [[should be locked]] at night."]],
        [["The report [[must finished]] today.", "The report [[must be finished]] today.", "Tulkojot burtiski \"ziņojums jāpabeidz\", iznāk bez *be*; angliski: *must be finished*."],
         ["Tickets [[can be buy]] online.", "Tickets [[can be bought]] online."],
         ["The door [[should be lock]] at night.", "The door [[should be locked]] at night."]],
        [{"t": "Rules and advice; who does it is not important", "s": ["must be", "should be", "has to be"],
          "ex": ["All forms [[must be signed]] by the manager."]},
         {"t": "Possibility and ability", "s": ["can be", "could be"], "ex": ["The problem [[can be solved]] in a day."]}],
        [{"t": "Noteikumi un padomi; nav svarīgi, kas to dara", "s": ["must be", "should be", "has to be"],
          "ex": ["All forms [[must be signed]] by the manager."]},
         {"t": "Iespēja un spēja", "s": ["can be", "could be"], "ex": ["The problem [[can be solved]] in a day."]}],
        ["The modal never changes, and there is no *to* after it: *It [[must be]] done today.*"],
        ["Modālais darbības vārds nemainās, un aiz tā nav *to*: *It [[must be]] done today.*"]),

    "causative": card(
        {"stack": "rows", "cols": FE, "rows": [
            ["have", "*have* + object + 3rd form: someone does it for us", "*I [[had]] my hair [[cut]].*"],
            ["get", "*get* + object + 3rd form (more informal)", "*We [[got]] the windows [[cleaned]].*"],
            ["Questions, negatives", "*do / does / did* + *have* + object + 3rd form", "*[[Did]] you [[have]] your car [[checked]]?*"],
            ["Something bad", "the same form: it happened to us", "*He [[had]] his wallet [[stolen]].*"]]},
        {"stack": "rows", "cols": FP, "rows": [
            ["have", "*have* + papildinātājs + 3. forma: kāds to izdara mūsu vietā", "*I [[had]] my hair [[cut]].*"],
            ["get", "*get* + papildinātājs + 3. forma (sarunvalodā)", "*We [[got]] the windows [[cleaned]].*"],
            ["Jautājumi, noliegumi", "*do / does / did* + *have* + papildinātājs + 3. forma", "*[[Did]] you [[have]] your car [[checked]]?*"],
            ["Kaut kas slikts", "tā pati forma: tas notika ar mums", "*He [[had]] his wallet [[stolen]].*"]]},
        [["I [[cut my hair]] at the hairdresser's.", "I [[had my hair cut]] at the hairdresser's."],
         ["I had [[cleaned my car]] yesterday.", "I had [[my car cleaned]] yesterday."],
         ["She is having her car [[repair]].", "She is having her car [[repaired]]."]],
        [["I [[cut my hair]] at the hairdresser's.", "I [[had my hair cut]] at the hairdresser's.", "Tulkojot burtiski \"es nogriezu matus\", iznāk *I cut my hair*, un tas nozīmē, ka griezi pats."],
         ["I had [[cleaned my car]] yesterday.", "I had [[my car cleaned]] yesterday."],
         ["She is having her car [[repair]].", "She is having her car [[repaired]]."]],
        [{"t": "A service someone does for us", "s": ["hairdresser", "mechanic", "dentist"], "ex": ["I'm [[having]] my laptop [[fixed]] this week."]},
         {"t": "Something bad that happened to us", "ex": ["She [[had]] her bag [[stolen]] on the train."]}],
        [{"t": "Pakalpojums, ko kāds dara mūsu labā", "s": ["hairdresser", "mechanic", "dentist"], "ex": ["I'm [[having]] my laptop [[fixed]] this week."]},
         {"t": "Kaut kas slikts, kas ar mums notika", "ex": ["She [[had]] her bag [[stolen]] on the train."]}],
        ["The object comes before the 3rd form: *I had [[my car]] [[washed]]*, not *I had washed my car* (that means I washed it)."],
        ["Papildinātājs ir pirms 3. formas: *I had [[my car]] [[washed]]*, nevis *I had washed my car* (tas nozīmē, ka mazgāju pats)."]),

    "adj_order": card(
        {"stack": "rows", "cols": FE, "rows": [
            ["Opinion first", "opinion before facts", "*a [[lovely]] [[old]] house*"],
            ["Facts in order", "size · age · shape · colour · origin · material + noun", "*a [[small]] [[old]] [[red]] [[Italian]] car*"],
            ["After be", "adjectives with *and*", "*The room is [[big]], [[bright]] and [[cheap]].*"]]},
        {"stack": "rows", "cols": FP, "rows": [
            ["Vispirms vērtējums", "vērtējums pirms faktiem", "*a [[lovely]] [[old]] house*"],
            ["Fakti secībā", "izmērs · vecums · forma · krāsa · izcelsme · materiāls + lietvārds", "*a [[small]] [[old]] [[red]] [[Italian]] car*"],
            ["Aiz be", "īpašības vārdi ar *and*", "*The room is [[big]], [[bright]] and [[cheap]].*"]]},
        [["an [[old lovely]] house", "a [[lovely old]] house"],
         ["a [[red big]] car", "a [[big red]] car"],
         ["two [[smalls]] boxes", "two [[small]] boxes"]],
        [["an [[old lovely]] house", "a [[lovely old]] house"],
         ["a [[red big]] car", "a [[big red]] car"],
         ["two [[smalls]] boxes", "two [[small]] boxes", "Tulkojot burtiski \"divas mazas kastes\", īpašības vārdam gribas daudzskaitli; angliski tas nemainās."]],
        [{"t": "Two or three adjectives before a noun", "s": ["opinion", "size", "age", "colour"], "ex": ["She bought a [[beautiful small black]] bag."]},
         {"t": "Where it comes from and what it is made of: last, just before the noun", "s": ["origin", "material"], "ex": ["a [[Spanish]] [[leather]] jacket"]}],
        [{"t": "Divi vai trīs īpašības vārdi pirms lietvārda", "s": ["opinion", "size", "age", "colour"], "ex": ["She bought a [[beautiful small black]] bag."]},
         {"t": "Izcelsme un materiāls: pēdējie, tieši pirms lietvārda", "s": ["origin", "material"], "ex": ["a [[Spanish]] [[leather]] jacket"]}],
        ["Usually not more than three adjectives before a noun; more sounds unnatural: *a [[nice]] [[new]] [[wooden]] table*."],
        ["Parasti ne vairāk kā trīs īpašības vārdi pirms lietvārda: *a [[nice]] [[new]] [[wooden]] table*."]),

    "so_such": card(
        {"stack": "rows", "cols": FE, "rows": [
            ["so", "*so* + adjective or adverb", "*The film was [[so long]]. He runs [[so fast]].*"],
            ["such", "*such* + (*a / an*) + (adjective) + noun", "*It was [[such a long film]]. They're [[such nice people]].*"],
            ["so much, so many", "*so much* + uncountable noun, *so many* + plural", "*[[so much]] noise, [[so many]] people*"],
            ["Result", "*so / such … that*", "*It was [[so cold that]] we stayed inside.*"]]},
        {"stack": "rows", "cols": FP, "rows": [
            ["so", "*so* + īpašības vārds vai apstākļa vārds", "*The film was [[so long]]. He runs [[so fast]].*"],
            ["such", "*such* + (*a / an*) + (īpašības vārds) + lietvārds", "*It was [[such a long film]]. They're [[such nice people]].*"],
            ["so much, so many", "*so much* + neskaitāms lietvārds, *so many* + daudzskaitlis", "*[[so much]] noise, [[so many]] people*"],
            ["Rezultāts", "*so / such … that*", "*It was [[so cold that]] we stayed inside.*"]]},
        [["It was [[so a]] long film.", "It was [[such a]] long film."],
         ["They are [[such a]] nice people.", "They are [[such]] nice people."],
         ["There were [[so much]] people.", "There were [[so many]] people."]],
        [["It was [[so a]] long film.", "It was [[such a]] long film.", "Latviski abus izsaka ar \"tik\"; tulkojot burtiski, aiz *so* paliek lietvārds."],
         ["They are [[such a]] nice people.", "They are [[such]] nice people."],
         ["There were [[so much]] people.", "There were [[so many]] people."]],
        [{"t": "To make a feeling stronger", "ex": ["The view was [[so beautiful]]!", "It was [[such a]] great day!"]},
         {"t": "To give the result", "s": ["that"], "ex": ["I was [[so tired that]] I fell asleep at once."]}],
        [{"t": "Lai sajūtu izteiktu stiprāk", "ex": ["The view was [[so beautiful]]!", "It was [[such a]] great day!"]},
         {"t": "Lai pateiktu rezultātu", "s": ["that"], "ex": ["I was [[so tired that]] I fell asleep at once."]}],
        ["*such* + plural or uncountable noun has no *a / an*: *[[such]] bad weather*."],
        ["*such* + daudzskaitlis vai neskaitāms lietvārds ir bez *a / an*: *[[such]] bad weather*."]),

    "unreal_time": card(
        {"stack": "rows", "cols": FE, "rows": [
            ["It's time", "*It's (high / about) time* + subject + past: it should happen now", "*It's [[high time]] we [[left]].*"],
            ["I'd rather (me)", "*I'd rather / I'd sooner* + base form", "*I'd [[rather stay]] at home.*"],
            ["I'd rather (you)", "*I'd rather* + another person + past", "*I'd rather you [[didn't tell]] anyone.*"]]},
        {"stack": "rows", "cols": FP, "rows": [
            ["It's time", "*It's (high / about) time* + teikuma priekšmets + pagātne: tam jau vajadzētu notikt", "*It's [[high time]] we [[left]].*"],
            ["I'd rather (es)", "*I'd rather / I'd sooner* + pamatforma", "*I'd [[rather stay]] at home.*"],
            ["I'd rather (tu)", "*I'd rather* + cits cilvēks + pagātne", "*I'd rather you [[didn't tell]] anyone.*"]]},
        [["It's high time we [[go]].", "It's high time we [[went]]."],
         ["I'd rather [[to walk]].", "I'd rather [[walk]]."],
         ["I'd rather you [[don't call]] me after ten.", "I'd rather you [[didn't call]] me after ten."]],
        [["It's high time we [[go]].", "It's high time we [[went]].", "Tulkojot burtiski \"ir laiks, lai mēs ejam\", iznāk tagadne; angliski: pagātne *went*."],
         ["I'd rather [[to walk]].", "I'd rather [[walk]]."],
         ["I'd rather you [[don't call]] me after ten.", "I'd rather you [[didn't call]] me after ten."]],
        [{"t": "Something should already be happening", "s": ["it's time", "it's high time", "it's about time"], "ex": ["It's [[about time]] you [[called]] your mother."]},
         {"t": "What I prefer, or what I want someone else to do", "s": ["would rather", "would sooner"], "ex": ["I'd [[sooner take]] the train than drive.", "I'd rather you [[came]] a bit earlier."]}],
        [{"t": "Tam jau vajadzētu notikt", "s": ["it's time", "it's high time", "it's about time"], "ex": ["It's [[about time]] you [[called]] your mother."]},
         {"t": "Ko es labāk darītu vai ko gribu, lai dara cits", "s": ["would rather", "would sooner"], "ex": ["I'd [[sooner take]] the train than drive.", "I'd rather you [[came]] a bit earlier."]}],
        ["The past form here is about now, not the past: *It's time we [[went]]* = we should go now."],
        ["Pagātnes forma šeit runā par tagadni: *It's time we [[went]]* = mums tagad jāiet."]),
}
