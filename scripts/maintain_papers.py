#!/usr/bin/env python3
"""Validate the bilingual bibliography and export a paper manifest."""
import argparse
import csv
import re
import time
from collections import Counter
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
HEAD = re.compile(r"^## (\d{2})\. (.*?) \((\d+)\)\s*$")
ROW = re.compile(r"^\|\s*(\d{2,})\s*\|")
SOURCE = re.compile(r"\[[^\]]+\]\((https?://[^)\s]+)\)")
CORE = re.compile(r"^- \[[ xX]\] #(\d{2,}) — \[([^\]]+)\]\((https?://[^)\s]+)\)")


def parse(path):
    text = path.read_text(encoding="utf-8")
    rows, groups, core = [], {}, []
    section = None
    for line in text.splitlines():
        m = HEAD.match(line)
        if m:
            section = int(m[1])
            if section in groups:
                raise ValueError(f"{path.name}: duplicate category {section}")
            groups[section] = (m[2], int(m[3]))
        elif line.startswith("## "):
            section = None
        if ROW.match(line):
            cells = [x.strip() for x in line.strip().strip("|").split("|")]
            if len(cells) != 6 or section is None:
                raise ValueError(f"{path.name}: malformed row: {line}")
            idx, title, venue, focus, source, priority = cells
            match = SOURCE.fullmatch(source)
            if not match or priority.strip("*") not in {"S", "A", "B"}:
                raise ValueError(f"{path.name}: invalid source or priority in row {idx}")
            rows.append(dict(id=int(idx), category_id=section,
                             category=groups[section][0], title=title, venue=venue,
                             focus=focus, url=match[1], priority=priority.strip("*")))
        m = CORE.match(line)
        if m:
            core.append((int(m[1]), m[2], m[3]))
    return text, rows, groups, core


def validate(path):
    text, rows, groups, core = parse(path)
    errors = []
    def require(ok, message):
        if not ok:
            errors.append(f"{path.name}: {message}")
    require(list(groups) == list(range(1, 8)), "expected seven ordered categories")
    require([r["id"] for r in rows] == list(range(1, len(rows) + 1)), "IDs must be consecutive")
    counts = Counter(r["category_id"] for r in rows)
    for i, (_, expected) in groups.items():
        require(counts[i] == expected, f"category {i}: count mismatch")
    require(f"Papers-{len(rows)}-" in text, "paper count badge mismatch")
    for field in ("title", "url"):
        normalized = [r[field].strip().lower().rstrip("/") for r in rows]
        require(len(set(normalized)) == len(normalized), f"duplicate {field}")
    lookup = {r["id"]: (r["title"], r["url"]) for r in rows}
    require(len(core) == len(set(i for i, _, _ in core)), "duplicate core reading references")
    for i, title, url in core:
        require(lookup.get(i) == (title, url), f"core reference #{i:02d} does not match table")
    require(f"Core%20Reading-{len(core)}-" in text, "core reading badge mismatch")
    return rows, core, errors


def write_csv(path, records):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not records:
        raise ValueError("No records to export")
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)
    print(f"Wrote {path} ({len(records)} rows)")


def check_url(url, timeout):
    # GET is more widely supported than HEAD. Do not download the body.
    request = Request(url, headers={"User-Agent": "DexterousManipulationBibliography/1.0"})
    try:
        with urlopen(request, timeout=timeout) as response:
            return str(response.status), response.geturl()
    except HTTPError as exc:
        return f"HTTP {exc.code}", str(exc)
    except (URLError, TimeoutError, OSError) as exc:
        return "error", str(exc)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("check", "export", "links"))
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, help="CSV path (export or links)")
    parser.add_argument("--timeout", type=float, default=15)
    args = parser.parse_args()
    en, en_core, errors = validate(args.root / "README.md")
    zh, zh_core, zh_errors = validate(args.root / "README.zh-CN.md")
    errors += zh_errors
    fields = ("id", "category_id", "title", "venue", "url", "priority")
    signature = lambda rows: [tuple(r[k] for k in fields) for r in rows]
    if signature(en) != signature(zh):
        errors.append("English and Chinese paper records differ")
    if en_core != zh_core:
        errors.append("English and Chinese core reading lists differ")
    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    print(f"OK: {len(en)} papers, seven categories, {len(en_core)} core references; bilingual records match.")
    if args.command == "export":
        write_csv(args.output or args.root / "exports" / "papers.csv", en)
    elif args.command == "links":
        records = []
        for r in en:
            status, detail = check_url(r["url"], args.timeout)
            records.append(dict(id=r["id"], title=r["title"], url=r["url"],
                                status=status, detail=detail))
            print(f"{r['id']:02d} {status} {r['title']}", flush=True)
            time.sleep(0.5)
        write_csv(args.output or args.root / "exports" / "link_report.csv", records)
        print("HTTP reachability is not paper identity verification; review errors manually.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
