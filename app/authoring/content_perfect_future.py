from dsl import M, G, T, O, W

# ───────────────────────── PAST CONTINUOUS ─────────────────────────
S = "past_continuous"

# A2.2
M(S, "A2.2", 1, "At 8 o'clock yesterday I ___ dinner.", "was cooking", ["cooked", "am cooking", "were cooking"],
  "An action in progress at a moment in the past: was/were + verb-ing.")
M(S, "A2.2", 2, "Which sentence shows an action in progress at a moment in the past?", "At nine, she was reading in bed.",
  ["At nine, she reads in bed.", "At nine, she read the book.", "At nine, she has read in bed."],
  "'At nine' is a moment in the past. The past continuous shows what was in progress then.")
G(S, "A2.2", 3, "They ___ TV when I arrived. (watch)", "were watching",
  "They = were + verb-ing.",
  [(r"\bwas watching\b", "'They' needs were, not was.")])
G(S, "A2.2", 3, "___ you ___ at 6 pm? (work)", [["Were"], ["working"]],
  "Question: Were + you + verb-ing.")
M(S, "A2.2", 4, "Which sentence is NOT correct?", "I was watch TV.",
  ["He was sleeping.", "They were playing.", "We weren't listening."],
  "After was/were we need verb-ing: I was watching TV.")
M(S, "A2.2", 5, "A friend asks: 'What were you doing at midnight?' Which answer is best?",
  "I was sleeping.", ["I sleep.", "I am sleeping.", "I have slept."],
  "The question uses the past continuous, so the answer also describes what was in progress.")
W(S, "A2.2", 6, "Write a sentence about what you were doing at 7 pm yesterday. Use was/were + verb-ing.",
  [(r"\b(was|were)\s+\w+ing\b", "Use was or were + verb-ing, for example: I was cooking dinner.")],
  "At 7 pm yesterday, I was cooking dinner.")

# B1.1
M(S, "B1.1", 1, "I ___ along the street when I saw an old friend.", "was walking", ["walked", "am walking", "were walking"],
  "A longer action in progress (was walking) is interrupted by a short action (saw).")
M(S, "B1.1", 2, "In 'When Mia called, I was cooking', which action started first?",
  "Cooking. It was already in progress.", ["Calling.", "Both at the same moment.", "We cannot know."],
  "The past continuous action was already happening when the short action (called) happened.")
G(S, "B1.1", 3, "While she ___, her phone ___. (drive / ring)", [["was driving"], ["rang"]],
  "Long action: was driving. Short action that interrupts: rang.")
G(S, "B1.1", 3, "It ___ when we left the house, so we took umbrellas. (rain)", "was raining",
  "The background situation is in progress: was raining.")
M(S, "B1.1", 4, "Which sentence is NOT correct?", "When I was a child, I was playing in the park every day.",
  ["When I arrived, they were having lunch.", "While I was reading, he was watching TV.", "She was cooking when the lights went out."],
  "Repeated actions in the past use the past simple (or used to), not the past continuous: I played in the park every day.")
M(S, "B1.1", 5, "You tell a story: 'I was walking home. Suddenly a dog ___ out of the garden.' Which form is best?",
  "ran", ["was running", "runs", "has run"],
  "A sudden, short action that interrupts uses the past simple.")
W(S, "B1.1", 6, "Write one sentence with 'when' about something that interrupted you. Use the past continuous and the past simple.",
  [(r"\b(was|were)\s+\w+ing\b", "Use was/were + verb-ing for the longer action."),
   (r"\bwhen\b", "Use the word when."),
   (r"\b(\w+ed|rang|came|saw|heard|started|arrived|called|stopped|broke|fell|went|got)\b", "Use the past simple for the short action (rang, arrived, called ...).")],
  "I was cooking dinner when my friend called.")

# B1.2
M(S, "B1.2", 1, "Choose the correct form: I ___ to call you, but my phone died.", "was going", ["went", "am going", "have gone"],
  "Was/were going to + base verb = a plan in the past that did not happen.")
M(S, "B1.2", 2, "What does 'I was going to call you' mean?", "I planned to call you, but I didn't.",
  ["I called you.", "I am going to call you now.", "I never wanted to call you."],
  "Was going to shows an intention in the past that was not completed.")
G(S, "B1.2", 3, "Sorry, I ___ to answer your email, but I was very busy. (go)", "was going",
  "Plan in the past: was going to + base verb.")
G(S, "B1.2", 3, "While the guests ___, the band ___ quiet music. (arrive / play)", [["were arriving"], ["was playing"]],
  "Two actions in progress at the same time: while + past continuous, past continuous.")
M(S, "B1.2", 4, "Which sentence is NOT correct?", "They was going to meet us, but they were late.",
  ["I was going to call you, but I lost your number.", "She was going to leave when he arrived.", "We were going to stay longer."],
  "They needs were: They were going to meet us.")
M(S, "B1.2", 5, "Which sentence best describes a plan that did not happen?",
  "We were going to travel to Italy, but we cancelled.", ["We are going to travel to Italy, but we cancelled.", "We travel to Italy, but we cancelled.", "We have travelled to Italy, but we cancelled."],
  "Past tense + but shows the plan changed: were going to.")
W(S, "B1.2", 6, "Write a sentence about a plan you had but did not do. Use was/were going to and but.",
  [(r"\b(was|were)\s+going\s+to\s+\w+", "Use was/were going to + base verb."),
   (r"\bbut\b", "Use the word but to say what happened instead.")],
  "I was going to go to the gym, but I was too tired.")

# ───────────────────────── PRESENT PERFECT ─────────────────────────
S = "present_perfect"

# A2.2
M(S, "A2.2", 1, "I have never ___ sushi.", "eaten", ["ate", "eat", "eating"],
  "Present perfect = have/has + past participle. The past participle of eat is eaten.")
M(S, "A2.2", 2, "Which sentence is about life experience (no exact time)?", "I've been to Spain.",
  ["I went to Spain in 2019.", "I'm going to Spain.", "I go to Spain every year."],
  "We use the present perfect for experiences up to now when the time is not important.")
G(S, "A2.2", 3, "She ___ her homework. (just / finish)", ["has just finished"],
  "Just goes between has/have and the past participle: has just finished.",
  [(r"has just finish\b", "After has we need the past participle: finished.")])
G(S, "A2.2", 3, "I haven't ___ her yet. (call)", "called",
  "Negative: haven't + past participle. 'Yet' goes with the present perfect.")
M(S, "A2.2", 4, "Which sentence is NOT correct?", "I have went to London twice.",
  ["She has lived here for years.", "Have you ever tried Thai food?", "We haven't seen that film yet."],
  "The past participle of go is gone (or been for visits): I have been to London twice.")
M(S, "A2.2", 5, "Which is the best short answer to: 'Have you ever been to Rome?'",
  "Yes, I have.", ["Yes, I did.", "Yes, I do.", "Yes, I am."],
  "Short answers repeat the helper verb of the question: Have you ...? Yes, I have.")
W(S, "A2.2", 6, "Write one sentence about something you have never done but would like to do. Use I have never.",
  [(r"\bi\s*(have|'ve)\s+never\s+\w+", "Use I have never + past participle, for example: I have never been to Japan.")],
  "I have never been to Japan.")

# B1.1
M(S, "B1.1", 1, "I've worked here ___ five years.", "for", ["since", "from", "ago"],
  "Use for + a period of time (five years). Use since + a starting point (2020).")
M(S, "B1.1", 2, "Which sentence means: it started in the past and is still true now?", "I have known Tom for ten years.",
  ["I knew Tom ten years ago.", "I know Tom ten years.", "I did know Tom for ten years."],
  "The present perfect with for/since connects the past with now.")
G(S, "B1.1", 3, "They ___ married for 20 years. (be)", "have been",
  "Unfinished period: have been + for 20 years.",
  [(r"\bare\b|\bwere\b", "With for/since and a situation that continues, use the present perfect: have been.")])
T(S, "B1.1", 3, "Make a question with How long: She has worked here since June.", ["How long has she worked here?"],
  "How long + has + subject + past participle.")
M(S, "B1.1", 4, "Which sentence is NOT correct?", "I have seen him yesterday.",
  ["She has lived here since 2015.", "We have known each other for years.", "Have you finished yet?"],
  "'Yesterday' is a finished time. Use the past simple: I saw him yesterday.")
M(S, "B1.1", 5, "Compare 'I lost my keys' and 'I've lost my keys'. Which one tells us the problem is still there now?",
  "I've lost my keys.", ["I lost my keys.", "Both tell us the same.", "Neither tells us this."],
  "The present perfect connects the past action with the result now.")
W(S, "B1.1", 6, "Write two sentences about how long you have lived in your city or worked in your job. Use for in one and since in the other.",
  [(r"\b(have|has|'ve)\s+\w+", "Use have/has + past participle."),
   (r"\bfor\s+\w+", "Use for + a period of time."),
   (r"\bsince\s+\w+", "Use since + a start time.")],
  "I have lived in Riga for ten years. I have worked here since 2020.")

# B1.2
M(S, "B1.2", 1, "It's the first time I ___ this dish.", "have tried", ["tried", "try", "am trying"],
  "After 'It's the first time' we use the present perfect.")
M(S, "B1.2", 2, "Which sentence has a finished time word, so we must use the past simple?", "I saw the film last night.",
  ["I've seen the film already.", "I've seen the film this week.", "I've seen the film twice."],
  "'Last night' is finished, so past simple. Without a finished time we can use the present perfect.")
G(S, "B1.2", 3, "How long ___ you ___ English? (study)", [["have"], ["studied", "been studying"]],
  "How long + have + you + past participle (or been + verb-ing).")
G(S, "B1.2", 3, "I ___ in three countries, so I speak a little of each language. (live)", "have lived",
  "Life experience up to now: have + past participle.")
M(S, "B1.2", 4, "Which sentence is NOT correct?", "I have visited Paris in 2018.",
  ["She has just left.", "I've known him since 2015.", "Have you ever been to Italy?"],
  "'In 2018' is a finished time. Use the past simple: I visited Paris in 2018.")
M(S, "B1.2", 5, "A colleague writes: 'I have sent the email yesterday.' Which comment is best?",
  "Use the past simple because 'yesterday' is finished: I sent the email yesterday.",
  ["It is correct. Do not change it.", "Use the future: I will send the email yesterday.", "Use the past continuous: I was sending the email yesterday."],
  "Finished time words (yesterday, last week, in 2018) need the past simple.")
W(S, "B1.2", 6, "Write two sentences: one present perfect about a place you have visited, and one past simple with the time you went.",
  [(r"\b(have|has|'ve)\s+(\w+ed|been|seen|visited|gone|done|taken|stayed)\b", "Use the present perfect in the first sentence (have been ...)."),
   (r"\b(in\s+\d{4}|last\s+\w+|\w+\s+years?\s+ago|yesterday|when I)\b", "Give a finished time in the second sentence (in 2022, last year, two years ago).")],
  "I have been to Lisbon. I went there in 2022.")

# ───────────────────────── PRESENT PERFECT CONTINUOUS ─────────────────────────
S = "present_perfect_continuous"

# B1.1
M(S, "B1.1", 1, "I'm tired. I ___ all day.", "have been working", ["worked", "am working", "was working"],
  "Present perfect continuous = have/has been + verb-ing. It shows an activity over a period up to now.")
M(S, "B1.1", 2, "What does 'I've been waiting for an hour' tell us?", "I started waiting an hour ago. I am still waiting (or I have just stopped).",
  ["I waited for one hour last week.", "I will wait for an hour.", "I never wait."],
  "The present perfect continuous shows how long an activity has been happening up to now.")
G(S, "B1.1", 3, "She ___ Spanish for six months. (learn)", "has been learning",
  "She + has been + verb-ing.")
T(S, "B1.1", 3, "Make a question with How long: They have been waiting.", ["How long have they been waiting?"],
  "How long + have + subject + been + verb-ing.")
M(S, "B1.1", 4, "Which sentence is NOT correct?", "I have been knowing him for years.",
  ["She has been working here since March.", "It has been raining all day.", "How long have you been learning English?"],
  "'Know' is a state verb. We say: I have known him for years.")
M(S, "B1.1", 5, "Your friend is out of breath because she was running until a minute ago. Which sentence explains why?",
  "I've been running.", ["I run.", "I will run.", "I ran yesterday."],
  "We use the present perfect continuous to explain a present situation by a recent activity.")
W(S, "B1.1", 6, "Write one sentence about something you have been doing a lot lately.",
  [(r"\b(have|has|'ve)\s+been\s+\w+ing\b", "Use have/has been + verb-ing, for example: I have been studying a lot.")],
  "I have been studying a lot lately.")

# B1.2
M(S, "B1.2", 1, "I ___ this book for two weeks, and I'm still reading it.", "have been reading", ["read", "have read", "am reading"],
  "An activity that started in the past and is still in progress: have been + verb-ing.")
M(S, "B1.2", 2, "Which sentence focuses on the result or number (not the activity)?", "I've written five emails.",
  ["I've been writing emails.", "I've been writing for an hour.", "I've been writing all morning."],
  "Present perfect simple = result or number. Present perfect continuous = the activity and its duration.")
G(S, "B1.2", 3, "Look at the floor! The children ___ with paint. (play)", "have been playing",
  "A recent activity with a visible result: have been playing.")
G(S, "B1.2", 3, "I ___ this book all week. I ___ three chapters. (read / finish)", [["have been reading"], ["have finished"]],
  "Activity over time: have been reading. Completed result: have finished.")
M(S, "B1.2", 4, "Which sentence is NOT correct?", "I've been writing five emails today.",
  ["She has been working here since March.", "How long have you been living here?", "They have been talking for hours."],
  "With an exact number we use the present perfect simple: I've written five emails today.")
M(S, "B1.2", 5, "Your boss asks why you look tired. You were in traffic for an hour until now. Which answer is best?",
  "I've been sitting in traffic for an hour.", ["I sit in traffic for an hour.", "I will sit in traffic for an hour.", "I sat in traffic tomorrow."],
  "A recent, continuing activity that explains the present: present perfect continuous.")
W(S, "B1.2", 6, "Write two sentences: one present perfect continuous about an activity, one present perfect simple about a result.",
  [(r"\b(have|has|'ve)\s+been\s+\w+ing\b", "Use have/has been + verb-ing in one sentence."),
   (r"\b(have|has|'ve)\s+(?!been\b)\w+", "Use have/has + past participle in the other sentence.")],
  "I've been studying all week. I've finished two units.")

# ───────────────────────── PAST PERFECT ─────────────────────────
S = "past_perfect"

# B1.2
M(S, "B1.2", 1, "When we arrived, the film ___ already ___.", "had ... started", ["has ... started", "was ... starting", "did ... start"],
  "Past perfect = had + past participle. It shows an earlier past action.")
M(S, "B1.2", 2, "In 'When I got to the station, the train had left', which happened first?", "The train left.",
  ["I got to the station.", "They happened at the same time.", "We cannot know."],
  "The past perfect (had left) is the earlier action.")
G(S, "B1.2", 3, "She was upset because she ___ her phone. (lose)", "had lost",
  "The reason came before the feeling: had + past participle.")
G(S, "B1.2", 3, "By the time I called, he ___ out. (already / go)", "had already gone",
  "Already goes between had and the past participle: had already gone.")
T(S, "B1.2", 3, "Join with After: I finished work. Then I went home.",
  ["After I had finished work, I went home.", "I went home after I had finished work."],
  "After + past perfect (earlier action), past simple (later action).")
M(S, "B1.2", 4, "Which sentence is NOT correct?", "When I arrived, she already has left.",
  ["When I arrived, she had already left.", "I had never seen snow before that day.", "He told me that he had lost his keys."],
  "For an earlier past action use had + past participle: she had already left.")
M(S, "B1.2", 5, "Tom arrived at 9. The meeting started at 8.30. Which sentence is correct?",
  "When Tom arrived, the meeting had already started.",
  ["When Tom arrived, the meeting has already started.", "When Tom arrived, the meeting would already start.", "When Tom arrived, the meeting is already started."],
  "The meeting started before Tom arrived, so we use the past perfect for the meeting.")
W(S, "B1.2", 6, "Write one sentence about something that had already happened when you arrived somewhere. Use When I arrived and had already.",
  [(r"\bhad\s+already\s+\w+", "Use had already + past participle."),
   (r"\bwhen\b|\bby the time\b", "Use When I arrived ... or By the time ...")],
  "When I arrived, the film had already started.")

# ───────────────────────── FUTURE FORMS ─────────────────────────
S = "future"

# A2.1
M(S, "A2.1", 1, "I am ___ to visit my grandmother tomorrow.", "going", ["go", "goes", "went"],
  "Plans: am / is / are + going to + base verb.")
M(S, "A2.1", 2, "Which sentence is about the future?", "We are going to eat out tonight.",
  ["We ate out last night.", "We always eat at home.", "We are eating now."],
  "Going to + base verb talks about a plan for the future.")
G(S, "A2.1", 3, "Tom ___ a party on Saturday. (have)", "is going to have",
  "A plan: is going to + base verb.",
  [(r"\bis going to has\b", "After going to we use the base verb: have, not has.")])
G(S, "A2.1", 3, "It's cold. I ___ my coat. (take)", ["'ll take", "will take"],
  "A quick decision now: will + base verb.")
T(S, "A2.1", 3, "Make a question: You are going to travel by train.", ["Are you going to travel by train?"],
  "Question: Are + you + going to + base verb?")
M(S, "A2.1", 4, "Which sentence is NOT correct?", "I going to buy a bike.",
  ["She is going to cook.", "We are going to swim.", "They are going to play."],
  "We need am / is / are before going to: I am going to buy a bike.")
M(S, "A2.1", 5, "A friend asks: 'What are you going to do at the weekend?' Which answer is best?",
  "I'm going to visit my parents.", ["I visited my parents.", "I visit my parents every day.", "I am visit my parents."],
  "The question is about a future plan, so we answer with going to.")
W(S, "A2.1", 6, "Write one sentence about your plan for tomorrow. Use I am going to.",
  [(r"\b(i am|i'm)\s+going\s+to\s+\w+", "Use I am going to + base verb, for example: I'm going to visit a friend.")],
  "I'm going to visit a friend tomorrow.")

# A2.2
M(S, "A2.2", 1, "Look at those clouds! It ___ rain.", "is going to", ["will to", "goes to", "is going"],
  "Going to is used for predictions based on what we can see now: is going to + base verb.")
M(S, "A2.2", 2, "Which sentence is a plan we made before now?", "I'm going to start a new course in March.",
  ["I'll carry your bag.", "I think prices will go up.", "OK, I'll answer the phone."],
  "Going to shows a plan or intention made before speaking.")
G(S, "A2.2", 3, "The phone is ringing. - I ___ it. (answer)", ["'ll answer", "will answer"],
  "A decision at the moment of speaking: will + base verb.")
G(S, "A2.2", 3, "We ___ to Rome next month. We've already bought the tickets. (go)", ["are going", "are going to go"],
  "A plan already arranged: are going (to).")
M(S, "A2.2", 4, "Which sentence is NOT correct?", "I will to help you.",
  ["I'm going to visit my aunt next week.", "It will be sunny tomorrow.", "She is going to have a baby."],
  "After will we use the base verb without 'to': I will help you.")
M(S, "A2.2", 5, "Black clouds are in the sky. Which sentence is best?", "It's going to rain.",
  ["It will rain.", "It rains.", "It rained."],
  "When we see evidence now, going to is the natural choice.")
W(S, "A2.2", 6, "Write a sentence about your plan for next weekend. Use going to.",
  [(r"\b(am|'m|is|are|'s|'re)\s+going\s+to\s+\w+", "Use am/is/are going to + base verb.")],
  "I'm going to visit my parents next weekend.")

# B1.1
M(S, "B1.1", 1, "If it ___ tomorrow, we will stay at home.", "rains", ["will rain", "is raining", "rain"],
  "After if, when and as soon as we use the present simple for the future.")
M(S, "B1.1", 2, "Which sentence is an arrangement (fixed time and place in your diary)?", "I'm seeing the dentist at 3 pm on Friday.",
  ["I'll see the dentist someday.", "I will probably see the dentist.", "The dentist is nice."],
  "The present continuous with a time shows a fixed arrangement.")
G(S, "B1.1", 3, "I'll call you when I ___ home. (get)", "get",
  "After when we use the present simple, not will.",
  [(r"\bwill get\b|\b'll get\b", "After when we use the present simple: when I get home.")])
G(S, "B1.1", 3, "Wait! I ___ you with that bag. (help)", ["'ll help", "will help"],
  "An offer at the moment of speaking: will + base verb.")
T(S, "B1.1", 3, "Rewrite with going to: I plan to buy a car.", ["I'm going to buy a car.", "I am going to buy a car."],
  "Going to shows a plan: am going to + base verb.")
M(S, "B1.1", 4, "Which sentence is NOT correct?", "I'll call you when I will arrive.",
  ["We're flying to Rome on Monday.", "I think it'll be a great trip.", "As soon as he arrives, we will start."],
  "In time clauses (when, as soon as, before) use the present simple: when I arrive.")
M(S, "B1.1", 5, "Your friend says: 'I will meet Anna at 6, we agreed yesterday.' Which form sounds more natural for an arrangement?",
  "I'm meeting Anna at 6.", ["I meet Anna at 6 yesterday.", "I met Anna at 6 tomorrow.", "I'm going to be met Anna at 6."],
  "For arrangements with a time we often use the present continuous.")
W(S, "B1.1", 6, "Write a sentence with when or as soon as about what you will do after class or work.",
  [(r"\b(when|as soon as|after|before|until)\b", "Use when, as soon as, after or before."),
   (r"\b(will|'ll|am going to|'m going to)\s+\w+", "Use will or going to for the later action.")],
  "As soon as I finish work, I'll go to the gym.")

# B1.2
M(S, "B1.2", 1, "Hurry up! The film ___ to start.", "is about", ["is for", "goes", "will"],
  "Be about to + base verb = very soon.")
M(S, "B1.2", 2, "Which sentence means something will happen very soon?", "The plane is about to take off.",
  ["The plane takes off every day.", "The plane took off.", "The plane has been taking off."],
  "Be about to is used for the very near future.")
G(S, "B1.2", 3, "Don't worry. I ___ anyone your secret. (not / tell)", ["won't tell", "will not tell"],
  "A promise: will / won't + base verb.")
G(S, "B1.2", 3, "Be careful! You ___ off that chair! (fall)", "are going to fall",
  "We can see it is about to happen: are going to + base verb.")
M(S, "B1.2", 4, "Which sentence is NOT correct?", "He is going to be arrive soon.",
  ["She is about to leave.", "Will you help me?", "It's going to rain; look at the sky."],
  "After going to we use the base verb: He is going to arrive soon.")
M(S, "B1.2", 5, "You see a colleague with heavy boxes. What is the best offer?", "I'll carry one of those for you.",
  ["I carry one of those for you.", "I'm carrying one of those for you.", "I carried one of those for you."],
  "Will is the natural choice for a spontaneous offer.")
W(S, "B1.2", 6, "Write two sentences: one prediction with going to (with a reason) and one spontaneous offer with will.",
  [(r"\bgoing\s+to\s+\w+", "Use going to + base verb in the prediction."),
   (r"\b(i'll|i will|shall i)\b", "Use I'll or I will for the offer.")],
  "It's going to rain; look at the clouds. I'll bring an umbrella for you.")
