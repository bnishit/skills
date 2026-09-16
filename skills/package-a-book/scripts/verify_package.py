#!/usr/bin/env python3
"""Run deterministic structural checks for a packaged book release."""

from __future__ import annotations

import hashlib
import json
import sys
import unicodedata
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


def fail(message: str) -> None:
    raise ValueError(message)


def check_source(base: Path, spec: dict) -> None:
    source = base / spec["path"]
    expected = spec["sha256"].lower()
    if len(expected) != 64 or any(c not in "0123456789abcdef" for c in expected):
        fail("locked_source.sha256 must be a 64-character hexadecimal SHA-256")
    actual = hashlib.sha256(source.read_bytes()).hexdigest()
    if actual != expected:
        fail(f"locked source hash mismatch: expected {expected}, got {actual}")


def normalize_text(value: str) -> str:
    return " ".join(unicodedata.normalize("NFKC", value).replace("\u00ad", "").split())


def read_stream(path: Path) -> list[tuple[str, str]]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw, list):
        fail(f"text stream must be a JSON list: {path}")
    stream = []
    seen = set()
    for index, block in enumerate(raw):
        if not isinstance(block, dict) or not isinstance(block.get("id"), str) or not isinstance(block.get("text"), str):
            fail(f"text stream item {index} must contain string id and text: {path}")
        block_id = block["id"]
        if block_id in seen:
            fail(f"duplicate block id {block_id!r} in {path}")
        seen.add(block_id)
        stream.append((block_id, normalize_text(block["text"])))
    return stream


def check_fidelity(base: Path, spec: dict, output_kinds: set[str]) -> None:
    source = read_stream(base / spec["source"])
    if not source:
        fail("source text stream is empty")
    editions = spec.get("editions", {})
    if set(editions) != output_kinds:
        fail("fidelity.editions must name every and only requested output kind")
    allowed_by_edition = {kind: set() for kind in editions}
    for addition in spec.get("allowed_additions", []):
        block_id = addition.get("id")
        kinds = addition.get("editions", [])
        if not isinstance(block_id, str) or not block_id:
            fail("every allowed addition needs a non-empty string id")
        for kind in kinds:
            if kind not in allowed_by_edition:
                fail(f"allowed addition names an unknown edition: {kind}")
            allowed_by_edition[kind].add(block_id)
    for kind, relative in editions.items():
        observed = read_stream(base / relative)
        observed_ids = {block_id for block_id, _ in observed}
        missing_additions = allowed_by_edition[kind] - observed_ids
        if missing_additions:
            fail(f"{kind} inventories absent additions: {sorted(missing_additions)}")
        comparable = [block for block in observed if block[0] not in allowed_by_edition[kind]]
        if comparable != source:
            mismatch = next((i for i, pair in enumerate(zip(comparable, source)) if pair[0] != pair[1]), min(len(comparable), len(source)))
            fail(f"{kind} text stream differs from source at ordered block {mismatch}; check for dropped, duplicated, reordered, or altered prose")


def check_epub(path: Path) -> None:
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        if not names or names[0] != "mimetype":
            fail("EPUB mimetype must be the first ZIP entry")
        info = archive.getinfo("mimetype")
        if info.compress_type != zipfile.ZIP_STORED:
            fail("EPUB mimetype must be stored without compression")
        if archive.read("mimetype") != b"application/epub+zip":
            fail("EPUB mimetype has the wrong value")
        container_name = "META-INF/container.xml"
        if container_name not in names:
            fail("EPUB is missing META-INF/container.xml")
        container = ET.fromstring(archive.read(container_name))
        rootfile = container.find(".//{*}rootfile")
        if rootfile is None or not rootfile.get("full-path"):
            fail("EPUB container does not name a package document")
        opf_name = rootfile.get("full-path")
        if opf_name not in names:
            fail(f"EPUB package document is missing: {opf_name}")
        opf = ET.fromstring(archive.read(opf_name))
        manifest = opf.findall(".//{*}manifest/{*}item")
        if not manifest:
            fail("EPUB package manifest is empty")
        metadata = opf.find(".//{*}metadata")
        if metadata is None:
            fail("EPUB package metadata is missing")
        dc_namespace = "{http://purl.org/dc/elements/1.1/}"
        for field in ("title", "identifier", "language"):
            values = metadata.findall(f"{dc_namespace}{field}")
            if not any((value.text or "").strip() for value in values):
                fail(f"EPUB metadata is missing dc:{field}")
        modified = [item for item in metadata.findall("{*}meta") if item.get("property") == "dcterms:modified"]
        if not any((item.text or "").strip() for item in modified):
            fail("EPUB metadata is missing dcterms:modified")
        opf_dir = Path(opf_name).parent
        manifest_by_id = {}
        for item in manifest:
            item_id = item.get("id")
            href = item.get("href")
            if item_id:
                manifest_by_id[item_id] = item
            if href and str(opf_dir / href) not in names:
                fail(f"EPUB manifest item is missing: {href}")
            if href and item.get("media-type") in {"application/xhtml+xml", "image/svg+xml", "application/xml", "text/xml"}:
                ET.fromstring(archive.read(str(opf_dir / href)))
        if not any("nav" in (item.get("properties") or "").split() for item in manifest):
            fail("EPUB manifest does not identify a navigation document")
        spine = opf.findall(".//{*}spine/{*}itemref")
        if not spine:
            fail("EPUB spine is empty")
        for itemref in spine:
            idref = itemref.get("idref")
            if not idref or idref not in manifest_by_id:
                fail(f"EPUB spine references an unknown manifest item: {idref}")


def check_pdf(path: Path) -> None:
    data = path.read_bytes()
    if not data.startswith(b"%PDF-"):
        fail("PDF header is missing")
    if b"%%EOF" not in data[-2048:]:
        fail("PDF end marker is missing")


def check_site(path: Path) -> None:
    text = path.read_text(encoding="utf-8").lower()
    if "name=\"viewport\"" not in text and "name='viewport'" not in text:
        fail("site is missing a viewport meta tag")
    if "<main" not in text:
        fail("site is missing a main landmark")
    if "<title" not in text:
        fail("site is missing a document title")
    html_index = text.find("<html")
    html_end = text.find(">", html_index)
    html_start = text[html_index:html_end] if html_index >= 0 and html_end >= 0 else ""
    if " lang=" not in html_start:
        fail("site root is missing a language attribute")


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: verify_package.py RELEASE_MANIFEST.json", file=sys.stderr)
        return 2
    manifest_path = Path(sys.argv[1]).resolve()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    base = manifest_path.parent
    checks = [("locked source", lambda: check_source(base, manifest["locked_source"]))]
    outputs = manifest.get("outputs", {})
    checkers = {"epub": check_epub, "pdf": check_pdf, "site": check_site}
    for kind, relative in outputs.items():
        if relative is None:
            continue
        if kind not in checkers:
            fail(f"unknown output kind: {kind}")
        path = base / relative
        checks.append((kind, lambda path=path, kind=kind: checkers[kind](path)))
    checks.append(("cross-format fidelity", lambda: check_fidelity(base, manifest["fidelity"], {kind for kind, path in outputs.items() if path is not None})))

    failed = False
    for label, check in checks:
        try:
            check()
            print(f"PASS  {label}")
        except (OSError, KeyError, ValueError, zipfile.BadZipFile, ET.ParseError) as error:
            failed = True
            print(f"FAIL  {label}: {error}")
    print("NOTE  declared streams must be extracted from actual artifacts; these checks do not prove extraction provenance or rendered quality")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
