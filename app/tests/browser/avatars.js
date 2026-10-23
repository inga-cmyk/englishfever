const { chromium, devices } = require('playwright');
const crypto = require('crypto'); const BASE = 'http://127.0.0.1:8099';
const SECRET = 'local-dev-secret-local-dev-secret-local-dev-secret-0000';
const tok = (uid, name, teacher) => { const x = Buffer.from(JSON.stringify({ uid, name, teacher: !!teacher, exp: Math.floor(Date.now() / 1000) + 100, n: crypto.randomBytes(6).toString('hex') })).toString('base64url'); return x + '.' + crypto.createHmac('sha256', SECRET).update(x).digest('base64url'); };
(async () => {
  const b = await chromium.launch(); let ok = true; const check = (n, c, x) => { ok = ok && !!c; console.log((c ? 'PASS ' : 'FAIL ') + n + (c ? '' : ' -> ' + JSON.stringify(x))); };
  const errs = [];
  async function learner(uid, name, avatar, extra) {
    const ctx = await b.newContext(); const p = await ctx.newPage(); p.on('pageerror', e => errs.push(e.message));
    await p.goto(BASE + '/sso.php?token=' + tok(uid, name)); await p.waitForSelector('#fn'); await p.click('button[type=submit]'); await p.waitForSelector('.hello h1');
    await p.evaluate(async (av) => { const post = (r, d) => fetch('api.php?r=' + r, { method: 'POST', headers: { 'X-EF': '1', 'Content-Type': 'application/json' }, body: JSON.stringify(d) }).then(r => r.json());
      if (av) await post('account/profile', { avatar: av });
      const s = await post('session/start', { mode: 'practice', skills: ['present_simple'], level: 'A2.1', length: 5 }); await post('session/answer', { session_id: s.session.id, item_id: s.item.id, answer: 'x', time_ms: 2000 }); }, avatar);
    return p;
  }
  const names = [['Maya', 'flame-raspberry'], ['Jānis', 'comet-plum'], ['Olga', 'sun-gold'], ['Tom', null], ['Ieva', 'leaf-ink'], ['Sam', 'wave-sand'], ['Nina', 'thermo-cream'], ['Alex', 'spark-gold']];
  let main;
  for (let i = 0; i < names.length; i++) { const p = await learner(6100 + i + Math.floor(Math.random() * 1000), names[i][0], names[i][1]); if (i === 0) main = p; else await p.context().close(); }
  // profile picker: collapsed at first, characters and symbols inside
  await main.goto(BASE + '/index.html#/profile'); await main.waitForSelector('.avpanel', { state: 'attached' });
  check('the avatar menu is collapsed at first', !(await main.locator('.avpanel').isVisible()) && (await main.locator('button:has-text("Change")').getAttribute('aria-expanded')) === 'false');
  await main.screenshot({ path: __dirname + '/shots/69-profile-collapsed.png', fullPage: true });
  await main.click('button:has-text("Change")');
  check('Change opens it', await main.locator('.avpanel').isVisible() && (await main.locator('button:has-text("Close")').getAttribute('aria-expanded')) === 'true');
  check('it offers Halloween, people, characters and symbols', (await main.locator('.avpanel .avopt').count()) === 8 + 10 + 9 + 8 + 1);
  await main.click('.avopt[aria-label="Captain"]'); await main.click('.avcolor[aria-label="Plum"]');
  await main.screenshot({ path: __dirname + '/shots/70-profile-avatar.png', fullPage: true });
  await main.click('.avpanel button:has-text("Save")'); await main.waitForSelector('.toast');
  check('saving collapses the menu', !(await main.locator('.avpanel').isVisible()));
  check('the header and top bar show the new avatar at once', /Captain, plum/g.test(await main.locator('.avatar-link svg').getAttribute('aria-label')) && /Captain, plum/g.test(await main.locator('.card:has(.avpanel) svg.avatar').first().getAttribute('aria-label')));
  await main.reload(); await main.waitForSelector('.avatar-link');
  check('the avatar is still there after a reload (saved on the server)', /Captain, plum/g.test(await main.locator('.avatar-link svg').getAttribute('aria-label')));
  await main.goto(BASE + '/index.html#/home'); await main.waitForSelector('.hello h1'); await main.waitForTimeout(300);
  check('the home greeting shows it', /Captain, plum/g.test(await main.locator('.hello svg.avatar').first().getAttribute('aria-label')));
  await main.screenshot({ path: __dirname + '/shots/71-home-avatar.png' });
  await main.goto(BASE + '/index.html#/leaderboard'); await main.waitForSelector('.lb-row'); await main.waitForTimeout(300);
  check('leaderboard rows show avatars', (await main.locator('.lb-row svg.avatar').count()) >= 6);
  const tomLabel = await main.locator('.lb-row:has-text("Tom") svg.avatar').getAttribute('aria-label');
  check('a learner who chose nothing gets an assigned symbol, not a blank', /Avatar: (Flame|Spark|Bolt|Sun|Thermometer|Wave|Comet|Leaf), /.test(tomLabel), tomLabel);
  await main.screenshot({ path: __dirname + '/shots/72-leaderboard-avatars.png', fullPage: true });
  // the initial is a normal choice now
  await main.goto(BASE + '/index.html#/profile'); await main.waitForSelector('.avpanel', { state: 'attached' }); await main.click('button:has-text("Change")');
  await main.click('.avopt[aria-label="My initial"]'); await main.click('.avpanel button:has-text("Save")'); await main.waitForSelector('.toast');
  check('"My initial" can be chosen', /Avatar: M/.test(await main.locator('.avatar-link svg').getAttribute('aria-label')), await main.locator('.avatar-link svg').getAttribute('aria-label'));
  // teacher view
  const tctx = await b.newContext(); const t = await tctx.newPage(); t.on('pageerror', e => errs.push(e.message));
  await t.goto(BASE + '/sso.php?token=' + tok(1, 'Inga Teacher', true)); await t.waitForSelector('table'); await t.waitForTimeout(300);
  check('teacher list shows avatars', (await t.locator('td.name svg.avatar').count()) >= 6);
  await t.screenshot({ path: __dirname + '/shots/73-teacher-avatars.png' });
  // phone: tab bar uses the avatar
  const m = await b.newContext({ ...devices['iPhone 13'] }); const mp = await m.newPage(); await mp.goto(BASE + '/sso.php?token=' + tok(7777 + Math.floor(Math.random() * 100), 'Phone Pat')); await mp.waitForSelector('#fn'); await mp.click('button[type=submit]'); await mp.waitForSelector('.hello h1');
  check('phone: the Profile tab shows the avatar', (await mp.locator('.tabbar a svg.avatar').count()) === 1);
  const over = await mp.evaluate(() => document.documentElement.scrollWidth > window.innerWidth + 1); check('phone: no sideways scrolling', !over);
  await mp.screenshot({ path: __dirname + '/shots/74-phone-avatar.png' });
  check('no page errors', errs.length === 0, errs); console.log(ok ? '\nALL PASS' : '\nSOME FAILED'); await b.close(); process.exit(ok ? 0 : 1);
})();
