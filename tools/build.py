#!/usr/bin/env python3
"""Build all course files from tools/units/uNN.py.
Usage: python3 tools/build.py            (all units)
       python3 tools/build.py 1 3        (only units 1 and 3)
Output: courses/b1/unit-NN/ (lesson pages, tutor-lms, speaking, listening scripts)
        dist/h5p/*.h5p        (H5P packages to upload)
"""
import csv, importlib.util, json, os, random, shutil, sys, uuid, zipfile
from html import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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
def c_cards(items, intro):
    return {"title": f"<p>{escape(intro)}</p>", "mode": "normal", "description": escape(intro),
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

# ---------- page helpers ----------
def sc(name): return f'<div class="h5p-activity"><p><em>Activity:</em></p>[h5p id="{name}"]</div>'
def table(rows, head):
    h = "".join(f"<th>{escape(x)}</th>" for x in head)
    b = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f"<table><tr>{h}</tr>{b}</table>"
def page(title, body): return f"<h1>{title}</h1>\n{body}\n"
def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(text)

# ---------- shared teaching text (easy English) ----------
WRITING_CORE = """
<h2>1. Formal or informal?</h2>
<p>We choose our words for the reader. We write <strong>informal</strong> emails to friends and family. We write <strong>formal</strong> emails to a boss, a teacher, a company or someone we do not know.</p>
""" + table([
    ["Hi Anna, / Dear Anna,", "Dear Mr Brown, / Dear Ms Smith, / Dear Sir or Madam,"],
    ["Thanks for your email. / Great to hear from you!", "Thank you for your email. / I am writing to ask about ..."],
    ["Can you ...? / Could you ...?", "Could you please ...? / I would be grateful if you could ..."],
    ["I'm sorry, but I can't ...", "Unfortunately, I am unable to ..."],
    ["Write soon! / See you! / Take care,", "I look forward to hearing from you. / Thank you for your help."],
    ["Love, / Best wishes, / Bye for now,", "Yours sincerely, (name known) / Yours faithfully, (name not known)"],
], ["Informal (friends)", "Formal (work, school, companies)"]) + """
<p><strong>Tips:</strong> In informal emails you can use short forms (<em>I'm, can't</em>), phrasal verbs and exclamation marks. In formal emails use full forms (<em>I am, cannot</em>), polite words (<em>please, would, could</em>) and no slang.</p>

<h2>2. A good email has four parts</h2>
<ol><li><strong>Greeting</strong> – Dear ... / Hi ...</li><li><strong>Reason</strong> – why you are writing (1 sentence)</li><li><strong>Main part</strong> – the details, one idea in each paragraph</li><li><strong>Ending</strong> – a closing sentence and a sign-off</li></ol>

<h2>3. Coherence and cohesion</h2>
<p><strong>Coherence</strong> means your ideas are in a clear order and the reader can follow them. Use paragraphs. Put one idea in each paragraph.</p>
<p><strong>Cohesion</strong> means the sentences are joined with small words. Use linking words:</p>
""" + table([
    ["adding", "and, also, too, as well as, in addition, moreover (formal)"],
    ["contrast", "but, however, although, on the other hand, in spite of"],
    ["reason / result", "because, so, as, therefore, that is why"],
    ["order", "first, then, after that, finally, at the end"],
    ["example", "for example, for instance, such as"],
], ["Use", "Linking words"]) + """
<p>Also use <strong>reference words</strong> so you do not repeat nouns: <em>My brother has a new job. <u>He</u> likes <u>it</u> very much. <u>This</u> is good news.</em></p>
"""

SPEAKING_FORMAT = """
<h2>How the speaking exam works</h2>
<ol>
<li><strong>Part 1 – Interview (2–3 minutes).</strong> The examiner asks you personal questions about your life and the unit topics. Give answers of 2–4 sentences, not just "yes" or "no".</li>
<li><strong>Part 2 – Long turn (1 minute).</strong> You talk alone about a picture or a topic. Do not stop! If you forget a word, explain it in other words (<em>It's a thing you use to ...</em>).</li>
<li><strong>Part 3 – Discussion (3 minutes).</strong> You and another student (or the examiner) talk about a question together. Give your opinion, ask for the other opinion, and agree or disagree politely.</li>
</ol>
<h3>Useful phrases</h3>
""" + table([
    ["Starting an answer", "Well, ... / Let me think. / That's an interesting question."],
    ["Giving an opinion", "I think ... / In my opinion, ... / I'd say that ..."],
    ["Giving a reason", "The reason is ... / That's because ... / This is why ..."],
    ["Agreeing / disagreeing", "I agree. / Exactly! / I see your point, but ... / I'm not sure about that."],
    ["Asking for help", "Sorry, could you repeat that? / What I mean is ..."],
], ["Function", "Phrases"])

# ---------- main build ----------
def load(n):
    spec = importlib.util.spec_from_file_location(f"u{n:02d}", os.path.join(ROOT, "tools", "units", f"u{n:02d}.py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m.UNIT

def tutor_q(item, rng):
    q, *ans = split(item)
    opts = ans[:]; rng.shuffle(opts)
    return {"type": "single_choice", "question": q, "options": opts, "correct": ans[0], "marks": 1}

def build_unit(n):
    u = load(n); U = f"u{n:02d}"
    assert len(u["pool"]) >= 40, f"unit {n}: pool must have 40 items, has {len(u['pool'])}"
    for k in ("listening_a", "listening_b"):
        sc_ = u[k]["script"]; u[k]["script_md"] = sc_
        u[k]["script_html"] = "<p>" + escape(sc_).replace("\n\n", "</p><p>").replace("\n", "<br>") + "</p>"
    out = os.path.join(ROOT, "courses", "b1", f"unit-{n:02d}")
    shutil.rmtree(out, ignore_errors=True)
    h5pdir = os.path.join(ROOT, "dist", "h5p"); os.makedirs(h5pdir, exist_ok=True)
    for f in os.listdir(h5pdir):
        if f.startswith(U + "-"): os.remove(os.path.join(h5pdir, f))
    reg = []   # registry of H5P activities
    def h5p(kind, short, title, content):
        name = f"{U}-{short}"
        reg.append(write_h5p(kind, name, f"B1 Unit {n} – {title}", content, h5pdir)); return sc(name)
    P = {}

    # 1 GRAMMAR
    g = u["grammar"]
    P["1-grammar"] = page(f"Unit {n} · Grammar: {g['title']}",
        f"<p><strong>Goal:</strong> {g['goal']}</p>\n{g['html']}\n<h2>Practice</h2>\n"
        + "<h3>Task 1: Type the missing words</h3>" + h5p("blanks", "grammar-blanks", "Grammar: type the answer", c_blanks(g["blanks"], "Type the correct form of the verb or the missing word."))
        + "<h3>Task 2: Choose the right answer</h3>" + h5p("choice", "grammar-choice", "Grammar: choose the answer", c_choice(g["choice"]))
        + "<h3>Task 3: Drag the words</h3>" + h5p("drag", "grammar-drag", "Grammar: drag the words", c_drag(g["drag"], "Drag each word or phrase to the correct gap.")))

    # 2 VOCABULARY
    v = u["vocab"]
    words = [split(w) for w in v["words"]]
    P["2-vocabulary"] = page(f"Unit {n} · Vocabulary: {u['topic']}",
        f"<p><strong>Goal:</strong> learn {len(words)} useful words and phrases about <em>{u['topic']}</em>.</p>\n<h2>Word list</h2>\n"
        + table([[f"<strong>{w[0]}</strong>", w[1], w[2], f"<em>{w[3]}</em>"] for w in words], ["Word / phrase", "Type", "Meaning", "Example"])
        + "\n<h2>Flashcards</h2><p>Look at the word. Say the meaning. Then turn the card.</p>"
        + h5p("cards", "vocab-flashcards", "Vocabulary flashcards", c_cards([(w[0], f"{w[2]}<br><em>{w[3]}</em>") for w in words], f"Flashcards: {u['topic']}"))
        + "\n<h2>Practice</h2><h3>Task 1: Type the missing word</h3>" + h5p("blanks", "vocab-blanks", "Vocabulary: type the word", c_blanks(v["blanks"], "Type the missing word. The first letters help you."))
        + "<h3>Task 2: Choose the right word</h3>" + h5p("choice", "vocab-choice", "Vocabulary: choose the word", c_choice(v["choice"]))
        + "<h3>Task 3: Drag the words</h3>" + h5p("drag", "vocab-drag", "Vocabulary: drag the words", c_drag(v["drag"], "Drag the words into the sentences.")))

    # 3 READING
    ra = u["reading_a"]
    P["3-reading"] = page(f"Unit {n} · Reading (exam practice)",
        "<p><strong>Exam tips:</strong> 1) Read the title and look at the text quickly. 2) Read the questions. 3) Find the part of the text for each answer. 4) For True / False / Not given: <em>Not given</em> means the text does not say it.</p>\n"
        f"<h2>{ra['title']}</h2>\n<div class=\"reading-text\">{ra['text']}</div>\n<h2>Questions</h2>"
        + h5p("choice", "reading-practice", "Reading exam practice", c_choice(ra["questions"]))
        + f'\n<p>Next: do the graded reading quiz <strong>"Unit {n} Reading"</strong> in Tutor LMS.</p>')

    # 4 LISTENING
    la = u["listening_a"]
    P["4-listening"] = page(f"Unit {n} · Listening (exam practice)",
        "<p><strong>Exam tips:</strong> 1) Read the questions before you listen. 2) You hear the recording twice. 3) Listen for the answer, not for every word. 4) Write an answer for every question.</p>\n"
        f"<h2>{la['title']}</h2>\n<p><em>Audio:</em> [audio src=\"/wp-content/uploads/english-fever/b1-unit-{n:02d}-listening-practice.mp3\"]</p>\n"
        "<p>Listen twice. Then answer the questions.</p>" + h5p("choice", "listening-practice", "Listening exam practice", c_choice(la["questions"]))
        + f'\n<details><summary>Show the script (read it after you finish)</summary>{la["script_html"]}</details>'
        + f'\n<p>Next: do the graded listening quiz <strong>"Unit {n} Listening"</strong> in Tutor LMS.</p>')

    # 5 SPEAKING
    sp = u["speaking"]
    cards = [split(c) for c in sp["cards"]]
    P["5-speaking"] = page(f"Unit {n} · Speaking (exam practice)",
        SPEAKING_FORMAT + "\n<h2>Part 1: Interview cards</h2><p>Turn a card. Answer the question in 2–4 sentences. The back of the card gives ideas and useful language. Record yourself and listen.</p>"
        + h5p("cards", "speaking-cards", "Interview cards", c_cards([(c[0], c[1]) for c in cards], f"Interview cards: {u['topic']}"))
        + f"\n<h2>Part 2: Long turn</h2><p>{sp['part2']}</p>\n<h2>Part 3: Discussion</h2><ul>" + "".join(f"<li>{q}</li>" for q in sp["part3"]) + "</ul>")

    # 6 WRITING
    w = u["writing"]
    P["6-writing"] = page(f"Unit {n} · Writing: informal and formal emails",
        f"<p><strong>Goal:</strong> {w['goal']}</p>\n{WRITING_CORE}\n<h2>4. Unit {n} examples</h2>\n"
        f"<h3>Informal email</h3><p><em>Task: {w['informal_task']}</em></p><blockquote>{w['informal_sample']}</blockquote>\n"
        f"<h3>Formal email</h3><p><em>Task: {w['formal_task']}</em></p><blockquote>{w['formal_sample']}</blockquote>\n"
        f"<p><strong>Notice:</strong> {w['notice']}</p>\n<h2>Practice</h2>"
        "<h3>Task 1: Formal or informal? Choose the right phrase</h3>" + h5p("choice", "writing-register", "Writing: choose the right register", c_choice(w["register"]))
        + "<h3>Task 2: Mark the linking words</h3>" + h5p("mark", "writing-mark", "Writing: find the linking words", c_mark(w["mark_text"], "Click on all the linking words (words that join ideas)."))
        + "<h3>Task 3: Complete the email with linking words</h3>" + h5p("drag", "writing-drag", "Writing: complete the email", c_drag(w["drag"], "Drag the linking words and email phrases to the gaps."))
        + f"\n<h2>Your turn</h2><p>Write <strong>both</strong> emails (100–120 words each).</p><p><strong>Informal:</strong> {w['own_informal']}</p><p><strong>Formal:</strong> {w['own_formal']}</p>"
        "<p><strong>Checklist:</strong> ☐ greeting ☐ reason for writing ☐ paragraphs ☐ 3 linking words ☐ correct register ☐ unit grammar ☐ unit vocabulary ☐ sign-off</p>")

    for k, body in P.items(): write(os.path.join(out, f"lesson-{k}.html"), body)

    # TUTOR LMS quizzes
    rng = random.Random(n)
    quizzes = [
        {"title": f"Unit {n} Grammar and Vocabulary", "description": "Answer 10 questions. You get new questions every time.",
         "settings": {"time_limit_minutes": 15, "attempts_allowed": 0, "passing_grade_percent": 70, "question_order": "random",
                      "max_questions_allowed_to_answer": 10, "feedback_mode": "retry", "show_correct_answers": True},
         "questions": [tutor_q(i, rng) for i in u["pool"]]},
        {"title": f"Unit {n} Reading", "description": f"<h3>{u['reading_b']['title']}</h3>{u['reading_b']['text']}",
         "settings": {"time_limit_minutes": 20, "attempts_allowed": 3, "passing_grade_percent": 60, "question_order": "sorting", "max_questions_allowed_to_answer": len(u["reading_b"]["questions"])},
         "questions": [tutor_q(i, rng) for i in u["reading_b"]["questions"]]},
        {"title": f"Unit {n} Listening", "description": f"<h3>{u['listening_b']['title']}</h3><p>Listen to the audio file twice (b1-unit-{n:02d}-listening-quiz.mp3). Then answer the questions.</p>",
         "settings": {"time_limit_minutes": 20, "attempts_allowed": 3, "passing_grade_percent": 60, "question_order": "sorting", "max_questions_allowed_to_answer": len(u["listening_b"]["questions"])},
         "questions": [tutor_q(i, rng) for i in u["listening_b"]["questions"]]},
    ]
    for q in quizzes:
        slug = q["title"].lower().replace(" ", "-")
        write(os.path.join(out, "tutor-lms", f"{slug}.json"), json.dumps(q, indent=1, ensure_ascii=False))
        with open(os.path.join(out, "tutor-lms", f"{slug}.csv"), "w", newline="", encoding="utf-8") as f:
            cw = csv.writer(f); cw.writerow(["quiz", "type", "question", "option_a", "option_b", "option_c", "correct_option"])
            for it in q["questions"]:
                o = it["options"] + [""] * (3 - len(it["options"]))
                cw.writerow([q["title"], "single_choice", it["question"], *o[:3], "ABC"[it["options"].index(it["correct"])]])

    # LISTENING SCRIPTS (to record) + SPEAKING CARDS (print)
    write(os.path.join(out, "listening", "scripts-to-record.md"),
          f"# Unit {n} listening scripts (record these; two speakers = two voices)\n\n"
          f"## Practice recording → b1-unit-{n:02d}-listening-practice.mp3\n\n{la['script_md']}\n\n"
          f"## Graded quiz recording → b1-unit-{n:02d}-listening-quiz.mp3\n\n{u['listening_b']['script_md']}\n")
    write(os.path.join(out, "speaking", "interview-cards-print.md"),
          f"# Unit {n} interview cards – {u['topic']}\n\n" + "\n".join(f"**Card {i+1}.** {c[0]}\n\n_Ideas:_ {c[1]}\n" for i, c in enumerate(cards)))

    # INDEX
    idx = [f"# Unit {n}: {u['title']}\n", f"Topic: {u['topic']} · Grammar: {g['title']}\n",
           "## WordPress build order\n", "1. Upload each file from `dist/h5p/` in **H5P Content → Add New → Upload**. Note each new ID.\n",
           "2. Create 6 pages from `lesson-*.html` (Custom HTML block). Replace every `[h5p id=\"uNN-name\"]` with the real shortcode `[h5p id=\"123\"]`.\n",
           "3. Record the audio from `listening/scripts-to-record.md`, upload to the Media Library.\n",
           "4. In Tutor LMS create 3 quizzes from `tutor-lms/` (see the root README for settings).\n",
           "\n## H5P activities\n", "| File | Type | Items |\n|---|---|---|\n"] + [f"| {r['name']}.h5p | {r['type']} | {r['items']} |\n" for r in reg]
    write(os.path.join(out, "INDEX.md"), "".join(idx))
    bad = [r for r in reg if r["items"] < 8]
    print(f"unit {n}: {len(reg)} H5P files, pool={len(u['pool'])}", "UNDER-8: " + str(bad) if bad else "")
    for r in reg:
        if r["type"] != "H5P.Dialogcards" or "speaking" in r["name"] or "flash" in r["name"]: pass

if __name__ == "__main__":
    ns = [int(a) for a in sys.argv[1:]] or [int(f[1:3]) for f in sorted(os.listdir(os.path.join(ROOT, "tools", "units"))) if f.startswith("u") and f.endswith(".py")]
    for n in ns: build_unit(n)
