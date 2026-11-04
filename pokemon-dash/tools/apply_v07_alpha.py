#!/usr/bin/env python3
"""Apply experimental Pokémon Dash 3D label IPS to an exact v0.6 APDE ROM.
Pure Python / standard library. Does not modify source ROM or save data.
"""
from pathlib import Path
import argparse
import hashlib

BASE_SHA256 = '2dd5d75336f3b3479e21bf795e7276b014d89e1fab59ec68c87760eeeba4018d'
ALPHA_SHA256 = 'd592391af5d125c902545d143c3bca3bc65acc2986efdd1690c6248fd856a16d'


def apply_ips(data: bytes, patch: bytes) -> bytes:
    if not patch.startswith(b'PATCH'):
        raise ValueError('Invalid IPS header')
    output = bytearray(data)
    pos = 5
    while True:
        if pos+3 > len(patch):
            raise ValueError('Truncated IPS')
        if patch[pos:pos+3] == b'EOF':
            return bytes(output)
        offset = int.from_bytes(patch[pos:pos+3], 'big')
        size = int.from_bytes(patch[pos+3:pos+5], 'big')
        pos += 5
        if size == 0:
            count = int.from_bytes(patch[pos:pos+2], 'big')
            value = patch[pos+2]
            pos += 3
            if offset + count > len(output):
                raise ValueError('IPS record beyond ROM')
            output[offset:offset+count] = bytes([value]) * count
        else:
            if offset + size > len(output) or pos + size > len(patch):
                raise ValueError('Invalid IPS range')
            output[offset:offset+size] = patch[pos:pos+size]
            pos += size


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('rom_v06', type=Path)
    parser.add_argument('--patch', type=Path, default=Path(__file__).resolve().parent.parent / 'patches' / 'v06_to_v07_alpha_pause_title.ips')
    parser.add_argument('--out', type=Path, default=Path('PokemonDash_v07_ALPHA_3D_TEST.nds'))
    args = parser.parse_args()
    rom = args.rom_v06.read_bytes()
    if rom[12:16] != b'APDE' or hashlib.sha256(rom).hexdigest() != BASE_SHA256:
        raise ValueError('Input must be exact Pokémon Dash USA v0.6 APDE ROM')
    patched = apply_ips(rom, args.patch.read_bytes())
    if len(patched) != len(rom) or hashlib.sha256(patched).hexdigest() != ALPHA_SHA256:
        raise ValueError('Test patch hash mismatch; output was not saved')
    args.out.write_bytes(patched)
    print('Created', args.out, '(EXPERIMENTAL — not emulator tested)')


if __name__ == '__main__':
    main()
