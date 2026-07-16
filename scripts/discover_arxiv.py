#!/usr/bin/env python3
"""Discover likely self-evolving-agent papers from arXiv.

This script creates a review queue. It deliberately does not classify papers as
self-evolving or modify the reviewed catalog.
"""

from __future__ import annotations

import argparse
import json
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date
from pathlib import Path

ATOM = "http://www.w3.org/2005/Atom"
NS = {"atom": ATOM}


def text(node: ET.Element | None, path: str) -> str:
    if node is None:
        return ""
    child = node.find(path, NS)
    return (child.text or "").strip() if child is not None else ""


def query_arxiv(query: str, limit: int) -> list[dict]:
    params = {
        "search_query": query,
        "start": "0",
        "max_results": str(limit),
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(params)
    request = urllib.request.Request(url, headers={"User-Agent": "awesome-self-evolving-agents/0.1"})
    with urllib.request.urlopen(request, timeout=30) as response:
        root = ET.fromstring(response.read())

    results = []
    for entry in root.findall("atom:entry", NS):
        identifier = text(entry, "atom:id").rsplit("/", 1)[-1]
        results.append(
            {
                "id": identifier,
                "title": " ".join(text(entry, "atom:title").split()),
                "summary": " ".join(text(entry, "atom:summary").split()),
                "published": text(entry, "atom:published"),
                "updated": text(entry, "atom:updated"),
                "authors": [
                    (author.find("atom:name", NS).text or "").strip()
                    for author in entry.findall("atom:author", NS)
                    if author.find("atom:name", NS) is not None
                ],
                "source": f"https://arxiv.org/abs/{identifier}",
                "review_status": "unreviewed",
                "discovered_on": date.today().isoformat(),
            }
        )
    return results


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--searches", type=Path, default=Path("data/searches.json"))
    parser.add_argument("--output", type=Path, default=Path("data/discovered.json"))
    parser.add_argument("--catalog", type=Path, default=Path("data/papers.json"))
    parser.add_argument("--limit-per-query", type=int, default=25)
    args = parser.parse_args()

    searches = json.loads(args.searches.read_text())
    reviewed_ids = {item["id"] for item in json.loads(args.catalog.read_text())}
    existing = {item["id"]: item for item in json.loads(args.output.read_text())} if args.output.exists() else {}
    discovered: dict[str, dict] = {}
    for query in searches:
        for item in query_arxiv(query, args.limit_per_query):
            if item["id"] not in reviewed_ids:
                discovered[item["id"]] = item
        time.sleep(3)

    existing.update(discovered)
    records = [item for item in existing.values() if item["id"] not in reviewed_ids]
    records.sort(key=lambda item: item["published"], reverse=True)
    args.output.write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n")
    print(f"wrote {len(records)} candidates to {args.output}")


if __name__ == "__main__":
    main()
