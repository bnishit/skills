---
name: second-life-writing
description: >
  Write simple, audience-aware text that remains useful when reused. Supports brief mode for short-lived
  messages and operational mode for cross-team or long-lived documents. Use for emails, Slack messages, PRDs,
  specs, articles, release notes, announcements, reports, proposals, and any writing, drafting, or editing task.
---

# Second-Life Writing

Write so anyone can read it, the right people find it useful, and it still works six months from now when you're not around to explain it.

Three rules, in order of importance:

1. **Simple English** — use small words, short sentences, no showing off.
2. **Write for the reader, not yourself** — change your language, depth, and structure based on who reads this.
3. **Build for the second life** — your writing will be reused. Make sure it works without you.

---

## Choose a Mode

Honor an explicit mode:

- `$second-life-writing brief`
- `$second-life-writing operational`

Otherwise, choose from the reader's needs:

### Brief

Use for Slack updates, short emails, executive summaries, and messages with one main audience or action.

- Lead with the result or ask.
- Keep the context, action, risk, and limit the reader needs now.
- Group audiences when they need the same information.
- Produce the shortest complete version. Do not cut a fact merely to hit a word count.

### Operational

Use for launches, support notes, rollout plans, incident guidance, specs, and documents that several teams will reuse.

- Preserve the facts, reasons, risks, actions, owners, and limits readers need later.
- Separate audiences only when their actions or required detail differ.
- Prefer useful bullets and short sections over dense prose.
- Mark missing operating facts. Never invent them to make the document feel complete.
- Stay inside the source. Do not create policies, metrics, owners, launch gates, workflows, or severity rules that the source does not support.
- Use examples only from the current task. Never import people, industries, or scenarios from unrelated instructions or earlier work.
- Produce an announcement when asked for an announcement. Do not expand it into a runbook, PRD, or test plan unless asked.
- State shared context and actions once. Keep audience sections only for what differs.
- Do not turn a risk or plausible outcome into a claimed goal or benefit.
- Do not add a user flow, template, or framework unless the source provides it or the reader needs it to act.

Choose **operational** when the document affects several teams, changes customer access or money, or could cause harm if a detail is lost. Choose **brief** when the message is short-lived and one clear action matters most.

---

## Rule 1: Simple English

Write at a 6th-to-8th grade reading level. This is not about dumbing things down. It is about being clear.

- Average sentence length: 12–18 words. Never past 25.
- Use common words. If a simpler word says the same thing, use it.
- One idea per sentence.
- Active voice over passive. ("QA found the bug" not "The bug was found by QA")
- No nested clauses. If you run out of breath reading it aloud, it is too long.

Simple English does NOT mean removing technical terms your audience knows. Engineers know "API" and "dead-letter queue." Keep those. Simple and precise are not opposites.

For the full word swap table (what to avoid and what to use instead), see [references/word-swaps.md](references/word-swaps.md).

---

## Rule 2: Write for the Reader

Before writing anything substantial, ask the user: "Who will read this?" and "Will other people or teams use this later?"

For quick writing (Slack, short emails), figure out the audience from context.

Different audiences need completely different writing. Engineers need exact details with no room for guessing. Sales needs talking points they can say on a call. Support needs step-by-step troubleshooting. Execs need two paragraphs max.

When one document serves multiple audiences, follow the selected mode. In operational mode, create separate sections when readers need different actions. In brief mode, group readers who need the same information.

For detailed guidance on what each audience type needs, see [references/audience-guide.md](references/audience-guide.md).

---

## Rule 3: Build for the Second Life

Your writing will be used again. A PRD becomes a decision log. A scenario sheet becomes a debugging tool. A release note answers "when did we change that?" six months later.

**The standalone test:** Imagine someone reads this in six months. They have never met you. Can they understand it and use it?

If not, add: a brief context line at the top, the reasoning behind decisions (not just the decisions), definitions for team-specific terms, and real numbers instead of vague descriptions.

**When to suggest a tool instead:** If the writing involves scenarios with calculations, logic people want to test with different inputs, or data that changes — suggest an interactive tool rather than a static document.

---

## Anti-Slop (always apply)

AI text has recognizable patterns. These quick rules catch the worst ones:

- **Cut filler:** If a phrase announces you're about to say something, remove it. ("Here's the thing:", "It turns out", "Let me be clear")
- **No emphasis crutches:** "Full stop.", "Let that sink in.", "This matters because"
- **No binary contrasts:** "Not because X. Because Y." Just state Y.
- **No dramatic fragments:** "Speed. Quality. Cost." Write a normal sentence.
- **Vary rhythm:** Mix sentence lengths. Two list items often beat three.
- **Trust the reader:** Do not explain why something matters after you say it.

For the full anti-slop checklist with examples, see [references/anti-slop.md](references/anti-slop.md).

---

## Make Every Line Earn Its Place

Keep a line when it adds meaning, evidence, action, a limit, or context the reader needs. Cut repetition, throat-clearing, and detail that serves no reader.

Run one compression pass after drafting:

1. Remove lines whose loss changes nothing.
2. Merge repeated points.
3. Replace vague claims with one concrete detail.
4. Stop before a cut removes meaning, proof, action, or needed context.

Compression means no waste. It does not mean every document must be short.

---

## Quick Check (before delivering)

1. **Simple enough?** — Any sentence over 25 words? Any unnecessarily complex word? Fix them.
2. **Right mode?** — Brief for the shortest complete message; operational when detail must survive reuse.
3. **Every line useful?** — Does it add meaning, proof, action, a limit, or needed context?
4. **Source-safe?** — Did you add a policy, promise, owner, example, or fact the source does not support?
5. **Right audience?** — Would this actually help the person reading it?
6. **Stands alone?** — Readable in six months with zero context?
7. **No slop?** — Any filler, jargon, or AI patterns? Cut them.
8. **Right format?** — Should this be a document, or would a tool work better?
