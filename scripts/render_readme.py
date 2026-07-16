#!/usr/bin/env python3
"""Render reviewed paper records into the README."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
PAPERS = ROOT / "data/papers.json"
START = "<!-- PAPERS:START -->"
END = "<!-- PAPERS:END -->"


def inline(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ").strip()


def link(label: str, url: str | None) -> str:
    return f"[{inline(label)}]({url})" if url else "-"


def render(records: list[dict]) -> str:
    lines = [
        "## Reviewed Papers",
        "",
        "Each row exposes the claims that matter for comparing evolution systems. `arXiv` means the venue was not independently confirmed as a peer-reviewed publication.",
        "",
        "| Paper | Venue | Mutable object | Scope | Evolution loop | Evidence | Validation | Code |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for paper in records:
        title = link(paper["title"], paper["source"])
        objects = ", ".join(inline(item) for item in paper["mutable_object"])
        code = link("repo", paper.get("code"))
        lines.append(
            "| "
            + " | ".join(
                [
                    title,
                    f"{inline(paper['venue_status'])} {inline(paper['year'])}",
                    objects,
                    inline(paper["evolution_scope"]),
                    inline(paper["loop"]),
                    inline(paper["evidence"]),
                    inline(paper["validation"]),
                    code,
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            f"Catalog size: **{len(records)} reviewed papers**. Full records and stable fields live in [`data/papers.json`](data/papers.json).",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    readme = README.read_text()
    before, marker, rest = readme.partition(START)
    if not marker:
        raise SystemExit(f"missing {START} marker")
    current, marker, after = rest.partition(END)
    if not marker:
        raise SystemExit(f"missing {END} marker")

    records = json.loads(PAPERS.read_text())
    rendered = render(records)
    README.write_text(before + START + "\n" + rendered + "\n" + END + after)
    print(f"rendered {len(records)} reviewed papers into README.md")


if __name__ == "__main__":
    main()
