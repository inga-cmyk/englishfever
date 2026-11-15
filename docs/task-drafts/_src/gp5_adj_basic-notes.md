# Batch 5, point `adj_basic` (A2.1): notes from the writer

Topic: Adjective order (a small old car) (`adj_order`), level A2.1 (the teacher added it on 15 November: prepared tasks only).
Grammar checked against Murphy, *English Grammar in Use*, unit 99 (adjectives before a noun and after *be*; no plural form).
Generator: `docs/task-drafts/_src/gp5_adj_basic.py` (9 calls, no `save()`).

## Mix (N = 9)
2 choice, 2 word order, 2 word bank, 2 typed gap, 1 whole sentence. One choice fewer than the 3-in-10 mix: the point's only
counted task is already a choice (*She has two small boxes.*, B1.1) and it has no *use* task, so the typed tasks keep their full share.
Checks: `check_draft.php` 9 accepted, 0 refused (6 typed variants, 0 refused); `option_audit.py` 0 flagged.
No model sentence is in `app/content/items.json` or `docs/task-drafts/*.csv`. Only A2.1 grammar: present of *be* and *have*, *need*, past of *rent*.

## Each task: what the learner must know, and why the wrong options compete
1. *Choose the correct option: The shops here ___.* are very expensive. A 2 x 2 of the point: *be* missing (*very expensive*), *-s* on the adjective (*are very expensives*), both (*very expensives*).
2. *Put the words in order.* she has a very good job. The adjective (with *very*) goes between *a* and the noun; *a job very good* is the typical mistake. No other order.
3. *Use the words in brackets: I need two ___ for the trip. (bag / big)* big bags. Adjective first, *-s* on the noun only; the brackets give the words in the wrong order, so *bags big* and *bigs bags* are the mistakes the task catches.
4. Bank *We have two ___ ___ in our garden.* big / trees; chips *bigs* (common learner mistake, allowed since 11 November) and *tree* (no *-s* after *two*). *trees big*, *bigs trees*, *big tree* are all wrong; only one combination is right.
5. *Which sentence has a mistake?* *We rented a car small for the week.* The other three are correct and about three different things: adjectives after *be* with *and*, an adjective before a plural noun (*new batteries*), an adjective before a noun after *has*.
6. *Use the words in brackets: My new headphones ___. (comfortable / very / be)* are very comfortable. The learner supplies *are* and keeps the adjective without *-s*; *very* can only stand before the adjective.
7. *Put the words in order.* my grandmother is very active for her age; also *for her age my grandmother is very active* (fronted phrase, said naturally). The adjective after *be* without a noun.
8. Bank *The rooms in this hotel ___ very ___.* are / clean; chips *cleans* (a real verb form and the *-s* mistake) and *have* (*have very clean* is the "adjective as a thing you have" mistake). No other combination is a sentence.
9. *Start with *Our*: We have very nice neighbours.* Our neighbours are very nice. | Our neighbours are nice. The adjective moves from before the noun to after *be* and stays without *-s* (*very nices*). Dropping *very* still shows the point, so it is accepted.

Settings in order: shopping, work, travel, home, mixed, technology, family, travel (hotel), neighbours; no setting twice in a row.

## Card lines needed
None. The card already has *Adjectives have no plural form: two small boxes* and *After be we can use and*. The point's "before the
noun" and "after *be* alone" are only implied by the card's examples. If the lead wants them explicit, one line (EN / LV):
- EN: *An adjective goes before the noun (a good job) or after be (The job is good).*
- LV: *Īpašības vārds stāv pirms lietvārda (a good job) vai aiz be (The job is good).*

## Doubts
- Latvian italics: the italics marker takes *Tulkojot*, *burtiski*, *tikai*, *lielas*, *somas* for English (tasks 3 and 4). These
  words are already in `LV_BY_FILE["gap-points-a2-1.csv"]` except *lielas somas*; the file this point goes into needs
  `Tulkojot burtiski tikai lielas somas` in its `LV_BY_FILE` set (I could not edit `lib.py`).
- The *Tulkojot burtiski* note is only on the plural tasks (3, 4): Latvian adjectives agree in number (*lielas somas*), which really
  causes *bigs bags*. Missing *be* is not a Latvian mistake (*Veikali ir dārgi*), so no note there.
- `latvian_lint.py` and `draft_rules_test.py` were not run on this file (not in the batch 5 check steps).
