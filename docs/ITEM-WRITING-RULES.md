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
