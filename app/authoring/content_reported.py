from dsl import M, G, T, O, W, D

# Reported speech and indirect questions.
# Word-order (O) tasks use lower-case words without punctuation, so more than one correct order can be accepted.

# ───────────────────────── REPORTED STATEMENTS ─────────────────────────
S = "rep_statements"

# B1.1
M(S, "B1.1", 1, "Complete the report. 'I am tired,' she said. → She said she ___ tired.", "was", ["is", "am", "will be"],
  "In reported speech the verb usually goes one step back in time: am / is → was.")
D(S, "B1.1", 2, "Match each sentence with its report.",
  [("'I work in a bank,' she said.", "She said she worked in a bank."), ("'I'm working late,' she said.", "She said she was working late."),
   ("'I finished the report,' she said.", "She said she had finished the report."), ("'I can come,' she said.", "She said she could come.")],
  "Reported speech goes one step back: work → worked, am working → was working, finished → had finished, can → could.")
G(S, "B1.1", 3, "'I don't like coffee,' Mark said. → Mark said he ___ coffee. (not / like)", ["didn't like", "did not like"],
  "The present simple moves back to the past simple: don't like → didn't like.",
  [(r"doesn't|does not|don't|do not", "In reported speech the present simple becomes the past simple: he didn't like.")])
M(S, "B1.1", 4, "Which sentence is NOT correct?", "He said me he was tired.",
  ["He told me he was tired.", "He said he was tired.", "He said to me that he was tired."],
  "After said we do not use a person directly. Use told me, or said to me.")
M(S, "B1.1", 5, "Report this: 'I can't come to the meeting,' Jon said. Choose the correct option.", "Jon said he couldn't come to the meeting.",
  ["Jon said I couldn't come to the meeting.", "Jon said he can't came to the meeting.", "Jon said he couldn't to come to the meeting."],
  "can't → couldn't, and I → he (Jon is talking about himself).")
W(S, "B1.1", 6, "Report this sentence. 'I'm learning Spanish,' Elena said. Start with Elena said.",
  [(r"^\s*elena said\b", "Start with Elena said."), (r"\bshe\b", "Change I to she."), (r"\bwas learning\b", "am learning becomes was learning.")],
  "Elena said she was learning Spanish.")

# B1.2
M(S, "B1.2", 1, "Choose the correct tense. Direct: 'I have finished.' Reported: He said he ___ finished.", "had", ["has", "have", "was"],
  "The present perfect (have finished) goes back to the past perfect (had finished).")
M(S, "B1.2", 2, "What usually happens to 'tomorrow' and 'now' in reported speech?",
  "They change to 'the next day' and 'then'.", ["They stay the same.", "They change to 'yesterday' and 'always'.", "They disappear."],
  "Time words move too: now → then, today → that day, tomorrow → the next day, yesterday → the day before.")
T(S, "B1.2", 3, "Report this: 'I'm leaving now,' Kate said.",
  ["Kate said she was leaving then.", "Kate said that she was leaving then.", "Kate said she was leaving at that moment.", "Kate said that she was leaving at that moment.",
   "Kate said she was leaving at that time.", "Kate said that she was leaving at that time.", "Kate said she was leaving right then."],
  "I → she, am leaving → was leaving, now → then.",
  [(r"\bnow\b", "Now usually becomes then or at that moment.")])
M(S, "B1.2", 4, "Which sentence is NOT correct?", "She said she will call me the next day.",
  ["She said she would call me the next day.", "She told me she had finished the report.", "He said he was working at home that day."],
  "Will goes back to would in reported speech: She said she would call me.")
M(S, "B1.2", 5, "You report a message to your manager: 'We are almost ready,' the team said. Choose the correct option.", "The team told me they were almost ready.",
  ["The team told me we were almost ready.", "The team said me they were almost ready.", "The team told they were almost ready."],
  "told needs a person (told me). We becomes they, and are goes back to were.")
W(S, "B1.2", 6, "Report what a colleague said yesterday: 'I'll send the file tomorrow.' Start with He said.",
  [(r"^\s*he said\b", "Start with He said."), (r"\bwould\b|'d\b", "will becomes would."), (r"\b(the next day|the following day|today|that day|the day after)\b", "tomorrow changes: the next day (or today).")],
  "He said he would send the file the next day.")
O(S, "B1.2", 3, "Put the words in order.", "she said she was leaving at six that day",
  "Reported speech: said + subject + backshifted verb. Today becomes that day.", ["she said she was leaving that day at six"])

# B2.1
M(S, "B2.1", 1, "Which modal verb does NOT change in reported speech?", "might", ["can", "will", "must"],
  "can → could, will → would, must → had to. Might, would, could, should and ought to stay the same.")
M(S, "B2.1", 2, "'The Earth goes round the Sun,' the teacher said. Which report is also correct, and why?",
  "The teacher said the Earth goes round the Sun, because it is always true.",
  ["It must be 'went', because said is in the past.", "It must be 'had gone'.", "It is wrong, because reported speech always changes the tense."],
  "When the fact is still true, the tense does not have to go back.")
T(S, "B2.1", 3, "Report this: 'You must finish by Friday,' my boss said.",
  ["My boss said I had to finish by Friday.", "My boss said that I had to finish by Friday.", "My boss told me I had to finish by Friday.", "My boss told me that I had to finish by Friday.",
   "My boss said I must finish by Friday.", "My boss told me I must finish by Friday."],
  "must can become had to. It can also stay must when the duty is still there.")
M(S, "B2.1", 4, "Which sentence is NOT correct?", "She told that she would be late.",
  ["She said that she would be late.", "She told me that she would be late.", "She told us she would be late."],
  "tell is always followed by a person: She told me / us ...")
M(S, "B2.1", 5, "Report this naturally: 'I won't sign it until the lawyer reads it,' the client said. Choose the correct option.",
  "The client said he wouldn't sign it until the lawyer had read it.",
  ["The client said he won't sign it until the lawyer will read it.", "The client said I wouldn't sign it until the lawyer reads it.", "The client told he wouldn't sign it until the lawyer read it."],
  "won't → wouldn't, I → he, and the earlier action goes back to the past perfect.")
W(S, "B2.1", 6, "Report a warning from your doctor: 'You must drink more water.' Start with My doctor said.",
  [(r"^\s*my doctor (said|told me)\b", "Start with My doctor said."), (r"\b(had to|must|should)\b", "must becomes had to (or stays must)."), (r"\b(i|me)\b", "Change you to I.")],
  "My doctor said I had to drink more water.")

# ───────────────────────── REPORTED QUESTIONS AND REQUESTS ─────────────────────────
S = "rep_questions"

# B1.2
M(S, "B1.2", 1, "Choose the correct report. 'Where do you work?' She asked me ___.", "where I worked",
  ["where did I work", "where do I work", "where I work did"],
  "In a reported question we use normal word order (subject + verb) and no do / does / did.")
M(S, "B1.2", 2, "Which word(s) do we use to report a yes/no question?", "if or whether", ["that", "what", "do"],
  "'Do you like jazz?' → He asked if (or whether) I liked jazz.")
G(S, "B1.2", 3, "'What time does the film start?' → She asked what time the film ___. (start)", "started",
  "Reported question: normal word order, the verb goes back to the past: started.",
  [(r"does|did|start$|^start\b", "No does or did in a reported question: ... what time the film started.")])
M(S, "B1.2", 4, "Which sentence is NOT correct?", "He asked me where did I live.",
  ["He asked me where I lived.", "He asked if I wanted a coffee.", "She asked whether it was true."],
  "A reported question has statement word order: where I lived, not where did I live.")
M(S, "B1.2", 5, "A hotel guest asked: 'Is breakfast included?' You report the question. Choose the correct option.", "The guest asked whether breakfast was included.",
  ["The guest asked was breakfast included.", "The guest asked that breakfast was included.", "The guest asked is breakfast included."],
  "Yes/no question: asked + if / whether + subject + verb.")
W(S, "B1.2", 6, "Report this question: 'Why are you leaving?' Start with Kate asked me why.",
  [(r"^\s*kate asked me why\b", "Start with Kate asked me why."), (r"\bi was leaving\b", "Statement word order: why I was leaving.")],
  "Kate asked me why I was leaving.")
M(S, "B1.2", 1, "Which sentence reports the request 'Please wait here,' the guard said?", "The guard told me to wait there.",
  ["The guard told me wait there.", "The guard told me that I wait here.", "The guard said me to wait there."],
  "Orders and requests: told / asked + person + to + base verb. Here becomes there.")
O(S, "B1.2", 3, "Put the words in order.", "she asked me where I lived", "Reported question: asked + question word + subject + verb.")
O(S, "B1.2", 3, "Put the words in order.", "he asked if I had finished the report", "Yes/no question: asked + if + subject + verb.")

# B2.1
M(S, "B2.1", 1, "Which report is correct? 'Can you help me?' she asked.", "She asked if I could help her.",
  ["She asked if could I help her.", "She asked can I help her.", "She asked that I could help her."],
  "can → could, you → I, me → her, and statement word order after if.")
M(S, "B2.1", 2, "'Don't touch that!' the nurse said. Which report is correct?", "The nurse told me not to touch it.",
  ["The nurse told me to not touching it.", "The nurse told me that I don't touch it.", "The nurse said me not to touch it."],
  "A negative order: told + person + not + to + base verb.")
T(S, "B2.1", 3, "Report this: 'Could you send me the invoice?' Lena asked.",
  ["Lena asked me to send her the invoice.", "Lena asked if I could send her the invoice.", "Lena asked whether I could send her the invoice.",
   "Lena asked me if I could send her the invoice.", "Lena asked me whether I could send her the invoice."],
  "A request can be reported with asked + person + to + base verb, or with if / whether + could.")
M(S, "B2.1", 4, "Which sentence is NOT correct?", "He asked me what time was it.",
  ["He asked me what time it was.", "He asked me when the train left.", "He asked me if I knew the way."],
  "In a reported question the subject comes before the verb: what time it was.")
M(S, "B2.1", 5, "You report a customer's question to your team: 'How long will the repair take?' the customer asked. Choose the correct option.",
  "The customer asked how long the repair would take.",
  ["The customer asked how long would the repair take.", "The customer asked how long will the repair take.", "The customer asked how long did the repair take."],
  "Normal word order, and will goes back to would.")
W(S, "B2.1", 6, "Report a request you received at work: 'Could you call the supplier?' Start with My manager asked me.",
  [(r"^\s*my manager asked me\b", "Start with My manager asked me."), (r"\bto call\b|\bif i could call\b|\bwhether i could call\b", "Use to call, or if / whether I could call.")],
  "My manager asked me to call the supplier.")

# B2.2
M(S, "B2.2", 1, "Which report is correct? 'What should I do?' he asked me.", "He asked me what to do.",
  ["He asked me what should he do.", "He asked me what he does.", "He asked me what to doing."],
  "A wh-question with should can be reported with a question word + to + base verb: what to do.")
M(S, "B2.2", 2, "What is the difference? A: 'She asked me what to do.' B: 'She asked me what she should do.'",
  "There is no difference in meaning. A is shorter.", ["A is about the past and B about the future.", "A is a request and B is a question.", "B is wrong."],
  "Both are correct. The to-infinitive form is shorter and common in careful English.")
T(S, "B2.2", 3, "Report this: 'Where should we meet?' they asked.",
  ["They asked where to meet.", "They asked where they should meet.", "They asked where we should meet."],
  "Question word + to-infinitive, or question word + subject + should.")
M(S, "B2.2", 4, "Which sentence is NOT correct?", "She asked me whether or not did I agree.",
  ["She asked me whether or not I agreed.", "She asked me whether I agreed or not.", "She asked if I agreed."],
  "After whether we use statement word order: whether or not I agreed.")
M(S, "B2.2", 5, "You write meeting minutes: 'Has the budget been approved?' Ms Novak asked. Choose the correct option.", "Ms Novak asked whether the budget had been approved.",
  ["Ms Novak asked has the budget been approved.", "Ms Novak asked whether had the budget been approved.", "Ms Novak asked that the budget had been approved."],
  "Yes/no question: asked + whether + subject + verb. The present perfect goes back to the past perfect.")
W(S, "B2.2", 6, "Report this question using whether. 'Is the data accurate?' the editor asked. Start with The editor asked whether.",
  [(r"^\s*the editor asked whether\b", "Start with The editor asked whether."), (r"\bthe data (was|had been)\b", "Use statement word order and the past: the data was accurate.")],
  "The editor asked whether the data was accurate.")

# ───────────────────────── REPORTING VERBS ─────────────────────────
S = "rep_verbs"

# B2.2
M(S, "B2.2", 1, "Which sentence reports 'I'm sorry I'm late' with a reporting verb?", "He apologised for being late.",
  ["He apologised that he was late.", "He apologised to be late.", "He apologised of being late."],
  "apologise for + -ing.")
D(S, "B2.2", 2, "Match each sentence with the best reporting verb.",
  [("'I'll definitely be there on time,' she said.", "promised"), ("'Don't touch the red button!' he said.", "warned"),
   ("'Why don't we try the new café?' she said.", "suggested"), ("'Yes, I broke the vase,' he said.", "admitted")],
  "A reporting verb shows what the speaker did: promise, warn, suggest, admit.")
T(S, "B2.2", 3, "Report with a reporting verb: 'I didn't take your phone,' Max said.",
  ["Max denied taking my phone.", "Max denied taking your phone.", "Max denied that he had taken my phone.", "Max denied having taken my phone.",
   "Max denied that he took my phone.", "Max denied that he had taken your phone."],
  "deny + -ing, or deny + that + clause.")
M(S, "B2.2", 4, "Which sentence is NOT correct?", "She suggested to go by train.",
  ["She suggested going by train.", "She suggested that we go by train.", "She suggested we should go by train."],
  "suggest is not followed by to + base verb. Use -ing or that + clause.")
M(S, "B2.2", 5, "Report a polite refusal: 'No, I won't work this weekend,' Sam said. Choose the correct option.", "Sam refused to work that weekend.",
  ["Sam refused working that weekend.", "Sam refused that he works this weekend.", "Sam refused me to work that weekend."],
  "refuse + to + base verb.")
W(S, "B2.2", 6, "Report this apology with apologise: 'Sorry I forgot the meeting,' Dana said.",
  [(r"\bapologi[sz]ed\b", "Use apologised."), (r"\bfor\s+(forgetting|having forgotten)\b", "Use for + -ing: apologised for forgetting.")],
  "Dana apologised for forgetting the meeting.")

# C1.1
M(S, "C1.1", 1, "Which sentence reports 'You broke the printer!' as an accusation?", "She accused me of breaking the printer.",
  ["She accused me to break the printer.", "She accused me that I broke the printer.", "She accused me for breaking the printer."],
  "accuse + person + of + -ing.")
M(S, "C1.1", 2, "What is the difference? A: 'He insisted on paying.' B: 'He offered to pay.'",
  "A means he would not let others pay. B is a polite offer.", ["A is a polite offer and B is a demand.", "Both mean the same.", "A is about the past and B about the future."],
  "insist on = refuse to accept a different decision. offer = suggest you will do something.")
T(S, "C1.1", 3, "Report with congratulate: 'Well done on winning the award!' Tim said to Jo.",
  ["Tim congratulated Jo on winning the award.", "Tim congratulated Jo for winning the award."],
  "congratulate + person + on + -ing.")
M(S, "C1.1", 4, "Which sentence is NOT correct?", "He blamed me for to lose the file.",
  ["He blamed me for losing the file.", "He accused me of losing the file.", "He admitted losing the file."],
  "blame + person + for + -ing.")
M(S, "C1.1", 5, "Report this concisely and naturally: 'I'm very sorry for the delay, and I will make sure it never happens again,' the manager said. Choose the correct option.",
  "The manager apologised for the delay and promised that it would not happen again.",
  ["The manager said that he was very sorry for the delay and he will make sure it never happens again.", "The manager apologised the delay and promised that it will not happen again.",
   "The manager apologised for the delay and promised to that it would not happen again."],
  "A reporting verb says what the speaker did. apologise for + noun, promise + that + clause.")
W(S, "C1.1", 6, "Report with a reporting verb. 'It wasn't me who broke it!' said Leo.",
  [(r"\b(denied|insisted|claimed|protested)\b", "Use a reporting verb such as denied or insisted.")],
  "Leo denied breaking it.")

# C1.2
M(S, "C1.2", 1, "Which sentence reports 'If I were you, I'd take the earlier train,' she said?", "She advised me to take the earlier train.",
  ["She suggested me to take the earlier train.", "She insisted me to take the earlier train.", "She advised to me take the earlier train."],
  "advise + person + to + base verb.")
M(S, "C1.2", 2, "'I'm not going to tell you who did it,' the officer said. Which reporting verb shows he said no?", "refused",
  ["promised", "admitted", "suggested"], "refuse (to + base verb) means to say no.")
T(S, "C1.2", 3, "Report with a reporting verb: 'You really should see a doctor about that cough,' my sister said.",
  ["My sister advised me to see a doctor about that cough.", "My sister urged me to see a doctor about that cough.", "My sister told me to see a doctor about that cough.",
   "My sister encouraged me to see a doctor about that cough.", "My sister recommended that I see a doctor about that cough.", "My sister recommended that I should see a doctor about that cough.",
   "My sister suggested that I see a doctor about that cough.", "My sister suggested that I should see a doctor about that cough."],
  "advise / urge / tell / encourage + person + to + base verb, or recommend / suggest + that + subject + base verb.")
M(S, "C1.2", 4, "Which sentence has a mistake?", "He recommended me to read the report carefully.",
  ["He recommended reading the report carefully.", "He recommended that I read the report carefully.", "He advised me to read the report carefully."],
  "recommend is not followed by person + to. Use recommend + -ing, recommend + that, or advise + person + to.")
M(S, "C1.2", 5, "You report a complaint in formal English: 'The service was terrible and nobody apologised,' the customer said. Choose the correct option.",
  "The customer complained that the service had been terrible and that nobody had apologised.",
  ["The customer complained about the service had been terrible.", "The customer complained to be terrible the service.", "The customer complained me that the service was terrible."],
  "complain + that + clause. The past goes back to the past perfect.")
W(S, "C1.2", 6, "Report with a reporting verb and a noun phrase: 'Thank you for everything you've done,' Mia said to the team.",
  [(r"\b(thanked|expressed)\b", "Use thanked (or expressed thanks).")],
  "Mia thanked the team for everything they had done.")

# ───────────────────────── INDIRECT QUESTIONS (POLITE) ─────────────────────────
S = "ind_polite"

# B1.1
M(S, "B1.1", 1, "Choose the correct sentence.", "Could you tell me where the station is?",
  ["Could you tell me where is the station?", "Could you tell me where's the station is?", "Could you tell me where the station?"],
  "After Could you tell me we use statement word order: where the station is.")
D(S, "B1.1", 2, "Match each direct question with its polite, indirect form.",
  [("Where is the toilet?", "Do you know where the toilet is?"), ("What time does the bank open?", "Could you tell me what time the bank opens?"),
   ("How much is this?", "Can you tell me how much this is?"), ("Is the shop open?", "I wonder if the shop is open.")],
  "An indirect question starts with a polite phrase, then uses statement word order (no do / does).")
G(S, "B1.1", 3, "Where does Anna live? → Do you know where Anna ___?", "lives",
  "In an indirect question there is no does: where Anna lives.",
  [(r"does|live$", "No does in the indirect part: ... where Anna lives.")])
M(S, "B1.1", 4, "Which sentence is NOT correct?", "Do you know what time does the film start?",
  ["Do you know what time the film starts?", "Could you tell me where she lives?", "I wonder how much it costs."],
  "No does after the question word in an indirect question: what time the film starts.")
M(S, "B1.1", 5, "You ask a stranger for the post office. Choose the most polite option.", "Excuse me, could you tell me where the post office is?",
  ["Where is the post office?", "Tell me where the post office is.", "Excuse me, where is the post office?"],
  "A polite phrase + an indirect question sounds softer and more polite.")
W(S, "B1.1", 6, "Write a polite indirect question to ask a colleague where the meeting room is. Start with Could you tell me.",
  [(r"^\s*could you tell me where\b", "Start with Could you tell me where."), (r"^(?!.*\bwhere\s+is\b)", "Use statement word order: where the meeting room is.")],
  "Could you tell me where the meeting room is?")
O(S, "B1.1", 3, "Put the words in order.", "could you tell me where the station is", "Polite phrase + question word + subject + verb.")
O(S, "B1.1", 3, "Put the words in order.", "do you know what time the bank opens", "Do you know + question word + subject + verb (no does).")

# B1.2
M(S, "B1.2", 1, "Choose the correct word: Do you know ___ the shop is open on Sundays?", "if", ["what", "where is", "do"],
  "For a yes/no question inside another question we use if or whether.")
M(S, "B1.2", 2, "Why is 'Could you tell me where is the station?' wrong?", "After 'Could you tell me' we need statement word order: where the station is.",
  ["Because we must use what instead of where.", "Because the sentence needs two question marks.", "Because 'Could' must be 'Can'."],
  "In an indirect question the verb comes after the subject.")
T(S, "B1.2", 3, "Make it polite: What time does the museum close?",
  ["Could you tell me what time the museum closes?", "Do you know what time the museum closes?", "Can you tell me what time the museum closes?",
   "Would you mind telling me what time the museum closes?", "I wonder what time the museum closes."],
  "Polite phrase + what time + subject + verb. No does.",
  [(r"does", "No does in the indirect part: ... what time the museum closes.")])
M(S, "B1.2", 4, "Which sentence is NOT correct?", "I wonder what does she want.",
  ["I wonder what she wants.", "Do you know who she is?", "Could you tell me if he's here?"],
  "After I wonder we use statement word order: what she wants.")
M(S, "B1.2", 5, "You write a polite email to a client. Choose the correct option.", "Could you let me know whether the contract has been signed?",
  ["Could you let me know has the contract been signed?", "Could you let me know if has the contract been signed?", "Could you let me know whether has been the contract signed?"],
  "Could you let me know + whether / if + subject + verb.")
W(S, "B1.2", 6, "Write an indirect question to ask a stranger whether the café takes cards. Start with Do you know if.",
  [(r"^\s*do you know (if|whether)\b", "Start with Do you know if."), (r"\b(takes|accepts|take|accept)\b", "Use takes or accepts cards."), (r"^(?!.*\bdoes\b)", "No does in the indirect part.")],
  "Do you know if the café takes cards?")
O(S, "B1.2", 3, "Put the words in order.", "I wonder what time the meeting starts", "I wonder + question word + subject + verb.")

# B2.1
M(S, "B2.1", 1, "Which sentence is correct and polite?", "Would you mind telling me how long the repair will take?",
  ["Would you mind telling me how long will the repair take?", "Would you mind to tell me how long the repair will take?", "Would you mind telling me how long does the repair take?"],
  "Would you mind + -ing, then statement word order.")
M(S, "B2.1", 2, "What is the difference? A: 'Where is the manager?' B: 'Do you happen to know where the manager is?'",
  "B is more polite and indirect.", ["A is more polite than B.", "B asks about the past.", "They are the same."],
  "Indirect questions with phrases like Do you happen to know sound softer.")
T(S, "B2.1", 3, "Make it indirect: Why didn't the order arrive?",
  ["Could you tell me why the order didn't arrive?", "Do you know why the order didn't arrive?", "Can you tell me why the order didn't arrive?",
   "I'd like to know why the order didn't arrive.", "Would you mind telling me why the order didn't arrive?"],
  "Polite phrase + why + subject + verb (past simple, no did).",
  [(r"\bdid\b", "No did in the indirect part: ... why the order didn't arrive.")])
M(S, "B2.1", 4, "Which sentence is NOT correct?", "I'd like to know where did you put the keys.",
  ["I'd like to know where you put the keys.", "Do you remember where you put the keys?", "I wonder where I put them."],
  "Statement word order after I'd like to know: where you put the keys.")
M(S, "B2.1", 5, "You call customer service. Choose the correct option.", "I was wondering if you could tell me when my order will be delivered.",
  ["I was wondering when will my order be delivered?", "I was wondering if you could tell me when will my order be delivered?", "I was wondering that you could tell me when my order will be delivered."],
  "I was wondering if you could tell me + when + subject + verb.")
W(S, "B2.1", 6, "Write a polite indirect question to ask when a report will be ready. Start with I was wondering.",
  [(r"^\s*i was wondering\b", "Start with I was wondering."), (r"\b(when|if|whether)\b", "Use when, if or whether."),
   (r"^(?!.*\b(when|where|what|why|how)\s+(will|would|is|are|was|were|does|do|did)\b)", "Use statement word order: when the report will be ready.")],
  "I was wondering if you could tell me when the report will be ready.")

# ───────────────────────── EMBEDDED QUESTIONS (ADVANCED) ─────────────────────────
S = "ind_advanced"

# B2.2
M(S, "B2.2", 1, "Which is correct? 'I don't know ___.'", "what to do", ["what to doing", "what do I", "what to I do"],
  "Question word + to + base verb: what to do.")
M(S, "B2.2", 2, "'I have no idea how to start.' What does 'how to start' mean?", "how I should start", ["when I started", "why I started", "that I will start"],
  "A question word + to-infinitive shows what you do not know how or what to do.")
T(S, "B2.2", 3, "Join with a question word + to: I don't know. What should I say?",
  ["I don't know what to say.", "I do not know what to say."],
  "I don't know + what + to + base verb.")
M(S, "B2.2", 4, "Which sentence is NOT correct?", "I can't decide whether accepting the offer.",
  ["I can't decide whether to accept the offer.", "I can't decide whether or not to accept the offer.", "I can't decide whether to accept the offer or not."],
  "After whether we use to + base verb, or a full clause.")
M(S, "B2.2", 5, "You write a formal email. Choose the correct option.", "It remains unclear who is responsible for the delay.",
  ["It remains unclear who is the responsible for the delay.", "It remains unclear who responsible is for the delay.", "It remains unclear who does responsible for the delay."],
  "Embedded question: who + is + responsible (statement order).")
W(S, "B2.2", 6, "Write a sentence with 'I have no idea' and a question word (how, what, where, when, who or why).",
  [(r"\bi have no idea (how|what|where|when|who|why|which)\b", "Use I have no idea + a question word.")],
  "I have no idea how long the meeting will take.")

# C1.1
M(S, "C1.1", 1, "Which sentence uses an embedded question as the subject?", "What he said surprised everyone.",
  ["He said what surprised everyone.", "What did he say surprised everyone.", "Surprised everyone what he said."],
  "What he said is a noun clause. It is the subject of surprised.")
M(S, "C1.1", 2, "'It depends on whether the budget is approved.' Why whether and not if?", "After a preposition we use whether, not if.",
  ["Because whether is more polite.", "Because the sentence is in the past.", "Because if is not a word."],
  "after prepositions: depends on whether, talk about whether.")
T(S, "C1.1", 3, "Combine: Who made the decision? It's not clear.",
  ["It's not clear who made the decision.", "It is not clear who made the decision."],
  "It's not clear + who + verb (statement order).")
M(S, "C1.1", 4, "Which sentence is NOT correct?", "We talked about how could we improve the results.",
  ["We talked about how to improve the results.", "We talked about how we could improve the results.", "We talked about whether to improve the results."],
  "No question order after about: how we could improve the results.")
M(S, "C1.1", 5, "You write a report: 'The question is ___.' Choose the correct option.", "whether the project is worth the cost",
  ["is the project worth the cost", "if is the project worth the cost", "whether is the project worth the cost"],
  "The question is + whether + subject + verb.")
W(S, "C1.1", 6, "Write a sentence starting with 'The question is' + whether / how / why + a clause.",
  [(r"^\s*the question is (whether|how|why|what|who|where|when)\b", "Start with The question is + a question word.")],
  "The question is whether we can afford the delay.")

# C1.2
M(S, "C1.2", 1, "Choose the correct word: ___ finishes first wins a prize.", "Whoever", ["Whomever", "Whatever", "However"],
  "Whoever is the subject of finishes. It means any person who.")
M(S, "C1.2", 2, "'Whatever he says, don't sign it.' What does 'whatever' mean here?", "it does not matter what he says",
  ["he says everything", "he says nothing", "he says it twice"], "whatever / whoever / wherever + clause: it does not matter what / who / where.")
T(S, "C1.2", 3, "Rewrite with a wh-ever word: It doesn't matter who calls. Don't answer.",
  ["Whoever calls, don't answer.", "Whoever calls, do not answer."],
  "Whoever + verb = it does not matter who.")
M(S, "C1.2", 4, "Which sentence is NOT correct?", "Whomever wins the contract will celebrate.",
  ["Whoever wins the contract will celebrate.", "Give it to whomever you trust.", "Give it to whoever wants it."],
  "Whoever wins: whoever is the subject. In 'whomever you trust', whomever is the object.")
M(S, "C1.2", 5, "You write a formal report. Choose the correct option.", "How the funds were spent remains to be investigated.",
  ["How were the funds spent remains to be investigated.", "How the funds were spent it remains to be investigated.", "How funds were the spent remains to be investigated."],
  "An embedded question used as the subject keeps statement word order.")
W(S, "C1.2", 6, "Write a sentence with 'whoever', 'whatever' or 'wherever' to describe a flexible rule at your workplace.",
  [(r"\b(whoever|whatever|wherever|whenever|whichever|however)\b", "Use whoever, whatever, wherever or similar.")],
  "You can sit wherever you like.")
