import sys,json,re,collections,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import classify as C, p4
import review as R
P=C.P; BY=C.BY; items=C.items
res=collections.defaultdict(list)
for _i in items: res[R.point(_i)].append(_i)
LV=['A2.1','A2.2','B1.1','B1.2','B2.1','B2.2','C1']; li=LV.index
meta=json.load(open(os.path.join(C.ROOT,'app/content/meta.json'))); TOP={s['id']:s for s in meta['skills']}
PARTLY=set('would_habit no_longer pc_always stative stative2 fut_past about_to no_none rel_which_all rel_prep cmp_double q_prep_end pp_been_gone vp_make_let vp_go_ing vp_to_ing vp_obj_to adv_irreg plural_reg unc_nouns prep_move prep_transport pas_act c0_c1 if_when c1_c2 c2_c3 whoever art_names adj_basic deduction rel_what must_vs_have_to wont_refuse'.split())
NOCARD=set('should_have sup_ever vp_ing_subject cmp_less cmp_adv v3 some_offers indef_adj'.split())
INSIDE={}
lead=collections.defaultdict(list)
for p in P:
    for n in p['needs']: lead[n].append(p['id'])
def counts(p):
    its=res.get(p['id'],[]); c=collections.Counter(i['role'] for i in its)
    lv=sorted({i['level'] for i in its},key=li)
    return c,lv,its
for p in P:
    c,lv,its=counts(p); p['c']=dict(c); p['tl']=lv; p['n']=len(its); p['cu']=c['check']+c['use']
    p['card']='no' if (p['topics']==['new'] or p['id'] in NOCARD) else ('partly' if p['id'] in PARTLY else 'yes')
    p['leads']=lead[p['id']]
def content(p):
    if p['topics']==['new'] and not p['n']: return 'none'
    if not p['n']: return f"card: {p['card']} · no tasks"
    c=p['c']; span=p['tl'][0] if len(p['tl'])==1 else p['tl'][0]+'–'+p['tl'][-1]
    where=' · inside '+', '.join(sorted({i['skill'] for i in res[p['id']]})) if p['topics']==['new'] else ''
    return f"card: {p['card']} · check {c.get('check',0)} · use {c.get('use',0)} · learn {c.get('learn',0)} ({span}){where}"
def src(p):
    out=[]
    m=p['mu']
    if m: out.append(m if re.match(r'AGU|from memory',m) else 'Murphy '+m)
    if p['te']: out.append('TE '+p['te'])
    if p['egp']: out.append('EGP: '+p['egp'])
    if p['note']: out.append(p['note'])
    return ' · '.join(out)
esc=lambda s:s.replace('|','\\|')
def ids(l): return ', '.join(f'`{x}`' for x in l) or '—'
def table(pts):
    o=['| id | name | can_do | needs | contrasts | typical_errors | sources | topic | content |','|---|---|---|---|---|---|---|---|---|']
    for p in pts:
        o.append('| '+' | '.join(esc(x) for x in [f"`{p['id']}`",p['name'],p['can'],ids(p['needs']),ids(p['vs']),p['err'] or '—',src(p),', '.join(p['topics']) if p['topics']!=['new'] else '*new*',content(p)])+' |')
    return '\n'.join(o)
NEWAB=[p for p in P if p['topics']==['new'] and p['level'][0]!='C']
OLD=[p for p in P if p['topics']!=['new']]
C1=[p for p in P if p['level'][0]=='C']
intro=f"""# Gramatikas karte (A2.1 līdz C1)

Sagatavots 2026. gada 13. novembrī pēc `docs/GRAMMAR-MAP-BRIEF.md`. Šis ir dokuments: lietotnē, uzdevumos un testos nekas nav mainīts.

## Kā lasīt

Karte ir viena tabula, sadalīta pa līmeņiem. Viena rinda ir viens **gramatikas punkts**, mazāks par tēmu. Kopā **{len(P)} punkti**: {len(OLD)} punkti, kas sedz pašreizējās 58 tēmas, {len(NEWAB)} punkti no atsauces sarakstiem A1 līdz B2, kuriem lietotnē satura nav, un {len(C1)} C1 punkti desmit virzienos. Ievads ir latviski, pati karte angliski.

| Sleja | Kas tajā ir |
|---|---|
| `id` | Īss, nemainīgs nosaukums, uz kuru atsaucas citas rindas |
| `name` | Punkta nosaukums ar formu vai piemēru |
| `can_do` | Ko izglītojamais prot pateikt vai izdarīt |
| `needs` | Punkti, kas jāprot pirms šī. Ierakstīts tikai tas, bez kā šo punktu nevar izpildīt, nevis viss, kas mācīts agrāk. `can` ir pirmais modālais darbības vārds, tāpēc pārējie modālie uz to atsaucas formas dēļ (bez *-s*, bez *to*, bez *do*) |
| `contrasts` | Punkti, ar kuriem šo jauc. Šeit vajadzīgi izvēles uzdevumi starp abām formām |
| `typical_errors` | Latviešu pieaugušo tipiskās kļūdas. Lielie burti (3S, DURATION) ir kodi no `docs/ERROR-TYPES.md` |
| `sources` | Murphy nodaļa, rinda atsauces sarakstā (TE), *English Grammar Profile* līmenis (EGP), piezīmes |
| `topic` | Pašreizējā tēma lietotnē (`app/content/meta.json`) vai *new* |
| `content` | Kas ir tagad: noteikumu kartīte (yes / partly / no) un uzdevumu skaits pēc lomas |

## Kā noteikts līmenis

1. **Pamats ir atsauces saraksts** (`docs/LEVEL-LISTS-test-english.md`): A1 saraksts ir mūsu A2.1, A2 saraksts ir A2.2, B1 saraksts ir B1.1 vai B1.2, B1+ saraksts ir B1.2 vai B2.1, B2 saraksts ir B2.1 vai B2.2, C1 saraksts ir C1 bez dalījuma, desmit virzieni saraksta secībā (Ingas lēmums 13. novembrī). Punkts stāv tajā sarakstā, kur tas parādās pirmo reizi.
2. **EGP ir pārbaude.** EGP rāda, kurā līmenī izglītojamie formu paši lieto eksāmenu darbos, tāpēc tas bieži ir vienu pakāpi vēlāk, nekā formu māca. Kur EGP ir par veselu līmeni vēlāk vai agrāk, tas ir ierakstīts slejā `sources` ar vārdu *Level:*, un pieci svarīgākie gadījumi ir izlemti ar Ingu 13. novembrī (`docs/GRAMMAR-MAP-GAPS.md`, 5. sadaļa); kartē pie tiem rakstīts *Decided by the teacher*.
3. **Murphy dod noteikumu un nodaļu.** C1 punktiem Murphy vietā ir Hewings (AGU).
4. **Viena saraksta iekšienē** (piemēram, B1.1 vai B1.2) punkts ir ielikts pēc priekšnosacījumiem un grūtības, nevis pēc vietas sarakstā. Ceļa secība paliek saraksta secība.

## Kas ir pārbaudīts un kas nav

| Avots | Kā izmantots |
|---|---|
| Murphy, *English Grammar in Use*, 5. izd. | Nodaļu numuri pārbaudīti pēc satura rādītāja (Ingas Drive eksemplārs). Nodaļu teksts nav lasīts viss; kur noteikums ņemts no atmiņas, tas ir standarta noteikums un sakrīt ar lietotnes kartītēm |
| *English Grammar Profile* | Pārbaudīts tiešsaistes tabulā (1222 apgalvojumi, lejupielādēta ar vietnes pašas pogu 13. novembrī). *not found in EGP* nozīmē, ka tabulā tāda ieraksta nav. Lietošanas noteikumi neļauj reklamēt materiālus kā "English Profile informed" bez atļaujas |
| test-english.com saraksti | Pēc `LEVEL-LISTS-test-english.md`. Pašas lapas A1 līdz B2 nav lasītas (vietne bloķē automātisku piekļuvi), tāpēc *(from memory)* pie TE rindas nozīmē: neesmu drošs, ka punkts ir tieši šajā nodarbībā |
| test-english C1 lapas | Ingas ekrānuzņēmumi. Redzētas pilnībā: *Advanced present simple and present continuous*, *The perfect tenses*, *can / be able to, may / might*, *The subjunctive*, *should*. Redzētas daļēji: *will, would* (bez *would* beigām un uzdevumiem), *Advanced past simple, past continuous and past perfect* (skaidrojuma apakšējā puse un 1. uzdevums). *Subject-verb agreement* (skaidrojums pilnībā, bez uzdevumiem), *Prepositions* (bez pirmās daļas un uzdevumiem). *Advanced word order* (skaidrojums pilnībā, bez uzdevumiem). *Advanced participle clauses* (pilnībā, ar 2. uzdevumu). Visi desmit virzieni ir salīdzināti ar lapām; trīs lapām trūkst pa daļai, un tie punkti kartē ir atzīmēti (*not in the part of the page seen*) |
| Hewings, *Advanced Grammar in Use*, 3. izd. (AGU) | Ingas PDF: nodaļu nosaukumi un 1. līdz 6., 15. līdz 17., 39. līdz 42., 55., 58., 59., 99., 100. nodaļas noteikumu teksts izlasīts. 13 nodaļām teksts no PDF neizvilkās; tur rakstīts *from memory* |
| *Gold New Edition C1*, Grammar reference | Ingas PDF, 17 lappuses: sadaļu virsraksti un pie punktiem nosauktās sadaļas |
| Uzdevumu skaits (`content`) | Visi {len(items)} uzdevumi no `tools/dump_items.php` ir piesaistīti punktiem failā `docs/GRAMMAR-MAP-TASKS.csv` (13. novembris). 3041 uzdevumu izlasīju pa vienam; automātiskā šķirošana pirms tam bija kļūdījusies katrā piektajā (663 pārvietoti). 273 uzdevumi ir sašķiroti pēc pazīmes teikumā bez lasīšanas: trīs ciešamās kārtas tēmas, kurām kartē ir tikai viens punkts, un vārdu secības uzdevumi nosacījuma teikumu un netiešo jautājumu tēmās. Uzdevums ir pie tā punkta, kura zināšanu tas prasa, arī ja tas ir citā tēmā |

No grāmatām un vietnes nav pārrakstīts neviens teikums vai uzdevums; piemēri kartē ir pašu (C1 piemēri pēc otrā lasījuma pārrakstīti no jauna, jo daļa bija pārāk tuvu Hewings teikumiem). Faili repozitorijā nav ielikti.

*Review of all verb tenses* (A2, B1, B1 līdz B2) nav gramatikas punkti, tāpēc kartē to nav: tie ir jaukti uzdevumi par esošajiem punktiem.
"""
out=[intro]
for lv in LV:
    pts=[p for p in P if p['level']==lv]
    out.append(f"\n## {lv} ({len(pts)} points)\n")
    for a in dict.fromkeys(p['area'] for p in pts):
        sub=[p for p in pts if p['area']==a]
        out.append(f"\n### {lv} · {a.split(' · ')[-1] if lv[0]=='C' else a}\n")
        if lv[0]=='C':
            s=p4.STRANDS[a]; out.append(f"*Sources seen:* {s[0]}.  \n*Task forms this strand needs:* {s[1]}.\n")
        out.append(table(sub))
out.append("""
## C1: what every strand stands on, and the task forms

C1 is mostly a choice between two correct forms by meaning or register, so the usual *one correct answer, three ungrammatical ones* is not enough. Every C1 point names the B2 (or lower) points it stands on in `needs`; where such a point is *new* (no content), C1 cannot be reached through the path until it is written. The B2 points that C1 needs and that have no content now:

""")
need_new=collections.defaultdict(list)
for p in C1:
    for n in p['needs']:
        if BY[n]['topics']==['new'] and BY[n]['level'][0]!='C': need_new[n].append(p['id'])
out.append('| missing point | level | needed by |\n|---|---|---|\n'+'\n'.join(f"| `{n}` {BY[n]['name']} | {BY[n]['level']} | {ids(v)} |" for n,v in sorted(need_new.items(),key=lambda x:li(BY[x[0]]['level']))))
out.append(open(os.path.join(C.HERE,'second_reading.md')).read())
open(os.path.join(C.ROOT,'docs/GRAMMAR-MAP.md'),'w').write('\n'.join(out)+'\n')
json.dump([{k:v for k,v in p.items() if k not in('rx',)} | {'content':content(p),'src':src(p)} for p in P],open(C.S+'points.json','w'),ensure_ascii=False)
print(len(P),len(OLD),len(NEWAB),len(C1)); print('need_new',len(need_new))
