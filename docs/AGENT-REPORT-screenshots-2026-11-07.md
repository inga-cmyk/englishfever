# Ekrānattēli un 27 ziņotie uzdevumi — 2026. gada 7. novembris

Sākuma kods: `claude/intelligent-albattani-2e9bfi` (sākuma komits `cea0fea4dd204d8276324bcafcdbb62548ddc384`). Darba kopija: `practice-app-work`. Dzīvajā vietnē lasīšanas režīmā pārbaudīta Reports lapa, versija **2026-11-06 14:06**. Tur visi 27 ziņojumi ir atvērti, uzdevumi apturēti. Vecās versijas var būt vēsturiskā ziņojuma saturs; ziņojums viens pats neapstiprina aktīvās jaunās versijas izvietošanu.

## Lietotnes labojumi

- Pēc parastas, Second Chance un līmeņa testa sērijas vairs nav Skills check. Tā vietā ir īss mainīgs uzmundrinājums. Prasmju analītika citos skatos saglabāta.
- Telefona sērijas rezultāti ir vienā kompaktā rindā; tie vairs neaizņem gandrīz visu ekrānu.
- Second Chance ar 100% pareizu atbilžu un bez jauna `fixed` skaita saņem atbilstošu pozitīvu virsrakstu.
- `nothing left to fix` netiek secināts no tā, ka nav nākamās tēmas. Kopsavilkums atšķir atvērtas kļūdas no vēlākas pārbaudes rindas.
- Sekmīgs tā paša teikuma atkārtojums neapliecina pārnesi uz jaunu teikumu, tomēr atliek tā atkārtotu piedāvāšanu par divām dienām. Dažāds uzdevums citā dienā joprojām var nostiprināt kļūdu. Citas rindā palikušās kļūdas nav dzēstas.
- Saglabātā līmeņa testa atskaite ar kļūdām vairs neapgalvo `No mistakes to fix`. Tajā paskaidrots, ka tas ir saglabāts rezultāts un pašreizējā atkārtošana redzama Home.
- Pie pareizi ievadītas alternatīvas redzama paša atbilde; parauga variants marķēts kā `Also possible`. Tom un virtuves krāsošanas uzdevumi saņem konkrētu alternatīvas skaidrojumu.
- Pareiza `had worked` atbilde šajā `narrative_b2` tipa ierakstāmā uzdevumā saglabā pareizo vērtējumu un XP, bet pati par sevi neaizver/nenostiprina kļūdu par `had been ... -ing`. Kļūdu aprēķins ir konservatīvāks; vēsturiskās atbilžu rindas nav pārrakstītas.
- Tēmas uzdevums un jaukta atkārtošana ir skaidrāk nošķirti ar `Review · mixed topics`. Lokālais integrācijas tests apstiprina, ka apzināti izvēlētais solis paliek savās tēmās. Vecā konkrētā sērija no attēliem netika rekonstruēta.
- Atsauksmes panelis ar pogu ietilpst ekrānā; iPhone bloķēto ievades lauku teksts saglabā tumšu, salasāmu krāsu.
- Komentāra ievades laikā Continue ir atspējota; pēc Send vai Cancel atkal pieejama.
- CSV importā saglabājas dialoga rindu pārnesumi.
- `I have ___ it` formu savienošanas uzdevumā `go → gone` nomainīts uz `break → broken`; izlabots angļu `3. form` formulējums. Vecās formas radīja negramatisko `I have gone it`.

## Visi 27 ziņojumi

| Nr. / ID | Pārbaudes secinājums un darbība |
|---|---|
| 1 c-0091 | Tagad pieņemta arī London/Riga pretējā secība: tiek vērtēta teikuma uzbūve. Paskaidrojums EN/LV pasaka, ka tas nav ģeogrāfijas tests. |
| 2 ps-A22-2a-r2 | Jauna pārskatīta versija: visi varianti ir pilni gramatiski teikumi ar atiešanas laiku; jāatšķir saraksts, cerība, pagātne un pašlaik notiekošais. Tas ir nozīmes atpazīšanas, nevis patstāvīgas formas uzrakstīšanas uzdevums. |
| 3 c-1022 | Pievienots skaidrs nākotnes norunāta pasākuma konteksts. Maldinātāji ir gramatiski veidotas formas (`have had / had / were having`), nevis `are have / will having`. |
| 4 c-1006 | Noņemta acīmredzamā vārdu banka. Jāieraksta forma no `win`, ar laika norādi `The final is tomorrow`. |
| 5 c-2058 | Savienošana pārstrādāta: jāsavieno teikums ar konkrētu secinājumu par pabeigšanu/turpināšanos. Vairs nav pārklājošos activity/result/how long/how many kategoriju. Atzīmēts `practice only`. |
| 6 fu-B12-6a | Jauna konkrēta situācija: tumši mākoņi, draugam nav lietussarga, jāprognozē un jāpiedāvā palīdzība. Vecā atbilde bija plāns, nevis prasītā prognoze, un saturēja `wll`; tā netiek automātiski pārskaitīta par pareizu. Brīvās rakstīšanas pārbaude joprojām ir ierobežota; AI pārbaude dzīvajā vietnē šajā darbā netika pārbaudīta. |
| 7 c-1015 | Labots EN/LV paskaidrojums tieši par `when + finish/have finished`; izņemts nesaistītais going to jautājuma skaidrojums. Pareizā sākotnējā atbilde saglabājas. |
| 8 c-1001 | Instrukcija tagad skaidri prasa jautājumu; pieņem jautājuma abas daļu secības, vairs ne apgalvojumu. Iepriekšējais apgalvojuma vērtējums netiek pārrakstīts. |
| 9 c-3215 | Situācija mainīta uz `I've hurt my hand`; B replika jaunā rindā. `did / do` saglabājas pareizi. |
| 10 ps-A21-5a-r2 | Atslēga pareiza: pēc does pamatforma `work`. Nav pamata labot vērtējumu. |
| 11 c-1027 | Pašreizējā failā nav `Why did you stay` pareizā/ nepareizā precīzā pāra. Visi varianti ir līdzīgas uzbūves pagātnes jautājumi; `did you stayed` ir vienīgā kļūda. Papildu izmaiņas nav vajadzīgas. |
| 12 c-2244 | Claude kodā jau pārstrādāts `contrast-1.csv`: `I ___ to Paris twice. The last time I ___ there was in May.` |
| 13 c-2246 | Atslēga dotajām atbildēm pareiza. Claude kodā trešais pāris jau mainīts uz `I have never lived in a big city → Not at any time in my life`. Atsevišķa jauna izmaiņa nav vajadzīga. |
| 14 c-2713 | Gaidītajā Where jautājumā jāaizstāj `in London`. Claude skaidrojums jau pasaka, kāpēc to izlaiž. Atbilde `where ... in London` jautā par vietu Londonas iekšienē; tā neatbilst paredzētajai informācijas aizstāšanai. |
| 15 c-1321 | Claude kodā situācija jau mainīta uz `get used to ___ from home (work)` → `working`. Vecajā uzdevumā `use` pamatoti nepareizs. |
| 16 ip-B12-2a-r2 | Claude jaunā versija r3 pārbauda pašu jautājuma secību, nevis teorijas atstāstīšanu. |
| 17 ca-C12-2a | Claude jaunā r2 versija ir formas ievietošanas uzdevums `I wish you ___ clicking your pen ...` → `would stop`. |
| 18 ia-C12-3a-r2 | Claude r3 versija precizē sākumu `Who...`; `Whoever calls, don't answer` un izvērstie varianti pieņemti. |
| 19 c-2848 | Claude `conjunctions-1.csv` jau ir vārdu bankas uzdevums ar `Therefore` teikuma sākumā. Vecajai atbildei trūka teikuma robežas un tā neievēroja norādīto pozīciju. |
| 20 rv-C11-3a-r2 | `on winning` bija pareizi un novērtēts pareizi. Precīzā vēsturiskā versija jau atgūta; jaunā r3 ir vārdu banka. |
| 21 c-2214 | Atbilde ir gramatiska, bet samaina nosacījumu un sekas. Claude to jau aizstājis ar ierobežotu `Had / left` vārdu banku. |
| 22 c-2731 | Atvērtā instrukcija ar laiku nosaukumiem Claude kodā jau aizstāta ar vārdu banku `had been waiting` u.c. `waited` nav automātiski pieņemts kā paredzētās iepriekš ilgušās darbības pierādījums. |
| 23 ia-C11-2a-r2 | Claude r4 pārbauda `The decision depends on ___ ...` → `whether`, nevis abstraktu teorijas nosaukšanu. |
| 24 cm-C11-1a-r3 | Claude r5 dots faktiskais pagātnes nosacījums un pašreizējās sekas; jāatrod tās pašas nozīmes teikums. |
| 25 rq-B21-2a | Claude r2 instrukcija pirms citāta; `told me not to touch` paskaidrots. |
| 26 rs-B21-1a-r2 | Claude r3 pārbauda konkrētā `I might be late` atstāstījumu; nav modal/backshift terminu jautājuma. |
| 27 ps-B11-2a-r3 | Claude r4 jau ir `Water ___ at 100 degrees Celsius` → `boils`; novērsts atšķirīgās tematikas norādījums. |

## Pārbaudes un ierobežojumi

- 44 telefona UI pārbaudes (320/390 px, EN/LV): izkārtojums, ievade, iepriekšējās atbildes, komentāra aizsardzība, jaunais kopsavilkums.
- 15 atsevišķas UI pārbaudes par alternatīvo atbildi, 100% Second Chance un līmeņa testa atskaiti. Saglabāti priekšskatījumi.
- 20 reālā CSV importētāja/vērtētāja pārbaudes; četros failos nav noraidītu rindu.
- 4 Second Chance plānošanas pārbaudes; 13 iepriekšējās konstrukciju pārbaudes.
- 483 iebūvēto jautājumu vērtēšana; 3341 vēstures, integrācijas un vārdu vilkšanas pārbaude; 46 ziņoto uzdevumu pārbaudes; 2830 CSV uzdevumos 0 pārbaudes kļūdu.
- Mācību ceļa integrācijas tests: 11 pārbaudes, visas veiksmīgas, arī izolēta izvēlēta tēma un jauktā atkārtošana.
- Visi 10 jaunie CSV labojumi saglabājas ģeneratora labošanas slānī; dialogam pārbaudīts arī reālais imports.
- PHP sintakse un JavaScript sintakse pārbaudīta. Testi izpildīti PHP 8.5 lokāli; uz dzīvo serveri nekas nav izvietots. iPhone Safari īpatnības jāpārbauda pēc izvietošanas; izmantoti Chromium telefona izmēri.

Nav veikta augšupielāde, CSV imports, jautājumu apstiprināšana vai Reports statusu maiņa dzīvajā vietnē. Avota kods sagatavots ievietošanai tajā pašā Claude darba zarā pēc Ingas pieprasījuma. GitHub problēmas nav aizvērtas.
