# Batch 4, point `vp_both` (B1.1): notes of the writer

Topic: Verb patterns (`verb_patterns`), level B1.1. There are 25 tasks in `gp4_vp_both.py`.

## Mix
7 choice, 5 typed gap, 3 whole sentence, 5 word order, 4 word bank, 1 matching. This is the brief's mix, unchanged.

## Sources (Murphy, *English Grammar in Use*; unit numbers from memory, they match the lead's)
- Unit 56: *begin, start, continue* take *-ing* or *to* with no difference. Murphy also says we do not normally use *-ing* after *-ing* (*it's starting to rain*). For that reason no task has *is starting / are beginning* before a gap.
- Unit 58: *like, love, hate* take both forms. *would like / would love / would hate / would prefer* take *to* (*Would you like to come?*, not *coming*). In British English *like doing* is closer to "enjoy" and *like to do* closer to "choose to". Both are correct in every sentence used here.
- Unit 59: *prefer doing / prefer to do*, and *would prefer to do*. Unit 59, not 56 or 58, is the unit for *prefer*. Name it in the point's sources.

## Decisions (so that no wrong option is correct English)
- **A choice or bank never offers both right forms.** Either the task is *Which sentence is NOT correct?* (three correct sentences that show both patterns), or the other right form is simply not among the options. The explanation then says that it is correct too (*started dancing* ... *started to dance* is correct too).
- **The wrong options are the point's own mistakes.** They are the base form alone (*started learn*, *like eat out*), *to* + *-ing* (*to dancing*), *would like* + *-ing*, and once *-ed* (*started danced*, copying the past from *started*).
- ***would prefer* + *-ing* is never a wrong option.** Swan calls it "normally" + infinitive, so a reader could defend *-ing*. Only *would like* and *would love* + *-ing* are used as mistakes.
- **No *prefer X to Y*** (only *-ing* there), **no *begin to understand / realise*** (only *to* there), and **no *stop / remember / forget / try*** (point `vp_meaning`).
- **Nouns in the brackets.** The hint verbs (*laugh, try, go, work, talk*) are needed in the verb form after *began / loves / prefer / continued / hate*. A noun reading gives no sentence. In the *Correct the mistake* tasks I used *spend* and *eat out*, which cannot be read as nouns. *like work* was avoided because *work* can be a noun.
- **Questions in word order** use *Put the words in order to make a question.* With the unpatched `lib.py`, `od()` added the statements *you would like to have a coffee before the meeting* and *before the meeting you would like to have a coffee* to the accepted orders of task 17. With the lead's patch only the questions should stay. Please check the built row.

## Task by task: what must the learner know, and why do the wrong options compete
Choice
1. *My laptop … continues ___ without any problems.* (to work / work / to working) After *continue*: *to* + base verb. *work* is the base-form mistake and *to working* mixes the two patterns. *working* (also right) is not offered.
2. *… the whole crowd started ___.* (dancing / dance / danced / to dancing) The learner must know that *start* takes *-ing* here. *to dance* is not offered.
3. *Which sentence is NOT correct?* *I'd like going to the concert …* The learner must know that *would like* takes only *to*. The other three are correct and about three different things: *hates to fly*, *started building*, *continued to work*.
4. *We'd love ___ to your party …* (to come / coming / come / to coming) *would love* + *to*. *coming* is the typical mistake.
5. *Which sentence is NOT correct?* *She started learn Spanish …* The base form after *start* is wrong. The other three are *love cooking*, *began to argue*, *would prefer to sit*.
6. *Which sentence is correct?* *My husband hates driving at night …* against *hates drive* and *hates to driving*. There are only three options: a fourth believable mistake does not exist.
7. *Which sentence is NOT correct?* *We like eat out …* The other three are *began to use*, *prefers to cycle*, *would like to join*.

Typed gap (both forms accepted in every gap)
8. *The audience began ___ before the actor finished his joke. (laugh)* takes *laughing | to laugh*.
9. *My partner loves ___ new recipes … (try)* takes *trying | to try*.
10. *Do you prefer ___ on holiday alone or with friends? (go)* takes *going | to go*.
11. *Many people continued ___ from home after the offices reopened. (work)* takes *working | to work*.
12. *I hate ___ on the phone, so I usually send a text message instead. (talk)* takes *talking | to talk*.

Whole sentence
13. *Say it another way with *to*: We started looking for a new flat …* The learner must know that *started to look* says the same. The *as soon as* clause may come first.
14. *Correct the mistake: I love spend time with my cousins …* Both *spending* and *to spend* are accepted.
15. *Correct the mistake: Would you like coming with us to the team lunch on Friday?* The only correction is *to come*. *Do you like coming* changes the meaning, so it is not accepted.

Word order
16. *she began to write a blog about her travels last year*. *last year* may come first.
17. *would you like to have a coffee before the meeting* (a question). *before the meeting* may come first.
18. *my father started using a smartphone when he turned seventy*. The *when* clause may come first, and *my father / he* may swap (*when my father turned seventy he started …*).
19. *she continued working at the hospital after her first child was born*. The *after* clause may come first.
20. *do you prefer to cook at home or go to restaurants* (a question). The two choices may swap. *or* blocks the statement.

Word bank (one right chip; the other right form is not a chip)
21. *During the long winter my brother started ___ his own furniture …* (making / make / to making)
22. *I'd like ___ a table for four at eight o'clock, please.* (to book / booking / book)
23. *My parents love ___ in the mountains …* (walking / walk / to walking)
24. *House prices will probably continue ___ next year …* (to rise / rise / to rising)

Matching (a learning task)
25. *it started* + *raining …*; *The baby … began* + *to cry loudly*; *my grandmother … still loves* + *working in her garden …*; *When you're back, I'd love* + *to see the photos from your trip*. I swapped every pair of endings, and in every swap at least one sentence is wrong or makes no sense. For example *I'd love working in her garden* is wrong for two reasons: *would love* + *-ing*, and *her*.

## Card lines needed (Verb patterns card)
1. Change the "both" line, adding *continue* and *prefer*:
   - EN: "Some verbs take both with a very similar meaning: *like, love, hate, prefer, start, begin, continue* (*I like swimming. ≈ I like to swim. It started raining. = It started to rain.*)"
   - LV: "Daži darbības vārdi der ar abiem ar ļoti līdzīgu nozīmi: like, love, hate, prefer, start, begin, continue (I like swimming. ≈ I like to swim. It started raining. = It started to rain.)"
   - In the v2 table cell: *like, love, hate, prefer, start, begin, continue*.
2. Add a new "Watch out" line:
   - EN: "*would like / would love / would prefer* + *to* only: *I'd like [[to go]].* (not *I'd like going*)"
   - LV: "*would like / would love / would prefer* + tikai *to*: *I'd like [[to go]].* (nevis *I'd like going*)"

## Latvian words that the italics marking takes for English (for `LV_BY_FILE`)
*tikai, Tikai, abas, pareizas, Tulkojot, burtiski, mums*

## Doubts
- The two *Tulkojot burtiski* notes say that the Latvian infinitive (*sāka mācīties*, *patīk ēst*) leads to the bare English verb. I think Latvian really causes this mistake: there is no *to* in the Latvian form. If the lead disagrees, drop the second sentence of the Latvian explanation in tasks 5 and 7.
- Task 6 has only three options.
