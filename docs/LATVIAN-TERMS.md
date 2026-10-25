# Latvian grammar terms in the practice app

The Latvian explanations (up to B1.2) use standard Latvian grammar terms where there is one, and short teaching words where learners are used to them. This page says which is which, so a Latvian teacher can review it quickly.

**How it was checked.** By searching Latvian sources (the sources are listed at the end). Only search summaries could be read; the grammar books themselves (for example *Latviešu valodas gramatika*, LU LVI 2013) were not available. Please have a Latvian teacher confirm the table, especially the last section.

## Changed after review

| Was | Now | Why |
|---|---|---|
| aktīvs, aktīva teikums | **darāmā kārta** (darāmās kārtas teikums) | standard term for the active voice |
| pasīvs, pasīva teikums | **ciešamā kārta** (ciešamajā kārtā, ciešamo kārtu, ciešamajai kārtai ...) | standard term for the passive voice |
| priekšmets (alone) | **teikuma priekšmets** in sentences, **teik. priekšmets** in formulas such as `Do / Does + teik. priekšmets + pamatforma` | "priekšmets" alone can be read as a thing; the sentence member is *teikuma priekšmets* |
| jautājuma vārds | **jautājamais vārds** (jautājamo vārdu, jautājamā vārda) | the usual teaching term is *jautājamie vārdi* (jautājamie vietniekvārdi and apstākļa vārdi: kas, kur, kad, kā, cik) |
| netiešajā daļā nav does | **palīgteikumā** nav does | the embedded question is a subordinate clause (palīgteikums) |
| if daļa var būt otrā vietā (rule card) | **nosacījuma palīgteikums (if daļa)** var būt otrā vietā | formal term, with the learner word in brackets |

## New texts (drafts in `docs/task-drafts/`): how they were checked
Every Latvian explanation in the question drafts and the two new rule cards (Modal verbs, Comparison) was written to this page and checked by `app/tests/latvian_lint.py`, which fails on: *pasīvs / aktīvs*, *divdabis* (use **3. forma**), *jautājuma vārds*, *tagadnes / pagātnes ilgstošā forma* (use **Present Continuous / Past Continuous**), *vienkāršā tagadne / pagātne* (use **Present Simple / Past Simple**), *salīdzināmā forma*, *priekšmets* without *teikuma* or *teik.*, and any English word that is not marked as an example. The generator (`docs/task-drafts/_src/lib.py`) rewrites old wording to these terms.

New terms in the Comparison card, **not yet checked by a Latvian teacher**: *pārākā pakāpe* (comparative), *vispārākā pakāpe* (superlative), *īpašības vārds* (adjective), *apstākļa vārds* (adverb). They are the standard terms of Latvian school grammar; please confirm.

New terms in the eight B1 topics (rule cards and drafts), **not yet checked by a Latvian teacher**; please confirm or replace:

| Used in | Term | English |
|---|---|---|
| Articles | **artikuls**, **bez artikula** | article, no article (Latvian has no articles; English lessons in Latvia use the word) |
| Quantity | **skaitāms / neskaitāms lietvārds**, **daudzskaitļa lietvārds** | countable / uncountable noun, plural noun |
| Relative clauses | **attieksmes palīgteikums**; **palīgteikums bez komatiem (vajadzīgs, lai zinātu, kuru)** and **ar komatiem (papildu informācija)** | relative clause; defining / non-defining (described, not named, because textbooks differ) |
| Time clauses | **laika palīgteikums**, **virsteikums** | time clause, main clause |
| Question tags | **tag** (kept in English), **īss jautājums teikuma beigās**; **balss krītas / ceļas** | question tag; falling / rising voice |
| Subject and object questions | **jautājums par teikuma priekšmetu / par papildinātāju**, **jautājamais vārds** | subject question, object question, question word |
| Verb patterns | **darbības vārds ar -ing**, **to + pamatforma**, **prievārds** | verb + -ing, to + base verb, preposition |

New terms in the nine topics of the second batch, **not yet checked by a Latvian teacher**; please confirm or replace:

| Used in | Term | English |
|---|---|---|
| More modals | **modālais darbības vārds**, **atļauts**, **nav vajadzības**, **esmu pārliecināts** | modal verb, allowed, not necessary, I am sure |
| Passive with modals | **modālais darbības vārds + be + 3. forma** (with the standard *ciešamā kārta*) | modal + be + 3rd form |
| Causative | **kāds to dara mūsu vietā** (described, no standard term; the English name *causative* is not used with learners) | someone does it for us |
| Verbs with two objects | **papildinātājs** (already in use), **cilvēks + lieta** | object, person + thing |
| -ed or -ing adjectives | **kas izraisa sajūtu / kā cilvēks jūtas** (described) | what causes the feeling / how a person feels |
| Adjective order | **viedoklis, izmērs, vecums, forma, krāsa, izcelsme, materiāls** | opinion, size, age, shape, colour, origin, material |
| Adverbs | **veida / biežuma / pakāpes apstākļa vārds** (the card says *Veids / Biežums / Pakāpe*) | adverb of manner / frequency / degree |
| So and such | **sekas** | result |
| Someone, anything, nobody | **nenoteiktie vietniekvārdi** is not used on the card (the words themselves are shown); **dubultais noliegums** is not named either | indefinite pronouns, double negative |

## Standard terms already in use (checked, no change)

darbības vārds · noliegums · jautājums · vārdu secība · netiešā runa / tiešā runa · palīgdarbības vārds · palīgteikums · laika palīgteikums · papildinātājs · vienskaitlis / daudzskaitlis · tagadne / pagātne / nākotne

## Teaching shortcuts kept on purpose (please decide)

| In the app | Formal alternative | Note |
|---|---|---|
| **3. forma** (past participle) | ciešamās kārtas pagātnes divdabis (passive) or darāmās kārtas pagātnes divdabis (perfect) | *3. forma* is what English lessons in Latvia use; the formal terms depend on the sentence, so one word fits all tasks |
| **pamatforma** (base verb) | nenoteiksme (without *to*) | in Latvian grammar *pamatforma* is the dictionary form, for verbs the infinitive, so it is close; add "nenoteiksme" if you prefer |
| **if daļa, otrā daļa, abās daļās** | nosacījuma palīgteikums, virsteikums | short learner words; the formal terms are used on the rule cards where it matters |
| **darbības vārds ar -ing / -s** | — | describes the English form; there is no Latvian term |
| **stāvokļa darbības vārdi** (state verbs) | — | teaching term for English *state verbs* |
| **Present Simple, Past Simple ...** | vienkāršā tagadne, vienkāršā pagātne ... | English tense names are kept because learners meet those names in books and tests; Latvian equivalents vary between textbooks |

## Sources used

- [LV TagSet 2.2.4, korpuss.lv](https://korpuss.lv/static/media/LV_TagSet_v.2.2.4_20250301.pdf): *darāmā kārta* and *ciešamā kārta* as verb categories
- [Darbības vārda kārta, Vikipēdija](https://lv.wikipedia.org/wiki/Darb%C4%ABbas_v%C4%81rda_k%C4%81rta) and [Darbības vārda laiks](https://lv.wikipedia.org/wiki/Darb%C4%ABbas_v%C4%81rda_laiks)
- [tezaurs.lv: divdabis](https://tezaurs.lv/divdabis): *ciešamās kārtas pagātnes divdabis*, *darāmās kārtas pagātnes divdabis*
- [LVTB sintaktiskās lomas](https://sintakse.korpuss.lv/docs/v2-16/LVTB_sint_lomas.pdf): *laika (apstākļa) palīgteikums*, *nosacījuma (apstākļa) palīgteikums*, sentence-member functions
- [enciklopedija.lv: Teikuma loceklis](https://enciklopedija.lv/skirklis/249767-teikuma-loceklis): sentence members (subject, predicate, complement, modifier, adverbial)
- [valoda.ailab.lv: Jautājamie vietniekvārdi](http://valoda.ailab.lv/latval/vidusskolai/morfol/vietn-jaut.htm) and [uzdevumi.lv: Jautājamie vietniekvārdi](https://www.uzdevumi.lv/p/latviesu-valoda/6-klase/vietniekvards-2922/re-47a5de96-1137-45e3-9579-c6705d1779f6)

## Latviski → Angliski tasks (teacher's decisions, 25 October)
- A matching task is called **savienošana** in Latvian (not *saskaņošana*).
- When the Latvian sentence has a time phrase that the English sentence does not have, put it **in brackets at the end** of the Latvian sentence (*Viņš spēlē tenisu. (tieši tagad)*), or translate the whole sentence with the time phrase in both languages.
