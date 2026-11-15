# Blind check r13: the judge's decisions (batch 5, A2 part, 15 November)

152 tasks (`pending/gap-fill-a2-1.csv`, generator `_src/gap_fill_a2.py`, modules `_src/gp5_<point>.py`), two readers; 49 flagged. Nothing needed the teacher. Row numbers are CSV lines, the same numbers as in `r13-flags.md`.

**(1) Rebuilt, need round r13b: CSV lines 140 and 145.**
- **r13-139, line 140 (pas_by):** *The windows of our office ___ ___ a small company every month. (clean)* needed three words in two gaps. Reader 2 split it *are / cleaned by*, and the grader checks each gap on its own, so the splits cannot be keyed. *every month* also left *were cleaned* (a past habit) open. Rebuilt: *Write one word in each gap: The windows of our office are ___ ___ a small company every month. (clean)* → *cleaned / by*. The task still tests the doer after *by*, and the 3rd form after *are*.
- **r13-144, line 145 (plural_only):** *Start with *These trousers*: This shirt is too expensive.* only swapped the noun, so it was not a rewrite (both readers). Rebuilt: *Correct the mistake: Your trousers looks great with that jacket.* → *Your trousers look great with that jacket.* The verb has no *-s* after an always-plural noun, and nothing in the sentence shows the plural. Notes files updated for both tasks.

**(2) Answers added that the readers found correct** (no new round, `record-current`):
- line 25: *were very comfortable* (no time word, so the past is correct too; the point is *be* + adjective).
- line 28: *Our neighbours are really nice.*
- line 31: *today she is running but usually she swims*.
- line 46: *A few cafés are near my office.* (less natural, still correct).
- line 75: *'s* (*the exam's really helpful*).
- line 86: *What time did you arrive home last night?* (*arrive home* has no *to* either, so the explanation fits it). Also *What time did you get to your home last night?*, which gets its own answer note: correct, because with *your* the word *home* is an ordinary noun, but we usually say *get home*.
- line 114: *No-one*.
- line 153: *At the meeting(,) we discussed the new timetable.*

**(3) Kept:**
- line 4: the reader's *do you want us to come with you* needs two *you* cards. There is only one, so the cards cannot make it.
- lines 3, 8, 51, 101, 122, 123: what the reader proposed is already accepted (*to watch / to play*, *It is very fast*, *farthest*, *traveling*, the present-tense correction).
- line 10: *my favourite hobby* fixes the speaker as *I*. *My sister loves cooking* does not say the same thing.
- line 19: *The two buses are late* does not start with *Two*. The start does not give the plural away: the learner still has to write *buses are*. *busses* stays accepted as a dictionary variant.
- line 22: *Use the words in brackets* asks for both words, and one gap for a phrase is the house pattern. The order and the *-s* are what is tested.
- line 26: *very active for her age* uses everyday words and is one clause: A2.
- lines 29, 53, 54, 55: "—" is house style for "no word" (ITEM-WRITING-RULES, the table of mistakes). *What time you usually finish work?* is a real learner mistake. *on this weekend* is wrong after Murphy 121 (no preposition before *this / next / last / every*).
- line 33: *He never is doing that* is not English. *never* + habit = *does*.
- line 37, 60, 63, 72, 73, 85, 89 (*i very much like my new flat*, correct and less natural, stays accepted), 91, 106, 116: the readers agree with the key, or their note is not a problem.
- line 48: *A wallet was empty* and *There was the wallet* are the two mistakes of the point. The capital only shows the position.
- line 68: *use go* names the verb, not the form. The learner still has to choose *gone* over *been*. Without *go*, *Rita has moved to Tokyo* would be another correct answer.
- line 112: *something* for *somewhere* is a believable mix-up inside the point (some- + thing / where).
- line 117: *swimming and to cycle* is not parallel. The reader agrees it is wrong.
- line 127: *in the tram* is the Latvian transfer (*tramvajā*). Murphy 129 gives *on* for trams, buses and trains, and the existing task (*I saw her in the train*) already marks *in* wrong.
- line 129: *by a taxi* is not English. Only *in* fits the open gap.
- line 135: the gap is before *a room*, and *I called book a room* is wrong, so writing *to* is the point.
- lines 137-141: *by* + doer in the present and past simple passive is on the map at A2.2 (teacher, 15 November), and test-english.com teaches the passive at A2. The level stays.
- line 149: *Oh no, I forgot!* makes the decision a new one, and Murphy 23 gives exactly this situation with *will* only. *going to* stays out (the contrast is the point).
- line 150: the instruction offers *will* or *going to*, so *I'm buying* is outside it. *Why are you saving…?* shows a plan: *going to*.

**Writers' doubts that no reader flagged:**
- pp_been_gone, line 61: *My parents have gone to Italy twice* stays the mistake. Murphy 8 and the card teach *been* for visits that are over. Accepting the American *gone* would also make line 63 (*We have ___ to the cinema twice*) open, and the point would disappear.
- adv_degree: *enjoyed … much* stays a wrong option (Murphy 87: not used alone in positive sentences).
- pas_by: the chip *of* stays (the Latvian genitive is a believable transfer).
- dep_none: *had a discussion* stays out, because the instruction asks for *discuss*.
- ps_pc: *He never did that* stays out next to *Look!*
- prep_none: *We arrived yesterday in Rome* stays out (Murphy 109: place before time).
- purpose_to: the *for the weekend* sentence is a correct sentence in a *Which sentence has a mistake?* task. That is allowed: it is about a different use of *for*.
- No other doubt needed a change.

**(4) Nothing needed the teacher.**

Checks after the changes: `check_draft.php` 152 accepted, 0 refused (232 typed variants, 0 refused). `option_audit.py` gives 1 flag, the known odd-theme flag on the count_unc mistake task. The draft rules and Latvian tests on the file found 0 problems.

**r13b (2 tasks, both readers):** *cleaned / by*: no other answer; the level note (passive with *by* at A2.2) is kept: the map and the teacher's decision put it at A2.2. *Your trousers look great…*: *Your pair of trousers looks great with that jacket.* is correct English and is accepted (only an answer added).
