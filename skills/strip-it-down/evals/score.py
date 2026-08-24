#!/usr/bin/env python3
"""Mechanical scorer for a strip-it-down chapter.

Usage:  score.py <file.html|file.txt> [...]

Measures the things the skill's contract makes countable, so a chapter can be
graded without a judge. Derived from the Symposium run (Aug 2026), where the
prose drifted 165 -> 311 words and nobody noticed because nothing counted.
"""
import re
import sys

STAGE = re.compile(
    r"\b(notice|watch|hold on to|hold that|feel |you may already|"
    r"most people[, ]|this is precisely|what just happened)",
    re.I,
)
TRAILER = re.compile(r"\bchapter \d+ (is|pushes|will|shows)|\bnext chapter\b", re.I)

LIMITS = {"prose_words": 140, "over_25w": 0, "em_dashes": 1, "claim_sentences": 1}


def strip_html(raw):
    """Return (prose, claim). Prose excludes SVG, footer, kicker, style, title."""
    raw = re.sub(r"<(script|style|svg|footer|head)[^>]*>.*?</\1>", " ", raw, flags=re.S | re.I)
    claim = ""
    m = re.search(r'<div class="claim">(.*?)</div>', raw, re.S | re.I)
    if m:
        claim = re.sub(r"<br\s*/?>", " ", m.group(1))
        raw = raw.replace(m.group(0), " ")
    raw = re.sub(r'<div class="kicker".*?</div>', " ", raw, flags=re.S | re.I)
    raw = re.sub(r"<h1[^>]*>.*?</h1>", " ", raw, flags=re.S | re.I)
    text = re.sub(r"<[^>]+>", " ", raw)
    return clean(text), clean(re.sub(r"<[^>]+>", " ", claim))


def clean(t):
    t = t.replace("&amp;", "&").replace("&nbsp;", " ").replace("&quot;", '"')
    return re.sub(r"\s+", " ", t).strip()


def sentences(t):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", t) if s.strip()]


def score(path):
    raw = open(path, encoding="utf-8").read()
    prose, claim = strip_html(raw) if "<" in raw[:200] else (clean(raw), "")
    sents = sentences(prose)
    words = prose.split()
    lens = [len(s.split()) for s in sents] or [0]
    r = {
        "prose_words": len(words),
        "avg_sentence": round(sum(lens) / len(lens), 1),
        "longest": max(lens),
        "over_25w": sum(1 for n in lens if n > 25),
        "em_dashes": prose.count("—") + claim.count("—"),
        "claim_sentences": len(sentences(claim)) if claim else None,
        "claim_words": len(claim.split()) if claim else None,
        "stage_directions": len(STAGE.findall(prose)),
        "next_ch_trailers": len(TRAILER.findall(prose)),
    }
    r["FAIL"] = [k for k, lim in LIMITS.items()
                 if r.get(k) is not None and r[k] > lim] \
        + (["stage_directions"] if r["stage_directions"] else []) \
        + (["next_ch_trailers"] if r["next_ch_trailers"] else [])
    return r


if __name__ == "__main__":
    cols = ["prose_words", "avg_sentence", "longest", "over_25w", "em_dashes",
            "claim_sentences", "stage_directions", "next_ch_trailers"]
    print(f"{'file':<34}" + "".join(f"{c[:9]:>11}" for c in cols) + "   verdict")
    for p in sys.argv[1:]:
        r = score(p)
        line = f"{p.split('/')[-1][:33]:<34}" + "".join(f"{str(r[c]):>11}" for c in cols)
        print(line + ("   PASS" if not r["FAIL"] else "   FAIL: " + ",".join(r["FAIL"])))
