#!/usr/bin/env python3
"""Make all listening MP3s with ElevenLabs from courses/<level>/unit-NN/listening/scripts-to-record.md.

Run it on YOUR computer (the API key must not go into chat or into the repo):
    export ELEVENLABS_API_KEY=...            # Windows PowerShell:  $env:ELEVENLABS_API_KEY="..."
    python3 tools/make_audio.py --dry-run     # shows the plan (voices, characters), makes no API calls, uses no credits
    python3 tools/make_audio.py               # makes every missing file in dist/audio/
    python3 tools/make_audio.py --unit 3      # one unit;  --only practice|quiz;  --force to remake existing files

Each recording gets its own voices: the speakers of one recording share an accent (British or American,
alternating from recording to recording) and the pair of voices changes from recording to recording.
Voices come from your ElevenLabs account (GET /v1/voices, using the labels gender and accent), or from a
file given with --voices-file:  {"female":[{"id":"...","accent":"british"}], "male":[{"id":"...","accent":"american"}]}

Files are named as in the lessons: b1-unit-01-listening-practice.mp3 and b1-unit-01-listening-quiz.mp3.
Upload them to the Media Library (folder wp-content/uploads/english-fever/).
Pauses between lines need ffmpeg + `pip install pydub`; without them the lines are joined without pauses.
"""
import argparse, glob, io, json, os, re, sys, time, urllib.error, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
API = "https://api.elevenlabs.io/v1"
MODEL = "eleven_multilingual_v2"
SPEED = 0.92                       # slightly slower than natural speech, good for B1 learners
PAUSE_SAME, PAUSE_CHANGE = 350, 650   # milliseconds

FEMALE = {"anna", "lena", "eva", "ella", "ieva", "sofia", "woman", "receptionist"}
MALE = {"tom", "dan", "mark", "markus", "man"}
LINE = re.compile(r"^([A-Z][A-Za-z]*(?: [A-Z][A-Za-z]*)?):\s+(.*\S)\s*$")

def parse_script(text):
    """-> list of (speaker, line). Lines without 'Name:' continue the previous speaker (or 'Narrator')."""
    out, cur = [], "Narrator"
    for raw in text.splitlines():
        raw = raw.strip()
        if not raw: continue
        m = LINE.match(raw)
        if m: cur = m.group(1); raw = m.group(2)
        out.append((cur, raw))
    return out

def read_recordings(level, unit, only):
    items = []
    for path in sorted(glob.glob(os.path.join(ROOT, "courses", level, "unit-*", "listening", "scripts-to-record.md"))):
        n = int(re.search(r"unit-(\d+)", path).group(1))
        if unit and n != unit: continue
        text = open(path, encoding="utf-8").read()
        for part in re.split(r"\n## ", text)[1:]:
            head, body = part.split("\n", 1)
            m = re.search(r"→\s*(\S+\.mp3)", head)
            if not m: continue
            kind = "practice" if "practice" in m.group(1) else "quiz"
            if only and kind != only: continue
            items.append({"unit": n, "kind": kind, "file": m.group(1), "lines": parse_script(body), "chars": len(body.strip())})
    return items

def assign_genders(speakers):
    """Names/roles we know (Anna, Tom, Woman ...) keep their gender. Others (Doctor, Presenter ...) get the gender
    opposite to a neighbour, so two people talking never sound the same."""
    known = {s: "female" if s.lower() in FEMALE else "male" if s.lower() in MALE else None for s in speakers}
    g = {}
    for i, s in enumerate(speakers):
        if known[s]: g[s] = known[s]; continue
        prev = g.get(speakers[i - 1]) if i else None
        nxt = known.get(speakers[i + 1]) if i + 1 < len(speakers) else None
        ref = prev or nxt
        g[s] = "female" if ref is None else "male" if ref == "female" else "female"
    return g

def pick_voices(pool, idx, speakers):
    """Same accent for the whole recording, alternating British/American; rotate through the pool."""
    accent = ("british", "american")[idx % 2]
    genders = assign_genders(speakers)
    chosen, used = {}, set()
    for s in speakers:
        cands = [v for v in pool[genders[s]] if v["accent"] == accent and v["id"] not in used] \
             or [v for v in pool[genders[s]] if v["id"] not in used] or pool[genders[s]]
        v = cands[(idx // 2) % len(cands)]
        chosen[s] = v; used.add(v["id"])
    return accent, genders, chosen

# ---------- ElevenLabs ----------
def call(method, url, key, body=None, accept="application/json"):
    req = urllib.request.Request(url, method=method, data=json.dumps(body).encode() if body is not None else None,
                                 headers={"xi-api-key": key, "Content-Type": "application/json", "Accept": accept})
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=120) as r: return r.read()
        except urllib.error.HTTPError as e:
            msg = e.read().decode("utf-8", "replace")[:300]
            if e.code in (429, 500, 502, 503) and attempt < 4: time.sleep(2 ** (attempt + 1)); continue
            raise SystemExit(f"ElevenLabs error {e.code}: {msg}")
    raise SystemExit("ElevenLabs: too many retries")

def load_pool(args, key):
    if args.voices_file:
        data = json.load(open(args.voices_file, encoding="utf-8"))
        return {g: [{"id": v["id"], "name": v.get("name", v["id"]), "accent": v.get("accent", "").lower()} for v in data[g]] for g in ("female", "male")}
    if not key: raise SystemExit("Set ELEVENLABS_API_KEY, or give --voices-file (dry-run with fake voices needs the file).")
    pool = {"female": [], "male": []}
    for v in json.loads(call("GET", f"{API}/voices", key)).get("voices", []):
        lab = v.get("labels") or {}
        gender, accent = (lab.get("gender") or "").lower(), (lab.get("accent") or "").lower()
        accent = "british" if "brit" in accent else "american" if "amer" in accent else ""
        if gender in pool and accent: pool[gender].append({"id": v["voice_id"], "name": v.get("name", ""), "accent": accent})
    for g in pool:
        if not pool[g]: raise SystemExit(f"No {g} British/American voices found in your account. Add some voices or use --voices-file.")
    return pool

def tts(key, voice_id, text):
    body = {"text": text, "model_id": MODEL, "voice_settings": {"stability": 0.5, "similarity_boost": 0.75, "speed": SPEED}}
    return call("POST", f"{API}/text-to-speech/{voice_id}?output_format=mp3_44100_128", key, body, accept="audio/mpeg")

def join_audio(chunks):
    """chunks: list of (mp3_bytes, pause_before_ms). Uses pydub+ffmpeg for pauses; otherwise plain concatenation."""
    try:
        from pydub import AudioSegment
        out = AudioSegment.silent(duration=300)
        for data, pause in chunks:
            out += AudioSegment.silent(duration=pause) + AudioSegment.from_file(io.BytesIO(data), format="mp3")
        out += AudioSegment.silent(duration=500)
        buf = io.BytesIO(); out.export(buf, format="mp3", bitrate="128k"); return buf.getvalue(), True
    except Exception:
        return b"".join(d for d, _ in chunks), False

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--level", default=os.environ.get("EF_LEVEL", "B1").lower())
    ap.add_argument("--unit", type=int); ap.add_argument("--only", choices=["practice", "quiz"])
    ap.add_argument("--dry-run", action="store_true"); ap.add_argument("--force", action="store_true")
    ap.add_argument("--voices-file"); ap.add_argument("--out", default=os.path.join(ROOT, "dist", "audio"))
    args = ap.parse_args()
    key = os.environ.get("ELEVENLABS_API_KEY", "")
    recs = read_recordings(args.level, args.unit, args.only)
    if not recs: raise SystemExit("No scripts found. Run python3 tools/build.py first.")
    pool = load_pool(args, key)
    os.makedirs(args.out, exist_ok=True)
    todo = total = 0
    for idx, r in enumerate(recs):
        speakers = list(dict.fromkeys(s for s, _ in r["lines"]))
        accent, genders, voices = pick_voices(pool, idx, speakers)
        dest = os.path.join(args.out, r["file"])
        skip = os.path.exists(dest) and not args.force
        plan = ", ".join(f"{s} = {voices[s]['name']} ({genders[s]})" for s in speakers)
        print(f"{'skip (exists)' if skip else 'make        '} {r['file']}  [{accent}, {r['chars']} chars]  {plan}")
        if skip: continue
        todo += 1; total += r["chars"]
        if args.dry_run: continue
        chunks, prev = [], None
        for s, text in r["lines"]:
            chunks.append((tts(key, voices[s]["id"], text), 0 if prev is None else PAUSE_CHANGE if s != prev else PAUSE_SAME)); prev = s
        data, pauses = join_audio(chunks)
        open(dest, "wb").write(data)
        print(f"   saved {dest}" + ("" if pauses else "   (no pauses: install ffmpeg + pydub for pauses between lines)"))
    print(f"\n{todo} recording(s), about {total} characters" + (" (dry run: nothing was generated)" if args.dry_run else ""))

if __name__ == "__main__":
    main()
