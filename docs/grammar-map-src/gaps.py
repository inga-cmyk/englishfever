import sys,json,re,collections,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import build as B
P=B.P; BY=B.BY; LV=B.LV; li=B.li; items=B.items; C=B.C
def ids(l): return ', '.join(f'`{x}`' for x in l)
o=[]
o.append(f"""# Gramatikas karte: robi un lēmumi

Sagatavots 2026. gada 13. novembrī kopā ar `docs/GRAMMAR-MAP.md`. Punktu `id` ir tie paši, kas kartē. Uzdevumu skaits pie punktiem ir pēc piesaistes failā `docs/GRAMMAR-MAP-TASKS.csv` (visi 3314 uzdevumi; 3041 izlasīts pa vienam, 273 sašķiroti pēc pazīmes teikumā).

Saturs: 1. punkti bez satura · 2. līmeņu atšķirības starp lietotni un karti · 3. punkti ar mazāk nekā 10 uzdevumiem · 4. kontrasta pāri bez izvēles uzdevumiem · 5. Ingas lēmumi un materiāli.
""")
# 1
new=[p for p in P if p['topics']==['new'] and p['level'][0]!='C']
has=[p for p in new if p['n']]
o.append(f"## 1. Atsauces sarakstu A1 līdz B2 punkti, kuriem lietotnē satura nav ({len(new)})\n\nNav ne kartītes, ne savas tēmas. "+str(len(has))+" no tiem ir daži uzdevumi citās tēmās ("+', '.join(f"`{p['id']}` {p['n']}" for p in has)+"); pārējiem nav neviena. Sleja *Vajadzīgs C1* rāda, vai uz šo punktu balstās kāds C1 punkts.\n")
c1need=collections.defaultdict(list)
for p in P:
    if p['level'][0]=='C':
        for n in p['needs']: c1need[n].append(p['id'])
for lv in LV[:6]:
    sub=[p for p in new if p['level']==lv]
    if not sub: continue
    o.append(f"\n**{lv}** ({len(sub)})\n\n| id | Punkts | Rinda atsauces sarakstā | Vajadzīgs C1 |\n|---|---|---|---|")
    for p in sub: o.append(f"| `{p['id']}` | {p['name']} | {p['te']} | {'jā' if c1need[p['id']] else ''} |")
o.append(f"\nC1: visi {sum(p['level'][0]=='C' for p in P)} punkti ir bez satura (lietotnē C1 līmeņa nav).\n")
# 2
later=[];earlier=[]
for p in P:
    if not p['n']: continue
    its=B.res[p['id']]; lvls=[li(i['level']) for i in its]; pl=li(p['level'])
    if min(lvls)>pl: later.append((min(lvls)-pl,p))
    below=sum(1 for x in lvls if x<pl)
    if below: earlier.append((pl-min(lvls),below,p))
o.append("## 2. Kur līmenis lietotnē atšķiras no kartes\n\nLīmeņi skaitīti pusēs (A2.1, A2.2, B1.1 …). Pus līmeņa atšķirība tajā pašā sarakstā (B1.1 un B1.2) nav kļūda; tabulās ir tikai būtiskākais.\n")
o.append("### 2.1. Lietotnē vēlāk nekā kartē: kartes līmenī uzdevumu nav\n\nIzglītojamais, kurš pēc kartes ir gatavs šim punktam, saņemtu grūtākus teikumus vai punktu neredzētu.\n\n| id | Punkts | Karte | Uzdevumi lietotnē | Tēma | Uzd. |\n|---|---|---|---|---|---|")
for d,p in sorted(later,key=lambda x:(-x[0],li(x[1]['level']))):
    o.append(f"| `{p['id']}` | {p['name']} | {p['level']} | {p['tl'][0]}{'–'+p['tl'][-1] if len(p['tl'])>1 else ''} | {', '.join(p['topics'])} | {p['n']} |")
o.append("\n### 2.2. Lietotnē agrāk nekā kartē (vismaz par veselu līmeni vai vairāk nekā 5 uzdevumi)\n\n| id | Punkts | Karte | Agrākais uzdevums | Uzdevumi zem kartes līmeņa | Tēma |\n|---|---|---|---|---|---|")
for d,b,p in sorted(earlier,key=lambda x:(-x[0],-x[1])):
    if d>=2 or b>5: o.append(f"| `{p['id']}` | {p['name']} | {p['level']} | {p['tl'][0]} | {b} no {p['n']} | {', '.join(p['topics'])} |")
# 3
pair=collections.Counter((i['skill'],i['level']) for i in items if i['role'] in('check','use'))
allp=collections.Counter((i['skill'],i['level']) for i in items)
low=[(k,pair[k]) for k in allp if pair[k]<10]
o.append("\n## 3. Punkti ar mazāk nekā 10 pārbaudes un lietošanas uzdevumiem\n\n**Precīzi, pa tēmas un līmeņa pāriem:** no "+str(len(allp))+" pāriem mazāk par 10 uzdevumiem, kas skaitās (*check* + *use*), ir "+(', '.join(f"{B.TOP[k[0]]['label']} {k[1]} ({n})" for k,n in sorted(low)) or 'nevienam')+".\n")
few=[p for p in P if p['topics']!=['new'] and p['cu']<10]
zero=[p for p in few if p['n']==0]; some=[p for p in few if p['n']>0]
o.append(f"**Pa punktiem:** no {sum(p['topics']!=['new'] for p in P)} punktiem ar tēmu lietotnē {len(some)} punktiem ir 1 līdz 9 uzdevumi, kas skaitās, un {len(zero)} punktiem nav neviena. Tas nenozīmē, ka tēmā uzdevumu trūkst: tēmas uzdevumi ir sakrājušies pie viena vai diviem punktiem, un pārējie punkti (parasti tie, kas uz kartītes ir tikai *Watch out* rindā) paliek gandrīz bez prakses.\n")
o.append("### 3.1. Punkti ar tēmu lietotnē, kuriem nav neviena uzdevuma\n\n| id | Punkts | Karte | Tēma | Kartīte |\n|---|---|---|---|---|")
for p in sorted(zero,key=lambda p:li(p['level'])): o.append(f"| `{p['id']}` | {p['name']} | {p['level']} | {', '.join(p['topics'])} | {p['card']} |")
o.append("\n### 3.2. No 1 līdz 9 uzdevumiem, kas skaitās\n\n| id | Punkts | Karte | check | use | learn | Tēma |\n|---|---|---|---|---|---|---|")
for p in sorted(some,key=lambda p:(li(p['level']),p['cu'])): o.append(f"| `{p['id']}` | {p['name']} | {p['level']} | {p['c'].get('check',0)} | {p['c'].get('use',0)} | {p['c'].get('learn',0)} | {', '.join(p['topics'])} |")
# 4
pairs=set()
for p in P:
    for v in p['vs']: pairs.add(tuple(sorted((p['id'],v))))
isnew=lambda x: BY[x]['topics']==['new']
pn=[pr for pr in pairs if isnew(pr[0]) or isnew(pr[1])]
ab=[pr for pr in pn if BY[pr[0]]['level'][0]!='C' and BY[pr[1]]['level'][0]!='C']
def opts(i): return [str(i.get('correct',''))],[str(x) for x in (i.get('wrong') or [])]
def has(l,rx): return any(re.search(rx,x,re.I) for x in l)
LAB=['present simple / present continuous', 'present perfect / past simple', 'past continuous / past simple', 'past perfect / past simple', 'present perfect simple / continuous', 'for / since', 'will / going to', 'going to / present continuous (arrangement)', "mustn't / don't have to", 'could / was able to, managed to', "must be / can't be, might be", 'first / second conditional (will / would)', 'second / third conditional (would / would have)', 'zero / first conditional (present / will)', 'used to / be used to, get used to', 'said / told', 'reported question / direct question order', 'so / such', 'much / many', 'few / little', 'some / any', 'a, an / the', 'the / no article', '-ed / -ing adjectives', 'during / while', 'by / until', 'although / despite', 'because / because of', 'who / which', 'that / who, which (after a comma)', 'passive / active', 'to + verb / -ing', 'comparative / superlative', 'as / than', 'adverb / adjective', 'tag with be / tag with do', 'subject / object question', 'wish + past / wish + had done', 'would rather + verb / would rather you + past']
M=[('ps_form','pc_form','present_simple present_continuous',r"\b(am|is|are|'m|'s|'re|isn't|aren't) (not )?\w+ing\b",r"^(?!.*\b\w+ing\b).+"),
 ('pp_form','pst_reg','present_perfect cmp_pp_ps past_simple',r"\b(have|has|'ve|haven't|hasn't)\b",r"^(?!.*\b(have|has|'ve|haven't|hasn't|had)\b).*\b(\w+ed|went|saw|did|was|were|bought|met|took|came|got|made|lost|left|found|didn't)\b"),
 ('pastc_form','pst_reg','past_continuous cmp_ps_pc narrative',r"\b(was|were|wasn't|weren't) (not )?\w+ing\b",r"^(?!.*\b\w+ing\b)(?!.*\bhad\b).+"),
 ('pastp_form','pst_reg','past_perfect narrative',r"\bhad(n't)? (\w+ )?\w+(ed|en|ne|wn|t|d)\b",r"^(?!.*\bhad\b)(?!.*\b(have|has)\b).+"),
 ('pp_form','ppc_form','present_perfect_continuous present_perfect',r"been \w+ing",r"\b(have|has|'ve|'s) (?!been \w+ing)\w+"),
 ('pp_form','pp_for_since','present_perfect present_perfect_continuous',r"^\W*for\W*$|\bfor\b",r"^\W*since\W*$|\bsince\b"),
 ('will_now','going_to','future',r"going to",r"\bwill\b|'ll\b|won't"),
 ('going_to','fut_arr','future',r"going to",r"\b(am|is|are|'m|'s|'re) (?!going to)\w+ing\b"),
 ('must_have_to','mustnt_dont','modal_verbs',r"mustn't|must not",r"(don't|doesn't) have to"),
 ('could_past','able_once','more_modals modal_verbs',r"\bcould\b",r"able to|managed"),
 ('deduction','must_have_to','more_modals',r"\bmust be\b",r"\bcan't be\b|\bmight be\b"),
 ('c1','c2','cond_first cond_second',r"\bwill\b|'ll\b|won't",r"\bwould\b|'d\b|wouldn't"),
 ('c2','c3','cond_second cond_third cond_mixed',r"would(n't)? have|'d have",r"\bwould(n't)?\b(?! have)|'d (?!have)\w+"),
 ('c0','c1','cond_zero cond_first',r"^(?!.*(\bwill\b|'ll\b|won't)).+",r"\bwill\b|'ll\b|won't"),
 ('used_to','be_used_to','used_to',r"\b(am|is|are|was|'m|'s|get|got|getting) used to\b",r"(?<!\bam )(?<!\bis )(?<!'m )(?<!'s )\bused to\b"),
 ('rep_say_tell','rep_backshift','rep_statements',r"\bsaid\b",r"\btold\b"),
 ('rep_q_wh','q_wh','rep_questions ind_polite',r"\b(where|what|when|why|how) (I|you|he|she|we|they|the|my|it) ",r"\b(where|what|when|why|how) (do|does|did|is|are|was|were|can|will)\b"),
 ('so_such_basic','too_enough','so_such',r"\bso\b",r"\bsuch\b"),
 ('much_many','a_few','quantity',r"\bmuch\b",r"\bmany\b"),
 ('a_few','few_little','quantity',r"\bfew\b",r"\blittle\b"),
 ('count_unc','indef_form','quantity indefinite_pronouns',r"\bsome",r"\bany"),
 ('a_an','a_the','articles articles_b1',r"^\W*(a|an)\W*$|\b(a|an)\b",r"\bthe\b"),
 ('a_the','art_general','articles articles_b1',r"\bthe\b",r"^\W*(—|-|no article)\W*$"),
 ('eding','dep_adj','adj_ed_ing',r"\w+ed\b",r"\w+ing\b"),
 ('during_while','by_until','time_clauses',r"\bduring\b",r"\bwhile\b"),
 ('by_until','during_while','time_clauses',r"\bby\b",r"\buntil\b"),
 ('contrast_b1','because_of','conj_clauses conj_linkers conj_b2',r"\balthough\b|even though",r"\bdespite\b|in spite of"),
 ('because_of','conj_so_bec','conj_clauses conj_linkers',r"\bbecause of\b",r"\bbecause\b(?! of)"),
 ('rel_subj','rel_where_whose','relative_clauses',r"\bwho\b",r"\bwhich\b"),
 ('rel_nondef','rel_subj','relative_clauses',r"\bthat\b",r"\bwhich\b|\bwho\b"),
 ('pas_pres','ps_form','present_simple_passive past_simple_passive',r"\b(is|are|was|were|isn't|aren't|wasn't|weren't) (\w+ )?\w+(ed|en|t|wn|ne)\b",r"^(?!.*\b(is|are|was|were|isn't|aren't|wasn't|weren't|be|been|being)\b).+"),
 ('vp_to','vp_ing','verb_patterns',r"\bto \w+",r"\b\w+ing\b"),
 ('cmp_er','sup','comparison',r"\bthe (most|\w+est|best|worst)\b",r"\b(more|\w+er|better|worse)\b(?!.*\bthe (most|\w+est)\b)"),
 ('cmp_er','cmp_as','comparison',r"\bas\b",r"\bthan\b"),
 ('adj_adv','link_adj','adverbs',r"\w+ly\b|\bwell\b",r"^(?!.*\w+ly\b)(?!.*\bwell\b).+"),
 ('tag_basic','so_neither','question_tags',r"isn't|aren't|wasn't|weren't",r"don't|doesn't|didn't"),
 ('q_subject','q_wh','subject_object_q',r"\b(who|what) (did|does|do)\b",r"\b(who|what) (?!did|does|do)\w+(ed|s)?\b"),
 ('wish_pres','wish_past','cond_advanced',r"\bhad \w+",r"^(?!.*\bhad \w+(ed|en)\b).+"),
 ('would_rather','rather_you','unreal_time',r"rather (you|he|she|we|they)",r"rather (not )?(?!you|he|she|we|they)\w+"),
]
o.append(f"\n## 4. Kontrasta pāri bez izvēles uzdevumiem\n\nKartē ir {len(pairs)} kontrasta pāri (A2.1 līdz C1.2). Izvēles uzdevums šeit nozīmē: abas formas ir starp atbilžu variantiem, un pareizā ir viena no tām.\n")
o.append(f"### 4.1. Pāri, kuros vienai pusei satura nav vispār\n\nTādu ir {len(pn)}: {len(ab)} līmeņos A2 līdz B2 un {len(pn)-len(ab)}, kuros ir C1 punkts. A2 līdz B2 pāri:\n")
by=collections.defaultdict(list)
for a,b in sorted(ab,key=lambda pr:max(li(BY[pr[0]]['level']),li(BY[pr[1]]['level']))):
    by[max(BY[a]['level'],BY[b]['level'],key=li)].append(f"`{a}` ↔ `{b}`")
for lv in LV[:6]:
    if by[lv]: o.append(f"- **{lv}:** "+' · '.join(by[lv]))
o.append("\n### 4.2. Galvenie formu pāri: cik izvēles uzdevumu ir tagad\n\nSaskaitīti izvēles uzdevumi (*mcq*) nosauktajās tēmās, kuros pareizā atbilde ir viena forma un starp nepareizajām ir otra. Vārdu bankas un ierakstāmie uzdevumi nav skaitīti. Skaitīts pēc formām atbilžu variantos, tāpēc skaits var atšķirties par vienu vai diviem.\n\n| Formu pāris | Tēmas, kurās skaitīts | Izvēles uzdevumi | Vērtējums |\n|---|---|---|---|")
meas=set()
for (a,b,tops,ra,rb),lab in zip(M,LAB):
    n=0
    for i in items:
        if i['kind']!='mcq' or i['skill'] not in tops.split(): continue
        c,w=opts(i)
        if (has(c,ra) and has(w,rb)) or (has(c,rb) and has(w,ra)): n+=1
    meas.add(tuple(sorted((a,b))))
    o.append(f"| {lab} | {tops.replace(' ',', ')} | {n} | {'nav' if n==0 else 'maz (zem 5)' if n<5 else 'ir'} |")
rest=[pr for pr in pairs if pr not in pn]
o.append(f"\n### 4.3. Pārējie pāri\n\nKartē ir {len(rest)} pāri, kuros abām pusēm saturs ir. Tabulā 4.2 saskaitīti 39 formu pāri, kam ir skaidra pazīme vārdos; pārējiem tādas pazīmes nav, un tie nav saskaitīti. Drošākais rādītājs tiem ir 3. sadaļa: ja vienam pāra punktam ir zem 10 uzdevumiem, arī izvēles uzdevumu starp abiem gandrīz noteikti nav.\n")
q=open(os.path.join(C.HERE,'questions.md')).read() if True else '## 5. Jautājumi Ingai\n\n(tiks pievienoti)\n'
o.append(q)
open(os.path.join(C.ROOT,'docs/GRAMMAR-MAP-GAPS.md'),'w').write('\n'.join(o)+'\n')
print(len(new),len(later),len(earlier),len(zero),len(some),len(pairs),len(pn),len(rest)); print(low)
