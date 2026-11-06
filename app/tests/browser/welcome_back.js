// Welcome back (teacher, 6 November): the right message for each situation, plain English for A2, one button that only closes it.
const { chromium } = require('playwright');
const BASE = 'http://127.0.0.1:8099', OUT = __dirname + '/shots/';
(async () => {
  const b = await chromium.launch(); let ok = true, n = 0; const errs = [];
  const check = (name, c, x) => { n++; if (!c) { ok = false; console.log('FAIL ' + name + (x !== undefined ? ' -> ' + JSON.stringify(x) : '')); } };
  async function open(visit, today, level, shot, scheme) {
    const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: shot ? 2 : 1, colorScheme: scheme || 'light' }); const p = await ctx.newPage();
    p.on('pageerror', e => errs.push(e.message));
    await p.goto(BASE + '/index.html'); await p.waitForSelector('#nick'); await p.fill('#nick', 'Welcome Tester'); await p.click('button[type=submit]'); await p.waitForSelector('.hello h1');
    await p.route(/api\.php\?r=dash/, async r => { const res = await r.fetch(); const j = await res.json();
      j.totals.answers = 40; j.today.answers = today; j.visit = visit; j.level_now = { level: level, from: 'answers', n: 40 }; r.fulfill({ response: res, json: j }); });
    await p.evaluate(() => sessionStorage.removeItem('ef_welcomed')); await p.goto(BASE + '/index.html#/home'); await p.reload(); await p.waitForSelector('.hello h1'); await p.waitForTimeout(500);
    const box = p.locator('.welcome-back');
    const txt = (await box.count()) ? await box.innerText() : null;
    if (shot) await p.screenshot({ path: OUT + shot });
    if (txt) { await p.locator('.welcome-back .btn').click(); await p.waitForTimeout(200); }
    const closed = (await p.locator('.welcome-back').count()) === 0;
    await ctx.close(); return { txt, closed };
  }
  const week = { week_days: 3, week_seconds: 2520 };
  let r = await open({ gap: 3, yesterday: { seconds: 0, answers: 0 }, ...week }, 0, 'B2.1', 'wb-gap3-b2.png');
  check('3 days away, B2: a message about the days, with this week', r.txt && /3 days|articles/.test(r.txt) && /This week: 3 days · 42 min/.test(r.txt), r.txt);
  check('the button closes it and Home stays', r.closed);
  r = await open({ gap: 3, yesterday: { seconds: 0, answers: 0 }, ...week }, 0, 'A2.2', 'wb-gap3-a2.png', 'dark');
  check('the same for A2: plain English', r.txt && /Welcome back! 3 days is a long time\. We missed you\./.test(r.txt), r.txt);
  r = await open({ gap: 1, yesterday: { seconds: 1500, answers: 30 }, ...week }, 0, 'B1.1', 'wb-long.png');
  check('a long session yesterday: the minutes', r.txt && /25 minutes/.test(r.txt), r.txt);
  r = await open({ gap: 14, yesterday: { seconds: 0, answers: 0 }, week_days: 0, week_seconds: 0 }, 0, 'B1.2');
  check('two weeks away: no week line when there was nothing this week', r.txt && !/This week/.test(r.txt), r.txt);
  r = await open({ gap: null, yesterday: { seconds: 0, answers: 0 }, ...week }, 5, 'B1.1');
  check('first visit of the day after practising today already: no message', r.txt === null, r.txt);
  console.log(errs.length ? 'ERR ' + errs.join(' | ') : (ok ? 'ALL PASS: ' + n + ' welcome-back checks' : 'SOME FAILED'));
  await b.close(); process.exit(ok && !errs.length ? 0 : 1);
})();
