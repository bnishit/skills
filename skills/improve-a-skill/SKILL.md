---
name: improve-a-skill
description: Evaluate and improve a reusable agent skill through overlap checks, realistic tasks, blind baseline comparisons, observable gates, and bounded iteration. Use when a draft or existing skill needs evidence that it changes behavior reliably; do not use merely to perform the skill's ordinary task.
---

# Improve a skill

Prove that a skill earns its context. A valid folder and a persuasive description are not evidence that it improves real work.

## Establish the job

Inspect the skill, its callers, adjacent skills, and any actual failures before editing. State:

- the recurring job and the users or agents who need it;
- when it should and should not activate;
- the decision or behavior it changes beyond the base model;
- the safety, permission, fidelity, or quality invariants it must preserve;
- the closest existing skill and why this one is not duplication.

If deleting or merging the skill would serve users equally well, recommend that. Do not keep a skill merely because work has already gone into it.

## Build evidence before rules

Collect three kinds of cases:

1. **Representative:** ordinary requests the skill should handle.
2. **Boundary:** near-neighbor requests it should decline or route elsewhere.
3. **Failure:** real or plausible cases that expose the current weakness.

Use real anonymized failures when permitted and synthetic fixtures otherwise. Never put confidential material into a portable skill or eval.

Research only the gaps that could change the workflow. Read [references/research.md](references/research.md) when outside guidance, internal knowledge, or saved material is relevant. A bookmark is a lead, not proof.

## Design the evaluation

Read [references/evaluation.md](references/evaluation.md) before running comparisons. For each case:

- define three to six observable outcome gates;
- separate hard gates from softer diagnostic dimensions;
- name the allowed side effects and the evidence needed to verify them;
- avoid exact wording, heading, or regex checks unless the wording itself is the contract.

Run the identical request in clean contexts against:

- the skill under test;
- no skill, when the question is whether a skill is needed;
- or the previous released version, when measuring an update.

Do not reveal the expected answer, suspected bug, or desired verdict to the runner. Use an independent grader where possible. Repeat subjective or high-variance cases at least three times; one strong run is a smoke test, not a reliability claim.

## Improve in bounded loops

Change one coherent cause at a time. Prefer, in order:

1. a sharper name or description when routing is wrong;
2. a clearer invariant or decision criterion when judgment is wrong;
3. a focused reference when only one mode needs detail;
4. a deterministic script when repeated mechanics are fragile;
5. an asset only when it belongs in generated output.

Re-run the affected cases and a small regression set. Keep a change only when the gain is observable and it does not worsen routing, cost, autonomy, or neighboring cases. Record rejected changes; they prevent the same attractive mistake from returning.

Stop when all hard gates pass across the planned trials, no severe regression appears, and the remaining uncertainty is honestly named. Do not chase a perfect average by adding universal rules. If the skill starts mirroring the test suite, reduce the checklist and add unseen cases.

## Keep the skill small

- Assume the agent already knows generic craft and reasoning.
- Put selection-critical information in the description, shared constraints in `SKILL.md`, and conditional detail in references.
- Link every reference from the point where it becomes relevant.
- Remove obsolete paths and duplicated explanations before adding new ones.
- Preserve user scope and authorization. A skill may describe a deploy, send, purchase, or deletion workflow; it does not grant permission to perform it.

Use [assets/evaluation-plan.md](assets/evaluation-plan.md) for a durable run record. Keep raw outputs outside the skill unless they are small, synthetic regression fixtures.

## Release decision

Before recommending installation or publication, report:

- baseline and candidate results by case and trial;
- hard-gate failures, regressions, token/time cost, and human-review findings;
- the exact changes kept and rejected;
- what was structurally validated versus behaviorally demonstrated;
- whether the skill is ready, needs another bounded iteration, should remain experimental, or should be deleted.

Validation proves structure only. Never turn one successful example into “the skill is reliable,” and never turn a score into a substitute for editorial, product, security, or domain judgment.
