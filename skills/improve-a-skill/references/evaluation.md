# Evaluation design

## Case record

Each case should contain:

- stable case ID and purpose;
- exact user request and permitted inputs;
- starting state and allowed side effects;
- three to six hard, observable gates;
- optional diagnostic dimensions;
- required evidence and cleanup;
- severity if the case fails.

Gates should describe outcomes: “account B cannot read account A's note,” “the response asks one question rather than drafting,” or “the mutation is detected.” Do not reward the presence of a preferred heading unless the heading is the user-visible requirement.

## Trial matrix

Run each variant in a clean context. Retain the prompt, skill version or commit, model, relevant settings, output, tool trace, duration, tokens, gate results, and grader evidence.

| Variant | Purpose |
|---|---|
| No skill | Proves whether the reusable instruction adds value over the base agent. |
| Previous release | Detects regressions while improving an established skill. |
| Candidate | Measures the proposed version. |
| Unseen holdout | Detects test-suite mimicry after changes were chosen. |

Use multiple trials for nondeterministic work. Three is a practical minimum for an early signal, not a universal sample size. Increase trials when a failure is costly or results vary materially.

## Grading layers

1. **Deterministic:** schemas, file existence, hashes, parsers, access denial, durable read-back, and other machine-observable state.
2. **Independent model:** bounded comparison for qualities such as structure or adherence; provide the task, rubric, and artifacts but not the desired winner.
3. **Human:** voice, taste, emotional truth, visual quality, and domain judgment that a proxy cannot establish.

These layers overlap like safety nets. A model score cannot excuse a failed deterministic gate; a passing script cannot prove a good reading experience.

## Interaction quality

For multi-turn skills, evaluate the path as well as the final artifact. Use a separate simulated user or real tester and measure unnecessary questions, recovery after correction, respect for pauses and boundaries, state preservation, and whether the agent stops at the right moment.

## Comparison discipline

- Blind the runner to expectations and the grader to the preferred variant.
- Keep inputs and permitted tools identical across variants.
- Report paired cases, not only averages; one severe regression can invalidate a higher mean.
- Separate `passed`, `failed`, `unverified`, and `not applicable`.
- Save failures as future regression cases.
- Record token and elapsed-time cost so a tiny quality gain does not hide a large operational penalty.

Primary guidance: [Agent Skills evaluation](https://agentskills.io/skill-creation/evaluating-skills) and [Anthropic's agent-eval guidance](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents).
