#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Apply verified 050A fixes to merged CP038-050 without changing IDs."""
import argparse
import json
from pathlib import Path


def read(path):
    results = []
    for number, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
        if not line.strip():
            raise ValueError(f"Blank row at {path}:{number}")
        row = json.loads(line)
        if not isinstance(row, dict) or not row.get("id"):
            raise ValueError(f"Missing ID at {path}:{number}")
        results.append(row)
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("merged", type=Path)
    parser.add_argument("--overlay", type=Path, default=Path("BAN_DINH_CHINH_050A.jsonl"))
    parser.add_argument("--output", type=Path, default=Path("BAN_DICH_TONG_HOP_038-050A.jsonl"))
    args = parser.parse_args()
    original = read(args.merged)
    corrections = read(args.overlay)
    if len(original) != 9150 or len(corrections) != 10:
        raise ValueError("Expected 9150 merged IDs and 10 corrections")
    by_id = {row["id"]: row for row in original}
    if len(by_id) != 9150 or len({row["id"] for row in corrections}) != 10:
        raise ValueError("Duplicate ID")
    updates = {}
    for changed in corrections:
        rid = changed["id"]
        old = by_id.get(rid)
        if old is None:
            raise ValueError("Unknown ID: " + rid)
        if set(changed) != set(old) or any(changed[k] != v for k,v in old.items() if k != "vi"):
            raise ValueError("Changed source / metadata: " + rid)
        vi = changed["vi"]
        if not vi or vi == old["vi"] or len(vi) > 37:
            raise ValueError("Invalid translated field: " + rid)
        if vi.count("<IDEOSP>") != old["vi"].count("<IDEOSP>"):
            raise ValueError("Control tokens changed: " + rid)
        updates[rid] = vi
    if args.output.exists():
        raise FileExistsError(args.output)
    result = [({**row, "vi": updates[row["id"]]} if row["id"] in updates else row) for row in original]
    args.output.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in result), encoding="utf-8")
    print(f"PASS: {len(result)} unique IDs, {len(updates)} corrections, 0 newly translated IDs")


if __name__ == "__main__":
    main()
