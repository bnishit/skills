---
name: product-editor
description: Review a product or UX specification before implementation. Judge whether it should exist, whether it serves the specific user, what should be cut, and whether behavior and design agree. Use for an editorial decision on a spec; not copyediting or implementation review.
---

# Product editor

## Composes with

| Skill | Handoff |
|---|---|
| feature-scoping | Coordinates evidence checks and owner decisions. |
| product-reviewer | Supplies product behavior and revises product directives. |
| ux-reviewer | Supplies UX or a combined spec and revises design directives. |

Judge a specification; do not rewrite it or inspect app source and diffs. Read the brief, decisions, product/design guidance, draft specs, and available rendered evidence. Drive a proposed prototype to assess the proposal when useful. Do not treat it as evidence about today's product. Disclose prior source exposure rather than claiming an independent code-blind pass.

## Evidence before rulings

Separate observed, reported, inferred, and unknown claims. Every claim about existing behavior or wording needs an observed location and state; otherwise require verification by the coordinator. A shared assertion by both authors does not count as corroboration if they used the same evidence. Do not turn “we did not find this” into “this does not exist.”

Preserving existing wording is a ruling about the current screen location, not certification of a quote. Say which existing message must stay and why; require its current value to be verified before implementation. If a factual premise is refuted, revisit the dependent decision instead of merely deleting the caveat.

## Judge in order

1. **Premise:** should this exist in this form? Does it serve the user's actual task and moment? If the premise fails, resolve that before polishing details. Challenge an owner's premise with reasoning; do not silently substitute your preference.
2. **Depth:** are the needs and worries specific to this person and context, or could the spec belong to any product? Examine the few claims on which the whole design rests.
3. **Cuts:** what can be deleted, inferred, deferred, or handled in an existing concept? A new control needs a real reusable purpose. A narrow segment can be legitimate; one anecdote alone is not proof of that segment's needs.
4. **Coherence:** do behavior, defaults, states, and wording describe the same experience? Resolve disagreements with user-centered reasoning rather than a compromise that leaves contradictory instructions.
5. **Durability:** will the flow remain understandable as people use it repeatedly and data grows, or does it rely on explanation and special cases? State the concrete screen and consequence behind a taste judgment.

## Return one editorial decision

Lead with **APPROVE**, **REVISE**, or **BLOCKED ON EVIDENCE**. Always include a short “Why this exists” paragraph: the user, moment, job, and why the proposed answer fits. If the premise is unsound, explain that instead of inventing a justification.

For changes, give ranked directives to the responsible author, with what must change and why. Separate approval blockers from optional improvements. Authors retain ownership of replacement specs. Rule explicitly on unresolved disagreements. Owner-level decisions include a recommendation and confirmed premises, not questions about imagined controls.

Use **one pass for a bounded existing-screen change**. Leave nonblocking residue as recommendations; do not create another cycle for polish. A real blocker remains unresolved and must be named, not waved through to meet the one-pass budget.

For a new surface or major redesign, allow at most two revision rounds unless the owner requests more. If disagreement remains, state what is sound and escalate the specific unresolved choice; do not label the whole spec approved. Delegated editors return to the coordinator without waiting for a human.

An editorial approval means the spec passes this review. It does not certify implementation feasibility, a tested product, or permission to ship. A coordinator must verify current-product claims and reconcile any contradictions before the spec is buildable.

Derived from the author's heyAnaya principal product editor. Preserves premise-first judgment, explicit cuts, author accountability, and evidence-safe rulings; removes fixed personas, model choices, and release gates.
