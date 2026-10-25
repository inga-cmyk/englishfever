# Working with Claude Cowork (testing in the browser)

Cowork tests the app in its browser; Claude Code (the coding session) fixes the code. Findings go into **GitHub Issues** in `inga-cmyk/englishfever`, so the coding session reads them directly and nothing has to be copied from chat to chat.

## Instruction to paste into Cowork

> You are testing the practice app at https://practice.englishfever.com for Inga, an English teacher (adult Latvian learners, levels A2–C1).
>
> **Report every finding as its own GitHub issue** in the repository `inga-cmyk/englishfever` (https://github.com/inga-cmyk/englishfever/issues/new). Title starts with `[Cowork]`, then a short description. Add the label `cowork` if it is offered. In the body:
> - **Where:** page or screen (Home, Placement, Practice, Second Chance, Tasks tab ...), app version from the footer, signed in as guest / learner / teacher, interface language.
> - **Steps:** numbered, so that the problem can be repeated.
> - **What happened** and **what should happen**. For a question: copy the instruction, sentence, options and the answer you gave, and the task ID if the page shows it.
> - **How sure:** certain bug / probably a bug / suggestion. Grammar claims: name the rule (e.g. Murphy, *English Grammar in Use*, unit 11).
> - A screenshot if it helps.
>
> One finding per issue; check the open issues first so you do not repeat one. Do not close issues. When you finish a round, add one issue `[Cowork] Round summary <date>` with a short list of what you checked and what you found nothing wrong with.
>
> **Do not:** change code or push to any branch; import CSV files, approve or retire questions, or change any setting on the live site unless Inga asks you to in this conversation; touch WordPress, englishfever.com or Hostinger; type learners' real names or emails into issues.

## How the coding session handles the issues

It reads the open `[Cowork]` issues when Inga asks (*"paskaties Cowork issues"*), checks each claim (grammar against the books, bugs by repeating the steps), fixes what is right on its working branch, and tells Inga in chat which ones it fixed, which it did not and why. It comments on or closes issues only when Inga says so.

## Before Cowork imports questions or changes settings

Use a test copy of the app (planned: a separate test address on Hostinger with its own database) so that trial imports do not reach learners. Until it exists, Cowork only tests and reports on the live site.
