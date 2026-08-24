---
name: apprentice
description: Use when the user wants to become able to DO something over many sessions — a practice, a craft, an instrument, a language, a physical skill — and wants the state of their learning kept on disk so any session can resume it. Not for mapping a field's thinking, and not for one hard idea explained in chapters.
---

# Apprentice

Take someone from cannot-do to can-do, across sessions, with the state on disk so no session starts from zero.

An apprentice is not a student. They are in the workshop, doing the thing badly, on purpose, under supervision. Every session ends with a rep they owe you before the next one.

## Composes with

| Edge | Skill | When it fires |
|---|---|---|
| **reaches for** | `second-life-writing` | before drafting any lesson, and as a check before the turn ends |
| **reaches for** | `show-me` | whenever the thing has a shape — a form, a sequence, a layout, a signal chain |
| **reaches for** | `strip-it-down` | when a single idea underneath the practice is the blocker, not the practice itself |
| reached for by | — | this is an entry point |

**Not this skill, if** they want to understand a field rather than perform in it — that is `going-to-the-library`. Or if one dense idea is the whole job — that is `strip-it-down`. Apprentice is for when the test of learning is *doing it*, not explaining it.

## Credit and what was changed

Based on **Matt Pocock's `teach` skill**, which supplied the durable idea: a learning workspace on disk, lessons as the unit, and the split between fluency strength (retrieval now) and storage strength (retention later).

Four deliberate changes, each from watching the original run:

1. **One state file, not five.** The original spreads state across a mission doc, a resources doc, learning records, notes and a glossary. In a real multi-session run the learner's own answers were recorded in none of them. Apprentice keeps `PRACTICE.md` and requires the answers.
2. **The learner's words, verbatim.** Never a paraphrase, never cleaned up. Their wording is the diagnostic, and it is what makes the next lesson theirs.
3. **A rep they owe, every session.** The original's field practice was optional. Here the session does not end without one, and the next session opens by asking how it went.
4. **A counted lesson contract**, so a lesson cannot quietly become a wall of text. Prose drifts upward every session unless something counts it.

## Step 0 — Ask before building

Use `AskUserQuestion`, two or three questions, once:

- **What do you want to be able to do that you can't do now?** Their answer, verbatim, is the first line of `PRACTICE.md` and every lesson ties to it.
- **What have you already tried, and where did it break?** This sets the starting rung. Assume zero otherwise — owning the gear is not practice, and reading about it is not practice.
- **How often will you actually practise, honestly?** The cadence sets lesson size. Twice a week is a different curriculum from daily.

## Step 1 — `PRACTICE.md`, the only state

```
GOAL (their words): "..."
STARTING POINT: what they could already do on <date>
CADENCE: <what they said, not what you'd like>
NOW: lesson N — <the one thing being drilled>
REP OWED: <what they must do before the next session>

## Log — newest last
N. <the one thing> ✅ <date>
   ASKED: "<the check, verbatim>"
   ANSWERED: "<their words, uncorrected>"
   REP: <what they were set> → <what happened, in their words>
   READ: got it / shaky / wrong model — <what that changes next session>
```

A field with nothing in it is a session that isn't finished.

## Step 2 — One lesson = one thing they can do by the end

Six slots, in order. Count before sending.

1. **CARRY** — 1 sentence. Their last rep and how it went, in their words.
2. **THE ONE THING** — ≤8 words. What they'll be able to do at the end of this lesson.
3. **DEMO** — the move itself, shown not described. If it has a shape, `show-me` draws it.
4. **YOUR TURN** — the smallest rep that proves the move. Doable now, in under five minutes.
5. **THE COMMON WAY IT GOES WRONG** — 1 sentence. Name the failure before they hit it.
6. **REP OWED** — what they do before the next session, and how they'll know it worked.

**Prose budget: 150 words across slots 1, 4, 5, 6.** Over means cut.

Then stop. One lesson per turn. Their rep sets the pace — landed it, drill the next thing; struggled, the struggle *is* the next lesson; skipped it, ask what got in the way before teaching anything.

## Step 3 — Feedback beats explanation

When they report a rep, respond to what they actually did, not to what the lesson said. A wrong rep is better data than a right answer, and the correction is the teaching. Do not re-explain the lesson — that is how a practice turns back into reading.

## Quick reference

| Move | Rule |
|---|---|
| State | one file, `PRACTICE.md`, answers verbatim |
| Lesson | 6 slots, 150 prose words, one doable thing |
| End | a rep they owe, always |
| Pace | their rep decides: next / re-drill / find the blocker |
| Register | `second-life-writing`, every time |
