# Verification

Verification has three layers. Passing one does not imply the others passed.

## 1. Source integrity

- Record the locked Markdown SHA-256 before building.
- Generate every edition from the same semantic intermediate.
- Export ordered reader-visible text streams automatically from the semantic source, built EPUB spine, built PDF, and built site DOM. Never hand-author an edition stream or satisfy the check by copying the source stream. Each entry must keep its stable block ID and text.
- Record the extractor command and version plus the corresponding artifact hash in the verification report. The supplied verifier compares declared streams; it cannot prove that a stream was honestly extracted from the artifact.
- Normalize only Unicode form, whitespace, soft hyphens, running heads, and page numbers. Byte equality is neither required nor useful.
- Explicitly inventory format-only additions such as a print colophon. After filtering those named IDs, fail any dropped, duplicated, reordered, or altered block.
- Re-hash the locked source after the build.

## 2. Structural checks

Create `release-manifest.json` from `assets/production-kit/release-manifest.example.json`, then run:

```bash
python3 scripts/verify_package.py release-manifest.json
```

The script checks the locked-source hash, ordered normalized text streams, requested files, EPUB container rules, basic PDF signature/trailer, and basic site mobile metadata. The build must extract the four text-stream JSON files named in the manifest from the actual artifacts. The script trusts those declared streams, so its pass is not independent proof of extraction or visual quality.

Use a standards validator for EPUB when available. Run a link checker on the site. Treat missing tools as unverified, not passed.

## 3. Rendered inspection

Inspect representative and risky pages:

- front cover at full size and phone-thumbnail size
- contents and first chapter navigation
- every part/chapter opener
- the densest page, longest heading, longest link, and largest image
- pages before and after every forced break
- final page and metadata

For EPUB, test a narrow phone viewport, enlarged type, and at least one real reading app. For PDF, rasterize all pages and inspect a contact sheet before opening flagged pages at full size. For the site, test 320 px, 390 px, and desktop; keyboard use; reading-time-left; progress restore; selection/highlight appearance and immediate dismissal; storage disclosure; privacy; and the promised account isolation.

For EPUB accessibility, inspect language, semantics, alt text, spine order, navigation, and accessibility metadata; run EPUBCheck and name its version. For PDF, inspect tags, logical reading order, document language, bookmarks, link order, and figure alternatives. For the site, include 200% text resize, custom text spacing, unobscured focus, and 320 CSS-pixel reflow in the rendered checks.

## Release report vocabulary

- **passed** — directly checked with named evidence
- **failed** — checked and wrong
- **unverified** — not checked or the required tool/environment was unavailable
- **not requested** — outside this release

Never turn `unverified` into `passed` because the artifact opens.

Standards and security basis: [EPUB 3.3](https://www.w3.org/TR/epub-33/), [EPUB Accessibility 1.1](https://www.w3.org/TR/epub-a11y-11/), [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [Tagged PDF guidance](https://pdfa.org/resource/tagged-pdf-q-a/), and OWASP guidance for [HTML5 storage](https://cheatsheetseries.owasp.org/cheatsheets/HTML5_Security_Cheat_Sheet.html) and [authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html).
