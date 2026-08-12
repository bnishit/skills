---
name: second-life-writing
description: >
  Write compact, plain-English text for the actual reader, with every line earning its place and enough context
  to remain useful when reused later. Use for emails, Slack messages, PRDs, specs, articles, release notes,
  announcements, reports, proposals, and any other writing, drafting, editing, or content creation task.
---

# Second-Life Writing

Write so anyone can read it, the right people find it useful, and it still works six months from now when you're not around to explain it.

Four rules, in order of importance:

1. **Simple English** — use small words, short sentences, no showing off.
2. **Every line earns its place** — make the point, keep what helps, cut the rest.
3. **Write for the reader, not yourself** — change the depth and structure based on who reads this.
4. **Build for the second life** — your writing will be reused. Make sure it works without you.

---

## Rule 1: Simple English

Write at a 6th-to-8th grade reading level. This is not about dumbing things down. It is about being clear.

- Average sentence length: 12–18 words. Never past 25.
- Use common words. If a simpler word says the same thing, use it.
- One idea per sentence.
- Active voice over passive. ("QA found the bug" not "The bug was found by QA")
- No nested clauses. If you run out of breath reading it aloud, it is too long.

Simple English does not mean removing terms the audience knows. Engineers know "API." Support may know "paywall." Define a term only when the intended reader may not know it.

For the full word swap table (what to avoid and what to use instead), see [references/word-swaps.md](references/word-swaps.md).

---

## Rule 2: Every Line Earns Its Place

Find the one point the reader must remember. Lead with it. Everything else must support it.

Keep a line only if it does at least one job:

- adds a fact, reason, or constraint
- gives evidence or a concrete example
- tells the reader what to decide or do
- adds context needed to understand the rest

Cut a line if it repeats the point, announces what comes next, states the obvious, or serves no reader action. Do not keep text to display effort.

Run a compression pass after drafting:

1. Remove any line whose loss changes nothing.
2. Merge repeated points and overlapping sections.
3. Replace broad claims with one concrete detail.
4. Stop when further cuts would remove meaning, proof, action, or needed context.

Efficient writing is not always short. A long document is justified only when each part helps its reader. Use one clear point per paragraph or section. Use a story or analogy only when it makes a hard idea easier to grasp.

## Rule 3: Write for the Reader

Before writing anything substantial, ask the user: "Who will read this?" and "Will other people or teams use this later?"

For quick writing (Slack, short emails), figure out the audience from context.

Different audiences need completely different writing. Engineers need exact details with no room for guessing. Sales needs talking points they can say on a call. Support needs step-by-step troubleshooting. Execs need two paragraphs max.

When one document serves multiple audiences, separate them only when their actions or needed detail differ. Do not create an audience section merely to acknowledge that group.

For detailed guidance on what each audience type needs, see [references/audience-guide.md](references/audience-guide.md).

---

## Rule 4: Build for the Second Life

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

## Quick Check (before delivering)

1. **Simple enough?** — Any sentence over 25 words? Any unnecessarily complex word? Fix them.
2. **One clear point?** — Can the reader say what this is about in one sentence?
3. **Every line useful?** — Does each line add meaning, proof, action, or needed context?
4. **Right audience?** — Would this help the person reading it?
5. **Stands alone?** — Readable in six months with zero context?
6. **No slop?** — Any filler, jargon, or AI patterns? Cut them.
7. **Right format?** — Should this be a document, or would a tool work better?
