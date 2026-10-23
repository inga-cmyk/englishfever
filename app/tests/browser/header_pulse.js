const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' }); let ok = true;
  const check = (n, c) => { ok = ok && !!c; console.log((c ? 'PASS ' : 'FAIL ') + n); };
  async function learner(name, answer, w = 700) {
    const ctx = await b.newContext({ viewport: { width: w, height: 900 }, deviceScaleFactor: 2 }); const p = await ctx.newPage(); await p.goto('http://127.0.0.1:8099/'); await p.waitForTimeout(500);
    await p.evaluate(async (name) => { await fetch('api.php?r=guest', { method: 'POST', headers: { 'X-EF': '1', 'Content-Type': 'application/json' }, body: JSON.stringify({ t: 5000, nickname: name }) }); }, name);
    if (answer) await p.evaluate(async () => { const post = async (r, d) => (await fetch('api.php?r=' + r, { method: 'POST', headers: { 'X-EF': '1', 'Content-Type': 'application/json' }, body: JSON.stringify(d) })).json();
      const s = await post('session/start', { mode: 'practice', skills: ['present_simple'], level: 'A2.1', length: 5 }); await post('session/answer', { session_id: s.session.id, item_id: s.item.id, answer: 'x', time_ms: 1000 }); });
    return p;
  }
  const clear = () => require('child_process').execSync("python3 -c \"import sqlite3; c=sqlite3.connect('/home/user/englishfever/app/var/ef.sqlite'); c.execute(\\\"DELETE FROM kv WHERE k='pulse'\\\"); c.commit()\"");
  const fresh = await learner('Nina', false); await fresh.reload(); await fresh.waitForTimeout(900);
  check('new guest: no "Practising as a guest"', (await fresh.locator('text=Practising as a guest').count()) === 0);
  check('new guest: the card still offers an account', (await fresh.locator('text=Create a free account to keep your results').count()) === 1);
  check('new guest: no "Short grammar questions that adapt to you" under the greeting', (await fresh.locator('.hello >> text=Short grammar questions').count()) === 0);
  check('no company chip while nobody is practising', (await fresh.locator('.chip-pulse').count()) === 0);
  for (const n of ['Anna', 'Bruno', 'Cilda']) await learner(n, true);
  clear(); await fresh.reload(); await fresh.waitForTimeout(900);
  check('3 are online: the header shows a green dot and 3', (await fresh.locator('.chip-pulse .pulse-dot').count()) === 1 && (await fresh.locator('.chip-pulse').innerText()).trim() === '3');
  check('it is next to the day count', await fresh.evaluate(() => { const c = [...document.querySelectorAll('#chips .chip-top')].map(x => x.className + '|' + x.textContent); return c.findIndex(x => /chip-pulse/.test(x)) - c.findIndex(x => /day/.test(x)) === 1; }));
  check('nothing about it on the Home page itself', (await fresh.locator('.homestat .pulse-pill').count()) === 0 && (await fresh.locator('main >> text=showed up today').count()) === 0);
  await fresh.screenshot({ path: 'header_pulse.png', clip: { x: 0, y: 0, width: 700, height: 420 } });
  // the "today" version: nobody answered in the last 10 minutes, but 3 or more did today
  require('child_process').execSync("python3 -c \"import sqlite3; c=sqlite3.connect('/home/user/englishfever/app/var/ef.sqlite'); c.execute('UPDATE attempts SET created_at = created_at - 3600'); c.execute(\\\"DELETE FROM kv WHERE k='pulse'\\\"); c.commit()\"");
  await fresh.reload(); await fresh.waitForTimeout(900);
  check('3 earlier today: the header shows the people icon and 3', (await fresh.locator('.chip-pulse svg').count()) === 1 && (await fresh.locator('.chip-pulse .pulse-dot').count()) === 0);
  const ph = await learner('Phone', false, 390); await ph.reload(); await ph.waitForTimeout(900);
  check('phone: no sideways scrolling with the chip', !(await ph.evaluate(() => document.documentElement.scrollWidth > document.documentElement.clientWidth)));
  await ph.screenshot({ path: 'header_pulse_phone.png', clip: { x: 0, y: 0, width: 390, height: 140 } });
  console.log(ok ? '\nALL PASS' : '\nSOME FAILED'); await b.close(); process.exit(ok ? 0 : 1);
})();
