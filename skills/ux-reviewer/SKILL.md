---
name: ux-reviewer
description: Author a UX specification or review rendered UI for hierarchy, interaction, state coverage, accessibility, and microcopy. Use for a running interface or a proposed design; small existing-screen changes can receive one combined product and UX spec. Not a source-code review.
---

# UX reviewer

## Composes with

| Skill | Handoff |
|---|---|
| feature-scoping | Supplies the brief, decisions, and evidence pack. |
| product-reviewer | Exchanges constraints for a new surface or major redesign. |
| product-editor | Evaluates the specification and resolves product/design disagreements. |

Choose **spec** or **review** from the request. Own interaction, visible states, and exact microcopy as well as appearance. Use this product's design guidance and rendered reference if they exist; do not import another product's typography, component rules, colors, or persona.

## Ground in the rendered experience

Judge the app or current captured evidence without reading source, diffs, or CSS files. Inspecting the live page's computed styles, accessibility tree, and focus order is useful. Do not edit app code. Disclose any prior source exposure; relabeling a pass does not make it independent.

For existing-product findings record the app/screen, environment, viewport, state, capture time, and evidence. Separate observed behavior from reported facts, inference, and unknowns. A prototype only establishes what is proposed. Mark existing copy with its observed location; otherwise label it new or unverified. Avoid “never” or “does not exist” claims from a limited walkthrough.

Compare the actual rendered reference with the app. If reference and written guidance conflict, surface the conflict and use the confirmed intended reference for visual judgment; do not silently overrule explicit accessibility requirements or owner decisions. If no reference exists, explain the user impact rather than inventing a house-style violation.

## Inspect the whole interaction

- **Hierarchy:** can a first-time user see the key fact and next action? Does the same concept look and behave consistently elsewhere?
- **Real content:** test relevant long names, large values, languages, narrow viewports, and zoom. Choose viewport sizes appropriate to the product; record them.
- **States:** inspect loading, empty, error, success, and partial/stale data where relevant and reachable. Empty states teach the next action. Errors say what survived and how to recover. Success proves what changed. Report unreachable states as untested, not missing.
- **Interaction:** focus placement/order, keyboard and escape behavior, labels, contrast, touch use, confirmation or undo, and clear response during delays. Apply the project's accessibility requirements; do not invent compliance from a screenshot.
- **Copy:** name the object and outcome, use clear action verbs, put meaning first, and answer the moment's worry. Write replacement wording for each copy finding; “improve copy” is not actionable.
- **Perceived stability:** layout shifts, scroll jumps, clipped text, misleading flashes, and delayed or ambiguous feedback can damage trust even if the action eventually succeeds.

Screenshots support visual findings. Record steps or a short recording for timing and keyboard findings that a still image cannot establish. Do not let a screenshot requirement erase a reproduced interaction defect.

## Spec mode

For a bounded change to an existing screen, write one combined product and UX spec from the evidence pack: user and trigger, entry point, behavior, defaults, layout, state transitions, exact copy, recovery, acceptance criteria, and exclusions. A new user accepting defaults should succeed. Explain why a new control is needed rather than assuming every request needs a setting.

Prototype only an unresolved choice in this light mode. One focused mock is often enough; a full rebuild is not required. Present-tense claims still need current evidence.

For a new surface or major redesign, exchange the draft with the product author when authorized. Fix the layout when a user job is unserved; preserve real disagreements for the editor. A chosen novel interaction should have a playable prototype of its essential flow: discovery, main action, cancel/recovery, and relevant loading/error/success states reachable through interaction. Static direction sketches are fine for comparing alternatives but do not prove the flow works.

Use an isolated prototype and synthetic or approved test data; do not send messages or mutate live data to demonstrate a design. If implementation is outside scope, deliver the spec and explicitly mark the prototype unbuilt. Label simulated behavior. Verify any prototype you do build by using it, not just reading its code.

## Review mode

Drive the app through the agreed user scenarios, with the rendered reference beside it where available. Review the experience as it runs, not whether source resembles a specification. Explain the user consequence of a spec deviation; harmless divergence is not automatically a blocker.

If only screenshots or recordings are available, state their coverage and limit conclusions to what they show. Do not claim live interaction validation. Return findings ranked by blocked use, meaningful friction/trust damage, and polish. Each names the screen/state, user impact, evidence, concrete correction or exact replacement copy, and affected reach if measured. End with tested coverage and untested states.

Return genuine owner choices with a recommendation. Delegated reviewers report to the coordinator without waiting for human replies. Review completion does not authorize implementation or release.

Derived from the author's heyAnaya UX owner-reviewer and lighter existing-screen workflow. Preserves rendered evidence, complete states, and exact copy while removing the clinic design system and fixed tools.
