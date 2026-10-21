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

  // Avatars: fixed pictures and colours (no uploads). The server stores only "picture-colour", e.g. "fox-gold".
  // Symbols are drawn as outline icons; characters are flat illustrations on a coloured circle.
  var AV_GLYPHS = {
    flame: ICONS.flame, bolt: ICONS.bolt,
    spark: '<path d="M12 3l2.2 6.8L21 12l-6.8 2.2L12 21l-2.2-6.8L3 12l6.8-2.2z"/>',
    sun: '<circle cx="12" cy="12" r="4"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M19.1 4.9 17 7M7 17l-2.1 2.1"/>',
    thermo: '<path d="M10 14.5V5a2 2 0 0 1 4 0v9.5a4 4 0 1 1-4 0z"/><path d="M12 9v7"/>',
    wave: '<path d="M2 10c2.5-3.5 5-3.5 7.5 0s5 3.5 7.5 0 3-2.5 5-2.5M2 17c2.5-3.5 5-3.5 7.5 0s5 3.5 7.5 0 3-2.5 5-2.5"/>',
    comet: '<circle cx="16.5" cy="7.5" r="3"/><path d="M14 10 4 20M11.5 7 4 11M17 13l-4 8"/>',
    leaf: '<path d="M5 19c0-8 5-13 14-14 0 9-5 14-14 14z"/><path d="M5 19c3-4 6-6 9-8"/>'
  };
  var K = '#241712';
  // Characters are flat, adult illustrations: ten people and two mascots. Drawn here, never uploaded.
  var SK = { fair: ['#F4D2B4', '#E4B592'], warm: ['#E3B58F', '#CF9870'], tan: ['#C58B62', '#AE7248'], brown: ['#9A6240', '#834F31'], deep: ['#6B4430', '#58362A'], olive: ['#D9A877', '#C48E5C'] };
  var HR = { brown: '#66442F', black: '#3A302B', auburn: '#A8512C', blond: '#E2BE70', grey: '#C3C6CC', white: '#E9E6DF', chestnut: '#8A5636' };
  function person(o) {
    var sk = SK[o.skin], hair = HR[o.hair];
    var out = (o.back || '').replace(/HAIR/g, hair);
    out += '<path d="M4.5 40C4.5 32 11 28.8 20 28.8C29 28.8 35.5 32 35.5 40Z" fill="' + o.top + '"/>';
    if (o.collar) out += o.collar;
    out += '<path d="M16.6 24.2H23.4V29.4C23.4 31.4 21.8 32.6 20 32.6C18.2 32.6 16.6 31.4 16.6 29.4Z" fill="' + sk[1] + '"/>';
    out += '<ellipse cx="12.6" cy="19.2" rx="1.6" ry="2.1" fill="' + sk[1] + '"/><ellipse cx="27.4" cy="19.2" rx="1.6" ry="2.1" fill="' + sk[1] + '"/>';
    out += '<ellipse cx="20" cy="18" rx="7.5" ry="8.6" fill="' + sk[0] + '"/>';
    if (o.beard) out += '<path d="M12.6 19.4C12.8 27.8 16 30 20 30C24 30 27.2 27.8 27.4 19.4C26.2 23.4 23.6 24.6 20 24.6C16.4 24.6 13.8 23.4 12.6 19.4Z" fill="' + hair + '"/>';
    out += '<ellipse cx="17" cy="18.5" rx=".95" ry="1.15" fill="' + K + '"/><ellipse cx="23" cy="18.5" rx=".95" ry="1.15" fill="' + K + '"/>';
    out += '<path d="M20 19.6Q19 21.4 20.6 21.5" fill="none" stroke="' + sk[1] + '" stroke-width=".8" stroke-linecap="round"/>';
    out += '<path d="M17.9 22.8Q20 24.5 22.1 22.8" fill="none" stroke="' + (o.beard ? '#F6E7DA' : K) + '" stroke-width="1" stroke-linecap="round"/>';
    out += (o.front || '').replace(/HAIR/g, hair);
    if (o.glasses) out += '<g fill="none" stroke="' + K + '" stroke-width=".9"><circle cx="17" cy="18.5" r="2.8"/><circle cx="23" cy="18.5" r="2.8"/><path d="M19.8 18.3H20.2M14.2 18.2L12.8 17.6M25.8 18.2L27.2 17.6"/></g>';
    return out;
  }
  var HF = {
    short: '<path d="M12.2 17.6C11.4 11 15 8.6 20 8.6C25 8.6 28.6 11 27.8 17.6C27.2 14.8 24.6 12.8 20.6 12.4C17.2 13.8 14 14.6 12.2 17.6Z" fill="HAIR"/>',
    quiff: '<path d="M12.2 17.4C11 10.5 14.6 7.6 20 7.6C25.6 7.6 29 10.6 27.8 17.4C27.4 14.4 25.6 12.4 22.6 11.8C18.8 12.8 14.6 13.4 12.2 17.4Z" fill="HAIR"/>',
    bun: '<circle cx="20" cy="6.8" r="3.2" fill="HAIR"/><path d="M12.2 17.6C11.4 11.4 15 9 20 9C25 9 28.6 11.4 27.8 17.6C27 14.8 24.4 12.8 20.4 12.4C17.2 13.8 14 14.6 12.2 17.6Z" fill="HAIR"/>',
    buzz: '<path d="M12.6 16C12.4 11.2 15.6 9.4 20 9.4C24.4 9.4 27.6 11.2 27.4 16C25.8 13.6 23.4 12.6 20 12.6C16.6 12.6 14.2 13.6 12.6 16Z" fill="HAIR"/>',
    side: '<path d="M12.2 17.8C11 10.4 15 8 20.4 8C25.6 8 28.8 11 27.8 17.6C27.4 15 25.8 13 23 12.2C19 12.6 14.6 14 12.2 17.8Z" fill="HAIR"/>',
    cap: '<path d="M12 16.6C11.6 10 15.2 8 20 8C24.8 8 28.4 10 28 16.6Z" fill="HAIR"/><path d="M11.4 16.6H28.6V15.2C28.6 14.4 28 14 27.4 14H12.6C12 14 11.4 14.4 11.4 15.2Z" fill="HAIR" opacity=".9"/>',
  };
  var HB = {
    long: '<path d="M11 18C9.8 8.8 14.6 6.8 20 6.8C25.4 6.8 30.2 8.8 29 18L30.2 31L9.8 31Z" fill="HAIR"/>',
    bob: '<path d="M11 19C10 9.4 14.6 7 20 7C25.4 7 30 9.4 29 19L29 25C29 26.4 28 27 26.6 27L13.4 27C12 27 11 26.4 11 25Z" fill="HAIR"/>',
    curly: '<g fill="HAIR"><circle cx="12.4" cy="13.8" r="4.4"/><circle cx="15.6" cy="9.4" r="4.6"/><circle cx="20.4" cy="8.2" r="4.8"/><circle cx="25" cy="9.8" r="4.5"/><circle cx="27.8" cy="14.2" r="4.4"/><circle cx="11.6" cy="19.4" r="3.6"/><circle cx="28.4" cy="19.4" r="3.6"/></g>',
  };
  var AV_CHARS = {
    ada: person({ skin: 'fair', hair: 'brown', top: '#2F4B7C', back: '', front: HF.side, glasses: true, collar: '<path d="M14.6 29.4L20 36L25.4 29.4L25.4 40H14.6Z" fill="#F4F1EA"/>' }),
    ben: person({ skin: 'tan', hair: 'black', top: '#E0A93B', front: HF.short, beard: true }),
    cleo: person({ skin: 'fair', hair: 'auburn', top: '#2E8B8B', back: HB.long, front: '<path d="M12.4 17.4C12 11.6 15.2 9 20 9C24.8 9 28 11.6 27.6 17.4C26.2 14.4 23.2 12.8 19.6 12.6C16.4 13 13.8 14.4 12.4 17.4Z" fill="HAIR"/><circle cx="12.4" cy="22" r="1.1" fill="#F2C94C"/><circle cx="27.6" cy="22" r="1.1" fill="#F2C94C"/>' }),
    dev: person({ skin: 'deep', hair: 'black', top: '#F4F1EA', front: HF.buzz }),
    eli: person({ skin: 'warm', hair: 'chestnut', top: '#3E7D5A', front: HF.bun, beard: true, glasses: true }),
    fay: person({ skin: 'olive', hair: 'black', top: '#8C79C6', back: HB.bob, front: '<path d="M12.2 17C11.8 11.6 15.4 9.2 20 9.2C24.6 9.2 28.2 11.6 27.8 17C25.4 15.4 22.4 14.2 20 12.2C17.6 14.2 14.6 15.4 12.2 17Z" fill="HAIR"/>' }),
    gus: person({ skin: 'brown', hair: 'grey', top: '#3A3F4B', beard: true, glasses: true, front: '<path d="M12.4 15.4C12.8 12.4 14.6 10.6 16.6 10.2C14.8 11.8 13.8 13.6 13.6 16Z" fill="HAIR"/><path d="M27.6 15.4C27.2 12.4 25.4 10.6 23.4 10.2C25.2 11.8 26.2 13.6 26.4 16Z" fill="HAIR"/>' }),
    hana: person({ skin: 'deep', hair: 'black', top: '#C8643C', back: HB.curly, front: '<circle cx="12.5" cy="23" r="1.9" fill="none" stroke="#F2C94C" stroke-width=".9"/><circle cx="27.5" cy="23" r="1.9" fill="none" stroke="#F2C94C" stroke-width=".9"/>' }),
    ivan: person({ skin: 'fair', hair: 'blond', top: '#E9E6DF', front: HF.quiff + '<path d="M10.8 19V16.4C10.8 11.4 14.6 8.2 20 8.2C25.4 8.2 29.2 11.4 29.2 16.4V19" fill="none" stroke="#3A3F4B" stroke-width="1.6" stroke-linecap="round"/><rect x="9.6" y="16.8" width="3.2" height="5.2" rx="1.4" fill="#3A3F4B"/><rect x="27.2" y="16.8" width="3.2" height="5.2" rx="1.4" fill="#3A3F4B"/>' }),
    june: person({ skin: 'olive', hair: 'white', top: '#2E8B8B', back: HB.bob, glasses: true, front: '<path d="M12.2 17C11.8 11.8 15.4 9.4 20 9.4C24.6 9.4 28.2 11.8 27.8 17C26 14.6 23 13.4 19.4 13C16.6 13.6 14 14.8 12.2 17Z" fill="HAIR"/>' }),
    fox: '<path d="M8 19L9.5 6.5L17.2 13Z" fill="#E8772E"/><path d="M32 19L30.5 6.5L22.8 13Z" fill="#E8772E"/>' +
      '<path d="M10.8 15L11.3 10.2L14.6 13.2Z" fill="#7A3B1B"/><path d="M29.2 15L28.7 10.2L25.4 13.2Z" fill="#7A3B1B"/>' +
      '<path d="M7.2 19.5C7.2 14.4 12.6 12 20 12C27.4 12 32.8 14.4 32.8 19.5C32.8 26.5 26.5 33.5 20 35C13.5 33.5 7.2 26.5 7.2 19.5Z" fill="#E8772E"/>' +
      '<path d="M8.4 22C13 22.6 17 26 20 29.5C23 26 27 22.6 31.6 22C30.6 28 25.5 33.2 20 34.2C14.5 33.2 9.4 28 8.4 22Z" fill="#FBF3E8"/>' +
      '<path d="M12.4 19.6Q14.4 18 16.4 19.6Q14.4 21.2 12.4 19.6Z" fill="' + K + '"/><path d="M23.6 19.6Q25.6 18 27.6 19.6Q25.6 21.2 23.6 19.6Z" fill="' + K + '"/><path d="M18.2 28.4H21.8L20 30.6Z" fill="' + K + '"/>',
    ember: '<path d="M20 4.5C21.4 10.8 30 14 30 24.5C30 30.6 25.8 34.8 20 34.8C14.2 34.8 10 30.6 10 24.5C10 20.8 12 18.2 14.4 15.8C14.8 18 15.8 19.6 17.6 20.4C16.4 14.4 17.6 9 20 4.5Z" fill="#F26A1B"/>' +
      '<path d="M20 18C22.8 22 26 24.6 26 28.8C26 32 23.4 33.8 20 33.8C16.6 33.8 14 32 14 28.8C14 25.6 17.4 22.8 20 18Z" fill="#FFC93C"/>' +
      '<ellipse cx="17.6" cy="28.4" rx=".95" ry="1.25" fill="' + K + '"/><ellipse cx="22.4" cy="28.4" rx=".95" ry="1.25" fill="' + K + '"/><path d="M18.8 31Q20 32 21.2 31" fill="none" stroke="' + K + '" stroke-width=".9" stroke-linecap="round"/>'
  };
  var AV_COLORS = { raspberry: ['#DE3163', '#FFFFFF'], gold: ['#DEC17A', '#020101'], ink: ['#1E1E2C', '#DEC17A'], cream: ['#F3EAD3', '#8A6A22'], plum: ['#4A1730', '#DEC17A'], sand: ['#A39E93', '#020101'] };
  var AV_NAMES = { flame: 'Flame', spark: 'Spark', bolt: 'Bolt', sun: 'Sun', thermo: 'Thermometer', wave: 'Wave', comet: 'Comet', leaf: 'Leaf',
    ada: 'Ada', ben: 'Ben', cleo: 'Cleo', dev: 'Dev', eli: 'Eli', fay: 'Fay', gus: 'Gus', hana: 'Hana', ivan: 'Ivan', june: 'June', fox: 'Fox', ember: 'Ember', initial: 'My initial',
    raspberry: 'Raspberry', gold: 'Gold', ink: 'Ink', cream: 'Cream', plum: 'Plum', sand: 'Sand' };
  var NS = 'http://www.w3.org/2000/svg';

  /** spec = "fox-gold" (character), "flame-plum" (symbol), "initial-ink" (first letter) or empty (first letter, dark). */
  function avatar(spec, name, size) {
    size = size || 40;
    var parts = (typeof spec === 'string' ? spec : '').split('-');
    var kind = AV_CHARS[parts[0]] ? 'char' : (AV_GLYPHS[parts[0]] ? 'glyph' : 'initial');
    var c = AV_COLORS[parts[1]];
    if (!c) { kind = 'initial'; c = AV_COLORS.ink; }
    var svg = document.createElementNS(NS, 'svg');
    svg.setAttribute('viewBox', '0 0 40 40'); svg.setAttribute('width', size); svg.setAttribute('height', size);
    svg.setAttribute('class', 'avatar'); svg.setAttribute('role', 'img');
    svg.setAttribute('aria-label', kind === 'initial' ? 'Avatar: ' + ((name || '?').trim().charAt(0).toUpperCase()) : 'Avatar: ' + AV_NAMES[parts[0]] + ', ' + AV_NAMES[parts[1]].toLowerCase());
    var circle = document.createElementNS(NS, 'circle');
    circle.setAttribute('cx', 20); circle.setAttribute('cy', 20); circle.setAttribute('r', 20); circle.setAttribute('fill', c[0]);
    svg.appendChild(circle);
    var grp = document.createElementNS(NS, 'g');
    grp.setAttribute('stroke-linecap', 'round'); grp.setAttribute('stroke-linejoin', 'round');
    if (kind === 'glyph') {
      grp.setAttribute('transform', 'translate(8 8)'); grp.setAttribute('fill', 'none'); grp.setAttribute('stroke', c[1]); grp.setAttribute('stroke-width', '1.8');
      grp.innerHTML = AV_GLYPHS[parts[0]]; // fixed strings from this file, never user input
      svg.appendChild(grp);
    } else if (kind === 'char') {
      grp.setAttribute('stroke', 'none');
      grp.innerHTML = AV_CHARS[parts[0]]; // fixed strings from this file, never user input
      svg.appendChild(grp);
    } else {
      var t = document.createElementNS(NS, 'text');
      t.setAttribute('x', 20); t.setAttribute('y', 26.5); t.setAttribute('text-anchor', 'middle'); t.setAttribute('fill', c[1]);
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

  window.UI = { avatar: avatar, AV_GLYPHS: Object.keys(AV_GLYPHS), AV_CHARS: Object.keys(AV_CHARS), AV_COLORS: Object.keys(AV_COLORS), AV_NAMES: AV_NAMES, AV_COLOR_VALUES: AV_COLORS, h: h, icon: icon, api: api, fmtDuration: fmtDuration, fmtAgo: fmtAgo, fmtDate: fmtDate, toast: toast, modal: modal };
})();
