---
name: restock
description: Use when a topic needs what has happened *recently* rather than what is durably known — "what's the landscape on X these days", "what's changed on X", "what happened in the last 30 days", "is this still true" — or when an existing library, canon, or reading list needs checking for entries that have since been superseded, corrected, or retracted.
---

# Restock

A canon tells you what is durably known. It cannot tell you what happened last month, and it quietly rots: a book gets superseded, a famous finding gets a corrigendum, a live debate resolves. Restocking is the librarian's job of walking the shelves and pulling what no longer holds.

Two modes. **Sweep** answers "what's happened lately on X" from nothing. **Restock** points at an existing library and refreshes it.

## Composes with

| Edge | Skill | When it fires |
|---|---|---|
| reached for by | `going-to-the-library` | building the Live Debates shelf, and any time an existing library is reopened after a gap |
| **reaches for** | `second-life-writing` | before writing the brief |
| **reaches for** | `show-me` | when the finding is a trend, a timeline, or a disagreement between sources |

## Credit and what was changed

Based on **Matt Van Horn's [`last30days`](https://github.com/mvanhorn/last30days-skill)** (MIT), which supplied the core move: sweep many sources in parallel, score by engagement and freshness, merge duplicates across sources, synthesise one brief with citations.

Three changes, for this stack:

1. **It restocks a library, not just a topic.** The original produces a standalone brief. This one can point at an existing `~/dev/library/<topic>/` and write back into it — refreshing the Live Debates shelf and flagging shelved works that no longer hold.
2. **Supersession is a first-class output.** Not just "what's new" but "what on your shelf is now wrong." That is the failure mode a canon actually has.
3. **No-key sources first, always.** The original's full source list needs CLIs, logins and API keys. Here the free tier is the default and everything else is opt-in, so the skill never fails closed.

Use the original instead when you want its depth — 19 sources, transcripts, prediction-market odds, and an accumulating searchable library of briefs. It does things this one deliberately does not.

## Step 1 — Ask what "recently" means

Thirty days is the default, not a law. A fast-moving product question wants 30 days; a scientific claim wants two years; a live legal question wants "since the last ruling." Ask once if it is unclear, and say the window in the brief.

## Step 2 — Sweep, cheapest sources first

Run these in parallel. Never let a missing key stop the sweep:

- **Always free, no setup:** web search, Hacker News, Reddit (take the comments and the scores, not just the post), GitHub, arXiv.
- **Free with a tool:** YouTube transcripts (`yt-dlp`), Techmeme, Digg.
- **Opt-in, needs auth:** X, LinkedIn, Bluesky, prediction markets. Skip silently and say in the brief which sources were not searched.

Expand each query into several — the topic's name, its practitioners' names, the product or paper it competes with, and the phrase a critic would use. One query returns one echo chamber.

## Step 3 — Score and merge

Rank by engagement × relevance × freshness, then merge the same story across sources into one item. A thing reported in five places is one finding with five citations, not five findings. Note when a claim traces back to a single primary source that everyone else is quoting — that is the single most common way a weak claim looks strong.

## Step 4 — The supersession pass

The part that earns this skill's place in the stack. For each work or claim already on the shelf, check specifically for:

- a **newer edition or successor book** by the same author
- a **correction, corrigendum, or retraction**
- a **failed replication** or a meta-analysis that overturns it
- a **methodological demolition** that is well cited but never reached the popular version
- the **live debate having resolved**, or having moved

Report each as: what was shelved · what happened · what replaces it. If nothing has changed, say so — "still holds, checked <date>" is a real result and it stops the next session re-checking.

## Step 5 — Write it back

Standalone: one brief, sources grouped, every claim cited, and an explicit list of what was *not* searched.

Restocking a library: update the Live Debates shelf, add or amend entries on the debunked shelf, mark superseded works on their own cards rather than deleting them — *"superseded by X, <date>"* teaches more than a silent removal. Then append one line to `RECORD.md` saying what was restocked and when, so the next session knows how fresh the shelves are.

## Never

- Never present engagement as evidence. A finding with 4,000 upvotes and no source is a popular claim, not a fact.
- Never let recency outrank quality. A month-old blog post does not supersede a replicated finding; it is a data point about the conversation, not about the world.
- Never quietly drop a source that failed. Name it as unsearched.
