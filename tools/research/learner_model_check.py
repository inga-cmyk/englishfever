import pandas as pd, numpy as np, math, json
from sklearn.metrics import roc_auc_score, log_loss, brier_score_loss
import sys
A=sys.argv[1]   # research answers export (answers.csv); never commit the data
a=pd.read_csv(A,encoding='utf-8-sig')
BASE={'A2.1':1,'A2.2':2,'B1.1':3,'B1.2':4,'B2.1':5,'B2.2':6,'C1.1':7,'C1.2':8}
a['d']=a.level.map(BASE)+(a.bloom-1)*0.2
a['base']=a.item.str.replace(r'-r\d+$','',regex=True)
a['first']=~a.duplicated(['pid','base'])
assert (a.groupby('pid').study_day.diff().dropna()>=0).all(), 'rows not in time order'
ev=a[a.task_role!='learn'].copy()
def fit(pts):
    th=3.0
    for _ in range(30):
        g=h=0.0
        for d,ok in pts:
            p=1/(1+math.exp(-1.7*(th-d))); g+=1.7*(ok-p); h+=2.89*p*(1-p)
        g-=(th-3)/9; h+=1/9
        st=max(-1.5,min(1.5,g/h)); th=max(0,min(10,th+st))
        if abs(st)<1e-4: break
    return th
rows=[]
glob=ev.correct.mean()
for pid,g in ev.groupby('pid',sort=False):
    hist=[]
    others=ev[ev.pid!=pid]
    lvmean=others.groupby('level').correct.mean().to_dict(); om=others.correct.mean()
    rolelv=others.groupby(['level','task_role']).correct.mean().to_dict()
    for r in g.itertuples():
        if len(hist)>=10:
            th=fit(hist[-60:])
            p_app=1/(1+math.exp(-1.7*(th-r.d)))
            run=np.mean([h[1] for h in hist[-60:]])
            rows.append(dict(pid=pid,y=r.correct,first=r.first,level=r.level,role=r.task_role,n_hist=len(hist),theta=th,d=r.d,
                p_app=p_app,p_const=om,p_run=run,p_level=lvmean.get(r.level,om),p_rolelv=rolelv.get((r.level,r.task_role),om),mode=r.mode))
        hist.append((r.d,r.correct))
P=pd.DataFrame(rows); P.to_csv('pred.csv',index=False)
print('predictions',len(P),'learners',P.pid.nunique(),'base rate',round(P.y.mean(),3))
models=['p_const','p_level','p_rolelv','p_run','p_app']
def met(df):
    out={}
    for m in models:
        p=df[m].clip(0.02,0.98)
        out[m]=(roc_auc_score(df.y,p) if df[m].nunique()>1 else 0.5, log_loss(df.y,p), brier_score_loss(df.y,p))
    return out
def show(df,name):
    print('\n==',name,len(df))
    for m,(auc,ll,br) in met(df).items(): print(f'{m:10s} AUC {auc:.3f}  logloss {ll:.3f}  Brier {br:.3f}')
show(P,'all evidence answers'); show(P[P['first']],'first exposure only'); show(P[P['mode']=='practice'],'practice only')
# combined: logistic on logit(p_app) + learner-independent? simple recalibration slope
from sklearn.linear_model import LogisticRegression
X=np.log(P.p_app.clip(.02,.98)/(1-P.p_app.clip(.02,.98))).values.reshape(-1,1)
lr=LogisticRegression(C=1e6).fit(X,P.y); print('\ncalibration slope',lr.coef_[0][0].round(2),'intercept',lr.intercept_[0].round(2))
# calibration table
P['bin']=pd.cut(P.p_app,[0,.5,.6,.7,.8,.9,1.0])
print(P.groupby('bin',observed=True).agg(n=('y','size'),pred=('p_app','mean'),obs=('y','mean')).round(3))
# within-learner AUC (does it rank a learner's own answers?)
w=[]
for pid,g in P.groupby('pid'):
    if g.y.nunique()>1 and len(g)>=40: w.append((len(g),roc_auc_score(g.y,g.p_app),roc_auc_score(g.y,g.p_rolelv)))
w=np.array(w); print('\nwithin-learner AUC, learners',len(w),'app mean',w[:,1].mean().round(3),'level+role mean',w[:,2].mean().round(3))
# cluster bootstrap for AUC differences
rng=np.random.default_rng(1); pids=P.pid.unique(); res={m:[] for m in models}; dd=[]
grp={p:g for p,g in P.groupby('pid')}
for b in range(1000):
    s=pd.concat([grp[p] for p in rng.choice(pids,len(pids))])
    if s.y.nunique()<2: continue
    aa={m:roc_auc_score(s.y,s[m]) if s[m].nunique()>1 else .5 for m in models}
    for m in models: res[m].append(aa[m])
    dd.append((aa['p_app']-aa['p_run'],aa['p_app']-aa['p_rolelv']))
for m in models: print(m,'AUC 95% CI',np.percentile(res[m],[2.5,97.5]).round(3))
dd=np.array(dd); print('app-run diff CI',np.percentile(dd[:,0],[2.5,97.5]).round(3),'app-rolelv diff CI',np.percentile(dd[:,1],[2.5,97.5]).round(3))
# by history length
P['hb']=pd.cut(P.n_hist,[9,30,60,150,2000],labels=['10-30','31-60','61-150','151+'])
for hb,g in P.groupby('hb',observed=True): print(hb,len(g),'AUC app',round(roc_auc_score(g.y,g.p_app),3),'logloss',round(log_loss(g.y,g.p_app.clip(.02,.98)),3),'const ll',round(log_loss(g.y,g.p_const.clip(.02,.98)),3))
