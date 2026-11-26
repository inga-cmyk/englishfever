# Blind check r21-3: flags for the judge

60 tasks, 2 readers.

## r21-3-001 · B1.1 · gap · built-in

Task: Look at the ticket: our flight ___ at 6.40 tomorrow morning. (leave)
Key: {"kind": "gap", "accepted": [["leaves", "is leaving", "will leave"]]}
- reader 1: instruction: Tense not signalled: 'is leaving' (arrangement) is also correct for a ticket/timetable context.
- reader 2: instruction: 'is leaving' also correct (less natural for a timetable).

## r21-3-002 · B1.1 · text · built-in

Task: Make it negative and use 'any': She has money.
Key: {"kind": "text", "accepted": [["She doesn't have any money.", "She does not have any money.", "She hasn't any money.", "She has not any money.", "She hasn't got any money.", "She has not got any money."]]}
- reader 2: instruction: 'use any' gives the answer away.
- reader 2: level: A2 task at B1.1.

## r21-3-004 · B1.1 · mcq · built-in

Task: Choose the correct option: I ___ my report last March.
options: am finishing | finished | finish | have finished
Key: {"kind": "mcq", "correct": "finished", "wrong": ["have finished", "finish", "am finishing"]}
- reader 1: level: Simple past with 'last March' is A2, too easy for B1.1.
- reader 2: level: A2 task at B1.1.

## r21-3-005 · B1.1 · write · built-in

Task: Write two sentences that start a story. Say what happened first and what happened next (use Then or After that).
Key: {"kind": "write", "model": "I got up late. Then I missed the bus.", "must": ["Use *Then* or *After that* to show the order.", "Use verbs in the past simple."]}
- reader 1: instruction: Open writing; unclear which 'forms' are checked (only Then/After that?).
- reader 1: level: Two simple past sentences: A2 task.
- reader 2: instruction: Open task; fine, but 'some forms' unclear to learner (is past simple expected?).

## r21-3-006 · B1.1 · mcq · built-in

Task: Which sentence means: it started in the past and is still true now?
options: I have known Tom for ten years. | I knew Tom ten years ago. | I know Tom ten years. | I did know Tom for ten years.
Key: {"kind": "mcq", "correct": "I have known Tom for ten years.", "wrong": ["I knew Tom ten years ago.", "I know Tom ten years.", "I did know Tom for ten years."]}
- reader 1: sense: 'I know Tom ten years' is an unlikely, random wrong option.

## r21-3-007 · B1.1 · mcq · built-in

Task: Which sentence is NOT correct?
options: She has lived here since 2015. | I have seen him yesterday. | Have you finished yet? | We have known each other for years.
Key: {"kind": "mcq", "correct": "I have seen him yesterday.", "wrong": ["She has lived here since 2015.", "We have known each other for years.", "Have you finished yet?"]}
- reader 2: level: Easy for B1.1.

## r21-3-008 · B1.1 · mcq · built-in

Task: Choose the correct option: I can't open the door. I ___ my keys.
options: had lost | lose | have lost | am losing
Key: {"kind": "mcq", "correct": "have lost", "wrong": ["lose", "am losing", "had lost"]}
- reader 2: level: A2/B1.1 borderline, easy.

## r21-3-009 · B1.2 · mcq · built-in

Task: Choose the correct option: I ___ the film last night.
options: 've seen | saw | was see | have seen
Key: {"kind": "mcq", "correct": "saw", "wrong": ["have seen", "'ve seen", "was see"]}
- reader 1: level: Plain past simple with 'last night' is A2, too easy for B1.2.
- reader 1: sense: ''ve seen' and 'have seen' are the same answer twice; 'was see' is not a believable learner error.
- reader 2: a wrong option that fits: 've seen and have seen are both wrong here; they are near duplicates.
- reader 2: level: Easy; 'was see' is a form few learners write.
- reader 2: sense: 'was see' is not a believable mistake; two options are the same form.

## r21-3-010 · B1.1 · mcq · built-in

Task: I'm tired and I'm still at my desk. I ___ all day.
options: am been working | have been working | has been working | have be working
Key: {"kind": "mcq", "correct": "have been working", "wrong": ["has been working", "have be working", "am been working"]}
- reader 1: instruction: No instruction line (e.g. 'Choose the correct option').
- reader 1: sense: 'am been working' and 'have be working' are random strings, not believable mistakes; 'has been working' is the only real distractor.
- reader 2: instruction: 'all day' with 'I'm tired' is fine.
- reader 2: sense: 'am been working' and 'have be working' are unlikely errors.

## r21-3-011 · B1.2 · mcq · built-in

Task: The film began at 7.00. We arrived at 7.15. When we arrived, the film ___ already ___.
options: had ... started | was ... starting | has ... started | did ... start
Key: {"kind": "mcq", "correct": "had ... started", "wrong": ["has ... started", "was ... starting", "did ... start"]}
- reader 1: a wrong option that fits: 'was ... starting' is grammatical English ('the film was already starting') though it clashes with 'began at 7.00'.
- reader 1: instruction: Two gaps in one option with '...' is a little confusing.
- reader 2: answer not accepted: ['had', 'started']
- reader 2: a wrong option that fits: 'was ... starting' is possible English (the film was already starting) though it clashes with 'began at 7.00'.
- reader 2: instruction: Two gaps with one choice; fine.
- the readers disagree

## r21-3-012 · B1.2 · mcq · built-in

Task: In 'When I got to the station, the train had left', which happened first?
options: Both together. | I got there. | The train left. | We can't know.
Key: {"kind": "mcq", "correct": "The train left.", "wrong": ["I got there.", "Both together.", "We can't know."]}
- reader 1: instruction: Question quotes 'I got to the station' but option says 'I got there'; 'We can't know' is odd (no 'we' in sentence).
- reader 1: sense: 'Both together' and 'We can't know' are weak distractors.

## r21-3-013 · B1.2 · mcq · built-in

Task: Hurry up! The film ___ to start.
options: will | goes | is about | is for
Key: {"kind": "mcq", "correct": "is about", "wrong": ["is for", "goes", "will"]}
- reader 1: instruction: No instruction line; 'be about to' structure is fully visible only via 'to start'.
- reader 2: level: 'be about to' is fine B1.2.
- reader 2: sense: 'is for' and 'will' are weak distractors.

## r21-3-014 · B1.1 · mcq · built-in

Task: In 'The report is checked by the manager', what is the focus?
options: The manager and what he does. | A plan for the report next week. | Something the manager did once. | The report and what happens to it.
Key: {"kind": "mcq", "correct": "The report and what happens to it.", "wrong": ["The manager and what he does.", "A plan for the report next week.", "Something the manager did once."]}
- reader 1: instruction: 'focus' is abstract for B1.1; options are vague and long, passive meaning rather than form.
- reader 2: instruction: 'focus' is vague; 'what is the focus' might confuse.

## r21-3-016 · B1.2 · mcq · built-in

Task: The new bridge ___ at the moment.
options: was being built | is building | is built | is being built
Key: {"kind": "mcq", "correct": "is being built", "wrong": ["is building", "is built", "was being built"]}
- reader 1: instruction: No instruction line.
- reader 2: level: Passive continuous is B2 rather than B1.2 for many.

## r21-3-017 · B1.2 · mcq · built-in

Task: Which sentence reports the guard's request: 'Please wait here.'
options: The guard told me to wait there. | The guard told me wait there. | The guard told me that I wait here. | The guard said me to wait there.
Key: {"kind": "mcq", "correct": "The guard told me to wait there.", "wrong": ["The guard told me wait there.", "The guard told me that I wait here.", "The guard said me to wait there."]}
- reader 1: sense: Options 2-4 are believable but 'told me that I wait here' is a strange error.
- reader 2: instruction: Gives 'Please wait here' so the here/there shift is the only hint; ok.

## r21-3-018 · B1.1 · mcq · built-in

Task: Choose the correct sentence.
options: Could you tell me where is the station? | Could you tell me where the station is? | Could you tell me where the station? | Could you tell me where's the station is?
Key: {"kind": "mcq", "correct": "Could you tell me where the station is?", "wrong": ["Could you tell me where is the station?", "Could you tell me where's the station is?", "Could you tell me where the station?"]}
- reader 1: level: Very easy for B1.1 (obvious word order, one option has no verb).
- reader 1: sense: 'where's the station is' is an impossible string.
- reader 2: level: Easy for B1.1 (A2/B1.1 border).
- reader 2: sense: Options 3 and 4 are random strings nobody writes.

## r21-3-019 · B1.2 · gap · b1-cond-rep-1.csv:196

Task: She asked him ___ he had seen the film.
word_cards: that | if | what
Key: {"kind": "gap", "accepted": [["if"]]}
- reader 1: instruction: 'whether' would be correct but is not a card; 'that' vs 'if' is answerable from 'had seen the film' only by meaning.
- reader 2: instruction: 'whether' not offered; fine.
- reader 2: level: Easy: only one card fits.

## r21-3-020 · B1.1 · gap · b1-new-1.csv:20

Task: When I was a teenager, I ___ any money, so I walked everywhere. (not / have)
Key: {"kind": "gap", "accepted": [["didn't use to have", "did not use to have", "didn't have", "did not have", "used not to have"]]}
- reader 1: another correct answer, not accepted: [["hadn't"], ['had not']]
- reader 1: instruction: 'hadn't any money' is correct but old-fashioned; gap needs both forms accepted.
- reader 2: another correct answer, not accepted: [["hadn't"], ['had not']]
- reader 2: instruction: 'hadn't any' is dated British, correct.

## r21-3-021 · B1.2 · mcq · b1-new-1.csv:28

Task: Choose the correct option: At first I hated the food, but now I ___ it.
options: am used to | am use to | used to | use to
Key: {"kind": "mcq", "correct": "am used to", "wrong": ["used to", "am use to", "use to"]}
- reader 1: instruction: Meaning is clear.
- reader 1: sense: 'am use to' and 'use to' are typo-type mistakes; fine.
- reader 2: instruction: 'now I like it' sense: 'am used to' fits but the gap meaning is a bit loose.
- reader 2: sense: 'use to' and 'am use to' are believable.

## r21-3-022 · B1.2 · mcq · b1-new-1.csv:32

Task: Which sentence is correct?
options: I used to have a bike when I was ten. | I use to have a bike when I was ten. | I am used to have a bike when I was ten. | I used have a bike when I was ten.
Key: {"kind": "mcq", "correct": "I used to have a bike when I was ten.", "wrong": ["I used have a bike when I was ten.", "I am used to have a bike when I was ten.", "I use to have a bike when I was ten."]}
- reader 1: sense: 'I used have' and 'I am used to have' are plausible errors; ok.

## r21-3-024 · B1.2 · text · b1-new-2.csv:35

Task: Join with *whose*: The man lives next door. His dog can open doors.
Key: {"kind": "text", "accepted": [["The man whose dog can open doors lives next door."]]}
- reader 1: instruction: No clue which man is the subject; also 'The man who lives next door has a dog that...' avoids 'whose' (instruction forces whose, fine).
- reader 2: another correct answer, not accepted: ['The man whose dog can open doors is my neighbour.']
- reader 2: instruction: Fine; learner might write 'The man who lives next door has a dog whose...' not accepted by instruction.

## r21-3-025 · B1.2 · text · b1-new-2.csv:36

Task: Join the two sentences: My uncle lives in Spain. He is a chef.
Key: {"kind": "text", "accepted": [["My uncle, who lives in Spain, is a chef.", "My uncle, who is a chef, lives in Spain."]]}
- reader 1: another correct answer, not accepted: ['My uncle lives in Spain and he is a chef.', 'My uncle lives in Spain and is a chef.', 'My uncle lives in Spain, where he is a chef.', 'My uncle is a chef and he lives in Spain.', 'My uncle, a chef, lives in Spain.']
- reader 1: instruction: No connector or structure given, so many correct answers; unclear which is wanted (relative clause?).
- reader 2: another correct answer, not accepted: [['My uncle lives in Spain and is a chef.'], ['My uncle lives in Spain and he is a chef.'], ['My uncle lives in Spain, and he is a chef.']]
- reader 2: instruction: No joining word named: many correct answers; unclear what is wanted (relative clause?).
- reader 2: level: Task wording fits B1 only if who is expected; as an open join it is A2.

## r21-3-026 · B1.1 · gap · b1-new-4.csv:60

Task: The letters ought to ___ sent today.
word_cards: been | be | being
Key: {"kind": "gap", "accepted": [["be"]]}
- reader 2: level: 'ought to' passive is B1.2/B2 and rare.

## r21-3-027 · B1.1 · order · b1-passives-1.csv:6

Task: Put the words in order.
word_cards: this | used | millions | is | of | by | software | people
Key: {"kind": "order", "sentence": "this software is used by millions of people", "also": []}
- reader 1: level: Easy for B1.1: passive is visible from cards, little challenge.
- reader 2: another correct answer, not accepted: ['this is software used by millions of people']
- reader 2: instruction: No capital or full stop; fine.

## r21-3-028 · B1.1 · text · b1-passives-1.csv:64

Task: Start with *This factory*: The company built this factory in 1990.
Key: {"kind": "text", "accepted": [["This factory was built by the company in 1990.", "This factory was built in 1990.", "In 1990 this factory was built by the company.", "In 1990 this factory was built."]]}
- reader 1: another correct answer, not accepted: ['This factory was built in 1990 by the company.']
- reader 2: another correct answer, not accepted: ['This factory was built in 1990 by the company.']

## r21-3-029 · B1.1 · gap · b1-tenses-1.csv:16

Task: Most people ___ tired when they ___ enough sleep.
word_cards: doesn't get | feels | don't get | feel
Key: {"kind": "gap", "accepted": [["feel"], ["don't get"]]}
- reader 1: level: Very easy (A2 present simple agreement).
- reader 1: sense: 'doesn't get/feels' are wrong by agreement only; weak distractors.

## r21-3-030 · B1.1 · text · b1-tenses-1.csv:27

Task: Rewrite with never: I don't eat fast food.
Key: {"kind": "text", "accepted": [["I never eat fast food."]]}
- reader 1: level: A2 level.
- reader 2: level: A2 task at B1.1.

## r21-3-031 · B1.1 · text · b1-tenses-1.csv:28

Task: Make a question with What time: The bank opens at nine.
Key: {"kind": "text", "accepted": [["What time does the bank open?"]]}
- reader 1: level: A2 level (present simple question).
- reader 2: another correct answer, not accepted: ['At what time does the bank open?', 'What time does the bank open at?']
- reader 2: level: A2 task at B1.1.

## r21-3-032 · B1.1 · text · b1-tenses-1.csv:65

Task: Make it negative: We are staying at a hotel.
Key: {"kind": "text", "accepted": [["We aren't staying at a hotel.", "We are not staying at a hotel.", "We're not staying at a hotel."]]}
- reader 1: level: A2 level.
- reader 2: level: A2 task at B1.1.

## r21-3-033 · B1.1 · text · b1-tenses-2.csv:22

Task: Rewrite with since: I started learning English in 2019 and I still learn it.
Key: {"kind": "text", "accepted": [["I have been learning English since 2019.", "I have learned English since 2019."]]}
- reader 1: another correct answer, not accepted: ['I have learnt English since 2019.', 'Since 2019 I have been learning English.']
- reader 1: instruction: 'Rewrite with since' but the learner must also change tense; fine but several tenses accepted.
- reader 2: another correct answer, not accepted: ['I have learnt English since 2019.']
- reader 2: instruction: 'since' named gives the answer; 'I still learn it' is awkward.

## r21-3-034 · B1.1 · text · b1-tenses-2.csv:24

Task: Make it negative: We have visited that museum.
Key: {"kind": "text", "accepted": [["We haven't visited that museum.", "We have not visited that museum."]]}
- reader 1: another correct answer, not accepted: ['We have never visited that museum.']
- reader 1: instruction: 'never' version is arguably also negative.
- reader 2: another correct answer, not accepted: ['We have never visited that museum.', "We haven't been to that museum."]
- reader 2: level: A2/B1.1 border, easy.

## r21-3-035 · B1.2 · text · b1-tenses-2.csv:25

Task: Make a question with ever: Your parents have travelled abroad.
Key: {"kind": "text", "accepted": [["Have your parents ever travelled abroad?", "Have your parents ever traveled abroad?"]]}
- reader 1: another correct answer, not accepted: ['Have your parents ever traveled abroad? (US spelling)']
- reader 2: another correct answer, not accepted: ['Have your parents ever traveled abroad? (US spelling)']

## r21-3-036 · B1.1 · mcq · b1-upgrades-1.csv:2

Task: Choose the best option: The timetable says our train ___ at 7.10, so we need to leave home by 6.30.
options: leaving | has left | leaves | left
Key: {"kind": "mcq", "correct": "leaves", "wrong": ["leaving", "left", "has left"]}
- reader 1: instruction: No signal that timetable present is wanted; fine.
- reader 1: level: Present for timetable is A2/B1 low; ok.
- reader 2: level: Easy.

## r21-3-037 · B1.1 · gap · b1-upgrades-1.csv:8

Task: Why ___ you ___ so much coffee this week? You usually only drink tea. (drink)
Key: {"kind": "gap", "accepted": [["are"], ["drinking"]]}
- reader 1: answer not accepted: ['have', 'been drinking']
- reader 1: another correct answer, not accepted: [['have', 'drunk'], ['did', 'drink']]
- reader 1: instruction: Tense not signalled; 'Why are you drinking' (temporary habit) fits 'this week' and 'You usually only drink tea' equally well; 'have you drunk' also correct.
- reader 2: another correct answer, not accepted: [['have', 'been drinking']]
- reader 2: instruction: 'do ... drink' is not correct here; present perfect continuous also fits 'this week'.
- the readers disagree

## r21-3-038 · B1.1 · text · b1-upgrades-1.csv:12

Task: Join the sentences with because: I stayed at home. I felt ill.
Key: {"kind": "text", "accepted": [["I stayed at home because I felt ill.", "Because I felt ill, I stayed at home."]]}
- reader 1: another correct answer, not accepted: ['I stayed at home because I was ill.']
- reader 1: level: A2 level.
- reader 2: level: A2 task at B1.1.

## r21-3-040 · B1.1 · mcq · b1-upgrades-1.csv:19

Task: Choose the correct option: I ___ in this flat for six years, and I still love the view from the balcony.
options: living | am living | live | have lived
Key: {"kind": "mcq", "correct": "have lived", "wrong": ["living", "live", "am living"]}
- reader 1: level: Fine.

## r21-3-041 · B1.1 · gap · b1-upgrades-1.csv:30

Task: I'll wait here until you ___ back. (come)
Key: {"kind": "gap", "accepted": [["come"]]}
- reader 1: another correct answer, not accepted: [['have come'], ['get']]
- reader 1: instruction: 'have come' (until you've come back) is also correct; 'get' is not the given verb.
- reader 2: another correct answer, not accepted: [['have come'], ["'ve come"]]
- reader 2: instruction: 'have come' also correct.

## r21-3-042 · B1.2 · mcq · b1-upgrades-1.csv:31

Task: Choose the correct option: I don't know yet, but I ___ come to the party if I finish work early.
options: would | have to | must | might
Key: {"kind": "mcq", "correct": "might", "wrong": ["must", "would", "have to"]}
- reader 1: sense: Only 'might' fits; fine.

## r21-3-043 · B1.1 · mcq · b1-upgrades-1.csv:33

Task: Choose the correct option: In our factory, every phone ___ by two different people before it leaves the building.
options: checks | is checked | was check | is checking
Key: {"kind": "mcq", "correct": "is checked", "wrong": ["checks", "is checking", "was check"]}
- reader 1: sense: 'was check' is an impossible string.

## r21-3-044 · B1.2 · text · b1-upgrades-1.csv:42

Task: Start with *The winner*: They will announce the winner on Friday.
Key: {"kind": "text", "accepted": [["The winner will be announced on Friday.", "On friday the winner will be announced."]]}
- reader 1: another correct answer, not accepted: ['The winner is going to be announced on Friday.', 'The winner will be announced by them on Friday.', 'The winner is to be announced on Friday.']
- reader 2: another correct answer, not accepted: [['The winner is going to be announced on Friday.'], ['The winner will be announced by them on Friday.']]
- reader 2: level: Passive future is B1.2/B2, fine.

## r21-3-045 · B1.1 · mcq · b1-upgrades-1.csv:43

Task: Choose the correct option: If the temperature ___ below zero, water turns into ice.
options: fell | will fall | falls | would fall
Key: {"kind": "mcq", "correct": "falls", "wrong": ["will fall", "fell", "would fall"]}
- reader 1: level: Zero conditional is A2/B1 low; fine.
- reader 2: level: Zero conditional is easy; A2.

## r21-3-046 · B1.1 · gap · compare-past-1.csv:12

Task: I ___ the party, but Chris ___ to go home. (enjoy / want)
Key: {"kind": "gap", "accepted": [["was enjoying", "enjoyed"], ["wanted"]]}
- reader 1: another correct answer, not accepted: [['am enjoying', 'wants'], ["'m enjoying", 'wants'], ["didn't enjoy", 'wanted']]
- reader 1: instruction: Tense not signalled: present 'I'm enjoying the party, but Chris wants to go home' is also natural; 'didn't enjoy ... but Chris wanted' is less logical but grammatical.
- reader 2: another correct answer, not accepted: [["didn't enjoy", 'wanted'], ['did not enjoy', 'wanted'], ['am enjoying', 'want'], ["'m enjoying", 'wants'], ['enjoy', 'want']]
- reader 2: instruction: No time context: past and present both possible; underdetermined.

## r21-3-047 · B1.1 · gap · compare-past-1.csv:27

Task: ___ you ___ Anna yesterday? (see)
Key: {"kind": "gap", "accepted": [["Did"], ["see"]]}
- reader 1: level: Simple past question is A2, too easy for B1.1.
- reader 2: level: A2 task at B1.1.

## r21-3-048 · B1.1 · gap · compare-past-1.csv:37

Task: Karen didn't come to the cinema with us. She ___ the film. (already / see)
Key: {"kind": "gap", "accepted": [["had already seen"]]}
- reader 1: answer not accepted: ['has already seen']
- reader 1: another correct answer, not accepted: [["'s already seen"]]
- reader 1: instruction: Tense not signalled: 'had already seen' is also correct (past narrative); American 'already saw' also possible. Gap holds three words with two bracket words, order must be inferred.
- reader 2: answer not accepted: ['has already seen']
- reader 2: another correct answer, not accepted: [["'s already seen"], ['already saw']]
- reader 2: instruction: Past reference makes 'had already seen' possible; 'already saw' is US.

## r21-3-049 · B1.1 · mcq · comparison-1.csv:32

Task: Which sentence says the difference is small?
options: This bag is the biggest in the shop. | This bag is much bigger than that one. | This bag is slightly bigger than that one. | This bag is far bigger than that one.
Key: {"kind": "mcq", "correct": "This bag is slightly bigger than that one.", "wrong": ["This bag is much bigger than that one.", "This bag is far bigger than that one.", "This bag is the biggest in the shop."]}
- reader 1: level: Easy; 'slightly' is a clue word only.
- reader 2: level: Easy; 'slightly' is a key word.

## r21-3-050 · B1.1 · order · comparison-1.csv:38

Task: Put the words in order.
word_cards: much | job | one | last | than | this | is | more | stressful | my
Key: {"kind": "order", "sentence": "this job is much more stressful than my last one", "also": []}
- reader 1: another correct answer, not accepted: ['my last job is much more stressful than this one', 'this one is much more stressful than my last job', 'my last one is much more stressful than this job']
- reader 1: instruction: Cards allow more than one correct order (which job is compared).
- reader 2: another correct answer, not accepted: ['my last job is much more stressful than this one', 'this one is much more stressful than my last job', 'my last one is much more stressful than this job']
- reader 2: instruction: Several orders possible.

## r21-3-051 · B1.1 · match · comparison-1.csv:39

Task: Match each sentence with its meaning.
left: The new phone is much faster. | The new phone is a bit faster. | The new phone is not as fast. | The new phone is the fastest.
right: a small difference | a big difference | the old one is faster | no other phone is faster
Key: {"kind": "match", "pairs": [["The new phone is much faster.", "a big difference"], ["The new phone is a bit faster.", "a small difference"], ["The new phone is not as fast.", "the old one is faster"], ["The new phone is the fastest.", "no other phone is faster"]]}
- reader 1: sense: 'not as fast' could also be read as 'a (big/small) difference'; weak.
- reader 2: sense: 'the old one is faster' assumes a comparison not stated.

## r21-3-052 · B1.1 · order · comparison-1.csv:49

Task: Put the words in order.
word_cards: bright | one | yesterday | the | is | we | saw | not | flat | this | as | as
Key: {"kind": "order", "sentence": "this flat is not as bright as the one we saw yesterday", "also": []}
- reader 1: answer not accepted: the flat we saw yesterday is not as bright as this one
- reader 1: another correct answer, not accepted: ['this one is not as bright as the flat we saw yesterday', 'the one we saw yesterday is not as bright as this flat']
- reader 1: instruction: More than one correct order.
- reader 2: another correct answer, not accepted: ['the one we saw yesterday is not as bright as this flat', 'this one is not as bright as the flat we saw yesterday', 'the flat we saw yesterday is not as bright as this one']
- reader 2: instruction: Several orders possible; 12 cards.
- reader 2: level: 12 cards is long for B1.1.
- the readers disagree

## r21-3-053 · B1.1 · gap · contrast-1.csv:14

Task: I ___ to Paris twice. The last time I ___ there was in May.
word_cards: go | have gone | have been | went
Key: {"kind": "gap", "accepted": [["have been"], ["went"]]}
- reader 1: level: 'have been' vs 'have gone' is classic B1; fine.
- reader 2: a wrong option that fits: 'have gone' is used in US English for 'twice' but means still away in British English; marginal.

## r21-3-054 · B1.1 · gap · learn-drag-3.csv:30

Task: I finished work. ___, I went to the gym.
word_cards: Since then | After that | After
Key: {"kind": "gap", "accepted": [["After that"]]}
- reader 1: level: A2 level; very easy.
- reader 2: level: A2 task at B1.1; easy.

## r21-3-055 · B1.1 · text · modal-verbs-1.csv:33

Task: Rewrite in the past: I have to get up early.
Key: {"kind": "text", "accepted": [["I had to get up early."]]}
- reader 1: level: A2 level.
- reader 2: level: A2 task at B1.1.

## r21-3-056 · B1.1 · text · modal-verbs-1.csv:37

Task: Make it negative: You should stay up late.
Key: {"kind": "text", "accepted": [["You shouldn't stay up late.", "You should not stay up late."]]}
- reader 1: sense: The original 'You should stay up late' is odd advice (adult, illogical without context).
- reader 2: level: A2 task at B1.1.
- reader 2: sense: Original advice 'You should stay up late' is odd.

## r21-3-057 · B1.1 · text · modal-verbs-1.csv:42

Task: Rewrite in the future with will have to: I have to pay.
Key: {"kind": "text", "accepted": [["I will have to pay.", "I'll have to pay."]]}
- reader 2: instruction: Names the form; copy task.

## r21-3-058 · B1.1 · mcq · modal-verbs-1.csv:53

Task: Choose the correct form: The test was cancelled, so we ___ study last night.
options: hadn't to | didn't have to | couldn't | mustn't
Key: {"kind": "mcq", "correct": "didn't have to", "wrong": ["couldn't", "mustn't", "hadn't to"]}
- reader 1: instruction: Meaning: 'couldn't study' is also logical-ish but wrong for cancellation; ok.
- reader 2: a wrong option that fits: 'couldn't' is grammatical but illogical after 'cancelled'.

## r21-3-059 · B1.1 · mcq · more-1.csv:115

Task: Choose the correct option: I'm looking forward to ___ you.
options: to see | see | seeing
Key: {"kind": "mcq", "correct": "seeing", "wrong": ["see", "to see"]}
- reader 1: level: A2/B1 border; only three options, easy.
- reader 2: level: A2/B1.1, easy; only three options.

## r21-3-060 · B1.1 · gap · said-told-1.csv:4

Task: Complete with *said* or *told*: The doctor ___ that I needed more sleep.
Key: {"kind": "gap", "accepted": [["said"]]}
- reader 1: instruction: Grammar terms none; markup asterisks around said/told visible to learner.
- reader 2: instruction: Both words given; 50/50 and *asterisks* show as markup. 'told me' not possible in one gap.

