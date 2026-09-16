---
name: package-a-book
description: Package a locked Markdown manuscript into a reflowable EPUB, print-ready PDF, and optional phone-first reader site. Use after the prose is approved, when edition integrity, art direction, privacy, and release verification matter; do not use to draft or substantively edit the book.
---

# Package a Book

Turn one approved manuscript into editions that feel designed for the reader without letting production silently rewrite the book.

## Composes with

| Edge | Skill | When it applies |
|---|---|---|
| receives from | `write-a-book` | after editorial approval and manuscript lock; it can also start from any independently supplied locked manuscript |

## Non-negotiable boundary

Treat the supplied Markdown as locked unless the user explicitly reopens editing. Typography, page breaks, metadata, captions, alt text, and navigation may change. Prose, order, claims, and meaning may not.

If production exposes a writing problem, record it and ask whether to reopen the manuscript. A late correction must unlock the source, produce a new lock and hash, and rebuild every requested edition. Never fix it only in one edition.

## Start with a release brief

Resolve only choices that materially change the outputs:

- title, author/imprint, language, and edition name
- requested editions: EPUB, PDF, optional site
- primary reading device and PDF page size
- visual mood, illustration density, and supplied assets
- intended site visibility; deployment and publication still require separate authorization
- whether reading progress, highlights, or notes are local-only or account-synced

Infer safe defaults when the context answers these. Do not make the user pick implementation details.

## Production sequence

1. Copy the locked manuscript into an isolated production directory. Record its SHA-256 before transforming it.
2. Build one semantic intermediate edition from the locked source. Derive EPUB, PDF, and site from that edition instead of maintaining three prose copies.
3. Create an art direction sheet before generating or placing art. Read [references/art-direction.md](references/art-direction.md) when the book needs a cover, illustrations, stickers, or decorative marginalia.
4. Produce the requested formats. Read [references/production-workflow.md](references/production-workflow.md) for format-specific requirements and the optional starter in `assets/production-kit/` when useful.
5. Verify content and behavior before calling the release complete. Read [references/verification.md](references/verification.md) and run `scripts/verify_package.py` against a release manifest.
6. Present the actual files and site URL, plus a short verification report. Name anything not verified.

## Design rules

- Design for the primary reader, not for a generic “book” aesthetic.
- Keep the EPUB reflowable. Do not reproduce print pages as images.
- Let the PDF feel composed, but preserve comfortable text size and margins on the target device.
- Use illustrations to deepen a moment, pace a section, or carry a recurring visual language. Do not decorate every gap.
- Covers must remain legible as a phone thumbnail and must not rely on generated text inside artwork.
- Captions must describe the actual image. Inside jokes and personal references belong only when the source supports them.
- Provide useful alt text. Decorative art should be marked decorative rather than narrated.
- Keep one visual system across formats: palette, type roles, spacing, rules, and image treatment.

## Privacy and authorization

- Inventory names, messages, photographs, locations, private anecdotes, and identifying metadata before packaging.
- Do not upload private text or assets to a model, converter, host, or analytics service without the user's authorization.
- A local build does not authorize publication. A working site does not authorize making it public.
- Strip hidden comments, source paths, EXIF data, debug files, and unused originals from release artifacts.
- Never use a real private project as a public fixture, demo, or eval. Use synthetic material.

## Release standard

A release is complete only when:

- the locked-source hash is recorded and unchanged
- artifact-derived normalized ordered text streams show that reader-visible prose was not dropped, duplicated, reordered, or altered; format-only additions are explicitly inventoried
- EPUB navigation, metadata, images, and reflow work in at least one real reader
- PDF cover, contents, page breaks, running matter, links, and image quality were visually inspected
- the site was tested at 320 px, 390 px, and desktop; progress restore, time left, selection UI, dismissal, storage, privacy, and account isolation match what was promised
- accessibility and privacy checks pass
- final filenames are stable and old drafts are excluded from the release folder

Do not report “verified” from a successful command alone. Pair structural checks with rendered inspection.
