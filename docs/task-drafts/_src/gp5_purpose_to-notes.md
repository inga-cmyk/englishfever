# Batch 5, point `purpose_to` (A2.2): notes

Source: `docs/task-drafts/_src/gp5_purpose_to.py`, topic *Contrast, purpose and reason* (app label *Contrast, purpose and
reason (although, despite, so that)*), level A2.2 (new for the topic; prepared tasks only, teacher's decision of 15 November).
Grammar: Murphy, *English Grammar in Use*, unit 64 (*to* + verb for purpose; *for* + noun, *go for a coffee*; not *for* + verb
or *for to* for why somebody does something).

## Mix (N = 6)
2 choice, 1 word order, 1 word bank, 1 typed gap, 1 whole sentence. That is the 3/2/2/2/1 mix scaled to 6. The point already
has 3 check tasks (all choices) and 1 use task (a correction), so I wrote a gap and a whole sentence instead of a third choice.
Everything is A2.2: one clause plus a *to* phrase, 6 to 9 words, no *so that* and no *in order to* in a question (B1).
*in order to / so as to* are still accepted in the typed answers because they are correct English.

## Task by task: what the learner must know, and why the wrong options compete
1. *He went to the doctor ___ a check-up.* for / to / on. A noun follows, so *for* (Murphy 64). *to* is the typical mix-up
   with *to* + verb and the literal translation of *uz pārbaudi*; *on* comes from the same *uz*. No situation needed.
2. *Which sentence has a mistake?* *I'm learning English for get a better job.* The other three are correct and about three
   different things: *to* + verb after *called*, *for a swim* (for + noun), *for the weekend* (time, not purpose).
   The mistake is the map's typical error (*for* + verb).
3. Word order: *he uses his phone to pay for everything*. The learner must put *to pay* after the object, with *for* staying
   with *everything*. Checked aloud: no other natural order (*to pay for everything he uses his phone* is not said).
4. Word bank: *She goes to the gym ___ ___ fit.* to · stay · for · staying. Only *to stay* is right; *for stay*, *for staying*,
   *to staying* are the typical mistakes of this point (map: *for get, for getting*). No other combination is correct.
5. Typed gap: *Why did you call the hotel? I called ___ a room. (book)* → *to book* (also *in order to book*, *so as to book*).
   The question *Why?* is needed: without it, *I called the hotel and booked a room* would be a second answer.
6. Whole sentence: *Join with *to*: I went to the post office. I sent a parcel there.* → *I went to the post office to send a
   parcel.* The learner must use the base verb (*send*, not *sent*) and drop *I*; *… to send a parcel there.* and *… in order
   to send a parcel.* are accepted.

## Card lines needed
None: the card already has *to* + verb (*She works hard to pass the test.*) and *for* + noun (*We went to the café for a
coffee.*), and the mistake *I went to the bank for get some money.* No task repeats a card example.

## Checks
`check_draft.php`: 6 accepted, 0 refused, 9 typed variants; `option_audit.py`: 0 flagged. CSV deleted afterwards.

## Doubts
- The Latvian lines avoid *pasaka / izsaka / pareizi* and the *Tulkojot burtiski…* opening, because `lv_mark` marks these
  words as English in a file that has no `LV_BY_FILE` entry. So task 1 has no *Tulkojot burtiski* note, although *uz
  pārbaudi* → *to / on a check-up* is a real Latvian-caused mistake. If the lead agent adds
  `LV_BY_FILE["<batch file>.csv"] = {"Tulkojot", "burtiski"}`, task 1's LV line can end: *Tulkojot burtiski *uz pārbaudi*,
  sanāk *to a check-up* vai *on a check-up*.*
- A bare *to* in Latvian text is read as Latvian (*to* = *tas*), so the LV lines show *to* only inside examples
  (*to pay, to book*).
- Task 2: *They are staying with us for the weekend* uses *for* for time, not purpose. It is correct and different, which is
  what the rule asks for; if the judge wants all four on purpose, replace it with *We stopped at a café for lunch.*
