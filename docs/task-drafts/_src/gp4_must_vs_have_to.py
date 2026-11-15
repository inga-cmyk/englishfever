"""Batch 4, point must_vs_have_to (B1.1): must or have to. Murphy unit 31 (must and have to), with unit 32 (mustn't / don't have to).
Teacher's decision (15 November): Murphy's "must = my own view, have to = somebody else's rule" is a British tendency, not a rule;
native speakers often use both. So the check / use tasks test only places where one form is really wrong: the past (had to,
didn't have to, Did … have to), the future after will (will have to, not will must), have to after another verb (might / will /
going to have to), questions and negatives with do / does (not Do I must, Have I to, Has she to, hasn't to), has to with he / she,
and mustn't (not allowed) against don't have to (not necessary) where the situation makes one meaning certain.
must and have to are never wrong options against each other in present-time obligation; in typed tasks both are accepted where
both are correct English. The meaning tendency (my view / a rule) appears only in two learning tasks: the meaning question
(learning_task()) and the matching task (learning automatically). Must I …? is correct (formal; on the card) and never a wrong option."""
from lib import gp, od, mc, tx, mt, learning_task
T = "Modal verbs"
L = "B1.1"

PAST = ("For the past use *had to*: *must* has no past form for obligation (not *must*, *have to* or *musted* with *last winter*).",
        "Pagātnē lieto *had to*: pienākumam *must* pagātnes formas nav (nevis *must*, *have to* vai *musted*, ja ir *last winter*).")
PASTQ = ("Past question: *Did* + subject + *have to*: *Did you have to show your passport?* After *did* the verb is *have*, not *had*.",
         "Jautājums pagātnē: *Did* + teik. priekšmets + *have to*: *Did you have to show your passport?* Aiz *did* ir *have*, nevis *had*.")
PASTNEG = ("Past negative: *didn't have to* = it was not necessary: *We didn't have to queue.*",
           "Noliegums pagātnē: *didn't have to* = nebija vajadzības: *We didn't have to queue.*")
FUT = ("*must* cannot follow *will*: use *will have to* (*we'll have to buy a new one*).",
       "Aiz *will* nevar likt *must*: lieto *will have to* (*we'll have to buy a new one*).")
MOD = ("*must* never follows another verb such as *might*, *will* or *going to*: use *have to* (*we might have to find …*, *we're going to have to …*).",
       "*must* nekad neliek aiz cita darbības vārda, piemēram, *might*, *will* vai *going to*: lieto *have to* (*we might have to find …*, *we're going to have to …*).")
Q = ("Questions with *have to* use *do / does*: *Do I have to …? Does she have to …?* Not *Do I must*, *Have I to* or *Has she to*.",
     "Jautājumos ar *have to* lieto *do / does*: *Do I have to …? Does she have to …?* Nevis *Do I must*, *Have I to* vai *Has she to*.")
HAS = ("With *he / she / it* use *has to*: *she has to have a medical check*. *must* is correct too and does not change.",
       "Ar *he / she / it* lieto *has to*: *she has to have a medical check*. Der arī *must*, un tas nemainās.")
DOESNT = ("*doesn't have to* = it is not necessary: *she doesn't have to come in*. With *he / she* use *doesn't*, not *don't*; *hasn't to* is not English.",
          "*doesn't have to* = nav vajadzības: *she doesn't have to come in*. Ar *he / she* lieto *doesn't*, nevis *don't*. *hasn't to* angliski nesaka.")
MUSTNT = ("*mustn't* = it is not allowed, or it is important not to do it: the tablets make you sleepy. *don't have to* would mean it is not necessary.",
          "*mustn't* = nedrīkst: tabletes rada miegainību. *don't have to* nozīmētu, ka nav vajadzības. Tulkojot burtiski, *must not* šķiet 'nav jā…', bet 'nav jā…' ir *don't have to*.")
DONT = ("*don't have to* = it is not necessary: the classes are included. *mustn't* would mean it is not allowed.",
        "*don't have to* = nav vajadzības: nodarbības jau ir iekļautas. *mustn't* nozīmētu 'nedrīkst'. Tulkojot burtiski, 'nav jā…' šķiet *must not*, bet *mustn't* ir 'nedrīkst'.")
MEAN = ("In British English *must* often shows the speaker's own feeling (*I must drink less coffee*), *have to* a rule or a situation (*Staff have to wear a badge*). Very often both are possible.",
        "Britu angļu valodā *must* bieži izsaka paša runātāja sajūtu (*I must drink less coffee*), *have to* noteikumu vai situāciju (*Staff have to wear a badge*). Ļoti bieži der abi.")
FORMS = ("*must* = I feel it is necessary; *had to* = it was necessary; *don't have to* = it is not necessary; *Do I have to …?* asks if it is necessary.",
         "*must* = es jūtu, ka tas ir vajadzīgs; *had to* = tas bija vajadzīgs; *don't have to* = nav vajadzības; *Do I have to …?* jautā, vai tas ir vajadzīgs.")

# ── choose (7 check + 1 learning) ──
# 1. past: had to; must / have to / musted all miss the past (last winter)
mc(T, L, 2, "Choose the correct option: My knee hurt so much last winter that I ___ stop running for two months.",
   "had to", ["must", "have to", "musted"], *PAST)
# 2. after might: have to, never must
mc(T, L, 2, "Choose the correct option: The hotel is almost full, so we ___ find somewhere else to stay tonight.",
   "might have to", ["might must", "might to", "must have to"], *MOD)
# 3. he / she question: Does … have to
mc(T, L, 2, "Which sentence is correct?", "Does your brother have to work late when the restaurant is busy?",
   ["Does your brother has to work late when the restaurant is busy?", "Has your brother to work late when the restaurant is busy?",
    "Do your brother have to work late when the restaurant is busy?"], *Q)
# 4. I question: Do I have to (Must I is correct and not offered)
mc(T, L, 2, "Choose the correct option: ___ show my student card every time I use the library?",
   "Do I have to", ["Do I must", "Have I to", "Must I to"],
   "Questions with *have to* use *do*: *Do I have to show …?* Not *Do I must* or *Have I to*, and no *to* after *must*.",
   "Jautājumos ar *have to* lieto *do*: *Do I have to show …?* Nevis *Do I must*, *Have I to* vai *Must I to*.")
# 5. she + not necessary: doesn't have to (mustn't is not offered: it would make sense too)
mc(T, L, 2, "Choose the correct option: My manager ___ come to the office on Fridays, so she usually works from home.",
   "doesn't have to", ["hasn't to", "don't have to", "doesn't must"], *DOESNT)
# 6. not allowed / important not to: mustn't
mc(T, L, 2, "Choose the correct option: These tablets can make you sleepy, so you ___ drive after taking them.",
   "mustn't", ["don't have to", "don't must", "mustn't to"], *MUSTNT)
# 7. NOT correct: will must; the other three are a past, a might and a question
mc(T, L, 2, "Which sentence is NOT correct?", "From May, drivers will must pay to enter the city centre.",
   ["We had to wait an hour for a doctor at the clinic yesterday.", "You might have to show your ID when you buy the tickets.",
    "Do you have to pay for parking at your new office?"], *FUT)
# 8. learning: the British tendency (my own feeling / a rule), never evidence
mc(T, L, 2, "Which sentence is the speaker's own idea, not a rule?", "I must drink less coffee in the evenings.",
   ["Staff have to wear a badge in the building.", "Passengers have to show their tickets on the train.", "Students have to hand in the essay by Friday."], *MEAN)
learning_task()

# ── word order (5) ──
od(T, L, 3, "Put the words in order to make a question.", "do we have to print our boarding passes", *Q)   # blind check r10: 14 cards was too long for B1.1
od(T, L, 3, "Put the words in order to make a question.", "does the new manager have to speak latvian", *Q)   # blind check r10: the two-clause question was too heavy for B1.1
od(T, L, 3, "Put the words in order.", "i had to cancel my dentist appointment because i was stuck at work",
   "For the past use *had to*: *I had to cancel …*. *must* has no past form for obligation.",
   "Pagātnē lieto *had to*: *I had to cancel …*. Pienākumam *must* pagātnes formas nav.",
   also=["because i was stuck at work i had to cancel my dentist appointment"])
od(T, L, 3, "Put the words in order.", "i'll have to renew my passport before we fly to canada", *FUT,
   also=["before we fly to canada i'll have to renew my passport"])
od(T, L, 3, "Put the words in order.", "we're going to have to hire more staff if sales keep growing", *MOD,
   also=["if sales keep growing we're going to have to hire more staff"])

# ── word bank (4): the wrong chips are real forms that miss the time or the meaning ──
gp(T, L, 3, "We ___ find a hotel near the station because the last train had already left.", "had to",
   "For the past use *had to*: the last train had already left. *must* and *have to* are not past forms.",
   "Pagātnē lieto *had to*: pēdējais vilciens jau bija aizgājis. *must* un *have to* nav pagātnes formas.",
   bank=["had to", "must", "have to"])
gp(T, L, 3, "If nobody can fix the printer today, we ___ ___ buy a new one.", "will / have to", *FUT, bank=["will", "have to", "must"])
gp(T, L, 3, "___ she ___ take the whole exam again if she fails one part?", "Does / have to", *Q, bank=["Does", "have to", "Has", "must"])
gp(T, L, 3, "The gym membership includes all the classes, so you ___ pay extra for yoga.", "don't have to", *DONT,
   bank=["don't have to", "mustn't", "don't must"])

# ── matching (1): a learning task; four forms with one verb, so only the form decides ──
mt(T, L, 2, "Match each sentence with its meaning.",
   [("I must book the tickets.", "I feel it's necessary."), ("I had to book the tickets.", "It was necessary in the past."),
    ("I don't have to book the tickets.", "It isn't necessary."), ("Do I have to book the tickets?", "I'm asking if it's necessary.")], *FORMS)

# ── typed gap (5) ──
gp(T, L, 3, "I couldn't park near the office, so I ___ leave the car three streets away. (have to)", "had to",
   "*couldn't* shows the past, so *had to*: *must* has no past form for obligation.",
   "*couldn't* rāda pagātni, tāpēc *had to*: pienākumam *must* pagātnes formas nav.")
gp(T, L, 3, "We ___ queue for long at the concert because we had bought our tickets online. (have to / not)",
   "didn't have to | did not have to", *PASTNEG)
gp(T, L, 3, "My sister works as a pilot, so she ___ have a medical check every year. (have to)",
   "has to | must | has got to | 's got to | needs to", *HAS)
gp(T, L, 3, "___ you ___ show your passport when you crossed the border last weekend? (have to)", "Did / have to", *PASTQ)
gp(T, L, 3, "My flatmate ___ get up early on Mondays because her first class starts at eleven. (have to / not)",
   "doesn't have to | does not have to | hasn't got to | has not got to",
   "*doesn't have to* = it is not necessary: her class starts late. With *she* use *doesn't*.",
   "*doesn't have to* = nav vajadzības: viņas nodarbība sākas vēlu. Ar *she* lieto *doesn't*.")

# ── whole sentence (3) ──
tx(T, L, 4, "Start with *Last month*: I have to work every Saturday to cover for a sick colleague.",
   "Last month I had to work every Saturday to cover for a sick colleague.",
   "*Last month* is the past: *I had to work*. *must* has no past form for obligation.",
   "*Last month* ir pagātne: *I had to work*. Pienākumam *must* pagātnes formas nav.")
tx(T, L, 4, "Make a yes/no question: Anna has to take the medicine twice a day while she is ill.",
   "Does Anna have to take the medicine twice a day while she is ill? | Must Anna take the medicine twice a day while she is ill? | "
   "Has Anna got to take the medicine twice a day while she is ill? | Does Anna have to take the medicine twice a day? | While she is ill, does Anna have to take the medicine twice a day?",
   "Question: *Does* + subject + *have to*: *Does Anna have to take …?* (*Must Anna take …?* is correct too, but formal.) Not *Has Anna to* or *Does Anna has to*.",
   "Jautājums: *Does* + teik. priekšmets + *have to*: *Does Anna have to take …?* (Der arī *Must Anna take …?*, bet tas ir oficiālāk.) Nevis *Has Anna to* vai *Does Anna has to*.")
tx(T, L, 4, "Say it another way with *might*: Perhaps we will have to sleep at the airport if the strike continues.",
   "We might have to sleep at the airport if the strike continues. | If the strike continues, we might have to sleep at the airport. | "
   "Perhaps we might have to sleep at the airport if the strike continues. | We might need to sleep at the airport if the strike continues. | "
   "If the strike continues, we might need to sleep at the airport.",
   "*might* + *have to*: *We might have to sleep …*. *will* goes; *must* cannot follow *might*.",
   "*might* + *have to*: *We might have to sleep …*. *will* izpaliek; aiz *might* nevar likt *must*.")
