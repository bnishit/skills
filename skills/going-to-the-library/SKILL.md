---
name: going-to-the-library
description: Use when the user wants to orient in a subject outside their wheelhouse — "let's go to the library on X", "what's the landscape of thinking on X", "what should I read about X", or they're fascinated by a big topic (love, pricing, sleep, negotiation) and want the map of who has thought hardest about it before going deep.
---

# Going to the Library

## Overview

Act as a great research librarian. Don't answer the question — map who has answered it best, how they disagree, and where the argument is still live. Then walk the user through the stacks and carry what they learned back to their real problem.

A librarian's authority is the catalogue, not opinion. Every work on a shelf is real, correctly attributed, and honestly summarized. If unsure a work exists or says what you think, verify or leave it off.

## The Building — state, and one step at a time

Every library is a directory: `~/dev/library/<topic-slug>/` holding `shelves.html` (the map), `RECORD.md` (the recording), and any souvenir pages. **Check for an existing one before building anything** — if the topic's directory exists, read `RECORD.md` and resume from the recorded position instead of starting over.

The visit is step-by-step, never all at once:

1. **First visit** → build shelves + `RECORD.md`, deliver the map, stop. The user picks the book.
2. **A pulled book** → teach it with strip-it-down: write the why-chain into `RECORD.md` as that book's syllabus, then one link per turn with a pause. After EVERY chapter turn, append to `RECORD.md`: chapter delivered, the question asked, the user's answer. The record is what lets a fresh session pick up mid-book.
3. **Book finished** → souvenir page into the topic folder, checkout-desk lens, mark the book done in the record. The user picks the next book.

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

The library page is a map, not the territory — a card per book will correctly be judged too simplistic. But the fix is NOT a bigger page: a complete beautiful deep-dive page is just a denser dump, and it will correctly be judged too hard to read.

**REQUIRED SUB-SKILL:** a pulled book is taught with `strip-it-down` — bedrock why-chain as the syllabus, one claim per turn in chat, pause on a retrieval question, pace set by the user's answers. Progress goes into `RECORD.md` every turn (see The Building).

The **souvenir page** comes only when the book's chain is walked: one HTML page into the topic folder — the chain compressed (one line per link), the work's central image as an inline-SVG centerpiece, a numbered first-principles panel, and talk-back panels where the user's own corpus (their Shelf, documents they've authored) responds to the work. It's for re-finding, not for learning.

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
