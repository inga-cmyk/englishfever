"""Three A2 topics built around frequent mistakes (docs/ERROR-TYPES.md, teacher's plan 25 October): prepositions after words,
subject and verb, irregular plurals. Explanations are one short line. A Latvian comparison only where Latvian really leads to the mistake;
otherwise "Tipiska kļūda". Where the right answer is no preposition, one option is "—".
Support goes from choosing (0) to typing with a clue (1) to typing without a clue (2)."""
from lib import *
import b1_topics
# Latvian words without Latvian letters come from lib.py (the same list the Latvian check uses)
NONE = "—"


def T(name, err, en, lv):
    ex = (en, lv)
    return Topic(name, mcq_b=2, text_b=3, match_b=2, err=err, order=ex, bank=ex, gap=ex, text=ex, mcq=ex, match=ex)


# ============ Prepositions after words (A2.1 / A2.2) ============
P = T("Prepositions after words (listen to, good at)", "DEP-PREP",
      "Some words always go with the same preposition: *listen to, wait for, look at, good at, afraid of*.",
      "Daži vārdi vienmēr iet kopā ar savu prievārdu: *listen to, wait for, look at, good at, afraid of*.")
WAIT = ("*wait for*: *I'm waiting for the bus.*", "Latviski *gaidu autobusu* (bez prievārda), angliski *wait for*: *I'm waiting for the bus.*")
LISTEN = ("*listen to*: *Listen to me.*", "Latviski *klausos mūziku* (bez prievārda), angliski *listen to*: *Listen to me.*")
LOOK = ("*look at*: *Look at this photo.*", "*look at* = skatīties uz kaut ko: *Look at this photo.*")
AFRAID = ("*afraid of*: *afraid of spiders*.", "Latviski *baidās no*, angliski *afraid of* (nevis *from*): *afraid of spiders*.")
INTEREST = ("*interested in*: *interested in football*.", "Latviski *interesējas par*, angliski *interested in*: *interested in football*.")
DEPEND = ("*depend on*, not *from*: *It depends on the weather.*", "Latviski *atkarīgs no*, angliski *depend on*: *It depends on the weather.*")
GOOD = ("*good at* + a subject or an activity: *good at maths*.", "*good at maths* = viņai padodas matemātika.")
BELONG = ("*belong to*: *This bag belongs to me.*", "Latviski *pieder man*, angliski *belongs to me*.")
THANK = ("*thank you for* + the thing: *Thank you for your help.*", "*thank you for* + tas, par ko pateicas: *Thank you for your help.*")
THINK = ("*think about* + what is in your mind: *I'm thinking about my holiday.*", "*think about* = domāt par: *I'm thinking about my holiday.*")
HELP = ("*help me*, no preposition. A typical mistake: *help to me*.", "*help me*, bez prievārda. Tipiska kļūda: *help to me*.")
CALL = ("*call me*, no preposition. A typical mistake: *call to me*.", "*call me*, bez prievārda. Tipiska kļūda: *call to me*.")
JOIN = ("*join the team*, no preposition. A typical mistake: *join to*.", "*join the team*, bez prievārda. Tipiska kļūda: *join to*.")
ANSWER = ("*answer the question*, no preposition.", "*answer the question*, bez prievārda.")
QEND = ("In a question the preposition goes to the end: *Who are you waiting for?*", "Jautājumā prievārds ir beigās: *Who are you waiting for?*")

P.mcq("A2.1", "Choose the correct option: I'm waiting ___ the bus.", "for", ["to", "from"], WAIT)
P.mcq("A2.1", "Choose the correct option: Please listen ___ me.", "to", ["at", "for"], LISTEN)
P.mcq("A2.1", "Choose the correct option: Look ___ this photo!", "at", ["to", "for"], LOOK)
P.mcq("A2.2", "Choose the correct option: My brother is afraid ___ spiders.", "of", ["from", "for"], AFRAID)
P.mcq("A2.2", "Choose the correct option: Are you interested ___ football?", "in", ["on", "about"], INTEREST)
P.mcq("A2.1", "Choose the correct option: Can you help ___ me?", NONE, ["to", "for"], HELP)
P.mcq("A2.2", "Choose the correct option: Please call ___ me when you get home.", NONE, ["to", "at"], CALL)
P.mcq("A2.2", "Which sentence is NOT correct?", "She joined to the team last year.", ["She joined the team last year.", "We are waiting for Anna.", "This bag belongs to me."], JOIN, b=4)
P.mcq("A2.2", "On the phone: Which sentence is NOT correct?", "It depends from the weather.", ["It depends on the weather.", "He is good at tennis.", "I paid for the tickets."], DEPEND, b=4)
P.mcq("B1.1", "Which question is correct?", "What are you looking at?", ["What are you looking?", "At what you are looking?"], QEND)
P.bank("A2.1", "She is very good ___ maths.", "at", ["of", "on"], GOOD)
P.bank("A2.1", "This phone belongs ___ my sister.", "to", ["at", "for"], BELONG)
P.bank("A2.2", "Thank you ___ your help.", "for", ["to", "at"], THANK)
P.bank("A2.1", "Can you answer ___ the question?", NONE, ["to", "at"], ANSWER)
P.bank("A2.2", "I'm thinking ___ my holiday.", "about", ["at", "to"], THINK)
P.gap("A2.1", "Do you listen ___ music in the car?", "to", LISTEN)
P.gap("A2.1", "We are waiting ___ the taxi.", "for", WAIT)
P.gap("A2.1", "Look ___ the board, please.", "at", LOOK)
P.gap("A2.2", "It depends ___ the weather.", "on", DEPEND)
P.gap("A2.2", "My little brother is afraid ___ the dark.", "of", AFRAID)
P.gap("A2.2", "She is interested ___ art.", "in", INTEREST)
P.gap("B1.1", "Who does this bag belong ___?", "to", BELONG)
P.gap("A2.2", "Thank you ___ the flowers.", "for", THANK)
P.text("A2.1", "Correct the mistake: Can you help to me?", "Can you help me?", HELP)
P.text("A2.2", "Correct the mistake: She joined to our team in May.", "She joined our team in May.", JOIN)
P.text("A2.2", "Correct the mistake: Please call to me tomorrow.", "Please call me tomorrow.", CALL)
P.text("A2.1", "Correct the mistake: I am waiting the bus.", "I am waiting for the bus. | I'm waiting for the bus.", WAIT)
P.order("B1.1", "what are you looking at", why=QEND)
P.order("B1.1", "who are you waiting for", why=QEND)
P.match("A2.2", "Match each beginning with its ending.",
        [("Turn up the music. I'm listening", "to my favourite song."), ("She plays the piano very well. She is good", "at music."),
         ("We'll see about the picnic. It depends", "on the weather."), ("He never goes near dogs. He's afraid", "of them.")],
        ("*listen to, good at, depend on, afraid of*: learn them in pairs.", "*listen to, good at, depend on, afraid of*: mācies tos pa pāriem."))

# ============ Subject and verb (A2.1 / A2.2) ============
A = T("Subject and verb (my friend lives, my friends live)", "AGREE",
      "One person or thing: verb + *-s* (*my friend lives*). More than one: no *-s* (*my friends live*).",
      "Viens: darbības vārds ar *-s* (*my friend lives*). Vairāki: bez *-s* (*my friends live*).")
AND = ("*and* makes more than one: *Tom and Anna live* (no *-s*).", "*and* nozīmē vairākus: *Tom and Anna live* (bez *-s*). Latviski forma ir viena: *dzīvo*.")
ONE = ("One person: verb + *-s*: *My mother works.*", "Viens cilvēks: darbības vārds ar *-s*: *My mother works.*")
MANY = ("More than one: no *-s*: *My friends play.*", "Vairāki: bez *-s*: *My friends play.* Latviski *draugs spēlē* un *draugi spēlē* ir viena forma.")
EVERY = ("*everybody, everyone, nobody* take *-s*: *Everybody knows.*", "*everybody, everyone, nobody* lieto ar *-s*: *Everybody knows.*")
DOES = ("One person: *Does*. More than one: *Do*.", "Vienam: *Does*. Vairākiem: *Do*.")
THERE = ("One thing: *there is*. More than one: *there are*.", "Viens: *there is*. Vairāki: *there are*. Latviski abos gadījumos *ir*.")
HAS = ("One person: *has*. More than one: *have*.", "Vienam: *has*. Vairākiem: *have*.")

A.mcq("A2.1", "Choose the correct option: My brother and my sister ___ in Riga.", "live", ["lives", "living"], AND)
A.mcq("A2.1", "Choose the correct option: Everybody ___ the answer.", "knows", ["know", "knowing"], EVERY)
A.mcq("A2.1", "Choose the correct option: My friends ___ football on Sundays.", "play", ["plays", "playing"], MANY)
A.mcq("A2.2", "Choose the correct option: Nobody ___ my name here.", "knows", ["know", "knowing"], EVERY)
A.mcq("A2.2", "Choose the correct option: ___ your parents live near you?", "Do", ["Does", "Is"], DOES)
A.mcq("A2.2", "Choose the correct option: There ___ a big park near my house.", "is", ["are", "be"], THERE)
A.mcq("A2.2", "Which sentence is NOT correct?", "My sister and her husband works in Riga.", ["My sister and her husband work in Riga.", "My sister works in Riga with her husband.", "Tom and Anna are married and live here."], AND, b=4)
A.mcq("A2.1", "At school: Which sentence is NOT correct?", "My friends lives near the school.", ["My friend lives near the school.", "My friends live near the school.", "Our teacher lives in Riga."], MANY, b=4)
A.bank("A2.1", "Tom and his brother ___ to the same school.", "go", ["goes", "going"], AND)
A.bank("A2.1", "My mother ___ in a hospital.", "works", ["work", "working"], ONE)
A.bank("A2.2", "There ___ two cafés near my house.", "are", ["is", "be"], THERE)
A.bank("A2.2", "Everyone in my family ___ coffee.", "likes", ["like", "liking"], EVERY)
A.bank("A2.2", "___ your sister speak English?", "Does", ["Do", "Is"], DOES)
A.gap("A2.1", "My best friend ___ in London. (live)", "lives", ONE)
A.gap("A2.1", "Tom and Anna ___ in London. (live)", "live", AND)
A.gap("A2.2", "Nobody ___ the answer. (know)", "knows", EVERY)
A.gap("A2.2", "There ___ three chairs in the room. (be)", "are", THERE)
A.gap("A2.2", "My sister ___ a car, but my brothers ___ bikes. (have)", "has / have", HAS)
A.gap("A2.1", "Our neighbours ___ a big dog. (have)", "have", HAS)
A.gap("A2.2", "___ your brother like football?", "Does", DOES)
A.gap("A2.2", "___ your parents work on Saturdays?", "Do", DOES)
A.gap("A2.2", "Now there ___ two banks in my street.", "are", THERE)
A.gap("A2.1", "My brother and I ___ twins.", "are", AND)
A.text("A2.2", "Correct the mistake: My sister and her friend works in a café.", "My sister and her friend work in a café.", AND)
A.text("A2.2", "Correct the mistake: Everybody know the rules.", "Everybody knows the rules.", EVERY)
A.text("A2.1", "Rewrite with My friends: My friend lives in Riga.", "My friends live in Riga.", MANY)
A.order("A2.1", "my parents live in a small village", why=MANY)
A.order("A2.2", "does your sister work at the weekend", why=DOES)
A.match("A2.2", "Match each beginning with its ending.",
        [("My sister", "lives in Riga."), ("My sisters", "live in Riga."), ("There", "are two cafés in our street.")],
        ("One: *lives*. More than one: *live*. Two cafés: *there are*.", "Viens: *lives*. Vairāki: *live*. Divas kafejnīcas: *there are*."))

# ============ Irregular plurals (A2.1 / A2.2) ============
I = T("Irregular plurals (children, people, men, teeth)", "IRR-PLURAL",
      "These nouns change in the plural: *child → children, person → people, man → men, woman → women, tooth → teeth, foot → feet, mouse → mice*.",
      "Šie lietvārdi daudzskaitlī mainās: *child → children, person → people, man → men, woman → women, tooth → teeth, foot → feet, mouse → mice*.")
CHILD = ("*child → children* (no *-s*).", "*child → children* (bez *-s*). Tipiska kļūda: *childrens*.")
PERSON = ("*person → people*.", "*person → people*.")
TOOTH = ("*tooth → teeth*.", "*tooth → teeth*. Tipiska kļūda: *tooths*.")
FOOT = ("*foot → feet*.", "*foot → feet*.")
MOUSE = ("*mouse → mice*.", "*mouse → mice*.")
MAN = ("*man → men*, *woman → women*.", "*man → men*, *woman → women*. Tipiska kļūda: *mans, womans*.")
POLICE = ("*police* is always plural: *The police are*.", "*police* vienmēr ir daudzskaitlī: *The police are*.")

I.mcq("A2.1", "Choose the correct option: I have two ___.", "children", ["childs", "childrens"], CHILD)
I.mcq("A2.1", "Choose the correct option: There are ten ___ in the room.", "people", ["person", "peoples"], PERSON)
I.mcq("A2.1", "Choose the correct option: Brush your ___ twice a day.", "teeth", ["tooths", "teeths"], TOOTH)
I.mcq("A2.1", "Choose the correct option: My ___ hurt after the long walk.", "feet", ["foots", "feets"], FOOT)
I.mcq("A2.2", "Choose the correct option: The cat caught two ___.", "mice", ["mouses", "mices"], MOUSE)
I.mcq("A2.2", "Choose the correct option: The police ___ looking for the driver.", "are", ["is", "am"], POLICE)
I.mcq("A2.2", "Which sentence is NOT correct?", "The childrens are playing outside.", ["My feet are cold.", "Two people are waiting.", "The women are laughing."], CHILD, b=4)
replaces("The childrens are playing outside.")
I.mcq("A2.2", "In town: Which sentence is NOT correct?", "The police is here.", ["The police are here.", "Mice are small.", "I have a bad tooth."], POLICE, b=4)
I.mcq("A2.1", "Choose the correct option: Two ___ are waiting outside.", "men", ["mans", "mens"], MAN)
I.bank("A2.2", "Three ___ work in our office.", "women", ["womans", "woman"], MAN)
I.gap("A2.1", "There is one woman and two ___ in the lift. (man)", "men", MAN)
I.gap("A2.2", "One woman, two ___.", "women", MAN)
I.bank("A2.1", "The ___ are in the garden.", "children", ["childs", "child"], CHILD)
I.bank("A2.1", "I have two bad ___.", "teeth", ["tooths", "tooth"], TOOTH)
I.bank("A2.2", "How many ___ live in your town?", "people", ["peoples", "person"], PERSON)
I.bank("A2.2", "We saw three ___ in the kitchen!", "mice", ["mouses", "mouse"], MOUSE)
I.bank("A2.2", "The police ___ asking questions.", "are", ["is", "was"], POLICE)
I.gap("A2.1", "I have one child, and my sister has three ___. (child)", "children", CHILD)
I.gap("A2.1", "I can stand on one foot, but it's easier on two ___. (foot)", "feet", FOOT)
I.gap("A2.2", "The dentist checked all my ___. (tooth)", "teeth", TOOTH)
I.gap("A2.2", "There is one person in the shop and five ___ outside. (person)", "people", PERSON)
I.gap("A2.2", "One mouse is cute, but ten ___ are a problem! (mouse)", "mice", MOUSE)
I.gap("A2.2", "The police ___ here. (be)", "are", POLICE)
I.gap("A2.1", "One tooth, two ___.", "teeth", TOOTH)
I.gap("A2.1", "One mouse, two ___.", "mice", MOUSE)
I.gap("A2.2", "One person, two ___.", "people", PERSON)
I.text("A2.1", "Correct the mistake: My childrens go to school by bus.", "My children go to school by bus.", CHILD)
I.text("A2.1", "Correct the mistake: I brush my tooths every morning.", "I brush my teeth every morning.", TOOTH)
I.text("A2.2", "Correct the mistake: The police is outside.", "The police are outside.", POLICE)
I.text("A2.2", "Rewrite with Two: The mouse is under the bed.", "Two mice are under the bed.", MOUSE)
I.order("A2.1", "the children are playing in the garden", why=CHILD)
I.order("A2.2", "how many people live in your house", why=PERSON)
I.match("A2.1", "Match each word with its plural.",
        [("child", "children"), ("person", "people"), ("man", "men"), ("tooth", "teeth"), ("foot", "feet"), ("mouse", "mice")],
        ("These plurals have no *-s*: learn them as pairs.", "Šiem daudzskaitļiem nav *-s*: mācies tos pa pāriem."))

save("a2-mistakes-1.csv")
