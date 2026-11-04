# Darba pārskats: twins-2

Datums: 2026. gada 4. novembris (Rīga).
Zars: `agent/twins-2`.
Sākumpunkts: `claude/intelligent-albattani-2e9bfi`, komits `e99462bcffe237d1088561482379e86d143eda1c`.
Izlasīti `docs/AGENT-HANDOVER.md`, `docs/ITEM-WRITING-RULES.md` un `docs/LATVIAN-TERMS.md`.
Repozitorijā netika atrasts `AGENTS.md`.

## Rezultāts

Sagatavoti 50 dvīņi 16 tēmu un līmeņu pāriem. Tie paliek `pending/` un gaida Ingas pārskatu.
Nav mainīti publicētie uzdevumi, 1. partija, lietotnes darbība, vērtētājs vai skolēnu dati.
Nav veidota pakotne, izvietojums vai pull request; nav veiktas darbības WordPress vai Hostinger.

Sadalījums: 16 izvēles, 20 vārdu secības uzdevumi (40% vilkšanas), 8 rakstāmu tukšumu un 6 teikuma rakstīšanas uzdevumi.
Īstais `Content::role` klasificē tos kā 36 `check` un 14 `use`; nav `learn` uzdevumu.
Katram dvīnim saglabāta oriģināla tēma, līmenis un uzdevuma veids. Pārskatā ir oriģināla fails un rinda vai ID,
instrukcija, atslēga un varianti; dvīnim norādīta instrukcija, visas pieņemtās atbildes, varianti un EN/LV skaidrojumi.

## Faili

| Fails | Izmaiņa |
|---|---|
| `docs/task-drafts/_src/twins_2.py` | Atkārtojams ģenerators; pārbauda oriģinālu saites, veidus, līmeņus, sadalījumu un alternatīvo kartīšu vārdus. |
| `docs/task-drafts/pending/twins-2.csv` | 50 importējamu melnrakstu; nav aizstāšanas norāžu. |
| `docs/task-drafts/pending/twins-2-review.md` | Pilns pārskats Ingas vērtējumam. |
| `app/tests/twins_2_test.php` | Izolēts integrācijas tests ar atmiņas datubāzi, īsto importētāju un vērtētāju. |
| `docs/task-drafts/_src/lib.py` | Tikai konkrētajam failam piesaistīta latviešu vārdu vārdnīca, lai LV vārdi netiktu rādīti kā angļu piemēri. Veco failu marķējums nemainās. |
| `app/tests/latvian_lint.py` | Pārbaude izmanto to pašu konkrētā faila vārdnīcu. |
| `docs/AGENT-REPORT-twins-2.md` | Šis pārskats. |

## Kāpēc atlase atšķiras no small_banks.py izdrukas

`tools/small_banks.py` dažus īsos tēmu nosaukumus nepiesaista to pilnajiem nosaukumiem un ID.
Tādēļ pirms rakstīšanas pārbaudīju skaitu arī ar īsto importētāju: visi sagatavotie CSV un 1. partija tika importēti
izolētā atmiņas datubāzē. Tika saskaitīti `Content::role` pierādījuma uzdevumi, apvienojot tēmas pēc faktiskajiem ID.
Piemēram, `verb_patterns/A2.2` jau bija 21, `comparison/A2.2` bija 16 un `modal_verbs/A2.2` bija 23 uzdevumi.
Šiem pāriem 2. partijā dvīņi nav pievienoti. Pats plānošanas skripts nav mainīts.

| Faktiskā tēma | Līmenis | Pirms 2. partijas | Jauni | Pēc simulēta importa |
|---|---|---:|---:|---:|
| narrative | B1.2 | 5 | 5 | 10 |
| cond_mixed | B2.1 | 6 | 4 | 10 |
| rep_verbs | B2.2 | 6 | 4 | 10 |
| ind_advanced | C1.1 | 6 | 4 | 10 |
| cmp_ps_pc | B1.1 | 6 | 4 | 10 |
| cond_third | B2.1 | 6 | 4 | 10 |
| rep_questions | B2.1 | 6 | 4 | 10 |
| aux_verbs | B1.1 | 7 | 3 | 10 |
| articles | B1.2 | 7 | 3 | 10 |
| cmp_ps_pc | A2.2 | 7 | 3 | 10 |
| narrative_b2 | B2.1 | 7 | 3 | 10 |
| cmp_pp_ps | B1.1 | 7 | 3 | 10 |
| cmp_pp_ps | A2.2 | 8 | 2 | 10 |
| narrative_b2 | B2.2 | 8 | 2 | 10 |
| narrative | B1.1 | 9 | 1 | 10 |
| comparison | B1.2 | 9 | 1 | 10 |

Šie ir plānošanas skaitļi, pieņemot arī 1. partijas importu, nevis apgalvojums par pašreizējo serveri vai skolēnu apguvi.

## Pārbaudes

| Pārbaude | Rezultāts |
|---|---|
| Ģeneratora izpilde | 50 oriģinālu saites, 16 pāri; visi alternatīvo secību vārdu komplekti sakrīt. |
| `php tools/check_draft.php docs/task-drafts/pending/twins-2.csv` | 50 pieņemti, 0 noraidīti; 90 rakstāmo atbilžu varianti, 0 noraidīti. |
| `php app/tests/twins_2_test.php` | 50 jauni uzdevumi; 0 dublikātu, 0 aizstāšanu, 0 brīdinājumu; atkārtots imports nemaina ierakstus. 252 vērtēšanas gadījumi, 0 kļūdu. |
| Iepriekšējā testa pārklājums | Visas vairāku tukšumu kombinācijas, pieņemtās kartīšu secības, MCQ nepareizo variantu noraidīšana, kļūdainas ievades kontrolpiemēri; visi 16 pāri sasniedz tieši 10. |
| `python3 tools/option_audit.py docs/task-drafts/pending/twins-2.csv` | 0 atzīmētu problēmu. |
| Rakstīšanas noteikumu tests ar nodošanas dokumentā paredzēto `pending/` ceļa aizstāšanu | 126 uzdevumi abās partijās, 0 problēmu. |
| Latviešu valodas pārbaude ar tādu pašu `pending/` ceļa aizstāšanu | 0 problēmu. |
| Esošo melnrakstu `latvian_lint.py`, `draft_rules_test.py`, `orders_test.py` | 0 problēmu; 2548 uzdevumi; `ALL PASS`. |
| `git diff --check` | Bez kļūdām. |

Pilnā `run_all.sh` kopa tika palaista. PHP/Python daļa iziet: grader, selfgrade, selfgrade_drafts,
error_model, bank_update, orders, sso, security, research, reports, tasks, comeback, drafts,
placement, pulse, probe, reword un draft_rules. Tas ietver 2548 esošo uzdevumu atbilžu pārbaudi.

Vide: macOS, instalētais MAMP PHP 8.3.9, Python 3.9 un Node 26. Pagaidu testu kopijās ārpus repozitorija
tika pielāgoti Linux absolūtie ceļi, Playwright moduļu atrašanās vieta un `timeout` palaišana.
Pārlūka testi nav atzīmēti kā izturēti: Chrome/Playwright palaišana beidzas ar `SIGABRT` vēl pirms lapas atvēršanas.
Tā kā `run_all.sh` cauruļvadi ne vienmēr nodod apakšprocesa kļūdas statusu, rezultāts izvērtēts pēc katras rindas,
nevis pēc pēdējā `FINISHED`. Lietotnes un repozitorija pārlūka testi šī ierobežojuma dēļ nav pārveidoti.

## Pētījuma dati

Pašlaik nav izmaiņu uzdevumu pasniegšanā vai vērtēšanā: `pending/` netiek iekļauts sagatavotajos jautājumos.
Pēc Ingas apstiprinājuma un vēlākas publicēšanas banka paplašināsies; tad jāreģistrē publicēšanas datums
`RESEARCH-DATA-PLAN.md` sadaļā Changes. Iepriekšējās atbildes un rezultāti netiek pārrakstīti.

## Atvērtais

- Ingas pedagoģiskais pārskats un apstiprinājums. CSV nepārvietot, kamēr tas nav saņemts.
- Murphy pilnais teksts repozitorijā nav pieejams; nepiesaku pārbaudi pret pilnu grāmatu kā pabeigtu.
  Izmantoti esošie uzdevumi un kartīšu tvērums; oriģinālu kļūdainās instrukcijas nav pārnestas.
  Struktūras papildus salīdzinātas ar Cambridge un British Council primārajiem skaidrojumiem:
  [netiešā runa](https://dictionary.cambridge.org/grammar/british-grammar/indirect-speech-reporting-questions),
  [jautājumu un lūgumu atstāstīšana](https://learnenglish.britishcouncil.org/free-resources/grammar/b1-b2/reported-speech-questions),
  [pagātnes laiku izvēle](https://dictionary.cambridge.org/grammar/british-grammar/past-continuous-),
  [jauktie nosacījuma teikumi](https://learnenglish.britishcouncil.org/free-resources/grammar/b1-b2/conditionals-third-mixed).
- Pārlūka testus atkārtot vidē, kurā Playwright var palaist Chromium.
- Pēc abu partiju simulēta importa paliek 9 nepietiekami tēmu un līmeņu pāri ar 33 trūkstošiem uzdevumiem:
  `cond_mixed/B2.2`, `cond_mixed/C1.1`, `rep_statements/B2.1`, `rep_questions/B2.2`,
  `rep_verbs/C1.2`, `ind_advanced/B2.2`, `ind_advanced/C1.2`, `conj_linkers/B1.1` (pa 4),
  `articles_b1/B1.2` (1). Pēc tiem nāk servera Usage → Repeats atlase; serveris šajā darbā nav atvērts.
- `small_banks.py` nosaukumu normalizācija ir atsevišķs turpmāks labojums.

Atkārtošana:

```bash
python3 docs/task-drafts/_src/twins_2.py
php tools/check_draft.php docs/task-drafts/pending/twins-2.csv
php app/tests/twins_2_test.php
python3 tools/option_audit.py docs/task-drafts/pending/twins-2.csv
python3 app/tests/latvian_lint.py
python3 app/tests/draft_rules_test.py
python3 app/tests/orders_test.py
```
