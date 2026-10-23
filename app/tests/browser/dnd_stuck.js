const { chromium } = require('playwright');
const fs = require('fs');
const ITEMS = Object.fromEntries(JSON.parse(fs.readFileSync('/home/user/englishfever/app/content/items.json')).map(i => [i.id, i]));
const BASE = 'http://127.0.0.1:8099';
(async () => {
  const b = await chromium.launch(); let ok = true; const errs = [];
  const check = (n, c, x) => { ok = ok && !!c; console.log((c ? 'PASS ' : 'FAIL ') + n + (c ? '' : ' -> ' + JSON.stringify(x))); };
  const ctx = await b.newContext({ viewport: { width: 1200, height: 900 } }); const p = await ctx.newPage();
  p.on('pageerror', e => errs.push(e.message));
  await p.goto(BASE + '/index.html'); await p.waitForSelector('#nick'); await p.waitForTimeout(1400); await p.click('button[type=submit]'); await p.waitForSelector('.hello h1');
  const post = (r, d) => p.evaluate(async ([r, d]) => (await fetch('api.php?r=' + r, { method: 'POST', headers: { 'X-EF': '1', 'Content-Type': 'application/json' }, body: JSON.stringify(d) })).json(), [r, d]);
  async function serveOrder() {
    for (let round = 0; round < 25; round++) {
      let cur = await post('session/start', { mode: 'practice', skills: ['cond_first', 'cond_second', 'rep_questions', 'ind_polite'], level: 'B1.1', length: 30 });
      for (let k = 0; k < 28 && cur.item; k++) {
        if (cur.item.kind === 'order') { await p.goto(BASE + '/index.html#/session'); await p.reload(); await p.waitForSelector('.dnd-bank .chip'); return; }
        const it = ITEMS[cur.item.id];
        const ans = it.kind === 'mcq' ? it.wrong[0] : (it.kind === 'gap' ? it.answers.map(() => 'zzz') : (it.kind === 'match' ? it.pairs.map(x => x[1]).reverse() : 'zzz'));
        const r = await post('session/answer', { session_id: cur.session.id, item_id: cur.item.id, answer: ans, time_ms: 2000 });
        if (r.done) break; cur = { session: r.session, item: r.next };
      }
    }
    throw new Error('no order task served');
  }
  const ghosts = () => p.locator('.chip.ghost').count();
  const flag = () => p.evaluate(() => document.documentElement.classList.contains('dnd-dragging'));
  const bankCount = () => p.locator('.dnd-bank .chip').count();
  async function startDrag() {
    const c = p.locator('.dnd-bank .chip').first(); const r = await c.boundingBox();
    const x = r.x + r.width / 2, y = r.y + r.height / 2;
    await p.mouse.move(x, y); await p.mouse.down(); await p.mouse.move(x + 30, y + 40, { steps: 4 }); await p.mouse.move(x + 200, y + 90, { steps: 5 });
    return { x: x + 200, y: y + 90 };
  }
  const settle = async () => { await p.mouse.up().catch(() => {}); await p.waitForTimeout(100); };

  await serveOrder();
  const n0 = await bankCount();
  // 1. a drag is visible while it lasts and gone after
  let pos = await startDrag();
  check('while dragging: one floating copy and the page is marked', (await ghosts()) === 1 && await flag(), [await ghosts(), await flag()]);
  await p.mouse.up(); await p.waitForTimeout(100);
  check('after a normal drop: no floating copy, mark removed', (await ghosts()) === 0 && !(await flag()));

  // 2. the card is replaced while it is being dragged (a re-render): the release must still end the drag
  pos = await startDrag();
  await p.evaluate(() => document.querySelectorAll('.dnd-bank .chip').forEach(x => x.remove()));
  await p.mouse.move(pos.x + 20, pos.y + 10, { steps: 3 }); await p.mouse.up(); await p.waitForTimeout(100);
  check('card removed mid-drag, then released: no floating copy', (await ghosts()) === 0 && !(await flag()), await ghosts());
  await p.reload(); await p.waitForSelector('.dnd-bank .chip');

  // 3. the release happens where we cannot see it (outside the window): the next move without a pressed button ends it
  pos = await startDrag();
  await p.evaluate(([x, y]) => window.dispatchEvent(new PointerEvent('pointermove', { pointerId: 1, pointerType: 'mouse', buttons: 0, clientX: x, clientY: y, bubbles: true })), [pos.x, pos.y]);
  check('move with no button pressed: the drag ends, no floating copy', (await ghosts()) === 0 && !(await flag()), await ghosts());
  await settle();
  check('...and nothing was dropped', (await bankCount()) === n0, await bankCount());

  // 4. Escape cancels
  pos = await startDrag(); await p.keyboard.press('Escape');
  check('Escape cancels: no floating copy, card still in the bank', (await ghosts()) === 0 && (await bankCount()) === n0, [await ghosts(), await bankCount()]);
  await settle();

  // 5. the browser cancels the pointer
  pos = await startDrag();
  await p.evaluate(() => window.dispatchEvent(new PointerEvent('pointercancel', { pointerId: 1, pointerType: 'mouse', bubbles: true })));
  check('pointercancel: no floating copy', (await ghosts()) === 0, await ghosts()); await settle();

  // 6. the window loses focus (Cmd-Tab, an alert, the system menu)
  pos = await startDrag(); await p.evaluate(() => window.dispatchEvent(new Event('blur')));
  check('window blur: no floating copy', (await ghosts()) === 0, await ghosts()); await settle();

  // 7. a left-over copy from earlier is removed by the next press on any card
  await p.evaluate(() => { const g = document.createElement('div'); g.className = 'chip ghost'; g.textContent = 'old'; document.body.appendChild(g); });
  check('a stale copy exists', (await ghosts()) === 1);
  const c = p.locator('.dnd-bank .chip').first(); const r = await c.boundingBox();
  await p.mouse.move(r.x + 5, r.y + 5); await p.mouse.down(); await p.mouse.up(); await p.waitForTimeout(100);
  check('pressing a card removes the stale copy', (await ghosts()) === 0, await ghosts());
  // that press was a tap: it placed the card; put it back
  await p.locator('.dnd-line .chip').first().click(); await p.waitForTimeout(50);

  // 8. leaving the task while dragging (new task / another page) clears it
  pos = await startDrag(); await p.evaluate(() => { location.hash = '#/home'; });
  await p.waitForSelector('.hello h1'); await p.waitForTimeout(150);
  check('leaving the task: no floating copy', (await ghosts()) === 0 && !(await flag()), await ghosts()); await settle();

  // 9. a stale copy does not cover the next task
  await p.evaluate(() => { const g = document.createElement('div'); g.className = 'chip ghost'; g.textContent = 'old'; document.body.appendChild(g); });
  await p.evaluate(() => { location.hash = '#/practice'; }); await p.waitForTimeout(400);
  check('showing another page clears a stale copy', (await ghosts()) === 0, await ghosts());

  check('no page errors', errs.length === 0, errs);
  console.log(ok ? '\nALL PASS' : '\nSOME FAILED'); await b.close(); process.exit(ok ? 0 : 1);
})();
