"""Batch 5, point purpose_to (A2.2): 6 tasks to reach 10 counted tasks. Murphy unit 64."""
from lib import gp, od, mc, tx
T = "Contrast, purpose and reason"
L = "A2.2"

# Murphy 64: to + verb says why somebody does something (not for + verb, not for to); for + noun says what somebody wants or needs
# (go for a coffee). No so that, no in order to in the questions (B1); in order to is accepted where a learner may write it.
TO = ("To say why somebody does something, use *to* + verb: *He uses his phone to pay.* Not *for pay* and not *for paying*.",
      "Kāpēc kāds kaut ko dara, norāda ar *to pay, to get, to stay*: *He uses his phone to pay.* Nevis *for pay* un nevis *for paying*.")

# choice (2)
mc(T, L, 2, "Choose the correct option: He went to the doctor ___ a check-up.", "for", ["to", "on"],
   "*for* + noun says what somebody goes somewhere for: *go to the doctor for a check-up*. *to* is followed by a verb (*to have a check-up*).",
   "*for* + lietvārds norāda, pēc kā kāds iet: *go to the doctor for a check-up*. Ar darbības vārdu būtu *to have a check-up*. Kļūda: *to a check-up*, *on a check-up*.")
mc(T, L, 2, "Which sentence has a mistake?", "I'm learning English for get a better job.",
   ["She called me to say thank you.", "We went to the beach for a swim.", "They are staying with us for the weekend."],
   "Before a verb, purpose is *to* + verb: *I'm learning English to get a better job*, not *for get*. *for* comes before a noun: *for a swim*.",
   "Pirms darbības vārda nolūku pauž ar *to get, to buy*: *I'm learning English to get a better job*, nevis *for get*. *for* lieto pirms lietvārda: *for a swim*.")
# word order (1)
od(T, L, 3, "Put the words in order.", "he uses his phone to pay for everything", *TO)
# word bank (1): for stay, for staying and to staying are the typical mistakes of this point (map: for get, for getting)
gp(T, L, 3, "She goes to the gym ___ ___ fit.", "to / stay", *TO, bank=["to", "stay", "for", "staying"])
# typed gap (1): the question Why? rules out "I called and booked a room"
gp(T, L, 3, "Why did you call the hotel? I called ___ a room. (book)", "to book | in order to book | so as to book",
   "The answer to *Why?* is *to* + verb: *I called to book a room.* Not *for book* or *for booking*.",
   "Atbilde uz *Why?* ir nolūks ar *to book*: *I called to book a room.* Nevis *for book* vai *for booking*.")
# whole sentence (1)
tx(T, L, 4, "Join with *to*: I went to the post office. I sent a parcel there.",
   "I went to the post office to send a parcel. | I went to the post office to send a parcel there. | I went to the post office in order to send a parcel.",
   "The second sentence says why: *to* + verb, without *I* and without the past form: *I went to the post office to send a parcel.*",
   "Otrais teikums norāda, kāpēc: *to send*, bez *I* un bez pagātnes formas *sent*: *I went to the post office to send a parcel.*")
