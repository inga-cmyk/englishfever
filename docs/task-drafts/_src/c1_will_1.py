"""C1 direction 4 (Advanced modals: will, would, should), round 1 (23 November 2026). Hewings, Advanced Grammar in Use (3rd ed.),
units 16, 20, 39; Murphy, English Grammar in Use, units 25, 33-34. Only places where the context leaves one form.
Contexts concrete but common; no Latvian surnames."""
from lib import gp, mc
T = "Advanced modals: will, would, should"
L = "C1"

# x_will_habit
mc(T, L, 4, "Which sentence has a mistake?", "Last night he would cook dinner for all of us.",
   ["Our cat will sit at the window for hours.", "At school she would always sit at the back.", "Wood will float on water."],
   "*will / would* describe typical behaviour, not one occasion: *Last night he cooked dinner for all of us.*",
   "*will / would* apraksta raksturīgu uzvedību, nevis vienu reizi: *Last night he cooked dinner for all of us.*")
mc(T, L, 4, "Which sentence has a mistake?", "The old factory would be next to the river.",
   ["Whenever we visited my uncle, we would play in his garden.", "Didn't you use to have red hair?",
    "We visited Switzerland four times in the nineties."],
   "For a past state that has changed, use *used to*, not *would*: *The old factory used to be next to the river.*",
   "Pagātnes stāvoklim, kas mainījies, lieto *used to*, nevis *would*: *The old factory used to be next to the river.*")
# x_wont_refuse
gp(T, L, 3, "I tried three times, but the printer ___ work this morning. (not / will)", "wouldn't | would not | won't | will not",
   "*wouldn't* for a refusal on one occasion, also by a thing: *the printer wouldn't work*.",
   "*wouldn't* atteikumam vienā reizē, arī lietai: *the printer wouldn't work*.")
# x_will_assume
gp(T, L, 4, "Don't ring them now: they ___ lunch. (will / have)", "'ll be having | will be having",
   "A confident guess about what is happening now: *will be* + *-ing*, *they'll be having lunch*.",
   "Drošs minējums par to, kas notiek tagad: *will be* + *-ing*, *they'll be having lunch*.")
gp(T, L, 4, "It's nine o'clock. She ___ the news by now. (will / hear)", "will have heard | 'll have heard",
   "A confident guess about something before now: *will have* + past participle, *she'll have heard the news by now*.",
   "Drošs minējums par to, kas jau noticis: *will have* + 3. forma, *she'll have heard the news by now*.")
# x_would_have
gp(T, L, 3, "I ___ to your party, but nobody told me about it. (come)", "would have come | 'd have come | could have come",
   "Something that did not happen in the past: *would have* + past participle, *I'd have come*.",
   "Kaut kas, kas pagātnē nenotika: *would have* + 3. forma, *I'd have come*.")
# x_should_expect
gp(T, L, 4, "I sent it on Monday, so the parcel ___ by now. (should / arrive)", "should have arrived",
   "*should have* + past participle for what we expect has happened: *the parcel should have arrived by now*.",
   "*should have* + 3. forma tam, ko sagaidām, ka jau ir noticis: *the parcel should have arrived by now*.")
# x_if_will
mc(T, L, 4, "Which sentence has a mistake?", "Should you will change your mind, just call us.",
   ["If you will follow me, I'll show you to your room.", "If you should need anything, just ask.",
    "If you'd take a seat, the doctor will see you shortly."],
   "*Should you* + base verb (= if you happen to): *Should you change your mind, just call us.* *If you will / would* = if you are willing.",
   "*Should you* + pamatforma (= ja gadījumā): *Should you change your mind, just call us.* *If you will / would* = ja esat ar mieru.")
# x_should_purpose
mc(T, L, 4, "Choose the correct option: Keep the receipt in case you ___ to return the shoes.", "should need",
   ["will need", "would need", "had needed"],
   "*in case* + *should* (or the present simple) for a small chance: *in case you should need to return them*, not *will*.",
   "*in case* + *should* (vai Present Simple) nelielai iespējai: *in case you should need to return them*, nevis *will*.")
