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
gp(T, L, 3, "What are you doing with that tape measure? I ___ the kitchen for the new cupboards. (measure)", "am measuring | 'm measuring | am going to measure | 'm going to measure",
   "*measure* here is an action happening now (using a tape measure): present continuous, *I'm measuring*.",
   "*measure* te ir darbība, kas notiek tagad (mēra ar mērlenti): Present Continuous, *I'm measuring*.")
# s2 home: measure = a state (the size)
gp(T, L, 3, "Our kitchen is tiny: it ___ only three metres by four. (measure)", "measures",
   "*measure* here gives the size, a state: present simple, *it measures*. The continuous is used only for the action of measuring.",
   "*measure* te norāda izmēru, tas ir stāvoklis: Present Simple, *it measures*. Ilgstošo formu lieto tikai darbībai (kāds mēra).")
# ── x_mental_cont: thinking verbs ──
# m2 work: consider = think about, only continuous
gp(T, L, 3, "My manager ___ taking early retirement, but she hasn't made up her mind yet. (consider)", "is considering | 's considering | has been considering | 's been considering",
   "*consider* in the meaning *think carefully about* is only used in the continuous: *she's considering taking early retirement*.",
   "*consider* nozīmē *rūpīgi apsvērt* lieto tikai ilgstošajā formā: *she's considering taking early retirement*.")
# ── x_always_cont: characteristic behaviour, a routine in progress ──
# a1 relationships: a complaint (as Advanced Grammar in Use 2.3)
tx(T, L, 4, "Your friend changes the order for the third time: \"Actually, I'll have the fish, not the pasta.\" Complain, using *constantly* and *change your mind*.",
   "You're constantly changing your mind. | You are constantly changing your mind. | You constantly change your mind.",
   "*be constantly* + *-ing* shows that something happens so often that it is typical of the person, often with irritation: "
   "*You're constantly changing your mind.*",
   "*be constantly* + *-ing* rāda, ka kaut kas notiek tik bieži, ka tas ir raksturīgi cilvēkam, bieži ar nepatiku: "
   "*You're constantly changing your mind.*")
# a2 work: a routine in progress at a time
gp(T, L, 4, "Write one word in each gap: Don't phone me at half past eight: I ___ usually ___ to work then. (drive)", "am | 'm / driving",
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
   also=["when I'm speaking you're constantly interrupting me", "you're interrupting me constantly when I'm speaking", "when I'm speaking you're interrupting me constantly"])

# ── added after round c1-1b (the judge dropped the copying tasks) ──
# s5 one verb, a state or an action: weigh, feel, fit
mc(T, L, 4, "Which sentence has a mistake?", "This old suitcase is weighing nearly five kilos.",
   ["The vet is weighing the dog right now.", "This scarf feels lovely and soft.",
    "They're fitting a new kitchen in our flat this week."],
   "*weigh* for the weight of something is a state: *This suitcase weighs 23 kilos*. *The vet is weighing the dog* is the action, "
   "so the continuous is right there.",
   "*weigh* svara nozīmē ir stāvoklis: *This suitcase weighs 23 kilos*. *The vet is weighing the dog* ir darbība, "
   "tāpēc tur ilgstošā forma ir pareiza.")
# p1 work: saying it is doing it (performative)
gp(T, L, 3, "Write to a customer: We ___ for the delay in replying to your email. (apologise)", "apologise | do apologise | apologize | do apologize",
   "When the words themselves are the act (apologising by saying it), use the present simple: *We apologise for the delay*, "
   "not *We're apologising*.",
   "Ja paši vārdi ir darbība (atvainojamies, to sakot), lieto Present Simple: *We apologise for the delay*, nevis *We're apologising*.")
# h1 news: a headline
mc(T, L, 3, "Which is the usual way to write this as a news headline?", "Health minister resigns over expenses",
   ["Health minister has resigned over expenses", "Health minister is resigning over expenses",
    "Health minister resigned over expenses"],
   "Headlines use the present simple for an event that has just happened: *Health minister resigns*. "
   "In a normal sentence we would say *has resigned*.",
   "Virsrakstos par tikko notikušu lietu lieto Present Simple: *Health minister resigns*. "
   "Parastā teikumā teiktu *has resigned*.")
