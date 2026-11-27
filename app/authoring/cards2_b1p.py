"""Rule card of the B1 topic "Active or passive? Present and past" (teacher, 27 November: the present and past simple passive are A2;
the B1 topic mixes both tenses and asks the learner to decide between active and passive). One card layout (cards2_c1.py):
a Form · Example table, exactly three typical mistakes, two or three "When we use it" blocks, one to three Watch out points, EN and LV.
Grammar: Murphy, English Grammar in Use, units 42 and 44. No example is a task's answer."""

from cards2_c1 import card

CARDS = {
    "active_passive": card(
        [['Active: the subject does it', 'subject + verb (present simple or past simple)', '*Our neighbour [[cuts]] the grass every Saturday.*'],
         ['Passive, present', '*am / is / are* + 3rd form', '*The grass [[is cut]] every Saturday.*'],
         ['Passive, past', '*was / were* + 3rd form', '*Our old sofa [[was taken]] away last week.*'],
         ['No object, no passive', '*happen, arrive, land, die, stay*: active only', '*Nothing exciting [[happened]] at the party.*']],
        [['Darāmā kārta: teikuma priekšmets dara darbību', 'teikuma priekšmets + darbības vārds (Present Simple vai Past Simple)', '*Our neighbour [[cuts]] the grass every Saturday.*'],
         ['Ciešamā kārta, tagadne', '*am / is / are* + 3. forma', '*The grass [[is cut]] every Saturday.*'],
         ['Ciešamā kārta, pagātne', '*was / were* + 3. forma', '*Our old sofa [[was taken]] away last week.*'],
         ['Nav papildinātāja, nav ciešamās kārtas', '*happen, arrive, land, die, stay*: tikai darāmā kārta', '*Nothing exciting [[happened]] at the party.*']],
        [['Our plane [[was landed]] at midnight.', 'Our plane [[landed]] at midnight.'],
         ['My wallet [[stole]] on the bus.', 'My wallet [[was stolen]] on the bus.'],
         ['The museum [[is opened]] in 1901.', 'The museum [[was opened]] in 1901.']],
        [['Our plane [[was landed]] at midnight.', 'Our plane [[landed]] at midnight.'],
         ['My wallet [[stole]] on the bus.', 'My wallet [[was stolen]] on the bus.', 'Latviski saka "maku nozaga" bez darītāja, tāpēc, tulkojot burtiski, *was* izlaiž.'],
         ['The museum [[is opened]] in 1901.', 'The museum [[was opened]] in 1901.']],
        [{'ex': ['Someone cleans the stairs every week. → The stairs [[are cleaned]] every week.'], 's': ['someone', 'people', 'they'],
          't': 'Who does it is unknown, not important or obvious: passive'},
         {'ex': ['My sister [[painted]] this picture.', 'This picture [[was painted]] [[by]] my sister.'], 's': ['by'],
          't': 'Who does it matters: active, or passive + *by*'},
         {'ex': ['The post [[is delivered]] at ten every day.', 'Yesterday it [[was delivered]] at two.'], 's': ['every day', 'usually', 'yesterday', 'ago', 'in 2010'],
          't': 'Time words choose present or past'}],
        [{'ex': ['Someone cleans the stairs every week. → The stairs [[are cleaned]] every week.'], 's': ['someone', 'people', 'they'],
          't': 'Darītājs nav zināms, nav svarīgs vai ir skaidrs: ciešamā kārta'},
         {'ex': ['My sister [[painted]] this picture.', 'This picture [[was painted]] [[by]] my sister.'], 's': ['by'],
          't': 'Svarīgi, kas to dara: darāmā kārta vai ciešamā kārta + *by*'},
         {'ex': ['The post [[is delivered]] at ten every day.', 'Yesterday it [[was delivered]] at two.'], 's': ['every day', 'usually', 'yesterday', 'ago', 'in 2010'],
          't': 'Laika vārdi izšķir tagadni vai pagātni'}],
        ['Ask who does the action. The subject does it: active (*Tom [[fixed]] the tap*). Something is done to the subject: passive (*The tap [[was fixed]]*).',
         '*by someone* and *by people* say nothing new: leave them out: *My bike [[was stolen]].*'],
        ['Pajautā, kurš darbību dara. Ja to dara teikuma priekšmets: darāmā kārta (*Tom [[fixed]] the tap*). Ja to dara ar teikuma priekšmetu: ciešamā kārta (*The tap [[was fixed]]*).',
         '*by someone* un *by people* neko jaunu nepasaka: tos izlaiž: *My bike [[was stolen]].*']),
}
