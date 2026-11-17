#!/usr/bin/env python3
"""Merge public Ragnarok DS ID->vi patches onto the original Cloud handoff ZIP.

Never modifies the original ZIP, its EN fields, the game ROM, fonts, or any binary.
Python 3 standard library only.
"""
import argparse
import json
import re
import zipfile
from pathlib import Path

CONTROL = re.compile(r"<C[0-9A-F]{4}>")
PRINTF = re.compile(r"%(?:\d+\$)?[-+0 #]*\d*(?:\.\d+)?[a-zA-Z%]")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--handoff", type=Path, required=True,
                        help="Original RagnarokDS_USA_BanGiao_Cloud.zip")
    parser.add_argument("--patch-dir", type=Path, required=True,
                        help="Ragnarok-DS/translation directory on vh/ragnarok-ds-usa")
    parser.add_argument("--output", type=Path, required=True,
                        help="Result ZIP with 33 translated JSONL files")
    args = parser.parse_args()
    if args.output.resolve() == args.handoff.resolve():
        parser.error("Refusing to overwrite original handoff ZIP")
    patches = {}
    files = sorted(args.patch_dir.glob("PATCH-DOT001-*.jsonl"))
    if not files:
        parser.error("No PATCH-DOT001-*.jsonl files found")
    for filename in files:
        for n, line in enumerate(filename.read_text(encoding="utf-8-sig").splitlines(), 1):
            if not line.strip():
                continue
            row = json.loads(line)
            uid, vi = row["id"], row["vi"]
            if uid in patches:
                raise ValueError(f"Duplicate ID in patches: {uid} at {filename}:{n}")
            if not isinstance(vi, str) or not vi:
                raise ValueError(f"Invalid vi: {uid}")
            patches[uid] = vi

    all_ids = set()
    updated = 0
    rows_count = 0
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(args.handoff) as source:
        names = sorted(n for n in source.namelist()
                       if n.startswith("translation/") and n.endswith(".jsonl"))
        if len(names) != 33:
            raise ValueError(f"Expected 33 translation files, found {len(names)}")
        with zipfile.ZipFile(args.output, "w", compression=zipfile.ZIP_DEFLATED) as target:
            for filename in names:
                data = []
                for line in source.read(filename).decode("utf-8-sig").splitlines():
                    row = json.loads(line)
                    uid = row["id"]
                    if uid in all_ids:
                        raise ValueError(f"Duplicate source ID: {uid}")
                    all_ids.add(uid)
                    rows_count += 1
                    if uid in patches:
                        vi = patches[uid]
                        en = row["en"]
                        if CONTROL.findall(en) != CONTROL.findall(vi):
                            raise ValueError(f"Changed control codes in {uid}")
                        if PRINTF.findall(en) != PRINTF.findall(vi):
                            raise ValueError(f"Changed printf placeholders in {uid}")
                        if any(x in vi for x in ("\x00", "\r", "\n", "\t")):
                            raise ValueError(f"Raw control character in {uid}")
                        if row.get("group") == "07-credit":
                            for side in ("lstrip", "rstrip"):
                                spaces_en = len(en) - len(getattr(en, side)(" "))
                                spaces_vi = len(vi) - len(getattr(vi, side)(" "))
                                if spaces_en != spaces_vi:
                                    raise ValueError(f"Credit padding changed in {uid}")
                        row["vi"] = vi
                        updated += 1
                    data.append(json.dumps(row, ensure_ascii=False))
                target.writestr(filename, "\n".join(data) + "\n")
            if len(all_ids) != rows_count:
                raise ValueError("Source ID uniqueness check failed")
            missing = sorted(set(patches) - all_ids)
            if missing:
                raise ValueError(f"Patch IDs missing in source: {missing[:5]}")
            report = {
                "source_rows": rows_count,
                "patch_records": len(patches),
                "applied": updated,
                "pending": rows_count - updated,
                "warning": "Partial translation; not a patched ROM. Vietnamese font and display QA still required."
            }
            target.writestr("BAO_CAO_GHEP_PATCH.json",
                            json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(report, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
