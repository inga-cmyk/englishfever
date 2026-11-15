"""Batch 5, point prep_move (A2.2): 9 tasks to reach 10 counted tasks. Murphy unit 126 (go to, arrive in / at, get to, go home, into / out of),
the unit given for this point in docs/GRAMMAR-MAP.md; across, through, along, past as in Murphy's Essential Grammar in Use (prepositions of movement)."""
from lib import gp, od, mc, tx
T = "Prepositions of time and place (in, on, at)"
L = "A2.2"

ARR_AT = ("*arrive at* + a place such as a hotel, a station or a cinema; *arrive in* + a city or country. Never *arrive to*.",
          "*arrive at* + konkrēta vieta, piemēram, viesnīca; *arrive in* = ierasties pilsētā vai valstī. Nekad *arrive to*. Tulkojot burtiski *ieradāmies uz viesnīcu*, sanāk kļūda *arrived to*.")
ARR_IN = ("*arrive in* + a city or country: *We arrived in Oslo.* Never *arrive to*.",
          "*arrive in* = ierasties pilsētā vai valstī: *We arrived in Oslo.* Tulkojot burtiski *atbraucām uz Norvēģiju*, sanāk kļūda *arrived to*.")
GET_TO = ("*get to* + a place = arrive there: *What time did you get to the office?* *arrive* needs *at*: *arrive at the office*.",
          "*get to* + vieta = nokļūt: *What time did you get to the office?* Ar *arrive* vajag *at*: *arrive at the office*.")
PAST = ("*past* = going by something without stopping: *Walk past the bank.* *passed* is the past of the verb *pass*.",
        "*past* = garām: *Walk past the bank.* *passed* ir darbības vārda *pass* pagātnes forma.")
ACROSS = ("*across* = from one side to the other: *swim across the river*.",
          "*across* = pāri, uz otru krastu vai pusi: *swim across the river*.")
THROUGH = ("*through* = in at one side and out at the other of something with sides or an opening: *through the window, through the tunnel*.",
           "*through* = caur, cauri: *through the window, through the tunnel*.")
ALONG = ("*along* = following a line such as a river, a road or a beach: *walk along the beach*.",
         "*along* = pa: *walk along the beach*.")
OUT_OF = ("*out of* = from inside to outside: *take your laptop out of your bag*. Opposite: *into*.",
          "*out of* = no iekšienes ārā: *take your laptop out of your bag*. Pretējais: *into*.")
HOME = ("*go home, get home, come home*: no *to* before *home*.",
        "*go home, get home, come home*: pirms *home* nelieto *to*. Tulkojot burtiski *nokļuvi uz mājām*, sanāk kļūda *get to home*.")

# ── choice (4) ──
# Murphy 126: arrive at + a building; "to" is the Latvian "uz", "—" the learner who drops it
mc(T, L, 2, "Choose the correct option: We arrived ___ the hotel after midnight.", "at", ["to", "—"], *ARR_AT)
# get to vs arrive: the wrong options are the three ways learners mix them
mc(T, L, 2, "Choose the correct option: What time did you ___ the office today?", "get to", ["get", "arrive", "arrive to"], *GET_TO)
mc(T, L, 2, "Which sentence has a mistake?", "We arrived to Oslo late on Friday.",
   ["She ran into the kitchen.", "The road goes through the forest.", "I walk past your house every day."], *ARR_IN)
mc(T, L, 2, "Choose the correct option: Walk ___ the bank and turn left.", "past", ["passed", "pass"], *PAST)
# ── word order (1) ──
od(T, L, 3, "Put the words in order.", "let's walk along the beach after lunch", *ALONG, also=["after lunch let's walk along the beach"])
# ── word bank (2) ──
gp(T, L, 3, "We swam ___ the river to the other side.", "across", *ACROSS, bank=["across", "through", "along"])
gp(T, L, 3, "The cat came in ___ the open window.", "through", *THROUGH, bank=["through", "across", "along"])
# ── typed gap (1) ──
gp(T, L, 3, "Write one word in each gap: At airport security, take your laptop ___ ___ your bag.", "out / of", *OUT_OF)
# ── whole sentence (1) ──
tx(T, L, 4, "Correct the mistake: What time did you get to home last night?", "What time did you get home last night?", *HOME)
