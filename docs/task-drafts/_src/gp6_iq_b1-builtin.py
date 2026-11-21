# Built-in indirect-question tasks, 21 November (gp6_iq_b1-notes.md). For the lead agent to paste at the END of revise() in
# app/authoring/content_review.py (after the option_fixes loop, so these win). Seven new versions -> the retired count in
# app/tests/bank_update_test.php goes up by 7 (check with the build: intermediate versions can change the count).
# Plus three ids to demote (practice only, no new version): add them to PRACTICE_ONLY in app/authoring/build.py (see the end).

    # indirect questions B1 (teacher, 21 November: too easy, the answer given away; gp6_iq_b1-notes.md)
    # ip-B11-2a (tester: "so easy for B1"): matched by the topic word (toilet = toilet). Now one person, four times: only the form decides.
    report_fix('ip-B11-2a',
        q='Match each question with its polite form.',
        pairs=[["Where does Anna work?", "Do you know where Anna works?"],
               ["Where did Anna work?", "Do you know where Anna worked?"],
               ["Where is Anna working?", "Do you know where Anna is working?"],
               ["Where will Anna work?", "Do you know where Anna will work?"]],
        why='The question word stays; *do / does / did* go, and the verb itself shows the time: *does … work* → *works*, *did … work* → *worked*.',
        why_lv='Jautājamais vārds paliek; *do / does / did* pazūd, un laiku rāda pats darbības vārds: *does … work* → *works*, *did … work* → *worked*.')
    # ip-B11-4a: the correct twin of the wrong sentence was an option (Do you know what time the film starts?): three different correct sentences
    report_fix('ip-B11-4a',
        wrong=["Can you tell me if this seat is free?", "Could you tell me where she lives?", "I wonder how much it costs."])
    # ip-B11-5a (tester: "the wrong sentences are not good samples"): a politeness choice solved without the grammar. Now the form decides.
    report_fix('ip-B11-5a',
        q='Choose the correct option: Do you know how long ___ to get to the airport by taxi?',
        correct='it takes', wrong=['does it take', 'it take', 'takes it'], wrong_why={}, wrong_why_lv={},
        why='No *does* in an indirect question, so the verb itself takes *-s*: *how long it takes*.',
        why_lv='Netiešajā jautājumā nav *does*, tāpēc *-s* ir pašam darbības vārdam: *how long it takes*.')
    # ip-B11-6a (tester: "the instruction gives the form away": "Ask … where the meeting room is"): a situation, no question words given
    report_fix('ip-B11-6a',
        q="You have just joined a gym and want to swim, but you can't find the swimming pool. Ask the person at the desk politely. Start with *Could you tell me* or *Do you know*.",
        must=[[r"\b(could|can|would) you (please )?tell me\b|\bdo you (happen to )?know\b",
               "A polite start: *Could you tell me …?* / *Do you know …?*",
               "Pieklājīgs sākums: *Could you tell me …?* / *Do you know …?*"],
              [r"\b(tell me|know)\s+(where|how|which|what|if|whether)\b",
               "Then a question word: *… where the pool is*.",
               "Tad jautājamais vārds: *… where the pool is*."],
              [r"^(?!.*\b(where|how|which \w+|what \w+)\s+(is|are|does|do|can|could|should|will)\s+(the|it|i|we|they|you|this|that|my)\b)",
               "After *where* the subject comes first: *where the pool is*, *where I can swim*, not *where is the pool*.",
               "Pēc *where* vispirms ir teikuma priekšmets: *where the pool is*, *where I can swim*, nevis *where is the pool*."]],
        model='Could you tell me where the swimming pool is?')
    # ip-B12-2a: the B1.1 choice again (where the station is) at B1.2. Now the past: did goes, the verb shows the past (Murphy 13: Where did you buy it?)
    report_fix('ip-B12-2a',
        q='Choose the correct option: Could you tell me where ___ ?',
        correct='you bought that jacket', wrong=['did you buy that jacket', 'did you bought that jacket', 'you have bought that jacket'],
        wrong_why={}, wrong_why_lv={},
        why='*Where did you buy that jacket?* becomes *where you bought that jacket*: no *did*, and the verb itself is in the past.',
        why_lv='*Where did you buy that jacket?* kļūst par *where you bought that jacket*: bez *did*, un pagātnē ir pats darbības vārds.')
    # ip-B12-4a (tester: "each sentence should be different not to give away the pair"): the correct twin (I wonder what she wants) is gone
    report_fix('ip-B12-4a',
        wrong=["I wonder why she left the party so early.", "Do you know who she is?", "Could you tell me if he's here?"])
    # ip-B12-6a (tester: "the instruction gives the form away": "Ask … if the café takes cards"): a situation; yes/no or wh, past or future
    report_fix('ip-B12-6a',
        q="Last week you emailed your landlord about the broken heater in your flat, but he hasn't answered. Write him one polite question. Start with *Could you tell me* or *I'd like to know*.",
        must=[[r"\b(could|can|would) you (please )?(tell me|let me know)\b|\bi[\'’]?d like to know\b|\bi would like to know\b|\bdo you (happen to )?know\b|\bi (was )?wonder(ing)?\b",
               "A polite start: *Could you tell me …?* / *I'd like to know …*",
               "Pieklājīgs sākums: *Could you tell me …?* / *I'd like to know …*"],
              [r"\b(tell me|let me know|know|wonder|wondering)\s+(if|whether|when|what|why|how|who)\b",
               "Then *if* or a question word: *… if you got my email*, *… when someone can repair the heater*.",
               "Tad *if* vai jautājamais vārds: *… if you got my email*, *… when someone can repair the heater*."],
              [r"^(?!.*\b(if|whether|when|why|how(?:\s+(?:long|soon|much))?|what(?:\s+time)?)\s+(did|does|do|has|have|is|are|was|were|will|can|could)\s+(you|he|she|it|they|the|my|someone|somebody|anyone|anybody|we|i)\b)",
               "After *if* or the question word the subject comes first, with no *did*: *if you got my email*, *when the heater will be repaired*.",
               "Pēc *if* vai jautājamā vārda vispirms ir teikuma priekšmets, bez *did*: *if you got my email*, *when the heater will be repaired*."]],
        model='Could you tell me if you got my email about the heater?')

# app/authoring/build.py, PRACTICE_ONLY (a flag, not content: no new version, the blind record stays): add
#     "ip-B11-3b-r3"            # could you tell me where the station is: the fourth word order with this frame (c-0884, var order, c-3324)
#     "var-ip-b11-order-01-r2"  # 'Start with *Could you tell me*' + where the bank is: the frame is given, the same order as ip-B11-3b
#     "ip-B12-3a-r2"            # Make it polite: What time does the museum close?  the B1.1 rewrite (c-0903) again at B1.2
# and change Content::role nothing: practice_only already gives 'learn'.
