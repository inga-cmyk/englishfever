"""Choice tasks for form pairs that had almost none (docs/NEXT-STEPS-BRIEF.md, part C, batch 2; docs/GRAMMAR-MAP-GAPS.md 4.2):
must be / can't be, during / while, by / until, could / was able to, although / despite, because / because of. Both forms are
correct English elsewhere, so the sentence decides (part A test: the situation is needed). DRAFT in pending/ until the teacher has
read it. would rather + verb / would rather you + past waits for batch 3 (decision 3: would rather is B1.2).
Grammar checked against Murphy 28 (must, can't), 27 (could, was able to), 113 (although, in spite of), 119 (during, for, while),
120 (by, until)."""
from lib import rows, save, mc

MOD = "More modals: might, could, be able to"
TIME = "Time clauses (when, as soon as, until)"
CON = "Contrast, purpose and reason (although, despite, so that)"
LINK = "However, although, because of, then"
Q = "Choose the correct option: "

DED = ("*must* = I am sure it is true; *can't* = I am sure it is not true. Not *mustn't*: it means that something is not allowed.",
       "*must* = noteikti tā ir; *can't* = noteikti tā nav. Ne *mustn't*: tas nozīmē, ka kaut ko nedrīkst.")
for ctx, ok, wrong in [
    ("The lights are off and nobody answers the door. They ___ be at home.", "can't", ["must", "mustn't"]),
    ("She's been running for an hour in this heat. She ___ be thirsty.", "must", ["can't", "mustn't"]),
    ("That ___ be Tom's car. He sold it last month.", "can't", ["must", "mustn't"]),
    ("Everyone outside is wearing a coat and a hat. It ___ be very cold today.", "must", ["can't", "mustn't"]),
    ("This ___ be the right address. There's no number 52 on this street.", "can't", ["must", "mustn't"]),
    ("Mark works at two jobs and has three small children. He ___ be bored at home.", "can't", ["must", "mustn't"]),
]:
    mc(MOD, "B1.2", 2, Q + ctx, ok, wrong, *DED)

DUR = ("*during* + a noun (*during the meeting*); *while* + a subject and a verb (*while I was looking*); *for* + how long (*for three years*).",
       "*during* + lietvārds (*during the meeting*); *while* + teikuma priekšmets un darbības vārds (*while I was looking*); *for* + cik ilgi (*for three years*).")
for ctx, ok, wrong in [
    ("My phone rang ___ the meeting, and everyone looked at me.", "during", ["while", "for"]),
    ("Someone stole my bag ___ I was looking at the menu.", "while", ["during", "for"]),
    ("We lived in Spain ___ three years before we moved to Riga.", "for", ["during", "while"]),
    ("I fell asleep ___ the film, so I don't know how it ends.", "during", ["while", "for"]),
    ("___ we were waiting for the train, it started to snow.", "While", ["During", "For"]),
    ("I made a lot of good friends ___ my time at university.", "during", ["while", "for"]),
]:
    mc(TIME, "B1.1", 2, Q + ctx, ok, wrong, *DUR)

BY = ("*by* = not later than that time (a deadline); *until* = up to that time (something goes on). *since* + the start of a time up to now (*since 2019*). *By the time* + past: something had already happened.",
      "*by* = ne vēlāk kā (termiņš); *until* = līdz tam laikam (kaut kas turpinās). *since* + sākuma brīdis līdz tagadnei (*since 2019*). *By the time* + pagātne: kaut kas jau bija noticis.")
for ctx, ok, wrong in [
    ("Please pay the bill ___ Friday.", "by", ["until", "since"]),
    ("The shop is open ___ ten tonight, so we still have time.", "until", ["by", "since"]),
    ("I'll wait for you here ___ six. Then I'm going home.", "until", ["by", "since"]),
    ("Guests must leave their rooms ___ eleven o'clock on the last day.", "by", ["until", "since"]),
    ("We have lived in this flat ___ 2019, and we still like it.", "since", ["by", "until"]),
    ("___ the time we reached the airport, our plane had already left.", "By", ["Until", "Since"]),
]:
    mc(TIME, "B1.1", 2, Q + ctx, ok, wrong, *BY)

ABLE = ("One success in the past: *was / were able to* or *managed to*, not *could*. *could* is for a general ability: *I could swim when I was five.*",
        "Vienreiz izdevās konkrētā situācijā pagātnē: *was / were able to* vai *managed to*, nevis *could*. *could* ir vispārīga spēja: *I could swim when I was five.*")
for ctx, ok, wrong in [
    ("The fire was big, but everyone ___ get out of the building.", "was able to", ["could", "was able"]),
    ("The main road was closed, but we ___ find another way home.", "were able to", ["could", "were able"]),
    ("In the end she ___ pass the exam, although it was very hard.", "managed to", ["could", "managed"]),
    ("Our flight was cancelled, but luckily we ___ get seats on the next one.", "were able to", ["could", "could to"]),
    ("The sofa was very heavy, but the two of us ___ carry it upstairs.", "managed to", ["could", "could to"]),
    ("My grandfather ___ speak four languages when he was young.", "could", ["managed to", "can"]),
]:
    mc(MOD, "B1.1", 2, Q + ctx, ok, wrong, *ABLE)

ALT = ("*although* + a subject and a verb (*although she studied*); *despite* + a noun or *-ing* (*despite the weather, despite having a cold*); *However,* starts a new sentence.",
       "*although* + teikuma priekšmets un darbības vārds (*although she studied*); *despite* + lietvārds vai *-ing* (*despite the weather, despite having a cold*); *However,* sāk jaunu teikumu.")
for ctx, ok, wrong in [
    ("___ the long journey, the children were not tired at all.", "Despite", ["Although", "However"]),
    ("___ she studied hard, she didn't pass the driving test.", "Although", ["Despite", "However"]),
    ("We had a great holiday ___ the bad weather.", "despite", ["although", "however"]),
    ("He still goes to work by bike ___ he is seventy.", "although", ["despite", "however"]),
    ("___ having a cold, Anna sang at the concert.", "Despite", ["Although", "However"]),
    ("The flat is quite small. ___, it is very close to the centre.", "However", ["Although", "Despite"]),
]:
    mc(CON, "B1.1", 2, Q + ctx, ok, wrong, *ALT)

BEC = ("*because* + a subject and a verb (*because it was raining*); *because of* + a noun (*because of the wind*); *so* gives the result (*It was closed, so we left*).",
       "*because* + teikuma priekšmets un darbības vārds (*because it was raining*); *because of* + lietvārds (*because of the wind*); *so* norāda uz sekām (*It was closed, so we left*).")
for ctx, ok, wrong in [
    ("The trains stopped ___ the strong wind.", "because of", ["because", "so"]),
    ("We took a taxi ___ it was raining very hard.", "because", ["because of", "so"]),
    ("The museum was closed, ___ we went to a café instead.", "so", ["because", "because of"]),
    ("I couldn't sleep ___ the noise from the street.", "because of", ["because", "so"]),
    ("He was late for work ___ he overslept.", "because", ["because of", "so"]),
    ("The concert was cancelled ___ the singer was ill.", "because", ["because of", "so"]),
]:
    mc(LINK, "B1.1", 2, Q + ctx, ok, wrong, *BEC)

save("pending/pairs-1.csv")
