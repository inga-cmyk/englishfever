"""Other correct orders for the word-order tasks. A learner who builds a different but correct sentence must not be marked wrong
(reports: "she didn't use to enjoy cooking but she loves it now", "my boss is the man who called you").
Three sources, all applied by lib.od():
  TIME  - a time phrase at the end of a statement may also come first  (yesterday I met her / I met her yesterday)
  PAIRS - two parts that can swap places: "if you heat ice | it melts" gives both orders, whichever one is the key
  EXTRA - single sentences written out
tests/orders_test.py checks that every entry here is used by a task and that each variant uses exactly the same words."""
import re

TIME = ["every day", "every morning", "every week", "every sunday", "on fridays", "on weekdays", "yesterday", "last weekend", "last week", "last night", "last year", "today", "tomorrow",
        "this evening", "this afternoon", "tonight", "next week", "next year", "at nine", "at six", "at seven", "in 1990", "in 1950", "in 1920", "in july", "at night", "at the moment",
        "these days", "right now", "soon", "lately", "twice a week", "all day", "the next day", "at the end of the month", "on friday evening", "within an hour", "within two days",
        "by the end of june", "since last september", "since march", "for hours", "for twenty minutes", "before noon", "after a few lessons", "later this afternoon", "before bed",
        "after the long day", "at sea level"]
QUESTION_START = {"what", "who", "where", "why", "how", "which", "when", "is", "are", "do", "does", "did", "can", "could", "will", "would", "has", "have", "had", "was", "were",
                  "should", "may", "might", "must", "shall"}
STOP = {" as ", " than ", " the one ", " and ", " but ", " so ", " because ", " when ", " while ", " if ", " until ", " that ", " before ", " after ", " unless ", " as soon as "}
PAIRS = """if you heat ice | it melts
if i drink coffee at night | i can't sleep
plants die | if they don't get water
if it rains | the streets get wet
if you press this key | the page goes down
when the sun goes down | it gets cold
if you don't eat | you feel hungry
if you add salt | the soup tastes better
if i run fast | i get hot
the soup gets cold | if you leave it
if it snows | we will build a snowman
i will lend you my book | if you ask
if you don't hurry | you will miss the train
she will be happy | if you call her
if we win the game | we'll celebrate
they won't come | if it rains
if you eat that | you will feel sick
we won't go | if it's too cold
it was raining | when we left the house
i was cooking | while my brother was watching tv
were you sleeping | when i called
we were walking home | when it started to rain
the sun was shining | and the birds were singing
if people don't sleep | they feel tired
if you help me | i will help you
if you heat water to one hundred degrees | it boils
if customers pay late | the company charges extra
when the temperature drops below zero | the roads become dangerous
if i don't sleep well | i find it hard to concentrate
plants grow slowly | if they don't get enough light
if you press the red button | the machine stops
people get nervous | if they have to speak in public
if the alarm goes off | everyone leaves the building
metal expands | when it gets hot
if a customer complains | the manager always listens
if you mix oil and vinegar | they separate
ice melts | if the temperature rises above zero
if you call me tomorrow | i will explain the new plan
we will miss the train | unless we leave right now
if the weather is good | we will have the party outside
she'll be very upset | if you forget her birthday again
what will you do | if you don't get the job
if i finish early | i'll join you at the restaurant
unless it stops raining | we won't be able to play
you will feel better | if you get some fresh air
if i had more free time | i would learn to play the piano
she would travel the world | if she won the lottery
what would you do | if you lost your keys
if i were you | i would talk to your manager
we would buy a bigger flat | if we had more money
if he spoke more slowly | i would understand him
they wouldn't be so tired | if they went to bed earlier
would you move abroad | if you got a good job offer
if i had known about the problem | i would have helped you
she would have passed the exam | if she had studied harder
if we hadn't missed the bus | we wouldn't have been late
what would you have done | if you had lost your passport
he would have won the race | if he hadn't fallen
if they had left earlier | they would have caught the train
i wouldn't have bought it | if i had read the reviews
if it hadn't rained | we would have gone to the beach
would she have said yes | if you had asked her
we would have stayed longer | if the weather had been better
i will call you | when i get home
we will leave | as soon as everyone is ready
wait here | until the doctor calls your name
i will send you the file | as soon as i have finished it
by the time you arrive | we will have finished dinner
she won't sign the contract | until she has read every page
after finishing work | she went straight to the gym
remember to turn off the lights | when you leave
we needn't have rushed | because the train was late
every phone is checked by two people | before it is sold
my wallet was stolen | while i was on the train
the match was cancelled | because of the heavy rain
you will be told | as soon as the decision is made
she rarely eats out | because she prefers to cook at home
i don't usually drink coffee after lunch | because it keeps me awake
he isn't answering his phone | because he is driving
why is she wearing a coat | when it is so warm
the weather is getting colder | and the days are getting shorter
she opened the letter and read it twice | before she answered
we used to play in the street | until it got dark
did you use to walk to school | when you were young
while i was walking to work | i met an old friend
the phone rang | while we were having dinner
what were you doing | when the lights went out
they were arguing loudly | when the teacher walked in
she was driving home | when she saw the accident
i have lived in this city | since i was a child
when i arrived | the film had already started
she was tired | because she had worked all night
they had left | before we got to the party
had you ever visited london | before that trip
by the time the police came | the thieves had escaped
we had finished dinner | when our guests arrived
i didn't recognise her | because she had changed her hair
after she had read the letter | she burst into tears
the train had already gone | when we reached the station
i'll call you | as soon as i get there
we won't be able to come | if it snows heavily
will you be at home | when the parcel arrives
should we leave | before it gets dark"""
EXTRA = {
    "the man who called you is my boss": ["my boss is the man who called you"],
    "the woman whose car was stolen called the police": ["the police called the woman whose car was stolen"],
    "she didn't use to enjoy cooking but now she loves it": ["she didn't use to enjoy cooking but she loves it now"],
    "could you pass me the salt please": ["please could you pass me the salt"],
    "they walked slowly to the station": ["they walked to the station slowly"],
    "the museum doesn't open on mondays during the winter": ["during the winter the museum doesn't open on mondays", "on mondays during the winter the museum doesn't open", "on mondays the museum doesn't open during the winter"],
    "i have a cat and a dog": ["i have a dog and a cat"],
}

_ALT = {}; GROUPS = []
for line in PAIRS.split("\n"):
    a, b = [x.strip() for x in line.split("|")]
    s1 = a + " " + b
    s2 = (b[4:] + " and " + a) if b.startswith("and ") else b + " " + a   # "X | and Y" swaps the two clauses around "and"
    _ALT.setdefault(s1, []).append(s2); _ALT.setdefault(s2, []).append(s1); GROUPS.append((s1, s2))
for k, v in EXTRA.items(): _ALT.setdefault(k, []).extend(v); GROUPS.append((k,))


def time_front(s):
    """The same statement with its closing time phrase first, or None."""
    toks = s.split()
    if toks[0] in QUESTION_START or any(x in " " + s + " " for x in STOP): return None
    for ph in sorted(TIME, key=lambda p: -len(p.split())):
        n = len(ph.split())
        if len(toks) > n + 2 and " ".join(toks[-n:]) == ph: return ph + " " + " ".join(toks[:-n])
    return None

def alternatives(s):
    out = []
    for x in _ALT.get(s, []) + [time_front(s)]:
        if x and x != s and x not in out: out.append(x)
    # a swapped sentence can also take a fronted time phrase of its own
    return out
