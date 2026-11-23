"""C1 direction 8 (Prepositions: position and advanced patterns), round 1 (23 November 2026). Hewings, Advanced Grammar in Use
(3rd ed.), units 55, 91-93; Murphy, English Grammar in Use, units 94, 128-136. Only places where one form is right."""
from lib import gp, mc
T = "Prepositions: position and advanced patterns"
L = "C1"

mc(T, L, 4, "Which sentence has a mistake?", "The colleague with who I share an office is on holiday.",
   ["The colleague I share an office with is on holiday.", "The person to whom the letter was addressed has moved.",
    "That's the flat that we looked at yesterday."],
   "A preposition goes before *whom* or *which*, never before *who* or *that*: *the colleague with whom I share an office* "
   "(or *the colleague I share an office with*).",
   "Prievārds stāv pirms *whom* vai *which*, nekad pirms *who* vai *that*: *the colleague with whom I share an office* "
   "(vai *the colleague I share an office with*).")
gp(T, L, 4, "The report shows the extent ___ which prices have risen.", "to",
   "A fixed formal phrase: *the extent to which*.",
   "Nemainīgs oficiāls izteiciens: *the extent to which*.")
gp(T, L, 4, "Nobody explained the basis ___ which the fee was calculated.", "on",
   "A fixed formal phrase: *the basis on which*.",
   "Nemainīgs oficiāls izteiciens: *the basis on which*.")
gp(T, L, 4, "Write one word in each gap: We received three offers, none ___ ___ was acceptable.", "of / which",
   "A number or quantity + *of which* for things: *none of which*, *most of which*, *both of which*.",
   "Skaits vai daudzums + *of which* lietām: *none of which*, *most of which*, *both of which*.")
mc(T, L, 4, "Which sentence has a mistake?", "Your complaint is being looked by our team.",
   ["He was accused of lying to the police.", "The problem has been dealt with.",
    "The plan was objected to by most residents."],
   "The preposition of the verb stays in the passive: *Your complaint is being looked into by our team.*",
   "Darbības vārda prievārds paliek arī ciešamajā kārtā: *Your complaint is being looked into by our team.*")
gp(T, L, 3, "I didn't know anyone at the party, so I had nobody to talk ___.", "to | with",
   "The preposition stays at the end of the infinitive: *nobody to talk to*.",
   "Prievārds paliek nenoteiksmes beigās: *nobody to talk to*.")
mc(T, L, 4, "Choose the correct option: The road was closed ___ repairing the bridge.", "with a view to",
   ["in order to", "so as to", "for the purpose to"],
   "*with a view to* + *-ing* (*to* here is a preposition): *with a view to repairing the bridge*.",
   "*with a view to* + *-ing* (*to* te ir prievārds): *with a view to repairing the bridge*.")
mc(T, L, 4, "Which sentence has a mistake?", "Despite that it rained, the match went ahead.",
   ["Everything depends on whether she signs.", "I'm curious about how the app works.",
    "In spite of the cold, we ate outside."],
   "After a preposition, not a bare *that*-clause: *Despite the fact that it rained…* (or *Although it rained…*).",
   "Aiz prievārda nelieto tikai *that*-palīgteikumu: *Despite the fact that the tickets were cheap…* (vai *Although the tickets were cheap…*).")
gp(T, L, 3, "The heavy rain prevented us ___ leaving the house all weekend.", "from",
   "*prevent* + object + *from* + *-ing*: *prevented us from leaving*.",
   "*prevent* + papildinātājs + *from* + *-ing*: *prevented us from leaving*.")
mc(T, L, 4, "Choose the correct option: Nobody ___ the owner has a key to the safe.", "other than",
   ["apart", "besides of", "in place of"],
   "*other than* = except: *Nobody other than the owner has a key* (also *except*, *but*, *apart from*).",
   "*other than* = izņemot: *Nobody other than the owner has a key* (arī *except*, *but*, *apart from*).")
gp(T, L, 3, "She has a real talent ___ explaining difficult ideas simply.", "for",
   "*a talent for* + *-ing*: *a talent for explaining*.",
   "*a talent for* + *-ing*: *a talent for explaining*.")
