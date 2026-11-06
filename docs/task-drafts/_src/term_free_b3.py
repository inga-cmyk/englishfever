"""Batch 3 without grammar terms (approved by the teacher, 6 November; docs/task-drafts/term-free-batch3-review.md). Applied through term_free.fix()."""
PREFIX = [
    ("Complete with a relative word (*who, which, whose, where*…): ", "Write the missing word: "),
    ("Use the verb in brackets: ", ""),
    ("Rewrite as a polite indirect question: ", "Ask politely. Start with *Could you tell me* or *Do you know*: "),
]
WHOLE = {   # old text -> (new text, new correct answer or None)
    "Use the future passive: The prizes ___ at the end of the show. (give)": ("At the end of tonight's show, the prizes ___ to the winners. (give)", "will be given | are going to be given"),
    "Use the present continuous passive: The guests ___ in the garden. (serve)": ("Right now the guests ___ in the garden. (serve)", None),
    "Use the present perfect passive: Several mistakes ___ in the report. (find)": ("Look at this! Several mistakes ___ in the report so far. (find)", None),
    "Make a question with who, about the object: Ben invited Maria.": ("Ask about *Maria* with *Who*: Ben invited Maria.", None),
    "Make a question with who, about the object: Maria thanked her teacher.": ("Ask about *her teacher* with *Who*: Maria thanked her teacher.", None),
    "Make a question with who, about the object: Anna lent her bike to Tom.": ("Ask about *Tom* with *Who*: Anna lent her bike to Tom.", None),
    "Make a question with what, about the subject: Something made that noise.": ("Ask about *Something* with *What*: Something made that noise.", None),
    "Rewrite with the superlative: No other mountain in this country is as high as Mount Hill.": ("Say the same, starting with *Mount Hill*: No other mountain in this country is as high as Mount Hill.", None),
}


def fix(task):
    """-> (new text, new correct answer or None) or None"""
    if task in WHOLE: return WHOLE[task]
    for old, rep in PREFIX:
        if task.startswith(old): return rep + task[len(old):], None
    return None
