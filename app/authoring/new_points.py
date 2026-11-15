"""The New group (teacher, 15 November, option A): the 17 grammar points that got their first tasks in batch 4 are shown as
their own tiles under "New" (practice picker and Rule cards), each with a short card of its own (EN and LV) and practice of
that point only. They replace the topics that were "New" until now. A point stays new for NEW_DAYS days from its date.
The cards use the v2 layout of cards2.py (table, mistakes, uses, watch; [[ ]] marks the form)."""

NEW_DAYS = 21   # teacher, 15 November: 21 days, or until newer points are added (the newest date wins: Content::liveMeta)
F_EN, F_LV = ["Form", "Example"], ["Forma", "Piemērs"]


def card(en_rows, lv_rows, mistakes_en, mistakes_lv, use_en, use_lv, watch_en, watch_lv):
    import re
    def head(a, b):   # the row heading is the form itself, as on the topic cards (teacher, 15 November): the marked words of the example
        forms = []
        for f in re.findall(r"\[\[(.+?)\]\]", b):
            f = f.strip("'")
            if f.lower() not in [x.lower() for x in forms]: forms.append(f)
        return " / ".join(forms[:3]) or a
    ch = lambda rows, col: {"cols": [col], "rows": [[r[2] if len(r) > 2 else head(r[0], r[1]), r[0] + " || " + r[1]] for r in rows], "stack": "rows"}   # rendered like the choice tables (cellRich)
    return {"en": {"choice": ch(en_rows, F_EN[1]), "mistakes": mistakes_en, "uses": use_en, "watch": watch_en},
            "lv": {"choice": ch(lv_rows, F_LV[1]), "mistakes": mistakes_lv, "uses": use_lv, "watch": watch_lv}}


POINTS = [
    # ── A2 (gap-points-a2-1.csv, 15 November) ──
    ("have_got", "Have got and have", "aux_verbs", "2026-11-15", card(
        [["have", "*I [[have got]] a car. She'[[s got]] two sisters.*"], ["negative", "*I [[haven't got]] a car. = I [[don't have]] a car.*"], ["question", "*[[Have]] you [[got]] a pen? = [[Do]] you [[have]] a pen?*"]],
        [["ir", "*I [[have got]] a car. She'[[s got]] two sisters.*"], ["noliegums", "*I [[haven't got]] a car. = I [[don't have]] a car.*"], ["jautājums", "*[[Have]] you [[got]] a pen? = [[Do]] you [[have]] a pen?*"]],
        [["[[Do]] you have [[got]] a pen?", "[[Have]] you [[got]] a pen?"], ["She [[have]] got a dog.", "She [[has]] got a dog."], ["Have you got a bike? Yes, I [[have got]].", "Have you got a bike? Yes, I [[have]]."]],
        [["[[Do]] you have [[got]] a pen?", "[[Have]] you [[got]] a pen?"], ["She [[have]] got a dog.", "She [[has]] got a dog."], ["Have you got a bike? Yes, I [[have got]].", "Have you got a bike? Yes, I [[have]]."]],
        [{"t": "Short answers", "ex": ["Have you got a car? Yes, I [[have]]. / No, I [[haven't]].", "Do you have a car? Yes, I [[do]]. / No, I [[don't]]."]}],
        [{"t": "Īsās atbildes", "ex": ["Have you got a car? Yes, I [[have]]. / No, I [[haven't]].", "Do you have a car? Yes, I [[do]]. / No, I [[don't]]."]}],
        ["For owning, no *-ing*: *She [[has got]] blue eyes.* (not *is having*)"],
        ["Piederībai nelieto *-ing*: *She [[has got]] blue eyes.* (nevis *is having*)"])),
    ("shall", "Shall I …? Shall we …?", "future", "2026-11-15", card(
        [["an offer", "*[[Shall]] I open the window?*"], ["a suggestion", "*[[Shall]] we go for a coffee?*"], ["a question word", "*What [[shall]] we do tonight?*"]],
        [["piedāvājums", "*[[Shall]] I open the window?*"], ["ierosinājums", "*[[Shall]] we go for a coffee?*"], ["jautājamais vārds", "*What [[shall]] we do tonight?*"]],
        [["[[Will]] I carry your bag? (an offer)", "[[Shall]] I carry your bag?"], ["Shall we [[to go]]?", "Shall we [[go]]?"], ["What [[we shall]] do?", "What [[shall we]] do?"]],
        [["[[Will]] I carry your bag? (piedāvājot)", "[[Shall]] I carry your bag?"], ["Shall we [[to go]]?", "Shall we [[go]]?"], ["What [[we shall]] do?", "What [[shall we]] do?"]],
        [{"t": "Answers", "ex": ["Shall I help you? Yes, please. / No, thanks, I'm fine.", "Shall we eat out? Good idea!"]}],
        [{"t": "Atbildes", "ex": ["Shall I help you? Yes, please. / No, thanks, I'm fine.", "Shall we eat out? Good idea!"]}],
        ["*shall* only with *I* and *we*, and the base verb after it."],
        ["*shall* tikai ar *I* un *we*, un aiz tā pamatforma."])),
    ("art_zero", "No article: I like cats. He lives in Riga.", "articles", "2026-11-15", card(
        [["things in general", "*I like [[cats]]. She drinks [[tea]].*"], ["names", "*He lives in [[Riga]]. [[Anna]] is from [[Latvia]].*"], ["sports, subjects", "*We play [[golf]]. She teaches [[maths]].*"]],
        [["vispārīgi", "*I like [[cats]]. She drinks [[tea]].*"], ["īpašvārdi", "*He lives in [[Riga]]. [[Anna]] is from [[Latvia]].*"], ["sports, mācības", "*We play [[golf]]. She teaches [[maths]].*"]],
        [["I like [[the]] cats. (all cats)", "I like [[cats]]."], ["He lives in [[the]] Riga.", "He lives in [[Riga]]."], ["She drinks [[the]] tea every morning.", "She drinks [[tea]] every morning."]],
        [["I like [[the]] cats. (visi kaķi)", "I like [[cats]]."], ["He lives in [[the]] Riga.", "He lives in [[Riga]]."], ["She drinks [[the]] tea every morning.", "She drinks [[tea]] every morning."]],
        [{"t": "*the* = these ones, the ones we know", "ex": ["[[Cats]] are clever. (all cats)", "[[The]] cats next door are noisy. (these cats)"]}],
        [{"t": "*the* = tieši šie, zināmie", "ex": ["[[Cats]] are clever. (visi kaķi)", "[[The]] cats next door are noisy. (tieši šie kaķi)"]}],
        ["Most countries have no article; *[[the]] UK, [[the]] USA* have one."],
        ["Vairumam valstu artikula nav; *[[the]] UK, [[the]] USA* ir izņēmumi."])),
    ("no_longer", "No longer, any more, any longer", "used_to", "2026-11-15", card(
        [["no longer", "*I [[no longer]] smoke. She's [[no longer]] my boss.*"], ["not … any more", "*I don't smoke [[any more]].*"], ["not … any longer", "*I don't smoke [[any longer]].*"]],
        [["no longer", "*I [[no longer]] smoke. She's [[no longer]] my boss.*"], ["not … any more", "*I don't smoke [[any more]].*"], ["not … any longer", "*I don't smoke [[any longer]].*"]],
        [["I don't smoke [[no more]].", "I don't smoke [[any more]]."], ["I [[no longer don't]] work there.", "I [[no longer]] work there."]],
        [["I don't smoke [[no more]].", "I don't smoke [[any more]].", "Tulkojot burtiski \"vairs nesmēķēju\", gribas divus noliegumus."], ["I [[no longer don't]] work there.", "I [[no longer]] work there."]],
        [{"t": "Where it goes", "ex": ["*no longer*: before the verb, after *be*: He [[no longer]] lives here. He's [[no longer]] here.", "*any more / any longer*: at the end: He doesn't live here [[any more]]."]}],
        [{"t": "Kur to liek", "ex": ["*no longer*: pirms darbības vārda, aiz *be*: He [[no longer]] lives here. He's [[no longer]] here.", "*any more / any longer*: beigās: He doesn't live here [[any more]]."]}],
        ["*anymore* (one word) is common too, especially in American English."],
        ["Bieži raksta arī *anymore* (vienā vārdā), īpaši amerikāņu angļu valodā."])),
    ("requests", "Could you …? Can I …? May I …?", "modal_verbs", "2026-11-15", card(
        [["you do it", "*[[Can]] / [[Could]] / [[Would]] you help me?*"], ["I do it", "*[[Can]] / [[Could]] / [[May]] I sit here?*"]],
        [["to dara otrs", "*[[Can]] / [[Could]] / [[Would]] you help me?*"], ["to daru es", "*[[Can]] / [[Could]] / [[May]] I sit here?*"]],
        [["Could you [[to help]] me?", "Could you [[help]] me?"], ["[[May you]] help me?", "[[Could you]] help me?"], ["Can you [[borrow]] me your pen?", "Can you [[lend]] me your pen?"]],
        [["Could you [[to help]] me?", "Could you [[help]] me?"], ["[[May you]] help me?", "[[Could you]] help me?"], ["Can you [[borrow]] me your pen?", "Can you [[lend]] me your pen?", "Latviski \"aizņemties\" un \"aizdot\" ir divi vārdi, angliski arī: *borrow* (paņemt), *lend* (iedot)."]],
        [{"t": "Answers", "ex": ["Could you help me? [[Sure.]] / [[Of course.]]", "Can I sit here? Yes, [[go ahead]]."]}],
        [{"t": "Atbildes", "ex": ["Could you help me? [[Sure.]] / [[Of course.]]", "Can I sit here? Yes, [[go ahead]]."]}],
        ["*Could* and *May* sound more polite than *Can*."],
        ["*Could* un *May* izklausās pieklājīgāk nekā *Can*."])),
    ("vp_ing_subject", "-ing at the start: Swimming is good for you", "verb_patterns", "2026-11-15", card(
        [["-ing + verb", "*[[Swimming]] is good for you.*"], ["-ing + more words", "*[[Learning]] a language takes time.*"]],
        [["-ing + darbības vārds", "*[[Swimming]] is good for you.*"], ["-ing + vēl vārdi", "*[[Learning]] a language takes time.*"]],
        [["[[Swim]] is good for you.", "[[Swimming]] is good for you."], ["[[Learn]] a language takes time.", "[[Learning]] a language takes time."], ["Watching old films [[are]] fun.", "Watching old films [[is]] fun."]],
        [["[[Swim]] is good for you.", "[[Swimming]] is good for you.", "Latviski \"peldēt ir veselīgi\": nenoteiksme, tāpēc gribas *Swim*."], ["[[Learn]] a language takes time.", "[[Learning]] a language takes time."], ["Watching old films [[are]] fun.", "Watching old films [[is]] fun."]],
        [{"t": "One activity: *is*", "ex": ["Cooking for friends [[relaxes]] me.", "[[Smoking]] is not allowed here."]}],
        [{"t": "Viena darbība: *is*", "ex": ["Cooking for friends [[relaxes]] me.", "[[Smoking]] is not allowed here."]}],
        ["*To learn a language takes time* is correct too, but formal; *It takes time to learn a language* is also common."],
        ["*To learn a language takes time* arī ir pareizi, bet oficiālāk; bieži saka arī *It takes time to learn a language*."])),
    ("vp_go_ing", "Go swimming, go for a walk, go to the gym", "verb_patterns", "2026-11-15", card(
        [["go + -ing", "*go [[shopping]], go [[swimming]], go [[skiing]]*"], ["go for a …", "*go [[for]] a walk, a run, a coffee*"], ["go to / on", "*go [[to]] the gym, go [[to]] work, go [[on]] holiday*"], ["go home", "*go [[home]]* (no *to*)"]],
        [["go + -ing", "*go [[shopping]], go [[swimming]], go [[skiing]]*"], ["go for a …", "*go [[for]] a walk, a run, a coffee*"], ["go to / on", "*go [[to]] the gym, go [[to]] work, go [[on]] holiday*"], ["go home", "*go [[home]]* (bez *to*)"]],
        [["Let's go [[to shopping]].", "Let's go [[shopping]]."], ["I'm going [[to home]].", "I'm going [[home]]."], ["We went [[for swimming]].", "We went [[swimming]]."]],
        [["Let's go [[to shopping]].", "Let's go [[shopping]]."], ["I'm going [[to home]].", "I'm going [[home]].", "Latviski \"iet uz mājām\", tāpēc gribas *to*."], ["We went [[for swimming]].", "We went [[swimming]]."]],
        [{"t": "Often both are possible", "ex": ["go [[swimming]] = go [[for]] a swim", "go [[running]] = go [[for]] a run"]}],
        [{"t": "Bieži der abi", "ex": ["go [[swimming]] = go [[for]] a swim", "go [[running]] = go [[for]] a run"]}],
        ["*go on* + *-ing* means *continue*: *Go on [[reading]].*"],
        ["*go on* + *-ing* nozīmē *turpināt*: *Go on [[reading]].*"])),
    # ── B1.1 (gap-points-b11-1.csv) ──
    ("if_when", "If or when", "cond_first", "2026-11-15", card(
        [["if = maybe", "*[[If]] I see her, I'll tell her.* (I'm not sure I'll see her.)"], ["when = sure", "*[[When]] I see her, I'll tell her.* (I'll see her.)"]],
        [["if = varbūt", "*[[If]] I see her, I'll tell her.* (Nezinu, vai satikšu.)"], ["when = noteikti", "*[[When]] I see her, I'll tell her.* (Noteikti satikšu.)"]],
        [["[[When]] it rains tomorrow, we'll stay in. (not sure)", "[[If]] it rains tomorrow, we'll stay in."], ["When I [[will arrive]], I'll call you.", "When I [[arrive]], I'll call you."]],
        [["[[When]] it rains tomorrow, we'll stay in. (nav droši)", "[[If]] it rains tomorrow, we'll stay in.", "Latviski abos gadījumos var teikt \"kad\", tāpēc angliski jāizšķir: droši vai nē."], ["When I [[will arrive]], I'll call you.", "When I [[arrive]], I'll call you."]],
        [{"t": "The first sentence decides", "ex": ["My train gets in at six. [[When]] I arrive, I'll call you.", "My brother might visit. [[If]] he comes, we'll go out."]}],
        [{"t": "Izšķir pirmais teikums", "ex": ["My train gets in at six. [[When]] I arrive, I'll call you.", "My brother might visit. [[If]] he comes, we'll go out."]}],
        ["After *if* and *when*: present simple, not *will*."],
        ["Aiz *if* un *when*: Present Simple, nevis *will*."])),
    ("vp_both", "Like, start, continue + -ing or to", "verb_patterns", "2026-11-15", card(
        [["both are right", "*I like [[swimming]]. = I like [[to swim]].*"], ["the same verbs", "*love, hate, prefer, start, begin, continue*"], ["would like", "*I'd like [[to go]].* (only *to*)"]],
        [["der abi", "*I like [[swimming]]. = I like [[to swim]].*"], ["tie paši darbības vārdi", "*love, hate, prefer, start, begin, continue*"], ["would like", "*I'd like [[to go]].* (tikai *to*)"]],
        [["I like [[work]] with him.", "I like [[working]] with him."], ["I'd like [[going]] home.", "I'd like [[to go]] home."], ["She started [[learn]] Spanish.", "She started [[learning]] Spanish."]],
        [["I like [[work]] with him.", "I like [[working]] with him."], ["I'd like [[going]] home.", "I'd like [[to go]] home."], ["She started [[learn]] Spanish.", "She started [[learning]] Spanish.", "Tulkojot burtiski \"sāka mācīties\", gribas pamatformu bez *to* vai *-ing*."]],
        [{"t": "Both right", "ex": ["It started [[raining]]. = It started [[to rain]].", "We continued [[working]]. = We continued [[to work]]."]}],
        [{"t": "Der abi", "ex": ["It started [[raining]]. = It started [[to rain]].", "We continued [[working]]. = We continued [[to work]]."]}],
        ["*stop, remember, forget, try* change their meaning with *-ing* or *to*."],
        ["*stop, remember, forget, try* ar *-ing* vai *to* maina nozīmi."])),
    ("no_none", "No, none, not any", "quantity", "2026-11-15", card(
        [["no + noun", "*There's [[no]] milk.*"], ["not any + noun", "*There isn't [[any]] milk.*"], ["none (alone, of)", "*How many came? [[None]]. [[None of]] my friends came.*"]],
        [["no + lietvārds", "*There's [[no]] milk.*"], ["not any + lietvārds", "*There isn't [[any]] milk.*"], ["none (viens, of)", "*How many came? [[None]]. [[None of]] my friends came.*"]],
        [["There isn't [[no]] milk.", "There isn't [[any]] milk."], ["[[None]] people came.", "[[No]] people came."], ["[[No of]] them came.", "[[None of]] them came."]],
        [["There isn't [[no]] milk.", "There isn't [[any]] milk.", "Latviski \"nav nekāda piena\": divi noliegumi, angliski tikai viens."], ["[[None]] people came.", "[[No]] people came."], ["[[No of]] them came.", "[[None of]] them came."]],
        [{"t": "Only one negative", "ex": ["I have [[nothing]] to wear. = I don't have [[anything]] to wear.", "✗ I don't have [[nothing]] to wear."]}],
        [{"t": "Tikai viens noliegums", "ex": ["I have [[nothing]] to wear. = I don't have [[anything]] to wear.", "✗ I don't have [[nothing]] to wear."]}],
        ["*None of* + plural can take a singular or a plural verb: *None of them [[has]] / [[have]] a car.*"],
        ["Aiz *none of* + daudzskaitlis der gan vienskaitlis, gan daudzskaitlis: *None of them [[has]] / [[have]] a car.*"])),
    ("must_vs_have_to", "Must or have to", "modal_verbs", "2026-11-15", card(
        [["now", "*I [[must]] / [[have to]] go.* (both are possible)"], ["past", "*I [[had to]] go.*"], ["future", "*I'll [[have to]] go. We [[might have to]] wait.*"], ["question", "*[[Do]] I [[have to]] sign here?*"]],
        [["tagad", "*I [[must]] / [[have to]] go.* (der abi)"], ["pagātne", "*I [[had to]] go.*"], ["nākotne", "*I'll [[have to]] go. We [[might have to]] wait.*"], ["jautājums", "*[[Do]] I [[have to]] sign here?*"]],
        [["I [[must]] work late yesterday.", "I [[had to]] work late yesterday."], ["We [[will must]] leave early.", "We [[will have to]] leave early."], ["She [[hasn't to]] work today.", "She [[doesn't have to]] work today."]],
        [["I [[must]] work late yesterday.", "I [[had to]] work late yesterday."], ["We [[will must]] leave early.", "We [[will have to]] leave early."], ["She [[hasn't to]] work today.", "She [[doesn't have to]] work today."]],
        [{"t": "*mustn't* and *don't have to* are different", "ex": ["You [[mustn't]] park here. (not allowed)", "You [[don't have to]] pay. (not necessary)"]}],
        [{"t": "*mustn't* un *don't have to* nozīmē dažādas lietas", "ex": ["You [[mustn't]] park here. (nedrīkst)", "You [[don't have to]] pay. (nav vajadzīgs)"]}],
        ["In British English *must* often shows the speaker's own feeling, *have to* a rule; very often both are possible."],
        ["Britu angļu valodā *must* bieži izsaka paša runātāja sajūtu, *have to* noteikumu; ļoti bieži der abi."])),
    # ── B1.2 (gap-points-b12-1.csv) ──
    ("pc_always", "He's always losing his keys!", "present_continuous", "2026-11-15", card(
        [["now", "*He'[[s always losing]] his keys!*"], ["past", "*She [[was always complaining]].*"], ["also", "*constantly, forever*: *They're [[constantly arguing]].*"]],
        [["tagad", "*He'[[s always losing]] his keys!*"], ["pagātne", "*She [[was always complaining]].*"], ["arī", "*constantly, forever*: *They're [[constantly arguing]].*"]],
        [["He [[always is]] losing his keys.", "He [[is always]] losing his keys."], ["She's always [[lose]] her keys.", "She's always [[losing]] her keys."]],
        [["He [[always is]] losing his keys.", "He [[is always]] losing his keys."], ["She's always [[lose]] her keys.", "She's always [[losing]] her keys."]],
        [{"t": "It happens too often, and it annoys me", "ex": ["My flatmate [[is always borrowing]] my charger. (and it drives me mad)", "My flatmate [[always borrows]] my charger. (correct too, but neutral)"]}],
        [{"t": "Tas notiek pārāk bieži, un tas mani kaitina", "ex": ["My flatmate [[is always borrowing]] my charger. (un tas mani kaitina)", "My flatmate [[always borrows]] my charger. (arī pareizi, bet neitrāli)"]}],
        ["*always* goes between *is / was* and the verb-*ing*."],
        ["*always* liek starp *is / was* un darbības vārdu ar *-ing*."])),
    ("would_habit", "Would for past habits", "used_to", "2026-11-15", card(
        [["a repeated action", "*Every summer we [[would go]] to the lake.*"], ["a state", "*I [[used to have]] a dog.* (not *would have*)"]],
        [["atkārtota darbība", "*Every summer we [[would go]] to the lake.*"], ["stāvoklis", "*I [[used to have]] a dog.* (nevis *would have*)"]],
        [["I [[would have]] a dog when I was a child.", "I [[used to have]] a dog when I was a child."], ["We [[would lived]] in Riga.", "We [[used to live]] in Riga."], ["Last summer we [[would go]] to Rome. (once)", "Last summer we [[went]] to Rome."]],
        [["I [[would have]] a dog when I was a child.", "I [[used to have]] a dog when I was a child."], ["We [[would lived]] in Riga.", "We [[used to live]] in Riga."], ["Last summer we [[would go]] to Rome. (vienreiz)", "Last summer we [[went]] to Rome."]],
        [{"t": "For actions, all three are right", "ex": ["We [[would play]] outside. = We [[used to play]] outside. = We [[played]] outside every day."]}],
        [{"t": "Darbībām der visi trīs", "ex": ["We [[would play]] outside. = We [[used to play]] outside. = We [[played]] outside every day."]}],
        ["Not with *have, be, live, know, like* (states): use *used to* or the past simple."],
        ["Nelieto ar *have, be, live, know, like* (stāvokļi): lieto *used to* vai Past Simple."])),
    ("should_have", "Should have, could have done", "more_modals", "2026-11-15", card(
        [["should have + 3rd form", "*You [[should have told]] me.* (you didn't, and it was wrong)"], ["shouldn't have + 3rd form", "*You [[shouldn't have shouted]].* (you did, and it was wrong)"], ["could have + 3rd form", "*We [[could have won]].* (it was possible, but it didn't happen)"]],
        [["should have + 3. forma", "*You [[should have told]] me.* (tu to neizdarīji, un tas bija nepareizi)"], ["shouldn't have + 3. forma", "*You [[shouldn't have shouted]].* (tu to izdarīji, un tas bija nepareizi)"], ["could have + 3. forma", "*We [[could have won]].* (tas bija iespējams, bet nenotika)"]],
        [["You [[should told]] me.", "You [[should have told]] me."], ["You should have [[tell]] me.", "You should have [[told]] me."], ["You should [[of]] told me.", "You should [[have]] told me."]],
        [["You [[should told]] me.", "You [[should have told]] me.", "Tulkojot burtiski \"vajadzēja pateikt\", gribas *should told*; pagātni rāda *have* + 3. forma."], ["You should have [[tell]] me.", "You should have [[told]] me."], ["You should [[of]] told me.", "You should [[have]] told me."]],
        [{"t": "*could have* can criticise too", "ex": ["You [[could have called]] me! (Why didn't you?)"]}],
        [{"t": "Ar *could have* arī var pārmest", "ex": ["You [[could have called]] me! (Kāpēc nepiezvanīji?)"]}],
        ["We say *should've*, but we write *should have*."],
        ["Runā saka *should've*, bet raksta *should have*."])),
    ("each_every", "Each, every, all, whole", "agreement", "2026-11-15", card(
        [["each / every + one", "*Every room [[has]] a balcony. Each student [[gets]] a book.*"], ["each of + the / my", "*Each of the flats [[has]] a garden.* (not *every of*)"], ["all day / every day", "*all day* = the whole day; *every day* = each day"]],
        [["each / every + viens", "*Every room [[has]] a balcony. Each student [[gets]] a book.*"], ["each of + the / my", "*Each of the flats [[has]] a garden.* (nevis *every of*)"], ["all day / every day", "*all day* = visu dienu; *every day* = katru dienu"]],
        [["Every [[students have]] a locker.", "Every [[student has]] a locker."], ["[[Every of]] them came.", "[[Each of]] them came."], ["my [[all]] life", "my [[whole]] life"]],
        [["Every [[students have]] a locker.", "Every [[student has]] a locker."], ["[[Every of]] them came.", "[[Each of]] them came.", "Tulkojot burtiski \"katrs no viņiem\", gribas *every of*."], ["my [[all]] life", "my [[whole]] life"]],
        [{"t": "Two things: *each*", "ex": ["She had a bag in [[each]] hand.", "[[Almost every]] colleague works from home. (not *almost each*)"]}],
        [{"t": "Divas lietas: *each*", "ex": ["She had a bag in [[each]] hand.", "[[Almost every]] colleague works from home. (nevis *almost each*)"]}],
        ["*the whole day = all day = all (of) the day*; *the whole book = all (of) the book*."],
        ["*the whole day = all day = all (of) the day*; *the whole book = all (of) the book*."])),
    ("rel_what", "What = the thing that", "relative_clauses", "2026-11-15", card(
        [["what (no noun before it)", "*I didn't hear [[what]] he said. [[What]] I need is a holiday.*"], ["noun / everything + that", "*Everything [[that]] he said was true. The book [[that]] I bought …*"]],
        [["what (pirms tā nav lietvārda)", "*I didn't hear [[what]] he said. [[What]] I need is a holiday.*"], ["lietvārds / everything + that", "*Everything [[that]] he said was true. The book [[that]] I bought …*"]],
        [["The book [[what]] I bought is great.", "The book [[that]] I bought is great."], ["Everything [[what]] he said was true.", "Everything [[that]] he said was true."], ["I didn't hear [[that]] he said.", "I didn't hear [[what]] he said."]],
        [["The book [[what]] I bought is great.", "The book [[that]] I bought is great.", "Latviski \"grāmata, ko es nopirku\": \"ko\", tulkojot burtiski, kļūst par *what*."], ["Everything [[what]] he said was true.", "Everything [[that]] he said was true.", "Tulkojot burtiski \"viss, ko viņš teica\", gribas *what*."], ["I didn't hear [[that]] he said.", "I didn't hear [[what]] he said."]],
        [{"t": "After a noun, *that* can be left out", "ex": ["Everything ([[that]]) he said was true.", "The book ([[that]]) I bought is great."]}],
        [{"t": "Aiz lietvārda *that* var izlaist", "ex": ["Everything ([[that]]) he said was true.", "The book ([[that]]) I bought is great."]}],
        ["*That's [[what]] I mean.* (not *That's that I mean*)"],
        ["*That's [[what]] I mean.* (nevis *That's that I mean*)"])),
    ("wont_refuse", "Won't: the door won't open", "future", "2026-11-15", card(
        [["now", "*My laptop [[won't]] switch on. He [[won't]] listen.*"], ["past", "*The car [[wouldn't]] start this morning.*"]],
        [["tagad", "*My laptop [[won't]] switch on. He [[won't]] listen.*"], ["pagātne", "*The car [[wouldn't]] start this morning.*"]],
        [["The door [[won't to]] open.", "The door [[won't]] open."], ["My laptop [[doesn't want to]] switch on.", "My laptop [[won't]] switch on."], ["Yesterday the car [[won't]] start.", "Yesterday the car [[wouldn't]] start."]],
        [["The door [[won't to]] open.", "The door [[won't]] open."], ["My laptop [[doesn't want to]] switch on.", "My laptop [[won't]] switch on.", "Tulkojot burtiski \"negrib ieslēgties\", gribas *doesn't want to*."], ["Yesterday the car [[won't]] start.", "Yesterday the car [[wouldn't]] start."]],
        [{"t": "A person or a thing refuses", "ex": ["The baby [[won't]] eat her soup.", "My friend [[wouldn't]] let me pay."]}],
        [{"t": "Cilvēks vai lieta atsakās", "ex": ["The baby [[won't]] eat her soup.", "My friend [[wouldn't]] let me pay."]}],
        ["*The car doesn't start* is correct too: it only says what happens."],
        ["*The car doesn't start* arī ir pareizi: tas tikai saka, kas notiek."])),
]


# The row headings: the form in focus, as on the topic cards (teacher, 15 November). Same for EN and LV.
HEADS = {
    "have_got": ["have got / has got", "haven't got / don't have", "Have you got …? / Do you have …?"],
    "shall": ["Shall I …?", "Shall we …?", "What / Where shall we …?"],
    "art_zero": ["— cats, — tea", "— Riga, — Latvia", "— golf, — maths"],
    "no_longer": ["no longer", "not … any more", "not … any longer"],
    "requests": ["Can / Could / Would you …?", "Can / Could / May I …?"],
    "vp_ing_subject": ["Swimming is …", "Learning a language takes …"],
    "vp_go_ing": ["go + -ing", "go for a …", "go to / go on", "go home"],
    "if_when": ["If …", "When …"],
    "vp_both": ["like + -ing / like + to", "love, hate, prefer, start, begin, continue", "would like + to"],
    "no_none": ["no + noun", "not any + noun", "none / none of"],
    "must_vs_have_to": ["must / have to", "had to", "will have to / might have to", "Do I have to …?"],
    "pc_always": ["is always + -ing", "was always + -ing", "constantly / forever + -ing"],
    "would_habit": ["would + verb", "used to + state"],
    "should_have": ["should have + 3rd form", "shouldn't have + 3rd form", "could have + 3rd form"],
    "each_every": ["each / every + singular", "each of the …", "all day / every day"],
    "rel_what": ["what …", "noun / everything + that"],
    "wont_refuse": ["won't + verb", "wouldn't + verb"],
}
for _pid, _l, _s, _d, _c in POINTS:
    for _lang in ("en", "lv"):
        for _row, _h in zip(_c[_lang]["choice"]["rows"], HEADS[_pid]):
            if _lang == "lv":
                for _a, _b in (("3rd form", "3. forma"), ("singular", "vienskaitlis"), ("noun", "lietvārds"), ("state", "stāvoklis"), ("verb", "darbības vārds")): _h = _h.replace(_a, _b)
            _row[0] = _h

# The tile picture: one everyday sentence with the form in gold (**…**), like the topic tiles (teacher, 15 November)
POSTER = {
    "have_got": "I **haven't got** time. I**'ve got** a cat.",
    "shall": "**Shall** we order pizza again?",
    "art_zero": "**Cats** ignore people. **Dogs** love them.",
    "no_longer": "I **no longer** check my email at night.",
    "requests": "**Could you** hold my coffee for a second?",
    "vp_ing_subject": "**Running** is easy. **Starting** is hard.",
    "vp_go_ing": "Let's **go for** a walk. Or **go shopping**.",
    "if_when": "**When** I get paid, I'll buy it. **If** I get paid…",
    "vp_both": "I love **cooking**. I love **to eat** even more.",
    "no_none": "**None of** my plants survived. **No** surprise.",
    "must_vs_have_to": "I **had to** work late. Again.",
    "pc_always": "You**'re always losing** your keys!",
    "would_habit": "Grandma **would bake** every Sunday.",
    "should_have": "I **should have saved** the file.",
    "each_every": "**Every** meeting **has** a meeting about it.",
    "rel_what": "**What** I need is a holiday.",
    "wont_refuse": "My laptop **won't** switch on. Today of all days.",
}
