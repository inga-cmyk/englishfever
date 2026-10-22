"""Italics for the examples in explanation texts.

An example is written *like this* in the data (the app shows it in italics). English texts are marked by hand
(italics_en.py); Latvian texts are marked here by rule, because every English word in a Latvian explanation is an example:

    Pēc does lieto pamatformu: start, nevis starts.   ->   Pēc *does* lieto pamatformu: *start*, nevis *starts*.

Names of tenses and conditionals (Present Simple, Second conditional ...) are terms, not examples, and stay plain.
italics_lv_fixes.py holds hand-corrected lines for the few texts where the rule is not enough.
"""
import re

ENTITY = re.compile(r"[*']")


def norm(s):
    """What must be identical between a text and its marked version: everything except the * marks and apostrophes/quotes."""
    return ENTITY.sub("", s)


def strip(s):
    return s.replace("*", "")


def index(*blocks):
    """norm(text) -> marked text, for hand-marked lines (one per line)."""
    out = {}
    for block in blocks:
        for line in block.strip().splitlines():
            line = line.strip()
            if line:
                out[norm(line)] = line
    return out


# ───────────────────────── Latvian ─────────────────────────
# Words without Latvian letters that are nevertheless Latvian. Every other word without Latvian letters is English.
LV_ASCII = set("""abi aiz ap apraksta ar atbild atbilde atbildi bez bija burtu cik cits daba dara darbs datiem daudzskaitlis daudzums
der dienu divas divus dubulto es failiem fakti faktiem fakts fona fons forma formas formu galotne gan grafika grafiki grafikiem
gribi iemesls ieradumi ieradumiem ieradumu iet ikdienas ilgi ilgums ir izskaidro izskaidrotu ja jau jo ka kad kas katru kaut
klientiem ko komatu kritika lai laika laiks laiku liec liek lieto lietot lika maz nav nebeigts nekad nelieto nenosauc nenotika
nepievieno nesena nesenu netika nevis nodomu noliegumos noliegums noliegumu nomaini norit norunas norunu noteikumam noteikumi
noteikumiem notiek notika notiks notikuma notikumi objekts otru pabeigta pabeigtas pabeigts pabeigtu padomam padoms pagaidu
pamatforma pamatformu parasta parasti parasto pat pati patiesi patiess patskani pavisam persona personas personu pateikt pateiktu
pieredze pieredzei pievieno pirms posms posmu procesi prognozes punktu radies raksta redzam redzamu runa saikne saka saki sapulce
sapulcei saraksti sarakstiem savieno savu seko sevi skaitu skan soli starp tad tagad tagadni tas teica teik teikuma teikumi teikums
teikumu teikumus tendence ticamas ticamo tiem tik tuvai un uz uzraksti uzreiz vai vairs vajag vakar var veido viena vienlaikus
vienskaitlis vienu virkne virknei jons bet velta toma par no pie man trim logs""".split())

# Words that are English in one place and Latvian in another ("to + pamatforma" / "lieto to"): English only next to English.
AMBIGUOUS = {"to"}

# Names of grammar, not examples
TERMS = re.compile(
    r"\b(?:(?:Present|Past|Future) (?:Perfect Continuous|Perfect Simple|Perfect|Continuous|Simple)|(?:Zero|First|Second|Third|Mixed|Advanced) conditionals?"
    r"|past participle|to-infinitive|Continuous|Simple|Perfect)\b|\b(?:Zero|First|Second|Third)(?=:)")

WORD = re.compile(r"-?[A-Za-zĀČĒĢĪĶĻŅŠŪŽāčēģīķļņšūž]+(?:'[A-Za-z]+)?|\d+(?:[.:]\d+)?|\x00\d+\x00")
DIACRITIC = re.compile(r"[ĀČĒĢĪĶĻŅŠŪŽāčēģīķļņšūž]")
GAP_OK = re.compile(r"^[\s/,+=→\-–.?!;\"]*$")   # no quote mark, colon or bracket: each ends an example


def lv_mark(text):
    held = []

    def hold(m):
        held.append(m.group(0))
        return "\x00%d\x00" % (len(held) - 1)

    s = TERMS.sub(hold, text)
    toks = [(m.group(0), m.start(), m.end()) for m in WORD.finditer(s)]
    kind = []
    for w, a, b in toks:
        lw = w.lower()
        if w.startswith("\x00"):
            kind.append("T")
        elif re.match(r"\d", w):
            kind.append("N")
        elif w.startswith("-"):
            kind.append("E")
        elif DIACRITIC.search(w) or lw in LV_ASCII:
            kind.append("L")
        elif lw in AMBIGUOUS:
            kind.append("?")
        else:
            kind.append("E")
    # ambiguous words are English next to an English word, otherwise Latvian
    for i, k in enumerate(kind):
        if k == "?":
            near = [kind[j] for j in (i - 1, i + 1) if 0 <= j < len(kind)]
            kind[i] = "E" if "E" in near else "L"

    def gap_ok(i, j):
        gap = s[toks[i][2]:toks[j][1]]
        return GAP_OK.match(gap) is not None and not re.search(r"[.?!]\s", gap)   # a sentence end ends the example

    runs = []
    i = 0
    while i < len(toks):
        if kind[i] != "E":
            i += 1
            continue
        j = i
        while j + 1 < len(toks):
            nxt = kind[j + 1]
            if nxt == "E" and gap_ok(j, j + 1):
                j += 1
            elif nxt == "N" and s[toks[j][2]:toks[j + 1][1]] == " " and not (
                    s[toks[j + 1][2]:toks[j + 1][2] + 1] == "." and j + 2 < len(toks) and kind[j + 2] == "L"):
                j += 1   # a number right after English words belongs to the example: "at 7.45", "in 2019"
            else:
                break
        runs.append([toks[i][1], toks[j][2], j - i + 1, toks[i][0][0].isupper()])
        i = j + 1

    out = []
    pos = 0
    for a, b, n, upper in runs:
        # a whole English sentence keeps its end mark inside the italics
        if n >= 2 and upper and b < len(s) and s[b] in ".?!" and (b + 1 == len(s) or s[b + 1] in " '"):
            b += 1
        # 'quoted' examples lose the quote marks the italics replace
        qa = a > 0 and s[a - 1] == "'"
        qb = b < len(s) and s[b] == "'"
        if qa and qb:
            out.append(s[pos:a - 1] + "*" + s[a:b] + "*")
            pos = b + 1
        else:
            out.append(s[pos:a] + "*" + s[a:b] + "*")
            pos = b
    out.append(s[pos:])
    r = "".join(out)
    return re.sub(r"\x00(\d+)\x00", lambda m: held[int(m.group(1))], r)
