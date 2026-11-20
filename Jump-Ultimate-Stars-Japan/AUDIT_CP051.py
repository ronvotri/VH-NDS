#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compare the authentic Japanese handover with JUS translation CP001-050.

Run from any directory:
    python AUDIT_CP051.py JumpUltimateStars_Japan_BanGiao_Cloud.zip \
        --translations Jump-Ultimate-Stars-Japan

This tool audits and extracts untranslated source rows. It NEVER invents
Japanese text or Vietnamese translations and NEVER patches a game ROM.
"""
import argparse
import hashlib
import io
import json
import re
from collections import defaultdict
from pathlib import Path
from zipfile import ZipFile

EXPECTED_SOURCE_FILES = 30
EXPECTED_SOURCE_ROWS = 34919
EXPECTED_TRANSLATED = 32746
EXPECTED_MISSING = 2173
EXPECTED_SHA = {
    "07-deck-001.jsonl": "dc52ad7a1a57f2298c576f6783c4fe2b915ff7947a0f987d643682cdfa789950",
    "08-credit-001.jsonl": "08982eb9c40751e1ce85f90349b1194e2ae12d1ca8e40c47c95b447398914224",
}
TRANSLATION_PATH = re.compile(r"(?:^|/)translation/([^/]+\.jsonl)$")
MAX_ENTRY_BYTES = 80 * 1024 * 1024


def from_archive(zf, depth=0):
    if depth > 3:
        raise ValueError("Too many nested archive levels")
    for entry in zf.infolist():
        if entry.is_dir() or entry.filename.startswith("__MACOSX/"):
            continue
        name = entry.filename.replace("\\", "/")
        if entry.file_size > MAX_ENTRY_BYTES:
            raise ValueError("Oversized archive entry: " + name)
        match = TRANSLATION_PATH.search(name)
        if match:
            yield match.group(1), zf.read(entry)
        elif name.lower().endswith(".zip"):
            with ZipFile(io.BytesIO(zf.read(entry))) as nested:
                yield from from_archive(nested, depth + 1)


def read_source(source_path):
    data = {}
    if source_path.is_dir():
        entries = [(p.name, p.read_bytes())
                   for p in source_path.rglob("*.jsonl")
                   if p.parent.name == "translation"]
    else:
        with ZipFile(source_path) as zf:
            entries = list(from_archive(zf))
    if len(entries) != EXPECTED_SOURCE_FILES:
        raise ValueError(f"Expected {EXPECTED_SOURCE_FILES} translation files; found {len(entries)}")
    source = {}
    for filename, raw in entries:
        if filename in data:
            raise ValueError("Duplicate source file: " + filename)
        digest = hashlib.sha256(raw).hexdigest()
        if filename in EXPECTED_SHA and digest != EXPECTED_SHA[filename]:
            raise ValueError(f"Unexpected SHA256 for {filename}: {digest}")
        rows = []
        for n, line in enumerate(raw.decode("utf-8-sig").splitlines()):
            if not line.strip():
                raise ValueError(f"Empty physical line: {filename}:{n}")
            row = json.loads(line)
            if not isinstance(row, dict) or not row.get("id") or not row.get("ja"):
                raise ValueError(f"Invalid source ID/JA: {filename}:{n}")
            if row.get("row_index", n) != n:
                raise ValueError(f"Wrong source row_index: {filename}:{n}")
            if Path(row.get("file", filename)).name != filename:
                raise ValueError(f"Wrong source file field: {filename}:{n}")
            if row["id"] in source:
                raise ValueError("Duplicate source ID: " + row["id"])
            normalized = dict(row)
            normalized["file"] = filename
            normalized["row_index"] = n
            source[row["id"]] = normalized
            rows.append(normalized)
        data[filename] = {"sha256": digest, "rows": rows}
    if len(source) != EXPECTED_SOURCE_ROWS:
        raise ValueError(f"Expected {EXPECTED_SOURCE_ROWS} IDs; found {len(source)}")
    return data, source


def read_checkpoint_deltas(directory, source):
    translated = {}
    stats = {}
    for cp in range(1, 51):
        filename = f"BAN_DICH_{cp:03d}.jsonl"
        path = directory / filename
        if not path.is_file():
            raise FileNotFoundError("Missing checkpoint: " + str(path))
        count = 0
        for line_no, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
            if not line.strip():
                raise ValueError(f"Blank translated row: {filename}:{line_no}")
            row = json.loads(line)
            rid = row.get("id")
            if rid in translated:
                raise ValueError(f"Duplicate translated ID {rid} in {filename}")
            original = source.get(rid)
            if original is None:
                raise ValueError(f"Translated ID absent from source: {rid}")
            for key in ("ja", "file", "row_index"):
                if row.get(key) != original.get(key):
                    raise ValueError(f"Source mismatch for {rid}: {key}")
            if "quiz_context" in original and row.get("quiz_context") != original["quiz_context"]:
                raise ValueError(f"Quiz context altered: {rid}")
            if not isinstance(row.get("vi"), str) or not row["vi"].strip():
                raise ValueError(f"Empty Vietnamese text: {rid}")
            translated[rid] = row
            count += 1
        stats[f"{cp:03d}"] = count
    if len(translated) != EXPECTED_TRANSLATED:
        raise ValueError(f"Expected {EXPECTED_TRANSLATED} translated IDs; found {len(translated)}")
    return translated, stats


def write_jsonl(path, records):
    path.write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in records),
                    encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Original handover ZIP or extracted source folder")
    parser.add_argument("--translations", type=Path, default=Path("."),
                        help="Folder containing BAN_DICH_001.jsonl to BAN_DICH_050.jsonl")
    parser.add_argument("--out", type=Path, default=Path("audit-051"))
    args = parser.parse_args()
    data, source = read_source(args.source)
    translated, cp_stats = read_checkpoint_deltas(args.translations, source)
    missing = []
    file_stats = []
    for filename, meta in sorted(data.items()):
        rows = meta["rows"]
        todo = [row for row in rows if row["id"] not in translated]
        missing.extend(todo)
        file_stats.append({
            "file": filename, "source_rows": len(rows),
            "translated": len(rows) - len(todo), "missing": len(todo),
            "source_sha256": meta["sha256"],
            "missing_row_indexes": [row["row_index"] for row in todo],
        })
    if len(missing) != EXPECTED_MISSING:
        raise ValueError(f"Expected {EXPECTED_MISSING} missing IDs; found {len(missing)}")
    args.out.mkdir(parents=True, exist_ok=True)
    write_jsonl(args.out / "CHUA_DICH_051.jsonl", missing)
    write_jsonl(args.out / "NGUON_DECK_CREDITS_051.jsonl",
                [row for row in missing if row["file"] in EXPECTED_SHA])
    qa = {
        "checkpoint": "051-source-audit",
        "status": "AUDIT_ONLY_NOT_TRANSLATED",
        "source_files": len(data), "source_ids": len(source),
        "translated_ids": len(translated), "missing_ids": len(missing),
        "checkpoint_counts": cp_stats, "files": file_stats,
        "source_text_modified": False,
        "new_translations": 0,
        "rom_and_font_tested": False,
        "note": "Presence/ID/JA/metadata audit only; not semantic or byte-fit QA.",
    }
    (args.out / "QA_KIEM_TOAN_051.json").write_text(
        json.dumps(qa, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("SOURCE:", len(source), "TRANSLATED:", len(translated), "MISSING:", len(missing))
    for entry in file_stats:
        if entry["missing"]:
            print(f"  {entry['file']}: {entry['missing']} missing / {entry['source_rows']}")
    print("Files written to", args.out)


if __name__ == "__main__":
    main()
