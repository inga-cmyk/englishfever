# Usage log: what learners open and press (28 October 2026)

The teacher wanted to see how learners use the app: where they start practice, whether they use the level test, Surprise me, Second Chance or My learning path, and which buttons they press.

## What is recorded

- **Where each session starts** (`psessions.source`): `placement` (level test), `path` (a step on My learning path), `path_check` (the quick check of an untried step below the placement level), `surprise` (Surprise me), `second_chance`, `home_topic` (a topic on Home), `practice_page` (topics chosen on the Practice page), `rule_card` (the Practise button on a rule card). Sessions from before this version have no source; the teacher page shows them as *Practice (before 28 October)*, except the level test, Second Chance and Surprise me, which are known from the session mode.
- **Actions** (`events` table): `page` (Home, Practice, Rules, Leaderboard, Profile, Placement, Summary), `rule_card` (from the Rules page, or `fb-…` under a task), `lang` (the flags), `skip`, `quit`, `review` (looking back at an earlier task), `report`, `sound`, `mood`, `path_step`, `bonus`.
- Only the name of the action, a short detail (a page name or topic id) and the time. Never text the learner typed. Teachers are not logged. At most 2000 actions per learner per day.
- The page sends the actions in small batches every 10 seconds. What is still waiting when the page closes is kept in the browser and sent on the next visit.

## Where to see it

- **Teacher → Usage**: how sessions are started (sessions, learners, answers), what learners open and press, and a table per learner. 7, 30 or 90 days. *Download CSV* gives every action and every session start with the learner's nickname.
- **Research export**: a fourth file, `events.csv`, with the same data for study participants, under their random code (study day, weekday, hour, minute, event, detail; session starts as `session_start` with the source and the number of answers).

## Privacy

The study information text and the privacy text now say that the app records which parts of the app a learner opens and uses. Deleting an account deletes its actions too.
