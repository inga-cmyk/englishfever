import sys,json,re,collections,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import classify as C
S=C.S
K={'mcq':'m','gap':'g','order':'o','text':'t','match':'x','write':'w'}
LVL={'A2.1':1,'A2.2':2,'B1.1':3,'B1.2':4,'B2.1':5,'B2.2':6}
BOIL=[r"^Choose the correct (option|form|word|answer)[:.]?\s*",r"^Complete (the sentence )?(with )?(one word|the correct form)?[:.]?\s*",r"^Put the words in order\.?\s*",r"^Which sentence is correct\??\s*",r"^Write the missing word( or words)?[:.]?\s*",r"^Use the verbs? in brackets[:.]?\s*",r"^Complete[:.]\s*"]
def line(i):
    q=i.get('q','')
    for b in BOIL: q=re.sub(b,'',q,flags=re.I)
    q=re.sub(r"^Which sentence is NOT correct\??\s*",'NOT: ',q,flags=re.I)
    q=re.sub(r"^Correct the (mistake|sentence)[:.]?\s*",'FIX: ',q,flags=re.I)
    k=i['kind']
    if k=='order': body=i.get('sentence','')
    elif k=='match': body=q[:50]+' :: '+' / '.join(a+' + '+b for a,b in i.get('pairs',[])[:3])
    elif k=='mcq': body=q+' => '+str(i.get('correct'))+' | '+' / '.join(str(w) for w in (i.get('wrong') or []))
    elif k=='write': body=q
    else: body=q+' => '+C.ans(i)
    return re.sub(r'\s+',' ',body)[:150]
# stable index per topic
idx={}
by=collections.defaultdict(list)
for i in C.items: by[i['skill']].append(i)
for t,its in by.items():
    for n,i in enumerate(its): idx[i['id']]=(t,n)
def key(i):   # the same key as app/tests/item_gates_test.py
    body = i.get("correct") or i.get("sentence") or (" ; ".join(a + " = " + b for a, b in i["pairs"]) if i.get("pairs") else "") or ""
    return " | ".join([i["skill"], i["level"], i["kind"], i["q"], body])
ASSIGN=json.load(open(os.path.join(C.HERE,'assign_keys.json'),encoding='utf-8'))
def point(i):
    a=ASSIGN.get(key(i))
    return a[0] if a and a[0] in C.BY else i['_p']
def how(i):
    a=ASSIGN.get(key(i))
    return a[1] if a else 'rule (new or changed task)'
if __name__=='__main__':
    for t in sys.argv[1:]:
        if t=='sizes':
            print({t:sum(len(line(i))+8 for i in its) for t,its in by.items()}); continue
        print('##',t,len(by[t]),'| points:',' '.join(p['id'] for p in C.bytopic[t]))
        g=collections.defaultdict(list)
        for n,i in enumerate(by[t]): g[point(i)].append((n,i))
        for p,its in g.items():
            print('>',p,len(its))
            for n,i in its: print(f"{n} {LVL[i['level']]}{K[i['kind']]}{'L' if i['role']=='learn' else ''} {line(i)}")
