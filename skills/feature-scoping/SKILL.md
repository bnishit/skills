---
name: feature-scoping
description: Scope a user-facing feature with the owner before implementation. Inspect what exists, resolve the important product decisions, explore only useful design alternatives, and hand off a buildable brief. Use when asked to scope or shape a feature; not for routine fixes or an already settled specification.
---

# Feature scoping

## Composes with

| Skill | Handoff |
|---|---|
| product-hypothesis-pressure-test | Optional, when the behavioral premise needs testing before choosing a feature. |
| product-reviewer | Product specification for a new surface or major redesign. |
| ux-reviewer | Combined product and UX specification for an existing screen; UX specification for a new surface. |
| product-editor | One editorial pass on the resulting specification. |

Run scoping in the owner-facing conversation. The goal is shared understanding, not a document the owner cannot explain. Use the existing project context and tools; no particular browser, model, directory, or industry is required.

## Ground the starting point

Inspect the current product, relevant source when available, product/design guidance, and prior decisions. State the environment and version or capture date. Inventory what exists, partly exists, overlaps, or conflicts with the idea. Do not ask the owner for facts you can discover. Source establishes implementation, not proof a path ran in production; measure any claimed affected population or label it unmeasured.

Play back the few facts that could change the scope. For example, a requested new signal may already exist but be hard to find. Prefer improving its existing home over adding another control.

## Resolve decisions in dependency order

Start with the premise, then the person and moment, the task and anxiety, scope boundaries, defaults, and success criteria. Challenge a weak premise plainly, with a reason and recommendation. Do not silently replace the owner's chosen objective.

Ask one material question at a time, with your recommended answer and why. Wait for an answer when the decision belongs to the owner. Do not repeat decisions already settled or force a ceremony on a complete brief. If asked for an autonomous draft, proceed with explicit assumptions and mark unresolved decisions.

Keep one short scoping document current: premise, user and moment, decisions, entry points, flow, defaults, success evidence, exclusions, and open questions. Use the project's existing document location. A person accepting the defaults should reach the intended value; settings are not the automatic answer to a single customer's request.

Use a small flow, table, or before/after view where it clarifies the decision. For a contested design, show a few materially different options and recommend one. Do not manufacture alternatives for settled choices. Direction sketches compare proposals; they do not diagnose the current product.

## Choose the smallest handoff

Do not expand a scope-only request into implementation or a full design process. When specification is requested or authorized, use:

- **Existing screen, bounded change:** one UX author covers both behavior and design, followed by one editor pass. Supply a current evidence pack. Prototype only the disputed interaction, if any. Nonblocking editorial suggestions remain recommendations; unresolved factual or product blockers stay explicit.
- **New surface or major redesign:** product and UX authors make separate drafts, exchange them, and record disagreements for the editor. A chosen novel interaction needs a playable prototype covering its essential flow and reachable failure states. Do not require a whole application build to resolve a small design choice.

**REQUIRED SUB-SKILL:** load ux-reviewer when authoring the combined or UX specification, product-reviewer when authoring a separate product specification, and product-editor when evaluating the resulting spec. These skills are in the same collection; install the named companions for the full handoff. If unavailable, finish the scoping brief and state which review remains undone rather than claiming it happened.

Separate roles can run as fresh agents only when delegation is available and authorized. Otherwise use clearly labeled sequential passes and disclose that they are not independent reviews. A session that has read source cannot claim to become code-blind by changing its role label; provide a sanitized pack to a fresh reviewer where possible.

## Evidence pack and factual check

Give product/design reviewers the user story, decisions, screenshots or recordings of affected states, relevant product/design rules, a rendered reference where available, and a scenario list. Include the app URL, viewport, capture time, environment, and test-data limits. Review prompts describe what the user needs to do, not component names or the implementation's preferred path.

Keep source and diffs with the coordinator. Mark each claim as observed, reported, inferred, or unknown; mark proposed behavior as new. Existing strings need their observed screen and state. A prototype is evidence of a proposal only. Agreement between reviewers is not additional evidence when they relied on the same source.

Before treating the spec as buildable, verify claims about existing controls, copy, coverage, and machine behavior. Resolve contradictions with current evidence; rework decisions resting on a refuted fact. Do not pass an owner a decision about a supposedly existing control until it has been confirmed. Preserve-copy rulings attach to the current screen location, not an unverified quote. Record verified values in the handoff; keep technical evidence separate from the user-facing narrative.

End with the proposed experience in this order: user, entry point, trigger, visible behavior, shortest flow, value, and limits. State the next decision or handoff. Spec readiness does not authorize live data changes, sending messages, or shipping.

Derived from the author's heyAnaya scoping and product/UX workflow. Preserves grounded questions, factual checks, and the lighter existing-screen default; removes clinic-specific tooling and mandatory multi-agent ceremony.
