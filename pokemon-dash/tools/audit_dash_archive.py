#!/usr/bin/env python3
"""Pokémon Dash (USA/APDE): read-only nested archive + RelocMod audit.
Usage: python tools/audit_dash_archive.py game.nds [--compare patched.nds] [--out audit]
Standard library only. Does not modify or redistribute ROM data.
"""
import argparse
import csv
import hashlib
import json
import struct
from pathlib import Path


def u32(b, p):
    return struct.unpack_from("<I", b, p)[0]


def files_from_nitrofs(b):
    fnt, _, fat, _ = struct.unpack_from("<IIII", b, 0x40)
    ndirs = struct.unpack_from("<H", b, fnt + 6)[0]
    dirs = [struct.unpack_from("<IHH", b, fnt + 8 * i) for i in range(ndirs)]
    files = {}

    def visit(index, prefix):
        rel, fid, _ = dirs[index]
        at = fnt + rel
        while b[at]:
            flag = b[at]
            at += 1
            name = b[at:at + (flag & 0x7f)].decode("latin1")
            at += flag & 0x7f
            if flag & 0x80:
                child = struct.unpack_from("<H", b, at)[0] - 0xf000
                at += 2
                visit(child, prefix + name + "/")
            else:
                s, e = struct.unpack_from("<II", b, fat + 8 * fid)
                files[prefix + name] = (s, e)
                fid += 1

    visit(0, "")
    return files


def nested_entries(a):
    if not a.startswith(b"NITRO Archive 1\0"):
        raise ValueError("Not a Pokémon Dash NITRO archive")
    n = u32(a, 0x10)
    if not (0 < n < 10000):
        raise ValueError("Invalid archive member count")
    for i in range(n):
        no, off, length = struct.unpack_from("<III", a, 0x20 + i * 12)
        if not (0 < no < len(a) and 0 <= off <= len(a) - length):
            raise ValueError("Out-of-range archive entry")
        end = a.find(b"\0", no)
        if end < 0:
            raise ValueError("Missing member name terminator")
        yield i, a[no:end].decode("latin1"), off, a[off:off + length]


def group(name):
    if "mdl_pause_" in name:
        return "pause"
    if "stage_st_intro" in name:
        return "stage_intro"
    if "mdl_t_stage_st_" in name:
        return "stage_title"
    if any(x in name for x in ("mdl_t_goal", "mdl_t_timesup",
                               "mdl_t_replay", "mdl_t_best_record", "mdl_t_cp_")):
        return "race_status"
    return "other"


def scan(rom):
    if rom[12:16] != b"APDE":
        raise ValueError("Expected Pokemon Dash USA (APDE)")
    fs = files_from_nitrofs(rom)
    start, end = fs["archive.archive"]
    archive = rom[start:end]
    rows = []
    for i, name, off, data in nested_entries(archive):
        flagged = name.startswith("en/") and name.endswith(".rel")
        if flagged and not data.startswith(b"NITRO RelocMod 1"):
            raise ValueError("Unexpected RelocMod header: " + name)
        rows.append({
            "index": i, "path": name, "offset_hex": hex(off), "bytes": len(data),
            "group": group(name), "en_rel_review": flagged,
            "model_version": u32(data, 0x10) if flagged else "",
            "raw_table_count": u32(data, 0x24) if flagged else "",
            "sha256": hashlib.sha256(data).hexdigest(),
        })
    return fs, archive, rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("rom", type=Path)
    ap.add_argument("--compare", type=Path)
    ap.add_argument("--out", type=Path, default=Path("audit"))
    a = ap.parse_args()
    raw = a.rom.read_bytes()
    fs, archive, rows = scan(raw)
    result = {
        "game": "APDE", "files": len(fs), "archive_members": len(rows),
        "en_rel_3d_to_review": sum(r["en_rel_review"] for r in rows),
        "rom_sha256": hashlib.sha256(raw).hexdigest(),
        "archive_sha256": hashlib.sha256(archive).hexdigest(),
        "3d_translation_state": "PENDING_DECODING",
    }
    if a.compare:
        _, comparison_archive, _ = scan(a.compare.read_bytes())
        result["archive_unchanged"] = archive == comparison_archive
    a.out.mkdir(parents=True, exist_ok=True)
    with (a.out / "nested_members.csv").open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    (a.out / "summary.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
