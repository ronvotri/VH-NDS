#!/usr/bin/env python3
"""Pokemon Dash: verify and apply two experimental Pause-label IPS patches.

Usage: python apply_v084_alpha.py PokemonDash_v082_ALPHA_ACCENT_FIX.nds
The source ROM is never overwritten. No original game data included.
"""
import argparse
import hashlib
from pathlib import Path

BASE_SHA256 = "acf443cba3c4333867e29d4df733fc896f561d7365b5f6f3420bbd25a95794e0"
OUTPUT_SHA256 = "823e6818bf32ed91e015c23c9ccfcda1089afa040c9d90834527a8e467e6237e"


def apply_ips(data: bytes, patch: bytes) -> bytes:
    if patch[:5] != b"PATCH":
        raise ValueError("Not an IPS patch")
    dst = bytearray(data)
    pos = 5
    while True:
        if pos + 3 > len(patch):
            raise ValueError("Truncated IPS")
        if patch[pos:pos+3] == b"EOF":
            return bytes(dst)
        if pos + 5 > len(patch):
            raise ValueError("Truncated IPS record")
        offset = int.from_bytes(patch[pos:pos+3], "big")
        length = int.from_bytes(patch[pos+3:pos+5], "big")
        pos += 5
        if length:
            if offset+length > len(dst) or pos+length > len(patch):
                raise ValueError("Invalid IPS write boundary")
            dst[offset:offset+length] = patch[pos:pos+length]
            pos += length
        else:
            if pos + 3 > len(patch):
                raise ValueError("Truncated IPS RLE")
            n = int.from_bytes(patch[pos:pos+2], "big")
            value = patch[pos+2]
            pos += 3
            if offset+n > len(dst):
                raise ValueError("Invalid RLE write boundary")
            dst[offset:offset+n] = bytes([value]) * n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("rom_v082", type=Path)
    ap.add_argument("--out", type=Path, default=Path("PokemonDash_v084_ALPHA_PAUSE.nds"))
    a = ap.parse_args()
    rom = a.rom_v082.read_bytes()
    if rom[12:16] != b"APDE" or hashlib.sha256(rom).hexdigest() != BASE_SHA256:
        raise ValueError("Need exact Pokémon Dash v0.8.2 Alpha APDE input")
    patches = Path(__file__).resolve().parent.parent / "patches"
    for name in ("v082_to_v083_alpha_retry.ips", "v083_to_v084_alpha_course.ips"):
        rom = apply_ips(rom, (patches/name).read_bytes())
    if len(rom) != 16 * 1024 * 1024 or hashlib.sha256(rom).hexdigest() != OUTPUT_SHA256:
        raise ValueError("Output verification failed; nothing was saved")
    a.out.write_bytes(rom)
    print("Wrote", a.out, "(experimental: not gameplay-tested)")


if __name__ == "__main__":
    main()
