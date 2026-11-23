"""C1 direction 7 (Subject and verb: advanced rules), round 1 (23 November 2026). Hewings, Advanced Grammar in Use (3rd ed.),
units 40-41; Murphy, English Grammar in Use, unit 82. Only places where one form is right in careful written English."""
from lib import gp, mc
T = "Subject and verb: advanced rules"
L = "C1"

gp(T, L, 3, "The number of applicants ___ fallen sharply this year. (have)", "has | had",
   "*The number of* + plural noun takes a singular verb: the number is one thing. *The number of applicants has fallen.*",
   "*The number of* + daudzskaitlis prasa darbības vārdu vienskaitlī: skaitlis ir viena lieta. *The number of applicants has fallen.*")
gp(T, L, 3, "A number of applicants ___ already withdrawn. (have)", "have | had",
   "*A number of* = several, so the verb is plural: *A number of applicants have withdrawn.* Compare: *The number of applicants has fallen* (the number is one thing).",
   "*A number of* = vairāki, tāpēc darbības vārds ir daudzskaitlī (salīdzini: *The number of applicants has fallen*, skaitlis ir viena lieta): *A number of applicants have withdrawn.*")
gp(T, L, 4, "The manager, together with two of her assistants, ___ coming to the meeting. (be)", "is | 's | was",
   "The main noun is *the manager*; a phrase with *together with* does not change the verb: *is coming*.",
   "Galvenais lietvārds ir *the manager*; izteiciens ar *together with* darbības vārdu nemaina: *is coming*.")
gp(T, L, 3, "Politics ___ never interested me much. (have)", "has | had",
   "*politics* ends in *-s* but takes a singular verb: *Politics has never interested me.*",
   "*politics* beidzas ar *-s*, bet darbības vārds ir vienskaitlī: *Politics has never interested me.*")
gp(T, L, 3, "The criteria for the award ___ changed this year. (have)", "have | had",
   "*criteria* is the plural of *criterion*: *The criteria have changed.*",
   "*criteria* ir *criterion* daudzskaitlis: *The criteria have changed.*")
gp(T, L, 3, "Ten kilometres ___ a long way to walk in this heat. (be)", "is | 's | was",
   "An amount seen as one distance takes a singular verb: *Ten kilometres is a long way.*",
   "Daudzums, ko uztver kā vienu attālumu, prasa vienskaitli: *Ten kilometres is a long way.*")
mc(T, L, 4, "Which sentence has a mistake?", "Each of the rooms have a private bathroom.",
   ["More than one guest has complained about the noise.", "Neither of the answers is correct.",
    "One in four adults has never been abroad."],
   "*each of* + plural noun takes a singular verb: *Each of the rooms has a private bathroom*.",
   "*each of* + daudzskaitlis prasa darbības vārdu vienskaitlī: *Each of the rooms has a private bathroom*.")
gp(T, L, 4, "Either the manager or her assistants ___ going to call you back. (be)", "are | were",
   "After *either … or*, the verb agrees with the nearer noun: *her assistants are*.",
   "Aiz *either … or* darbības vārds saskan ar tuvāko lietvārdu: *her assistants are*.")
gp(T, L, 4, "Being late for every meeting ___ not going to help your career. (be)", "is | 's | was",
   "An *-ing* clause as the subject is singular, even if it contains a plural noun: *Being late for every meeting is…*",
   "Darbības vārds ar *-ing* kā teikuma priekšmets ir vienskaitlī, arī ja tajā ir daudzskaitlis: *Being late for every meeting is…*")
gp(T, L, 4, "After three days, the jury ___ still arguing among themselves. (be)", "are | were",
   "The jury as separate people (*among themselves*): plural verb, *are arguing*.",
   "Žūrija kā atsevišķi cilvēki (*among themselves*): darbības vārds daudzskaitlī, *are arguing*.")

# teacher's tester, 23 November: *and* changes the verb, *together with* does not
gp(T, L, 4, "We need two more chairs: the manager and two of her assistants ___ coming to the meeting tomorrow. (be)", "are | 're | will be",
   "With *and*, the subject is plural: *The manager and two of her assistants are coming.* With *together with*, it stays singular: *The manager, together with two of her assistants, is coming.*",
   "Ar *and* teikuma priekšmets ir daudzskaitlī: *The manager and two of her assistants are coming.* Ar *together with* tas paliek vienskaitlī: *The manager, together with two of her assistants, is coming.*")
