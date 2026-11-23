"""C1 direction 10 (Advanced word order: inversion and fronting), round 1 (23 November 2026). Hewings, Advanced Grammar in Use
(3rd ed.), units 98-100, 85; Murphy, English Grammar in Use, appendix on inversion. Only places where one form is right."""
from lib import gp, mc, tx, note
T = "Advanced word order: inversion and fronting"
L = "C1"

gp(T, L, 4, "Write one word in each gap: Rarely ___ I ___ such a beautiful sunset. (have / see)", "have | had / seen",
   "After *Rarely* at the start, the helping verb comes before the subject: *Rarely have I seen…*",
   "Pēc *Rarely* teikuma sākumā palīgdarbības vārds stāv pirms teikuma priekšmeta: *Rarely have I seen…*")
note('had / seen :: Also possible, about a time in the past. :: Arī pareizi, ja runa ir par laiku pagātnē.')
mc(T, L, 4, "Which sentence has a mistake?", "Never I have felt so tired in my life.",
   ["Hardly had we sat down when the phone rang.", "No sooner had she arrived than it started to rain.",
    "Under no circumstances should you open this door."],
   "After *Never* at the start: helping verb + subject: *Never have I felt so tired.*",
   "Pēc *Never* teikuma sākumā: palīgdarbības vārds + teikuma priekšmets: *Never have I felt so tired.*")
gp(T, L, 4, "Write one word in each gap: Not until the guests had gone ___ we ___ the stain on the carpet. (notice)", "did / notice",
   "*Not until* + first clause, then inversion in the second (with *did* for the past simple): *did we notice*.",
   "*Not until* + pirmā daļa, tad inversija otrajā (Past Simple ar *did*): *did we notice*.")
tx(T, L, 4, "Start with *So loud*: The music was so loud that we couldn't hear each other.",
   "So loud was the music that we couldn't hear each other. | So loud was the music that we could not hear each other. | So loud was the music that we couldn't hear one another. | So loud was the music that we could not hear one another.",
   "*So* + adjective at the start, then *be* before the subject: *So loud was the music that…*",
   "*So* + īpašības vārds sākumā, tad *be* pirms teikuma priekšmeta: *So loud was the music that…*")
tx(T, L, 4, "Start with *Had*: If I had known about the traffic, I would have left earlier.",
   "Had I known about the traffic, I would have left earlier. | Had I known about the traffic, I'd have left earlier. | Had I known about the traffic, I would've left earlier.",
   "A condition without *if*: *Had* + subject + past participle: *Had I known…*",
   "Nosacījums bez *if*: *Had* + teikuma priekšmets + 3. forma: *Had I known…*")
tx(T, L, 4, "Start with *Should*: If you need any help, please call reception.",
   "Should you need any help, please call reception. | Should you need any help, call reception.",
   "A formal condition without *if*: *Should* + subject + base verb: *Should you need any help…*",
   "Oficiāls nosacījums bez *if*: *Should* + teikuma priekšmets + pamatforma: *Should you need any help…*")
gp(T, L, 4, "Just as we left the house, down ___ the rain. (come)", "came",
   "After an adverb of place at the start (*down, out, in*), the verb can come before a noun subject: *down came the rain*.",
   "Ja teikums sākas ar vietas apstākļa vārdu (*down, out, in*), darbības vārds var stāvēt pirms lietvārda: *down came the rain*.")
tx(T, L, 3, "Start with *What* and end with *a long holiday*: I need a long holiday.", "What I need is a long holiday. | What I really need is a long holiday. | What I need's a long holiday. | What I need is to have a long holiday.",
   "*What* + subject + verb + *is* puts the focus on the thing: *What I need is a long holiday.*",
   "*What* + teikuma priekšmets + darbības vārds + *is* izceļ lietu: *What I need is a long holiday.*")
gp(T, L, 4, "Cold ___ it was, we went for a swim in the lake.", "though | as",
   "Adjective + *though / as* + subject + verb = although it was cold: *Cold though it was, …*",
   "Īpašības vārds + *though / as* + teikuma priekšmets + darbības vārds = lai gan bija auksti: *Cold though it was, …*")

# ── added 23 November to reach 10 counted tasks ──
# x_inv_so
gp(T, L, 4, "Such ___ the noise from the party that nobody in the street could sleep.", "was",
   "*Such* + *be* + subject at the start: *Such was the noise that…* (= the noise was so great that…).",
   "*Such* + *be* + teikuma priekšmets sākumā: *Such was the noise that…* (= troksnis bija tik liels, ka…).")
# x_inv_main
gp(T, L, 4, "Write one word in each gap: Only when I got home ___ I ___ that my wallet was missing. (realise)", "did / realise | realize",
   "*Only when* + first clause, then inversion in the second (with *did*): *did I realise*.",
   "*Only when* + pirmā daļa, tad inversija otrajā (ar *did*): *did I realise*.")

# teacher's tester, 23 November: a cleft sentence with a clear focus, and Here + pronoun
tx(T, L, 4, "Put the focus on *the noise*. Start with *What*: The noise really annoys me.",
   "What really annoys me is the noise. | What annoys me is the noise.",
   "*What* + verb + *is* + the thing in focus at the end: *What really annoys me is the noise.*",
   "*What* + darbības vārds + *is* + izceltā lieta beigās: *What really annoys me is the noise.*")
mc(T, L, 3, "Choose the correct option: Look, there's our bus! Here ___!", "it comes",
   ["comes it", "does it come", "it is coming"],
   "After *Here*, a noun comes after the verb (*Here comes the bus*), but a pronoun comes before it: *Here it comes!*",
   "Pēc *Here* lietvārds stāv aiz darbības vārda (*Here comes the bus*), bet vietniekvārds pirms tā: *Here it comes!*")
