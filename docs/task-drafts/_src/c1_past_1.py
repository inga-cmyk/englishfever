"""C1 direction 2 (Advanced past simple, past continuous and past perfect), round 1 (23 November 2026).
Hewings, Advanced Grammar in Use (3rd ed.), units 4-5 (exercises 4.1, 5.2, 5.3); Murphy, English Grammar in Use, units 6, 15-16.
Only places where the context leaves one form (the book's own "only one is correct" cases): events that follow one another,
a count of repeated actions, a state before a past moment, a report of something that had happened, the cause of a past state,
wish + past perfect, a past habit as a complaint, a polite request. Contexts concrete but common; no Latvian surnames."""
from lib import gp, mc
T = "Advanced past simple, past continuous and past perfect"
L = "C1"

# x_past_both: events that follow one another are both past simple
gp(T, L, 4, "Write one word in each gap: The smoke alarm ___ off as soon as he ___ the candle underneath it. (go, light)", "went / lit",
   "Two completed events that follow one another: past simple for both (*went off as soon as he lit*). "
   "The continuous would mean that one was in progress when the other happened.",
   "Divi pabeigti notikumi, kas seko viens otram: abiem Past Simple (*went off as soon as he lit*). "
   "Ilgstošā forma nozīmētu, ka viens jau notika, kad notika otrs.")
# x_pastc_repeat: a count needs the past simple
mc(T, L, 4, "Which sentence has a mistake?", "We were flying to Oslo four times last year.",
   ["While my car was being repaired, I was cycling to work.", "When the builders were here, I was making them tea all day.",
    "She dropped her keys while she was getting out of the taxi."],
   "With a count of repeated actions (*four times last year*), use the past simple: *We flew to Oslo four times.* "
   "The continuous is possible for repeated actions in a limited, temporary period (*While my car was being repaired, I was cycling*).",
   "Ja atkārtotas darbības saskaita (*four times last year*), lieto Past Simple: *We flew to Oslo four times.* "
   "Ilgstošā forma iespējama atkārtotām darbībām īslaicīgā periodā (*While my car was being repaired, I was cycling*).")
# x_pastp_choice: a report of something earlier
gp(T, L, 3, "As soon as I saw her at the party, I was sure we ___ before. (meet)", "had met | 'd met",
   "*I was sure* is in the past, and the meeting was earlier still: past perfect, *we had met before* (not *we met*).",
   "*I was sure* ir pagātnē, un tikšanās bija vēl agrāk: Past Perfect, *we had met before* (nevis *we met*).")
gp(T, L, 3, "Write one word in each gap: I loved it. It was the best film I ___ ever ___. (see)", "had / seen",
   "The film is compared with everything seen up to that past moment: *the best film I had ever seen* (past perfect).",
   "Filma tiek salīdzināta ar visu, kas redzēts līdz tam pagātnes brīdim: *the best film I had ever seen* (Past Perfect).")
# x_pastpc_choice: a state verb stays simple
gp(T, L, 3, "We ___ each other for years before we started working together. (know)", "had known | 'd known",
   "*know* is a state verb: past perfect simple, *had known*, not *had been knowing*.",
   "*know* ir stāvokļa darbības vārds: Past Perfect Simple, *had known*, nevis *had been knowing*.")
# x_pastp_deduce: the cause of a past state
gp(T, L, 4, "His voice was hoarse because he ___ all afternoon at the match. (shout)", "had been shouting | 'd been shouting | had shouted | 'd shouted",
   "The shouting was over and explains how his voice was later: past perfect continuous, *had been shouting* (not *was shouting*).",
   "Kliegšana jau bija beigusies un izskaidro, kāda vēlāk bija viņa balss: Past Perfect Continuous, *had been shouting* (nevis *was shouting*).")
mc(T, L, 3, "Choose the correct option: When I got back to my desk, I could see that someone ___ my files.", "had moved",
   ["has moved", "had been moved", "is moving"],
   "A conclusion about something that happened before a past moment (*when I got back*): past perfect, *someone had moved my files*.",
   "Secinājums par to, kas notika pirms pagātnes brīža (*when I got back*): Past Perfect, *someone had moved my files*.")
# x_unreal_past: wish + past perfect
gp(T, L, 3, "These shoes are too small and the shop won't take them back. I wish I ___ the receipt. (keep)", "had kept | 'd kept",
   "A regret about the past: *I wish* + past perfect, *I wish I had kept the receipt*. *I wish I kept* would be about the present.",
   "Nožēla par pagātni: *I wish* + Past Perfect, *I wish I had kept the receipt*. *I wish I kept* būtu par tagadni.")
# x_pastc_always: a past habit as a complaint
gp(T, L, 4, "Write one word in each gap: My old flatmate ___ always ___ the lights on. It drove me mad. (leave)", "was / leaving",
   "*was always* + *-ing*: a past habit that annoyed someone (*was always leaving the lights on*).",
   "*was always* + *-ing*: pagātnes ieradums, kas kādu kaitināja (*was always leaving the lights on*).")
# x_past_polite: a polite request now
mc(T, L, 4, "Which sentence has a mistake?", "I had wondered if you could help me with this report.",
   ["I was wondering if you might have a minute.", "I wanted to ask you about Friday.", "We were hoping you could join us."],
   "A polite request about now uses the past simple or continuous (*I was wondering if…, I wanted to ask…*), not the past perfect: "
   "*I had wondered* means that you wondered before some other past moment.",
   "Pieklājīgs lūgums par tagadni lieto Past Simple vai Continuous (*I was wondering if…, I wanted to ask…*), nevis Past Perfect: "
   "*I had wondered* nozīmē, ka domāji to pirms kāda cita pagātnes brīža.")
