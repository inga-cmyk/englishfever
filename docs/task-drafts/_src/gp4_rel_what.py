"""Batch 4, point rel_what (B1.2): what = the thing(s) that. Murphy unit 93 (section D: Everything (that) they said was true,
not Everything what; What = the thing(s) that: Did you hear what they said?; also unit 92 for that / which after a noun).
what has no noun before it (I didn't hear what he said. What I need is a holiday.); after a noun use that / which (or nothing
when it is the object); after everything / something / anything / all use that (or nothing), not what.
Wrong options: what after a noun or everything / all (the Latvian kas / ko mistake), that or which for the thing that, nothing at all
where what is needed. Where 'which' could be read as 'which one' (I can't remember which he chose) it is never a wrong option;
where nothing (zero) is correct after a noun, it is never a wrong option either."""
from lib import gp, od, mc, tx, mt, learning_task
T = "Relative clauses"
L = "B1.2"

WHAT = ("*what* = the thing(s) that, with no noun before it: *I didn't hear what he said.* *that* and *which* cannot mean *the thing that*.",
        "*what* = tas, ko / tas, kas; pirms tā nav lietvārda: *I didn't hear what he said.* *that* un *which* šeit nevar aizstāt *what*.")
WHAT_S = ("A *what*-clause can be the subject: *What I need is a holiday.* (= The thing that I need is a holiday.)",
          "Teikums var sākties ar *what*: *What I need is a holiday.* (= Tas, kas man vajadzīgs, ir atvaļinājums.)")
NOUN = ("After a noun use *that* or *which* (or nothing when it is the object), not *what*: *the jacket (that) I ordered*.",
        "Aiz lietvārda lieto *that* vai *which* (vai neko, ja tas ir papildinātājs), nevis *what*: *the jacket (that) I ordered*.")
EVERY = ("After *everything, something, anything, all* use *that* (or nothing), not *what*: *Everything (that) he said was true.*",
         "Tulkojot burtiski „viss, ko viņš teica”, sanāk *everything what he said*. Angliski aiz *everything, something, anything, all* lieto *that* (vai neko): *Everything (that) he said was true.*")

# choose (7)
mc(T, L, 2, "Choose the correct option: Sorry, I didn't hear ___ you said about the meeting time.", "what", ["that", "—"], *WHAT)
# 'which' left out on purpose: 'I didn't hear which (one) you said' is a question form for some readers
mc(T, L, 2, "Choose the correct option: The jacket ___ I ordered online last week doesn't fit me.", "which", ["what", "who", "where"], *NOUN)
mc(T, L, 2, "Which sentence is correct?", "Everything that he told us about the hotel was true.",
   ["Everything what he told us about the hotel was true.", "All what he told us about the hotel was true."], *EVERY)
mc(T, L, 2, "Which sentence is correct?", "What I really need right now is a long holiday.",
   ["That I really need right now is a long holiday.", "Which I really need right now is a long holiday.",
    "The thing what I really need right now is a long holiday."], *WHAT_S)
mc(T, L, 2, "Which sentence is NOT correct?", "The film what we watched last night was far too long.",
   ["I couldn't believe what I saw at the airport.", "Everything she cooked for the party was delicious.",
    "Tell me what you think of my new haircut."],
   "After a noun use *that* or *which* (or nothing), not *what*: *The film (that) we watched last night was far too long.*",
   "Aiz lietvārda lieto *that* vai *which* (vai neko), nevis *what*: *The film (that) we watched last night was far too long.*")
mc(T, L, 2, "Which sentence is NOT correct?", "All what I want for my birthday is a quiet dinner.",
   ["The shoes that I use for running are very light.", "What surprised me most was the price of coffee.",
    "I'll tell you everything I know about the job."],
   "After *all* use *that* or nothing, not *what*: *All (that) I want for my birthday is a quiet dinner.*",
   "Tulkojot burtiski „viss, ko es gribu”, sanāk *all what I want*. Angliski aiz *all* lieto *that* vai neko: *All (that) I want for my birthday is a quiet dinner.*")
mc(T, L, 2, "Choose the correct option: That's exactly ___ I was trying to explain to my boss.", "what", ["that", "which", "—"], *WHAT)

# type a word (5): the instruction names the two words, because all / everything / something also fit some of these gaps
gp(T, L, 3, "Write *what* or *that*: The pizza ___ we ordered last night was cold when it arrived.", "that", *NOUN)
gp(T, L, 3, "Write *what* or *that*: I can't remember ___ the teacher said about the exam.", "what", *WHAT)
gp(T, L, 3, "Write *what* or *that*: Is there anything ___ I can do to help you with the move?", "that", *EVERY)
gp(T, L, 3, "Write *what* or *that*: ___ worries me most about the trip is the cost of the flights.", "What | what", *WHAT_S)
gp(T, L, 3, "Write *what* or *that*: The app ___ my sister recommended really helps me sleep better.", "that", *NOUN)

# whole sentence (3)
tx(T, L, 4, "Say it another way with *what*: The thing I enjoy most about my job is meeting new people.",
   "What I enjoy most about my job is meeting new people. | Meeting new people is what I enjoy most about my job.", *WHAT_S)
tx(T, L, 4, "Correct the mistake: Everything what she told me about the course was useful.",
   "Everything that she told me about the course was useful. | Everything she told me about the course was useful. | "
   "Everything which she told me about the course was useful. | What she told me about the course was useful.", *EVERY)
tx(T, L, 4, "Correct the mistake: I didn't understand that the mechanic said about my car.",
   "I didn't understand what the mechanic said about my car. | I didn't understand everything that the mechanic said about my car. | "
   "I didn't understand everything the mechanic said about my car. | I didn't understand all that the mechanic said about my car. | "
   "I didn't understand all the mechanic said about my car.",
   "*that* cannot mean *the thing that*: *I didn't understand what the mechanic said*. *said* needs an object, and *what* is it.",
   "*that* šeit nevar aizstāt *what*: *I didn't understand what the mechanic said*. Aiz *said* vajag papildinātāju, un tas ir *what*.")

# word order (5)
od(T, L, 3, "Put the words in order.", "what she said at the wedding surprised everyone", *WHAT_S,
   also=["what she said surprised everyone at the wedding", "at the wedding what she said surprised everyone"])
od(T, L, 3, "Put the words in order.", "i didn't understand what the doctor told me about the test", *WHAT)
od(T, L, 3, "Put the words in order.", "all i want after work is a hot shower", *EVERY, also=["after work all i want is a hot shower", "all i want is a hot shower after work"])
od(T, L, 3, "Put the words in order.", "i'm sorry about everything that happened last night", *EVERY)
od(T, L, 3, "Put the words in order to make a question.", "did you find what you were looking for", *WHAT)

# word bank (4): the wrong chips are the mistakes of this point; nothing (zero) is never a possible answer because a chip must be used
gp(T, L, 3, "___ really annoyed me was the noise from the street.", "What", *WHAT_S, bank=["What", "That", "Which"])
gp(T, L, 3, "I'll send you everything ___ you need for the conference.", "that", *EVERY, bank=["that", "what"])
gp(T, L, 3, "The best thing about the trip was the people ___ we met on the way.", "that", *NOUN, bank=["that", "what", "which"])
gp(T, L, 3, "Excuse me, this isn't ___ I ordered.", "what", *WHAT, bank=["what", "that", "which"])

# matching (1): a learning task automatically. Each beginning takes only its own ending
mt(T, L, 2, "Match each beginning with its ending.", [
   ("Thank you so much for everything", "you did for my family."),
   ("The waiter didn't understand", "what I wanted to order."),
   ("The laptop that I bought last month", "stopped working after a week."),
   ("What I like most about my job", "is the people I work with.")],
   "*what* without a noun before it (*didn't understand what I wanted*, *What I like most … is*); after *everything* or a noun, *that* or nothing (*everything you did*, *the laptop that I bought*).",
   "*what* bez lietvārda pirms tā (*didn't understand what I wanted*, *What I like most … is*); aiz *everything* vai lietvārda *that* vai nekas (*everything you did*, *the laptop that I bought*).")
