# Blind check c1-2b: flags for the judge

4 tasks, 2 readers.

## c1-2b-001 · C1 · gap · c1-pres-2.csv:2

Task: Write one word in each gap: So I'm at the bakery, I ___ ___ in the queue, and this woman suddenly ___ round and hands me her dog. (stand, turn)
Key: {"kind": "gap", "accepted": [["am", "'m"], ["standing"], ["turns"]]}
- reader 1: instruction: Does not say the gaps are in the present (anecdote) tense; the learner must infer from 'So I'm at the bakery'. Gap count is unclear: 'I ___ ___' is two gaps, so 'I'm' (one typed word) vs 'am' needs a ruling. Fairly easy for C1 once the present is seen.
- reader 1: level: Present-tense storytelling is a nice C1 point, but the sentence is simple vocabulary; a B1 learner could solve it.
- reader 2: another correct answer, not accepted: [['was', 'standing', 'turned'], ['stand', '', 'turns']]
- reader 2: instruction: Three gaps for two verbs, and the instruction says 'one word' but 'I'm' is one typed token; learner may type "'m". Hint (stand, turn) does not say which tense. Past-tense version (was standing / turned) is also correct English but clashes with the present opening 'I'm at the bakery'; list it.
- reader 2: level: Narrative present is more B2 than C1; no C1 nuance, solvable by a B1/B2 learner.

## c1-2b-002 · C1 · mcq · c1-pres-2.csv:3

Task: Which sentence has a mistake?
options: So I'm sitting on the train, and this man opens a bag of crisps. | We're having dinner when all the lights go out. | Then the waiter looks at him and says, "Are you sure?" | So this man is walking into a café and he orders a glass of milk.
Key: {"kind": "mcq", "correct": "So this man is walking into a café and he orders a glass of milk.", "wrong": ["So I'm sitting on the train, and this man opens a bag of crisps.", "We're having dinner when all the lights go out.", "Then the waiter looks at him and says, \"Are you sure?\""]}
- reader 1: a wrong option that fits: We're having dinner when all the lights go out. (continuous + 'when' + simple is correct in narration, and is also natural; if the key marks the 'is walking' one only, this one is a risk). The 'walking' sentence is also arguably fine: 'a man is walking into a café' is acceptable as a joke setup.
- reader 1: instruction: No context says these are anecdote/joke narration, so several options can be defended.
- reader 1: sense: The intended mistake (continuous instead of simple for a completed event in a story) is borderline, not a clear error; a learner could not tell which is wrong. 'We're having dinner when...' reads like a mistake to some, so the options are not clearly separable.
- reader 2: level: Present continuous vs simple in anecdotes is B1/B2 form-focus, not C1 use/nuance.
- reader 2: sense: Option 4 'is walking into a café and he orders' is believable but the others are all fine; a native might accept 'is walking into' in very casual telling, so the mistake is slightly arguable.

## c1-2b-003 · C1 · gap · c1-pres-2.csv:7

Task: The app ___ to work on my phone. Can you check it? (not / appear)
Key: {"kind": "gap", "accepted": [["doesn't appear", "does not appear", "didn't appear", "did not appear", "appears not"]]}
- reader 1: another correct answer, not accepted: [["isn't appearing"], ["hasn't appeared"]]
- reader 1: instruction: Ambiguous: the verb hint '(not / appear)' gives no tense or meaning cue; 'doesn't appear to work' (seems not to) and 'isn't appearing' are both possible, and 'is not appearing to work' sounds odd. One gap but two words typed; say whether contractions are accepted. The sentence does not make clear that the point is state-vs-action use of 'appear'.
- reader 1: level: 'appear to' = 'seem to' is C1-ish, but the task as written could be solved at B1 with the simple present.
- reader 1: sense: 'isn't appearing to work' is a plausible learner error but is unnatural; the context does not force the simple form.
- reader 2: instruction: '(not / appear)' gives the negative and verb; only the tense/auxiliary is tested. 'appears not' (one gap, one word) is correct but formal.
- reader 2: level: 'appear to' with a negative is fine for C1 but the form is easy.

## c1-2b-004 · C1 · gap · c1-pres-2.csv:8

Task: My sister and her husband ___ their first baby next month. (expect)
Key: {"kind": "gap", "accepted": [["are expecting", "'re expecting"]]}
- reader 1: another correct answer, not accepted: [['will be expecting'], ['are going to expect']]
- reader 1: instruction: Context ('next month') alone does not fix the tense; 'will be expecting' is also correct English (less natural for a future baby; fine for 'will be expecting a baby by then'). Simple 'expect' alone is wrong.
- reader 1: level: 'are expecting a baby' is B1 vocabulary and present continuous for future; too easy for C1.
- reader 2: another correct answer, not accepted: [['will be expecting']]
- reader 2: instruction: Number of gaps/words not stated (one gap, two words); 'next month' makes present continuous obvious.
- reader 2: level: Too easy for C1: present continuous for future arrangement is B1; a B1 learner can solve it.

