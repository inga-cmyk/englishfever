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
  var K = '#241712', RED = '#C8283C', GOLD = '#F2C94C';
  // Characters are flat, stylish illustrations (people, a superhero, a few funny figures). Drawn here, never uploaded.
  function mixHex(a, b, t) { var x = parseInt(a.slice(1), 16), y = parseInt(b.slice(1), 16), o = '#'; [16, 8, 0].forEach(function (s) { var c = Math.round(((x >> s) & 255) * (1 - t) + ((y >> s) & 255) * t); o += (c < 16 ? '0' : '') + c.toString(16); }); return o; }
  function lighten(c, t) { return mixHex(c, '#ffffff', t); }
  function darken(c, t) { return mixHex(c, '#000000', t); }
  var SK = { fair: ['#F6D5BA', '#E6B896'], warm: ['#E8BC96', '#D3A07A'], tan: ['#C98F66', '#B27650'], brown: ['#9A6240', '#834F31'], deep: ['#6B4430', '#58362A'], olive: ['#DDAF7E', '#C8945F'] };
  var FACE = 'M12.7 16.2C12.7 11.4 15.9 9.4 20 9.4C24.1 9.4 27.3 11.4 27.3 16.2C27.3 21.4 24.4 26.6 20 26.9C15.6 26.6 12.7 21.4 12.7 16.2Z';
  function brows(c, o) { o = o || {}; return '<g fill="none" stroke="' + c + '" stroke-width="' + (o.w || 1) + '" stroke-linecap="round"><path d="' + (o.raise ? 'M14.2 14.2Q16.4 12.4 18.8 13.8' : 'M14.4 15.5Q16.6 14.5 18.8 15.4') + '"/><path d="M21.2 15.4Q23.4 14.5 25.6 15.5"/></g>'; }
  function eyes(lash) { return '<ellipse cx="16.9" cy="18.3" rx=".95" ry="1.2" fill="' + K + '"/><ellipse cx="23.1" cy="18.3" rx=".95" ry="1.2" fill="' + K + '"/>' + (lash ? '<path d="M15.8 17.6L14.8 16.9M24.2 17.6L25.2 16.9" fill="none" stroke="' + K + '" stroke-width=".7" stroke-linecap="round"/>' : ''); }
  function lips(c) { return '<path d="M17.6 23Q18.9 22.1 20 22.8Q21.1 22.1 22.4 23Q21.3 24.6 20 24.6Q18.7 24.6 17.6 23Z" fill="' + c + '"/>'; }
  function line(d, w, c) { return '<path d="' + d + '" fill="none" stroke="' + (c || K) + '" stroke-width="' + (w || 1) + '" stroke-linecap="round"/>'; }
  var M = {
    smile: line('M17.9 23Q20 24.8 22.1 23'),
    smirk: line('M18.2 23.4Q20.4 24.4 22.6 22.6'),
    flat: line('M18.2 23.6H21.8'),
    grin: '<path d="M17 22.6Q20 23 23 22.6Q22.4 25.8 20 25.8Q17.6 25.8 17 22.6Z" fill="#fff" stroke="' + K + '" stroke-width=".8" stroke-linejoin="round"/>'
  };
  function blush(c) { return '<circle cx="15.2" cy="21.2" r="1.8" fill="' + c + '" opacity=".3"/><circle cx="24.8" cy="21.2" r="1.8" fill="' + c + '" opacity=".3"/>'; }
  function nose(sk) { return line('M20 19.4Q19.2 21.2 20.7 21.4', 0.8, sk[1]); }
  function glasses(c) { return '<g fill="none" stroke="' + c + '" stroke-width=".9"><circle cx="16.9" cy="18.3" r="2.8"/><circle cx="23.1" cy="18.3" r="2.8"/><path d="M19.7 18.1H20.3M14.1 17.9L12.8 17.4M25.9 17.9L27.2 17.4"/></g>'; }
  function blazer(top, shirt) { var d = darken(top, 0.28); return '<path d="M16.2 29.2L20 36.6L23.8 29.2Z" fill="' + shirt + '"/><path d="M14 29.4L19.4 38.8L16 40L12 33.2Z" fill="' + d + '"/><path d="M26 29.4L20.6 38.8L24 40L28 33.2Z" fill="' + d + '"/>'; }
  function hoop(x, y) { return '<circle cx="' + x + '" cy="' + y + '" r="1.8" fill="none" stroke="' + GOLD + '" stroke-width=".8"/>'; }
  function drop(x, y) { return '<circle cx="' + x + '" cy="' + y + '" r=".8" fill="' + GOLD + '"/><path d="M' + x + ' ' + (y + .6) + 'V' + (y + 2.2) + '" stroke="' + GOLD + '" stroke-width=".6"/><circle cx="' + x + '" cy="' + (y + 2.6) + '" r=".9" fill="' + GOLD + '"/>'; }
  var PEARLS = '<g fill="#FFFDF5" stroke="#D8D0C0" stroke-width=".25"><circle cx="16.3" cy="29.9" r=".65"/><circle cx="17.3" cy="30.9" r=".65"/><circle cx="18.6" cy="31.5" r=".65"/><circle cx="20" cy="31.7" r=".65"/><circle cx="21.4" cy="31.5" r=".65"/><circle cx="22.7" cy="30.9" r=".65"/><circle cx="23.7" cy="29.9" r=".65"/></g>';
  var CURLS = '<g fill="HAIR"><circle cx="12.4" cy="13.8" r="4.4"/><circle cx="15.6" cy="9.4" r="4.6"/><circle cx="20.4" cy="8.2" r="4.8"/><circle cx="25" cy="9.8" r="4.5"/><circle cx="27.8" cy="14.2" r="4.4"/><circle cx="11.6" cy="19.4" r="3.6"/><circle cx="28.4" cy="19.4" r="3.6"/></g>';

  function person(o) {
    var sk = SK[o.skin], hair = o.hair || '#3A302B';
    function hc(s) { return (s || '').replace(/HAIR/g, hair).replace(/HI/g, lighten(hair, 0.4)).replace(/HD/g, darken(hair, 0.25)); }
    var out = (o.cape || '') + hc(o.back);
    out += '<path d="M4.5 40C4.5 32 11 28.8 20 28.8C29 28.8 35.5 32 35.5 40Z" fill="' + o.top + '"/>' + (o.outfit || '');
    out += '<path d="M16.6 24.2H23.4V29.4C23.4 31.4 21.8 32.6 20 32.6C18.2 32.6 16.6 31.4 16.6 29.4Z" fill="' + sk[1] + '"/>' + (o.neck || '');
    out += '<ellipse cx="12.6" cy="19.2" rx="1.6" ry="2.1" fill="' + sk[1] + '"/><ellipse cx="27.4" cy="19.2" rx="1.6" ry="2.1" fill="' + sk[1] + '"/>';
    out += '<path d="' + FACE + '" fill="' + sk[0] + '"/>' + hc(o.under) + nose(sk) + (o.beard ? hc('<path d="M12.7 19C12.8 26 16 29 20 29C24 29 27.2 26 27.3 19C26.3 23 23.6 24.4 20 24.4C16.4 24.4 13.7 23 12.7 19Z" fill="HAIR"/>') : '');
    out += (o.mouth || M.smile) + eyes(o.lash) + brows(o.browc || darken(hair, 0.1), o.brow) + (o.acc || '') + hc(o.stache) + hc(o.front) + (o.hat || '') + (o.prop || '');
    return out;
  }
  var AV_CHARS = {
    vera: person({ skin: 'fair', hair: '#EBC86E', top: '#1F3A5F', outfit: blazer('#1F3A5F', '#F6F2EA'), neck: PEARLS, under: blush('#E8788A'), mouth: lips(RED), lash: true, browc: '#B8924A',
      back: '<path d="M10.2 17.4C8.4 8.4 13.6 5.6 20 5.6C26.4 5.6 31.6 8.4 29.8 17.4C31 21.6 32.8 26 31.8 31.2C30 32.4 28 31.4 27 29.4L26.6 24L13.4 24L13 29.4C12 31.4 10 32.4 8.2 31.2C7.2 26 9 21.6 10.2 17.4Z" fill="HAIR"/>',
      front: '<path d="M12.2 18.4C11.2 10.8 15 7.8 20 7.8C25.4 7.8 29 10.8 27.8 18.4C27.4 15.2 25.6 13.2 22.8 12.4C19.6 11.4 16.4 12.6 14.6 14.6Z" fill="HAIR"/><path d="M15 10.6C16.8 8.8 20 8.4 22.6 9.2M23 10.4C24.8 10.6 26 11.8 26.4 13.4" fill="none" stroke="HI" stroke-width="1" stroke-linecap="round"/>' +
        '<path d="M11.2 19C10.2 24 10.6 28.4 9.4 31.8C11.8 32.2 13.4 30.8 14 28.2L13.8 20Z" fill="HAIR"/><path d="M28.8 19C29.8 24 29.4 28.4 30.6 31.8C28.2 32.2 26.6 30.8 26 28.2L26.2 20Z" fill="HAIR"/><path d="M11.6 22C11.2 25 11.4 27.6 10.8 29.8M28.4 22C28.8 25 28.6 27.6 29.2 29.8" fill="none" stroke="HI" stroke-width=".8" stroke-linecap="round"/>' + drop(12.6, 23.2) }),
    marco: person({ skin: 'tan', hair: '#2E2622', top: '#7A2E3B', neck: '<rect x="15.2" y="25.2" width="9.6" height="7.2" rx="3.2" fill="#8E3A49"/>' + line('M15.6 28.6Q20 30.4 24.4 28.6', 0.6, '#5E222D'), brow: { w: 1.3 }, mouth: M.smirk,
      under: '<path d="M12.8 19.6C13 25 16.2 27 20 27C23.8 27 27 25 27.2 19.6C26.2 22.6 23.6 23.8 20 23.8C16.4 23.8 13.8 22.6 12.8 19.6Z" fill="HAIR" opacity=".28"/>',
      front: '<path d="M12.4 16.4C11.6 10 15.4 7.4 20.4 7.4C25.4 7.4 28.6 10.2 27.6 16.4C27.2 13.4 25.2 11.4 22.4 10.6C18.6 10.2 14.6 11.6 12.4 16.4Z" fill="HAIR"/><path d="M16.6 9.6C18.6 8.9 21 8.9 22.8 9.4" fill="none" stroke="HI" stroke-width=".7" stroke-linecap="round" opacity=".55"/>' }),
    cleo: person({ skin: 'fair', hair: '#B5532B', top: '#E8DCC5', outfit: '<path d="M13.4 29.6L18.4 38L15.2 40L11.8 33Z" fill="#CBBD9F"/><path d="M26.6 29.6L21.6 38L24.8 40L28.2 33Z" fill="#CBBD9F"/>', lash: true, mouth: lips('#B8434A'), browc: '#8A3A1E',
      neck: '<path d="M14.8 28.2C17 30.8 23 30.8 25.2 28.2L26.2 31.6C23 33.8 17 33.8 13.8 31.6Z" fill="#2F7D5B"/><path d="M21 32L24.4 37.8L22 39L19.6 33Z" fill="#256349"/>',
      under: '<g fill="#8A3A1E" opacity=".5"><circle cx="17.6" cy="20.2" r=".35"/><circle cx="18.8" cy="20.9" r=".35"/><circle cx="16.6" cy="20.6" r=".35"/><circle cx="22.2" cy="20.9" r=".35"/><circle cx="23.4" cy="20.2" r=".35"/><circle cx="21.2" cy="20.2" r=".35"/><circle cx="24.4" cy="20.6" r=".35"/></g>',
      back: '<path d="M11 17C10 8.6 14.4 6.4 20 6.4C25.6 6.4 30 8.6 29 17L29.8 27.6C29.8 29.2 28.4 29.8 27 29.4L13 29.4C11.6 29.8 10.2 29.2 10.2 27.6Z" fill="HAIR"/>',
      front: '<path d="M20 8.4C15 8.4 11.8 11.4 12.2 18.6C14.6 17.4 17.6 14.8 20 10Z" fill="HAIR"/><path d="M20 8.4C25 8.4 28.2 11.4 27.8 18.6C25.4 17.4 22.4 14.8 20 10Z" fill="HAIR"/><path d="M14 12.6C15.6 10.8 17.8 10 20 9.8M26 12.6C24.4 10.8 22.2 10 20 9.8" fill="none" stroke="HI" stroke-width=".9" stroke-linecap="round"/>' }),
    hana: person({ skin: 'deep', hair: '#2F2623', top: '#C8643C', outfit: '<path d="M15 29.2Q20 33 25 29.2" fill="none" stroke="#E8A860" stroke-width="1.2" stroke-linecap="round"/>', mouth: M.grin, lash: true, browc: '#2F2623',
      back: '<g fill="HAIR"><circle cx="11.6" cy="19.4" r="3.6"/><circle cx="28.4" cy="19.4" r="3.6"/><circle cx="12.4" cy="13.8" r="4.4"/><circle cx="27.8" cy="14.2" r="4.4"/><circle cx="15.6" cy="9.4" r="4.6"/><circle cx="25" cy="9.8" r="4.5"/><circle cx="20.4" cy="8.2" r="4.8"/></g>',
      front: '<g fill="HAIR"><circle cx="15.6" cy="11.2" r="3.1"/><circle cx="20.4" cy="10.2" r="3.3"/><circle cx="25" cy="11.6" r="3.1"/></g><path d="M14 9.6C16 8 18.6 7.6 20.6 7.8" fill="none" stroke="HI" stroke-width=".9" stroke-linecap="round"/>' + hoop(12.4, 24) + hoop(27.6, 24) }),
    fay: person({ skin: 'olive', hair: '#2A2430', top: '#8C79C6', outfit: blazer('#8C79C6', '#F4F1EA'), mouth: lips('#9E2B50'), lash: true, browc: '#2A2430',
      back: '<path d="M11 19C10 9.4 14.6 7 20 7C25.4 7 30 9.4 29 19L29 25C29 26.4 28 27 26.6 27L13.4 27C12 27 11 26.4 11 25Z" fill="HAIR"/>',
      front: '<path d="M12.2 17C11.4 10.6 15.2 8.2 20 8.2C24.8 8.2 28.6 10.6 27.8 17C27.6 14.4 26 12.8 20 12.8C14 12.8 12.4 14.4 12.2 17Z" fill="HAIR"/><path d="M11.4 18.4L12 26.4C12.2 27 13 27 13.2 26.4L13.8 19ZM28.6 18.4L28 26.4C27.8 27 27 27 26.8 26.4L26.2 19Z" fill="HAIR"/><path d="M15 10.4C17 9.2 19.6 9 22 9.4" fill="none" stroke="HI" stroke-width=".9" stroke-linecap="round"/><circle cx="12.6" cy="23" r=".9" fill="#FFFDF5"/><circle cx="27.4" cy="23" r=".9" fill="#FFFDF5"/>' }),
    june: person({ skin: 'fair', hair: '#E9E4D6', top: '#2A2A33', outfit: '<path d="M16.6 29.4L20 35.4L23.4 29.4Z" fill="#F4F1EA"/><path d="M14 29.4L19.4 38.8L16 40L12 33.2Z" fill="#3A3A46"/><path d="M26 29.4L20.6 38.8L24 40L28 33.2Z" fill="#3A3A46"/><path d="M19.2 38.6L18.4 40" stroke="#8C8C99" stroke-width=".7"/>', mouth: lips(RED), browc: '#B9B09A',
      acc: '<path d="M12.6 16.2C13.6 16.2 14.4 16.8 15.2 16.8C16.8 16.8 18.4 16.8 19.5 17.2C19.5 19.6 18.2 21 16.4 21C14.2 21 13.1 19 12.6 16.2Z" fill="' + K + '"/><path d="M27.4 16.2C26.4 16.2 25.6 16.8 24.8 16.8C23.2 16.8 21.6 16.8 20.5 17.2C20.5 19.6 21.8 21 23.6 21C25.8 21 26.9 19 27.4 16.2Z" fill="' + K + '"/><path d="M19.5 17.4H20.5" stroke="' + K + '" stroke-width=".8"/><path d="M14 17.8L16 17.8M24 17.8L26 17.8" stroke="#fff" stroke-width=".7" opacity=".55" stroke-linecap="round"/>',
      front: '<path d="M12.4 16C11.6 9.4 15.4 7.2 20.6 7.2C25.8 7.2 28.6 9.8 27.6 16C27.2 13 25.4 11 22.6 10.2C19.2 12.4 15 13 12.4 16Z" fill="HAIR"/><path d="M15 9.8C17 8.4 20 8.2 22.4 8.8" fill="none" stroke="#fff" stroke-width=".9" stroke-linecap="round" opacity=".8"/><path d="M11.6 15.6L12.2 20.4L13 18L12.7 15Z" fill="HAIR"/><path d="M28.4 15.6L27.8 20.4L27 18L27.3 15Z" fill="HAIR"/>' + '<path d="M12.2 22.4L13.4 24.6L11 24.6Z" fill="' + GOLD + '"/><path d="M27.8 22.4L29 24.6L26.6 24.6Z" fill="' + GOLD + '"/>' }),
    dev: person({ skin: 'deep', hair: '#2F2623', top: '#3E6EA8', outfit: '<path d="M16.6 29.4L20 35L23.4 29.4Z" fill="#F4F1EA"/><path d="M14.4 29.6L18.4 38.6L15.6 40L12.6 33Z" fill="#32598A"/><path d="M25.6 29.6L21.6 38.6L24.4 40L27.4 33Z" fill="#32598A"/>', mouth: M.grin, browc: '#2F2623', brow: { w: 1.2 },
      front: '<path d="M12.6 16C12.4 11.2 15.6 9.2 20 9.2C24.4 9.2 27.6 11.2 27.4 16C25.8 13.6 23.4 12.4 20 12.4C16.6 12.4 14.2 13.6 12.6 16Z" fill="HAIR"/><circle cx="12.8" cy="21.2" r=".75" fill="' + GOLD + '"/>' }),
    eli: person({ skin: 'warm', hair: '#8A5636', top: '#3E7D5A', outfit: '<path d="M20 31.4V40" stroke="#2C5E43" stroke-width=".8"/><circle cx="20" cy="34.4" r=".55" fill="#F4F1EA"/><circle cx="20" cy="37.4" r=".55" fill="#F4F1EA"/>', beard: true, mouth: line('M18.4 23.2Q20 24.4 21.6 23.2', 1, '#F6E7DA'), acc: glasses(K),
      front: '<circle cx="20" cy="6.6" r="3.2" fill="HAIR"/><path d="M12.2 17.6C11.4 11.4 15 9 20 9C25 9 28.6 11.4 27.8 17.6C27 14.8 24.4 12.8 20.4 12.4C17.2 13.8 14 14.6 12.2 17.6Z" fill="HAIR"/>' }),
    gus: person({ skin: 'brown', hair: '#E9E6DF', top: '#8A5A44', outfit: '<path d="M20 30.4V40" stroke="#6E4333" stroke-width=".8"/><circle cx="20" cy="33.6" r=".6" fill="#E8D5B0"/><circle cx="20" cy="36.6" r=".6" fill="#E8D5B0"/><path d="M16.4 29.4L20 33L23.6 29.4Z" fill="#E8D5B0"/>', beard: true, mouth: line('M18.6 23.1Q20 24.2 21.4 23.1', 1, '#C9A89A'), acc: glasses(K), browc: '#E9E6DF', brow: { w: 1.3 },
      hat: '<path d="M11.8 14.4C11.6 8.8 15.4 7.4 20 7.4C24.6 7.4 28.4 8.8 28.2 14.4Z" fill="#7A6A58"/><path d="M10.4 14.4C13 15.8 27 15.8 29.6 14.4C29.6 16.4 25 17.6 20 17.6C15 17.6 10.4 16.4 10.4 14.4Z" fill="#5E5040"/><path d="M14 10.4L16.6 8.6M18 12L21.6 8.2M23 12.4L26.4 9.4" stroke="#968670" stroke-width=".6" fill="none"/>',
      front: '<path d="M12 15.6L12.6 21L13.4 18.4Z" fill="HAIR"/><path d="M28 15.6L27.4 21L26.6 18.4Z" fill="HAIR"/>' }),
    ivan: person({ skin: 'fair', hair: '#E2BE70', top: '#E9E6DF', mouth: M.smile, browc: '#B8924A',
      under: '<path d="M12.8 19.6C13 25 16.2 27 20 27C23.8 27 27 25 27.2 19.6C26.2 22.6 23.6 23.8 20 23.8C16.4 23.8 13.8 22.6 12.8 19.6Z" fill="HAIR" opacity=".3"/>',
      front: '<path d="M12.2 17.4C11 10.5 14.6 7.6 20 7.6C25.6 7.6 29 10.6 27.8 17.4C27.4 14.4 25.6 12.4 22.6 11.8C18.8 12.8 14.6 13.4 12.2 17.4Z" fill="HAIR"/><path d="M10.8 19V16.4C10.8 11.4 14.6 8.2 20 8.2C25.4 8.2 29.2 11.4 29.2 16.4V19" fill="none" stroke="#3A3F4B" stroke-width="1.6" stroke-linecap="round"/><rect x="9.6" y="16.8" width="3.2" height="5.2" rx="1.4" fill="#3A3F4B"/><rect x="27.2" y="16.8" width="3.2" height="5.2" rx="1.4" fill="#3A3F4B"/>' }),
    nova: person({ skin: 'tan', hair: '#2B2433', top: '#2B4C9B', cape: '<path d="M2.8 40C3 30.6 8 26.8 14 27L26 27C32 26.8 37 30.6 37.2 40Z" fill="' + RED + '"/><path d="M5.6 40C6 33 9 29.6 12.6 28.8L11 40ZM34.4 40C34 33 31 29.6 27.4 28.8L29 40Z" fill="' + darken(RED, 0.25) + '"/>',
      outfit: '<circle cx="20" cy="36.6" r="2.9" fill="' + GOLD + '"/><path d="M20.9 34.6L18.8 37H20.4L19.5 38.8L21.7 36.2H20.1Z" fill="' + RED + '"/>', neck: '<circle cx="14.2" cy="29.6" r="1" fill="' + GOLD + '"/><circle cx="25.8" cy="29.6" r="1" fill="' + GOLD + '"/><path d="M14.2 29.6Q20 31.8 25.8 29.6" fill="none" stroke="' + GOLD + '" stroke-width=".7"/>', mouth: lips('#B8434A'), lash: true, browc: '#2B2433', brow: { raise: true },
      back: '<path d="M11 18C10 8.6 14.6 6.6 20 6.6C25.4 6.6 30 8.6 29 18L29 24.6C29 26 28 26.6 26.6 26.6L13.4 26.6C12 26.6 11 26 11 24.6Z" fill="HAIR"/>',
      acc: '<path d="M12.4 16.2C13.6 15.2 16 16.2 20 16.2C24 16.2 26.4 15.2 27.6 16.2C27.8 19.4 25.4 20.8 23.2 20.6C21.6 20.5 20.8 19.4 20 19.4C19.2 19.4 18.4 20.5 16.8 20.6C14.6 20.8 12.2 19.4 12.4 16.2Z" fill="' + RED + '"/><ellipse cx="16.9" cy="18.2" rx="1.5" ry=".9" fill="#fff"/><ellipse cx="23.1" cy="18.2" rx="1.5" ry=".9" fill="#fff"/><circle cx="17.1" cy="18.2" r=".55" fill="' + K + '"/><circle cx="23.3" cy="18.2" r=".55" fill="' + K + '"/>',
      front: '<path d="M12.2 17C11.6 10.6 15.4 8.2 20.2 8.2C25 8.2 28.6 10.6 27.8 17C27.4 14.2 25.4 12.4 22.6 11.8C19 13.6 15 13.8 12.2 17Z" fill="HAIR"/><path d="M15.4 10.4C17.2 9.2 19.8 8.8 22 9.4" fill="none" stroke="HI" stroke-width=".9" stroke-linecap="round"/>' }),
    captain: person({ skin: 'warm', hair: '#6B4A2F', top: RED, cape: '<path d="M2.8 40C3 30.6 8 26.8 14 27L26 27C32 26.8 37 30.6 37.2 40Z" fill="#E0A93B"/><path d="M5.6 40C6 33 9 29.6 12.6 28.8L11 40ZM34.4 40C34 33 31 29.6 27.4 28.8L29 40Z" fill="' + darken('#E0A93B', 0.25) + '"/>',
      outfit: '<path d="M20 33.6L21 35.8L23.4 36L21.6 37.6L22.2 39.8L20 38.6L17.8 39.8L18.4 37.6L16.6 36L19 35.8Z" fill="' + GOLD + '"/>', neck: '<circle cx="14.2" cy="29.6" r="1" fill="' + GOLD + '"/><circle cx="25.8" cy="29.6" r="1" fill="' + GOLD + '"/>', mouth: M.grin, brow: { raise: true, w: 1.3 }, browc: '#4A3320',
      under: line('M20 25.4V26.4', 0.7, '#B27650'),
      acc: '<path d="M12.4 16.2C13.6 15.2 16 16.2 20 16.2C24 16.2 26.4 15.2 27.6 16.2C27.8 19.4 25.4 20.8 23.2 20.6C21.6 20.5 20.8 19.4 20 19.4C19.2 19.4 18.4 20.5 16.8 20.6C14.6 20.8 12.2 19.4 12.4 16.2Z" fill="#243B8B"/><ellipse cx="16.9" cy="18.2" rx="1.5" ry=".9" fill="#fff"/><ellipse cx="23.1" cy="18.2" rx="1.5" ry=".9" fill="#fff"/><circle cx="17.1" cy="18.2" r=".55" fill="' + K + '"/><circle cx="23.3" cy="18.2" r=".55" fill="' + K + '"/>',
      front: '<path d="M12.2 17.4C11 10.5 14.6 7.2 20 7.2C25.6 7.2 29 10.4 27.8 17.4C27.4 14.4 25.6 12.2 22.6 11.4C18.8 12.4 14.6 13.2 12.2 17.4Z" fill="HAIR"/><path d="M15 9.4C17.4 7.8 21 7.6 23.8 8.6" fill="none" stroke="HI" stroke-width=".9" stroke-linecap="round"/>' }),
    sleuth: person({ skin: 'fair', hair: '#6A4A2E', top: '#7A6A58', outfit: '<path d="M13.8 28.6L17.6 27.8L19 33L14.6 33.4Z" fill="#8F7F69"/><path d="M26.2 28.6L22.4 27.8L21 33L25.4 33.4Z" fill="#8F7F69"/><path d="M8 36L12 40M16 34L20 40M24 34L28 40" stroke="#6A5B4A" stroke-width=".6"/>', mouth: M.smirk, brow: { raise: true, w: 1.4 }, browc: '#6A4A2E',
      hat: '<path d="M11.6 13.4C11.4 7.4 15.4 5.8 20 5.8C24.6 5.8 28.6 7.4 28.4 13.4C25.4 12.2 14.6 12.2 11.6 13.4Z" fill="#8A6A44"/><path d="M13.4 12.4C16 14.4 24 14.4 26.6 12.4L27 14C24.6 16 15.4 16 13 14Z" fill="#6B4F2E"/><path d="M11.4 13C9.8 15.6 10.2 18 11.8 19.4L12.8 14Z" fill="#6B4F2E"/><path d="M28.6 13C30.2 15.6 29.8 18 28.2 19.4L27.2 14Z" fill="#6B4F2E"/><path d="M14 8.6L16 12M18 7.4V11.6M22 7.4V11.6M26 8.6L24 12" stroke="#6B4F2E" stroke-width=".6" fill="none"/><circle cx="20" cy="5.6" r="1" fill="#6B4F2E"/>',
      prop: '<path d="M27.6 22.6L32.2 27.8" stroke="#6B4F2E" stroke-width="2" stroke-linecap="round"/><circle cx="24.4" cy="19.4" r="4.6" fill="#CFE8F7" fill-opacity=".7" stroke="#6B4F2E" stroke-width="1.1"/><ellipse cx="24.4" cy="19.2" rx="2.3" ry="2.7" fill="#fff" stroke="' + K + '" stroke-width=".5"/><circle cx="24.6" cy="19.4" r="1.2" fill="' + K + '"/><path d="M22.2 17.2Q23 16.2 24.2 16" stroke="#fff" stroke-width=".7" fill="none" stroke-linecap="round"/>' }),
    reggie: person({ skin: 'fair', hair: '#C3C6CC', top: '#2A2A33', outfit: '<path d="M16.2 29.2L20 36.6L23.8 29.2Z" fill="#F6F2EA"/><path d="M14 29.4L19.4 38.8L16 40L12 33.2Z" fill="#1A1A22"/><path d="M26 29.4L20.6 38.8L24 40L28 33.2Z" fill="#1A1A22"/>',
      neck: '<path d="M20 30L16.2 28.4V31.4ZM20 30L23.8 28.4V31.4Z" fill="' + RED + '"/><circle cx="20" cy="30" r=".9" fill="' + darken(RED, 0.3) + '"/>', mouth: '', under: blush('#E27C7C'), browc: '#9A9DA6', brow: { w: 1.5 },
      acc: '<circle cx="23.1" cy="18.3" r="2.7" fill="#fff" fill-opacity=".25" stroke="#C9A227" stroke-width=".9"/><path d="M25.7 19.8C27.4 22 27.6 26 26.6 30.4" fill="none" stroke="#C9A227" stroke-width=".5"/>',
      stache: '<path d="M20 21.4C18.6 20.2 15.4 20.4 14 22.4C15 22.8 16.6 22.6 18.2 22.4C19 22.4 19.6 22.6 20 22.6C20.4 22.6 21 22.4 21.8 22.4C23.4 22.6 25 22.8 26 22.4C24.6 20.4 21.4 20.2 20 21.4Z" fill="#2A2A33"/><path d="M14 22.4C13 23.2 13.2 24.6 14.4 24.8M26 22.4C27 23.2 26.8 24.6 25.6 24.8" fill="none" stroke="#2A2A33" stroke-width=".8" stroke-linecap="round"/>',
      front: '<path d="M11.4 13.6C10.2 15.2 10.6 18 12 19.4L12.8 14Z" fill="HAIR"/><path d="M28.6 13.6C29.8 15.2 29.4 18 28 19.4L27.2 14Z" fill="HAIR"/>',
      hat: '<path d="M12.2 12.6C12 6.6 15.6 5.4 20 5.4C24.4 5.4 28 6.6 27.8 12.6Z" fill="#2A2A33"/><path d="M9.4 12.6C12 14.4 28 14.4 30.6 12.6C30.6 14.2 26 15 20 15C14 15 9.4 14.2 9.4 12.6Z" fill="#1A1A22"/><path d="M12.2 11.2C16 12.6 24 12.6 27.8 11.2L27.8 12.6C24 14 16 14 12.2 12.6Z" fill="' + RED + '"/><path d="M15 7.6C16.6 6.6 18.6 6.4 20.4 6.6" fill="none" stroke="#5A5A66" stroke-width=".8" stroke-linecap="round"/>' }),
    will: person({ skin: 'fair', hair: '#4A3426', top: '#1F1F27', outfit: '<g fill="' + GOLD + '"><circle cx="20" cy="34.4" r=".6"/><circle cx="20" cy="36.8" r=".6"/><circle cx="20" cy="39.2" r=".6"/></g>', brow: { raise: true }, browc: '#4A3426', mouth: line('M18.4 23.8Q20 24.8 21.6 23.8', 0.9, '#B07070'),
      neck: '<g fill="#F4F1EA" stroke="#CFC8B8" stroke-width=".4"><circle cx="13.4" cy="29.6" r="2"/><circle cx="15.8" cy="30.8" r="2"/><circle cx="18.4" cy="31.4" r="2"/><circle cx="21.6" cy="31.4" r="2"/><circle cx="24.2" cy="30.8" r="2"/><circle cx="26.6" cy="29.6" r="2"/></g>',
      stache: '<path d="M20 22C18.8 21.4 16.6 21.6 15.6 22.8C17 22.8 18.6 22.6 20 22.8C21.4 22.6 23 22.8 24.4 22.8C23.4 21.6 21.2 21.4 20 22Z" fill="HAIR"/><path d="M18.8 25L20 28L21.2 25Z" fill="HAIR"/>',
      back: '<path d="M10.4 15C9.6 9 13.4 7.2 16.2 7.8L16.8 12C14.2 13.4 12.8 16 12.8 20L12.6 27.4C11 27.6 10.2 25.6 10.4 22Z" fill="HAIR"/><path d="M29.6 15C30.4 9 26.6 7.2 23.8 7.8L23.2 12C25.8 13.4 27.2 16 27.2 20L27.4 27.4C29 27.6 29.8 25.6 29.6 22Z" fill="HAIR"/>',
      front: '<path d="M14.4 11C16.4 9 23.6 9 25.6 11C24 10.2 16 10.2 14.4 11Z" fill="HAIR"/><circle cx="12.4" cy="23.6" r="1.1" fill="none" stroke="' + GOLD + '" stroke-width=".7"/>' }),
    guard: person({ skin: 'warm', hair: '#2B2420', top: RED, outfit: '<path d="M12 29.8L28 40M28 29.8L12 40" stroke="#F4F1EA" stroke-width="1.6"/><g fill="' + GOLD + '"><circle cx="20" cy="34.2" r=".8"/><circle cx="20" cy="37.2" r=".8"/></g>', neck: '<path d="M16 29L20 31L24 29V30.4L20 32.6L16 30.4Z" fill="#7A1520"/>', mouth: M.flat, browc: '#3A2A22', brow: { w: 1.3 },
      hat: '<path d="M11 15C10.4 6.4 14.4 2.4 20 2.4C25.6 2.4 29.6 6.4 29 15C26.4 13 13.6 13 11 15Z" fill="#2B2420"/><path d="M14 6.6C14.6 9 14.4 11 14 12.6M17.4 4.4C18 7.4 17.8 10 17.4 12.4M21 4C21.6 7 21.4 10 21 12.4M24.4 4.8C25 7.6 24.8 10 24.4 12.4M27 7.4C27.4 9.4 27.2 11 26.8 12.4" stroke="#4A403A" stroke-width=".7" fill="none" stroke-linecap="round"/><path d="M11.8 14.4C15 15.6 25 15.6 28.2 14.4" fill="none" stroke="#1A1614" stroke-width="1.2"/><path d="M12.8 15L13.2 22.6M27.2 15L26.8 22.6" fill="none" stroke="' + GOLD + '" stroke-width=".9"/><path d="M12.6 7.4C10.8 5.4 9.2 6.8 9.6 9.2C10 11.4 11.6 11.6 12.6 10.8Z" fill="' + RED + '"/>' }),
    prof: person({ skin: 'tan', hair: '#ECE9E2', top: '#6A5A48', outfit: '<path d="M16.4 29.2L20 33.4L23.6 29.2Z" fill="#F4F1EA"/><path d="M14 29.4L19 38.8L16 40L11.8 33Z" fill="#54483A"/><path d="M26 29.4L21 38.8L24 40L28.2 33Z" fill="#54483A"/><rect x="11" y="36" width="3.4" height="2.6" rx=".6" fill="#8A6A44" transform="rotate(-18 12.7 37.3)"/>',
      neck: '<path d="M20 30L16.4 28.6V31.4ZM20 30L23.6 28.6V31.4Z" fill="#B8434A"/><circle cx="20" cy="30" r=".9" fill="#8A2E36"/>', mouth: M.grin, browc: '#ECE9E2', brow: { raise: true, w: 1.6 }, acc: glasses('#3A3F4B'),
      back: '<g fill="HAIR"><circle cx="10" cy="14.4" r="4.4"/><circle cx="13" cy="9" r="4.4"/><circle cx="18.2" cy="6.6" r="4.6"/><circle cx="23.6" cy="6.8" r="4.6"/><circle cx="28.4" cy="9.6" r="4.4"/><circle cx="31" cy="15" r="4.2"/><circle cx="10.4" cy="21.2" r="3"/><circle cx="30.2" cy="21.4" r="3"/></g>',
      stache: '<path d="M20 21.2C18.4 20.2 15.8 20.4 15 22C16.4 22.6 18.4 22.2 20 22.4C21.6 22.2 23.6 22.6 25 22C24.2 20.4 21.6 20.2 20 21.2Z" fill="HAIR" stroke="#CFC8BA" stroke-width=".3"/>',
      front: '<path d="M13.4 11.4C15.4 9.4 24.6 9.4 26.6 11.4C24.6 10.6 15.4 10.6 13.4 11.4Z" fill="HAIR"/>' }),
    fox: '<path d="M8 19L9.5 6.5L17.2 13Z" fill="#E8772E"/><path d="M32 19L30.5 6.5L22.8 13Z" fill="#E8772E"/>' +
      '<path d="M10.8 15L11.3 10.2L14.6 13.2Z" fill="#7A3B1B"/><path d="M29.2 15L28.7 10.2L25.4 13.2Z" fill="#7A3B1B"/>' +
      '<path d="M7.2 19.5C7.2 14.4 12.6 12 20 12C27.4 12 32.8 14.4 32.8 19.5C32.8 26.5 26.5 33.5 20 35C13.5 33.5 7.2 26.5 7.2 19.5Z" fill="#E8772E"/>' +
      '<path d="M8.4 22C13 22.6 17 26 20 29.5C23 26 27 22.6 31.6 22C30.6 28 25.5 33.2 20 34.2C14.5 33.2 9.4 28 8.4 22Z" fill="#FBF3E8"/>' +
      '<path d="M12.4 19.6Q14.4 18 16.4 19.6Q14.4 21.2 12.4 19.6Z" fill="' + K + '"/><path d="M23.6 19.6Q25.6 18 27.6 19.6Q25.6 21.2 23.6 19.6Z" fill="' + K + '"/><path d="M18.2 28.4H21.8L20 30.6Z" fill="' + K + '"/>',
    ember: '<path d="M20 4.5C21.4 10.8 30 14 30 24.5C30 30.6 25.8 34.8 20 34.8C14.2 34.8 10 30.6 10 24.5C10 20.8 12 18.2 14.4 15.8C14.8 18 15.8 19.6 17.6 20.4C16.4 14.4 17.6 9 20 4.5Z" fill="#F26A1B"/>' +
      '<path d="M20 18C22.8 22 26 24.6 26 28.8C26 32 23.4 33.8 20 33.8C16.6 33.8 14 32 14 28.8C14 25.6 17.4 22.8 20 18Z" fill="#FFC93C"/>' +
      '<path d="M14.6 25.4H25.4V27C25.4 28.4 24.4 29 23.4 29H22.4C21.4 29 20.8 28.4 20.6 27.6H19.4C19.2 28.4 18.6 29 17.6 29H16.6C15.6 29 14.6 28.4 14.6 27Z" fill="' + K + '"/><path d="M16 26.2H17.6M21.6 26.2H23.2" stroke="#fff" stroke-width=".6" opacity=".55" stroke-linecap="round"/><path d="M18 31Q20.4 32.4 22.4 30.6" fill="none" stroke="' + K + '" stroke-width=".9" stroke-linecap="round"/>'
  };
  var AV_COLORS = { raspberry: ['#DE3163', '#FFFFFF'], gold: ['#DEC17A', '#020101'], ink: ['#1E1E2C', '#DEC17A'], cream: ['#F3EAD3', '#8A6A22'], plum: ['#4A1730', '#DEC17A'], sand: ['#A39E93', '#020101'] };
  var AV_NAMES = { flame: 'Flame', spark: 'Spark', bolt: 'Bolt', sun: 'Sun', thermo: 'Thermometer', wave: 'Wave', comet: 'Comet', leaf: 'Leaf',
    vera: 'Vera', marco: 'Marco', cleo: 'Cleo', hana: 'Hana', fay: 'Fay', june: 'June', dev: 'Dev', eli: 'Eli', gus: 'Gus', ivan: 'Ivan',
    nova: 'Nova', captain: 'Captain', sleuth: 'Sleuth', reggie: 'Reggie', will: 'Will', guard: 'Guard', prof: 'Professor', fox: 'Fox', ember: 'Ember', initial: 'My initial',
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

  window.UI = { avatar: avatar, AV_GLYPHS: Object.keys(AV_GLYPHS), AV_CHARS: Object.keys(AV_CHARS), AV_PEOPLE: ['vera', 'marco', 'cleo', 'hana', 'fay', 'june', 'dev', 'eli', 'gus', 'ivan'], AV_FUN: ['nova', 'captain', 'sleuth', 'reggie', 'will', 'guard', 'prof', 'ember', 'fox'], AV_COLORS: Object.keys(AV_COLORS), AV_NAMES: AV_NAMES, AV_COLOR_VALUES: AV_COLORS, h: h, icon: icon, api: api, fmtDuration: fmtDuration, fmtAgo: fmtAgo, fmtDate: fmtDate, toast: toast, modal: modal };
})();
