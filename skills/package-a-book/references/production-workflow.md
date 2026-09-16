# Production workflow

Use only the sections for the requested editions.

## Canonical build model

Keep these layers separate:

1. **Locked source** — approved Markdown plus a recorded SHA-256.
2. **Semantic edition** — structured HTML/XHTML with stable chapter and reader-visible block IDs.
3. **Presentation** — shared design tokens plus format-specific CSS.
4. **Artifacts** — EPUB, PDF, and site generated from the semantic edition.

Do not copy-edit in the semantic or presentation layers. Keep generated files out of the source directory.

Recommended release layout:

```text
release/
  source/locked-manuscript.md
  build/semantic/
  assets/
  output/title.epub
  output/title.pdf
  output/site/
  release-manifest.json
  verification-report.txt
```

## Reflowable EPUB

- Use EPUB 3.3 with UTF-8 XHTML, a navigation document, and a complete OPF manifest/spine.
- Put `mimetype` first in the ZIP and store it uncompressed.
- Include title, author, well-formed language, identifier, modified time, cover metadata, and truthful accessibility metadata. Do not claim accessibility conformance without testing it.
- Split at meaningful chapter boundaries, not arbitrary byte or page limits.
- Use relative units and a linear reading order. Avoid fixed heights, positioned body text, and print page numbers.
- Embed only licensed fonts and compress images to a sensible display size.
- Mark decorative images with empty alt text; give meaningful images concise alt text.
- Preserve semantic headings, lists, landmarks, document language, and spine order. Test font scaling, dark mode tolerance, navigation, links, and images in a real reader.
- Run EPUBCheck. A structurally valid ZIP is not enough.

## PDF

- Confirm the intended use: phone reading, home printing, or commercial printing.
- Set explicit trim size, bleed if needed, margins, type scale, widows/orphans policy, and image resolution.
- Keep the title page, copyright/edition page, contents, part openers, chapters, epilogue, and afterword semantically distinct.
- Use running heads and page numbers only where they help. Suppress them on display pages.
- Prevent blank trailing pages and accidental isolated headings.
- Export fonts and links correctly. Inspect rasterized pages, not just the source HTML.
- Prefer a tagged PDF with document language, headings, lists, figures, alt text, bookmarks, and logical reading order. Do not claim PDF/UA conformance unless an appropriate validator and human inspection support it.
- For phone-first PDFs, favor a smaller page, larger body type, shorter lines, and fewer ornamental margins.

## Optional reader site

- Start with a readable page before adding application behavior.
- Include viewport metadata, semantic headings, focus states, reduced-motion support, and a comfortable mobile measure.
- Make chapter navigation, reading progress, and estimated time understandable without instruction.
- If highlights or notes exist, make the selection affordance obvious and dismiss it when selection clears or the user taps elsewhere.
- Show highlight controls only after a real non-empty selection inside readable book content. Dismiss them immediately when the selection clears, collapses, moves outside the book, or the user taps elsewhere.
- Calculate reading time left from the remaining reader-visible text and update it as the reader advances. Label it as an estimate.
- State storage truthfully:
  - `local-only`: stays in this browser/device
  - `account-synced`: requires authenticated server persistence and a tested read-back
- Treat highlights and notes as private content. Do not put authentication tokens, session identifiers, or sensitive notes in `localStorage`. Local browser storage is convenience, not confidentiality.
- Do not imply account sync because a sign-in button exists. Verify save, reload, a second session, and sign-out behavior.
- Test the complete reader at 320 px, 390 px, and a desktop width. Overflow, covered text, unreachable controls, or unreadable notes fail the gate.
- For account sync, verify that a second account cannot read, change, or infer the first account's progress, highlights, or notes.
- Enforce ownership on the server for every read and write. Hidden buttons, random IDs, or client-supplied account IDs are not authorization. Test cross-account denial through the same deployed request path users take.
- Avoid trackers by default. If analytics are requested, disclose them and keep private reading text out of events.

Target WCAG 2.2 AA for the reader. In addition to the named widths, test 200% text resize, 320 CSS-pixel reflow without two-dimensional scrolling, custom text spacing, keyboard-only operation, visible and unobscured focus, contrast, and touch target size.

The starter in `assets/production-kit/` provides neutral design tokens and local-only progress. It is a base, not a finished identity or an account-sync implementation.

Building a deployable site is not authorization to deploy or publish it. Ask immediately before that external step and confirm the intended visibility.

## Delivering the release

Use stable human-readable filenames. Deliver only final artifacts, not build caches or alternate drafts. Report:

- locked-source SHA-256
- artifact names and sizes
- readers/browsers and device widths tested
- accessibility and privacy result
- any check that remains manual or incomplete
