# Features and the theory behind them (inventory for the thesis)

Made 22 November 2026 from the code on this branch, following `docs/THESIS-UX-THEORY.md` (the teacher's framework, in Latvian; section 14.1:
mark every proposed function as existing, partly built or proposed, do not invent what the app can do). Function numbers F01-F12 are from
that document. Sources are in `docs/THESIS-LITERATURE.md` (section 12 for the ones added with this framework).

Status: **existing** = built and live; **partly** = something close is built, but not what the framework describes; **proposed** = not built.
Checked in the code only, not yet with learners on a phone: the P1 check (framework section 12) is still to do.

## Overview

| # | Function | Status | What the app has now (where) |
|---|---|---|---|
| F01 | One clear start / continue action | existing | Home shows one main thing to do (the path step or *Continue where you stopped*) with one button, plus three small links (`app.js` home, around line 541). The step can be refused: the learner can choose any topic. |
| F02 | Flexible session length | partly | Lengths are fixed by the entry point: path step 10, *Surprise me* 12, a new learner's first taste 8, rule card 5, Second Chance up to 10 (`Engine::start`, `app.js`). The learner cannot choose a short 3-5 question session. The level test has Quick / Medium / Full. |
| F03 | Saved continue point | existing | `session/resume`: an unfinished session is offered on Home as *Continue where you stopped*; every answer is saved when it is sent. |
| F04 | Clear feedback | existing | Right / wrong with text, *Why* (EN, LV up to B1.2), *Also possible*, Latvian note on typical mistakes, rule card (?), *I don't know*, *Report* on every task (reports go to the teacher; faulty tasks are fixed and the answers marked `unfair_wrong`). Not built: a hint before a second try. |
| F05 | Concrete end of session | existing | Results page: score, the mistakes fixed in this session (`fixed_list`), buttons *Again*, *Harder*, Home; no pressure to start another (`viewSummary`). |
| F06 | Evidence of learning over time | existing | Path states *learned* (10+ different check / use tasks, two days) and *mastered* (3+ days later, three never-seen tasks); mistakes *Fixed* (another task of that kind) and *Locked in* (another day, another task); spaced review of fixed mistakes in Second Chance (`Mistakes::reviewDue`). Same task again is marked `exposure` and left out of learning measures. |
| F07 | Rhythm chosen by the learner | proposed | Only a **daily streak** (`Stats::streak`; the Home line *Practise today to keep your streak alive*). The streak can be hidden per learner as a study condition (`Research::FACTORS`, `cond.streak = off`). No weekly goal, no pause. See `docs/PRACTICE-RHYTHM-COACH.md`. |
| F08 | Concrete start plan ("When I ..., I will ...") | proposed | Nothing. The reminder card asks only for a time. |
| F09 | Reminders the learner controls | partly | *Remind me every day*: the learner picks a time and adds a daily event to their own calendar (.ics or Google Calendar); they control it in their calendar. Daily only; the app sends nothing itself. |
| F10 | Coming back without punishment | partly | *Welcome back* greeting after a gap (2 days, 3-4, a week, weeks, a month; A2 and B1+ versions, humorous, never more often than every 3 hours, never during practice) with *This week: N days · M min*; Second Chance (own mistakes, each in a new sentence). Progress is never lost after a gap. But the streak resets to 0 and some lines speak of *missing* the learner, which can read as guilt for a planned break. |
| F11 | Manageable review after a break | partly | Second Chance takes at most 1-2 due reviews and fills up to 10 tasks; review is mixed into path steps (60 / 25 / 15). No "debt" is shown. Not checked: how much review piles up after a long break. |
| F12 | Two separate views: regularity and performance | partly | Separate already: streak and the 7-day minutes bar (regularity), *My level*, path states and Learning evidence (performance); more visits do not raise the level. Missing: regularity against the learner's own plan; *My level* says when there are too few answers (under 10) but its predictions are too extreme (`docs/THESIS-ASSESSMENT.md`). |

## Link form (framework section 13), one record per existing function

The teacher fills in *Learner need* and *Author's solution* with her own words; the agent filled in what the code shows. Dates are from
`docs/CHANGELOG-practice-app.md` and the code comments (teacher decisions).

### F01 One next step on Home
- **Function and version:** Home main card with one button; the path step or *Continue*. Live since the end of October 2026; *less is more* rule 6 November.
- **Learner need:** (teacher)
- **Theory:** COM-B capability and opportunity (Michie et al., 2011); perceived ease of use (Davis, 1989); too many options can stop choice (Iyengar & Lepper, 2000; but see Scheibehenne et al., 2010).
- **Author's solution:** (teacher) the grammar map and the path choose the step; the learner can still choose any topic.
- **Triggered by:** the learning path state; an unfinished session comes first. Without data: the level test or the first taste.
- **Learner control:** other topics, *Surprise me*, Second Chance.
- **Expected mechanism:** fewer decisions before the first answer.
- **Evaluation:** time and clicks from opening the app to the first answer (events `page`, `session_start`); sessions by `source`.
- **Limits:** the events show where a session started, not why the learner chose it.

### F03 Continue where you stopped
- **Function and version:** `session/resume`, Home *Continue*.
- **Theory:** COM-B opportunity; the goal-gradient effect (Kivetz et al., 2006): a started task pulls towards its end.
- **Triggered by:** a session with answers left. **Control:** the learner can start something else.
- **Evaluation:** share of resumed sessions that are finished. **Limits:** a session left open on another device.

### F04 Feedback after every answer
- **Function and version:** *Why* EN / LV, *Also possible*, Latvian notes, rule card, *Report*; Latvian explanations since early November.
- **Theory:** formative feedback (Shute, 2008); feedback about the task, not the person (Hattie & Timperley, 2007; Kluger & DeNisi, 1996); SDT competence (Ryan & Deci, 2020).
- **Author's solution:** (teacher) her explanations, the Latvian notes where Latvian causes the mistake, the rule that a correct form is never marked wrong.
- **Evaluation:** `feedback_seconds` (reading time), `rule_card_before`, later success on a different task of the same point (*Fixed*).
- **Limits:** reading time is not understanding.

### F05 Results page
- **Theory:** peak-end (Kahneman et al., 1993); small wins and competence (Bandura, 1977).
- **Shows:** only what happened in the session (score, fixed mistakes). **Control:** Home, again, harder.
- **Evaluation:** which button is chosen (`source = summary`).

### F06 Learned, mastered, fixed, locked in
- **Theory:** spaced practice (Cepeda et al., 2006; Kim & Webb, 2022), retrieval practice (Roediger & Karpicke, 2006), mixed practice (Nakata & Suzuki, 2019), mastery learning (Bloom, 1968).
- **Author's solution:** (teacher) the rule *10 different tasks, two days, recognise + use + one typed answer*; *mastered* only with never-seen tasks.
- **Evaluation:** *Locked in* and *mastered* rates; `exposure = 1` answers only.
- **Limits:** item difficulty not calibrated yet (median 2 answers per item).

### F09, F10, F11 (partly built): see `docs/PRACTICE-RHYTHM-COACH.md`, which proposes how to complete them together with F07 and F08.

## Data for the framework's section 10 (compared with the research export)

| Framework definition | In the export now | Gap |
|---|---|---|
| Practice day = a day with a real answer | `active_days`, `days.csv` (answers > 0) | none |
| Completed session | `sessions` = sessions with at least one answer | no *finished* flag per session; `quit` event exists |
| Plan realisation | nothing | needs the plan with its versions (F07) |
| Return after a set break | can be computed from `days.csv` | no fixed break defined yet (proposal: 7 days, and 14 days as the framework suggests) |
| Delayed performance | `exposure`, *Locked in*, *mastered* (app) | not in the export as a separate measure |
| Support shown and accepted | `welcome` and `reminder` are tracked in the app | not in `events.csv` of the research export |
| Self-report (obstacle, readiness, usefulness) | `mood` event only | proposed (F07 obstacle question) |

Changing the export is a change to the research data: it gets a dated line in `docs/RESEARCH-DATA-PLAN.md` when it is built.
