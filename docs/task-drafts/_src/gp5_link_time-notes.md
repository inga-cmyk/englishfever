# Batch 5, point `link_time` (A2.2): notes

Source: `docs/task-drafts/_src/gp5_link_time.py`, topic *However, although, because of, then* (`conj_linkers`), level A2.2.
Grammar: the map gives no Murphy EGiU unit for this point. I checked *before / after* + subject + verb against Murphy 25
(*when / before / after* + present) and *before / after* + *-ing* against Murphy 60 (preposition + *-ing*). *before* + noun is
on the rule card (*before work*).

## Mix (N = 3)
2 word banks and 1 choice (*Which sentence has a mistake?*). The point already has 3 check tasks (2 choices, 1 word order) and
4 use tasks (2 typed gaps, 2 corrections), but no word bank, so a bank was the first thing to add. I left out a word order on
purpose: with two clauses and a time word, the cards almost always give a second sentence that is correct English with another
meaning (*I read before I go to bed* / *I go to bed before I read*), and the comma after a time clause that comes first
cannot be tested with cards. What the existing tasks did not cover was *after* / *before* joining a clause or a noun, and the
map's error *Before go to bed*. The three new tasks cover exactly those.

## Task by task: what the learner must know, and why the wrong options compete
1. Bank: *___ we had dinner, we went for a walk by the sea.* After · Then · After that. The learner must know that *after*
   joins two clauses in one sentence, while *then* / *after that* start a new sentence. *Then we had dinner, we went …* is the
   likely mistake from *pēc tam*. *Before* and *When* are not offered because both would be correct English.
2. Bank: *We always buy popcorn ___ the film.* before · while · when. Only *before* can stand before a bare noun. *while the
   film* and *when the film* are real learner mistakes (Latvian *filmas laikā* / *kad filma*), but here both need subject +
   verb. *after* and *during* are not offered because they would be correct.
3. Choice: *Which sentence has a mistake?* → *Before go to work, I walk the dog.* (the map's typical error: *before* + bare
   verb). The other three are correct and about three different things: *After that,* starting a new sentence; *while* +
   past continuous; a *when* clause first with a comma. The settings are travel, sport, home and work.

## Card lines needed
None. The card has *before / after* + noun / *-ing* / subject + verb, *then / after that*, *while*, and *when*. No task repeats
a card example (*before work* was avoided on purpose).

## Checks
`check_draft.php`: 3 accepted, 0 refused. `option_audit.py`: 0 flagged. I deleted the CSV afterwards. I reworded the Latvian
lines to avoid *abas, jaunu, likt, citu*, which `lv_mark` marked as English.

## Doubts
- Murphy unit numbers (25, 60) are from the 4th/5th edition numbering as I know it; the map itself lists the point as "not a
  Murphy EGiU unit".
- Task 1: someone could argue that *Then we had dinner, we went …* is acceptable in very informal writing. It is a comma
  splice and wrong in standard written English, so I kept it as the believable mistake.
- The existing B1.1 word order *she reads the news while she has breakfast* (conjunctions-1.csv:55) also allows the swapped
  clauses *she has breakfast while she reads the news*. I noticed it but did not change it (outside this task).
