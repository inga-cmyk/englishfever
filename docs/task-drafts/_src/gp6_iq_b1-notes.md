# Indirect questions B1: demote the easy tasks, write meaningful ones (21 November)

Teacher, 21 November: "Indirect questions at B1 are probably too easy. In places the answer is given away. We need meaningful
tasks with understandable instructions that make the learner think." Learners were right in 93% of answers. Grammar: Murphy
unit 50 (Do you know where …? / Could you tell me if …?), unit 13 for *Where did you buy it?* (details of a finished past event:
past simple). Every task uses only what the ind_polite card teaches: statement order after the frame, no *do / does / did*,
*if / whether* for yes/no, a full stop after *I wonder / I'd like to know*, no tense change.

## Files

| File | What |
|---|---|
| `_src/gp6_iq_b1.py` | **new**: 24 check / use tasks, 12 B1.1 + 12 B1.2. No `save()`: add it to a batch generator (as `gap_fill_a2.py` imports the `gp5_*` modules). It patches `lib.plain` so that *Put the words in order to make a question.* stays (the same patch as `gap_fill_a2.py`). |
| `_src/gp6_iq_b1-builtin.py` | **new**: 7 `report_fix(...)` lines for `content_review.py` (paste at the end of `revise()`), and 3 ids for `PRACTICE_ONLY` in `app/authoring/build.py` |
| `_src/b1_cond_rep.py` → `b1-cond-rep-1.csv` | 12 rows practice only, 2 rows replaced (`replaces(...)`) |
| `_src/rq_order_1.py` → `rq-order-1.csv` | 19 of the 20 indirect-question rows practice only |
| `_src/b1_upgrades.py` → `b1-upgrades-1.csv` | 2 rows practice only |
| `_src/learner_fixes_20261121_iq.json` (+ one loading line in `learner_fixes.py`) → `twins-1.csv` | B2.1 *When does the shop close?*: answers added |
| `app/tests/bad_examples.json` | 6 new `reader` entries |

The four CSVs were regenerated; a column diff against the old files shows only the *practice only* column, the two replaced rows
and the answers of the B2.1 row. `php tools/check_draft.php`: 0 refused for all; `option_audit.py` on the new tasks: one flag,
read (below). `item_gates_test.py` on a copy with the new tasks: only `blind` and `point` (expected: the new tasks need a blind
round and a point). `draft_rules_test.py` 0 problems; `latvian_lint.py` no new finding; `instr_italics_test.js` PASS.

## How the import handles it (read in `app/src/CustomItems.php`)
- **Practice only:** the row keeps its text, so `dupKey` finds the imported task; its data differs (`practice_only`), so the import
  says *Already added: … updated* and updates it in place (status and results stay). `Content::role` then gives *learn*. The
  practice flag is not in the blind hash (`task_hash`), so no new blind record is needed for a demotion.
- **Replaced:** the new row with `replaces("old correct option")` retires the old task (`oldKey`: same topic and level, the old
  correct option for a choice) and adds the new one. The old row is gone from the generator, so it is not imported again.
- **Built-in:** `report_fix` makes a new `-rN` version (the old one retired); a demotion without a new version is the
  `PRACTICE_ONLY` set in `build.py` (as ip-B11-3a, ip-B12-1a on 14 November).

## The 70 B1 tasks: decision for each

**Kept as check / use (11):** ip-B11-1a (the basic choice *where the station is*), ip-B11-3c (order, *what time the bank opens*),
c-0886 (order, *I'd like to know how much this costs*), c-0887 (order, *if this bus goes to the airport*), c-0903 (rewrite
*What time does the bank open?*: the learner must drop *does* and add *-s*, not only swap two words), c-0888 (order, *I wonder
whether she has already left*), c-0889 (order, *how I can get to the station*), c-0905 (rewrite *Is there a bank …?*: needs *if*),
ip-B12-3b (order, *I wonder what time the meeting starts.*), ip-B12-5a-r2 (*whether the contract has been signed*), c-3332
(order, *do you know if there is a café near the station*).

**Changed, still check / use (8):**
| Task | What was wrong | Now |
|---|---|---|
| ip-B11-4a (built-in) | *Which sentence has a mistake?* with the correct twin *Do you know what time the film starts?* among the options | wrong options: *Can you tell me if this seat is free? / Could you tell me where she lives? / I wonder how much it costs.* |
| ip-B11-5a-r2 (built-in) | tester: "the wrong sentences are not good samples": a politeness choice (*You, where is …?*) solved without grammar | *Choose the correct option: Do you know how long ___ to get to the airport by taxi?* **it takes** / does it take / it take / takes it |
| ip-B11-6a-r3 (built-in, write) | tester: "the instruction gives the form away" (*Ask … where the meeting room is*) | *You have just joined a gym and want to swim, but you can't find the swimming pool. Ask the person at the desk politely. Start with *Could you tell me* or *Do you know*.* Checks: a polite start; a question word after it; no inversion after *where / how / which … / what …* (also catches *what time does*). Model: *Could you tell me where the swimming pool is?* |
| c-0913 (b1-cond-rep-1.csv) | *NOT correct* with four sentences about one platform, two of them twins | *Which sentence has a mistake?* **Can you tell me where can I leave my bike?** / Do you know which platform the train leaves from? / I wonder how long this report will take. / Do you know if the gym is open on Sundays? (`replaces("Could you tell me where is the platform?")`) |
| ip-B12-2a-r3 (built-in) | the B1.1 choice *where the station is* again at B1.2 | *Choose the correct option: Could you tell me where ___ ?* **you bought that jacket** / did you buy that jacket / did you bought that jacket / you have bought that jacket (Murphy 13: details of a past event, past simple) |
| ip-B12-4a (built-in) | tester: "each sentence should be different not to give away the pair" (*I wonder what she wants* next to *what does she want*) | wrong options: *I wonder why she left the party so early. / Do you know who she is? / Could you tell me if he's here?* |
| ip-B12-6a-r3 (built-in, write) | tester: "the instruction gives the form away" (*Ask … if the café takes cards*) | *Last week you emailed your landlord about the broken heater in your flat, but he hasn't answered. Write him one polite question. Start with *Could you tell me* or *I'd like to know*.* Checks: polite start; *if* or a question word; no inversion and no *did / will / has* before the subject after it. Model: *Could you tell me if you got my email about the heater?* |
| c-0914 (b1-cond-rep-1.csv) | *NOT correct* with the correct twin and two more breakfast sentences | *Which sentence has a mistake?* **Could you tell me why did the bank block my card?** / Do you know whether the museum has reopened? / I wonder who will win the match tonight. / I'm not sure how much we paid for the hotel. (`replaces("Do you know what time does breakfast start?")`) |

**Practice only now (learn, never evidence) (36):**
- Quote + frame, only two words change places (the teacher's *'Where is the toilet?' … too easy*), rq-order-1.csv:
  c-3317 to c-3324 (B1.1), c-3325 to c-3331 and c-3333 to c-3336 (B1.2): 19 tasks.
- The same frame and sentence again: c-0884 (*where the nearest bank is*), c-0885 (*what time the shop opens*), c-0892 (bank
  *the toilets are*), c-2147 (*where the station is*, as ip-B11-1a), ip-B11-3b-r3 (order, *where the station is*),
  var-ip-b11-order-01-r2 (order with *Start with Could you tell me*: the frame given), ip-B12-3a-r2 (*Make it polite: What
  time does the museum close?*, the B1.1 rewrite again at B1.2), c-0890 (*why the train is late*), c-0891 (*I don't know who he
  is*, five words, one swap).
- Two-word swap rewrites: c-0904 (*Where can I buy tickets?*), c-0906 (*How much is this jacket?*), c-0907 (*Why is the train
  late?*), c-2148 (*Make it polite: Where is the nearest bank?*).
- Wrong options that miss the real mistake (nobody writes *that / what* there; the mistake is leaving out *if* or keeping the
  question order), as ip-B12-1a on 27 October: c-0894, c-0912 (*if / that / what*), c-0898 (*whether / that / what*), c-0896
  (*where / that / did*: a choice of question word, not of order).

**Already learning tasks, unchanged (15):** c-0893, c-0895, c-0899, c-0900, c-0908, c-0909, c-0911, ip-B11-3a,
var-ip-b11-match-01-r2, c-0897, c-0901, c-0902, c-0910, ip-B12-1a; and **ip-B11-2a**, rewritten (tester: "so easy for B1"): it was
matched by the topic word (*toilet = toilet*); now one person four times, only the form decides: *Where does / did / is … / will
Anna work?* → *where Anna works / worked / is working / will work*.

**Counts after the change** (check / use): B1.1 9 old + 12 new = 21; B1.2 10 old + 12 new = 22. Learning: B1.1 28, B1.2 23.

## The 24 new tasks (gp6_iq_b1.py): what the learner must know, why the wrong options compete
B1.1 (present, *can*, *is / are*, present continuous, *if*); point iq_wh unless marked iq_yn.
1. mc *Could you tell me what this word ___ ?* **means** / mean / does it mean / it means: no *does*, so *-s* goes to the verb; *mean* (did not restore *-s*), *does it mean* (kept the question), *it means* (double subject) are the three real mistakes.
2. bank *Do you know where ___ ___ buy a phone charger near here?* **I · can** (+ *do*): statement order after *where* with *can* (the lead's *where I can leave my bike* idea); *can I*, *do I*, *I do* are wrong.
3. typed *Use the words in brackets: Can you tell me how often ___ on Sundays? (the night bus / run)* → **the night bus runs** (| *is running*): the learner builds subject + verb, so the order is not given; the trap is *does the night bus run* / *the night bus run*.
4. bank *I can't hear the guide. Do you know what ___ ___ talking about?* **she · is** (+ *does*): present continuous, subject before *is*.
5. tx need: printer at work, *Start with *Do you know where*.* 56 answers (the printer is / I can print … / there is a printer …, with *Excuse me* and *please*). No question words in the situation.
6. tx *Correct the mistake: Hi Eva, could you tell me how much does the course cost? I'd like to sign up.* → *how much the course costs* (the grader accepts the corrected words alone). The real slip *the course cost* stays wrong.
7. order *i wonder why my laptop is so slow*: statement order and a full stop after *I wonder*.
8. order (question) *can you tell me how the coffee machine works*.
9. mc (iq_yn) *I'd like to know ___ any free tables for tonight.* **if there are** / are there / if are there / there are: *if* missing, half-fixed, or no *if*.
10. tx need: the old town, *Start with *Could you tell me how*.* 56 answers (how I can get / how I get / how to get / how far … is / how long it takes …, *from here*).
11. typed (iq_yn) *Use the words in brackets. Add any missing word: I'd like to know ___ a balcony. … (our room / have)* → **if / whether our room has (got)**: the learner must add *if* and put *-s* on *have*.
12. bank (iq_yn) *Can you tell me ___ ___ ___ English? I need help with the menu.* **if · the waiter · speaks** (+ *does, speak*): *does the waiter speak* (question kept) and *if the waiter speak* (*-s* lost) are the two real mistakes. The chip *speak* does not agree with *the waiter* on purpose: losing *-s* after dropping *does* is the mistake of this point.

B1.2 (past without *did*, *was*, present perfect, *if / whether* after other frames):
13. typed *Use the words in brackets: Do you know where ___ the car last night? It isn't in the garage. (Tom / park)* → **Tom parked**: *last night* fixes the past; the traps are *did Tom park* and *Tom park*.
14. bank (iq_yn) *I wonder ___ ___ ___ my email. She hasn't answered yet.* **if · Maria · got** (+ *get, did*): *did Maria get* (question kept), *if Maria get* (past lost: the typical Latvian learner mistake).
15. mc (iq_yn) *Could you check ___ the parcel yet?* **if they have sent** / have they sent / if have they sent / did they send. *if they sent … yet* (American) is not an option. option_audit flags *did they send* as a different theme: read, it is the question-with-*did* mistake; kept.
16. order *i'd like to know where you learned to cook like that*: no *did*, past in the verb.
17. tx need: a colleague's laptop bag, *Start with *Could you tell me where*.* 52 answers (*where you bought / got it (from)*, *where I can / could buy / get one*), no *Excuse me* (a colleague).
18. bank *Do you know how long ___ ___ ___ in this company? She knows everyone.* **Anna · has · worked** (+ *does, work*): *has Anna worked* and *does Anna work* are the inversions.
19. tx *Correct the mistake: Dear Mr Kalns, could you tell me when did you send the invoice? We still haven't received it.* → *when you sent the invoice* (not *when you send*).
20. order (question) *do you know why the meeting was cancelled*.
21. typed (iq_yn) *Use the words in brackets. Add any missing word: Can you remember ___ the back door before we left? (you / lock)* → **if / whether you locked**, also *had locked* (*before we left*).
22. mc *Do you know where ___ yesterday? He didn't come to work.* **Mark was** / was Mark / Mark is / Mark has been: order, past lost, a perfect with *yesterday*.
23. tx need (iq_yn): the umbrella left in a meeting room, *Start with *Do you know if*.* 92 answers (*anyone / someone / somebody / anybody* + *has found / found / has seen / saw / has taken / took / has handed (it) in …*, and the passives *it has been found / was handed in …*).
24. bank (iq_yn) *I'm not sure ___ ___ ___ ___ the tickets yet. Let me check my email.* **if · we · have · booked** (+ *did, book*).

Settings: learning, shopping, travel, tourism, work (printer, coffee machine, meeting, invoice, colleague), technology, hotel,
restaurant, home, relationships. Frames: *Could you tell me, Can you tell me, Do you know, I wonder, I'd like to know, I'm not
sure, Can you remember, Could you check*. Not two tasks in a row with the same setting.

## B2.1 *Ask politely, starting with *Do you know*: When does the shop close?* (local c-3413, twins-1.csv:72)
A learner wrote *Do you know what time the shop closes?* (the card's example says *what time the shop opens*) and was refused.
*What time* asks the same as *when*: accepted now, also *Do you happen to know …* and *… today?*: 8 answers, overlay
`learner_fixes_20261121_iq.json`. Only answers were added, so no new blind round (`record-current`).

## bad_examples.json (reader, 6 entries)
Quote + frame (two words swap); a writing instruction that already says the indirect question; *has a mistake* with the correct
twin; a politeness choice with rude wrong options; a typed polite question with one wording only (*when / what time*);
choices whose wrong options miss the real mistake (*if / that / what*).

## For the lead agent
1. Add `gp6_iq_b1.py` to a batch file (e.g. a `gap_fill_b1.py` that imports it, or its own `save("…csv")`), give the 24 tasks
   their points (above: iq_wh, iq_yn) in `docs/grammar-map-src/assign_keys.json`, and carry iq_wh to the new keys of c-0913 and
   c-0914 (both iq_wh).
2. Paste `gp6_iq_b1-builtin.py` into `content_review.py` (end of `revise()`), add the 3 ids to `PRACTICE_ONLY` in `build.py`,
   retired count in `bank_update_test.php` +7 (confirm with the build). The 2 write tasks and their checks were tested with
   PHP `preg_match` on 25 sample answers (all as intended).
3. Blind round for: the 24 new tasks, c-0913, c-0914, and the 7 built-in versions. The demotions need none.
4. **Incident:** my first write of `learner_fixes_20261121.json` overwrote the file the other agent had created a few minutes
   earlier (its 3 entries: conjunctions-1 *nevertheless / nonetheless*, b1-new-4 *could you please pass me the salt*,
   comparison-1 *that jacket is cheaper than this one*). I rebuilt the 3 entries exactly from its regenerated CSVs (the CSVs
   now regenerate byte for byte), and moved my own entry to `learner_fixes_20261121_iq.json`. If the other agent had written
   entries it had not yet regenerated, they are lost: please ask it to check its file.
5. Rule card line suggested (the card has no example with *did*): under *No tense change*, add *Where did she go? → Do you know
   where she [[went]]?* (LV the same example; heading LV *Laiks nemainās: pazūd tikai *do / does / did**).

## Not decided / doubts
- The write task at B1.1 refuses *Could you tell me the way to the pool?* (correct English, no indirect question): the feedback
  says "Then a question word". The old task did the same; a list cannot help in a write task.
- Two chips that do not agree with the subject (*speak* with *the waiter*, *get* with *Maria*): kept on purpose (above); the
  8 November rule bans mismatches that can be rejected without the topic, here the mismatch IS the topic's mistake.
- ip-B11-2a (learning) shows *did* and *will* at B1.1: recognition only, matching is never evidence.
