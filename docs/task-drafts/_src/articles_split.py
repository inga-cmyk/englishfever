"""Articles split in two, like Murphy (teacher, 29 October): Articles (a, an, the) stays for a/an and the basics;
'The or no article' (B1) takes the tasks about the or no article. Moved tasks keep their text and say
"from: Articles" in the replaces column, so the importer retires the copy in Articles and keeps one task.
Then a few new B1 tasks, so the new topic has 25."""
import csv, os
from lib import *

HERE = os.path.dirname(os.path.abspath(__file__))
NEW = "The or no article"
MOVE = ["violin", "to ___ poor", "United States", "Alps", "Baltic Sea", "to ___ work by bus", "go to the bed",
        "Dogs are loyal", "the Latvia", "elderly", "English very well", "Danube", "the Spanish"]
moved = 0
for f in ("b1-new-1.csv", "more-1.csv"):
    for r in csv.reader(open(os.path.join(HERE, "..", f), encoding="utf-8-sig")):
        if not r[0].startswith("Articles") or r[1] == "A2.2": continue
        if any(k in r[3] or k in r[4] for k in MOVE):
            r = r + [""] * (len(HEAD) - len(r)); r[0] = NEW; r[9] = "from: Articles"; rows.append(r); moved += 1

G = ex = ("No article for things in general; *the* for a particular one.", "Bez artikula, ja runājam vispārīgi; the, ja par konkrētu.")
T = Topic(NEW, mcq_b=2, text_b=3, mcq=G, gap=G, text=G, order=G, match=G)
T.mcq("B1.1", "Choose the correct option: ___ Thames flows through London.", "The", ["—", "A"],
      ("Rivers take *the*: *the Thames, the Danube*.", "Upēm vajag the: the Thames, the Danube."))
T.mcq("B1.2", "Choose the correct option: ___ unemployed need help to find work.", "The", ["—", "An"],
      ("*the* + adjective = a group of people: *the unemployed, the poor*.", "the + īpašības vārds = cilvēku grupa: the unemployed, the poor."))
T.mcq("B1.2", "Which sentence is correct?", "Life is too short to drink bad coffee.", ["The life is too short to drink bad coffee.", "A life is too short to drink bad coffee."],
      ("*life* in general: no article.", "Dzīve vispārīgi: bez artikula."))
T.mcq("B1.1", "Which sentence is NOT correct?", "We visited the Riga last summer.", ["We visited Riga last summer.", "We visited the Old Town in Riga last summer."],
      ("Cities take no article: *Riga*.", "Pilsētām artikulu nelieto: Riga."))
T.gap("B1.1", "Complete with *the* or nothing: She lives in ___ Netherlands.", "the",
      ("Country names with a plural or *Kingdom, States, Republic* take *the*.", "Valstu nosaukumiem daudzskaitlī vai ar Kingdom, States, Republic vajag the."))
T.text("B1.1", "Correct the mistake: We usually go to the work by car.", "We usually go to work by car.",
       ("*go to work*: work as a purpose, no article.", "go to work: darbs kā nolūks, bez artikula."))
T.text("B1.2", "Correct the mistake: The Mount Everest is in the Himalayas.", "Mount Everest is in the Himalayas.",
       ("One mountain: no article. A mountain range: *the Himalayas*.", "Vienam kalnam artikulu nelieto, kalnu grēdai vajag the: the Himalayas."))
T.order("B1.1", "my grandmother is in hospital again", why=
        ("*in hospital* = as a patient, no article.", "in hospital = kā pacients, bez artikula."))
T.match("B1.2", "Match each beginning with its ending.", [("She is in prison", "as a prisoner."), ("Her lawyer went to the prison", "to talk to his client."), ("Ellie goes to school", "as a pupil."), ("Ellie's mother went to the school", "to meet the teacher.")],
        ("A place used for its purpose: no article. The building only: *the*.", "Vieta tās nolūkam: bez artikula. Tikai ēka: the."))
T.mcq("B1.2", "Choose the correct option: ___ rich should pay more tax.", "The", ["—", "A"],
      ("*the* + adjective = a group of people: *the rich*.", "the + īpašības vārds = cilvēku grupa: the rich."))
T.mcq("B1.1", "Choose the correct option: We had ___ lunch in a small café.", "—", ["the", "an"],
      ("Meals take no article: *have lunch, have breakfast*.", "Ēdienreizēm artikulu nelieto: have lunch, have breakfast."))
print("moved", moved)
save("articles-split-1.csv")
