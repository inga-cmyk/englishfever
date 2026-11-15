# Batch 4, point `would_habit` (B1.2): notes of the writer

Source: `docs/task-drafts/_src/gp4_would_habit.py`, topic *Used to and be used to* (`used_to`), level B1.2.
Grammar: Murphy, *English Grammar in Use*, unit 36 (*would* for repeated past actions: *we would all get up early*; not for states: *I used to have a car*, not *I would have*), with unit 18 (*used to* for past habits and states; the Past Simple for one event).

Design rule for the whole set: wherever *would* fits (a repeated action), *used to* and the Past Simple fit too. So they are never a wrong option, and no task asks the learner to choose *would* against them. What the tasks test:
1. *would* is wrong with states (*have, live, know, like, own*): there *used to* / Past Simple is the only answer and *would* + state is the wrong option (14 tasks).
2. *would* + base verb (not *would sang, would to sing, would made*) (5 tasks).
3. *would* / *used to* are not for one event at a given time (*last summer, last month, last weekend*) (3 tasks).
4. Word order of *would* + verb, in sentences that also show the state / action split (3 orders).
No *be* + *would*: *He would be tired after work* is possible English (a repeated temporary state), so *be* is kept out of every wrong option.

## Mix (25, as in the brief)
7 choice, 5 word order, 4 word bank, 1 matching (learning task automatically), 5 typed gap, 3 whole sentence.

## What the learner must know, task by task
Choice
1. *When I lived in Spain, I ___ a little scooter that I rode everywhere.* → *used to have*. *have* (own) is a state: *would have* is the point's mistake; *was having* (state in the continuous) and *use to have* (no -d) are common mistakes. *had* is not offered.
2. *When we were students, we ___ in a tiny flat near the station.* → *used to live*; *would live* (state), *use to live*, *were used to live* (confusion with *be used to*).
3. NOT correct: *We would know all our neighbours when we lived in the village.* The other three are correct and about three different things: *would* + action (grandmother baking), *used to* + state (uncle's hotel), Past Simple for a habit (train to work).
4. Which is correct: *When my children were small, I would sing to them every night.* against *would sang*, *would to sing*, *was used to sing*: the form after *would*.
5. *As a teenager, I ___ spicy food, but now I cook curry every week.* → *didn't use to like*; *wouldn't like* (state), *didn't used to like*, *wasn't used to like*.
6. *Last summer we ___ to Greece for two weeks and loved every minute.* → *went*; *would go* and *used to go* (one event), *have gone* (*last summer*).
7. *My grandparents ___ a farm, and every summer we would help them with the harvest.* → *used to own*; the sentence itself shows *would* with an action, so the learner sees why *would own* is wrong. *were owning*, *use to own*.

Word order
8. *when we lived by the sea we would swim before breakfast* (+ the *when* part last).
9. *my uncle used to be a fisherman and he would get up at four*: the cards *would* and *used to* cannot swap (*my uncle would be a fisherman* is wrong). No other order.
10. *my grandmother would sing old songs while she cooked dinner* (+ *while* part first; + *while my grandmother cooked dinner she would sing old songs*, the swapped people).
11. *on long car journeys my brother and i would play word games* (+ the phrase last).
12. *we used to have a garden where we would grow our own vegetables*: again the swap gives *would have a garden* (wrong).

Word bank (wrong chips are real forms or the common mistakes of this point)
13. *Before I moved here, I ___ a cat that always slept on my laptop.* used to have / would have / was having.
14. *Every August my grandmother ___ jam from the berries we picked in the forest.* would make / would made / would to make.
15. *Before they retired, my parents ___ in a flat in the city centre.* used to live / would live / use to live.
16. *In my first job, my boss ___ ___ us coffee every Monday morning.* would · bring · brought · to: only *would bring*; no chip pair gives another sentence (*brought to us coffee* is wrong).

Matching (learning)
17. *When I was a student, I used to* = *have very long hair.* / *When it snowed, my dad would* = *take us sledging in the park.* / *Before the bridge was built, people would* = *cross the river by ferry.* / *My parents didn't use to* = *like my friends, but now they do.* Swap test: *have very long hair* can follow only *used to* / *didn't use to* (not *would*); *I used to take us* and *people would like my friends, but now they do* fail; *my dad would like my friends, but now they do* fails (*they*). Only one full pairing works.

Typed gap
18. *When I was a student, I ___ a really old car that broke down every week. (have)* → *used to have | had*; *would have* refused (state).
19. *When I worked at the market, I ___ every customer by name. (know)* → *used to know | knew*.
20. *Use *would*: Every Sunday my grandfather ___ us fishing on the lake. (take)* → *would take | 'd take*. Named because *used to take / took* are equally correct; the task is the base form after *would*.
21. *When we were kids, my sister and I ___ for hours about whose turn it was to wash up. (argue)* → *would argue | 'd argue | used to argue | argued* (all correct for a repeated action).
22. *Last month I ___ to Tallinn for a job interview, and I got the job! (go)* → *went* (one event).

Whole sentence
23. *Say it another way with *would*: When I was young, my father used to cook pancakes every Saturday.* → *… my father would cook pancakes every Saturday* (both clause orders).
24. *Correct the mistake: When I was a child, I would have a little garden of my own.* → *used to have* or *had* (both clause orders; the grader also takes the corrected words alone).
25. *Correct the mistake: Last weekend we would go hiking in the mountains.* → *went* (both orders).

## Card lines
The card already has the needed line (watch: *would* + verb for past habits, not for states). Optional, to cover tasks 6, 22 and 25 on the card itself: extend the use line
- EN: *Not for one finished event: use the Past Simple (*We went to Rome last year*, not *used to go* or *would go*).*
- LV: *Ne vienam pabeigtam notikumam: lieto Past Simple (*We went to Rome last year*, nevis *used to go* vai *would go*).*

## Latvian words marked as English (for `LV_BY_FILE`)
galotnes, nevar, pabeigtam, notikumam, daudzas, reizes, likt

## Unsure
- Task 21: *were arguing* is not accepted (past continuous for a childhood habit without *always* is not natural); a reader may raise it.
- Task 3 and task 1: *would know*, *would have* (own) are wrong by Murphy 36; I kept *be* out of every wrong option because *would be* can be correct for a repeated temporary state.
- Checks: `check_draft.php` 25 accepted, 0 refused, 31 typed variants 0 refused; `option_audit.py` 0 flagged; `latvian_lint` and `draft_rules_test` on the file 0 problems; the item gates (except blind / point) run on the rows: no finding.
