import os
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.abspath(os.path.join(HERE,'..','..'))
WORK=os.environ.get('GM_WORK','/tmp/grammar-map'); os.makedirs(WORK,exist_ok=True)
import sys,json,re,collections; sys.path.insert(0,HERE)
import lib, p1, p2, p3, fixes, p4
P=lib.POINTS; BY={p['id']:p for p in P}
S=WORK+'/'
items=json.load(open(S+'items.json'))
def ans(i):
    if i.get('correct'): return str(i['correct'])
    a=i.get('answers') or []
    if a and isinstance(a[0],list): return a[0][0]
    return i.get('model') or ''
def text(i):
    parts=[i.get('q',''),'=>',ans(i)]
    if i.get('sentence'): parts.append(i['sentence'])
    if i.get('pairs'): parts.append(' / '.join(' '.join(x) for x in i['pairs']))
    return ' '.join(parts)
def opts(i): return [str(i.get('correct',''))]+[str(x) for x in (i.get('wrong') or [])]
def has(o,rx): return any(re.search(rx,x,re.I) for x in o)
def choice(a,b): return lambda i,tx: i['kind']=='mcq' and has(opts(i),a) and has(opts(i),b)
# topic-specific patterns and corrections of the first draft (sentence and answer only, never the explanation)
TIMEW=r"\b(when|as soon as|until|till|before|after|once)\b"
OVR={
 'ps_pc':{'present_simple':r"\bnow\b|at the moment|look!|listen!|\btoday\b|this week|these days",'present_continuous':r"every (day|week|morning|evening|year|summer)|usually|\boften\b|\bnever\b|on (mondays|sundays|saturdays|fridays)|=> \w+s\b"},
 'stative':{'present_continuous':r"\b(know|knows|want|wants|need|needs|believe|believes|understand|understands|belong|belongs|prefer|prefers|agree|agrees|mean|means|own|owns|seem|seems|love|loves|hate|hates)\b",'present_simple':r"\b(know|knows|want|wants|need|needs|believe|believes|understand|understands|belong|belongs)\b.*\b(now|at the moment)\b"},
 'stative2':r"\bthink(s|ing)?\b.*\b(about|of)\b|\b(is|are|am|'s|'re) being\b|\btastes?\b|\bsmells?\b|\bhaving (a|lunch|dinner|breakfast)\b.*\bhas\b",
 'pc_always':r"\b(always|constantly|forever) \w+ing\b",
 'pp_ps':{'past_simple':r"\b(have|has|'ve) (you |he |she |they )?(ever|never|just|already)\b|\byet\b|\bsince\b",'present_perfect':r"yesterday|last (week|year|night|month|summer|weekend|monday|friday)|\bago\b|in (19|20)\d\d\b|\bwhen did\b"},
 'v3':None,
 'pp_been_gone':r"\b(been|gone) to\b",
 'pp_ps_now':r"from (19|20)\d\d to|this (morning|week|month|year)|\btoday\b|so far",
 'ppc_result':r"out of breath|dirty|\bwet\b|red eyes|eyes are red|covered in|you look|why (are|is) (you|he|she|your)",
 'pp_ppc':lambda i,tx: (i['skill']=='present_perfect_continuous' and re.search(r"=> .*\b(have|has|'ve|'s|haven't|hasn't)\b(?!.*been \w+ing)",tx,re.I) and not re.search(r"been \w+ing",ans(i),re.I)) or bool(re.search(r"how (much|many)",tx,re.I)),
 'pastc_when':{'past_continuous':r"\b(when|while)\b",'cmp_ps_pc':r"."},
 'pastc_two':{'past_continuous':r"while .*\b(was|were)\b.*\b(was|were)\b|\b(was|were) \w+ing,? and .*(was|were) \w+ing"},
 'past_seq':r"three times|twice|many times|several times",
 'pastp_order':None,'pastp_form':{'past_perfect':r"$^"},'pastp_by':{'past_perfect':r"by the time|\bnever\b.*before|\balready\b|\bjust\b"},
 'will_going':choice(r"going to",r"\bwill\b|'ll\b|won't"),
 'will_now':r"\b(I|we)'ll (help|get|carry|open|call|answer|have|take|pay|do|show|lend|send|bring|check|go and)\b",
 'fut_time_clause':{'future':TIMEW,'conj_linkers':TIMEW[:-2]+r"\b.*\b(will|'ll|won't)\b|\b(will|'ll|won't)\b.*"+TIMEW,'time_clauses':r"$^"},
 'could_past':r"\bcould(n't)?\b.*\b(when|years old|as a child|last|yesterday|ago)\b|\bwhen\b.*\b(was|were)\b.*\bcould",
 'requests':r"\b(could|can|would|may) (you|I|we)\b.*\?|please",
 'mustnt_dont':r"mustn't|must not|don't have to|doesn't have to",
 'should':r"\bshould(n't)?\b",
 'might':r"\bmight\b|\bmay\b",'deduction':r"\b(must|can't|might|could|may) (not )?be\b",'able_once':r"managed to|\b(was|were|wasn't|weren't) able to\b",
 'neednt':r"needn't(?! have)|don't need to|doesn't need to",
 'pas_by':r"\bby (my|the|a|an|his|her|our|their|some|people|\w+ \w+)\b",
 'pas_negq':r"\?|n't\b|\bnot\b|make a (yes/no )?question|make it negative",
 'pas_act':r"^(rewrite|start with|make (it|the sentence) passive|change)|\b(somebody|someone)\b|\bthey (make|made|built|clean|speak|sell|sold|grow|use|check|stole|invite|send|sent|will|have|are)\b",
 'pas_modal_past':r"\bhave been \w+",
 'caus_get':r"\b(get|got|gets|getting)\b|stolen|broken into",
 'if_when':choice(r"^\W*if\W*$|\bif\b",r"^\W*when\W*$|\bwhen\b"),
 'c0_c1':{'cond_zero':r"tonight|tomorrow|this (evening|weekend)|next (week|month)|\bwill\b|'ll\b",'cond_first':r"\balways\b|every time|whenever|usually"},
 'c1_c2':None,'c2_c3':None,
 'c2_were':r"\bwere you\b|if (I|he|she|it) were\b",
 'c3_modal':r"could have|might have|could've|might've|couldn't have",
 'wish_would':r"wish.*\bwould(n't)?\b",
 'wish_past':r"(wish|if only).*\bhad(n't)? (\w+ly )?(\w+ed|been|known|gone|done|seen|taken|told|bought|left|said|chosen|eaten|met|brought|kept|sold|spent|read|written|had)\b",
 'wish_pres':r"\bwish\b|if only",
 'rep_say_tell':lambda i,tx: (i['kind']=='mcq' and has(opts(i),r"\b(said|say|says)\b") and has(opts(i),r"\b(told|tell|tells)\b") and not re.search(r"\bto \w+",str(i.get('correct')))) or (i['kind']=='gap' and ans(i).lower() in ('said','told','say','tell','said to','told me')),
 'rep_pron_time':r"the next day|the day before|the following|the previous|that day|that night|the week before|the next (week|month)",
 'rep_backshift2':r"=> .*\bhad (\w+ly )?(\w+ed|been|gone|done|seen|lost|left|taken|bought|found|forgotten|met|made|told|written|broken|sold|had|won|heard|read|eaten|spent)\b",
 'rep_stay':r"\bsays\b|\btells\b|\bearth\b|still (lives|works)",
 'rep_orders':r"\b(told|asked|ordered|begged|warned|reminded) (me|him|her|us|them|\w+) (not )?to\b|=> .*\b(not )?to \w+\b(?<!to me)(?<!to him)(?<!to her)",
 'q_wh':{'aux_verbs':r"\b(what|where|when|why|how|which|who)\b",'subject_object_q':r"$^"},
 'tag_special':r"aren't I|shall we|will you\?|\b(nobody|no one|nothing|everybody|everyone|somebody|never|hardly)\b|\blet's\b|\bthere (is|are|was|were)\b",
 'iq_whether':{'ind_advanced':r"$^"},
 'vp_like_ing':r"\b(like|likes|love|loves|hate|hates|liked|loved)\b (\w+ing|to \w+|___)|\b(like|likes|love|loves|hate|hates)\b.*=> (\w+ing|to \w+)\b",
 'vp_prep_ing':{'verb_patterns':r"\b(in|at|for|about|of|before|after|without|by|on|instead of|from) (\w+ing\b|___ \()|\b(in|at|for|about|of|before|after|without|by) ___.*=> \w+ing\b",'dep_prepositions':r"\b(at|in|of|for|about|on) \w+ing\b"},
 'vp_ing_subject':r"(: |^)(\w+ing|___) (\w+ )?(\w+ )?(is|are|was|takes|makes|helps|can)\b.*(=> \w+ing)?",
 'vp_to':r"\b(want|wants|wanted|need|needs|needed|decid\w+|hop\w+|plan\w*|learn\w*|agree\w*|promis\w+|manag\w+|refus\w+|offer\w*|expect\w*|afford|tend\w*|fail\w*|arrang\w+|pretend\w*|threaten\w*|would like|'d like)\b (not )?(to|___)",
 'purpose_to':r"\bto (get|buy|see|learn|ask|meet|help|pay|find|make|take|catch|save|study|improve|check|pick|tell|visit|book|talk|speak|keep|have|send|do|be)\b|\bfor (a|an|some|the|my) \w+",
 'because_of':{'conj_linkers':r"because of|due to",'conj_clauses':r"because of|due to|owing to"},
 'link_time':r"\b(then|after that|afterwards|before|after|while|when|first|finally|next|as soon as)\b",
 'count_unc':r"\b(some|any)\b",'some_offers':r"would you like (some|any|___)|(can|could) I have (some|any|___)|\bany (seat|time|day|bus|colour|of them)\b",
 'much_many':None,'a_few':r"\ba (few|little)\b",'few_little':r"(?<!\ba )\b(few|little)\b (\w+ )?(friends|people|time|money|hope|chance|information|interest|students|days)",
 'too_enough':r"\btoo\b|\benough\b",'no_none':r"\bno\b (\w+)|\bnone\b",
 'indef_neg':r"n't .*\bany(one|body|thing|where)\b|\b(nobody|nothing|no one|nowhere)\b",
 'indef_sing':r"\b(every|some|any|no)(one|body|thing)\b (is|are|was|were|has|have|knows|know|likes|like|wants|want|does|do|works|work|needs|need|___)\b|\btheir\b",
 'a_an':r"\b(a|an) (nurse|doctor|teacher|engineer|student|driver|pilot|lawyer|dentist|chef|waiter|vet)\b|\ban\b|___ (hour|apple|umbrella|university|egg|orange|engineer|honest|old|interesting|uniform|european)",
 'the_unique':r"\bthe (sun|moon|sky|sea|world|same|first|second|last|next|best|worst|most|biggest|tallest|only|internet|piano|guitar|violin|cinema|radio)\b",
 'art_general':{'articles':r"$^"},'art_names':r"\b(Latvia|Spain|France|Italy|Germany|Riga|London|Paris|Europe|Asia|Africa|Netherlands|United (States|Kingdom)|USA|UK|Alps|Daugava|Baltic|Atlantic|Pacific|Thames|Nile|Lake|Mount|Spanish|English|French|German|Latvian|Japan|China|Poland|Estonia|Lithuania|Sweden|Norway|Finland)\b",
 'adv_position':lambda i,tx: i['kind']=='order',
 'adv_degree':r"\b(very|really|quite|extremely)\b (?!amazing|perfect|exhausted|delicious|terrible|awful|fantastic|freezing|huge|tiny|brilliant)\w+|very much",
 'adv_extreme':r"\b(absolutely|completely|totally|utterly)\b|\bvery (amazing|perfect|exhausted|delicious|terrible|awful|fantastic|freezing|huge|tiny|brilliant)",
 'adj_basic':r"\bsmalls\b|\bbigs\b|\bolds\b|\bnews\b",
 'cmp_adv':r"more \w+ly\b|\b(faster|harder|earlier|later|better|worse)\b than\b.*\b(runs?|works?|drives?|arrived?|speaks?|sings?|plays?|types?)\b|\b(runs?|works?|drives?|speaks?|sings?|plays?) (\w+ )?(faster|harder|better|worse|more)\b",
 'cmp_as':r"\bas \w+ as\b|as ___ as|\bnot as\b|the same|different from",
 'cmp_less':r"\bless\b|\bleast\b|than I (am|do|did|was)\b",
 'so_that':r"\b(so|such)\b.*\bthat (I|we|he|she|they|it|you|nobody|everyone|the|my|no one)\b|join|one sentence",
 'conj_so_bec':r"\bso\b|\bbecause\b",'conj_parallel':r"\w+ing (and|or) \w+ing|\band (left|went|sat|took|closed|opened)\b",
 'during_while':r"\bduring\b|\bwhile\b",'by_until':r"\bby (five|six|seven|eight|nine|ten|noon|midnight|friday|monday|tomorrow|the end|then|next|\d)|\buntil\b|\btill\b",
 'reason_b1':r"\b(as|since)\b (it|he|she|we|they|you|I|the|there|my)\b",
 'rel_obj':r"\b(that|which|who) (I|we|you|they|he|she|my|our)\b|\b(the|a) \w+ (I|we|you|they|he|she) (bought|saw|met|read|made|wrote|told|gave|found|like|liked|need|want|recommended|ordered|borrowed|lost|watched|chose|sent|use|love|know)\b",
 'rel_where_whose':r"\b(where|whose|who's)\b",'rel_what':r"\bwhat\b",
 'rel_nondef':r",\s*(who|which|whose|where|that)\b",'rel_which_all':r", which (was|is|means|meant|made|makes|surprised|annoyed|explains|shows|proved)\b",
 'rel_prep':r"\b(to|with|for|about|in|from|of) (whom|which)\b|\b(live in|talking to|talked about|looking for|work with|worked for|listening to|waiting for|stayed at|applied for|telling you about|talking about)[.?!]?\s*$",
 'prep_none':r"\b(next|last|this|every) (monday|tuesday|wednesday|thursday|friday|saturday|sunday|week|year|month|weekend|summer|morning|evening|day|time)\b|=> —",
 'dep_adj':{'dep_prepositions':r"\b(good|bad|afraid|interested|proud|different|married|keen|fond|tired|angry|annoyed|worried|excited|surprised|bored|famous|responsible|similar|full|aware|capable|sorry|kind|nice|scared|frightened|pleased|disappointed|crazy|ready|late|sure|typical|short|jealous|ashamed|fed up|happy|engaged|related)\b (___|at|of|in|to|about|with|for|from|on|by)\b",'adj_ed_ing':r"\b(interested|bored|excited|surprised|annoyed|tired|worried|frightened|pleased|disappointed) (___|in|with|about|at|of|by)\b"},
 'dep_basic':r"\b(listen\w*|look\w*|wait\w*|talk\w*|speak\w*|ask\w*|pay\w*|paid) (___|to|at|for)\b",
 'dep_none':r"=> —|\b(discuss\w*|call\w*|phone\w*|join\w*|answer\w*|enter\w*|reach\w*|marr\w+|contact\w*|attend\w*)\b",
 'prep_move':{'dep_prepositions':r"\barriv\w+\b",'prep_time_place':r"\barriv\w+\b|\b(into|out of|across|through|along|past|towards)\b"},
 'each_every':r"\b(every|each)\b (?!one\b|body|thing|where|day|week|year|month|morning|evening|time)\w+",
 'unc_nouns':r"\b(advice|advices|information|informations|furniture|news|luggage|hair|homework|equipment|knowledge)\b",
 'sup_ever':r"\b(I|we|she|he|they|you)('ve|'s| have| has) ever\b.*|ever (seen|read|eaten|had|been|met|visited|heard|tasted|watched)",
 'used_to_ps':r"\busually\b|last (year|week|month|summer|night)|\bonce\b|in 20\d\d|yesterday",
}
PRIO={'pastc_two':5,'able_once':5,'deduction':5,'pas_act':6,'will_going':7,'rather_you':5,'wish_would':6,'wish_past':5,'rel_which_all':6,'rel_prep':5,'purpose_b2':5,'prep_transport':5,'some_offers':5,'vp_meaning':8,'vp_obj_to':7,'vp_make_let':7,'vp_to_ing':6,'vp_prep_ing':5,'if_when':6,'rep_say_tell':7,'rep_orders':5,'sup_ever':8,'cmp_double':6,'cmp_modify':5,'adv_position':1,'adv_extreme':5,'pp_ppc':4,'ppc_result':5,'c1_unless':6,'neednt_have':6,'pc_always':6,'tag_special':5,'whoever':6,'iq_to':5,'iq_subject':7,'pp_ps':3,'ps_pc':3,'few_little':5,'a_few':4,'too_enough':6,'no_none':3,'unc_nouns':5,'plural_only':5,'each_every':3,'agr_head':5,'the_adj':6,'art_places':4,'adv_irreg':4,'link_adj':3}
ONLY={'narrative':['narr_mix'],'cmp_ps_pc':['pastc_when','past_seq']}
bytopic=collections.defaultdict(list)
for p in P:
    for t in p['topics']: bytopic[t].append(p)
EXPL={'cmp_ps_pc':'pastc_when','adj_ed_ing':'eding','adj_order':'adj_order','dep_prepositions':'dep_verb','agreement':'agr_basic','conj_basic':'conj_and_but','conj_clauses':'contrast_b1','conj_b2':'contrast_b2','quantity':'much_many','adverbs':'adj_adv','verb_patterns':'vp_ing','comparison':'cmp_er','so_such':'so_such_basic','prep_time_place':'prep_time','irregular_plurals':'plural_irr','indefinite_pronouns':'indef_form','relative_clauses':'rel_subj','two_objects':'two_obj','unreal_time':'its_time_past','ind_advanced':'iq_whether','ind_polite':'iq_wh','question_tags':'tag_basic','subject_object_q':'q_subject','aux_verbs':'q_yesno','rep_verbs':'rv_ing','rep_questions':'rep_q_wh','rep_statements':'rep_backshift','cond_advanced':'c_inv','used_to':'used_to','causative':'caus_have','passive_modals':'pas_modal','more_modals':'be_able','narrative':'narr_mix','past_perfect':'pastp_form','present_perfect':'pp_form','modal_verbs':'must_have_to','past_simple':'pst_reg','articles':'a_the','articles_b1':'art_general','future':'will_form','conj_linkers':'link_however','time_clauses':'fut_time_clause','cmp_pp_ps':'pp_ps','present_perfect_continuous':'ppc_form','cond_zero':'c0','cond_first':'c1','cond_second':'c2','cond_third':'c3','cond_mixed':'c_mixed','narrative_b2':'pastpc','present_simple':'ps_form','present_continuous':'pc_form','past_continuous':'pastc_form','present_simple_passive':'pas_pres','past_simple_passive':'pas_past','present_continuous_passive':'pas_cont','present_perfect_passive':'pas_perf','future_passive':'pas_will'}
def default(t,lv):
    c=[p for p in bytopic[t] if p['topics'][0]==t and lv in p['dl']]
    return c[0] if c else BY[EXPL[t]]
def rule(p,t):
    r=OVR.get(p['id'],p['rx']) if p['id'] in OVR else p['rx']
    if isinstance(r,dict): r=r.get(t, None if p['id'] in ('pastc_when','pastc_two','q_wh','iq_whether','art_general','pastp_form','pastp_by','fut_time_clause','ps_pc','stative','pp_ps','c0_c1','vp_prep_ing','because_of','dep_adj','prep_move') else p['rx'])
    return r
def classify(i):
    t=i['skill']; tx=text(i)
    cands=[p for p in bytopic[t] if t not in ONLY or p['id'] in ONLY[t]]
    for p in sorted(cands,key=lambda p:-PRIO.get(p['id'],0)):
        r=rule(p,t)
        if r is None: continue
        if callable(r):
            if r(i,tx): return p['id']
        elif re.search(r,tx,re.I): return p['id']
    return default(t,i['level'])['id']
res=collections.defaultdict(list)
for i in items:
    i['_p']=classify(i); res[i['_p']].append(i)
json.dump({i['id']:i['_p'] for i in items},open(S+'assign.json','w'))
if __name__=='__main__':
    LV=['A2.1','A2.2','B1.1','B1.2','B2.1','B2.2']; arg=sys.argv[1:]; import random; random.seed(1)
    for t in ([a for a in arg if a in bytopic] or sorted(bytopic)):
        if t=='new': continue
        print('##',t)
        for p in bytopic[t]:
            its=[i for i in res[p['id']] if i['skill']==t]
            c=collections.Counter(i['level'] for i in its)
            print('  ',p['id'],p['level'],len(its),' '.join(f"{l}:{c[l]}" for l in LV if c[l]))
            if arg:
                for i in random.sample(its,min(3,len(its))): print('      ',i['level'],i['kind'],'|',text(i)[:140].replace('\n',' '))
