#!/usr/bin/env python3
"""Rebuild an all-checkpoint 1-52 Vietnamese JUS JSONL from repo files.

Run: python Jump-Ultimate-Stars-Japan/TAO_TONG_HOP_052.py

ID overlays are corrections, not additional translated records.
"""
import argparse
import hashlib
import json
from pathlib import Path

CHECKPOINTS = 52
EXPECTED_UNIQUE = 33680
OVERLAYS = ['BAN_DINH_CHINH_037B.jsonl', 'BAN_DINH_CHINH_037C.jsonl',
            'BAN_DINH_CHINH_046A.jsonl', 'BAN_DINH_CHINH_050A.jsonl']


def rows(path):
    with path.open(encoding='utf-8-sig') as source:
        for i, line in enumerate(source, 1):
            if not line.strip():
                raise ValueError(f'Blank line: {path}:{i}')
            x = json.loads(line)
            if not isinstance(x, dict) or not x.get('id'):
                raise ValueError(f'Invalid row: {path}:{i}')
            yield x


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory', type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument('--out', type=Path, default=Path('BAN_DICH_TONG_HOP_001-052.jsonl'))
    args = parser.parse_args()
    translations = {}
    for cp in range(1, CHECKPOINTS+1):
        src = args.directory / f'BAN_DICH_{cp:03}.jsonl'
        if not src.is_file():
            raise FileNotFoundError(src)
        for x in rows(src):
            rid = x['id']
            if rid in translations:
                raise ValueError(f'Duplicate checkpoint ID: {rid} ({cp})')
            if not isinstance(x.get('vi'), str) or not x['vi'].strip():
                raise ValueError('Missing Vietnamese: ' + rid)
            translations[rid] = x
    if len(translations) != EXPECTED_UNIQUE:
        raise ValueError(f'Unexpected translated total {len(translations)}, expected {EXPECTED_UNIQUE}')
    for name in OVERLAYS:
        src = args.directory / name
        if not src.exists():
            raise FileNotFoundError(src)
        for fix in rows(src):
            old = translations.get(fix['id'])
            if old is None:
                raise ValueError(f'Unknown correction ID: {fix["id"]}')
            for key, value in fix.items():
                if key not in ('id','vi') and key in old and old[key] != value:
                    raise ValueError(f'Correction changed {key}: {fix["id"]}')
            if not isinstance(fix.get('vi'), str) or not fix['vi'].strip():
                raise ValueError('Empty correction: '+fix['id'])
            old['vi'] = fix['vi']
    data = sorted(translations.values(), key=lambda x:(x['file'],x['row_index']))
    if args.out.exists():
        raise FileExistsError(args.out)
    text = ''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in data)
    args.out.write_text(text,encoding='utf8')
    print('PASS:',len(data),'unique Vietnamese IDs; SHA256:',hashlib.sha256(text.encode()).hexdigest())

if __name__=='__main__':
    main()
