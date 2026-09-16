# Evaluation guidance

Evaluate decisions and produced artifacts, not the presence of exact headings. Use the mode-specific manuscript rubric in `references/evaluation-rubric.md` where a draft exists.

## Run the suite honestly

- Start every run with clean context. Give the agent the skill path, prompt, input files, and output directory, but never the expected answer.
- Run the same prompt without the skill, or against a snapshot of the previous version, as the baseline.
- Repeat subjective or high-variance cases at least three times. A single strong run is an example, not a reliability result.
- Record output, duration, and token use for each run. Compare quality gains with the extra cost and ceremony the skill introduces.
- Grade observable expectations with cited evidence. Use deterministic checks for files and state; use an independent rubric plus periodic human review for voice, emotional honesty, and literary quality.
- Keep a short set of three to six outcome gates for each case, then use richer editorial dimensions diagnostically. Too many binary checks invite checklist-shaped prose; vague scores hide regressions. A run fails when a gate fails even if its average score looks good.
- Add real failures as regression cases. Do not rewrite the suite merely to bless the newest output.

Personal discovery needs at least one multi-turn simulation. Let a separate agent play the author through ambiguity, correction, a privacy boundary, and a cold resume; score both the final project state and the quality and number of interview turns.

For each case, check:

- correct mode and proportionate clarification;
- durable state that distinguishes source, decision, uncertainty, and next action;
- a book promise and architecture capable of sustaining book length;
- no invented facts, feelings, sources, canon, or permissions;
- mode-specific depth rather than generic long-form prose;
- explicit handoff boundary between locked manuscript and production formats.

Treat routing, source or canon integrity, architecture, and the reader promise as gates. A polished sample cannot compensate for failure on one of these.

For fiction, reward causal alternatives, constraints that arise from the premise, human and moral cost, continuity tracking, and consequences that alter later choices. Do not reward operational detail about real-world violence; the purpose is narrative evaluation.

Method basis: [Agent Skills eval guidance](https://agentskills.io/skill-creation/evaluating-skills) and [Anthropic's agent-eval guidance](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents).
