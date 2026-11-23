"""C1 direction 5 (Advanced modals: can, be able to, may, might), round 1 (23 November 2026). Hewings, Advanced Grammar in Use
(3rd ed.), units 15, 17; Murphy, English Grammar in Use, units 26-30. Only places where the context leaves one form."""
from lib import gp, mc
T = "Advanced modals: can, be able to, may, might"
L = "C1"

# x_allowed_once
mc(T, L, 4, "Which sentence has a mistake?", "Last night the children could stay up until eleven.",
   ["We could stay up late on Saturdays when we were kids.", "We couldn't go out on school nights.",
    "In the end we were allowed to leave early."],
   "Permission on one occasion: *were allowed to*, not *could*: *Last night the children were allowed to stay up until eleven.* "
   "*could* is for permission that was always there, and *couldn't* is fine for both.",
   "Atļauja vienā reizē: *were allowed to*, nevis *could*: *Last night the children were allowed to stay up until eleven.* "
   "*could* ir atļaujai, kas bija vienmēr, un *couldn't* der abos gadījumos.")
# x_able_limits
mc(T, L, 4, "Choose the correct option: After driving round for three hours, we ___ find a parking space.", "were able to",
   ["could", "can", "have been able to"],
   "One success on one past occasion: *were able to* (or *managed to*), not *could*: *we were able to find a parking space*.",
   "Viens izdevies mēģinājums pagātnē: *were able to* (vai *managed to*), nevis *could*: *we were able to find a parking space*.")
mc(T, L, 4, "Which sentence has a mistake?", "The forms are able to be filled in online.",
   ["I could hear the sea from my hotel room.", "We were able to finish the job on time.", "She'll be able to drive next year."],
   "Before a passive, use *can*: *The forms can be filled in online*, not *are able to be*.",
   "Pirms ciešamās kārtas lieto *can*: *The forms can be filled in online*, nevis *are able to be*.")
# x_may_might
mc(T, L, 4, "Which sentence has a mistake?", "May the figures in the report be wrong?",
   ["The results may point to a wider problem.", "Could the figures be wrong?", "Is she likely to accept the offer?"],
   "We don't ask about possibility with *May…?*: *Could the figures be wrong?* or *Are the figures likely to be wrong?*",
   "Par iespējamību nejautā ar *May…?*: *Could the figures be wrong?* vai *Are the figures likely to be wrong?*")
# x_may_well
mc(T, L, 4, "Choose the correct option: The next bus is in an hour, so we ___ walk.", "might as well",
   ["might as good", "might so well", "might well as"],
   "*might / may as well* + base verb = it is the only sensible thing to do: *we might as well walk*.",
   "*might / may as well* + pamatforma = tas ir vienīgais saprātīgais: *we might as well walk*.")
gp(T, L, 4, "You ___ me you were bringing five friends! I would have made more food. (might / warn)", "might have warned",
   "*You might have* + past participle: you should have done it (a reproach): *You might have warned me!*",
   "*You might have* + 3. forma: tev vajadzēja to izdarīt (pārmetums): *You might have warned me!*")
# x_might_cont
gp(T, L, 4, "This time next week I ___ on a beach in Crete. (may / lie)", "may be lying | might be lying",
   "A possible activity at a future moment: *may be* + *-ing*, *I may be lying on a beach*.",
   "Iespējama darbība nākotnes brīdī: *may be* + *-ing*, *I may be lying on a beach*.")
gp(T, L, 4, "He didn't sound serious about leaving. He ___ . (might / joke)", "might have been joking | might have joked",
   "A possible activity in the past: *might have been* + *-ing*, *he might have been joking*.",
   "Iespējama darbība pagātnē: *might have been* + *-ing*, *he might have been joking*.")
# x_can_typical
mc(T, L, 3, "Choose the correct option: Winters here ___ very long, so bring warm clothes.", "can be",
   ["can being", "are able to be", "could have been"],
   "*can* for what is sometimes or typically true: *Winters here can be very long.*",
   "*can* tam, kas mēdz būt vai ir raksturīgi: *Winters here can be very long.*")
