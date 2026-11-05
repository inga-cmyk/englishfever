# Ingas ekrānuzņēmumu un 14 atgriezto jautājumu labojumi

2026. gada 5. novembris. Zars `agent/fix-feedback-and-reported-items`, sākums `4789d152516d93dffee897154683c52390d798d6` no `claude/intelligent-albattani-2e9bfi`.

## Lietotnes uzvedība

- *used to do* un *be/get used to doing* vairs neaizstāj cits citu kļūdas izlabošanā, nostiprināšanā vai atkārtotā atvēršanā. Tas attiecas arī uz `for_item` un līdzīgo uzdevumu atlasi. Jauktas vai neatpazītas konstrukcijas netiek izmantotas kā citas konstrukcijas apguves pierādījums.
- Mācīšanās uzdevumi (`learn`) neietilpst kļūdu pierādījumu aprēķinā. Paplašināta nozīmes jautājumu atpazīšana ar “What does it/this/that say/mean?”.
- Vēlākai pārbaudei neizvēlas teikumu, kas jau kalpojis kļūdas izlabošanai. Ja citas piemērotas versijas nav, var atgriezt sākotnējo teikumu citā dienā. Tā paša teikuma atkārtošana tajā pašā dienā kļūdu neizlabo.
- Jau saglabātais sesijas `slot` tiek nodots arī pārlūkam. Atkārtošanas uzdevumam redzams *Review*, nākamā soļa uzdevumam *Next step*. Atlases proporcijas un tēmu secība nav mainītas.
- *Strengthen the basics* paskaidro, ka nesenās atbildes liecina par vajadzību atkārtot konkrēto tēmu un vispārējais līmenis nav mainījies.
- Kategoriju kopsavilkumā ir atbilžu skaits un *Not checked*, ja kategorijā nav atbilžu. Paskaidrots, ko šīs sesijas rezultāts ļauj secināt par teikumu rakstīšanu.
- Pilna teikuma ievade ir augošs vairākrindu lauks. Arī pareizi iesniegtā atbilde pilnībā redzama atsauksmē. Telefona platumā sesijas vadība un garie tēmu nosaukumi aplaužas rindās; *Stop* paliek redzams.
- *used to go* ezera uzdevumam tagad ir konkrētā ieraduma paskaidrojums EN un LV.

## Visi 14 jautājumi

| Nr. | Atsauksmē dotais ID | Rezultāts |
|---|---|---|
| 1 | c-2727 | Tenisa teikums tagad ir vārdu bankas uzdevums. Pareizi *had been playing*; pārējie varianti *have been playing / had been played / had playing*. Instrukcijā nav laiku nosaukumu. Imports arhivē tieši atsauksmē doto veco uzdevumu. |
| 2 | ip-B12-2a-r2 | Jaunais `ip-B12-2a-r3`: *Could you tell me ___?* Pareizi *where the station is*; varianti kļūdās vārdu secībā un jautājuma veidošanā. EN un LV paskaidrojumi. |
| 3 | c-3101 | *It's high time we ___ home. The last bus leaves in ten minutes.* Pareizi *went*; *have gone / will go / had went*. Nav mākslīgā *to going*. Jaunais formulējums ļauj importā arhivēt veco versiju. |
| 4 | ca-C12-2a | Jau izlabots sākuma zarā: `ca-C12-2a-r2`, *I wish you ___ clicking your pen. It's driving me mad.* → *would stop*. Saglabāts. |
| 5 | ia-C12-3a-r2 | Jau izlabots: `ia-C12-3a-r3`, *Write one sentence that starts with Who…*. Pieņem *Whoever calls, don't answer / do not answer*. Vecā versija paliek vēsturē. |
| 6 | c-2848 | Jau izlabots `conjunctions-1.csv`: *Sales fell. ___, we have decided to close the shop.* → *Therefore*. Imports aizstāj veco stingri ierobežotās izvietošanas uzdevumu. Atsauksmē dotais teikums neatbilda vecajai instrukcijai un tam trūka teikuma robežas; vecais vērtējums netiek pārrēķināts. |
| 7 | rv-C11-3a-r2 | Precīzā vēsturiskā versija atgūta no Git komita `b98e16c`, iekļauta publicēto versiju arhīvā. Atsauksmē atkal pieejams oriģinālais uzdevums ar *on winning*. Jaunajiem uzdevumiem paliek jau izlabotais `rv-C11-3a-r3` ar *on*. |
| 8 | c-2214 | Jau izlabots `a2-forms-1.csv`: *___ she ___ earlier, she would have caught the train.* → *Had / left*. Vecā atbilde ir gramatiska, bet maina nosacījumu un sekas; vecais vārdu kārtošanas uzdevums šo atšķirību nepietiekami ierobežoja. |
| 9 | c-2731 | Autobusa teikums tagad ir vārdu bankas uzdevums: *had been waiting / have been waiting / had been waited / had waiting*. Pareizi pirmais. Vairs nav atvērta laika izvēle ar garu teorijas instrukciju. |
| 10 | ia-C11-2a-r2 | Precīzais oriģināls atgūts no `b98e16c`; arhivēta arī sākuma zarā aktīvā `-r3`. Jaunais `ia-C11-2a-r4`: *The decision depends on ___ the budget is approved.* → *whether*. |
| 11 | cm-C11-1a-r3 | Jaunais `cm-C11-1a-r5`: dots fakts *I did not take that job, so I am not rich now* un jāizvēlas teikums ar to pašu nozīmi. Visi varianti ir pilni teikumi; maldinātāji maina laiku, noliegumu vai cēloņsakarību. Saglabāta arī precīzā `-r3` vēsture. |
| 12 | rq-B21-2a | Jaunais `rq-B21-2a-r2`: instrukcija pirms citāta, bez pievienota runātāja taga. Atsauksme paskaidro *told me not to touch*. |
| 13 | rs-B21-1a-r2 | Jaunais `rs-B21-1a-r3`: jāatstāsta *I might be late*. Pareizi *She said she might be late*. Netiek prasīti termini *modal* un *backshift*. |
| 14 | ps-B11-2a-r3 | Jau izlabots sākuma zarā: `ps-B11-2a-r4`, *Water ___ at 100 degrees Celsius.* → *boils*. Saglabāts. |

## Pārbaudes

- `python3 app/authoring/build.py`: 483 aktīvi uzdevumi, 265 arhivētas versijas, 58 tēmas.
- Pilnais `app/tests/browser/run_all.sh` komplekts izpildīts. Pēc mācīšanās uzdevumu izslēgšanas divi testi vēl pieņēma iepriekšējos kļūdu skaitīšanas noteikumus; tie pielāgoti un izpildīti atkārtoti: `probe_test.py` un `comeback_ui.js` tagad **ALL PASS**. Pārējās komplekta pārbaudes izgāja pilnajā skrējienā.
- `mistake_construction_test.php`: **13 pārbaudes**, ieskaitot neatbilstošu `for_item`, mācīšanās uzdevumu, atvēršanu un nostiprināšanu citā dienā.
- `reported_drafts_test.php`: trīs precīzie vecie uzdevumi arhivēti, jaunie atbilžu varianti pieņemti, otrais imports neveido kopijas.
- `bank_update_test.php`: **2955** vēstures un integrācijas pārbaudes.
- `mobile_feedback.js`: **32 pārbaudes**, 320 un 390 px, EN un LV. Pārbaudīts atkārtošanas marķējums, *Stop*, augošais lauks, visa iesniegtā atbilde, iepriekšējo atbilžu skatīšana un *Not checked*. EN un LV ekrānuzņēmumi vizuāli apskatīti; tie ir testa dati ar API imitāciju.
- Trīs mainīto CSV importa pārbaudes: attiecīgi **60 / 9 / 142 pieņemti, 0 atteikti**; ierakstāmo atbilžu variantiem **0 atteiktu**.
- `draft_rules_test.py`: **2789 jautājumi, 0 problēmu**. `latvian_lint.py`: **0 problēmu**.
- `option_audit.py`: mainītajām rindām nav jaunu norāžu. Izlasītas četras norādes par jau esošām nemainītām rindām: *Which sentence has a mistake?* piedāvā gramatiski pareizos pretpiemērus, bet trīs formas uzdevumos visas izvēles atbilst vienam teikumam.
- JavaScript sintakse pārbaudīta. CSV saglabā to ģeneratoru CRLF formātu; Git whitespace pārbaudē CRLF tiek uzrādīts kā rindas beigu atstarpe.

Testos atjaunināti pilnu teikumu lauka selektori un noņemti ar konkrētu izstrādātāja mapi saistīti failu ceļi. Kļūdu aprēķina testi tagad nošķir mācīšanās uzdevumus un atkārtojumu tajā pašā dienā. `probe_test` pārbauda pašreizējo noteikumu: pēc atkārtotas kļūdas tiek reģistrēta vajadzība atkārtot, nepalielinot sesijas garumu.

## Ietekme uz pētījumu un nodošana

Vēsturiskās atbilžu rindas, XP un līmeņu ieraksti netiek mainīti. No vēstures aprēķinātie *fixed / locked / reopened* rādītāji var kļūt konservatīvāki. Divi iepriekš ierakstāmie B2 uzdevumi tagad piedāvā izvēli, tāpēc šo versiju rezultātus nevar pielīdzināt patstāvīgai formas uzrakstīšanai. Izmaiņa ierakstīta `RESEARCH-DATA-PLAN.md`.

Darbs ir pārskatīšanas zarā. Pārskatīt diff pret sākuma komitu, tad sagatavot ZIP no apstiprinātajiem labojumiem. Pēc Ingas veiktas augšupielādes: **Prepared questions → Add all → Approve all**, lai stātos spēkā sagatavoto uzdevumu labojumi. Šajā darbā nav izvietošanas, WordPress izmaiņu, PR vai sapludināšanas.
