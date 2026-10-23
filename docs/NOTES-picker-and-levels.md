# Notes: practice picker and levels (not built yet)

Status: agreed with Inga in chat, **nothing of this is built**. Build only when she says so.

## Picker layout (her suggestion)
1. **Level** first: A1, A2, B1, B2, C1, C2, all shown to every learner (multi-select, e.g. A2 + B1).
   - A1 and C2 are **greyed out** until they have questions.
   - Learners may pick any level; no locking by their estimated level.
2. **Topics**: only topics that have questions at the chosen level(s). A2 shows basic grammar, reported speech only from B1/B2, and so on.
3. **Number of questions**: rename "tasks" to **questions** everywhere learners see it (picker "10 tasks" etc.). Teacher tab "Tasks" could become "Add questions".
4. **Start.**
- **No topic ticked**: a random mix of topics, all suitable for the chosen level(s), as many questions as selected.
- Full levels only (A2, B1, B2, C1). Questions labelled A2.1/A2.2 stay in the bank but are grouped under A2, so one topic at A2 serves easier and harder cases (same for B1.1/B1.2 and so on). Learners never see the half-levels.
- Same topic, different depth by level: A2 = basic forms, B2/C1 = advanced rules for the same grammar. Needs a rule card per level.

## Writing tasks
- Change "Write two sentences." to **"Write one sentence."** (65 writing tasks; most already ask for one). Check each prompt still makes sense. The two-word minimum check stays.

## Technical sketch (for later)
- `session/start`: accept `levels` (full levels) and allow empty `skills` = mix. Engine keeps `state.levels` (the half-levels allowed) and `pickNext` filters items to them instead of the +/-1 window. Start ability = lowest allowed half-level BASE + 0.3, adapts within the allowed set.
- Keep the old path (single level, "Surprise me", placement) working.
- `Content::liveMeta()` should report which full levels each topic really has questions in.
- Update tests: menu, topics_sound, e2e, tasks, bank_update.

## Level reference material
- Inga pasted a general CEFR explainer (A1 to C2 can-do statements, from a commercial blog). Useful only for **general** level descriptions; it has **no grammar** per level.
- To label levels and write standard rule cards I need a grammar syllabus per level: course-book grammar contents pages (unit lists with level) or the Cambridge English Grammar Profile. Ask Inga for pages per topic, starting with the topics she wants standardised first (present/past tenses, modals).
- Plan once she sends them: audit every task's level against the source and list mismatches (change nothing without her word); write per-level rule cards; write a "can do" list per topic per level; draft new questions for her to approve.
- Current bank spread: A2 121, B1 257, B2 68, C1 44 (no A1, no C2). Levels were labelled by Claude, not from a reference.
