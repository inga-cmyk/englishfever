const { chromium } = require('playwright');
const fs = require('fs');
const BASE = 'http://127.0.0.1:8099', OUT = __dirname + '/shots/';
fs.mkdirSync(OUT, { recursive: true });
const raw = JSON.parse(fs.readFileSync('/home/user/englishfever/app/content/items.json', 'utf8'));
const ITEMS = {}; (Array.isArray(raw) ? raw : raw.items).forEach(i => { ITEMS[i.id] = i; });
let ok = true; const errors = [];
function check(n, c, x) { ok = ok && !!c; console.log((c ? 'PASS ' : 'FAIL ') + n + (c ? '' : '  -> ' + x)); }
const esc = t => t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 420, height: 900 } }); await ctx.addInitScript(() => {
    try { localStorage.setItem('ef_sound', '1'); } catch (e) {}
    window.__notes = 0;
    window.AudioContext = class { constructor() { this.state = 'running'; this.currentTime = 0; this.destination = {}; }
      createOscillator() { window.__notes++; return { type: '', frequency: { value: 0 }, connect() {}, start() {}, stop() {} }; }
      createGain() { return { gain: { setValueAtTime() {}, exponentialRampToValueAtTime() {} }, connect() {} }; } resume() {} };
  });
  const page = await ctx.newPage();
  page.on('pageerror', e => errors.push(e.message));
  await page.goto(BASE + '/sso-demo.php?uid=' + (8000 + Math.floor(Math.random() * 900)) + '&name=Comeback%20UI');
  await page.waitForSelector('#fn'); await page.click('button[type=submit]'); await page.waitForSelector('.hello h1');
  const post = (r, d) => page.evaluate(async ([r, d]) => (await fetch('api.php?r=' + r, { method: 'POST', headers: { 'X-EF': '1', 'Content-Type': 'application/json' }, body: JSON.stringify(d) })).json(), [r, d]);
  let s = await post('session/start', { mode: 'practice', skills: ['present_simple'], level: 'A2.1', length: 5 }), item = s.item;
  for (let i = 0; i < 5 && item; i++) { const a = await post('session/answer', { session_id: s.session.id, item_id: item.id, answer: 'zzz', time_ms: 2000 }); item = a.next; }
  await page.goto(BASE + '/index.html#/home'); await page.reload(); await page.waitForSelector('.card.focus');
  const card = page.locator('.card.fn-chance');
  check('Home shows the Second Chance card with the number of mistakes', await card.count() === 1 && /5 mistakes to fix/.test(await card.innerText()), await card.count() ? await card.innerText() : 'no card');
  await page.screenshot({ path: OUT + 'comeback-home.png', fullPage: true });
  await card.locator('button').click(); await page.waitForSelector('.task .q');
  check('the session is labelled Second Chance', /Second Chance/.test(await page.locator('.sess-top').innerText()));
  let fixedLines = 0, n = 0;
  for (let k = 0; k < 5; k++) {
    await page.waitForSelector('.task .q'); await page.waitForTimeout(150);
    const cur = await page.evaluate(async () => (await (await fetch('api.php?r=session/resume')).json()).resume);
    const it = ITEMS[cur.item.id];
    if (it.kind === 'mcq') await page.locator('label.opt', { hasText: it.correct }).first().click();
    else if (it.kind === 'gap' && it.bank) { for (let i = 0; i < it.answers.length; i++) await page.locator('.dnd-bank .chip', { hasText: new RegExp('^' + esc(it.answers[i][0]) + '$') }).first().click(); }
    else if (it.kind === 'gap') { const inputs = page.locator('.task .q input.blank'); for (let i = 0; i < await inputs.count(); i++) await inputs.nth(i).fill(it.answers[i][0]); }
    else if (it.kind === 'text') await page.fill('.task input.type-in', it.answers[0][0]);
    else if (it.kind === 'order') { for (const t of it.sentence.split(' ')) await page.locator('.dnd-bank .chip', { hasText: new RegExp('^' + esc(t) + '$') }).first().click(); }
    else if (it.kind === 'match') { for (const t of it.pairs.map(p => p[1])) await page.locator('.dnd-bank .chip', { hasText: new RegExp('^' + esc(t) + '$') }).first().click(); }
    else await page.fill('.task textarea.write', it.model);
    await page.click('.task .btn:has-text("Check answer")'); await page.waitForSelector('.feedback');
    if (await page.locator('.fixed-line').count()) fixedLines++;
    if (k === 0) { await page.screenshot({ path: OUT + 'comeback-feedback.png', fullPage: true }); check('fixing a mistake plays its own four-note chime (a plain right answer plays two)', (await page.evaluate(() => window.__notes)) === 4, await page.evaluate(() => window.__notes)); }
    n++; await page.click('.feedback .nextrow .btn'); await page.waitForTimeout(300);
    if (await page.locator('.wins, h1:has-text("Great job")').count()) break;
  }
  await page.waitForSelector('h1');
  const h1 = await page.locator('h1').first().innerText();
  check('every correct Comeback answer says "Mistake fixed"', fixedLines === 5, fixedLines);
  check('the summary praises with the number of fixed mistakes', /Great job! 5 mistakes fixed\./.test(h1), h1);
  check('the summary says nothing is waiting', /All clear/.test(await page.locator('body').innerText()));
  await page.screenshot({ path: OUT + 'comeback-summary.png', fullPage: true });
  await page.goto(BASE + '/index.html#/home'); await page.reload(); await page.waitForSelector('.card.focus');
  check('Home hides the card when nothing is waiting', await page.locator('.card.fn-chance').count() === 0);
  check('no page errors', errors.length === 0, errors);
  console.log(ok ? 'ALL PASS' : 'SOME FAILED'); await b.close(); process.exit(ok ? 0 : 1);
})();
