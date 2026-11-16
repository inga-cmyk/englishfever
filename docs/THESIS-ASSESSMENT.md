# Master's project: how it is assessed, and where the app is going

Recorded 16 November 2026 from the teacher's rubric (her .docx is not committed). Read this before writing anything for her report or
final presentation.

## Assessment rubric (written work and presentation)

Eight criteria, each 1-10 points (10-9 top, 8-6 middle, 5-1 low). What the top level asks for:

| # | Criterion | Top level (10-9) |
|---|---|---|
| 1 | Introduction | Clearly defined aim, tasks and relevance; a well-founded research plan. |
| 2 | Project development steps | A clear, detailed description of the development steps, including methods and an analysis of the challenges. |
| 3 | Evaluation methodology | Clearly described research methods and data-analysis approaches; logical evaluation criteria. |
| 4 | Results obtained or expected | Results clearly set out and logically justified; their impact and significance stated. |
| 5 | Conclusions and perspectives | Clear, considered conclusions; concrete future development options. |
| 6 | Presentation quality | Clear, structured delivery; engaging and convincing speech; suitable visuals. |
| 7 | Answers to questions | Convincing answers that show deep understanding of the work and the research. |
| 8 | Overall form and language | Professional layout; precise, academic language. |

Middle level typically means: right parts present, but less precise, less detailed or not fully justified. Low level: vague, superficial,
no logical sequence, no future steps, many language errors.

## The teacher's decisions that frame the work (16 November 2026)

- The research is about **engagement** and the factors that help or hinder it; the app is one engagement mechanism. Learning results matter
  in relation to engagement. Engagement data count from the first day (21 October 2026). She will explain this change of focus in the
  report and the final presentation.
- Knowledge gains (pre / post / delayed test, appendix of the project plan) are measured only once the app is complete or nearly complete.
- Handing in the thesis does **not** end the app's development. Her long-term aim: a precise grammar system that adapts well **without
  generative AI at run time**, based on the algorithms built (grammar map, learner model, task selection, spaced review). AI (Claude) is
  used at design time to write and check tasks; every task is approved by the teacher.

## Where the material is

- Report draft with charts: https://claude.ai/artifact/9qPkXsFAVHFAFNExUurqXF (system, task pipeline diagram, engagement and learning data).
- Project plan: her .docx, rewritten 16 November (engagement focus, first results, phases); not committed.
- Data definitions and changes: `docs/RESEARCH-DATA-PLAN.md`.
- Literature with checked references (habits, motivation, feedback, language apps, tutoring systems): `docs/THESIS-LITERATURE.md`.

## Learner model check (16 November 2026, first look, 27 learners, 6561 predictions)

Script: `tools/research/learner_model_check.py ANSWERS.csv` (the research export; the data are never committed). For every check / use
answer the app's own model (*My level*: ability from the last 60 evidence answers, difficulty = level base + 0.2 per thinking level,
slope 1.7) predicted right / wrong from the learner's earlier answers only.

- Ranking is weak for every model: AUC 0.62 for the app's model, 0.61 for the learner's running average, 0.61 for level + task kind
  without the learner, 0.65 for running average + level + task kind (left-one-learner-out). The app's model is not better than the
  running average (difference -0.02 to +0.05, bootstrap by learner).
- The app's predictions are far too extreme (calibration slope 0.23): predicted 29 % -> observed 63 %; predicted 96 % -> observed 83 %.
  The data give a slope of about 0.33 per half-level, not 1.7.
- Within learners, A2.2 is harder than A2.1 and B1.1 harder than A2.2, but B1.2, B2.1 and B2.2 are about as hard as B1.1 (few answers
  above B1.2: to confirm). A typed answer (role *use*) is about as much harder as one half-level; the model hardly counts it.
- Item difficulty cannot be calibrated yet: 2578 items met for the first time, median 2 answers per item, 36 items with 10 or more.
  Options for later: anchor tasks served to everyone (changes what is served: a dated research line), or many more learners.
- Not changed in the app. Changing the slope or adding the task kind to the difficulty changes *My level*: the teacher decides.
