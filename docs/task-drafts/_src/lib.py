"""Helpers that write a task CSV in the format of the Tasks tab (app/src/CustomItems.php)."""
import csv, os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "app", "authoring"))
import italics
# Latvian words without Latvian letters that the built-in list does not have yet. Kept here, not in italics.py, so the published explanations are untouched.
italics.LV_ASCII |= set('''apgriez divi filma gariem grupai ieradumam nesens notikums noliegts noteikums nulles otrais pirmais tagadnes vienas zilbes abus aizliegts atbildes
beidzas beidzies cita darba divdabi divdabis esam garums grupa ieradums izteikt jebkuru laba ideja lielu lietas likums maigs mana istaba ne nekas nelielu padomu paliek saraksta
laikiem stingri tagadne tagadnei tam tava tur zilbe celtnieks viedoklis lielāks mazāks dod rezultatu jauns vecs vecaks gads gadu pasaule pilsetas pilseta cena cenas darbs darbi'''.split())
HEAD = ["topic", "level", "type", "task", "correct answer", "wrong options / checks", "explanation shown to learner", "explanation in Latvian", "thinking level"]
rows = []

# Latvian wording follows docs/LATVIAN-TERMS.md: English tense names are kept, "3. forma" for the participle, "ciešamā kārta", "teikuma priekšmets".
LV_SUBS = [
    (r"[Pp]asīva darbības vārdi", "ciešamās kārtas darbības vārdi"), (r"Pasīvs pagātnē:", "Ciešamā kārta, Past Simple:"), (r"Pasīvs nākotnē:", "Ciešamā kārta, Future:"), (r"Pasīvs procesā:", "Ciešamā kārta, Present Continuous:"),
    (r"Pasīva jautājums:", "Jautājums ciešamajā kārtā:"), (r"Pasīvs, ", "Ciešamā kārta, "), (r"Pasīvs:", "Ciešamā kārta:"), (r"pasīvs\b", "ciešamā kārta"), (r"Pasīvs\b", "Ciešamā kārta"),
    (r"[Vv]ienkāršo tagadni|[Vv]ienkāršā tagadne", "Present Simple"), (r"[Vv]ienkāršo pagātni|[Vv]ienkāršā pagātne", "Past Simple"),
    (r"[Tt]agadnes ilgstošā forma|[Tt]agadnes ilgstošo formu|[Tt]agadnes ilgstošā", "Present Continuous"), (r"[Pp]agātnes ilgstošā forma|[Pp]agātnes ilgstošo formu", "Past Continuous"),
    (r"[Ii]lgstošā forma", "Continuous forma"), (r"[Ss]alīdzināmā forma", "pārākā pakāpe"), (r"[Ss]alīdzināmo formu", "pārāko pakāpi"),
    (r"pagātnes divdabi\b", "3. formu"), (r"pagātnes divdabis\b", "3. forma"), (r"[Dd]ivdabi\b", "3. formu"), (r"[Dd]ivdabis\b", "3. forma"),
    (r"(?<!teikuma )(?<!teik\. )\b[Pp]riekšmets\b", "teik. priekšmets"), (r"(?<!teikuma )(?<!teik\. )\bpriekšmeta\b", "teikuma priekšmeta"), (r"(?<!teikuma )(?<!teik\. )\bpriekšmetu\b", "teikuma priekšmetu"),
]
def lv_fix(t):
    t = t.replace("*", "")
    for a, b in LV_SUBS: t = re.sub(a, b, t)
    return italics.lv_mark(t)   # every English word in a Latvian explanation is an example: the same rule the built-in explanations use
def mc(t, lv, b, q, ok, wrong, why, lvw): rows.append([t, lv, "mcq", q, ok, " | ".join(wrong), why, lvw, b])
def gp(t, lv, b, q, ok, why, lvw, bank=None): rows.append([t, lv, "gap", q, ok, ("bank: " + " | ".join(bank)) if bank else "", why, lvw, b])
def tx(t, lv, b, q, ok, why, lvw): rows.append([t, lv, "text", q, " | ".join(ok) if isinstance(ok, (list, tuple)) else ok, "", why, lvw, b])
def od(t, lv, b, q, ok, why, lvw, also=None): rows.append([t, lv, "order", q, ok, ("also accepted: " + " | ".join(also)) if also else "", why, lvw, b])
def mt(t, lv, b, q, pairs, why, lvw): rows.append([t, lv, "match", q, " ; ".join(f"{a} = {c}" for a, c in pairs), "", why, lvw, b])
def save(name):
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", name)
    with open(out, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f); w.writerow(HEAD)
        for r in rows: w.writerow(r[:7] + [lv_fix(r[7])] + r[8:])
    print(name, len(rows), "rows")


# ───────── compact builders for the big batches ─────────
LVMAP = {
    "*We* goes with *were*, not *was*.": "*We* lieto ar *were*, nevis *was*.",
    "*Wasn't listening* = she was not in the middle of listening.": "*Wasn't listening* = viņa tobrīd neklausījās.",
    "With *last week* (a finished time) we use the past simple.": "Ar *last week* (pabeigts laiks) lieto Past Simple.",
    "We can see it now, so we use *going to*.": "Mēs to redzam tagad, tāpēc lieto *going to*.",
    "After *will* we use the base verb, without *to*.": "Pēc *will* lieto pamatformu bez *to*.",
    "*Bread* is uncountable: *is baked*.": "*Bread* ir neskaitāms: *is baked*.",
    "After *was* we need the 3. form: *destroyed*.": "Pēc *was* vajag 3. formu: *destroyed*.",
    "No *will* after *if* in a general truth.": "Vispārīgā patiesībā pēc *if* nav *will*.",
    "No *will* after *if*.": "Pēc *if* nav *will*.",
    "*Manager* is *he / she*, so *doesn't*.": "*Manager* ir *he / she*, tāpēc *doesn't*.",
    "After *doesn't* the verb has no *-s*.": "Pēc *doesn't* darbības vārdam nav *-s*.",
    "*Understand* is a state verb: *I don't understand*.": "*Understand* ir stāvokļa darbības vārds: *I don't understand*.",
    "*Know* is a state verb: *we know*.": "*Know* ir stāvokļa darbības vārds: *we know*.",
    "After *is* the verb needs *-ing*: *is having*.": "Pēc *is* darbības vārdam vajag *-ing*: *is having*.",
    "After *did* the verb is in the base form: *go*.": "Pēc *did* darbības vārds ir pamatformā: *go*.",
    "After *didn't* we use *use to*, not *used to*.": "Pēc *didn't* lieto *use to*, nevis *used to*.",
    "The Past Continuous action was already in progress when the call came.": "Past Continuous darbība jau norisinājās, kad zvans pienāca.",
    "*They* goes with *were*.": "*They* lieto ar *were*.",
    "A finished time (*last weekend*) needs the Past Simple.": "Pabeigts laiks (*last weekend*) prasa Past Simple.",
    "Use *for* with a length of time, *since* with a starting point.": "*For* lieto ar laika ilgumu, *since* ar sākuma punktu.",
    "*Know* is a state verb: *I've known*.": "*Know* ir stāvokļa darbības vārds: *I've known*.",
    "After *been* the verb needs *-ing*.": "Pēc *been* darbības vārdam vajag *-ing*.",
    "The earlier event needs *had finished*.": "Agrākajam notikumam vajag *had finished*.",
    "*Never* already makes it negative: no *n't*.": "*Never* jau ir noliegums: bez *n't*.",
    "After *when* we use the Present Simple for the future.": "Pēc *when* nākotnei lieto Present Simple.",
    "*Breakfast* is singular: *is served*.": "*Breakfast* ir vienskaitlī: *is served*.",
    "*Machines* is plural: *are checked*.": "*Machines* ir daudzskaitlī: *are checked*.",
    "After *is* we need the 3. form: *visited*.": "Pēc *is* vajag 3. formu: *visited*.",
    "After *was* we need the 3. form: *robbed*.": "Pēc *was* vajag 3. formu: *robbed*.",
    "*Trees* is plural: *were damaged*.": "*Trees* ir daudzskaitlī: *were damaged*.",
    "After *being* we need the 3. form: *written*.": "Pēc *being* vajag 3. formu: *written*.",
    "*Rooms* is plural: *are being cleaned*.": "*Rooms* ir daudzskaitlī: *are being cleaned*.",
    "After *been* we need the 3. form: *signed*.": "Pēc *been* vajag 3. formu: *signed*.",
    "*People* is plural: *have been arrested*.": "*People* ir daudzskaitlī: *have been arrested*.",
    "After *will be* we need the 3. form: *introduced*.": "Pēc *will be* vajag 3. formu: *introduced*.",
    "We need *be*: *will be announced*.": "Vajag *be*: *will be announced*.",
    "*Will* is not used after *if* or *unless* here.": "Pēc *if* vai *unless* šeit nelieto *will*.",
    "After *if* we need the Present Simple, not *will*.": "Pēc *if* vajag Present Simple, nevis *will*.",
    "*Unless* already means *if not*: no second negative.": "*Unless* jau nozīmē *if not*: otra noliegumu nevajag.",
    "In the second conditional the *if* part uses the past: *knew*, not *would know*.": "Otrajā nosacījumā *if* daļā lieto pagātni: *knew*, nevis *would know*.",
    "The result part needs *would*: *she would buy it*.": "Rezultāta daļā vajag *would*: *she would buy it*.",
    "The third conditional uses *had* in the *if* part: *had studied*, not *would have studied*.": "Trešajā nosacījumā *if* daļā ir *had*: *had studied*, nevis *would have studied*.",
    "After *wouldn't have* we need the 3. form: *missed*.": "Pēc *wouldn't have* vajag 3. formu: *missed*.",
    "*Told* needs an object: *told me*; *said* does not.": "Aiz *told* vajag papildinātāju: *told me*; aiz *said* tā nav.",
    "With *will* in the report we need *would*: *would come*.": "Netiešajā runā *will* kļūst par *would*: *would come*.",
    "In a reported question the verb follows the subject: *where I lived*.": "Netiešajā jautājumā darbības vārds ir aiz teik. priekšmeta: *where I lived*.",
    "After *asked* the question has normal word order, without *did*.": "Pēc *asked* jautājumam ir parastā vārdu secība, bez *did*.",
    "In an indirect question the verb follows the subject: *where the platform is*.": "Netiešajā jautājumā darbības vārds ir aiz teik. priekšmeta: *where the platform is*.",
    "No *does* in an indirect question: *what time breakfast starts*.": "Netiešajā jautājumā nav *does*: *what time breakfast starts*.",
}

class Topic:
    """One topic with default explanations (English, Latvian) per question type. Item-specific explanations override them."""
    def __init__(self, name, mcq_b=2, text_b=4, match_b=2, **ex):
        self.t = name; self.ex = ex; self.seen = set(); self.mb = mcq_b; self.tb = text_b; self.xb = match_b
    def _why(self, kind, why):
        if isinstance(why, (tuple, list)): return why
        if why: return (why, LVMAP[why])   # an English-only explanation must have its Latvian twin in LVMAP
        return self.ex[kind]
    def _uniq(self, q, extra=""):
        key = (q, extra)
        if key in self.seen: raise SystemExit("duplicate in script: " + q)
        self.seen.add(key)
    def order(self, lv, sent, also=None, why=None, cue="Put the words in order.", b=3):
        self._uniq(cue, sent); w = self._why("order", why); od(self.t, lv, b, cue, sent, w[0], w[1], also)
    def bank(self, lv, q, ans, extra, why=None, b=3):
        self._uniq(q); w = self._why("bank", why); ans = [ans] if isinstance(ans, str) else ans
        assert len(set(ans + extra)) == len(ans + extra) and len(extra) >= 1, q
        gp(self.t, lv, b, q, " / ".join(ans), w[0], w[1], bank=ans + extra)
    def gap(self, lv, q, ans, why=None, b=3):
        self._uniq(q); w = self._why("gap", why); gp(self.t, lv, b, q, ans, w[0], w[1])
    def text(self, lv, q, ans, why=None, b=None):
        self._uniq(q); w = self._why("text", why); tx(self.t, lv, b or self.tb, q, ans, w[0], w[1])
    def mcq(self, lv, q, ok, wrong, why=None, b=None):
        self._uniq(q); w = self._why("mcq", why); mc(self.t, lv, b or self.mb, q, ok, wrong, w[0], w[1])
    def match(self, lv, q, pairs, why=None, b=None):
        self._uniq(q); w = self._why("match", why); mt(self.t, lv, b or self.xb, q, pairs, w[0], w[1])
