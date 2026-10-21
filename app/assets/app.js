// English Fever practice app (A2.1 – B1.2 tenses). Single page, hash routes.
(function () {
  'use strict';
  var h = UI.h, icon = UI.icon, api = UI.api;
  var root = document.getElementById('app');
  var chrome = document.getElementById('chrome');
  var footer = document.getElementById('foot');

  var state = {
    config: null, meta: null, user: null, dash: null,
    todaySeconds: 0, streak: 0, sess: null, prefill: null, lastInteraction: Date.now(),
  };

  // ───────── helpers ─────────
  var VOICE_LABEL = { active: 'Active', passive: 'Passive' };
  function bloomName(n) { return state.meta.bloom[String(n)].name; }
  function bloomDots(n) {
    var d = h('span', { class: 'bloomdots', title: 'Thinking level ' + n + ' of 6: ' + bloomName(n) });
    for (var i = 1; i <= 6; i++) d.appendChild(h('i', { class: i <= n ? 'on' : '' }));
    return d;
  }
  function skillById(id) { return state.meta.skills.filter(function (s) { return s.id === id; })[0]; }
  function pct(c, n) { return n ? Math.round(100 * c / n) : 0; }
  function loading() { return h('div', { class: 'loading', role: 'status' }, h('div', { class: 'spin' }), h('span', { class: 'sr' }, 'Loading')); }
  function show(node) { root.replaceChildren(node); window.scrollTo(0, 0); var hd = node.querySelector && node.querySelector('h1'); if (hd) { hd.setAttribute('tabindex', '-1'); hd.focus({ preventScroll: true }); } }
  function fail(e) { show(h('div', { class: 'card' }, h('h2', null, 'Something went wrong'), h('p', null, e.message || 'Please try again.'), h('a', { class: 'btn', href: '#/home' }, 'Back to home'))); }
  function levelPill(l) { return h('span', { class: 'pill' }, l); }

  // ───────── boot ─────────
  function boot() {
    Promise.all([api('config'), api('meta'), api('me')]).then(function (r) {
      state.config = r[0]; state.meta = r[1]; state.user = r[2].user;
      footer.replaceChildren(
        h('div', null, h('a', { href: state.config.privacy_url, target: '_blank', rel: 'noopener' }, 'Privacy policy'), ' · We store your nickname, scores and time spent. ',
          state.config.contact_email ? h('a', { href: 'mailto:' + state.config.contact_email }, state.config.contact_email) : null));
      if (state.user) startHeartbeat();
      window.addEventListener('hashchange', route);
      ['pointerdown', 'keydown', 'scroll', 'input'].forEach(function (ev) { window.addEventListener(ev, function () { state.lastInteraction = Date.now(); }, { passive: true }); });
      route();
    }).catch(function (e) { root.replaceChildren(h('div', { class: 'card' }, h('h2', null, 'The app cannot start'), h('p', null, e.message))); });
  }

  // ───────── time tracking ─────────
  var hbTimer = null, hbLast = Date.now();
  function startHeartbeat() {
    if (hbTimer) return;
    hbLast = Date.now();
    hbTimer = setInterval(function () {
      var now = Date.now();
      var secs = Math.min(30, Math.round((now - hbLast) / 1000));
      hbLast = now;
      if (!state.user || document.visibilityState !== 'visible' || now - state.lastInteraction > 60000 || secs < 1) return;
      state.todaySeconds += secs;
      renderChips();
      api('heartbeat', { seconds: secs }).catch(function () {});
    }, 10000);
  }

  function stopHeartbeat() { if (hbTimer) { clearInterval(hbTimer); hbTimer = null; } state.todaySeconds = 0; state.streak = 0; }

  // ───────── chrome (top bar and mobile tabs) ─────────
  function renderChrome(active) {
    if (!state.user) { chrome.replaceChildren(); return; }
    var teacher = state.user.role === 'teacher';
    var items = teacher
      ? [['#/teacher', 'Students', 'users'], ['#/practice', 'Practice', 'target'], ['#/leaderboard', 'Leaderboard', 'trophy'], ['#/profile', 'Profile', 'user']]
      : [['#/home', 'Home', 'home'], ['#/practice', 'Practice', 'target'], ['#/leaderboard', 'Leaderboard', 'trophy'], ['#/profile', 'Profile', 'user']];
    var nav = h('nav', { class: 'nav', 'aria-label': 'Main' }, items.map(function (i) {
      return h('a', { href: i[0], 'aria-current': active === i[0] ? 'page' : null }, i[1]);
    }));
    var tabs = h('nav', { class: 'tabbar', 'aria-label': 'Main' }, items.map(function (i) {
      return h('a', { href: i[0], 'aria-current': active === i[0] ? 'page' : null }, icon(i[2]), i[1]);
    }));
    var chips = h('div', { class: 'chips', id: 'chips' });
    var bar = h('header', { class: 'topbar' }, h('div', { class: 'topbar-in' },
      h('a', { class: 'brand', href: teacher ? '#/teacher' : '#/home' }, h('span', { class: 'dot' }), 'English Fever ', h('b', null, 'Practice')),
      nav, h('div', { class: 'spacer' }), chips));
    chrome.replaceChildren(bar, tabs);
    renderChips();
  }

  function renderChips() {
    var c = document.getElementById('chips');
    if (!c || !state.user || state.user.role === 'teacher') return;
    c.replaceChildren(
      state.user.guest ? h('button', { class: 'chip-top', style: 'background:none;cursor:pointer', title: 'Guest: results are not saved', onclick: function () { guestInvite(true); } }, 'Guest · save progress') : null,
      h('span', { class: 'chip-top', title: 'Daily streak' }, icon('flame'), String(state.streak), ' day' + (state.streak === 1 ? '' : 's')),
      h('span', { class: 'chip-top hide-m', title: 'Time practised today' }, icon('clock'), UI.fmtDuration(state.todaySeconds)));
  }

  function refreshDash() {
    return api('dashboard').then(function (d) {
      state.dash = d; state.todaySeconds = d.today.seconds; state.streak = d.streak.current;
      renderChips();
      return d;
    });
  }

  // ───────── router ─────────
  function go(hash) { if (location.hash === hash) route(); else location.hash = hash; }

  function route() {
    var hash = location.hash || '#/';
    var parts = hash.replace(/^#\/?/, '').split('/');
    var name = parts[0] || '';
    if (!state.user) { renderChrome(); return viewWelcome(); }
    startHeartbeat();
    var u = state.user;
    if (!u.nick_set && u.provider === 'wp' && name !== 'nickname') { location.hash = '#/nickname'; return; }
    if (name === '' || name === 'welcome') { location.hash = u.role === 'teacher' ? '#/teacher' : '#/home'; return; }
    renderChrome('#/' + name);
    show(loading());
    var v = {
      home: viewHome, practice: viewPractice, placement: viewPlacementIntro, session: viewSession, summary: viewSummary,
      leaderboard: viewLeaderboard, profile: viewProfile, teacher: function () { return parts[1] === 'student' ? viewTeacherStudent(parts[2]) : viewTeacher(); },
      nickname: viewNickname, rules: viewRules,
    }[name];
    if (name.indexOf('teacher') === 0 && u.role !== 'teacher') { location.hash = '#/home'; return; }
    (v || viewHome)(parts);
  }

  // ───────── welcome / sign in ─────────
  function viewWelcome() {
    var cfg = state.config;
    var errBox = h('div');
    var nick = h('input', { type: 'text', id: 'nick', autocomplete: 'off', autocapitalize: 'off', spellcheck: 'false', maxlength: '30', placeholder: 'Your nickname', required: true });
    var guestForm = h('form', { novalidate: true, onsubmit: function (e) {
      e.preventDefault(); errBox.replaceChildren();
      var btn = guestForm.querySelector('button[type=submit]'); btn.disabled = true;
      api('guest', { nickname: nick.value }).then(function (r) {
        state.user = r.user; startHeartbeat(); go('#/home');
      }).catch(function (err) { btn.disabled = false; errBox.replaceChildren(h('div', { class: 'err', role: 'alert' }, err.message)); });
    } },
      h('div', { class: 'field' }, h('label', { for: 'nick' }, 'Nickname'), nick),
      errBox,
      h('button', { class: cfg.sso ? 'btn ghost block' : 'btn block', type: 'submit' }, 'Start as guest'),
      h('p', { class: 'small muted', style: 'margin:10px 0 0;text-align:center' }, 'Guest results are not saved.'));

    var card = [];
    if (cfg.sso) {
      card.push(
        h('h2', { style: 'text-align:center' }, 'Registered at englishfever.com?'),
        h('a', { class: 'btn block', href: cfg.wp_login_url }, 'Continue with my account'),
        h('p', { class: 'small muted', style: 'text-align:center;margin:10px 0 0' }, 'No new password. Your results are saved.'),
        h('div', { class: 'or' }, 'or'),
        h('h2', { style: 'text-align:center' }, 'Try it as a guest'));
    } else {
      card.push(h('h2', { style: 'text-align:center' }, 'Start practising'));
    }
    card.push(guestForm);
    if (cfg.register_url) card.push(h('p', { class: 'small', style: 'text-align:center;margin:16px 0 0' }, 'No account yet? ', h('a', { href: cfg.register_url }, 'Create a free account')));

    show(h('div', null,
      h('section', { class: 'hero' },
        h('div', { class: 'bar' }),
        h('h1', null, 'Practise English tenses. ', h('em', null, 'Know what to fix next.')),
        h('p', null, 'Short tasks for adult learners, from A2.1 to B1.2. Active and passive. You get clear feedback after every answer, and the tasks get easier or harder to fit you.'),
        h('div', { class: 'points' },
          h('div', null, h('b', null, 'Placement test'), '24 quick questions. See your gaps and where to start.'),
          h('div', null, h('b', null, 'Your choice'), 'Pick one tense or several, and the level you want.'),
          h('div', null, h('b', null, 'Real thinking'), 'Not only gaps: spot mistakes, judge answers and write your own sentences.'))),
      h('div', { class: 'card', style: 'max-width:480px;margin:0 auto' }, card)));
  }

  // The invitation shown to guests after practice: create a free account to keep the results.
  function guestInvite(force) {
    if (!state.user || !state.user.guest || !state.config) return;
    if (!force) {
      try { if (Date.now() - (+localStorage.getItem('ef_invite') || 0) < 86400000) return; } catch (e) {}
    }
    try { localStorage.setItem('ef_invite', String(Date.now())); } catch (e) {}
    var cfg = state.config;
    var m = UI.modal(h('div', null,
      h('div', { class: 'label' }, 'Keep your progress'),
      h('h2', null, 'Create a free account to save your results'),
      h('p', null, 'You are practising as a guest. If you clear your browser or use another device, your results are lost. With a free account you keep your results, streak and level, and you can join the leaderboard.'),
      h('p', { class: 'small muted' }, 'Everything you did as a guest moves to your new account. After you register, come back to this page and press “Continue with my account”.'),
      h('div', { class: 'row' },
        cfg.register_url ? h('a', { class: 'btn', href: cfg.register_url }, 'Create free account') : null,
        cfg.sso ? h('a', { class: cfg.register_url ? 'btn ghost' : 'btn', href: cfg.wp_login_url }, 'I already have an account') : null,
        h('button', { class: 'linkbtn', id: 'later' }, 'Not now'))));
    m.el.querySelector('#later').onclick = m.close;
  }

  function guestBanner() {
    var cfg = state.config;
    return h('div', { class: 'card pad-s row between', style: 'margin-bottom:16px;border-color:var(--gold)' },
      h('div', null, h('b', { style: 'color:var(--text)' }, 'You are practising as a guest'),
        h('div', { class: 'small muted' }, 'Create a free account to keep your results and join the leaderboard.')),
      h('div', { class: 'row' },
        cfg.register_url ? h('a', { class: 'btn small', href: cfg.register_url }, 'Create account') : null,
        cfg.sso ? h('a', { class: cfg.register_url ? 'btn ghost small' : 'btn small', href: cfg.wp_login_url }, 'Sign in') : null));
  }

  // ───────── home ─────────
  function viewHome() {
    if (state.user.role === 'teacher') { location.hash = '#/teacher'; return; }
    Promise.all([refreshDash(), api('session/resume')]).then(function (r) {
      var d = r[0], resume = r[1].resume;
      var nodes = [];
      if (state.user.guest) nodes.push(guestBanner());
      nodes.push(h('div', { class: 'hello' },
        h('div', null, h('div', { class: 'label' }, 'Welcome back'), h('h1', { style: 'margin:0' }, state.user.nickname)),
        h('p', { class: 'muted' }, d.streak.today_done ? 'You practised today. Nice work!' : (d.streak.current ? 'Practise today to keep your streak alive.' : 'Do one task today to start a streak.'))));

      if (resume) {
        nodes.push(h('div', { class: 'card pad-s row between', style: 'margin-bottom:16px;border-color:var(--gold)' },
          h('div', null, h('b', { style: 'color:var(--text)' }, 'You have an unfinished ' + (resume.session.mode === 'placement' ? 'placement test' : 'practice session')),
            h('div', { class: 'small muted' }, resume.session.n + ' of ' + resume.session.length + ' done')),
          h('button', { class: 'btn small', onclick: function () { state.sess = newSess(resume.session, resume.item); location.hash = '#/session'; } }, 'Continue')));
      }

      nodes.push(h('div', { class: 'grid g4', style: 'margin-bottom:16px' },
        stat('flame', d.streak.current, d.streak.current === 1 ? 'day streak' : 'day streak', 'streak'),
        stat('clock', UI.fmtDuration(d.today.seconds), 'practised today'),
        stat('bolt', d.totals.xp, 'points (XP)'),
        stat('check', d.totals.accuracy === null ? '–' : d.totals.accuracy + '%', 'correct overall')));

      var rep = d.placement && d.placement.report;
      var started = d.totals.answers > 0;
      nodes.push(h('div', { class: 'grid g2', style: 'margin-bottom:16px' },
        h('div', { class: 'card' }, h('div', { class: 'label' }, 'Option 1'), h('h2', null, rep ? 'Your placement result' : 'Take the placement test'),
          rep ? h('div', null,
            h('div', { class: 'row', style: 'margin-bottom:10px' }, h('span', { class: 'levelbadge' }, rep.overall_level), h('span', { class: 'muted small' }, 'about ' + rep.overall_level + ' · ' + UI.fmtAgo(d.placement.at))),
            h('p', null, 'Start with: ', rep.gaps.map(function (g) { return g.label; }).join(', ') + '.'),
            h('div', { class: 'row' }, h('button', { class: 'btn small', onclick: function () { showPlacementReport(rep); } }, 'See gaps and plan'),
              h('a', { class: 'btn ghost small', href: '#/placement' }, 'Take it again')))
            : h('div', null, h('p', null, 'About 24 questions, around 10 minutes. You get a gap report and a plan for where to begin.'),
              h('a', { class: 'btn', href: '#/placement' }, 'Start the test', icon('arrow')))),
        h('div', { class: 'card' }, h('div', { class: 'label' }, 'Option 2'), h('h2', null, 'Choose what to practise'),
          h('p', null, 'Pick one tense or several, and the level you want. A quick check of 3 tasks comes first, then the tasks adapt to you.'),
          h('a', { class: started ? 'btn' : 'btn ghost', href: '#/practice' }, 'Choose tenses', icon('arrow')))));

      nodes.push(h('div', { class: 'grid g2', style: 'margin-bottom:16px' },
        h('div', { class: 'card' }, h('h2', null, 'This week'), weekChart(d.week)),
        h('div', { class: 'card' }, h('h2', null, 'Your thinking skills'), h('p', { class: 'small muted' }, 'How often you are right at each level of thinking.'), bloomBars(d.bloom))));

      nodes.push(h('div', { class: 'card' }, h('div', { class: 'row between' }, h('h2', { style: 'margin:0' }, 'Your tenses'), h('a', { href: '#/rules', class: 'small' }, 'Rule cards')),
        h('p', { class: 'small muted' }, 'Your level estimate appears after 3 or more tasks in a tense.'),
        h('div', { class: 'skillgrid' }, d.skills.map(skillCard))));
      show(h('div', null, nodes));
    }).catch(fail);
  }

  function stat(ic, v, k, cls) {
    return h('div', { class: 'card pad-s stat ' + (cls || '') }, h('div', { class: 'v' }, icon(ic), String(v)), h('div', { class: 'k' }, k));
  }

  function weekChart(week) {
    var max = Math.max.apply(null, week.map(function (w) { return w.seconds; }).concat([60]));
    var today = week[week.length - 1].day;
    return h('div', { class: 'bars', role: 'img', 'aria-label': 'Minutes practised in the last 7 days' }, week.map(function (w) {
      var dt = new Date(w.day + 'T12:00:00');
      return h('div', { class: 'b' }, h('div', { class: 'm' }, w.seconds ? String(Math.max(1, Math.round(w.seconds / 60))) : ''),
        h('div', { class: 'col' + (w.day === today ? ' today' : ''), style: 'height:' + Math.max(3, Math.round(70 * w.seconds / max)) + 'px' }),
        h('div', { class: 'd' }, dt.toLocaleDateString(undefined, { weekday: 'short' }).slice(0, 2)));
    }));
  }

  function bloomBars(b) {
    return h('div', { class: 'hbars' }, [1, 2, 3, 4, 5, 6].map(function (i) {
      var v = b[String(i)];
      return h('div', { class: 'hbar' }, h('span', { class: 'nm' }, bloomName(i)),
        h('div', { class: 'meter' }, h('i', { style: 'width:' + (v ? pct(v.correct, v.n) : 0) + '%' })),
        h('span', { class: 'vl' }, v ? pct(v.correct, v.n) + '%' : '–'));
    }));
  }

  function skillCard(s) {
    return h('div', { class: 'skill' },
      h('div', { class: 'top' }, h('div', null, h('div', { class: 'name' }, s.label), h('div', { class: 'small muted' }, VOICE_LABEL[s.voice] + ' · ' + s.levels[0] + (s.levels.length > 1 ? '–' + s.levels[s.levels.length - 1] : ''))),
        s.level_est ? h('span', { class: 'pill dark' }, '≈ ' + s.level_est) : h('span', { class: 'pill' }, s.n ? s.n + (s.n === 1 ? ' task' : ' tasks') : 'New')),
      h('div', { class: 'meter gold', 'aria-label': 'Accuracy' }, h('i', { style: 'width:' + (s.accuracy || 0) + '%' })),
      h('div', { class: 'row between' }, h('span', { class: 'small muted' }, s.n ? s.accuracy + '% correct · ' + s.n + ' tasks' : 'Not started'),
        h('button', { class: 'linkbtn small', onclick: function () { state.prefill = { skills: [s.id], level: s.level_est || s.levels[0] }; location.hash = '#/practice'; } }, 'Practise')));
  }

  // ───────── placement ─────────
  function viewPlacementIntro() {
    show(h('div', { class: 'sess' }, h('div', { class: 'card' },
      h('div', { class: 'label' }, 'Placement test'), h('h1', null, 'Find your starting point'),
      h('p', null, 'You will answer ' + state.meta.placement_length + ' short questions about active and passive tenses. It takes about 10 minutes.'),
      h('ul', { style: 'padding-left:20px;margin:0 0 18px' },
        h('li', null, 'The questions get easier or harder to fit your answers.'),
        h('li', null, 'You will see if each answer is right, with a short explanation.'),
        h('li', null, 'At the end you get your level and the 3 tenses to work on first.')),
      h('p', { class: 'small muted' }, 'Do not worry about mistakes. They help us find the right place to start. You can stop at any time.'),
      h('div', { class: 'row' }, h('button', { class: 'btn', id: 'go' }, 'Start the test'), h('a', { class: 'btn ghost', href: '#/home' }, 'Not now')))));
    document.getElementById('go').addEventListener('click', function () {
      this.disabled = true;
      api('session/start', { mode: 'placement' }).then(function (r) { state.sess = newSess(r.session, r.item); location.hash = '#/session'; }).catch(fail);
    });
  }

  // ───────── practice picker ─────────
  function viewPractice() {
    var d = state.dash;
    var pre = state.prefill; state.prefill = null;
    var guess = (d && d.placement && d.placement.report) ? d.placement.report.overall_level : 'A2.2';
    var selected = {};
    (pre ? pre.skills : []).forEach(function (s) { selected[s] = true; });
    var level = pre ? pre.level : guess;
    var length = 10;
    var note = h('div', { class: 'small muted', 'aria-live': 'polite' });
    var startBtn = h('button', { class: 'btn', disabled: true }, 'Start practice');
    var err = h('div');

    function checkbox(s) {
      var inp = h('input', { type: 'checkbox', value: s.id, checked: !!selected[s.id], onchange: function () { selected[s.id] = inp.checked; update(); } });
      return h('label', null, inp, h('span', null, s.label, ' ', h('small', null, s.levels[0] + (s.levels.length > 1 ? '–' + s.levels[s.levels.length - 1] : ''))));
    }
    function group(voice, title) {
      var list = state.meta.skills.filter(function (s) { return s.voice === voice; });
      return h('div', { class: 'picker-group' },
        h('div', { class: 'row between' }, h('h3', null, title),
          h('button', { class: 'linkbtn small', onclick: function () { list.forEach(function (s) { selected[s.id] = true; }); redraw(); } }, 'Select all')),
        h('div', { class: 'chipsel', role: 'group', 'aria-label': title }, list.map(checkbox)));
    }
    function update() {
      var ids = Object.keys(selected).filter(function (k) { return selected[k]; });
      startBtn.disabled = ids.length === 0;
      var low = ids.map(skillById).filter(function (s) { return s.levels.indexOf(level) < 0; });
      note.textContent = low.length ? low.map(function (s) { return s.label + ' has tasks at ' + s.levels.join(', ') + ' only. We will use the nearest ones.'; }).join(' ') : '';
    }
    var holder = h('div');
    function redraw() {
      holder.replaceChildren(
        group('active', 'Active tenses'), group('passive', 'Passive tenses'),
        h('div', { class: 'picker-group' }, h('h3', null, 'Level'),
          h('div', { class: 'seg', role: 'radiogroup', 'aria-label': 'Level' }, state.meta.levels.map(function (l) {
            return h('label', null, h('input', { type: 'radio', name: 'lv', value: l, checked: l === level, onchange: function () { level = l; update(); } }), h('span', null, l));
          })), h('p', { class: 'small muted', style: 'margin-top:8px' }, 'B2 levels are coming soon.')),
        h('div', { class: 'picker-group' }, h('h3', null, 'Length'),
          h('div', { class: 'seg', role: 'radiogroup', 'aria-label': 'Number of tasks' }, [10, 15, 20].map(function (n) {
            return h('label', null, h('input', { type: 'radio', name: 'len', value: String(n), checked: n === length, onchange: function () { length = n; } }), h('span', null, n + ' tasks'));
          }))));
      update();
    }
    startBtn.addEventListener('click', function () {
      startBtn.disabled = true;
      var ids = Object.keys(selected).filter(function (k) { return selected[k]; });
      api('session/start', { mode: 'practice', skills: ids, level: level, length: length }).then(function (r) {
        state.sess = newSess(r.session, r.item); location.hash = '#/session';
      }).catch(function (e) { startBtn.disabled = false; err.replaceChildren(h('div', { class: 'err', role: 'alert' }, e.message)); });
    });
    redraw();
    show(h('div', { class: 'sess' }, h('div', { class: 'card' },
      h('div', { class: 'label' }, 'Practice'), h('h1', null, 'Choose what to practise'),
      h('p', null, 'Pick one tense or several. The first 3 tasks are a quick check. After that, tasks get harder when you are right and easier when you need more help.'),
      holder, note, err, h('div', { class: 'row', style: 'margin-top:16px' }, startBtn,
        h('a', { class: 'btn ghost', href: '#/placement' }, 'Take the placement test instead')))));
  }

  // ───────── session ─────────
  function newSess(session, item) { return { session: session, item: item, startedAt: Date.now(), result: null, last: null }; }

  function viewSession() {
    var S = state.sess;
    if (!S) { return api('session/resume').then(function (r) { if (r.resume) { state.sess = newSess(r.resume.session, r.resume.item); viewSession(); } else location.hash = '#/home'; }).catch(fail); }
    var it = S.item, ses = S.session;
    var answerGetter, canSubmit = function () { return false; };
    var submit = h('button', { class: 'btn', disabled: true }, 'Check answer');
    var area = h('div');
    var qEl = h('div', { class: 'q' });
    var inputs = [];
    var chosen = null;

    function ready() { submit.disabled = !canSubmit(); }

    if (it.kind === 'mcq') {
      qEl.textContent = it.q;
      var wrap = h('div', { class: 'opts', role: 'radiogroup', 'aria-label': 'Answer options' });
      it.options.forEach(function (o, i) {
        var inp = h('input', { type: 'radio', name: 'opt', value: o, id: 'o' + i, onchange: function () { chosen = o; ready(); } });
        wrap.appendChild(h('label', { class: 'opt', for: 'o' + i, 'data-opt': o }, inp, h('span', { class: 'mark' }), h('span', null, o)));
      });
      area.appendChild(wrap);
      answerGetter = function () { return chosen; };
      canSubmit = function () { return chosen !== null; };
    } else if (it.kind === 'gap') {
      var parts = it.q.split('___');
      parts.forEach(function (p, i) {
        qEl.appendChild(document.createTextNode(p));
        if (i < parts.length - 1) {
          var inp = h('input', { type: 'text', class: 'blank', autocomplete: 'off', autocapitalize: 'off', spellcheck: 'false', 'aria-label': 'Answer ' + (i + 1), oninput: ready });
          inputs.push(inp); qEl.appendChild(inp);
        }
      });
      answerGetter = function () { return inputs.map(function (i) { return i.value; }); };
      canSubmit = function () { return inputs.every(function (i) { return i.value.trim() !== ''; }); };
    } else if (it.kind === 'text') {
      qEl.textContent = it.q;
      var t = h('input', { type: 'text', class: 'type-in', autocomplete: 'off', autocapitalize: 'sentences', spellcheck: 'false', placeholder: 'Type your answer', 'aria-label': 'Your answer', oninput: ready });
      inputs.push(t); area.appendChild(t);
      answerGetter = function () { return t.value; };
      canSubmit = function () { return t.value.trim() !== ''; };
    } else {
      qEl.textContent = it.q;
      var ta = h('textarea', { class: 'write', placeholder: 'Write your answer here', 'aria-label': 'Your answer', spellcheck: 'true', oninput: ready });
      inputs.push(ta); area.appendChild(ta);
      area.appendChild(h('p', { class: 'small muted', style: 'margin-top:-8px' }, 'We check the key grammar in your sentence. A model answer is shown after.'));
      answerGetter = function () { return ta.value; };
      canSubmit = function () { return ta.value.trim().split(/\s+/).length >= 2; };
    }

    inputs.forEach(function (i) {
      if (i.tagName === 'INPUT') i.addEventListener('keydown', function (e) { if (e.key === 'Enter' && canSubmit()) { e.preventDefault(); doSubmit(); } });
    });

    var feedback = h('div', { 'aria-live': 'polite' });
    var taskStart = Date.now();

    function doSubmit() {
      if (!canSubmit() || submit.disabled) return;
      submit.disabled = true;
      var ans = answerGetter();
      api('session/answer', { session_id: ses.id, item_id: it.id, answer: ans, time_ms: Date.now() - taskStart }).then(function (r) {
        S.session = r.session; S.last = r; state.todaySeconds = state.todaySeconds;
        lock(); showFeedback(r, ans);
        if (r.done) S.summary = r.summary;
      }).catch(function (e) {
        submit.disabled = false;
        if (e.status === 409) { api('session/resume').then(function (x) { if (x.resume) { state.sess = newSess(x.resume.session, x.resume.item); viewSession(); } else { location.hash = '#/home'; } }); return; }
        feedback.replaceChildren(h('div', { class: 'err', role: 'alert' }, e.message));
      });
    }
    submit.addEventListener('click', doSubmit);

    function lock() {
      inputs.forEach(function (i) { i.disabled = true; i.readOnly = true; });
      area.querySelectorAll('input[type=radio]').forEach(function (r) { r.disabled = true; });
      submit.remove();
    }

    function showFeedback(r, ans) {
      var res = r.result;
      if (it.kind === 'mcq') {
        var wrap = area.querySelector('.opts'); wrap.classList.add('locked');
        wrap.querySelectorAll('.opt').forEach(function (l) {
          var o = l.getAttribute('data-opt');
          if (o === res.show) l.classList.add('right'); else if (o === chosen) l.classList.add('wrong');
        });
      }
      var good = res.correct;
      var cheers = ['Correct!', 'Well done!', 'Yes, that is right!', 'Good job!', 'Exactly right!'];
      var fb = h('div', { class: 'feedback ' + (good ? 'good' : 'bad') });
      fb.appendChild(h('h3', null, icon(good ? 'check' : 'cross'), good ? cheers[Math.floor(Math.random() * cheers.length)] : (it.kind === 'write' ? 'Almost – check these points' : 'Not quite'),
        res.xp ? h('span', { class: 'pill ' + (good ? 'good' : 'pink'), style: 'margin-left:auto' }, '+' + res.xp + ' XP') : null));

      if (!good && it.kind === 'mcq' && chosen) fb.appendChild(h('p', null, h('b', null, 'You chose: '), chosen));
      if (!good && (it.kind === 'gap' || it.kind === 'text')) {
        var given = Array.isArray(ans) ? ans.join(' / ') : ans;
        fb.appendChild(h('p', null, h('b', null, 'You wrote: '), given));
      }
      if (res.specific) fb.appendChild(h('p', null, h('b', null, 'Tip: '), res.specific));
      if (it.kind === 'write') {
        fb.appendChild(h('div', { class: 'ans' }, h('b', null, 'Model answer: '), res.show));
        fb.appendChild(h('p', null, res.why));
      } else {
        if (!good || it.kind !== 'mcq') fb.appendChild(h('div', { class: 'ans' }, h('b', null, good ? 'Answer: ' : 'Correct answer: '), res.show));
        fb.appendChild(h('p', null, h('b', null, 'Why: '), res.why));
      }
      fb.appendChild(ruleDetails(res.skill, !good));

      var nextText = r.done ? (ses.mode === 'placement' ? 'See my result' : 'See my results') : 'Next task';
      var nextBtn = h('button', { class: 'btn', onclick: function () { next(r); } }, nextText, icon('arrow'));
      var adaptNote = null;
      if (!r.done && ses.mode === 'practice' && ses.phase !== 'diagnostic' && res.adapt !== 'same') {
        adaptNote = h('span', { class: 'adapt' }, icon(res.adapt === 'harder' ? 'up' : 'down'), res.adapt === 'harder' ? 'Next: a bit harder' : 'Next: a bit easier, to build confidence');
      } else if (!r.done && ses.mode === 'practice' && ses.phase === 'diagnostic') {
        adaptNote = h('span', { class: 'adapt' }, 'Quick check: ' + Math.min(3, ses.n) + ' of 3');
      }
      fb.appendChild(h('div', { class: 'nextrow' }, adaptNote || h('span'), nextBtn));
      feedback.replaceChildren(fb);
      nextBtn.focus();
      var prog = document.getElementById('prog');
      if (prog) prog.style.width = Math.round(100 * ses.n / ses.length) + '%';
    }

    function next(r) {
      if (r.done) { state.sess = null; state.lastSummary = r.summary; go('#/summary'); return; }
      state.sess = newSess(r.session, r.next);
      viewSession();
    }

    var phaseLabel = ses.mode === 'placement' ? 'Placement test' : (ses.phase === 'diagnostic' ? 'Quick check' : 'Practice');
    var done = ses.n;
    show(h('div', { class: 'sess' },
      h('div', { class: 'sess-top' }, h('span', null, phaseLabel + ' · Task ' + (done + 1) + ' of ' + ses.length),
        h('button', { class: 'linkbtn small', onclick: function () { stopSession(ses); } }, 'Stop')),
      h('div', { class: 'progress', role: 'progressbar', 'aria-valuemin': '0', 'aria-valuemax': String(ses.length), 'aria-valuenow': String(done) }, h('i', { id: 'prog', style: 'width:' + Math.round(100 * done / ses.length) + '%' })),
      h('div', { class: 'card task' },
        h('h1', { class: 'sr' }, 'Task ' + (done + 1)),
        h('div', { class: 'meta' }, h('span', { class: 'pill dark' }, it.skill_label), levelPill(it.level),
          h('span', { class: 'pill', title: state.meta.bloom[String(it.bloom)].desc }, bloomName(it.bloom), ' ', bloomDots(it.bloom))),
        qEl, area, h('div', { class: 'row' }, submit), feedback)));
    var first = inputs[0] || (area.querySelector('input[type=radio]'));
    if (first && it.kind !== 'mcq') first.focus();
  }

  function stopSession(ses) {
    var m = UI.modal(h('div', null, h('h2', null, 'Stop now?'), h('p', null, 'Your answers so far are saved. You can see a short result for the tasks you did.'),
      h('div', { class: 'row' }, h('button', { class: 'btn', id: 'yes' }, 'Stop and see result'), h('button', { class: 'btn ghost', id: 'no' }, 'Keep going'))));
    m.el.querySelector('#no').onclick = m.close;
    m.el.querySelector('#yes').onclick = function () {
      m.close();
      api('session/quit', { session_id: ses.id }).then(function (r) {
        state.sess = null; state.lastSummary = r.summary; go('#/summary');
      }).catch(fail);
    };
  }

  function ruleDetails(skillId, open) {
    var s = skillById(skillId); if (!s) return h('span');
    var r = s.rule;
    return h('details', { class: 'rule', open: false }, h('summary', null, 'Rule reminder: ' + s.label), ruleCard(s));
  }

  function ruleCard(s) {
    var r = s.rule;
    return h('div', { class: 'rulecard' },
      h('b', { style: 'color:var(--text)' }, 'How to make it'), h('ul', null, r.form.map(function (x) { return h('li', null, x); })),
      h('b', { style: 'color:var(--text)' }, 'When we use it'), h('ul', null, r.use.map(function (x) { return h('li', null, x); })),
      h('p', { class: 'small' }, h('b', null, 'Signal words: '), r.signals),
      h('div', { class: 'ex' }, h('b', null, 'Example: '), r.example));
  }

  // ───────── summary ─────────
  function viewSummary() {
    var s = state.lastSummary;
    if (!s) { location.hash = '#/home'; return; }
    setTimeout(function () { if (location.hash === '#/summary') guestInvite(false); }, 700);
    if (s.mode === 'placement') return summaryPlacement(s);
    var nodes = [];
    nodes.push(h('div', { class: 'card', style: 'margin-bottom:16px' },
      h('div', { class: 'label' }, 'Practice finished'), h('h1', null, s.accuracy >= 80 ? 'Great work!' : (s.accuracy >= 50 ? 'Good effort!' : 'Keep going – this is how you learn.')),
      h('div', { class: 'grid g3' },
        h('div', null, h('div', { class: 'big' }, s.correct + '/' + s.n), h('div', { class: 'muted small' }, 'correct')),
        h('div', null, h('div', { class: 'big' }, '+' + s.xp), h('div', { class: 'muted small' }, 'XP points')),
        h('div', null, h('div', { class: 'big' }, s.accuracy + '%'), h('div', { class: 'muted small' }, 'accuracy')))));
    nodes.push(h('div', { class: 'grid g2', style: 'margin-bottom:16px' },
      h('div', { class: 'card' }, h('h2', null, 'By tense'), h('ul', { class: 'clean' }, s.by_skill.map(function (k) {
        return h('li', { style: 'margin-bottom:12px' }, h('div', { class: 'row between' }, h('b', { style: 'color:var(--text)' }, k.label), h('span', { class: 'pill dark' }, '≈ ' + k.level_est)),
          h('div', { class: 'meter gold', style: 'margin:6px 0 3px' }, h('i', { style: 'width:' + pct(k.correct, k.n) + '%' })), h('span', { class: 'small muted' }, k.correct + ' of ' + k.n + ' correct'));
      }))),
      h('div', { class: 'card' }, h('h2', null, 'By type of thinking'), bloomBars(s.by_bloom))));
    var steps = s.next || [];
    nodes.push(h('div', { class: 'card', style: 'margin-bottom:16px' }, h('h2', null, 'What next?'),
      h('ul', { class: 'clean' }, steps.length ? steps.map(function (n) {
        return h('li', { style: 'margin-bottom:10px' }, h('div', { class: 'row between' }, h('span', null, n.text),
          n.type === 'review' ? h('button', { class: 'btn ghost small', onclick: function () { rulesModal(n.skill); } }, 'Rule card')
            : h('button', { class: 'btn small', onclick: function () { state.prefill = { skills: state.lastSkills || s.by_skill.map(function (k) { return k.id; }), level: n.level }; location.hash = '#/practice'; } }, 'Try ' + n.level)));
      }) : h('li', null, 'Do another round to build your streak and see your level move.'))));
    nodes.push(h('div', { class: 'row' }, h('button', { class: 'btn', onclick: function () { state.prefill = { skills: s.by_skill.map(function (k) { return k.id; }), level: s.level }; location.hash = '#/practice'; } }, 'Practise again'), h('a', { class: 'btn ghost', href: '#/home' }, 'Home')));
    show(h('div', { class: 'sess', style: 'max-width:860px' }, nodes));
  }

  function summaryPlacement(s) { show(h('div', { class: 'sess', style: 'max-width:860px' }, placementReport(s, true))); }

  function placementReport(s, fresh) {
    var nodes = [];
    nodes.push(h('div', { class: 'card', style: 'margin-bottom:16px' },
      h('div', { class: 'label' }, fresh ? 'Placement test finished' : 'Placement result'), h('h1', null, 'Your level is about ', h('span', { class: 'levelbadge' }, s.overall_level)),
      h('p', null, s.correct + ' of ' + s.n + ' correct. This is an estimate to help you start in the right place, not an exam grade.'),
      s.overall_level === 'B1.2' ? h('p', { class: 'small muted' }, 'You are at the top of what is available now. B2 levels are coming soon.') : null,
      s.overall_level === 'A2.1' ? h('p', { class: 'small muted' }, 'A2.1 is the first level in this app. If most tasks felt too hard, that is fine: start with the tenses below and ask your teacher about easier material.') : null));
    nodes.push(h('div', { class: 'card', style: 'margin-bottom:16px' }, h('h2', null, 'Start with these 3 tenses'),
      h('ol', { class: 'gaps', style: 'padding-left:20px' }, s.gaps.map(function (g) {
        return h('li', null, h('div', { class: 'row between' }, h('div', null, h('b', { style: 'color:var(--text)' }, g.label), h('div', { class: 'small muted' }, g.why)),
          h('button', { class: 'btn small', onclick: function () { state.prefill = { skills: [g.id], level: g.level }; location.hash = '#/practice'; } }, 'Practise ' + g.level)));
      })),
      h('div', { class: 'row', style: 'margin-top:8px' }, h('button', { class: 'btn', onclick: function () { state.prefill = { skills: s.gaps.map(function (g) { return g.id; }), level: s.overall_level }; location.hash = '#/practice'; } }, 'Practise all 3 together'),
        h('a', { class: 'btn ghost', href: '#/practice' }, 'Choose my own'))));
    nodes.push(h('div', { class: 'grid g2' },
      h('div', { class: 'card' }, h('h2', null, 'All tested tenses'), h('ul', { class: 'clean' }, s.by_skill.map(function (k) {
        return h('li', { class: 'lvrow' }, h('span', null, k.label), h('span', { class: 'nowrap' }, h('span', { class: 'small muted' }, k.correct + '/' + k.n + ' '), h('span', { class: 'pill dark' }, '≈ ' + k.level_est)));
      })), (s.untested && s.untested.length) ? h('p', { class: 'small muted', style: 'margin-top:10px' }, 'Not tested because they looked too advanced for now: ' + s.untested.map(function (u) { return u.label; }).join(', ') + '.') : null),
      h('div', { class: 'card' }, h('h2', null, 'By type of thinking'), bloomBars(s.by_bloom), h('p', { class: 'small muted', style: 'margin-top:12px' }, 'The test uses the first four levels (Remember to Analyse). Practice adds Evaluate and Create tasks.'))));
    nodes.push(h('div', { class: 'row', style: 'margin-top:16px' }, h('a', { class: 'btn ghost', href: '#/home' }, 'Home')));
    return nodes;
  }

  function showPlacementReport(rep) { state.lastSummary = rep; show(h('div', { class: 'sess', style: 'max-width:860px' }, placementReport(rep, false))); }

  // ───────── rules ─────────
  function viewRules() {
    show(h('div', null, h('div', { class: 'hello' }, h('div', null, h('div', { class: 'label' }, 'Reference'), h('h1', { style: 'margin:0' }, 'Rule cards'))),
      h('div', { class: 'grid g2' }, state.meta.skills.map(function (s) {
        return h('div', { class: 'card' }, h('div', { class: 'row between' }, h('h3', { style: 'margin:0' }, s.label), h('span', { class: 'pill' }, VOICE_LABEL[s.voice])), ruleCard(s));
      }))));
  }
  function rulesModal(id) {
    var s = skillById(id);
    var m = UI.modal(h('div', null, h('h2', null, s.label), ruleCard(s), h('div', { class: 'row', style: 'margin-top:14px' }, h('button', { class: 'btn', id: 'c' }, 'Close'))));
    m.el.querySelector('#c').onclick = m.close;
  }

  // ───────── leaderboard ─────────
  function viewLeaderboard() {
    var period = 'week';
    var holder = h('div');
    function load() {
      holder.replaceChildren(loading());
      api('leaderboard', undefined, { period: period }).then(function (r) {
        var rows = r.rows;
        var list = rows.length ? h('div', { class: 'card', style: 'padding:0;overflow:hidden' }, rows.map(function (x) {
          return h('div', { class: 'lb-row' + (x.me ? ' me' : '') }, h('div', { class: 'lb-rank' + (x.rank <= 3 ? ' top' : '') }, String(x.rank)),
            h('div', { class: 'lb-name' }, x.nickname, x.me ? h('span', { class: 'pill', style: 'margin-left:8px' }, 'You') : null),
            h('div', { class: 'small muted num' }, x.minutes + ' min'), h('div', { class: 'lb-xp' }, x.xp + ' XP'));
        })) : h('div', { class: 'card empty' }, h('p', null, period === 'week' ? 'No points yet this week. Be the first!' : 'No points yet.'), h('a', { class: 'btn', href: '#/practice' }, 'Practise now'));
        holder.replaceChildren(
          period === 'week' ? h('p', { class: 'small muted' }, 'Weeks start on Monday. Points come from correct answers, with more points for higher thinking levels.') : null,
          list,
          (r.me && r.me.rank > 20) ? h('div', { class: 'card pad-s', style: 'margin-top:12px' }, 'Your rank: ', h('b', { style: 'color:var(--text)' }, '#' + r.me.rank), ' · ' + r.me.xp + ' XP') : null,
          r.guest ? h('div', { class: 'card pad-s', style: 'margin-top:12px;border-color:var(--gold)' }, h('b', { style: 'color:var(--text)' }, 'Guests are not on the leaderboard.'), ' Create a free account to join it and keep your results. ',
            state.config.register_url ? h('a', { href: state.config.register_url }, 'Create account') : null)
          : (r.hidden ? h('p', { class: 'small muted', style: 'margin-top:12px' }, state.user.role === 'teacher' ? 'Teachers are not shown on the leaderboard.' : 'You are hidden from the leaderboard. You can change this in your profile.') : null));
      }).catch(fail);
    }
    var tabs = h('div', { class: 'tabs', role: 'tablist', style: 'max-width:320px' },
      ['week', 'all'].map(function (p) {
        return h('button', { role: 'tab', 'aria-selected': String(p === period), onclick: function () { period = p; tabs.querySelectorAll('button').forEach(function (b, i) { b.setAttribute('aria-selected', String(['week', 'all'][i] === period)); }); load(); } }, p === 'week' ? 'This week' : 'All time');
      }));
    show(h('div', { class: 'sess', style: 'max-width:760px' }, h('div', { class: 'hello' }, h('div', null, h('div', { class: 'label' }, 'Leaderboard'), h('h1', { style: 'margin:0' }, 'Top learners'))), tabs, holder));
    load();
  }

  // ───────── profile ─────────
  function viewProfile() {
    var u = state.user, guest = u.guest;
    var msg = h('div');
    var nick = h('input', { type: 'text', id: 'pn', value: u.nickname, maxlength: '30', autocapitalize: 'off', spellcheck: 'false' });
    var board = h('input', { type: 'checkbox', id: 'pb', checked: u.show_on_board });
    var profile = h('form', { onsubmit: function (e) {
      e.preventDefault(); msg.replaceChildren();
      api('account/profile', { nickname: nick.value, show_on_board: board.checked }).then(function (r) { state.user = r.user; msg.replaceChildren(h('div', { class: 'ok', role: 'status' }, 'Saved.')); }).catch(function (er) { msg.replaceChildren(h('div', { class: 'err', role: 'alert' }, er.message)); });
    } },
      h('div', { class: 'field' }, h('label', { for: 'pn' }, guest ? 'Nickname' : 'Name shown to others'), nick,
        guest ? null : h('span', { class: 'hint' }, 'On the leaderboard and to your teacher. A real name or a nickname.')),
      guest ? null : h('div', { class: 'field' }, h('label', { style: 'display:flex;gap:10px;align-items:center;font-weight:500' }, board, 'Show me on the leaderboard')),
      msg, h('button', { class: 'btn', type: 'submit' }, 'Save'));

    var cards = [];
    if (guest) cards.push(guestBanner());
    cards.push(h('div', { class: 'card' }, h('h2', null, 'Profile'), profile));
    if (!guest) cards.push(h('div', { class: 'card' }, h('h2', null, 'Sign-in'), h('p', null, 'You signed in with your englishfever.com account. Manage your password on the website.')));
    cards.push(h('div', { class: 'card' }, h('h2', null, 'Your data'),
      h('p', null, guest ? 'As a guest we keep only your nickname, your answers and the time you practise. Guest data is deleted after 60 days without a visit.'
        : 'We keep your name, your answers, your scores and the time you practise. Your teacher can see them. We never share them with anyone else.'),
      h('div', { class: 'row' },
        h('button', { class: 'btn ghost small', onclick: function () {
          api('account/export').then(function (d) { var a = h('a', { href: URL.createObjectURL(new Blob([JSON.stringify(d, null, 2)], { type: 'application/json' })), download: 'my-practice-data.json' }); document.body.appendChild(a); a.click(); a.remove(); }).catch(fail);
        } }, 'Download my data'),
        h('button', { class: 'btn ghost small', onclick: deleteAccount }, 'Delete my results'),
        h('a', { href: state.config.privacy_url, target: '_blank', rel: 'noopener', class: 'small' }, 'Privacy policy'))));
    cards.push(h('div', null, h('button', { class: 'btn dark', onclick: function () {
      api('logout', {}).then(function () { state.user = null; state.dash = null; stopHeartbeat(); go('#/'); });
    } }, icon('logout'), guest ? 'Leave guest session' : 'Sign out')));
    show(h('div', { class: 'sess', style: 'max-width:620px' }, h('div', { class: 'hello' }, h('div', null, h('div', { class: 'label' }, guest ? 'Guest' : 'Account'), h('h1', { style: 'margin:0' }, u.nickname))), h('div', { class: 'grid' }, cards)));
  }

  function deleteAccount() {
    var em = h('div');
    var m = UI.modal(h('div', null, h('h2', null, 'Delete your results?'), h('p', null, 'This deletes your results, history and profile in the practice app. It cannot be undone. Your englishfever.com account is not affected.'), em,
      h('div', { class: 'row', style: 'margin-top:14px' }, h('button', { class: 'btn', id: 'del' }, 'Delete'), h('button', { class: 'btn ghost', id: 'cancel' }, 'Cancel'))));
    m.el.querySelector('#cancel').onclick = m.close;
    m.el.querySelector('#del').onclick = function () {
      api('account/delete', { confirm: true }).then(function () { m.close(); state.user = null; stopHeartbeat(); go('#/'); UI.toast('Your results were deleted.'); }).catch(function (e) { em.replaceChildren(h('div', { class: 'err', role: 'alert' }, e.message)); });
    };
  }

  // ───────── first visit with an englishfever.com account ─────────
  function viewNickname() {
    renderChrome();
    var msg = h('div');
    var nick = h('input', { type: 'text', id: 'fn', value: state.user.nickname, maxlength: '30', autocapitalize: 'off', spellcheck: 'false', required: true });
    var board = h('input', { type: 'checkbox', id: 'fb', checked: true });
    show(h('div', { class: 'card', style: 'max-width:480px;margin:20px auto' }, h('div', { class: 'label' }, 'Welcome'), h('h1', null, 'How should we show your name?'),
      h('p', null, 'Other learners and your teacher see this name. Keep your real name or choose a nickname.'),
      h('form', { onsubmit: function (e) {
        e.preventDefault();
        api('account/profile', { nickname: nick.value, show_on_board: board.checked }).then(function (r) { state.user = r.user; go('#/home'); }).catch(function (er) { msg.replaceChildren(h('div', { class: 'err', role: 'alert' }, er.message)); });
      } }, h('div', { class: 'field' }, h('label', { for: 'fn' }, 'Name'), nick),
        h('div', { class: 'field' }, h('label', { style: 'display:flex;gap:10px;align-items:center;font-weight:500' }, board, 'Show me on the leaderboard')), msg,
        h('button', { class: 'btn block', type: 'submit' }, 'Continue'))));
  }

  // ───────── teacher ─────────
  function viewTeacher() {
    api('teacher/students').then(function (r) {
      var all = r.students, sortKey = 'last_seen', dir = -1, q = '';
      var weekActive = all.filter(function (s) { return s.week_answers > 0; }).length;
      var withAcc = all.filter(function (s) { return s.accuracy !== null; });
      var avg = withAcc.length ? Math.round(withAcc.reduce(function (a, s) { return a + s.accuracy; }, 0) / withAcc.length) : null;
      var tbody = h('tbody');
      var cols = [
        ['nickname', 'Student'], ['level_est', 'Level'], ['last_seen', 'Last active'], ['week_minutes', 'Week (min)', 'r'], ['week_answers', 'Week tasks', 'r'],
        ['total_minutes', 'Total (min)', 'r'], ['xp', 'XP', 'r'], ['accuracy', 'Correct', 'r'], ['streak', 'Streak', 'r'],
      ];
      var thead = h('thead', null, h('tr', null, cols.map(function (c) {
        return h('th', { class: c[2] || '', 'data-k': c[0], tabindex: '0', role: 'columnheader', onclick: function () { sortBy(c[0]); }, onkeydown: function (e) { if (e.key === 'Enter') sortBy(c[0]); } }, c[1]);
      })));
      function sortBy(k) { if (sortKey === k) dir = -dir; else { sortKey = k; dir = (k === 'nickname' || k === 'level_est') ? 1 : -1; } draw(); }
      function draw() {
        thead.querySelectorAll('th').forEach(function (t) { if (t.getAttribute('data-k') === sortKey) t.setAttribute('aria-sort', dir > 0 ? 'ascending' : 'descending'); else t.removeAttribute('aria-sort'); });
        var rows = all.filter(function (s) { return !q || (s.nickname + ' ' + (s.full_name || '')).toLowerCase().indexOf(q) >= 0; });
        rows.sort(function (a, b) {
          var x = a[sortKey], y = b[sortKey];
          if (x === null || x === undefined) x = (typeof y === 'string') ? '' : -1;
          if (y === null || y === undefined) y = (typeof x === 'string') ? '' : -1;
          if (typeof x === 'string') return dir * x.localeCompare(y);
          return dir * (x - y);
        });
        tbody.replaceChildren.apply(tbody, rows.length ? rows.map(function (s) {
          return h('tr', null,
            h('td', { class: 'name' }, h('a', { href: '#/teacher/student/' + s.id }, s.nickname), s.provider === 'guest' ? h('span', { class: 'pill', style: 'margin-left:8px' }, 'guest') : null, s.full_name && s.full_name !== s.nickname ? h('div', { class: 'small muted' }, s.full_name) : null),
            h('td', null, s.level_est ? h('span', { class: 'pill dark' }, '≈ ' + s.level_est) : h('span', { class: 'muted' }, '–')),
            h('td', null, UI.fmtAgo(s.last_seen)), h('td', { class: 'r num' }, String(s.week_minutes)), h('td', { class: 'r num' }, String(s.week_answers)),
            h('td', { class: 'r num' }, String(s.total_minutes)), h('td', { class: 'r num' }, String(s.xp)),
            h('td', { class: 'r num' }, s.accuracy === null ? '–' : s.accuracy + '%'), h('td', { class: 'r num' }, String(s.streak)));
        }) : [h('tr', null, h('td', { colspan: String(cols.length), class: 'empty' }, all.length ? 'No students match.' : 'No students yet. Share the practice link with your learners.'))]);
      }
      var search = h('input', { type: 'text', placeholder: 'Search students', 'aria-label': 'Search students', style: 'max-width:260px', oninput: function () { q = search.value.trim().toLowerCase(); draw(); } });
      draw();
      show(h('div', null,
        h('div', { class: 'hello' }, h('div', null, h('div', { class: 'label' }, 'Teacher'), h('h1', { style: 'margin:0' }, 'Students')),
          h('a', { class: 'btn ghost small', href: 'api.php?r=teacher/export', download: '' }, 'Export all answers (CSV)')),
        h('div', { class: 'grid g4', style: 'margin-bottom:16px' }, stat('users', all.filter(function (s) { return s.provider !== 'guest'; }).length, 'registered'), stat('user', all.filter(function (s) { return s.provider === 'guest'; }).length, 'guests'), stat('flame', weekActive, 'active this week'), stat('check', avg === null ? '–' : avg + '%', 'average correct')),
        h('div', { class: 'row', style: 'margin-bottom:12px' }, search),
        h('div', { class: 'tablewrap' }, h('table', null, thead, tbody))));
    }).catch(fail);
  }

  function viewTeacherStudent(id) {
    api('teacher/student', undefined, { id: id }).then(function (r) {
      var u = r.user, d = r.dashboard;
      var maxMin = Math.max.apply(null, r.days.map(function (x) { return x.minutes; }).concat([5]));
      var days = h('div', { class: 'bars', style: 'height:100px', role: 'img', 'aria-label': 'Minutes per day, last 30 days' }, r.days.map(function (x, i) {
        return h('div', { class: 'b', title: x.day + ': ' + x.minutes + ' min, ' + x.answers + ' tasks' }, h('div', { class: 'col' + (i === r.days.length - 1 ? ' today' : ''), style: 'max-width:14px;height:' + Math.max(3, Math.round(80 * x.minutes / maxMin)) + 'px' }));
      }));
      var skillRows = d.skills.filter(function (s) { return s.n > 0; }).map(function (s) {
        return h('tr', null, h('td', null, s.label), h('td', null, VOICE_LABEL[s.voice]), h('td', null, s.level_est ? h('span', { class: 'pill dark' }, '≈ ' + s.level_est) : h('span', { class: 'muted' }, 'few tasks')), h('td', { class: 'r num' }, String(s.n)), h('td', { class: 'r num' }, s.accuracy + '%'));
      });
      var rep = d.placement && d.placement.report;
      show(h('div', null,
        h('a', { href: '#/teacher', class: 'small' }, '← All students'),
        h('div', { class: 'hello', style: 'margin-top:8px' }, h('div', null, h('div', { class: 'label' }, 'Student'), h('h1', { style: 'margin:0' }, u.nickname), h('p', { class: 'muted small' }, (u.full_name ? u.full_name + ' · ' : '') + (u.provider === 'guest' ? 'guest (not registered)' : 'englishfever.com account') + ' · joined ' + UI.fmtAgo(u.joined) + ' · last active ' + UI.fmtAgo(u.last_seen)))),
        h('div', { class: 'grid g4', style: 'margin-bottom:16px' }, stat('clock', UI.fmtDuration(d.totals.seconds), 'time practised'), stat('check', d.totals.accuracy === null ? '–' : d.totals.accuracy + '%', 'correct (' + d.totals.answers + ' tasks)'), stat('flame', d.streak.current + ' / ' + d.streak.best, 'streak (best)'), stat('bolt', d.totals.xp, 'XP')),
        h('div', { class: 'grid g2', style: 'margin-bottom:16px' },
          h('div', { class: 'card' }, h('h2', null, 'Last 30 days'), days, h('p', { class: 'small muted', style: 'margin:8px 0 0' }, 'Each bar is one day (minutes practised).')),
          h('div', { class: 'card' }, h('h2', null, 'Thinking levels'), bloomBars(d.bloom))),
        rep ? h('div', { class: 'card', style: 'margin-bottom:16px' }, h('h2', null, 'Placement test'), h('p', null, 'Level: ', h('span', { class: 'levelbadge', style: 'font-size:1.1rem;padding:3px 12px' }, rep.overall_level), ' · ' + UI.fmtAgo(d.placement.at) + ' · ' + rep.correct + '/' + rep.n + ' correct'),
          h('p', { class: 'small' }, h('b', null, 'Gaps: '), rep.gaps.map(function (g) { return g.label + ' (' + g.level + ')'; }).join(', '))) : null,
        h('div', { class: 'card', style: 'margin-bottom:16px;padding:0;overflow:hidden' }, h('h2', { style: 'padding:18px 18px 0' }, 'Tenses'),
          skillRows.length ? h('div', { class: 'tablewrap', style: 'border:0;border-radius:0' }, h('table', null, h('thead', null, h('tr', null, ['Tense', 'Voice', 'Level', 'Tasks', 'Correct'].map(function (t, i) { return h('th', { class: i > 2 ? 'r' : '' }, t); }))), h('tbody', null, skillRows))) : h('p', { class: 'empty' }, 'No tasks done yet.')),
        h('div', { class: 'card', style: 'padding:0;overflow:hidden' }, h('h2', { style: 'padding:18px 18px 0' }, 'Recent answers'),
          r.recent.length ? h('div', { class: 'tablewrap', style: 'border:0;border-radius:0' }, h('table', null, h('thead', null, h('tr', null, ['When', 'Task', 'Answer', '', 'Level', 'Thinking', 'Sec'].map(function (t) { return h('th', null, t); }))),
            h('tbody', null, r.recent.map(function (a) {
              return h('tr', null, h('td', { class: 'small' }, UI.fmtDate(a.at)), h('td', { style: 'max-width:340px;overflow:hidden;text-overflow:ellipsis' }, a.q), h('td', { style: 'max-width:220px;overflow:hidden;text-overflow:ellipsis' }, a.answer || ''),
                h('td', null, h('span', { class: 'pill ' + (a.correct ? 'good' : 'pink') }, a.correct ? '✓' : '✗')), h('td', null, a.level), h('td', null, bloomName(a.bloom)), h('td', { class: 'num' }, String(a.seconds)));
            })))) : h('p', { class: 'empty' }, 'No answers yet.'))));
    }).catch(fail);
  }

  boot();
})();
