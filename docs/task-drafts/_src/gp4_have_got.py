"""Batch 4, point have_got (A2.1): have got / has got and have for possession, with the negative, the question and the short
answer of each (I haven't got / I don't have, Have you got …? / Do you have …?, Yes, I have.). Murphy unit 17.
No past (had) at this level. Old-fashioned British forms without got or do (I haven't a car, Has she a car?) are never wrong
options (Murphy 17: 'less usual'); in typed negatives and questions they are accepted."""
from lib import gp, od, mc, tx, mt, learning_task
T = "Auxiliary verbs: be, do, have (Are you…? Do you…? Have you…?)"
L = "A2.1"

HG = ("*have got* = *have* (own). *I / you / we / they have got*, *he / she / it has got*: *She's got two sisters.*",
      "*have got* = *have* (piederēt). *I / you / we / they have got*, *he / she / it has got*: *She's got two sisters.*")
Q = ("Question: *Have / Has* + subject + *got*: *Has she got a car?* Or with *do*: *Does she have a car?* Not *Does she have got …?*",
     "Jautājums: *Have / Has* + teik. priekšmets + *got*: *Has she got a car?* Vai ar *do*: *Does she have a car?* Nevis *Does she have got …?*")
NEG = ("Negative: *haven't got / hasn't got* or *don't have / doesn't have*. *got* never comes after *do*: not *don't have got*.",
       "Noliegums: *haven't got / hasn't got* vai *don't have / doesn't have*. Aiz *do* nekad nav *got*: nevis *don't have got*.")
DO = ("After *do / does / don't / doesn't* use *have*: no *-s*, no *got*: *Does she have …? We don't have …*",
      "Aiz *do / does / don't / doesn't* lieto *have*: bez *-s*, bez *got*: *Does she have …? We don't have …*")
SHORT = ("A short answer to *Have you got …?* repeats *have / has* without *got*: *Yes, I have. No, she hasn't.* To *Do you have …?*: *Yes, I do.*",
         "Īsajā atbildē uz *Have you got …?* atkārto *have / has* bez *got*: *Yes, I have.* (nevis *Yes, I have got.*) Uz *Do you have …?*: *Yes, I do.*")
STATE = ("*have* (own) is a state: no *-ing*. *She has got blue eyes*, not *She is having blue eyes*.",
         "*have* (piederēt) ir stāvoklis: bez *-ing*. *She has got blue eyes*, nevis *She is having blue eyes*.")

# ── choose (7) ──
# a. question with have got, plural subject: Have, not Has / Do / Are
mc(T, L, 2, "Choose the correct option: ___ your neighbours got a dog?", "Have", ["Has", "Do", "Are"],
   "*your neighbours* = *they*: *Have they got …?* With *got* the question starts with *have / has*, not *do* or *are*.",
   "*your neighbours* = *they*: *Have they got …?* Ar *got* jautājums sākas ar *have / has*, nevis *do* vai *are*.")
# b. three typical mistakes in one question
mc(T, L, 2, "Which sentence is correct?", "Has your office got a kitchen?",
   ["Does your office have got a kitchen?", "Have your office got a kitchen?", "Is your office having a kitchen?"], *Q)
# c. negative with does
mc(T, L, 2, "Which sentence is correct?", "She doesn't have a laptop at home.",
   ["She doesn't has a laptop at home.", "She doesn't have got a laptop at home.", "She don't have a laptop at home."], *DO)
# d. short answer
mc(T, L, 2, "Choose the correct short answer: 'Have you got a bike?'", "Yes, I have.", ["Yes, I have got.", "Yes, I am.", "Yes, I've."], *SHORT)   # blind check r9: "Yes, I do." is heard too
# e. negative with have got
mc(T, L, 2, "Choose the correct option: We ___ any milk.", "haven't got", ["don't have got", "hasn't got", "not have got"], *NEG)
# f. NOT correct: three different correct uses
mc(T, L, 2, "Which sentence is NOT correct?", "My sister is having blue eyes.",
   ["Have you got any plans for Saturday?", "Our flat doesn't have a lift.", "My phone's got a great camera."], *STATE)
# g. question word + has + subject + got
mc(T, L, 2, "Choose the correct option: What kind of car ___ got?", "has she", ["she has", "does she", "have she"],
   "Question word + *has* + subject + *got*: *What kind of car has she got?* Or: *What kind of car does she have?*",
   "Jautājamais vārds + *has* + teik. priekšmets + *got*: *What kind of car has she got?* Vai: *What kind of car does she have?*")

# ── word order (5) ──
od(T, L, 3, "Put the words in order to make a question.", "have you got a minute", *Q)
od(T, L, 3, "Put the words in order.", "my brother hasn't got a driving licence", *NEG)
od(T, L, 3, "Put the words in order to make a question.", "does your flat have a balcony", *DO, also=["your flat does have a balcony"])   # the instruction becomes "Put the words in order." (plain()); the stressed statement is correct English
od(T, L, 3, "Put the words in order.", "we don't have time for lunch today", *NEG, also=["today we don't have time for lunch", "we don't have time today for lunch"])   # r9
od(T, L, 3, "Put the words in order.", "my gym has got a new sauna", *HG, also=["my new gym has got a sauna"])   # r9

# ── word bank (4): the wrong chips build the typical mistakes of this point ──
gp(T, L, 3, "Does this bus ___ wifi?", "have", *DO, bank=["have", "has", "have got"])
gp(T, L, 3, "My parents ___ ___ a big garden.", "have / got", *STATE, bank=["have", "got", "are", "having"])
gp(T, L, 3, "Sorry, I ___ ___ any change.", "haven't / got", *NEG, bank=["haven't", "got", "don't"])
gp(T, L, 3, "___ the room ___ a fridge?", "Has / got", *Q, bank=["Has", "got", "Does"])

# ── matching (1): a learning task (the subject AND the first word of the question decide) ──
mt(T, L, 2, "Match each question with its short answer.",
   [("Have you got a pen?", "Yes, I have."), ("Do they have a garden?", "No, they don't."),   # r9: one pronoun per pair
    ("Has Mark got a job?", "No, he hasn't."), ("Does Anna have a sister?", "Yes, she does.")], *SHORT)

# ── typed gap (5) ──
gp(T, L, 3, "My sister ___ three cats. (have got)", "has got | 's got", *HG)
gp(T, L, 3, "We ___ a car, so we cycle to work. (not / have got)", "haven't got | have not got | don't have | do not have", *NEG)   # r9
gp(T, L, 3, "'Has the new library got a café?' 'Yes, it ___.'", "has", *SHORT)
gp(T, L, 3, "___ you ___ an umbrella? (have got)", "Have / got", *Q)
gp(T, L, 3, "My grandparents ___ a computer. (not / have)", "don't have | haven't got | haven't | have no", *NEG)

# ── whole sentence (3): both the have got form and the do form are accepted ──
tx(T, L, 4, "Make it negative: My laptop has got a camera.",
   "My laptop hasn't got a camera. | My laptop doesn't have a camera. | My laptop has no camera. | My laptop hasn't a camera.", *NEG)
tx(T, L, 4, "Make a yes/no question: Tom has got a motorbike.",
   "Has Tom got a motorbike? | Does Tom have a motorbike? | Has Tom a motorbike?", *Q)
tx(T, L, 4, "Make a question with *How many*: She has got two children.",
   "How many children has she got? | How many children does she have? | How many children has she? | How many kids has she got? | How many kids does she have?", *Q)
