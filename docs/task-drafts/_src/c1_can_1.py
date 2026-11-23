"""C1 direction 5 (Advanced modals: can, be able to, may, might), round 1 (23 November 2026). Hewings, Advanced Grammar in Use
(3rd ed.), units 15, 17; Murphy, English Grammar in Use, units 26-30. Only places where the context leaves one form."""
from lib import gp, mc, note
T = "Advanced modals: can, be able to, may, might"
L = "C1"

# x_allowed_once
mc(T, L, 4, "Which sentence has a mistake?", "Last night the children could stay up until eleven.",
   ["I could hear the neighbours arguing all night.", "We couldn't go out on school nights.",
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
   ["The results may point to a wider problem.", "The trains might be late because of the snow.", "Is she likely to accept the offer?"],
   "We don't ask about possibility with *May…?*: *Could the figures be wrong?* or *Are the figures likely to be wrong?*",
   "Par iespējamību nejautā ar *May…?*: *Could the figures be wrong?* vai *Are the figures likely to be wrong?*")
# x_may_well
mc(T, L, 4, "Which sentence has a mistake?", "Nothing's on, so we might as good go to bed.",
   ["You may well be right about the price.", "You might have told me the café was closed.", "There's no milk, so I'll have my tea black."],
   "*might / may as well* (not *as good*) = the sensible choice when there is nothing better to do: *we might as well go to bed*.",
   "*might / may as well* (nevis *as good*) = saprātīga izvēle, ja nav nekā labāka: *we might as well go to bed*.")
gp(T, L, 4, "You might ___ ___ me you were bringing five friends! I would have made more food.", "have / warned",
   "*You might have* + 3rd form: you should have done it (a reproach): *You might have warned me!*",
   "*You might have* + 3. forma: tev vajadzēja to izdarīt (pārmetums): *You might have warned me!*",
   bank=["have", "warned", "warn", "had"])
# x_might_cont
gp(T, L, 4, "This time next week I ___ ___ ___ on a beach in Crete.", "may / be / lying",
   "A possible activity at a future moment: *may be* + *-ing*, *I may be lying on a beach*.",
   "Iespējama darbība nākotnes brīdī: *may be* + *-ing*, *I may be lying on a beach*.",
   bank=["may", "be", "lying", "lie", "have"])
gp(T, L, 4, "He didn't sound serious about leaving. He ___ ___ ___ ___.", "might / have / been / joking",
   "A possible activity in the past: *might have been* + *-ing*, *he might have been joking*.",
   "Iespējama darbība pagātnē: *might have been* + *-ing*, *he might have been joking*.",
   bank=["might", "have", "been", "joking", "joked", "be"])
# x_can_typical
mc(T, L, 4, "Which sentence has a mistake?", "Winters here are able to be very long.",
   ["Travelling with small children can be exhausting.", "She can't have left already: her coat is still here.",
    "It may snow tonight, so drive carefully."],
   "*can* for what is sometimes or typically true, not *be able to*: *Winters here can be very long.*",
   "*can* tam, kas mēdz būt vai ir raksturīgi, nevis *be able to*: *Winters here can be very long.*")

# ── added 23 November to reach 10 counted tasks ──
# x_may_but
mc(T, L, 4, "Which sentence has a mistake?", "Although she may be young, but she learns fast.",
   ["The flat may be small, but it's bright and quiet.", "He might not be the fastest, but he never gives up.",
    "It may well rain later, so take an umbrella."],
   "*may … but* already admits one point and then disagrees, so *although* is not needed: *She may be young, but she learns fast.*",
   "*may … but* jau atzīst vienu un tad iebilst, tāpēc *although* nav vajadzīgs: *She may be young, but she learns fast.*")

# teacher's tester, 23 November: *can* for what is generally true, *may* for a prediction about this case
mc(T, L, 4, "Choose the correct option: The forecast says snow until April, so this winter ___ unusually long.", "may be",
   ["can be", "is able to be", "may being"],
   "A prediction about this particular winter: *may be*. *can be* is for what is generally or sometimes true (*Winters here can be very long*).",
   "Prognoze par šo konkrēto ziemu: *may be*. *can be* ir par to, kas mēdz būt vispār (*Winters here can be very long*).")
