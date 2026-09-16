# Evaluation guidance

Run every case in clean context against both the current skill and a no-skill or previous-version baseline. Do not show the runner the expectations. Repeat behavior-heavy cases at least three times and retain outputs, timing, and token use.

Use deterministic graders for hashes, parseability, links, reading order, missing assets, and text-stream fidelity. Use rendered inspection and human review for typography, illustration fit, phone comfort, and whether the editions feel like one book. A script pass cannot compensate for a visual, privacy, or accessibility failure.

Give each case three to six release gates and keep softer design observations as diagnostics. This prevents both failure modes: a vague “looks good” verdict and a giant checklist that the workflow can game while producing an incoherent book.

For a reader site with account sync, test through two real test accounts. Save as account A, read back after reload and a second session, then prove account B cannot read, alter, enumerate, or infer A's progress, highlights, or notes. Static HTML, local storage, and a visible sign-in control cannot pass this case.

Keep failures as regression fixtures. Do not weaken a gate because the current toolchain cannot verify it; mark it `unverified`.

Method basis: [Agent Skills eval guidance](https://agentskills.io/skill-creation/evaluating-skills) and [Anthropic's agent-eval guidance](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents).
