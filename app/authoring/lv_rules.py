"""Latvian rule cards for every topic that has levels up to B1.2. The example sentence stays English."""
from lv_data import LV_RULES

LV_RULES.update({
    "present_simple": {
        "form": ["I / you / we / they + darbības vārda pamatforma: I work.", "he / she / it + darbības vārds ar -s: She works.",
                 "Noliegums: don't / doesn't + pamatforma.", "Jautājums: Do / Does + teik. priekšmets + pamatforma?"],
        "use": ["Ieradumi un ikdienas rutīna.", "Vienmēr patiesi fakti.", "Saraksti un grafiki (the train leaves at 7.45)."],
        "signals": "always, usually, often, sometimes, never, every day (vienmēr, parasti, bieži, dažreiz, nekad, katru dienu)",
    },
    "present_continuous": {
        "form": ["am / is / are + darbības vārds ar -ing: I am working.", "Noliegums: am / is / are + not + -ing.", "Jautājums: Am / Is / Are + teik. priekšmets + -ing?"],
        "use": ["Darbība, kas notiek tieši tagad.", "Pagaidu situācijas.", "Mainīgas, norisošas situācijas.", "Fiksēti nākotnes plāni."],
        "signals": "now, at the moment, today, this week, these days, tomorrow (plāniem)",
    },
    "past_simple": {
        "form": ["Regulārie darbības vārdi: pamatforma + -ed (worked).", "Neregulārie darbības vārdi ir jāiemācās (go - went, see - saw).",
                 "Noliegums: didn't + pamatforma.", "Jautājums: Did + teik. priekšmets + pamatforma?", "Pagātnes ieradumi: used to + pamatforma."],
        "use": ["Pabeigtas darbības pabeigtā laikā.", "Darbību virkne stāstā.", "Pagātnes ieradumi un stāvokļi (used to)."],
        "signals": "yesterday, last week, in 2019, three days ago (vakar, pagājušajā nedēļā, 2019. gadā, pirms trim dienām)",
    },
    "past_continuous": {
        "form": ["was / were + -ing: I was working.", "Noliegums: wasn't / weren't + -ing.", "Jautājums: Was / Were + teik. priekšmets + -ing?",
                 "Plāns, kas nenotika: was / were going to + pamatforma."],
        "use": ["Darbība, kas pagātnē noteiktā brīdī bija procesā.", "Garāku darbību pārtrauc īsa darbība (Past Simple).", "Stāsta fons."],
        "signals": "at 8 o'clock yesterday, while, when, as",
    },
    "present_perfect": {
        "form": ["have / has + darbības vārda 3. forma (past participle): I have seen it.", "Noliegums: haven't / hasn't + 3. forma.", "Jautājums: Have / Has + teik. priekšmets + 3. forma?"],
        "use": ["Dzīves pieredze (bez precīza laika).", "Kaut kas sācies pagātnē un turpinās (for / since).", "Pagātnes darbība ar rezultātu tagad.", "Jaunākās ziņas (just, already, yet)."],
        "signals": "ever, never, just, already, yet, for, since, so far, this week",
    },
    "present_perfect_continuous": {
        "form": ["have / has been + -ing: I have been working.", "Noliegums: haven't / hasn't been + -ing.", "Jautājums: Have / Has + teik. priekšmets + been + -ing?"],
        "use": ["Darbība, kas sākās pagātnē un turpinās tagad.", "Nesena darbība, kas izskaidro situāciju tagad.", "Cik ilgi kaut kas notiek."],
        "signals": "for, since, all day, lately, recently, how long",
    },
    "past_perfect": {
        "form": ["had + 3. forma: I had finished.", "Noliegums: hadn't + 3. forma.", "Jautājums: Had + teik. priekšmets + 3. forma?"],
        "use": ["Agrākā no divām pagātnes darbībām.", "Pagātnes notikuma iemesls."],
        "signals": "before, after, by the time, already, when",
    },
    "future": {
        "form": ["will + pamatforma: I will help you.", "going to: am / is / are going to + pamatforma.", "Present Continuous: I'm meeting Anna at six.",
                 "Pēc when / if / as soon as lieto Present Simple."],
        "use": ["will: ātri lēmumi, piedāvājumi, solījumi, prognozes.", "going to: plāni un prognozes ar pierādījumiem.", "Present Continuous: fiksētas norunas.", "be about to: pavisam tuvā nākotne."],
        "signals": "tomorrow, next week, soon, when, as soon as, if",
    },
    "present_simple_passive": {
        "form": ["am / is / are + 3. forma: English is spoken here.", "Noliegums: isn't / aren't + 3. forma.", "Jautājums: Is / Are + teik. priekšmets + 3. forma?"],
        "use": ["Kad svarīgāka ir darbība vai tās objekts, nevis darītājs.", "Procesi, noteikumi un paziņojumi."],
        "signals": "often, every day, usually, in my country",
    },
    "past_simple_passive": {
        "form": ["was / were + 3. forma: The book was written in 1990.", "Noliegums: wasn't / weren't + 3. forma.", "Jautājums: Was / Were + teik. priekšmets + 3. forma?"],
        "use": ["Pagātnes notikumi, kad darītājs nav zināms vai nav svarīgs.", "Vēsture, ziņas.", "by + darītājs, ja tas ir svarīgi."],
        "signals": "yesterday, last year, in 1889, when",
    },
    "present_continuous_passive": {
        "form": ["am / is / are being + 3. forma: The road is being repaired."],
        "use": ["Darbība, kas notiek tagad, un darītājs nav svarīgs."],
        "signals": "now, at the moment, right now",
    },
    "present_perfect_passive": {
        "form": ["has / have been + 3. forma: The email has been sent.", "Jautājums: Has / Have + teik. priekšmets + been + 3. forma?"],
        "use": ["Jaunākās ziņas vai darbības ar rezultātu tagad.", "Darbības līdz šim brīdim (so far, already, yet)."],
        "signals": "already, yet, just, so far, recently",
    },
    "future_passive": {
        "form": ["will be + 3. forma: You will be told soon.", "Noliegums: won't be + 3. forma.", "Jautājums: Will + teik. priekšmets + be + 3. forma?"],
        "use": ["Nākotnes notikumi, kad darītājs nav zināms vai nav svarīgs.", "Paziņojumi."],
        "signals": "tomorrow, next week, soon, by Friday",
    },
    "cond_zero": {
        "form": ["If + Present Simple, Present Simple: If you heat ice, it melts.", "Var lietot arī when vai whenever: Whenever it rains, the road gets slippery.",
                 "Noliegums: If you don't water plants, they die."],
        "use": ["Vienmēr patiesi fakti (zinātne, daba).", "Vispārīgi noteikumi un ieradumi.", "Norādījumi: If the light is red, stop."],
        "signals": "if, when, whenever, every time",
    },
    "cond_first": {
        "form": ["If + Present Simple, will + pamatforma: If it rains, we will stay home.", "Nosacījuma palīgteikums (if daļa) var būt arī otrā vietā: We will stay home if it rains.",
                 "Rezultātā var lietot arī may, might, can, should.", "Pēc if nelieto will: If it rains (nevis If it will rain)."],
        "use": ["Reālas, iespējamas nākotnes situācijas.", "Solījumi, brīdinājumi un piedāvājumi.", "First conditional = viena nākotnes situācija. Zero conditional = vienmēr patiesi."],
        "signals": "if, unless, as soon as, when, in case",
    },
    "cond_second": {
        "form": ["If + Past Simple, would + pamatforma: If I won the lottery, I would quit my job.", "Rūpīgā valodā visām personām lieto were: If I were you, ...",
                 "Jautājums: What would you do if ...?", "Would vietā var lietot could vai might."],
        "use": ["Nereālas vai maz ticamas situācijas tagadnē vai nākotnē.", "Padoms: If I were you, I'd talk to your manager.", "Iztēle."],
        "signals": "if, imagine, suppose, if I were you",
    },
    "cond_third": {
        "form": ["If + Past Perfect, would have + 3. forma: If I had known, I would have called.", "Noliegums: If I hadn't ..., I wouldn't have ...",
                 "Could have vai might have, ja rezultāts nav tik drošs."],
        "use": ["Nereālas situācijas pagātnē: tas nenotika.", "Nožēla un kritika.", "Iztēle par citādu pagātni."],
        "signals": "if, if only, too late, I wish (pagātne)",
    },
    "rep_statements": {
        "form": ["said / told + (that) + teikums: She said (that) she was tired.",
                 "Laiks parasti iet vienu soli atpakaļ: am/is → was, work → worked, worked → had worked, will → would, can → could.",
                 "Mainās vietniekvārdi un laika vārdi: I → he/she, now → then, today → that day, tomorrow → the next day, here → there.",
                 "tell vajag personu: He told me. say bez personas: He said that ..."],
        "use": ["Pastāstīt, ko cits cilvēks teica.", "Ja fakts joprojām ir patiess vai pastāsti uzreiz, laiku var nemainīt: She says she's tired."],
        "signals": "said, told, now → then, yesterday → the day before",
    },
    "rep_questions": {
        "form": ["Jā/nē jautājumi: asked + if / whether + teik. priekšmets + darbības vārds: She asked if I liked coffee.",
                 "Jautājumi ar jautājamo vārdu: asked + jautājamais vārds + teik. priekšmets + darbības vārds: He asked where I lived.",
                 "Parasta vārdu secība, bez do / does / did: She asked what I did (nevis what did I do).",
                 "Lūgumi un rīkojumi: told / asked + persona + (not) to + pamatforma: He told me to wait."],
        "use": ["Pastāstīt, ko kāds jautāja.", "Pastāstīt, ko kāds lika vai lūdza darīt."],
        "signals": "asked, wondered, wanted to know, told someone to",
    },
    "ind_polite": {
        "form": ["Sāc ar: Could you tell me / Do you know / Can you tell me / I wonder.", "Tad lieto teikuma vārdu secību: ... where the station is (nevis where is the station).",
                 "Bez do / does / did palīgteikumā: ... what time the shop opens.", "Jā/nē jautājumos lieto if vai whether: Do you know if she is here?"],
        "use": ["Pieklājīgi jautājumi pēc informācijas.", "Sarunā ar svešiem cilvēkiem, klientiem un darbā.", "Pēc I wonder ... / I'd like to know ... liek punktu; pēc Could you / Do you know ... jautājuma zīmi."],
        "signals": "Could you tell me, Do you know, I wonder, I'd like to know, Would you mind telling me",
    },
})


LV_RULES["modal_verbs"] = {
    "form": ["can / should / must + darbības vārda pamatforma: I can swim. You should rest. He must go.",
             "Nav -s ar he / she / it: he can, she should, it must.",
             "Noliegums: can't (cannot), shouldn't, mustn't + pamatforma. Jautājums: Can / Should / Must + teik. priekšmets + pamatforma?",
             "have to ir parasts darbības vārds: she has to go. Noliegums un jautājums ar do / does: I don't have to go. Do you have to go?"],
    "use": ["can: spēja (I can swim) un atļauja (Can I sit here?).",
            "should: padoms (You should see a doctor).",
            "must / have to: tas ir nepieciešams, noteikums vai pienākums (You must wear a seat belt. I have to wear a uniform at work). Bieži der abi.",
            "mustn't = aizliegts. don't have to = nav obligāti (You mustn't park here. You don't have to pay).",
            "must nav pagātnes ne nākotnes formas: lieto had to / will have to (I had to work late. We will have to leave early)."],
    "signals": "rule, law, allowed, necessary, advice, ability (noteikums, likums, atļauts, nepieciešams, padoms, spēja)",
}


LV_RULES["comparison"] = {
    "form": ["Īsie īpašības vārdi: īpašības vārds + -er + than (Rachel is taller than Tom). Vispārākā pakāpe: the + īpašības vārds + -est (the tallest).",
             "Pareizrakstība: big - bigger - the biggest; nice - nicer - the nicest; heavy - heavier - the heaviest.",
             "Garie īpašības vārdi (divas vai vairāk zilbes): more / the most + īpašības vārds (more expensive than, the most expensive).",
             "Neregulārie: good - better - the best; bad - worse - the worst; far - further - the furthest.",
             "as + īpašības vārds + as = vienāds (My phone is as fast as yours). not as ... as = mazāk (This bag is not as heavy as that one)."],
    "use": ["Pārākā pakāpe: salīdzina divus cilvēkus vai lietas. Vispārākā pakāpe: viens salīdzināts ar visiem pārējiem grupā (the tallest student in the class).",
            "Aiz vispārākās pakāpes lieto in + vieta vai grupa: the biggest city in the country.",
            "the same as, similar to, different from: It is the same colour as mine.",
            "much / a lot / a bit / slightly + pārākā pakāpe parāda, cik liela ir atšķirība (much cheaper, a bit colder). less ... than un the least ir pretējs more ... than un the most."],
    "signals": "than, as ... as, the ... -est, in, much, a bit, the same as (nekā, tikpat ... kā, visā, daudz, mazliet, tāds pats kā)",
}


import b1_topics as _b1  # noqa: E402
LV_RULES.update(_b1.LV_CARDS)

