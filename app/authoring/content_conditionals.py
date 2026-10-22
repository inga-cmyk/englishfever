from dsl import M, G, T, O, W, D

# The if-part of a second conditional must not contain will/would. The comma is not required: with a comma the if-part is
# everything before it; without one, only "if + subject + would/will" is flagged (so "If I won I would go" is fine).
NO_WOULD_AFTER_IF = r"^(?!\s*if\b(?:[^,]*\b(?:will|would)\b[^,]*,|(?!.*,)\s+(?:(?:the|my|our|your|his|her|their|this|that)\s+)?\w+\s+(?:would|will|'d)\b))"

# Conditionals: zero, first, second, third, mixed, advanced.
# Word-order (O) tasks use lower-case words without punctuation, so more than one correct order can be accepted.

# ───────────────────────── ZERO CONDITIONAL ─────────────────────────
S = "cond_zero"

# A2.2
M(S, "A2.2", 1, "Choose the correct form: If you heat ice, it ___.", "melts", ["will melt", "melting", "is melt"],
  "Zero conditional: if + present simple, present simple. It describes something that is always true.")
D(S, "A2.2", 2, "Match each beginning with the right ending. These are things that are always true.",
  [("If you heat water to 100 degrees,", "it boils."), ("If you don't sleep enough,", "you feel tired."),
   ("If the traffic light is red,", "cars stop."), ("If you mix red and blue,", "you get purple.")],
  "The zero conditional (if + present simple, present simple) is for facts and general rules.")
G(S, "A2.2", 3, "If you ___ the button, the coffee machine ___. (press / start)", [["press"], ["starts"]],
  "Zero conditional: present simple in both parts.",
  [(r"will", "In the zero conditional we use the present simple in both parts: no will.")])
M(S, "A2.2", 4, "Which sentence is NOT correct?", "If you will heat ice, it melts.",
  ["If you heat ice, it melts.", "If I drink coffee at night, I can't sleep.", "If people don't eat, they get hungry."],
  "We do not use will after if. Say: If you heat ice, it melts.")
M(S, "A2.2", 5, "A learner wrote: 'If you will mix blue and yellow, you get green.' What is the best advice?",
  "Remove will: 'If you mix blue and yellow, you get green.'",
  ["Change get to will get: 'If you will mix blue and yellow, you will get green.'", "Change mix to mixes.", "It is correct. Do not change it."],
  "In the zero conditional both verbs are in the present simple. Will is not used.")
W(S, "A2.2", 6, "Write a sentence about something that always happens in your office or at home. Start with If and use the present simple.",
  [(r"^\s*if\b", "Start with If."), (r"^(?!.*\b(will|won't|would|'ll)\b)", "Do not use will. In the zero conditional both parts use the present simple.")],
  "If I skip breakfast, I get grumpy by ten.")

# B1.1
M(S, "B1.1", 1, "Which word can replace 'if' in a zero conditional? 'If it rains, the street floods.'", "whenever", ["unless", "although", "because"],
  "In a zero conditional, when or whenever means the same as if: it is always true.")
M(S, "B1.1", 2, "Which sentence is a zero conditional (always true), not a first conditional (one future situation)?",
  "If metal gets hot, it expands.",
  ["If it gets hot tomorrow, I will go to the beach.", "If the shop is closed, we will try the other one.", "If I had more time, I would learn Italian."],
  "A zero conditional describes a general truth. The others are about one future situation or an imaginary one.")
T(S, "B1.1", 3, "Rewrite with when: If you press this button, the door opens.",
  ["When you press this button, the door opens.", "Whenever you press this button, the door opens."],
  "In a zero conditional, when and whenever can replace if.",
  [(r"will", "Use the present simple in both parts: ... the door opens.")])
M(S, "B1.1", 4, "Which sentence is NOT correct?", "If people don't sleep enough, they would be grumpy.",
  ["If people don't sleep enough, they get grumpy.", "Whenever I forget my umbrella, it rains.", "If the printer jams, everybody panics."],
  "A general truth uses the present simple in both parts: they get grumpy.")
M(S, "B1.1", 5, "Your manager writes a rule: 'If a visitor will arrive, sign them in at reception.' Which version is best?",
  "If a visitor arrives, sign them in at reception.",
  ["If a visitor would arrive, sign them in at reception.", "If a visitor arrived, sign them in at reception.", "If a visitor will arrive, signing them in at reception."],
  "A rule uses if + present simple, then an instruction. We do not use will after if.")
W(S, "B1.1", 6, "Write a rule for a new colleague. Use If + present simple, then an instruction (for example: If the light is red, wait).",
  [(r"^\s*if\b", "Start with If."), (r"^(?!.*\b(will|would|won't|'ll)\b)", "Do not use will or would in a rule like this.")],
  "If the printer jams, ask Marta for help.")

# ───────────────────────── FIRST CONDITIONAL ─────────────────────────
S = "cond_first"

# A2.2
M(S, "A2.2", 1, "Choose the correct form: If it ___ tomorrow, we will stay at home.", "rains", ["will rain", "rained", "is raining"],
  "In the if-part we use the present simple, even when we talk about the future.")
M(S, "A2.2", 2, "What does this sentence mean? 'If you finish the report, I'll buy you a coffee.'",
  "It is a promise about a possible future.",
  ["It is a fact that is always true.", "It is about something in the past.", "It is about an impossible situation."],
  "The first conditional talks about real, possible future situations. Here it is a promise.")
G(S, "A2.2", 3, "If she ___ late, we ___ without her. (be / start)", [["is"], ["will start", "'ll start"]],
  "First conditional: if + present simple, will + base verb.",
  [(r"^will\b", "After if we use the present simple: If she is late, ...")])
M(S, "A2.2", 4, "Which sentence is NOT correct?", "If I will see him, I will tell him.",
  ["If you hurry, you'll catch the bus.", "She'll be angry if you forget.", "If it's sunny, we'll have lunch outside."],
  "No will in the if-part. Say: If I see him, I will tell him.")
M(S, "A2.2", 5, "A friend writes: 'If I will have time, I will call you.' What is the best advice?",
  "Say 'If I have time, I'll call you.'",
  ["Say 'If I would have time, I will call you.'", "Say 'If I had time, I will call you.'", "It is correct. Do not change it."],
  "After if we use the present simple: If I have time, I'll call you.")
W(S, "A2.2", 6, "Write a promise to a colleague. Start with If, use the present simple after if and will in the second part. Put a comma after the if-part.",
  [(r"^\s*if\b", "Start with If."), (r"\b(will|'ll)\b", "Use will in the second part."),
   (r"^(?!\s*if\b[^,]*\b(will|would)\b)", "Use the present simple after if (no will), and put a comma after the if-part.")],
  "If you cover my shift, I will bring you cake.")
O(S, "A2.2", 3, "Put the words in order.", "if you ask nicely I will help you",
  "First conditional: if + present simple, will + base verb. The if-part can come first or second.",
  ["I will help you if you ask nicely"])
G(S, "A2.2", 3, "If you ___ the bus, you ___ be late. (miss / will)", [["miss"], ["will"]],
  "First conditional: if + present simple, will + base verb.")

# B1.1
M(S, "B1.1", 1, "Choose the correct word: We won't finish on time ___ we start now.", "unless", ["if", "when", "although"],
  "Unless means if ... not: We won't finish unless we start now.")
D(S, "B1.1", 2, "Match each beginning with the most natural ending.",
  [("If the train is late,", "we will take a taxi."), ("If you eat that curry,", "you will need a glass of milk."),
   ("If you don't back up your files,", "you might lose everything."), ("Unless it stops raining,", "the picnic will be cancelled.")],
  "In the first conditional we describe a possible future situation and its likely result.")
G(S, "B1.1", 3, "___ you finish early, we ___ go for a drink.", [["If"], ["will"]],
  "First conditional: If + present simple, will + base verb.", bank=["If", "Unless", "will", "would"])
G(S, "B1.1", 3, "I'll call you as soon as I ___ at the station. (arrive)", ["arrive", "get", "reach"],
  "After as soon as, when and before we use the present simple for the future.",
  [(r"will", "After as soon as we use the present simple: ... as soon as I arrive.")])
M(S, "B1.1", 4, "Which sentence is NOT correct?", "I'll text you when I will get home.",
  ["I'll text you as soon as I get home.", "If you don't hurry, you'll miss it.", "We won't go unless the weather improves."],
  "After when, as soon as, if and unless we use the present simple for the future: when I get home.")
M(S, "B1.1", 5, "You want to warn a friend who keeps forgetting his password. Which sentence is correct and sounds like a warning?",
  "If you forget it again, you'll be locked out.",
  ["If you will forget it again, you'll be locked out.", "If you forgot it again, you'll be locked out.", "If you forget it again, you locked out."],
  "A warning uses if + present simple, then will + base verb.")
W(S, "B1.1", 6, "Write a sentence with unless about something you must do to avoid a problem.",
  [(r"\bunless\b", "Use unless.")],
  "Unless I leave now, I will miss my train.")
M(S, "B1.1", 1, "Which sentence is a correct first conditional?", "If it snows tonight, the office will close.",
  ["If it will snow tonight, the office closes.", "If it snowed tonight, the office will close.", "If it snows tonight, the office would close."],
  "First conditional: if + present simple, will + base verb.")
O(S, "B1.1", 3, "Put the words in order.", "unless you hurry you will miss the train",
  "Unless means if ... not. After unless we use the present simple.", ["you will miss the train unless you hurry"])

# B1.2
M(S, "B1.2", 1, "Choose the correct form: I'll call you as soon as I ___.", "arrive", ["will arrive", "would arrive", "arrived"],
  "After as soon as we use the present simple for the future.")
M(S, "B1.2", 2, "What is the difference? A: 'If you're late, I'll be angry.' B: 'If you're late, I might be angry.'",
  "A is more certain than B.",
  ["B is more certain than A.", "A is about the past and B is about the future.", "There is no difference."],
  "Will is certain. Might, may and could show that the result is possible but not sure.")
T(S, "B1.2", 3, "Rewrite with unless: If you don't practise, you won't improve.",
  ["Unless you practise, you won't improve.", "Unless you practice, you won't improve."],
  "Unless means if ... not. After unless we use the present simple (no negative).",
  [(r"unless you don't", "After unless we do not use a negative: Unless you practise, ...")])
M(S, "B1.2", 4, "Which sentence is NOT correct?", "Unless you don't hurry, you will be late.",
  ["Unless you hurry, you will be late.", "If you don't hurry, you will be late.", "You will be late unless you hurry."],
  "Unless already means if ... not, so we do not add a second negative.")
M(S, "B1.2", 5, "In an email to a client you want to sound confident but polite. Which sentence is best?",
  "If you send us the documents today, we will process your request by Friday.",
  ["If you will send us the documents today, we will process your request by Friday.", "If you sent us the documents today, we will process your request by Friday.",
   "If you send us the documents today, we would process your request by Friday."],
  "Real future condition: if + present simple, will + base verb.")
W(S, "B1.2", 6, "Write a sentence with in case (for example: I'll take an umbrella in case it rains). Use the present simple after in case.",
  [(r"\bin case\b", "Use in case."), (r"^(?!.*\bin case\b.*\b(will|would)\b)", "After in case we use the present simple: in case it rains.")],
  "I'll take a charger in case my phone dies.")

# ───────────────────────── SECOND CONDITIONAL ─────────────────────────
S = "cond_second"

# B1.1
M(S, "B1.1", 1, "Choose the correct form: If I ___ a million euros, I would buy a boat.", "had", ["have", "will have", "would have"],
  "Second conditional: if + past simple, would + base verb.")
M(S, "B1.1", 2, "What does this sentence mean? 'If I were taller, I would play basketball.'",
  "I am not tall, so I don't play basketball.",
  ["I am tall and I play basketball.", "I will be taller soon.", "I played basketball when I was young."],
  "The second conditional talks about unreal or unlikely situations. The verb is past, but the meaning is now.")
G(S, "B1.1", 3, "If I ___ the boss, I ___ cancel all Monday meetings. (be)", [["were", "was"], ["would", "'d"]],
  "Second conditional: if + past simple (were), would + base verb.")
M(S, "B1.1", 4, "Which sentence is NOT correct?", "If I will win the lottery, I would buy an island.",
  ["If I won the lottery, I would buy an island.", "If I were you, I wouldn't do that.", "What would you do if you saw a ghost?"],
  "The if-part uses the past simple, not will: If I won the lottery, ...")
M(S, "B1.1", 5, "Your friend can't decide whether to quit and become a baker. You give advice. Which sentence is best?",
  "If I were you, I would talk to a few bakers first.",
  ["If I am you, I will talk to a few bakers first.", "If I would be you, I talk to a few bakers first.", "If I was you, I will talk to a few bakers first."],
  "For advice we say: If I were you, I would + base verb.")
W(S, "B1.1", 6, "Write a sentence about what you would do if you won a free holiday. Start with If, use the past simple after if and would in the second part.",
  [(r"^\s*if\b", "Start with If."), (r"\b(would|'d)\b", "Use would in the second part."),
   (NO_WOULD_AFTER_IF, "Use the past simple after if (not would): If I won a holiday, I would go to Iceland.")],
  "If I won a free holiday, I would go to Iceland.")
G(S, "B1.1", 3, "If I ___ a cat, I ___ sleep all day.", [["were"], ["would"]],
  "Second conditional: if + were / past simple, would + base verb.", bank=["were", "would", "will", "had"])
O(S, "B1.1", 3, "Put the words in order.", "if I had more time I would learn the piano",
  "Second conditional: if + past simple, would + base verb. The if-part can come first or second.", ["I would learn the piano if I had more time"])

# B1.2
M(S, "B1.2", 1, "Which question is correct? '___ you do if you lost your passport abroad?'", "What would", ["What will", "What did", "What are"],
  "Second conditional question: What would you do if you + past simple?")
D(S, "B1.2", 2, "Match each sentence with its meaning.",
  [("If I had a car, I would drive to work.", "I don't have a car."), ("If I have a car next year, I will drive to work.", "Maybe I'll buy one."),
   ("If I had had a car, I would have driven to work.", "I didn't have a car then."), ("If you heat ice, it melts.", "This is always true.")],
  "Zero: always true. First: real future. Second: unreal now. Third: unreal past.")
T(S, "B1.2", 3, "Rewrite as a second conditional: I don't have enough money, so I can't buy a new laptop.",
  ["If I had enough money, I could buy a new laptop.", "If I had enough money, I would buy a new laptop.", "If I had enough money, I'd buy a new laptop."],
  "Second conditional: if + past simple, would / could + base verb.",
  [(r"if i have\b", "Use the past simple after if: If I had enough money, ...")])
M(S, "B1.2", 4, "Which sentence is NOT correct?", "If I would have more free time, I would join a choir.",
  ["If I had more free time, I would join a choir.", "I would join a choir if I had more free time.", "If I had more free time, I might join a choir."],
  "Do not use would in the if-part. Say: If I had more free time, ...")
M(S, "B1.2", 5, "You advise a manager. Which sentence is correct and polite?", "If I were you, I would speak to the team before the meeting.",
  ["If I were you, I will speak to the team before the meeting.", "If I am you, I would speak to the team before the meeting.", "If you were me, I would speak to the team before the meeting."],
  "Advice: If I were you, I would + base verb.")
W(S, "B1.2", 6, "Write a sentence about an unlikely job you would like. Use if + past simple and would.",
  [(r"^\s*if\b", "Start with If."), (r"\b(would|'d)\b", "Use would in the second part."),
   (NO_WOULD_AFTER_IF, "Use the past simple after if (not would): If I were a pilot, I would fly.")],
  "If I were a pilot, I would fly to Iceland every weekend.")

# B2.1
M(S, "B2.1", 1, "Which is correct? 'If I ___ you, I'd think twice about that offer.'", "were", ["am", "would be", "had been"],
  "In careful English we use were for all persons after if in the second conditional.")
M(S, "B2.1", 2, "What is the difference? A: 'If I had time, I would help.' B: 'If I had time, I might help.'",
  "B is less certain than A.", ["A is less certain than B.", "A is about the past and B about the future.", "There is no difference in meaning."],
  "Would shows the result is certain in that imaginary situation. Might shows it is only possible.")
G(S, "B2.1", 3, "If the company ___ more flexible hours, people ___ happier. (offer / be)", [["offered", "were to offer"], ["would be", "'d be"]],
  "Second conditional: if + past simple (or were to + base verb), would + base verb.")
M(S, "B2.1", 4, "Which sentence has a mistake?", "If I would know the answer, I would tell you.",
  ["If I knew the answer, I would tell you.", "If I knew the answer, I'd tell you.", "I would tell you if I knew the answer."],
  "Would does not go in the if-part. Say: If I knew the answer, I would tell you.")
M(S, "B2.1", 5, "Which sentence is best for a polite request in a formal email?", "I would be grateful if you could send me the report by Friday.",
  ["I would be grateful if you will send me the report by Friday.", "I would grateful if you could send me the report by Friday.", "I would be grateful if you could to send me the report by Friday."],
  "A polite request: I would be grateful if you could + base verb.")
W(S, "B2.1", 6, "Write advice for a colleague who works too much. Start with If I were you and use would.",
  [(r"^\s*if i (were|was) you\b", "Start with If I were you."), (r"\b(would|'d)\b", "Use would in the second part.")],
  "If I were you, I would switch off my phone after seven.")

# ───────────────────────── THIRD CONDITIONAL ─────────────────────────
S = "cond_third"

# B1.2
M(S, "B1.2", 1, "Choose the correct form: If I ___ earlier, I wouldn't have missed the train.", "had left", ["left", "would have left", "have left"],
  "Third conditional: if + past perfect, would have + past participle.")
M(S, "B1.2", 2, "'If we had booked earlier, we would have got a cheaper flight.' What really happened?",
  "We did not book early, and the flight was expensive.",
  ["We booked early and got a cheap flight.", "We will book early next time.", "We never fly."],
  "The third conditional imagines a different past. The real past was the opposite.")
G(S, "B1.2", 3, "If you ___ me about the meeting, I ___ there. (tell / be)", [["had told"], ["would have been", "'d have been"]],
  "Third conditional: if + had + past participle, would have + past participle.",
  [(r"^told\b", "In the if-part use had + past participle: had told.")])
M(S, "B1.2", 4, "Which sentence is NOT correct?", "If I would have known, I would have called you.",
  ["If I had known, I would have called you.", "I would have called you if I had known.", "If I hadn't known, I wouldn't have called you."],
  "Do not use would in the if-part. Say: If I had known, ...")
M(S, "B1.2", 5, "A colleague forgot to save a file and lost two hours of work. Which comment is a correct third conditional?",
  "If you had saved it every ten minutes, you wouldn't have lost so much work.",
  ["If you saved it every ten minutes, you wouldn't have lost so much work.", "If you had saved it every ten minutes, you won't lose so much work.",
   "If you would have saved it every ten minutes, you wouldn't have lost so much work."],
  "Third conditional: if + past perfect, would have + past participle.")
W(S, "B1.2", 6, "Write a sentence about a mistake you made once (for example, a missed bus). Start with If I had and use would have.",
  [(r"^\s*if i had\b", "Start with If I had."), (r"\b(would|wouldn't|could|might)\s+(not\s+)?have\b|'d\s+(not\s+)?have\b", "Use would have + past participle in the second part.")],
  "If I had checked the time, I wouldn't have missed the bus.")
O(S, "B1.2", 3, "Put the words in order.", "if I had known about the party I would have bought a gift",
  "Third conditional: if + past perfect, would have + past participle.", ["I would have bought a gift if I had known about the party"])

# B2.1
M(S, "B2.1", 1, "Choose the correct form: She would have passed the exam if she ___ harder.", "had studied", ["studied", "would study", "has studied"],
  "Third conditional: would have + past participle, if + past perfect.")
M(S, "B2.1", 2, "'If he hadn't been so rude, we might have signed the deal.' What does 'might have' show?",
  "The result was possible but not certain.", ["The result was certain.", "The result was impossible.", "The deal was signed."],
  "Might have and could have show a possible result of the imagined past. Would have shows a certain one.")
T(S, "B2.1", 3, "Rewrite as a third conditional: I didn't see the sign, so I parked there and got a fine.",
  ["If I had seen the sign, I wouldn't have parked there.", "If I had seen the sign, I wouldn't have got a fine.", "If I had seen the sign, I would not have got a fine.",
   "If I had seen the sign, I wouldn't have gotten a fine.", "If I had seen the sign, I wouldn't have been fined.", "If I had seen the sign, I would not have parked there."],
  "Third conditional: if + had seen, would not have + past participle.")
M(S, "B2.1", 4, "Which sentence has a mistake?", "If the team has been better prepared, we would have won.",
  ["If the team had been better prepared, we would have won.", "We would have won if the team had been better prepared.", "If the team hadn't been so tired, we might have won."],
  "The if-part needs the past perfect: had been, not has been.")
M(S, "B2.1", 5, "Which sentence is best for a polite criticism in a work review?", "If you had told us earlier, we could have adjusted the schedule.",
  ["If you told us earlier, we could have adjusted the schedule.", "If you had told us earlier, we could adjust have the schedule.", "If you would tell us earlier, we could have adjusted the schedule."],
  "Third conditional with could have: if + past perfect, could have + past participle.")
W(S, "B2.1", 6, "Write a sentence about a decision that changed your life. Start with If I hadn't and use would have.",
  [(r"^\s*if i (hadn't|had not)\b", "Start with If I hadn't."), (r"\b(would|wouldn't|could|might)\s+(not\s+)?have\b|'d\s+(not\s+)?have\b", "Use would have + past participle in the second part.")],
  "If I hadn't joined that course, I wouldn't have met my best friend.")

# B2.2
M(S, "B2.2", 1, "Which pair is correct? 'If she ___ the warning, she ___ the accident.'", "had heard / would have avoided",
  ["heard / would avoid", "had heard / would avoid", "would have heard / had avoided"],
  "Third conditional: if + past perfect, would have + past participle.")
M(S, "B2.2", 2, "What is the difference? A: 'If you had asked, I would have helped.' B: 'If you asked, I would help.'",
  "A is about the past (you did not ask). B is about now or the future.",
  ["A is about now. B is about the past.", "Both are about the past.", "There is no difference."],
  "Third conditional = past, unreal. Second conditional = present or future, unreal.")
G(S, "B2.2", 3, "If he ___ (not / drive) so fast, he ___ (not / lose) his licence.",
  [["hadn't driven", "had not driven"], ["wouldn't have lost", "would not have lost", "'d not have lost"]],
  "Negative third conditional: hadn't + past participle, wouldn't have + past participle.")
M(S, "B2.2", 4, "Which sentence has a mistake?", "If I'd have known about the traffic, I would've left earlier.",
  ["If I'd known about the traffic, I would've left earlier.", "If I had known about the traffic, I would have left earlier.", "Had I known about the traffic, I would have left earlier."],
  "'If I'd have known' is a common mistake. In the if-part use had + past participle: If I'd known.")
M(S, "B2.2", 5, "Which sentence expresses regret best in a formal apology?", "If I had realised the impact of my decision, I would have acted differently.",
  ["If I realised the impact of my decision, I would have acted differently.", "If I would have realised the impact of my decision, I acted differently.", "If I had realise the impact of my decision, I would have acted differently."],
  "Formal regret about the past: if + past perfect, would have + past participle.")
W(S, "B2.2", 6, "Write a sentence about what would have happened in history if one thing had been different (for example a famous discovery).",
  [(r"\bif\b", "Use if."), (r"\bhad(n't| not)?\b", "Use the past perfect (had / hadn't) in the if-part."), (r"\b(would|might|could)\s+(not\s+)?have\b", "Use would / might / could have + past participle in the result.")],
  "If Alexander Fleming hadn't left his dish uncovered, penicillin might not have been discovered.")

# ───────────────────────── MIXED CONDITIONALS ─────────────────────────
S = "cond_mixed"

# B2.1
M(S, "B2.1", 1, "Which sentence is a mixed conditional (past condition, present result)?", "If I had taken that job, I would be rich now.",
  ["If I took that job, I would be rich.", "If I had taken that job, I would have been rich.", "If I take that job, I will be rich."],
  "Mixed conditional: if + past perfect (past), would + base verb (now).")
M(S, "B2.1", 2, "'If I hadn't moved to Riga, I wouldn't have this job now.' What does it mean?",
  "I moved to Riga, so I have this job today.", ["I didn't move to Riga, so I have no job.", "I will move to Riga.", "I have this job, but I never lived in Riga."],
  "A past action (moved) has a result in the present (have this job).")
G(S, "B2.1", 3, "If I ___ English at school, I ___ fluent now. (learn / be)", [["had learned", "had learnt"], ["would be", "'d be"]],
  "Mixed conditional: if + had + past participle, would + base verb.")
M(S, "B2.1", 4, "Which sentence is NOT correct?", "If I would have studied medicine, I would be a doctor now.",
  ["If I had studied medicine, I would be a doctor now.", "If I'd studied medicine, I'd be a doctor now.", "I would be a doctor now if I had studied medicine."],
  "Do not use would in the if-part: If I had studied medicine, ...")
M(S, "B2.1", 5, "Which sentence best explains why someone is tired today because of last night?", "If I hadn't stayed up so late, I wouldn't be so tired now.",
  ["If I didn't stay up so late, I wouldn't have been so tired now.", "If I hadn't stayed up so late, I wouldn't have been so tired now.", "If I wouldn't have stayed up so late, I wasn't so tired now."],
  "Past cause, present result: if + past perfect, would + base verb.")
W(S, "B2.1", 6, "Write a sentence about how a past decision affects you now. Start with If I had and use would + base verb (not would have).",
  [(r"^\s*if i had\b", "Start with If I had."), (r"\b(would|'d)\s+(?!have\b)\w+", "Use would + base verb for the present result.")],
  "If I had gone to bed earlier, I would feel better now.")

# B2.2
M(S, "B2.2", 1, "Complete: 'If I weren't so shy, I ___ asked her out last year.'", "would have", ["would", "will have", "had"],
  "Present quality (weren't), past result (would have asked): if + past simple, would have + past participle.")
M(S, "B2.2", 2, "'If she were more organised, she wouldn't have missed the deadline.' What does it say?",
  "She is not organised in general, and that caused the missed deadline.", ["She is organised, but she missed the deadline.", "She will be organised next week.", "She did not miss the deadline."],
  "A present, permanent quality caused a past result.")
T(S, "B2.2", 3, "Rewrite as a mixed conditional: He didn't take the job, so he isn't living in Paris now.",
  ["If he had taken the job, he would be living in Paris now.", "If he'd taken the job, he'd be living in Paris now."],
  "Mixed conditional: if + had + past participle, would + base verb.")
M(S, "B2.2", 4, "Which sentence is NOT correct?", "If I am more careful, I wouldn't have lost my keys.",
  ["If I were more careful, I wouldn't have lost my keys.", "If I had been more careful, I wouldn't have lost my keys.", "If I hadn't been so careless, I wouldn't be searching now."],
  "Do not use am in an unreal condition. Say: If I were more careful, ...")
M(S, "B2.2", 5, "A colleague says: 'If I had a better memory, I would have remembered your birthday.' Which comment explains the grammar best?",
  "It is a mixed conditional: a present quality (memory) with a past result.",
  ["It is a first conditional about the future.", "It is a zero conditional about a fact.", "It is a third conditional because of would have."],
  "The if-part is past simple (present quality). The result is would have + past participle (past).")
W(S, "B2.2", 6, "Write a mixed conditional sentence: a present quality + a past result (for example: If I were braver, I would have ...).",
  [(r"\bif\b", "Use if."), (r"\b(would|wouldn't|could|might)\s+(not\s+)?have\b|'d\s+(not\s+)?have\b", "Use would have + past participle for the past result.")],
  "If I were more patient, I wouldn't have shouted at the printer yesterday.")

# C1.1
M(S, "C1.1", 1, "Which sentence uses inversion in a mixed conditional?", "Had I taken that job, I would be rich now.",
  ["Had I take that job, I would be rich now.", "If had I taken that job, I would be rich now.", "Did I take that job, I would be rich now."],
  "Inversion replaces if with Had + subject + past participle.")
M(S, "C1.1", 2, "'Were I more experienced, I would have applied for the director role last year.' What does 'Were I' replace?",
  "If I were", ["If I had been", "If I will be", "Unless I was"],
  "Were I = If I were. It is formal.")
T(S, "C1.1", 3, "Rewrite with inversion: If I had listened to my accountant, I wouldn't be in this mess now.",
  ["Had I listened to my accountant, I wouldn't be in this mess now.", "Had I listened to my accountant, I'd not be in this mess now."],
  "Inversion: Had + subject + past participle replaces if I had + past participle.")
M(S, "C1.1", 4, "Which sentence is NOT correct?", "Hadn't I taken that job, I wouldn't be living here now.",
  ["Had I not taken that job, I wouldn't be living here now.", "Had I taken that job, I would be rich now.", "Were I braver, I would have said no."],
  "Negative inversion is Had I not ..., not Hadn't I ...")
M(S, "C1.1", 5, "Which sentence is best in a formal report about a past failure with a present effect?",
  "Had the contract been checked properly, we would not be facing these penalties now.",
  ["If the contract had checked properly, we would not be facing these penalties now.", "Had the contract been checked properly, we wouldn't facing these penalties now.", "Had checked the contract properly, we would not be facing these penalties now."],
  "Passive inversion: Had + object + been + past participle.")
W(S, "C1.1", 6, "Write a mixed conditional with inversion about a past decision and its effect today. Start with Had I.",
  [(r"^\s*had i\b", "Start with Had I."), (r"\b(would|wouldn't|'d)\b", "Use would in the second part.")],
  "Had I saved more when I was young, I would be more relaxed about money today.")

# ───────────────────────── ADVANCED CONDITIONALS ─────────────────────────
S = "cond_advanced"

# C1.1
M(S, "C1.1", 1, "Which sentence means the same as 'If you should need any help, call me'?", "Should you need any help, call me.",
  ["Did you need any help, call me.", "Would you need any help, call me.", "Need you any help, call me."],
  "Should + subject + base verb is a formal way to say if you should ...")
M(S, "C1.1", 2, "What does 'unless' mean in 'We'll start unless it rains'?", "if it does not rain", ["if it rains", "because it rains", "although it rains"],
  "Unless = if ... not.")
T(S, "C1.1", 3, "Rewrite with unless: You will not get a refund if you don't have a receipt.",
  ["You will not get a refund unless you have a receipt.", "Unless you have a receipt, you will not get a refund."],
  "Unless replaces if ... not, so the verb after unless is positive.",
  [(r"unless you don't", "After unless we do not use a negative: ... unless you have a receipt.")])
M(S, "C1.1", 4, "Which sentence is NOT correct?", "Unless you don't hurry, we will miss the flight.",
  ["Unless you hurry, we will miss the flight.", "If you don't hurry, we will miss the flight.", "We will miss the flight unless you hurry."],
  "Unless already contains the negative. Do not add another one.")
M(S, "C1.1", 5, "Which sentence is the most formal?", "Should you require further information, please contact our office.",
  ["If you want more info, ring us.", "If you need more information, just call us.", "Call us if you need more info."],
  "Should + subject + verb is formal and common in business letters.")
W(S, "C1.1", 6, "Write a sentence with 'provided that' or 'as long as' to give a condition for a favour.",
  [(r"\b(provided that|providing that|as long as|so long as)\b", "Use provided that or as long as.")],
  "You can borrow my laptop as long as you bring it back by Friday.")

# C1.2
M(S, "C1.2", 1, "Which sentence expresses regret about the present?", "I wish I lived closer to the sea.",
  ["I wish I had lived closer to the sea.", "I wish I will live closer to the sea.", "I wish I would live closer to the sea."],
  "wish + past simple = regret about a present situation.")
M(S, "C1.2", 2, "'I wish you would stop clicking your pen.' What does 'wish + would' show?",
  "annoyance about someone's repeated behaviour", ["regret about the past", "a plan for the future", "a polite offer"],
  "wish + would is for things that annoy us and that we want to change.")
G(S, "C1.2", 3, "I wish I ___ that email yesterday. Now everyone knows.", "hadn't sent",
  "wish + past perfect = regret about the past.", bank=["hadn't sent", "didn't send", "wouldn't send", "haven't sent"])
M(S, "C1.2", 4, "Which sentence has a mistake?", "If only I would have saved more money when I was young.",
  ["If only I had saved more money when I was young.", "I wish I had saved more money when I was young.", "If only I saved more money now."],
  "If only + past perfect is used for regret about the past. Not would have.")
M(S, "C1.2", 5, "Which version sounds best in a speech about a past failure?", "If only we had listened to the warning signs, we would not be in this position.",
  ["If only we would have listened to the warning signs, we would not be in this position.", "If only we listened to the warning signs, we would not be in this position.", "If only we had listen to the warning signs, we would not be in this position."],
  "If only + had + past participle, then would + base verb for the present result.")
W(S, "C1.2", 6, "Write a sentence with 'I wish' or 'If only' about something you regret from last year.",
  [(r"\b(i wish|if only)\b", "Use I wish or If only."), (r"\bhad(n't| not)?\b", "For a regret about the past use the past perfect (had / hadn't).")],
  "I wish I had started learning Spanish last year.")
