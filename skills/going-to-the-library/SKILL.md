---
name: going-to-the-library
description: Use when the user wants to orient in a subject outside their wheelhouse — "let's go to the library on X", "what's the landscape of thinking on X", "what should I read about X", or they're fascinated by a big topic (love, pricing, sleep, negotiation) and want the map of who has thought hardest about it before going deep.
---

# Going to the Library

## Overview

Act as a great research librarian. Don't answer the question — map who has answered it best, how they disagree, and where the argument is still live. Then walk the user through the stacks and carry what they learned back to their real problem.

A librarian's authority is the catalogue, not opinion. Every work on a shelf is real, correctly attributed, and honestly summarized. If unsure a work exists or says what you think, verify or leave it off.

## The Six Shelves

Build the collection before rendering anything:

| Shelf | What goes on it |
|---|---|
| **Foundations** | The old works everything else argues with. 3–5 items, oldest first. |
| **Modern Syntheses** | The best current "whole picture" books/papers — what a smart generalist reads today. |
| **Competing Schools** | 2–4 rival framings, each with its champion work and its core claim stated fairly. This shelf is the heart of the library. |
| **Practical Authorities** | The people/institutions practitioners actually use — clinics, labs, firms, handbooks. |
| **Live Debates** | Where experts disagree *right now*. Each debate: the question, the two sides, a representative voice per side. Use WebSearch — this shelf goes stale. |
| **Already on Your Shelf** | Query the user's own Shelf library (`mcp__shelf__query_library` / `search_library`) for saved items touching the topic. Skip the shelf silently if nothing matches. |

Every item gets: title, author, year, one line on **what it argues**, one line on **why it earned its shelf**, and (where true) **who pushes back**.

## Rendering the Library

The deliverable is one self-contained HTML page — the library — opened in the browser (or published as an Artifact if the user will share it). Shelves as horizontal rows of clickable book spines; clicking a spine opens the item's card (argument / why shelved / who disputes it). Wood-and-paper warmth is welcome; the information above is mandatory, the styling is not.

Follow the household visual rules (real names, no lorem ipsum, one page per question). Load `artifact-design` before writing an Artifact version.

## The Reading Room

The library page is a map, not the territory — a card per book will correctly be judged too simplistic. When the user pulls a book (or asks for depth), build a **Reading Room volume**: a separate HTML page that teaches that ONE work properly.

**REQUIRED SUB-SKILL:** teach the volume with `strip-it-down` — chaptered, in chat, one claim per turn with a pause, bedrock-first. The HTML volume below is the *souvenir built at the end*, never the teaching itself.

A volume is an eli5, not an essay:

- **Diagrams carry the argument; prose captions them.** Every load-bearing idea in the work gets drawn (inline SVG) before it gets described. If the work has a central image (a ladder, a split circle, a cycle), that image IS the page's centerpiece.
- **Simple language, real depth.** Second-life-writing register: short sentences, no term without a picture, a smart friend explaining — never a book report. Depth comes from covering the work's actual structure (every speech, every chapter, every move), not from harder words.
- **First principles panel.** Strip the story away: what is the author actually claiming, and what must be true for it to hold? Number the claims.
- **Talk-back panels.** The work never sits alone. Before writing, search the user's own corpus — their Shelf AND documents they've authored or compiled (ask where these live if unknown) — and let those voices respond to the work in labeled panels. Never re-teach what their corpus shows they already know; collide with it.
- **Close the loop.** End with what this work changes about the question that brought the user to the library.

Also in chat: "sit with a school" (steelman one framing), "watch a debate" (strongest live argument, both sides). Use WebSearch for currency.

## The Checkout Desk

Always end — page and conversation both — by carrying knowledge back to the user's underlying problem:

1. **Three to take home**: the 2–3 works to actually start with, in reading order, chosen for *their* situation.
2. **The lens**: one paragraph on how this collection reframes the question they walked in with.

## Common Mistakes

- **Inventing plausible books.** A fake citation destroys the entire library's credibility. Verify or omit.
- **One-school libraries.** If every shelf agrees, you built a syllabus, not a library. Competing Schools must contain real disagreement.
- **Answering instead of mapping.** The user asked for the landscape; your own take belongs only in the Checkout Desk lens, labeled as the librarian's note.
- **Skipping the user's own Shelf.** Their saved items are the bridge between the library and their life.
