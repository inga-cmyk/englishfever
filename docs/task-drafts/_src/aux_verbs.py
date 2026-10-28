"""Auxiliary verbs: be, do, have (teacher, 28 October: learners mix up Are you / Do you / Did you / Have you).
Every wrong option is ungrammatical; one natural answer. A Latvian comparison only where Latvian leads to the mistake
(a Latvian question has no auxiliary: "Vai tev garšo kafija?"); otherwise a short rule."""
from lib import *

def ex(en, lv): return (en, lv)
BE = ex("*be* (*am / is / are*) with *-ing*, an adjective or a place: *Are you tired? Is it raining?*",
        "*be* (*am / is / are*) ar *-ing*, īpašības vārdu vai vietu: *Are you tired? Is it raining?*")
DO = ex("*do / does* with other verbs in the present simple: *Do you like coffee? Does she work here?*",
        "Latviešu jautājumā palīgdarbības vārda nav (Vai tev garšo kafija?), bet angliski ar parastu darbības vārdu vajag *do / does*: *Do you like coffee?*")
DOES = ex("*he / she / it*: *does*, and the main verb has no *-s*: *Does she work here?*",
          "*he / she / it*: *does*, un pamatdarbības vārds ir bez *-s*: *Does she work here?*")
DID = ex("*did* with other verbs in the past simple, then the base verb: *Did you see it?*",
         "*did* ar citiem darbības vārdiem Past Simple, tad pamatforma: *Did you see it?*")
WAS = ex("*be* in the past: *was / were*, no *did*: *Were you at home?*",
         "*be* pagātnē: *was / were*, bez *did*: *Were you at home?*")
HAVE = ex("*have / has* with the 3rd form (present perfect): *Have you ever been to London?*",
          "*have / has* ar 3. formu (Present Perfect): *Have you ever been to London?*")
SHORT = ex("A short answer repeats the auxiliary of the question: *Do you…? Yes, I do. Is she…? No, she isn't.*",
           "Īsajā atbildē atkārto jautājuma palīgdarbības vārdu: *Do you…? Yes, I do. Is she…? No, she isn't.*")
QW = ex("Question word + auxiliary + subject + verb: *Where do you live? What are you doing?*",
        "Jautājamais vārds + palīgdarbības vārds + teik. priekšmets + darbības vārds: *Where do you live? What are you doing?*")

T = Topic("Auxiliary verbs: be, do, have (Are you…? Do you…? Have you…?)", mcq_b=2, text_b=3,
          mcq=DO, bank=DO, gap=DO, text=DO, order=QW, match=DO)

# ── choose ──
T.mcq("A2.1", "Choose the correct option: ___ you like coffee?", "Do", ["Are", "Have"], DO, b=1)
T.mcq("A2.1", "Choose the correct option: ___ you tired?", "Are", ["Do", "Have"], BE, b=1)
T.mcq("A2.1", "Choose the correct option: ___ she work in a bank?", "Does", ["Do", "Is"], DOES, b=1)
T.mcq("A2.1", "Choose the correct option: ___ they at home yesterday?", "Were", ["Did", "Was"], WAS)
T.mcq("A2.1", "Choose the correct option: ___ you see the film last night?", "Did", ["Were", "Have"], DID)
T.mcq("A2.2", "Choose the correct option: ___ you ever been to London?", "Have", ["Did", "Are"], HAVE)
T.mcq("A2.2", "Choose the correct option: What ___ you doing?", "are", ["do", "have"], BE)
T.mcq("A2.2", "Choose the correct option: Where ___ you live?", "do", ["are", "have"], QW)
T.mcq("A2.2", "Choose the correct option: ___ he done his homework yet?", "Has", ["Did", "Is"], HAVE)
T.mcq("A2.2", "Choose the correct option: ___ it raining?", "Is", ["Does", "Has"], BE)
T.mcq("A2.2", "Choose the correct option: ___ your parents live near you?", "Do", ["Does", "Are"], DO)
T.mcq("B1.1", "Choose the correct option: How long ___ you known her?", "have", ["do", "are"], HAVE)
T.mcq("B1.1", "Choose the correct option: ___ you going to call him?", "Are", ["Do", "Have"],
      ex("*going to* goes with *be*: *Are you going to call him?*", "*going to* lieto ar *be*: *Are you going to call him?*"))
T.mcq("B1.1", "Choose the correct option: Who ___ you talking to on the phone just now?", "were", ["did", "have"],
      ex("*-ing* goes with *be*; *just now* is the past: *were*.", "*-ing* lieto ar *be*; *just now* ir pagātne: *were*."))

# ── short answers ──
T.mcq("A2.1", "Choose the correct short answer: 'Do you like tea?' 'Yes, I ___.'", "do", ["am", "have"], SHORT, b=1)
T.mcq("A2.2", "Choose the correct short answer: 'Is she your sister?' 'No, she ___.'", "isn't", ["doesn't", "hasn't"], SHORT)
T.mcq("A2.2", "Choose the correct short answer: 'Have you finished?' 'Yes, I ___.'", "have", ["did", "am"], SHORT)

# ── write the missing word ──
GAP_Q = "Write the missing word (am, is, are, do, does, did, have or has): "
T.gap("A2.1", GAP_Q + "___ your brother play football?", "Does", DOES)
T.gap("A2.1", GAP_Q + "___ you at work now?", "Are", BE)
T.gap("A2.2", GAP_Q + "___ you finish work early yesterday?", "Did", DID)
T.gap("A2.2", GAP_Q + "___ she ever eaten sushi?", "Has", HAVE)
T.gap("A2.2", GAP_Q + "Why ___ you laughing?", "are", BE)
T.gap("A2.2", GAP_Q + "What time ___ the shop open?", "does", DOES)
T.gap("B1.1", GAP_Q + "___ you been waiting long?", "Have", HAVE)
T.gap("B1.1", GAP_Q + "Where ___ you go on holiday last year?", "did", DID)

# ── make a question ──
T.text("A2.1", "Make a question: She works on Saturdays.", ["Does she work on Saturdays?"], DOES)
T.text("A2.2", "Make a question: They are watching TV.", ["Are they watching TV?"], BE)
T.text("A2.2", "Make a question: You have seen this film.", ["Have you seen this film?"], HAVE)
T.text("A2.2", "Make a question: He went to the doctor.", ["Did he go to the doctor?"], DID)
T.text("B1.1", "Make a question: You were late again.", ["Were you late again?"], WAS)

# ── word order ──
T.order("A2.2", "where do your parents live", why=QW, cue="Put the words in order to make a question.")
T.order("B1.1", "what have you been doing all day", why=QW, cue="Put the words in order to make a question.")

# short answers with a whole reply to choose (teacher, 28 October): Latvian answers with the main verb ("Jā, gribu"), English repeats the auxiliary
SHORT_LV = ex("A short answer repeats the auxiliary of the question, not the main verb: *Do you want…? Yes, I do.*",
              "Latviski atbild ar darbības vārdu (Jā, gribu), bet angliski atkārto jautājuma palīgdarbības vārdu: *Do you want…? Yes, I do.*")
Q = "Choose the correct short answer: "
T.mcq("A2.1", Q + "'Do you have a car?'", "Yes, I do.", ["Yes, I have.", "Yes, I am."], SHORT_LV)
T.mcq("A2.2", Q + "'Have you seen Peter today?'", "No, I haven't.", ["No, I don't.", "No, I wasn't."], SHORT)
T.mcq("A2.1", Q + "'Does she like jazz?'", "Yes, she does.", ["Yes, she like.", "Yes, she likes."], SHORT_LV)
T.mcq("A2.1", Q + "'Do you want to come with me?'", "Yes, I do.", ["Yes, I want.", "Yes, I am."], SHORT_LV)
T.mcq("A2.1", Q + "'Did you enjoy the film?'", "Yes, I did.", ["Yes, I enjoyed.", "Yes, I was."], SHORT_LV)
T.mcq("A2.1", Q + "'Are you hungry?'", "No, I'm not.", ["No, I don't.", "No, I haven't."], SHORT)
T.mcq("A2.2", Q + "'Has he called you?'", "Yes, he has.", ["Yes, he does.", "Yes, he is."], SHORT)
T.mcq("A2.1", Q + "'Were they at the party?'", "No, they weren't.", ["No, they didn't.", "No, they don't."], SHORT)
T.mcq("A2.1", Q + "'Can you swim?'", "Yes, I can.", ["Yes, I do.", "Yes, I am."], SHORT)
T.mcq("A2.2", Q + "'Do your parents live in Riga?'", "No, they don't.", ["No, they doesn't.", "No, they aren't."], SHORT)
T.mcq("A2.1", Q + "'Is it raining?'", "Yes, it is.", ["Yes, it does.", "Yes, it rains."], SHORT)
T.gap("A2.2", "Write the short answer: 'Does Anna speak French?' 'No, she ___.'", "doesn't", SHORT_LV)

save("aux-verbs-1.csv")
