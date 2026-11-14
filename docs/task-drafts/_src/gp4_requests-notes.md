# Batch 4, point `requests` (A2.2), topic Modal verbs (`modal_verbs`)

Source file: `docs/task-drafts/_src/gp4_requests.py` (25 calls, no `save()`).
Grammar: Murphy unit 37 (A asking people to do things: *Can / Could you…?*; B asking for things: *Can / Could I have…?*;
C asking to do things: *Can / Could / May I…?*, *may* more formal; answers *Yes, of course / Sure / Go ahead*).
*Would you…?* as a request: Murphy unit 36 (*Would you please be quiet?*). Left out on purpose: *Would you mind + -ing*,
*Do you mind if* (B1), *Would you like* (point `would_like`), *Shall I* (point `shall`).

## Mix (as in the brief)
7 choice, 5 word order, 4 word bank, 1 matching (learning), 5 typed gap, 3 whole sentence.
No task has the modal open on its own (*___ you help me?*): the choices offer only one fitting modal, the typed gaps are
the verb after the modal, the person (*I*) or *go ahead*.

## What the learner must know, and why the wrong options compete
Choice
1. *Could you ___ the window, please?* open / to open / opening / opens: base verb after *could*; *to*, *-ing*, *-s* are the typical errors.
2. *Would you check my email, please?* vs *to check / checking / checked*: base verb after *would*.
3. NOT correct: *May you help me with this form?*; the other three are *May I* (permission), *Could you* (request), *Can I* (permission). *May* only with *I*.
4. *Can I ___ a coffee and a croissant, please?* have / to have / having: asking for things, *Can I have*.
5. *Can I borrow your pen…?* vs *Can you borrow me…*, *Can I to borrow…*, *Can I lend…*: who does it (I borrow / you lend) and the base verb.
6. *May I see your passport, please?* vs *May I to see*, *May I seeing*, *May you show me*: *May I* + base verb; no *May you*.
7. *Can you give me a lift to work?* vs *Do you can…*, *Can you to give…*, *Can you giving…*: no *do* with *can*; base verb.

Typed gap
8. *Could you ___ this word to me? (explain)* → explain: no *to explain*.
9. *Can ___ borrow your charger? Mine is at home.* → I | we: *Can I* = I do it; *you* gives nonsense (your own charger). *we* accepted.
10. *Would you ___ quiet, please? I'm on the phone. (be)* → be: base verb *be*, not *are / to be*.
11. *'Can I take a photo of your garden?' 'Yes, go ___.'* → ahead | on (*go on* as a yes is also correct British English).
12. *Could your sister ___ me to the airport tomorrow? (take)* → take: no *-s* with a third-person subject after *could*.

Whole sentence
13. *Start with *Could you*: Please wait here.*: turn an order into a request; *please* in any position and *for me* accepted.
14. *Start with *May I*: I want to ask you a question.*: *May I* + base verb; with or without *you*, *please* in any position.
15. *Say it another way with *Can I*: Can you lend me some money?*: you lend → I borrow (with or without *from you*, *please*).

Word order (lib `od()` turns the instruction into *Put the words in order.* and accepts the statement, so each sentence was chosen so that the statement is natural too)
16. *can i pay by card* (also *i can pay by card*); 17. *could you speak more slowly* (also *you could speak more slowly*; I left out *please* because *you could speak more slowly please* is not natural); 18. *may i sit next to you*; 19. *can you send me the link*; 20. *could you help me with my bags* (I first had *would you help me…*, but *you would help me with my bags* on its own is not natural).

Word bank
21. *Could you ___ me your notes from the lesson?* lend / borrow / to lend: *borrow me* is the classic mistake.
22. *Can I ___ your bike this afternoon?* use / to use / using.
23. *Would you ___ me a favour?* do / to do / doing.
24. *___ you ___ the door, please?* Would · close · May · to close: only *Would + close*; *May you* and *to close* are mistakes of this point. No other chip pair is correct.

Matching (learning)
25. *Could you lend* + *me your charger?* / *Can I borrow* + *your umbrella?* / *Would you help* + *me with this bag?* / *May I* + *come in?*. Swap test: every swap of two right sides breaks at least one sentence (*Can I borrow me your charger*, *Would you help your umbrella*, *May I me with this bag*…).

Settings: home, work, an office form, a café, learning, travel, the commute, technology, hobbies, relationships. Not the same setting twice in a row.
Duplicates: every model sentence was searched in `app/content/items.json` and `docs/task-drafts/*.csv`. None found (only unrelated sentences share a phrase: *Please be quiet. I ___ to concentrate.*, *Please wait here* in a reported-speech task).

## Card lines needed (modal_verbs card has only *Could you…? / Can you…?* and *Can I sit here?*)
The tasks also use *would* (requests), *could I* and *may I* (permission), *Can I have* and *borrow / lend*. Proposed changes, within the card's style (3 "uses" blocks and at most 3 "watch" points, so I extend a block instead of adding one):
- uses block "Polite requests" → title EN *Polite requests and permission* / LV *Pieklājīgi lūgumi un atļauja*;
  `s`: *Can you…? Could you…? Would you…? Can I…? Could I…? May I…?*;
  `ex` EN = LV: *[[Could]] you help me, please?* · *[[May]] I come in?*
- use line (EN): *can / could / would you*: a request (*Could you help me?*); *can / could / may I*: asking for permission (*May I come in?*), *may* is more formal.
  LV: *can / could / would you*: lūgums (*Could you help me?*); *can / could / may I*: atļaujas lūgšana (*May I come in?*), *may* ir oficiālāks.
- watch line (EN): *Can I…?* = I do it, *Can you…?* = you do it: *Can I [[borrow]] your pen? Can you [[lend]] me your pen?* *May* only with *I / we*: not *May you help me?*
  LV: *Can I…?* = to daru es, *Can you…?* = to dara otrs: *Can I [[borrow]] your pen? Can you [[lend]] me your pen?* *May* tikai ar *I / we*: nevis *May you help me?*

## Latvian marking
`aizdodat` (Latvian "you lend", in the explanation of tasks 5, 15 and 21) is marked as English by `italics.lv_mark`. Please add it to `LV_BY_FILE["<final name>.csv"]` in `_src/lib.py` (I may not edit lib.py). `latvian_lint.py` passes either way. *bez to* stays unmarked, as in the approved `a2-rel-might-1.csv`.

## Doubts
- Task 11: *go ahead | on*. A reader may also suggest *Sure*-type answers, but the gap is fixed after *go*. If the lead thinks *go on* sounds too casual as permission, keep it accepted anyway (it is correct).
- Task 9: *we* is accepted (*Can we borrow your charger? Mine is at home.* is a little odd but possible).
- Word orders accept the statement (lib behaviour), so the order tasks check word order and the base verb more than the request itself.
- Murphy unit numbers are from memory of the 4th/5th edition (37 requests, permission; 36 *would*). Please check against the copy you have.
- *borrow / lend* is in 5 tasks (5, 9, 15, 21, 25). That is the clearest *I vs you* contrast the lead named, but it is a vocabulary pair. If that is too many, task 21 can be changed to *Could you ___ me with this box?* help / to help / helping.
