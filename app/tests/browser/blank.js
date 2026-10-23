const { chromium, devices } = require('playwright');
const BASE = 'http://127.0.0.1:8099';
(async () => {
  const b = await chromium.launch(); let ok = true; const check = (n, c, x) => { ok = ok && !!c; console.log((c ? 'PASS ' : 'FAIL ') + n + (c ? '' : ' -> ' + JSON.stringify(x))); };
  for (const [label, opts] of [['desktop', { viewport: { width: 1280, height: 800 } }], ['phone', { ...devices['iPhone 13'] }]]) {
    const ctx = await b.newContext(opts); const p = await ctx.newPage();
    await p.goto(BASE + '/index.html'); await p.waitForSelector('#nick'); await p.waitForTimeout(1400); await p.click('button[type=submit]'); await p.waitForSelector('.hello h1');
    const post = (r, d) => p.evaluate(async ([r, d]) => (await fetch('api.php?r=' + r, { method: 'POST', headers: { 'X-EF': '1', 'Content-Type': 'application/json' }, body: JSON.stringify(d) })).json(), [r, d]);
    let found = false;
    for (let round = 0; round < 8 && !found; round++) {
      const s = await post('session/start', { mode: 'practice', skills: ['present_continuous_passive', 'present_perfect_continuous', 'past_perfect_continuous'], level: 'B1.2', length: 20 });
      for (let k = 0; k < 20 && !found; k++) {
        await p.goto(BASE + '/index.html#/session'); await p.reload(); await p.waitForSelector('.task');
        if (await p.locator('input.blank').count()) { found = true; break; }
        const cur = await post('session/resume', {}).catch(() => null);
        const r = await p.evaluate(async () => (await (await fetch('api.php?r=session/resume', { headers: { 'X-EF': '1' } })).json()));
        if (!r.resume) break;
        await post('session/answer', { session_id: r.resume.session.id, item_id: r.resume.item.id, answer: r.resume.item.kind === 'gap' ? ['x'] : 'x', time_ms: 2000 });
      }
    }
    check(label + ': found a gap task', found);
    if (!found) continue;
    const box = p.locator('input.blank').first();
    const w0 = (await box.boundingBox()).width;
    await box.fill('has been being repaired');
    const w1 = (await box.boundingBox()).width;
    const fits = await box.evaluate(e => e.scrollWidth <= e.clientWidth + 1);
    check(label + ': the box grows for a long answer (' + Math.round(w0) + ' -> ' + Math.round(w1) + ' px)', w1 > w0 && fits, { w0, w1, fits });
    await box.fill('is');
    const w2 = (await box.boundingBox()).width;
    check(label + ': and shrinks back to its normal size', Math.abs(w2 - w0) < 2, { w0, w2 });
    await box.fill('would have been being completed by the end of the week by them');
    const cardBox = await p.locator('.task').boundingBox(); const bb = await box.boundingBox();
    check(label + ': a very long answer stays inside the card', bb.x + bb.width <= cardBox.x + cardBox.width + 1, { bb, cardBox });
    await p.screenshot({ path: __dirname + '/shots/80-blank-' + label + '.png' });
    await ctx.close();
  }
  console.log(ok ? '\nALL PASS' : '\nSOME FAILED'); await b.close(); process.exit(ok ? 0 : 1);
})();
