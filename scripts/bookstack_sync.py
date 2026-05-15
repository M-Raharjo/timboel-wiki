#!/usr/bin/env python3
"""
Sync a Git folder hierarchy into BookStack.

Hierarchy:
  root/
    shelf-folder/
      _shelf.yml
      book-folder/
        _book.yml
        chapter-folder/
          _chapter.yml
          page.md
        direct-page-in-book.md

Rules:
  - Creates/updates shelves, books, chapters, and pages.
  - Attaches synced books to their shelf.
  - Does not delete or archive remote content.
  - Uses names as identity. Keep names stable.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path
from typing import Any

import requests
import yaml


META_FILES = {"_shelf.yml", "_book.yml", "_chapter.yml"}


def clean_name_from_path(path: Path) -> str:
    """Turn '01-sop' into 'SOP', 'sales-order' into 'Sales Order'."""
    name = path.stem if path.is_file() else path.name
    name = re.sub(r"^\d+[-_. ]*", "", name)
    name = name.replace("-", " ").replace("_", " ").strip()
    return name.title() if name else path.name


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    return data or {}


def split_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    raw_meta = text[4:end]
    body = text[end + 5 :]
    meta = yaml.safe_load(raw_meta) or {}
    return meta, body


def read_markdown_page(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    meta, body = split_frontmatter(text)
    return meta, body.rstrip() + "\n"


class BookStackClient:
    def __init__(self, base_url: str, token_id: str, token_secret: str) -> None:
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"Token {token_id}:{token_secret}",
                "Content-Type": "application/json",
                "Accept": "application/json",
            }
        )

    def request(self, method: str, path: str, **kwargs: Any) -> Any:
        url = f"{self.base_url}/api/{path.lstrip('/')}"
        response = self.session.request(method, url, timeout=60, **kwargs)
        if response.status_code >= 400:
            raise RuntimeError(
                f"{method} {url} failed: HTTP {response.status_code}\n{response.text}"
            )
        if response.status_code == 204 or not response.text.strip():
            return None
        return response.json()

    def list_all(self, endpoint: str) -> list[dict[str, Any]]:
        records: list[dict[str, Any]] = []
        offset = 0
        count = 500
        while True:
            result = self.request("GET", endpoint, params={"count": count, "offset": offset})
            batch = result.get("data", [])
            records.extend(batch)
            total = result.get("total", len(records))
            if len(records) >= total or not batch:
                break
            offset += count
        return records

    def find_by_name(self, endpoint: str, name: str, parent_key: str | None = None, parent_id: int | None = None) -> dict[str, Any] | None:
        for record in self.list_all(endpoint):
            if record.get("name") != name:
                continue
            if parent_key is not None and parent_id is not None and record.get(parent_key) != parent_id:
                continue
            return record
        return None

    def read(self, endpoint: str, item_id: int) -> dict[str, Any]:
        return self.request("GET", f"{endpoint}/{item_id}")

    def create(self, endpoint: str, payload: dict[str, Any]) -> dict[str, Any]:
        return self.request("POST", endpoint, json=payload)

    def update(self, endpoint: str, item_id: int, payload: dict[str, Any]) -> dict[str, Any]:
        return self.request("PUT", f"{endpoint}/{item_id}", json=payload)


class Syncer:
    def __init__(self, client: BookStackClient, root: Path, dry_run: bool = False) -> None:
        self.client = client
        self.root = root
        self.dry_run = dry_run

    def log(self, message: str) -> None:
        print(message, flush=True)

    def ensure_shelf(self, shelf_dir: Path) -> dict[str, Any]:
        meta = load_yaml(shelf_dir / "_shelf.yml")
        name = meta.get("name") or clean_name_from_path(shelf_dir)
        description = meta.get("description", "")

        existing = self.client.find_by_name("shelves", name)
        payload = {"name": name, "description": description}

        if existing:
            self.log(f"SHELF update: {name}")
            if not self.dry_run:
                return self.client.update("shelves", existing["id"], payload)
            return existing

        self.log(f"SHELF create: {name}")
        if not self.dry_run:
            return self.client.create("shelves", payload)
        return {"id": -1, "name": name, "books": []}

    def ensure_book(self, book_dir: Path) -> dict[str, Any]:
        meta = load_yaml(book_dir / "_book.yml")
        name = meta.get("name") or clean_name_from_path(book_dir)
        description = meta.get("description", "")

        existing = self.client.find_by_name("books", name)
        payload = {"name": name, "description": description}

        if existing:
            self.log(f"BOOK update: {name}")
            if not self.dry_run:
                return self.client.update("books", existing["id"], payload)
            return existing

        self.log(f"BOOK create: {name}")
        if not self.dry_run:
            return self.client.create("books", payload)
        return {"id": -1, "name": name}

    def ensure_chapter(self, chapter_dir: Path, book: dict[str, Any], priority: int) -> dict[str, Any]:
        meta = load_yaml(chapter_dir / "_chapter.yml")
        name = meta.get("name") or clean_name_from_path(chapter_dir)
        description = meta.get("description", "")

        existing = self.client.find_by_name("chapters", name, "book_id", book["id"])
        payload = {
            "book_id": book["id"],
            "name": name,
            "description": description,
            "priority": meta.get("priority", priority),
        }

        if existing:
            self.log(f"CHAPTER update: {book['name']} / {name}")
            if not self.dry_run:
                return self.client.update("chapters", existing["id"], payload)
            return existing

        self.log(f"CHAPTER create: {book['name']} / {name}")
        if not self.dry_run:
            return self.client.create("chapters", payload)
        return {"id": -1, "name": name, "book_id": book["id"]}

    def ensure_page(self, page_path: Path, book: dict[str, Any], chapter: dict[str, Any] | None, priority: int) -> dict[str, Any]:
        meta, markdown = read_markdown_page(page_path)
        name = meta.get("name") or first_h1(markdown) or clean_name_from_path(page_path)

        parent_label = f"{book['name']} / {chapter['name']}" if chapter else book["name"]
        parent_key = "chapter_id" if chapter else "book_id"
        parent_id = chapter["id"] if chapter else book["id"]

        existing = self.client.find_by_name("pages", name, parent_key, parent_id)
        payload = {
            parent_key: parent_id,
            "name": name,
            "markdown": markdown,
            "priority": meta.get("priority", priority),
        }

        tags = meta.get("tags")
        if tags:
            payload["tags"] = normalize_tags(tags)

        if existing:
            self.log(f"PAGE update: {parent_label} / {name}")
            if not self.dry_run:
                return self.client.update("pages", existing["id"], payload)
            return existing

        self.log(f"PAGE create: {parent_label} / {name}")
        if not self.dry_run:
            return self.client.create("pages", payload)
        return {"id": -1, "name": name, parent_key: parent_id}

    def attach_books_to_shelf(self, shelf: dict[str, Any], synced_book_ids: list[int]) -> None:
        if self.dry_run:
            self.log(f"SHELF attach books: {shelf['name']} -> {synced_book_ids}")
            return

        full_shelf = self.client.read("shelves", shelf["id"])
        existing_ids = [book["id"] for book in full_shelf.get("books", [])]
        merged = existing_ids[:]
        for book_id in synced_book_ids:
            if book_id not in merged:
                merged.append(book_id)

        payload = {
            "name": full_shelf["name"],
            "description": full_shelf.get("description", ""),
            "books": merged,
        }
        self.log(f"SHELF books: {full_shelf['name']} -> {merged}")
        self.client.update("shelves", shelf["id"], payload)

    def sync(self) -> None:
        if not self.root.exists():
            raise RuntimeError(f"Root path does not exist: {self.root}")

        for shelf_dir in sorted_dirs(self.root):
            shelf = self.ensure_shelf(shelf_dir)
            synced_book_ids: list[int] = []

            for book_dir in sorted_dirs(shelf_dir):
                book = self.ensure_book(book_dir)
                synced_book_ids.append(book["id"])

                chapter_priority = 0
                page_priority = 0

                for md in sorted(book_dir.glob("*.md")):
                    if md.name.startswith("_"):
                        continue
                    self.ensure_page(md, book, None, page_priority)
                    page_priority += 1

                for chapter_dir in sorted_dirs(book_dir):
                    chapter = self.ensure_chapter(chapter_dir, book, chapter_priority)
                    chapter_priority += 1

                    for md in sorted(chapter_dir.glob("*.md")):
                        if md.name.startswith("_"):
                            continue
                        self.ensure_page(md, book, chapter, page_priority)
                        page_priority += 1

            self.attach_books_to_shelf(shelf, synced_book_ids)


def normalize_tags(tags: Any) -> list[dict[str, str]]:
    if isinstance(tags, list):
        out = []
        for item in tags:
            if isinstance(item, dict):
                out.append({"name": str(item.get("name", "")), "value": str(item.get("value", ""))})
            else:
                out.append({"name": str(item), "value": ""})
        return out
    if isinstance(tags, dict):
        return [{"name": str(k), "value": str(v)} for k, v in tags.items()]
    return []


def first_h1(markdown: str) -> str | None:
    for line in markdown.splitlines():
        match = re.match(r"^#\s+(.+?)\s*$", line)
        if match:
            return match.group(1).strip()
    return None


def sorted_dirs(path: Path) -> list[Path]:
    return sorted(
        [p for p in path.iterdir() if p.is_dir() and not p.name.startswith(".") and not p.name.startswith("_")],
        key=lambda p: p.name,
    )


def env_required(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync Git markdown hierarchy to BookStack shelves.")
    parser.add_argument("root", help="Root folder containing shelf folders, usually: bookstack")
    parser.add_argument("--dry-run", action="store_true", help="Print actions without writing to BookStack")
    args = parser.parse_args()

    client = BookStackClient(
        base_url=env_required("BOOKSTACK_URL"),
        token_id=env_required("BOOKSTACK_TOKEN_ID"),
        token_secret=env_required("BOOKSTACK_TOKEN_SECRET"),
    )

    Syncer(client, Path(args.root), dry_run=args.dry_run).sync()
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
