// Small DOM helpers, icons and the API client. No frameworks, no third-party requests.
(function () {
  'use strict';

  function h(tag, props) {
    var el = document.createElement(tag);
    props = props || {};
    Object.keys(props).forEach(function (k) {
      var v = props[k];
      if (v === null || v === undefined || v === false) return;
      if (k === 'class') el.className = v;
      else if (k.slice(0, 2) === 'on' && typeof v === 'function') el.addEventListener(k.slice(2), v);
      else if (k === 'value' || k === 'checked' || k === 'disabled' || k === 'selected' || k === 'open') el[k] = v;
      else el.setAttribute(k, v === true ? '' : v);
    });
    for (var i = 2; i < arguments.length; i++) append(el, arguments[i]);
    return el;
  }

  function append(el, kid) {
    if (kid === null || kid === undefined || kid === false) return;
    if (Array.isArray(kid)) kid.forEach(function (k) { append(el, k); });
    else if (kid instanceof Node) el.appendChild(kid);
    else el.appendChild(document.createTextNode(String(kid)));
  }

  // replaceChildren(null) would insert the text "null"; skip empty values like h() does
  var origReplace = Element.prototype.replaceChildren;
  Element.prototype.replaceChildren = function () {
    var kids = Array.prototype.slice.call(arguments).filter(function (k) { return k !== null && k !== undefined && k !== false; });
    return origReplace.apply(this, kids);
  };

  var ICONS = {
    flame: '<path d="M12 3c1 3.5 5 5.5 5 10a5 5 0 0 1-10 0c0-2 1-3.2 2-4 .3 1.2 1 2 2 2 0-3-1-5 1-8z"/>',
    clock: '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    bolt: '<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>',
    trophy: '<path d="M8 4h8v5a4 4 0 0 1-8 0zM8 6H5a3 3 0 0 0 3 4M16 6h3a3 3 0 0 1-3 4M12 13v4M8 21h8M10 17h4"/>',
    user: '<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/>',
    home: '<path d="M3 11 12 3l9 8M5 10v10h5v-6h4v6h5V10"/>',
    target: '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>',
    users: '<circle cx="9" cy="8" r="3.5"/><path d="M2 20c0-3.5 3-5.5 7-5.5s7 2 7 5.5M16 5a3.5 3.5 0 0 1 0 7M18 14.5c2.5.6 4 2.3 4 5.5"/>',
    check: '<path d="m5 12 5 5 9-10"/>',
    cross: '<path d="M6 6l12 12M18 6 6 18"/>',
    arrow: '<path d="M5 12h14M13 6l6 6-6 6"/>',
    up: '<path d="m6 14 6-6 6 6"/>',
    down: '<path d="m6 10 6 6 6-6"/>',
    book: '<path d="M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2zM4 19a2 2 0 0 1 2-2h13"/>',
    logout: '<path d="M9 4H5v16h4M16 8l4 4-4 4M20 12H9"/>',
  };

  // Avatars: a fixed set of glyphs and colours (no uploads). The server stores only "glyph-colour".
  var AV_GLYPHS = {
    flame: ICONS.flame, bolt: ICONS.bolt,
    spark: '<path d="M12 3l2.2 6.8L21 12l-6.8 2.2L12 21l-2.2-6.8L3 12l6.8-2.2z"/>',
    sun: '<circle cx="12" cy="12" r="4"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M19.1 4.9 17 7M7 17l-2.1 2.1"/>',
    thermo: '<path d="M10 14.5V5a2 2 0 0 1 4 0v9.5a4 4 0 1 1-4 0z"/><path d="M12 9v7"/>',
    wave: '<path d="M2 10c2.5-3.5 5-3.5 7.5 0s5 3.5 7.5 0 3-2.5 5-2.5M2 17c2.5-3.5 5-3.5 7.5 0s5 3.5 7.5 0 3-2.5 5-2.5"/>',
    comet: '<circle cx="16.5" cy="7.5" r="3"/><path d="M14 10 4 20M11.5 7 4 11M17 13l-4 8"/>',
    leaf: '<path d="M5 19c0-8 5-13 14-14 0 9-5 14-14 14z"/><path d="M5 19c3-4 6-6 9-8"/>'
  };
  var AV_COLORS = { raspberry: ['#DE3163', '#FFFFFF'], gold: ['#DEC17A', '#020101'], ink: ['#1E1E2C', '#DEC17A'], cream: ['#F3EAD3', '#8A6A22'], plum: ['#4A1730', '#DEC17A'], sand: ['#A39E93', '#020101'] };
  var AV_NAMES = { flame: 'Flame', spark: 'Spark', bolt: 'Bolt', sun: 'Sun', thermo: 'Thermometer', wave: 'Wave', comet: 'Comet', leaf: 'Leaf', raspberry: 'Raspberry', gold: 'Gold', ink: 'Ink', cream: 'Cream', plum: 'Plum', sand: 'Sand' };
  var NS = 'http://www.w3.org/2000/svg';

  /** spec = "flame-raspberry" or empty (then the first letter of the name is shown). */
  function avatar(spec, name, size) {
    size = size || 40;
    var parts = (typeof spec === 'string' ? spec : '').split('-');
    var g = AV_GLYPHS[parts[0]], c = AV_COLORS[parts[1]];
    var svg = document.createElementNS(NS, 'svg');
    svg.setAttribute('viewBox', '0 0 40 40'); svg.setAttribute('width', size); svg.setAttribute('height', size);
    svg.setAttribute('class', 'avatar'); svg.setAttribute('role', 'img');
    svg.setAttribute('aria-label', g && c ? 'Avatar: ' + AV_NAMES[parts[0]] + ', ' + AV_NAMES[parts[1]].toLowerCase() : 'Avatar: ' + ((name || '?').trim().charAt(0).toUpperCase()));
    var circle = document.createElementNS(NS, 'circle');
    circle.setAttribute('cx', 20); circle.setAttribute('cy', 20); circle.setAttribute('r', 20); circle.setAttribute('fill', c ? c[0] : '#1E1E2C');
    svg.appendChild(circle);
    if (g && c) {
      var grp = document.createElementNS(NS, 'g');
      grp.setAttribute('transform', 'translate(8 8)'); grp.setAttribute('fill', 'none'); grp.setAttribute('stroke', c[1]);
      grp.setAttribute('stroke-width', '1.8'); grp.setAttribute('stroke-linecap', 'round'); grp.setAttribute('stroke-linejoin', 'round');
      grp.innerHTML = g; // fixed strings from this file, never user input
      svg.appendChild(grp);
    } else {
      var t = document.createElementNS(NS, 'text');
      t.setAttribute('x', 20); t.setAttribute('y', 26.5); t.setAttribute('text-anchor', 'middle'); t.setAttribute('fill', '#DEC17A');
      t.setAttribute('font-size', 19); t.setAttribute('font-weight', 700); t.setAttribute('font-family', 'system-ui, -apple-system, Segoe UI, sans-serif');
      t.textContent = (name || '?').trim().charAt(0).toUpperCase();
      svg.appendChild(t);
    }
    return svg;
  }

  function icon(name) {
    var s = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    s.setAttribute('viewBox', '0 0 24 24');
    s.setAttribute('fill', 'none');
    s.setAttribute('stroke', 'currentColor');
    s.setAttribute('stroke-width', '2');
    s.setAttribute('stroke-linecap', 'round');
    s.setAttribute('stroke-linejoin', 'round');
    s.setAttribute('aria-hidden', 'true');
    s.innerHTML = ICONS[name] || '';
    return s;
  }

  function api(route, data, query) {
    var url = 'api.php?r=' + encodeURIComponent(route);
    if (query) Object.keys(query).forEach(function (k) { url += '&' + k + '=' + encodeURIComponent(query[k]); });
    var opts = { credentials: 'same-origin', headers: { 'X-EF': '1' } };
    if (data !== undefined) {
      opts.method = 'POST';
      opts.headers['Content-Type'] = 'application/json';
      opts.body = JSON.stringify(data);
    }
    return fetch(url, opts).then(function (r) {
      return r.json().catch(function () { return { error: 'Unexpected answer from the server.' }; }).then(function (j) {
        if (!r.ok || j.error) {
          var e = new Error(j.error || 'Something went wrong.');
          e.status = r.status;
          throw e;
        }
        return j;
      });
    });
  }

  function fmtDuration(sec) {
    sec = Math.max(0, Math.round(sec));
    var m = Math.round(sec / 60);
    if (sec < 60) return sec + ' sec';
    if (m < 60) return m + ' min';
    var hr = Math.floor(m / 60);
    return hr + ' h ' + (m % 60 < 10 ? '0' : '') + (m % 60) + ' min';
  }

  function fmtAgo(ts) {
    if (!ts) return 'never';
    var d = Math.floor(Date.now() / 1000) - ts;
    if (d < 120) return 'just now';
    if (d < 3600) return Math.floor(d / 60) + ' min ago';
    if (d < 86400) return Math.floor(d / 3600) + ' h ago';
    var days = Math.floor(d / 86400);
    return days === 1 ? 'yesterday' : days + ' days ago';
  }

  function fmtDate(ts) {
    var d = new Date(ts * 1000);
    return d.toLocaleDateString(undefined, { day: 'numeric', month: 'short' }) + ' ' +
      d.toLocaleTimeString(undefined, { hour: '2-digit', minute: '2-digit' });
  }

  function toast(msg) {
    var t = h('div', { class: 'toast', role: 'status' }, msg);
    document.body.appendChild(t);
    setTimeout(function () { t.remove(); }, 2600);
  }

  function modal(content) {
    var prev = document.activeElement;
    var back = h('div', { class: 'modal-back', role: 'dialog', 'aria-modal': 'true' });
    var box = h('div', { class: 'modal' }, content);
    back.appendChild(box);
    function onHash() { close(); }
    function close() { window.removeEventListener('hashchange', onHash); back.remove(); if (prev && prev.focus) prev.focus(); }
    window.addEventListener('hashchange', onHash); // a popup never outlives the page it was opened on
    back.addEventListener('click', function (e) { if (e.target === back) close(); });
    back.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
    document.body.appendChild(back);
    var f = box.querySelector('input,button,textarea');
    if (f) f.focus();
    return { close: close, el: box };
  }

  window.UI = { avatar: avatar, AV_GLYPHS: Object.keys(AV_GLYPHS), AV_COLORS: Object.keys(AV_COLORS), AV_NAMES: AV_NAMES, AV_COLOR_VALUES: AV_COLORS, h: h, icon: icon, api: api, fmtDuration: fmtDuration, fmtAgo: fmtAgo, fmtDate: fmtDate, toast: toast, modal: modal };
})();
