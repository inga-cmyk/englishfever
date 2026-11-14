import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import lib, p1, p2, p3, fixes, p4, collections
P=lib.POINTS; ids=[p['id'] for p in P]
LV=['A2.1','A2.2','B1.1','B1.2','B2.1','B2.2','C1']
by={p['id']:p for p in P}
dup=[i for i,c in collections.Counter(ids).items() if c>1]; print('points',len(P),'dup',dup)
for p in P:
    for k in ('needs','vs'):
        for x in p[k]:
            if x not in by: print('UNKNOWN',p['id'],k,x)
            elif k=='needs' and LV.index(by[x]['level'])>LV.index(p['level']): print('NEED LATER',p['id'],p['level'],'needs',x,by[x]['level'])
    if p['id'] in p['needs']: print('SELF',p['id'])
# cycles
def cyc(i,st,seen):
    if i in st: return st[st.index(i):]+[i]
    if i in seen: return None
    seen.add(i)
    for n in by[i]['needs']:
        if n in by:
            r=cyc(n,st+[i],seen)
            if r: return r
seen=set()
for i in ids:
    r=cyc(i,[],seen)
    if r: print('CYCLE',r)
print(collections.Counter(p['level'] for p in P)); print('new',sum(p['topics']==['new'] for p in P))
import json; mt=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','app/content/meta.json')))
tids={s['id'] for s in mt['skills']}; used=set()
for p in P:
    for t in p['topics']:
        if t!='new' and t not in tids: print('BAD TOPIC',p['id'],t)
        used.add(t)
print('topics without a point',tids-used)
for t in tids:
    ds=[p['id'] for p in P if t in p['topics'] and p['d']]
    if len(ds)!=1: print('DEFAULT',t,ds)
