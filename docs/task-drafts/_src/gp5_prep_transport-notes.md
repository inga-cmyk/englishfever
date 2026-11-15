# Batch 5, point `prep_transport` (A2.2), topic Prepositions of time and place (in, on, at): notes

**N = 7.** The point already has 2 check tasks (choice *I always read a book ___ the bus.*; bank *I was ___ the bus when you called, and now I'm ___ a taxi.*) and 1 use task (*Correct the mistake: I saw her in the train.*). With these 7 it reaches 10.

**Murphy:** *English Grammar in Use*, unit 128 in the map's numbering (*by car, by bus, by train*: no article; *in my car*, *on the bus* when there is *a / the / my*; *on foot*), and the in / on / at unit the map gives as 127 (*in a car / taxi*, *on a bus / train / plane*). Doubt: I could not open Murphy here, so the unit numbers follow `docs/GRAMMAR-MAP.md`; the grammar itself is standard and the same in every edition.

**Mix (out of 7):** 2 choice, 2 word bank, 2 typed gap, 1 whole sentence, **no word order**. Reason: the point is one preposition before a vehicle; in a word order the cards would only be put in their one possible place (*we went to the airport in a taxi*), so it would not test *by / in / on* (brief, point 3: use a word order only where the order needs the point). The two order slots went to one more bank and one more typed gap. The point had only 1 use task, so 3 of the 7 are written (2 gaps, 1 sentence).

**Stays on transport:** nothing about *to / into / through / arrive in / at* or *get in / get on* (that is `prep_move`, written at the same time). No sentence with *arrive*.

## Task by task: what the learner must know, and why the wrong options compete
1. Choice *Is it cheaper to travel to Tallinn ___ bus?* (by / with / on / in): *by* + vehicle with no article. *with bus* is the Latvian calque (*ar autobusu*); *on bus* and *in bus* are the learner who knows *on the bus* but forgets that it needs the article. No situation, none needed.
2. *Which sentence has a mistake?* *My daughter goes to school by foot.*: *on foot*, the most common mistake of this point (*by* is generalised from *by car / by bus*). The three correct sentences are about three different things: *by train* (no article), *on the plane*, *in his car*.
3. Bank *Today I'm going to work ___ Tom's car.* (in / by / on / with): with a possessive in front of the noun only *in* is possible; *by Tom's car* is the typical *by my car* mistake, *on* is the public-transport preposition put on a car, *with* the calque. *Today* makes the present continuous natural (a one-off arrangement).
4. Bank *I met an old friend ___ the tram yesterday.* (on / in / at): *on* + tram (public transport). *in the tram* is the Latvian *tramvajā*; *at the tram* the learner who thinks of a stop. I did not put *by* in this bank: *by the tram* (= next to it) is correct English.
5. Typed *Let's go to the museum ___ foot.* → *on*: only *on* fits; the mistake is *by*. Own instruction *Write the missing word:* so that `lib.gp` does not add the topic's *Complete with in, on or at* (which would be a wrong hint here).
6. Typed *We went to the airport ___ a taxi.* → *in*: the article in the sentence rules out *by* (*by taxi* but *in a taxi*); *on a taxi* is wrong. Only *in*.
7. Sentence *Correct the mistake: I go to work by my car.* → *I go to work in my car.* | *I go to work by car.* Both are corrections of the one mistake (*by* + *my*), so both are accepted; nothing else is a correction.

Settings in order: travel, family / school, work, friends, leisure, travel, work (no setting twice in a row except travel / work separated by others). Every sentence was searched in `app/content/items.json` and `docs/task-drafts/*.csv`: none exists.

## Card lines needed
The card has only *in a car or taxi, but on public transport*. The point also needs *by* + no article and *on foot*. Suggested line under **watch** (and in `v2.watch`):
- EN: *[[by]] + transport with no a / the / my (*by car, by bus, by train*), but *[[in]] my car, [[on]] the bus*. Walking: *[[on]] foot*, not *by foot*: *I go to work [[by]] bus, but today I'm [[on]] foot.*
- LV: *[[by]]* + transportlīdzeklis bez *a / the / my* (*by car, by bus, by train*), bet *[[in]] my car, [[on]] the bus*. Kājām = *[[on]] foot*, nevis *by foot*: *I go to work [[by]] bus, but today I'm [[on]] foot.*

## Doubts
- *in the tram* / *in the train*: some British speakers say it; Murphy and the card teach *on*, and the existing task (*I saw her in the train*) already marks *in* wrong, so I followed that. A blind reader may flag task 4.
- Latvian explanations are worded with words that `lib.py` / `italics.py` already know (*taksometrā*, *tramvajā*, *ar autobusu*), because plain ASCII Latvian words such as *taksometrs*, *tramvajs* would be marked as English examples. The *with bus* note starts *Latviski …, bet angliski …* like the existing transport tasks, not *Tulkojot burtiski*, for the same reason.
- Checks: `check_draft.php` 7 accepted, 0 refused; `option_audit.py` 0 flagged; the pending CSV was deleted.
