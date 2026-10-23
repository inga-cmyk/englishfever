from lib import *
import b1_topics
italics.LV_ASCII |= b1_topics.LV_WORDS
B = dict(mcq_b=3, text_b=4, match_b=3)

# ============ Question tags (A2.2 / B1.1 / B1.2) ============
P = Topic("Question tags", **B,
    order=("Positive sentence + negative tag. Negative sentence + positive tag. The tag repeats the auxiliary.", "Apgalvojošs teikums + nolieguma tag, noliegts teikums + apgalvojošs tag. Tag atkārto palīgdarbības vārdu."),
    bank=("The tag repeats the auxiliary and changes positive to negative (or negative to positive): *You like tea, don't you?*", "Tag atkārto palīgdarbības vārdu un maina apgalvojumu uz noliegumu (vai otrādi): *You like tea, don't you?*"),
    gap=("The tag repeats the auxiliary and changes positive to negative (or negative to positive).", "Tag atkārto palīgdarbības vārdu un maina apgalvojumu uz noliegumu (vai otrādi)."),
    text=("Add a tag: the same auxiliary and subject (*it, she, they*), the opposite meaning. Present Simple: *do / does*. Past Simple: *did*.", "Pievieno tag: tas pats palīgdarbības vārds un teik. priekšmets (*it, she, they*), pretējs apgalvojums. Present Simple: *do / does*. Past Simple: *did*."),
    mcq=("The tag repeats the auxiliary and changes positive to negative (or negative to positive): *You like tea, don't you?*", "Tag atkārto palīgdarbības vārdu un maina apgalvojumu uz noliegumu (vai otrādi): *You like tea, don't you?*"),
    match=("The tag matches the auxiliary and the subject of the sentence.", "Tag atbilst teikuma palīgdarbības vārdam un teik. priekšmetam."))
for s, l in [("you are from latvia aren't you", "A2.2"), ("she can swim can't she", "A2.2"), ("they live here don't they", "A2.2"),
             ("you haven't seen my keys have you", "B1.1"), ("let's go for a walk shall we", "B1.1"), ("she wasn't at the meeting was she", "B1.1"),
             ("you wouldn't mind waiting a few minutes would you", "B1.2"), ("nobody told her about the change did they", "B1.2"), ("there is a problem with the printer isn't there", "B1.2")]:
    P.order(l, s)
P.bank("A2.2", "It's cold today, ___ it?", "isn't", ["doesn't", "aren't"])
P.bank("A2.2", "You don't like coffee, ___ you?", "do", ["does", "are"])
P.bank("B1.1", "You've finished, ___ you?", "haven't", ["don't", "aren't"])
P.bank("B1.1", "She wasn't late, ___ she?", "was", ["did", "is"])
P.bank("B1.1", "Open the window, ___ you?", "will", ["do", "are"])
P.bank("B1.2", "He ought to apologise, ___ he?", "shouldn't", ["doesn't", "isn't"])
P.bank("B1.2", "She used to live here, ___ she?", "didn't", ["doesn't", "wasn't"])
P.bank("B1.2", "Let's not argue, ___ we?", "shall", ["will", "do"])
P.gap("A2.2", "Your sister can drive, ___ she?", "can't")
P.gap("A2.2", "They went to school, ___ they?", "didn't")
P.gap("B1.1", "We should leave soon, ___ we?", "shouldn't")
P.gap("B1.1", "He had left already, ___ he?", "hadn't")
P.gap("B1.1", "You don't know her, ___ you?", "do")
P.gap("B1.2", "You wouldn't mind waiting, ___ you?", "would")
P.gap("B1.2", "I'm not late, ___ I?", "am")
P.gap("B1.2", "Somebody has left a bag here, ___ they?", "haven't | have not")
P.mcq("A2.2", "Choose the correct option: You are a student, ___ ?", "aren't you", ["don't you", "isn't you", "aren't I"])
P.mcq("A2.2", "Choose the correct option: She likes pizza, ___ ?", "doesn't she", ["isn't she", "doesn't it", "don't she"])
P.mcq("A2.2", "Choose the correct option: They aren't here, ___ ?", "are they", ["do they", "is they", "are them"])
P.mcq("A2.2", "Choose the correct option: We can swim here, ___ ?", "can't we", ["don't we", "aren't we", "won't we"])
P.mcq("B1.1", "Choose the correct option: He hasn't called, ___ ?", "has he", ["does he", "did he", "is he"])
P.mcq("B1.1", "Choose the correct option: You'll help me, ___ ?", "won't you", ["don't you", "aren't you", "haven't you"])
P.mcq("B1.1", "Choose the correct option: Let's go to the cinema, ___ ?", "shall we", ["will we", "do we", "don't we"])
P.mcq("B1.1", "Choose the correct option: I'm right, ___ ?", "aren't I", ["amn't I", "am not I", "isn't I"])
P.mcq("B1.1", "At a party: which sentence is NOT correct?", "You went to the party, weren't you?", ["You went to the party, didn't you?", "You were at the party, weren't you?", "You haven't been there, have you?"], b=4)
P.mcq("B1.1", "Which sentence is correct?", "Nobody called, did they?", ["Nobody called, did it?", "Nobody called, do they?", "Nobody called, are they?"], b=3)
P.mcq("B1.2", "In an office: which sentence has the correct tag?", "There is a problem, isn't there?", ["There is a problem, isn't it?", "There is a problem, doesn't there?", "There is a problem, aren't there?"], b=3)
P.mcq("B1.2", "Choose the correct option: Everyone enjoyed the film, ___ ?", "didn't they", ["didn't he", "didn't it", "weren't they"])
P.mcq("B1.2", "Choose the correct option: You've never been to Japan, ___ ?", "have you", ["did you", "are you", "do you"])
P.mcq("B1.2", "In a letter: which sentence is NOT correct?", "He ought to apologise, doesn't he?", ["He ought to apologise, shouldn't he?", "You'd better hurry, hadn't you?", "She used to live here, didn't she?"], b=4)
P.mcq("B1.2", "Choose the correct option: Nobody likes being ignored, ___ ?", "do they", ["does it", "are they", "has it"])
P.text("A2.2", "Add a question tag: You like tea.", ["You like tea, don't you?"], b=3)
P.text("A2.2", "Add a question tag: She is tired.", ["She is tired, isn't she?", "She's tired, isn't she?"], b=3)
P.text("B1.1", "Add a question tag: You haven't seen Tom.", ["You haven't seen Tom, have you?"], b=4)
P.text("B1.1", "Add a question tag: Let's have lunch.", ["Let's have lunch, shall we?"], b=4)
P.text("B1.2", "Add a question tag: Nobody has called.", ["Nobody has called, have they?"], b=4)
P.text("B1.2", "Add a question tag: There's a problem.", ["There's a problem, isn't there?", "There is a problem, isn't there?"], b=4)
P.match("A2.2", "Match each sentence with its tag.", [("You are happy,", "aren't you?"), ("She likes tea,", "doesn't she?"), ("They can swim,", "can't they?"), ("We went home,", "didn't we?")])
P.match("B1.1", "Match each short sentence with its tag.", [("I am late,", "aren't I?"), ("Let's start,", "shall we?"), ("Close the door,", "will you?"), ("Nobody came,", "did they?")])
P.match("B1.2", "Match each pattern with its meaning.", [("falling voice on the tag", "you expect agreement"), ("rising voice on the tag", "you really ask"), ("positive sentence", "negative tag"), ("negative sentence", "positive tag")])

# ============ Subject and object questions (A2.2 / B1.1 / B1.2) ============
P = Topic("Subject and object questions", **B,
    order=("Subject question: question word + verb. Object question: question word + *did / does* + subject + verb.", "Jautājums par teikuma priekšmetu: jautājamais vārds + darbības vārds. Jautājums par papildinātāju: jautājamais vārds + *did / does* + teik. priekšmets + darbības vārds."),
    bank=("Subject question (*Who called?*): no *did / does*. Object question (*Who did you call?*): *did / does* + subject + base verb.", "Jautājums par teikuma priekšmetu (*Who called?*): bez *did / does*. Jautājums par papildinātāju (*Who did you call?*): *did / does* + teik. priekšmets + pamatforma."),
    gap=("Subject question (*Who called?*): no *did / does*. Object question (*Who did you call?*): *did / does* + subject + base verb.", "Jautājums par teikuma priekšmetu (*Who called?*): bez *did / does*. Jautājums par papildinātāju (*Who did you call?*): *did / does* + teik. priekšmets + pamatforma."),
    text=("Ask about the subject: question word + verb. Ask about the object: question word + *did / does* + subject + base verb.", "Jautājums par teikuma priekšmetu: jautājamais vārds + darbības vārds. Jautājums par papildinātāju: jautājamais vārds + *did / does* + teik. priekšmets + pamatforma."),
    mcq=("Subject question (*Who called?*): no *did / does*. Object question (*Who did you call?*): *did / does* + subject + base verb.", "Jautājums par teikuma priekšmetu (*Who called?*): bez *did / does*. Jautājums par papildinātāju (*Who did you call?*): *did / does* + teik. priekšmets + pamatforma."),
    match=("If the question word is the subject, there is no *did / does*.", "Ja jautājamais vārds ir teik. priekšmets, nav *did / does*."))
for s, l in [("who wrote this email", "A2.2"), ("what did you buy at the market", "A2.2"), ("who lives next door to you", "A2.2"),
             ("who left the door open last night", "B1.1"), ("what did you say to the manager", "B1.1"), ("which team won the match yesterday", "B1.1"),
             ("who did you give the tickets to", "B1.2"), ("which of these companies did you apply to last year", "B1.2")]:
    P.order(l, s)
P.bank("A2.2", "Who ___ the window? Sam broke it.", "broke", ["did broke", "broken"])
P.bank("A2.2", "What ___ you do last night?", "did", ["does", "do"])
P.bank("B1.1", "___ phoned you this morning?", "Who", ["Who did", "What did"])
P.bank("B1.1", "What ___ your sister buy at the shop yesterday?", "did", ["does", "do"])
P.bank("B1.1", "Who ___ this beautiful picture? Picasso painted it.", "painted", ["did painted", "painting"])
P.bank("B1.2", "Who ___ you to the party? Sam invited me.", "invited", ["did invited", "invite"])
P.bank("B1.2", "Who ___ she live with?", "does", ["do", "is"])
P.bank("B1.2", "What ___ to the old cinema last year?", "happened", ["did happened", "happens"])
P.gap("A2.2", "___ called you? Anna called me.", "Who")
P.gap("A2.2", "___ did she meet? She met Tom.", "Who | Whom")
P.gap("B1.1", "Who ___ the last piece of cake? (eat)", "ate")
P.gap("B1.1", "What ___ you eat for dinner last night?", "did")
P.gap("B1.1", "Who ___ you invite to the party? (Tom)", "did")
P.gap("B1.2", "Who ___ to the cinema with? (you / go)", "did you go")
P.gap("B1.2", "How many students ___ the exam last year? (pass)", "passed")
P.mcq("A2.2", "Tom called Anna. Which question asks about Tom?", "Who called Anna?", ["Who did Tom call?", "Who did call Anna?", "Who Tom called?"])
P.mcq("A2.2", "Tom called Anna. Which question asks about Anna?", "Who did Tom call?", ["Who called Anna?", "Who Tom called?", "Who Tom did call?"])
P.mcq("A2.2", "Choose the correct option: ___ lives in this house?", "Who", ["Who does", "What does", "Which do"])
P.mcq("A2.2", "Choose the correct option: What ___ you want for lunch?", "do", ["does", "are", "is"])
P.mcq("B1.1", "Choose the correct option: ___ happened at the meeting yesterday?", "What", ["What did", "What does", "What was"])
P.mcq("B1.1", "Choose the correct option: Who ___ you at the station? Sam met me.", "met", ["did met", "did meeting", "does met"])
P.mcq("B1.1", "In a chat: which sentence is NOT correct?", "Who did called you last night?", ["Who called you last night?", "Who did you call last night?", "What happened last night?"], b=4)
P.mcq("B1.1", "Which question asks about the object?", "What did she say?", ["Who said that?", "What happened?", "Who knows?"], b=3)
P.mcq("B1.1", "Choose the correct option: Which team ___ the match last Sunday?", "won", ["did won", "does won", "win"])
P.mcq("B1.2", "Choose the correct option: Who ___ with last night?", "did you go", ["you went", "did you went", "went you"])
P.mcq("B1.2", "In a text: which sentence is correct?", "Who did you talk to at the party?", ["Who you talked to at the party?", "Who did you talked to at the party?", "Who talk to you at the party did?"], b=3)
P.mcq("B1.2", "In an exam: which sentence is correct?", "How many people came to the party?", ["How many people did came to the party?", "How many people comes to the party?", "How many people they came to the party?"], b=3)
P.mcq("B1.2", "In a message: which sentence is NOT correct?", "What did happened at the meeting?", ["What happened at the meeting?", "What did you decide at the meeting?", "Who spoke at the meeting?"], b=4)
P.mcq("B1.2", "Choose the correct option: ___ is responsible for this mistake?", "Who", ["Who does", "Who did", "What does"], b=3)
P.text("A2.2", "Make a question with who, about the person who did it: Ben broke the cup.", ["Who broke the cup?"], b=4)
P.text("A2.2", "Make a question with who, about the object: Ben invited Maria.", ["Who did Ben invite?", "Whom did Ben invite?"], b=4)
P.text("B1.1", "Make a question with what, about the subject: Something made that noise.", ["What made that noise?"], b=4)
P.text("B1.1", "Make a question with who, about the object: Maria thanked her teacher.", ["Who did Maria thank?", "Whom did Maria thank?"], b=4)
P.text("B1.2", "Make a question about the person who did the action: Someone has taken my umbrella.", ["Who has taken my umbrella?"], b=5)
P.text("B1.2", "Make a question with who, about the object: Anna lent her bike to Tom.", ["Who did Anna lend her bike to?", "Whom did Anna lend her bike to?", "To whom did Anna lend her bike?"], b=5)
P.text("A2.2", "Ask about the person: Ben broke the cup.", ["Who broke the cup?"], b=4)
P.text("A2.2", "Ask about Maria: Ben invited Maria.", ["Who did Ben invite?", "Whom did Ben invite?"], b=4)
P.text("B1.1", "Ask about the thing: Something made that noise.", ["What made that noise?"], b=4)
P.text("B1.1", "Ask about the teacher: Maria thanked her teacher.", ["Who did Maria thank?", "Whom did Maria thank?"], b=4)
P.text("B1.2", "Ask about Tom: Anna lent her bike to Tom.", ["Who did Anna lend her bike to?", "Whom did Anna lend her bike to?", "To whom did Anna lend her bike?"], b=5)
P.match("A2.2", "Match each question with what it asks about.", [("Who called Tom?", "the person who called"), ("Who did Anna call?", "the person Anna called"), ("What fell?", "the thing that fell"), ("What did Anna buy?", "the thing Anna bought")])
P.match("B1.1", "Match each statement with its question.", [("Tom ate the pizza. (who?)", "Who ate the pizza?"), ("Tom ate the pizza. (what?)", "What did Tom eat?"), ("The car stopped. (what?)", "What stopped?"), ("Maria saw a ghost. (who?)", "Who saw a ghost?")])
P.match("B1.2", "Match each sentence with the question about it.", [("Someone called. (who?)", "Who called?"), ("Anna called someone. (who?)", "Who did Anna call?"), ("Something broke. (what?)", "What broke?"), ("Anna broke something. (what?)", "What did Anna break?")])

# ============ Verb patterns: -ing or to (A2.2 / B1.1 / B1.2) ============
P = Topic("Verb patterns", **B,
    order=("Check the verb: *enjoy / finish / avoid* + *-ing*; *want / decide / hope* + *to*.", "Pārbaudi darbības vārdu: aiz *enjoy / finish / avoid* — *-ing*; aiz *want / decide / hope* — *to*."),
    bank=("The first verb decides: *enjoy / finish / avoid / suggest* + *-ing*; *want / decide / hope / manage / refuse* + *to* + base verb. After a preposition: *-ing*.", "Pirmais darbības vārds nosaka formu: *enjoy / finish / avoid / suggest* + *-ing*; *want / decide / hope / manage / refuse* + *to* + pamatforma. Aiz prievārda: *-ing*."),
    gap=("The first verb decides: *-ing* after *enjoy / finish / avoid*; *to* + base verb after *want / decide / hope*.", "Pirmais darbības vārds nosaka formu: *-ing* aiz *enjoy / finish / avoid*; *to* + pamatforma aiz *want / decide / hope*."),
    text=("The first verb decides: *-ing* or *to* + base verb. After a preposition (*before, at, in*) we use *-ing*.", "Pirmais darbības vārds nosaka formu: *-ing* vai *to* + pamatforma. Aiz prievārda (*before, at, in*) lieto *-ing*."),
    mcq=("The first verb decides: *enjoy / finish / avoid / suggest* + *-ing*; *want / decide / hope / manage / refuse* + *to* + base verb. After a preposition: *-ing*.", "Pirmais darbības vārds nosaka formu: *enjoy / finish / avoid / suggest* + *-ing*; *want / decide / hope / manage / refuse* + *to* + pamatforma. Aiz prievārda: *-ing*."),
    match=("The first verb decides: *-ing* or *to*. After a preposition: *-ing*.", "Pirmais darbības vārds nosaka formu: *-ing* vai *to*. Aiz prievārda: *-ing*."))
for s, l in [("i enjoy reading before bed", "A2.2"), ("she wants to learn spanish", "A2.2"), ("he finished cleaning his room", "A2.2"),
             ("she suggested taking the earlier train", "B1.1"), ("after finishing work she went straight to the gym", "B1.1"), ("they can't afford to buy a house in the city centre", "B1.1"),
             ("i will never forget meeting her for the first time", "B1.2"), ("remember to turn off the lights when you leave", "B1.2"), ("he stopped to talk to a neighbour on the way home", "B1.2")]:
    P.order(l, s)
P.bank("A2.2", "I'd like ___ a coffee.", "to have", ["having", "have"])
P.bank("A2.2", "She likes ___ in the garden.", "working", ["to working", "work"])
P.bank("B1.1", "I avoid ___ coffee in the evening.", "drinking", ["to drink", "drink"])
P.bank("B1.1", "She refused ___ the contract.", "to sign", ["signing", "sign"])
P.bank("B1.1", "Before ___ the house, check the windows.", "leaving", ["to leave", "leave"])
P.bank("B1.2", "I'm thinking of ___ jobs next year.", "changing", ["to change", "change"])
P.bank("B1.2", "She was accused of ___ the money.", "stealing", ["to steal", "steal"])
P.bank("B1.2", "He pretended ___ asleep.", "to be", ["being", "be"])
P.gap("A2.2", "He hopes ___ a job soon. (find)", "to find")
P.gap("A2.2", "They avoid ___ in the rush hour. (drive)", "driving")
P.gap("B1.1", "He admitted ___ the window. (break)", "breaking | having broken")
P.gap("B1.1", "We can't afford ___ a new car. (buy)", "to buy")
P.gap("B1.1", "She keeps ___ me the same question. (ask)", "asking")
P.gap("B1.2", "We regret ___ you that the flight is cancelled. (inform)", "to inform")
P.gap("B1.2", "I really regret ___ so rude to her. (be)", "being | having been")
P.gap("B1.2", "She insisted on ___ the bill. (pay)", "paying")
P.mcq("A2.2", "Choose the correct option: I enjoy ___ to music.", "listening", ["to listen", "listen", "listened"])
P.mcq("A2.2", "Choose the correct option: She wants ___ a new phone.", "to buy", ["buying", "buy", "bought"])
P.mcq("A2.2", "Choose the correct option: He finished ___ his homework at nine.", "doing", ["to do", "do", "done"])
P.mcq("A2.2", "Choose the correct option: We decided ___ at home.", "to stay", ["staying", "stay", "stayed"])
P.mcq("B1.1", "Choose the correct option: Thank you for ___ me with the heavy bags.", "helping", ["to help", "help", "helped"])
P.mcq("B1.1", "Choose the correct option: I'm looking forward to ___ you next week.", "seeing", ["see", "to see", "saw"])
P.mcq("B1.1", "Choose the correct option: He suggested ___ a taxi.", "taking", ["to take", "take", "took"])
P.mcq("B1.1", "Choose the correct option: They managed ___ the problem quickly.", "to solve", ["solving", "solve", "solved"])
P.mcq("B1.1", "In an email: which sentence is NOT correct?", "She promised helping me with the move.", ["She promised to help me with the move.", "She suggested helping me with the move.", "She offered to help me with the move."], b=4)
P.mcq("B1.1", "Which sentence is correct?", "He is good at solving problems.", ["He is good at solve problems.", "He is good at to solve problems.", "He is good to solving problems."], b=3)
P.mcq("B1.2", "Choose the correct option: I forgot ___ the milk, so we have none for breakfast.", "to buy", ["buying", "bought", "buy"])
P.mcq("B1.2", "Choose the correct option: She was tired, so she stopped ___ a break.", "to take", ["taking", "take", "took"])
P.mcq("B1.2", "Choose the correct option: Remember ___ your passport when you go to the airport.", "to take", ["taking", "take", "took"])
P.mcq("B1.2", "Choose the correct option: I'll never forget ___ the Eiffel Tower for the first time.", "seeing", ["to see", "see", "saw"])
P.mcq("B1.2", "Which sentence means he quit smoking?", "He stopped smoking.", ["He stopped to smoke.", "He started smoking.", "He wanted to smoke."], b=3)
P.mcq("B1.2", "In a letter: which sentence is NOT correct?", "She enjoys to cook for her friends.", ["She enjoys cooking for her friends.", "She loves to cook for her friends.", "She likes cooking for her friends."], b=4)
P.mcq("B1.2", "Choose the correct option: She apologised for ___ late.", "being", ["to be", "be", "been"])
P.text("A2.2", "Make a sentence with decide: I will go home early.", ["I decided to go home early."], b=4)
P.text("A2.2", "Make a sentence with finish: I cleaned the kitchen.", ["I finished cleaning the kitchen."], b=4)
P.text("B1.1", "Rewrite with suggested: 'Let's go to the cinema,' said Ben.", ["Ben suggested going to the cinema.", "Ben suggested that we go to the cinema."], b=5)
P.text("B1.1", "Rewrite with before: She checked the windows. Then she left the house.", ["She checked the windows before leaving the house.", "Before leaving the house, she checked the windows."], b=5)
P.text("B1.2", "Rewrite with stopped: He used to smoke, but he doesn't now.", ["He stopped smoking.", "He has stopped smoking."], b=5)
P.text("B1.2", "Rewrite with forgot: I didn't lock the door because I forgot.", ["I forgot to lock the door."], b=5)
# no-hint twins: same patterns, the verb is not named; the sentence has one mistake and the context decides
P.text("A2.2", "Correct the mistake: We decided staying at home.", ["We decided to stay at home."], b=4)
P.text("A2.2", "Correct the mistake: I finished to clean the kitchen.", ["I finished cleaning the kitchen."], b=4)
P.text("B1.1", "Correct the mistake: Ben suggested to go to the cinema.", ["Ben suggested going to the cinema.", "Ben suggested that we go to the cinema.", "Ben suggested we go to the cinema."], b=5)
P.text("B1.1", "Correct the mistake: Before to leave the house, she checked the windows.", ["Before leaving the house, she checked the windows."], b=5)
P.text("B1.2", "Correct the mistake: My grandfather stopped to smoke ten years ago.", ["My grandfather stopped smoking ten years ago."], b=5)
P.text("B1.2", "Correct the mistake: I forgot locking the door, so the flat was open all night.", ["I forgot to lock the door, so the flat was open all night."], b=5)
P.match("A2.2", "Match each pattern with its example.", [("verb + -ing", "I enjoy cooking."), ("verb + to + base verb", "I want to cook."), ("preposition + -ing", "I'm good at cooking."), ("like, love, hate", "I like cooking. = I like to cook.")])
P.match("B1.1", "Match each group of words with its pattern.", [("enjoy, avoid, finish", "+ -ing"), ("want, decide, hope", "+ to + base verb"), ("good at, interested in", "preposition + -ing"), ("can, must, should", "+ base verb, no to")])
P.match("B1.2", "Match each phrase with its meaning.", [("stop smoking", "quit"), ("stop to smoke", "pause in order to smoke"), ("remember locking", "a memory of the past action"), ("remember to lock", "do the task")])
save("b1-new-3.csv")
