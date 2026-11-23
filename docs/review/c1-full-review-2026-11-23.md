# C1 full review, 23 November 2026

Independent review of everything made for the new C1 level: the ten rule cards (`app/authoring/cards2_c1.py`, EN and LV), the old-layout `CARDS` / `LV_CARDS` entries at the end of `app/authoring/b1_topics.py`, the ten tile lines (`TILE_LINES` in `app/assets/app.js`), the 114 tasks in `docs/task-drafts/c1-*.csv` (generators `docs/task-drafts/_src/c1_*.py`) and the judge notes `docs/review/blind/c1-*-judge.md`.
Nothing was changed. Grammar was checked against Hewings, *Advanced Grammar in Use* (3rd ed.), and Murphy. British English is the default.

How the findings are written: **where** (file, topic, row or task), **problem**, **rule** (the document and line it breaks), **fix** (exact new text), **must fix** or **suggestion**.

Short names for the rule sources:
- IWR = `docs/ITEM-WRITING-RULES.md`, HO = `docs/AGENT-HANDOVER.md`, LVT = `docs/LATVIAN-TERMS.md`, BE = `app/tests/bad_examples.json`.
- The rule that applies most often: IWR 164 *"A help card example is never a task's answer. Before a task goes in, compare its answers with the card of its point."* (and BE, c-2206: *"Compare every task of a point with its card (examples, mistakes, watch lines) and use another…"*).
- IWR 171 *"…the example on a topic card has one short, witty, everyday sentence that shows the rule … Not a plain textbook sentence (*I'm measuring the kitchen*)…"*; HO 44 (the same, teacher, 23 November).
- HO 158 *"one style: a form table, exactly three typical mistakes, two or three 'When we use it' blocks, one to three 'Watch out' points, EN and LV in the same structure"*.
- HO 61 *"a Latvian note on a typical mistake only where Latvian causes it, starting *Tulkojot burtiski…*"*.

**What passes on every card:** one Form · Example table with four rows; exactly three mistakes; two or three *When we use it* blocks; one or two *Watch out* points; EN and LV have the same structure; the form is marked `[[ ]]`. **What passes on every task:** no grammar terms in instructions, no double dash, no Latvian surnames, no *skolēni*, `check_draft.php` 0 refused for all 11 files.

**The biggest problem (cards):** every example on every C1 card (table, mistakes, *When we use it* and *Watch out*) is the answer, the wrong sentence or a right option of a C1 task, often word for word. A learner who opens the card with the *?* during a task sees the answer. The new texts below (A, card by card) replace all of them with complete, natural, mostly witty everyday sentences that match no task. Each block can be pasted into `cards2_c1.py` as it is.


## A. Rule cards (`app/authoring/cards2_c1.py`)

### A0. Points for all cards

**A0.1 · All ten cards · the noun that decides is not marked (teacher's comment b)** · *must fix*
- Problem: in sentences where the subject noun decides the verb or the word order, only the verb is marked (green). The markup already exists: commit f37d32d added `{{noun}}` (class `hl-noun`, bold with a gold underline, `app.js` `nounHl`, `app.css` 1038). No card uses it yet.
- Rule: the teacher's instruction today (b): mark the main nouns, but not in the same green as the form.
- Fix: use `{{ }}` where the noun is the point:
  - (1) **adv_agree**, every example (the noun that decides: *{{The boss}}, together with her two dogs, [[is]]…*);
  - (2) **adv_order**, the subject after the helping verb (*[[Seldom have]] {{I}} seen…*);
  - (3) **adv_part**, the subject of the main clause that the *-ing* part belongs to (*[[Trying]] to look relaxed, {{I}} spilled…*), and in the wrong sentence, the wrong subject;
  - (4) **adv_subj**, the subject after *that* that keeps the base form (*insists that {{breakfast}} [[be]] served*).

  The new texts below already include this. Suggestion for the style: the tiles show the form in gold, so a gold underline for the noun on the cards can be read as "the form" by learners who come from a tile. Consider a dotted underline in the text colour (`border-bottom: 2px dotted currentColor`) and keep the bold.

**A0.2 · All cards, EN · "past participle" where all other cards say "3rd form"** · *suggestion*
- Problem: the EN C1 cards write *will have + past participle*, *can be + past participle*, *having + past participle*. `cards2_h.py` and the B cards write *3rd form*, and the LV C1 cards write *3. forma*.
- Rule: HO 158 (one style for all cards); HO 154 lists the *past participle* / *3rd form* mix as an open inconsistency.
- Fix: write *3rd form* on the EN C1 cards. The new texts below do this.

**A0.3 · LV cards and LV task explanations · three names for the same thing** · *suggestion*
- Problem: *ilgstošā forma*, *Continuous forma* and *vienkāršā forma* / *Present Simple* are all used for the same idea. The generator `lib.py` `LV_SUBS` turns *ilgstošā forma* into *Continuous forma*, but the cards (adv_present, adv_perfect) keep *ilgstošā forma*.
- Rule: IWR 12 *"Latvian terms from LATVIAN-TERMS.md"*; LVT *"Present Simple, Past Simple … English tense names are kept"*.
- Fix: use *Present Simple / Present Continuous / Continuous forma* everywhere, as the new LV texts below do.

**A0.4 · All cards · the witty card example is not shown** · *must fix* (see also D2)
- Problem: the witty line exists only in `b1_topics.py` `CARDS[...]["example"]`. `ruleCard2()` (app.js 1816-1883) never shows `example`, so the v2 card shows only plain textbook sentences.
- Rule: IWR 171, HO 44.
- Fix: put the witty line on the card itself, as the first example of a *When we use it* block or as a table example. The new texts below do this for every card.

### A1. adv_present (Advanced present simple and continuous)

**A1.1 · row 4 · heading "Saying it does it" / "Vārdi ir darbība"** · *must fix*
- Problem: the heading says nothing (the teacher's comment c). The description *"apologise, promise, suggest: present simple"* does not explain why.
- Fix: EN *"Promising, apologising, suggesting"* · *"saying the verb is the act itself (*I promise* = I make a promise with these words): present simple, not continuous"*. LV *"Solīt, atvainoties, ieteikt"* · *"pasakot šo darbības vārdu, mēs jau izdarām pašu darbību (*I promise* = ar šiem vārdiem es dodu solījumu): Present Simple, nevis Continuous"*.

**A1.2 · row 3 · "Typical behaviour" / "Raksturīga uzvedība"** · *must fix*
- Problem: the heading leaves out the point of the form (irritation). The card's own old text says *"often with irritation"*.
- Fix: EN *"Annoying habits"* · *"*always / constantly / forever* + continuous: it happens too often and it annoys us"*. LV *"Kaitinošs ieradums"* · *"*always / constantly / forever* + Continuous forma: tas notiek pārāk bieži, un tas mūs kaitina"*.

**A1.3 · row 1 example *The kitchen measures 3 by 4. I'm measuring it now.*** · *must fix*
- Problem: IWR 171 names exactly this sentence as the kind that is not allowed. It is also illogical (why measure a kitchen whose size you know?), "3 by 4" has no unit, and it is the answer of c1-pres-1 rows 2-3.
- Fix: see the new block.

**A1.4 · row 2 example *I believe you now.*** · *must fix*
- Problem: not something people say. The description does not say the key point, that these verbs stay simple *even about this moment*.

**A1.5 · use 2 example *So I'm standing in the queue and this woman turns round…*** · *must fix*
- Problem: an unfinished sentence (the teacher's comment a), and the answer of c1-pres-2 row 2.

**A1.6 · watch line *"I'm not suggesting is as correct as I don't suggest"*** · *must fix*
- Problem: wrong. *I don't suggest you were careless* is not natural English in this meaning: Hewings unit 1 gives the continuous as the usual negative of these verbs. The example is also a right option of c1-pres-2 row 9.

**A1.7 · every example is a task** · *must fix*
- *measures / measuring* = pres-1 rows 2-3; *considers taking early retirement* = pres-1 row 4; *constantly changing his mind* = pres-1 row 5; *suitcase is weighing five kilos* = pres-1 row 9; *We apologise for the delay* = pres-1 row 10; *I'm promising I'll pay you back* = pres-2 row 9; *Jones passes to Taylor, who shoots and scores* = pres-2 row 4; *I gather you're looking for a flat* = pres-2 row 5.
- Rule: IWR 164; BE c-2206.

**A1.8 · points the tasks test but the card does not teach** · *must fix*
- Problem: *usually* + continuous (pres-1 row 6), *I'm wondering if* (pres-2 row 6), *appear* = seem (pres-2 row 7), *be expecting a baby* (pres-2 row 8). They are only in the old `CARDS` text, which the v2 card replaces.
- Rule: IWR 71 *"every task of a topic uses only the forms on its card"*.

**New card (replaces A1.1-A1.8):**
```python
"adv_present": card(
    [["One verb, two meanings", "a state (what something is like, what we think) → simple; an action going on → continuous", "*I [[think]] the sofa is too big. I'[[m thinking]] of selling it.*"],
     ["Verbs that stay simple", "*believe, doubt, own, belong, know, prefer*: simple, even about this very moment", "*Right now I [[doubt]] we'll finish before midnight.*"],
     ["Annoying habits", "*always / constantly / forever* + continuous: it happens too often and it annoys us", "*My laptop [[is forever updating]] itself when I'm in a hurry.*"],
     ["Promising, apologising, suggesting", "saying the verb is the act itself (*I promise* = I make a promise with these words): present simple, not continuous", "*I [[suggest]] we order pizza and call it a meeting.*"]],
    [["Viens darbības vārds, divas nozīmes", "stāvoklis (kāds kaut kas ir, ko mēs domājam): Present Simple; darbība, kas notiek: Present Continuous", "*I [[think]] the sofa is too big. I'[[m thinking]] of selling it.*"],
     ["Paliek Present Simple", "*believe, doubt, own, belong, know, prefer*: Present Simple arī par šo brīdi", "*Right now I [[doubt]] we'll finish before midnight.*"],
     ["Kaitinošs ieradums", "*always / constantly / forever* + Continuous forma: tas notiek pārāk bieži, un tas mūs kaitina", "*My laptop [[is forever updating]] itself when I'm in a hurry.*"],
     ["Solīt, atvainoties, ieteikt", "pasakot šo darbības vārdu, mēs jau izdarām pašu darbību (*I promise* = ar šiem vārdiem es dodu solījumu): Present Simple, nevis Continuous", "*I [[suggest]] we order pizza and call it a meeting.*"]],
    [["This bag [[is belonging]] to the man by the window.", "This bag [[belongs]] to the man by the window."],
     ["She [[considers]] moving to Spain.", "She[['s considering]] moving to Spain."],
     ["I[['m apologising]] for the mess in the kitchen.", "I [[apologise]] for the mess in the kitchen."]],
    (same three for LV),
    [{"t": "A feeling or situation that is new, temporary or changing", "s": ["these days", "at the moment", "this week"], "ex": ["I [[love]] my job. I'm just not [[loving]] this Monday.", "I'm [[finding]] this course harder than I expected."]},
     {"t": "Stories, jokes and live commentary: the background continuous, the events simple", "s": ["so", "suddenly", "and then"], "ex": ["So I'm [[sitting]] in the dentist's chair, and my phone [[starts]] playing my ringtone at full volume.", "Silva [[takes]] the corner, the keeper [[drops]] it, and it's in!"]},
     {"t": "News we have heard, and polite requests", "s": ["I hear", "I gather", "I'm wondering if"], "ex": ["I [[gather]] the meeting has been moved to Thursday.", "I'[[m wondering]] if you could cover my shift on Friday."]}],
    [{"t": "Sajūta vai situācija, kas ir jauna, īslaicīga vai mainās", (same s, ex)},
     {"t": "Stāsti, joki un tiešraides komentārs: fons Continuous formā, notikumi Present Simple", (same s, ex)},
     {"t": "Dzirdēta ziņa un pieklājīgs lūgums", (same s, ex)}],
    ["In the negative, the continuous is usual: *I'[[m not saying]] it's your fault.* (= that is not what I mean)",
     "Some verbs change meaning in the continuous: *She [[appears]] to be asleep.* (= seems) · *She'[[s appearing]] in a musical.* (= is performing) · *We'[[re expecting]] a baby.* (= she is pregnant)",
     "*usually* + continuous: something in progress at that time: *At seven I'[[m usually feeding]] the cat.*"],
    ["Noliegumā parasti lieto Continuous formu: *I'[[m not saying]] it's your fault.* (= es to nedomāju)",
     "Dažiem darbības vārdiem Continuous formā ir cita nozīme: *She [[appears]] to be asleep.* (= šķiet) · *She'[[s appearing]] in a musical.* (= uzstājas) · *We'[[re expecting]] a baby.* (= gaidām bērnu)",
     "*usually* + Continuous forma: darbība tajā laikā parasti jau notiek: *At seven I'[[m usually feeding]] the cat.*"]),
```

### A2. adv_past

**A2.1 · row 2 · heading "A count" / "Skaits"** · *must fix*
- Problem: the heading says nothing. The row's example is also mistake 1 of the same card, word for word: the same sentence twice on one card.
- Fix: EN *"How many times"* · *"a number of times (*three times, twice*): past simple, never continuous"*. LV *"Cik reižu"* · *"reižu skaits (*three times, twice*): Past Simple, nekad Continuous"*.

**A2.2 · row 1 LV "Viens pēc otra"** · *suggestion*
- Problem: no noun, so it is unclear what follows what.
- Fix: *"Notikumi cits pēc cita"*.

**A2.3 · every example is a task** · *must fix*
- *alarm went off as soon as he lit the candle* = past-1 row 2; *flew to Oslo four times* = row 3; *sure we had met before* = row 4; *hoarse … had been shouting* = row 6; *had been knowing each other* = row 5 (the exact repeat BE c-2206 warns about); *have hoped the weather would hold* = row 9; *dropped her keys while … taxi* = row 3 option; *had hoped to finish by Friday*, *was meaning to call you* = row 9 options; *I wish I had kept the receipt* = row 8 answer.
- Rule: IWR 164; BE c-2206.

**A2.4 · row 4 "The cause of a past state"** · *suggestion*
- Problem: it covers only the cause. Task past-1 row 11 (*had been waiting for over an hour* by a past moment) tests an activity going on up to a past moment, which no row teaches.
- Fix: the description in the new block.

**New card:**
```python
"adv_past": card(
    [["Events in order", "past simple for each event, also after *as soon as, the moment*", "*My phone [[died]] the moment I [[found]] the address.*"],
     ["How many times", "a number of times (*three times, twice*): past simple, never continuous", "*We [[moved]] house three times before I was ten.*"],
     ["Earlier than a past moment", "past perfect: *had* + 3rd form", "*By the time I got to the shop, they [[had sold]] the last cake.*"],
     ["Up to a past moment, and its result", "past perfect continuous: *had been* + *-ing*", "*I was exhausted because I [[had been painting]] the kitchen all day.*"]],
    [["Notikumi cits pēc cita", "Past Simple katram notikumam, arī aiz *as soon as, the moment*", (same example)],
     ["Cik reižu", "reižu skaits (*three times, twice*): Past Simple, nekad Continuous", (same)],
     ["Agrāk par pagātnes brīdi", "Past Perfect: *had* + 3. forma", (same)],
     ["Līdz pagātnes brīdim, un tā sekas", "Past Perfect Continuous: *had been* + *-ing*", (same)]],
    [["We [[were going]] to the gym three times last week.", "We [[went]] to the gym three times last week."],
     ["I [[had been owning]] that car for years before it broke down.", "I [[had owned]] that car for years before it broke down."],
     ["We [[have expected]] a quiet weekend, but the in-laws arrived.", "We [[had expected]] a quiet weekend, but the in-laws arrived."]],
    (same three for LV),
    [{"t": "A situation and the event that happened in it", "s": ["while", "when", "as"], "ex": ["The fire alarm [[went off]] while I [[was washing]] my hair."]},
     {"t": "Plans and hopes that came to nothing", "s": ["had hoped", "were going to", "had planned"], "ex": ["I [[had planned]] a healthy dinner. Then I walked past the bakery.", "We [[were going to]] paint the hall, but we watched a film instead."]}],
    [{"t": "Situācija un notikums, kas tajā notika", ...}, {"t": "Plāni un cerības, kas nepiepildījās", ...}],
    ["*I wish* + past perfect: a regret about the past: *I wish I [[had taken]] a photo of the menu.*"],
    ["*I wish* + Past Perfect: nožēla par pagātni: *I wish I [[had taken]] a photo of the menu.*"]),
```

### A3. adv_perfect

**A3.1 · row 3 · heading "since", description "present perfect for the rest"** · *must fix*
- Problem: *"for the rest"* is vague. The row does not teach *since you've lived here* (both situations still going on), which task perf-1 row 5 tests. LV *"Present Perfect pārējam"* is just as vague.
- Fix: in the new block.

**A3.2 · mistake 2 *Once you [[paid]] … / Once you've [[paid]]*** · *must fix*
- Problem: the marked word *paid* did not change, and the change (*'ve*) is not marked.
- Rule: the brief: *"only the changed words marked in a mistake"* (cards2 docstrings, `app.js` 1858).
- Fix: *"You can leave the moment you [[finished]]."* / *"You can leave the moment you'[[ve finished]]."* (in the new block).

**A3.3 · the future perfect (task perf-1 row 12, *By next May I'll have taught…*) is not on the v2 card** · *must fix*
- Rule: IWR 71.
- Fix: a third *When we use it* block (in the new block).

**A3.4 · row 4 "The first time" with a *third time* example; *It was the first time* + past perfect (perf-1 row 9 option) is missing** · *suggestion*

**A3.5 · every example is a task** · *must fix*
- *three coffees* = perf-1 row 2; *didn't do much this morning* = row 3; *Since she joined, sales have doubled* = row 4; *third time she's lost her keys* = row 8; *first time I am seeing snow* = row 9; *Once you paid* = row 7; *been having this phone since May* = row 11; *text you the moment I've got the results* = row 6; *thought to have left the country* = row 13; *denied having read the letter* = row 14; *rung four times / been ringing all morning* = rows 10-11.

**New card:**
```python
"adv_perfect": card(
    [["The time is not over yet", "*today, this week, this morning* (while it is still morning): present perfect", "*It's only Tuesday, and I'[[ve]] already [[spent]] my weekly budget.*"],
     ["The time is over", "*this morning* said in the afternoon: past simple", "*It's three o'clock. I [[skipped]] breakfast this morning, and now I could eat a horse.*"],
     ["since", "*since* + past simple for when it started, present perfect in the main clause; if both still go on, present perfect in both", "*Since I [[bought]] a smartwatch, I'[[ve become]] obsessed with steps.*"],
     ["The first, second … time", "*This is the first time* + present perfect; *It was the first time* + past perfect", "*This is the first time I'[[ve made]] bread, so please be kind.*"]],
    [["Laiks vēl nav beidzies", "*today, this week, this morning* (kamēr vēl ir rīts): Present Perfect", (same)],
     ["Laiks ir beidzies", "*this morning*, ja runājam pēcpusdienā: Past Simple", (same)],
     ["since", "*since* + Past Simple: kad tas sākās; galvenajā teikumā Present Perfect; ja abas situācijas vēl turpinās, abās Present Perfect", (same)],
     ["Pirmā, otrā … reize", "*This is the first time* + Present Perfect; *It was the first time* + Past Perfect", (same)]],
    [["It's the first time I [[eat]] sushi.", "It's the first time I'[[ve eaten]] sushi."],
     ["You can leave the moment you [[finished]].", "You can leave the moment you'[[ve finished]]."],
     ["I'[[ve been owning]] this bike since 2019.", "I'[[ve owned]] this bike since 2019."]],
    [["It's the first time I [[eat]] sushi.", "It's the first time I'[[ve eaten]] sushi.", "Tulkojot burtiski \"pirmo reizi ēdu\", iznāk tagadne; angliski: *I've eaten*."], (2 and 3 as EN)],
    [{"t": "A future moment in a time clause", "s": ["the moment", "once", "as soon as"], "ex": ["Call me the moment you'[[ve landed]]."]},
     {"t": "The perfect after *to* and *-ing*", "s": ["seems to", "admitted", "having"], "ex": ["She seems [[to have forgotten]] our meeting.", "He admitted [[having eaten]] my yoghurt."]},
     {"t": "Up to a point in the future", "s": ["by Friday", "by the time", "by next year"], "ex": ["By the time you read this, I'[[ll have left]] the office."]}],
    [{"t": "Nākotnes brīdis laika palīgteikumā", ...}, {"t": "*to have* + 3. forma un *having* + 3. forma", ...}, {"t": "Līdz brīdim nākotnē: *will have* + 3. forma", ...}],
    ["How many: simple (*I'[[ve sent]] six emails*); how long, the activity: continuous (*I'[[ve been sending]] emails all morning*)."],
    ["Cik daudz: vienkāršā forma (*I'[[ve sent]] six emails*); cik ilgi, pati darbība: Continuous (*I'[[ve been sending]] emails all morning*)."]),
```

### A4. adv_will

**A4.1 · watch 1 *"If you will / would after if is polite"*** · *must fix*
- Problem: a garbled sentence (*if* … after *if*), and the example *If you'll follow me* is a right option of will-1 row 9. LV has the same mistake.
- Fix: EN *"After *if*, *will / would* can mean *if you are willing* (polite): *If you'[[ll]] just sign here, you can take the keys.*"* LV *"Aiz *if* forma *will / would* var nozīmēt \"ja esat ar mieru\" (pieklājīgi): *If you'[[ll]] just sign here, you can take the keys.*"*

**A4.2 · mistake 3 *Should you will change your mind*** · *must fix*
- Problem: a form nobody writes. The same mistake is on the adv_order card (*Should you will need help*), and will-1 row 9 has the same sentence.
- Rule: IWR 161 *"never a form nobody writes"*.
- Fix: *"In case you [[will need]] a taxi, here's the number."* / *"In case you [[need]] a taxi, here's the number."*

**A4.3 · row 1 *"will (now)"*** · *suggestion*
- Problem: reads as "will = present". Row 4 *"What we expect"* / *"Ko sagaidām"* is vague.

**A4.4 · every example is a task** · *must fix*
- *cat will sit at the window for hours* = will-1 row 2 option; *printer wouldn't work this morning* = row 4; *She'll have heard the news by now* = row 6; *parcel should have arrived by now* = row 8; *Last night he would cook dinner for us* = row 2; *old factory would be next to the river* = row 3; *would have come, but nobody told me* = row 7; *in case you should need it* = row 10; *I'd say that's about right* = row 11.

**New card:**
```python
"adv_will": card(
    [["Typical behaviour", "*will* for what someone or something usually does, *would* for the past; never for one occasion", "*My dad [[will]] tell the same joke at every family dinner.*"],
     ["Refusing", "*won't / wouldn't*, also about machines and things", "*The car [[wouldn't]] start, so I took the bus.*"],
     ["A confident guess", "*will be* + *-ing* (now), *will have* + 3rd form (before now)", "*Look at that queue: they'[[ll have sold]] out by now.*"],
     ["What should have happened by now", "*should have* + 3rd form: we expect it has happened", "*Their plane [[should have landed]] by now. Let's check the app.*"]],
    [["Raksturīga uzvedība", "*will* tam, ko kāds vai kaut kas parasti dara, *would* pagātnē; nekad vienai reizei", (same)],
     ["Atteikšanās", "*won't / wouldn't*, arī par mašīnām un lietām", (same)],
     ["Drošs minējums", "*will be* + *-ing* (tagad), *will have* + 3. forma (līdz šim brīdim)", (same)],
     ["Kam jau vajadzēja notikt", "*should have* + 3. forma: sagaidām, ka tas jau ir noticis", (same)]],
    [["Yesterday she [[would phone]] me at midnight.", "Yesterday she [[phoned]] me at midnight."],
     ["My grandparents [[would live]] in a tiny flat.", "My grandparents [[used to live]] in a tiny flat."],
     ["In case you [[will need]] a taxi, here's the number.", "In case you [[need]] a taxi, here's the number."]],
    (same for LV),
    [{"t": "What did not happen", "s": ["but", "otherwise"], "ex": ["I [[would have called]] you, but my phone was dead."]},
     {"t": "Formal conditions and a small chance", "s": ["should you", "if you should", "in case"], "ex": ["[[Should]] the printer jam again, please call IT.", "Take an umbrella in case it [[should]] rain."]}],
    [{"t": "Kas nenotika", ...}, {"t": "Oficiāls nosacījums un neliela iespēja", ...}],
    ["After *if*, *will / would* can mean *if you are willing* (polite): *If you'[[ll]] just sign here, you can take the keys.*", "*I'd say* makes an opinion softer: *I'[[d say]] she's about forty.*"],
    ["Aiz *if* forma *will / would* var nozīmēt \"ja esat ar mieru\" (pieklājīgi): *If you'[[ll]] just sign here, you can take the keys.*", "*I'd say* padara viedokli maigāku: *I'[[d say]] she's about forty.*"]),
```

### A5. adv_can

**A5.1 · row 3 "Before a passive" / "Pirms ciešamās kārtas"** · *must fix*
- Problem: the heading names the wrong idea (the point is *in* the passive, not before it). The description does not say *not be able to be*, which is the whole point.
- Fix: EN *"In the passive"* · *"*can be* + 3rd form, not *be able to be*"*. LV *"Ciešamajā kārtā"* · *"*can be* + 3. forma, nevis *be able to be*"*.

**A5.2 · use 1 "The only sensible thing, or a reproach"** · *suggestion*
- Problem: two unrelated meanings under one heading. Use 2 LV *"Atzīst vienu, pirms iebilst"* is not natural Latvian.
- Fix: three blocks (in the new block). LV *"Piekrīt vienam, bet iebilst"*.

**A5.3 · every example is a task** · *must fix*
- *were able to park* = can-1 row 3; *kids were allowed to stay up* = row 2 (and = mistake 1 of the same card); *forms can be filled in online* = row 4 (and = mistake 2); *might have been joking* = row 9; *May the figures be wrong?* = row 5; *bus is in an hour, so we might as well walk* = row 6; *might have warned me* = row 7; *flat may be small, but it's bright* = row 11 option; *Winters here can be very long* = row 10.

**New card:**
```python
"adv_can": card(
    [["One success in the past", "*was able to / managed to*, not *could*", "*The shop was closing, but I [[managed to]] grab the last loaf.*"],
     ["Permission on one occasion", "*was / were allowed to*, not *could*", "*On my birthday I [[was allowed to]] leave work at noon.*"],
     ["In the passive", "*can be* + 3rd form, not *be able to be*", "*This sofa [[can be]] turned into a bed.*"],
     ["Possibly happening", "*may / might be* + *-ing* (now or later); *might have been* + *-ing* (the past)", "*Don't wait for me: I [[might be working]] late.*"]],
    [["Viens izdevies mēģinājums pagātnē", "*was able to / managed to*, nevis *could*", (same)],
     ["Atļauja vienā reizē", "*was / were allowed to*, nevis *could*", (same)],
     ["Ciešamajā kārtā", "*can be* + 3. forma, nevis *be able to be*", (same)],
     ["Iespējams, notiek", "*may / might be* + *-ing* (tagad vai vēlāk); *might have been* + *-ing* (pagātnē)", (same)]],
    [["Yesterday I [[could]] get tickets for the final.", "Yesterday I [[was able to]] get tickets for the final."],
     ["This problem [[is able to be]] solved quite easily.", "This problem [[can be]] solved quite easily."],
     ["[[May]] she be at home already?", "[[Could]] she be at home already?"]],
    [["Yesterday I [[could]] get tickets for the final.", "Yesterday I [[was able to]] get tickets for the final.", "Tulkojot burtiski \"vakar es varēju dabūt biļetes\", iznāk *could*; vienai izdevušai reizei angliski saka *was able to*."], (2 and 3 as EN)],
    [{"t": "The only sensible thing", "s": ["might as well", "may as well"], "ex": ["It's raining anyway, so we [[might as well]] stay in and watch a film."]},
     {"t": "Admitting a point, then disagreeing", "s": ["may … but", "might … but"], "ex": ["The car [[may be]] old, but it has never let me down."]},
     {"t": "A reproach: you should have", "s": ["might have", "could have"], "ex": ["You [[might have told]] me the party was fancy dress!"]}],
    [{"t": "Vienīgais saprātīgais", ...}, {"t": "Piekrīt vienam, bet iebilst", ...}, {"t": "Pārmetums: tev vajadzēja", ...}],
    ["*can* for what is sometimes true: *Flying with a baby [[can be]] exhausting.*", "*could* is fine for one occasion with *see, hear* and *hardly*: *I [[could]] hardly hear the speaker.*"],
    ["*can* tam, kas mēdz būt: *Flying with a baby [[can be]] exhausting.*", "Vienai reizei *could* der ar *see, hear* un *hardly*: *I [[could]] hardly hear the speaker.*"]),
```

### A6. adv_subj

**A6.1 · row 2 example *…that it [[not be]] taken with alcohol.*** · *must fix*
- Problem: a fragment that starts with "…" (the teacher's comment a). It is also the answer of subj-1 row 3.
- Fix: *"*The doctor recommended that he [[not drive]] for a week.*"*

**A6.2 · row 4 "Unreal" / "Nereāli"** · *must fix*
- Problem: a one-word heading (LV is an adverb, "unreally"). Use 2 *"Unreal now and unreal then"* repeats row 4.
- Fix: EN *"Unreal situations"* · *"*were* for every person after *if, I wish, as if*"*; LV *"Nereāla situācija"* · *"*were* visām personām aiz *if, I wish, as if*"*. Use 2 becomes *"Preferences about other people: now and in the past"* / *"Ko gribam no cita cilvēka: tagad un pagātnē"*.

**A6.3 · row 1 example with *insist*** · *suggestion*
- Problem: *insist that* + an ordinary verb also means "say firmly that it is true", which makes the rule less clear (the same problem is task C26).
- Fix: in the new block (a witty line, also the new tile).

**A6.4 · LV note on mistake 2 *"gribas would"*** · *suggestion*
- Problem: colloquial.
- Fix: *"Tulkojot burtiski \"ja veikals slēgtos\", iznāk *would*; aiz *if* to nelieto."*

**A6.5 · mistake 1 marks *the director to resign* as a whole** · *suggestion*
- Fix: mark only the changed words (new block).

**A6.6 · every example is a task** · *must fix*
- *insist that he be told* = subj-1 rows 2 and 10; *not be taken with alcohol* = row 3; *odd that she should say that* = row 4; *If I were you, I'd take it* = row 6 option; *demanded the director to resign* = row 2; *If the bank would refuse, we'd sell the car* = row 6; *wouldn't have sold the car* = row 11; *recommended that she rest* = row 2 option; *every guest have a ticket* = row 9; *I wish it were Friday* = row 6 option; *I'd rather you had told me* = row 7; *be that as it may, come what may* = rows 8, 12.

**New card:**
```python
"adv_subj": card(
    [["After *demand, insist, recommend*", "*that* + the base form for every person (no *-s*)", "*My cat insists that {{breakfast}} [[be]] served at five.*"],
     ["The negative", "*not* + base form", "*The doctor recommended that {{he}} [[not drive]] for a week.*"],
     ["Surprise", "*It's odd / strange that* + *should* + base form", "*It's strange that he [[should]] be so calm before an exam.*"],
     ["Unreal situations", "*were* for every person after *if, I wish, as if*", "*I wish {{my flat}} [[were]] closer to work.*"]],
    [["Aiz *demand, insist, recommend*", "*that* + pamatforma visām personām (bez *-s*)", (same)],
     ["Noliegums", "*not* + pamatforma", (same)],
     ["Pārsteigums", "*It's odd / strange that* + *should* + pamatforma", (same)],
     ["Nereāla situācija", "*were* visām personām aiz *if, I wish, as if*", (same)]],
    [["The landlord demanded [[us to pay]] in cash.", "The landlord demanded [[that we pay]] in cash."],
     ["If the shop [[would close]], we'd have nowhere to buy bread.", "If the shop [[closed]], we'd have nowhere to buy bread."],
     ["I'd rather you [[wouldn't have told]] my mum.", "I'd rather you [[hadn't told]] my mum."]],
    [(1 as EN), ["If the shop [[would close]], we'd have nowhere to buy bread.", "If the shop [[closed]], we'd have nowhere to buy bread.", "Tulkojot burtiski \"ja veikals slēgtos\", iznāk *would*; aiz *if* to nelieto."], (3 as EN)],
    [{"t": "Formal demands, rules and advice", "s": ["require", "it is vital that", "recommend"], "ex": ["It's vital that nobody [[touch]] the red button.", "The bank requires that every customer [[show]] ID."]},
     {"t": "Preferences about other people: now and in the past", "s": ["I'd rather", "I'd sooner"], "ex": ["I'd rather you [[didn't]] call me before nine.", "I'd rather you [[had asked]] me first."]}],
    [{"t": "Oficiālas prasības, noteikumi un ieteikumi", ...}, {"t": "Ko gribam no cita cilvēka: tagad un pagātnē", ...}],
    ["Fixed phrases keep the old form: *If you want to leave, [[so be it]].* Also *[[be that as it may]]* (= even so), *[[come what may]]* (= whatever happens)."],
    ["Nemainīgi izteicieni saglabā seno formu: *If you want to leave, [[so be it]].* Arī *[[be that as it may]]* (= tomēr), *[[come what may]]* (= lai kas notiktu)."]),
```

### A7. adv_agree

**A7.1 · table descriptions are fragments** · *must fix*
- Problem: *"not the words around it"*, *"singular / plural"*, *"singular verb"*, *"the nearer noun decides"*. A learner cannot read the rule from them (the teacher's comment c). LV *"nevis vārdi ap to"*, *"vienskaitlis / daudzskaitlis"* are the same.
- Fix: in the new block.

**A7.2 · the noun that decides is not marked** · *must fix*
- Problem: on this card it matters most (A0.1).

**A7.3 · LV watch *"Palīgteikums kā teikuma priekšmets"* for *Being late for every meeting*** · *must fix*
- Problem: *palīgteikums* is a clause with its own finite verb, so the term is wrong for an *-ing* phrase. The same error is in task agree-1 row 10 LV (*"-ing palīgteikums"*).
- Rule: IWR 12, LVT.
- Fix: *"Ja teikuma priekšmets ir darbības vārds ar *-ing* vai vesels palīgteikums, darbības vārds ir vienskaitlī: …"*

**A7.4 · LV use 2 *"Grupa kā viens vai kā cilvēki"*** · *suggestion*
- Fix: *"Grupa kā viena vienība vai kā atsevišķi cilvēki"*.

**A7.5 · every example is a task** · *must fix*
- *manager, with two assistants, is coming* = agree-1 row 4; *number of applicants has fallen* = row 2 (and = mistake 2); *Each of the rooms has … bathroom* = row 8 (and = mistake 1); *Either … or his parents are coming* = row 9; *criteria has changed* = row 6; *Politics has never interested me* = row 5; *Ten kilometres is a long way* = row 7; *jury are still arguing among themselves* = row 11; *Being late for every meeting* = row 10.

**New card:**
```python
"adv_agree": card(
    [["The main noun decides", "a phrase with *with, together with, as well as* does not change the verb", "*{{The boss}}, together with her two dogs, [[is]] joining the meeting.*"],
     ["the number of / a number of", "*the number of* (one number) + singular verb; *a number of* (= several) + plural verb", "*{{The number}} of people working from home [[has]] doubled.* · *{{A number of}} my colleagues [[have]] bought a dog.*"],
     ["each of / neither of", "singular verb in careful English", "*{{Each}} of my plants [[needs]] a different amount of water.*"],
     ["either … or", "the noun nearer the verb decides", "*Either my sister or {{my parents}} [[are]] picking me up.*"]],
    [["Izšķir galvenais lietvārds", "frāze ar *with, together with, as well as* darbības vārdu nemaina", (same)],
     ["the number of / a number of", "*the number of* (viens skaitlis) + darbības vārds vienskaitlī; *a number of* (= vairāki) + daudzskaitlis", (same)],
     ["each of / neither of", "rūpīgā valodā darbības vārds vienskaitlī", (same)],
     ["either … or", "izšķir lietvārds, kas ir tuvāk darbības vārdam", (same)]],
    [["The quality of the photos [[are]] amazing.", "{{The quality}} of the photos [[is]] amazing."],
     ["The news [[are]] on at nine.", "{{The news}} [[is]] on at nine."],
     ["The police [[is]] looking for the driver.", "{{The police}} [[are]] looking for the driver."]],
    (same for LV),
    [{"t": "Singular though it looks plural", "s": ["economics", "twenty euros", "ten kilometres"], "ex": ["{{Economics}} [[was]] my worst subject.", "{{Twenty euros}} [[is]] a lot for a sandwich."]},
     {"t": "A group as one unit or as separate people", "s": ["the team", "my family", "the staff"], "ex": ["{{My family}} [[are]] all coming for dinner, so we need more chairs."]}],
    [{"t": "Vienskaitlis, lai gan izskatās pēc daudzskaitļa", ...}, {"t": "Grupa kā viena vienība vai kā atsevišķi cilvēki", ...}],
    ["An *-ing* phrase or a whole clause as the subject takes a singular verb: *{{Answering emails at midnight}} [[is]] a bad habit.*"],
    ["Ja teikuma priekšmets ir darbības vārds ar *-ing* vai vesels palīgteikums, darbības vārds ir vienskaitlī: *{{Answering emails at midnight}} [[is]] a bad habit.*"]),
```

### A8. adv_prep

**A8.1 · mistake 2 *Despite that it rained, we went.*** · *must fix*
- Problem: sounds unfinished (the teacher's comment a), and it is task prep-1 row 8.
- Fix: *"We enjoyed the trip despite [[that]] it rained every day."* / *"We enjoyed the trip despite [[the fact that]] it rained every day."*

**A8.2 · examples that are fragments, not sentences** · *must fix*
- *the person to whom it was addressed*, *the colleague I share an office with*, *the extent to which prices rose*, *Nobody to talk to.*, mistake 1 *The colleague with who I share an office.* (a full stop after a noun phrase).
- Rule: the teacher's comment a; IWR 98 *"Every sentence makes sense"*.

**A8.3 · row 4 "Stays in place" / "Paliek savā vietā"** · *must fix*
- Problem: it does not say what stays where.
- Fix: EN *"The preposition stays with its verb"* · *"also in a passive and after *to* + verb"*; LV *"Prievārds paliek pie sava darbības vārda"* · *"arī ciešamajā kārtā un aiz *to* + darbības vārds"*.

**A8.4 · use 2 example *The road was closed with a view to repairing the bridge.*** · *must fix*
- Problem: not natural (*with a view to* is a person's intention; reader 2 in c1-6 said the same), and it is task prep-1 row 7.
- Fix: *"He's learning Spanish [[with a view to]] moving to Valencia."*

**A8.5 · watch repeats use 2 (*with a view to repairing*)** · *suggestion*
- Rule: the brief: *"every Watch out says something the card does not already say"*.
- Fix: *"In questions, the preposition usually goes to the end: *Who did you go [[with]]?* (formal: *[[With whom]] did you go?*)"* / LV *"Jautājumos prievārds parasti ir beigās: *Who did you go [[with]]?* (oficiāli: *[[With whom]] did you go?*)"*

**A8.6 · *prevent … from* (task prep-1 row 9) is not on the v2 card** · *suggestion*
- Fix: an example in use 1 (new block).

**A8.7 · every example is a task** · *must fix*
- *with who/whom I share an office* = prep-1 row 2; *person to whom … addressed* = row 2 option; *extent to which* = row 3; *being looked into* = row 5; *nobody to talk to* = row 6; *Despite that it rained* = row 8; *depends on whether she signs* = row 8 option; *talent for explaining* = row 11; *with a view to repairing the bridge* = row 7; *Nobody other than the owner has a key* = row 10.

**New card:**
```python
"adv_prep": card(
    [["Formal: preposition first", "preposition + *whom / which*; never before *who* or *that*", "*This is the drawer [[in which]] I keep my good intentions.*"],
     ["Everyday: preposition last", "*who / that* or nothing, and the preposition at the end", "*That's the friend I went to Rome [[with]].*"],
     ["Fixed formal phrases", "*the extent to which, the way in which, none of which*", "*He sent three CVs, [[none of which]] had his phone number on it.*"],
     ["The preposition stays with its verb", "also in a passive and after *to* + verb", "*This bed has never been [[slept in]].* · *I need something to write [[with]].*"]],
    [["Oficiāli: prievārds pirmais", "prievārds + *whom / which*; nekad pirms *who* vai *that*", (same)],
     ["Ikdienā: prievārds beigās", "*who / that* vai nekas, un prievārds teikuma beigās", (same)],
     ["Nemainīgi oficiāli izteicieni", "*the extent to which, the way in which, none of which*", (same)],
     ["Prievārds paliek pie sava darbības vārda", "arī ciešamajā kārtā un aiz *to* + darbības vārds", (same)]],
    [["The hotel [[at that]] we stayed was lovely.", "The hotel [[at which]] we stayed was lovely."],
     ["We enjoyed the trip despite [[that]] it rained every day.", "We enjoyed the trip despite [[the fact that]] it rained every day."],
     ["The tickets have already been [[paid]].", "The tickets have already been [[paid for]]."]],
    (same for LV),
    [{"t": "After a preposition: *-ing*, a *wh*-clause or *the fact that*", "s": ["depends on", "worried about", "stop someone from"], "ex": ["It all [[depends on how]] much it costs.", "Nothing will stop me [[from finishing]] this cake."]},
     {"t": "Formal prepositions of several words", "s": ["with a view to", "in the event of", "regardless of"], "ex": ["He's learning Spanish [[with a view to]] moving to Valencia.", "[[In the event of]] fire, use the stairs."]}],
    [{"t": "Aiz prievārda: *-ing*, *wh*-palīgteikums vai *the fact that*", ...}, {"t": "Oficiāli vairākvārdu prievārdi", ...}],
    ["In questions, the preposition usually goes to the end: *Who did you go [[with]]?* (formal: *[[With whom]] did you go?*)"],
    ["Jautājumos prievārds parasti ir beigās: *Who did you go [[with]]?* (oficiāli: *[[With whom]] did you go?*)"]),
```

### A9. adv_part

**A9.1 · mistake 1 *[[Walking into the office]], the lights were off.* / *[[Walking into the office]], I saw the lights were off.*** · *must fix*
- Problem: the part that did not change is marked, and the change (*I saw*) is not.
- Fix: in the new block (*Looking out of the window, [[the rain started]]* / *…, [[I saw that it had started to rain]]*).

**A9.2 · LV note on mistake 1 starts *"Latviski…"*, and *"angliski gaismas nevar ienākt"* is awkward** · *must fix*
- Rule: HO 61 (*starting Tulkojot burtiski…*).
- Fix: *"Tulkojot burtiski \"skatoties pa logu, sāka līt\", iznāk, ka pa logu skatījās lietus; angliski abām daļām vajag vienu teikuma priekšmetu: *I saw*."*

**A9.3 · LV *"priekšmets"* alone** · *must fix*
- Where: row 1 heading *"Tas pats priekšmets"* and description *"…ir viens priekšmets"*, row 4 *"Savs priekšmets"*, watch *"kopīgs priekšmets"*.
- Rule: LVT 13 *"priekšmets (alone) → teikuma priekšmets in sentences, teik. priekšmets in formulas"*.
- Fix: in the new block.

**A9.4 · row 2 "Earlier or cause" / *"having + past participle; not first"*** · *must fix*
- Problem: *"not first"* reads as "not at the start". The example *Having finished, she went home.* is incomplete: finished what? (BE / IWR 74 *"the sentence must make sense on its own"*).

**A9.5 · row 4 example *With prices going up, families struggle.*** · *must fix*
- Problem: unnatural (the present simple; *are struggling* is meant), and it is part-1 row 6.

**A9.6 · *on / in / by / without* + *-ing* is missing on the v2 card** · *must fix*
- Problem: the judge (c1-7) promised a card line for task part-1 row 9 (*On / In / By / Without hearing*), but it is only in the hidden old `CARDS` text.
- Rule: IWR 71, IWR 168 (options only from the card).
- Fix: a third use block (new block).

**A9.7 · mistake 2 *Knowing not anyone*** · *suggestion*
- Problem: not a mistake learners really make (IWR 161).
- Fix: *"[[Being]] lost my keys, I had to call a locksmith."* / *"[[Having]] lost my keys, …"*

**A9.8 · every example is a task** · *must fix*
- *Opening the door, she saw the cat* = part-1 row 2 option; *Having finished, she went home* = row 3; *Stored in a dry place, seeds keep for years* = row 5; *With prices going up* = row 6; *Walking into the office, the lights* = row 2; *On hearing the news* = row 9; *burst its banks, flooding the streets* = row 8; *Keep refrigerated once opened* = row 10; *Judging by the queue, the café is popular* = row 11.

**New card:**
```python
"adv_part": card(
    [["One subject for both parts", "the *-ing* part tells us about the subject of the main clause", "*[[Trying]] to look relaxed, {{I}} spilled coffee on my interviewer.*"],
     ["An earlier action or a reason", "*having* + 3rd form; in the negative, *not* comes first", "*[[Having missed]] the last bus, we walked home in the rain.* · *[[Not having]] a key, I waited in the car.*"],
     ["A passive meaning", "3rd form (= which is / was …)", "*[[Left]] in the sun, {{chocolate}} melts in minutes.*"],
     ["Its own subject", "*with* + noun + *-ing*; *there being* + noun", "*[[With the kids watching]] cartoons, we finally had a quiet coffee.*"]],
    [["Viens teikuma priekšmets abām daļām", "daļa ar *-ing* ir par galvenā teikuma priekšmetu", (same)],
     ["Agrāka darbība vai iemesls", "*having* + 3. forma; noliegumā *not* stāv pirmais", (same)],
     ["Ciešamās kārtas nozīme", "3. forma (= kas ir / bija …)", (same)],
     ["Savs teikuma priekšmets", "*with* + lietvārds + *-ing*; *there being* + lietvārds", (same)]],
    [["Looking out of the window, [[the rain started]].", "Looking out of the window, [[I saw that it had started to rain]]."],
     ["[[Being]] lost my keys, I had to call a locksmith.", "[[Having]] lost my keys, I had to call a locksmith."],
     ["[[At]] arriving at the hotel, we were given a welcome drink.", "[[On]] arriving at the hotel, we were given a welcome drink."]],
    [["Looking out of the window, [[the rain started]].", "Looking out of the window, [[I saw that it had started to rain]].", "Tulkojot burtiski \"skatoties pa logu, sāka līt\", iznāk, ka pa logu skatījās lietus; angliski abām daļām vajag vienu teikuma priekšmetu: *I saw*."], (2 and 3 as EN)],
    [{"t": "The result of the main clause", "s": ["sending", "causing", "leaving"], "ex": ["The train stopped suddenly, [[sending]] my coffee across the carriage."]},
     {"t": "Short forms after a conjunction", "s": ["if in doubt", "when asked", "once opened"], "ex": ["[[If in doubt]], ask the pharmacist.", "[[When asked]] about the price, he changed the subject."]},
     {"t": "*on, by, without* + *-ing*", "s": ["on (= when)", "by (= how)", "without (= not doing)"], "ex": ["[[On seeing]] the bill, he suddenly needed the toilet.", "You can save a lot [[by cooking]] at home."]}],
    [{"t": "Galvenā teikuma rezultāts", ...}, {"t": "Īsās formas aiz saikļa", ...}, {"t": "*on, by, without* + *-ing*", "s": ["on (= kad)", "by (= kā)", "without (= nedarot)"], ...}],
    ["Comment phrases need no shared subject: *[[Judging by]] his face, the meeting went badly.*"],
    ["Komentāra izteicieniem kopīgs teikuma priekšmets nav vajadzīgs: *[[Judging by]] his face, the meeting went badly.*"]),
```

### A10. adv_order

**A10.1 · row 4 example *Had I known, I'd have left earlier.*** · *must fix*
- Problem: known what? This exact problem is recorded as an old mistake.
- Rule: IWR 74 *"An inverted-conditional … task with a missing object (*Had I known* what?) | the sentence must make sense on its own"*.

**A10.2 · row 3 "So / Such" teaches only *So*** · *must fix*
- Problem: task order-1 row 11 (*Such ___ the noise…*) tests *Such* + *be*, which neither the v2 card nor the old `CARDS` text teaches.
- Rule: IWR 71.

**A10.3 · LV *"priekšmets"* alone** · *must fix*
- Where: row 1 *"palīgdarbības vārds + priekšmets"*, row 3 *"… + *be* + priekšmets"*.
- Rule: LVT 13. Fix: *"teik. priekšmets"* (new block).

**A10.4 · LV note on mistake 1 starts *"Latviski…"*** · *must fix*
- Rule: HO 61.
- Fix: in the new block (moved to the *Only then* mistake, where Latvian word order really causes it).

**A10.5 · mistake 3 *Should you will need help*** · *must fix*
- Problem: a form nobody writes (IWR 161), and the same as adv_will mistake 3.

**A10.6 · row 1 "Negative start"** · *suggestion*
- Problem: *Rarely* is not negative. Row 2 uses *"inversion"*, which the card never explains. Use 2 *"Admitting something formally"* / *"Oficiāli atzīst"* is vague.

**A10.7 · every example is a task** · *must fix*
- *Rarely have I seen such a sunset* = order-1 row 2; *Not until they left did we notice the stain* = row 4; *So loud was the music* = row 5; *Had I known, I'd have left earlier* = row 6; *Never I have felt so tired* = row 3; *What I need is a long holiday* = row 9; *Cold though it was, we went for a swim* = row 10; *Here comes the bus!* = row 8.

**New card:**
```python
"adv_order": card(
    [["*Never, Rarely, Seldom, Hardly* first", "a negative or limiting word at the start: helping verb + subject", "*[[Seldom have]] {{I}} seen my dog look so guilty.*"],
     ["*Not until, Only when, Only after*", "in the second part, the helping verb comes before the subject", "*Only after the guests had left [[did]] {{I}} find the cake I'd hidden.*"],
     ["*So* + adjective, *Such* + *be*", "*So* + adjective + *be* + subject; *Such* + *be* + subject (= so great)", "*[[So strong was]] {{the coffee}} that I could hear colours.* · *[[Such was]] {{the queue}} that we gave up.*"],
     ["A condition without *if*", "*Had / Should / Were* + subject come first", "*[[Had]] {{I}} known it was fancy dress, I'd have come as a pirate.*"]],
    [["*Never, Rarely, Seldom, Hardly* sākumā", "nolieguma vai ierobežojuma vārds teikuma sākumā: palīgdarbības vārds + teik. priekšmets", (same)],
     ["*Not until, Only when, Only after*", "otrajā daļā palīgdarbības vārds stāv pirms teikuma priekšmeta", (same)],
     ["*So* + īpašības vārds, *Such* + *be*", "*So* + īpašības vārds + *be* + teik. priekšmets; *Such* + *be* + teik. priekšmets (= tik liels)", (same)],
     ["Nosacījums bez *if*", "*Had / Should / Were* + teik. priekšmets teikuma sākumā", (same)]],
    [["[[Little she knew]] what was waiting at home.", "[[Little did she know]] what was waiting at home."],
     ["Only then [[I understood]] the joke.", "Only then [[did I understand]] the joke."],
     ["[[Was I]] you, I'd ask for a refund.", "[[Were I]] you, I'd ask for a refund."]],
    [(1 as EN), ["Only then [[I understood]] the joke.", "Only then [[did I understand]] the joke.", "Tulkojot burtiski \"tikai tad es sapratu\", paliek parastā secība; angliski pēc *Only then* nāk *did I understand*."], (3 as EN)],
    [{"t": "Focus on one part", "s": ["what … is", "all … is", "it was … who"], "ex": ["[[What I love about Mondays is]] that they end.", "[[It was]] my brother [[who]] ate the last biscuit."]},
     {"t": "*although*, said more strongly", "s": ["adjective + as", "adjective + though"], "ex": ["[[Tired as I was]], I finished the report."]}],
    [{"t": "Izceļ vienu daļu", ...}, {"t": "*although* stiprāk: īpašības vārds + *as / though*", ...}],
    ["After *Here / There* + a noun, the verb comes first: *There [[goes]] my weekend!* (but *There it [[goes]]!*)"],
    ["Pēc *Here / There* ar lietvārdu darbības vārds stāv pirmais: *There [[goes]] my weekend!* (bet *There it [[goes]]!*)"]),
```

### A11. Old-layout entries in `b1_topics.py` (CARDS / LV_CARDS, ten C1 topics)

**A11.1 · the old texts are no longer shown on the card, but they differ from it** · *suggestion*
- Problem: since `cards2_c1.py`, the v2 card replaces them. They are still used for italics marking (`italics_en.py` 686) and as the source of `example`. Several points the tasks test are only there (A1.8, A3.3, A9.6), and `LV_CARDS["adv_part"]` uses the banned term *"Divdabja teicienam"* (LVT: *divdabis* → *3. forma*).
- Fix: after the cards are rewritten, align the old `form` / `use` lines with the new card (or mark them in a comment as not shown), and change *"Divdabja teicienam"* to *"Daļai ar *-ing* vai 3. formu"*.


## B. Tile lines (`TILE_LINES`, `app/assets/app.js` 2105)

**B1 · adv_agree *"The number of unread emails **has** reached 2,000. None of them **is** urgent."*** · *must fix*
- Problem: *none of* is not on the card. *None of them are urgent* is just as correct (Hewings unit 40, Murphy), so marking **is** as "the rule" teaches something false.
- Fix: *"The number of unread emails **has** reached 2,000. Each of them **says** 'urgent'."* (also in `b1_topics.py` `CARDS["adv_agree"]["example"]`).

**B2 · adv_subj *"If I **were** a cat, I'd ignore emails too."*** · *suggestion*
- Problem: a B1 second conditional. It does not show the C1 point of the topic (the base form after *insist / demand*).
- Fix: *"My cat **insists** that breakfast **be** served at five."*

**B3 · adv_past *"I **was** quietly **eating** your biscuits when you **walked** in."*** · *suggestion*
- Problem: the B1 interrupted past continuous, not a C1 point of the card.
- Fix: *"I **had planned** a healthy dinner. Then I **walked** past the bakery."* (plans that came to nothing).

**B4 · adv_perfect *"This is the third time I**'ve lost** my glasses today. They're on my head."*** · *suggestion*
- Problem: witty, but the same frame as task perf-1 row 8 (*This is the third time she ___ her keys this week!*).
- Fix: *"It's only Tuesday, and I**'ve** already **spent** my weekly budget."*

The other six lines (adv_present, adv_will, adv_can, adv_prep, adv_part, adv_order) are witty, show the rule of their topic and mark the form: no finding.


## C. Tasks (`docs/task-drafts/c1-*.csv`, generators `_src/c1_*.py`)

Rows are CSV line numbers (header = line 1).

### C0. Points that affect many tasks

**C1 · LV explanations: Latvian words marked as English (shown in italics as English examples)** · *must fix*
- Problem: no C1 file has an `LV_BY_FILE` entry in `_src/lib.py`, so `lv_mark` marks Latvian words without Latvian letters as English. Some cases even run across the English: agree-1 row 4 *"*the manager; izteiciens*"*, pres-2 row 3 *"*So this* man *walks into a caf*é"*, will-1 row 11 *"*I'd say padara viedokli*"*.
- Where: agree-1 rows 2, 4, 7, 8, 9; can-1 3, 7; order-1 4, 9, 10, 11, 12; part-1 2, 4, 7, 8, 11; past-1 2, 3, 6, 9; perf-1 2, 5, 7, 10, 13, 14; prep-1 3, 4, 6, 7, 8; pres-1 2, 3, 4, 5, 6, 9; pres-2 2, 3, 5, 6, 8, 9; subj-1 2, 4, 5, 8, 12; will-1 2, 4, 6, 8, 9, 10, 11.
- Rule: HO 163 *"Latvian words that the italics marking takes for English … go into LV_BY_FILE"*; IWR 64.
- Fix: add to `_src/lib.py`:
  ```python
  _C1_LV = set("""prasa skaitlis lieta Galvenais izteiciens nemaina uztver vienskaitli saskan izdevies tev inversija lietu auksti troksnis liels
  Divdabja teicienam pats galvenajam teikumam Gaismas iemeslam divdabja iemeslu teiciens pabeigti otram abiem saskaita beigusies balss nogale
  desmit Abas tu te noticis pareizi skaits perfekts nenoteiksmes tikai ierasta nepatiku svara galvenie nodotu apgalvojuma gaida ieteikt objektu
  izsaka ticamai seno notiktu reizi atteikumam lietai esat mieru nelielai padara viedokli otrs""".split())
  for _n in ("c1-agree-1.csv", "c1-can-1.csv", "c1-order-1.csv", "c1-part-1.csv", "c1-past-1.csv", "c1-perf-1.csv",
             "c1-prep-1.csv", "c1-pres-1.csv", "c1-pres-2.csv", "c1-subj-1.csv", "c1-will-1.csv"):
      LV_BY_FILE[_n] = _C1_LV
  ```
  Then regenerate and check that the CSVs change only in column 8. Explanations are not part of the blind hash: check with `blind_check.py export X --keys unchecked`.

**C2 · alternative answers accepted without their own note** · *must fix*
- Problem: the `answer notes` column is empty in all 11 C1 files, so a learner who types the other form sees *Correct* with the explanation of the main form.
- Where (each needs `answer :: EN :: LV`):
  - pres-1 row 2 *am going to measure*
  - row 4 *has been considering / may be considering*
  - row 5 *You constantly change your mind* (the explanation teaches only the continuous)
  - pres-2 row 7 *didn't appear*
  - past-1 row 6 *had shouted*
  - row 10 *hasn't changed* (the explanation says past perfect, *"not didn't change"*)
  - row 11 *had waited*
  - perf-1 row 5 *have been living*
  - row 6 *get*
  - row 12 *will have been teaching*
  - subj-1 row 3 *is not / isn't*
  - row 9 *has*
  - row 12 *might*
  - will-1 row 4 *won't*
  - row 7 *could have come*
  - part-1 row 5 *If / When stored*
  - row 10 *open*
  - row 11 *Judged*
  - prep-1 row 4 *upon*
  - row 6 *with*
  - row 11 *at*
- Rule: HO 55 *"accept it and give it its own note … Never show *Correct* with the explanation of another form"*; IWR 116.
- Example: past-1 row 10: `hasn't changed :: Also possible: the school is still the same now, so the present perfect is fine; the past perfect is the form after *found* (the moment in the past). :: Arī pareizi: skola joprojām ir tāda pati, tāpēc der Present Perfect; aiz *found* (pagātnes brīdis) parasti lieto Past Perfect.`
- Example: part-1 row 11: `Judged :: Also possible, but *Judging by* is the usual fixed phrase. :: Arī pareizi, bet parastais izteiciens ir *Judging by*.`

**C3 · a word that never changes given in brackets** · *must fix*
- Problem: the bracket gives the answer. The judge (c1-5, 012) kept *"(should / say)"* because "the cue asks for should".
- Where: can-1 rows 7 *(might / warn)*, 8 *(may / lie)*, 9 *(might / joke)*; subj-1 row 4 *(should / say)*; will-1 rows 4 *(not / will)*, 5 *(will / have)*, 6 *(will / hear)*, 8 *(should / arrive)*, 12 *(will / be)*.
- Rule: IWR 156 *"A word that never changes (*will, can, must, shall*…) is never given in brackets: it is the answer. Make it a word bank"*.
- Fix (word banks, wrong chips that build real forms or common learner mistakes; checked that no other combination is correct):
  - can-1 row 7: *"You might ___ ___ me you were bringing five friends! I would have made more food."* bank `have · warned · warn · had` → *have warned*.
  - can-1 row 8: *"This time next week I ___ ___ ___ on a beach in Crete."* bank `may · be · lying · lie · have` → *may be lying*.
  - can-1 row 9: *"He didn't sound serious about leaving. He ___ ___ ___ ___."* bank `might · have · been · joking · joked · be` → *might have been joking*.
  - subj-1 row 4: *"It's odd that she ___ ___ ___ that. She's usually so polite."* bank `should · have · said · say · has` → *should have said* (no *would*: *It's odd that she would say that* is correct).
  - will-1 row 4: *"Choose the correct option: I tried three times, but the printer ___ work this morning."* ok *wouldn't*; wrong *wasn't | hasn't | isn't* (no *didn't*: correct English).
  - will-1 row 5: *"Don't ring them now: they ___ ___ ___ lunch."* bank `will · be · having · have · been` → *will be having*.
  - will-1 row 6: *"It's nine o'clock. She ___ ___ ___ the news by now."* bank `will · have · heard · has · hear` → *will have heard*.
  - will-1 row 8: *"I sent it on Monday, so the parcel ___ ___ ___ by now."* bank `should · have · arrived · has · arrive` → *should have arrived*.
  - will-1 row 12: *"The doorbell's ringing. That ___ ___ the courier: I'm expecting a parcel."* bank `will · be · is · being` → *will be* (this also replaces the unnatural *"There's the doorbell"*).

**C4 · the question mix: almost no drag-and-drop** · *must fix*
- Problem: 114 C1 tasks hold one word order (pres-1 row 8), no word bank and no matching. Every file is gaps and choices.
- Rule: IWR 11 *"Question mix per 10: 3 choose, 4 drag-and-drop (order, word bank, matching), 2 type a word or words, 1 type the whole sentence. Write new batches with at least 40% drag-and-drop."*
- Fix: the nine banks in C3 bring the share to about 9%. Further natural candidates for word order: order-1 rows 2, 4, 12 (inversion is word order: *Put the words in order.* with *rarely / have / I / seen / such / a / beautiful / sunset*); part-1 row 3; prep-1 rows 2, 6. A learning drag task (practice only) next to each choice (IWR *Learning drag tasks*) does not count as evidence and does not solve the mix of check tasks.

**C5 · level: tasks both readers marked B1 / B2, kept by the judge with one general line** · *suggestion* (see D4)
- Where: perf-1 rows 3, 4, 8, 9 (*this morning*, *since she joined*, *the third time*, *the first time I am seeing*: Murphy B1 units); past-1 rows 4, 5, 7 (plain past perfect); can-1 rows 3, 4; will-1 rows 5, 6; all of agree-1 (both c1-6 readers: "B2 at most").
- Rule: IWR 169 *"A form mistake that a B1 learner spots at once … is not a C1 task"*; IWR 59 / HO 59.
- Fix: keep the Hewings units, but give the C1 layer the Hewings exercises use (a context where the B1 form would also look possible). For example, perf-1 row 9: *"Which sentence has a mistake?"* with the wrong *"It was the first time I have flown business class."* (past frame + present perfect), not *"This is the first time I am seeing snow."*

### C6. Single tasks

**C6.1 · pres-1 row 7, option *At eight I'm usually driving to work.*** · *must fix*
- Problem: the answer of the task in the row before it (row 6, *I ___ usually ___ to work then*) in the same setting.
- Rule: IWR 27 *"Not the same setting in two tasks in a row"*; IWR 161 (no near-copy).
- Fix: *"I'm seeing the dentist on Friday."*

**C6.2 · pres-1 row 9, the explanation does not match the task** · *must fix*
- Problem: EN and LV say *"This suitcase weighs 23 kilos"*, but the task says *nearly five kilos*.
- Rule: the brief *"The feedback must fit the task"*.
- Fix: EN *"*weigh* for how heavy something is is a state: *This old suitcase weighs nearly five kilos.* *The vet is weighing the dog* is the action, so the continuous is right there."* LV *"*weigh* nozīmē \"sver\" (cik smags) ir stāvoklis: *This old suitcase weighs nearly five kilos.* *The vet is weighing the dog* ir darbība, tāpēc tur Continuous forma ir pareiza."*

**C6.3 · pres-1 row 5, double quotation marks** · *suggestion*
- Problem: the house style for quotes is single (*'…'*).
- Fix: *"Your friend changes the order for the third time: 'Actually, I'll have the fish, not the pasta.' Complain, using *constantly* and *change your mind*."*

**C6.4 · pres-2 row 3, the LV explanation is broken** · *must fix*
- Problem: *"*So this* man *walks into a caf*é *and orders*…"*.
- Fix (after C1): *"Jokā vai stāstā tagadnē galvenie notikumi ir Present Simple: *So this man walks into a café and orders…* Fons var būt Continuous formā (*I'm sitting on the train*)."* Also *suggestion*: *is walking into a café* can be read as background (Hewings 1 allows the continuous for the scene). The mistake would be clearer with *"So this man is walking into a café, he is ordering a glass of milk, and the waiter is saying…"* or a different event verb (*is sitting down*).

**C6.5 · pres-2 row 6** · *must fix*
- Problem: two right options are near-copies of the wrong one (*I was wondering if you were free…*, *I wonder whether you'd mind…* next to *I'm wondering could you look…*). The mistake is word order in an indirect question (the B1 indirect-question point), and *I'm wondering* is not on the card (A1.8).
- Rule: IWR 161; IWR 71.
- Fix: right options *"We're hoping to move in by the end of May."* · *"I'm thinking of joining a gym."* · *"She's always asking me for advice."* (and the card line in A1).

**C6.6 · past-1 row 5 *We ___ each other for years before we started working together. (know)*** · *must fix*
- Problem: *knew* is also correct (with *before*, the order is clear: Murphy unit 15). The key refuses it. The frame is the one BE c-2206 forbids repeating (*know each other*).
- Fix: *"By the time Sam and I started working together, we ___ each other for ten years. (know)"* → *had known | 'd known* (*by the time* + a period up to that past moment excludes *knew*).

**C6.7 · past-1 row 12 *I wish you ___ me about the party. I would have come.*** · *must fix*
- Problem: the same scene as will-1 row 7 (*I ___ to your party, but nobody told me about it*), and the second *I wish* + *had* task in this topic (row 8).
- Rule: IWR 100 *"Different topics or levels do not reuse the same scene"*.
- Fix: *"We drove all the way there for nothing. I wish you ___ me the restaurant was closed on Mondays. (tell)"* → *had told | 'd told*.

**C6.8 · perf-1 row 11, option *I've been ringing the bank all morning.*** · *must fix*
- Problem: the scene and answer of the task just before it (row 10).
- Rule: IWR 27, 161.
- Fix: *"We've been waiting for the plumber since nine."*

**C6.9 · perf-1 row 10 *"Nobody answers."*** · *suggestion*
- Fix: *"Nobody's answering."* (more natural).

**C6.10 · can-1 row 2, option *We could stay up late on Saturdays when we were kids.*** · *must fix*
- Problem: a near-copy of the wrong sentence (*the children could stay up until eleven*), so the pair gives the answer.
- Rule: IWR 161.
- Fix: *"I could hear the neighbours arguing all night."*

**C6.11 · can-1 row 5, option *Could the figures be wrong?*** · *must fix*
- Problem: the corrected form of the wrong sentence (*May the figures in the report be wrong?*).
- Rule: IWR 161.
- Fix: *"The trains might be late because of the snow."*

**C6.12 · can-1 row 6, wrong options *might as good | might so well | might well as*** · *must fix*
- Problem: strings nobody writes (readers c1-5 and c1-7: "B1/B2").
- Rule: IWR 161, 162.
- Fix: *"Which sentence has a mistake?"* · wrong *"There's nothing on TV, so we might as good go to bed."* · right *"It may well rain later, so take a coat."* · *"You might have told me the café was closed."* · *"There's no milk, so I'll have my tea black."*. EN *"*might / may as well* (not *as good*) = it is the only sensible thing: *we might as well go to bed*."* LV *"*might / may as well* (nevis *as good*) = tas ir vienīgais saprātīgais: *we might as well go to bed*."*

**C6.13 · can-1 row 10 *Winters here ___ very long* (wrong *can being*)** · *must fix*
- Problem: *can being* is a form nobody writes, and the sentence is the card's watch line (A5).
- Fix: *"Which sentence has a mistake?"* · wrong *"Winters here are able to be very long, so bring warm clothes."* · right *"Travelling with small children can be exhausting."* · *"She can't have left already: her coat is still here."* · *"It may snow tonight, so drive carefully."*. EN *"*can* for what is sometimes or typically true, not *be able to*: *Winters here can be very long.*"*

**C6.14 · can-1 row 11 *She may not much experience, but she learns fast.*** · *must fix*
- Problem: a missing verb (readers: "a typo, not a C1 mistake"). It tests nothing about *may … but*.
- Rule: IWR 161, 169.
- Fix: wrong *"Although she may not have much experience, but she learns fast."* EN *"*may … but* already admits one point and then disagrees, so *although* is not needed: *She may not have much experience, but she learns fast.*"* LV *"*may … but* jau atzīst vienu un tad iebilst, tāpēc *although* nav vajadzīgs: *She may not have much experience, but she learns fast.*"*

**C6.15 · will-1 row 7 *I ___ to your party, but nobody told me about it. (come)*** · *must fix*
- Problem: *might have come* is correct and refused. An open gap that several modals fit (would / could / might).
- Rule: HO 53; IWR *"No open gap that several words fit"*.
- Fix: bank *"I ___ ___ ___ to your party, but nobody told me about it."* `would · have · come · came · had` → *would have come* (*would had come*, *would have came* are common learner mistakes).

**C6.16 · will-1 row 9 *Should you will change your mind, just call us.*** · *must fix*
- Problem: a form nobody writes.
- Rule: IWR 161.
- Fix: wrong *"If should you change your mind, just call us."* (a real mix of *if* and inversion). EN *"Use *If you should* or *Should you*, not both: *Should you change your mind, just call us.*"* LV *"Lieto *If you should* vai *Should you*, ne abus kopā: *Should you change your mind, just call us.*"*

**C6.17 · will-1 row 11 *I'd say*, wrong *I would to say | I'd said | I'm saying*** · *must fix*
- Problem: both c1-9 readers: B1 level; *I would to say* is "a random impossible string"; *I'm saying* is grammatical. The judge kept it with a reason the instruction does not give ("asks for the softer opinion").
- Fix: replace with a C1 task of the card (typical past behaviour): *"Choose the correct option: My first flatmate ___ always leave his socks on the sofa. It drove me mad."* ok *would*; wrong *will | was | has*. EN *"*would* for typical, often annoying behaviour in the past: *he would always leave his socks on the sofa*."* LV *"*would* raksturīgai, bieži kaitinošai uzvedībai pagātnē: *he would always leave his socks on the sofa*."*

**C6.18 · subj-1 row 2, LV *"nelieto objektu + to"*** · *must fix*
- Rule: LVT (*papildinātājs* is the term in use).
- Fix: *"Aiz *demand* nelieto papildinātāju + *to*: …"*

**C6.19 · subj-1 rows 5, 6, 11: the same scene three times** · *must fix*
- Problem: *bank refuses / sell the car* (rows 5, 6, in a row) and *sold the car* (row 11). Reader 2 in c1-5 flagged it; the judge did not answer.
- Rule: IWR 27, 100.
- Fix: row 6: *"If the landlord would raise the rent again, we would move out."* (right version *raised*). Row 11: *"I'd rather you wouldn't have posted that photo."* (right *hadn't posted*).

**C6.20 · subj-1 row 8, wrong options *Be that as it is | Being that as it may | Be it as that may*** · *must fix*
- Problem: reader 2 in c1-5: "random strings"; the judge did not answer.
- Fix: wrong *"Being that as it may | Come what may | As it may be"*.

**C6.21 · subj-1 row 10 *I insist that he ___ told the whole truth.*, wrong *is being*** · *must fix*
- Problem: *I insist that he is being told the whole truth* is correct English (*insist* = say firmly that something is true).
- Rule: IWR 4 / HO 51.
- Fix: *"Choose the correct option: The lawyer demanded that her client ___ told the whole truth."* ok *be*; wrong *is being | to be | being*.

**C6.22 · subj-1 rows 8, 12, LV *"ar seno konjunktīvu"*** · *suggestion*
- Problem: *konjunktīvs* is not a term of LATVIAN-TERMS.md, and the card says *"senā forma"*.
- Fix: *"Nemainīgs izteiciens ar seno *be* formu"*.

**C6.23 · will-1 row 9, LV *"(= ja gadījumā)"*** · *suggestion*
- Problem: a calque.
- Fix: *"(= ja nu gadījumā)"*.

**C6.24 · prep-1 row 7 *The road was closed ___ repairing the bridge.*** · *must fix*
- Problem: not natural (reader 2 in c1-6), and the card example.
- Fix: *"Choose the correct option: She took a part-time job ___ starting her own business."* ok *with a view to*; wrong *in order to | so as to | for the purpose to*. EN *"*with a view to* + *-ing* (*to* here is a preposition): *with a view to starting her own business*."*

**C6.25 · prep-1 row 8, the LV explanation is about another sentence** · *must fix*
- Problem: *"Despite the fact that the tickets were cheap… (vai Although the tickets were cheap…)"* (the task is about rain).
- Fix: *"Aiz prievārda nelieto tikai *that*-palīgteikumu: *Despite the fact that it rained…* (vai *Although it rained…*)."*

**C6.26 · prep-1 row 10, wrong option *in place of*** · *suggestion*
- Problem: not a believable mistake for *other than*.
- Rule: IWR 162.
- Fix: *"except of"*.

**C6.27 · prep-1 row 11, *talent at* accepted** · *suggestion*
- Problem: rare (the standard collocation is *a talent for*).
- Fix: remove it, or keep it with a note (C2).

**C6.28 · part-1 row 4 *Not ___ anyone … (know)*** · *must fix*
- Problem: *Not* is given, so only *-ing* is needed (a B1 step, and the point *"not goes first"* is given away).
- Rule: IWR 169.
- Fix: *"Write one word in each gap: ___ ___ anyone in the city, he felt very lonely at first. (not / know)"* → *Not / knowing*.

**C6.29 · part-1 rows 2, 4, LV *"Divdabja teicienam"*, *"divdabja"*** · *must fix*
- Rule: LVT (*divdabis* → *3. forma*; *latvian_lint* bans *divdabis*).
- Fix: row 2 *"Daļai ar *-ing* ir tas pats teikuma priekšmets, kas galvenajam teikumam."* Row 4 *"*Not* stāv pirms formas ar *-ing*."* (If the teacher prefers the real Latvian term *divdabja teiciens*, that is one question for her, with this recommendation.)

**C6.30 · agree-1 row 10, LV *"-ing palīgteikums"*** · *must fix*
- Fix: *"Darbības vārds ar *-ing* kā teikuma priekšmets ir vienskaitlī, arī ja tajā ir daudzskaitlis: …"* (see A7.3).

**C6.31 · order-1 row 2 *Rarely ___ I ___ such a beautiful sunset. (have / see)*** · *must fix*
- Problem: *had / seen* (*Rarely had I seen…*) is correct and refused.
- Fix: add *had / seen* with a note, or add *in my life* (*Rarely in my life ___ I ___ such a beautiful sunset*), which still allows *had*, so the note is the safer fix: `had / seen :: Also possible, about a time in the past. :: Arī pareizi, ja runa ir par laiku pagātnē.`

**C6.32 · order-1 row 8 *Here ___ the bus! (come)*** · *must fix*
- Problem: both c1-7 readers: A2 / B1, a fixed phrase. It is also the card's watch line.
- Rule: IWR 169.
- Fix: *"Just as we left the house, down ___ the rain. (come)"* → *came*. EN *"After an adverb of place at the start (*down, out, in*), the verb can come before a noun subject: *down came the rain*."* LV *"Ja teikums sākas ar vietas apstākļa vārdu (*down, out, in*), darbības vārds var stāvēt pirms lietvārda: *down came the rain*."* Add this line to the card's watch (replacing *There goes my weekend!* if there should be only one line).

**C6.33 · order-1 row 6 (*would've*) and row 9 (*What a long holiday I need!*)** · *suggestion*
- Problem: row 6: add *Had I known about the traffic, I would've left earlier.* to the key. Row 9: reader 2 in c1-7 found *What a long holiday I need!* (starts with *What*, keeps the idea); the judge did not answer.
- Fix: accept it with a note, or reword the instruction: *"Start with *What* and end with *a long holiday*:"*.

**C6.34 · brackets with a comma *(go, light)*, *(stand, turn)*, *(pass, shoot)*** · *suggestion*
- Where: past-1 row 2, pres-2 rows 2, 4.
- Rule: house style in IWR 156 and HO (*(miss / be)*, *(study / pass)*).
- Fix: *(go / light)*, *(stand / turn)*, *(pass / shoot)*.

**C6.35 · agree-1 row 11, AmE *is* refused with *the jury … among themselves*** · *suggestion*
- Problem: AmE speakers mostly say *are* here too, so the refusal is defensible.
- Fix: no change needed; the explanation could say *"(American English uses *is* for the group as one unit, but *themselves* makes it people)"*.


## D. Other

**D1 · `?v=` not bumped after a front-end change** · *must fix*
- Problem: commit f37d32d changed `app/assets/app.js` and `app/assets/app.css` (`{{noun}}` marking). `app/index.html` still has `?v=190`, set in the commit before (337e121), so browsers keep the old files.
- Rule: HO 158 *"When the front end changes, bump ?v= in app/index.html (forgotten from 22 to 23 November)"*; HO 183.
- Fix: `?v=191` in all five places in `app/index.html`, and in `app.js` where it is read.

**D2 · the witty card example is never displayed on v2 cards** · *must fix*
- Problem: `ruleCard()` returns `ruleCard2()` when `r.v2` exists, and `ruleCard2()` has no `example`. The witty lines in `b1_topics.py` are therefore shown only on tiles. This affects every v2 card, not only C1.
- Rule: IWR 171, HO 44.
- Fix (choose one, ask the teacher): (a) put the witty line into the card data as the first example of a use block (done for C1 in section A); or (b) show `s.rule.example` in `ruleCard2()` under the table as *Example:* (display only, needs `?v=`).

**D3 · C1 topics went live with 9-17 tasks** · *must fix* (one question to the teacher)
- Problem: the written rule is 25 per level for a new topic; the C1 topics have 10 or more counted tasks per topic (the changelog: "Every C1 topic can now be learned"), not 25.
- Rule: IWR 14 *"New topic: at least 25 questions per level before it goes live"*; the batch 4 decision "25 per point" (HO 113).
- Fix: either write the missing tasks (about 13 per topic, with the banks of C3 and C4), or ask the teacher once whether 10 (the learnable minimum) is her decision for C1, and write it down dated.

**D4 · judge decisions that were not sound** · *must fix*
- c1-5 012 and c1-9 012: kept *(should / say)* and *(will / be)*: against IWR 156 (C3).
- c1-5 016: did not answer the reader's "random strings" (C6.20).
- c1-5 014: did not answer the reader's "Task 13 shares the same sentence" (C6.19).
- c1-9 001: kept *may not much experience* although a reader called it a typo (C6.14).
- c1-9 011: kept *I'd say* with a reason the task does not give, ignoring "an impossible string" from both readers (C6.17).
- c1-7 008: kept *Here comes the bus* although both readers said A2 / B1 (C6.32).
- c1-6 018: did not answer "closed with a view to … is a little odd" (C6.24).
- c1-6 021: did not answer "'apart' … obviously wrong; 'besides of' is not English" (C6.26).
- c1-4 016, c1-3 003 and c1-6 (agreement): added *won't*, *hasn't changed*, *had / was* without asking for an answer note (C2).
- Every round: "Level notes: kept (Hewings is the model)" as a blanket answer. Hewings is the source of the points, but IWR 169 still requires that a B1 learner cannot solve the task at once; each level note needs its own answer (C5).
- Also: c1-7 says a card line on *on / in / by / without* was added, but it is not on the card learners see (A9.6).
- Rule: BLIND-CHECK.md step 4 *"A third reader (the judge) decides every flag against Murphy and the rules"*.
- Fix: re-judge these flags with the fixes above, in one new blind round for every changed task (BLIND-CHECK *The gate*: a changed task needs a new record).

**D5 · no judge notes for rounds c1-1 and c1-1b** · *suggestion*
- Problem: only `flags.md` exists (c1-2b, c1-3b and c1-8 are covered inside other judge files).
- Rule: BLIND-CHECK step 4.
- Fix: add a short `c1-1-judge.md` / `c1-1b-judge.md`, or one line in `c1-1c-judge.md` saying those rounds were replaced by c1-1c.

**D6 · no review file for the C1 batches** · *suggestion*
- Problem: the C1 generators have no `-notes.md` or `-review.md` (the task, answer, wrong options, EN and LV explanation, source unit). The teacher's 21 November process (she does not read drafts) makes it less urgent, but the review file is how a later reviewer checks a batch.
- Rule: HO 161 *"a review file pending/<name>-review.md"*; writer-brief *"Files you create … notes.md"*.

**D7 · the mistakes found here are not yet stopped by a gate or `bad_examples.json`** · *suggestion*
- Rule: IWR *"Every report ends in one of three: a new gate, a new line in bad_examples.json, or a note why no rule is needed"*.
- Fix: three new entries in `app/tests/bad_examples.json`:
  - (1) `gate` candidate *card_copy*: a v2 card example (table, mistake, use, watch) equal to a task answer or option of its topic after normalising (catches A1.7 … A10.7);
  - (2) `gate` candidate in `latvian_lint.py`: a `*…*` span in an LV explanation that contains only Latvian words (catches C1; today the lint reports nothing for the C1 files);
  - (3) `reader`: *"pres-1 / prep-1 (23 November): the explanation quotes another sentence (23 kilos; the tickets were cheap): read every explanation against its own task."*

**D8 · the old `example` and `form` texts in `b1_topics.py` are out of date** · *suggestion*
- Fix: after the card rewrite, update them in the same change (A11.1), so the italics source and the tile source match what learners see.


## Counts

| Group | Findings | of them *must fix* |
|---|---|---|
| A. Cards | 62 (A0.1-A0.4, A1.1-A1.8, A2.1-A2.4, A3.1-A3.5, A4.1-A4.4, A5.1-A5.3, A6.1-A6.6, A7.1-A7.5, A8.1-A8.7, A9.1-A9.8, A10.1-A10.7, A11.1) | 46 |
| B. Tiles | 4 | 1 |
| C. Tasks | 40 (C1-C5, C6.1-C6.35) | 30 |
| D. Other | 8 | 4 |
| **Total** | **114** | **81** |
