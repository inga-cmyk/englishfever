# Batch 5, point `prep_move` (A2.2), topic Prepositions of time and place: notes

**Point:** Movement: *to, into, out of, across, through, along, past*; *arrive in / at* (also *get to*, *go home*). Before this batch: 0 check, 1 use (*Write in, on or at: We arrived ___ Riga late at night.*, more-1.csv:73). These 9 tasks bring it to 10. None of the sentences exists in `app/content/items.json` or `docs/task-drafts/*.csv`.

**Topic:** *Prepositions of time and place (in, on, at)*, A2.2: the existing task of the point is there, and movement is place. *Prepositions after words* (A2.2 too) was the other option; I did not use it. I kept off transport (*by car, on the bus, get on / off*), which the `prep_transport` writer covers at the same time: no bus, car, train or taxi in any sentence.

**Murphy:** *English Grammar in Use* unit 126 (the unit the map gives: *go to*, *arrive in / at*, *get to*, *go / get home*, *into / out of*). *across, through, along, past* come from Murphy's *Essential Grammar in Use*, in the unit on prepositions of movement (Murphy 126 does not cover them). The map lists the TE A2 lesson *Prepositions of movement* for the same scope.

**Mix (9):** 4 choice, 1 word order, 2 word bank, 1 typed gap, 1 whole sentence. The brief asks for about 3 / 2 / 2 / 2 / 1. I changed one word order to a choice. In a word order the preposition card is given, so the order shows only whether the learner knows where *along* goes, and that is weak evidence. A second word order (*out of*, *get to*) would only have been copying too. The point had no *check* task, so the extra choice fills that gap: there are now 7 check tasks and 3 use tasks.

## Task by task: what the learner must know, and why the wrong options compete
1. *We arrived ___ the hotel after midnight.* (at / to / —): *arrive at* + a building. *to* is the Latvian *uz* (*ieradāmies uz viesnīcu*), the most common mistake; *—* is the learner who copies *reach the hotel*. I left out *in* on purpose: *arrive in the hotel* is rare but some speakers say it, so it is not a safe wrong option.
2. *What time did you ___ the office today?* (get to / get / arrive / arrive to): the learner must know that *get* needs *to* and *arrive* needs *at*. Each wrong option is one of the ways learners mix the two verbs.
3. *Which sentence has a mistake?* → *We arrived to Oslo late on Friday.* (should be *in*). The three correct sentences are about three different movements: *into* (ran into the kitchen), *through* (the road through the forest), *past* (walk past your house).
4. *Walk ___ the bank and turn left.* (past / passed / pass): *past* is the preposition for going by something. *passed* (the verb) is a frequent spelling mistake because the two words sound the same, and *pass* is the bare verb. *by* would also be correct, so I did not offer it.
5. Order *let's walk along the beach after lunch* (+ *after lunch let's walk along the beach*): *along* + the line you follow. There is only one noun after a preposition, so no card can move to another noun. *let's walk after lunch along the beach* is not natural, so I did not accept it.
6. Bank *We swam ___ the river to the other side.* (across / through / along): *to the other side* asks for *across*. *along* contradicts *to the other side*. *through the river* is the Latvian *cauri* calque and is not used for crossing water.
7. Bank *The cat came in ___ the open window.* (through / across / along): an opening asks for *through*. *across* and *along* the window make no sense, but a learner who mixes up the three movement words might pick them.
8. Typed *Write one word in each gap: At airport security, take your laptop ___ ___ your bag.* → *out / of*: the learner must write *out of*, not *out from* or *from*. No other pair of words fits the two gaps in this situation.
9. Whole sentence *Correct the mistake: What time did you get to home last night?* → *What time did you get home last night?*: no *to* before *home*. The mistake comes from the Latvian *uz mājām*. The grader also accepts only the corrected words.

## Card lines needed (the card of *Prepositions of time and place* has only *arrive in / at*)
- **form** (EN): *Movement: *to* (towards a place), *into* / *out of* (in / out of a room or a box), *across* (from one side to the other), *through* (in at one side and out at the other: a window, a tunnel, a forest), *along* (following a road, a river, a beach), *past* (going by something). *get to* a place, but *go home, get home* (no *to*).*
- **form** (LV): *Kustība: *to* (uz kādu vietu), *into* / *out of* (iekšā / ārā), *across* (pāri), *through* (caur, cauri), *along* (pa ceļu, gar upi), *past* (garām). *get to* + vieta, bet *go home, get home* (bez *to*).*
- **mistakes** pair: *What time did you get [[to home]]?* → *What time did you get [[home]]?*

## Doubts
- The Latvian explanations contain the ASCII Latvian words *Tulkojot, burtiski, caur, cauri*. `italics.lv_mark` marks them as English examples (the save run showed *\*Tulkojot burtiski\**, *\*through = caur, cauri\**). They need a `LV_BY_FILE` entry in `lib.py` for the final CSV name, as earlier batches have (I may not edit `lib.py`). I reworded every other Latvian word so that it carries a Latvian letter or is already in the list.
- Typed gaps of this topic get the default instruction *Complete with *in*, *on* or *at*:* (`GAP_INSTR` in `lib.py`), which would be wrong here. Task 8 therefore has its own instruction (*Write one word in each gap:*), and the default is not applied.
- Task 1: I offered no *in*. If the judge wants a third wrong option, *on* is safe, *in* is not.
- Checks: `check_draft.php` 9 accepted, 0 refused; `option_audit.py` 0 flagged; `pending/zz5-prep_move.csv` deleted.
