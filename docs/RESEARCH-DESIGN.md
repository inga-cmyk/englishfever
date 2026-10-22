# Learning study: what keeps people coming back to practise

Notes for the thesis. How the practice app supports a study, what it can and cannot tell you, and what to settle before the first participant. How to switch it on is in [PRACTICE-APP.md](PRACTICE-APP.md), section *Learning study*.

## The question

What makes adult learners return and keep a regular practice habit, and do two common app features (a daily streak counter and a leaderboard) help?

## What the app records (per participant, from the moment of consent)

| Kind | Variable (file) |
|---|---|
| **Outcomes** | `active_days`, `weeks_active`, `longest_streak`, `active_day1/7/30`, `first_active_day`, `last_active_day`, `observed_days` (`people.csv`); active days over time (`days.csv`); `sessions` |
| **Engagement detail** | answers, seconds, XP per day (`days.csv`); hour and weekday of every answer, topic, level, thinking level, correct, seconds (`answers.csv`) |
| **Starting point** | `placement_level` (latest placement after consent), `join_week`, `consent_week` |
| **Chosen by the learner (not randomised)** | `explanations_lv` (Latvian explanations), `avatar_chosen`, `board_opt_in`, `sessions_smart` (the "Surprise me" button) |
| **Randomised** | `cond_streak`, `cond_leaderboard` ("on" = the normal app, "off" = hidden) |

A day counts as **active** when at least one task was answered. A day that is missing from `days.csv` means no activity. `observed_days` is the number of days since consent: use it so that a late joiner is not mistaken for someone who dropped out.

## The experiment

Two factors, **randomised independently** among people who joined (a 2 × 2 design):

- **Streak counter** on or off. "Off" hides the counter, the streak tile and the streak wording. The streak is still counted.
- **Leaderboard** on or off. "Off" hides the tab and the setting, and the person is not listed on the board.

Allocation is in shuffled blocks of four per factor (two of each), made when the person joins; the order inside a block comes from a keyed hash, so it can be reproduced but not guessed. The allocation order is stored (`conditions.seq`) and the groups stay the same size to within one person.

Everything else (avatar, language, topic choice, "Surprise me") is chosen by the learner, so differences there are **correlations**, not effects.

Possible hypotheses to settle *before* you look at data (write them down, ideally pre-register them): a visible streak raises the share who return on the next days and the number of active weeks (commitment, loss aversion); a leaderboard raises activity for some and lowers it for others (social comparison), so look at whether the effect depends on level or on activity in the first week.

## How many people

Rough, for a single comparison of two proportions with 80 % power and α = 0.05:

| Difference you want to detect | People per group |
|---|---|
| 30 % → 50 % still active at day 30 | about 90 |
| 20 % → 40 % | about 80 |
| 30 % → 40 % | about 350 |

In a 2 × 2 design each main effect compares half of all participants with the other half, so double the group size for the total. With fewer people, only large effects can be found; say so, and report effect sizes with confidence intervals rather than only p-values. A pilot with 20–30 people is still useful for checking that the whole chain works and for descriptive results.

## Analysis ideas

- **Retention:** logistic regression of `active_day7` / `active_day30` on `cond_streak * cond_leaderboard`, restricted to people with enough `observed_days`; add `placement_level` as a covariate.
- **Time to last activity:** survival analysis (Kaplan–Meier, Cox regression) with `observed_days` as the censoring time.
- **Habit strength:** count of `weeks_active` (Poisson or negative binomial); within-person patterns from `days.csv` (regularity, gaps), and time of day from `answers.csv`.
- **Descriptive:** what the people who keep going have in common (level, topics, "Surprise me", Latvian explanations, time of day); label this as exploratory.

## Limits to state in the paper

- **Self-selection:** people who register and agree to take part are already motivated; randomisation holds among them, not for learners in general.
- **Contamination:** participants may talk to each other or see each other's screens. The leaderboard "off" group also makes the board smaller for everyone else.
- **Small and short:** a few weeks of data cannot show a lasting habit. The habit literature often cites weeks to months; check the sources (for example Lally and colleagues, 2010) rather than relying on a number from memory.
- **One teacher, one context:** a Latvian grammar app run by one teacher.
- **Recorded time** is time the page was open and active, not learning.

## Before the first participant (checklist)

1. **Ethics approval** from your university, with the information sheet and consent wording. Replace the default text with the approved wording (`research_text`, `research_text_lv`) and add the information sheet link (`research_info_url`).
2. **Minors.** The invitation asks the person to confirm they are 18 or older, or that a parent or guardian agrees. That is a confirmation, not a check. If younger learners will take part, your ethics board will tell you what is needed.
3. **Privacy policy** on the website: add the paragraph from PRACTICE-APP.md and the researcher's details.
4. **Retention:** decide how long the data is kept (at least until the thesis is assessed) and who may open the exports. Teachers can open the Students page, including the exports; the files have no names but are *pseudonymised, not anonymous*.
5. **Test with a colleague** (join, answer, leave, download) and read `readme.txt`.
6. **Start the clock:** switch on `research_enabled` and `experiments`; export weekly and keep dated copies.
7. **After the study:** consider telling participants which features were hidden for some of them, and switch `experiments` back to `[]`.
