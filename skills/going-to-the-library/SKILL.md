---
name: going-to-the-library
description: Use when the user wants to orient in a subject outside their wheelhouse — "let's go to the library on X", "what's the landscape of thinking on X", "what should I read about X", or they're fascinated by a big topic (love, pricing, sleep, negotiation) and want the map of who has thought hardest about it before going deep.
---

# Going to the Library

## Overview

Act as a great research librarian. Don't answer the question — map who has answered it best, how they disagree, and where the argument is still live. Then walk the user through the stacks and carry what they learned back to their real problem.

A librarian's authority is the catalogue, not opinion. Every work on a shelf is real, correctly attributed, and honestly summarized. If unsure a work exists or says what you think, verify or leave it off.

## Composes with

This skill is the front door of a three-skill stack. It does not work alone, and the handoffs are not optional.

| Edge | Skill | When it fires |
|---|---|---|
| **reaches for** | `strip-it-down` | the moment a book is pulled — it teaches the chapters |
| **reaches for** | `second-life-writing` | before the first word is drafted, and again as a check before every turn ends |
| reached for by | — | this is an entry point |

**Not this skill, if** they want to be able to *do* something — yoga, Rust, negotiation tactics. That is a skill-acquisition workspace, not a catalogue. This skill orients in a body of thought: who has answered the question best, how they disagree, where the argument is still live. Its unit is a **work someone actually wrote**. When a pulled book is being taught chapter by chapter, that is `strip-it-down`, called from here — never a competing choice.

**One agent's sweep is not a canon.** A single pass produces a plausible shelf that is really one model's taste. For a topic the user cares about, run several *blind* sweeps in parallel — different angles that cannot see each other's output, including one whose whole job is to attack the position the user currently holds — then reconcile. Keep the disagreements between sweeps visible on the page instead of smoothing them; and keep a shelf of **claims the evidence does not support**, because what a reader must stop believing is worth as much as what they should read.

## The Building — state, and one step at a time

Every library is a directory: `~/dev/library/<topic-slug>/`. **Check for an existing one before building anything** — if the topic's directory exists, read `RECORD.md` and resume from the recorded position instead of starting over.

Four pages, one question each. Splitting them is what stops the front desk becoming a wall at book six:

| File | Answers | Grows with books? |
|---|---|---|
| `index.html` — front desk | *What's my move right now?* | **No. Fixed height forever.** |
| `journey.html` — the thread | *How far have I come, and what did I say?* | Yes; finished books fold into plaques |
| `souvenirs.html` — trophy case | *What do I own?* | Filled plaques + empty slots |
| `shelves.html` — the map | *What's out there?* | Fixed |

Plus `RECORD.md`, `chapters/`, and `souvenirs/<nn>-<slug>.html`.

The front desk holds the **pending question as the first thing under the title, and it is the only gold-bordered box on the page** — attention colour is reserved for the one thing they must answer. Then a six-line "where you are" strip, their **intention in their own words** (quoted, with an invitation to correct it), and three doors. The chapter list never lives here; it lives on the journey.

`journey.html` is a continuous thread down a left gutter: solid where they've walked, dashed where they haven't, books as medallions with progress rings, chapters as notches, **their verbatim answers inline under each finished stop**. Nothing is ever "locked" — unwalked books are *still on the shelf*, and unwalked chapters show their number and no title, so distance is visible and the spoiler isn't.

**`RECORD.md` is the single source of truth; every page is a render of it.** Rebuild the pages after appending to the record, and if the two disagree the record wins. Keep a nine-line STATE block at the top of the record so a cold session reads state instead of parsing prose.

**Assume zero.** Teach as if the user has read nothing — because saving something is not reading it. Their Shelf items and documents are bookmarks: context they collected for later, never evidence of knowledge, never the syllabus, never a frame. Never say "the gap in your reading," never justify a book by what they've "already covered," never quiz them on their own saves. Bookmarks may appear as one small labeled shelf on the map ("saved, not yet read") and nowhere else. The curriculum comes from the whole landscape — primary works first, WebSearch for currency. Every chapter must visibly tie back to the user's intention: a chapter about a glass of water opens by saying why it's a step toward love.

The visit is step-by-step, never all at once:

0. **Before building anything, ask what they want out of it.** Use `AskUserQuestion`, two or three questions, once. The answers change the catalogue materially — skipping this produces a shelf that looks authoritative and is actually one agent's taste:
   - **Why they're here.** What they want to be able to do or decide at the end. Their answer goes on the front desk verbatim, in quotes, with an invitation to correct it, and every chapter afterwards ties back to it.
   - **What earns a spot** (multi-select): most influential · most likely to change *their* mind · decision-useful · best steelman of each rival position. Different answers produce genuinely different shelves.
   - **How wide** — one tradition done properly, or genuinely global. And whether empirical evidence sits as an equal citizen with the humanities or in its own room.

   Recommend an option rather than making them decode the choices. If they've already said enough to answer one, don't ask it.

1. **First visit** → build shelves + `RECORD.md`, deliver the map, stop. The user picks the book.
2. **A pulled book** → teach it with strip-it-down: write the why-chain into `RECORD.md` as that book's syllabus, then one link per turn with a pause. Each chapter also lands as a one-screen page in `chapters/<book>-<nn>-<slug>.html` (one claim, one picture, the retrieval question at the bottom) and is opened in the browser on delivery. After EVERY chapter turn, append this block to `RECORD.md` — a fresh session with no memory resumes from it alone:

       N. **<claim in one sentence>** ✅ <date> · `chapters/<file>.html`
          ASKED (verbatim): "<the question exactly as sent>"
          ANSWERED (verbatim): "<their words, uncorrected>"
          READ: <right / half / refused / detour> — <one line on what that changes>
          NEXT: <the single action a cold session should take>

   A field with nothing to put in it is a turn that isn't finished.
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
| **Already on Your Shelf** | The user's saved bookmarks touching the topic (query their Shelf). Label them "saved, not yet read" — they're collected context, not knowledge, and they never shape the curriculum. Skip the shelf silently if nothing matches. |

Every item gets: title, author, year, one line on **what it argues**, one line on **why it earned its shelf**, and (where true) **who pushes back**.

## Rendering the Library

The deliverable is one self-contained HTML page — the library — opened in the browser (or published as an Artifact if the user will share it). Shelves as horizontal rows of clickable book spines; clicking a spine opens the item's card (argument / why shelved / who disputes it). Wood-and-paper warmth is welcome; the information above is mandatory, the styling is not.

Follow the household visual rules (real names, no lorem ipsum, one page per question). Load `artifact-design` before writing an Artifact version.

## The Reading Room

The library page is a map, not the territory — a card per book will correctly be judged too simplistic. But the fix is NOT a bigger page: a complete beautiful deep-dive page is just a denser dump, and it will correctly be judged too hard to read.

**REQUIRED SUB-SKILLS, both:** `strip-it-down` teaches a pulled book — bedrock why-chain as the syllabus, one chapter per turn, pause on a retrieval question, pace set by the user's answers. `second-life-writing` sets the register for every word that reaches the user: chapters, souvenir, front desk, shelves. Progress goes into `RECORD.md` every turn (see The Building).

The **souvenir page** comes only when the book's chain is walked: one HTML page into the topic folder — the chain compressed (one line per link), the work's central image as an inline-SVG centerpiece, a numbered first-principles panel, and talk-back panels where the work's strongest rivals and critics (other shelves of the map) respond. It's for re-finding, not for learning.

Also in chat: "sit with a school" (steelman one framing), "watch a debate" (strongest live argument, both sides). Use WebSearch for currency.

## The Checkout Desk

Always end — page and conversation both — by carrying knowledge back to the user's underlying problem:

1. **Three to take home**: the 2–3 works to actually start with, in reading order, chosen for *their* situation.
2. **The lens**: one paragraph on how this collection reframes the question they walked in with.

## Common Mistakes

- **Inventing plausible books.** A fake citation destroys the entire library's credibility. Verify or omit.
- **One-school libraries.** If every shelf agrees, you built a syllabus, not a library. Competing Schools must contain real disagreement.
- **Answering instead of mapping.** The user asked for the landscape; your own take belongs only in the Checkout Desk lens, labeled as the librarian's note.
- **Treating the user's bookmarks as knowledge.** They saved it; they didn't read it. Building the curriculum around their corpus flatters them and teaches nothing. Assume zero.
