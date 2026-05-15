# BookStack Shelf Sync

Sync a Git folder hierarchy into BookStack.

## Hierarchy

```text
bookstack/
  01-sop/                  # Shelf
    _shelf.yml
    sales/                 # Book
      _book.yml
      quotation/           # Chapter
        _chapter.yml
        create-quotation.md # Page
```

## GitHub secrets

Create these repository secrets:

```text
BOOKSTACK_URL
BOOKSTACK_TOKEN_ID
BOOKSTACK_TOKEN_SECRET
```

Example:

```text
BOOKSTACK_URL=https://bookstack.example.com
```

## Local dry run

```bash
export BOOKSTACK_URL="https://wiki.pttimboel.com"
export BOOKSTACK_TOKEN_ID="xxx"
export BOOKSTACK_TOKEN_SECRET="yyy"
python scripts/bookstack_sync.py bookstack --dry-run
```

## Publish manually from GitHub

Go to:

```text
Actions → Publish BookStack Shelves → Run workflow
```

## Rules

- GitHub is the source of truth.
- BookStack is the rendered wiki.
- Do not edit synced pages directly in BookStack.
- This script does not delete remote content.
