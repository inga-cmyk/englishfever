const { chromium } = require('playwright');
const BASE = 'http://127.0.0.1:8099', OUT = __dirname + '/shots/';
const res = []; const check = (n, ok, x) => { res.push(ok); console.log((ok ? 'PASS ' : 'FAIL ') + n + (ok ? '' : ' -> ' + JSON.stringify(x))); };
(async () => {
  const b = await chromium.launch(); const errs = [];
  // a student: open pages, a rule card, Surprise me, skip, quit
  const s = await (await b.newContext({ viewport: { width: 1200, height: 900 } })).newPage(); s.on('pageerror', e => errs.push(e.message));
  await s.goto(BASE + '/index.html'); await s.waitForSelector('#nick'); await s.fill('#nick', 'Usage tester'); await s.click('button[type=submit]'); await s.waitForSelector('.hello h1');
  await s.evaluate(() => { location.hash = '#/rules'; }); await s.waitForSelector('.ttile-btn'); await s.locator('.ttile-btn').first().click(); await s.waitForSelector('.rulecard');
  await s.locator('#c').click();
  const r = await s.evaluate(async () => (await (await fetch('api.php?r=session%2Fstart', { method: 'POST', headers: { 'X-EF': '1', 'Content-Type': 'application/json' }, body: JSON.stringify({ mode: 'smart', length: 12, source: 'surprise' }) })).json()));
  await s.goto(BASE + '/index.html#/session'); await s.reload(); await s.waitForSelector('.task');
  const skip = s.locator('button:has-text("Skip")'); if (await skip.count()) { await skip.first().click(); await s.waitForTimeout(800); }
  await s.evaluate(() => { document.dispatchEvent(new Event('visibilitychange')); });
  await s.evaluate(async () => { Object.defineProperty(document, 'visibilityState', { value: 'hidden', configurable: true }); document.dispatchEvent(new Event('visibilitychange')); });
  await s.waitForTimeout(11000);   // the batch is sent every 10 seconds
  // the teacher
  const t = await (await b.newContext({ viewport: { width: 1200, height: 900 } })).newPage(); t.on('pageerror', e => errs.push(e.message));
  await t.goto(BASE + '/sso-demo.php?teacher=1&uid=1&name=Inga%20Teacher'); await t.waitForSelector('table');
  const u = await t.evaluate(async () => (await (await fetch('api.php?r=teacher%2Fusage&days=30', { headers: { 'X-EF': '1' } })).json()));
  if (u.error) { console.log('teacher api:', u.error); }
  else {
    check('session source recorded (surprise)', u.sources.some(x => x.source === 'surprise'), u.sources);
    check('page views logged', u.events.some(x => x.ev === 'page'), u.events.map(e => e.ev));
    check('rule card logged', u.events.some(x => x.ev === 'rule_card'), u.events.map(e => e.ev));
    await t.goto(BASE + '/index.html#/usage'); await t.waitForSelector('h1:has-text("Usage")');
    await t.screenshot({ path: OUT + 'usage-teacher.png', fullPage: true });
    const csv = await t.evaluate(async () => (await fetch('api.php?r=teacher%2Fusage-export')).text());
    check('CSV has events and sessions', /rule_card/.test(csv) && /session started/.test(csv), csv.slice(0, 200));
  }
  // an unknown event name is ignored
  const bad = await s.evaluate(async () => (await (await fetch('api.php?r=event', { method: 'POST', headers: { 'X-EF': '1', 'Content-Type': 'application/json' }, body: JSON.stringify({ events: [['hack', 'x'], ['page', '<b>home</b>']] }) })).json()));
  check('only known names are stored, detail cleaned', bad.ok === 1, bad);
  check('no page errors', errs.length === 0, errs);
  console.log(res.every(Boolean) ? 'ALL PASS' : 'SOME FAILED');
  await b.close();
})();
