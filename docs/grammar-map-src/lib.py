POINTS=[]; _area=[None]
def AREA(a): _area[0]=a
def P(id,name,level,can,n='',v='',e='',m='',t='',g='',topic='new',rx=None,d=0,dl='',s='',s2=''):
    POINTS.append(dict(id=id,name=name,level=level,can=can,needs=n.split(),vs=v.split(),err=e,mu=m,te=t,egp=g,topics=topic.split(),rx=rx,d=d,dl=dl.split(),note=' '.join(x for x in (s,s2) if x),area=_area[0]))
