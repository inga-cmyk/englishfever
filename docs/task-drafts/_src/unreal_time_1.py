"""Unreal time and preferences (C1; teacher, 4 November, option A): it's (high / about) time + past, would rather / would sooner.
Sources: British Council LearnEnglish "Unreal time" (C1), Murphy Units 38 and 60. Our own sentences; exactly one option fits;
American "I'd rather you not ..." is accepted where the learner types. Approved by the teacher on 4 November."""
from lib import *

UT = Topic("Unreal time and preferences (it's high time, I'd rather)")
TIME = ("*It's (high / about) time* + subject + past: it should happen now, and it is already late.", "*It's (high / about) time* + teikuma priekšmets + pagātne: tam jau vajadzētu notikt, un ir jau vēlu.")
ME = ("*I'd rather / I'd sooner* + base form: what I prefer to do myself.", "*I'd rather / I'd sooner* + pamatforma: ko es pats labāk darītu.")
YOU = ("*I'd rather* + another person + past: what I want someone else to do (or not to do).", "*I'd rather* + cits cilvēks + pagātne: ko gribu, lai dara (vai nedara) kāds cits.")

UT.mcq("C1.1", "Choose the correct option: It's about time you ___ your mother.", "called", ["will call", "calling", "to call"], why=TIME)
UT.bank("C1.1", "It's time we ___ home. The last bus leaves in ten minutes.", "went", ["will go", "going", "to going"], why=TIME)
UT.mcq("C1.1", "Choose the correct option: It's high time the city ___ something about the traffic.", "did", ["will do", "doing", "to do"], why=TIME)
UT.text("C1.1", "Write one sentence that starts with *It's high time*: You should really start looking for a new job.",
        ["It's high time you started looking for a new job.", "It's high time you started to look for a new job.", "It's high time you looked for a new job.",
         "It is high time you started looking for a new job.", "It is high time you started to look for a new job.", "It is high time you looked for a new job."], why=TIME)
UT.mcq("C1.1", "Choose the correct option: I'd rather ___ at home tonight. I'm exhausted.", "stay", ["stayed", "to stay", "staying"], why=ME)
UT.bank("C1.2", "I'd sooner ___ the train than drive in this snow.", "take", ["took", "to take", "taking"], why=ME)
UT.mcq("C1.2", "Choose the correct option: I'd rather you ___ me the truth now than later.", "told", ["will tell", "telling", "to tell"], why=YOU)
UT.mcq("C1.2", "Which sentence has a mistake?", "I'd rather to walk than take the bus.", ["I'd rather you came a bit earlier.", "It's high time they fixed the road.", "I'd sooner stay here than go out."],
       why=("*I'd rather* + base form, without *to*: *I'd rather walk*.", "*I'd rather* + pamatforma bez *to*: *I'd rather walk*."))
UT.text("C1.2", "Write one sentence that starts with *I'd rather you*: Please don't bring your dog to the office.",
        ["I'd rather you didn't bring your dog to the office.", "I would rather you didn't bring your dog to the office.",
         "I'd rather you not bring your dog to the office.", "I would rather you not bring your dog to the office."], why=YOU)

save("unreal-time-1.csv")   # approved by the teacher on 4 November
