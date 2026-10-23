const { chromium, devices } = require('playwright');
const fs = require('fs');
const ITEMS = Object.fromEntries(JSON.parse(fs.readFileSync('/home/user/englishfever/app/content/items.json')).map(i => [i.id, i]));
const BASE = 'http://127.0.0.1:8099';
// the install hint appears on Home after the first practice (Home is quiet for a brand-new learner): practise a little, then show Home again without reloading
async function practise(pg) {
  const post = (r, d) => pg.evaluate(async ([r, d]) => (await fetch('api.php?r=' + r, { method: 'POST', headers: { 'X-EF': '1', 'Content-Type': 'application/json' }, body: JSON.stringify(d) })).json(), [r, d]);
  let cur = await post('session/start', { mode: 'practice', skills: ['present_simple'], level: 'A2.1', length: 10 });
  const it = ITEMS[cur.item.id]; const ans = it.kind === 'mcq' ? it.correct : (it.kind === 'gap' ? it.answers.map(a => a[0]) : (it.answers ? it.answers[0][0] : 'x'));
  cur = await post('session/answer', { session_id: cur.session.id, item_id: cur.item.id, answer: ans, time_ms: 2000 });
  await post('session/quit', { session_id: cur.session.id });
  await pg.evaluate(() => { location.hash = '#/rules'; }); await pg.waitForTimeout(200);
  await pg.evaluate(() => { location.hash = '#/home'; }); await pg.waitForSelector('.card.focus h2:has-text("Ready to practise")');
}
const errs = []; let ok = true;
const check = (n, c, x) => { ok = ok && !!c; console.log((c ? 'PASS ' : 'FAIL ') + n + (c ? '' : '  -> ' + JSON.stringify(x))); };
(async () => {
  const b = await chromium.launch();

  // ---- desktop: manifest, icons, service worker, offline
  const ctx = await b.newContext({ viewport: { width: 1200, height: 800 } });
  const p = await ctx.newPage();
  p.on('pageerror', e => errs.push(e.message));
  await p.goto(BASE + '/index.html'); await p.waitForSelector('.hero');
  const man = await p.evaluate(async () => { const l = document.querySelector('link[rel=manifest]'); const r = await fetch(l.href); return await r.json(); });
  check('manifest has name, standalone display and brand colours', man.name === 'English Fever Practice' && man.display === 'standalone' && man.theme_color === '#020101' && man.background_color === '#F7F5EE', man);
  const sizes = await p.evaluate(async (icons) => Promise.all(icons.map(async i => { const r = await fetch(i.src); const bm = await createImageBitmap(await r.blob()); return [i.sizes, bm.width + 'x' + bm.height, i.purpose]; })), man.icons);
  check('icons exist at the declared sizes (192, 512, maskable 512)', sizes.length === 3 && sizes.every(s => s[0] === s[1]), sizes);
  const touch = await p.evaluate(async () => { const l = document.querySelector('link[rel=apple-touch-icon]'); const bm = await createImageBitmap(await (await fetch(l.href)).blob()); return bm.width; });
  check('apple touch icon is 180 px', touch === 180, touch);
  check('iOS web app meta tags', await p.evaluate(() => !!document.querySelector('meta[name=apple-mobile-web-app-capable]') && /viewport-fit=cover/.test(document.querySelector('meta[name=viewport]').content)));
  await p.evaluate(() => navigator.serviceWorker.ready); await p.reload(); await p.waitForSelector('.hero'); await p.waitForTimeout(500);
  check('service worker active and controlling the page', await p.evaluate(() => !!navigator.serviceWorker.controller));
  // sign in as guest so the API gets used, then check what is cached
  await p.fill('#nick', 'Pwa tester'); await p.click('button[type=submit]'); await p.waitForSelector('.hello h1');
  await p.goto(BASE + '/index.html#/leaderboard'); await p.waitForTimeout(800);
  const cached = await p.evaluate(async () => { const out = []; for (const k of await caches.keys()) { const c = await caches.open(k); out.push(...(await c.keys()).map(r => r.url)); } return out; });
  check('app files are cached', cached.some(u => /assets\/app\.js/.test(u)) && cached.some(u => /index\.html|\/$/.test(u)), cached.length);
  check('the API, login and answers are never cached', !cached.some(u => /api\.php|sso\.php/.test(u)), cached.filter(u => /api\.php|sso\.php/.test(u)));
  await ctx.setOffline(true); await p.goto(BASE + '/index.html'); await p.waitForTimeout(1200);
  const txt = await p.evaluate(() => document.body.innerText);
  check('offline: the app opens and says so politely (no blank page)', /You are offline/.test(txt) && /Try again/.test(txt), txt.slice(0, 120));
  await ctx.setOffline(false);
  // desktop home: no install card, profile has it
  await p.goto(BASE + '/index.html'); await p.waitForSelector('.hello h1'); await p.waitForTimeout(300);
  check('desktop home: no install card', !(await p.locator('#install-card').count()));
  await p.goto(BASE + '/index.html#/profile'); await p.waitForSelector('#pn');
  check('desktop profile without a browser install button: nothing to say, no card', (await p.locator('#install-card').count()) === 0);
  await p.evaluate(() => { const e = new Event('beforeinstallprompt'); e.prompt = () => Promise.resolve(); e.userChoice = Promise.resolve({ outcome: 'dismissed' }); window.dispatchEvent(e); });
  await p.goto(BASE + '/index.html#/home'); await p.waitForSelector('.hello h1'); await p.goto(BASE + '/index.html#/profile'); await p.waitForSelector('#install-card', { timeout: 3000 }).catch(() => {});
  const dtxt = await p.locator('#install-card').count() ? await p.locator('#install-card').innerText() : '';
  check('desktop with a browser install button: "Install the app on this computer"', /Install the app on this computer/.test(dtxt) && /Install the app/.test(dtxt) && !/phone/i.test(dtxt), dtxt);

  // ---- iPhone Safari
  const ip = await b.newContext({ ...devices['iPhone 13'] }); const i = await ip.newPage(); i.on('pageerror', e => errs.push(e.message));
  await i.goto(BASE + '/index.html'); await i.waitForSelector('.hero'); await i.fill('#nick', 'Phone tester'); await i.click('button[type=submit]'); await i.waitForSelector('.hello h1'); await practise(i);
  const ic = i.locator('#install-card'); await ic.waitFor();
  const it = await ic.innerText();
  check('iPhone: card explains Share > Add to Home Screen', /Share/.test(it) && /Add to Home Screen/.test(it), it);
  check('iPhone: the title says phone', /phone’s home screen/i.test(it), it);
  await i.screenshot({ path: __dirname + '/shots/60-iphone-install.png' });
  await i.click('#install-card button:has-text("Not now")');
  await i.goto(BASE + '/index.html#/home'); await i.waitForSelector('.hello h1'); await i.waitForTimeout(300);
  check('"Not now" hides it (remembered)', !(await i.locator('#install-card').count()));

  // ---- installed (standalone): never shown
  const st = await b.newContext({ ...devices['iPhone 13'] }); await st.addInitScript(() => { Object.defineProperty(navigator, 'standalone', { get: () => true }); });
  const s = await st.newPage(); await s.goto(BASE + '/index.html'); await s.waitForSelector('.hero'); await s.fill('#nick', 'Installed'); await s.click('button[type=submit]'); await s.waitForSelector('.hello h1');
  await s.goto(BASE + '/index.html#/profile'); await s.waitForSelector('#pn');
  check('installed app: no install hint anywhere', !(await s.locator('#install-card').count()));

  // ---- Android Chrome: real install button
  const an = await b.newContext({ ...devices['Pixel 7'] }); const a = await an.newPage(); a.on('pageerror', e => errs.push(e.message));
  await a.goto(BASE + '/index.html'); await a.waitForSelector('.hero');
  await a.evaluate(() => { window.__prompted = 0; const e = new Event('beforeinstallprompt'); e.prompt = () => { window.__prompted++; return Promise.resolve(); }; e.userChoice = Promise.resolve({ outcome: 'accepted' }); window.dispatchEvent(e); });
  await a.fill('#nick', 'Droid'); await a.click('button[type=submit]'); await a.waitForSelector('.hello h1'); await practise(a);
  const btn = a.locator('#install-card button:has-text("Install the app")'); await btn.waitFor();
  await btn.click(); await a.waitForTimeout(300);
  check('Android: "Install the app" calls the browser prompt', (await a.evaluate(() => window.__prompted)) === 1);

  const an2 = await b.newContext({ ...devices['Pixel 7'] }); const a2 = await an2.newPage(); a2.on('pageerror', e => errs.push(e.message));
  await a2.goto(BASE + '/index.html'); await a2.waitForSelector('.hero'); await a2.fill('#nick', 'Droid2'); await a2.click('button[type=submit]'); await a2.waitForSelector('.hello h1'); await practise(a2);
  const at = await a2.locator('#install-card').innerText();
  check('Android without a prompt: menu wording, for the phone', /On your phone/.test(at) && /Install app/.test(at) && /Add to Home screen/.test(at), at);
  console.log(errs.length ? 'ERRORS: ' + errs.join('; ') : 'no page errors');
  console.log(ok && !errs.length ? '\nALL PASS' : '\nSOME FAILED'); await b.close(); process.exit(ok && !errs.length ? 0 : 1);
})();
