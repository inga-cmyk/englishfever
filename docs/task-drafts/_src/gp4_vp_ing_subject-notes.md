# Batch 4, point `vp_ing_subject` (A2.2): -ing as the subject

Generator: `docs/task-drafts/_src/gp4_vp_ing_subject.py` (topic *Verb patterns*, 25 tasks).
Checks run: `check_draft.php` 25 accepted, 0 refused (14 typed variants); `option_audit.py` 0 flagged; `latvian_lint.py` and
`draft_rules_test.py` (temporary copies on the one file) 0 problems.

## Mix
7 choice, 5 word order, 4 word bank, 1 matching (learning), 5 typed gap, 3 whole sentence: the mix of the brief, no change.
Two kinds of knowledge are tested, about half each: (a) the form at the start is *-ing* (not the base verb, not *to + -ing*);
(b) the verb after the activity is singular (*is, saves, does, doesn't*), also in questions and negatives.

## Sources
Murphy has no unit for this point. Used: Murphy 53 (verb + -ing: the -ing form), 60 (preposition + -ing: the -ing form used
like a noun), 65 (adjective + to: *It's good to swim*, the other correct way to say it). *To learn a language takes time* is
correct but formal and rare (Swan, *Practical English Usage*, infinitive as subject: possible, but *It … to* or *-ing* is
usual). Consequences: *to + verb* is never a wrong option, and every typed gap at the start of a statement accepts it.
Questions (*Is ___ a car expensive?*, *Why is ___ so popular?*) rule it out (*Is to rent …?* is not English), so those keys
hold only *-ing*. The wrong option *To + -ing* (*To walking*) is the typical mistake from the map (*To smoking is not allowed*).
Sentences with *reading books* as subject are avoided on purpose: *reading books* is also a noun (books for learning to read),
so *Reading books are …* can be correct.

## Task by task: what the learner must know, and why the wrong options compete
Choice
1. *___ is good for your heart.* Walking / Walk / To walking: the start needs -ing; *Walk* is the Latvian infinitive copied
   (*Staigāt ir veselīgi*), *To walking* is the mixed form. *To walk* is not offered (correct).
2. *Meeting new people ___ fun.* is / are / were: the activity is one thing; *people* pulls towards *are / were*.
3. *___ a new language takes time.* Learning / Learn / To learning: as 1 (*Mācīties svešvalodu …*). *To learn* not offered.
4. *Booking flights early ___ money.* saves / save / saving: singular verb; *flights* pulls to *save*, *saving* is the -ing echo.
5. *Which sentence is correct?* Cooking relaxes me after work / Cook … / Cooking relax … / To cooking …: one wrong form each,
   all three are the typical errors of the point.
6. *___ long hours makes me tired.* Working / Work / To working: as 1.
7. *Which sentence is NOT correct?* *Watching the news make me sad.* (agreement; *news* looks plural) against three correct
   sentences on three different things (driving at night, a question about parking at a hotel, learning to cook).

Word order (all *Put the words in order.*; no second natural order was found)
8. cycling to work saves me money. 9. travelling alone is not always easy. 10. playing the guitar helps me relax.
11. is learning english hard for you (*to make a question*; the statement is not accepted, the instruction asks for a question).
12. charging my phone takes two hours.
The learner must put the -ing activity first as one block and the singular verb after it.

Word bank
13. *___ is my favourite way to relax.* Reading / Read / To reading.
14. *Riding a bike ___ me fit.* keeps / keep / keeping (*bike* is singular, but *keep* is the mistake when the learner sees
    *riding* as "the verb"; *keeping* the -ing echo).
15. *___ ___ English help you at work?* Does speaking / Do / speak: *Do speaking*, *Does speak*, *Do speak* are all wrong; only
    one combination is English.
16. *___ ___ not allowed in this lake.* Swimming is / Swim / are: the sign sentence; *Swimming are* and *Swim is* are wrong.

Matching (learning task)
17. Brushing your teeth twice a day = keeps them healthy; Wearing a helmet on a bike = protects your head; Speaking English
    well = helps you find a good job; Booking a hotel early = makes it cheaper. Every swap of two endings was read: none makes
    sense (*them* needs *teeth*, *it cheaper* needs something you pay for). It is matched by meaning, so it is a learning task
    only, as matching always is.

Typed gap
18. *Is ___ a car expensive in Riga? (rent)* renting only (*Is to rent …?* is not English).
19. *___ late at night is bad for you. (eat)* Eating | To eat.
20. *Why is ___ so popular in Denmark? (cycle)* cycling only.
21. *___ to music helps me work. (listen)* Listening | To listen.
22. *Getting up early ___ never easy for me. (be)* is | was: any singular form is right; the task is about *are*.
    (*has been* cannot fit the gap before *never*.)

Whole sentence
23. *Make it negative: Flying makes me nervous.* → Flying doesn't make me nervous. (*doesn't*, not *don't*).
24. *Make a yes/no question: Living in a big city is expensive.* → Is living in a big city expensive? | Is living expensive
    in a big city? (the whole activity stays together after *Is*).
25. *Make a yes/no question: Using this app saves you time.* → Does using this app save you time? (*Does*, base verb).

Settings rotate: health, relationships, learning, travel, hobbies, work, media, technology; no two neighbours share one.
Every model sentence was searched in `app/content/items.json` and `docs/task-drafts/*.csv`: none exists. The one near scene,
*wear a seat belt … It is the law* (`modal-verbs-1.csv`), was avoided (the matching uses a helmet). No overlap with
`gp4_vp_go_ing.py` (same topic and level).

## Card lines needed (the `verb_patterns` card says nothing about this point)
Add one "When we use it" block to `verb_patterns` in `app/authoring/cards2_rest.py` (and the same in `cards2_a2.py`), after the
*stop, remember, forget, try* block:

EN:
```python
{"t": "*-ing* at the start: the activity is the subject",
 "ex": ["[[Swimming]] is good for you.", "[[Learning]] a language takes time.",
        "Watching old films [[is]] relaxing. (one activity: *is*, not *are*)"]}
```
LV:
```python
{"t": "*-ing* teikuma sākumā: aktivitāte ir teikuma priekšmets",
 "ex": ["[[Swimming]] is good for you.", "[[Learning]] a language takes time.",
        "Watching old films [[is]] relaxing. (viena aktivitāte: *is*, nevis *are*)"]}
```
Optional, if the block may carry a note: EN *"To learn a language takes time" is also correct, but formal.* /
LV *"To learn a language takes time" arī ir pareizi, bet tas ir oficiālāk.* The older `rule` lists (`form`) could take
EN *-ing as the subject: Swimming is good for you. Learning a language takes time.* / LV *-ing forma kā teikuma priekšmets:
Swimming is good for you. Learning a language takes time.*

## Doubts and things for the lead
- `Tulkojot burtiski` (tasks 1 and 3) is marked as English by `italics.lv_mark`, as in the published files that use it. If it
  should stay plain, add `tulkojot burtiski` to `LV_BY_FILE` for the file name this batch is saved under. Every other Latvian
  word was chosen so that it is read as Latvian (*aktivitāte* instead of *nodarbe*, which the marker takes for English); if
  Inga prefers *nodarbe*, add `nodarbe nodarbi nodarbei` to `LV_BY_FILE` and change the helper texts.
- Word orders with *is* (9, 11 has the question instruction) can also be turned into a question with the same cards (*is travelling alone
  not always easy*); as in the house style, that order is not accepted (the instruction gives no question).
- Task 23: *Flying never makes me nervous* is negative in meaning; it is not accepted (the instruction asks for the negative
  of the same sentence). Readers may list it.
- Task 24: *Is living expensive in a big city?* is accepted as a correct but less usual order.
