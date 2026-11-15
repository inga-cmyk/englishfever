"""Batch 4, point each_every (B1.2): each, every, all, whole. Murphy units 90 (all, every and whole) and 91 (each and every).
every / each + singular noun + singular verb (Every room has…, Each student gets…); each of + the / my / them + plural noun,
usually with a singular verb (Murphy 91: Each of the books is…; a plural verb is heard: accepted in typed tasks, never a wrong
option); every cannot stand alone or before of (each of them, every one of them, not every of them); each for two things
(each hand, Murphy 91); almost every / every single, not almost each (Murphy 91); all day (= the whole day) vs every day
(= on each day), and all day, not all the day (Murphy 90); the whole + noun, my whole life (= all my life), not my all life,
not whole the day (Murphy 90). No task makes the learner choose between each and every where both fit."""
from lib import gp, od, mc, tx, mt, learning_task
T = "Subject and verb (my friend lives, my friends live)"
L = "B1.2"

EV = ("*every* and *each* + singular noun + singular verb: *Every room has…*, *Each student gets…*.",
      "Aiz *every* un *each* ir lietvārds vienskaitlī un darbības vārds vienskaitlī: *Every room has…*, *Each student gets…*.")
EACH_OF = ("*each of* + *the / my / them* + plural noun: *each of the flats*, *each of my brothers*. *every* cannot go before *of*: say *every one of them*.",
           "Tulkojot burtiski *katrs no…*, gribas teikt *every of*. Angliski saka *each of* + *the / my / them* + daudzskaitlis (*each of the flats*) vai *every one of them*.")
ALL_DAY = ("*all day* = the whole day, from morning to evening (no *the*: not *all the day*); *every day* = on each day: Monday, Tuesday…",
           "*all day* = visu dienu, no rīta līdz vakaram (bez *the*); *every day* = katru dienu: pirmdien, otrdien…")
WHOLE = ("*whole* comes after *the / my*: *the whole day*, *my whole life* (= *all day*, *all my life*). Not *my all life*, not *whole the day*.",
         "*whole* liek aiz *the / my*: *the whole day*, *my whole life* (= *all day*, *all my life*). Nevis *my all life* un nevis *whole the day*.")
TWO = ("For two things use *each*, not *every*: *in each hand*, *on each side*. *both* needs a plural noun: *in both hands*.",
       "Divām lietām lieto *each*, nevis *every*: *in each hand*, *on each side*. Aiz *both* ir daudzskaitlis: *in both hands*.")
ALMOST = ("We say *almost every* and *every single*, not *almost each*: *almost every colleague*.",
          "Saka *almost every* un *every single*, nevis *almost each*: *almost every colleague*.")

# ── choose (7) ──
mc(T, L, 2, "Choose the correct option: ___ in our new hotel has a balcony, so guests can have breakfast outside.", "Every room",
   ["Every rooms", "All room", "Each of room"], *EV)
mc(T, L, 2, "Choose the correct option: At the end of the course, each ___ a certificate, even if they missed a class.", "student gets",
   ["students get", "student get", "students gets"], *EV)
mc(T, L, 2, "Choose the correct option: I've known Marta ___ because our mothers were best friends.", "my whole life",
   ["my all life", "whole my life", "the whole my life"], *WHOLE)
mc(T, L, 2, "Choose the correct option: I was so tired after the night flight that I stayed in bed ___ on Sunday.", "all day",
   ["every day", "all the days", "whole day"], *ALL_DAY)
mc(T, L, 2, "Which sentence is correct?", "Each of the flats in our building has its own parking space.",
   ["Each of flats in our building has its own parking space.", "Every of the flats in our building has its own parking space.",
    "Each the flats in our building has its own parking space."], *EACH_OF)
mc(T, L, 2, "Which sentence is NOT correct?", "Every player in our club get a free shirt in spring.",
   ["The whole village came to watch the concert in the park.", "It snowed all day, so most of the trains were late.",
    "Almost every shop in the centre closes at six."],
   "*every* + singular noun + singular verb: *Every player gets*, not *get*. The other three are correct: *the whole village*, *all day*, *almost every shop … closes*.",
   "Aiz *every* darbības vārds ir vienskaitlī: *Every player gets*, nevis *get*. Pārējie trīs ir pareizi: *the whole village*, *all day*, *almost every shop … closes*.")
mc(T, L, 2, "Choose the correct option: She was carrying a heavy bag in ___ hand, so she couldn't open the door.", "each",
   ["every", "all", "both"], *TWO)

# ── type a word (5): the instruction names the two words where other words would also fit ──
gp(T, L, 3, "Write *each* or *every*: We tried three new apps for learning Spanish, and ___ of them was useful.", "each",
   "*every* cannot go before *of*: *each of them* (or *every one of them*).",
   "Tulkojot burtiski *katrs no tiem*, gribas teikt *every of them*. Pirms *of* lieto *each*: *each of them* (vai *every one of them*).")
gp(T, L, 3, "Write *all* or *every*: The museum is open ___ day except Monday, from ten until six.", "every",
   "*every day* = on each day (here all days but Monday). *all day* = one whole day, from morning to evening.",
   "*every day* = katru dienu (te visas dienas, izņemot pirmdienu). *all day* = visu vienu dienu, no rīta līdz vakaram.")
gp(T, L, 3, "Every laptop in our office ___ the same password, which is not very safe. (have)", "has | has got", *EV)
gp(T, L, 3, "Each of the ___ on our walking tour got a free map of the old town. (visitor)", "visitors",
   "*each of the* + plural noun: *each of the visitors*. Without *of*: *each visitor*.",
   "Aiz *each of the* ir daudzskaitlis: *each of the visitors*. Bez *of*: *each visitor*.")
gp(T, L, 3, "Write *all* or *whole*: The ___ team stayed late on Friday to finish the project on time.", "whole",
   "After *the* use *whole*: *the whole team*. *all* comes before *the*: *all the team*.",
   "Aiz *the* lieto *whole*: *the whole team*. *all* liek pirms *the*: *all the team*.")

# ── whole sentence (3) ──
tx(T, L, 4, "Say it another way with *whole*: I spent all day at the airport because my flight was cancelled.",
   "I spent the whole day at the airport because my flight was cancelled. | Because my flight was cancelled, I spent the whole day at the airport.",
   *WHOLE)
tx(T, L, 4, "Say it another way with *every*: All the lessons at our language school last ninety minutes.",
   "Every lesson at our language school lasts ninety minutes. | Every lesson at our language school lasts 90 minutes. | "
   "Every single lesson at our language school lasts ninety minutes. | Every single lesson at our language school lasts 90 minutes. | "
   "Every one of the lessons at our language school lasts ninety minutes. | Every one of the lessons at our language school lasts 90 minutes. | "
   "Every one of the lessons at our language school last ninety minutes. | Every one of the lessons at our language school last 90 minutes.",
   "*all the* + plural noun + plural verb (*All the lessons last*); *every* + singular noun + singular verb (*Every lesson lasts*).",
   "Aiz *all the* ir daudzskaitlis (*All the lessons last*); aiz *every* ir vienskaitlis un darbības vārds ar *-s* (*Every lesson lasts*).")
tx(T, L, 4, "Make a yes/no question: Every member of the team has access to the shared folder.",
   "Does every member of the team have access to the shared folder? | Has every member of the team got access to the shared folder?",
   "*every member* is singular, so the question uses *does*: *Does every member … have …?* After *does* the verb is *have*, not *has*.",
   "*every member* ir vienskaitlī, tāpēc jautājumā lieto *does*: *Does every member … have …?* Aiz *does* ir *have*, nevis *has*.")

# ── word order (5) ──
od(T, L, 3, "Put the words in order.", "each of my sisters lives in a different country so we talk online",
   "*each of my sisters* + singular verb: *lives*.", "*each of my sisters* + darbības vārds vienskaitlī: *lives*.")
od(T, L, 3, "Put the words in order to make a question.", "does every guest need a ticket for tomorrow's boat trip",
   "*every guest* is singular: *Does every guest need …?*", "*every guest* ir vienskaitlī: *Does every guest need …?*")
od(T, L, 3, "Put the words in order.", "we were stuck in traffic all day and missed the start of the wedding", *ALL_DAY)
od(T, L, 3, "Put the words in order.", "i missed the match because i spent the whole evening answering emails", *WHOLE,
   also=["because i spent the whole evening answering emails i missed the match"])
od(T, L, 3, "Put the words in order.", "i've read every single review but i can't decide which phone to buy", *ALMOST,
   also=["i can't decide which phone to buy but i've read every single review"])

# ── word bank (4): the wrong chips are the mistakes of this point; no plural-verb chip after each of (a plural verb is heard there) ──
gp(T, L, 3, "Each of my ___ ___ a different hobby, so family weekends are never boring.", "brothers / has",
   "*each of my* + plural noun + singular verb: *each of my brothers has*. Not *each of my brother*.",
   "Aiz *each of my* ir daudzskaitlis, darbības vārds vienskaitlī: *each of my brothers has*. Nevis *each of my brother*.",
   bank=["brothers", "has", "brother"])
gp(T, L, 3, "I've had a headache ___ ___ morning, so I'm going home early.", "the / whole", *WHOLE, bank=["the", "whole", "every"])
gp(T, L, 3, "My grandmother phones me ___ ___, usually just after her lunch, to ask about the kids.", "every / day",
   "*every day* = on each day (a habit); *all day* = from morning to evening. *whole* needs *the*: *the whole day*.",
   "*every day* = katru dienu (ieradums); *all day* = no rīta līdz vakaram. Aiz *whole* vajag *the*: *the whole day*.",
   bank=["every", "day", "all", "whole"])
gp(T, L, 3, "Almost ___ colleague in my team works from home on Fridays, so the office is very quiet.", "every", *ALMOST,
   bank=["every", "each", "all"])

# ── matching (1): a learning task automatically; each ending fits only its own beginning (of + them / singular noun / plural noun / room) ──
mt(T, L, 2, "Match each beginning with its ending.", [
   ("We invited forty people, and each of", "them brought a small gift."),
   ("It was a long night, but every", "guest stayed until the end."),
   ("The food was great, and all the", "guests asked for the recipes."),
   ("When the band started, the whole", "room got up to dance.")],
   "*each of them*; *every* + singular noun and verb (*every guest stayed*); *all the* + plural noun (*all the guests*); *the whole room*.",
   "*each of them*; aiz *every* vienskaitlis (*every guest stayed*); aiz *all the* daudzskaitlis (*all the guests*); *the whole room*.")
