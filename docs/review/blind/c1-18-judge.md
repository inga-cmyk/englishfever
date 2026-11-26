# Judge: blind round c1-18 (C1 drag-and-drop round 1, 70 tasks), 26 November 2026

Source: `docs/task-drafts/_src/c1_drag_1.py` → `c1-drag-1.csv`. Checked against Murphy, Hewings *Advanced Grammar in Use*, Swan
*Practical English Usage*, `ITEM-WRITING-RULES.md`, the C1 rule cards (`app/authoring/cards2_c1.py`), the grammar map's mistake
lists and the other C1 drafts (`c1-*.csv`).

**Totals: KEEP 23 · ACCEPT 5 · CHANGE 41 · DROP 1.** Nothing goes to the teacher.

Notes for whoever applies this:
- **Script bug, not a task problem.** In every order task the flags say "answer not accepted" for the key sentence itself. The
  cause is `tools/blind_check.py` line 107: `norm(a[0])` takes the first *character* when a reader writes the order answer as a
  string. I ignored those lines. The script needs a fix before the next round (accept a string or a one-item list).
- **Why so many changes.** Besides the readers' points (second answers, movable adverbials, B1-level forms), three things the
  readers could not see: (1) **card examples used as answers**: 019 (*The car wouldn't start, so I took the bus*), 029 (*The
  doctor recommended that he not drive*), 030 (*I'd rather you had asked me first*), 034 (*If you want to leave, so be it*),
  043 (*The hotel at which we stayed*), 053 (*If in doubt, ask the pharmacist*), 062 (*Little did she know what was waiting*),
  066 (*I'm finding this course harder*), 069 (*So I'm sitting in the dentist's chair …*), 013 (*It's only Tuesday, and I've
  already spent …*); (2) **near-copies of tasks in the other C1 drafts**: 004 (c1-past-1 *I was cycling to work*), 005
  (c1-past-1 *hoarse … had been shouting*), 009 (c1-perf-1 *This is the third time she has lost her keys this week*), 010
  (c1-perf-1 *By next May I will have been teaching … for ten years*), 011 (c1-perf-1 *Once you paid, the order can't be
  changed*), 012 (c1-perf-1 *I have been ringing the bank all morning*), 050 (c1-part-1 *Having finished the report, she went
  home*), 067 (c1-pres-2 *Anna tells me you've started running*), 069/070 (c1-pres-2 bakery story and football commentary),
  and B2.1 compare-past-1 *I had been writing the report for three hours when my laptop crashed* (so 006 could not become
  that); (3) **order tasks in the agreement topic** whose cards hold only the right verb, so the topic was not tested.
- **Questions with hidden punctuation.** Where the cards also make a natural yes/no question, it is accepted (as in r11b);
  where the question is grammatical but nobody would say it (*were we hoping you might help us*, *should you have told me
  you were going to be late*), it is not.
- **No "Start with" in order tasks**: `plain()` removes it (061 was written with *Start with At*, the readers saw only *Put the
  words in order.*), so inversion in an order task cannot be forced; those tasks were turned into word banks or the
  uninverted order is accepted.
- Every CHANGE is a new task and needs a new blind round (BLIND-CHECK.md). The five ACCEPT tasks only add accepted answers
  and can be recorded with `record-current` (14 November exception).
- Format below: gap tasks give the sentence, the correct chips in order, the wrong chips, EN and LV explanations. Order tasks
  give the sentence (lowercase, as the generator writes it) and every other order to accept.

---

## c1-18-001 · I ___ ___ to retire at sixty, but then prices went up.
**CHANGE.** The readers are right that it is too easy: *have / was* give no believable alternative after *then prices went up*.
The new second clause is in the present, so *have planned* becomes a real temptation. (*was planning* would also be right, so
there is no *planning* chip.)
- Gap: `I ___ ___ to retire at sixty, but with prices the way they are, I'll have to keep working.`
- Correct: `had · planned`
- Wrong chips: `have · plan`
- EN: *had planned to*: a plan that will not happen now. *have planned* would mean the plan still stands, but the second half says it does not.
- LV: *had planned to*: plāns, kas tagad neīstenosies. *have planned* nozīmētu, ka plāns joprojām ir spēkā, bet teikuma otrā daļa saka pretējo.

## c1-18-002 · we were hoping you might help us with the move
**CHANGE.** The readers' question order is not natural English (not accepted), but they are right about the level: 10 cards in
one obvious order. The new sentence adds the indirect question after *wondering if* (statement order) and *might be able to*.
- Order: `we were wondering if you might be able to help us with the move`
- Other orders: none (*were we wondering if …* is not a natural question).
- EN: *We were wondering if …* (past continuous) is a softer, more polite request than *We wonder if …*. After *if* the words keep statement order: *if you might be able to*.
- LV: *We were wondering if …* (Past Continuous) ir maigāks, pieklājīgāks lūgums nekā *We wonder if …*. Aiz *if* vārdu secība ir kā apgalvojumā: *if you might be able to*.

## c1-18-003 · When we were teenagers, my sister ___ ___ borrowing my clothes without asking.
**CHANGE.** Agreed: *is / has* clash with *When we were teenagers* at once. Three gaps; the wrong chips are the grammar map's
mistakes for this point (*was always borrow*, *had always borrowing*).
- Gap: `When we were teenagers, my sister ___ ___ ___ my clothes without asking.`
- Correct: `was · always · borrowing`
- Wrong chips: `had · borrow`
- EN: *was always* + *-ing*: an annoying habit in the past. *always* goes between *was* and the *-ing* form.
- LV: *was always* + darbības vārds ar *-ing*: kaitinošs ieradums pagātnē. *always* stāv starp *was* un formu ar *-ing*.

## c1-18-004 · during the strike we were walking to work every day
**CHANGE.** Two movable time phrases give five or more natural orders, and the scene repeats c1-past-1 (*While my car was being
repaired, I was cycling to work*). Turned into a word bank.
- Gap: `During last summer's heatwave, we ___ ___ in the garden every night.`
- Correct: `were · sleeping`
- Wrong chips: `have · slept`
- EN: The past continuous for something repeated during a limited, temporary period: *we were sleeping in the garden* (only during the heatwave). *last summer* is finished, so not *have slept*.
- LV: Past Continuous darbībai, kas atkārtojās ierobežotā, pagaidu laikā: *we were sleeping in the garden* (tikai karstuma laikā). *last summer* ir beidzies, tāpēc nevis *have slept*.

## c1-18-005 · Her eyes were red and her voice was shaky. She ___ ___ ___.
**CHANGE.** Too easy (only one string is grammatical) and a near-copy of c1-past-1 (*His voice was hoarse because he had been
shouting*) and of the card (*I had been painting the kitchen all day*). New scene; *has been staying* is the map's mistake
(present perfect about a past moment).
- Gap: `When we got back from holiday, the heating was on and there were dirty cups in the sink. Someone ___ ___ ___ in the flat.`
- Correct: `had · been · staying`
- Wrong chips: `has · stayed`
- EN: A conclusion about what had been going on before a past moment (*when we got back*): *had been staying*. *has been staying* would be about now.
- LV: Secinājums par to, kas bija noticis pirms brīža pagātnē (*when we got back*): *had been staying*. *has been staying* būtu par tagadni.

## c1-18-006 · I ___ ___ the report when the power went off, so I lost an hour's work.
**CHANGE.** Agreed: interrupted past continuous is A2-B1, and *had* builds no real form. New point from the card: a number of
times needs the simple form, never the continuous (*had been ringing three times* is on the map's mistake list).
- Gap: `By the time I found my phone, she ___ ___ ___ me four times.`
- Correct: `had · already · texted`
- Wrong chips: `been · texting`
- EN: *four times* is a number of times, so the simple form: *had already texted*. *had been texting me four times* is wrong: the continuous does not count.
- LV: *four times* ir reižu skaits, tāpēc vienkāršā forma: *had already texted*. *had been texting me four times* ir nepareizi: Continuous formu neizmanto, kad skaita reizes.

## c1-18-007 · I was going to call you but I fell asleep
**CHANGE.** Agreed: *was going to* is B1, and the frame copies the card (*We were going to paint the hall, but …*). New sentence
with *had expected* + object + *to*; one natural order.
- Order: `i had expected the interview to be much harder than it was`
- Other orders: none.
- EN: *had expected*: what I thought before; it turned out differently (*than it was*).
- LV: *had expected*: ko domāju iepriekš; iznāca citādi (*than it was*).

## c1-18-008 · She is said ___ ___ ___ a fortune on the house.
**KEEP.** The only note is "acceptable"; only *to have spent* fits, and *to having / to spend* are real wrong forms.

## c1-18-009 · this is the third time the lift has broken down this month
**CHANGE.** *this is the third time this month the lift has broken down* is just as natural, and the frame repeats c1-perf-1
(*This is the third time she has lost her keys this week!*). New task: the past side of the point (*It was the first time* +
past perfect), as a word bank.
- Gap: `It was the first time she ___ ___ on the left, so she was very nervous.`
- Correct: `had · driven`
- Wrong chips: `has · drove`
- EN: *It was the first time* + past perfect: *had driven*. With *It's the first time* it would be *has driven*.
- LV: *It was the first time* + Past Perfect: *had driven*. Ar *It's the first time* būtu *has driven*.

## c1-18-010 · By June, we ___ ___ ___ ___ here for twenty years.
**CHANGE.** Near-copy of c1-perf-1 (*By next May I will have been teaching at this school for ten years*). New task: a state verb,
where the future continuous is the map's mistake.
- Gap: `By the end of this month, I ___ ___ ___ this car for exactly ten years.`
- Correct: `will · have · had`
- Wrong chips: `be · having`
- EN: *by* + a future moment + *for ten years*: future perfect, *will have had*. *have* (= own) is a state, so not *will be having*.
- LV: *by* + nākotnes brīdis + *for ten years*: Future Perfect, *will have had*. *have* (= piederēt) ir stāvokļa darbības vārds, tāpēc nevis *will be having*.

## c1-18-011 · Once you ___ ___ the form, you can't change your answers.
**CHANGE.** Near-copy of c1-perf-1 (*Once you paid, the order can't be changed*); reader 1 is also right that *will submitted*
is not a form. New scene; *will dry* after *once* is the map's mistake. (*is dry* would be correct, so there is no *is* chip.)
- Gap: `Once the paint ___ ___, you can put the furniture back.`
- Correct: `has · dried`
- Wrong chips: `will · dry`
- EN: After *once* about the future we use the present perfect (or the present), not *will*: *once the paint has dried*.
- LV: Aiz *once*, runājot par nākotni, lieto Present Perfect (vai Present Simple), nevis *will*: *once the paint has dried*.

## c1-18-012 · I've been trying to reach you all afternoon
**CHANGE.** *I've been trying all afternoon to reach you* is also natural, the form is B1, and the scene repeats c1-perf-1
(*I have been ringing the bank all morning*). New task from the card (*He admitted having eaten my yoghurt*): *having* + 3rd form.
- Gap: `I don't remember ___ ___ this film before, but I know how it ends.`
- Correct: `having · seen`
- Wrong chips: `to · see`
- EN: *remember having seen* = remember an earlier experience. *remember to see* means "not forget to do it" and does not fit.
- LV: *remember having seen* = atcerēties agrāku pieredzi. *remember to see* nozīmē "neaizmirst izdarīt", un tas te neder.

## c1-18-013 · It's only Tuesday, and I ___ ___ three emails from the landlord this week.
**CHANGE.** Agreed: A2-B1, and a near-copy of the card (*It's only Tuesday, and I've already spent my weekly budget*) and of two
c1-perf-1 tasks (*It's only ten o'clock …*, *It's only eleven …*). New task: the perfect infinitive for an imagined past.
- Gap: `She told the boss he was wrong in front of everyone? I'd love ___ ___ ___ his face!`
- Correct: `to · have · seen`
- Wrong chips: `saw · having`
- EN: *I'd love to have seen*: a wish about the past that cannot come true now (*to have* + 3rd form).
- LV: *I'd love to have seen*: vēlēšanās par pagātni, kas vairs nevar piepildīties (*to have* + 3. forma).

## c1-18-014 · the house is thought to have been built in the 1890s
**ACCEPT** `is the house thought to have been built in the 1890s` (a natural question with the same cards). Not accepted:
*in the 1890s the house is thought to have been built* (fronted, not natural).

## c1-18-015 · If you ___ ___ any problems with the app, just email us.
**KEEP.** No reader found a problem; *will have / would have* are wrong after *if* here, *had* builds nothing with the other chips.

## c1-18-016 · she would spend hours in the garden when she was a child
**KEEP.** Both clause orders are already in the key; the readers' "not accepted" is the script bug.

## c1-18-017 · If you ___ ___ to bed at two every night, of course you're tired!
**KEEP.** Both readers call it a good C1 item; only *will go* fits.

## c1-18-018 · I ___ ___ ___ the shops would be open on a Sunday. (not flagged)
**KEEP.** Only *would have thought* fits; *will have thought* is a real form that does not.

## c1-18-019 · the car wouldn't start this morning so I took the bus
**CHANGE.** This is the will card's own example (*The car wouldn't start, so I took the bus.*); also a near-copy of c1-will-1
(*the printer wouldn't work this morning*), and *this morning* moves to three places. *wouldn't* for refusal is already a B1.2
point (gap-points-b12-1). New sentence: *would* to make an opinion softer.
- Order: `i'm afraid i'd have to disagree with you on that`
- Also accept: `i'd have to disagree with you on that i'm afraid`
- EN: *I'd have to disagree* is a softer, more polite way to say *I disagree*: *would* adds distance.
- LV: *I'd have to disagree* ir maigāks, pieklājīgāks veids, kā pateikt *I disagree*: *would* rada distanci.

## c1-18-020 · Leave a little earlier in case the roads ___ ___ busy.
**CHANGE (setting only).** The point and the chips are right (*will be* after *in case* is the card's mistake), but reader 2 is
right that formal *should* after the chatty *Leave a little earlier* sounds stilted. A formal notice fits *should*.
- Gap: `Please allow extra time for your journey in case the roads ___ ___ busy.`
- Correct: `should · be`
- Wrong chips: `will · would`
- EN: *in case* + *should*: a formal way to talk about a possible situation. Not *will* or *would* after *in case*.
- LV: *in case* + *should*: oficiāls veids, kā runāt par iespējamu situāciju. Aiz *in case* nelieto *will* vai *would*.

## c1-18-021 · you should have told me you were going to be late
**KEEP.** *should you have told me …* is grammatical but nobody would say it (not accepted); the comma-spliced order is not
natural either.

## c1-18-022 · We ___ ___ well take a taxi: the last bus has gone.
**KEEP.** Only *might as* fits; *good* gives the real mistake *might as good*.

## c1-18-023 · he can't have been at home last night
**KEEP.** The fronted *last night* order is already in the key; *can't he have been at home last night* is not a natural question.

## c1-18-024 · The roads around here ___ ___ really dangerous in winter.
**CHANGE.** Agreed: *can* for what is sometimes true is B1, and the content repeats c1-can-1 (*Winters here are able to be very
long*, *can be exhausting*). New task: *can* is wrong for a guess about one situation now (card: *May she be at home already?*
→ *Could*; map: *It can be snowing now*).
- Gap: `I've rung the bell twice and nobody's answering. They ___ ___ out in the garden.`
- Correct: `might · be`
- Wrong chips: `can · being`
- EN: A guess about this situation now: *might be* (or *may / could be*). *can be* is only for what is sometimes true in general.
- LV: Minējums par šo situāciju tagad: *might be* (vai *may / could be*). *can be* lieto tikai tam, kas vispār mēdz būt.

## c1-18-025 · The museum was closed, but we ___ ___ to walk round the garden.
**CHANGE.** Agreed: *could* cannot fill two gaps (*could allowed*), so the point was not tested. Now both answers are two words:
*could go* is the real mistake (card: *was / were allowed to*, not *could*, for permission on one occasion; Swan).
- Gap: `The house itself was closed to visitors, but we ___ ___ into the garden.`
- Correct: `were · allowed`
- Wrong chips: `could · go`
- EN: Permission on one occasion in the past: *were allowed* (into). *could go* is used for general permission, not for one occasion.
- LV: Atļauja vienā reizē pagātnē: *were allowed* (into). *could go* lieto vispārējai atļaujai, nevis vienai reizei.

## c1-18-026 · she may be clever but she has no common sense
**ACCEPT** `clever she may be but she has no common sense` (fronting for contrast: correct and idiomatic, Swan; same meaning).
Not accepted: the clauses swapped (*she has no common sense but she may be clever*): it loses the meaning of *may … but*.

## c1-18-027 · From our seats, we ___ ___ the actors' faces clearly.
**CHANGE.** Agreed: *could see* is A2-B1, *managed* builds no form, and the content repeats c1-can-1 (*I could hear the sea*).
New task: *may well*; *may good* is the map's mistake.
- Gap: `With this much snow, the match ___ ___ be cancelled, so check the website before you set off.`
- Correct: `may · well`
- Wrong chips: `can · good`
- EN: *may well* = it is quite likely. Not *may good*, and not *can* for a guess about one event.
- LV: *may well* = diezgan iespējams. Nevis *may good*, un nevis *can*, minot par vienu notikumu.

## c1-18-028 · they might have been delayed by the snow
**ACCEPT** `might they have been delayed by the snow` (a natural question with the same cards).

## c1-18-029 · The doctor recommended that he ___ ___ coffee for a month.
**CHANGE.** Both readers are right: *drink no coffee* is correct, and *drinks* after *recommended that* is arguable (BrE ordinary
tense). It is also almost the subjunctive card's example (*The doctor recommended that he not drive for a week*). New scene; the
wrong chips build no ordinary tense that anyone could defend (*to speak* after *that* is the map's mistake type).
- Gap: `The coach advised that the captain ___ ___ to journalists before the final.`
- Correct: `not · speak`
- Wrong chips: `to · speaks`
- EN: *advise that* + subject + base form; the negative is *not* + base form: *that the captain not speak*. No *to* after *that*.
- LV: *advise that* + teikuma priekšmets + pamatforma; noliegumā *not* + pamatforma: *that the captain not speak*. Aiz *that* nelieto *to*.

## c1-18-030 · I'd rather you had asked me before taking my car
**CHANGE.** The readers' fronted order is awkward (not accepted), but the sentence is the card's example (*I'd rather you had
asked me first*). New sentence, one natural order.
- Order: `i'd rather we had booked somewhere with a pool`
- Other orders: none.
- EN: *I'd rather* + subject + past perfect: a wish about the past (*we booked somewhere else*).
- LV: *I'd rather* + teikuma priekšmets + Past Perfect: vēlēšanās par pagātni (*mēs rezervējām citu vietu*).

## c1-18-031 · It is vital that the patient ___ ___ left alone tonight.
**KEEP.** Reader 2 confirms; *not being / not been* are wrong, *be not* is archaic.

## c1-18-032 · If the factory ___ ___ close, two hundred people would lose their jobs. (not flagged)
**KEEP.** Only *were to* fits with *would*; *is to / has to* need *will*. Different scene from c1-subj-1 (*If the bank were to refuse the loan*).

## c1-18-033 · the committee insisted that the decision be made public
**CHANGE.** *public* can also go before a noun, so the cards build other sentences (*the public insisted that the committee
decision be made*). New ending without an adjective.
- Order: `the committee insisted that the decision be announced to all staff`
- Other orders: none (*the decision insisted …* is nonsense).
- EN: *insist that* + subject + base form: *the decision be announced* (for every person, also in the past).
- LV: *insist that* + teikuma priekšmets + pamatforma: *the decision be announced* (visām personām, arī pagātnē).

## c1-18-034 · If that's your final decision, so ___ ___.
**CHANGE.** The reader's note (a fixed phrase) is fine, but the frame *If …, so be it* copies the card (*If you want to leave, so
be it.*). Same point, another frame.
- Gap: `My colleagues may think I'm rude for leaving at five, but so ___ ___.`
- Correct: `be · it`
- Wrong chips: `is · was`
- EN: A fixed phrase that keeps the old form: *so be it* (= I accept it). Not *so is it*.
- LV: Nemainīgs izteiciens, kas saglabā seno formu: *so be it* (= es to pieņemu). Nevis *so is it*.

## c1-18-035 · the landlord requested that all tenants should leave their keys at reception
**CHANGE.** Agreed: *all* moves (*all their keys*) and landlord and tenants can swap. New sentence whose people cannot swap.
- Order: `the captain requested that passengers should remain in their seats`
- Other orders: none.
- EN: *request that* + *should* + verb: the British way, less formal than the base form alone.
- LV: *request that* + *should* + darbības vārds: britu variants, mazāk oficiāls nekā tikai pamatforma.

## c1-18-036 · The news ___ ___ better than we expected.
**CHANGE.** Agreed: *news is* is B1 (and the card's own example is *The news is on at nine*); *is getting better than we
expected* is also odd. New noun from the same point (map: *This pair of glasses are new*).
- Gap: `This pair of glasses ___ ___ me over two hundred euros.`
- Correct: `has · cost`
- Wrong chips: `have · costed`
- EN: The subject is *pair* (singular), so *has cost*. The past form of *cost* is *cost*.
- LV: Teikuma priekšmets ir *pair* (vienskaitlis), tāpēc *has cost*. *cost* pagātnes forma ir *cost*.

## c1-18-037 · the majority of the residents are against the new car park
**CHANGE.** Agreed: *the majority of the new residents are against the car park* is just as good. As an order task it also
did not test agreement (the cards hold only *are*). New word bank: the subject, not the plural complement, decides (map
x_agr_clause: *The biggest cost are the salaries*).
- Gap: `Our biggest expense ___ ___ ___ the rent and the heating bills.`
- Correct: `has · always · been`
- Wrong chips: `have · being`
- EN: The subject is *expense* (singular); what comes after the verb does not change it: *has always been*.
- LV: Teikuma priekšmets ir *expense* (vienskaitlis); tas, kas seko darbības vārdam, to nemaina: *has always been*.

## c1-18-038 · She is one of the few doctors who ___ ___ home visits.
**KEEP.** *who* refers to *doctors*, so the verb is plural (Hewings, Swan). *still makes* is common in speech, but the card's
point x_agr_rel lists exactly this as the mistake in careful English, and *few* makes the plural even clearer. Not accepted.

## c1-18-039 · There ___ ___ three cars parked outside your house all morning.
**KEEP.** Only the contraction *there's* is heard with a plural, in speech; the full *There has been three cars* is not standard,
and the card x_agr_there teaches *there are / have been* with plurals. Not accepted.

## c1-18-040 · two thirds of the money has already been spent
**CHANGE.** *already* moves (*has been spent already*), and the order task did not test the point (the cards hold only *has*).
Word bank instead.
- Gap: `Two thirds of the money ___ ___ spent on salaries.`
- Correct: `has · been`
- Wrong chips: `have · being`
- EN: A fraction + *of* + an uncountable noun takes a singular verb: *two thirds of the money has been spent*.
- LV: Daļa + *of* + neskaitāms lietvārds: darbības vārds vienskaitlī, *two thirds of the money has been spent*.

## c1-18-041 · The cost of the repairs ___ ___ higher than we thought. (not flagged)
**KEEP.** Only *was much* fits; *were* (agreement with *repairs*) and *more higher* are real mistakes.

## c1-18-042 · neither the teacher nor the students were happy with the results
**KEEP.** With the people swapped the verb must be *was* (the nearer noun decides, card: *either … or*); *neither the students nor
the teacher were* is the careful-style mistake the map lists. Putting *students* next to *were* is exactly what the task tests.

## c1-18-043 · This is the hotel ___ ___ we stayed on our honeymoon.
**CHANGE.** The task is fine in itself, but the answer copies the card (*The hotel at which we stayed was lovely*). Same point,
a person, so *whom*.
- Gap: `The manager ___ ___ I worked in my first job taught me everything I know.`
- Correct: `for · whom`
- Wrong chips: `who · that · which`
- EN: In formal English the preposition goes before *whom* (people) or *which* (things), never before *who* or *that*: *the manager for whom I worked*.
- LV: Oficiālā valodā prievārds stāv pirms *whom* (cilvēki) vai *which* (lietas), nekad pirms *who* vai *that*: *the manager for whom I worked*.

## c1-18-044 · this is the problem we need to deal with
**CHANGE.** Agreed: *the problem we need to deal with is this* and the question *is this the problem …* are correct. The new
sentence starts with a contraction (no question possible) and has a two-word verb with its preposition at the end.
- Order: `it's not the kind of job you can walk away from`
- Other orders: none.
- EN: In everyday English the preposition stays at the end, with its verb: *a job you can walk away from*.
- LV: Ikdienas valodā prievārds paliek beigās pie sava darbības vārda: *a job you can walk away from*.

## c1-18-045 · She has two brothers, both ___ ___ live abroad.
**KEEP.** *both of them live abroad* joins two sentences with a comma only (a comma splice); the card teaches *none / both of
which / whom* for one sentence. Not accepted.

## c1-18-046 · The course is open to everyone, ___ ___ age.
**KEEP.** *regardless of* is on the card's list of formal multi-word prepositions; a B1 learner does not know it, and *despite of*
is a real mistake.

## c1-18-047 · the matter is being looked into by the police
**ACCEPT** `is the matter being looked into by the police` (a natural question with the same cards).

## c1-18-048 · He insisted ___ ___ for the whole meal.
**CHANGE.** Agreed: *insist on* + *-ing* is B1-B2. New task: noun + preposition + *-ing* (map: *little hope to win*).
- Gap: `Two goals down with five minutes left, there's little hope ___ ___ the match now.`
- Correct: `of · winning`
- Wrong chips: `to · win`
- EN: The noun *hope* takes *of* + *-ing*: *little hope of winning* (not *hope to win* after the noun).
- LV: Lietvārdam *hope* seko *of* + darbības vārds ar *-ing*: *little hope of winning* (aiz lietvārda nevis *hope to win*).

## c1-18-049 · she's not an easy person to work with
**KEEP.** Only the script bug; reader 2 says "Fine".

## c1-18-050 · ___ ___ the email, she deleted it at once.
**CHANGE.** Near-copy of c1-part-1 (*Having finished the report, she went home early*; *Having checked the train times …*).
New point from the card: one subject for both parts (map: *Walking home, it started to rain*).
- Gap: `Unpacking my suitcase at the hotel, ___ ___ that my passport was missing.`
- Correct: `I · noticed`
- Wrong chips: `it · seemed`
- EN: The *-ing* part tells us about the subject of the main clause: I was unpacking, so *I noticed*. *it seemed* would mean that "it" was unpacking.
- LV: Daļa ar *-ing* ir par galvenā teikuma priekšmetu: koferi izsaiņoju es, tāpēc *I noticed*. *it seemed* nozīmētu, ka izsaiņoja "it".

## c1-18-051 · not wanting to wake the children we spoke in whispers
**KEEP.** Both clause orders are already in the key. *wanting not to wake the children …* is not accepted: the card teaches
*not* first (*Not having a key*), and the readers themselves call it less natural.

## c1-18-052 · The weather ___ ___, we decided to stay indoors.
**CHANGE.** Both readers: correct but stilted for an everyday sentence (*As the weather was bad* is what people say). The
construction belongs in formal reports; a news-style sentence gives it a natural home and a C1 form (perfect passive).
- Gap: `All flights ___ ___ ___, passengers were offered rooms at a nearby hotel.`
- Correct: `having · been · cancelled`
- Wrong chips: `were · being`
- EN: A participle clause with its own subject (*All flights*), formal: *All flights having been cancelled, …* (= because all flights had been cancelled). *were being cancelled* would join two sentences with only a comma.
- LV: Teiciens ar savu teikuma priekšmetu (*All flights*), oficiāli: *All flights having been cancelled, …* (= tā kā visi reisi bija atcelti). *were being cancelled* savienotu divus teikumus tikai ar komatu.

## c1-18-053 · ___ ___ doubt, ask a member of staff.
**CHANGE.** Reader 2's point (capitals) is minor, but the sentence copies the card (*If in doubt, ask the pharmacist.*). Same
point, another conjunction + participle.
- Gap: `___ ___, he refused to go to bed until the match was over.`
- Correct: `Though · exhausted`
- Wrong chips: `If · exhausting`
- EN: Conjunction + 3rd form with no subject and no verb: *Though exhausted* (= although he was exhausted). *exhausting* describes what makes someone tired.
- LV: Saiklis + 3. forma bez teikuma priekšmeta un darbības vārda: *Though exhausted* (= lai gan viņš bija ļoti noguris). *exhausting* raksturo to, kas nogurdina.

## c1-18-054 · the woman sitting next to me on the plane was a famous actress
**CHANGE.** Agreed: *on the plane* and *next to me* swap, and the task was easy. Word bank: where the short *-ing* form is not
possible (map: *the candidates interviewing today* for those being interviewed).
- Gap: `The flats ___ ___ near the station will be ready next spring.`
- Correct: `being · built`
- Wrong chips: `building · are · have`
- EN: The flats do not build anything; they are being built: the short form of *which are being built* is *being built*.
- LV: Dzīvokļi paši neko neceļ, tos ceļ: īsā forma no *which are being built* ir *being built*.

## c1-18-055 · The storm brought down power lines, ___ thousands of homes ___ electricity. (not flagged)
**KEEP.** Only *leaving … without* fits; *left* is the map's mistake (*…, flooded the lower streets*). Different scene from c1-part-1.

## c1-18-056 · generally speaking people here are very friendly
**CHANGE.** Agreed: the phrase can go first, in the middle or last, and *speaking generally* also exists. Word bank instead;
*spoken* and the adjective are the map's mistakes (*Generally spoken; Speaking general*).
- Gap: `___ ___, the job isn't mine until I've signed the contract.`
- Correct: `Strictly · speaking`
- Wrong chips: `Strict · spoken`
- EN: *Strictly speaking* is a fixed comment phrase (= if we are exact): adverb + *speaking*.
- LV: *Strictly speaking* ir nemainīgs komentāra izteiciens (= ja runājam precīzi): apstākļa vārds + *speaking*.

## c1-18-057 · Not only ___ ___ late, but he also forgot the tickets. (not flagged)
**KEEP.** Only *was he* fits; *he was* (no inversion) and *did he late* are the real mistakes.

## c1-18-058 · no sooner had the film started than the power went off
**ACCEPT** `the film had no sooner started than the power went off` (standard English, Swan, Hewings; the learner still needs
*no sooner … than*). Inversion cannot be forced here: the generator removes *Start with* from order instructions.

## c1-18-059 · ___ ___ to resign, who would replace her? (not flagged)
**KEEP.** Only *Were she* fits.

## c1-18-060 · ___ ___ I like him, I can't agree with him on this. (not flagged)
**KEEP.** Only *Much as* fits; *So that* and *So as* make no sentence.

## c1-18-061 · at the top of the hill stands an old church
**CHANGE.** Agreed: *an old church stands at the top of the hill* is correct, and an order task cannot force the inversion (the
*Start with At* line was removed by `plain()`). The sentence is also the name of the grammar point. Word bank: after a place
phrase the verb agrees with the subject that follows it.
- Gap: `Opposite our office ___ two new cafés, so lunch is never a problem.`
- Correct: `are`
- Wrong chips: `is · stands · there`
- EN: A place phrase first, then the verb, then the subject. The subject is *two new cafés* (plural), so *are*.
- LV: Vietas apzīmētājs pirmais, tad darbības vārds, tad teikuma priekšmets. Teikuma priekšmets ir *two new cafés* (daudzskaitlis), tāpēc *are*.

## c1-18-062 · Little ___ ___ know that the house was full of secrets. (not flagged)
**CHANGE.** The readers missed it: this is the order card's example (*Little did she know what was waiting at home.*). Another
negative word at the start.
- Gap: `Not once ___ ___ thank us for looking after his dog.`
- Correct: `did · he`
- Wrong chips: `has · was`
- EN: After *Not once* at the start, *did* comes before the subject: *Not once did he thank us*.
- LV: Pēc *Not once* teikuma sākumā *did* stāv pirms teikuma priekšmeta: *Not once did he thank us*.

## c1-18-063 · all we need now is a bit of luck
**CHANGE.** Agreed: *now all we need is …*, *a bit of luck is all we need now* and more are natural. Word bank on the same card
line (*what … is*); *was resigned* is the map's mistake.
- Gap: `What she did ___ ___ out of the meeting without a word.`
- Correct: `was · walk`
- Wrong chips: `walked · is`
- EN: *What she did was* + base form puts the focus on the action: *What she did was walk out*. Not *was walked*.
- LV: *What she did was* + pamatforma izceļ darbību: *What she did was walk out*. Nevis *was walked*.

## c1-18-064 · You ___ ___ very difficult today. That's not like you.
**KEEP.** *be being* + adjective for behaviour now is on the C1 card (*you're being very quiet*); the wrong chips build real
wrong forms (*are been*).

## c1-18-065 · we're hoping you can join us for dinner on Saturday
**CHANGE.** Agreed: B1 and *on Saturday for dinner* is equally natural. New sentence with *wondering whether* + *you'd mind* +
*-ing*; the contraction rules out a question.
- Order: `i'm wondering whether you'd mind swapping seats with me`
- Other orders: none.
- EN: *I'm wondering whether …* (present continuous) is a softer, more polite request than *Would you swap …?*
- LV: *I'm wondering whether …* (Present Continuous) ir maigāks, pieklājīgāks lūgums nekā *Would you swap …?*

## c1-18-066 · I ___ ___ it harder and harder to get up in the mornings.
**CHANGE.** Almost the card's example (*I'm finding this course harder than I expected*). Another mental-state verb.
- Gap: `I ___ ___ more and more how much I miss the sea.`
- Correct: `am · realising`
- Wrong chips: `realise · was`
- EN: A growing awareness now: the continuous, *I'm realising more and more*.
- LV: Apziņa, kas tagad pieaug: Present Continuous, *I'm realising more and more*.

## c1-18-067 · Anna ___ ___ you're moving to Berlin. Is it true?
**CHANGE.** Near-copy of c1-pres-2 (*Anna tells me you've started running*). New sentence; *is telling* (map: *I am hearing
you've moved*) and *says me* are the believable mistakes.
- Gap: `Your brother ___ ___ you've decided to sell the flat. Is that right?`
- Correct: `tells · me`
- Wrong chips: `is · telling · says`
- EN: News we have heard: present simple, *Your brother tells me …*. *say* takes no person straight after it.
- LV: Ziņa, ko esam dzirdējuši: Present Simple, *Your brother tells me …*. Aiz *say* cilvēks uzreiz nestāv.

## c1-18-068 · we're loving every minute of our holiday
**CHANGE.** Agreed: seven cards, one obvious order. New sentence with a mental-state verb in the continuous.
- Order: `i'm already regretting my decision to move to the countryside`
- Also accept: `i'm regretting my decision to move to the countryside already`
- EN: *regret* about a feeling that is new and growing now can be continuous: *I'm already regretting*.
- LV: *regret* par sajūtu, kas ir jauna un tagad pieaug, var būt Present Continuous formā: *I'm already regretting*.

## c1-18-069 · so I'm standing at the bus stop and this man comes up to me
**CHANGE.** The task is correct, but the story present now appears in the card (*So I'm sitting in the dentist's chair …*) and
twice in c1-pres-2 (*So I'm at the bakery … this woman suddenly turns round*). Another point of the topic: verbs that do the act
by being said (map: *I'm admitting I was wrong* said as the act).
- Gap: `OK, OK, I ___ ___: I forgot to book the restaurant.`
- Correct: `admit · it`
- Wrong chips: `am · admitting`
- EN: Saying *I admit it* is the act of admitting, so the present simple: not *I'm admitting it*.
- LV: Pasakot *I admit it*, cilvēks jau atzīstas, tāpēc Present Simple: nevis *I'm admitting it*.

## c1-18-070 · And now the chef ___ the onions and ___ them into the hot pan.
**DROP.** Too easy (the past chips go at once after *And now*), and the commentary point is already tested by c1-pres-2 (*And
Jones passes the ball to Taylor, who shoots and scores!*) and shown on the card (*Silva takes the corner …*). In a word bank the
real contrast (simple for a quick completed action, not *is chopping*) needs two-word slots, and in a live demonstration the
continuous is often also correct, so no version has exactly one answer. The topic keeps six drag tasks.
