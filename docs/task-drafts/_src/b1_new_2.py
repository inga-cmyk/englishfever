from lib import *
import b1_topics
italics.LV_ASCII |= b1_topics.LV_WORDS
B = dict(mcq_b=3, text_b=4, match_b=3)

# ============ Relative clauses (B1.1 / B1.2) ============
P = Topic("Relative clauses", **B,
    order=("Noun + *who / which / that / where* + the rest of the clause.", "Lietvārds + *who / which / that / where* + palīgteikuma turpinājums."),
    bank=("*who* = people, *which* = things, *that* = both, *where* = places, *whose* = belongs to. After a comma we do not use *that*.", "*who* = cilvēki, *which* = lietas, *that* = abi, *where* = vietas, *whose* = kam pieder. Pēc komata *that* nelieto."),
    gap=("*who* = people, *which* = things, *where* = places, *whose* = belongs to.", "*who* = cilvēki, *which* = lietas, *where* = vietas, *whose* = kam pieder."),
    text=("Join two sentences with *who / which / that / where / whose*. Do not repeat the noun or the object.", "Savieno divus teikumus ar *who / which / that / where / whose*. Neatkārto lietvārdu vai papildinātāju."),
    mcq=("*who* = people, *which* = things, *that* = both, *where* = places, *whose* = belongs to. After a comma we do not use *that*.", "*who* = cilvēki, *which* = lietas, *that* = abi, *where* = vietas, *whose* = kam pieder. Pēc komata *that* nelieto."),
    match=("*who / which / where / whose* show what the clause describes.", "*who / which / where / whose* parāda, ko apraksta palīgteikums."))
for s, l, al in [("the man who called you is my boss", "B1.1", None), ("i love the film that we saw yesterday", "B1.1", None), ("this is the house where i grew up", "B1.1", None),
                 ("my brother who lives in berlin is a nurse", "B1.2", None), ("the woman whose car was stolen called the police", "B1.2", None),
                 ("the hotel where we stayed was right next to the beach", "B1.2", None)]:
    P.order(l, s, also=al)
P.bank("B1.1", "A dentist is a person ___ looks after your teeth.", "who", ["which", "where"])
P.bank("B1.1", "A library is a place ___ you can borrow books.", "where", ["who", "whose"])
P.bank("B1.1", "This is the song ___ I told you about.", "that", ["who", "whose", "where"])
P.bank("B1.2", "The house ___ roof is red belongs to my aunt.", "whose", ["which", "who", "where"])
P.bank("B1.2", "Paris, ___ is the capital of France, is very busy in summer.", "which", ["that", "who"])
P.gap("B1.1", "She is the girl ___ brother plays for the national team.", "whose")
P.gap("B1.1", "The hotel ___ we stayed was close to the beach.", "where | in which")
P.gap("B1.2", "This is the road along ___ we walked.", "which")
P.gap("B1.2", "Anna, ___ husband is a pilot, travels a lot.", "whose")
P.gap("B1.2", "Last year we visited Rome, ___ my parents got married.", "where | in which")
P.mcq("B1.1", "Choose the correct option: The woman ___ lives next door is a nurse.", "who", ["which", "where", "whose"])
P.mcq("B1.1", "Choose the correct option: This is the phone ___ I bought last week.", "which", ["who", "where", "whose"])
P.mcq("B1.1", "Choose the correct option: That is the café ___ we first met.", "where", ["who", "which", "whose"])
P.mcq("B1.1", "Choose the correct option: He is the man ___ car was stolen.", "whose", ["who", "which", "where"])
P.mcq("B1.1", "At school: which sentence is NOT correct?", "The book which I bought it was boring.", ["The book which I bought was boring.", "The book I bought was boring.", "The book that I bought was boring."], b=4)
P.mcq("B1.1", "Which sentence is correct?", "The students who passed the exam were very happy.", ["The students which passed the exam were very happy.", "The students who they passed the exam were very happy.", "The students where passed the exam were very happy."], b=3)
P.mcq("B1.2", "Choose the correct option: My brother, ___ lives in Berlin, is a nurse.", "who", ["that", "which", "whose"])
P.mcq("B1.2", "Choose the correct option: The report, ___ I finished last night, is on your desk.", "which", ["that", "who", "what"])
P.mcq("B1.2", "In an email: which sentence is NOT correct?", "My sister, that lives in Paris, is a teacher.", ["My sister, who lives in Paris, is a teacher.", "My sister who lives in Paris is a teacher.", "The sister that lives in Paris is a teacher."], b=4)
P.mcq("B1.2", "In a text: which sentence is correct?", "The man I spoke to was very helpful.", ["The man I spoke was very helpful.", "The man I spoke to him was very helpful.", "The man who I spoke him to was very helpful."], b=3)
P.mcq("B1.2", "Which sentence is punctuated correctly?", "Tom, who is my neighbour, plays the drums.", ["Tom who is my neighbour plays the drums.", "Tom, who is my neighbour plays the drums.", "Tom who, is my neighbour, plays the drums."], b=4)
P.mcq("B1.2", "Choose the correct option: The hotel in ___ we stayed was lovely.", "which", ["that", "where", "who"])
P.mcq("B1.2", "Choose the correct option: She won the prize, ___ surprised everyone.", "which", ["what", "that", "who"])
P.text("B1.1", "Join with who: I know a woman. She speaks five languages.", ["I know a woman who speaks five languages."], b=5)
P.text("B1.1", "Join the two sentences: I have a friend. She works as a pilot.", ["I have a friend who works as a pilot.", "I have a friend that works as a pilot."], b=5)
P.text("B1.1", "Join with where: This is the town. I was born there.", ["This is the town where I was born."], b=5)
P.text("B1.2", "Join with which: She passed her driving test. This surprised everyone.", ["She passed her driving test, which surprised everyone."], b=5)
P.text("B1.2", "Join with whose: I met a man. His dog can open doors.", ["I met a man whose dog can open doors."], b=5)
P.text("B1.2", "Join the two sentences: My uncle lives in Spain. He is a chef.", ["My uncle, who lives in Spain, is a chef.", "My uncle, who is a chef, lives in Spain."], b=5)
P.text("B1.1", "Join the two sentences: This is the town. I was born there.", ["This is the town where I was born.", "This is the town in which I was born."], b=5)
P.text("B1.2", "Join the two sentences: She passed her driving test. This surprised everyone.", ["She passed her driving test, which surprised everyone."], b=5)
P.text("B1.2", "Join the two sentences: I met a man. His dog can open doors.", ["I met a man whose dog can open doors."], b=5)
P.match("B1.1", "Match each word with what it describes.", [("who", "a person"), ("which", "a thing"), ("where", "a place"), ("whose", "belongs to someone")])


def _ver(mains, clauses, conns, fronted=True):
    """Every sensible one-sentence version: main clause + connector + clause, and connector + clause + comma + main clause."""
    out = []
    for m in mains:
        for c in clauses:
            for k in conns:
                out.append(f"{m} {k} {c}.")
                if fronted: out.append(f"{k.capitalize()} {c}, {m}.")
    return out

# ============ Time clauses (B1.1 / B1.2) ============
P = Topic("Time clauses", **B,
    order=("Time word + Present Simple, then *will* or *going to* in the main clause.", "Laika vārds + Present Simple, pēc tam *will* vai *going to* virsteikumā."),
    bank=("After *when / as soon as / until / before / after* we use the Present Simple for the future, not *will*.", "Pēc *when / as soon as / until / before / after* nākotnei lieto Present Simple, nevis *will*."),
    gap=("After *when / as soon as / until / before / after* we use the Present Simple (or the Present Perfect) for the future, not *will*.", "Pēc *when / as soon as / until / before / after* nākotnei lieto Present Simple (vai Present Perfect), nevis *will*."),
    text=("The time clause has the Present Simple. It can come first (with a comma) or second.", "Laika palīgteikumā ir Present Simple. Tas var būt pirmais (ar komatu) vai otrais."),
    mcq=("After *when / as soon as / until / before / after* we use the Present Simple for the future, not *will*.", "Pēc *when / as soon as / until / before / after* nākotnei lieto Present Simple, nevis *will*."),
    match=("*when, as soon as, until, while* show how two events are connected in time.", "*when, as soon as, until, while* parāda, kā divi notikumi saistīti laikā."))
for s, l, al in [("i will call you when i get home", "B1.1", ["when i get home i will call you"]), ("we will leave as soon as everyone is ready", "B1.1", ["as soon as everyone is ready we will leave"]),
                 ("wait here until the doctor calls your name", "B1.1", None),
                 ("i will send you the file as soon as i have finished it", "B1.2", ["as soon as i have finished it i will send you the file"]), ("by the time you arrive we will have finished dinner", "B1.2", None),
                 ("she won't sign the contract until she has read every page", "B1.2", ["until she has read every page she won't sign the contract"])]:
    P.order(l, s, also=al)
P.bank("B1.1", "Let's leave before it ___ dark.", "gets", ["will get", "got"])
P.bank("B1.1", "I'll cook dinner when I ___ home.", "get", ["will get", "am get"])
P.bank("B1.1", "We'll go for a walk after we ___ lunch.", "have", ["will have", "had"])
P.bank("B1.2", "I'll tidy up after the guests ___ .", "have left", ["will leave", "left"])
P.bank("B1.2", "Let's wait ___ the rain stops.", "until", ["while", "during"])
P.bank("B1.2", "I'll phone you ___ I know the result.", "as soon as", ["during", "since"])
P.gap("B1.1", "She will be happy when she ___ the good news. (hear)", "hears | has heard")
P.gap("B1.1", "I won't go out until it ___ raining. (stop)", "stops | has stopped")
P.gap("B1.1", "Wait here until the doctor ___ your name. (call)", "calls | has called")
P.gap("B1.2", "I'll have a shower after I ___ the washing-up. (finish)", "finish | have finished")
P.gap("B1.2", "We'll start the meeting when everybody ___ . (arrive)", "arrives | has arrived")
P.gap("B1.2", "Please don't leave the building until the fire alarm ___ . (stop)", "stops | has stopped")
P.mcq("B1.1", "Choose the correct option: I'll call you as soon as I ___ home.", "get", ["will get", "am getting", "got"])
P.mcq("B1.1", "Choose the correct option: We'll wait here until the bus ___ .", "comes", ["will come", "is coming", "came"])
P.mcq("B1.1", "Choose the correct option: When I ___ the results, I'll tell you.", "get", ["will get", "got", "am getting"])
P.mcq("B1.1", "Choose the correct option: She'll feel better after she ___ some rest.", "has", ["will have", "had", "is having"])
P.mcq("B1.1", "Between friends: which sentence is NOT correct?", "I'll text you when I will arrive.", ["I'll text you when I arrive.", "When I arrive, I'll text you.", "I'll text you as soon as I arrive."], b=4)
P.mcq("B1.1", "At the door: which sentence is correct?", "Don't open the door until I tell you.", ["Don't open the door until I will tell you.", "Don't open the door until I told you.", "Don't open the door until I'm telling you."], b=3)
P.mcq("B1.2", "Choose the correct option: I'll send the file as soon as I ___ it.", "have finished", ["will finish", "finished", "am finishing"])
P.mcq("B1.2", "In a message: which sentence is NOT correct?", "I'll call you after I will have spoken to her.", ["I'll call you after I have spoken to her.", "I'll call you after I speak to her.", "After I speak to her, I'll call you."], b=4)
P.text("B1.1", "Rewrite with when: First I will finish work. Then I will call you.", ["I will call you when I finish work.", "I'll call you when I finish work.", "When I finish work, I will call you.", "When I finish work, I'll call you.", "I will call you when I have finished work.", "I'll call you when I have finished work.", "When I have finished work, I will call you.", "When I have finished work, I'll call you."], b=5)
P.text("B1.1", "Join with as soon as: I will get the tickets. I will let you know.", ["As soon as I get the tickets, I will let you know.", "As soon as I get the tickets, I'll let you know.", "I will let you know as soon as I get the tickets.", "I'll let you know as soon as I get the tickets."], b=5)
P.text("B1.2", "Rewrite with before: First I'll check the dates. After that I'll book the tickets.", ["I'll check the dates before I book the tickets.", "I will check the dates before I book the tickets.", "Before I book the tickets, I'll check the dates.", "Before I book the tickets, I will check the dates."], b=5)
P.text("B1.2", "Rewrite with until: You can't go out. First you must finish your homework.", ["You can't go out until you finish your homework.", "You can't go out until you have finished your homework.", "Until you finish your homework, you can't go out.", "Until you have finished your homework, you can't go out."], b=5)
P.text("B1.1", "Join the two plans in one sentence: First I will finish work. Then I will call you.",
       _ver(["I will call you", "I'll call you"], ["I finish work", "I have finished work"], ["when", "as soon as", "after", "once"]), b=5)
P.text("B1.1", "Join the two plans in one sentence: I will get the tickets. Then I will let you know.",
       _ver(["I will let you know", "I'll let you know"], ["I get the tickets", "I have got the tickets", "I've got the tickets"], ["when", "as soon as", "after", "once"]), b=5)
P.text("B1.2", "Join the two plans in one sentence: I'll check the dates first. After that I'll book the tickets.",
       _ver(["I'll check the dates", "I will check the dates"], ["I book the tickets"], ["before"])
       + _ver(["I'll book the tickets", "I will book the tickets"], ["I check the dates", "I have checked the dates", "I've checked the dates"], ["after", "once"]), b=5)
P.text("B1.2", "Join the two sentences: You can't go out. First you must finish your homework.",
       _ver(["You can't go out", "You cannot go out"], ["you finish your homework", "you have finished your homework"], ["until", "before"]), b=5)
P.match("B1.1", "Match each word with its meaning.", [("when", "at that time"), ("as soon as", "immediately after"), ("until", "up to that moment"), ("while", "at the same time")])
P.match("B1.2", "Match each time phrase with its meaning.", [("until", "up to that moment"), ("by the time", "not later than that moment"), ("as soon as", "immediately after"), ("whenever", "every time that")])
save("b1-new-2.csv")
