import sys,json,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import build as B, p4
P=B.P
data=[dict(id=p['id'],n=p['name'],l=p['level'],a=p['area'].split(' · ',1)[-1] if p['level'][0]=='C' else p['area'],c=p['can'],nd=p['needs'],vs=p['vs'],ld=p['leads'],e=p['err'],s=B.src(p),
           t=[B.TOP[t]['label'] for t in p['topics']] if p['topics']!=['new'] else [],k=B.content(p),cu=p['cu'],st=('none' if p['n']==0 else 'thin' if p['cu']<10 else 'ok')) for p in P]
strands={k.split(' · ',1)[-1]:v for k,v in p4.STRANDS.items()}
html=r'''<meta name="claude:viewport-fit-sides" content="cover">
<title>Gramatikas karte</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,400;0,500;0,600;1,400&family=Space+Grotesk:wght@500;600&display=swap">
<style>
/* layout: a sticky band with level switch and search; below it one column of grammar areas, each a list of points that open in place */
:root{--bg:#f6f8f8;--surface:#ffffff;--fg:#16242a;--muted:#5a6b72;--line:#d9e1e3;--accent:#0b6b74;--accent-soft:#e0f0f1;--ok:#2f7d4f;--thin:#a36a00;--none:#b3413a;--chip:#eef2f3;
 --display:"Space Grotesk","Segoe UI",system-ui,sans-serif;--body:"Inter","Segoe UI",system-ui,sans-serif}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#10181b;--surface:#172226;--fg:#e6eef0;--muted:#9bb0b6;--line:#2a3a40;--accent:#5cc3cc;--accent-soft:#17343a;--ok:#6fcf97;--thin:#e6b450;--none:#f08a80;--chip:#1f2d32;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#10181b;--surface:#172226;--fg:#e6eef0;--muted:#9bb0b6;--line:#2a3a40;--accent:#5cc3cc;--accent-soft:#17343a;--ok:#6fcf97;--thin:#e6b450;--none:#f08a80;--chip:#1f2d32;color-scheme:dark}
body{background:var(--bg);color:var(--fg);font-family:var(--body);font-size:15px;line-height:1.5}
.wrap{max-width:980px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
header .wrap{padding-block:28px 12px}
h1{font-family:var(--display);font-weight:600;font-size:clamp(26px,5vw,36px);margin:0 0 6px;text-wrap:balance}
.lede{color:var(--muted);max-width:65ch;margin:0}
.totals{display:flex;flex-wrap:wrap;gap:8px 22px;margin:16px 0 0;padding:0;list-style:none;font-variant-numeric:tabular-nums}
.totals b{font-family:var(--display);font-size:20px;margin-right:6px}
.bar{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;background:var(--bg);border-bottom:1px solid var(--line)}
body::before{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);z-index:10;background:var(--bg)}
.bar .wrap{display:flex;flex-wrap:wrap;gap:10px;align-items:center;padding-block:10px}
.levels{display:flex;flex-wrap:wrap;gap:6px}
.levels button,.filters button{font:inherit;font-weight:500;border:1px solid var(--line);background:var(--surface);color:var(--fg);padding:6px 11px;border-radius:999px;cursor:pointer;font-variant-numeric:tabular-nums}
.levels button[aria-pressed="true"],.filters button[aria-pressed="true"]{background:var(--accent);border-color:var(--accent);color:var(--bg)}
button:focus-visible,input:focus-visible,summary:focus-visible,a:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
#q{font:inherit;flex:1 1 180px;min-width:0;padding:7px 12px;border:1px solid var(--line);border-radius:8px;background:var(--surface);color:var(--fg)}
.filters{display:flex;flex-wrap:wrap;gap:6px}
main .wrap{padding-block:18px 60px;display:flex;flex-direction:column;gap:26px}
section h2{font-family:var(--display);font-weight:600;font-size:19px;margin:0 0 8px;display:flex;gap:10px;align-items:baseline;flex-wrap:wrap}
section h2 small{font-family:var(--body);font-weight:400;font-size:13px;color:var(--muted)}
.strand{font-size:13.5px;color:var(--muted);margin:0 0 10px;max-width:80ch}
.strand b{color:var(--fg);font-weight:600}
.pts{display:flex;flex-direction:column;border:1px solid var(--line);border-radius:10px;background:var(--surface);overflow:hidden}
details+details{border-top:1px solid var(--line)}
summary{list-style:none;cursor:pointer;display:grid;grid-template-columns:auto 1fr auto;gap:10px;align-items:baseline;padding:10px 14px}
summary::-webkit-details-marker{display:none}
.lv{font-family:var(--display);font-size:12px;font-weight:600;color:var(--accent);letter-spacing:.02em;min-width:34px}
.nm{font-weight:500;min-width:0}
.dot{font-size:12px;white-space:nowrap;color:var(--muted)}
.dot i{display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:5px;vertical-align:baseline}
.ok i{background:var(--ok)}.thin i{background:var(--thin)}.none i{background:transparent;border:1.5px solid var(--none)}
details[open]>summary{background:var(--accent-soft)}
.body{padding:4px 14px 16px;display:grid;grid-template-columns:118px 1fr;gap:8px 14px;font-size:14px}
.body dt{color:var(--muted);font-size:12px;text-transform:uppercase;letter-spacing:.06em;padding-top:3px}
.body dd{margin:0;min-width:0;overflow-wrap:anywhere}
.can{font-size:15px}
.chips{display:flex;flex-wrap:wrap;gap:6px}
.chips a{text-decoration:none;color:var(--fg);background:var(--chip);border:1px solid var(--line);border-radius:6px;padding:2px 8px;font-size:13px}
.chips a span{color:var(--accent);font-size:11px;font-weight:600;margin-right:5px}
.chips a:hover{border-color:var(--accent)}
.src{color:var(--muted);font-size:13px}
.empty{color:var(--muted)}
code{font-family:ui-monospace,Menlo,monospace;font-size:12px;color:var(--muted)}
@media (max-width:560px){.body{grid-template-columns:1fr;gap:2px 0}.body dt{padding-top:10px}summary{grid-template-columns:auto 1fr}.dot{grid-column:2}}
@media (prefers-reduced-motion:no-preference){details[open] .body{animation:in .15s ease-out}@keyframes in{from{opacity:.4}to{opacity:1}}}
</style>
<header><div class="wrap">
<h1>Gramatikas karte</h1>
<p class="lede">Visi gramatikas punkti no A2.1 līdz C1: ko izglītojamais prot, kas jāprot pirms tam, uz ko punkts ved tālāk un kas lietotnē jau ir. Punktu teksts ir angliski, kā kartē <code>docs/GRAMMAR-MAP.md</code>.</p>
<ul class="totals" id="totals"></ul>
</div></header>
<div class="bar"><div class="wrap">
<div class="levels" id="levels" role="group" aria-label="Līmenis"></div>
<input id="q" type="search" placeholder="Meklēt: wish, passive, used to…" aria-label="Meklēt punktu">
<div class="filters" id="filters" role="group" aria-label="Saturs"></div>
</div></div>
<main><div class="wrap" id="out"></div></main>
<script>
const D=__DATA__, STR=__STR__;
const LV=["A2.1","A2.2","B1.1","B1.2","B2.1","B2.2","C1"], BY=Object.fromEntries(D.map(p=>[p.id,p]));
const ST={ok:"10 un vairāk uzdevumu",thin:"1 līdz 9 uzdevumi",none:"uzdevumu nav"};
let lv="A2.1", fl="all", q="";
const esc=s=>s.replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const em=s=>esc(s).replace(/\*([^*]+)\*/g,"<em>$1</em>");
const chips=a=>a.length?'<div class="chips">'+a.map(i=>`<a href="#p-${i}" data-go="${i}"><span>${BY[i].l}</span>${esc(BY[i].n)}</a>`).join("")+"</div>":'<span class="empty">nav</span>';
function row(p){return `<details id="p-${p.id}"><summary><span class="lv">${p.l}</span><span class="nm">${esc(p.n)}</span><span class="dot ${p.st}"><i></i>${ST[p.st]}</span></summary>
<dl class="body"><dt>Prot</dt><dd class="can">${em(p.c)}</dd>
<dt>Vajag pirms</dt><dd>${chips(p.nd)}</dd><dt>Ved uz</dt><dd>${chips(p.ld)}</dd><dt>Jauc ar</dt><dd>${chips(p.vs)}</dd>
<dt>Tipiskas kļūdas</dt><dd>${p.e?em(p.e):'<span class="empty">nav ierakstītas</span>'}</dd>
<dt>Avoti</dt><dd class="src">${em(p.s)}</dd>
<dt>Lietotnē</dt><dd>${p.t.length?esc(p.t.join("; "))+"<br>":""}<span class="src">${esc(p.k==="none"?"nav ne kartītes, ne uzdevumu":p.k)}</span> <code>${p.id}</code></dd></dl></details>`}
function draw(){
  const words=q.toLowerCase().split(/\s+/).filter(Boolean);
  let pts=D.filter(p=>(words.length||p.l===lv)&&(fl==="all"||p.st===fl)&&words.every(w=>(p.n+" "+p.c+" "+p.id+" "+p.e).toLowerCase().includes(w)));
  const areas=[...new Set(pts.map(p=>p.a))];
  document.getElementById("out").innerHTML=areas.length?areas.map(a=>{const s=pts.filter(p=>p.a===a);
    return `<section><h2>${esc(a)} <small>${s.length} ${s.length===1?"punkts":"punkti"}</small></h2>${STR[a]?`<p class="strand"><b>Redzētie avoti:</b> ${em(STR[a][0])}.<br><b>Vajadzīgās uzdevumu formas:</b> ${em(STR[a][1])}.</p>`:""}<div class="pts">${s.map(row).join("")}</div></section>`}).join(""):'<p class="empty">Nekas neatbilst. Noņem filtru vai meklē citu vārdu.</p>';
  document.querySelectorAll("#levels button").forEach(b=>b.setAttribute("aria-pressed",String(!words.length&&b.dataset.l===lv)));
  document.querySelectorAll("#filters button").forEach(b=>b.setAttribute("aria-pressed",String(b.dataset.f===fl)));
}
document.getElementById("levels").innerHTML=LV.map(l=>`<button data-l="${l}">${l} <span style="opacity:.7">${D.filter(p=>p.l===l).length}</span></button>`).join("");
document.getElementById("filters").innerHTML=[["all","visi"],["ok","10 un vairāk"],["thin","1 līdz 9"],["none","uzdevumu nav"]].map(([f,t])=>`<button data-f="${f}">${t}</button>`).join("");
document.getElementById("totals").innerHTML=[[D.length,"punkti"],[D.filter(p=>p.st==="ok").length,"ar 10 un vairāk uzdevumiem"],[D.filter(p=>p.st==="thin").length,"ar 1 līdz 9"],[D.filter(p=>p.st==="none"&&p.l[0]!=="C").length,"bez uzdevumiem, A2 līdz B2"],[D.filter(p=>p.l[0]==="C").length,"C1 punkti"]].map(([n,t])=>`<li><b>${n}</b>${t}</li>`).join("");
document.getElementById("levels").onclick=e=>{const b=e.target.closest("button");if(!b)return;lv=b.dataset.l;q="";document.getElementById("q").value="";draw();try{history.replaceState(null,"","#"+lv.replace(".","-"))}catch(_){}};
document.getElementById("filters").onclick=e=>{const b=e.target.closest("button");if(!b)return;fl=b.dataset.f;draw()};
document.getElementById("q").oninput=e=>{q=e.target.value;draw()};
document.getElementById("out").onclick=e=>{const a=e.target.closest("a[data-go]");if(!a)return;e.preventDefault();const p=BY[a.dataset.go];lv=p.l;fl="all";q="";document.getElementById("q").value="";draw();const el=document.getElementById("p-"+p.id);el.open=true;el.scrollIntoView({block:"center"})};
const h=(location.hash||"").slice(1).replace("-",".");if(LV.includes(h))lv=h;
draw();
</script>
'''
html=html.replace('__DATA__',json.dumps(data,ensure_ascii=False).replace('</','<\\/')).replace('__STR__',json.dumps(strands,ensure_ascii=False).replace('</','<\\/'))
open(B.C.S+'gramatikas-karte.html','w').write(html); print(len(html))
