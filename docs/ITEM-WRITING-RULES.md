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
