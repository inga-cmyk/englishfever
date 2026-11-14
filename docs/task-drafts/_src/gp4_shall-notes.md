# Batch 4, point `shall` (A2.1): notes

Source: `docs/task-drafts/_src/gp4_shall.py`, topic *Future: will, going to, present continuous*, level A2.1.
Grammar: Murphy, *English Grammar in Use*, unit 22 (Shall I …? / Shall we …? to ask somebody's opinion, in offers and
suggestions; *shall* in questions only with *I* and *we*), unit 21 (*I'll …* as an offer in a statement).

## Mix (25, as in the brief)
7 choice, 5 word order, 4 word bank, 1 matching (learning), 5 typed gap, 3 whole sentence.

## Decisions that apply to every task
- *Should I / Can I / Could I / Do you want me to …?* and *Let's … / Why don't we …?* are correct, so they are never a wrong
  option, and no typed gap has *shall* itself as the answer: the gaps are the verb after *shall* (verb in brackets) or the
  question word, so the answer is fixed.
- Wrong options come from the typical errors of the point: *Will I / Do I …?* as an offer, *Will we / Do we …?* as a
  suggestion, *shall* + *to* / *-ing* / past, *Where we shall …?* (statement order), *Shall you …?* as a request,
  a short answer with *shall* to an offer.
- All five word orders are question-word questions. `plain()` in `lib.py` turns *Put the words in order to make a
  question.* into *Put the words in order.*, and the cards of a yes/no question (*shall i carry your bag*) also make a correct
  statement (*I shall carry your bag.*). With *what / how / where / which / what time* first, no statement can be built.
- No question tags (*Let's go, shall we?* is B1 and already has tasks in Question tags).
- Latvian: no *Tulkojot burtiski* note; the Latvian offer (*Vai atvērt logu?*, *Vai man palīdzēt?*) does not lead to
  *Will I*. Some Latvian words without diacritics were marked as English by `lv_mark` (*citam, tikai, pareizi, ideju*), so
  the Latvian lines are worded around them; *bez to* reads as Latvian, so the *to* / *-ing* mistake is shown only inside the
  wrong example in the Latvian line.

## Task by task: what the learner must know, and why the wrong options compete
Choice
1. *Your hands are full. ___ I open the door?* Shall / Will / Do: an offer is *Shall I*. *Will I* (Latvian future) and
   *Do I* are real questions elsewhere, so the short situation is needed (cover test).
2. *Shall we ___ a break?* have / to have / having / had: base verb after *shall* (the typical *Shall we to go / going*).
3. *Which sentence is correct?* *Shall I help you with your suitcase?* against *to help / helping / helped*.
4. *Which sentence is correct?* *Where shall we have lunch?* against *Where we shall have lunch?* (statement order),
   *Where shall we to have lunch?*, *Where shall have we lunch?*
5. *Which sentence is NOT correct?* *Shall we to meet at six?*; the others are an offer and two question-word questions.
6. *Which sentence is NOT correct?* *Shall you call me later?* (*shall* only with I / we; a request is *Can you / Will you*);
   the others are a suggestion, a *What time shall we* question and an offer.
7. *A friend asks: 'Shall I make you a sandwich?'* *Yes, please.* against *Yes, you shall / Yes, I shall / Yes, you will*:
   the reply to an offer. The question in quotes is needed (it is what is answered).

Word order (all *Put the words in order.* after `plain()`; every other order checked aloud: none)
8. *what shall i bring to the party*; 9. *how shall we get to the airport*; 10. *where shall i put these boxes*;
11. *which bus shall we take*; 12. *what time shall we start the meeting*. The learner must put *shall* before *I / we*
    after the question word (not *What I shall bring*).

Word bank
13. *I'm bored. ___ we go for a walk?* Shall / Will / Do: a suggestion; *Will we / Do we go for a walk?* are questions
    about the future or a habit, wrong here because of *I'm bored*.
14. *Shall I ___ you a taxi?* call / to call / calling.
15. *What ___ ___ watch tonight?* shall / we / you: *What shall we*; the chips also build *What we shall watch* (statement
    order) and *What shall you watch* (shall with you), both mistakes of this point.
16. *Shall we ___ ___ the beach on Sunday?* go / to / going: *go to*; the other pairs give *Shall we going to* and
    *Shall we to go*, the two typical errors.

Matching (learning)
17. *Shall I open the window? / Where shall we meet? / What shall we have for dinner? / When shall I call you?* with
    *Yes, please. It's hot in here. / Outside the cinema. / Fish and rice. / After six. I'm at work till then.* Swapping any
    two answers gives nonsense (a place for *When*, *Yes, please* for *Where*). It is matched by meaning, so learning only.

Typed gap
18. *It's raining. Shall we ___ a taxi? (take)* take; 19. *Your phone is dead. Shall I ___ you mine? (lend)* lend;
21. *I'm going to the shop. Shall I ___ you anything? (get)* get; 22. *We're free tonight. What shall we ___? (do)* do:
    base verb after *shall* (*to take*, *taking* are the expected mistakes). The verb in brackets fixes the word.
20. *Write the missing word: ___ shall I put your coat? On the chair?* Where (the answer *On the chair?* asks for a place).

Whole sentence
23. *Say it another way with *Shall I*: Do you want me to book a table?* Shall I book a table? (+ *for you / for us*).
24. *Make a question with *Where*: Shall we go to Italy this summer?* Where shall we go this summer? | Where shall we go?
25. *Make a question with *What*: Shall we cook pasta tonight?* What shall we cook tonight? | What shall we cook?
    (the fronted time phrase is added by `auto_answers`).

## Card lines needed (the Future card has *Shall I…? / Shall we…?* with *Shall I open the window? Shall we go?*)
- In `uses`, add a second example to the shall line, for question words:
  EN *[[Where shall we]] meet?* · LV the same example (the Latvian title already says *piedāvājumiem un ierosinājumiem*).
  Or as a `watch` line: EN *Question word + shall + we / I: [[What shall we]] do tonight? (not What we shall do?)*
  LV *Jautājamais vārds + shall + we / I: [[What shall we]] do tonight? (nevis What we shall do?)*
- In `mistakes`, add: [*[[Will I]] open the window?* → *[[Shall I]] open the window?*] (offer); LV note none needed.
Tasks 6 and 7 rely on *Can you…? / Will you…?* (requests) and *Yes, please.* only in the explanation and the correct
answer; neither needs a card line.

## Doubts
- *Will I …?* as an offer (task 1) is wrong in standard British and American English (Murphy 22), but Irish and Scottish
  English use it. If a reader flags it, the BrE default and Murphy decide.
- *Shall you call me later?* (task 6): *shall* with *you* survives only in old-fashioned formal English (*Shall you be at
  home?*), never as a request; I kept it as the wrong sentence.
- Task 20: *So shall I put your coat? On the chair?* is barely possible; only *Where* is accepted.
- Task 7 has an intro (*A friend asks: '…'*): it is the pattern of fu-A21-5a and is needed, since the task is the reply.
