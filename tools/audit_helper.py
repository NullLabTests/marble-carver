#!/usr/bin/env python3
"""Helper for adding audit notes to carving attempts.

Usage:
    python tools/audit_helper.py --add carvings/attempt_001.md
    python tools/audit_helper.py --list carvings/
"""

import argparse
import re
from datetime import date
from pathlib import Path


AUDIT_NUMBER_RE = re.compile(r"audit_(\d+)")
ATTEMPT_NUMBER_RE = re.compile(r"attempt_(\d+)")


def find_attempt_number(filepath: str) -> str | None:
    m = ATTEMPT_NUMBER_RE.search(filepath)
    return m.group(1) if m else None


def find_next_audit_number(directory: str) -> str:
    existing = []
    for f in Path(directory).glob("audit_*.md"):
        m = AUDIT_NUMBER_RE.match(f.stem)
        if m:
            existing.append(int(m.group(1)))
    return str(max(existing) + 1 if existing else 1).zfill(3)


def generate_audit_note(
    attempt_path: str, attempt_number: str, audit_number: str
) -> str:
    today = date.today().isoformat()
    return f"""# Audit Note {audit_number}

> **Date:** {today}
> **Author:** (your name)
> **Original attempt:** [attempt_{attempt_number}.md](attempt_{attempt_number}.md)

---

## Scope

This audit note addresses claim(s) made in **attempt {attempt_number}**.

---

## Original claim (unchanged)

> *Quote the exact claim from the original attempt here.*

The original text remains visible at `attempt_{attempt_number}.md`.

---

## What was wrong

(Describe the error.)

- [ ] Logical error / flawed reasoning
- [ ] Incorrect data / miscalculation
- [ ] Misattributed or invalid citation
- [ ] Methodological flaw
- [ ] Other:

---

## Correction

(State the correct claim or result.)

---

## Impact on downstream attempts

-

---

## Lessons

(What did we learn from this mistake?)
"""


def add_audit(attempt_path: str) -> str:
    attempt = Path(attempt_path)
    if not attempt.exists():
        raise FileNotFoundError(f"Attempt not found: {attempt_path}")

    attempt_num = find_attempt_number(attempt_path)
    if not attempt_num:
        raise ValueError(f"Could not parse attempt number from: {attempt_path}")

    audit_num = find_next_audit_number(str(attempt.parent))
    audit_path = attempt.parent / f"audit_{audit_num}.md"

    if audit_path.exists():
        raise FileExistsError(f"Audit note already exists: {audit_path}")

    content = generate_audit_note(attempt_path, attempt_num, audit_num)
    audit_path.write_text(content)

    # Add pointer to audit note in the attempt file
    pointer = f"\n> **Audit note:** [audit_{audit_num}.md](audit_{audit_num}.md)\n"
    original = attempt.read_text()
    if "**Audit note:**" not in original:
        attempt.write_text(original + pointer)

    return str(audit_path)


def list_attempts(directory: str) -> list[str]:
    return sorted(str(f) for f in Path(directory).glob("attempt_*.md"))


def main():
    parser = argparse.ArgumentParser(
        description="Manage audit notes for carving attempts."
    )
    parser.add_argument("--add", help="Path to an attempt file to audit.")
    parser.add_argument(
        "--list",
        action="store_true",
        help="List all attempts in a directory.",
    )
    parser.add_argument("directory", nargs="?", default=".", help="Target directory.")
    args = parser.parse_args()

    if args.add:
        audit_path = add_audit(args.add)
        print(f"✅ Created audit note: {audit_path}")

    if args.list:
        attempts = list_attempts(args.directory)
        if attempts:
            print(f"Found {len(attempts)} attempt(s):")
            for a in attempts:
                print(f"  • {a}")
        else:
            print("No attempts found.")


if __name__ == "__main__":
    main()
