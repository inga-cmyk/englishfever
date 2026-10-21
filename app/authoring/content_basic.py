from dsl import M, G, T, O, W

# ───────────────────────── PRESENT SIMPLE (active) ─────────────────────────
S = "present_simple"

# A2.1
M(S, "A2.1", 1, "Choose the correct form: She ___ in a bank.", "works", ["work", "is work", "working"],
  "With he, she and it we add -s to the verb: she works.",
  {"work": "Careful: 'she' is third person singular, so the verb needs -s."})
M(S, "A2.1", 2, "Which sentence is about a habit (something you do again and again)?",
  "I drink tea every morning.", ["I am drinking tea now.", "I drank tea yesterday.", "I will drink tea tomorrow."],
  "'Every morning' shows a habit. We use the present simple for habits and routines.")
G(S, "A2.1", 3, "My brother ___ football. (not / like)", ["doesn't like", "does not like"],
  "With he, she, it we use doesn't + the base verb: he doesn't like.",
  [(r"\bdoesn't likes\b|\bdoes not likes\b", "After doesn't we use the base verb: like, not likes."),
   (r"\bdon't like\b|\bdo not like\b", "'My brother' = he. With he/she/it we use doesn't, not don't.")])
T(S, "A2.1", 3, "Make it negative: They play tennis on Sundays.", ["They don't play tennis on Sundays.", "They do not play tennis on Sundays."],
  "With I, you, we, they we make the negative with don't + base verb.",
  [(r"\bdoesn't\b|\bdoes not\b", "'They' needs don't, not doesn't.")])
M(S, "A2.1", 4, "Which sentence is NOT correct?", "She don't work on Sunday.",
  ["He plays the guitar.", "Do you like pizza?", "We live in Riga."],
  "With 'she' we say doesn't: She doesn't work on Sunday.")
M(S, "A2.1", 5, "A friend writes: 'Does he works here?' What is the best advice?",
  "Write 'Does he work here?' After does we use the base verb.",
  ["The sentence is correct. Do not change it.", "Write 'Do he works here?'", "Write 'Is he works here?'"],
  "In questions the helper verb (do/does) shows the person. The main verb stays in the base form: Does he work?")
W(S, "A2.1", 6, "Write one sentence about what your friend or colleague does every day. Start with He or She.",
  [(r"\b(he|she)\s+(?!is\b|was\b|has\b)\w+s\b", "Use he or she + a verb with -s, for example: she starts work at eight."),
   (r"\b(every|each)\s+(day|morning|evening|week|weekday|afternoon)\b|\b(always|usually|often|sometimes|never)\b",
    "Add a time word such as every day, usually or always.")],
  "She starts work at eight every day.")

# A2.2
M(S, "A2.2", 1, "Choose the correct word: Where ___ your sister work?", "does", ["do", "is", "works"],
  "Questions in the present simple: do/does + subject + base verb. Sister = she, so does.")
M(S, "A2.2", 2, "Which sentence is about a timetable?", "The train leaves at 7.45 tomorrow.",
  ["The train is leaving now.", "The train left at 7.45 yesterday.", "I am on the train."],
  "We use the present simple for fixed timetables, even for the future.")
G(S, "A2.2", 3, "What time ___ the film ___? (start)", [["does"], ["start"]],
  "Question: What time + does + subject + base verb.",
  [(r"starts", "After does we use the base verb: start, not starts.")])
T(S, "A2.2", 3, "Make a question with How: She goes to work by bus.", ["How does she go to work?", "How does she get to work?"],
  "Question: How + does + she + base verb. The -es goes away: goes becomes go.",
  [(r"\bgoes\b", "After does use the base verb: go, not goes.")])
M(S, "A2.2", 4, "Which sentence is NOT correct?", "Do they speaks English?",
  ["My sister never eats fish.", "He doesn't have a car.", "We usually go by bus."],
  "After do we need the base verb: Do they speak English?")
M(S, "A2.2", 5, "Your colleague says: 'He go to the gym on Mondays.' What is the best advice?",
  "Say 'He goes to the gym on Mondays.' Add -es for he, she, it.",
  ["Say 'He go to the gym on Mondays.' It is correct.", "Say 'He is go to the gym on Mondays.'", "Say 'He going to the gym on Mondays.'"],
  "With he, she, it the present simple verb takes -s or -es: he goes.")
W(S, "A2.2", 6, "Write a question to ask a new colleague about their free time. Start with Do you or What do you.",
  [(r"^\s*(do|what do|where do|when do|how often do|who do)\s+you\b", "Start with Do you ... or What do you ..."),
   (r"\?\s*$", "End the question with a question mark.")],
  "What do you usually do at the weekend?")

# B1.1
M(S, "B1.1", 1, "Which verb do we NOT usually use with -ing?", "know", ["run", "swim", "jump"],
  "Verbs of thinking, feeling and having (know, like, want, need, believe) are state verbs. We use the present simple: I know.")
M(S, "B1.1", 2, "Which sentence is a general truth (always true)?", "Water boils at 100 degrees.",
  ["The water is boiling now.", "The water boiled yesterday.", "I'm boiling water for tea."],
  "We use the present simple for facts and things that are always true.")
G(S, "B1.1", 3, "Our flight ___ at 6.40 tomorrow morning. (leave)", "leaves",
  "The present simple is used for timetables, even for the future: the flight leaves.")
T(S, "B1.1", 3, "Make it negative and use 'any': She has money.",
  ["She doesn't have any money.", "She does not have any money.", "She hasn't any money.", "She has not any money."],
  "Negative: doesn't + base verb. With 'any' for uncountable or plural nouns.")
M(S, "B1.1", 4, "Which sentence is NOT correct?", "I am liking this song.",
  ["The museum opens at nine.", "How much does it cost?", "He doesn't speak French."],
  "'Like' is a state verb. We say: I like this song.")
M(S, "B1.1", 5, "Your friend says: 'I'm wanting a coffee.' What is the best correction?",
  "'I want a coffee.' Want is a state verb, so we use the present simple.",
  ["'I'm wanting a coffee.' It is correct.", "'I wanted a coffee now.'", "'I am want a coffee.'"],
  "State verbs (want, need, like, know) are normally not used in the continuous.")
W(S, "B1.1", 6, "Write two sentences about your timetable for tomorrow (work or class). Use the present simple with a time.",
  [(r"\b(starts?|begins?|opens?|leaves?|ends?|finish(es)?|closes?|arrives?)\b.{0,40}\bat\s+\d", "Use a timetable verb (starts, finishes, leaves ...) with 'at' and a time."),
   (r"[.!?]\s+\S", "Write two sentences.")],
  "My class starts at 9.00. It finishes at 11.30.")

# ───────────────────────── PRESENT CONTINUOUS (active) ─────────────────────────
S = "present_continuous"

# A2.1
M(S, "A2.1", 1, "Look! The children ___ in the garden.", "are playing", ["play", "is playing", "plays"],
  "Right now: am/is/are + verb-ing. 'The children' = they, so are playing.")
M(S, "A2.1", 2, "Which sentence is happening right now?", "I'm cooking dinner.",
  ["I cook dinner every day.", "I cooked dinner yesterday.", "I will cook dinner tomorrow."],
  "The present continuous shows an action in progress now.")
G(S, "A2.1", 3, "Shh! The baby ___. (sleep)", "is sleeping",
  "Now: is + sleeping. The baby = it.",
  [(r"\bsleeps\b", "For an action happening now we use is + verb-ing: is sleeping.")])
G(S, "A2.1", 3, "She ___ in the park now. (run)", "is running",
  "Spelling: run becomes running (we double the n).",
  [(r"\bis runing\b", "Short verbs with one vowel + one consonant double the last letter: running.")])
M(S, "A2.1", 4, "Which sentence is NOT correct?", "They are play football.",
  ["He is watching TV.", "I am reading a book.", "We are having lunch."],
  "After are we need verb-ing: They are playing football.")
M(S, "A2.1", 5, "A friend is at the station and you ask about now. Which question is best?",
  "What are you doing now?", ["What do you do now?", "What you are doing now?", "What are you do now?"],
  "For right now we use are + you + verb-ing.")
W(S, "A2.1", 6, "Look around you. Write one sentence about what you are doing now. Start with I am.",
  [(r"\bi\s*(am|'m)\s+\w+ing\b", "Use I am (or I'm) + verb-ing, for example: I am sitting at my desk.")],
  "I am sitting at my desk.")

# A2.2
M(S, "A2.2", 1, "My brother ___ for an exam this week, so he is very busy.", "is studying", ["studies", "study", "studying"],
  "A temporary situation around now: am/is/are + verb-ing.")
M(S, "A2.2", 2, "Which sentence is about a plan for the future?", "I'm meeting Anna tomorrow at five.",
  ["I meet Anna every Friday.", "I met Anna yesterday.", "Anna is my friend."],
  "The present continuous with a future time word shows a fixed plan.")
G(S, "A2.2", 3, "What ___ you ___ this weekend? (do)", [["are"], ["doing"]],
  "Question: What + are + you + verb-ing.")
T(S, "A2.2", 3, "Make it negative: They are waiting for the bus.",
  ["They aren't waiting for the bus.", "They are not waiting for the bus."],
  "Negative: am/is/are + not + verb-ing.")
M(S, "A2.2", 4, "Which sentence is NOT correct?", "She is have a shower.",
  ["Are you coming to the party?", "We aren't working today.", "It is raining."],
  "After is we need verb-ing: She is having a shower.")
M(S, "A2.2", 5, "Your friend is in Riga for one month only. Which sentence is best?",
  "I'm living in a small flat this month.", ["I live in a small flat this month.", "I lived in a small flat this month.", "I will living in a small flat."],
  "The continuous shows a temporary situation.")
W(S, "A2.2", 6, "Write a question to ask a friend about their plans for tonight. Use Are you + verb-ing.",
  [(r"\bare\s+you\s+\w+ing\b", "Use Are you + verb-ing, for example: Are you going out tonight?"),
   (r"\?\s*$", "End the question with a question mark.")],
  "Are you going out tonight?")

# B1.1
M(S, "B1.1", 1, "Please be quiet. I ___ to concentrate.", "am trying", ["try", "tries", "trying"],
  "An action in progress at the moment of speaking: am + verb-ing.")
M(S, "B1.1", 2, "Which sentence describes a change that is happening now?", "The weather is getting colder.",
  ["The weather is cold in winter.", "It was cold yesterday.", "It gets cold in winter every year."],
  "We use the present continuous for changes in progress: getting colder, growing, rising.")
G(S, "B1.1", 3, "These days more people ___ from home. (work)", "are working",
  "A trend around now: are + verb-ing.")
T(S, "B1.1", 3, "Make a question with Why: He is shouting.", ["Why is he shouting?"],
  "Question word + is + subject + verb-ing.")
M(S, "B1.1", 4, "Which sentence is NOT correct?", "She is wanting a new phone.",
  ["I'm having a great time here.", "We're meeting at six.", "The prices are going up."],
  "'Want' is a state verb. We say: She wants a new phone.")
M(S, "B1.1", 5, "Is this statement true? 'I'm living with my parents at the moment' sounds more temporary than 'I live with my parents.'",
  "Yes. The continuous shows that the situation is temporary.",
  ["No. They mean exactly the same.", "No. Only 'live' can show a temporary situation.", "Yes, but only for children."],
  "The present continuous often shows that something is temporary or changing.")
W(S, "B1.1", 6, "Write one sentence about a change in your life or your city these days. Use the present continuous.",
  [(r"\b(am|is|are|'m|'s|'re)\s+\w+ing\b", "Use am/is/are + verb-ing."),
   (r"\b(these days|nowadays|at the moment|now|this year|more and more|lately)\b", "Add a time phrase such as these days or at the moment.")],
  "More people are working from home these days.")

# ───────────────────────── PAST SIMPLE (active) ─────────────────────────
S = "past_simple"

# A2.1
M(S, "A2.1", 1, "Yesterday I ___ to the cinema.", "went", ["go", "goed", "going"],
  "Go is irregular. The past form is went.")
M(S, "A2.1", 2, "Which sentence is about something finished in the past?", "We visited Rome last year.",
  ["We visit Rome every year.", "We are visiting Rome.", "We will visit Rome."],
  "'Last year' is a finished time. We use the past simple.")
G(S, "A2.1", 3, "She ___ TV last night. (not / watch)", ["didn't watch", "did not watch"],
  "Negative past simple: didn't + base verb.",
  [(r"didn't watched|did not watched", "After didn't we use the base verb: watch, not watched.")])
T(S, "A2.1", 3, "Make a question: He played football.", ["Did he play football?"],
  "Question: Did + subject + base verb.",
  [(r"\bplayed\b", "After did we use the base verb: play, not played.")])
M(S, "A2.1", 4, "Which sentence is NOT correct?", "I didn't went to school.",
  ["She visited her aunt.", "We watched a film.", "He had breakfast at 7."],
  "After didn't use the base verb: I didn't go to school.")
M(S, "A2.1", 5, "A friend writes: 'I buyed a new phone yesterday.' What is the best advice?",
  "Write 'I bought a new phone.' Buy is irregular: bought.",
  ["Write 'I buy a new phone yesterday.'", "Write 'I did bought a new phone.'", "The sentence is correct."],
  "Many common verbs are irregular. You must learn them: buy - bought, go - went, see - saw.")
W(S, "A2.1", 6, "Write one sentence about what you did yesterday. Use a past verb and the word yesterday.",
  [(r"\b(\w+ed|went|had|saw|did|made|took|got|came|ate|bought|met|read|wrote|drank|gave|found|was|were|slept|left)\b", "Use a verb in the past (for example: met, went, worked)."),
   (r"\byesterday\b", "Use the word yesterday.")],
  "Yesterday I met a friend for coffee.")

# A2.2
M(S, "A2.2", 1, "Where ___ you ___ last summer?", "did ... go", ["do ... went", "did ... went", "were ... go"],
  "Past simple questions: did + subject + base verb.")
M(S, "A2.2", 2, "Which words usually go with the past simple?", "yesterday, last week, three days ago",
  ["already, yet, just", "now, at the moment, these days", "always, usually, never"],
  "Finished time words (yesterday, last week, ago) go with the past simple.")
G(S, "A2.2", 3, "We ___ late because the bus ___ slow. (be)", [["were"], ["was"]],
  "Be in the past: I/he/she/it was, you/we/they were.")
G(S, "A2.2", 3, "He ___ at 7 and ___ a shower. (wake up / have)", [["woke up"], ["had"]],
  "Both verbs are irregular: wake - woke, have - had.")
M(S, "A2.2", 4, "Which sentence is NOT correct?", "Did you saw the match?",
  ["I met her two years ago.", "They didn't like the food.", "What did he say?"],
  "After did we use the base verb: Did you see the match?")
M(S, "A2.2", 5, "A colleague asks: 'What did you do at the weekend?' Which answer is best?",
  "I went hiking with my brother.", ["I go hiking with my brother.", "I am going hiking with my brother.", "I have gone hiking with my brother."],
  "The question is in the past simple, so we answer about a finished time with the past simple.")
W(S, "A2.2", 6, "Write two short sentences about your last holiday or day off. Use the past simple.",
  [(r"\b(was|were|went|had|saw|visited|stayed|ate|took|met|bought|\w+ed)\b", "Use verbs in the past simple (went, stayed, visited ...)."),
   (r"[.!?]\s+\S", "Write two sentences.")],
  "I went to the sea. We swam every day.")

# B1.1
M(S, "B1.1", 1, "Last year, they ___ married in Paris.", "got", ["get", "getting", "gotten"],
  "Get is irregular. The past simple form is got.")
M(S, "B1.1", 2, "Which sentence shows two actions, one after the other, in the past?", "She opened the door and walked in.",
  ["She was opening the door and walking in.", "She opens the door and walks in.", "She has opened the door and has walked in."],
  "We use the past simple for a series of finished actions in order.")
G(S, "B1.1", 3, "I ___ Tom at the party, so I called him later. (not / see)", ["didn't see", "did not see"],
  "Negative: didn't + base verb.")
T(S, "B1.1", 3, "Make a question with When: She moved to London.", ["When did she move to London?"],
  "Question word + did + subject + base verb.",
  [(r"\bmoved\b", "After did we use the base verb: move.")])
M(S, "B1.1", 4, "Which sentence is NOT correct?", "Why did you went home early?",
  ["I didn't have time yesterday.", "When did they arrive?", "She called me at six."],
  "After did we use the base verb: Why did you go home early?")
M(S, "B1.1", 5, "You want to say your report was finished in March. Which sentence is best?",
  "I finished it in March.", ["I have finished it in March.", "I am finishing it in March.", "I finish it in March."],
  "'In March' is a finished time, so we use the past simple, not the present perfect.")
W(S, "B1.1", 6, "Write two sentences that start a story. Say what happened first and what happened next (use Then or After that).",
  [(r"\b(then|after that|later|next)\b", "Use Then or After that to show the order."),
   (r"\b(\w+ed|went|had|saw|got|came|took|made|met|woke|was|were|left)\b", "Use verbs in the past simple.")],
  "I got up late. Then I missed the bus.")

# B1.2
M(S, "B1.2", 1, "Which sentence is correct?", "We used to play in the park every day.",
  ["We use to play in the park every day.", "We used to playing in the park every day.", "We were used to play in the park every day."],
  "Past habits: used to + base verb.")
M(S, "B1.2", 2, "What does 'I used to smoke' tell us?", "I smoked in the past, but I don't smoke now.",
  ["I smoke now, but not very often.", "I am starting to smoke.", "I will smoke in the future."],
  "Used to talks about past habits or states that are no longer true.")
G(S, "B1.2", 3, "Did you ___ to live in a flat? (use)", "use",
  "In questions and negatives we write 'use to' (not 'used to'): Did you use to ...?")
G(S, "B1.2", 3, "He ___ to like fish, but now he loves it. (not / use)", ["didn't use", "did not use"],
  "Negative: didn't use to + base verb.")
M(S, "B1.2", 4, "Which sentence is NOT correct?", "I didn't used to like coffee.",
  ["She used to live in Paris.", "Did you use to play chess?", "They used to work here."],
  "After didn't we write 'use to': I didn't use to like coffee.")
M(S, "B1.2", 5, "Which sentence is best to talk about a repeated habit in the past?",
  "As a child, I used to visit my grandparents every summer.",
  ["As a child, I visited my grandparents last summer.", "As a child, I am visiting my grandparents every summer.", "As a child, I have visited my grandparents every summer."],
  "'Used to' + 'every summer' shows a repeated past habit.")
W(S, "B1.2", 6, "Write one sentence about something you used to do as a child, but don't do now.",
  [(r"\bused\s+to\s+\w+", "Use used to + base verb."),
   (r"\b(but|now|no longer|any more|anymore)\b", "Add but ... now ... to show it has changed.")],
  "I used to collect stickers, but I don't collect them now.")
