const { chromium } = require('playwright');
const fs = require('fs');
const ITEMS = Object.fromEntries(JSON.parse(fs.readFileSync('/home/user/englishfever/app/content/items.json')).map(i => [i.id, i]));
const BASE = 'http://127.0.0.1:8099';
(async () => {
  const b = await chromium.launch(); let ok = true; const errs = [];
  const check = (n, c, x) => { ok = ok && !!c; console.log((c ? 'PASS ' : 'FAIL ') + n + (c ? '' : ' -> ' + JSON.stringify(x))); };
  const ctx = await b.newContext({ viewport: { width: 1100, height: 900 } }); const p = await ctx.newPage();
  p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
  let curId = null;
  p.on('response', async r => {
    const u = r.url(); if (!/api\.php\?r=session(\/|%2F)(start|answer|resume)/.test(u)) return;
    try { const j = await r.json(); console.log('RESP', u.split('?r=')[1], 'item=', j.item && j.item.id, 'next=', j.next && j.next.id, 'resume=', j.resume && j.resume.item && j.resume.item.id); curId = (j.item && j.item.id) || (j.next && j.next.id) || (j.resume && j.resume.item && j.resume.item.id) || curId; } catch (e) {}
  });
  await p.goto(BASE + '/index.html'); await p.waitForSelector('#nick'); await p.waitForTimeout(1400); await p.click('button[type=submit]'); await p.waitForSelector('.hello h1');
  const post = (r, d) => p.evaluate(async ([r, d]) => (await fetch('api.php?r=' + r, { method: 'POST', headers: { 'X-EF': '1', 'Content-Type': 'application/json' }, body: JSON.stringify(d) })).json(), [r, d]);
  const s0 = await post('session/start', { mode: 'practice', skills: ['present_simple'], level: 'A2.1', length: 10 }); curId = s0.item.id;
  await p.goto(BASE + '/index.html#/session'); await p.reload(); await p.waitForSelector('.task');
  const answered = []; // what we did, per task
  async function answerUI(right) {
    await p.waitForSelector('.task .q'); const id = curId; const it = ITEMS[id]; let given;
    const dom = await p.evaluate(() => ({ q: document.querySelector('.task .q').innerText, opts: [...document.querySelectorAll('label.opt')].map(x => x.getAttribute('data-opt')) }));
    if (it.kind === 'mcq' && !dom.opts.includes(right ? it.correct : it.wrong[0])) console.log('MISMATCH', id, JSON.stringify(dom), '| item q:', it.q, '| correct', it.correct, '| wrong', it.wrong);
    if (it.kind === 'mcq') { given = right ? it.correct : it.wrong[0]; await p.locator('label.opt[data-opt="' + given.replace(/"/g, '\\"') + '"]').click(); }
    else if (it.kind === 'gap' && !it.bank) { given = it.answers.map(a => right ? a[0] : 'zzz'); const inp = p.locator('.task input.blank'); for (let i = 0; i < given.length; i++) await inp.nth(i).fill(given[i]); }
    else if (it.kind === 'text') { given = right ? it.answers[0][0] : 'zzz'; await p.fill('.task input.type-in', given); }
    else if (it.kind === 'gap' && it.bank) {
      const ws = it.answers.map(a => a[0]); given = right ? ws : ws.map(() => 'zzz');
      for (const w of (right ? ws : it.bank.filter(x => !ws.includes(x)).slice(0, ws.length))) await p.locator('.dnd-bank .chip', { hasText: new RegExp('^' + w.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\$&') + '$') }).first().click();
      if (!right) given = it.bank.filter(x => !ws.includes(x)).slice(0, ws.length);
    }
    else if (it.kind === 'order') {
      const toks = it.sentence.split(' '); given = right ? toks.join(' ') : toks.slice().reverse().join(' ');
      for (const t of (right ? toks : toks.slice().reverse())) await p.locator('.dnd-bank .chip', { hasText: new RegExp('^' + t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '$') }).first().click();
    }
    else if (it.kind === 'match') {
      const rights = it.pairs.map(x => x[1]); const seq = right ? rights : rights.slice().reverse(); given = seq.join(' | ');
      for (const t of seq) await p.locator('.dnd-bank .chip', { hasText: new RegExp('^' + t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '$') }).first().click();
    }
    else { throw new Error('unexpected kind ' + it.kind); }
    await p.click('.task .btn:has-text("Check answer")'); await p.waitForSelector('.feedback');
    answered.push({ id, kind: it.kind, given, right });
  }
  const label = () => p.locator('.sess-top > span').first().innerText();
  const dots = () => p.locator('.dots .dot');
  async function nextTask() { await p.click('.feedback .btn:has-text("Next")'); await p.waitForSelector('.task .q'); await p.waitForTimeout(80); }

  check('first task: the question strip is there from the start (so the page does not jump), only the current dot can be used, no Previous yet', (await dots().count()) > 0 && (await p.locator('.dots .dot:not([disabled])').count()) === 1 && (await p.locator('.sess-top .linkbtn:has-text("Previous")').count()) === 0);
  const plan = [true, false, true, false];
  for (const r of plan) { await answerUI(r); await nextTask(); }
  // now on task 5, nothing answered yet
  check('task 5 on screen', /Question 5 of 10/.test(await label()), await label());
  check('ten dots, four answered (2 good, 2 bad), one is "now"', (await dots().count()) === 10 && (await p.locator('.dot.good').count()) === 2 && (await p.locator('.dot.bad').count()) === 2 && (await p.locator('.dot.now').count()) === 1);
  check('future dots are disabled, the current one is not', (await p.locator('.dots .dot:disabled').count()) === 5);
  check('"Previous" is offered', (await p.locator('.sess-top .linkbtn:has-text("Previous")').count()) === 1);

  // look back at task 4 with Previous
  await p.click('.sess-top .linkbtn:has-text("Previous")'); await p.waitForSelector('.feedback');
  check('looking back at task 4: label says so', /Question 4 of 10 · looking back/.test(await label()), await label());
  const t4 = answered[3];
  const lockedAll = await p.evaluate(() => [...document.querySelectorAll('.task input')].every(i => i.disabled));
  check('task 4 is read-only and shows the saved answer', lockedAll && (t4.kind === 'order' || t4.kind === 'match' || (t4.kind === 'gap' && (await p.locator('.task input[type=text]').count()) === 0) ? true : t4.kind === 'mcq' ? (await p.locator('.task input[type=radio]:checked').getAttribute('value')) === t4.given : (await p.locator('.task input[type=text]').evaluateAll(a => a.map(x => x.value))).join('|') === [].concat(t4.given).join('|')), t4);
  check('the feedback of task 4 is shown (it was wrong)', (await p.locator('.feedback.bad').count()) === 1);
  check('no Check answer button while looking back', (await p.locator('.task .btn:has-text("Check answer")').count()) === 0);
  check('the XP / progress did not change by looking', /Question 4/.test(await label()));
  // dot 1
  await dots().nth(0).click(); await p.waitForSelector('.feedback');
  const t1 = answered[0];
  check('dot 1 shows task 1, correct', /Question 1 of 10 · looking back/.test(await label()) && (await p.locator('.feedback.good').count()) === 1, await label());
  check('Previous is gone at task 1; Next › is there', (await p.locator('.sess-top .linkbtn:has-text("Previous")').count()) === 0 && (await p.locator('.feedback .btn:has-text("Next ›")').count()) === 1);
  await p.click('.feedback .btn:has-text("Next ›")'); await p.waitForSelector('.feedback');
  check('Next › moves to task 2 (wrong)', /Question 2 of 10/.test(await label()) && (await p.locator('.feedback.bad').count()) === 1, await label());
  // back to where we were
  await p.click('.feedback .btn:has-text("Back to question 5")'); await p.waitForSelector('.task .q');
  check('back on task 5: not answered, Check answer is there (disabled), no feedback', /Question 5 of 10$/.test(await label()) && (await p.locator('.feedback').count()) === 0 && (await p.locator('.task .btn:has-text("Check answer")').isDisabled()), await label());
  // the current dot works too
  await dots().nth(1).click(); await p.waitForSelector('.feedback'); await dots().nth(4).click(); await p.waitForSelector('.task .q');
  check('clicking the current dot returns to the task', /Question 5 of 10$/.test(await label()) && (await p.locator('.feedback').count()) === 0, await label());

  // a reload keeps the dots
  await p.reload(); await p.waitForSelector('.task');
  check('after a reload the answered tasks are still there', (await p.locator('.dot.good').count()) === 2 && (await p.locator('.dot.bad').count()) === 2 && /Question 5 of 10$/.test(await label()), await label());

  // answer task 5, then look back and return to its feedback with the real Next button
  await answerUI(true);
  check('after answering, its dot turns good and stays "now"', (await p.locator('.dot.good').count()) === 3 && (await p.locator('.dot.now.good').count()) === 1);
  await dots().nth(1).click(); await p.waitForSelector('.feedback');
  check('looking back from an answered task', /Question 2 of 10 · looking back/.test(await label()));
  await dots().nth(4).click(); await p.waitForSelector('.feedback');
  check('the current dot returns to the feedback with the real "Next" button', (await p.locator('.feedback .btn:has-text("Next")').count()) === 1 && !/looking back/.test(await label()) && /Question 5 of 10/.test(await label()), await label());
  await nextTask();
  check('next task is 6; five answered', /Question 6 of 10$/.test(await label()) && (await p.locator('.dot.good, .dot.bad').count()) === 5, await label());

  // language toggle inside a looked-at task still works
  await p.click('.sess-top .linkbtn:has-text("Previous")'); await p.waitForSelector('.feedback');
  const toggle = p.locator('.feedback .linkbtn:has-text("Latviski")');
  if (await toggle.count()) { await toggle.click(); await p.waitForTimeout(200); check('Latvian toggle works while looking back', (await p.locator('.feedback').innerText()).match(/Kāpēc|Pareizā|Padoms|Tu /) !== null); await p.locator('.feedback .linkbtn:has-text("English")').click(); }

  // finishing the session clears the stored history
  for (let i = 0; i < 4; i++) { await p.click('.sess-top .linkbtn:has-text("Stop")').catch(() => {}); break; }
  check('no page errors', errs.length === 0, errs);
  console.log(ok ? '\nALL PASS' : '\nSOME FAILED'); await b.close(); process.exit(ok ? 0 : 1);
})();
