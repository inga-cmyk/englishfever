const { chromium } = require('playwright');
const BASE = 'http://127.0.0.1:8099';
(async () => {
  const b = await chromium.launch(); let ok = true; const errs = [];
  const check = (n, c, x) => { ok = ok && !!c; console.log((c ? 'PASS ' : 'FAIL ') + n + (c ? '' : ' -> ' + JSON.stringify(x))); };
  const ctx = await b.newContext({ viewport: { width: 1100, height: 900 } }); const p = await ctx.newPage();
  p.on('pageerror', e => errs.push(e.message));
  await p.goto(BASE + '/index.html'); await p.waitForSelector('#nick'); await p.waitForTimeout(1400); await p.click('button[type=submit]'); await p.waitForSelector('.hello h1');
  const post = (r, d) => p.evaluate(async ([r, d]) => (await fetch('api.php?r=' + r, { method: 'POST', headers: { 'X-EF': '1', 'Content-Type': 'application/json' }, body: JSON.stringify(d) })).json(), [r, d]);
  let s0; for (let k = 0; k < 40; k++) { s0 = await post('session/start', { mode: 'practice', skills: ['present_simple'], level: 'A2.1', length: 10 }); if (s0.item.id === 'ps-A21-1a') break; } // this test needs that task
  await p.goto(BASE + '/index.html#/session'); await p.reload(); await p.waitForSelector('.task .q');
  const opts = await p.locator('label.opt').evaluateAll(a => a.map(x => x.getAttribute('data-opt')));
  const wrong = opts.find(o => o !== 'works');
  await p.locator('label.opt[data-opt="' + wrong + '"]').click(); await p.click('.task .btn:has-text("Check answer")'); await p.waitForSelector('.feedback');
  const ems = await p.locator('.feedback p em, .feedback .ans em').allInnerTexts();
  check('English: examples in the explanation are in italics', ems.length >= 2 && ems.join('|').includes('she works'), ems);
  const whyHtml = await p.locator('.feedback p', { hasText: 'Why:' }).innerHTML();
  check('the explanation is plain text around <em> only', !/[*]/.test(whyHtml) && /<em>/.test(whyHtml), whyHtml);
  // Latvian
  await p.click('.feedback .linkbtn:has-text("Latviski")'); await p.waitForTimeout(200);
  const emsLv = await p.locator('.feedback p em').allInnerTexts();
  check('Latvian: the English words are italic, the Latvian words are not', emsLv.length >= 2 && emsLv.join('|').includes('she works') && !emsLv.some(t => /pievieno|darbības|vārdam/.test(t)), emsLv);
  const kapec = await p.locator('.feedback p', { hasText: 'Kāpēc' }).innerText();
  check('Latvian explanation text reads normally (no stars)', !/\*/.test(kapec) && /Ar /.test(kapec), kapec);
  // rule card
  await p.click('.feedback details.rule summary'); await p.waitForTimeout(150);
  const ruleEm = await p.locator('.feedback details.rule em').allInnerTexts();
  check('rule card: forms, signal words and the example are in italics', ruleEm.some(t => /^always/.test(t)) && ruleEm.some(t => /She works/.test(t)) && ruleEm.some(t => t === 'She starts work at eight every day.'), ruleEm);
  const bold = await p.locator('.feedback details.rule').innerText();
  check('rule card has no stars', !/\*/.test(bold));
  // rules page
  await p.goto(BASE + '/index.html#/rules'); await p.waitForSelector('details.rule, .rulecard, h1'); await p.waitForTimeout(300);
  check('rules page: no stars anywhere on screen', !/\*/.test(await p.locator('body').innerText()));
  // markup in text cannot become elements
  const x = await p.evaluate(() => { const f = UI.rich('<img src=x onerror=alert(1)> and *a<b>b*'); const d = document.createElement('div'); d.appendChild(f); return { imgs: d.querySelectorAll('img').length, bs: d.querySelectorAll('b').length, ems: d.querySelectorAll('em').length, text: d.textContent }; });
  check('rich(): markup in the text stays text', x.imgs === 0 && x.bs === 0 && x.ems === 1 && x.text.includes('<img'), x);
  check('no page errors', errs.length === 0, errs);
  console.log(ok ? '\nALL PASS' : '\nSOME FAILED'); await b.close(); process.exit(ok ? 0 : 1);
})();
