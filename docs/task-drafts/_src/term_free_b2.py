"""Batch 2 without grammar terms (draft, 6 November): the instruction that names a tense or "passive" goes; where the sentence
alone would allow another tense, a time word is added. Not applied until the teacher approves (term_free.BATCHES)."""
import re

PREFIX = [
    ("Use the past simple: ", ""),
    ("Use the present simple: ", ""),
    ("Use the past simple passive: ", ""),
    ("Use the present simple passive: ", ""),
    ("Use the present perfect: ", ""),
    ("Use the past simple or the past continuous: ", ""),
    ("Use the past continuous: ", ""),
    ("Use the past perfect: ", ""),
    ("Complete the passive form: ", "Write the missing word or words: "),
    ("Complete with the correct form of *have* or *get* + past participle: I'm going to have my eyes ___.", "Write the missing word: I'm going to have my eyes ___."),
    ("Complete with the correct form of *have* or *get* + past participle: He had his phone ___ on the bus.", "Write the missing word: He had his phone ___ on the bus."),
    ("Complete with the correct form of *have* or *get* + past participle: ", "Someone else does it for you. Write the missing word or words: "),
]
# after the instruction is gone: sentences that would allow another tense get a time word (old text without instruction -> new)
CONTEXT = {
    "We ___ a taxi to the station. (take)": "Yesterday we ___ a taxi to the station. (take)",
    "He ___ a letter to his friend. (write)": "Yesterday he ___ a letter to his friend. (write)",
    "It ___ cold, so we ___ inside. (be / stay)": "It ___ cold yesterday, so we ___ inside. (be / stay)",
    "How much money ___ you ___ at the shop? (spend)": "How much money ___ you ___ at the shop yesterday? (spend)",
    "She ___ her keys at home this morning. (leave)": "She ___ her keys at home yesterday morning. (leave)",
    "I ___ the blue shirt, not the red one. (choose)": "Yesterday I ___ the blue shirt, not the red one. (choose)",
    "She ___ the bus to work this morning. (take)": "She ___ the bus to work yesterday morning. (take)",
    "She ___ the door, ___ her coat and ___ out into the rain. (open / take / walk)": "Yesterday she ___ the door, ___ her coat and ___ out into the rain. (open / take / walk)",
    "Mia ___ to school by bus. (go)": "Mia ___ to school by bus every day. (go)",
    "He ___ his emails first thing in the morning, before he ___ a coffee. (check / make)": "He usually ___ his emails first thing in the morning, before he ___ a coffee. (check / make)",
    "My brother ___ his homework after dinner. (do)": "My brother always ___ his homework after dinner. (do)",
    "My brother ___ get up at five for work. (have to)": "My brother ___ get up at five every day for work. (have to)",
    "The match ___ because of rain. (cancel)": "Yesterday the match ___ because of rain. (cancel)",
    "The guests ___ at the door by the manager. (meet)": "Yesterday the guests ___ at the door by the manager. (meet)",
    "The film ___ in London. (shoot)": "The film ___ in London in 2019. (shoot)",
    "The books ___ by a famous writer. (write)": "The books ___ by a famous writer in the 1950s. (write)",
    "The prize ___ to a young artist. (give)": "Last year the prize ___ to a young artist. (give)",
    "Where ___ the photos ___ ? (take)": "Where ___ the photos ___ last summer? (take)",
    "Nobody ___ about the changes. (tell)": "Last week nobody ___ about the changes. (tell)",
    "The car ___ by a neighbour. (find)": "Yesterday the car ___ by a neighbour. (find)",
    "The suspects ___ at the airport, but the money ___ . (arrest / not find)": "Yesterday the suspects ___ at the airport, but the money ___ . (arrest / not find)",
    "Where ___ the cars ___ ? (build)": "Where ___ the cars ___ these days? (build)",
    "The rules ___ to all new members. (explain)": "Every year the rules ___ to all new members. (explain)",
    "They ___ a lot of photos this week. (take)": "They ___ a lot of photos so far this week. (take)",
    "At midnight they ___ . (sleep)": "At midnight last night they ___ . (sleep)",
    "What ___ she ___ at seven? (do)": "I called her at seven yesterday. What ___ she ___ then? (do)",
    "At 9 p.m. she ___ a film. (watch)": "At 9 p.m. yesterday she ___ a film, so she didn't hear the phone. (watch)",
}
# a second correct form, with its own note (new text -> (answer, English, Latvian))
NOTES = {
    "Start with *The new road*: They will open the new road next month.": ("The new road will open next month.", "Correct English too, but it means the road opens (the day it is ready). *Will be opened* says that someone will open it.", "Arī pareiza angļu valoda, bet tas nozīmē, ka ceļš atveras (diena, kad tas ir gatavs). *Will be opened* pasaka, ka kāds to atvērs."),
    "My sister ___ a red bike. (have)": ("has got", "Correct too: *has got* means the same as *has*.", "Arī pareizi: *has got* nozīmē to pašu, ko *has*."),
    "I ___ my phone. Can you help me look? (lose)": ("lost", "Correct too. *I lost my phone* only tells what happened; *have lost* also says that you still haven't got it.", "Arī pareizi. *I lost my phone* tikai pasaka, kas notika; *have lost* pasaka arī to, ka tālruņa joprojām nav."),
    "I ___ my passport, so I need a new one. (lose)": ("lost", "Correct too. *I lost my passport* only tells what happened; *have lost* also says that you still haven't got it now.", "Arī pareizi. *I lost my passport* tikai pasaka, kas notika; *have lost* pasaka arī to, ka pases joprojām nav."),
    "Sorry, I can't find the report. I think I ___ it on the train. (leave)": ("left", "Correct too, and very common: *I left it on the train* tells when it happened; *have left* stresses that it is still there now.", "Arī pareizi un ļoti bieži: *I left it on the train* pasaka, kad tas notika; *have left* uzsver, ka tas joprojām ir tur."),
    "She was upset because she ___ her ticket. (lose)": ("lost", "Correct too in everyday speech. *Had lost* makes it clear that she lost it before she was upset.", "Ikdienas runā arī pareizi. *Had lost* skaidri pasaka, ka viņa to pazaudēja, pirms bija bēdīga."),
    "I ___ my homework before dinner, so I watched TV. (finish)": ("finished", "Correct too: *before* already shows the order. *Had finished* makes it even clearer that it came first.", "Arī pareizi: *before* jau parāda secību. *Had finished* vēl skaidrāk pasaka, ka tas notika vispirms."),
    "Before he became a pilot, he ___ in a bank. (work)": ("worked", "Correct too: *before* already shows the order. *Had worked* makes it even clearer that it came first.", "Arī pareizi: *before* jau parāda secību. *Had worked* vēl skaidrāk pasaka, ka tas notika vispirms."),
}
AUX = re.compile(r"^(.*?)\s+(is|are|was|were|has|have|will|must|can|could|should)\b", re.I)


def passive_start(task, correct):
    """'Make it passive: S' -> 'Start with *X*: S' (X = the start of the answer, before the verb)."""
    m = re.match(r"^Make it passive(?:\. Start with \*([^*]+)\*)?: (.+)$", task)
    if not m: return None
    x = m.group(1)
    if not x:
        a = AUX.match(correct.split(" | ")[0])
        if not a: return None
        x = a.group(1)
    return f"Start with *{x}*: {m.group(2)}"


def fix(task, typ, correct):
    """-> new task text or None"""
    p = passive_start(task, correct)
    if p: return p
    for old, rep in PREFIX:
        if task.startswith(old):
            rest = rep + task[len(old):]
            return CONTEXT.get(rest, rest) if rep == "" else rest
    return None
