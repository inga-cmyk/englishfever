"""Batch 5, point was_were (A2.1): 6 tasks to reach 10 counted tasks. Murphy unit 10 (was / were), with unit 12 (no did with be)."""
from lib import gp, od, mc, tx
T = "Past simple"
L = "A2.1"

AGR = ("*I / he / she / it* + *was*; *you / we / they* + *were*. A plural noun (*the tickets*) = *they*: *The tickets were …*",
       "*I / he / she / it* + *was*; *you / we / they* + *were*. Daudzskaitļa lietvārds (*the tickets*) = *they*: *The tickets were …*")
Q = ("A question with *be* starts with *Was / Were*, without *did*: *Were your parents …?* *your parents* = *they*, so *Were*.",
     "Jautājums ar *be* sākas ar *Was / Were*, bez *did*: *Were your parents …?* *your parents* = *they*, tāpēc *Were*.")
NEG = ("Negative of *be*: *wasn't / weren't*, without *didn't*. *the shops* = *they*: *The shops weren't busy.*",
       "*be* noliegums: *wasn't / weren't*, bez *didn't*. *the shops* = *they*: *The shops weren't busy.*")
ORDER_YOU = ("Question word + *were* + *you*: *Where were you …?* With *you* it is always *were*, and *be* needs no *did*.",
             "Jautājamais vārds + *were* + *you*: *Where were you …?* Ar *you* vienmēr ir *were*. Ar *be* nelieto *did*.")
ORDER_WH = ("Question word + *was / were* + subject: *Why was your phone off?* No *did* with *be*.",
            "Jautājamais vārds + *was / were* + teik. priekšmets: *Why was your phone off?* Ar *be* nelieto *did*.")
TXQ = ("Move *was* in front of the subject: *Was the exam difficult?* No *did*: not *Did the exam be difficult?*",
       "*was* pārceļ pirms teikuma priekšmeta: *Was the exam difficult?* Bez *did*: nevis *Did the exam be difficult?*")

# choice (1): the point has two choices already
mc(T, L, 2, "Which sentence has a mistake?", "The concert tickets was expensive.",
   ["Were you at the gym on Monday?", "My keys weren't in my bag.", "We were in Riga last weekend."], *AGR)
# word bank (2): Did / didn't are the typical mistake with be; Was / wasn't the agreement mistake
gp(T, L, 3, "___ your parents at the wedding?", "Were", *Q, bank=["Were", "Was", "Did"])
gp(T, L, 3, "The shops ___ busy yesterday.", "weren't", *NEG, bank=["weren't", "wasn't", "didn't"])
# word order (2): where was / were goes in a question with a question word (a yes/no order would also accept the statement)
od(T, L, 3, "Put the words in order.", "where were you at lunchtime", *ORDER_YOU)
od(T, L, 3, "Put the words in order.", "why was your phone off", *ORDER_WH)
# whole sentence (1)
tx(T, L, 4, "Make a yes/no question: The exam was difficult.", "Was the exam difficult? | Was it difficult?", *TXQ)
