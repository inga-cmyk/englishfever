"""C1 direction 9 (Advanced participle clauses), round 1 (23 November 2026). Hewings, Advanced Grammar in Use (3rd ed.),
units 58-59; Murphy, English Grammar in Use, unit 68. Only places where one form is right."""
from lib import gp, mc
T = "Advanced participle clauses"
L = "C1"

mc(T, L, 4, "Which sentence has a mistake?", "Walking into the office, the lights were all off.",
   ["Opening the door, she saw the cat on the table.", "Built in the 1930s, the bridge is still in use.",
    "Not knowing what to say, I kept quiet."],
   "A participle clause has the same subject as the main clause. The lights were not walking: *Walking into the office, I saw that the lights were all off.*",
   "Divdabja teicienam ir tas pats teikuma priekšmets, kas galvenajam teikumam. Gaismas negāja: *Walking into the office, I saw that the lights were all off.*")
gp(T, L, 3, "___ finished the report, she went home early. (have)", "Having",
   "*Having* + past participle: the first action was complete before the second: *Having finished the report, she went home.*",
   "*Having* + 3. forma: pirmā darbība bija pabeigta pirms otrās: *Having finished the report, she went home.*")
gp(T, L, 3, "Not ___ anyone in the city, he felt very lonely at first. (know)", "knowing",
   "*Not* + *-ing* for a reason: *Not knowing anyone, he felt lonely.* *Not* goes before the participle.",
   "*Not* + *-ing* iemeslam: *Not knowing anyone, he felt lonely.* *Not* stāv pirms divdabja.")
gp(T, L, 4, "___ in a cool, dry place, the seeds will keep for years. (store)", "Stored | If stored | When stored",
   "A past participle at the start for a passive meaning (= if they are stored): *Stored in a cool, dry place, the seeds will keep.*",
   "3. forma sākumā ciešamās kārtas nozīmei (= ja tās glabā): *Stored in a cool, dry place, the seeds will keep.*")
gp(T, L, 3, "___ prices going up every month, many families are struggling.", "With",
   "*With* + noun + *-ing* describes the situation: *With prices going up every month, …*",
   "*With* + lietvārds + *-ing* apraksta situāciju: *With prices going up every month, …*")
mc(T, L, 4, "Choose the correct option: ___ no questions, the chair closed the meeting.", "There being",
   ["Being there", "It being", "There were"],
   "*There being* + noun gives the reason in formal style: *There being no questions, the chair closed the meeting.*",
   "*There being* + lietvārds oficiālā stilā norāda iemeslu: *There being no questions, the chair closed the meeting.*")
gp(T, L, 4, "The river burst its banks, ___ the streets near the station. (flood)", "flooding",
   "An *-ing* clause after the main clause for its direct result: *…, flooding the streets.*",
   "*-ing* teiciens aiz galvenā teikuma tiešam rezultātam: *…, flooding the streets.*")
mc(T, L, 3, "Choose the correct option: ___ hearing the news, she burst into tears.", "On",
   ["In", "By", "Without"],
   "*On* + *-ing* = at the moment when: *On hearing the news* = when she heard the news.",
   "*On* + *-ing* = tajā brīdī, kad: *On hearing the news* = kad viņa dzirdēja ziņu.")
gp(T, L, 3, "Keep the jar in the fridge once ___. (open)", "opened",
   "*once* + past participle (= once it has been opened): *Keep refrigerated once opened.*",
   "*once* + 3. forma (= kad tas ir atvērts): *Keep refrigerated once opened.*")
gp(T, L, 3, "___ by the queue outside, the new café is very popular. (judge)", "Judging",
   "A fixed comment phrase: *Judging by…* (it does not need the subject of the main clause).",
   "Nemainīgs komentāra izteiciens: *Judging by…* (tam nav vajadzīgs galvenā teikuma priekšmets).")
