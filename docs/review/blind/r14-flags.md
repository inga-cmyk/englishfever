# Blind check r14: flags for the judge

7 tasks, 2 readers.

## r14-005 · A2.1 · text · gap-fill-a2-1.csv:51

Task: Correct the mistake. Change one word: There's a few snow on the roads today.
Key: {"kind": "text", "accepted": [["There's a little snow on the roads today.", "There is a little snow on the roads today.", "Today There's a little snow on the roads.", "Today there is a little snow on the roads."]]}
- reader 1: instruction: 'Change one word' plus the visible 'a few' gives away the type of fix (few -> little); acceptable but mild.

## r14-007 · A2.1 · text · gap-fill-a2-1.csv:65

Task: Make a yes/no question: There are some yoga classes on Sunday.
Key: {"kind": "text", "accepted": [["Are there any yoga classes on Sunday?"]]}
- reader 1: another correct answer, not accepted: [['Are there some yoga classes on Sunday?'], ['Are there yoga classes on Sunday?'], ['Are there any yoga classes on Sundays?'], ['Are there some yoga classes on Sundays?']]
- reader 1: instruction: No hint whether to keep 'some' or change to 'any'; 'Are there some...' is also correct (less natural); 'yes/no question' is a grammar term some A2 learners may not know.
- reader 2: another correct answer, not accepted: ['Are there some yoga classes on Sunday?', 'Are there yoga classes on Sunday?']
- reader 2: instruction: Less natural but correct: 'some' kept in a question (offer/expected yes). 'yes/no question' is a mild grammar term.

