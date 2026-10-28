// English Fever practice app (grammar A2.1 – C1). Single page, hash routes.
(function () {
  'use strict';
  var h = UI.h, icon = UI.icon, api = UI.api;
  var root = document.getElementById('app');
  var chrome = document.getElementById('chrome');
  var footer = document.getElementById('foot');

  var state = {
    config: null, meta: null, user: null, dash: null,
    todaySeconds: 0, streak: 0, sess: null, prefill: null, lastInteraction: Date.now(), reported: {},
  };

  // ───────── helpers ─────────
  function areaLabel(id) { var a = state.meta.areas.filter(function (x) { return x.id === id; })[0]; return a ? a.label : id; }
  /** Features the learning study can hide for a learner (state.user.cond, e.g. {streak: 'off'}). Everyone outside the study sees everything. */
  function feat(name) { return !(state.user && state.user.cond && state.user.cond[name] === 'off'); }
  /** Learners see A2, B1, B2, C1; the half-levels (A2.1, A2.2 ...) only steer the difficulty inside the app. */
  function lv(l) { return String(l === null || l === undefined ? '' : l).replace(/\.\d$/, ''); }
  function levelRange(s) { var a = lv(s.levels[0]), b = lv(s.levels[s.levels.length - 1]); return a === b ? a : a + '–' + b; }
  /** The englishfever.com student dashboard (config dashboard_url), or the website home page. */
  var PROMPT_SPLIT = /^((?:Choose|Make|Use|Rewrite|Complete|Ask|Give|Put|Change|Write|Turn|Report|Say|Correct|Fill|Match|Join|Finish|Answer|Decide|Find|Rephrase|Transform|Reorder|Order)[^:\n]{0,120}?):\s+([\s\S]*\p{L}[\s\S]*)$/u;
  // the main site: the configured address, else the root of the dashboard / registration address
  function mainSiteUrl() {
    var c = state.config || {};
    if (c.site_url) return c.site_url;
    var u = c.dashboard_url || c.register_url || '';
    try { return u ? new URL(u).origin + '/' : ''; } catch (e) { return ''; }
  }
  function dashboardUrl() { return (state.config && (state.config.dashboard_url || state.config.site_url)) || ''; }
  // ───── which topics are in reach ─────
  function levelIdx(l) { return state.meta.levels.indexOf(l); }
  /** The learner's level: the placement result, else the average of the topic estimates, else unknown (null). */
  function learnerLevel(d) {
    if (d && d.placement && d.placement.report && d.placement.report.overall_level) return d.placement.report.overall_level;
    var est = d ? d.skills.filter(function (s) { return s.level_est; }).map(function (s) { return levelIdx(s.level_est); }) : [];
    if (!est.length) return null;
    return state.meta.levels[Math.round(est.reduce(function (a, b) { return a + b; }, 0) / est.length)];
  }
  /** Topics whose tasks start more than two sub-levels above the learner (A2.1 while the level is unknown) wait behind a link. Topics already practised always show. */
  function inReach(s, d) { var l = learnerLevel(d); return s.n > 0 || levelIdx(s.levels[0]) <= (l ? levelIdx(l) : 0) + 2; }
  function showHigh() { try { return localStorage.getItem('ef_show_high') === '1'; } catch (e) { return false; } }
  function setShowHigh(v) { try { localStorage.setItem('ef_show_high', v ? '1' : '0'); } catch (e) {} }
  /** The level to practise a topic at: its own estimate, else the learner's level kept inside the levels the topic has. */
  function topicLevel(s, d) {
    if (s.level_est) return s.level_est;
    var l = learnerLevel(d);
    if (!l) return s.levels[0];
    return state.meta.levels[Math.max(levelIdx(s.levels[0]), Math.min(levelIdx(s.levels[s.levels.length - 1]), levelIdx(l)))];
  }
  /** One tap: a 10-question session in this topic. */
  function startTopic(btn, s, d) {
    btn.disabled = true;
    api('session/start', { mode: 'practice', skills: [s.id], levels: [topicLevel(s, d).slice(0, 2)], length: 10 }).then(function (r) {
      state.sess = newSess(r.session, r.item); location.hash = '#/session';
    }).catch(function (e) { btn.disabled = false; UI.toast(e.message); });
  }
  function openAreas() { try { return JSON.parse(localStorage.getItem('ef_areas') || '{}') || {}; } catch (e) { return {}; } }
  function rememberArea(id, open) { try { var m = openAreas(); m[id] = open; localStorage.setItem('ef_areas', JSON.stringify(m)); } catch (e) {} }
  function bloomName(n) { return state.meta.bloom[String(n)].name; }
  function bloomDots(n) {
    var d = h('span', { class: 'bloomdots', title: 'Thinking level ' + n + ' of 6: ' + bloomName(n) });
    for (var i = 1; i <= 6; i++) d.appendChild(h('i', { class: i <= n ? 'on' : '' }));
    return d;
  }
  function skillById(id) { return state.meta.skills.filter(function (s) { return s.id === id; })[0]; }
  function pct(c, n) { return n ? Math.round(100 * c / n) : 0; }
  function loading() { return h('div', { class: 'loading', role: 'status' }, h('div', { class: 'spin' }), h('span', { class: 'sr' }, 'Loading')); }
  function show(node) { if (window.DnD) DnD.clear(); root.replaceChildren(node); window.scrollTo(0, 0); var hd = node.querySelector && node.querySelector('h1'); if (hd) { hd.setAttribute('tabindex', '-1'); hd.focus({ preventScroll: true }); } }
  function fail(e) {
    if (e && e.status === 401 && state.user && state.user.role === 'teacher') {
      return show(h('div', { class: 'card', style: 'max-width:520px;margin:30px auto' }, h('h2', null, 'Please sign in again'), h('p', null, e.message),
        state.config.wp_login_url ? h('a', { class: 'btn', href: state.config.wp_login_url }, 'Sign in with englishfever.com') : null));
    }
    show(h('div', { class: 'card' }, h('h2', null, 'Something went wrong'), h('p', null, e.message || 'Please try again.'), h('a', { class: 'btn', href: '#/home' }, 'Back to home')));
  }
  function levelPill(l) { return h('span', { class: 'pill' }, lv(l)); }

  // ───────── install on the phone (home screen) ─────────
  var deferredInstall = null;
  window.addEventListener('beforeinstallprompt', function (e) { e.preventDefault(); deferredInstall = e; });
  window.addEventListener('appinstalled', function () { deferredInstall = null; var c = document.getElementById('install-card'); if (c) c.remove(); });

  function isStandalone() { return (window.matchMedia && window.matchMedia('(display-mode: standalone)').matches) || window.navigator.standalone === true; }
  function isIos() { return /iphone|ipad|ipod/i.test(navigator.userAgent) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1); }
  function isPhoneLike() { return (window.matchMedia && window.matchMedia('(max-width: 900px)').matches) || isIos() || /android/i.test(navigator.userAgent); }

  /**
   * A short card about putting the app on the home screen (phones) or installing it (computers whose browser offers a real install button).
   * A computer without an install button gets nothing: there is no honest one-line instruction that fits every browser.
   */
  function installCard(always) {
    var phone = isPhoneLike();
    if (isStandalone() || (!always && !phone)) return null;
    if (!phone && !deferredInstall) return null;
    if (!always) { try { if (Date.now() - (+localStorage.getItem('ef_install_hidden') || 0) < 30 * 86400000) return null; } catch (e) {} }
    if (!always) { try { var vd = JSON.parse(localStorage.getItem('ef_visit_days') || '[]'), today = new Date().toDateString(); if (vd.indexOf(today) < 0) { vd.push(today); localStorage.setItem('ef_visit_days', JSON.stringify(vd.slice(-5))); } if (vd.length < 3) return null; } catch (e) {} }   // only from the third day of use: a first visit has enough to look at
    var how;
    if (deferredInstall) {
      how = h('button', { class: 'btn small', onclick: function () {
        deferredInstall.prompt(); deferredInstall.userChoice.then(function () { deferredInstall = null; var c = document.getElementById('install-card'); if (c) c.remove(); });
      } }, 'Install the app');
    } else if (isIos()) {
      how = h('span', { class: 'small' }, 'In Safari tap ', h('b', null, 'Share'), ' (the square with an arrow), then ', h('b', null, 'Add to Home Screen'), '.');
    } else if (/android/i.test(navigator.userAgent)) {
      how = h('span', { class: 'small' }, 'On your phone, open the browser menu (⋮) and choose ', h('b', null, 'Install app'), ' or ', h('b', null, 'Add to Home screen'), '.');
    } else {
      return null;
    }
    return h('div', { id: 'install-card', class: 'card pad-s row between', style: 'margin-bottom:16px' },
      h('div', null, h('b', { style: 'color:var(--text)' }, phone ? 'Add to your phone’s home screen' : 'Install the app on this computer'), h('div', { style: 'margin-top:6px' }, how)),
      always ? null : h('button', { class: 'linkbtn small', onclick: function () { try { localStorage.setItem('ef_install_hidden', String(Date.now())); } catch (e) {} var c = document.getElementById('install-card'); if (c) c.remove(); } }, 'Not now'));
  }

  // ───────── registering on the website ─────────
  // Registration needs an email confirmation, which can take a while. The app remembers the click so a returning
  // guest sees "Sign in" instead of the sign-up invitation.
  function regPending() { try { return Date.now() - (+localStorage.getItem('ef_reg') || 0) < 7 * 86400000; } catch (e) { return false; } }
  function registerLink(cls, label) {
    return h('a', { class: cls, href: 'register.php', onclick: function () { try { localStorage.setItem('ef_reg', String(Date.now())); } catch (e) {} } }, label);
  }

  // ───────── boot ─────────
  function boot() {
    if ('serviceWorker' in navigator) navigator.serviceWorker.register('sw.js').catch(function () {});
    Promise.all([api('config'), api('meta'), api('me')]).then(function (r) {
      state.config = r[0]; state.meta = r[1]; state.user = r[2].user; state.welcome = r[2].welcome || null;
      footer.replaceChildren(
        h('div', null, state.config.site_url ? h('span', null, h('a', { href: state.config.site_url }, '← englishfever.com'), ' · ') : null, h('a', { href: state.config.privacy_url, target: '_blank', rel: 'noopener' }, 'Privacy policy'), ' · ',
          state.config.contact_email ? h('a', { href: 'mailto:' + state.config.contact_email }, state.config.contact_email) : null),
        h('div', { class: 'small', style: 'margin-top:4px;opacity:.7' }, 'Version ' + (state.config.version || 'dev')));
      if (state.user) startHeartbeat();
      if (state.user && !state.user.guest) { try { localStorage.removeItem('ef_reg'); } catch (e) {} }
      window.addEventListener('hashchange', route);
      ['pointerdown', 'keydown', 'scroll', 'input'].forEach(function (ev) { window.addEventListener(ev, function () { state.lastInteraction = Date.now(); }, { passive: true }); });
      route();
    }).catch(function (e) {
      var offline = !navigator.onLine || /failed to fetch|network|load failed/i.test(e.message || '');
      root.replaceChildren(h('div', { class: 'card', style: 'max-width:480px;margin:40px auto;text-align:center' },
        h('h2', null, offline ? 'You are offline' : 'The app cannot start'),
        h('p', null, offline ? 'Practice needs an internet connection. Connect and try again.' : e.message),
        h('button', { class: 'btn', onclick: function () { location.reload(); } }, 'Try again')));
    });
  }

  // ───────── time tracking ─────────
  var hbTimer = null, hbLast = Date.now();
  function startHeartbeat() {
    if (hbTimer) return;
    hbLast = Date.now();
    hbTimer = setInterval(function () {
      var now = Date.now();
      var secs = Math.min(60, Math.round((now - hbLast) / 1000));
      hbLast = now;
      if (!state.user || document.visibilityState !== 'visible' || now - state.lastInteraction > 60000 || secs < 1) return;
      state.todaySeconds += secs;
      renderChips();
      api('heartbeat', { seconds: secs }).then(function (r) { if (r && r.pulse) { state.pulse = r.pulse; renderChips(); } }).catch(function () {});
    }, 30000);   // every 30 seconds: a third of the requests of before (October outage)
  }

  function stopHeartbeat() { if (hbTimer) { clearInterval(hbTimer); hbTimer = null; } state.todaySeconds = 0; state.streak = 0; clearHistories(); }

  // ───────── chrome (top bar and mobile tabs) ─────────
  function renderChrome(active) {
    if (!state.user) { chrome.replaceChildren(); return; }
    var teacher = state.user.role === 'teacher';
    var items = teacher
      ? [['#/teacher', 'Students', 'users'], ['#/reports', 'Reports', 'flag', state.user.reports_open], ['#/tasks', 'Add questions', 'book'], ['#/practice', 'Practice', 'target'], ['#/leaderboard', 'Leaderboard', 'trophy'], ['#/profile', 'Profile', 'user']]
      : [['#/home', 'Home', 'home'], ['#/practice', 'Practice', 'target'], ['#/leaderboard', 'Leaderboard', 'trophy'], ['#/profile', 'Profile', 'user']];
    if (!feat('leaderboard')) items = items.filter(function (i) { return i[0] !== '#/leaderboard'; });
    var nav = h('nav', { class: 'nav', 'aria-label': 'Main' }, items.map(function (i) {
      return h('a', { href: i[0], 'aria-current': active === i[0] ? 'page' : null }, i[1], i[3] ? h('span', { class: 'badge' }, String(i[3])) : null);
    }));
    var tabs = h('nav', { class: 'tabbar', 'aria-label': 'Main' }, items.map(function (i) {
      return h('a', { href: i[0], 'aria-current': active === i[0] ? 'page' : null }, i[2] === 'user' ? UI.avatar(state.user.avatar, state.user.nickname, 24) : icon(i[2]), i[1], i[3] ? h('span', { class: 'badge' }, String(i[3])) : null);
    }));
    var chips = h('div', { class: 'chips', id: 'chips' });
    var bar = h('header', { class: 'topbar' }, h('div', { class: 'topbar-in' },
      h('span', { class: 'brand' }, h('a', { class: 'dot', href: teacher ? '#/teacher' : '#/home', 'aria-label': 'Practice home' }), mainSiteUrl() ? h('a', { class: 'brand-site', href: mainSiteUrl(), target: '_blank', rel: 'noopener' }, 'English Fever') : h('a', { class: 'brand-site', href: teacher ? '#/teacher' : '#/home' }, 'English Fever'), h('a', { class: 'brand-sub', href: teacher ? '#/teacher' : '#/home' }, 'Practice')),
      state.config && state.config.beta ? betaPill() : null,
      nav, h('div', { class: 'spacer' }),
      dashboardUrl() ? h('a', { class: 'sitelink' + (state.user.guest ? ' sitelink-guest' : ''), target: '_blank', rel: 'noopener', href: state.user.guest ? (state.config.site_url || dashboardUrl()) : dashboardUrl() }, state.user.guest ? 'englishfever.com ↗' : 'My dashboard ↗') : null, chips,
      h('a', { class: 'avatar-link', href: '#/profile', 'aria-label': 'Your profile' }, UI.avatar(state.user.avatar, state.user.nickname, 32))));
    chrome.replaceChildren(bar, tabs);
    renderChips();
  }

  /** Company in the top bar, next to the streak: a green dot and a number = learning now; the people icon and a number = showed up today (while fewer than 3 are online). Never for fewer than 3. */
  function pulseChip() {
    var pu = state.pulse;
    if (!pu || !(pu.now >= 3 || pu.today >= 3)) return null;
    var live = pu.now >= 3, num = live ? pu.now : pu.today, tip = live ? 'learning now' : 'showed up today';
    return h('span', { class: 'chip-top chip-pulse', title: num + ' ' + tip, 'aria-label': num + ' ' + tip }, live ? h('i', { class: 'pulse-dot', 'aria-hidden': 'true' }) : icon('users'), String(num));
  }

  function renderChips() {
    var c = document.getElementById('chips');
    if (!c || !state.user || state.user.role === 'teacher') return;
    c.replaceChildren(
      state.user.guest ? h('button', { class: 'chip-top', style: 'background:none;cursor:pointer', title: 'Guest: results are not saved', onclick: function () { guestInvite(true); } }, 'Guest', h('span', { class: 'chip-more' }, ' · save progress')) : null,
      feat('streak') ? h('span', { class: 'chip-top', title: 'Daily streak' }, icon('flame'), String(state.streak), h('span', { class: 'chip-unit' }, ' day' + (state.streak === 1 ? '' : 's'))) : null,
      pulseChip(),
      h('span', { class: 'chip-top hide-m', title: 'Time practised today' }, icon('clock'), UI.fmtDuration(state.todaySeconds)));
  }

  function refreshDash() {
    return api('dashboard').then(function (d) {
      state.dash = d; state.todaySeconds = d.today.seconds; state.streak = d.streak.current; state.pulse = d.pulse || state.pulse;
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
      nickname: viewNickname, rules: viewRules, reports: viewReports, tasks: viewTasks, evidence: viewEvidence,
    }[name];
    if ((name.indexOf('teacher') === 0 || name === 'reports' || name === 'tasks' || name === 'evidence') && u.role !== 'teacher') { location.hash = '#/home'; return; }
    (v || viewHome)(parts);
  }

  // ───────── welcome / sign in ─────────
  function viewWelcome() {
    var cfg = state.config;
    var errBox = h('div');
    var nick = h('input', { type: 'text', id: 'nick', autocomplete: 'off', autocapitalize: 'words', spellcheck: 'false', maxlength: '30', placeholder: 'Your name (or a nickname)' });
    var shownAt = Date.now();
    var trap = h('input', { type: 'text', name: 'website', id: 'website', tabindex: '-1', autocomplete: 'off' });
    var guestForm = h('form', { novalidate: true, onsubmit: function (e) {
      e.preventDefault(); errBox.replaceChildren();
      var btn = guestForm.querySelector('button[type=submit]'); btn.disabled = true;
      // The server refuses forms sent within 1.2 s of opening (bots). A fast person just waits a moment, unseen.
      setTimeout(function () {
        api('guest', { nickname: nick.value, t: Date.now() - shownAt, website: trap.value }).then(function (r) {
          state.user = r.user; startHeartbeat(); go('#/home');
        }).catch(function (err) { btn.disabled = false; errBox.replaceChildren(h('div', { class: 'err', role: 'alert' }, err.message)); });
      }, Math.max(0, 1300 - (Date.now() - shownAt)));
    } },
      h('div', { class: 'field' }, h('label', { for: 'nick' }, 'Your name'), nick),
      h('div', { 'aria-hidden': 'true', style: 'position:absolute;left:-9999px;top:auto;width:1px;height:1px;overflow:hidden' }, h('label', { for: 'website' }, 'Leave this empty'), trap), // a trap for bots
      errBox,
      h('button', { class: 'btn block', type: 'submit' }, 'Continue as guest'),   // the main way in for a new person (teacher, 27 October)
      null);

    var card = [];
    card.push(h('h2', { style: 'text-align:center' }, cfg.sso ? 'Try it as a guest' : 'Start practising'), guestForm);
    if (cfg.sso) card.push(
      h('div', { class: 'or' }, 'or'),
      h('h2', { style: 'text-align:center' }, 'Registered at englishfever.com?'),
      h('a', { class: 'btn ghost block', href: cfg.wp_login_url }, icon('user'), 'Continue with my account'));
    if (cfg.register_url) card.push(h('p', { class: 'small', style: 'text-align:center;margin:16px 0 0' }, 'No account yet? ', registerLink('', 'Create a free account')));

    show(h('div', null,
      h('section', { class: 'hero' },
        h('div', { class: 'bar' }),
        h('h1', null, 'Practise English grammar. ', h('em', null, 'Know what to fix next.')),
        h('p', null, 'Short grammar questions for adult learners, A2 to C1. Clear feedback after every answer.'),
        cfg.beta ? h('p', { class: 'betaline' }, betaPill()) : null,
        h('div', { class: 'hero-feats' },   // what the app gives, as three icons (they looked like buttons as boxes; teacher, 27 October)
          h('span', null, h('i', null, icon('up')), 'Find your level'),
          h('span', null, h('i', null, icon('target')), 'Fix your mistakes'),
          h('span', null, h('i', null, icon('bolt')), 'Think, not guess'))),
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
      h('h2', null, 'Save your results with a free account'),
      h('p', null, 'Guest results are lost if you clear your browser or change device.'),
      h('div', { class: 'row' },
        cfg.register_url ? registerLink('btn', 'Create free account') : null,
        cfg.sso ? h('a', { class: cfg.register_url ? 'btn ghost' : 'btn', href: cfg.wp_login_url }, 'I already have an account') : null,
        h('button', { class: 'linkbtn', id: 'later' }, 'Not now'))));
    m.el.querySelector('#later').onclick = m.close;
  }

  /** My learning path: the course-book order and what this learner has mastered (docs/LEARNING-PATH.md).
      Shows the current step with a button, the next few steps and how many are done; "All steps" opens the whole path. */
  function pathCard() {
    var card = h('div', { class: 'card pathcard' }, h('div', { class: 'row between' }, h('h2', { style: 'margin:0' }, 'My learning path'), h('span', { class: 'small muted' }, '…')));
    var all = false;
    function start(el, st) {
      el.disabled = true;
      api('session/start', { mode: 'practice', skills: st.topics, levels: [st.level], length: (st.below && !st.answers) ? 6 : 10 }).then(function (r) {
        state.sess = newSess(r.session, r.item); location.hash = '#/session';
      }).catch(function (e) { el.disabled = false; UI.toast(e.message); });
    }
    // accuracy as a colour: pink → orange → yellow → yellow-green → green (hue -15° … 140°); grey = not tried yet
    function hue(p) { return 'hsl(' + ((-15 + 1.55 * p + 360) % 360) + ' 62% 46%)'; }
    function node(st) {
      var rec = st.id === path.current, has = st.pct !== null;
      var col = has ? hue(st.pct) : null;
      var sub = st.status === 'done' ? 'Mastered' : st.status === 'refresh' ? 'Time to refresh' : !has ? (st.below ? 'You may know it: a quick check' : 'Not tried yet')
        : plural(st.answers, 'answer', 'answers');
      var el = h('button', { type: 'button', class: 'pnode ' + st.status + (rec ? ' rec' : '') + (st.needs ? ' combo' : ''), onclick: function () { start(el, st); } },
        h('span', { class: 'pdot', style: col ? 'border-color:' + col + ';' + (st.status === 'done' ? 'background:' + col + ';color:#fff' : 'color:' + col) : '', 'aria-hidden': 'true' },
          (st.status === 'done' || st.status === 'refresh') ? icon('check') : (st.needs ? '⇄' : String(st.num))),
        h('span', { class: 'pbody' },
          h('span', { class: 'ptext' }, rec ? h('span', { class: 'prec' }, '★ Recommended') : null, h('b', null, st.label),
            h('small', null, st.level + ' · ' + sub + (st.best_after && st.best_after.length ? ' · best after ' + st.best_after.join(', ') : '')),
            has ? h('span', { class: 'mini' }, h('i', { style: 'width:' + Math.max(4, st.pct) + '%;background:' + col })) : null),
          h('span', { class: 'ppct', style: col ? 'color:' + col : '' }, has ? st.pct + '%' : ''),
          rec ? h('span', { class: 'btn small' }, (st.below && !st.answers) ? 'Quick check' : 'Go', icon('arrow')) : null));
      return el;
    }
    var path = null;
    function draw() {
      var steps = path.steps;
      var ci = steps.findIndex(function (s) { return s.id === path.current; });
      var show = all ? steps.map(function (s, i) { return [s, i]; })
        : steps.map(function (s, i) { return [s, i]; }).filter(function (p) { return ci < 0 ? p[1] >= steps.length - 3 : (p[1] >= ci - 1 && p[1] <= ci + 3); });
      card.replaceChildren(
        h('div', { class: 'row between' }, h('h2', { style: 'margin:0' }, 'My learning path'), h('span', { class: 'small muted' }, path.done + ' / ' + path.total + ' done')),
        h('div', { class: 'ppath' }, show.map(function (p) { return node(p[0]); })),
        h('button', { type: 'button', class: 'btn ghost small', style: 'margin-top:6px', onclick: function () { all = !all; draw(); } }, all ? 'Show less' : 'All steps'));
    }
    api('path').then(function (r) { var k = 0; r.steps.forEach(function (st) { if (!st.needs) st.num = ++k; }); path = r; draw(); }).catch(function () { card.remove(); });
    return card;
  }

  /** Guests: two clear buttons, no explanation text (teacher, 27 October: everyone knows what Log in and Create account do). */
  function guestBanner() {
    var cfg = state.config, pending = regPending();
    var create = cfg.register_url ? registerLink('btn', 'Create account') : null;
    var signin = cfg.sso ? h('a', { class: 'btn ghost', href: cfg.wp_login_url }, icon('user'), 'Log in') : null;
    if (!create && !signin) return null;
    return h('div', { class: 'guestbar' }, signin, create);
  }

  // ───────── learning study (optional, registered learners only) ─────────
  // Switched on in config.php. The wording below is a plain default: replace it with the text your ethics review approved
  // ('research_text' and 'research_text_lv' in config.php, paragraphs separated by an empty line).
  var STUDY = {
    en: {
      title: 'Help with a learning study?', yes: 'Yes, I take part', no: 'No, thanks', later: 'Ask me later', info: 'Read the information sheet',
      body: ['Inga, the teacher behind English Fever, is researching what helps people keep up regular practice. If you take part, your practice data (when and how often you practise, which tasks you do and how you do) is analysed under a random code, not your name. Some features, such as the streak counter or the leaderboard, may look different for you than for other learners. Your results and the grammar content stay the same.',
        'Taking part is optional. By choosing “Yes” you confirm that you are 18 or older, or that a parent or guardian agrees. You can leave at any time on your Profile page; your data is then no longer used.'],
      label: 'Learning study', joined: 'You are taking part in the learning study. Thank you!', left: 'You are not taking part.', leave: 'Leave the study', join: 'Take part', thanks: 'Thank you for taking part!', byebye: 'You have left the study.',
    },
    lv: {
      title: 'Palīdziet pētījumā?', yes: 'Jā, piedalos', no: 'Nē, paldies', later: 'Vēlāk', info: 'Informācija par pētījumu',
      body: ['Inga, skolotāja, kas veido English Fever, pēta, kas palīdz cilvēkiem mācīties regulāri. Ja piedalīsieties, jūsu mācību dati (kad un cik bieži mācāties, kādus uzdevumus veicat un kā jums sokas) tiks analizēti ar nejaušu kodu, nevis ar jūsu vārdu. Dažas funkcijas, piemēram, dienu skaitītājs vai līderu saraksts, jums var izskatīties citādi nekā citiem. Jūsu rezultāti un gramatikas saturs paliek tie paši.',
        'Dalība ir brīvprātīga. Izvēloties “Jā”, jūs apliecināt, ka jums ir 18 gadi vai vairāk, vai ka vecāks vai aizbildnis piekrīt. Jūs varat jebkurā brīdī izstāties savā profila lapā; jūsu dati vairs netiks izmantoti.'],
      label: 'Mācību pētījums', joined: 'Jūs piedalāties mācību pētījumā. Paldies!', left: 'Jūs nepiedalāties.', leave: 'Izstāties', join: 'Piedalīties', thanks: 'Paldies par dalību!', byebye: 'Jūs izstājāties no pētījuma.',
    },
  };
  function studyTexts() {
    var lv = state.user && state.user.lang === 'lv', d = STUDY[lv ? 'lv' : 'en'];
    var custom = lv ? state.config.research_text_lv : state.config.research_text;
    return { d: d, body: custom ? custom.split(/\n\s*\n/) : d.body };
  }
  function studyEligible() { return !!state.user && !state.user.guest && state.user.role === 'student'; }
  function setStudy(join) {
    return api('account/research', { join: join }).then(function (r) { state.user = r.user; renderChrome(location.hash.split('/').slice(0, 2).join('/')); return r; });
  }
  function studyLater() { try { return Date.now() - (+localStorage.getItem('ef_study_later') || 0) < 7 * 86400000; } catch (e) { return false; } }

  /** The invitation on the home page: once per learner, "Ask me later" waits a week. */
  function studyPrompt() {
    if (!state.config.research || !studyEligible() || state.user.research !== 0 || studyLater()) return null;
    var t = studyTexts(), d = t.d, msg = h('div');
    function answer(join) {
      setStudy(join).then(function () { UI.toast(join ? d.thanks : d.byebye); route(); }).catch(function (e) { msg.replaceChildren(h('div', { class: 'err', role: 'alert' }, e.message)); });
    }
    return h('div', { class: 'card', style: 'margin-bottom:16px;border-color:var(--gold)' },
      h('div', { class: 'label' }, d.label), h('h2', null, d.title),
      t.body.map(function (p) { return h('p', null, p); }),
      state.config.research_info_url ? h('p', null, h('a', { href: state.config.research_info_url, target: '_blank', rel: 'noopener' }, d.info)) : null,
      msg,
      h('div', { class: 'row' },
        h('button', { class: 'btn', onclick: function () { answer(true); } }, d.yes),
        h('button', { class: 'btn ghost', onclick: function () { answer(false); } }, d.no),
        h('button', { class: 'linkbtn', onclick: function (e) { try { localStorage.setItem('ef_study_later', String(Date.now())); } catch (er) {} e.target.closest('.card').remove(); } }, d.later)));
  }

  /** On the profile page: shows the state and lets the learner join or leave at any time. */
  function studyProfileCard() {
    if (!studyEligible() || !(state.config.research || state.user.research === 1)) return null;
    var t = studyTexts(), d = t.d, msg = h('div');
    var joined = state.user.research === 1;
    function change(join) {
      setStudy(join).then(function () { UI.toast(join ? d.thanks : d.byebye); viewProfile(); }).catch(function (e) { msg.replaceChildren(h('div', { class: 'err', role: 'alert' }, e.message)); });
    }
    return h('div', { class: 'card' }, h('h2', null, d.label),
      h('p', null, joined ? d.joined : d.left),
      joined ? null : [t.body.map(function (p) { return h('p', { class: 'small muted' }, p); }),
        state.config.research_info_url ? h('p', { class: 'small' }, h('a', { href: state.config.research_info_url, target: '_blank', rel: 'noopener' }, d.info)) : null],
      msg,
      joined ? h('button', { class: 'btn ghost small', onclick: function () { change(false); } }, d.leave)
        : h('button', { class: 'btn small', onclick: function () { change(true); } }, d.join));
  }

  // ───────── home ─────────
  // A quiet page: a greeting, ONE thing to do now, three small links and one muted line. The streak and the time practised today are
  // already in the top bar; the topics and the progress charts are one tap away (folded, and the choice is remembered on the device).
  function viewHome() {
    if (state.user.role === 'teacher') { location.hash = '#/teacher'; return; }
    Promise.all([refreshDash(), api('session/resume')]).then(function (r) {
      var d = r[0], resume = r[1].resume;
      var started = d.totals.answers > 0;
      var rep = d.placement && d.placement.report;
      var nodes = [];
      if (state.welcome) {
        var wl = state.welcome;
        nodes.push(h('div', { class: 'card pad-s row between', style: 'margin-bottom:16px;border-color:var(--good)' },
          h('div', null, h('b', { style: 'color:var(--text)' }, 'Your account is ready'),
            h('div', { class: 'small muted' }, 'Guest results moved over: ' + wl.answers + ' questions, ' + wl.xp + ' XP.')),
          h('button', { class: 'btn small', onclick: function (e) { state.welcome = null; e.target.closest('.card').remove(); } }, 'Great')));
      }
      nodes.push(h('div', { class: 'hello' },
        h('div', { class: 'row', style: 'gap:12px;flex-wrap:nowrap' }, UI.avatar(state.user.avatar, state.user.nickname, 52),
          h('div', null, h('h1', { style: 'margin:0' }, (started ? 'Welcome back, ' : 'Welcome, ') + state.user.nickname),
            !started ? null : h('p', { class: 'muted' }, d.streak.today_done ? 'You practised today. Nice work!'
              : (!feat('streak') ? 'Answer a few questions today.' : (d.streak.current ? 'Practise today to keep your streak alive.' : 'Answer one question today to start a streak.')))))));

      // the one thing to do now
      var main, mainBtn;
      if (resume) {
        mainBtn = h('button', { class: 'btn pulse', onclick: function () { state.sess = newSess(resume.session, resume.item); location.hash = '#/session'; } }, 'Continue', icon('arrow'));
        main = [h('h2', null, 'Continue where you stopped'),
          h('p', { class: 'muted' }, (resume.session.mode === 'placement' ? 'Placement test: ' : 'Practice session: ') + resume.session.n + ' of ' + resume.session.length + ' done.'), mainBtn];
      } else if (!started) {
        mainBtn = h('a', { class: 'btn pulse', href: '#/placement' }, 'Find my level', icon('arrow'));
        main = [h('h2', null, 'Start here'), h('p', { class: 'muted' }, 'A short test (5 to 18 minutes) shows where to begin.'), mainBtn];
      } else {
        mainBtn = surpriseButton('btn pulse', 'Practise now');
        main = [h('h2', null, 'Ready to practise?'), h('p', { class: 'muted' }, 'A short session picked from your own mistakes.'), mainBtn];
      }
      // the other ways in: small buttons with icons, not underlined text (teacher, 27 October)
      var links = h('div', { class: 'tiles' },
        h('a', { class: 'tile', href: '#/practice' }, h('span', { class: 'tile-ic' }, icon('target')), 'Topics'),
        (!started && !resume) ? null : (rep ? h('button', { type: 'button', class: 'tile', onclick: function () { showPlacementReport(rep); } }, h('span', { class: 'tile-ic' }, icon('up')), 'My level') : h('a', { class: 'tile', href: '#/placement' }, h('span', { class: 'tile-ic' }, icon('up')), 'Level test')),
        h('a', { class: 'tile', href: '#/rules' }, h('span', { class: 'tile-ic' }, icon('book')), 'Rules'),
        (!state.user.guest && dashboardUrl()) ? h('a', { class: 'tile only-m', target: '_blank', rel: 'noopener', href: dashboardUrl() }, h('span', { class: 'tile-ic' }, icon('home')), 'My dashboard') : null);
      // the main card: dark like the header, one bright button, the learner's numbers in a quiet strip (teacher, 27 October: stylish, not noisy)
      var CHEERS = ['Ready for 5 minutes of brain gym?', 'Your verbs missed you.', 'Small steps. Big English.', 'Mistakes welcome here.', 'One question at a time.',
        'Grammar, but make it fun.', 'Coffee first? Then English.', "Let's fix one thing today.", "Today's a good day to be Present Perfect.", 'Your brain called. It wants a challenge.'];
      var cheer = h('div', { class: 'hero-cheer' }, CHEERS[Math.floor(Math.random() * CHEERS.length)]);   // a short friendly line, a new one each visit (teacher, 27 October)
      var strip = started ? h('div', { class: 'hero-stats' },
        feat('streak') ? h('span', null, icon('flame'), h('b', null, String(d.streak.current)), d.streak.current === 1 ? ' day' : ' days') : null,
        h('span', null, icon('bolt'), h('b', null, String(d.totals.xp)), ' XP'),
        d.totals.accuracy === null ? null : h('span', null, icon('check'), h('b', null, d.totals.accuracy + '%'), ' correct')) : null;
      nodes.push(h('div', { class: 'card focus hero-card' }, cheer, main, strip));
      nodes.push(links);
      var cb = d.comeback || { open: 0, fixed: 0 };
      if (cb.open > 0 || cb.review > 0) {   // open mistakes, or mistakes fixed a few days ago that are due for a check
        var n = Math.min(10, cb.open + (cb.review || 0));
        nodes.push(h('div', { class: 'card pad-s fn-chance' },
          h('div', { class: 'row between', style: 'flex-wrap:nowrap;gap:14px' },
            h('div', null, h('b', { style: 'color:var(--text)' }, 'Second Chance'),
              h('div', { class: 'small muted' }, (cb.open ? plural(cb.open, 'mistake', 'mistakes') + ' to fix' : plural(cb.review, 'earlier mistake', 'earlier mistakes') + ' to check again') + ' · ' + chanceLength(n))),
            comebackButton('btn small fn-chance', 'Start'))));
      }
      if (started) nodes.push(pathCard());   // My learning path (teacher, 28 October)
      var gb = state.user.guest ? guestBanner() : null; if (gb) nodes.push(gb);   // guests: Log in / Create account, side by side under the main things
      var invite = studyPrompt();   // the learning-study invitation comes after the main card, never before it
      if (invite) nodes.push(invite);

      var ic = started ? installCard(false) : null; if (ic) nodes.push(ic);
      var nStarted = d.skills.filter(function (s) { return s.n > 0; }).length;
      if (started) {   // progress above the topics (teacher, 27 October)
        nodes.push(foldCard('progress', 'My progress', h('span', { class: 'fold-icons', 'aria-label': 'this week and thinking skills' }, icon('clock'), icon('up')), function () {
          return h('div', { class: 'grid g2' }, h('div', null, h('h3', null, 'This week'), weekChart(d.week)), h('div', null, h('h3', null, 'How you do'), catBars(d.cats)));
        }));
      }
      if (started) nodes.push(foldCard('topics', 'Your topics', nStarted ? nStarted + ' started' : 'practise one topic at a time', function () { return topicsCard(d); }));
      show(h('div', { class: 'home' }, nodes));
    }).catch(fail);
  }

  /** A closed-by-default card for the things Home does not need to show all the time; opening it is remembered on this device. */
  function foldCard(key, title, hint, body) {
    var saved = {}; try { saved = JSON.parse(localStorage.getItem('ef_home') || '{}') || {}; } catch (e) {}
    var inner = h('div', { class: 'fold-body' });
    var det = h('details', { class: 'card fold', open: !!saved[key] }, h('summary', null, h('span', { class: 'h3' }, title), h('span', { class: 'small muted' }, hint)), inner);
    function fill() { if (!inner.firstChild) inner.appendChild(body()); }
    if (det.open) fill();
    det.addEventListener('toggle', function () {
      if (det.open) fill();
      saved[key] = det.open ? 1 : 0; try { localStorage.setItem('ef_home', JSON.stringify(saved)); } catch (e) {}
    });
    return det;
  }

  /** "Surprise me": the server picks topics from the learner's own mistakes and gaps. */
  function surpriseButton(cls, label) {
    var b = h('button', { class: cls, type: 'button', onclick: function () {
      b.disabled = true;
      api('session/start', { mode: 'smart', length: 12 }).then(function (r) { state.sess = newSess(r.session, r.item); location.hash = '#/session'; })
        .catch(function (e) { b.disabled = false; UI.toast(e.message); });
    } }, icon('bolt'), label || 'Surprise me');
    return b;
  }

  /** "Second Chance": the learner's own open mistakes, each one met again as a similar question. */
  function comebackButton(cls, label) {
    var b = h('button', { class: cls, type: 'button', onclick: function () {
      b.disabled = true;
      api('session/start', { mode: 'comeback' }).then(function (r) { state.sess = newSess(r.session, r.item); location.hash = '#/session'; })
        .catch(function (e) { b.disabled = false; UI.toast(e.message); });
    } }, icon('refresh'), label || 'Start');
    return b;
  }
  /** Second Chance takes up to 10 mistakes at a time, about 40 seconds each: the learner sees the finish line before starting. */
  function chanceLength(open) { var q = Math.min(10, open); return plural(q, 'question', 'questions') + ' · about ' + Math.max(1, Math.round(q * 0.7)) + ' min'; }
  function plural(n, one, many) { return n + ' ' + (n === 1 ? one : many); }

  function stat(ic, v, k, cls) {
    return h('div', { class: 'card pad-s stat ' + (cls || '') }, h('div', { class: 'v' }, icon(ic), String(v)), h('div', { class: 'k' }, k));
  }

  function weekChart(week) {
    var max = Math.max.apply(null, week.map(function (w) { return w.seconds; }).concat([60]));
    var today = week[week.length - 1].day;
    return h('div', { class: 'bars', role: 'img', 'aria-label': 'Minutes practised in the last 7 days' }, week.map(function (w) {
      var dt = new Date(w.day + 'T12:00:00');
      return h('div', { class: 'b' }, h('div', { class: 'm' }, w.seconds ? String(Math.max(1, Math.round(w.seconds / 60))) : ''),
        h('div', { class: 'col' + (w.day === today ? ' is-today' : ''), style: 'height:' + Math.max(3, Math.round(70 * w.seconds / max)) + 'px' }),
        h('div', { class: 'd' }, dt.toLocaleDateString(undefined, { weekday: 'short' }).slice(0, 2)));
    }));
  }

  /** Learners see three plain kinds of task instead of six thinking levels (teacher, 28 October): Recognise (levels 1-2), Use (3), Write (4-6). Teachers keep the six levels. */
  // by the kind of task, not the thinking level (a "choose the correct sentence" task is Recognise even when it is a level-5 task; teacher, 28 October)
  var CATS = [['Recognise', '👀', 'choose, match', 'recognise'], ['Use', '🧩', 'fill in, put in order', 'use'], ['Write', '✍️', 'correct, rewrite', 'write']];
  function catOf(kind) { return kind === 'mcq' || kind === 'match' ? CATS[0] : (kind === 'text' || kind === 'write' ? CATS[2] : CATS[1]); }
  function catBars(b) {
    return h('div', { class: 'cats' }, CATS.map(function (c) {
      var v = (b || {})[c[3]] || { n: 0, correct: 0 }, n = v.n, ok = v.correct;
      var p = n ? pct(ok, n) : null;
      return h('div', { class: 'cat' }, h('div', { class: 'cat-em', 'aria-hidden': 'true' }, c[1]), h('b', null, c[0]), h('small', null, c[2]),
        h('div', { class: 'ring', style: 'background:radial-gradient(var(--surface) 0 57%, transparent 58%), conic-gradient(var(--btn) 0 ' + (p || 0) + '%, var(--line) 0)' }, p === null ? '–' : p + '%'));
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

  /** "Your topics" on Home: fold-away areas, only the topics in reach, a link for the rest. */
  function topicsCard(d) {
    var holder = h('div');
    // the area practised last is open; the others stay folded until the learner opens them (and the choice is remembered)
    var latest = d.skills.slice().sort(function (a, b) { return b.last - a.last; })[0];
    var openArea = (latest && latest.last) ? latest.area : state.meta.areas[0].id;
    function draw() {
      var high = showHigh(), hidden = 0, saved = openAreas();   // hidden = topics too advanced for this learner, whether shown or not
      var areas = state.meta.areas.map(function (a) {
        var all = d.skills.filter(function (s) { return s.area === a.id; });
        var list = all.filter(function (s) { return high || inReach(s, d); });
        hidden += all.filter(function (s) { return !inReach(s, d); }).length;
        if (!list.length) return null;
        var started = list.filter(function (s) { return s.n > 0; }).length;
        var det = h('details', { class: 'area-fold', open: (a.id in saved) ? !!saved[a.id] : a.id === openArea },
          h('summary', null, h('span', { class: 'h3' }, a.label), h('span', { class: 'small muted' }, started + ' of ' + list.length + ' started')),
          h('div', { class: 'skillgrid' }, list.map(function (s) { return skillCard(s, d); })));
        det.addEventListener('toggle', function () { rememberArea(a.id, det.open); });
        return det;
      });
      holder.replaceChildren.apply(holder, areas.concat([highLink(hidden, high, draw)]));
    }
    draw();
    return holder;
  }

  /** The link under a topic list: show or hide the topics that are well above the learner's level. */
  function highLink(hidden, high, redraw) {
    if (!hidden) return null;   // nothing is too advanced: no link, so it never does nothing
    return h('p', { style: 'margin:14px 0 0' }, h('button', { type: 'button', class: 'linkbtn small', onclick: function () { setShowHigh(!high); redraw(); } },
      high ? 'Hide topics for higher levels' : 'Show topics for higher levels (' + hidden + ')'));
  }

  function skillCard(s, d) {
    var go = h('button', { class: 'btn ghost small', type: 'button', onclick: function () { startTopic(go, s, d); } }, 'Practise');
    return h('div', { class: 'skill' },
      h('div', { class: 'top' }, h('div', null, h('div', { class: 'name' }, s.label), h('div', { class: 'small muted' }, levelRange(s))),
        s.level_est ? h('span', { class: 'pill dark', title: 'Your estimated level in this topic' }, '≈ ' + lv(s.level_est)) : h('span', { class: 'pill' }, s.n ? 'Started' : 'New')),
      h('div', { class: 'meter gold', 'aria-label': 'Accuracy' }, h('i', { style: 'width:' + (s.accuracy || 0) + '%' })),
      h('div', { class: 'row between' }, h('span', { class: 'small muted' }, s.n ? s.n + ' done · ' + s.accuracy + '% correct' : 'Not started'),
        h('span', { class: 'row', style: 'gap:10px;flex-wrap:nowrap' },
          h('button', { class: 'linkbtn small', type: 'button', title: 'Options', onclick: function () { state.prefill = { skills: [s.id], level: topicLevel(s, d) }; location.hash = '#/practice'; } }, 'Options'),
          go)));
  }

  // ───────── teacher: does slip-or-gap / locked-in work? numbers only ─────────
  function viewEvidence() {
    api('teacher/evidence').then(function (e) {
      var p = e.probes, m = e.mistakes;
      function pct(a, b) { return b ? Math.round(100 * a / b) + '%' : '–'; }
      var enough = p.first_probes >= 5 || m.fixed >= 5;
      var sounds = [['right', 'Right'], ['wrong', 'Wrong'], ['fixed', 'Fixed'], ['tricky', 'Tricky'], ['locked', 'Locked in']];
      show(h('div', null,
        h('div', { class: 'row between', style: 'margin-bottom:14px' }, h('div', null, h('div', { class: 'label' }, 'Teacher'), h('h1', { style: 'margin:0' }, 'Learning evidence')),
          h('a', { class: 'small', href: '#/teacher' }, '← Students')),
        h('p', { class: 'small muted' }, 'Counts only, no names. Mistakes of the last 45 days. ' + (enough ? '' : 'Too few so far to say anything: the numbers fill in as learners miss and meet questions again.')),
        h('h2', null, 'A missed question, asked again'),
        h('div', { class: 'grid g4', style: 'margin-bottom:16px' },
          stat('refresh', p.first_probes, 'asked again'),
          stat('check', p.slips + ' · ' + pct(p.slips, p.first_probes), 'right: a slip'),
          stat('flag', p.gaps + ' · ' + pct(p.gaps, p.first_probes), 'missed again: a gap'),
          stat('target', p.angle_right + ' of ' + p.angle_probes, 'right after a gap, from other angles')),
        h('h2', null, 'Mistakes'),
        h('div', { class: 'grid g4', style: 'margin-bottom:16px' },
          stat('users', m.learners, 'learners'),
          stat('flag', m.open, 'open'),
          stat('check', m.fixed, 'fixed'),
          stat('flame', m.locked + ' · ' + pct(m.locked, m.fixed), 'locked in, of fixed')),
        h('p', { class: 'small muted' }, 'Locked in = right again on another day with a different question of that kind. Opened again after being fixed: ' + m.reopened + ' (' + pct(m.reopened, m.fixed) + ' of fixed).'),
        (e.topics && e.topics.length) ? h('div', { class: 'card', style: 'margin:16px 0' }, h('h2', { style: 'margin:0 0 8px' }, 'Where the gaps are'),
          h('ul', { class: 'clean' }, e.topics.map(function (t) { return h('li', { class: 'lvrow' }, h('span', null, t.label), h('span', { class: 'small muted nowrap' }, plural(t.gaps, 'gap', 'gaps') + ' in ' + t.probes + ' asked again')); }))) : null,
        h('div', { class: 'card', style: 'margin-top:16px' }, h('h2', { style: 'margin:0 0 8px' }, 'The sounds'),
          h('div', { class: 'row', style: 'gap:8px;flex-wrap:wrap' }, sounds.map(function (x) { return h('button', { type: 'button', class: 'btn ghost small', onclick: function () { Sound.preview(x[0]); } }, x[1]); })),
          h('p', { class: 'small muted', style: 'margin:10px 0 0' }, 'Learners hear them only with sound on (Profile).'))));
    }).catch(fail);
  }

  // ───────── teacher: reported tasks ─────────
  var REPORT_FILTERS = [['open', 'Open'], ['fixed', 'Fixed'], ['dismissed', 'Not a problem'], ['all', 'All']];

  /** The task as the teacher needs to judge it: text, key, wrong options. */
  function promptNodes(q) { // instruction on one line, the sample sentence below in italics (as learners see it)
    var m = PROMPT_SPLIT.exec(q || '');
    return m ? [h('span', null, UI.rich(UI.markForms(m[1])), ':'), h('br'), h('em', null, m[2])] : [q || ''];
  }

  function taskHead(t) {
    return h('div', null,
      h('div', { class: 'meta', style: 'display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-bottom:8px' },
        h('span', { class: 'pill dark' }, t.skill || '?'), t.level ? levelPill(t.level) : null, t.kind ? h('span', { class: 'pill' }, t.kind) : null, h('code', { class: 'taskid' }, t.id)),
      h('div', { style: 'font-weight:600;color:var(--text);margin-bottom:6px' }, promptNodes(t.q)),
      t.key ? h('div', { class: 'small muted' }, h('b', null, t.options ? 'Correct: ' : 'Accepted: '), t.key) : null,
      t.options ? h('div', { class: 'small muted' }, h('b', null, 'Wrong options: '), t.options.join('  |  ')) : null,
      t.why ? h('div', { class: 'small muted' }, h('b', null, 'Shown to learner: '), UI.rich(t.why)) : null,
      t.why_lv ? h('div', { class: 'small muted' }, h('b', null, 'Latvian: '), UI.rich(t.why_lv)) : null);
  }

  function reportCard(g) {
    var st = g.status;
    function setStatus(status) {
      api('teacher/report-status', { item_id: g.task.id, status: status }).then(function (x) { state.user.reports_open = x.open; viewReports(); }).catch(function (e) { UI.toast(e.message); });
    }
    var det = h('details', { class: 'rep-list' }, h('summary', null, g.count + (g.count === 1 ? ' report' : ' reports')),
      h('ul', null, g.reports.map(function (x) {
        return h('li', null, x.who, ' · ', UI.fmtAgo(x.at),
          x.answer ? h('div', { class: 'small' }, 'Answered: “', x.answer, '” ', x.correct === 1 ? '(marked right)' : '(marked wrong)') : null,
          x.comment ? h('div', { class: 'small' }, '“', x.comment, '”') : null);
      })));
    var label = { 'new': 'New', seen: 'Seen', fixed: 'Fixed', dismissed: 'Not a problem' }[st] || st;
    return h('div', { class: 'card rep' },
      h('div', { class: 'row between', style: 'align-items:flex-start;flex-wrap:nowrap' }, taskHead(g.task), h('span', { class: 'pill ' + (st === 'new' ? 'pink' : (st === 'fixed' ? 'good' : '')), style: 'flex:none' }, label)),
      det,
      (st === 'new' || st === 'seen') ? h('div', { class: 'small muted', style: 'margin-top:8px' }, 'Paused: not shown to learners until you decide.') : null,
      h('div', { class: 'row', style: 'margin-top:12px' },
        (st === 'fixed' || st === 'dismissed')
          ? h('button', { class: 'btn ghost small', onclick: function () { setStatus('new'); } }, 'Reopen')
          : [h('button', { class: 'btn small', title: 'The task has been corrected (by you or in a new upload). It goes back to learners.', onclick: function () { setStatus('fixed'); } }, 'Mark fixed'),
             h('button', { class: 'btn ghost small', title: 'The task is right as it is. It goes back to learners unchanged.', onclick: function () { setStatus('dismissed'); } }, 'Not a problem'),
             st === 'new' ? h('button', { class: 'linkbtn small', title: 'You have read it and will decide later. The task stays paused.', onclick: function () { setStatus('seen'); } }, 'Mark as seen') : null]));
  }

  function viewReports() {
    var filter = state.repFilter || 'open';
    api('teacher/reports', undefined, { status: filter }).then(function (r) {
      state.user.reports_open = r.open; renderChrome('#/reports');
      var seg = h('div', { class: 'seg', role: 'radiogroup', 'aria-label': 'Show' }, REPORT_FILTERS.map(function (f) {
        return h('label', null, h('input', { type: 'radio', name: 'rf', value: f[0], checked: f[0] === filter, onchange: function () { state.repFilter = f[0]; viewReports(); } }), h('span', null, f[1]));
      }));
      // one block of plain text with every report on this tab, to paste into a chat with Claude (teacher, 28 October)
      var copyBtn = h('button', { type: 'button', class: 'btn small', disabled: !r.groups.length, onclick: function () {
        var txt = r.groups.map(function (g, i) {
          var t = g.task;
          return [(i + 1) + '. ' + t.id + ' · ' + (t.skill || '') + ' · ' + (t.level || '') + ' · ' + (t.kind || ''), 'Task: ' + (t.q || ''),
            t.key ? (t.options ? 'Correct: ' : 'Accepted: ') + t.key : null, t.options ? 'Wrong options: ' + t.options.join(' | ') : null,
            g.reports.map(function (x) { return '- ' + (x.answer ? 'Answered "' + x.answer + '" ' + (x.correct === 1 ? '(marked right)' : '(marked wrong)') : '') + (x.comment ? ' Comment: "' + x.comment + '"' : ''); }).join('\n')].filter(Boolean).join('\n');
        }).join('\n\n');
        (navigator.clipboard ? navigator.clipboard.writeText(txt) : Promise.reject()).then(function () { UI.toast('Copied ' + plural(r.groups.length, 'report', 'reports') + '. Paste it into the chat.'); })
          .catch(function () { var ta = h('textarea', { style: 'width:100%;height:240px' }); ta.value = txt; UI.modal(h('div', null, h('h2', null, 'Copy this text'), ta)); ta.select(); });
      } }, 'Copy for Claude');
      var list = r.groups.length ? r.groups.map(reportCard)
        : [h('div', { class: 'card empty' }, 'Nothing here.')];
      var hard = r.hard.length ? [h('h2', { style: 'margin:28px 0 6px' }, 'Often answered wrongly'),
        h('p', { class: 'small muted' }, '70% or more wrong, at least 8 answers.'),
        r.hard.map(function (x) { return h('div', { class: 'card pad-s rep' }, taskHead(x.task), h('div', { class: 'small muted' }, x.pct + '% wrong · ' + x.n + ' answers')); })] : [];
      show(h('div', null,
        h('div', { class: 'row between', style: 'margin-bottom:14px' }, h('div', null, h('div', { class: 'label' }, 'Teacher'), h('h1', { style: 'margin:0' }, 'Reported questions')),
          h('span', { class: 'row', style: 'gap:8px' }, copyBtn, h('a', { class: 'btn ghost small', href: 'api.php?r=teacher/reports-export' }, 'Download CSV'))),
        h('p', { class: 'small muted', style: 'margin:0 0 12px' }, h('b', null, 'Mark fixed'), ': the task is corrected · ', h('b', null, 'Not a problem'), ': the task is right · ', h('b', null, 'Mark as seen'), ': decide later (the task stays paused).'),
        h('div', { style: 'margin-bottom:16px' }, seg), list, hard));
    }).catch(fail);
  }

  // ───────── teacher: add tasks from a spreadsheet ─────────
  var TASK_TABS = [['draft', 'Drafts'], ['approved', 'Approved'], ['retired', 'Retired']];

  /** All prepared draft files at once: check, then add (they arrive as drafts; "Approve all" on the Drafts tab publishes them). */
  function preparedCard() {
    var out = h('div');
    var check = h('button', { class: 'btn small', type: 'button' }, 'Check prepared questions');
    function sum(r) { return [r.ok + ' new', r.updated ? r.updated + ' updated' : null, r.same ? r.same + ' already there' : null, r.bad ? r.bad + ' with problems' : null].filter(Boolean).join(' · '); }
    check.addEventListener('click', function () {
      check.disabled = true; check.textContent = 'Checking…';
      api('teacher/items-import-prepared', {}).then(function (r) {
        check.disabled = false; check.textContent = 'Check prepared questions';
        var add = (r.ok || r.updated) ? h('button', { class: 'btn', type: 'button', onclick: function (e) {
          e.target.disabled = true; e.target.textContent = 'Adding…';
          api('teacher/items-import-prepared', { confirm: true }).then(function (x) { UI.toast(sum(x)); state.taskTab = 'draft'; viewTasks(); })
            .catch(function (er) { e.target.disabled = false; UI.toast(er.message); });
        } }, 'Add all (' + (r.ok + r.updated) + ')') : h('p', { class: 'small muted' }, 'Everything is already added.');
        out.replaceChildren(h('p', null, h('b', null, sum(r))),
          h('details', null, h('summary', { class: 'small' }, r.files.length + ' files'), h('ul', { class: 'small' }, r.files.map(function (f) {
            return h('li', null, f.file + ': ' + sum(f), f.problems.length ? h('div', { class: 'err small' }, f.problems.join(' ')) : null);
          }))), h('div', { class: 'row', style: 'margin-top:10px' }, add));
      }).catch(function (e) { check.disabled = false; check.textContent = 'Check prepared questions'; UI.toast(e.message); });
    });
    return h('div', { class: 'card', style: 'margin-bottom:16px' }, h('h2', { style: 'margin:0 0 6px' }, 'Prepared questions'),
      h('p', { class: 'small muted', style: 'margin:0 0 10px' }, 'All question files that come with the app, in one go. New ones arrive as drafts; corrected ones are updated where they are.'), check, out);
  }

  function viewTasks() {
    api('teacher/items').then(function (r) {
      var tab = state.taskTab || (r.items.draft.length ? 'draft' : 'approved');
      var result = h('div');
      var file = h('input', { type: 'file', accept: '.csv,text/csv,text/plain', 'aria-label': 'Choose a CSV file' });

      function setStatus(ids, status) {
        api('teacher/items-status', { ids: ids, status: status }).then(function () { viewTasks(); }).catch(function (e) { UI.toast(e.message); });
      }

      function showCheck(csv, res) {
        var bad = res.rows.filter(function (x) { return !x.ok; }), warned = res.rows.filter(function (x) { return x.ok && x.warnings.length; });
        var upd = res.updated || 0, same = res.same || 0;
        var add = (res.ok || upd) ? h('button', { class: 'btn', type: 'button', onclick: function (e) {
          e.target.disabled = true;
          api('teacher/items-import', { csv: csv, confirm: true }).then(function (x) { UI.toast((x.ok ? x.ok + ' added as drafts' : '') + (x.ok && x.updated ? ', ' : '') + (x.updated ? x.updated + ' updated' : '')); state.taskTab = 'draft'; viewTasks(); })
            .catch(function (er) { e.target.disabled = false; UI.toast(er.message); });
        } }, (res.ok ? 'Add ' + res.ok + (res.ok === 1 ? ' question' : ' questions') + ' as drafts' : '') + (res.ok && upd ? ' and ' : '') + (upd ? (res.ok ? 'update ' : 'Update ') + upd : '')) : null;
        result.replaceChildren(h('div', { class: 'card', style: 'margin-bottom:16px' },
          h('h2', { style: 'margin:0 0 8px' }, [res.ok + ' new', upd ? upd + ' updated' : null, same ? same + ' already there' : null, res.bad ? res.bad + ' with problems' : null].filter(Boolean).join(' · ')),
          bad.length ? h('ul', { class: 'rep-list-plain' }, bad.map(function (x) { return h('li', { style: 'margin-bottom:8px' }, h('b', null, 'Row ' + x.line + ': '), (x.q || '').slice(0, 70), h('div', { class: 'err small', style: 'margin:2px 0 0' }, x.errors.join(' '))); })) : null,
          warned.length ? h('ul', { class: 'rep-list-plain' }, warned.map(function (x) { return h('li', { class: 'small muted', style: 'margin-bottom:6px' }, h('b', null, 'Row ' + x.line + ': '), x.warnings.join(' ')); })) : null,
          h('div', { class: 'row', style: 'margin-top:12px' }, add)));
      }

      file.addEventListener('change', function () {
        var f = file.files && file.files[0]; if (!f) return;
        var fr = new FileReader();
        fr.onload = function () {
          var csv = String(fr.result || '');
          api('teacher/items-import', { csv: csv }).then(function (res) { showCheck(csv, res); })
            .catch(function (e) { result.replaceChildren(h('div', { class: 'card err', role: 'alert' }, e.message)); });
        };
        fr.readAsText(f, 'UTF-8');
      });

      var seg = h('div', { class: 'seg', role: 'radiogroup', 'aria-label': 'Show' }, TASK_TABS.map(function (t) {
        return h('label', null, h('input', { type: 'radio', name: 'tt', value: t[0], checked: t[0] === tab, onchange: function () { state.taskTab = t[0]; viewTasks(); } }), h('span', null, t[1] + ' (' + r.items[t[0]].length + ')'));
      }));
      var list = r.items[tab].map(function (x) {
        var acts = tab === 'draft' ? [h('button', { class: 'btn small', onclick: function () { setStatus([x.id], 'approved'); } }, 'Approve'), h('button', { class: 'btn ghost small', onclick: function () { setStatus([x.id], 'retired'); } }, 'Retire')]
          : tab === 'approved' ? [h('button', { class: 'btn ghost small', onclick: function () { setStatus([x.id], 'draft'); } }, 'Back to draft'), h('button', { class: 'btn ghost small', onclick: function () { setStatus([x.id], 'retired'); } }, 'Retire')]
          : [h('button', { class: 'btn ghost small', onclick: function () { setStatus([x.id], 'draft'); } }, 'Back to draft')];
        return h('div', { class: 'card rep' }, taskHead({ id: x.id, skill: x.skill, level: x.level, kind: x.kind, q: x.q, key: x.key, options: x.options }), h('div', { class: 'row', style: 'margin-top:10px' }, acts));
      });
      var bulk = (tab === 'draft' && r.items.draft.length > 1) ? h('button', { class: 'btn small', style: 'margin-left:12px', onclick: function () { setStatus(r.items.draft.map(function (x) { return x.id; }), 'approved'); } }, 'Approve all ' + r.items.draft.length) : null;
      show(h('div', null,
        h('div', { class: 'row between', style: 'margin-bottom:14px' }, h('div', null, h('div', { class: 'label' }, 'Teacher'), h('h1', { style: 'margin:0' }, 'Questions')),
          h('a', { class: 'btn ghost small', href: 'api.php?r=teacher/items-template' }, 'Download template')),
        preparedCard(),
        h('div', { class: 'card', style: 'margin-bottom:16px' }, h('h2', { style: 'margin:0 0 10px' }, 'Add questions from a CSV file'), file,
          h('details', { style: 'margin-top:12px' }, h('summary', { class: 'small' }, 'Topic names'), h('ul', { class: 'small', style: 'columns:2;margin:8px 0 0' }, r.topics.map(function (t) { return h('li', null, t); })))),
        result,
        h('div', { style: 'margin:8px 0 14px' }, seg, bulk),
        list.length ? list : h('div', { class: 'card empty' }, 'Nothing here.')));
    }).catch(fail);
  }

  // ───────── test version notice ─────────
  function betaPill() { return h('span', { class: 'betapill', title: 'This is a test version: the questions are still being checked' }, h('span', { class: 'long' }, 'Test version'), h('span', { class: 'short' }, 'Test')); }
  // ───────── placement ─────────
  function viewPlacementIntro() {
    var sizes = [[12, 'Quick', 'about 5 minutes'], [24, 'Medium', 'about 10 minutes'], [40, 'Full', 'about 18 minutes']];
    var size = 24;
    var go = h('button', { class: 'btn', id: 'go' }, 'Start the test');
    var seg = h('div', { class: 'sizes', role: 'radiogroup', 'aria-label': 'Test length' }, sizes.map(function (z) {
      return h('label', { class: 'size' }, h('input', { type: 'radio', name: 'sz', value: String(z[0]), checked: z[0] === size, onchange: function () { size = z[0]; } }),
        h('span', null, h('b', null, z[1]), h('span', { class: 'muted' }, z[0] + ' questions'), h('span', { class: 'small muted' }, z[2])));
    }));
    show(h('div', { class: 'sess' }, h('div', { class: 'card' },
      h('div', { class: 'label' }, 'Placement test'), h('h1', null, 'Find your starting point'),
      h('p', null, 'The questions adapt to your answers.'), seg,
      h('div', { class: 'row', style: 'margin-top:16px' }, go, h('a', { class: 'btn ghost', href: '#/home' }, 'Not now')))));
    go.addEventListener('click', function () {
      this.disabled = true; this.setAttribute('aria-busy', 'true'); this.textContent = 'Starting…';   // the server can take a moment: say so
      api('session/start', { mode: 'placement', length: size }).then(function (r) { state.sess = newSess(r.session, r.item); location.hash = '#/session'; }).catch(fail);
    });
  }

  // ───────── practice picker ─────────
  function viewPractice() {
    if (!state.dash) { var pf = state.prefill; return refreshDash().then(function () { state.prefill = pf; viewPractice(); }).catch(fail); }
    var d = state.dash;
    var pre = state.prefill; state.prefill = null;
    var FULL = state.meta.full_levels, COUNT = state.meta.level_counts, SKC = state.meta.skill_counts || {};
    var LEVEL_NAMES = { A1: 'Elementary', A2: 'Pre-intermediate', B1: 'Intermediate', B2: 'Upper-intermediate', C1: 'Advanced', C2: 'Proficient' };
    function full(l) { return String(l || '').slice(0, 2); }
    var guess = full((d && d.placement && d.placement.report) ? d.placement.report.overall_level : (learnerLevel(d) || 'A2.1'));
    var levels = {}; levels[(pre && pre.level) ? full(pre.level) : (COUNT[guess] ? guess : 'A2')] = true;
    var selected = {};
    (pre ? pre.skills : []).forEach(function (s) { selected[s] = true; });
    var length = 10;
    var startBtn = h('button', { class: 'btn', type: 'button' }, 'Start');
    var err = h('div');
    var holder = h('div');

    function chosenLevels() { return FULL.filter(function (l) { return levels[l]; }); }
    function countAt(s) { return chosenLevels().reduce(function (n, l) { return n + ((SKC[s.id] || {})[l] || 0); }, 0); }
    function shortLabel(s) { return s.label.replace(/\s*[(:].*$/, ''); }

    var openMap = {};   // areas start closed, except the ones with chosen topics
    function group(area) {
      var list = state.meta.skills.filter(function (s) { return s.area === area.id && countAt(s) > 0; });
      if (!list.length) return null;
      var n = list.filter(function (s) { return selected[s.id]; }).length;
      var det = h('details', { class: 'picker-group', open: (area.id in openMap) ? openMap[area.id] : n > 0 },
        h('summary', null, h('span', { class: 'h3' }, area.label), h('span', { class: 'pill', style: 'margin-left:8px;' + (n ? '' : 'display:none') }, n + ' chosen')),
        h('div', { class: 'chipsel tilesel tilegrid', role: 'group', 'aria-label': area.label }, list.map(function (s) {
          var inp = h('input', { type: 'checkbox', value: s.id, checked: !!selected[s.id], onchange: function () { selected[s.id] = inp.checked; redrawLater(); } });
          var rule = h('button', { type: 'button', class: 'ttile-rule', 'aria-label': 'Rule: ' + s.label, title: 'Rule', onclick: function (e) { e.preventDefault(); e.stopPropagation(); rulesModal(s.id); } }, '?');   // a quick look at the rule before practising
          return h('label', null, inp, topicTile(s), h('span', { class: 'ttile-check', 'aria-hidden': 'true' }, icon('check')), rule);
        })));
      det.addEventListener('toggle', function () { openMap[area.id] = det.open; });
      return det;
    }
    var timer = null;
    function redrawLater() { clearTimeout(timer); timer = setTimeout(redraw, 0); }
    function redraw() {
      // topics that have no questions at the chosen levels disappear (and are unticked)
      state.meta.skills.forEach(function (s) { if (selected[s.id] && countAt(s) === 0) delete selected[s.id]; });
      var ids = Object.keys(selected).filter(function (k) { return selected[k]; });
      startBtn.replaceChildren(ids.length ? 'Start' : 'Start mixed practice');
      startBtn.disabled = chosenLevels().length === 0;
      var levelRow = h('div', { class: 'seg lvseg', role: 'group', 'aria-label': 'Level' }, FULL.filter(function (l) { return (COUNT[l] || 0) > 0; }).map(function (l) {   // only the levels that have questions (A2 to C1 now)
        var has = (COUNT[l] || 0) > 0;
        var inp = h('input', { type: 'checkbox', value: l, checked: !!levels[l], disabled: !has, onchange: function () { levels[l] = inp.checked; redraw(); } });
        return h('label', { class: has ? '' : 'off', title: has ? LEVEL_NAMES[l] : LEVEL_NAMES[l] + ': coming soon' }, inp, h('span', null, l));
      }));
      holder.replaceChildren(
        h('div', { class: 'picker-group' }, levelRow),
        h('div', { class: 'picker-group' }, h('div', null, state.meta.areas.map(group))),
        h('div', { class: 'picker-group' }, h('h3', null, 'Questions'),
          h('div', { class: 'seg', role: 'radiogroup', 'aria-label': 'Number of questions' }, [10, 15, 20].map(function (n) {
            return h('label', null, h('input', { type: 'radio', name: 'len', value: String(n), checked: n === length, onchange: function () { length = n; } }), h('span', null, String(n)));
          }))));
    }
    startBtn.addEventListener('click', function () {
      startBtn.disabled = true; startBtn.setAttribute('aria-busy', 'true'); startBtn.textContent = 'Starting…';
      var ids = Object.keys(selected).filter(function (k) { return selected[k]; });
      api('session/start', { mode: 'practice', skills: ids, levels: chosenLevels(), length: length }).then(function (r) {
        state.sess = newSess(r.session, r.item); location.hash = '#/session';
      }).catch(function (e) { startBtn.disabled = false; startBtn.removeAttribute('aria-busy'); redraw(); err.replaceChildren(h('div', { class: 'err', role: 'alert' }, e.message)); });
    });
    redraw();
    show(h('div', { class: 'sess' }, h('div', { class: 'card' },
      h('div', { class: 'row between' }, h('h1', { style: 'margin:0' }, 'Practice'), h('span', { class: 'row', style: 'gap:8px' }, (d.comeback && d.comeback.open) ? comebackButton('btn small fn-chance', 'Second Chance (' + d.comeback.open + ')') : null, surpriseButton('btn small fn-surprise'))),
      holder, err, h('div', { class: 'row', style: 'margin-top:16px' }, startBtn))));
  }

  // ───────── session ─────────
  // A blank grows with what is typed, so a long answer such as "has been being repaired" is always fully visible.
  var measure = document.createElement('canvas').getContext('2d');
  function fitBlank(inp) {
    var cs = getComputedStyle(inp), fs = parseFloat(cs.fontSize) || 16;
    measure.font = cs.fontWeight + ' ' + cs.fontSize + ' ' + cs.fontFamily;
    var pad = parseFloat(cs.paddingLeft) + parseFloat(cs.paddingRight) + parseFloat(cs.borderLeftWidth) + parseFloat(cs.borderRightWidth);
    inp.style.width = Math.ceil(Math.max(9.5 * fs, measure.measureText(inp.value).width + pad + 14)) + 'px';
  }
  function growBox(ta) { ta.style.height = 'auto'; ta.style.height = Math.max(ta.scrollHeight, 110) + 'px'; }

  // The tasks answered so far in this session are kept so the learner can look back at them (read-only: an answer is
  // already recorded and decides the next task). They survive a reload in the same tab and are gone when the tab closes.
  function histKey(id) { return 'ef_hist_' + id; }
  function loadHistory(id) { try { var v = JSON.parse(sessionStorage.getItem(histKey(id)) || '[]'); return Array.isArray(v) ? v : []; } catch (e) { return []; } }
  function saveHistory(S) { try { sessionStorage.setItem(histKey(S.session.id), JSON.stringify(S.history)); } catch (e) {} }
  function clearHistories() { try { Object.keys(sessionStorage).forEach(function (k) { if (k.indexOf('ef_hist_') === 0) sessionStorage.removeItem(k); }); } catch (e) {} }
  /** curN: number of the task this object stands for (0-based); it does not change when the answer comes back. */
  function newSess(session, item, history) { return { session: session, item: item, curN: session.n, startedAt: Date.now(), result: null, last: null, history: history || loadHistory(session.id) }; }

  /** rv: number of an earlier task to look back at (read-only); none = the current task. */
  function viewSession(rv) {
    var S = state.sess;
    if (!S) { return api('session/resume').then(function (r) { if (r.resume) { state.sess = newSess(r.resume.session, r.resume.item); viewSession(); } else location.hash = '#/home'; }).catch(fail); }
    var H = S.history || (S.history = []);
    var entry = function (n) { return H.filter(function (e) { return e.n === n; })[0] || null; };
    var rev = (rv === undefined || rv === null) ? null : entry(rv);   // an earlier task, looked at again
    var reviewing = !!rev;
    var answeredNow = !reviewing && !!S.last && !!entry(S.curN);       // the current task, already answered, feedback still on screen
    if (answeredNow) rev = entry(S.curN);
    var at = rev ? rev.n : S.curN;                                   // number of the task on screen (0-based)
    var it = rev ? rev.item : S.item, ses = S.session;
    var answerGetter, canSubmit = function () { return false; };
    var submit = h('button', { class: 'btn', disabled: true }, 'Check answer');
    var skipBtn = h('button', { type: 'button', class: 'btn ghost skipbtn' }, 'Skip');   // "I don't know": no guessing, no XP; the topic comes back in Second Chance (teacher, 27 October)
    var area = h('div');
    var qEl = h('div', { class: 'q' });
    var inputs = [];
    var chosen = null;
    var board = null; // a drag-and-drop board (word order, matching or word-bank gap)

    function ready() { submit.disabled = !canSubmit(); }

    // "Rewrite in the past: I have to get up early." -> the instruction, then the sample sentence on its own line in italics
    var SPLIT = PROMPT_SPLIT;
    var promptSplit = SPLIT.exec(it.q || '');
    if (!promptSplit && it.kind === 'gap') {   // every gap task has an instruction line, like the other task types
      var lead = /^((?:Use|Complete|Write|Put|Choose|Add)\b[^.?!_]*)[.]\s+(.*___.*)$/.exec(it.q || '');   // "Use the present simple. My sister ___ here." -> the first sentence is the instruction
      promptSplit = lead ? [it.q, lead[1], lead[2]] : [it.q, 'Complete the sentence', it.q];
    }
    var promptSample = promptSplit ? promptSplit[2] : (it.q || '');
    function setPrompt(el, text) { // plain prompt text, with the instruction split off when there is one
      var m = SPLIT.exec(text || '');
      if (!m) { el.textContent = text; return; }
      el.appendChild(h('span', { class: 'q-instr' }, UI.rich(UI.markForms(m[1])), ':')); el.appendChild(h('br')); el.appendChild(h('em', { class: 'q-sample' }, m[2]));
    }

    if (it.kind === 'mcq') {
      setPrompt(qEl, it.q);
      var wrap = h('div', { class: 'opts', role: 'radiogroup', 'aria-label': 'Answer options' });
      it.options.forEach(function (o, i) {
        var inp = h('input', { type: 'radio', name: 'opt', value: o, id: 'o' + i, onchange: function () { chosen = o; ready(); } });
        wrap.appendChild(h('label', { class: 'opt', for: 'o' + i, 'data-opt': o }, inp, h('span', { class: 'mark' }), h('span', null, o)));
      });
      area.appendChild(wrap);
      answerGetter = function () { return chosen; };
      canSubmit = function () { return chosen !== null; };
    } else if (it.kind === 'order' || it.kind === 'match' || (it.kind === 'gap' && it.bank)) {
      if (it.kind === 'order') { setPrompt(qEl, it.q); board = DnD.order(it.tokens, ready); }
      else if (it.kind === 'match') { setPrompt(qEl, it.q); board = DnD.match(it.lefts, it.rights, ready); }
      else { board = DnD.bankGap(promptSample, it.bank, ready); qEl = board.sentence;
        if (promptSplit) { // instruction line, then the sentence (with its gaps) in italics
          var smp = h('em', { class: 'q-sample' }); while (qEl.firstChild) smp.appendChild(qEl.firstChild);
          qEl.appendChild(h('span', { class: 'q-instr' }, UI.rich(UI.markForms(promptSplit[1])), ':')); qEl.appendChild(h('br')); qEl.appendChild(smp);
        } area.appendChild(h('p', { class: 'small muted dnd-hint', style: 'margin:0 0 10px' }, 'Tap or drag the words into the gaps.')); }
      area.appendChild(board.el);
      requestAnimationFrame(function () { if (board.el.offsetHeight) board.el.style.minHeight = board.el.offsetHeight + 'px'; });   // the board keeps its first height, so the Check button does not move while cards are placed
      answerGetter = board.answer; canSubmit = board.complete;
    } else if (it.kind === 'gap') {
      var parts = promptSample.split('___');
      var sampleEl = promptSplit ? h('em', { class: 'q-sample' }) : qEl;
      if (promptSplit) { qEl.appendChild(h('span', { class: 'q-instr' }, UI.rich(UI.markForms(promptSplit[1])), ':')); qEl.appendChild(h('br')); qEl.appendChild(sampleEl); }
      parts.forEach(function (p, i) {
        sampleEl.appendChild(document.createTextNode(p));
        if (i < parts.length - 1) {
          var inp = h('input', { type: 'text', class: 'blank', autocomplete: 'off', autocapitalize: 'off', spellcheck: 'false', 'aria-label': 'Answer ' + (i + 1), oninput: function (e) { fitBlank(e.target); ready(); } });
          inputs.push(inp); sampleEl.appendChild(inp);
        }
      });
      answerGetter = function () { return inputs.map(function (i) { return i.value; }); };
      canSubmit = function () { return inputs.every(function (i) { return i.value.trim() !== ''; }); };
    } else if (it.kind === 'text') {
      setPrompt(qEl, it.q);
      var t = h('input', { type: 'text', class: 'type-in', autocomplete: 'off', autocapitalize: 'sentences', spellcheck: 'false', placeholder: 'Type your answer', 'aria-label': 'Your answer', oninput: ready });
      inputs.push(t); area.appendChild(t);
      answerGetter = function () { return t.value; };
      canSubmit = function () { return t.value.trim() !== ''; };
    } else {
      setPrompt(qEl, it.q);
      var ta = h('textarea', { class: 'write', placeholder: 'Write your answer here', 'aria-label': 'Your answer', spellcheck: 'true', oninput: function (e) { growBox(e.target); ready(); } });
      inputs.push(ta); area.appendChild(ta);
      answerGetter = function () { return ta.value; };
      canSubmit = function () { return ta.value.trim().split(/\s+/).length >= 2; };
    }

    inputs.forEach(function (i) {
      if (i.tagName === 'INPUT') i.addEventListener('keydown', function (e) { if (e.key === 'Enter' && canSubmit()) { e.preventDefault(); doSubmit(); } });
    });

    var feedback = h('div', { 'aria-live': 'polite' });
    var taskStart = Date.now();

    function doSubmit(skip) {
      if (skip !== true && !canSubmit()) return;
      if (submit.disabled && skip !== true) return;
      submit.disabled = true; skipBtn.disabled = true;
      var ans = skip === true ? (it.kind === 'mcq' || it.kind === 'text' || it.kind === 'write' ? '' : []) : answerGetter();
      api('session/answer', { session_id: ses.id, item_id: it.id, answer: ans, skip: skip === true, time_ms: Date.now() - taskStart }).then(function (r) {
        S.session = r.session; S.last = r; state.todaySeconds = state.todaySeconds;
        S.history = H.filter(function (e) { return e.n !== at; }).concat([{ n: at, item: it, ans: ans, result: r.result }]); H = S.history; saveHistory(S);
        lock(); showFeedback(r, ans); drawDots(); drawPrev();
        Sound.play(r.result.locked ? 'locked' : r.result.fixed ? 'fixed' : r.result.gap ? 'tricky' : r.result.correct ? 'right' : ((r.result.near || it.kind === 'write') ? 'almost' : 'wrong'));
        if (r.done) S.summary = r.summary;
      }).catch(function (e) {
        submit.disabled = !canSubmit(); skipBtn.disabled = false;
        if (e.status === 409) { api('session/resume').then(function (x) { if (x.resume) { state.sess = newSess(x.resume.session, x.resume.item); viewSession(); } else { location.hash = '#/home'; } }); return; }
        feedback.replaceChildren(h('div', { class: 'err', role: 'alert' }, e.message));
      });
    }
    submit.addEventListener('click', function () { doSubmit(); });
    skipBtn.addEventListener('click', function () { doSubmit(true); });

    function lock() {
      inputs.forEach(function (i) { i.disabled = true; i.readOnly = true; });
      area.querySelectorAll('.dnd-hint').forEach(function (x) { x.remove(); });   // the drag hint is not needed once the answer is checked
      area.querySelectorAll('input[type=radio]').forEach(function (r) { r.disabled = true; });
      if (board) board.lock();
      submit.remove(); skipBtn.remove();
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
      if (board && !res.skipped) board.mark(it.kind === 'match' ? res.marks : res.correct);
      drawFeedback(r, ans, true);
      var prog = document.getElementById('prog');
      if (prog) prog.style.width = Math.round(100 * ses.n / ses.length) + '%';
    }

    // The explanation can be shown in English or Latvian (up to B1.2). The learner's choice is remembered.
    var openRuleNext = false;   // a flag was pressed: show the rule open in the new language
    function drawFeedback(r, ans, first) {
      var res = r.result;
      var hasLv = !!res.why_lv;
      var lv = hasLv && state.user.lang === 'lv';
      var good = res.correct;
      var cheers = lv ? ['Pareizi!', 'Labi izdarīts!', 'Jā, tieši tā!', 'Lieliski!', 'Tieši tā!'] : ['Correct!', 'Well done!', 'Yes, that is right!', 'Good job!', 'Exactly right!'];
      var fb = h('div', { class: 'feedback ' + (good ? 'good' : 'bad') });
      var tips = (good && res.notes) ? res.notes : [];
      // rule reminder = a question-mark button and the flags beside it: a flag opens the rule (and the whole explanation) in that language (teacher, 27 October)
      function flag(code) {
        var on = (code === 'lv') === lv;
        return h('button', { type: 'button', class: 'langbtn ' + code + (on ? ' on' : ''), 'aria-pressed': on ? 'true' : 'false', 'aria-label': code === 'lv' ? 'Noteikums latviski' : 'Rule in English', title: code === 'lv' ? 'Latviski' : 'English',
          onclick: function (e) {
            e.preventDefault(); e.stopPropagation();
            var d = fb.querySelector('details.rule');
            if (on) { if (d) d.open = !d.open; return; }
            state.user.lang = code;
            api('account/profile', { lang: code }).catch(function () {});
            openRuleNext = true;
            drawFeedback(r, ans, false);
          } });
      }
      var langBtn = hasLv ? [flag('lv'), flag('en')] : [];
      fb.appendChild(h('h3', { class: res.skipped ? 'skipped' : null }, icon(good ? 'check' : res.skipped ? 'arrow' : 'cross'), res.skipped ? (lv ? 'Izlaists – lūk, atbilde' : 'Skipped – here is the answer') : it.kind === 'write' ? (good ? (lv ? 'Vajadzīgā forma ir' : 'The form you need is there') : (lv ? 'Pārbaudi uzdevuma prasības' : 'Check the task rules')) : (good ? (tips.length ? (lv ? 'Pareizi – ar nelielu rakstības padomu' : 'Correct – with a small spelling tip') : cheers[lastCheer = (lastCheer === null ? Math.floor(Math.random() * cheers.length) : lastCheer)]) : (res.near ? (lv ? 'Gandrīz – pārbaudi vienu vārdu' : 'Almost – one word to check') : (lv ? 'Ne gluži' : 'Not quite'))),
        res.xp ? h('span', { class: 'pill xp xp-' + (res.xp >= 20 ? 4 : res.xp >= 14 ? 3 : res.xp >= 10 ? 2 : 1), style: 'margin-left:auto' }, '+' + res.xp + ' XP') : null));

      if (res.fixed) fb.appendChild(h('p', { class: 'fixed-line' }, icon('check'), h('b', null, lv ? 'Agrāka kļūda šajā tēmā izskatās izlabota.' : 'An earlier mistake on this topic looks fixed.')));
      var cmp = (!good && !res.skipped && (it.kind === 'text' || it.kind === 'order') && typeof res.show === 'string')
        ? wordDiff(it.kind === 'order' ? (ans || []).join(' ') : String(ans || ''), res.show) : null;   // your sentence and the right one, the different words marked (teacher, 27 October)
      if (cmp) fb.appendChild(h('div', { class: 'compare' },
        h('div', { class: 'cmp-row' }, h('span', { class: 'cmp-mark bad', 'aria-hidden': 'true' }, '✗'), h('span', { class: 'sr' }, lv ? 'Tava atbilde: ' : 'Your answer: '), h('span', null, cmp[0])),
        h('div', { class: 'cmp-row' }, h('span', { class: 'cmp-mark good', 'aria-hidden': 'true' }, '✓'), h('span', { class: 'sr' }, lv ? 'Pareizi: ' : 'Correct: '), h('span', null, cmp[1]))));
      if (!good && !res.skipped && it.kind === 'mcq' && chosen) fb.appendChild(h('p', null, h('b', null, lv ? 'Tu izvēlējies: ' : 'You chose: '), h('span', { class: 'mine' }, chosen)));
      if (!good && !res.skipped && (it.kind === 'gap' || (it.kind === 'text' && !cmp))) {
        var given = Array.isArray(ans) ? ans.join(' / ') : ans;
        fb.appendChild(h('p', null, h('b', null, lv ? 'Tu uzrakstīji: ' : 'You wrote: '), h('span', { class: 'mine' }, given)));
      }
      if (!good && !res.skipped && it.kind === 'order' && !cmp) fb.appendChild(h('p', null, h('b', null, lv ? 'Tava secība: ' : 'Your order: '), h('span', { class: 'mine' }, (ans || []).join(' '))));
      var spec = lv && res.specific_lv ? res.specific_lv : res.specific;
      if (spec) fb.appendChild(h('p', null, h('b', null, lv ? 'Padoms: ' : 'Tip: '), UI.rich(spec)));
      if (tips.length) fb.appendChild(h('p', null, h('b', null, 'Small tips: '), tips.join(' ')));
      var why = lv ? res.why_lv : res.why;
      if (it.kind === 'write') {
        fb.appendChild(h('p', { class: 'small' }, lv ? 'Šī pārbaude redz tikai vajadzīgo formu. Salīdzini savu atbildi ar piemēru.' : 'This only checks the form you need. Compare your answer with the model.'));
        fb.appendChild(h('div', { class: 'ans' }, h('b', null, lv ? 'Piemēra atbilde: ' : 'Model answer: '), res.show));
        fb.appendChild(h('p', null, UI.rich(why)));
      } else {
        if (it.kind === 'match') {
          if (!good && res.pairs) fb.appendChild(h('div', { class: 'ans' }, h('b', null, lv ? 'Pareizi: ' : 'Correct pairs: '),
            h('ul', { class: 'pairs' }, res.pairs.map(function (p) { return h('li', null, p[0], ' → ', h('b', null, p[1])); }))));
        } else if ((!good || it.kind !== 'mcq') && !cmp) {
          var findWrong = it.kind === 'mcq' && /^Which sentence (is NOT correct|has a mistake)\?/.test(it.q || '');   // the answer is the faulty sentence: do not call it "correct"
          fb.appendChild(h('div', { class: 'ans' }, h('b', null, good ? (lv ? 'Atbilde: ' : 'Answer: ') : findWrong ? (lv ? 'Nepareizais teikums: ' : 'The wrong sentence: ') : (lv ? 'Pareizā atbilde: ' : 'Correct answer: ')), good || findWrong ? res.show : h('span', { class: 'right-ans' }, res.show)));
        }
        fb.appendChild(h('p', null, h('b', null, lv ? 'Kāpēc: ' : 'Why: '), UI.rich(why)));
      }
      fb.appendChild(ruleDetails(res.skill, !good, lv, langBtn));

      var nextText = r.done ? 'See my results' : 'Next';
      var nextBtn = h('button', { class: 'btn', onclick: function () { next(r); } }, nextText, icon('arrow'));
      if (reviewing) {   // looking back at an earlier task: move between answered tasks or go back to where we were
        var older = olderOf(at), newer = H.filter(function (e) { return e.n > at; }).sort(function (a, b) { return a.n - b.n; })[0];
        fb.appendChild(h('div', { class: 'nextrow' },
          h('span', { class: 'row', style: 'gap:8px' },
            older ? h('button', { class: 'btn ghost small', onclick: function () { viewSession(older.n); } }, '‹ Previous') : null,
            newer ? h('button', { class: 'btn ghost small', onclick: function () { viewSession(newer.n); } }, 'Next ›') : null),
          h('button', { class: 'btn', onclick: function () { viewSession(); } }, S.last ? 'Back to question ' + (S.curN + 1) + ' feedback' : 'Back to question ' + (S.curN + 1), icon('arrow'))));
        var wasOpenR = feedback.querySelector('details.rule[open]');
        feedback.replaceChildren(fb);
        if (wasOpenR) { var dr = fb.querySelector('details.rule'); if (dr) dr.open = true; }
        return;
      }
      var adaptNote = null;
      if (!r.done && ses.mode === 'practice' && res.adapt !== 'same') {
        adaptNote = h('span', { class: 'adapt' }, icon(res.adapt === 'harder' ? 'up' : 'down'), res.adapt === 'harder' ? (lv ? 'Nākamais: mazliet grūtāks' : 'Next: a bit harder') : (lv ? 'Nākamais: mazliet vieglāks' : 'Next: a bit easier'));
      }
      fb.appendChild(h('div', { class: 'nextrow' }, adaptNote || h('span'), nextBtn));
      var wasOpen = feedback.querySelector('details.rule[open]');
      feedback.replaceChildren(fb);
      if (wasOpen || openRuleNext) { var d = fb.querySelector('details.rule'); if (d) d.open = true; }
      openRuleNext = false;
      if (first) nextBtn.focus();
    }
    var lastCheer = null;

    function next(r) {
      if (r.done) { state.sess = null; state.lastSummary = r.summary; Sound.play((r.summary && r.summary.fixed) ? 'fixed' : 'done'); go('#/summary'); return; }
      state.sess = newSess(r.session, r.next, S.history);
      viewSession();
    }

    function olderOf(n) { return H.filter(function (e) { return e.n < n; }).sort(function (a, b) { return b.n - a.n; })[0] || null; }
    var dotsEl = h('div', { class: 'dots', role: 'group', 'aria-label': 'Questions in this session' });
    function drawDots() {

      var items = [];
      for (var i = 0; i < ses.length; i++) {
        (function (i) {
          var e = entry(i), on = i === at, isCur = i === S.curN;
          var label = 'Question ' + (i + 1) + (e ? (e.result.correct ? ', correct' : ', not correct') + (on ? ', shown now' : ', look back') : (isCur ? ', the question you are on' : ', not done yet'));
          items.push(h('button', { type: 'button', class: 'dot' + (e ? (e.result.correct ? ' good' : ' bad') : '') + (on ? ' now' : ''), 'aria-label': label, title: 'Question ' + (i + 1), 'aria-current': on ? 'step' : null, disabled: !e && !isCur,
            onclick: function () { if (isCur) { if (reviewing) viewSession(); } else if (e) viewSession(i); } }, String(i + 1)));
        })(i);
      }
      dotsEl.replaceChildren.apply(dotsEl, items);
    }
    var prevSlot = h('span');
    function drawPrev() {
      var o = olderOf(at);
      prevSlot.replaceChildren(o ? h('button', { class: 'linkbtn small', onclick: function () { viewSession(o.n); } }, '‹ Previous') : null);
    }

    // "Report a problem": a small link on every task, and a prompt under a wrong answer
    function reportedDone() { reportBtn.disabled = true; reportBtn.replaceChildren(icon('check'), h('span', null, 'Reported')); }
    function sendReport() {
      reportBtn.disabled = true;
      api('report', { item_id: it.id }).then(function () { state.reported[it.id] = true; reportedDone(); UI.toast('Reported. Thank you!'); })
        .catch(function (e) { reportBtn.disabled = false; UI.toast(e.message); });
    }
    var reportBtn = h('button', { type: 'button', class: 'linkbtn report-link', title: 'Report this question', onclick: sendReport },
      icon('flag'), h('span', null, 'Report'));
    if (state.reported[it.id]) reportedDone();
    var taskIdEl = state.user.role === 'teacher' ? h('span', { class: 'small muted taskid', title: 'Task ID' }, it.id) : null;

    var phaseLabel = ses.mode === 'placement' ? 'Placement test' : (ses.bonus ? 'Bonus · double XP' : (ses.comeback ? 'Second Chance' : 'Practice'));
    var done = ses.n;
    drawDots(); drawPrev();
    show(h('div', { class: 'sess' + (ses.comeback ? ' mode-chance' : '') },
      h('div', { class: 'sess-top' }, h('span', null, phaseLabel + ' · Question ' + (at + 1) + ' of ' + ses.length + (reviewing ? ' · looking back' : '')),
        h('span', { class: 'row', style: 'gap:16px;flex-wrap:nowrap' }, prevSlot, soundButton(), h('button', { class: 'linkbtn small', onclick: function () { stopSession(ses); } }, 'Stop'))),
      h('div', { class: 'progress', role: 'progressbar', 'aria-valuemin': '0', 'aria-valuemax': String(ses.length), 'aria-valuenow': String(done) }, h('i', { id: 'prog', style: 'width:' + Math.round(100 * done / ses.length) + '%' })),
      dotsEl,
      h('div', { class: 'card task' },
        h('h1', { class: 'sr' }, 'Question ' + (at + 1)),
        h('div', { class: 'meta' }, h('span', { class: 'pill dark', title: it.skill_label }, String(it.skill_label || '').replace(/\s*[(:].*$/, '')), ses.mode === 'placement' ? null : levelPill(it.level),   // no level or thinking-level labels in the test: they can worry a learner (teacher, 27 October)
          ses.mode === 'placement' ? null : h('span', { class: 'pill' }, catOf(it.kind)[1] + ' ' + catOf(it.kind)[0]), taskIdEl, reportBtn),
        qEl, area, h('div', { class: 'row', style: 'gap:18px' }, submit, ses.mode === 'placement' || rev ? null : skipBtn), feedback)));
    if (rev) {   // an answered task: put the answer back, lock it and show the feedback again
      var a = rev.ans;
      if (it.kind === 'mcq') area.querySelectorAll('input[type=radio]').forEach(function (r) { if (r.value === a) { r.checked = true; chosen = a; } });
      else if (board) board.set(a);
      else if (it.kind === 'gap') inputs.forEach(function (inp, i) { inp.value = (a && a[i]) || ''; fitBlank(inp); });
      else if (inputs[0]) { inputs[0].value = a || ''; if (it.kind === 'write') growBox(inputs[0]); }
      lock(); showFeedback(answeredNow ? S.last : { result: rev.result, done: false }, a);
      return;
    }
    var first = inputs[0] || (area.querySelector('input[type=radio]'));
    if (first && it.kind !== 'mcq') first.focus();
  }

  function stopSession(ses) {
    var m = UI.modal(h('div', null, h('h2', null, 'Stop now?'), h('p', null, 'Your answers so far are saved.'),
      h('div', { class: 'row' }, h('button', { class: 'btn', id: 'yes' }, 'Stop and see result'), h('button', { class: 'btn ghost', id: 'no' }, 'Keep going'))));
    m.el.querySelector('#no').onclick = m.close;
    m.el.querySelector('#yes').onclick = function () {
      m.close();
      api('session/quit', { session_id: ses.id }).then(function (r) {
        state.sess = null; state.lastSummary = r.summary; go('#/summary');
      }).catch(fail);
    };
  }

  /** Word-by-word comparison: the words that differ are marked in your answer (red) and in the right one (green). */
  function wordDiff(a, b) {
    var A = a.trim().split(/\s+/).filter(Boolean), B = b.trim().split(/\s+/).filter(Boolean);
    var n = function (w) { return w.toLowerCase().replace(/[^a-z0-9'’]/g, ''); };
    var L = A.map(function () { return new Array(B.length + 1).fill(0); }); L.push(new Array(B.length + 1).fill(0));
    for (var i = A.length - 1; i >= 0; i--) for (var j = B.length - 1; j >= 0; j--) L[i][j] = n(A[i]) === n(B[j]) ? L[i + 1][j + 1] + 1 : Math.max(L[i + 1][j], L[i][j + 1]);
    var keepA = {}, keepB = {}; i = 0; j = 0;
    while (i < A.length && j < B.length) { if (n(A[i]) === n(B[j])) { keepA[i++] = keepB[j++] = true; } else if (L[i + 1][j] >= L[i][j + 1]) i++; else j++; }
    var out = function (W, keep, cls) { var r = []; W.forEach(function (w, k) { if (k) r.push(' '); r.push(keep[k] ? w : h('mark', { class: cls }, w)); }); return r; };
    return [out(A, keepA, 'del'), out(B, keepB, 'ins')];
  }

  function ruleDetails(skillId, open, lv, flags) {
    var s = skillById(skillId); if (!s) return h('span');
    var name = (lv && s.rule_lv ? 'Atgādinājums: ' : 'Rule reminder: ') + s.label;
    return h('details', { class: 'rule' + (flags && flags.length ? ' flagged' : ''), open: false },
      h('summary', { 'aria-label': name, title: name }, h('span', { class: 'rule-q', 'aria-hidden': 'true' }, '?'), flags && flags.length ? h('span', { class: 'langswitch' }, flags) : null), ruleCard(s, lv));
  }

  /** "Negative: *don't / doesn't* + base verb: *I don't work.*" -> a label, the pattern as blocks (forms in gold, slots in grey) and the example below.
      A line without "+" stays a plain line. (UDL: the pattern can be seen, not only read; teacher, 28 October) */
  function formulaRow(x) {
    var t = String(x || '');
    if (t.indexOf(' + ') < 0) return h('div', { class: 'f-row f-plain' }, UI.rich(t));
    var label = '', example = '';
    var c = t.indexOf(': ');
    if (c > 0 && t.slice(0, c).indexOf(' + ') < 0) { label = t.slice(0, c); t = t.slice(c + 2); }
    var c2 = t.lastIndexOf(': ');
    if (c2 > 0 && t.slice(c2 + 2).indexOf(' + ') < 0) { example = t.slice(c2 + 2); t = t.slice(0, c2); }
    t = t.replace(/[.]$/, '');
    var parts = t.split(' + '), blocks = [];
    parts.forEach(function (p, i) {
      if (i) blocks.push(h('span', { class: 'f-plus', 'aria-hidden': 'true' }, '+'));
      var form = /^\*[^*]+\*$/.test(p.trim()) || /\*/.test(p);
      blocks.push(h('span', { class: 'f-blk' + (form ? ' f-form' : ''), }, UI.rich(p.trim().replace(/^\*([^*]+)\*$/, '$1'))));
    });
    return h('div', { class: 'f-row' }, label ? h('div', { class: 'f-label' }, UI.rich(label)) : null, h('div', { class: 'f-blocks' }, blocks),
      example ? h('div', { class: 'f-ex' }, '→ ', UI.rich(example)) : null);
  }
  /** New card layout (teacher, 28 October; authoring/cards2.py): [[x]] = the part of the form to notice, *x* = italics. */
  function hl(t) {
    var frag = document.createDocumentFragment();
    String(t || '').split(/\[\[|\]\]/).forEach(function (part, i) {
      if (!part) return;
      if (i % 2) { var b = document.createElement('b'); b.className = 'hl'; b.textContent = part; frag.appendChild(b); }
      else frag.appendChild(UI.rich(part));
    });
    return frag;
  }
  function richHl(t) {   // italics around a highlight: *I [[do]].* -> the whole sentence in italics, "do" coloured
    var out = document.createDocumentFragment();
    String(t || '').split('*').forEach(function (part, i) {
      if (!part) return;
      if (i % 2) { var em = document.createElement('em'); em.appendChild(hl(part)); out.appendChild(em); } else out.appendChild(hl(part));
    });
    return out;
  }
  var TL_X = { repeat: [18, 36, 54, 72, 90, 108], experience: [26, 46], recent: [70], point: [36], future: [100] };
  function timeline(kind, lv) {   // a small picture of the meaning: past - now - future
    var NS = 'http://www.w3.org/2000/svg';
    function el(n, a) { var e = document.createElementNS(NS, n); Object.keys(a).forEach(function (k) { e.setAttribute(k, a[k]); }); return e; }
    var svg = el('svg', { viewBox: '0 0 124 40', class: 'tl', 'aria-hidden': 'true' });
    svg.appendChild(el('line', { x1: 6, y1: 22, x2: 118, y2: 22, class: 'tl-axis' }));
    svg.appendChild(el('line', { x1: 80, y1: 12, x2: 80, y2: 30, class: 'tl-now' }));
    var t = el('text', { x: 80, y: 39, 'text-anchor': 'middle', class: 'tl-lbl' }); t.textContent = lv ? 'tagad' : 'now'; svg.appendChild(t);
    if (kind === 'always') svg.appendChild(el('line', { x1: 8, y1: 22, x2: 116, y2: 22, class: 'tl-bar' }));
    if (kind === 'upto') { svg.appendChild(el('line', { x1: 22, y1: 22, x2: 74, y2: 22, class: 'tl-bar' })); svg.appendChild(el('path', { d: 'M72 16 L80 22 L72 28 Z', class: 'tl-head' })); }
    if (kind === 'now') svg.appendChild(el('circle', { cx: 80, cy: 22, r: 5, class: 'tl-head' }));
    (TL_X[kind] || []).forEach(function (x) { svg.appendChild(el('path', { d: 'M' + (x - 4) + ' 18 L' + (x + 4) + ' 26 M' + (x + 4) + ' 18 L' + (x - 4) + ' 26', class: 'tl-x' })); });
    return svg;
  }
  function cellRich(c) {   // "description || example": the example on its own line, in italics; " ;; " = one more position with its own example (teacher, 28 October)
    var segs = String(c).split(' ;; ');
    return h('span', null, segs.map(function (seg, k) {
      var i = seg.indexOf('|| ');
      if (i < 0) return h('span', { class: 'rc-desc' }, richHl(seg));
      var d = seg.slice(0, i).trim();
      return h('span', { class: 'rc-seg' + (k ? ' more' : '') }, d ? h('span', { class: 'rc-desc' }, richHl(d)) : null, h('span', { class: 'rc-eg' }, richHl(seg.slice(i + 3))));
    }));
  }
  function badHl(t) {   // the wrong part of a wrong sentence: red and underlined, the rest plain
    var frag = document.createDocumentFragment();
    String(t || '').split(/\[\[|\]\]/).forEach(function (part, i) {
      if (!part) return;
      if (i % 2) { var b = document.createElement('b'); b.className = 'bad-hl'; b.textContent = part; frag.appendChild(b); } else frag.appendChild(document.createTextNode(part));
    });
    return frag;
  }
  function ruleCard2(v, lv, watch) {
    var parts = [];
    var T = lv ? { form: 'Kā to veido', bad: 'Biežākās kļūdas', use: 'Kad to lieto', watch: 'Uzmanies' } : { form: 'How to make it', bad: 'Typical mistakes', use: 'When we use it', watch: 'Watch out' };
    parts.push(h('h3', { class: 'rc-h' }, T.form));
    if (v.table) {
      parts.push(h('div', { class: 'rc-scroll rc-wide' + (v.table.plain ? ' rc-keep' : '') }, h('table', { class: 'rc-table' + (v.table.plain ? ' rc-plain' : '') },
        h('thead', null, h('tr', null, h('th', null, ''), v.table.cols.map(function (c, i) { return h('th', { class: 'c' + i }, c); }))),
        h('tbody', null, v.table.rows.map(function (r) {
          return h('tr', null, h('th', { scope: 'row' }, r[0]), r.slice(1).map(function (c, i) { return h('td', { class: 'c' + i }, hl(c)); }));
        })))));
      parts.push(h('div', { class: 'rc-stack' + (v.table.plain ? ' rc-plain' : '') }, v.table.cols.map(function (c, i) {   // the same table for a phone: one block per column
        return h('div', { class: 'rc-col c' + i }, h('div', { class: 'rc-col-h' }, c), v.table.rows.map(function (r) {
          return h('div', { class: 'rc-col-r' }, h('span', { class: 'who' }, r[0]), h('span', null, hl(r[i + 1])));
        }));
      })));
      if (v.table.short) parts.push(h('p', { class: 'rc-note' }, richHl(v.table.short)));
    }
    if (v.choice) {
      parts.push(h('div', { class: 'rc-scroll rc-wide' }, h('table', { class: 'rc-table rc-choice' },
        h('thead', null, h('tr', null, h('th', null, ''), v.choice.cols.map(function (c) { return h('th', { class: 'big' }, c); }))),
        h('tbody', null, v.choice.rows.map(function (r) {
          return h('tr', null, h('th', { scope: 'row' }, r[0]), r.slice(1).map(function (c) { return h('td', null, cellRich(c)); }));
        })))));
      parts.push(h('div', { class: 'rc-stack' }, v.choice.cols.map(function (c, i) {
        return h('div', { class: 'rc-col' }, h('div', { class: 'rc-col-h big' }, c), v.choice.rows.map(function (r) {
          return h('div', { class: 'rc-col-r' }, h('span', { class: 'who' }, r[0]), h('span', null, cellRich(r[i + 1])));
        }));
      })));
      if (v.choice.note) parts.push(h('p', { class: 'rc-note' }, richHl(v.choice.note)));
    }
    if (v.mistakes && v.mistakes.length) {
      parts.push(h('h3', { class: 'rc-h' }, T.bad));
      parts.push(h('div', { class: 'rc-bad' }, v.mistakes.map(function (m) {
        var marked = m[0].indexOf('[[') >= 0;   // the changed words are marked: no strike-through, only those words coloured
        return h('div', { class: 'rc-pair' + (marked ? ' marked' : '') }, h('span', { class: 'no' }, h('span', { class: 'mk', 'aria-label': lv ? 'nepareizi' : 'wrong' }, '✗'), marked ? h('em', null, badHl(m[0])) : h('s', null, m[0])),
          h('span', { class: 'yes' }, h('span', { class: 'mk', 'aria-label': lv ? 'pareizi' : 'right' }, '✓'), marked ? h('em', null, hl(m[1])) : m[1]),
          m[2] ? h('span', { class: 'rc-why' }, richHl(m[2])) : null);   // why Latvian speakers make this mistake
      })));
    }
    if (v.uses && v.uses.length) {
      parts.push(h('h3', { class: 'rc-h' }, T.use));
      v.uses.forEach(function (u) {
        parts.push(h('div', { class: 'rc-use' },
          h('div', { class: 'rc-use-top' }, h('div', null, h('b', { class: 'rc-use-t' }, richHl(u.t)),
            u.s && u.s.length ? h('div', { class: 'rc-sig' }, u.s.map(function (x) { return h('span', { class: 'chip' }, x); })) : null),
            u.tl ? timeline(u.tl, lv) : null),
          h('ul', { class: 'rc-ex' }, (u.ex || []).map(function (x) {   // "✗ ..." = a wrong example, in red
            if (x.indexOf('✗ ') === 0) return h('li', { class: 'rc-ex-bad' }, h('span', { class: 'mk', 'aria-label': lv ? 'nepareizi' : 'wrong' }, '✗ '), h('em', null, badHl(x.slice(2))));
            return h('li', null, h('em', null, hl(x)));
          }))));
      });
    }
    if (watch && watch.length) parts.push(h('div', { class: 'watch' }, h('b', null, '⚠ ', T.watch), h('ol', null, watch.map(function (x) { return h('li', null, richHl(x)); }))));
    return h('div', { class: 'rulecard rc2' }, parts);
  }
  function ruleCard(s, lv) {
    var r = lv && s.rule_lv ? s.rule_lv : s.rule, l = lv && s.rule_lv;
    if (r.v2) return ruleCard2(r.v2, !!l, r.watch);
    return h('div', { class: 'rulecard' },
      h('b', { style: 'color:var(--text)' }, l ? 'Kā to veido' : 'How to make it'), h('div', { class: 'formulas' }, r.form.map(formulaRow)),
      h('b', { style: 'color:var(--text)' }, l ? 'Kad to lieto' : 'When we use it'), h('ul', null, r.use.map(function (x) { return h('li', null, UI.rich(x)); })),
      r.watch && r.watch.length ? h('div', { class: 'watch' }, h('b', null, '⚠ ', l ? 'Uzmanies' : 'Watch out'), h('ol', null, r.watch.map(function (x) { return h('li', null, UI.rich(x)); }))) : null,
      h('p', { class: 'small' }, h('b', null, l ? 'Signālvārdi: ' : 'Signal words: '), UI.rich(r.signals)),
      h('div', { class: 'ex' }, h('b', null, l ? 'Piemērs: ' : 'Example: '), UI.rich(s.rule.example)));
  }

  // ───────── summary ─────────
  function viewSummary() {
    var s = state.lastSummary;
    if (!s) { location.hash = '#/home'; return; }
    setTimeout(function () { if (location.hash === '#/summary') guestInvite(false); }, 700);
    if (s.mode === 'placement') return summaryPlacement(s);
    var nodes = [];
    var fixed = s.fixed || 0;
    var headline = s.comeback
      ? (fixed ? 'Great job! ' + plural(fixed, 'mistake', 'mistakes') + ' fixed.' : 'Good try. Look at these again.')
      : (s.accuracy >= 80 ? 'Great work!' : (s.accuracy >= 50 ? 'Good effort!' : 'Keep going – this is how you learn.'));
    // real progress only: topics where this session went clearly better than the learner's recent history
    var better = (s.by_skill || []).filter(function (k) { var now = pct(k.correct, k.n); return k.prev_accuracy !== null && k.prev_accuracy !== undefined && k.n >= 3 && now >= k.prev_accuracy + 10; });
    var wins = [];
    if (fixed && !s.comeback) wins.push(h('li', null, icon('check'), (fixed === 1 ? '1 earlier mistake on these topics looks fixed.' : fixed + ' earlier mistakes on these topics look fixed.')));
    better.forEach(function (k) { wins.push(h('li', null, icon('up'), k.label + ': ' + k.prev_accuracy + '% → ' + pct(k.correct, k.n) + '%')); });
    if (s.fixed_total && s.fixed_total > fixed) wins.push(h('li', null, icon('flame'), 'Fixed so far: ' + s.fixed_total));
    nodes.push(h('div', { class: 'card', style: 'margin-bottom:16px' },
      h('div', { class: 'label' }, s.comeback ? 'Second Chance' : 'Practice finished'), h('h1', null, headline),
      wins.length ? h('ul', { class: 'clean wins' }, wins) : null,
      (s.comeback || fixed) ? h('p', { class: 'today' }, h('b', null, 'Today: '), plural(fixed, 'mistake', 'mistakes') + ' fixed', s.locked ? ', ' + s.locked + ' checked again' : '', s.next_topic ? [' · ', h('b', null, 'Next time: '), s.next_topic] : ' · nothing left to fix') : null,
      s.bonus ? bonusCard(s) : null,
      (s.open_after && !s.bonus) ? h('p', { class: 'row', style: 'gap:12px' }, h('span', { class: 'small muted' }, 'Still to fix: ' + s.open_after), comebackButton('btn small fn-chance', 'Second Chance')) : null,
      h('div', { class: 'grid g3' },
        h('div', null, h('div', { class: 'big' }, s.correct + '/' + s.n), h('div', { class: 'muted small' }, 'correct')),
        h('div', null, h('div', { class: 'big' }, '+' + s.xp), h('div', { class: 'muted small' }, 'XP points')),
        h('div', null, h('div', { class: 'big' }, s.accuracy + '%'), h('div', { class: 'muted small' }, 'accuracy')))));
    nodes.push(h('div', { class: 'grid g2', style: 'margin-bottom:16px' },
      h('div', { class: 'card' }, h('h2', null, 'By topic'), h('ul', { class: 'clean' }, s.by_skill.map(function (k) {
        return h('li', { style: 'margin-bottom:12px' }, h('div', { class: 'row between' }, h('b', { style: 'color:var(--text)' }, k.label), h('span', { class: 'pill dark' }, '≈ ' + lv(k.level_est))),
          h('div', { class: 'meter gold', style: 'margin:6px 0 3px' }, h('i', { style: 'width:' + pct(k.correct, k.n) + '%' })), h('span', { class: 'small muted' }, k.correct + ' of ' + k.n + ' correct'));
      }))),
      h('div', { class: 'card' }, h('h2', null, 'How you did'), catBars(s.by_cat))));
    var steps = s.next || [];
    nodes.push(h('div', { class: 'card', style: 'margin-bottom:16px' }, h('h2', null, 'What next?'),
      h('ul', { class: 'clean' }, steps.length ? steps.map(function (n) {
        return h('li', { style: 'margin-bottom:10px' }, h('div', { class: 'row between' }, h('span', null, n.text),
          n.type === 'review' ? h('button', { class: 'btn ghost small', onclick: function () { rulesModal(n.skill); } }, 'Rule card')
            : h('button', { class: 'btn small', onclick: function () { state.prefill = { skills: state.lastSkills || s.by_skill.map(function (k) { return k.id; }), level: n.level }; location.hash = '#/practice'; } }, 'Try harder')));
      }) : h('li', null, (feat('streak') ? 'Do another round to build your streak and see your level move.' : 'Do another round to see your level move.')))));
    nodes.push(h('div', { class: 'row' }, h('button', { class: 'btn', onclick: function () { state.prefill = { skills: s.by_skill.map(function (k) { return k.id; }), level: s.level }; location.hash = '#/practice'; } }, 'Practise again'), h('a', { class: 'btn ghost', href: '#/home' }, 'Home')));
    show(h('div', { class: 'sess', style: 'max-width:860px' }, nodes));
  }

  /** After Second Chance: 1 or 2 optional bonus questions for double XP (teacher's rule). Skipping is fine and says so. */
  function bonusCard(s) {
    var card = h('div', { class: 'card pad-s fn-bonus', style: 'margin:12px 0' });
    var go = h('button', { class: 'btn small', type: 'button' }, 'Try it');
    var no = h('button', { class: 'btn ghost small', type: 'button' }, 'Enough for today');
    go.addEventListener('click', function () {
      go.disabled = no.disabled = true; go.textContent = 'Starting…';
      api('session/bonus', { session_id: s.session_id }).then(function (r) { state.sess = newSess(r.session, r.item); location.hash = '#/session'; })
        .catch(function (e) { go.disabled = no.disabled = false; go.textContent = 'Try it'; UI.toast(e.message); });
    });
    no.addEventListener('click', function () { card.replaceChildren(h('b', { style: 'color:var(--text)' }, 'Done for today – well done!')); });
    card.append(h('div', { class: 'row between', style: 'gap:12px' },
      h('div', null, h('b', { style: 'color:var(--text)' }, 'Bonus: ' + plural(s.bonus, 'question', 'questions')), h('div', { class: 'small muted' }, 'Double XP')),
      h('span', { class: 'row', style: 'gap:8px' }, go, no)));
    return card;
  }

  function summaryPlacement(s) { show(h('div', { class: 'sess', style: 'max-width:860px' }, placementReport(s, true))); }

  function placementReport(s, fresh) {
    var nodes = [];
    var found = String(lv(s.overall_level)).slice(0, 2);   // the result as a big level on a dark card, the ladder under it, one gold button (teacher, 28 October)
    nodes.push(h('div', { class: 'card focus hero-card', style: 'margin-bottom:16px' },
      h('div', { class: 'hero-cheer' }, fresh ? 'Placement test finished' : 'Placement result'),
      h('div', { class: 'lvbig' }, lv(s.overall_level), h('small', null, 'your level')),
      (s.ladder && s.ladder.length) ? h('div', { class: 'ladder' }, s.ladder.map(function (l) { return h('span', { class: l.level === found ? 'on' : '' }, l.level, h('b', null, l.correct + '/' + l.n)); })) : null,
      h('a', { class: 'btn', href: '#/practice', style: 'margin-top:4px' }, 'Start practising', icon('arrow')),
      h('div', { class: 'hero-stats' }, h('span', null, icon('check'), h('b', null, s.correct + ' / ' + s.n), ' correct')),
      (s.sure === 'rough' && s.n < 20) ? h('p', { class: 'small muted' }, 'A short test gives a rough level. The Full test is more exact.') : h('p', { class: 'small muted' }, 'A guide, not an exam grade.'),
      s.overall_level === 'C1.2' ? h('p', { class: 'small muted' }, 'This is the top level in the app.') : null,
      (s.overall_level === 'A2.1' && !s.basics) ? h('p', { class: 'small muted' }, 'A2 is the first level here. Ask your teacher about easier material.') : null));
    var ng = s.gaps.length;
    if (s.basics) nodes.push(h('div', { class: 'card', style: 'margin-bottom:16px' }, h('div', { class: 'row between' },
      h('div', null, h('h2', { style: 'margin:0 0 4px' }, 'Start with A2 basics'), h('div', { class: 'small muted' }, 'Build the foundations first.')),
      h('button', { class: 'btn', onclick: function () { state.prefill = { skills: [], level: 'A2.1' }; location.hash = '#/practice'; } }, 'Practise A2'))));
    var weak = s.gaps.map(function (g) { return g.label; });
    var atLevel = s.n - s.correct - (s.parked || 0);   // missed above the level found: kept for later, not offered now
    var parkedNote = s.parked ? h('div', { class: 'small muted' }, plural(s.parked, 'harder question', 'harder questions') + ' you missed will come back when you practise that level.') : null;
    if (fresh && s.open_after && atLevel > 0) {
      nodes.push(h('div', { class: 'card fn-chance', style: 'margin-bottom:16px' }, h('div', { class: 'row between' },
        h('div', null, h('b', { style: 'color:var(--text)' }, plural(atLevel, 'mistake', 'mistakes') + ' at your level'), parkedNote,
          weak.length ? h('div', { class: 'small muted' }, 'Topics: ' + weak.join(', ') + '. A few questions cannot show a real gap; Second Chance does.') : null),
        comebackButton('btn small fn-chance', 'Second Chance'))));
    } else if (!s.basics) {
      nodes.push(h('div', { class: 'card', style: 'margin-bottom:16px' }, h('h2', null, 'No mistakes to fix'), h('p', { class: 'muted' }, s.parked ? 'Nothing to fix at your level.' : (s.n > s.correct ? 'Nothing left to fix.' : 'Nothing was missed.')), parkedNote,
        h('a', { class: 'btn', href: '#/practice' }, 'Practise')));
    }
    nodes.push(h('div', { class: 'card' }, h('h2', null, 'How you did'), catBars(s.by_cat)));   // the topics tested are on My learning path, where they can be opened
    nodes.push(h('div', { class: 'row', style: 'margin-top:16px' }, h('a', { class: 'btn ghost', href: '#/home' }, 'Home')));
    return nodes;
  }

  function showPlacementReport(rep) { state.lastSummary = rep; show(h('div', { class: 'sess', style: 'max-width:860px' }, placementReport(rep, false))); }

  // ───────── rules ─────────
  // Topic tiles (teacher, 27 October): a short, funny sentence per topic, the form in gold; the same tiles on Rules and Practice
  var TILE_LINES = {
    present_simple: 'My cat **ignores** me every morning.', present_continuous: "I**'m not procrastinating**. I**'m researching**.",
    past_simple: 'I **fell asleep** during the meeting.', past_continuous: 'At 3 a.m. I **was** still **scrolling**.',
    present_perfect: "I**'ve eaten** all the biscuits. Sorry.", present_perfect_continuous: "I**'ve been learning** this grammar rule all week.",
    past_perfect: 'By midnight, the cake **had disappeared**.', future: "I**'m going to** start my diet on Monday.",
    present_simple_passive: 'Most emails **are written** by AI now.', past_simple_passive: 'My password **was changed** by my cat.',
    present_continuous_passive: 'You **are being watched**. By your smartwatch.', present_perfect_passive: 'The coffee machine **has been fixed**! Finally.',
    future_passive: 'The cake **will be eaten** by midnight.', modal_verbs: "You **should** go to bed. It's 2 a.m.",
    comparison: 'My phone knows me **better than** I do.', cond_zero: 'If I **open** Instagram, I **lose** an hour.',
    cond_first: 'If I **say** "five minutes", it**\'ll** be an hour.', cond_second: "If I **had** a euro for every typo, I**'d** be rich.",
    cond_third: 'If you **had told** me it was a video call, I **would have brushed** my hair.', cond_mixed: 'If I **had bought** Bitcoin in 2010, I **would be** rich now.',
    cond_advanced: 'I **wish** AI **could** tidy my desk.', rep_statements: 'He said he **would call** me.',
    rep_questions: 'He asked where the coffee **was**.', rep_verbs: 'The AI **refused** to write my essay. Rude.',
    ind_polite: 'Could you tell me where the cake **is**?', ind_advanced: "I don't know **what to say**.",
    used_to: 'I **used to** read books. Now I read comments.', articles: '**An** elephant walked into **a** café.',
    quantity: "There's **not enough** coffee in this world.", relative_clauses: 'I have a friend **who** talks to plants.',
    time_clauses: "I'll call you **when** I **wake up**.", question_tags: "You love grammar, **don't you**?",
    subject_object_q: '**Who** ate my sandwich?', verb_patterns: 'I enjoy **doing** nothing.',
    more_modals: 'I **might** go to the gym tomorrow.', passive_modals: 'Some meetings **should be replaced** by emails.',
    causative: 'I **had** my CV **written** by AI. Oops.', two_objects: 'Give **me** the chocolate.',
    adj_ed_ing: "It's **confusing**. Even AI is **confused**.", adj_order: 'I wear my **comfortable old grey woollen** jumper to every video call.',
    adverbs: 'My colleague **hardly ever** works.', so_such: 'It was **such** a long meeting.',
    indefinite_pronouns: "I've got **nothing** to wear. Again.", dep_prepositions: "I'm good **at** sleeping.",
    agreement: 'Nobody **reads** the instructions.', irregular_plurals: '**Men** work hard. **Women** spend harder.',
    prep_time_place: 'See you **on** Friday **at** 8.'
  };
  function posterText(t) {   // **form** -> gold bold; the rest plain text (no markup from data becomes elements)
    return String(t || '').split('**').map(function (part, i) { return i % 2 ? h('b', null, part) : document.createTextNode(part); });
  }
  function topicTile(s, extra) {
    var ai = state.meta.skills.findIndex(function (k) { return k.id === s.id; });   // each tile its own colour, like a poster wall
    return h('span', { class: 'ttile' + (extra ? ' ' + extra : '') },
      h('span', { class: 'ttile-art pat' + (Math.max(0, ai) % 8) }, h('span', { class: 'ttile-lv' }, levelRange(s)), h('span', { class: 'ttile-line' }, posterText(TILE_LINES[s.id] || s.label))),
      h('span', { class: 'ttile-nm' }, s.label.replace(/\s*[(:].*$/, '')));
  }

  function viewRules() {
    var lv = state.user.lang === 'lv';
    function flagBtn(code) {   // the same flags as under the feedback, no words
      var on = (code === 'lv') === lv;
      return h('button', { type: 'button', class: 'langbtn ' + code + (on ? ' on' : ''), 'aria-pressed': on ? 'true' : 'false', 'aria-label': code === 'lv' ? 'Latviski' : 'English', title: code === 'lv' ? 'Latviski' : 'English', onclick: function () {
        if (on) return; state.user.lang = code; api('account/profile', { lang: code }).catch(function () {}); viewRules();
      } });
    }
    var toggle = h('span', { class: 'langswitch' }, flagBtn('lv'), flagBtn('en'));
    show(h('div', null, h('div', { class: 'hello' }, h('div', null, h('div', { class: 'label' }, 'Reference'), h('h1', { style: 'margin:0' }, 'Rule cards')), toggle),
      state.meta.areas.map(function (a, i) {   // tiles by area; a tile opens its rule card
        var list = state.meta.skills.filter(function (s) { return s.area === a.id; });
        if (!list.length) return null;
        return h('div', { class: 'area-block' }, h('h2', null, a.label), h('div', { class: 'tilegrid' }, list.map(function (s) {
          return h('button', { type: 'button', class: 'ttile-btn', onclick: function () { rulesModal(s.id); } }, topicTile(s));
        })));
      })));
  }
  function rulesModal(id) {
    var s = skillById(id);
    var go = h('button', { class: 'btn', type: 'button' }, 'Practise', icon('arrow'));   // straight from the rule to the tasks (teacher, 28 October)
    var m = UI.modal(h('div', null, h('h2', null, s.label), ruleCard(s, state.user.lang === 'lv'),
      h('div', { class: 'row', style: 'margin-top:14px;gap:10px' }, go, h('button', { class: 'btn ghost', id: 'c' }, 'Close'))));
    m.el.classList.add('modal-wide');   // room for the form table
    m.el.querySelector('#c').onclick = m.close;
    go.onclick = function () { var dash = state.dash; startTopic(go, Object.assign({}, s, (dash && dash.skills || []).find(function (k) { return k.id === s.id; }) || {}), dash); m.close(); };
  }

  /** Leaderboard avatar: with a mood, a small emoji sits on it and a tap shows the saying in a bubble. */
  document.addEventListener('click', function (e) {   // a tap anywhere else closes an open mood bubble
    if (e.target.closest && e.target.closest('.mood-av')) return;
    document.querySelectorAll('.mood-pop').forEach(function (p) { p.hidden = true; });
    document.querySelectorAll('.lb-row.pop-open').forEach(function (r) { r.classList.remove('pop-open'); });
  });
  function moodAvatar(x) {
    var av = UI.avatar(x.avatar, x.nickname, 30);
    var m = x.mood && MOODS[x.mood];
    if (!m) return av;
    var pop = h('span', { class: 'mood-pop', role: 'status', hidden: true }, m[0] + ' ' + m[1]);
    var btn = h('button', { type: 'button', class: 'mood-av', 'aria-label': x.nickname + ': ' + m[1], 'aria-expanded': 'false', onclick: function (e) {
      e.stopPropagation();
      var open = pop.hidden;
      document.querySelectorAll('.mood-pop').forEach(function (p) { p.hidden = true; });
      document.querySelectorAll('.mood-av').forEach(function (b) { b.setAttribute('aria-expanded', 'false'); });
      document.querySelectorAll('.lb-row.pop-open').forEach(function (r) { r.classList.remove('pop-open'); });
      pop.hidden = !open; btn.setAttribute('aria-expanded', String(open));
      var row = btn.closest('.lb-row'); if (row && open) row.classList.add('pop-open');   // above the next rows
    } }, av, h('span', { class: 'mood-dot', 'aria-hidden': 'true' }, m[0]));
    return h('span', { class: 'mood-wrap' }, btn, pop);
  }

  /** A medal for the top three: a ribbon and a coin with a rim and the place number; the coin shines now and then. */
  function medal(rank) {
    var c = [['#FFF1B8', '#E8C45A', '#A87A18'], ['#FFFFFF', '#C9D0D8', '#7F8995'], ['#FFE0C4', '#CD8A4F', '#7E4720']][rank - 1];
    var id = 'md' + rank + Math.random().toString(36).slice(2, 7);
    function S(tag, at, kids) { var e = document.createElementNS('http://www.w3.org/2000/svg', tag); for (var k in at) e.setAttribute(k, at[k]); (kids || []).forEach(function (x) { e.appendChild(x); }); return e; }
    var t = S('text', { x: 20, y: 35.5, 'text-anchor': 'middle', 'font-size': 12, 'font-weight': 800, 'font-family': 'Inter, system-ui, sans-serif', fill: rank === 2 ? '#2b3138' : '#3d2608' }); t.textContent = String(rank);
    var svg = S('svg', { viewBox: '0 0 40 48', width: 34, height: 41, 'aria-hidden': 'true' }, [
      S('path', { d: 'M9 0h9l5 14-6 6z', fill: '#1A7F70' }), S('path', { d: 'M31 0h-9l-5 14 6 6z', fill: '#C93A63' }),
      S('defs', {}, [S('radialGradient', { id: id, cx: '35%', cy: '30%', r: '75%' }, [S('stop', { offset: '0', 'stop-color': c[0] }), S('stop', { offset: '.55', 'stop-color': c[1] }), S('stop', { offset: '1', 'stop-color': c[2] })])]),
      S('circle', { cx: 20, cy: 31, r: 15, fill: c[2] }), S('circle', { cx: 20, cy: 31, r: 12.5, fill: 'url(#' + id + ')' }),
      S('circle', { cx: 20, cy: 31, r: 10, fill: 'none', stroke: c[2], 'stroke-opacity': '.45', 'stroke-dasharray': '1.5 1.8' }), t]);
    return h('span', { class: 'medal m' + rank, title: ['Gold', 'Silver', 'Bronze'][rank - 1] + ' medal' }, svg);
  }


  // ───────── leaderboard ─────────
  function viewLeaderboard() {
    if (!feat('leaderboard')) { location.hash = '#/home'; return; }
    var period = 'week';
    var holder = h('div');
    function load() {
      holder.replaceChildren(loading());
      api('leaderboard', undefined, { period: period }).then(function (r) {
        var rows = r.rows;
        // the top three get shining medals; the one who spent the most time thinking gets a clock badge (teacher, 27 October)
        var maxMin = rows.reduce(function (m, x) { return Math.max(m, x.minutes || 0); }, 0);
        // the fastest: most XP per minute, among those with at least 10 minutes (one lucky minute does not count)
        var fast = rows.filter(function (x) { return x.minutes >= 10; }).sort(function (a, b) { return b.xp / b.minutes - a.xp / a.minutes; })[0];
        var list = rows.length ? h('div', { class: 'card lb-card', style: 'padding:0' }, rows.map(function (x) {
          return h('div', { class: 'lb-row' + (x.me ? ' me' : '') }, x.rank <= 3 ? h('div', { class: 'lb-rank' }, medal(x.rank)) : h('div', { class: 'lb-rank' }, String(x.rank)),
            h('div', { class: 'lb-name' }, moodAvatar(x), h('span', { class: 'lb-text' }, x.nickname), x.me ? h('span', { class: 'pill', style: 'margin-left:8px' }, 'You') : null),
            h('div', { class: 'small muted num lb-min' }, (maxMin > 0 && x.minutes === maxMin) ? h('span', { class: 'thinking', title: 'Thinker of the week: most time spent thinking' }, h('i'), h('i'), h('i')) : null,
              (fast && fast === x) ? h('span', { class: 'supersonic', title: 'Supersonic: most XP per minute' }, icon('bolt')) : null, x.minutes + ' min'), h('div', { class: 'lb-xp' }, x.xp + ' XP'));
        })) : h('div', { class: 'card empty' }, h('p', null, period === 'week' ? 'No points yet this week. Be the first!' : 'No points yet.'), h('a', { class: 'btn', href: '#/practice' }, 'Practise now'));
        holder.replaceChildren(
          list,
          (r.me && r.me.rank > 20) ? h('div', { class: 'card pad-s', style: 'margin-top:12px' }, 'Your rank: ', h('b', { style: 'color:var(--text)' }, '#' + r.me.rank), ' · ' + r.me.xp + ' XP') : null,
          r.guest ? h('div', { class: 'card pad-s row between', style: 'margin-top:12px' }, h('b', { style: 'color:var(--text)' }, 'Guests are not ranked.'),
            state.config.register_url ? registerLink('btn small', 'Create account') : null)
          : ((r.hidden && state.user.role !== 'teacher') ? h('p', { class: 'small muted', style: 'margin-top:12px' }, 'You are hidden from the leaderboard.') : null));
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
      h('div', { class: 'field' }, h('label', { for: 'pn' }, guest ? 'Your name' : 'Display name'), nick),
      (guest || !feat('leaderboard')) ? null : h('div', { class: 'field' }, h('label', { style: 'display:flex;gap:10px;align-items:center;font-weight:500' }, board, 'Show me on the leaderboard')),
      msg, h('button', { class: 'btn', type: 'submit' }, 'Save'));

    var cards = [];
    if (guest) cards.push(guestBanner());
    cards.push(avatarCard());
    if (!state.user.guest && feat('leaderboard')) cards.push(moodCard());   // only people on the leaderboard can be seen by others
    cards.push(langCard());
    cards.push(soundCard());
    var study = studyProfileCard(); if (study) cards.push(study);
    var pic = installCard(true); if (pic) cards.push(pic);
    cards.push(h('div', { class: 'card' }, h('h2', null, 'Profile'), profile));
    if (!guest && !u.track_time) cards.push(h('div', { class: 'card pad-s' }, h('b', { style: 'color:var(--text)' }, 'Time tracking is off '), '(set on englishfever.com). Your answers are still saved.'));
    cards.push(h('div', { class: 'card' }, h('h2', null, 'Your data'),
      h('div', { class: 'row' },
        h('button', { class: 'btn ghost small', onclick: function () {
          api('account/export').then(function (d) { var a = h('a', { href: URL.createObjectURL(new Blob([JSON.stringify(d, null, 2)], { type: 'application/json' })), download: 'my-practice-data.json' }); document.body.appendChild(a); a.click(); a.remove(); }).catch(fail);
        } }, 'Download my data'),
        h('button', { class: 'btn ghost small', onclick: deleteAccount }, 'Delete my results'),
        h('a', { href: state.config.privacy_url, target: '_blank', rel: 'noopener', class: 'small' }, 'Privacy policy'))));
    cards.push(h('div', null, h('button', { class: 'btn ghost', onclick: function () {
      api('logout', {}).then(function () { state.user = null; state.dash = null; stopHeartbeat(); go('#/'); });
    } }, icon('logout'), guest ? 'Quit' : 'Sign out')));
    show(h('div', { class: 'sess', style: 'max-width:620px' }, h('div', { class: 'hello' }, h('div', null, h('div', { class: 'label' }, guest ? 'Guest' : 'Account'), h('h1', { style: 'margin:0' }, u.nickname))), h('div', { class: 'grid' }, cards)));
  }

  /** A small speaker button in a practice session. Sounds are off until switched on (here or in Profile). */
  function soundButton() {
    var b = h('button', { type: 'button', class: 'linkbtn small speaker' });
    function draw() {
      var on = Sound.on();
      b.replaceChildren(icon(on ? 'volume' : 'mute'));
      b.setAttribute('aria-pressed', String(on));
      b.setAttribute('aria-label', on ? 'Sound is on. Press to turn it off.' : 'Sound is off. Press to turn it on.');
      b.title = on ? 'Sound on' : 'Sound off';
    }
    b.addEventListener('click', function () { Sound.set(!Sound.on()); if (Sound.on()) Sound.play('right'); draw(); });
    draw();
    return b;
  }

  /** Profile: sounds, off by default; kept on this device. */
  function soundCard() {
    var cb = h('input', { type: 'checkbox', id: 'snd', checked: Sound.on(), onchange: function () { Sound.set(cb.checked); if (cb.checked) Sound.play('right'); } });
    // an icon and a switch, no explanation (teacher, 27 October: people know these signs)
    return h('div', { class: 'card pad-s row between', style: 'flex-wrap:nowrap' }, h('span', { class: 'sound-ic', 'aria-hidden': 'true' }, icon('volume')),
      h('label', { class: 'switch', title: 'Sound on / off' }, cb, h('i'), h('span', { class: 'sr' }, 'Sound for right and wrong answers')));
  }

  /** Grammar explanations in English or Latvian (Latvian is written for levels up to B1.2). */
  function langCard() {
    var msg = h('span', { class: 'small muted', role: 'status' });
    var seg = h('div', { class: 'seg', role: 'radiogroup', 'aria-label': 'Language of the explanations' }, [['en', 'English'], ['lv', 'Latviešu']].map(function (o) {
      return h('label', null, h('input', { type: 'radio', name: 'lang', value: o[0], checked: (state.user.lang || 'en') === o[0], onchange: function () {
        state.user.lang = o[0];
        api('account/profile', { lang: o[0] }).then(function () { msg.textContent = 'Saved'; }).catch(function () {});
      } }), h('span', null, o[1]));
    }));
    return h('div', { class: 'card' }, h('h2', null, 'Explanations'), h('div', { class: 'row' }, seg, msg), h('p', { class: 'small muted', style: 'margin:10px 0 0' }, 'Latvian: levels up to B1.2.'));
  }

  /** Choose a character, symbol or initial and a background colour. Collapsed until "Change" is pressed. */
  // Mood sayings (teacher, 27 October): chosen from this list in Profile, seen by others on the leaderboard (tap the avatar)
  var MOODS = { fire: ['🔥', 'On fire'], unstoppable: ['🚀', 'Unstoppable'], thinking: ['🤔', 'Thinking hard'], confused: ['😵‍💫', 'Confused but trying'],
    coffee: ['☕', 'Powered by coffee'], turtle: ['🐢', 'Slow but sure'], loading: ['🧠', 'Brain loading…'], boss: ['😎', 'Grammar boss'],
    perfect: ['🙃', 'Present Perfectly confused'], onemore: ['📚', 'Just one more question'], sleep: ['💤', 'Should be sleeping'], unicorn: ['🦄', 'Irregular, like my verbs'] };
  function moodCard() {
    var grid = h('div', { class: 'moods' });
    function draw() {
      grid.replaceChildren.apply(grid, Object.keys(MOODS).map(function (k) {
        var on = state.user.mood === k;
        return h('button', { type: 'button', class: 'mood' + (on ? ' on' : ''), 'aria-pressed': on ? 'true' : 'false', onclick: function () {
          var next = on ? null : k;
          api('account/profile', { mood: next }).then(function (r) { state.user = r.user; draw(); }).catch(function (e) { UI.toast(e.message); });
        } }, h('span', { class: 'mood-em', 'aria-hidden': 'true' }, MOODS[k][0]), MOODS[k][1]);
      }));
    }
    draw();
    return h('div', { class: 'card' }, h('h2', null, 'Your mood'), grid);
  }

  function avatarCard() {
    var u = state.user, cur = (u.avatar || '').split('-');
    var pick = { pic: cur[0] || 'ember', color: cur[1] || 'raspberry' };
    var open = false;
    var head = h('div', { class: 'row between', style: 'flex-wrap:nowrap' });
    var panel = h('div', { class: 'avpanel', hidden: true });
    var toggle = h('button', { type: 'button', class: 'btn ghost small', 'aria-expanded': 'false', 'aria-controls': 'avpanel', onclick: function () { setOpen(!open); } });
    panel.id = 'avpanel';
    var msg = h('div');
    function setOpen(v) {
      open = v; panel.hidden = !v; toggle.setAttribute('aria-expanded', String(v)); toggle.textContent = v ? 'Close' : 'Change';
      if (v) { var c = u.avatar ? u.avatar.split('-') : []; pick.pic = c[0] || pick.pic; pick.color = c[1] || pick.color; drawPanel(); }
    }
    function group(title, pics) {
      return h('div', { class: 'avgroup' }, h('div', { class: 'label' }, title),
        h('div', { class: 'avgrid', role: 'radiogroup', 'aria-label': title }, pics.map(function (g) {
          return h('button', { type: 'button', class: 'avopt', role: 'radio', 'aria-checked': String(g === pick.pic), 'aria-label': UI.AV_NAMES[g], title: UI.AV_NAMES[g], onclick: function () { pick.pic = g; drawPanel(); } }, UI.avatar(g + '-' + pick.color, u.nickname, 50));
        })));
    }
    function drawPanel() {
      panel.replaceChildren(
        group('Halloween', UI.AV_HALLOWEEN), group('People', UI.AV_PEOPLE), group('Characters', UI.AV_FUN), group('Symbols', UI.AV_GLYPHS.concat(['initial'])),
        h('div', { class: 'avgroup' }, h('div', { class: 'label' }, 'Background'),
          h('div', { class: 'avcolors', role: 'radiogroup', 'aria-label': 'Background colour' }, UI.AV_COLORS.map(function (c) {
            return h('button', { type: 'button', class: 'avcolor', role: 'radio', 'aria-checked': String(c === pick.color), 'aria-label': UI.AV_NAMES[c], title: UI.AV_NAMES[c], style: 'background:' + UI.AV_COLOR_VALUES[c][0], onclick: function () { pick.color = c; drawPanel(); } });
          }))),
        msg, h('div', { class: 'row', style: 'margin-top:14px' }, h('button', { type: 'button', class: 'btn small', onclick: save }, 'Save')));
    }
    function drawHead() {
      head.replaceChildren(h('div', { class: 'row', style: 'gap:14px;flex-wrap:nowrap' }, UI.avatar(u.avatar, u.nickname, 56), h('h2', { style: 'margin:0' }, 'Your avatar')), toggle);
    }
    function save() {
      msg.replaceChildren();
      api('account/profile', { avatar: pick.pic + '-' + pick.color }).then(function (r) {
        state.user = r.user; u = r.user; renderChrome('#/profile'); drawHead(); setOpen(false); UI.toast('Avatar saved');
      }).catch(function (e) { msg.replaceChildren(h('div', { class: 'err', role: 'alert' }, e.message)); });
    }
    drawHead(); setOpen(false);
    return h('div', { class: 'card' }, head, panel);
  }

  function deleteAccount() {
    var em = h('div');
    var m = UI.modal(h('div', null, h('h2', null, 'Delete your results?'), h('p', null, 'This deletes your results and profile in the practice app. It cannot be undone.'), em,
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
      h('form', { onsubmit: function (e) {
        e.preventDefault();
        api('account/profile', { nickname: nick.value, show_on_board: board.checked }).then(function (r) { state.user = r.user; go('#/home'); }).catch(function (er) { msg.replaceChildren(h('div', { class: 'err', role: 'alert' }, er.message)); });
      } }, h('div', { class: 'field' }, h('label', { for: 'fn' }, 'Name'), nick, h('p', { class: 'small muted', style: 'margin:6px 0 0' }, 'Only this name is shown to other learners. It is your first name; you can change it to a nickname.')),
        h('div', { class: 'field' }, h('label', { style: 'display:flex;gap:10px;align-items:center;font-weight:500' }, board, 'Show me on the leaderboard')), msg,
        h('button', { class: 'btn block', type: 'submit' }, 'Continue'))));
  }

  // ───────── teacher ─────────
  function viewTeacher() {
    api('teacher/students').then(function (r) {
      var all = r.students, sortKey = 'last_seen', dir = -1, q = '';
      // who the list shows: my students (enrolled in my Tutor courses, or added by me), all registered users, or everyone including guests
      var VIEWS = [['mine', 'My students'], ['registered', 'Registered'], ['all', 'Everyone']];
      function inView(s, v) { return v === 'all' || (v === 'registered' && s.provider !== 'guest') || (v === 'mine' && !!s.mine); }
      var view = null; try { view = localStorage.getItem('ef_tview'); } catch (e) {}
      if (!VIEWS.some(function (x) { return x[0] === view; })) view = all.some(function (s) { return s.mine; }) ? 'mine' : 'registered';
      var statsBox = h('div', { class: 'grid g4', style: 'margin-bottom:16px' });
      var exportLink = h('a', { class: 'btn ghost small', download: '' }, 'Export answers (CSV)');
      var tabs = h('div', { class: 'tabs', role: 'tablist', style: 'max-width:520px' });
      function drawTabs() {
        tabs.replaceChildren.apply(tabs, VIEWS.map(function (x) {
          var n = all.filter(function (s) { return inView(s, x[0]); }).length;
          return h('button', { role: 'tab', 'aria-selected': String(x[0] === view), onclick: function () { view = x[0]; try { localStorage.setItem('ef_tview', view); } catch (e) {} draw(); } }, x[1] + ' (' + n + ')');
        }));
      }
      function drawStats(list) {
        var weekActive = list.filter(function (s) { return s.week_answers > 0; }).length;
        var withAcc = list.filter(function (s) { return s.accuracy !== null; });
        var avg = withAcc.length ? Math.round(withAcc.reduce(function (a, s) { return a + s.accuracy; }, 0) / withAcc.length) : null;
        var weekMin = list.reduce(function (a, s) { return a + s.week_minutes; }, 0);
        statsBox.replaceChildren(stat('users', list.length, view === 'all' ? 'learners' : (view === 'mine' ? 'my students' : 'registered')), stat('flame', weekActive, 'active this week'), stat('check', avg === null ? '–' : avg + '%', 'average correct'), stat('clock', UI.fmtDuration(weekMin * 60), 'practised this week'));
      }
      var tbody = h('tbody');
      var cols = [
        ['nickname', 'Student'], ['level_est', 'Level'], ['last_seen', 'Last active'], ['week_minutes', 'Week (min)', 'r'], ['week_answers', 'Week questions', 'r'],
        ['total_minutes', 'Total (min)', 'r'], ['xp', 'XP', 'r'], ['accuracy', 'Correct', 'r'], ['streak', 'Streak', 'r'],
      ];
      var thead = h('thead', null, h('tr', null, cols.map(function (c) {
        return h('th', { class: c[2] || '', 'data-k': c[0], tabindex: '0', role: 'columnheader', onclick: function () { sortBy(c[0]); }, onkeydown: function (e) { if (e.key === 'Enter') sortBy(c[0]); } }, c[1]);
      })));
      function sortBy(k) { if (sortKey === k) dir = -dir; else { sortKey = k; dir = (k === 'nickname' || k === 'level_est') ? 1 : -1; } draw(); }
      function draw() {
        thead.querySelectorAll('th').forEach(function (t) { if (t.getAttribute('data-k') === sortKey) t.setAttribute('aria-sort', dir > 0 ? 'ascending' : 'descending'); else t.removeAttribute('aria-sort'); });
        drawTabs(); drawStats(all.filter(function (s) { return inView(s, view); }));
        exportLink.href = 'api.php?r=teacher/export&view=' + view;
        var rows = all.filter(function (s) { return inView(s, view) && (!q || (s.nickname + ' ' + (s.full_name || '')).toLowerCase().indexOf(q) >= 0); });
        rows.sort(function (a, b) {
          var x = a[sortKey], y = b[sortKey];
          if (x === null || x === undefined) x = (typeof y === 'string') ? '' : -1;
          if (y === null || y === undefined) y = (typeof x === 'string') ? '' : -1;
          if (typeof x === 'string') return dir * x.localeCompare(y);
          return dir * (x - y);
        });
        tbody.replaceChildren.apply(tbody, rows.length ? rows.map(function (s) {
          return h('tr', null,
            h('td', { class: 'name' }, h('span', { class: 'row', style: 'gap:10px;flex-wrap:nowrap' }, UI.avatar(s.avatar, s.nickname, 26), h('a', { href: '#/teacher/student/' + s.id }, s.nickname)), s.provider === 'guest' ? h('span', { class: 'pill', style: 'margin-left:8px' }, 'guest') : null, s.full_name && s.full_name !== s.nickname ? h('div', { class: 'small muted' }, s.full_name) : null, s.provider === 'guest' ? h('div', { class: 'small muted' }, 'first seen ' + UI.fmtAgo(s.joined)) : null),
            h('td', null, s.placement_level ? h('span', { class: 'pill dark', title: 'Placement test' }, lv(s.placement_level)) : null,
              s.placement_at ? h('span', { class: 'small muted' }, ' ' + new Date(s.placement_at * 1000).toLocaleDateString(undefined, { day: 'numeric', month: 'short' })) : null,
              s.level_est ? h('div', { class: 'small muted', title: 'Estimate from practice answers' }, 'practice ≈ ' + lv(s.level_est)) : (s.placement_level ? null : h('span', { class: 'muted' }, '–'))),
            h('td', null, UI.fmtAgo(s.last_seen)), h('td', { class: 'r num' }, String(s.week_minutes)), h('td', { class: 'r num' }, String(s.week_answers)),
            h('td', { class: 'r num' }, String(s.total_minutes)), h('td', { class: 'r num' }, String(s.xp)),
            h('td', { class: 'r num' }, s.accuracy === null ? '–' : s.accuracy + '%'), h('td', { class: 'r num' }, String(s.streak)));
        }) : [h('tr', null, h('td', { colspan: String(cols.length), class: 'empty' }, q ? 'No one matches.' : (view === 'mine' ? 'No students here yet. Open a learner and choose “Add to my students”.' : 'No learners yet. Share the practice link.')))]);
      }
      var search = h('input', { type: 'text', placeholder: 'Search students', 'aria-label': 'Search students', style: 'max-width:260px', oninput: function () { q = search.value.trim().toLowerCase(); draw(); } });
      draw();
      api('teacher/sync-status').then(function (st) {
        var box = document.getElementById('syncbox');
        if (!box || !st.configured) return;
        var bad = !!st.last_error;
        box.replaceChildren(h('div', { class: 'card pad-s', style: 'margin-bottom:14px;' + (bad ? 'border-color:var(--bad)' : '') },
          h('b', { style: 'color:var(--text)' }, 'Website activity tracker: '), bad ? 'problem' : (st.last_ok ? 'connected' : 'waiting for the first practice session'),
          st.last_ok ? h('span', { class: 'small muted' }, ' · last sent ' + UI.fmtAgo(st.last_ok)) : null,
          st.students_waiting ? h('span', { class: 'small muted' }, ' · ' + st.students_waiting + ' waiting') : null,
          bad ? h('div', { class: 'small', style: 'margin-top:6px;color:var(--bad)' }, st.last_error) : null));
      }).catch(function () {});
      api('teacher/research').then(function (st) {
        var box = document.getElementById('researchbox');
        if (!box || !(st.enabled || st.joined)) return;
        function dl(file, label) { return h('a', { class: 'btn ghost small', href: 'api.php?r=teacher/research-export&file=' + file, download: '' }, label); }
        box.replaceChildren(h('div', { class: 'card', style: 'margin-bottom:14px' },
          h('div', { class: 'label' }, 'Learning study'),
          h('p', { style: 'margin:4px 0 8px' }, h('b', { style: 'color:var(--text)' }, st.joined + ' of ' + st.registered), ' registered learners take part (' + st.declined + ' said no).' + (st.enabled ? '' : ' The study is switched off in config.php; people can still leave and you can still download.')),
          st.factors.length ? h('ul', { class: 'clean small', style: 'margin:0 0 10px' }, st.factors.map(function (f) { return h('li', null, f.label + ': ' + f.on + ' see it, ' + f.off + ' do not'); }))
            : h('p', { class: 'small muted', style: 'margin:0 0 10px' }, 'No conditions switched on. Add them under “experiments” in config.php.'),
          h('div', { class: 'row' }, dl('people', 'People (CSV)'), dl('days', 'Days (CSV)'), dl('answers', 'Answers (CSV)'), dl('readme', 'Read me (TXT)')),
          h('p', { class: 'small muted', style: 'margin:10px 0 0' }, 'No names in these files. Data starts at each person’s consent.')));
      }).catch(function () {});
      show(h('div', null,
        h('div', { class: 'hello' }, h('div', null, h('div', { class: 'label' }, 'Teacher'), h('h1', { style: 'margin:0' }, 'Students')),
          h('span', { class: 'row', style: 'gap:14px' }, h('a', { class: 'linkbtn small', href: '#/evidence' }, 'Learning evidence'), exportLink)),
        tabs, statsBox,
        h('div', { id: 'syncbox' }),
        h('div', { id: 'researchbox' }),
        h('div', { class: 'row', style: 'margin-bottom:12px' }, search),
        h('div', { class: 'tablewrap' }, h('table', null, thead, tbody))));
    }).catch(fail);
  }

  function viewTeacherStudent(id) {
    api('teacher/student', undefined, { id: id }).then(function (r) {
      var u = r.user, d = r.dashboard;
      var again = function () { viewTeacherStudent(id); };
      var moder = h('div', { class: 'row' },
        u.provider === 'guest' ? null : h('button', { class: 'btn ghost small', onclick: function () { api('teacher/moderate', { user_id: u.id, hide: !u.board_hidden }).then(again).catch(fail); } }, u.board_hidden ? 'Show on leaderboard' : 'Hide from leaderboard'),
        u.mine === 'course' ? h('span', { class: 'pill good' }, 'In your Tutor course')
          : h('button', { class: 'btn ghost small', onclick: function () { api('teacher/mine', { user_id: u.id, mine: u.mine !== 'added' }).then(again).catch(fail); } }, u.mine === 'added' ? 'Remove from my students' : 'Add to my students'),
        h('button', { class: 'btn ghost small', onclick: function () { if (confirm('Replace this name with "Learner ####"?')) api('teacher/moderate', { user_id: u.id, reset_name: true }).then(again).catch(fail); } }, 'Reset name'));
      var maxMin = Math.max.apply(null, r.days.map(function (x) { return x.minutes; }).concat([5]));
      var days = h('div', { class: 'bars', style: 'height:100px', role: 'img', 'aria-label': 'Minutes per day, last 30 days' }, r.days.map(function (x, i) {
        return h('div', { class: 'b', title: x.day + ': ' + x.minutes + ' min, ' + x.answers + ' questions' }, h('div', { class: 'col' + (i === r.days.length - 1 ? ' today' : ''), style: 'max-width:14px;height:' + Math.max(3, Math.round(80 * x.minutes / maxMin)) + 'px' }));
      }));
      var skillRows = d.skills.filter(function (s) { return s.n > 0; }).map(function (s) {
        return h('tr', null, h('td', null, s.label), h('td', null, areaLabel(s.area)), h('td', null, s.level_est ? h('span', { class: 'pill dark' }, '≈ ' + lv(s.level_est)) : h('span', { class: 'muted' }, 'few tasks')), h('td', { class: 'r num' }, String(s.n)), h('td', { class: 'r num' }, s.accuracy + '%'));
      });
      var rep = d.placement && d.placement.report;
      show(h('div', null,
        h('a', { href: '#/teacher', class: 'small' }, '← All students'),
        h('div', { class: 'hello', style: 'margin-top:8px' }, h('div', { class: 'row', style: 'gap:14px;flex-wrap:nowrap' }, UI.avatar(u.avatar, u.nickname, 56), h('div', null, h('div', { class: 'label' }, 'Student'), h('h1', { style: 'margin:0' }, u.nickname), h('p', { class: 'muted small' }, (u.full_name ? u.full_name + ' · ' : '') + (u.provider === 'guest' ? 'guest (not registered)' : 'englishfever.com account') + ' · joined ' + UI.fmtAgo(u.joined) + ' · last active ' + UI.fmtAgo(u.last_seen)))), moder),
        h('div', { class: 'grid g4', style: 'margin-bottom:16px' }, stat('clock', UI.fmtDuration(d.totals.seconds), 'time practised'), stat('check', d.totals.accuracy === null ? '–' : d.totals.accuracy + '%', 'correct (' + d.totals.answers + ' tasks)'), stat('flame', d.streak.current + ' / ' + d.streak.best, 'streak (best)'), stat('bolt', d.totals.xp, 'XP')),
        h('div', { class: 'grid g2', style: 'margin-bottom:16px' },
          h('div', { class: 'card' }, h('h2', null, 'Last 30 days'), days),
          h('div', { class: 'card' }, h('h2', null, 'Thinking levels'), bloomBars(d.bloom))),
        rep ? h('div', { class: 'card', style: 'margin-bottom:16px' }, h('h2', null, 'Placement test'), h('p', null, 'Level: ', h('span', { class: 'levelbadge', style: 'font-size:1.1rem;padding:3px 12px' }, rep.overall_level), ' · ' + UI.fmtAgo(d.placement.at) + ' · ' + rep.correct + '/' + rep.n + ' correct'),
          h('p', { class: 'small' }, h('b', null, 'Gaps: '), rep.gaps.map(function (g) { return g.label + ' (' + g.level + ')'; }).join(', '))) : null,
        h('div', { class: 'card', style: 'margin-bottom:16px;padding:0;overflow:hidden' }, h('h2', { style: 'padding:18px 18px 0' }, 'Topics'),
          skillRows.length ? h('div', { class: 'tablewrap', style: 'border:0;border-radius:0' }, h('table', null, h('thead', null, h('tr', null, ['Topic', 'Area', 'Level', 'Questions', 'Correct'].map(function (t, i) { return h('th', { class: i > 2 ? 'r' : '' }, t); }))), h('tbody', null, skillRows))) : h('p', { class: 'empty' }, 'No tasks done yet.')),
        h('div', { class: 'card', style: 'padding:0;overflow:hidden' }, h('h2', { style: 'padding:18px 18px 0' }, 'Recent answers'),
          r.recent.length ? h('div', { class: 'tablewrap', style: 'border:0;border-radius:0' }, h('table', null, h('thead', null, h('tr', null, ['When', 'Question', 'Answer', '', 'Level', 'Thinking', 'Sec'].map(function (t) { return h('th', null, t); }))),
            h('tbody', null, r.recent.map(function (a) {
              return h('tr', null, h('td', { class: 'small' }, UI.fmtDate(a.at)), h('td', { style: 'max-width:340px;overflow:hidden;text-overflow:ellipsis' }, a.q, h('div', { class: 'small muted' }, a.id)),
                h('td', { style: 'max-width:260px' }, a.answer || '', a.key ? h('div', { class: 'small muted' }, 'Expected: ' + a.key) : null, a.note ? h('div', { class: 'small note-tip' }, 'Accepted with a tip: ' + a.note) : null),
                h('td', null, h('span', { class: 'pill ' + (a.correct ? 'good' : 'pink') }, a.correct ? '✓' : '✗')), h('td', null, a.level), h('td', null, bloomName(a.bloom)), h('td', { class: 'num' }, String(a.seconds)));
            })))) : h('p', { class: 'empty' }, 'No answers yet.'))));
    }).catch(fail);
  }

  boot();
})();
