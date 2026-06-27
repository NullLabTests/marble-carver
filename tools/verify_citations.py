#!/usr/bin/env python3
"""Verify citations (PMIDs, DOIs) against public APIs.

Usage:
    python tools/verify_citations.py --check <path>
    python tools/verify_citations.py --check carvings/ --report
"""

import argparse
import re
import subprocess
import sys
import urllib.request
import urllib.parse
import json
from pathlib import Path


PMID_RE = re.compile(r"PMID:\s*(\d+)")
DOI_RE = re.compile(r"DOI:\s*(10\.\S+)")


def extract_citations(filepath: str) -> list[dict]:
    """Extract PMIDs and DOIs from a Markdown file."""
    path = Path(filepath)
    if not path.exists():
        return []
    text = path.read_text()
    pmids = [{"type": "pmid", "id": m} for m in PMID_RE.findall(text)]
    dois = [{"type": "doi", "id": d} for d in DOI_RE.findall(text)]
    return pmids + dois


def verify_pmid(pmid: str) -> dict:
    """Verify PMID via NCBI E-utilities."""
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id={pmid}&retmode=json"
    try:
        with urllib.request.urlopen(url, timeout=10) as resp:
            data = json.loads(resp.read())
            uid = str(pmid)
            if uid in data.get("result", {}).get("uids", []):
                info = data["result"][uid]
                return {
                    "valid": True,
                    "title": info.get("title", ""),
                    "year": info.get("pubdate", ""),
                    "source": info.get("source", ""),
                }
    except Exception:
        pass
    return {"valid": False}


def verify_doi(doi: str) -> dict:
    """Verify DOI via crossref API."""
    url = f"https://api.crossref.org/works/{urllib.parse.quote(doi)}"
    try:
        with urllib.request.urlopen(url, timeout=10) as resp:
            data = json.loads(resp.read())
            msg = data.get("message", {})
            return {
                "valid": True,
                "title": msg.get("title", [""])[0] if msg.get("title") else "",
                "year": (msg.get("published-print") or msg.get("published-online") or {}).get("date-parts", [[None]])[0][0],
                "source": (msg.get("publisher") or ""),
            }
    except Exception:
        pass
    return {"valid": False}


def check_file(filepath: str, report: bool = False) -> list[dict]:
    """Check all citations in a file."""
    citations = extract_citations(filepath)
    results = []
    for c in citations:
        if c["type"] == "pmid":
            result = verify_pmid(c["id"])
        else:
            result = verify_doi(c["id"])
        results.append({**c, **result})
    return results


def main():
    parser = argparse.ArgumentParser(
        description="Verify PMIDs and DOIs in carving documents."
    )
    parser.add_argument(
        "--check",
        required=True,
        help="File or directory to check.",
    )
    parser.add_argument(
        "--report",
        action="store_true",
        help="Print a detailed report.",
    )
    args = parser.parse_args()

    path = Path(args.check)
    files = [str(f) for f in path.rglob("*.md")] if path.is_dir() else [str(path)]

    all_results = {}
    for f in files:
        results = check_file(f, report=args.report)
        if results:
            all_results[f] = results

    total = sum(len(v) for v in all_results.values())
    valid = sum(1 for v in all_results.values() for r in v if r.get("valid"))
    failed = total - valid

    print(f"Checked {len(files)} files, {total} citations.")
    print(f"  ✅ {valid} verified")
    print(f"  ❌ {failed} failed or not found")

    if args.report:
        for f, results in all_results.items():
            print(f"\n--- {f} ---")
            for r in results:
                status = "✅" if r.get("valid") else "❌"
                label = f"{r['type'].upper()}: {r['id']}"
                extra = ""
                if r.get("title"):
                    extra = f" → {r['title'][:80]}"
                print(f"  {status} {label}{extra}")

    return 1 if failed > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
