#!/usr/bin/env python3
"""
One-time BookStack shelf pull.

Exports one BookStack shelf into a local folder:

output/
  Shelf Name/
    Book Name/
      _book.yml
      Chapter Name/
        _chapter.yml
        Page Name.md
      Direct Page Name.md

Usage:

  export BOOKSTACK_URL="https://bookstack.example.com"
  export BOOKSTACK_TOKEN_ID="xxx"
  export BOOKSTACK_TOKEN_SECRET="yyy"

  python pull_bookstack_shelf.py --shelf-id 12 --out ./bookstack-export
  python pull_bookstack_shelf.py --shelf-name "SOP" --out ./bookstack-export

Dependencies:

  pip install requests pyyaml
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

import requests
import yaml


def env_required(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        print(f"ERROR: Missing environment variable: {name}", file=sys.stderr)
        sys.exit(1)
    return value


def safe_name(name: str, max_len: int = 100) -> str:
    name = name.strip()
    name = re.sub(r"[\\/:\*\?\"<>\|]+", "-", name)
    name = re.sub(r"\s+", " ", name)
    name = name.strip(" .")
    if not name:
        name = "untitled"
    return name[:max_len].rstrip(" .")


def write_yaml(path: Path, data: Dict[str, Any]) -> None:
    path.write_text(
        yaml.safe_dump(data, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )


def frontmatter(meta: Dict[str, Any], body: str) -> str:
    return (
        "---\n"
        + yaml.safe_dump(meta, sort_keys=False, allow_unicode=True).strip()
        + "\n---\n\n"
        + body.lstrip()
    )


class BookStackClient:
    def __init__(self, base_url: str, token_id: str, token_secret: str, delay: float = 0.0):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"Token {token_id}:{token_secret}",
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
        )
        self.delay = delay

    def request(self, method: str, path: str, **kwargs) -> Any:
        url = f"{self.base_url}/api/{path.lstrip('/')}"
        if self.delay:
            time.sleep(self.delay)

        response = self.session.request(method, url, timeout=60, **kwargs)

        if response.status_code >= 400:
            print(f"\nERROR: {method} {url}", file=sys.stderr)
            print(f"Status: {response.status_code}", file=sys.stderr)
            print(response.text[:2000], file=sys.stderr)
            response.raise_for_status()

        if not response.text.strip():
            return None

        return response.json()

    def get(self, path: str, **params) -> Any:
        params = {k: v for k, v in params.items() if v is not None}
        return self.request("GET", path, params=params)

    def list_all(self, path: str, **params) -> List[Dict[str, Any]]:
        results: List[Dict[str, Any]] = []
        offset = 0
        count = 100

        while True:
            payload = self.get(path, **params, offset=offset, count=count)
            data = payload.get("data", []) if isinstance(payload, dict) else []

            results.extend(data)

            total = payload.get("total")
            if total is not None and len(results) >= int(total):
                break
            if len(data) < count:
                break

            offset += count

        return results

    def find_shelf_by_name(self, name: str) -> Optional[Dict[str, Any]]:
        shelves = self.list_all("shelves")
        for shelf in shelves:
            if shelf.get("name") == name:
                return shelf
        return None


def extract_page_markdown(page: Dict[str, Any]) -> str:
    markdown = page.get("markdown")
    if markdown:
        return markdown

    raw_html = page.get("raw_html")
    html = page.get("html")

    fallback = raw_html or html or ""
    if fallback:
        return (
            "<!--\n"
            "This page did not return native Markdown from BookStack.\n"
            "The content below is exported HTML fallback.\n"
            "-->\n\n"
            + fallback
        )

    return ""


def page_meta(page: Dict[str, Any], location: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "bookstack_type": "page",
        "bookstack_id": page.get("id"),
        "name": page.get("name"),
        "slug": page.get("slug"),
        "book_id": location.get("book_id"),
        "chapter_id": location.get("chapter_id"),
        "created_at": page.get("created_at"),
        "updated_at": page.get("updated_at"),
        "source_url": page.get("url"),
    }


def export_page(
    client: BookStackClient,
    page_id: int,
    target_dir: Path,
    book_id: int,
    chapter_id: Optional[int] = None,
) -> None:
    page = client.get(f"pages/{page_id}")

    page_name = safe_name(page.get("name", f"page-{page_id}"))
    path = target_dir / f"{page_name}.md"

    body = extract_page_markdown(page)

    meta = page_meta(
        page,
        {
            "book_id": book_id,
            "chapter_id": chapter_id,
        },
    )

    path.write_text(frontmatter(meta, body), encoding="utf-8")
    print(f"PAGE    {path}")


def export_chapter(client: BookStackClient, chapter_id: int, book_dir: Path, book_id: int) -> None:
    chapter = client.get(f"chapters/{chapter_id}")

    chapter_name = safe_name(chapter.get("name", f"chapter-{chapter_id}"))
    chapter_dir = book_dir / chapter_name
    chapter_dir.mkdir(parents=True, exist_ok=True)

    write_yaml(
        chapter_dir / "_chapter.yml",
        {
            "bookstack_type": "chapter",
            "bookstack_id": chapter.get("id"),
            "name": chapter.get("name"),
            "slug": chapter.get("slug"),
            "book_id": chapter.get("book_id"),
            "description": chapter.get("description"),
            "created_at": chapter.get("created_at"),
            "updated_at": chapter.get("updated_at"),
            "source_url": chapter.get("url"),
        },
    )

    print(f"CHAPTER {chapter_dir}")

    pages = chapter.get("pages", [])
    for page in sorted(pages, key=lambda p: (p.get("priority", 0), p.get("name", ""))):
        export_page(client, int(page["id"]), chapter_dir, book_id=book_id, chapter_id=chapter_id)


def export_book(client: BookStackClient, book_id: int, shelf_dir: Path) -> None:
    book = client.get(f"books/{book_id}")

    book_name = safe_name(book.get("name", f"book-{book_id}"))
    book_dir = shelf_dir / book_name
    book_dir.mkdir(parents=True, exist_ok=True)

    write_yaml(
        book_dir / "_book.yml",
        {
            "bookstack_type": "book",
            "bookstack_id": book.get("id"),
            "name": book.get("name"),
            "slug": book.get("slug"),
            "description": book.get("description"),
            "created_at": book.get("created_at"),
            "updated_at": book.get("updated_at"),
            "source_url": book.get("url"),
        },
    )

    print(f"BOOK    {book_dir}")

    contents = book.get("contents", [])
    contents = sorted(contents, key=lambda c: (c.get("priority", 0), c.get("name", "")))

    for entry in contents:
        entry_type = entry.get("type")
        entry_id = int(entry["id"])

        if entry_type == "chapter":
            export_chapter(client, entry_id, book_dir, book_id=book_id)
        elif entry_type == "page":
            export_page(client, entry_id, book_dir, book_id=book_id, chapter_id=None)
        else:
            print(f"SKIP unknown book content type: {entry_type} id={entry_id}", file=sys.stderr)


def export_shelf(client: BookStackClient, shelf: Dict[str, Any], out_dir: Path) -> None:
    shelf_id = int(shelf["id"])
    shelf_detail = client.get(f"shelves/{shelf_id}")

    shelf_name = safe_name(shelf_detail.get("name", f"shelf-{shelf_id}"))
    shelf_dir = out_dir / shelf_name
    shelf_dir.mkdir(parents=True, exist_ok=True)

    write_yaml(
        shelf_dir / "_shelf.yml",
        {
            "bookstack_type": "shelf",
            "bookstack_id": shelf_detail.get("id"),
            "name": shelf_detail.get("name"),
            "slug": shelf_detail.get("slug"),
            "description": shelf_detail.get("description"),
            "created_at": shelf_detail.get("created_at"),
            "updated_at": shelf_detail.get("updated_at"),
            "source_url": shelf_detail.get("url"),
        },
    )

    print(f"SHELF   {shelf_dir}")

    books = shelf_detail.get("books", [])
    books = sorted(books, key=lambda b: b.get("name", ""))

    for book in books:
        export_book(client, int(book["id"]), shelf_dir)


def main() -> None:
    parser = argparse.ArgumentParser(description="One-time pull/export of a BookStack shelf.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--shelf-id", type=int, help="BookStack shelf ID to export.")
    group.add_argument("--shelf-name", help="Exact BookStack shelf name to export.")
    parser.add_argument("--out", default="./bookstack-export", help="Output directory.")
    parser.add_argument("--delay", type=float, default=0.0, help="Delay between API calls in seconds.")
    args = parser.parse_args()

    base_url = env_required("BOOKSTACK_URL")
    token_id = env_required("BOOKSTACK_TOKEN_ID")
    token_secret = env_required("BOOKSTACK_TOKEN_SECRET")

    client = BookStackClient(base_url, token_id, token_secret, delay=args.delay)

    if args.shelf_id:
        shelf = client.get(f"shelves/{args.shelf_id}")
    else:
        shelf = client.find_shelf_by_name(args.shelf_name)
        if not shelf:
            print(f"ERROR: Shelf not found by exact name: {args.shelf_name}", file=sys.stderr)
            sys.exit(1)

    out_dir = Path(args.out).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    export_shelf(client, shelf, out_dir)

    print("\nDONE")
    print(f"Exported to: {out_dir}")


if __name__ == "__main__":
    main()
