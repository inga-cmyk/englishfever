"""C1 direction 1 (Advanced present simple and continuous), round 1, second version (22 November 2026): points x_state_cont,
x_mental_cont, x_always_cont. Hewings, Advanced Grammar in Use (3rd ed.), units 1-2; Murphy, English Grammar in Use, units 3-4.
Draft: no C1 topic in the app yet, so these rows are not packaged.

The first version tested form mistakes (I am agree, is belonging) and the blind readers found them B1 (round c1-1). Teacher,
22 November: the context must be concrete but common; follow the Advanced Grammar in Use exercises. So, as in its exercises 1.1,
1.2 and 2.3: the same verb in a state meaning and an action meaning (measure, fit), verbs that stay simple even in a C1 context
(doubt, believe) or are only continuous in one meaning (consider = think about), complaints with constantly / forever, and a
routine in progress at a time. In every task the context leaves one form only. No Latvian surnames (teacher, 22 November)."""
from lib import gp, od, mc, tx
T = "Advanced present simple and continuous"
L = "C1"

# ── x_state_cont: one verb, a state or an action ──
# s1 home: measure = an action in progress
gp(T, L, 3, "What are you doing with that tape measure? I ___ the kitchen for the new cupboards. (measure)", "am measuring | 'm measuring",
   "*measure* here is an action happening now (using a tape measure): present continuous, *I'm measuring*.",
   "*measure* te ir darbība, kas notiek tagad (mēra ar mērlenti): Present Continuous, *I'm measuring*.")
# s2 home: measure = a state (the size)
gp(T, L, 3, "Our kitchen is tiny: it ___ only three metres by four. (measure)", "measures",
   "*measure* here gives the size, a state: present simple, *it measures*. The continuous is used only for the action of measuring.",
   "*measure* te norāda izmēru, tas ir stāvoklis: Present Simple, *it measures*. Ilgstošo formu lieto tikai darbībai (kāds mēra).")
# s3 home: fit = an action (install)
gp(T, L, 3, "We're eating out all week because they ___ a new kitchen in our flat. (fit)", "are fitting | 're fitting",
   "*fit* here means install, an action that is going on this week: present continuous, *they're fitting*. "
   "In the state meaning (*The jacket fits you*) it is simple.",
   "*fit* te nozīmē uzstādīt, darbība, kas notiek šonedēļ: Present Continuous, *they're fitting*. "
   "Stāvokļa nozīmē (*The jacket fits you*) lieto vienkāršo formu.")
# s4 relationships: be + being = behaviour now (both gaps leave only the continuous; get also works)
gp(T, L, 4, "Write one word in each gap: Why ___ you ___ so difficult about this? It's only a small change.", "are | were / being | getting",
   "*be* in the continuous (*are being*) describes how someone is behaving now, not what they are like: "
   "*Why are you being so difficult?* = why are you acting like this?",
   "*be* ilgstošajā formā (*are being*) apraksta, kā kāds uzvedas tagad, nevis kāds viņš ir: "
   "*Why are you being so difficult?* = kāpēc tu tagad tā uzvedies?")

# ── x_mental_cont: thinking verbs ──
# m1 work: doubt stays simple
gp(T, L, 3, "It's nearly ten o'clock. I ___ the pharmacy is still open, but we can try. (doubt)", "doubt",
   "*doubt* is a state of mind and is rarely continuous: *I doubt the pharmacy is still open*.",
   "*doubt* ir domāšanas stāvoklis, un ilgstošo formu gandrīz nelieto: *I doubt the pharmacy is still open*.")
# m2 work: consider = think about, only continuous
gp(T, L, 3, "My manager ___ taking early retirement, but she hasn't made up her mind yet. (consider)", "is considering | 's considering",
   "*consider* in the meaning *think carefully about* is only used in the continuous: *she's considering taking early retirement*.",
   "*consider* nozīmē *rūpīgi apsvērt* lieto tikai ilgstošajā formā: *she's considering taking early retirement*.")
# m3 relationships: believe stays simple, even "now"
gp(T, L, 3, "OK, I ___ you now. I'm sorry I didn't take your story seriously. (believe)", "believe",
   "*believe* stays in the present simple, also with *now*: *I believe you now*, not *I'm believing you now*.",
   "*believe* paliek Present Simple arī ar *now*: *I believe you now*, nevis *I'm believing you now*.")
# m4 the meanings together
mc(T, L, 4, "Which sentence has a mistake?", "He considers taking early retirement next year.",
   ["I'm finding the new routine quite tiring.", "I suggest you book a table in advance.",
    "This dress doesn't fit me any more."],
   "*consider* meaning *think about doing* is continuous: *He's considering taking early retirement*. "
   "*I'm finding* (a new impression), *I suggest* (the act of suggesting) and *doesn't fit* (a state) are correct.",
   "*consider* nozīmē *apsvērt* lieto ilgstošajā formā: *He's considering taking early retirement*. "
   "*I'm finding* (jauns iespaids), *I suggest* (ieteikums ar pašiem vārdiem) un *doesn't fit* (stāvoklis) ir pareizi.")

# ── x_always_cont: characteristic behaviour, a routine in progress ──
# a1 relationships: a complaint (as Advanced Grammar in Use 2.3)
tx(T, L, 4, "Answer with *constantly* and *change your mind*: \"Actually, I'll have the fish, not the pasta.\"",
   "You're constantly changing your mind. | You are constantly changing your mind.",
   "*be constantly* + *-ing* shows that something happens so often that it is typical of the person, often with irritation: "
   "*You're constantly changing your mind.*",
   "*be constantly* + *-ing* rāda, ka kaut kas notiek tik bieži, ka tas ir raksturīgi cilvēkam, bieži ar nepatiku: "
   "*You're constantly changing your mind.*")
# a2 work: a routine in progress at a time
gp(T, L, 4, "Don't phone me at half past eight: I ___ usually ___ to work then. (drive)", "am | 'm / driving",
   "*usually* + present continuous: something we regularly do that is in progress at that time (*I'm usually driving to work then*).",
   "*usually* + Present Continuous: ierasta darbība, kas tajā laikā jau notiek (*I'm usually driving to work then*).")
# a3 the form: where forever goes
mc(T, L, 3, "Which sentence has a mistake?", "My neighbour forever is borrowing my tools.",
   ["He's always offering to help with the shopping.", "At eight I'm usually driving to work.",
    "She constantly checks her phone in meetings."],
   "*forever*, *always*, *constantly* go after *is*: *My neighbour is forever borrowing my tools.*",
   "*forever*, *always*, *constantly* stāv aiz *is*: *My neighbour is forever borrowing my tools.*")
# a4 relationships: the word order of a complaint
od(T, L, 3, "Put the words in order.", "you're constantly interrupting me when I'm speaking",
   "*constantly* goes between *you're* and the *-ing* form; the *when*-part can come first or second.",
   "*constantly* stāv starp *you're* un *-ing* formu; daļa ar *when* var būt pirmā vai otrā.",
   also=["when I'm speaking you're constantly interrupting me"])
