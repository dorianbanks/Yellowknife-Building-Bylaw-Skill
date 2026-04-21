#!/usr/bin/env python3
"""
lookup.py — citation and keyword resolver for the City of Yellowknife
Building By-law No. 5058.

Usage:
    python3 lookup.py 29                       # section 29
    python3 lookup.py "§29(1)(b)"              # sub-clause of §29
    python3 lookup.py "section 64"             # natural language
    python3 lookup.py "Schedule B"             # named schedule
    python3 lookup.py --search sprinkler       # keyword search
    python3 lookup.py --list                   # dump all sections
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
SKILL = HERE.parent
CITATIONS = SKILL / "references" / "citations.json"
INDEX_MD = SKILL / "references" / "index.md"
PDF = SKILL / "assets" / "yk_bylaw_5058_2022.pdf"


def load_data() -> dict:
    with CITATIONS.open("r", encoding="utf-8") as f:
        return json.load(f)


# ---------------------------------------------------------------------------
# Citation normalization
# ---------------------------------------------------------------------------

_SECTION_RE = re.compile(
    r"""
    ^\s*
    (?:section\s+|sec\.?\s*|§\s*|s\.?\s*)?   # optional "section", "§", "s."
    (\d+)                                     # section number
    (.*)$                                     # trailing sub-nav (ignored)
    """,
    re.IGNORECASE | re.VERBOSE,
)

_SCHEDULE_RE = re.compile(
    r"^\s*(?:schedule\s+)?([A-Ea-e])\b.*$",
    re.IGNORECASE,
)


def resolve_section(query: str, data: dict) -> dict | None:
    """Return the section record for a §N-style query."""
    m = _SECTION_RE.match(query)
    if not m:
        return None
    num = m.group(1)
    trailing = (m.group(2) or "").strip()
    rec = data["sections"].get(num)
    if rec is None:
        return None
    out = dict(rec)
    out["section"] = num
    out["query_trailing"] = trailing
    return out


def resolve_schedule(query: str, data: dict) -> dict | None:
    """Return a Schedule A–E record."""
    if "schedule" not in query.lower():
        return None
    m = _SCHEDULE_RE.match(query.strip())
    if not m:
        return None
    letter = m.group(1).upper()
    rec = data["schedules"].get(letter)
    if rec is None:
        return None
    out = dict(rec)
    out["schedule"] = letter
    return out


# ---------------------------------------------------------------------------
# Search
# ---------------------------------------------------------------------------


def keyword_search(term: str, data: dict) -> list[dict]:
    """Case-insensitive substring search across sections and schedules."""
    term_l = term.lower()
    hits: list[dict] = []
    for num, rec in data["sections"].items():
        if term_l in rec["title"].lower() or term_l in str(rec.get("note", "")).lower():
            hits.append(
                {
                    "kind": "section",
                    "id": f"§{num}",
                    "page": rec["page"],
                    "title": rec["title"],
                }
            )
    for letter, rec in data["schedules"].items():
        if term_l in rec["title"].lower():
            hits.append(
                {
                    "kind": "schedule",
                    "id": f"Schedule {letter}",
                    "page": rec["page"],
                    "title": rec["title"],
                }
            )
    if term_l in "index.md".lower():
        return hits
    # also grep index.md for richer matches (heading lines)
    if INDEX_MD.exists():
        for i, line in enumerate(INDEX_MD.read_text(encoding="utf-8").splitlines(), 1):
            if term_l in line.lower() and line.strip().startswith("|"):
                hits.append({"kind": "index", "line": i, "snippet": line.strip()})
    return hits


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------


def format_section(rec: dict) -> str:
    trailing = rec.get("query_trailing", "")
    tail = f" {trailing}" if trailing else ""
    return (
        f"§{rec['section']}{tail}  (Part {rec.get('part', '?')})\n"
        f"  Title: {rec['title']}\n"
        f"  PDF page: {rec['page']}\n"
        f"  Bylaw: City of Yellowknife Building By-law No. 5058 (adopted 2022-05-30)\n"
        + (f"  Note: {rec['note']}\n" if rec.get("note") else "")
        + f"  PDF: {PDF}\n"
        f"  Suggested Read: Read(file_path=\"{PDF}\", pages=\"{rec['page']}-{rec['page']+2}\")"
    )


def format_schedule(rec: dict) -> str:
    return (
        f"Schedule {rec['schedule']}\n"
        f"  Title: {rec['title']}\n"
        f"  PDF page (start): {rec['page']}\n"
        f"  PDF: {PDF}\n"
        f"  Suggested Read: Read(file_path=\"{PDF}\", pages=\"{rec['page']}-{rec['page']+3}\")"
    )


def format_hits(hits: list[dict]) -> str:
    if not hits:
        return "No matches."
    lines = []
    for h in hits:
        if h.get("kind") == "section":
            lines.append(f"  [{h['id']:>5}] p.{h['page']:>2}  {h['title']}")
        elif h.get("kind") == "schedule":
            lines.append(f"  [{h['id']}] p.{h['page']:>2}  {h['title']}")
        elif h.get("kind") == "index":
            lines.append(f"  index.md:{h['line']}  {h['snippet']}")
    return "\n".join(lines)


def list_all(data: dict) -> str:
    lines = ["PART 1 — Administrative Requirements"]
    for num, rec in data["sections"].items():
        if rec.get("part") == 1:
            lines.append(f"  §{num:>2}  p.{rec['page']:>2}  {rec['title']}")
    lines.append("")
    lines.append("PART 2 — Local Construction Requirements")
    for num, rec in data["sections"].items():
        if rec.get("part") == 2:
            lines.append(f"  §{num:>2}  p.{rec['page']:>2}  {rec['title']}")
    lines.append("")
    lines.append("SCHEDULES")
    for letter, rec in data["schedules"].items():
        lines.append(f"  Schedule {letter}  p.{rec['page']:>2}  {rec['title']}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Citation and keyword lookup for City of Yellowknife Building By-law No. 5058.",
    )
    p.add_argument("citation", nargs="?", help="Section number or 'Schedule X' reference")
    p.add_argument("--search", "-s", help="Keyword search across titles + index.md")
    p.add_argument("--list", "-l", action="store_true", help="List all sections and schedules")
    args = p.parse_args(argv)

    data = load_data()

    if args.list:
        print(list_all(data))
        return 0

    if args.search:
        print(format_hits(keyword_search(args.search, data)))
        return 0

    if not args.citation:
        p.print_help()
        return 2

    q = args.citation
    sch = resolve_schedule(q, data)
    if sch:
        print(format_schedule(sch))
        return 0

    sec = resolve_section(q, data)
    if sec:
        print(format_section(sec))
        return 0

    print(
        f"Unrecognised citation: {q!r}\n"
        "Try: '29', '§29(1)(b)', 'section 64', 'Schedule B', or --search <keyword>.",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
