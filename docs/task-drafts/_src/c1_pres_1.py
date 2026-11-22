"""C1 direction 1 (Advanced present simple and continuous), round 1: points x_state_cont, x_mental_cont, x_always_cont,
4 tasks each. Murphy, English Grammar in Use, units 3-4 (always + continuous; state verbs; I'm being / I am); Hewings,
Advanced Grammar in Use, units 1-2. Draft (22 November 2026): no C1 topic in the app yet, so these rows are not packaged.

The continuous of a state verb (we're loving it, I'm finding) is a choice of the speaker, so a choice between it and the simple
form would have two correct answers. The tasks therefore test (a) the verbs that stay simple (consist of, belong, own, agree,
understand, prefer), (b) where the continuous is the only form (two gaps: are ... being; is always + -ing), (c) the form
(is always losing, not is always lose)."""
from lib import gp, od, mc, tx
T = "Advanced present simple and continuous"
L = "C1"

# ── x_state_cont: state verbs in the continuous ──
# s1 work: a mistake with consist of
mc(T, L, 3, "Which sentence has a mistake?", "The new committee is consisting of five senior managers.",
   ["We're really loving the new office, especially the view.", "You're being very quiet today. Is anything wrong?",
    "This old farmhouse belongs to my grandmother."],
   "*consist of* describes what something is made of, a permanent state: it is not used in the continuous (*consists of*). "
   "*We're loving* (a feeling about something new) and *You're being quiet* (behaviour today) are correct.",
   "*consist of* apraksta, no kā kaut kas sastāv: tas ir pastāvīgs stāvoklis, tāpēc ilgstošo formu nelieto (*consists of*). "
   "*We're loving* (sajūta par kaut ko jaunu) un *You're being quiet* (uzvedība šodien) ir pareizi.")
# s2 relationships: behaviour now, only the continuous fits two gaps
gp(T, L, 4, "Write one word in each gap: Why ___ you ___ so difficult about this? It's only a small change.", "are | were / being",
   "*be* in the continuous (*are being*) describes how someone is behaving now, not what they are like: "
   "*Why are you being so difficult?* = why are you acting like this?",
   "*be* ilgstošajā formā (*are being*) apraksta, kā kāds uzvedas tagad, nevis kāds viņš ir: "
   "*Why are you being so difficult?* = kāpēc tu tagad tā uzvedies?")
# s3 lifestyle: belong stays simple
mc(T, L, 3, "Choose the correct option: This flat ___ to my aunt, so we only pay a small rent.", "belongs",
   ["is belonging", "is belonged", "belong"],
   "*belong to* is a permanent state (who it is owned by): present simple, *belongs*. It is not used in the continuous or the passive.",
   "*belong to* ir pastāvīgs stāvoklis (kam tas pieder): Present Simple, *belongs*. Ilgstošo formu un ciešamo kārtu nelieto.")
# s4 travel: a mistake with own
mc(T, L, 3, "Which sentence has a mistake?", "My parents are owning two flats in the centre of Riga.",
   ["She's being very generous with her time this week.", "I believe the conference starts at ten.",
    "We're really enjoying the course so far."],
   "*own* is a state verb (possession): *My parents own two flats*. *She's being generous* is correct: behaviour this week.",
   "*own* ir stāvokļa darbības vārds (piederība): *My parents own two flats*. Tulkojot burtiski *mani vecāki pašlaik pieder*, "
   "gribas lietot ilgstošo formu, bet angliski saka *own*. *She's being generous* ir pareizi: uzvedība šonedēļ.")

# ── x_mental_cont: thinking and feeling verbs ──
# m1 work: agree stays simple (a common mistake: I am agree)
mc(T, L, 2, "Choose the correct option: I ___ with almost everything you said in your email.", "agree",
   ["am agree", "am agreeing", "agreeing"],
   "*agree* is a state of mind: present simple, *I agree*. *I am agree* mixes *be* with the verb; *I'm agreeing* is not used.",
   "*agree* ir domāšanas stāvoklis: Present Simple, *I agree*. Tulkojot burtiski *es esmu vienisprātis*, iznāk *I am agree*, "
   "bet angliski *agree* ir darbības vārds: *I agree*.")
# m2 hobbies: prefer stays simple
mc(T, L, 3, "Which sentence has a mistake?", "I'm preferring tea to coffee these days.",
   ["I'm finding the new software surprisingly easy to use.", "We're beginning to regret buying such a big car.",
    "She's realising how much work the move involves."],
   "*prefer* stays in the present simple, even with *these days*: *I prefer tea to coffee these days*. "
   "*find*, *regret* and *realise* can be continuous for a feeling or thought that is new or growing.",
   "*prefer* paliek Present Simple arī ar *these days*: *I prefer tea to coffee these days*. "
   "*find*, *regret* un *realise* var būt ilgstošajā formā, ja doma vai sajūta ir jauna vai pieaug.")
# m3 learning: understand stays simple; the cards could give "am understanding", which the apology rules out
gp(T, L, 3, "Sorry, I ___ ___ what you mean. Could you explain it again?", "don't / understand",
   "*understand* is a state of mind: *I don't understand*. Not *I'm not understanding* or *I am understanding*.",
   "*understand* ir domāšanas stāvoklis: *I don't understand*. Ne *I'm not understanding*, ne *I am understanding*.",
   bank=["don't", "understand", "am", "understanding"])
# m4 relationships: understand in a typed gap
gp(T, L, 3, "My grandmother ___ every word you say, but she can't answer in English. (understand)", "understands",
   "*understand* is a state: present simple, *understands*, not *is understanding*.",
   "*understand* ir stāvoklis: Present Simple, *understands*, nevis *is understanding*.")

# ── x_always_cont: always / forever + continuous ──
# a1 lifestyle: where always goes
od(T, L, 3, "Put the words in order.", "my flatmate is always losing his keys",
   "*always* goes between *is* and the *-ing* form: *is always losing*. With the continuous it shows that something happens "
   "again and again, often with irritation.",
   "*always* stāv starp *is* un *-ing* formu: *is always losing*. Ar ilgstošo formu tas rāda, ka kaut kas notiek atkal un atkal, "
   "bieži ar nepatiku.")
# a2 relationships: a routine in progress at a time
gp(T, L, 4, "Don't call us at seven: we ___ usually ___ the children to bed then. (put)", "are | 're / putting",
   "*usually* + present continuous: a routine that is in progress at that time (*we are usually putting them to bed then*).",
   "*usually* + Present Continuous: ierasta darbība, kas tajā laikā jau notiek (*we are usually putting them to bed then*).")
# a3 learning: a mistake in the form
mc(T, L, 3, "Which sentence has a mistake?", "She is always forget her password at work.",
   ["He's constantly interrupting me in meetings.", "We usually have dinner at about seven.",
    "My boss is forever changing the deadlines."],
   "After *is always*, the *-ing* form: *She is always forgetting her password* (or *She always forgets*).",
   "Aiz *is always* lieto *-ing* formu: *She is always forgetting her password* (vai *She always forgets*).")
# a4 lifestyle: a complaint with forever
tx(T, L, 4, "Say it as a complaint with *forever*: My brother leaves his shoes in the hall.",
   "My brother is forever leaving his shoes in the hall. | My brother's forever leaving his shoes in the hall.",
   "*is forever* + *-ing* shows annoyance at something that happens again and again: *He is forever leaving his shoes in the hall.*",
   "*is forever* + *-ing* izsaka nepatiku par to, kas notiek atkal un atkal: *He is forever leaving his shoes in the hall.*")
