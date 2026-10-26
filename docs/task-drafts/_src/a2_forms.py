"""Typed forms (teacher's feedback, 27 October): the matching tasks for verb forms and plurals can be guessed from how the words look,
so they stay as practice-only first steps, and these tasks ask the learner to type the form in a sentence. The clue in brackets names
the word, not the form. Plus a no-hint twin for the inversion task whose hint (Start with Had I) gives the answer away."""
from lib import *

PS = Topic("Past simple", gap=("Irregular verbs have their own past form: learn each one.", "Neregulārajiem darbības vārdiem ir sava pagātnes forma: tā jāiemācās."))
def ps(q, verb, past):
    PS.gap("A2.1", q, past, why=(f"*{verb} → {past}*: an irregular past form.", f"*{verb} → {past}*: neregulāra pagātnes forma."), b=3)
ps("Yesterday I ___ a pizza for lunch. (eat)", "eat", "ate")
ps("We ___ our old teacher at the station last week. (meet)", "meet", "met")
ps("She ___ her keys at home this morning. (leave)", "leave", "left")
ps("Tom ___ a cake to the party on Saturday. (bring)", "bring", "brought")
ps("I ___ the blue shirt, not the red one. (choose)", "choose", "chose")
ps("My parents ___ a new car last month. (buy)", "buy", "bought")
ps("I ___ about you yesterday. (think)", "think", "thought")
ps("He ___ a long email to his boss on Monday. (write)", "write", "wrote")
ps("We ___ to the seaside last summer. (go)", "go", "went")
ps("She ___ the bus to work this morning. (take)", "take", "took")
ps("I ___ a great film on Friday. (see)", "see", "saw")
ps("They ___ home late last night. (come)", "come", "came")

PP = Topic("Present perfect", gap=("*have / has* + the 3rd form. Irregular verbs have their own 3rd form.", "*have / has* + 3. forma. Neregulārajiem darbības vārdiem ir sava 3. forma."))
def pp(q, verb, form):
    PP.gap("A2.2", q, form, why=(f"*have / has* + 3rd form: *{verb} → {form}*.", f"*have / has* + 3. forma: *{verb} → {form}*."), b=3)
pp("Have you ever ___ snails? (eat)", "eat", "eaten")
pp("She has ___ her keys again. (lose)", "lose", "lost")
pp("We have already ___ the tickets. (buy)", "buy", "bought")
pp("Have you ___ my phone anywhere? (see)", "see", "seen")
pp("He has ___ to London twice. (be)", "be", "been")
pp("I have never ___ a horse. (ride)", "ride", "ridden")
pp("They have ___ a new bridge over the river. (build)", "build", "built")
pp("My sister has ___ three books about cats. (write)", "write", "written")

IP = Topic("Irregular plurals (children, people, men, teeth)", gap=("Some nouns have an irregular plural: *child → children*.", "Dažiem lietvārdiem ir neregulārs daudzskaitlis: *child → children*."))
def ip(q, one, many):
    IP.gap("A2.1", q, many, why=(f"*one {one}, two {many}*: an irregular plural.", f"*one {one}, two {many}*: neregulārs daudzskaitlis."), b=3)
ip("Two ___ are playing in the park. (child)", "child", "children")
ip("Many ___ came to the party. (person)", "person", "people")
ip("I brush my ___ twice a day. (tooth)", "tooth", "teeth")
ip("My ___ hurt after the long walk. (foot)", "foot", "feet")
ip("There are three ___ in our team. (woman)", "woman", "women")
ip("We saw two ___ in the kitchen! (mouse)", "mouse", "mice")

# the inversion task without the hint (its twin with "Start with Had I" stays as a practice-only first step)
od("Advanced conditionals: inversion, unless, wish", "C1.1", 3, "Put the words in order.",
   "had she left earlier she would have caught the train",
   "*Had she left* means *If she had left*. Inversion removes *if* and puts *had* before the subject.",
   "*Had she left* nozīmē *If she had left*. Inversija izlaiž *if* un liek *had* pirms teikuma priekšmeta.",
   also=["she would have caught the train had she left earlier"])
rows[-1][6] = rows[-1][6].replace(" " + audit_fixes.ORDER_Q[0], "")   # starts with had, but it is not a question
rows[-1][7] = rows[-1][7].replace(" " + audit_fixes.ORDER_Q[1], "")

save("a2-forms-1.csv")
