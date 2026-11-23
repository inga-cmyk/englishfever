"""Eight topics that the B1 reference teaches and the bank did not have: rule cards (English marked with * for italics, Latvian plain) and their place in the topic list.
Their tasks are added by the teacher on the Tasks page (CSV drafts in docs/task-drafts), so the topics stay hidden until they have approved tasks."""

AREAS_NEW = [("nouns", "Nouns and articles"), ("clauses", "Linking ideas"), ("questions", "Question forms"), ("patterns", "Verb patterns")]

SKILLS_NEW = [
    ("used_to", "Used to and be used to", "active", ["A2.2", "B1.1", "B1.2"]),
    ("articles", "Articles: a, an, the", "nouns", ["A2.1", "A2.2", "B1.1", "B1.2"]),   # A2.1: no article (art_zero), prepared tasks only (teacher, 14 November)
    ("quantity", "Quantity: some, any, much, many, enough", "nouns", ["A2.1", "A2.2", "B1.1"]),   # A2.1: a few / a little, countable and uncountable, prepared tasks only (teacher, 15 November, batch 5)
    ("relative_clauses", "Relative clauses (who, which, that, where)", "clauses", ["A2.2", "B1.1", "B1.2"]),
    ("time_clauses", "Time words and clauses (then, while, when, until)", "clauses", ["A2.2", "B1.1", "B1.2"]),   # in Linking ideas (teacher, 22 November: that area mixes many forms; not with the conditionals); the time words of conj_linkers moved here (topic_layout.py)
    ("question_tags", "Question tags (isn't it? don't you?)", "questions", ["A2.2", "B1.1", "B1.2"]),
    ("subject_object_q", "Subject and object questions", "questions", ["A2.2", "B1.1", "B1.2"]),
    ("verb_patterns", "Verb patterns: -ing or to", "patterns", ["A2.1", "A2.2", "B1.1", "B1.2"]),   # A2.1: like + -ing, want + to, prepared tasks only (teacher, 15 November, batch 5)
]

ABBR_NEW = {"used_to": "ut", "articles": "art", "quantity": "qty", "relative_clauses": "rel", "time_clauses": "tcl", "question_tags": "qtg", "subject_object_q": "soq", "verb_patterns": "vpt"}

# English rule cards, hand-marked: *examples and forms are italic*
CARDS = {
    "used_to": {
        "form": ["*used to* + base verb: *I used to live in Riga.*",
                 "Negative: *didn't use to* + base verb (no *-d*): *She didn't use to like fish.*",
                 "Question: *Did* + subject + *use to* + base verb? *Did you use to play tennis?*",
                 "*be used to / get used to* + noun or verb-*ing*: *I'm used to getting up early. It took me a month to get used to the cold.*"],
        "use": ["*used to*: a habit or a state in the past that is not true now (*I used to smoke. He used to be shy*).",
                "Not for one finished event: use the Past Simple (*We went to Rome last year*).",
                "*be used to / get used to*: something is (or becomes) normal for you. It is different from *used to*!"],
        "signals": "*when I was young, as a child, in those days, now, any more*",
        "example": "*I used to walk to school, but now I'm used to taking the bus.*",
    },
    "articles": {
        "form": ["*a / an* + singular countable noun: *a book, an apple* (*an* before a vowel sound: *an hour*, *a university*).",
                 "*the* + singular, plural or uncountable noun: *the book, the books, the water.*",
                 "No article: plural and uncountable nouns in general (*Dogs are friendly. I like coffee*) and most names of people, cities and countries (*Riga, Latvia*)."],
        "use": ["*a / an*: one of many, or the first time we mention something (*I saw a film. It was a comedy*).",
                "*the*: something both people know, something already mentioned, or the only one (*the film we saw, the sun, the Internet*).",
                "*the* is also used with superlatives, rivers, seas and some countries (*the best, the Baltic Sea, the UK*).",
                "No article: general things, meals, and places used for their purpose (*have breakfast, go to school, at work*)."],
        "signals": "*first mention, already mentioned, the only one, in general*",
        "example": "*I bought a jacket and a hat. The jacket was cheap, but I love hats.*",
    },
    "quantity": {
        "form": ["*some / any* + plural or uncountable noun: *some apples, any milk.*",
                 "*many* + plural: *many people*. *much* + uncountable: *much time*. Mostly in questions and negatives: *How many? How much? not many, not much.*",
                 "*a lot of / lots of* + both, mostly in positive sentences: *a lot of people, a lot of time.*",
                 "*a few* + plural: *a few friends*. *a little* + uncountable: *a little time*. *few / little* (without *a*) = almost none.",
                 "*enough* + noun: *enough chairs*. Adjective + *enough*: *big enough*. *too much / too many* = more than we need."],
        "use": ["*some*: positive sentences and offers (*Would you like some tea?*). *any*: questions and negatives (*Do you have any brothers? I don't have any money*).",
                "*a few / a little* = a small number, a positive feeling. *few / little* = almost none, a negative feeling.",
                "*too much / too many* is a problem. *not enough* = less than we need."],
        "signals": "*how many, how much, a few, a little, enough, too much, too many*",
        "example": "*There isn't much time and there are too many things to do.*",
    },
    "relative_clauses": {
        "form": ["*who* = people, *which* = things, *that* = people or things: *a woman who lives next door, a phone which takes good photos.*",
                 "*where* = places, *whose* = belongs to: *the restaurant where we met, a driver whose car was stolen.*",
                 "Defining clause: no commas, it tells us which one: *The woman who called is my boss.* *Who / which / that* can be left out when it is the object: *the film we saw.*",
                 "Non-defining clause: commas, extra information, not *that*: *My brother, who lives in Berlin, is a nurse.*"],
        "use": ["A relative clause gives more information about a noun and joins two sentences into one.",
                "Defining: we need it to know which person or thing. Non-defining: extra information we could leave out.",
                "Do not repeat the object: *the book that I bought*, not *the book that I bought it.*"],
        "signals": "*who, which, that, where, whose, commas*",
        "example": "*The woman who called is my boss, and the office where she works is in Riga.*",
    },
    "time_clauses": {
        "form": ["*when / as soon as / until / before / after / while* + Present Simple (not *will*) for the future: *I'll call you when I arrive.*",
                 "The time clause can come first (with a comma) or second: *When I arrive, I'll call you.* = *I'll call you when I arrive.*",
                 "With *after* and *before* the Present Perfect is also possible: *I'll call you after I've finished.*"],
        "use": ["The main clause has *will / going to* or an order; the time clause has the present.",
                "*when* = at that time. *as soon as* = immediately. *until* = up to that moment (*Wait here until I come back*). *before / after* = which happens first. *while* = at the same time."],
        "signals": "*then, after that, when, as soon as, until, before, after, while, during, by the time*",
        "example": "*I'll tell you the news as soon as I get home.*",
    },
    "question_tags": {
        "form": ["Positive sentence, negative tag: *You like tea, don't you?*",
                 "Negative sentence, positive tag: *She isn't here, is she?*",
                 "The tag repeats the auxiliary: *is / are / was / were, have / has, can, will, should*. With the Present Simple and Past Simple: *do / does / did*.",
                 "Special: *I am* → *aren't I?* *Let's* → *shall we?* An order → *will you?* *Nobody / nothing* → positive tag with *they / it*."],
        "use": ["Voice goes down: you are sure and want agreement (*It's cold, isn't it?*).",
                "Voice goes up: you are not sure and really ask (*You're not working today, are you?*).",
                "The tag has the same tense as the sentence: *He went home, didn't he?*"],
        "signals": "*isn't it? don't you? can't he? will you? aren't I?*",
        "example": "*You haven't seen my keys, have you?*",
    },
    "subject_object_q": {
        "form": ["Object question with most main verbs in the present or past simple: question word + *do / does / did* + subject + base verb: *Who did you meet? What does she want?* With another auxiliary or a modal, that word comes first: *What are you doing? Who can you see?*",
                 "Neutral subject question: the question word is the subject, no *do / does / did*: *Who met you? What happened? Who wants coffee?* (Only for emphasis: *Who did call?*)",
                 "The verb keeps the normal form: *Who lives here?* (with *-s*), not *Who does live here?*"],
        "use": ["Ask about the person or thing that does the action: subject question (*Tom called me → Who called you?*).",
                "Ask about the person or thing the action happens to: object question (*I called Tom → Who did you call?*).",
                "Look at the answer: if the answer is the subject, the neutral question has no *did / does*."],
        "signals": "*who, what, which, whose as the subject: no do / does / did*",
        "example": "*Who wrote this email? Who did you send it to?*",
    },
    "verb_patterns": {
        "form": ["verb + *-ing*: *enjoy, finish, keep, avoid, mind, suggest, practise* (*I enjoy reading. She suggested going home.*)",
                 "verb + *to* + base verb: *want, need, decide, hope, plan, learn, agree, promise, manage, refuse* (*I want to leave. He decided to stay.*)",
                 "preposition + *-ing*: *interested in learning, good at cooking, before leaving, thank you for helping.*",
                 "Some verbs take both with a very similar meaning: *like, love, hate, start, begin* (*I like swimming. ≈ I like to swim.* The emphasis can differ.)",
                 "Different meaning: *stop / remember / forget / try* + *-ing* or *to* (*I stopped smoking = I quit. I stopped to smoke = I stopped in order to smoke.*)"],
        "use": ["The verb decides: learn which verbs go with *-ing* and which with *to*.",
                "After a preposition we use *-ing* when a verb follows directly: *She's good at drawing.* (A question word + *to* can also follow: *about how to improve it*.)",
                "*stop / remember / forget / try*: *-ing* = about something done or an experiment; *to* = a task or a purpose."],
        "signals": "*enjoy, avoid, finish + -ing; want, decide, hope + to; after a preposition: -ing*",
        "example": "*I enjoy cooking, but I decided to eat out tonight.*",
    },
}

# Latvian rule cards (plain; English examples are marked by the build)
LV_CARDS = {
    "used_to": {
        "form": ["used to + darbības vārda pamatforma: I used to live in Riga.",
                 "Noliegums: didn't use to + pamatforma (bez -d): She didn't use to like fish.",
                 "Jautājums: Did + teik. priekšmets + use to + pamatforma? Did you use to play tennis?",
                 "be used to / get used to + lietvārds vai darbības vārds ar -ing: I'm used to getting up early. It took me a month to get used to the cold."],
        "use": ["used to: ieradums vai stāvoklis pagātnē, kas tagad vairs nav spēkā (I used to smoke. He used to be shy).",
                "Nelieto vienam pabeigtam notikumam: lieto Past Simple (We went to Rome last year).",
                "be used to / get used to: kaut kas ir (vai kļūst) ierasts. Tas atšķiras no used to!"],
        "signals": "when I was young, as a child, in those days, now, any more (kad biju jauns, bērnībā, tolaik, tagad, vairs)",
    },
    "articles": {
        "form": ["a / an + vienskaitļa skaitāms lietvārds: a book, an apple (an pirms patskaņa skaņas: an hour, a university).",
                 "the + vienskaitļa, daudzskaitļa vai neskaitāms lietvārds: the book, the books, the water.",
                 "Bez artikula: daudzskaitļa un neskaitāmi lietvārdi vispārīgā nozīmē (Dogs are friendly. I like coffee) un lielākā daļa cilvēku, pilsētu un valstu nosaukumu (Riga, Latvia)."],
        "use": ["a / an: viens no daudziem vai kaut kas, ko piemin pirmoreiz (I saw a film. It was a comedy).",
                "the: kaut kas, ko abi zina, kas jau minēts vai kas ir vienīgais (the film we saw, the sun, the Internet).",
                "the lieto arī ar vispārākās pakāpes formu, upēm, jūrām un dažām valstīm (the best, the Baltic Sea, the UK).",
                "Bez artikula: vispārīgas lietas, ēdienreizes un vietas ar to parasto nozīmi (have breakfast, go to school, at work)."],
        "signals": "first mention, already mentioned, the only one, in general (pirmoreiz, jau minēts, vienīgais, vispārīgi)",
    },
    "quantity": {
        "form": ["some / any + daudzskaitļa vai neskaitāms lietvārds: some apples, any milk.",
                 "many + daudzskaitlis: many people. much + neskaitāms lietvārds: much time. Galvenokārt jautājumos un noliegumos: How many? How much? not many, not much.",
                 "a lot of / lots of + abi veidi, galvenokārt apgalvojumos: a lot of people, a lot of time.",
                 "a few + daudzskaitlis: a few friends. a little + neskaitāms lietvārds: a little time. few / little (bez a) = gandrīz nav.",
                 "enough + lietvārds: enough chairs. Īpašības vārds + enough: big enough. too much / too many = vairāk, nekā vajag."],
        "use": ["some: apgalvojumos un piedāvājumos (Would you like some tea?). any: jautājumos un noliegumos (Do you have any brothers? I don't have any money).",
                "a few / a little = neliels daudzums, pozitīvs vērtējums. few / little = gandrīz nav, negatīvs vērtējums.",
                "too much / too many ir problēma. not enough = mazāk, nekā vajag."],
        "signals": "how many, how much, a few, a little, enough, too much, too many (cik, mazliet, pietiekami, par daudz)",
    },
    "relative_clauses": {
        "form": ["who = cilvēki, which = lietas, that = cilvēki vai lietas: a woman who lives next door, a phone which takes good photos.",
                 "where = vietas, whose = kam pieder: the restaurant where we met, a driver whose car was stolen.",
                 "Palīgteikums bez komatiem (vajadzīgs, lai zinātu, kuru): The woman who called is my boss. Who / which / that var izlaist, ja tas ir papildinātājs: the film we saw.",
                 "Palīgteikums ar komatiem (papildu informācija), ne that: My brother, who lives in Berlin, is a nurse."],
        "use": ["Attieksmes palīgteikums dod vairāk informācijas par lietvārdu un savieno divus teikumus vienā.",
                "Bez komatiem: informācija vajadzīga, lai zinātu, par kuru cilvēku vai lietu runa. Ar komatiem: papildu informācija, ko var izlaist.",
                "Nekad neatkārto papildinātāju: the book that I bought, nevis the book that I bought it."],
        "signals": "who, which, that, where, whose, commas (komati)",
    },
    "time_clauses": {
        "form": ["when / as soon as / until / before / after / while + Present Simple (nevis will) nākotnei: I'll call you when I arrive.",
                 "Laika palīgteikums var būt pirmais (ar komatu) vai otrais: When I arrive, I'll call you. = I'll call you when I arrive.",
                 "Ar after un before iespējams arī Present Perfect: I'll call you after I've finished."],
        "use": ["Virsteikumā ir will / going to vai pavēle; laika palīgteikumā ir tagadne.",
                "when = tajā laikā. as soon as = uzreiz. until = līdz tam brīdim (Wait here until I come back). before / after = kas notiek pirmais. while = vienlaikus."],
        "signals": "then, after that, when, as soon as, until, before, after, while, during, by the time (tad, pēc tam, kad, līdzko, līdz, pirms, pēc, kamēr)",
    },
    "question_tags": {
        "form": ["Apgalvojošs teikums, nolieguma tag: You like tea, don't you?",
                 "Noliegts teikums, apgalvojošs tag: She isn't here, is she?",
                 "Tag atkārto palīgdarbības vārdu: is / are / was / were, have / has, can, will, should. Ar Present Simple un Past Simple: do / does / did.",
                 "Īpašie gadījumi: I am → aren't I? Let's → shall we? Pavēle → will you? Nobody / nothing → apgalvojošs tag ar they / it."],
        "use": ["Balss krītas: esi pārliecināts un gaidi piekrišanu (It's cold, isn't it?).",
                "Balss ceļas: neesi drošs un tiešām jautā (You're not working today, are you?).",
                "Tag ir tajā pašā laikā kā teikums: He went home, didn't he?"],
        "signals": "isn't it? don't you? can't he? will you? aren't I? (īss jautājums teikuma beigās)",
    },
    "subject_object_q": {
        "form": ["Jautājums par papildinātāju ar lielāko daļu darbības vārdu Present vai Past Simple: jautājamais vārds + do / does / did + teik. priekšmets + pamatforma: Who did you meet? What does she want? Ar citu palīgdarbības vārdu vai modālo vārdu tas ir pirmais: What are you doing? Who can you see?",
                 "Neitrāls jautājums par teikuma priekšmetu: jautājamais vārds pats ir teik. priekšmets, bez do / does / did: Who met you? What happened? Who wants coffee? (Tikai uzsvaram: Who did call?)",
                 "Darbības vārds paliek parastajā formā: Who lives here? (ar -s), nevis Who does live here?"],
        "use": ["Jautā par cilvēku vai lietu, kas veic darbību: jautājums par teikuma priekšmetu (Tom called me → Who called you?).",
                "Jautā par cilvēku vai lietu, ar ko darbība notiek: jautājums par papildinātāju (I called Tom → Who did you call?).",
                "Paskaties uz atbildi: ja atbilde ir teik. priekšmets, neitrālajā jautājumā nav did / does."],
        "signals": "who, what, which, whose as the subject: no do / does / did (kā teik. priekšmets: bez do / does / did)",
    },
    "verb_patterns": {
        "form": ["darbības vārds + -ing: enjoy, finish, keep, avoid, mind, suggest, practise (I enjoy reading. She suggested going home.)",
                 "darbības vārds + to + pamatforma: want, need, decide, hope, plan, learn, agree, promise, manage, refuse (I want to leave. He decided to stay.)",
                 "prievārds + -ing: interested in learning, good at cooking, before leaving, thank you for helping.",
                 "Daži darbības vārdi der ar abiem ar ļoti līdzīgu nozīmi: like, love, hate, start, begin (I like swimming. ≈ I like to swim. Uzsvars var atšķirties.)",
                 "Atšķirīga nozīme: stop / remember / forget / try + -ing vai to (I stopped smoking = es atmetu. I stopped to smoke = es apstājos, lai nosmēķētu.)"],
        "use": ["Darbības vārds nosaka formu: iemācies, kuri vārdi iet ar -ing un kuri ar to.",
                "Aiz prievārda lieto -ing, ja tieši seko darbības vārds: She's good at drawing. (Var sekot arī jautājamais vārds + to: about how to improve it.)",
                "stop / remember / forget / try: -ing = par jau izdarītu vai izmēģinājumu; to = uzdevums vai mērķis."],
        "signals": "enjoy, avoid, finish + -ing; want, decide, hope + to; after a preposition: -ing (aiz prievārda: -ing)",
    },
}


# Latvian words without Latvian letters that the italics rule would take for English examples. Added only while the cards of these topics and the drafts are marked,
# so the markup of the published explanations stays exactly as it was.
LV_WORDS = set("""ieradums vienam pabeigtam notikumam tikai ne ierasts biju jauns tolaik artikula valstu nosaukumu viens daudziem piemin pirmoreiz zina lietas vietas veidi apgalvojumos
mazliet pietiekami daudz kuru komatiem izlaist papildu attieksmes dod lietu pirmais otrais tagadne tam noliegts balss esi gaidi neesi pats paliek veic paskaties abiem atmetu nosaka kuri komati
kam pieder nolieguma jautajums darbibas vards verbs lietvards nosaukums laiks laika piemers piemeri atbilde atbildes nozime forma formas uzdevums merkis pieredze pienakums iespeja""".split())


# ───────── second batch: more structures the B1 reference teaches ─────────
AREAS_NEW.append(("adjectives", "Adjectives and adverbs"))
SKILLS_NEW.extend([
    ("more_modals", "More modals: might, could, be able to", "modals", ["A2.2", "B1.1", "B1.2"]),
    ("passive_modals", "Passive with modals (must be done)", "passive", ["B1.1", "B1.2"]),
    ("causative", "Causative: have something done", "patterns", ["B1.1", "B1.2"]),
    ("two_objects", "Verbs with two objects (give me, tell her)", "patterns", ["A2.2", "B1.1"]),
    ("adj_ed_ing", "-ed or -ing adjectives (bored, boring)", "adjectives", ["A2.2", "B1.1"]),
    ("adj_order", "Adjective order (a small old car)", "adjectives", ["A2.1", "B1.1", "B1.2"]),   # A2.1: adjective before the noun, after be, no plural, prepared tasks only (teacher, 15 November, batch 5)
    ("adverbs", "Adverbs: manner, frequency, degree", "adjectives", ["A2.2", "B1.1", "B1.2"]),
    ("so_such", "So and such", "adjectives", ["B1.1", "B1.2"]),
    ("indefinite_pronouns", "Someone, anything, nobody", "nouns", ["A2.2", "B1.1"]),
])
ABBR_NEW.update({"more_modals": "mm", "passive_modals": "pmo", "causative": "cau", "two_objects": "two", "adj_ed_ing": "aei", "adj_order": "aor", "adverbs": "adv", "so_such": "ssu", "indefinite_pronouns": "ind"})

CARDS.update({
    "more_modals": {
        "form": ["*might / may / could* + base verb = possible: *It might rain. She may be late. He could be at home.*",
                 "Negative: *might not / may not* + base verb: *They might not come.* *can't* = I am sure it is not true.",
                 "*be able to* + base verb = *can* in other tenses: *I was able to finish. She will be able to help. I haven't been able to call.*",
                 "*could* = ability in general in the past (*I could swim at five*). *was able to* = one success (*I was able to catch the bus*).",
                 "*needn't* + base verb = not necessary: *You needn't wait.* *needn't have* + 3. form = I did it, but it was not necessary: *We needn't have hurried.*",
                 "*be allowed to* + base verb = permission: *We are allowed to park here. Children weren't allowed to enter.*"],
        "use": ["*might / may / could*: something is possible and we are not sure. *must*: we are sure it is true. *can't*: we are sure it is not true.",
                "*can* has no future or perfect form: use *be able to* (*I'll be able to come on Friday*).",
                "*needn't* (or *don't need to / don't have to*) = not necessary. *mustn't* = not allowed.",
                "*be allowed to* = permission from a rule or a person. *can* is shorter, but it has no past or future form."],
        "signals": "*perhaps, maybe, possibly, one time, not necessary, rules, allowed*",
        "example": "*It might rain, so you needn't water the plants.*",
    },
    "passive_modals": {
        "form": ["modal + *be* + 3. form: *The report must be finished today. Tickets can be bought online.*",
                 "Negative: modal + *not* + *be* + 3. form: *It can't be repaired. Shoes mustn't be worn inside.*",
                 "Question: modal + subject + *be* + 3. form? *Can this be done? Should the door be locked?*",
                 "Past: modal + *have been* + 3. form: *The window should have been closed. The accident could have been avoided.*"],
        "use": ["We use the passive with a modal for rules, advice, possibility and ability when the doer is not important (*Tickets can be bought online*).",
                "The modal stays the same: *must / should / can / could / might / will / ought to / has to* + *be* + 3. form.",
                "The doer can be added with *by*: *This must be signed by the manager.*"],
        "signals": "*must be, can be, should be, ought to be, has to be, should have been*",
        "example": "*The tickets can be bought online, but they must be paid for today.*",
    },
    "causative": {
        "form": ["*have* + object + 3. form: *I had my hair cut. She is having her car repaired.*",
                 "*get* + object + 3. form is more informal: *We got the windows cleaned.*",
                 "Questions and negatives with *do / does / did*: *Do you have your car washed? I didn't have it checked.*",
                 "The doer is usually not named; with *by*: *I had my passport checked by the police.*"],
        "use": ["Someone does a service for us (we ask or pay): *I had my laptop fixed* = someone fixed it for me.",
                "Compare: *I cut my hair* = I did it. *I had my hair cut* = a hairdresser did it.",
                "It can also mean something bad happens to us: *He had his wallet stolen.*",
                "Common services: haircut, car repair, photo, dentist, delivery, painting, cleaning."],
        "signals": "*have / get something done, hairdresser, mechanic, dentist, repaired, cut*",
        "example": "*We had the kitchen painted last month, and next week we're getting the roof repaired.*",
    },
    "two_objects": {
        "form": ["verb + person + thing: *She gave me a present. He sent his mother a letter.*",
                 "verb + thing + *to / for* + person: *She gave a present to me. He bought a gift for his mother.*",
                 "*to*: give, send, show, tell, lend, offer, pay, teach, write, bring. *for*: buy, make, cook, find, get, keep, save.",
                 "When the thing is a pronoun, use *to / for*: *Show it to me.* (not *Show me it*)"],
        "use": ["Both patterns have the same meaning. We often put the person first (*She told me a story*) and use *to / for* when the thing is more important.",
                "*explain, suggest, describe, introduce*: always the thing first: *She explained the problem to me.* (not *She explained me the problem*)"],
        "signals": "*give, send, show, tell, lend, buy, make, to, for*",
        "example": "*I bought my sister a book, and I gave it to her yesterday.*",
    },
    "adj_ed_ing": {
        "form": ["*-ing* adjective: the thing or person that causes the feeling: *a boring film, an interesting book, a tiring day.*",
                 "*-ed* adjective: the person who has the feeling: *I am bored. She was interested. We felt tired.*",
                 "Pairs: *bored / boring, interested / interesting, excited / exciting, tired / tiring, surprised / surprising, annoyed / annoying, confused / confusing.*"],
        "use": ["*The film was boring* (it causes the feeling). *The audience was bored* (they have the feeling).",
                "A person can cause the feeling too: *He is boring* (he makes others bored). *He is bored* (he feels bored).",
                "After *be / feel / look / seem*: *She looks tired* (she is tired). *The lesson is tiring* (it makes us tired)."],
        "signals": "*feel, felt, seem, a film, a lesson, a story, a day*",
        "example": "*I was so bored because the film was really boring.*",
    },
    "adj_order": {
        "form": ["Opinion before fact: *a lovely old house* (not *an old lovely house*).",
                 "Order of facts: size, age, shape, colour, origin, material, then the noun: *a small old round red Italian wooden table.*",
                 "Before a noun we usually use two or three adjectives. After *be* we can use *and*: *The room is big, bright and cheap.*",
                 "Adjectives have no plural form: *two small boxes* (not *two smalls boxes*)."],
        "use": ["Remember: opinion, size, age, shape, colour, origin, material, noun.",
                "*a big red Spanish car* sounds natural. *a Spanish red big car* does not."],
        "signals": "*opinion, size, age, colour, origin, material*",
        "example": "*She bought a beautiful small black leather bag.*",
    },
    "adverbs": {
        "form": ["Manner: adjective + *-ly*: *slow - slowly, careful - carefully, easy - easily, happy - happily.* Irregular: *good - well, fast - fast, hard - hard, late - late.*",
                 "Frequency: *always, usually, often, sometimes, never*. Before the main verb, after *be*: *She often walks. He is always late.*",
                 "Degree: *very, really, quite, extremely, too* + adjective or adverb: *very quickly, quite cold.* *enough* comes after the adjective: *warm enough.*",
                 "Position: manner adverbs go after the verb or the object: *She speaks English well. He drove the car carefully.*"],
        "use": ["Adjectives describe nouns (*a quick answer*). Adverbs describe verbs, adjectives and other adverbs (*She answered quickly*).",
                "After *be, look, feel, seem, sound* we use an adjective: *She looks happy.* (not *happily*)",
                "*hard* = with effort (*work hard*), *hardly* = almost not (*I can hardly see*). *late* = not on time, *lately* = recently.",
                "Extreme adjectives (*perfect, amazing, exhausted*) take *absolutely / completely*, not *very*."],
        "signals": "*-ly, always, never, very, quite, too, enough, absolutely*",
        "example": "*He drives carefully, and he never drives too fast.*",
    },
    "so_such": {
        "form": ["*so* + adjective or adverb: *The film was so long. He runs so fast.*",
                 "*such* + (*a / an*) + (adjective) + noun: *It was such a long film. They are such nice people.*",
                 "*so much / so many* + noun: *so much noise, so many people.*",
                 "Result: *so / such ... that*: *It was so cold that we stayed inside. It was such a cold day that we stayed inside.*"],
        "use": ["*so* goes before an adjective or adverb with no noun; *such* goes before a noun (with or without an adjective).",
                "*such* + plural or uncountable noun has no *a / an*: *such good friends, such bad weather.*",
                "*so / such ... that* tells us the result."],
        "signals": "*so, such, so much, so many, that (result)*",
        "example": "*It was such a cold day that we stayed in, and we were so tired.*",
    },
    "indefinite_pronouns": {
        "form": ["*some-* (positive): *someone, somebody, something, somewhere.* *any-* (questions and negatives): *anyone, anybody, anything, anywhere.* *no-*: *no one, nobody, nothing, nowhere.* *every-*: *everyone, everybody, everything, everywhere.*",
                 "They take a singular verb: *Everyone is here. Nothing has changed.*",
                 "With a negative verb we use *any-*, not *no-*: *I don't know anything.* (not *I don't know nothing*)",
                 "Offers and requests: *Would you like something to drink?* (*some-*). Questions: *Is there anyone here?*",
                 "We use *they / their* for *somebody, anybody, everybody, nobody*: *Everybody did their best.*"],
        "use": ["*some-* when we expect yes (offers, requests) or the thing exists; *any-* in questions and negatives or when it does not matter (*Anyone can join*).",
                "*no-* already makes the sentence negative: no double negative.",
                "*everyone / everybody* = all the people; *every one* = each single one of a group."],
        "signals": "*someone, anything, nobody, everything, anywhere, nowhere*",
        "example": "*Everybody was there, but nobody said anything.*",
    },
})

LV_CARDS.update({
    "more_modals": {
        "form": ["might / may / could + pamatforma = iespējams: It might rain. She may be late. He could be at home.",
                 "Noliegums: might not / may not + pamatforma: They might not come. can't = esmu pārliecināts, ka tā nav.",
                 "be able to + pamatforma = can citos laikos: I was able to finish. She will be able to help. I haven't been able to call.",
                 "could = spēja pagātnē vispār (I could swim at five). was able to = viens panākums (I was able to catch the bus).",
                 "needn't + pamatforma = nav vajadzības: You needn't wait. needn't have + 3. forma = es to izdarīju, bet nevajadzēja: We needn't have hurried.",
                 "be allowed to + pamatforma = atļauts: We are allowed to park here. Children weren't allowed to enter."],
        "use": ["might / may / could: kaut kas ir iespējams, bet neesam droši. must: esam pārliecināti, ka tā ir. can't: esam pārliecināti, ka tā nav.",
                "can nav nākotnes un perfekta formas: lieto be able to (I'll be able to come on Friday).",
                "needn't (vai don't need to / don't have to) = nav nepieciešams. mustn't = aizliegts.",
                "be allowed to = atļauja no noteikuma vai cilvēka. can ir īsāks, bet tam nav pagātnes un nākotnes formas."],
        "signals": "perhaps, maybe, possibly, one time, not necessary, rules, allowed (varbūt, iespējams, vienu reizi, nav vajadzības, noteikumi, atļauts)",
    },
    "passive_modals": {
        "form": ["modālais darbības vārds + be + 3. forma: The report must be finished today. Tickets can be bought online.",
                 "Noliegums: modālais darbības vārds + not + be + 3. forma: It can't be repaired. Shoes mustn't be worn inside.",
                 "Jautājums: modālais darbības vārds + teik. priekšmets + be + 3. forma? Can this be done? Should the door be locked?",
                 "Pagātne: modālais darbības vārds + have been + 3. forma: The window should have been closed. The accident could have been avoided."],
        "use": ["Ciešamo kārtu ar modālo darbības vārdu lieto noteikumiem, padomiem, iespējai un spējai, kad darītājs nav svarīgs (Tickets can be bought online).",
                "Modālais darbības vārds nemainās: must / should / can / could / might / will / ought to / has to + be + 3. forma.",
                "Darītāju var pievienot ar by: This must be signed by the manager."],
        "signals": "must be, can be, should be, ought to be, has to be, should have been (jābūt, var būt, vajadzētu būt)",
    },
    "causative": {
        "form": ["have + papildinātājs + 3. forma: I had my hair cut. She is having her car repaired.",
                 "get + papildinātājs + 3. forma ir sarunvalodā: We got the windows cleaned.",
                 "Jautājumi un noliegumi ar do / does / did: Do you have your car washed? I didn't have it checked.",
                 "Darītāju parasti nenosauc; ar by: I had my passport checked by the police."],
        "use": ["Kāds mums veic pakalpojumu (mēs lūdzam vai maksājam): I had my laptop fixed = kāds man to salaboja.",
                "Salīdzini: I cut my hair = es pats to izdarīju. I had my hair cut = frizieris to izdarīja.",
                "Tas var nozīmēt arī nepatīkamu notikumu: He had his wallet stolen.",
                "Biežākie pakalpojumi: matu griešana, auto remonts, fotogrāfija, zobārsts, piegāde, krāsošana, tīrīšana."],
        "signals": "have / get something done, hairdresser, mechanic, dentist, repaired, cut (frizieris, mehāniķis, zobārsts, salabots, apgriezts)",
    },
    "two_objects": {
        "form": ["darbības vārds + cilvēks + lieta: She gave me a present. He sent his mother a letter.",
                 "darbības vārds + lieta + to / for + cilvēks: She gave a present to me. He bought a gift for his mother.",
                 "to: give, send, show, tell, lend, offer, pay, teach, write, bring. for: buy, make, cook, find, get, keep, save.",
                 "Ja lieta ir vietniekvārds, lieto to / for: Show it to me. (nevis Show me it)"],
        "use": ["Abām konstrukcijām ir viena nozīme. Bieži cilvēku liek pirmo (She told me a story) un lieto to / for, kad lieta ir svarīgāka.",
                "explain, suggest, describe, introduce: vienmēr vispirms lieta: She explained the problem to me. (nevis She explained me the problem)"],
        "signals": "give, send, show, tell, lend, buy, make, to, for (dot, sūtīt, parādīt, pastāstīt, aizdot, pirkt, taisīt)",
    },
    "adj_ed_ing": {
        "form": ["-ing īpašības vārds: lieta vai cilvēks, kas izraisa sajūtu: a boring film, an interesting book, a tiring day.",
                 "-ed īpašības vārds: cilvēks, kuram ir šī sajūta: I am bored. She was interested. We felt tired.",
                 "Pāri: bored / boring, interested / interesting, excited / exciting, tired / tiring, surprised / surprising, annoyed / annoying, confused / confusing."],
        "use": ["The film was boring (tā izraisa sajūtu). The audience was bored (cilvēkiem ir šī sajūta).",
                "Sajūtu var izraisīt arī cilvēks: He is boring (viņš citiem liek garlaikoties). He is bored (viņam ir garlaicīgi).",
                "Aiz be / feel / look / seem: She looks tired (viņa ir noguruse). The lesson is tiring (tā nogurdina)."],
        "signals": "feel, felt, seem, a film, a lesson, a story, a day (just, šķist, filma, stunda, stāsts, diena)",
    },
    "adj_order": {
        "form": ["Vispirms viedoklis, pēc tam fakti: a lovely old house (nevis an old lovely house).",
                 "Faktu secība: izmērs, vecums, forma, krāsa, izcelsme, materiāls, tad lietvārds: a small old round red Italian wooden table.",
                 "Pirms lietvārda parasti lieto divus vai trīs īpašības vārdus. Aiz be var lietot and: The room is big, bright and cheap.",
                 "Īpašības vārdiem nav daudzskaitļa formas: two small boxes (nevis two smalls boxes)."],
        "use": ["Atceries: viedoklis, izmērs, vecums, forma, krāsa, izcelsme, materiāls, lietvārds.",
                "a big red Spanish car skan dabiski. a Spanish red big car neskan."],
        "signals": "opinion, size, age, colour, origin, material (viedoklis, izmērs, vecums, krāsa, izcelsme, materiāls)",
    },
    "adverbs": {
        "form": ["Veids: īpašības vārds + -ly: slow - slowly, careful - carefully, easy - easily, happy - happily. Neregulāri: good - well, fast - fast, hard - hard, late - late.",
                 "Biežums: always, usually, often, sometimes, never. Pirms darbības vārda, aiz be: She often walks. He is always late.",
                 "Pakāpe: very, really, quite, extremely, too + īpašības vārds vai apstākļa vārds: very quickly, quite cold. enough ir aiz īpašības vārda: warm enough.",
                 "Vieta teikumā: veida apstākļa vārds ir aiz darbības vārda vai papildinātāja: She speaks English well. He drove the car carefully."],
        "use": ["Īpašības vārdi apraksta lietvārdus (a quick answer). Apstākļa vārdi apraksta darbības vārdus, īpašības vārdus un citus apstākļa vārdus (She answered quickly).",
                "Aiz be, look, feel, seem, sound lieto īpašības vārdu: She looks happy. (nevis happily)",
                "hard = ar pūlēm (work hard), hardly = gandrīz nē (I can hardly see). late = novēloti, lately = nesen.",
                "Ar galējiem īpašības vārdiem (perfect, amazing, exhausted) lieto absolutely / completely, nevis very."],
        "signals": "-ly, always, never, very, quite, too, enough, absolutely (vienmēr, nekad, ļoti, diezgan, pārāk, pietiekami)",
    },
    "so_such": {
        "form": ["so + īpašības vārds vai apstākļa vārds: The film was so long. He runs so fast.",
                 "such + (a / an) + (īpašības vārds) + lietvārds: It was such a long film. They are such nice people.",
                 "so much / so many + lietvārds: so much noise, so many people.",
                 "Sekas: so / such ... that: It was so cold that we stayed inside. It was such a cold day that we stayed inside."],
        "use": ["so lieto pirms īpašības vārda vai apstākļa vārda bez lietvārda; such — pirms lietvārda (ar īpašības vārdu vai bez tā).",
                "such + daudzskaitlis vai neskaitāms lietvārds bez a / an: such good friends, such bad weather.",
                "so / such ... that parāda sekas."],
        "signals": "so, such, so much, so many, that (result) (tik, tāds, tik daudz, ka)",
    },
    "indefinite_pronouns": {
        "form": ["some- (apgalvojumos): someone, somebody, something, somewhere. any- (jautājumos un noliegumos): anyone, anybody, anything, anywhere. no-: no one, nobody, nothing, nowhere. every-: everyone, everybody, everything, everywhere.",
                 "Tiem seko vienskaitļa darbības vārds: Everyone is here. Nothing has changed.",
                 "Ar noliegtu darbības vārdu lieto any-, nevis no-: I don't know anything. (nevis I don't know nothing)",
                 "Piedāvājumos un lūgumos: Would you like something to drink? (some-). Jautājumos: Is there anyone here?",
                 "Ar somebody, anybody, everybody, nobody lieto they / their: Everybody did their best."],
        "use": ["some- lieto, kad gaidām atbildi jā (piedāvājumi, lūgumi) vai kad kaut kas pastāv; any- jautājumos un noliegumos vai kad nav svarīgi (Anyone can join).",
                "no- jau veido noliegumu: dubultā noliegumu nelieto.",
                "everyone / everybody = visi cilvēki; every one = katrs atsevišķi no grupas."],
        "signals": "someone, anything, nobody, everything, anywhere, nowhere (kāds, kaut kas, neviens, viss, kaut kur, nekur)",
    },
})


# ───────── third batch (teacher's plan, 25 October): A2 topics built around frequent mistakes (docs/ERROR-TYPES.md) ─────────
SKILLS_NEW.extend([
    ("dep_prepositions", "Prepositions after words (listen to, good at)", "prepositions", ["A2.1", "A2.2", "B1.1"]),
    ("agreement", "Subject and verb (my friend lives, my friends live)", "active", ["A2.1", "A2.2", "B1.2"]),   # B1.2: each / every / all / whole, prepared tasks only (teacher, 15 November)
    ("irregular_plurals", "Irregular plurals (children, people, men, teeth)", "nouns", ["A2.1", "A2.2"]),
])
ABBR_NEW.update({"dep_prepositions": "dpr", "agreement": "agr", "irregular_plurals": "ipl"})

CARDS.update({
    "dep_prepositions": {
        "form": ["Some words always go with the same preposition. Learn them in pairs: *listen to, wait for, look at, talk to, ask for, pay for, belong to, depend on, think about.*",
                 "Adjectives too: *good at, afraid of, interested in, proud of, different from.*",
                 "Some verbs take no preposition: *call me, help me, meet you, join the team, answer the question.*"],
        "use": ["After the preposition comes a noun or a pronoun: *Listen to me. I'm waiting for the bus.*",
                "In a question the preposition often goes to the end: *What are you looking at? Who are you waiting for?*"],
        "signals": "*listen to music, wait for the bus, good at maths, call me*",
        "example": "*I'm waiting for Anna. She's good at maths, but she's afraid of dogs.*",
    },
    "agreement": {   # rewritten 28 October from the grammar books (Murphy: singular and plural, there is / are, each / every, one of)
        "form": ["One person or thing + verb-*s*: *My friend lives in Riga.*",
                 "More than one + verb: *My friends live in Riga.*",
                 "One: *is / was / has / does*. More: *are / were / have / do*. *She has a car. They have two.*"],
        "use": ["*and* makes more than one: *Tom and Anna live here.*",
                "*everybody, nobody, something, everyone* + verb-*s*: *Everybody knows. Nothing works.*"],
        "watch": ["The verb agrees with the main word, not the nearest one: *The box of apples is heavy. The people in my office are nice.*",
                  "*each / every* + one: *Every student has a book.*",
                  "*one of* + plural noun + verb-*s*: *One of my friends lives in London.*",
                  "Uncountable words are singular: *The news is good. Money isn't everything. This information is useful.*",
                  "Some words are always plural: *People are friendly. The police are here. My jeans are new.*",
                  "*there is* + one or uncountable, *there are* + more: *There is some milk. There are two cafés.*"],
        "signals": "*he, she, it, everybody, nobody, every, one of, and, there is / there are*",
        "example": "*Everybody in my family likes coffee, but my parents drink tea.*",
    },
    "irregular_plurals": {
        "form": ["Most nouns add *-s*: *a book, two books*. These change: *child → children, person → people, man → men, woman → women, tooth → teeth, foot → feet, mouse → mice.*",
                 "No extra *-s*: *children*, not *childrens*; *teeth*, not *tooths*.",
                 "*police* has no *-s*, but it is always plural: *The police are here.*"],
        "use": ["These words take a plural verb: *The children are tired. People like it. My feet hurt.*"],
        "signals": "*child, person, man, woman, tooth, foot, mouse, police*",
        "example": "*One mouse is cute, but ten mice are a problem!*",
    },
})

LV_CARDS.update({
    "dep_prepositions": {
        "form": ["Daži vārdi vienmēr iet kopā ar savu prievārdu. Tos mācās pa pāriem: listen to, wait for, look at, talk to, ask for, pay for, belong to, depend on, think about.",
                 "Arī īpašības vārdi: good at, afraid of, interested in, proud of, different from.",
                 "Daži darbības vārdi ir bez prievārda: call me, help me, meet you, join the team, answer the question."],
        "use": ["Aiz prievārda ir lietvārds vai vietniekvārds: Listen to me. I'm waiting for the bus.",
                "Jautājumā prievārds bieži ir beigās: What are you looking at? Who are you waiting for?"],
        "signals": "listen to music, wait for the bus, good at maths, call me (klausīties mūziku, gaidīt autobusu, viņai padodas matemātika, piezvani man)",
    },
    "agreement": {
        "form": ["Viens cilvēks vai lieta + darbības vārds ar -s: My friend lives in Riga.",
                 "Vairāki + darbības vārds bez -s: My friends live in Riga.",
                 "Vienam: is / was / has / does. Vairākiem: are / were / have / do. She has a car. They have two."],
        "use": ["Latviski draugs dzīvo un draugi dzīvo: forma ir viena. Angliski tā mainās: lives / live.",
                "and nozīmē vairākus: Tom and Anna live here. everybody, nobody, something, everyone lieto ar -s: Everybody knows."],
        "watch": ["Darbības vārds saskaņojas ar galveno vārdu, nevis ar tuvāko: The box of apples is heavy. The people in my office are nice.",
                  "each / every + viens: Every student has a book.",
                  "one of + daudzskaitlis + darbības vārds ar -s: One of my friends lives in London.",
                  "Nesaskaitāmie vārdi ir vienskaitlī: The news is good. Money isn't everything. Latviski ziņas ir daudzskaitlī, angliski news ir vienskaitlī.",
                  "Daži vārdi vienmēr ir daudzskaitlī: People are friendly. The police are here. My jeans are new.",
                  "there is + viens vai nesaskaitāms, there are + vairāki: There is some milk. There are two cafés."],
        "signals": "he, she, it, everybody, nobody, every, one of, and, there is / there are (viņš, viņa, visi, neviens, katrs, viens no, un, ir)",
    },
    "irregular_plurals": {
        "form": ["Lielākajai daļai lietvārdu pievieno -s: a book, two books. Šie mainās: child → children, person → people, man → men, woman → women, tooth → teeth, foot → feet, mouse → mice.",
                 "Bez papildu -s: children, nevis childrens; teeth, nevis tooths.",
                 "police ir bez -s, bet vienmēr daudzskaitlī: The police are here."],
        "use": ["Ar šiem vārdiem lieto daudzskaitļa darbības vārdu: The children are tired. People like it. My feet hurt."],
        "signals": "child, person, man, woman, tooth, foot, mouse, police (bērns, cilvēks, vīrietis, sieviete, zobs, pēda, pele, policija)",
    },
})


# ───────── fourth batch (teacher, 28 October): missing A2 topics, one at a time ─────────
AREAS_NEW.append(("prepositions", "Prepositions"))
SKILLS_NEW.append(("prep_time_place", "Prepositions of time and place (in, on, at)", "prepositions", ["A2.1", "A2.2"]))
ABBR_NEW.update({"prep_time_place": "ptp"})
CARDS.update({
    "prep_time_place": {
        "form": ["Time: *at* + clock time (*at 7*), *on* + day or date (*on Monday, on 5 May*), *in* + month, year, season or part of the day (*in May, in 2020, in winter, in the morning*). But *at night*.",
                 "No preposition before *tomorrow, yesterday* and *next / last / this / every* + time: *See you next Monday.*",
                 "Place: *at* + a point or a place where you do something (*at the bus stop, at work, at home*), *in* + inside or an area (*in the fridge, in my bag, in Riga*), *on* + a surface (*on the table, on the wall, on the third floor*)."],
        "use": ["Ask: is it a clock time, a day or a longer period? Is it a point, inside something, or on a surface?"],
        "signals": "*at 7, on Monday, in May, at night, at work, in the kitchen, on the wall*",
        "example": "*I start work at 9 on Mondays, but in summer I work from home.*",
    },
})
LV_CARDS.update({
    "prep_time_place": {
        "form": ["Laiks: at + pulksteņa laiks (at 7), on + diena vai datums (on Monday, on 5 May), in + mēnesis, gads, gadalaiks vai dienas daļa (in May, in 2020, in winter, in the morning). Bet at night.",
                 "Bez prievārda pirms tomorrow, yesterday un next / last / this / every + laiks: See you next Monday.",
                 "Vieta: at + punkts vai vieta, kur kaut ko dara (at the bus stop, at work, at home), in + iekšā vai teritorija (in the fridge, in my bag, in Riga), on + uz virsmas (on the table, on the wall, on the third floor)."],
        "use": ["Pajautā sev: vai tas ir pulksteņa laiks, diena vai ilgāks laiks? Vai tas ir punkts, kaut kā iekšā vai uz virsmas?"],
        "signals": "at 7, on Monday, in May, at night, at work, in the kitchen, on the wall (septiņos, pirmdien, maijā, naktī, darbā, virtuvē, pie sienas)",
    },
})

# ───────── auxiliary verbs (teacher, 28 October): Are you / Do you / Did you / Have you get mixed up ─────────
SKILLS_NEW.append(("aux_verbs", "Auxiliary verbs: be, do, have (Are you…? Do you…? Have you…?)", "questions", ["A2.1", "A2.2", "B1.1"]))
ABBR_NEW.update({"aux_verbs": "aux"})
CARDS.update({
    "aux_verbs": {
        "form": ["*be* with *-ing*, adjectives and places: *Are you working? Is she tired?*",
                 "*do / does / did* with other verbs in the present and past simple: *Do you work here? Did you see it?*",
                 "*have / has* with the 3rd form (present perfect): *Have you seen it?*"],
        "use": ["Questions, negatives and short answers need the auxiliary: *Are you…? I don't… Yes, I have.*"],
        "signals": "*am, is, are, was, were, do, does, did, have, has*",
        "example": "*Are you hungry? Do you want a sandwich? Have you eaten today?*",
    },
})
LV_CARDS.update({
    "aux_verbs": {
        "form": ["be ar -ing, īpašības vārdiem un vietām: Are you working? Is she tired?",
                 "do / does / did ar citiem darbības vārdiem Present Simple un Past Simple: Do you work here? Did you see it?",
                 "have / has ar 3. formu (Present Perfect): Have you seen it?"],
        "use": ["Jautājumos, noliegumos un īsajās atbildēs vajag palīgdarbības vārdu: Are you…? I don't… Yes, I have."],
        "signals": "am, is, are, was, were, do, does, did, have, has",
    },
})


# ───────── comparing past tenses (teacher, 29 October; Murphy, English Grammar in Use, Units 6, 13-16) ─────────
SKILLS_NEW.extend([
    ("cmp_ps_pc", "Past simple or past continuous", "active", ["A2.2", "B1.1"]),
    ("cmp_pp_ps", "Present perfect or past simple", "active", ["A2.2", "B1.1"]),
    ("narrative", "Narrative tenses: past simple, past continuous, past perfect", "active", ["B1.1", "B1.2"]),
    ("narrative_b2", "Narrative tenses with past perfect continuous", "active", ["B2.1", "B2.2"]),
])
ABBR_NEW.update({"cmp_ps_pc": "cpc", "cmp_pp_ps": "cpp", "narrative": "nar", "narrative_b2": "nr2"})
CARDS.update({
    "cmp_ps_pc": {"form": ["*was / were* + *-ing*: in the middle of an action. Past simple: a complete action."],
                  "use": ["*We were walking home when I met Dan.*"], "signals": "*when, while, at 10.30*", "example": "*Matt phoned while we were having dinner.*"},
    "cmp_pp_ps": {"form": ["*have / has* + 3rd form: the situation now. Past simple: only the past."],
                  "use": ["*Tom has lost his key. Tom lost his key yesterday.*"], "signals": "*yesterday, ago, today, since*", "example": "*I've burnt myself. How did you do that?*"},
    "narrative": {"form": ["Past continuous: the background. Past simple: the events. Past perfect: what happened before."],
                  "use": ["*When Sarah arrived, Paul had gone home.*"], "signals": "*when, already, by the time*", "example": "*When we got home, somebody had broken into the flat.*"},
    "narrative_b2": {"form": ["*had been* + *-ing*: an activity that went on before a moment in the past."],
                     "use": ["*It had been raining, so the ground was wet.*"], "signals": "*for, since, all day, how long*", "example": "*We'd been playing for half an hour when it started to rain.*"},
})
LV_CARDS.update({
    "cmp_ps_pc": {"form": ["was / were + -ing: darbības vidū. Past Simple: pabeigta darbība."], "use": ["We were walking home when I met Dan."], "signals": "when, while, at 10.30"},
    "cmp_pp_ps": {"form": ["have / has + 3. forma: situācija tagad. Past Simple: tikai pagātne."], "use": ["Tom has lost his key. Tom lost his key yesterday."], "signals": "yesterday, ago, today, since"},
    "narrative": {"form": ["Past Continuous: fons. Past Simple: notikumi. Past Perfect: kas notika pirms tam."], "use": ["When Sarah arrived, Paul had gone home."], "signals": "when, already, by the time"},
    "narrative_b2": {"form": ["had been + -ing: darbība, kas notika pirms kāda brīža pagātnē."], "use": ["It had been raining, so the ground was wet."], "signals": "for, since, all day, how long"},
})

# ───────── articles split in two, like Murphy (teacher, 29 October): a/an and the at A2, the or no article at B1 ─────────
SKILLS_NEW.append(("articles_b1", "The or no article (school, the school)", "nouns", ["B1.1", "B1.2"]))
ABBR_NEW.update({"articles_b1": "art2"})
CARDS.update({
    "articles_b1": {"form": ["No article: things in general, meals, languages, places used for their purpose, most countries. *the*: a particular one."],
                    "use": ["*I like coffee. I like the coffee you made.*"], "signals": "*in general, school, work, bed, the Alps, the poor*",
                    "example": "*Children love games. The children in my class love games.*"},
})
LV_CARDS.update({
    "articles_b1": {"form": ["Bez artikula: vispārīgi, ēdienreizes, valodas, vietas to nolūkam, vairums valstu. the: konkrēts."],
                    "use": ["I like coffee. I like the coffee you made."], "signals": "in general, school, work, bed, the Alps, the poor"},
})

# ───────── joining ideas (teacher, 2 November; scope from test-english.com A1, A2, B1, B1+; Murphy Units 64, 113) ─────────
SKILLS_NEW.extend([
    ("conj_basic", "And, but, or, so, because", "clauses", ["A2.1", "A2.2"]),
    ("conj_linkers", "However, although, because of", "clauses", ["A2.2", "B1.1"]),   # then / while / before: now in time_clauses (teacher, 22 November)
    ("conj_clauses", "Contrast, purpose and reason (although, despite, so that)", "clauses", ["A2.2", "B1.1", "B1.2", "B2.1"]),   # A2.2: purpose with to and for, prepared tasks only (teacher, 15 November, batch 5)
])
ABBR_NEW.update({"conj_basic": "cj1", "conj_linkers": "cj2", "conj_clauses": "cj3"})
CARDS.update({
    "conj_basic": {"form": ["*and* = similar information, *but* = contrast, *or* = choice, *so* = result, *because* = reason."],
                   "use": ["*The shop was closed, so I went home. I went home because the shop was closed.*"], "signals": "*and, but, or, so, because*",
                   "example": "*It was late, so we left.*"},
    "conj_linkers": {"form": ["Contrast: *However,* starts a new sentence; *although* + subject + verb. Reason: *because* + subject + verb; *because of* + noun."],
                     "use": ["*Although it was raining, we went out.*"], "signals": "*however, although, because, because of*",
                     "example": "*The flight was late because of the snow.*"},
    "conj_clauses": {"form": ["Contrast: *although* + clause, *despite* + noun or -ing. Purpose: *to*, *so that* + could / would, *for* + noun. Reason: *as, since*, *due to* + noun."],
                     "use": ["*We went out despite the rain.*"], "signals": "*although, even though, despite, in spite of, so that, in order to, due to*",
                     "example": "*I wrote it down so that I wouldn't forget it.*"},
})
LV_CARDS.update({
    "conj_basic": {"form": ["and = līdzīga informācija, but = pretstats, or = izvēle, so = rezultāts, because = iemesls."], "use": ["It was late, so we left."], "signals": "and, but, or, so, because"},
    "conj_linkers": {"form": ["Pretstats: However, sāk jaunu teikumu; although + teikums. Iemesls: because + teikums; because of + lietvārds."], "use": ["Although it was raining, we went out."], "signals": "however, although, because, because of"},
    "conj_clauses": {"form": ["Pretstats: although + teikums, despite + lietvārds vai -ing. Nolūks: to, so that + could / would, for + lietvārds. Iemesls: as, since, due to + lietvārds."], "use": ["We went out despite the rain."], "signals": "although, despite, so that, in order to, due to"},
})
SKILLS_NEW.append(("conj_b2", "Contrast, purpose, reason and result (whereas, in case, therefore)", "clauses", ["B2.1", "B2.2"]))
ABBR_NEW.update({"conj_b2": "cj4"})
CARDS["conj_b2"] = {"form": ["Contrast: *nevertheless, yet, whereas*. Purpose: *in order for* + person + *to*, *for* + -ing, *in case*. Reason: *owing to, on account of* + noun. Result: *as a result, therefore, consequently*."],
                    "use": ["*Take an umbrella in case it rains.*"], "signals": "*whereas, nevertheless, yet, in case, owing to, as a result, therefore*",
                    "example": "*We have therefore decided to close the shop.*"}
LV_CARDS["conj_b2"] = {"form": ["Pretstats: nevertheless, yet, whereas. Nolūks: in order for + persona + to, for + -ing, in case. Iemesls: owing to, on account of + lietvārds. Rezultāts: as a result, therefore, consequently."],
                       "use": ["Take an umbrella in case it rains."], "signals": "whereas, nevertheless, yet, in case, owing to, therefore"}

# C1: unreal time and preferences (teacher, 4 November, option A): it's (high / about) time, would rather / would sooner.
# British Council "Unreal time" (C1); Murphy Unit 38 (it's time) and Unit 60 (would rather). Not conditionals, so a topic of its own.
SKILLS_NEW.append(("unreal_time", "Unreal time and preferences (it's high time, I'd rather)", "conditionals", ["B1.2", "C1.1", "C1.2"]))
ABBR_NEW.update({"unreal_time": "unr"})
CARDS["unreal_time"] = {"form": ["*It's (high / about) time* + subject + past: it should happen now, and it is late. *I'd rather / I'd sooner* + base form: what I prefer to do. *I'd rather* + another person + past: what I want someone else to do."],
                        "use": ["*It's high time we left. I'd rather stay at home. I'd rather you didn't tell anyone.*"],
                        "signals": "*it's time, it's high time, it's about time, would rather, would sooner*",
                        "example": "*It's about time you called your mother.*"}
LV_CARDS["unreal_time"] = {"form": ["It's (high / about) time + teikuma priekšmets + pagātne: tam jau vajadzētu notikt. I'd rather / I'd sooner + pamatforma: ko es labāk darītu. I'd rather + cits cilvēks + pagātne: ko gribu, lai dara kāds cits."],
                           "use": ["It's high time we left. I'd rather you didn't tell anyone."], "signals": "it's high time, it's about time, would rather, would sooner"}

# ───────── C1 direction 1 (teacher, 22 November): C1 is a real level again; Hewings, Advanced Grammar in Use, units 1-2 ─────────
SKILLS_NEW.append(("adv_present", "Advanced present simple and continuous", "active", ["C1"]))
ABBR_NEW.update({"adv_present": "apr"})
CARDS.update({
    "adv_present": {
        "form": ["Some verbs have a state meaning (simple) and an action meaning (simple or continuous): *The kitchen measures 3 by 4 metres* / *I'm measuring the kitchen.* Also *weigh, fit, feel, have, appear, think*.",
                 "Verbs that stay simple even for a short time: *believe, consist of, doubt, own, belong, know, prefer, agree*. *consider* (= think about doing) is continuous: *She's considering early retirement.*",
                 "*always, constantly, forever* + continuous: *He's forever borrowing my tools.* *usually* + continuous for something in progress at a time: *At eight I'm usually driving to work.*",
                 "Saying it is doing it: present simple: *We apologise for the delay. I suggest you book early.*"],
        "use": ["The continuous of a state verb shows that a feeling or a situation is new, temporary or changing: *We're loving the new office. I'm finding the course quite hard.*",
                "*always / forever* + continuous: typical behaviour, often with irritation.",
                "Stories and jokes, live commentary, headlines and the contents of books and films use the present: *Minister resigns. In the film, a pilot returns to his village.*"],
        "signals": "*measure, weigh, fit, consider, believe, doubt, own, always, constantly, forever, usually, apologise, suggest*",
        "example": "*I love my job. I'm just not loving this Monday.*",
    },
})
LV_CARDS.update({
    "adv_present": {
        "form": ["Dažiem darbības vārdiem ir stāvokļa nozīme (vienkāršā forma) un darbības nozīme (vienkāršā vai ilgstošā forma): *The kitchen measures 3 by 4 metres* / *I'm measuring the kitchen.* Arī *weigh, fit, feel, have, appear, think*.",
                 "Darbības vārdi, kas paliek vienkāršajā formā arī īsu laiku: *believe, consist of, doubt, own, belong, know, prefer, agree*. *consider* (= apsvērt) ir ilgstošajā formā: *She's considering early retirement.*",
                 "*always, constantly, forever* + ilgstošā forma: *He's forever borrowing my tools.* *usually* + ilgstošā forma, ja darbība tajā laikā jau notiek: *At eight I'm usually driving to work.*",
                 "Ja paši vārdi ir darbība, lieto Present Simple: *We apologise for the delay. I suggest you book early.*"],
        "use": ["Stāvokļa darbības vārda ilgstošā forma rāda, ka sajūta vai situācija ir jauna, īslaicīga vai mainās: *We're loving the new office. I'm finding the course quite hard.*",
                "*always / forever* + ilgstošā forma: raksturīga uzvedība, bieži ar nepatiku.",
                "Stāstos un jokos, tiešraides komentāros, virsrakstos un grāmatu un filmu satura stāstījumā lieto tagadni: *Minister resigns. In the film, a pilot returns to his village.*"],
        "signals": "measure, weigh, fit, consider, believe, doubt, own, always, constantly, forever, usually, apologise, suggest",
    },
})

# ───────── C1 direction 2 (23 November): Hewings, Advanced Grammar in Use, units 4-5 ─────────
SKILLS_NEW.append(("adv_past", "Advanced past simple, past continuous and past perfect", "active", ["C1"]))
ABBR_NEW.update({"adv_past": "apa"})
CARDS.update({
    "adv_past": {
        "form": ["Events that follow one another: past simple for all of them: *The alarm went off as soon as he lit the candle.*",
                 "A count of repeated actions: past simple (*We flew to Oslo four times last year*); the continuous only for a temporary period (*While my car was being repaired, I was cycling to work*).",
                 "Something earlier than a past moment: past perfect: *I was sure we had met before. It was the best film I had ever seen.* What caused a past state: *He was hoarse because he had been shouting all afternoon.*",
                 "Past forms that are not about the past: *I wish I had kept the receipt* (a regret about the past); *I was wondering if you could help* (a polite request now)."],
        "use": ["*was always / forever* + *-ing*: a past habit that annoyed someone: *My old flatmate was always leaving the lights on.*",
                "The past continuous for a situation, the past simple for the event that happened in it: *She dropped her keys while she was getting out of the taxi.*",
                "State verbs stay simple, also before a past moment: *We had known each other for years*, not *had been knowing*."],
        "signals": "*as soon as, while, four times, before, ever, by then, because, always, forever, I wish, I was wondering*",
        "example": "*I was quietly eating your biscuits when you walked in.*",
    },
})
LV_CARDS.update({
    "adv_past": {
        "form": ["Notikumi, kas seko viens otram: visiem Past Simple: *The alarm went off as soon as he lit the candle.*",
                 "Atkārtotas darbības ar skaitu: Past Simple (*We flew to Oslo four times last year*); ilgstošā forma tikai īslaicīgam periodam (*While my car was being repaired, I was cycling to work*).",
                 "Kaut kas notika pirms cita pagātnes brīža: Past Perfect: *I was sure we had met before. It was the best film I had ever seen.* Kas izraisīja stāvokli pagātnē: *He was hoarse because he had been shouting all afternoon.*",
                 "Pagātnes formas, kas nav par pagātni: *I wish I had kept the receipt* (nožēla par pagātni); *I was wondering if you could help* (pieklājīgs lūgums tagad)."],
        "use": ["*was always / forever* + *-ing*: pagātnes ieradums, kas kādu kaitināja: *My old flatmate was always leaving the lights on.*",
                "Past Continuous situācijai, Past Simple notikumam, kas tajā notika: *She dropped her keys while she was getting out of the taxi.*",
                "Stāvokļa darbības vārdi paliek vienkāršajā formā arī pirms pagātnes brīža: *We had known each other for years*, nevis *had been knowing*."],
        "signals": "as soon as, while, four times, before, ever, by then, because, always, forever, I wish, I was wondering",
    },
})

# ───────── C1 direction 3 (23 November): Hewings, Advanced Grammar in Use, units 3, 6 ─────────
SKILLS_NEW.append(("adv_perfect", "The perfect tenses: forms and uses", "active", ["C1"]))
ABBR_NEW.update({"adv_perfect": "apf"})
CARDS.update({
    "adv_perfect": {
        "form": ["*this morning, today, this week*: present perfect while the time is still going on (*It's ten and I've drunk three coffees this morning*), past simple when it is over (*I didn't do much this morning*, said at six).",
                 "*since*: past simple for the point in the past, present perfect in the main part: *Since she joined the team, sales have doubled.* Both still going on: *since you've lived here*.",
                 "*the moment, once, as soon as, after* + present perfect (or present simple) for the future, + past simple for the past: *I'll text you the moment I've got the results. The moment we landed, I texted her.*",
                 "*It's the first / second time* + present perfect; *It was the first time* + past perfect: *This is the third time she's lost her keys.*",
                 "The perfect after *to* and prepositions: *He is thought to have left. She denied having read it.* Future: *By May I'll have taught here for ten years.*"],
        "use": ["The continuous for an activity up to now, the simple for a number, a result or a state: *I've rung the bank four times. I've been ringing the bank all morning. I've had this phone since May.*"],
        "signals": "*this morning, today, since, the moment, once, the first time, the third time, by May, is thought to, denied*",
        "example": "*This is the third time I've lost my glasses today. They're on my head.*",
    },
})
LV_CARDS.update({
    "adv_perfect": {
        "form": ["*this morning, today, this week*: Present Perfect, kamēr laiks vēl turpinās (*It's ten and I've drunk three coffees this morning*), Past Simple, kad tas beidzies (*I didn't do much this morning*, sakot sešos vakarā).",
                 "*since*: Past Simple brīdim pagātnē, Present Perfect galvenajā daļā: *Since she joined the team, sales have doubled.* Ja abas situācijas turpinās: *since you've lived here*.",
                 "*the moment, once, as soon as, after* + Present Perfect (vai Present Simple) nākotnei, + Past Simple pagātnei: *I'll text you the moment I've got the results. The moment we landed, I texted her.*",
                 "*It's the first / second time* + Present Perfect; *It was the first time* + Past Perfect: *This is the third time she's lost her keys.*",
                 "Perfekts aiz *to* un prievārdiem: *He is thought to have left. She denied having read it.* Nākotnē: *By May I'll have taught here for ten years.*"],
        "use": ["Ilgstošā forma darbībai līdz šim brīdim, vienkāršā skaitam, rezultātam vai stāvoklim: *I've rung the bank four times. I've been ringing the bank all morning. I've had this phone since May.*"],
        "signals": "this morning, today, since, the moment, once, the first time, the third time, by May, is thought to, denied",
    },
})

# ───────── C1 direction 4 (23 November): Hewings, Advanced Grammar in Use, units 16, 20, 39 ─────────
SKILLS_NEW.append(("adv_will", "Advanced modals: will, would, should", "modals", ["C1"]))
ABBR_NEW.update({"adv_will": "awl"})
CARDS.update({
    "adv_will": {
        "form": ["*will* / *would* for typical behaviour, never for one occasion: *Our cat will sit at the window for hours. At school she would sit at the back.* But *Last night he cooked dinner.* For a past state, *used to*: *The factory used to be there.*",
                 "*won't / wouldn't* for refusing, also things and one occasion: *The printer wouldn't work this morning.* Criticism: *If you will stare at a screen all day…*",
                 "*will* for a confident guess about now or the past: *They'll be having lunch now. She'll have heard the news by now.*",
                 "*would have* + past participle for what did not happen: *I would have come, but nobody told me.*",
                 "*should* for what we expect: *The parcel should have arrived by now.* Formal: *If you should need anything… / Should you need anything… / in case you should need it.*"],
        "use": ["*If you will / would* = if you are willing (a polite request): *If you'll follow me, I'll show you to your room.*"],
        "signals": "*for hours, always, whenever, by now, nobody told me, refused, in case, should you*",
        "example": "*My laptop won't switch on. It will always do this before a deadline.*",
    },
})
LV_CARDS.update({
    "adv_will": {
        "form": ["*will* / *would* raksturīgai uzvedībai, nekad vienai reizei: *Our cat will sit at the window for hours. At school she would sit at the back.* Bet *Last night he cooked dinner.* Pagātnes stāvoklim *used to*: *The factory used to be there.*",
                 "*won't / wouldn't* atteikumam, arī lietām un vienai reizei: *The printer wouldn't work this morning.* Kritika: *If you will stare at a screen all day…*",
                 "*will* drošam minējumam par tagadni vai pagātni: *They'll be having lunch now. She'll have heard the news by now.*",
                 "*would have* + 3. forma tam, kas nenotika: *I would have come, but nobody told me.*",
                 "*should* tam, ko sagaidām: *The parcel should have arrived by now.* Oficiāli: *If you should need anything… / Should you need anything… / in case you should need it.*"],
        "use": ["*If you will / would* = ja esat ar mieru (pieklājīgs lūgums): *If you'll follow me, I'll show you to your room.*"],
        "signals": "for hours, always, whenever, by now, nobody told me, refused, in case, should you",
    },
})

# ───────── C1 directions 5 and 6 (23 November): Hewings, Advanced Grammar in Use, units 15, 17, 39, 85 ─────────
SKILLS_NEW.append(("adv_can", "Advanced modals: can, be able to, may, might", "modals", ["C1"]))
SKILLS_NEW.append(("adv_subj", "The subjunctive: I insist that he be told, if I were", "conditionals", ["C1"]))   # area: agent proposal (23 November), next to Unreal time
ABBR_NEW.update({"adv_can": "acn", "adv_subj": "asb"})
CARDS.update({
    "adv_can": {
        "form": ["One past success: *was able to / managed to*, not *could*: *After three hours we were able to find a parking space.* Permission once: *were allowed to*: *Last night the children were allowed to stay up.* (*could* = always: *We could stay up late on Saturdays.*)",
                 "*can* before a passive: *The forms can be filled in online* (not *are able to be*).",
                 "Questions about possibility: *Could…? Is… likely to…?*, not *May…?*: *Could the figures be wrong?*",
                 "*may / might be* + *-ing*, *may / might have been* + *-ing*: *This time next week I may be lying on a beach. He might have been joking.*",
                 "*might as well* = the only sensible thing: *There's no bus, so we might as well walk.* *You might have warned me!* = you should have."],
        "use": ["*can* for what is sometimes true: *Winters here can be very long.*"],
        "signals": "*after three hours, last night, once, this time next week, might as well, might have, could… be*",
        "example": "*The diet starts on Monday. Today I might as well finish the cake.*",
    },
    "adv_subj": {
        "form": ["After *demand, insist, recommend, suggest, propose, request* + *that*: the base form for every person (formal), or *should* + base form: *The doctor recommended that she rest. I insist that he be told.* Not *demanded him to resign*.",
                 "Negative: *not* + base form: *We recommend that the medicine not be taken with alcohol.*",
                 "*It's odd / surprising that* + *should*: *It's odd that she should say that.*",
                 "*were* for all persons in unreal situations: *If I were you… I wish it were Friday. If the bank were to refuse…* (not *would refuse* after *if*).",
                 "*I'd rather you had told me* (the past), *I'd rather you told me* (now or later)."],
        "use": ["Fixed phrases: *be that as it may, so be it, come what may, suffice it to say*."],
        "signals": "*demand, insist, recommend, suggest, it is vital that, I wish, if I were, as if, I'd rather, be that as it may*",
        "example": "*If I were a cat, I'd ignore emails too.*",
    },
})
LV_CARDS.update({
    "adv_can": {
        "form": ["Viens izdevies mēģinājums pagātnē: *was able to / managed to*, nevis *could*: *After three hours we were able to find a parking space.* Atļauja vienu reizi: *were allowed to*: *Last night the children were allowed to stay up.* (*could* = vienmēr: *We could stay up late on Saturdays.*)",
                 "*can* pirms ciešamās kārtas: *The forms can be filled in online* (nevis *are able to be*).",
                 "Jautājumi par iespējamību: *Could…? Is… likely to…?*, nevis *May…?*: *Could the figures be wrong?*",
                 "*may / might be* + *-ing*, *may / might have been* + *-ing*: *This time next week I may be lying on a beach. He might have been joking.*",
                 "*might as well* = vienīgais saprātīgais: *There's no bus, so we might as well walk.* *You might have warned me!* = vajadzēja brīdināt."],
        "use": ["*can* tam, kas mēdz būt: *Winters here can be very long.*"],
        "signals": "after three hours, last night, once, this time next week, might as well, might have, could… be",
    },
    "adv_subj": {
        "form": ["Aiz *demand, insist, recommend, suggest, propose, request* + *that*: pamatforma visām personām (oficiāli) vai *should* + pamatforma: *The doctor recommended that she rest. I insist that he be told.* Nevis *demanded him to resign*.",
                 "Noliegums: *not* + pamatforma: *We recommend that the medicine not be taken with alcohol.*",
                 "*It's odd / surprising that* + *should*: *It's odd that she should say that.*",
                 "*were* visām personām nereālās situācijās: *If I were you… I wish it were Friday. If the bank were to refuse…* (nevis *would refuse* aiz *if*).",
                 "*I'd rather you had told me* (pagātne), *I'd rather you told me* (tagad vai vēlāk)."],
        "use": ["Nemainīgi izteicieni: *be that as it may, so be it, come what may, suffice it to say*."],
        "signals": "demand, insist, recommend, suggest, it is vital that, I wish, if I were, as if, I'd rather, be that as it may",
    },
})

# ───────── C1 directions 7 and 8 (23 November): Hewings, Advanced Grammar in Use, units 40-41, 55, 92-93 ─────────
SKILLS_NEW.append(("adv_agree", "Subject and verb: advanced rules", "active", ["C1"]))   # the same area as Subject and verb (agreement)
SKILLS_NEW.append(("adv_prep", "Prepositions: position and advanced patterns", "prepositions", ["C1"]))
ABBR_NEW.update({"adv_agree": "aag", "adv_prep": "apr2"})
CARDS.update({
    "adv_agree": {
        "form": ["The main noun decides, not the words around it: *The manager, together with two assistants, is coming.* A clause as the subject is singular: *Being late for every meeting is not going to help.*",
                 "*The number of* + plural noun + singular verb; *a number of* + plural verb: *The number of applicants has fallen. A number of applicants have withdrawn.*",
                 "*each of / neither of* + singular verb in writing: *Each of the rooms has its own bathroom.* *either … or*: the nearer noun decides: *Either the manager or her assistants are going to call.*",
                 "Singular: *politics, economics, the news*; an amount as one thing: *Ten kilometres is a long way.* Plural: *criteria, phenomena*.",
                 "A group as its members: plural verb: *The jury are still arguing among themselves.*"],
        "use": ["Ask: what is the main noun? Is the group one unit or its members?"],
        "signals": "*together with, as well as, the number of, a number of, each of, either … or, politics, criteria, ten kilometres*",
        "example": "*The number of unread emails has reached 2,000. None of them is urgent.*",
    },
    "adv_prep": {
        "form": ["Formal: preposition + *whom / which*; everyday: the preposition at the end. Never before *who* or *that*: *the colleague with whom I share an office / the colleague I share an office with*.",
                 "Fixed formal phrases: *the extent to which, the basis on which, the way in which*. Numbers: *three offers, none of which was acceptable*.",
                 "The preposition stays after a passive or an infinitive: *Your complaint is being looked into. I had nobody to talk to.*",
                 "After a preposition: *-ing*, a *wh*-clause or *the fact that*, never a bare *that*-clause: *despite the fact that…, depends on whether…*",
                 "Multi-word prepositions: *with a view to + -ing, in the event of, regardless of, other than*."],
        "use": ["Check which preposition the noun or verb takes: *a talent for, prevent someone from*."],
        "signals": "*whom, which, to which, on which, none of which, looked into, to talk to, with a view to, other than, despite the fact that*",
        "example": "*This is the meeting in which nothing was decided.*",
    },
})
LV_CARDS.update({
    "adv_agree": {
        "form": ["Izšķir galvenais lietvārds, nevis vārdi ap to: *The manager, together with two assistants, is coming.* Palīgteikums kā teikuma priekšmets ir vienskaitlī: *Being late for every meeting is not going to help.*",
                 "*The number of* + daudzskaitlis + darbības vārds vienskaitlī; *a number of* + daudzskaitlis: *The number of applicants has fallen. A number of applicants have withdrawn.*",
                 "*each of / neither of* + vienskaitlis rakstos: *Each of the rooms has its own bathroom.* *either … or*: izšķir tuvākais lietvārds: *Either the manager or her assistants are going to call.*",
                 "Vienskaitlis: *politics, economics, the news*; daudzums kā viena lieta: *Ten kilometres is a long way.* Daudzskaitlis: *criteria, phenomena*.",
                 "Grupa kā tās locekļi: daudzskaitlis: *The jury are still arguing among themselves.*"],
        "use": ["Pajautā: kurš ir galvenais lietvārds? Vai grupa ir viena vienība vai tās locekļi?"],
        "signals": "together with, as well as, the number of, a number of, each of, either … or, politics, criteria, ten kilometres",
    },
    "adv_prep": {
        "form": ["Oficiāli: prievārds + *whom / which*; ikdienā prievārds beigās. Nekad pirms *who* vai *that*: *the colleague with whom I share an office / the colleague I share an office with*.",
                 "Nemainīgi oficiāli izteicieni: *the extent to which, the basis on which, the way in which*. Ar skaitu: *three offers, none of which was acceptable*.",
                 "Prievārds paliek aiz ciešamās kārtas vai nenoteiksmes: *Your complaint is being looked into. I had nobody to talk to.*",
                 "Aiz prievārda: *-ing*, *wh*-palīgteikums vai *the fact that*, nekad tikai *that*-palīgteikums: *despite the fact that…, depends on whether…*",
                 "Vairākvārdu prievārdi: *with a view to + -ing, in the event of, regardless of, other than*."],
        "use": ["Pārbaudi, kādu prievārdu prasa lietvārds vai darbības vārds: *a talent for, prevent someone from*."],
        "signals": "whom, which, to which, on which, none of which, looked into, to talk to, with a view to, other than, despite the fact that",
    },
})

# ───────── C1 directions 9 and 10 (23 November): Hewings, Advanced Grammar in Use, units 58-59, 98-100 ─────────
SKILLS_NEW.append(("adv_part", "Advanced participle clauses", "clauses", ["C1"]))   # area: agent proposal (23 November)
SKILLS_NEW.append(("adv_order", "Advanced word order: inversion and fronting", "clauses", ["C1"]))   # area: agent proposal (23 November)
ABBR_NEW.update({"adv_part": "apt", "adv_order": "aor2"})
CARDS.update({
    "adv_part": {
        "form": ["The participle clause has the same subject as the main clause: *Opening the door, she saw the cat.* Not *Walking into the office, the lights were off.*",
                 "*Having* + past participle for an earlier action or a cause: *Having finished the report, she went home.* *Not* goes first: *Not knowing anyone, he felt lonely.*",
                 "Past participle for a passive meaning: *Stored in a dry place, the seeds keep for years. Keep refrigerated once opened.*",
                 "With its own subject: *With prices going up, many families are struggling. There being no questions, the chair closed the meeting.*",
                 "After the main clause, for the result: *The river burst its banks, flooding the streets.*",
                 "*on* + *-ing* = when (*On hearing the news…*), *in* + *-ing* = while doing, *by* + *-ing* = the method (*by booking early*), *without* + *-ing* = not doing (*without locking the door*)."],
        "use": ["Fixed phrases that comment on the whole sentence: *Judging by the queue…, Generally speaking…, Considering the price…*"],
        "signals": "*having, not knowing, once opened, with, there being, on hearing, judging by*",
        "example": "*Having eaten the whole pizza, I started my diet.*",
    },
    "adv_order": {
        "form": ["After a negative or limiting word at the start, the helping verb comes before the subject: *Rarely have I seen such a sunset. Never have I felt so tired. No sooner had she arrived than it rained.*",
                 "*Not until / Only when* + first clause, then inversion in the second: *Not until the guests had gone did we notice the stain.*",
                 "*So* + adjective + *be* + subject: *So loud was the music that we couldn't talk.*",
                 "Conditions without *if*: *Had I known…, Should you need anything…, Were the bank to refuse…*",
                 "*Here comes the bus!*; *What I need is a holiday.*; *Cold though it was, we went for a swim.*"],
        "use": ["Formal and emphatic style: speeches, reports, stories."],
        "signals": "*never, rarely, hardly, no sooner, not until, only when, so … that, had, should, what … is, though*",
        "example": "*Never have I regretted a nap.*",
    },
})
LV_CARDS.update({
    "adv_part": {
        "form": ["Divdabja teicienam ir tas pats teikuma priekšmets, kas galvenajam teikumam: *Opening the door, she saw the cat.* Nevis *Walking into the office, the lights were off.*",
                 "*Having* + 3. forma agrākai darbībai vai cēlonim: *Having finished the report, she went home.* *Not* stāv pirmais: *Not knowing anyone, he felt lonely.*",
                 "3. forma ciešamās kārtas nozīmei: *Stored in a dry place, the seeds keep for years. Keep refrigerated once opened.*",
                 "Ar savu teikuma priekšmetu: *With prices going up, many families are struggling. There being no questions, the chair closed the meeting.*",
                 "Aiz galvenā teikuma, rezultātam: *The river burst its banks, flooding the streets.*",
                 "*on* + *-ing* = kad (*On hearing the news…*), *in* + *-ing* = darot, *by* + *-ing* = veids (*by booking early*), *without* + *-ing* = nedarot (*without locking the door*)."],
        "use": ["Nemainīgi izteicieni, kas komentē visu teikumu: *Judging by the queue…, Generally speaking…, Considering the price…*"],
        "signals": "having, not knowing, once opened, with, there being, on hearing, judging by",
    },
    "adv_order": {
        "form": ["Pēc nolieguma vai ierobežojoša vārda teikuma sākumā palīgdarbības vārds stāv pirms teikuma priekšmeta: *Rarely have I seen such a sunset. Never have I felt so tired. No sooner had she arrived than it rained.*",
                 "*Not until / Only when* + pirmā daļa, tad inversija otrajā: *Not until the guests had gone did we notice the stain.*",
                 "*So* + īpašības vārds + *be* + teikuma priekšmets: *So loud was the music that we couldn't talk.*",
                 "Nosacījumi bez *if*: *Had I known…, Should you need anything…, Were the bank to refuse…*",
                 "*Here comes the bus!*; *What I need is a holiday.*; *Cold though it was, we went for a swim.*"],
        "use": ["Oficiāls un uzsvērts stils: runas, ziņojumi, stāsti."],
        "signals": "never, rarely, hardly, no sooner, not until, only when, so … that, had, should, what … is, though",
    },
})
