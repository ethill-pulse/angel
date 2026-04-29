#!/usr/bin/env python3
"""Summarize lines changed per author per category from *_prs_categorized.csv files."""

import csv
import glob
import sys
from collections import defaultdict

def parse_csvs(pattern="*_prs_categorized.csv"):
    files = glob.glob(pattern)
    if not files:
        print(f"No files matched: {pattern}", file=sys.stderr)
        sys.exit(1)

    # { author: { category: { added, removed } } }
    data = defaultdict(lambda: defaultdict(lambda: {"added": 0, "removed": 0, "prs": 0}))

    for path in sorted(files):
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                author = (row.get("AUTHOR") or "").strip()
                category = (row.get("CATEGORY") or "UNKNOWN").strip()
                if not author or not category:
                    continue
                try:
                    added = int(row.get("LINES_ADDED") or 0)
                    removed = int(row.get("LINES_REMOVED") or 0)
                except ValueError:
                    continue
                data[author][category]["added"] += added
                data[author][category]["removed"] += removed
                data[author][category]["prs"] += 1

    return data

def print_summary(data):
    # Collect all categories
    all_cats = sorted({cat for cats in data.values() for cat in cats})
    authors = sorted(data.keys())

    col_w = max(len(a) for a in authors) + 2
    cat_w = max(len(c) for c in all_cats) + 2

    # Header
    print(f"\n{'AUTHOR':<{col_w}}  {'CATEGORY':<{cat_w}}  {'PRs':>5}  {'ADDED':>8}  {'REMOVED':>8}  {'PERCENT':>8}")
    print("-" * (col_w + cat_w + 42))

    for author in authors:
        cats = data[author]
        author_total = sum(v["added"] + v["removed"] for v in cats.values())
        total_prs = sum(v["prs"] for v in cats.values())
        first = True
        for cat in all_cats:
            if cat not in cats:
                continue
            v = cats[cat]
            cat_total = v["added"] + v["removed"]
            pct = (cat_total / author_total * 100) if author_total else 0
            a_str = f"{author:<{col_w}}" if first else " " * col_w
            print(f"{a_str}  {cat:<{cat_w}}  {v['prs']:>5}  {v['added']:>8}  {v['removed']:>8}  {pct:>7.1f}%")
            first = False
        # Author total
        total_added = sum(v["added"] for v in cats.values())
        total_removed = sum(v["removed"] for v in cats.values())
        print(f"{'':>{col_w}}  {'TOTAL':<{cat_w}}  {total_prs:>5}  {total_added:>8}  {total_removed:>8}  {'100.0%':>8}")
        print()

    # Grand total across all authors
    grand: dict = defaultdict(lambda: {"added": 0, "removed": 0, "prs": 0})
    for cats in data.values():
        for cat, v in cats.items():
            grand[cat]["added"] += v["added"]
            grand[cat]["removed"] += v["removed"]
            grand[cat]["prs"] += v["prs"]

    grand_total = sum(v["added"] + v["removed"] for v in grand.values())
    grand_added = sum(v["added"] for v in grand.values())
    grand_removed = sum(v["removed"] for v in grand.values())
    grand_prs = sum(v["prs"] for v in grand.values())

    print("=" * (col_w + cat_w + 42))
    print(f"\n{'ALL AUTHORS':<{col_w}}  {'CATEGORY':<{cat_w}}  {'PRs':>5}  {'ADDED':>8}  {'REMOVED':>8}  {'PERCENT':>8}")
    print("-" * (col_w + cat_w + 42))
    first = True
    for cat in all_cats:
        if cat not in grand:
            continue
        v = grand[cat]
        cat_total = v["added"] + v["removed"]
        pct = (cat_total / grand_total * 100) if grand_total else 0
        a_str = f"{'ALL AUTHORS':<{col_w}}" if first else " " * col_w
        print(f"{a_str}  {cat:<{cat_w}}  {v['prs']:>5}  {v['added']:>8}  {v['removed']:>8}  {pct:>7.1f}%")
        first = False
    print(f"{'':>{col_w}}  {'TOTAL':<{cat_w}}  {grand_prs:>5}  {grand_added:>8}  {grand_removed:>8}  {'100.0%':>8}")

if __name__ == "__main__":
    import os
    workspace = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pattern = os.path.join(workspace, "*_prs_categorized.csv")
    data = parse_csvs(pattern)
    print_summary(data)
