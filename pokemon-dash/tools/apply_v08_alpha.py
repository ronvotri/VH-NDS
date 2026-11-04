#!/usr/bin/env python3
"""Apply experimental Pokemon Dash v0.7-alpha -> v0.8-alpha incremental IPS.

Verifies game APDE and SHA-256 before *and after* patching. No ROM distribution.
"""
from pathlib import Path
import argparse
import hashlib

BASE = 'd592391af5d125c902545d143c3bca3bc65acc2986efdd1690c6248fd856a16d'
OUTPUT = '635353b74025daf83e9a4d0a121e24896696fa0c2e8cf644c444e60ab57f0b3b'


def apply_ips(data: bytes, patch: bytes) -> bytes:
    if patch[:5] != b'PATCH':
        raise ValueError('Invalid IPS header')
    result = bytearray(data)
    pos = 5
    while pos < len(patch):
        if patch[pos:pos+3] == b'EOF':
            return bytes(result)
        if pos+5 > len(patch):
            raise ValueError('Truncated IPS')
        offset = int.from_bytes(patch[pos:pos+3], 'big')
        size = int.from_bytes(patch[pos+3:pos+5], 'big')
        pos += 5
        if size:
            if offset+size > len(result) or pos+size > len(patch):
                raise ValueError('Out-of-bounds IPS record')
            result[offset:offset+size] = patch[pos:pos+size]
            pos += size
        else:
            count = int.from_bytes(patch[pos:pos+2], 'big')
            value = patch[pos+2]
            pos += 3
            if offset+count > len(result):
                raise ValueError('Out-of-bounds IPS RLE')
            result[offset:offset+count] = bytes([value]) * count
    raise ValueError('Missing IPS EOF')


def main():
    p = argparse.ArgumentParser()
    p.add_argument('rom_v07', type=Path)
    p.add_argument('--patch', type=Path, default=Path(__file__).resolve().parent.parent / 'patches' / 'v07_to_v08_alpha_pause_continue.ips')
    p.add_argument('--out', type=Path, default=Path('PokemonDash_v08_ALPHA_3D_PAUSE_TEST.nds'))
    a = p.parse_args()
    raw = a.rom_v07.read_bytes()
    if raw[12:16] != b'APDE' or hashlib.sha256(raw).hexdigest() != BASE:
        raise ValueError('Expected exact Pokemon Dash USA v0.7 ALPHA input')
    new = apply_ips(raw, a.patch.read_bytes())
    if len(new) != len(raw) or hashlib.sha256(new).hexdigest() != OUTPUT:
        raise ValueError('Output hash mismatch: nothing saved')
    a.out.write_bytes(new)
    print(f'Saved {a.out} — UNTESTED ALPHA; do not replace stable v0.6')


if __name__ == '__main__':
    main()
