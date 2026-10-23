const { chromium } = require('playwright');
const fs = require('fs');
const ITEMS = Object.fromEntries(JSON.parse(fs.readFileSync('/home/user/englishfever/app/content/items.json')).map(i => [i.id, i]));
const BASE = 'http://127.0.0.1:8099';
const esc = s => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
(async () => {
  const b = await chromium.launch(); let ok = true; const errs = [];
  const check = (n, c, x) => { ok = ok && !!c; console.log((c ? 'PASS ' : 'FAIL ') + n + (c ? '' : ' -> ' + JSON.stringify(x))); };
  const ctx = await b.newContext({ viewport: { width: 1200, height: 900 } }); const p = await ctx.newPage();
  p.on('pageerror', e => errs.push(e.message));
  await p.goto(BASE + '/index.html'); await p.waitForSelector('#nick'); await p.waitForTimeout(1400); await p.click('button[type=submit]'); await p.waitForSelector('.hello h1');
  const post = (r, d) => p.evaluate(async ([r, d]) => (await fetch('api.php?r=' + r, { method: 'POST', headers: { 'X-EF': '1', 'Content-Type': 'application/json' }, body: JSON.stringify(d) })).json(), [r, d]);
  // get to a session whose NEXT tasks include order / match / bank gap: answer plain tasks by API (wrong, to keep it easy) until the wanted kind is current
  async function until(pred, skills) {
    for (let round = 0; round < 80; round++) {
      let cur = await post('session/start', { mode: 'practice', skills: skills || ['cond_first', 'cond_second', 'rep_questions', 'ind_polite', 'ind_advanced', 'cond_third'], level: 'B1.1', length: 30 });
      for (let k = 0; k < 28 && cur.item; k++) {
        if (pred(cur.item)) return cur;
        const it = ITEMS[cur.item.id];
        const ans = it.kind === 'mcq' ? it.wrong[0] : (it.kind === 'gap' ? it.answers.map(() => 'zzz') : (it.kind === 'order' ? it.sentence.split(' ').reverse() : (it.kind === 'match' ? it.pairs.map(x => x[1]).reverse() : 'zzz')));
        const r = await post('session/answer', { session_id: cur.session.id, item_id: cur.item.id, answer: ans, time_ms: 2000 });
        if (r.done) break; cur = { session: r.session, item: r.next };
      }
    }
    throw new Error('wanted task not served');
  }
  async function open() { await p.goto(BASE + '/index.html#/session'); await p.reload(); await p.waitForSelector('.task .q'); }

  // ── order
  let cur = await until(i => i.kind === 'order'); let id = cur.item.id; const toks = ITEMS[id].sentence.split(' ');
  await open();
  for (const t of toks) await p.locator('.dnd-bank .chip', { hasText: new RegExp('^' + esc(t) + '$') }).first().click();
  await p.click('.task .btn:has-text("Check answer")'); await p.waitForSelector('.feedback');
  await p.click('.feedback .btn:has-text("Next")'); await p.waitForSelector('.task .q');
  await p.click('.sess-top .linkbtn:has-text("Previous")'); await p.waitForSelector('.feedback');
  check('order: the saved order is back in the line', (await p.locator('.dnd-line .chip').allInnerTexts()).join(' ') === toks.join(' '), await p.locator('.dnd-line .chip').allInnerTexts());
  check('order: bank is empty, cards are locked, line is marked', (await p.locator('.dnd-bank .chip').count()) === 0 && (await p.locator('.dnd-line .chip:not([disabled])').count()) === 0 && (await p.locator('.dnd-line.ok').count()) === 1);
  await p.click('.feedback .btn:has-text("Back to question")'); await p.waitForSelector('.task .q');

  // ── match
  cur = await until(i => i.kind === 'match'); id = cur.item.id; const m = ITEMS[id];
  await p.goto(BASE + '/index.html#/session'); await p.reload(); await p.waitForSelector('.task .q');
  // fill the slots in order, right-hand cards by tapping (each tap takes the first free slot)
  for (const pair of m.pairs) await p.locator('.dnd-bank .chip', { hasText: new RegExp('^' + esc(pair[1]) + '$') }).first().click();
  const before = await p.locator('.slot .chip').allInnerTexts();
  await p.click('.task .btn:has-text("Check answer")'); await p.waitForSelector('.feedback');
  await p.click('.feedback .btn:has-text("Next")'); await p.waitForSelector('.task .q');
  await p.click('.sess-top .linkbtn:has-text("Previous")'); await p.waitForSelector('.feedback');
  const after = await p.locator('.slot .chip').allInnerTexts();
  check('match: the saved pairs are back in their slots', before.join('|') === after.join('|') && after.length === m.pairs.length, [before, after]);
  check('match: slots are marked', (await p.locator('.slot.ok, .slot.bad').count()) === m.pairs.length);

  // ── word bank gap
  cur = await until(i => i.kind === 'gap' && i.bank, ['cond_first', 'cond_second']); id = cur.item.id; const g = ITEMS[id];
  await p.goto(BASE + '/index.html#/session'); await p.reload(); await p.waitForSelector('.task .q');
  for (const a of g.answers) await p.locator('.dnd-bank .chip', { hasText: new RegExp('^' + esc(a[0]) + '$') }).first().click();
  const b1 = await p.locator('.slot .chip').allInnerTexts();
  await p.click('.task .btn:has-text("Check answer")'); await p.waitForSelector('.feedback');
  await p.click('.feedback .btn:has-text("Next")'); await p.waitForSelector('.task .q');
  await p.click('.sess-top .linkbtn:has-text("Previous")'); await p.waitForSelector('.feedback');
  check('word bank: the words are back in the gaps', (await p.locator('.slot .chip').allInnerTexts()).join('|') === b1.join('|') && b1.length === g.answers.length, [b1, await p.locator('.slot .chip').allInnerTexts()]);

  check('no page errors', errs.length === 0, errs);
  console.log(ok ? '\nALL PASS' : '\nSOME FAILED'); await b.close(); process.exit(ok ? 0 : 1);
})();
