#!/usr/bin/env python3
"""Build all course files from tools/units/uNN.py (+ tools/units/extras.py).
Usage: python3 tools/build.py            (all units)
       python3 tools/build.py 1 3        (only units 1 and 3)
Level:  EF_LEVEL=B1 (default). Output goes to courses/<level>/unit-NN/ and dist/ (dist/<level>/ for levels other than B1).
Rules implemented here are written down in docs/BUILD-RULES-FOR-NEXT-LEVELS.md.
"""
import csv, importlib.util, io, json, os, random, re, shutil, sys, uuid, zipfile
from html import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEVEL = os.environ.get("EF_LEVEL", "B1").upper()
LVL = LEVEL.lower()
DIST = os.path.join(ROOT, "dist") if LEVEL == "B1" else os.path.join(ROOT, "dist", LVL)
# words to write, number of unit words to use in the written task (docs section 6)
WRITING_SIZE = {"A1": ("60–80", 4), "A2": ("60–80", 4), "B1": ("100–120", 6), "B2": ("150–180", 8), "C1": ("150–180", 8), "C2": ("150–180", 8)}
WORDS, VOCAB_N = WRITING_SIZE.get(LEVEL, ("100–120", 6))

H5P_LIBS = {
    "blanks": ("H5P.Blanks", 1, 14), "drag": ("H5P.DragText", 1, 10),
    "choice": ("H5P.SingleChoiceSet", 1, 11), "cards": ("H5P.Dialogcards", 1, 9),
    "mark": ("H5P.MarkTheWords", 1, 11),
}
SC_BEHAVIOUR = {"timeoutCorrect": 2000, "timeoutWrong": 3000, "soundEffectsEnabled": True,
                "enableRetry": True, "enableSolutionsButton": True, "passPercentage": 70, "autoContinue": True}

def split(s): return [p.strip() for p in s.split("|")]

# ---------- H5P content builders ----------
def c_blanks(items, intro):
    return {"text": f"<p>{escape(intro)}</p>", "questions": [f"<p>{i}</p>" for i in items],
            "behaviour": {"enableRetry": True, "enableSolutionsButton": True, "caseSensitive": False,
                          "autoCheck": False, "separateLines": True}}
def c_drag(items, intro):
    return {"taskDescription": f"<p>{escape(intro)}</p>", "textField": "\n".join(items),
            "behaviour": {"enableRetry": True, "enableSolutionsButton": True, "instantFeedback": False}}
def c_choice(items, intro=None):
    ch = []
    for it in items:
        q, *ans = split(it)           # first answer is the correct one
        ch.append({"subContentId": str(uuid.uuid4()), "question": f"<p>{q}</p>", "answers": [f"<p>{a}</p>" for a in ans]})
    return {"choices": ch, "behaviour": SC_BEHAVIOUR}
def c_cards(items, title):
    # title shown once; description left empty (it used to repeat the title)
    return {"title": f"<p>{escape(title)}</p>", "mode": "normal", "description": "",
            "dialogs": [{"text": f"<p>{f}</p>", "answer": f"<p>{b}</p>"} for f, b in items],
            "behaviour": {"enableRetry": True, "randomCards": True, "disableBackwardsNavigation": False, "scaleTextNotCard": False}}
def c_mark(text, intro):
    return {"taskDescription": f"<p>{escape(intro)}</p>", "textField": text,
            "behaviour": {"enableRetry": True, "enableSolutionsButton": True}}

def write_h5p(kind, name, title, content, outdir):
    lib, maj, mino = H5P_LIBS[kind]
    meta = {"title": title, "language": "en", "mainLibrary": lib, "embedTypes": ["iframe"], "license": "U",
            "preloadedDependencies": [{"machineName": lib, "majorVersion": maj, "minorVersion": mino}]}
    path = os.path.join(outdir, f"{name}.h5p")
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("h5p.json", json.dumps(meta, indent=1))
        z.writestr("content/content.json", json.dumps(content, indent=1, ensure_ascii=False))
    return {"name": name, "title": title, "type": lib, "items": count(kind, content)}
def count(kind, c):
    if "choices" in c: return len(c["choices"])
    if "dialogs" in c: return len(c["dialogs"])
    text = " ".join(c["questions"]) if "questions" in c else c["textField"]
    return text.count("*") // 2          # number of gaps / marked words

# ---------- page helpers (ef-box templates, docs section 3) ----------
def slugify(title):
    """Same idea as WordPress sanitize_title: lowercase, non-alphanumerics become single hyphens."""
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", title.lower())).strip("-")
def sc(title): return f'[h5p slug="{slugify(title)}"]'
def box(kind, title, body):
    return f'<div class="ef-box ef-box--{kind}">\n<h3>{title}</h3>\n{body}\n</div>\n'
def tabula(html): return html.replace("<table>", '<table class="ef-tabula">')
def table(rows, head):
    h = "".join(f"<th>{escape(x)}</th>" for x in head)
    b = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="ef-tabula"><tr>{h}</tr>{b}</table>'
def rinda(a, b): return f'<div class="ef-rinda">\n<div class="ef-kolonna">\n{a}</div>\n<div class="ef-kolonna">\n{b}</div>\n</div>\n'
def loose_h3(text): return f'<h3 style="margin:32px 0 18px">{text}</h3>\n'
def page(title_icon, body): return f"<h2>{title_icon}</h2>\n{body}"
def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(text)
def task(title, shortcode): return f"<h4>{title}</h4>\n{shortcode}\n"

WARN = re.compile(r"^(Watch out|Common mistake|Be careful|Careful)", re.I)
TIPS = re.compile(r"^(Tip|Quick test|Time words|Study tip|Signal words|Notice)", re.I)
def sections(html, icon="📘"):
    """Split a lesson's HTML (with <h2> sections) into neutral boxes; warnings -> pink boxes, tips -> yellow boxes."""
    out = []
    for part in re.split(r"(?=<h2>)", html.strip()):
        if not part.strip(): continue
        m = re.match(r"<h2>(.*?)</h2>", part, re.S)
        title, body = (m.group(1), part[m.end():]) if m else ("", part)
        extra = []
        def pull(mm):
            label = re.sub(r"[:!]\s*$", "", mm.group(1).strip())
            if WARN.match(label): extra.append(box("rozs", f"⚠️ {mm.group(1).strip().rstrip(':')}", f"<p>{mm.group(2).strip()}</p>")); return ""
            if TIPS.match(label): extra.append(box("tip", f"💡 {mm.group(1).strip().rstrip(':')}", f"<p>{mm.group(2).strip()}</p>")); return ""
            return mm.group(0)
        body = re.sub(r"<p><strong>([^<]*)</strong>(.*?)</p>", pull, body, flags=re.S)
        if body.strip() or title: out.append(box("vocab", f"{icon} {title}".strip(), tabula(body.strip())))
        out.extend(extra)
    return "".join(out)

def speaking_practice(qs):
    return box("speaking", "🗣️ Speaking practice", "<ol>" + "".join(f"<li>{escape(q)}</li>" for q in qs) + "</ol>")

# ---------- exam tips from the real task type (docs section 4) ----------
def reading_tips(questions):
    """Tips follow the task type the learner sees on THIS page. The practice is a/b/c multiple choice, so the tips are
    multiple-choice tips. A True / False / Not given tip is only written when EVERY question on the page has that format."""
    if all(q.startswith("True, False or Not given") for q in questions):
        tips = ["Read the title and look at the text quickly.", "Read each statement. Then find the part of the text about it.",
                "<em>True</em> = the text says the same. <em>False</em> = the text says the opposite. <em>Not given</em> = the text does not say it."]
    else:
        tips = ["Read the title and look at the text quickly.",
                "Read each question. Then find the part of the text that answers it.",
                "Check all the options (a, b, c). Wrong options often use words from the text, but they say something different."]
    return box("tip", "💡 Exam tips", "<ol>" + "".join(f"<li>{t}</li>" for t in tips) + "</ol>")
def listening_tips():
    tips = ["Read the questions and the three options before you listen.", "Listen for the main idea, not for every word.",
            "Wrong options may use a word from the recording, but they say something different.",
            "Choose one answer for every question, even if you are not sure."]
    return box("tip", "💡 Exam tips", "<ol>" + "".join(f"<li>{t}</li>" for t in tips) + "</ol>")

# ---------- shared teaching text (easy English) ----------
WRITING_SECTIONS = [
 ("1. Formal or informal?", """<p>We choose our words for the reader. We write <strong>informal</strong> emails to friends and family. We write <strong>formal</strong> emails to a boss, a teacher, a company or someone we do not know.</p>""" + table([
    ["Hi Anna, / Dear Anna,", "Dear Mr Brown, / Dear Ms Smith, / Dear Sir or Madam,"],
    ["Thanks for your email. / Great to hear from you!", "Thank you for your email. / I am writing to ask about ..."],
    ["Can you ...? / Could you ...?", "Could you please ...? / I would be grateful if you could ..."],
    ["I'm sorry, but I can't ...", "Unfortunately, I am unable to ..."],
    ["Write soon! / See you! / Take care,", "I look forward to hearing from you. / Thank you for your help."],
    ["Love, / Best wishes, / Bye for now,", "Yours sincerely, (name known) / Yours faithfully, (name not known)"],
 ], ["Informal (friends)", "Formal (work, school, companies)"]) + """<p><strong>Tips:</strong> In informal emails you can use short forms (<em>I'm, can't</em>), phrasal verbs and exclamation marks. In formal emails use full forms (<em>I am, cannot</em>), polite words (<em>please, would, could</em>) and no slang.</p>"""),
 ("2. A good email has four parts", """<ol><li><strong>Greeting</strong> – Dear ... / Hi ...</li><li><strong>Reason</strong> – why you are writing (1 sentence)</li><li><strong>Main part</strong> – the details, one idea in each paragraph</li><li><strong>Ending</strong> – a closing sentence and a sign-off</li></ol>"""),
 ("3. Coherence and cohesion", """<p><strong>Coherence</strong> means your ideas are in a clear order and the reader can follow them. Use paragraphs. Put one idea in each paragraph.</p>
<p><strong>Cohesion</strong> means the sentences are joined with small words. Use linking words:</p>""" + table([
    ["adding", "and, also, too, as well as, in addition, moreover (formal)"],
    ["contrast", "but, however, although, on the other hand, in spite of"],
    ["reason / result", "because, so, as, therefore, that is why"],
    ["order", "first, then, after that, finally, at the end"],
    ["example", "for example, for instance, such as"],
 ], ["Use", "Linking words"]) + """<p>Also use <strong>reference words</strong> so you do not repeat nouns: <em>My brother has a new job. <u>He</u> likes <u>it</u> very much. <u>This</u> is good news.</em></p>"""),
]
SPEAKING_FORMAT = """<ol>
<li><strong>Part 1 – Interview (2–3 minutes).</strong> The examiner asks you personal questions about your life and the unit topics. Give answers of 2–4 sentences, not just "yes" or "no".</li>
<li><strong>Part 2 – Long turn (1 minute).</strong> You talk alone about a picture or a topic. Do not stop! If you forget a word, explain it in other words (<em>It's a thing you use to ...</em>).</li>
<li><strong>Part 3 – Discussion (3 minutes).</strong> You and another student (or the examiner) talk about a question together. Give your opinion, ask for the other opinion, and agree or disagree politely.</li>
</ol>
<h4>Useful phrases</h4>
""" + table([
    ["Starting an answer", "Well, ... / Let me think. / That's an interesting question."],
    ["Giving an opinion", "I think ... / In my opinion, ... / I'd say that ..."],
    ["Giving a reason", "The reason is ... / That's because ... / This is why ..."],
    ["Agreeing / disagreeing", "I agree. / Exactly! / I see your point, but ... / I'm not sure about that."],
    ["Asking for help", "Sorry, could you repeat that? / What I mean is ..."],
], ["Function", "Phrases"])

# ---------- loading and checks ----------
def load(n):
    spec = importlib.util.spec_from_file_location(f"u{n:02d}", os.path.join(ROOT, "tools", "units", f"u{n:02d}.py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m.UNIT
def load_extras():
    spec = importlib.util.spec_from_file_location("extras", os.path.join(ROOT, "tools", "units", "extras.py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def check_unit(n, u, ex):
    """Fail loudly on malformed items: every MC item needs a question + 2-3 distinct answers; practice sets need 8+ items."""
    groups = {"pool": u["pool"], "grammar.choice": u["grammar"]["choice"], "vocab.choice": u["vocab"]["choice"],
              "reading_a": u["reading_a"]["questions"], "reading_b": u["reading_b"]["questions"],
              "listening_a": u["listening_a"]["questions"], "listening_b": u["listening_b"]["questions"],
              "writing.register": u["writing"]["register"]}
    for name, items in groups.items():
        assert name == "pool" or len(items) >= 8, f"unit {n}: {name} has {len(items)} items (<8)"
        for it in items:
            p = split(it)
            assert len(p) in (3, 4) and len(set(p[1:])) == len(p) - 1, f"unit {n}: bad item in {name}: {it!r}"
    for name, items in {"grammar.blanks": u["grammar"]["blanks"], "grammar.drag": u["grammar"]["drag"], "vocab.blanks": u["vocab"]["blanks"],
                        "vocab.drag": u["vocab"]["drag"], "writing.drag": u["writing"]["drag"]}.items():
        assert len(items) >= 8 and all(i.count("*") >= 2 and i.count("*") % 2 == 0 for i in items), f"unit {n}: bad gaps in {name}"
    assert len(u["vocab"]["words"]) >= 12 and len(u["speaking"]["cards"]) >= 10
    assert u["writing"]["mark_text"].count("*") // 2 >= 8
    assert len(u["pool"]) >= 40, f"unit {n}: pool must have 40 items, has {len(u['pool'])}"
    sp = ex.SPEAKING.get(n)
    assert sp and len(sp["grammar"]) == 10 and len(sp["vocab"]) == 10, f"unit {n}: extras.py needs exactly 10 + 10 speaking questions"
    assert n in ex.GRAMMAR_LABEL, f"unit {n}: extras.py needs a GRAMMAR_LABEL"

# ---------- Tutor LMS quiz CSV (docs section 8) ----------
QUOTA = lambda s: s  # text is used as is; the check below rejects anything unsafe
def quiz_question(item, order):
    q, *ans = split(item)
    m = re.match(r"True, False or Not given:\s*(.*)", q)
    title, text = ("True, False or Not given", m.group(1)) if m else ("Choose the correct answer", q)
    correct = ans[0]
    return {"title": title, "text": text, "order": order, "answers": ans, "correct": correct, "explanation": f"Correct answer: {correct}"}
def quiz_csv(title, intro, settings, items, rng):
    """settings: dict(time, attempts, pass_, shown, order, feedback). Returns CSV text."""
    buf = io.StringIO(); w = csv.writer(buf, quoting=csv.QUOTE_ALL, lineterminator="\n")
    w.writerow(["settings", title, intro, settings["time"], "minutes", "0", settings["attempts"], settings["pass_"], settings["shown"],
                "0", "single_question", settings["order"], "0", "200", "500", settings["feedback"], "0", "0", "0", "percent", "0"])
    for i, it in enumerate(items, 1):
        q = quiz_question(it, i)
        w.writerow(["question", q["title"], f"<p>{q['text']}</p>", "single_choice", "1.00", i, "", "", "1", f"<p>{q['explanation']}</p>", ""])
        shuffled = q["answers"][:]; rng.shuffle(shuffled)
        for j, a in enumerate(shuffled, 1):
            w.writerow(["answer", a, "text", "1" if a == q["correct"] else "0", "0", "", j])
    return buf.getvalue()
def check_quiz_csv(text, name, n_questions, shown):
    """Self-check from docs section 8. Raises AssertionError."""
    assert "\\" not in text, f"{name}: backslash found"
    rows = list(csv.reader(io.StringIO(text), delimiter=",", quotechar='"', escapechar=None))
    assert rows and rows[0][0] == "settings" and sum(r[0] == "settings" for r in rows) == 1, f"{name}: first row must be the only settings row"
    cols = {"settings": 21, "question": 11, "answer": 7}
    nq, cur = 0, None
    for r in rows:
        assert r[0] in cols and len(r) == cols[r[0]], f"{name}: bad row {r[:2]} ({len(r)} columns)"
        if r[0] == "answer":
            assert not re.search(r"[<>]", r[1]), f"{name}: tags in answer {r[1]!r}"
            cur.append(r[3])
        if r[0] == "question":
            if cur is not None: assert cur.count("1") == 1, f"{name}: question needs exactly one correct answer"
            cur = []; nq += 1
            assert r[1].lower() not in r[2].lower() or not r[2], f"{name}: instruction repeated in question text: {r[2]!r}"
    assert cur.count("1") == 1, f"{name}: last question needs exactly one correct answer"
    assert nq == n_questions, f"{name}: {nq} questions, expected {n_questions}"
    assert int(rows[0][8]) == shown, f"{name}: shown={rows[0][8]}, expected {shown}"

# ---------- assignment (docs section 6) ----------
def assignment_html(n, u, ex):
    w = u["writing"]; g = ex.GRAMMAR_LABEL[n]
    rubric = table([
        ["<strong>Grammar</strong><br>" + g[0].upper() + g[1:], "Used correctly in most sentences. Only small mistakes.", "Used, but several mistakes. Sometimes the meaning is not clear.", "Missing or mostly incorrect."],
        ["<strong>Vocabulary</strong><br>Words from the Unit %d word list" % n, f"{VOCAB_N} or more words or phrases used correctly and naturally.", f"{max(VOCAB_N//2,2)}–{VOCAB_N-1} used. Some are incorrect.", f"0–{max(VOCAB_N//2,2)-1} used."],
        ["<strong>Writing phrases and structure</strong><br>From the Writing lesson", "Correct greeting and ending for the register, clear reason for writing, paragraphs, 3 or more linking words.", "Most are present, but register or linking words are not always correct.", "Few are present. Structure unclear or wrong register."],
    ], ["Criteria", "5 points", "3 points", "1 point"])
    return (box("tip", "🎯 What to do", f"<p>Write <strong>one</strong> email ({WORDS} words). Choose Option A or Option B. You can write in the text box or upload a file. You may write the second email for extra practice and send it as a second file.</p>")
        + loose_h3("✍️ Choose your task")
        + rinda(box("vocab", "✉️ Option A: informal email", f"<p>{w['own_informal']}</p>"), box("vocab", "✉️ Option B: formal email", f"<p>{w['own_formal']}</p>"))
        + box("vocab", "📋 How your work is assessed", f"<p>Total: 15 points (3 criteria × 5 points). To pass: 9 points.</p>{rubric}")
        + box("tip", "💡 Check before you hand in", "<ul><li>☐ Greeting and ending are right for the email type</li><li>☐ Clear reason for writing</li><li>☐ Paragraphs, one idea in each</li><li>☐ At least 3 linking words</li><li>☐ Unit grammar and unit words used</li><li>☐ Word count: " + WORDS + "</li></ul>"))

# ---------- main build ----------
def build_unit(n, ex):
    u = load(n); U = f"u{n:02d}"
    check_unit(n, u, ex)
    for k in ("listening_a", "listening_b"):
        sc_ = u[k]["script"]; u[k]["script_md"] = sc_
        u[k]["script_html"] = "<p>" + escape(sc_).replace("\n\n", "</p><p>").replace("\n", "<br>") + "</p>"
    out = os.path.join(ROOT, "courses", LVL, f"unit-{n:02d}")
    shutil.rmtree(out, ignore_errors=True)
    h5pdir = os.path.join(DIST, "h5p"); os.makedirs(h5pdir, exist_ok=True)
    for f in os.listdir(h5pdir):
        if f.startswith(U + "-"): os.remove(os.path.join(h5pdir, f))
    reg = []
    def h5p(kind, short, title, content):
        full = f"{LEVEL} Unit {n} – {title}"
        reg.append(write_h5p(kind, f"{U}-{short}", full, content, h5pdir)); reg[-1]["slug"] = slugify(full); return sc(full)
    P = {}
    sp = ex.SPEAKING[n]

    # 1 GRAMMAR
    g = u["grammar"]
    practice = (task("Task 1: Type the missing words", h5p("blanks", "grammar-blanks", "Grammar: type the answer", c_blanks(g["blanks"], "Type the correct form of the verb or the missing word.")))
        + task("Task 2: Choose the right answer", h5p("choice", "grammar-choice", "Grammar: choose the answer", c_choice(g["choice"])))
        + task("Task 3: Drag the words", h5p("drag", "grammar-drag", "Grammar: drag the words", c_drag(g["drag"], "Drag each word or phrase to the correct gap."))))
    P["1-grammar"] = page(f"🧩 Unit {n} · Grammar: {g['title']}",
        box("tip", "🎯 Goal", f"<p>You will learn to {g['goal'].rstrip('.')}.</p>")
        + sections(g["html"]) + box("praksa", "✏️ Practice", practice) + speaking_practice(sp["grammar"]))

    # 2 VOCABULARY
    v = u["vocab"]; words = [split(w) for w in v["words"]]
    wl = table([[f"<strong>{w[0]}</strong>", w[1], w[2], f"<em>{w[3]}</em>"] for w in words], ["Word / phrase", "Type", "Meaning", "Example"])
    cards = h5p("cards", "vocab-flashcards", "Vocabulary flashcards", c_cards([(w[0], f"{w[2]}<br><em>{w[3]}</em>") for w in words], f"Flashcards: {u['topic']}"))
    practice = (task("Task 1: Type the missing word", h5p("blanks", "vocab-blanks", "Vocabulary: type the word", c_blanks(v["blanks"], "Type the missing word. The first letters help you.")))
        + task("Task 2: Choose the right word", h5p("choice", "vocab-choice", "Vocabulary: choose the word", c_choice(v["choice"])))
        + task("Task 3: Drag the words", h5p("drag", "vocab-drag", "Vocabulary: drag the words", c_drag(v["drag"], "Drag the words into the sentences."))))
    P["2-vocabulary"] = page(f"🔤 Unit {n} · Vocabulary: {u['topic']}",
        box("tip", "🎯 Goal", f"<p>You will learn {len(words)} useful words and phrases about <em>{u['topic']}</em>.</p>")
        + box("vocab", "🔤 Word list", wl) + box("praksa", "🃏 Flashcards", "<p>Look at the word. Say the meaning. Then turn the card.</p>\n" + cards)
        + box("praksa", "✏️ Practice", practice) + speaking_practice(sp["vocab"]))

    # 3 READING (tip comes from the questions on THIS page)
    ra = u["reading_a"]
    P["3-reading"] = page(f"📖 Unit {n} · Reading (exam practice)", reading_tips(ra["questions"])
        + box("vocab", f"📄 {ra['title']}", ra["text"])
        + box("praksa", "✏️ Questions", h5p("choice", "reading-practice", "Reading exam practice", c_choice(ra["questions"]))))

    # 4 LISTENING
    la = u["listening_a"]
    audio = f'<p>[audio src="/wp-content/uploads/english-fever/{LVL}-unit-{n:02d}-listening-practice.mp3"]</p>\n<p>Listen twice, if you need to.</p>'
    P["4-listening"] = page(f"🎧 Unit {n} · Listening (exam practice)", listening_tips()
        + box("listening", f"🎧 {la['title']}", audio)
        + box("praksa", "✏️ Questions", h5p("choice", "listening-practice", "Listening exam practice", c_choice(la["questions"])))
        + box("vocab", "📜 Script", f'<details><summary>Show the script (read it after you finish)</summary>{la["script_html"]}</details>'))

    # 5 SPEAKING
    s = u["speaking"]; cards_ = [split(c) for c in s["cards"]]
    P["5-speaking"] = page(f"🗣️ Unit {n} · Speaking (exam practice)",
        box("vocab", "🗣️ How the speaking exam works", SPEAKING_FORMAT)
        + box("praksa", "🃏 Part 1: Interview cards", "<p>Turn a card. Answer the question in 2–4 sentences. The back of the card gives ideas and useful language. Record yourself and listen.</p>\n" + h5p("cards", "speaking-cards", "Interview cards", c_cards([(c[0], c[1]) for c in cards_], f"Interview cards: {u['topic']}")))
        + box("speaking", "🗣️ Part 2: Long turn", f"<p>{s['part2']}</p>")
        + box("speaking", "🗣️ Part 3: Discussion", "<ul>" + "".join(f"<li>{q}</li>" for q in s["part3"]) + "</ul>"))

    # 6 WRITING
    w = u["writing"]
    secs = "".join(box("vocab", f"📘 {t}", b) for t, b in WRITING_SECTIONS)
    ex_boxes = rinda(box("vocab", "✉️ Informal email", f"<p><em>Task: {w['informal_task']}</em></p><blockquote>{w['informal_sample']}</blockquote>"),
                     box("vocab", "✉️ Formal email", f"<p><em>Task: {w['formal_task']}</em></p><blockquote>{w['formal_sample']}</blockquote>"))
    practice = (task("Task 1: Formal or informal? Choose the right phrase", h5p("choice", "writing-register", "Writing: choose the right register", c_choice(w["register"])))
        + task("Task 2: Mark the linking words", h5p("mark", "writing-mark", "Writing: find the linking words", c_mark(w["mark_text"], "Click on all the linking words (words that join ideas).")))
        + task("Task 3: Complete the email with linking words", h5p("drag", "writing-drag", "Writing: complete the email", c_drag(w["drag"], "Drag the linking words and email phrases to the gaps."))))
    own = rinda(box("vocab", "✉️ Option A: informal", f"<p>{w['own_informal']}</p>"), box("vocab", "✉️ Option B: formal", f"<p>{w['own_formal']}</p>"))
    P["6-writing"] = page(f"📝 Unit {n} · Writing: informal and formal emails",
        box("tip", "🎯 Goal", f"<p>You will learn to {w['goal'].rstrip('.')}.</p>") + secs
        + loose_h3(f"📘 4. Unit {n} examples") + ex_boxes
        + box("tip", "💡 Notice", f"<p>{w['notice']}</p>") + box("praksa", "✏️ Practice", practice)
        + box("praksa", "✍️ Your turn", f"<p>Choose <strong>one</strong> email ({WORDS} words) and hand it in in the <strong>Writing assignment</strong> that follows this lesson.</p>{own}"
              "<p><strong>Checklist:</strong> ☐ greeting ☐ reason for writing ☐ paragraphs ☐ 3 linking words ☐ correct register ☐ unit grammar ☐ unit vocabulary ☐ sign-off</p>"))
    for k, body in P.items(): write(os.path.join(out, f"lesson-{k}.html"), body)

    # ASSIGNMENT
    write(os.path.join(out, "assignment", f"writing-assignment-unit-{n}.html"), assignment_html(n, u, ex))
    write(os.path.join(out, "assignment", f"writing-assignment-unit-{n}.json"), json.dumps({
        "title": f"Writing assignment: Unit {n}", "summary_file": f"writing-assignment-unit-{n}.html",
        "assignment_option": {"total_mark": 15, "pass_mark": 9, "upload_files_limit": 2, "upload_file_size_limit": 5,
                              "attempts_allowed": 2, "is_retry_allowed": 1, "time_duration": {"value": 0, "time": "weeks"}},
        "note": "Check 'Total attempts' in Tutor after import (B1 showed 3 although 2 was sent)."}, indent=1))

    # TUTOR LMS quizzes (CSV in Tutor's importer format + a .json copy + the quiz description as HTML)
    rng = random.Random(n)
    qs = [
     (f"Unit {n} Grammar and Vocabulary", "Answer 10 questions. You get new questions every time.", u["pool"], dict(time=15, attempts=0, pass_=70, shown=10, order="rand", feedback="reveal"), None),
     (f"Unit {n} Reading", "Read the text and answer the questions.", u["reading_b"]["questions"], dict(time=20, attempts=3, pass_=60, shown=len(u["reading_b"]["questions"]), order="sorting", feedback="default"),
       f"<h3>{u['reading_b']['title']}</h3>{u['reading_b']['text']}"),
     (f"Unit {n} Listening", "Listen and answer the questions.", u["listening_b"]["questions"], dict(time=20, attempts=3, pass_=60, shown=len(u["listening_b"]["questions"]), order="sorting", feedback="default"),
       f"<h3>{u['listening_b']['title']}</h3><p>[audio src=\"/wp-content/uploads/english-fever/{LVL}-unit-{n:02d}-listening-quiz.mp3\"]</p><p>Listen twice, if you need to. Then answer the questions.</p>"),
    ]
    for title, intro, items, st, descr in qs:
        slug = slugify(title)
        text = quiz_csv(title, intro, st, items, rng)
        check_quiz_csv(text, title, len(items), st["shown"])
        write(os.path.join(out, "tutor-lms", f"{slug}.csv"), text)
        write(os.path.join(out, "tutor-lms", f"{slug}.json"), json.dumps({"title": title, "settings": st, "questions": [quiz_question(i, k) for k, i in enumerate(items, 1)]}, indent=1, ensure_ascii=False))
        if descr: write(os.path.join(out, "tutor-lms", f"{slug}.description.html"), descr)

    # LISTENING SCRIPTS (to record) + SPEAKING CARDS (print)
    write(os.path.join(out, "listening", "scripts-to-record.md"),
          f"# Unit {n} listening scripts (record these; two speakers = two voices)\n\n"
          f"## Practice recording → {LVL}-unit-{n:02d}-listening-practice.mp3\n\n{la['script_md']}\n\n"
          f"## Graded quiz recording → {LVL}-unit-{n:02d}-listening-quiz.mp3\n\n{u['listening_b']['script_md']}\n")
    write(os.path.join(out, "speaking", "interview-cards-print.md"),
          f"# Unit {n} interview cards – {u['topic']}\n\n" + "\n".join(f"**Card {i+1}.** {c[0]}\n\n_Ideas:_ {c[1]}\n" for i, c in enumerate(cards_)))

    idx = [f"# Unit {n}: {u['title']}\n", f"Topic: {u['topic']} · Grammar: {g['title']}\n",
           "## Build order (see docs/BUILD-RULES-FOR-NEXT-LEVELS.md)\n", "1. Upload each file from `dist/h5p/` (H5P Content > Add New > Upload). Do not change the titles.\n",
           "2. Create the 6 lessons from `lesson-*.html` in Tutor LMS (topic: Unit %d).\n" % n,
           "3. Create the Writing assignment from `assignment/`.\n", "4. Import the 3 quizzes from `tutor-lms/*.csv` (one first, open it, then the rest). Put `*.description.html` in the quiz description.\n",
           "5. Record `listening/scripts-to-record.md` and upload the MP3s.\n",
           "\n## H5P activities\n", "| File | Type | Items | Slug used in the lesson page |\n|---|---|---|---|\n"] + [f"| {r['name']}.h5p | {r['type']} | {r['items']} | {r['slug']} |\n" for r in reg]
    write(os.path.join(out, "INDEX.md"), "".join(idx))
    bad = [r for r in reg if r["items"] < 8]
    print(f"{LEVEL} unit {n}: {len(reg)} H5P files, pool={len(u['pool'])}", "UNDER-8: " + str(bad) if bad else "")

if __name__ == "__main__":
    ex = load_extras()
    ns = [int(a) for a in sys.argv[1:]] or [int(f[1:3]) for f in sorted(os.listdir(os.path.join(ROOT, "tools", "units"))) if re.fullmatch(r"u\d\d\.py", f)]
    for n in ns: build_unit(n, ex)
