const { chromium, devices } = require('playwright');
const fs = require('fs');
const ITEMS = Object.fromEntries(JSON.parse(fs.readFileSync('/home/user/englishfever/app/content/items.json')).map(i => [i.id, i]));
const BASE = 'http://127.0.0.1:8099';
const OUT = __dirname + '/shots/';
const esc = s => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
(async () => {
  const b = await chromium.launch(); let ok = true; const errs = [];
  const check = (n, c, x) => { ok = ok && !!c; console.log((c ? 'PASS ' : 'FAIL ') + n + (c ? '' : ' -> ' + JSON.stringify(x))); };

  async function learner(opts) {
    const ctx = await b.newContext(opts); const p = await ctx.newPage();
    p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
    await p.goto(BASE + '/index.html'); await p.waitForSelector('#nick'); await p.waitForTimeout(1400); await p.click('button[type=submit]'); await p.waitForSelector('.hello h1');
    return { ctx, p };
  }
  const post = (p, r, d) => p.evaluate(async ([r, d]) => (await fetch('api.php?r=' + r, { method: 'POST', headers: { 'X-EF': '1', 'Content-Type': 'application/json' }, body: JSON.stringify(d) })).json(), [r, d]);
  // Practice starts with three plain check tasks, so answer quickly (by API) until the wanted kind shows up.
  async function serve(p, kind, skills, level, pred) {
    for (let round = 0; round < 25; round++) {
      let cur = await post(p, 'session/start', { mode: 'practice', skills, level, length: 30 });
      for (let k = 0; k < 28 && cur.item; k++) {
        if (cur.item.kind === kind && (!pred || pred(cur.item))) { await p.goto(BASE + '/index.html#/session'); await p.reload(); await p.waitForSelector('.task'); return cur.item; }
        const it = ITEMS[cur.item.id];
        // wrong answers keep the difficulty low, so the plain Bloom 1-3 tasks of the level come first
        const ans = it.kind === 'mcq' ? it.wrong[0] : (it.kind === 'gap' ? it.answers.map(() => 'zzz') : (it.kind === 'order' ? it.sentence.split(' ').reverse() : (it.kind === 'match' ? it.pairs.map(x => x[1]).reverse() : 'zzz')));
        const r = await post(p, 'session/answer', { session_id: cur.session.id, item_id: cur.item.id, answer: ans, time_ms: 2000 });
        if (r.done) break;
        cur = { session: r.session, item: r.next };
      }
    }
    return null;
  }
  async function center(loc) { const r = await loc.boundingBox(); return { x: r.x + r.width / 2, y: r.y + r.height / 2 }; }
  async function mouseDrag(p, from, to) {
    const a = await center(from), t = await center(to);
    await p.mouse.move(a.x, a.y); await p.mouse.down(); await p.mouse.move(a.x + 12, a.y + 12, { steps: 3 }); await p.mouse.move(t.x, t.y, { steps: 8 }); await p.mouse.up();
  }

  // ───── word order, desktop ─────
  {
    const { ctx, p } = await learner({ viewport: { width: 1200, height: 900 } });
    const pub = await serve(p, 'order', ['cond_first', 'cond_second', 'rep_questions', 'ind_polite'], 'B1.1');
    check('an order task was served', !!pub);
    const it = ITEMS[pub.id]; const toks = it.sentence.split(' ');
    const shown = await p.locator('.dnd-bank .chip').allInnerTexts();
    check('the cards are the words of the sentence, in a different order', JSON.stringify([...shown].sort()) === JSON.stringify([...toks].sort()) && shown.join(' ') !== toks.join(' '), shown);
    check('Check answer is off until every card is placed', await p.locator('.task .btn:has-text("Check answer")').isDisabled());
    await p.screenshot({ path: OUT + '90-order-start.png', fullPage: true });
    // first card by mouse drag into the line, the rest by tapping
    const first = p.locator('.dnd-bank .chip', { hasText: new RegExp('^' + esc(toks[0]) + '$') }).first();
    await mouseDrag(p, first, p.locator('.dnd-line'));
    check('dragging a card into the line works', (await p.locator('.dnd-line .chip').allInnerTexts()).join(' ') === toks[0], await p.locator('.dnd-line .chip').allInnerTexts());
    // drag it back to the bank
    await mouseDrag(p, p.locator('.dnd-line .chip').first(), p.locator('.dnd-bank'));
    check('dragging it back to the bank works', (await p.locator('.dnd-line .chip').count()) === 0 && (await p.locator('.dnd-bank .chip').count()) === toks.length);
    // keyboard: focus a card and press Enter
    await p.locator('.dnd-bank .chip', { hasText: new RegExp('^' + esc(toks[0]) + '$') }).first().focus(); await p.keyboard.press('Enter');
    check('Enter on a focused card places it', (await p.locator('.dnd-line .chip').count()) === 1);
    for (let i = 1; i < toks.length; i++) await p.locator('.dnd-bank .chip', { hasText: new RegExp('^' + esc(toks[i]) + '$') }).first().click();
    check('Check answer turns on when all cards are placed', !(await p.locator('.task .btn:has-text("Check answer")').isDisabled()));
    await p.click('.task .btn:has-text("Check answer")'); await p.waitForSelector('.feedback');
    check('the right order is marked correct', (await p.locator('.feedback.good').count()) === 1 && (await p.locator('.dnd-line.ok').count()) === 1, await p.locator('.feedback').innerText());
    check('the cards are locked after checking', (await p.locator('.dnd .chip:not([disabled])').count()) === 0);
    await p.screenshot({ path: OUT + '91-order-done.png', fullPage: true });
    // a wrong order
    await p.click('.feedback .btn');
    const pub2 = await serve(p, 'order', ['cond_first', 'cond_second', 'rep_questions', 'ind_polite'], 'B1.1');
    const toks2 = ITEMS[pub2.id].sentence.split(' ');
    for (const t of [...toks2].reverse()) await p.locator('.dnd-bank .chip', { hasText: new RegExp('^' + esc(t) + '$') }).first().click();
    await p.click('.task .btn:has-text("Check answer")'); await p.waitForSelector('.feedback');
    const txt = await p.locator('.feedback').innerText();
    check('a wrong order is marked wrong and shows the correct sentence', (await p.locator('.feedback.bad').count()) === 1 && /Correct answer/.test(txt) && (await p.locator('.dnd-line.bad').count()) === 1, txt.slice(0, 120));
    // "Which sentence is NOT correct?": the answer is the faulty sentence, so it is not called "Correct answer" (Cowork issue 18)
    await p.click('.feedback .btn');
    const NOTQ = ['Which sentence is NOT correct?', 'Which sentence has a mistake?'];
    const pub3 = await serve(p, 'mcq', ['present_simple', 'present_continuous', 'past_simple', 'past_continuous', 'present_perfect', 'future', 'present_simple_passive', 'past_simple_passive', 'cond_zero', 'cond_first'], 'A2.2', it => NOTQ.includes(it.q));
    check('a "NOT correct" question was served', !!pub3);
    if (pub3) {
      await p.locator('.task label, .task .opt').filter({ hasText: ITEMS[pub3.id].wrong[0] }).first().click();
      await p.click('.task .btn:has-text("Check answer")'); await p.waitForSelector('.feedback');
      const txt3 = await p.locator('.feedback').innerText();
      check('a "NOT correct" question names the answer "The wrong sentence", not "Correct answer"', /The wrong sentence: /.test(txt3) && !/Correct answer/.test(txt3), txt3.slice(0, 160));
    }
    await ctx.close();
  }

  // ───── matching, desktop ─────
  {
    const { ctx, p } = await learner({ viewport: { width: 1200, height: 900 } });
    const pub = await serve(p, 'match', ['cond_zero', 'cond_first', 'ind_polite', 'rep_statements'], 'B1.1');
    check('a matching task was served', !!pub);
    const it = ITEMS[pub.id];
    check('every left text has a slot', (await p.locator('.dnd-row').count()) === it.pairs.length);
    await p.screenshot({ path: OUT + '92-match-start.png', fullPage: true });
    // drag the first right-hand card into the first slot, tap the rest
    const c0 = p.locator('.dnd-bank .chip', { hasText: new RegExp('^' + esc(it.pairs[0][1]) + '$') }).first();
    await mouseDrag(p, c0, p.locator('.dnd-row .slot').first());
    check('dragging a card into a slot works', (await p.locator('.dnd-row .slot').first().innerText()) === it.pairs[0][1]);
    // drag another card onto the occupied slot: they swap and the old card goes back to the bank
    const c1 = p.locator('.dnd-bank .chip').first(); const c1txt = await c1.innerText();
    await mouseDrag(p, c1, p.locator('.dnd-row .slot').first());
    check('dropping on a filled slot swaps the cards', (await p.locator('.dnd-row .slot').first().innerText()) === c1txt && (await p.locator('.dnd-bank .chip', { hasText: new RegExp('^' + esc(it.pairs[0][1]) + '$') }).count()) === 1);
    // put everything right: clear slot 0 and tap in order
    await p.locator('.dnd-row .slot .chip').first().click();
    for (const pr of it.pairs) await p.locator('.dnd-bank .chip', { hasText: new RegExp('^' + esc(pr[1]) + '$') }).first().click();
    await p.click('.task .btn:has-text("Check answer")'); await p.waitForSelector('.feedback');
    check('correct pairs are marked correct', (await p.locator('.feedback.good').count()) === 1 && (await p.locator('.slot.ok').count()) === it.pairs.length);
    await p.click('.feedback .btn');
    // wrong: rotate the answers
    const pub2 = await serve(p, 'match', ['cond_zero', 'cond_first', 'ind_polite', 'rep_statements'], 'B1.1');
    const it2 = ITEMS[pub2.id]; const rot = [...it2.pairs.slice(1), it2.pairs[0]];
    for (const pr of rot) await p.locator('.dnd-bank .chip', { hasText: new RegExp('^' + esc(pr[1]) + '$') }).first().click();
    await p.click('.task .btn:has-text("Check answer")'); await p.waitForSelector('.feedback');
    check('wrong pairs are marked and the right pairs are shown', (await p.locator('.slot.bad').count()) >= 2 && (await p.locator('.feedback .pairs li').count()) === it2.pairs.length);
    await p.screenshot({ path: OUT + '93-match-wrong.png', fullPage: true });
    await ctx.close();
  }

  // ───── word bank gap, phone with touch ─────
  {
    const { ctx, p } = await learner({ ...devices['iPhone 13'] });
    const pub = await serve(p, 'gap', ['cond_first', 'cond_second'], 'B1.1', i => i.bank);
    check('a word-bank gap was served', !!pub);
    const it = ITEMS[pub.id];
    check('the sentence has gaps and a bank with decoys', (await p.locator('.dnd-sentence .slot').count()) === it.answers.length && (await p.locator('.dnd-bank .chip').count()) > it.answers.length);
    // touch drag with the DevTools protocol: first answer by dragging, the others by tapping
    await p.evaluate(() => document.querySelector('.dnd-bank').scrollIntoView({ block: 'center' })); await p.waitForTimeout(200);   // a tall task can leave the bank under the bottom menu bar; a learner would scroll first
    const cdp = await ctx.newCDPSession(p);
    const chip = p.locator('.dnd-bank .chip', { hasText: new RegExp('^' + esc(it.answers[0][0]) + '$') }).first();
    const a = await center(chip), t = await center(p.locator('.dnd-sentence .slot').first());
    await cdp.send('Input.dispatchTouchEvent', { type: 'touchStart', touchPoints: [{ x: a.x, y: a.y }] });
    for (let k = 1; k <= 8; k++) await cdp.send('Input.dispatchTouchEvent', { type: 'touchMove', touchPoints: [{ x: a.x + (t.x - a.x) * k / 8, y: a.y + (t.y - a.y) * k / 8 }] });
    await cdp.send('Input.dispatchTouchEvent', { type: 'touchEnd', touchPoints: [] });
    check('a touch drag drops a word into the gap', (await p.locator('.dnd-sentence .slot').first().innerText()) === it.answers[0][0], await p.locator('.dnd-sentence .slot').first().innerText());
    for (let i = 1; i < it.answers.length; i++) await p.locator('.dnd-bank .chip', { hasText: new RegExp('^' + esc(it.answers[i][0]) + '$') }).first().tap();
    const over = await p.evaluate(() => document.documentElement.scrollWidth > window.innerWidth + 1);
    check('phone: no sideways scrolling', !over);
    await p.screenshot({ path: OUT + '94-bank-phone.png', fullPage: true });
    await p.tap('.task .btn:has-text("Check answer")'); await p.waitForSelector('.feedback');
    check('the right words are marked correct', (await p.locator('.feedback.good').count()) === 1 && (await p.locator('.slot.ok').count()) === it.answers.length);
    await ctx.close();
  }

  check('no page errors', errs.length === 0, errs);
  console.log(ok ? '\nALL PASS' : '\nSOME FAILED'); await b.close(); process.exit(ok ? 0 : 1);
})();
