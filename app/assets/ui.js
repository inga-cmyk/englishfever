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
    function close() { back.remove(); if (prev && prev.focus) prev.focus(); }
    back.addEventListener('click', function (e) { if (e.target === back) close(); });
    back.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
    document.body.appendChild(back);
    var f = box.querySelector('input,button,textarea');
    if (f) f.focus();
    return { close: close, el: box };
  }

  window.UI = { h: h, icon: icon, api: api, fmtDuration: fmtDuration, fmtAgo: fmtAgo, fmtDate: fmtDate, toast: toast, modal: modal };
})();
