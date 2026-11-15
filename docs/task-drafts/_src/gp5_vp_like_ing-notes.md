# gp5_vp_like_ing: notes (batch 5, A2.1, 9 tasks)

Point `vp_like_ing` "Like, love, hate + -ing; want + to". Topic *Verb patterns* (`verb_patterns`), level A2.1 (new level for the topic, prepared tasks only, teacher 15 November). Already there: 1 check task (word bank *She likes ___ in the garden.*, A2.2). No use tasks.

## Mix (9) and why
- 2 choice (1 gap, 1 *Which sentence has a mistake?*), 1 word order, 1 word bank, 3 typed gaps, 2 whole sentences.
- That gives 5 use tasks and 4 check tasks. With the existing check task the point ends at 5 check and 5 use.
- Reasons for leaving the default mix. The point had no use tasks, so most of the new ones are typed (brief 5, point 2). There is only one word order. At A2.1 most *like / want* orders give the -ing or *to* form on the cards, so putting them in order does not test the point. The one I kept makes the learner place *to* (*want to come*, not the common *want come to*).

## Murphy
Unit 53 (verb + -ing), unit 54 (verb + to), unit 58 (*like / love / hate* + -ing or *to*, almost the same meaning). So *to* + verb is never a wrong option after *like / love / hate*, and every typed gap after them accepts both forms. After *want*, only *to* + base verb is right.

## Per task: what the learner must know, and why the wrong options compete
1. *My brother hates ___ early.* → *getting up*. They must know that *hate* is followed by -ing. *get up* is the typical mistake carried over from Latvian (*I like cook*). *gets up* is agreement with *brother*. *to getting up* mixes the two patterns. *to get up* is correct, so it is not an option.
2. *My dad loves ___ old films. (watch)* → *watching | to watch*. They must not write the base verb *watch* or *watches* after *loves*. Both correct forms are accepted.
3. Order *do you want to come with us*. *to* must go straight after *want* and before *come*. The learner mistake *want come to* (or *with us to come*) is ruled out. No other order is correct, and the statement form is impossible with *do*.
4. *I want ___ my own café one day. (open)* → *to open*. Typical mistakes are *want open* and *want opening*. *want* + *to* is the only correct pattern.
5. Word bank *My parents want ___ ___ a dog.* (to · get · getting · gets) → *to / get*. The wrong chips build the real mistakes *to getting* and *to gets* (and *getting* / *gets* on their own). Only one combination of two chips is correct.
6. *Which sentence has a mistake?* → *Ben likes play tennis on Sundays.* (base verb after *likes*: the map's typical error). The three correct sentences are about three different things: *want to visit* (travel), *love walking* (hobby), *like working from home* (work, question).
7. *Does your partner like ___ computer games? (play)* → *playing | to play*. This is the same pattern in a question with *does*. A learner who writes *plays* (agreement with *partner*) or *play* is wrong.
8. *Correct the mistake: Maria wants take a taxi to the airport.* → *Maria wants to take a taxi to the airport.* The learner must add *to*. The grader also accepts the corrected words alone.
9. *Say it another way with *love*: Cooking is my favourite hobby.* → *I love cooking. | I love to cook.* (with *really* or *very much* accepted too). The learner must build *love* + -ing / *to* themselves, and the answer is not given. Any form with the base verb (*I love cook*) is refused.

Settings, in order: daily routine, family / films, social plans, work, home / pets, mixed, technology, travel, hobbies. Every sentence is 5 to 8 words (task 8 has 9).

## Card lines needed
None. The card already has *like, love, hate … + -ing ≈ to* and *want … + to + base verb* in the `v2.choice` table, and *I want going home* among the mistakes. No task repeats a card example.

## Latvian
Two explanations have the *Tulkojot burtiski…* note (tasks 6 and 8). Latvian uses the infinitive after *patīk* and *gribu* (*Benam patīk spēlēt*, *gribu iet*), and that leads to the base verb without *to*. The italics marker treats some ASCII Latvian words in these notes as English. In the test CSV it printed *Tulkojot burtiski Benam\** and *Tulkojot burtiski gribu\**. When this file goes into the batch CSV, add `Tulkojot burtiski Benam gribu iet` to that file's `LV_BY_FILE` entry in `lib.py` (as was done for `gap-points-a2-1.csv`). The marker also leaves the Latvian-looking *to* in *(vai to + pamatforma)* plain.

## Doubts
- Task 1, wrong option *to getting up*: it is a real learner mix, but less common than the other two. *got up* would be a form nobody writes after *hates*, so I did not use it.
- The order task (3) shows only *Put the words in order.* after `plain()`, although I wrote *… to make a question*. The answer is a question with *do* and has no statement reading, so this is harmless.
- Task 9: other paraphrases with *love* are possible (*I love my hobby: cooking.*). I accepted the natural ones with -ing and *to*. A reader may find another one.
