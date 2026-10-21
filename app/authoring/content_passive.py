from dsl import M, G, T, O, W

PART = r"(made|grown|produced|sold|built|eaten|used|called|spoken|cleaned|checked|sent|held|delivered|written|done|kept|opened|closed|\w+ed)"

# ───────────────────────── PRESENT SIMPLE PASSIVE ─────────────────────────
S = "present_simple_passive"

# A2.2
M(S, "A2.2", 1, "English ___ in many countries.", "is spoken", ["speaks", "is speak", "are spoken"],
  "Passive = be + past participle. English is singular, so is spoken.")
M(S, "A2.2", 2, "Which sentence is passive?", "Rice is grown in Asia.",
  ["Farmers grow rice in Asia.", "People eat rice.", "Rice grows in Asia."],
  "In a passive sentence the thing that receives the action is the subject: Rice is grown.")
G(S, "A2.2", 3, "Bread ___ from flour. (make)", "is made",
  "Passive present simple: is/are + past participle. Bread = it.",
  [(r"\bmakes\b", "Use the passive: is made.")])
G(S, "A2.2", 3, "These cars ___ in Germany. (build)", "are built",
  "These cars = they, so are built.")
M(S, "A2.2", 4, "Which sentence is NOT correct?", "Coffee is grow in Brazil.",
  ["Cheese is made from milk.", "The shops are closed on Sunday.", "Letters are delivered every day."],
  "The passive needs the past participle: Coffee is grown in Brazil.")
M(S, "A2.2", 5, "Why do we say 'Tickets are sold here'?", "The action is important. We don't need to say who sells them.",
  ["Because the tickets are very old.", "Because we want to say who sells them.", "Because the sentence is in the past."],
  "We use the passive when the action or the object is more important than the person who does it.")
W(S, "A2.2", 6, "Write one sentence about a product in your country. Use is made, is grown or are produced.",
  [(r"\b(is|are)\s+" + PART + r"\b", "Use is/are + past participle (is made, are grown ...).")],
  "Cheese is made in many parts of Latvia.")

# B1.1
M(S, "B1.1", 1, "Where ___ these phones made?", "are", ["do", "is", "did"],
  "Question: be + subject + past participle. These phones = plural, so are.")
M(S, "B1.1", 2, "In 'The report is checked by the manager', what is the focus?", "The report and what happens to it.",
  ["The manager only.", "A future plan.", "A past event."],
  "In the passive the subject (the report) is the focus.")
G(S, "B1.1", 3, "The office ___ every evening. (clean)", "is cleaned",
  "Passive present simple: is + past participle.")
T(S, "B1.1", 3, "Change to the passive: They sell fresh bread here.", ["Fresh bread is sold here."],
  "Object becomes the subject. Verb: is/are + past participle. Fresh bread is sold here.",
  [(r"\bsells\b|\bsell\b", "Use the passive: is sold, not sells.")])
M(S, "B1.1", 4, "Which sentence is NOT correct?", "Are the tickets checking at the door?",
  ["Is English taught in your school?", "Cars are washed here.", "The rooms are cleaned every day."],
  "Passive questions need the past participle: Are the tickets checked at the door?")
M(S, "B1.1", 5, "You want to write a neutral email and not blame anyone. Which sentence is best?",
  "The invoices are sent on Fridays.", ["You send the invoices on Fridays.", "Someone sends the invoices on Fridays.", "I think you send the invoices on Fridays."],
  "The passive keeps the focus on the action and does not name a person.")
W(S, "B1.1", 6, "Write one sentence about how something is made or done at your workplace. Use the passive.",
  [(r"\b(is|are)\s+" + PART + r"\b", "Use is/are + past participle.")],
  "All orders are checked twice before they are sent.")

# B1.2
M(S, "B1.2", 1, "___ English spoken in your office?", "Is", ["Does", "Do", "Are"],
  "Passive question: Is + subject + past participle.")
M(S, "B1.2", 2, "Which sentence is the passive of 'People often call him Mo'?", "He is often called Mo.",
  ["He often calls Mo.", "He is often calling Mo.", "Mo is often called him."],
  "The object (him) becomes the subject (He): He is often called Mo.")
G(S, "B1.2", 3, "How often ___ the website ___? (update)", [["is"], ["updated"]],
  "Passive question: How often + is + subject + past participle.")
T(S, "B1.2", 3, "Change to the passive without 'by': Someone cleans the rooms daily.",
  ["The rooms are cleaned daily.", "The rooms are cleaned every day."],
  "We leave out the agent (someone) because it is not important.")
M(S, "B1.2", 4, "Which sentence is NOT correct?", "The email is send every week.",
  ["Is this product made in Latvia?", "The meetings are held on Mondays.", "Many languages are spoken here."],
  "The passive needs the past participle: is sent.")
M(S, "B1.2", 5, "Which sentence puts the focus on the data, not on the person?", "The data is collected online.",
  ["Someone collects the data online.", "We collect the data online.", "They collect the data online."],
  "The passive moves the focus to the data.")
W(S, "B1.2", 6, "Write two sentences about how a product or service in your company is made or delivered. Use the passive and use by in one sentence.",
  [(r"\b(is|are)\s+" + PART + r"\b", "Use is/are + past participle."),
   (r"\bby\s+\w+", "Use by + the person or company who does it.")],
  "The orders are packed in our warehouse. They are delivered by a courier company.")

# ───────────────────────── PAST SIMPLE PASSIVE ─────────────────────────
S = "past_simple_passive"

# A2.2
M(S, "A2.2", 1, "The Eiffel Tower ___ in 1889.", "was built", ["built", "is built", "were built"],
  "Past passive: was/were + past participle. Tower = it, so was built.")
M(S, "A2.2", 2, "Which sentence is passive?", "The window was broken yesterday.",
  ["Someone broke the window.", "The window broke.", "He is breaking the window."],
  "The window receives the action. Passive: was + broken.")
G(S, "A2.2", 3, "The letters ___ yesterday. (send)", "were sent",
  "Letters = plural, so were + past participle (sent).")
G(S, "A2.2", 3, "This picture ___ by Picasso. (paint)", "was painted",
  "Picture = it, so was painted.")
M(S, "A2.2", 4, "Which sentence is NOT correct?", "The book was wrote by Tom.",
  ["The cake was eaten.", "We were invited to the party.", "The door was closed."],
  "The past participle of write is written: The book was written by Tom.")
M(S, "A2.2", 5, "Which sentence is correct for a past event when we don't know who did it?", "My bike was stolen.",
  ["My bike stole.", "My bike was stealing.", "My bike were stolen."],
  "Passive past: was/were + past participle. Bike = singular, so was stolen.")
W(S, "A2.2", 6, "Write one sentence about a famous building or invention. Use was/were built, invented or discovered.",
  [(r"\b(was|were)\s+" + PART + r"\b", "Use was/were + past participle.")],
  "The telephone was invented in 1876.")

# B1.1
M(S, "B1.1", 1, "When ___ this museum opened?", "was", ["did", "is", "has"],
  "Passive question in the past: When + was + subject + past participle.")
M(S, "B1.1", 2, "Which sentence tells us who did the action?", "The song was written by Adele.",
  ["The song was written.", "The song is written.", "The song writes."],
  "Use by + agent when we want to say who did the action.")
G(S, "B1.1", 3, "Where ___ the film ___? (film)", [["was"], ["filmed"]],
  "Question: Where + was + subject + past participle.")
T(S, "B1.1", 3, "Change to the passive: Someone stole my wallet.", ["My wallet was stolen."],
  "Passive: was + past participle. We leave out 'someone'.",
  [(r"\bstole\b", "Use the passive: was stolen.")])
M(S, "B1.1", 4, "Which sentence is NOT correct?", "She was gave a prize.",
  ["The thieves were arrested by the police.", "The bridge was built in 1998.", "I was told the news by Tom."],
  "The past participle of give is given: She was given a prize.")
M(S, "B1.1", 5, "A news report says what happened but the person who did it is unknown. Which sentence is best?",
  "A car was stolen last night.", ["Someone stealing a car last night.", "A car steals last night.", "A car were stolen last night."],
  "The passive is common in news reports when the doer is unknown.")
W(S, "B1.1", 6, "Write two sentences about something that was done at your workplace last week. Use the passive.",
  [(r"\b(was|were)\s+" + PART + r"\b", "Use was/were + past participle."),
   (r"[.!?]\s+\S", "Write two sentences.")],
  "A new printer was installed. The old one was thrown away.")

# B1.2
M(S, "B1.2", 1, "The documents ___ by the manager yesterday.", "were signed", ["was signed", "signed", "are signed"],
  "Documents = plural, so were + past participle.")
M(S, "B1.2", 2, "Which sentence has the same meaning as 'The police arrested two men'?", "Two men were arrested (by the police).",
  ["Two men arrested the police.", "Two men are arresting.", "Two men were arresting."],
  "Active object (two men) becomes passive subject: Two men were arrested.")
G(S, "B1.2", 3, "Our flight ___ because of the storm, so we ___ a hotel room. (cancel / give)", [["was cancelled", "was canceled"], ["were given"]],
  "Two passives: was cancelled, were given.")
T(S, "B1.2", 3, "Change to the passive: The company hired 20 new workers last year.",
  ["Twenty new workers were hired last year.", "20 new workers were hired last year.",
   "Twenty new workers were hired by the company last year.", "20 new workers were hired by the company last year."],
  "New workers is the subject. Was/were + past participle.")
M(S, "B1.2", 4, "Which sentence is NOT correct?", "The invoice was send on Monday.",
  ["The package was delivered yesterday.", "The decision was made last week.", "We were told to wait."],
  "Use the past participle: The invoice was sent on Monday.")
M(S, "B1.2", 5, "You want to mention a mistake politely, without blaming anyone. Which sentence is best?",
  "A mistake was made in the report.", ["You made a mistake in the report.", "Someone is making a mistake.", "I think you make mistakes."],
  "The passive hides the doer and sounds more neutral.")
W(S, "B1.2", 6, "Write two sentences to a customer: say what was done to fix a problem. Use the passive.",
  [(r"\b(was|were)\s+" + PART + r"\b", "Use was/were + past participle."),
   (r"[.!?]\s+\S", "Write two sentences.")],
  "Your order was checked again. A new part was sent to you today.")

# ───────────────────────── PRESENT CONTINUOUS PASSIVE ─────────────────────────
S = "present_continuous_passive"

# B1.2
M(S, "B1.2", 1, "The new bridge ___ at the moment.", "is being built", ["is building", "is built", "was being built"],
  "Present continuous passive: am/is/are being + past participle.")
M(S, "B1.2", 2, "Which sentence means: the work is in progress now?", "The road is being repaired.",
  ["The road was repaired.", "The road is repaired every year.", "The road will be repaired."],
  "Is being + past participle shows the action is happening now.")
G(S, "B1.2", 3, "Please wait. Your order ___. (prepare)", "is being prepared",
  "Order = it. In progress now: is being prepared.")
G(S, "B1.2", 3, "The rooms ___ right now. (clean)", "are being cleaned",
  "Rooms = plural: are being cleaned.")
M(S, "B1.2", 4, "Which sentence is NOT correct?", "The report is being write.",
  ["The hotel is being renovated.", "The cars are being washed now.", "My email is being checked."],
  "Use the past participle: The report is being written.")
M(S, "B1.2", 5, "A technician is still working on your computer. What is the best sentence?",
  "Your computer is being fixed.", ["Your computer is fixed.", "Your computer was fixed.", "Your computer fixes."],
  "'Is fixed' means the job is finished. 'Is being fixed' means it is in progress.")
W(S, "B1.2", 6, "Write one sentence about something that is being built, repaired or changed in your area now. Use is/are being.",
  [(r"\b(is|are)\s+being\s+\w+", "Use is/are being + past participle.")],
  "A new shopping centre is being built near my house.")

# ───────────────────────── PRESENT PERFECT PASSIVE ─────────────────────────
S = "present_perfect_passive"

# B1.1
M(S, "B1.1", 1, "My car ___ repaired, so I can drive again.", "has been", ["have been", "is been", "has being"],
  "Present perfect passive: has/have been + past participle.")
M(S, "B1.1", 2, "Which sentence is the passive of 'They have finished the project'?", "The project has been finished.",
  ["The project have been finished.", "The project has finished.", "The project is being finished."],
  "has been + finished. Project is singular, so has.")
G(S, "B1.1", 3, "All the tickets ___. (sell)", "have been sold",
  "Tickets = plural, so have been sold.")
T(S, "B1.1", 3, "Change to the passive: Someone has stolen my bag.", ["My bag has been stolen."],
  "has been + past participle.")
M(S, "B1.1", 4, "Which sentence is NOT correct?", "The rooms has been prepared.",
  ["The windows have been cleaned.", "The room has been booked.", "Has the letter been sent?"],
  "Rooms is plural, so have been prepared.")
M(S, "B1.1", 5, "Which sentence tells us the email is now available to check?", "The email has been sent.",
  ["The email was sent.", "The email will be sent.", "The email is sending."],
  "The present perfect passive links the past action with now.")
W(S, "B1.1", 6, "Write a sentence about something that has been done at your home or office this week. Use has/have been + past participle.",
  [(r"\b(has|have)\s+been\s+\w+", "Use has/have been + past participle.")],
  "The windows have been cleaned this week.")

# B1.2
M(S, "B1.2", 1, "___ the problem been solved yet?", "Has", ["Is", "Have", "Did"],
  "Question: Has + subject + been + past participle.")
M(S, "B1.2", 2, "Which sentence sounds like news that is important right now?", "The road has been closed because of the accident.",
  ["The road was closed in 1999.", "The road closes every night.", "The road is closing."],
  "The present perfect passive is used for recent news with a result now.")
G(S, "B1.2", 3, "Several mistakes ___ in the report so far. (find)", "have been found",
  "So far = up to now: have been found.")
T(S, "B1.2", 3, "Change to the passive: They have already sent the invoice.", ["The invoice has already been sent."],
  "Already goes between has and been.")
M(S, "B1.2", 4, "Which sentence is NOT correct?", "The room has be cleaned.",
  ["The decision has been made.", "Has the form been signed?", "The package has been delivered."],
  "We need been: The room has been cleaned.")
M(S, "B1.2", 5, "Compare 'The bridge was closed' and 'The bridge has been closed'. Which one tells us the bridge is probably still closed now?",
  "The bridge has been closed.", ["The bridge was closed.", "Both tell us the same.", "Neither tells us this."],
  "Present perfect = connection with now.")
W(S, "B1.2", 6, "Write two sentences about changes that have been made in your company, school or city. Use has/have been + past participle at least once.",
  [(r"\b(has|have)\s+been\s+\w+", "Use has/have been + past participle."),
   (r"[.!?]\s+\S", "Write two sentences.")],
  "A new office has been opened. Many old computers have been replaced.")

# ───────────────────────── WILL PASSIVE ─────────────────────────
S = "future_passive"

# B1.1
M(S, "B1.1", 1, "Your parcel ___ tomorrow.", "will be delivered", ["will deliver", "is deliver", "will be deliver"],
  "Future passive: will be + past participle.")
M(S, "B1.1", 2, "Which sentence is a prediction about what will happen to the road?", "The new road will be opened next year.",
  ["The new road was opened last year.", "The new road opens every day.", "The new road is opening."],
  "Will be + past participle looks forward and focuses on the road.")
G(S, "B1.1", 3, "The results ___ on Friday. (announce)", "will be announced",
  "will be + past participle.")
T(S, "B1.1", 3, "Change to the passive: They will open the shop at 9.", ["The shop will be opened at 9."],
  "will be + past participle.")
M(S, "B1.1", 4, "Which sentence is NOT correct?", "The prize will be giving to the winner.",
  ["The meeting will be held in Room 3.", "You will be informed by email.", "The work will be finished by June."],
  "Use the past participle: The prize will be given to the winner.")
M(S, "B1.1", 5, "You do not want to say who will do the action. Which sentence is best?", "The files will be checked on Monday.",
  ["Someone checks the files on Monday.", "The files check on Monday.", "The files will checking on Monday."],
  "The passive keeps the focus on the files.")
W(S, "B1.1", 6, "Write one sentence about something that will be done in your city or company next year. Use will be + past participle.",
  [(r"\bwill\s+be\s+\w+", "Use will be + past participle.")],
  "A new library will be opened in my city next year.")

# B1.2
M(S, "B1.2", 1, "___ the new rules be explained to us?", "Will", ["Do", "Are", "Have"],
  "Passive question: Will + subject + be + past participle.")
M(S, "B1.2", 2, "Which sentence is the passive of 'They will announce the winner tomorrow'?", "The winner will be announced tomorrow.",
  ["The winner will announce tomorrow.", "The winner is announcing tomorrow.", "The winner was announced tomorrow."],
  "will + be + past participle.")
G(S, "B1.2", 3, "Don't worry. Everything ___ before the guests arrive. (prepare)", "will be prepared",
  "will be + past participle.")
T(S, "B1.2", 3, "Change to the passive: We will send the tickets by email.", ["The tickets will be sent by email."],
  "will be + past participle.")
M(S, "B1.2", 4, "Which sentence is NOT correct?", "The class will be cancel.",
  ["The tickets won't be sold after Friday.", "Will the room be cleaned?", "You will be told the date soon."],
  "Use the past participle: The class will be cancelled.")
M(S, "B1.2", 5, "In an airport announcement, which sentence is best?", "Passengers will be informed of any changes.",
  ["Passengers informing of any changes.", "Passengers inform of any changes.", "Passengers are informing of any changes."],
  "Announcements often use the passive: will be informed.")
W(S, "B1.2", 6, "Write two sentences for a notice at work about changes next month. Use will be + past participle.",
  [(r"\bwill\s+be\s+\w+", "Use will be + past participle."),
   (r"[.!?]\s+\S", "Write two sentences.")],
  "The office will be closed on Monday. All staff will be informed by email.")
