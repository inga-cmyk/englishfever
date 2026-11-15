"""Batch 4, point would_habit (B1.2): would + base verb for actions repeated in the past, not for states. Murphy unit 36
(would: past habits, 'we would all get up early'; not for states), with unit 18 (used to: habits and states).
Where would fits (a repeated action), used to and the Past Simple fit too: they are never a wrong option, and every typed
gap with an action verb accepts would / 'd / used to / Past Simple, or says *Use *would*:*. What is tested:
would is wrong with states (have, live, know, like, own), so used to / Past Simple is the only answer there;
would + base verb (not would sang / would to sing); would and used to are not for one event (last summer)."""
from lib import gp, od, mc, tx, mt, learning_task
T = "Used to and be used to"
L = "B1.2"

ACT = ("*would* + base verb: an action that happened again and again in the past. *used to* and the Past Simple are also correct here.",
       "*would* + pamatforma: darbība, kas pagātnē atkārtojās. Šeit der arī *used to* un Past Simple.")
STATE = ("*have, live, know, like, own* are states, not actions: use *used to* (or the Past Simple), not *would*: *I used to have a dog.*",
         "*have, live, know, like, own* ir stāvokļa darbības vārdi: lieto *used to* (vai Past Simple), nevis *would*: *I used to have a dog.*")
BASE = ("After *would* comes the base verb, with no *to* and no ending: *I would sing*, not *would sang* or *would to sing*.",
        "Aiz *would* liek pamatformu bez galotnes: *I would sing*, nevis *would sang* vai *would to sing*.")
def once(when):
    """One event at a given time: Past Simple, not would / used to."""
    return (f"One finished event at a given time (*{when}*) takes the Past Simple. *would* and *used to* are for things that happened many times.",
            f"Vienam pabeigtam notikumam noteiktā laikā (*{when}*) lieto Past Simple. *would* un *used to* lieto tam, kas notika daudzas reizes.")
MIX = ("A state (*have, live, know, like, own*) takes *used to*; a repeated action can take *would*: *We used to have a garden where we would grow vegetables.*",
       "Stāvoklim (*have, live, know, like, own*) lieto *used to*; atkārtotai darbībai var lietot *would*: *We used to have a garden where we would grow vegetables.*")
def order(ex, part):
    """Word order: subject + would + base verb; the part named can go first or last."""
    return (f"Subject + *would* + base verb + the rest: *{ex}*. The *{part}* part can go first or last.",
            f"Teikuma priekšmets + *would* + pamatforma + pārējais: *{ex}*. *{part}* daļu var likt sākumā vai beigās.")

# choose (7): the wrong option is would + a state, would + a wrong verb form, or would for one event; used to / Past Simple
# are never wrong options where would fits. No situation in front: the sentence itself decides (cover test).
mc(T, L, 2, "Choose the correct option: When I lived in Spain, I ___ a little scooter that I rode everywhere.", "used to have",
   ["would have", "was having", "use to have"], *STATE)
mc(T, L, 2, "Choose the correct option: When we were students, we ___ in a tiny flat near the station.", "used to live",
   ["would live", "use to live", "were used to live"], *STATE)
mc(T, L, 2, "Which sentence is NOT correct?", "We would know all our neighbours when we lived in the village.",
   ["Every Sunday my grandmother would bake bread for the whole family.", "My uncle used to own a small hotel by the sea.",
    "In my first job, I took the train to work every day."], *STATE)
mc(T, L, 2, "Which sentence is correct?", "When my children were small, I would sing to them every night.",
   ["When my children were small, I would sang to them every night.", "When my children were small, I would to sing to them every night.",
    "When my children were small, I was used to sing to them every night."], *BASE)
mc(T, L, 2, "Choose the correct option: As a teenager, I ___ spicy food, but now I cook curry every week.", "didn't use to like",
   ["wouldn't like", "didn't used to like", "wasn't used to like"],
   "*like* is a state, so *would* is not possible: *I didn't use to like spicy food* (or *I didn't like it*). After *didn't*: *use to*, not *used to*.",
   "*like* ir stāvokļa darbības vārds, tāpēc *would* nevar lietot: *I didn't use to like spicy food* (vai *I didn't like it*). Aiz *didn't* raksta *use to*, nevis *used to*.")
mc(T, L, 2, "Choose the correct option: Last summer we ___ to Greece for two weeks and loved every minute.", "went",
   ["would go", "used to go", "have gone"], *once("last summer"))
mc(T, L, 2, "Choose the correct option: My grandparents ___ a farm, and every summer we would help them with the harvest.", "used to own",
   ["would own", "were owning", "use to own"], *MIX)

# word order (5): every natural order is listed; two of them mix used to (state) and would (action), so the cards
# 'would' and 'used to' cannot change places (we would have a garden / my uncle would be a fisherman are wrong)
od(T, L, 3, "Put the words in order.", "when we lived by the sea we would swim before breakfast", *order("we would swim", "when"),
   also=["we would swim before breakfast when we lived by the sea"])
od(T, L, 3, "Put the words in order.", "my uncle used to be a fisherman and he would get up at four", *MIX)
od(T, L, 3, "Put the words in order.", "my grandmother would sing old songs while she cooked dinner", *order("my grandmother would sing", "while"),
   also=["while she cooked dinner my grandmother would sing old songs", "while my grandmother cooked dinner she would sing old songs"])
od(T, L, 3, "Put the words in order.", "on long car journeys my brother and i would play word games", *order("my brother and I would play", "on long car journeys"),
   also=["my brother and i would play word games on long car journeys"])
od(T, L, 3, "Put the words in order.", "we used to have a garden where we would grow our own vegetables", *MIX)

# word bank (4): the wrong chips are would + a state, would + a wrong form, use to (no -d)
gp(T, L, 3, "Before I moved here, I ___ a cat that always slept on my laptop.", "used to have", *STATE,
   bank=["used to have", "would have", "was having"])
gp(T, L, 3, "Every August my grandmother ___ jam from the berries we picked in the forest.", "would make", *BASE,
   bank=["would make", "would made", "would to make"])
gp(T, L, 3, "Before they retired, my parents ___ in a flat in the city centre.", "used to live", *STATE,
   bank=["used to live", "would live", "use to live"])
gp(T, L, 3, "In my first job, my boss ___ ___ us coffee every Monday morning.", "would / bring", *BASE,
   bank=["would", "bring", "brought", "to"])

# matching (1, learning): the state ending (have very long hair) fits only after used to; the other endings are tied to
# their beginnings (snow / sledging with us, bridge / river, my parents / they)
mt(T, L, 2, "Match each beginning with its ending.", [
    ("When I was a student, I used to", "have very long hair."),
    ("When it snowed, my dad would", "take us sledging in the park."),
    ("Before the bridge was built, people would", "cross the river by ferry."),
    ("My parents didn't use to", "like my friends, but now they do.")], *MIX)

# typed gap (5): a state verb accepts used to / Past Simple only; an action verb accepts every correct form, or says Use would
gp(T, L, 3, "When I was a student, I ___ a really old car that broke down every week. (have)", "used to have | had", *STATE)
gp(T, L, 3, "When I worked at the market, I ___ every customer by name. (know)", "used to know | knew", *STATE)
gp(T, L, 3, "Use *would*: Every Sunday my grandfather ___ us fishing on the lake. (take)", "would take | 'd take", *BASE)
gp(T, L, 3, "When we were kids, my sister and I ___ for hours about whose turn it was to wash up. (argue)",
   "would argue | 'd argue | used to argue | argued", *ACT)
gp(T, L, 3, "Last month I ___ to Tallinn for a job interview, and I got the job! (go)", "went", *once("last month"))

# whole sentence (3)
tx(T, L, 4, "Say it another way with *would*: When I was young, my father used to cook pancakes every Saturday.",
   "When I was young, my father would cook pancakes every Saturday. | My father would cook pancakes every Saturday when I was young. | Every Saturday my father would cook pancakes when I was young.", *ACT)
tx(T, L, 4, "Correct the mistake: When I was a child, I would have a little garden of my own.",
   "When I was a child, I used to have a little garden of my own. | When I was a child, I had a little garden of my own. | I used to have a little garden of my own when I was a child. | I had a little garden of my own when I was a child.", *STATE)
tx(T, L, 4, "Correct the mistake: Last weekend we would go hiking in the mountains.",
   "Last weekend we went hiking in the mountains. | We went hiking in the mountains last weekend.", *once("last weekend"))
