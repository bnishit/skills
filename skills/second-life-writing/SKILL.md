---
name: second-life-writing
description: >
  Write in simple English that anyone can understand, calibrated precisely for the audience, and built to be
  useful long after the author has moved on. Use this skill whenever Claude is producing ANY text for the user:
  emails, Slack messages, PRDs, specs, articles, release notes, announcements, reports, proposals, or any
  other writing. Even short messages benefit from audience clarity, simple language, and anti-slop filtering.
  If Claude is writing words a human will read, this skill applies. Trigger on any writing, drafting, editing,
  or content creation task — even casual messages.
---

# Second-Life Writing

Write so anyone can read it, the right people find it useful, and it still works six months from now when you're not around to explain it.

Three rules, in order of importance:

1. **Simple English** — use small words, short sentences, no showing off.
2. **Write for the reader, not yourself** — change your language, depth, and structure based on who reads this.
3. **Build for the second life** — your writing will be reused. Make sure it works without you.

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

When one document serves multiple audiences, do not write one version for everyone. Create clearly separated sections labeled plainly: "For Sales", "For Support."

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

## Quick Check (before delivering)

1. **Simple enough?** — Any sentence over 25 words? Any unnecessarily complex word? Fix them.
2. **Right audience?** — Would this actually help the person reading it?
3. **Stands alone?** — Readable in six months with zero context?
4. **No slop?** — Any filler, jargon, or AI patterns? Cut them.
5. **Right format?** — Should this be a document, or would a tool work better?
