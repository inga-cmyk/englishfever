"""Batch 4, point wont_refuse (B1.2): won't for refusing (The door won't open. He won't listen.) and wouldn't for a
refusal in the past (The car wouldn't start). Murphy unit 21 (won't = refuse: The car won't start; she won't listen)
and unit 36 (wouldn't = refused: he wouldn't speak to me).
doesn't start / isn't starting / can't open / didn't start are correct English too (a fact, not a refusal): they are never
a wrong option. The wrong options are form mistakes (won't to, won't -ing, willn't, wouldn't + past) or won't with a fixed
past time (yesterday, last night). won't for the future (It won't rain) is not used: every sentence is a refusal."""
from lib import gp, od, mc, tx, mt, learning_task
T = "Future: will, going to, present continuous"
L = "B1.2"

FORM = ("*won't* + base verb, no *to* and no *-ing*: *It won't switch on.* = it refuses to work.",
        "*won't* + pamatforma: *It won't switch on.* = tas atsakās darboties. Nevis *won't to switch on* vai *won't switching on*.")
PAST = ("A refusal in the past: *wouldn't* + base verb (*The lock wouldn't open.*). With a past time such as *yesterday* or *last night*, not *won't*.",
        "Atteikšanās pagātnē: *wouldn't* + pamatforma (*The lock wouldn't open.*). Ar pagātnes laiku (*yesterday*, *last night*) nelieto *won't*.")
PERSON = ("*won't* is the same for every person, and the verb after it has no *-s*: *He won't listen.*",
          "*won't* visām personām ir vienāds, un darbības vārdam aiz tā nav -s: *He won't listen.*")
QUEST = ("In a question, *won't* goes before the subject: *Why won't she answer?* (not *Why she won't answer?*).",
         "Jautājumā *won't* liek pirms teikuma priekšmeta: *Why won't she answer?* (nevis *Why she won't answer?*).")

# ---------- choice (7) ----------
mc(T, L, 2, "Choose the correct option: I've charged it all night, but my phone still ___.", "won't switch on",
   ["won't to switch on", "won't switching on", "willn't switch on"],
   "*won't* + base verb = it refuses to work: *My phone won't switch on.* No *to*, no *-ing*; the short form of *will not* is *won't*.",
   "Tulkojot burtiski *negrib ieslēgties*, sanāk *doesn't want to switch on*. Par lietu, kas atsakās darboties, angliski saka *won't* + pamatforma: *My phone won't switch on.* Nevis *won't to switch on* vai *won't switching on*.")
mc(T, L, 2, "Choose the correct option: Yesterday I was late for work because my bike lock ___.", "wouldn't open",
   ["wouldn't opened", "wouldn't to open", "won't open"], *PAST)
mc(T, L, 2, "Choose the correct option: I've told Max it's dangerous, but he ___ to me.", "won't listen",
   ["won't listens", "won't to listen", "willn't listen"], *PERSON)
mc(T, L, 2, "Which sentence is correct?", "The key card wouldn't open my hotel room last night.",
   ["The key card wouldn't opened my hotel room last night.", "The key card won't open my hotel room last night.",
    "The key card wouldn't to open my hotel room last night."], *PAST)
mc(T, L, 2, "Which sentence is NOT correct?", "My sister won't to lend me her car.",
   ["This window won't close properly.", "The engine didn't start at first.", "The taxi driver wouldn't take my card."],
   "After *won't* comes the base verb, without *to*: *My sister won't lend me her car.* The others are correct; *didn't start* is a correct way to tell what happened, too.",
   "Aiz *won't* lieto pamatformu: *My sister won't lend me her car*, nevis *won't to lend*. Pārējie teikumi ir pareizi; arī *didn't start* ir pareizs veids, kā pastāstīt, kas notika.")
mc(T, L, 2, "Which sentence is NOT correct?", "My landlord wouldn't fixed the heating.",
   ["The printer won't print in colour.", "Our cat won't eat dry food.", "He wouldn't tell me his name."],
   "After *wouldn't* comes the base verb, not the past: *My landlord wouldn't fix the heating.* The others are correct.",
   "Aiz *wouldn't* lieto pamatformu, nevis pagātnes formu: *My landlord wouldn't fix the heating.* Pārējie teikumi ir pareizi.")
mc(T, L, 2, "Choose the correct option: Why ___ inside? It's freezing out there.", "won't the dog come",
   ["the dog won't come", "won't the dog to come", "won't the dog comes"],
   "In a question, *won't* goes before the subject and the verb stays in the base form: *Why won't the dog come inside?*",
   "Jautājumā *won't* liek pirms teikuma priekšmeta, un darbības vārds paliek pamatformā: *Why won't the dog come inside?*")

# ---------- typed gap (5) ----------
gp(T, L, 3, "Write *won't* or *wouldn't*: I tried to send you the photos last night, but the wifi ___ work.", "wouldn't",
   "*last night* is past, so the refusal is *wouldn't*: *the wifi wouldn't work.*",
   "*last night* ir pagātne, tāpēc atteikšanās ir *wouldn't*: *the wifi wouldn't work.*")
gp(T, L, 3, "Write *won't* or *wouldn't*: Can you help me with this suitcase? The zip ___ close.", "won't",
   "The problem is now (*Can you help me?*), so *won't*: *The zip won't close.* = it refuses to close.",
   "Problēma ir tagad (*Can you help me?*), tāpēc *won't*: *The zip won't close.* = rāvējslēdzējs nekādi neaizveras.")
gp(T, L, 3, "Write *won't* or *wouldn't*: The cash machine ___ give me any money yesterday, so I borrowed some from Ana.", "wouldn't",
   "*yesterday* is past, so *wouldn't*: *The cash machine wouldn't give me any money.*",
   "*yesterday* ir pagātne, tāpēc *wouldn't*: *The cash machine wouldn't give me any money.*")
gp(T, L, 3, "My sister was upset and wouldn't ___ to anyone at the party. (speak)", "speak",
   "After *wouldn't* comes the base verb, also in a story about the past: *wouldn't speak*, not *wouldn't spoke*.",
   "Aiz *wouldn't* lieto pamatformu, arī stāstot par pagātni: *wouldn't speak*, nevis *wouldn't spoke*.")
gp(T, L, 3, "My son won't ___ his homework, however often I ask him. (do)", "do",
   "After *won't* the verb has no *-s*, also after *he*: *He won't do his homework.*",
   "Aiz *won't* darbības vārdam nav -s, arī aiz *he*: *He won't do his homework.*")

# ---------- whole sentence (3) ----------
tx(T, L, 4, "Say it another way with *won't*: My computer refuses to open this file.",
   "My computer won't open this file. | My computer won't open the file. | This file won't open on my computer.",
   "*refuses to open* = *won't open*: *won't* + base verb, no *to*.",
   "*refuses to open* = *won't open*: *won't* + pamatforma, nevis *won't to open*.")
tx(T, L, 4, "Say it another way with *wouldn't*: My neighbour refused to move his car last night.",
   "My neighbour wouldn't move his car last night. | My neighbor wouldn't move his car last night.",
   "*refused to move* = *wouldn't move*: a refusal in the past is *wouldn't* + base verb.",
   "*refused to move* = *wouldn't move*: atteikšanās pagātnē ir *wouldn't* + pamatforma.")
tx(T, L, 4, "Make a question with *Why*: The baby won't eat her soup.",
   "Why won't the baby eat her soup? | Why will the baby not eat her soup? | Why won't she eat her soup? | Why won't the baby eat? | Why won't she eat?",
   *QUEST)

# ---------- word order (5) ----------
od(T, L, 3, "Put the words in order.", "my dad won't wear his glasses even when he's driving", *PERSON,
   also=["even when he's driving my dad won't wear his glasses", "my dad won't even wear his glasses when he's driving"])
od(T, L, 3, "Put the words in order.", "my car wouldn't start this morning so i worked from home", *PAST,
   also=["this morning my car wouldn't start so i worked from home", "my car wouldn't start so i worked from home this morning"])
od(T, L, 3, "Put the words in order to make a question.", "why won't you tell me what happened at work", *QUEST)
od(T, L, 3, "Put the words in order.", "my friend wouldn't let me pay for dinner last night", *PAST,
   also=["last night my friend wouldn't let me pay for dinner"])
od(T, L, 3, "Put the words in order.", "i've tried two keys but this door still won't open", *FORM)

# ---------- word bank (4) ----------
gp(T, L, 3, "Yesterday the hotel lift ___ ___, so we took the stairs.", "wouldn't / move", *PAST,
   bank=["wouldn't", "won't", "move", "moved"])
gp(T, L, 3, "My grandmother is very independent and ___ ___ anyone help her.", "won't / let", *PERSON,
   bank=["won't", "let", "lets", "letting"])
gp(T, L, 3, "Why ___ ___ ___ me? I've called her five times today.", "won't / she / answer", *QUEST,
   bank=["won't", "she", "answer", "answers"])
gp(T, L, 3, "Yesterday the shop assistant ___ ___ me a refund, so I complained.", "wouldn't / give", *PAST,
   bank=["wouldn't", "won't", "give", "gave"])

# ---------- matching (1, learning) ----------
mt(T, L, 2, "Match each beginning with its ending.",
   [("My laptop won't", "switch on."), ("Why won't", "the tap stop dripping?"),
    ("Last night the baby wouldn't", "stop crying."), ("I asked twice, but she", "wouldn't tell me.")],
   "*won't / wouldn't* + base verb (*won't switch on*, *wouldn't stop*); in a question *won't* comes before the subject (*Why won't the tap stop dripping?*); after a subject we need *won't* or *wouldn't* before the verb (*she wouldn't tell me*).",
   "*won't / wouldn't* + pamatforma (*won't switch on*, *wouldn't stop*); jautājumā *won't* liek pirms teikuma priekšmeta (*Why won't the tap stop dripping?*); aiz teikuma priekšmeta pirms darbības vārda vajag *won't* vai *wouldn't* (*she wouldn't tell me*).")
