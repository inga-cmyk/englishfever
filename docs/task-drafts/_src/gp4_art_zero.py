"""Batch 4, point art_zero (A2.1): no article with plural and uncountable nouns in general and with names of people,
cities and most countries (I like cats. She drinks tea. He lives in Riga.). Murphy, English Grammar in Use, unit 75
(children / the children: no article for things in general; section A, with plural and uncountable nouns, also sports and
school subjects) and unit 77 (names with and without the 1: people, cities, most countries; the UK, the USA as exceptions).
Every sentence either is about a name or makes the general meaning certain (a habit word, a kind-level comparison,
even small ones, a situation that makes the meaning general), so that *the* is wrong and not only a different meaning."""
from lib import gp, od, mc, tx, mt, learning_task
T = "Articles"
L = "A2.1"

NAME = ("No article with names of people, cities and most countries: *Anna, Riga, Latvia*.",
        "Ar cilvēku, pilsētu un lielākās daļas valstu nosaukumiem artikulu nelieto: *Anna, Riga, Latvia*.")
UNC = ("No article with an uncountable noun when we mean it in general: *I don't eat meat.*",
       "Ar neskaitāmu lietvārdu vispārīgā nozīmē artikulu nelieto: *I don't eat meat.*")
PL = ("No article with a plural noun when we mean all of them in general: *Spiders scare me.* With *the* it would mean some particular ones.",
      "Ar daudzskaitļa lietvārdu vispārīgā nozīmē (visi kopumā) artikulu nelieto: *Spiders scare me.* *the* norādītu uz kādiem noteiktiem.")
SPORT = ("Sports and school subjects are uncountable nouns: no article (*play golf, teach maths*). But instruments take *the*: *play the piano*.",
         "Sporta veidi un skolas mācības (matemātika, vēsture) ir neskaitāmi lietvārdi: bez artikula (*play golf, teach maths*). Bet mūzikas instrumentiem vajag *the*: *play the piano*.")

# ── choice (7) ──
# Murphy 77: country name, no article; "a / an Croatia" is the learner who puts an article before every noun
mc(T, L, 2, "Choose the correct option: We went to ___ Croatia last summer.", "—", ["the", "a"], *NAME)
# Murphy 75: school subject in general; "the maths" needs "of ..." to be correct
mc(T, L, 2, "Choose the correct option: My sister teaches ___ maths in Riga.", "—", ["the", "a"], *SPORT)
# the situation is needed: without "I'm vegetarian", "I don't eat the meat" (on this plate) is correct English (cover test)
mc(T, L, 2, "Choose the correct option: I'm vegetarian. I don't eat ___ meat.", "—", ["the", "a"],
   "*I'm vegetarian* = meat in general, so no article: *I don't eat meat.* *The meat* would be some particular meat.",
   "*I'm vegetarian* = gaļa vispārīgi, tāpēc bez artikula: *I don't eat meat.* *The meat* būtu kāda noteikta gaļa.")
mc(T, L, 2, "Which sentence is correct?", "Peter is from Canada.",
   ["Peter is from the Canada.", "The Peter is from Canada.", "The Peter is from the Canada."], *NAME)
mc(T, L, 2, "Which sentence is correct?", "My husband plays golf at weekends.",
   ["My husband plays the golf at weekends.", "My husband plays a golf at weekends."], *SPORT)
# NOT correct: the other three are about three different things (uncountable, plural, the UK)
mc(T, L, 2, "Which sentence is NOT correct?", "My parents live in the Spain.",
   ["We eat fish on Fridays.", "Tom collects old cameras.", "They live in the UK."],
   "Most countries have no article: *Spain, Latvia*. A few names take *the*: *the UK, the USA*.",
   "Lielākajai daļai valstu artikula nav: *Spain, Latvia*. Daži nosaukumi ir ar *the*: *the UK, the USA*.")
mc(T, L, 2, "Which sentence is NOT correct?", "She studies the history at university.",
   ["Anna and her sister live in Paris.", "Horses need a lot of space to run.", "I don't drink milk with my coffee."],
   "School subjects in general have no article: *She studies history.* (*the history of Rome* is one particular history.)",
   "Skolas mācībām (vēsture, matemātika) vispārīgi artikula nav: *She studies history.* (*the history of Rome* ir kāda noteikta vēsture.)")

# ── word order (5) ──
# moving the card gives "the green tea in morning": wrong, so one place for "the"
od(T, L, 3, "Put the words in order.", "i drink green tea in the morning", *UNC, also=["in the morning i drink green tea"])
od(T, L, 3, "Put the words in order.", "my grandfather doesn't like computers", *PL)
od(T, L, 3, "Put the words in order.", "my wife and i met in paris", *NAME)
od(T, L, 3, "Put the words in order to make a question.", "do you like classical music", *UNC)
od(T, L, 3, "Put the words in order.", "we want to visit japan next year", *NAME, also=["next year we want to visit japan"])

# ── word bank (4): "the" is the mistake of this point; "a" left out where it builds no form anyone writes ──
gp(T, L, 3, "Our new manager is from ___ Sweden.", "—", *NAME, bank=["—", "the"])
gp(T, L, 3, "I usually listen to ___ jazz in the car.", "—",
   "Kinds of music in general have no article: *I listen to jazz.* *usually* shows it is a habit, not one particular piece.",
   "Mūzikas veidiem vispārīgi artikula nav: *I listen to jazz.* *usually* rāda, ka tas ir ieradums, nevis kāds noteikts skaņdarbs.",
   bank=["—", "the"])
# "than cats" is general, so "the dogs" (particular dogs) does not fit the comparison
gp(T, L, 3, "I think ___ dogs are better pets than cats.", "—", *PL, bank=["—", "the"])
gp(T, L, 3, "My kids spend hours on ___ social media.", "—", *UNC, bank=["—", "the"])

# ── matching (1, learning) ──
mt(T, L, 2, "Match each beginning with its ending.", [("My cousin lives in", "Rome."), ("Every morning I drink", "orange juice."),
   ("My daughter is afraid of", "snakes."), ("At weekends we play", "volleyball.")],
   "No article with names (*Rome*), uncountable nouns (*orange juice*, *volleyball*) and plurals (*snakes*) in general.",
   "Bez artikula: nosaukumi (*Rome*), neskaitāmi lietvārdi (*orange juice*, *volleyball*) un daudzskaitlis (*snakes*) vispārīgā nozīmē.")

# ── typed gap (5): the learner writes the noun from the brackets; the right form is the plural with no article ──
gp(T, L, 3, "My daughter is afraid of ___, even small ones. (spider)", "spiders", *PL)
gp(T, L, 3, "In big cities, ___ are often faster than cars. (bike)", "bikes", *PL)
gp(T, L, 3, "___ are cheaper than laptops. (tablet)", "tablets", *PL)
gp(T, L, 3, "___ are my favourite flowers. (rose)", "roses", *PL)
gp(T, L, 3, "My son collects ___. He has hundreds. (stamp)", "stamps",
   "A hobby is about the things in general: *He collects stamps.* Plural, no article.",
   "Hobijs ir par lietām vispārīgi: *He collects stamps.* Daudzskaitlis, bez artikula.")

# ── whole sentence (3) ──
tx(T, L, 4, "Correct the mistake: My uncle works in the London.", "My uncle works in London.", *NAME)
tx(T, L, 4, "Correct the mistake: We play the basketball on Fridays.", "We play basketball on Fridays. | On Fridays we play basketball.", *SPORT)
tx(T, L, 4, "Correct the mistake: I eat the bread with every meal.", "I eat bread with every meal.",
   "*with every meal* = a habit, bread in general: no article.", "*with every meal* = ieradums, *bread* vispārīgā nozīmē: bez artikula.")
