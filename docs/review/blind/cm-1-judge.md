# Judge: blind round cm-1 ("Correct the mistake" round 1: Present simple, Past simple, Future; 28 tasks), 27 November 2026

Source: `docs/task-drafts/_src/correct_mistake_1.py` → `correct-mistake-1.csv`. Checked against Murphy (units 2-5, 13, 19-23),
`ITEM-WRITING-RULES.md` (all dated sections), the rule cards (`app/authoring/cards2.py`, `cards2_a2.py`, `cards2_b.py`,
`cards2_d.py`, `new_points.py`), the grammar map's typical errors, the bank (`app/content/items.json`) and the other drafts.
How the checker works was taken into account: `Grader::norm` handles *n't, 'm, 're, 've, 'll*, commas and the final stop (not
*'s*); `Grader::correctedPart` lets the learner type only the corrected words, so a learner never has to retype a correct part.

**Totals: KEEP 13 (incl. 10 unflagged) · ADD ANSWERS 2 · REWRITE 13 · DROP 0.** Nothing goes to the teacher.

Notes for whoever applies this:
- **What the readers could not see: card examples and near-copies in the bank.** Rule of 21 November: *a help card example is
  never a task's answer*; rule of 4 November: *different topics or levels do not reuse the same scene*. Hits:
  001 (agreement card mistake *My sister work in a bank* → *works*), 008 (present simple card *Water boils at 100 degrees*),
  019 (future card *I'm going to visit my aunt this weekend*; fu-A21-5a *I'm going to visit my parents*, same topic and level),
  021 (shall card and future card *Shall I open the window?* / *✗ Will I open the window?*; match task *Shall I open the
  window? = Yes, please. It's hot in here*), 022 (fu-A22-2a option *Your bag looks heavy. I'll carry it.*, same topic and
  level; shall card *Will I carry your bag?*), 023 (future card *I'm meeting Anna at six*; pc-A22-2a *I'm meeting Anna
  tomorrow at five*), 027 (wont_refuse card and future card *The car wouldn't start this morning*; B1.2 order task *my car
  wouldn't start this morning so i worked from home*), 028 (fu-B12-1a *Hurry up! The film ___ start.* → *is about to*: the
  same sentence, same topic and level), 009 (dep_prepositions card and two tasks *It depends on the weather*), 016 (C1 card
  *… lost my keys, I had to call a locksmith*; present perfect option *I lost my keys yesterday*). The new sentences below were
  checked against the bank and the drafts (no hit).
- **"Keep …" where several corrections are possible** (rule of 3 November). For *going to* tasks the readers rightly found the
  present continuous and *will* as other fixes (019, 020, 024, 026); *Keep *going to** (or *Keep *going**) rules them out
  without naming a tense, as in the existing *Correct the sentence. Keep *will*: We will can visit you next summer.*
  `Grader::correctedPart` accepts *Correct the mistake. Keep …:* (its pattern allows up to 40 characters before the colon).
- **Generator bug (not a task problem).** In `correct-mistake-1.csv` the LV explanation of 028 came out as
  *\*be about\* to + pamatforma = tūlīt: \*The film is about\* to \*start\**: the LV pass (`lv_for_file` → `lv_fix` in
  `_src/lib.py`) takes *to* for a Latvian word and moves it out of the italics. The new 028 has *about to* in its LV text
  again: check the CSV after generating, and fix the LV pass or add an exception.
- Every REWRITE is a new task and needs a new blind round. 006 and 007 only add accepted answers (006 also answer notes, which
  the 6 November rule requires so that "Correct" is never shown with the explanation of another form).
- Rejected reader answers fall into four kinds, so they are not repeated each time: (a) **the subject made plural** (*My
  sisters work*, *Do your brothers play*): another sentence, not a correction; (b) **emphasis added** (*I do agree*, *It all
  depends*, *always boils*, *just about to*); (c) **a correct part changed or removed** (*Could you say it again*, dropping
  *yesterday*, *about to begin*); (d) **the tense of the whole sentence changed** (*It will depend*, *I thought this plan is*).
  In each case the learner who knows the point types the key answer; with `correctedPart` they can also type only the fixed
  words.

---

## cm-1-001 · My sister work in a hotel and she loves it.
**REWRITE.** The corrected sentence is the agreement card's own mistake example (*My sister work in a bank.* → *My sister
works in a bank.*) with one noun changed. Reader 1 is also right that *My sister is working in a hotel and she loves it* is
correct (a temporary job); a habit word removes it. Reader 2's *My sisters work … they love* is kind (a).
- Sentence: `Correct the mistake: My neighbour walk her dog every morning before work.`
- Accepted: `My neighbour walks her dog every morning before work.`
- EN: *he / she / it* + verb-*s*: *My neighbour walks*. *every morning* is a habit.
- LV: *he / she / it* + darbības vārds ar *-s*: *My neighbour walks*. *every morning* rāda ieradumu.
- (*is walking … every morning* is wrong without *always*; *My neighbours walk their dog* needs two changes and another subject.)

## cm-1-002 · I am agree with you about the price.
**KEEP.** *I do agree* is kind (b): emphasis that the sentence did not have. The mistake (*am* + verb) is the grammar map's
BE-VERB error, removed by one change.

## cm-1-003 · Do your brother play any sport?
**KEEP.** Both readers' *Do your brothers play any sport?* is kind (a): it asks about other people. The task is about *your
brother* = *he*; the explanation says so. The sentence is short and natural at A2.1.

## cm-1-006 · Sorry, I am not understanding the question. Can you say it again?
**ADD ANSWERS** (with answer notes). *I can't understand* and *I didn't understand* fix the same mistake (no continuous with
*understand*) in another correct way, and both are what people really say here; *didn't* changes one verb, not the time of
the sentence (you heard the question a moment ago). *Could you say it again?* is kind (c).
- Add: `Sorry, I can't understand the question. Can you say it again?`
  - Note EN: Also correct: *can't understand* says you are not able to understand it. *understand* is a state verb, so never *am not understanding*.
  - Note LV: Arī pareizi: *can't understand* saka, ka tu nespēj to saprast. *understand* ir stāvokļa darbības vārds, tāpēc nekad *am not understanding*.
- Add: `Sorry, I didn't understand the question. Can you say it again?`
  - Note EN: Also correct: *didn't understand* is about the moment you heard it. *understand* is a state verb, so never *am not understanding*.
  - Note LV: Arī pareizi: *didn't understand* ir par brīdi, kad tu to dzirdēji. *understand* ir stāvokļa darbības vārds, tāpēc nekad *am not understanding*.

## cm-1-007 · I'm thinking this plan is too expensive for us, so let's look for another one.
**ADD ANSWERS.** The mistake stays. Murphy unit 4 marks it explicitly (*I think Mary is Canadian … not I'm thinking*), and it is
the grammar map's typical error for this point (*I am thinking it is a good idea*). Reader 2's point that *I'm thinking* + a
clause is heard in informal speech is true for a suggestion that is still forming (*I'm thinking we could leave early*). Here
it is a judgement (*this plan is too expensive*) followed by a conclusion (*so let's look for another one*). That is an
opinion, so the simple form is the clear answer at B1.1. Reader 1's *I think that …* is the same correction with the optional
*that*; accept it. *I thought this plan is …* mixes the tenses (wrong); *I do think* is kind (b).
- Add: `I think that this plan is too expensive for us, so let's look for another one.`

## cm-1-008 · Water is boiling at 100 degrees Celsius, so the thermometer will show 100 when it starts to bubble.
**REWRITE.** *Water boils at 100 degrees* is the present simple card's example for facts. (Reader 2's *always boils* is kind (b).)
- Sentence: `Correct the mistake: Light is travelling faster than sound, so you see the lightning before you hear the thunder.`
- Accepted: `Light travels faster than sound, so you see the lightning before you hear the thunder.`
- EN: A fact that is always true: present simple, *Light travels faster than sound*. *is travelling* = it is happening now.
- LV: Fakts, kas vienmēr ir patiess: Present Simple, *Light travels faster than sound*. *is travelling* = tas notiek tagad.

## cm-1-009 · It's depend on the weather, so we'll decide about the picnic tomorrow morning.
**REWRITE** (scene only). Reader 2's *It all depends* is kind (b) and *It will depend* is kind (d). However, *It depends on the
weather* is an example on the dependent prepositions card and the answer of two tasks there (*It depends ___ the weather*,
*Which sentence is NOT correct? … It depends from the weather*). A new object keeps the mistake.
- Sentence: `Correct the mistake: It's depend on the traffic, so I can't say what time I'll be home.`
- Accepted: `It depends on the traffic, so I can't say what time I'll be home.`
- EN (unchanged): *depend* is a verb: *It depends on*, not *It's depend*.
- LV (unchanged): *depend* ir darbības vārds: *It depends on*, nevis *It's depend*. Tulkojot burtiski *tas ir atkarīgs*, rodas *It's depend*.

## cm-1-016 · I have lost my keys yesterday, so I had to call a locksmith.
**REWRITE** (scene only). Reader 2's sentence without *yesterday* is kind (c): it removes the time that makes the mistake. The
scene repeats the C1 card (*Having lost my keys, I had to call a locksmith*) and the present perfect option *I lost my keys
yesterday*.
- Sentence: `Correct the mistake: I have seen this film yesterday, so let's watch something else tonight.`
- Accepted: `I saw this film yesterday, so let's watch something else tonight.`
- EN: *yesterday* is a finished time: past simple, *I saw*, not *I have seen*.
- LV: *yesterday* ir pabeigts laiks: Past Simple, *I saw*, nevis *I have seen*.
- (*I've already seen this film* drops *yesterday*, kind (c); *I watched* changes the verb: not accepted.)

## cm-1-019 · I'm going visit my parents this weekend.
**REWRITE.** Both readers are right: *I'm visiting my parents this weekend* and *I'll visit …* are other correct fixes. The
answer is also the future card's example (*I'm going to visit my aunt this weekend*) and fu-A21-5a (*I'm going to visit my
parents*). New scene (not *a new sofa*: B1 order task *we are going to buy a new sofa*), and *Keep *going**.
- Sentence: `Correct the mistake. Keep *going*: We're going get a dog next year.`
- Accepted: `We're going to get a dog next year.` (*We are going to …* is covered by `norm`; the fronted *Next year we're going to get a dog.* by `auto_answers.py`.)
- EN: *going to* + base verb: *We're going to get*.
- LV: *going to* + pamatforma: *We're going to get*.

## cm-1-020 · She going to look for a new flat in May.
**REWRITE** (instruction only). The readers' *She's looking for a new flat in May* and *She will look …* also fix it. *Keep
*going to** keeps the task on the missing *is*.
- Sentence: `Correct the mistake. Keep *going to*: She going to look for a new flat in May.`
- Accepted (unchanged): `She is going to look for a new flat in May. | She's going to look for a new flat in May.`
- EN / LV unchanged.

## cm-1-021 · Will I open the window? It's very hot in here.
**REWRITE.** *Shall I open the window?* is the first example on the shall card and in the future card, which also shows *✗ Will
I open the window?*. The match task *Shall I open the window? = Yes, please. It's hot in here.* uses the same sentence. The
readers are right that *Can / Could / May I …?* also correct *Will I* (offer or permission, both correct English after *It's
very cold in here*). The task is about the wrong *Will I*, so every modal that fixes it is accepted. *Do you want me to …?*
is a new structure and is not accepted.
- Sentence: `Correct the mistake: Will I turn on the heating? It's very cold in here.`
- Accepted: `Shall I turn on the heating? It's very cold in here. | Should I turn on the heating? It's very cold in here. | Can I turn on the heating? It's very cold in here. | Could I turn on the heating? It's very cold in here. | May I turn on the heating? It's very cold in here.`
- EN: An offer: *Shall I …?* (or *Can I …?*). *Will I turn on …?* asks about the future, not what you can do for someone.
- LV: Piedāvājums: *Shall I …?* (vai *Can I …?*). *Will I turn on …?* jautā par nākotni, nevis piedāvā palīdzību.

## cm-1-022 · Your bag looks heavy. I carry it for you.
**REWRITE.** The answer is almost word for word a wrong option of fu-A22-2a in the same topic and level (*Your bag looks heavy.
I'll carry it.*). The shall card also has *Will I carry your bag?*. The readers are right that *I can …* is a correct offer, so
it is accepted. *Let me …* is a new structure (no subject *I*), and *I'm going to …* does not fit an offer you make now: both
are not accepted.
- Sentence: `Correct the mistake: It's late. I walk you to the bus stop.`
- Accepted: `It's late. I'll walk you to the bus stop. | It's late. I can walk you to the bus stop.` (*I will* is covered by `norm`.)
- EN: An offer you decide on now: *will*, *I'll walk you*. *I can walk you …* is an offer too.
- LV: Piedāvājums, ko izlem tagad: *will*, *I'll walk you*. *I can walk you …* arī ir piedāvājums.
- (The old LV reason *Tulkojot burtiski *es to aiznesu** is left out: Latvian more often says *aiznesīšu* here, so the
  comparison is not sure; rule *a Latvian reason for a mistake that has none*.)

## cm-1-023 · I meet Anna for lunch tomorrow, so I can't help you then.
**REWRITE** (scene only; the mistake and the decision stay). Reader 2's doubt does not hold. Murphy 19 keeps the present simple
for timetables (*The film starts at 8*) and marks it wrong for personal arrangements (*I'm meeting … not I meet*). *I meet
… tomorrow* is the grammar map's typical error for this point. Both readers called *I will meet* "less natural". Murphy 19 and
21 mark it wrong for an arrangement (*not I will meet*), and the map lists *I will meet the dentist at ten* as this point's
error, so it is not accepted. The scene must change: *I'm meeting Anna* is the future card's example (*I'm meeting Anna at
six*) and is also in pc-A22-2a.
- Sentence: `Correct the mistake: I meet a client at nine tomorrow, so I can't take the kids to school.`
- Accepted: `I'm meeting a client at nine tomorrow, so I can't take the kids to school. | I'm going to meet a client at nine tomorrow, so I can't take the kids to school.`
- Answer note on the *going to* answer: EN *Also correct: *going to* is your plan. *I'm meeting a client* says it is already arranged.* · LV *Arī pareizi: *going to* ir tavs plāns. *I'm meeting a client* saka, ka tikšanās jau ir norunāta.*
- EN: An arrangement with a time and another person: present continuous, *I'm meeting a client*.
- LV: Norunāta tikšanās ar laiku un citu cilvēku: Present Continuous, *I'm meeting a client*.

## cm-1-024 · What you are going to do after the course?
**REWRITE** (instruction only). Both readers' *What are you doing after the course?* and *What will you do …?* are correct, but
they change the form instead of the word order. *Keep *going to** makes the word order the only fix.
- Sentence: `Correct the mistake. Keep *going to*: What you are going to do after the course?`
- Accepted (unchanged): `What are you going to do after the course? | After the course, what are you going to do?`
- EN / LV unchanged.

## cm-1-025 · I promise I tell you as soon as I hear any news about the job.
**KEEP.** *I promise I'm going to tell you* (both readers: "less natural") does not fit a promise. Murphy 21 uses *will* for
promises (*I promise I'll …*), and *going to* says you had already decided. The six accepted answers already cover *will*,
*'ll*, *promise to* and both clause orders.

## cm-1-026 · Are you going to sell your old car or you are going to keep it?
**REWRITE** (instruction only). *… or will you keep it?* and *… or are you keeping it?* are correct and fix the word order by
changing the form. *Are you going to sell or keep your old car?* rebuilds the sentence (not accepted). *Keep *going to**
leaves the word order as the fix. The ellipsis answer (*… or keep it?*) still keeps *going to* and stays accepted.
- Sentence: `Correct the mistake. Keep *going to*: Are you going to sell your old car or you are going to keep it?`
- Accepted (unchanged): `Are you going to sell your old car or are you going to keep it? | Are you going to sell your old car or keep it?`
- EN / LV unchanged.

## cm-1-027 · The car won't start this morning, so I took the bus to work.
**REWRITE.** Both readers are right that two clauses can be repaired: *this morning* can be now, so *… so I'll take the bus* is
correct too (the 29 October rule says to replace such a time with an unambiguous one). The answer is also the wont_refuse card's
example and the future card's (*The car wouldn't start this morning*), and the B1.2 order task *my car wouldn't start this
morning so i worked from home*. Not a printer either (C1 *the printer ___ work this morning*, B1.2 *The printer won't print in
colour*). *last night* fixes the past, and *couldn't call* cannot become present. *wouldn't* is on the B1.2 card, and *didn't*
is accepted, so the level is fine. *wasn't charging* is correct English too, so it is accepted with a note.
- Sentence: `Correct the mistake: My phone won't charge last night, so I couldn't call you.`
- Accepted: `My phone wouldn't charge last night, so I couldn't call you. | My phone didn't charge last night, so I couldn't call you. | My phone wasn't charging last night, so I couldn't call you.`
- Answer note on *didn't charge*: EN *Also correct: *didn't charge* only says what happened. *wouldn't charge* says the phone refused, although you tried.* · LV *Arī pareizi: *didn't charge* tikai saka, kas notika. *wouldn't charge* saka, ka telefons atteicās lādēties, lai gan tu mēģināji.*
- Answer note on *wasn't charging*: EN *Also correct: *wasn't charging* describes the night. *wouldn't charge* says the phone refused, although you tried.* · LV *Arī pareizi: *wasn't charging* apraksta, kas notika naktī. *wouldn't charge* saka, ka telefons atteicās lādēties, lai gan tu mēģināji.*
- EN: *won't charge* = it refuses to charge now. *last night* is past: *wouldn't charge*.
- LV: *won't charge* = tas atsakās lādēties tagad. *last night* ir pagātne: *wouldn't charge*.

## cm-1-028 · Hurry up! The film is about starting.
**REWRITE.** It is the same sentence as fu-B12-1a (*Hurry up! The film ___ start.* → *is about to*), same topic and level. The
readers' *is starting*, *is going to start* and *starts soon* are correct, but they give up *about*. *just about to start* is
kind (b) and *about to begin* is kind (c). New scene (not the train: card example *The train is about to leave*; not *Can I
call you back? I …*: an A2.1 present continuous task), and *Keep *about**. *I'm about going* is the map's typical error
(*I'm about leaving*).
- Sentence: `Correct the mistake. Keep *about*: Sorry, I can't talk now. I'm about going into a meeting.`
- Accepted: `Sorry, I can't talk now. I'm about to go into a meeting.` (*I am* is covered by `norm`.)
- EN: *be about to* + base verb = very soon: *I'm about to go into a meeting*.
- LV: *be about to* + pamatforma = tūlīt: *I'm about to go into a meeting*. (Check that the LV pass does not move *to* out of the italics: see the note at the top.)

---

## Unflagged tasks (read briefly)
- **004** *My boss doesn't drinks coffee after lunch*, **005** *Where you usually buy your vegetables?*, **010** *We was very
  tired …*, **011** *I buyed …*, **013** *Robert join our team two months ago*, **014** *I didn't saw …*, **015** *… before
  three years*, **017** *Where did you stayed …*, **018** *… I catched the last bus*: **KEEP.** One mistake each, a real
  learner error at the level (grammar map: 3S / BASE / DO / PAST-FORM / *before two days*), one fix. Nothing in the bank or on
  the cards repeats them.
- **012** *Did you went to the concert on Friday?*: **KEEP.** The past simple card has the same mistake (*Did you went out?*),
  but the answer is a different sentence. The card shows the error type, which is what the task practises.

## Questions for the teacher
None.
