# Rules for writing questions (from Inga's feedback; use them for every new batch)

1. **Layers inside one level.** For the same sentence type, write a *hinted* version and a *hint-free* version at the same level.
   - Hinted (recognition): `Make it negative with don't have to: We have to pay today.`
   - Hint-free (next layer): `Make the sentence negative: We have to pay today. (It is not necessary.)` or a short context line that makes one answer the natural one.
   - `Complete with have to or has to: Tom ___ wear a tie.` -> hint-free: `Tom ___ wear a tie at work. It is the rule.` with the answers listed (`has to | must`).
2. **Hint-free questions need a clear context** and the answer list must accept **every** possible correct answer (variants, contractions, both clause orders).
3. **The suggested form is a language item.** It is shown in italics (the app does this automatically for the words after *with*, and for 'quoted' forms; or write `*don't have to*` by hand). The suggested form must differ from the form in the sample sentence, so the task is never "copy it".
4. **Wrong options must be wrong**, not "less natural". Use forms that are ungrammatical in that sentence (wrong agreement, missing -ing, base form after a past), never a second valid tense.
5. **One instruction line, one sample sentence**, instruction first, sample in italics on the next line (automatic for "Instruction: sample").
6. **Question mix per 10**: 3 choose, 4 drag-and-drop (order, word bank, matching), 2 type a word or words, 1 type the whole sentence. Write new batches with at least 40% drag-and-drop.
7. **Short explanations**, English and Latvian, Latvian terms from `LATVIAN-TERMS.md`.
8. **Sentence length by layer**: A2 about 5-9 words, one clause, everyday words; B1 about 10-16 words, two clauses, wider vocabulary, no clue word. Negatives and questions are A2 as well.
9. **New topic**: at least 25 questions per level before it goes live; existing topics aim for 50 per level.

## Learn or check (rule from Inga, 3 November)
- For every task decide: does it **check** understanding, or **help build** it? A task that can be solved from the meaning alone, without the grammar (matching beginnings and endings by context, "Which sentence is about a habit?"), is a first step in learning a topic, not evidence that the learner knows the form.
- Writing tasks must not give the answer away: no "Start with He or She and add an activity", no "Use I am going to". Give the situation; the check looks for the form. Name a form only when choosing it is not the point of the task.
- In word-order tasks, check whether the people can be swapped (*she … I* → *I … she*): if the sentence is still correct, accept it.

## New topics: scope from test-english.com (rule from Inga, 2 November)
- Before a new topic is added (card or tasks), read what test-english.com teaches about it at that level (the lesson for the topic in docs/LEVEL-LISTS-test-english.md) and cover the same points, in the same order.
- Use it for the scope only: our own examples and explanations, no copied sentences or exercises. Check the grammar against Murphy as before.

## Topics of the sentences (rule from Inga, 1 November)
- New tasks follow the best existing tasks as models (same instruction style, ungrammatical wrong options, one sensible answer) and vary the setting: travel, work, hobbies, lifestyle, learning, relationships, technologies; current events only at B2 and C1.
- Not the same setting in two tasks in a row of one topic and level; real, adult situations, no children's-book sentences.

## A situation, never grammar terms (rule from Inga, 29 October)
- Learners do not know words like *vowel, consonant, present perfect, passive*. A task never asks for them (*Match each phrase with how its first word starts*, *Which sentence is passive?*). Terms belong on the rule card.
- The sentence itself shows what to use, and a wrong answer is clear from the example (*He wears ___ uniform at work.* → *a*). Learners see the pattern from examples (*an apple, an hour*) or open the card.
- *Make a question* always says which question: *Make a question with *What*: …* or *Make a yes/no question: …*. Both kinds are mixed.
- No speaker tag after a quote (*…,' she said.*): *Which sentence reports this: '…'*.
- A context that leaves the tense open (*this morning? It's four o'clock now*) is replaced by an unambiguous time word (*yesterday*), not explained.
- In *Which sentence is NOT correct?* the other three sentences are about three different things, not one copy of the wrong sentence.

## Plain instructions (rule from Inga)
- The instruction says what to do and nothing else: *Which sentence is NOT correct?*, *Which sentence is correct?*, *Put the words in order.*, *Match each beginning with its ending.* No setting in front (*At work: ...*, *In the team: ...*), no hint after a word-order instruction (*Compare two years.*), no topic after a matching instruction, no *Your friend writes: '...' Choose the correct option.* The sentence, the options and the tiles carry the content.
- Two tasks may therefore share the same instruction. The importer counts a task as a duplicate only when instruction **and** content (correct option, sentence, pairs) are the same; it never asks for new wording to make a prompt unique.
- Forms named in an instruction are italic one by one, never *and* / *or* between them or the colon: Write one sentence with *older* and *than*:
- The CSV generators apply this automatically (`plain()` in `docs/task-drafts/_src/lib.py`).

## Matching tasks: one sensible pairing only (rule from Inga)
- A matching task is only valid when exactly **one** way of pairing the cards makes sense. If two endings fit two beginnings (*The new phone is much* / *a bit* + *faster* / *heavier*), the learner is guessing and a right answer proves nothing.
- Test every task: swap any two endings. If both versions are grammatical and sensible, rewrite it.
- What works: the verb is in the beginning and its object or agent in the ending (*My brother always forgets* + *his keys.*); a different pronoun in every short answer (*Yes, I have.* / *No, he hasn't.* / *No, they haven't.*); four different topics in four if-sentences (bus, doctor, phone, winning); meanings and forms that cannot be swapped (*much faster* = a big difference).
- What does not work: adverbs only (*never / just / already* + any object), *since / for* + two time phrases, answers like *Not yet.* or *Yes, twice.* that fit many questions, two beginnings with the same subject and auxiliary.

## Mistakes made before, and the check that stops each one
`python3 app/tests/draft_rules_test.py` and `app/tests/drafts_test.py` (with `latvian_lint.py`) run on every draft file; they must pass before a file is handed over.

| Mistake | Check |
|---|---|
| A setting in front of the question (*At work: which sentence is NOT correct?*) | `draft_rules_test`: no *X: which ...* |
| *Your friend writes: '...' Choose the correct option.* | `draft_rules_test`: banned intro |
| A hint after *Put the words in order* (*Compare two years.*) | `draft_rules_test` and `plain()` in `lib.py`: the instruction is exactly *Put the words in order.* |
| A topic after the matching instruction (*...with its ending: unless.*) | `draft_rules_test` and `plain()` |
| A matching task whose cards can be swapped (*much / a bit* + *faster / heavier*) | `draft_rules_test`: cards that start or end alike are listed and must be read (the list of read exceptions is in the test); the rule above |
| The same question twice under different wording (it would overwrite the first one on re-import) | `draft_rules_test`: same content in two rows |
| A question that repeats a built-in one | `drafts_test`: the importer refuses it |
| Only one of several correct typed answers accepted | read each typed gap: list every correct form (*stops \| has stopped*) |
| Wrong options that are also correct (*had* for *was having*) | the rule above; read every option |
| Forms in italics together with *and* / *or* | `tests/browser/instr_italics.js` |
| Latvian words marked as English, or old terms (*pasīvs*, *divdabis*) | `latvian_lint.py` |
| An explanation cut to one character, or missing | `draft_rules_test`: length check; `drafts_test` |

| A `;` inside a matching pair (it separates the pairs) | `drafts_test` / `tasks_test`: the importer rejects the row |
| A word-order task that has a second correct order (time phrase first, *if*-part second, *and* clauses swapped, *my boss is the man who called you*) | `alt_orders.py` adds them; `tests/orders_test.py`; when writing a new order task, say the sentence aloud both ways |
| A wrong option that is also correct English (*will freeze* after *If water gets very cold, it ___*) | read every option in the sentence; a main-clause blank in a conditional needs distractors that are wrong in that sentence |
| A hint word that is both a verb and a noun (*(film)*) | use a verb that cannot be a noun (*(take)*); read the hint as a learner would |
| A topic's tasks use a form its rule card does not teach (*would* in *used to / be used to*) | every task of a topic uses only the forms on its card |
| A wrong option that is illogical for the question (*Both are about the past* to *what is the difference?*) | make each wrong option a believable mistake |
| A model sentence that is not natural (*Unless you don't hurry*) or an instruction that makes the *correct* option an ungrammatical sentence | ask *Which sentence is NOT correct?* or *Which sentence means the same?* with natural options |
| An inverted-conditional or other word-order task with a missing object (*Had I known* what?) | the sentence must make sense on its own |
| A matching task with a vague instruction (*Match each clause with its meaning*) | name what is matched (*Match each sentence with its tag*) or drop the task |
| A typed task where another correct answer exists (*suggested seeing*, *is starting* for a plan, *Every day the rooms are cleaned*) | name the form in the instruction (*Use the present perfect:*) or list the other answers; contractions, clause order and a fronted time phrase are accepted automatically (`auto_answers.py`, the grader) |
| The same sentence in two topics with different keys (*What time ___ the film ___?*: does / did) | a time word in each (*usually*, *last night*); tested by comparing every typed task |
| A Latvian "reason" for a mistake that has none (*call to me*: Latvian also says *piezvani man*) | say *Tipiska kļūda* and give the English pattern; compare with Latvian only when the Latvian form really causes the mistake |
| A choice or word bank about a missing / extra preposition with no "nothing" option | give **—** (no preposition) as one of the options when the right answer is no preposition |
| A Latvian gloss that translates word for word (*good at = laba kādā jomā*) | say it the Latvian way: *good at maths* = *viņai padodas matemātika* |

## Added 3 November (teacher's review of the twins, batch 1)
- **Exactly one answer fits the instruction and the context.** This replaces "wrong options are always ungrammatical": in *Which sentence has a mistake?* the other options must be correct; in *Choose the most formal option* the others may be grammatical. A tense combination is not wrong in itself (mixed conditionals exist): give the situation that rules the other options out (*We got lost yesterday because we didn't check the map. Imagine the opposite.*).
- **No open gap that several words fit.** *___ you help me?* takes can / could / will / would; *There was ___ much traffic* takes too / so; *play ___ a team* takes for / on. Use a choice with one fitting option, or accept every correct word.
- **Say what to change when several corrections are possible.** *Correct the sentence. Keep "will"*, *Remove one unnecessary word*. A correction that changes the meaning or the structure (*have to* for *must*) is not the answer to a form task.
- **Two gaps: say "one word in each gap"**, and give the direction of a change (*Flights cost more every year. They are getting ___ and ___ expensive.*).
- **Answer keys for typed answers list the contractions the checker cannot work out**: *'d* (had / would) and *'s* in every combination (*If I'd known…, I'd have…*). The checker already accepts *n't* = *not*, *can't* = *cannot*, straight and curly apostrophes, commas and the final full stop.
- **No grammar terms in instructions**, including *the correct preposition*: use *Complete with one word*.
- **The level fits the skill.** Basic *unless*, *as long as*, *wish* + past, *apologise for*, *remind someone to* are B1–B2: at C1 use *But for*, *Were it not for / Had it not been for*, inversion with *Were / Should / Had*, *It's high time* + past, *I'd rather you* + past, *wish* + *could have*, *deny / advise / urge* patterns. Basic forms may stay at C1 only as review.
- **A formal context alone does not make a use task**: choosing the only grammatical sentence of four is recognition, whatever the setting.

## Added 4 November (review of twins batch 2)
- **One twin per source task.** Never clone one sentence frame with new nouns (*the sun / the meeting / the concert had begun when we arrived*): ten near-copies would let a learner reach *Learned* by recognising one frame. Take twins of different source tasks; the generator stops on a second twin of the same source.
- **A word count must not give the answer away.** In a task about choosing a tense, *Complete with one word* rules out *were walking* or *have managed*. Write *Use the verb in brackets:* (or *Use the verbs in brackets:*) and let the situation decide.
- **No tense names in instructions** (*Use the past simple, past continuous or past perfect* is a grammar term too): *Use the verb(s) in brackets:*.
- **Accept only one answer where the task is about that form.** *By the end of the lesson, Eva ___ (answer)* that also accepts *answered* does not test the past perfect: give a situation that needs it (*By the time the bell rang, … so she left early*) and accept only that form.
- **Do not accept forms that change the meaning** (*should know* in a mixed conditional reads as an obligation).
- **Every sentence makes sense**, also the wrong options (*If I had save a copy, I would have kept the original file* is illogical even when corrected).
- **Word-order tasks accept only natural orders.** Two clause orders around *when / while / if* are fine; fronted phrases like *half an hour she spent choosing…* or *all morning what have you been cooking* are not.
- **Different topics or levels do not reuse the same scene** (*it was snowing when we arrived* and *…when we reached the hotel*).

## Learning drag tasks (teacher, 4 November)
- Next to a check / use task, a **new drag task with the same sentence** may be added for learning: a word order, or a word bank with the right words and two extra ones. It is marked *practice only* (`learning_task()` in `_src/lib.py`), so `Content::role` gives *learn*: it is practised in learning mode but never counts as evidence (not in the level test, not in the quick check, not in the ten for *Learned*). The check / use task stays the evidence.
- The same rules apply: only natural word orders (both clause orders around *if / when / because / whatever*), extra words in a bank that do not fit (*won't / had* for *wouldn't have*), the explanation of the task with the same sentence.
- First set: `pending/learn-drag-3.csv` for twins batch 3 (`_src/learn_drag_3.py`). The principle can be applied to every topic.
- Before adding learning tasks, import them next to every prepared file (`php` check as in `docs/AGENT-HANDOVER.md`): a word order with the same sentence as an existing one at another level is taken as the same task and would overwrite it (*despite feeling ill he went to work* already existed at B1.2). Every learning task must import as **new**.

- **A learning task is never a copy.** Its source is a check / use task that is **not** a drag task (a choice, a typed gap, a rewrite); the learning task turns that sentence into a word order or a word bank. Never take a word order, a word bank or a matching task as the source: a drag task with the same sentence and the same type is the same task (nothing new to practise, and the import would overwrite the existing one). Different wording of the instruction does not make it new.
- Before showing samples, check every one against the bank: same sentence + same task type anywhere in `app/content/items.json` or `docs/task-drafts/*.csv` = not allowed.

## No grammar terms, precise prompts (teacher, 6 November)

- A task never needs a grammar term to be solved (*passive, past simple, question tag, adverb, backshift, modal, plural, conditional, preposition* …). The learner must be able to do it without knowing what the term means.
- Instead of the term, the prompt makes the form necessary: a time word or a situation (*yesterday*, *still*, *for weeks*), a frame (*one child, two ___*), or a start (*Start with My wallet*). The prompt is short, precise and easy to take in.
- A start or an example never contains the answer: *Start with My wallet* is fine, *Start with My wallet was* is not.
- When the context allows a second correct form, accept it, and the feedback for that answer explains what it means and how it differs (*answer notes* column): never show "Correct" with an explanation of a different form as if the learner had written that one.
- In Latvian texts the people who use the app are *izglītojamie*, not *skolēni*.
- Scope (teacher, 6 November): only the **task instructions** lose the grammar terms. Explanations (*Why*), answer notes and rule cards keep the grammar words (*present perfect, passive, 3rd form, verb, subject* …): there the learner may meet and learn the names.
- Matching (teacher, 6 November): no two pairs whose meanings could be swapped. *I have just moved here* also means "I didn't live here before", so it cannot stand next to *I lived here … = I don't live here now*. Each right-hand side must fit only its own sentence.

## Word-bank wrong options (teacher, 8 November)
- Gaps may stay one word each, but the bank words must combine into **real tenses / forms**
  (e.g. *We ___ ___ this car since 2018.* → were · have · had · having: *have had* is right, *were having* is a real
  form that does not fit). The learner must know which form the sentence needs.
- No wrong option that can be rejected without knowing the topic: no subject–verb mismatch (*We has*, *We is*),
  no non-existent forms (*is get*), no word of another kind.

## Gates: rules that are tested, and the second reader (teacher, 11 November)
- A rule that a script can measure is a test in `app/tests/item_gates_test.py`; the packaging stops when a **new** task breaks it. Now tested: no grammar term in an instruction; word-bank chips are real forms or common learner mistakes, and agree with the subject; a word order that starts with *should / can / will / is / have …* says *to make a question* (or accepts the statement); *Make a question* says which question; no speaker tag after a quote; a typed sentence accepts *'d*; matching with short labels is read for swappable pairs; *izglītojamie*, not *skolēni*.
- **Wrong forms as wrong answers (teacher, 11 November):** a form that does not exist may be a wrong option or a bank word when it is a **common learner mistake** (*womans, childs, tooths, buyed, didn't used to, more better*): then it is what the task is about. Forms that nobody writes (*wills, coulds, is get, had went, reliabler*) stay out, as decided on 8 November.
- **No speaker tag after a quote, in any task (teacher, 11 November):** not *'I'm working late,' she said.* Say who speaks before the quote (*The guard's request: '…'*) or give the start of the report (*Start with *She said*: '…'*).
- **Reported speech follows the taught rule (teacher, 11 November):** after a past reporting verb the tense goes one step back, and only that form is accepted (*He asked me if I liked jazz*, not *like*), although Murphy (unit 48) allows the present while the situation is still the same. The explanation says why: the step back is always correct; the present is everyday use, and here we practise the rule. Where it is easy, give a situation that has changed (*Ten years ago … Now he drinks it every day*). The tasks that are **about** the tense staying (*The Earth goes round the Sun*) keep it. The rule card's example with a speaker tag (*"I'm working late," he said.*) stays as an exception.
- Findings that existed when a gate was added are in `app/tests/item_gates_baseline.json` (list for the teacher: `docs/task-drafts/pending/gates-known-findings.md`). When a gate flags a task that is fine, read it, then run the test with `--update`; never bend the task to pass.
- Every corrected mistake stays as an example in `app/tests/bad_examples.json`. With `gate`: the test proves the gate still catches it. With `reader`: no script can catch it.
- **Second reader.** Before a draft goes to the teacher, a different agent (not the writer) reads it with one job: for every task, try to find a second correct answer, a swappable pair, a wrong option that is correct English, and check each `reader` case in `bad_examples.json`. Its findings go into the review file next to the tasks.
- **Every report ends in one of three:** a new gate, a new line in `bad_examples.json`, or a note why no rule is needed (the report was not a mistake).
