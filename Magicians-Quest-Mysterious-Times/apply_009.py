#!/usr/bin/env python3
"""Apply manually reviewed Vietnamese translations to two 0020 dialogue JSONL files.

Run on a fresh extraction of checkpoint 008. Fails rather than overwriting
existing non-empty translations. Keeps ID/en/ctx/file ordering unchanged.
"""
from pathlib import Path
import json
import re
import unicodedata

root = Path(__file__).resolve().parent
TOKEN = re.compile(r"\$\d{3}(?:'[^;\r\n\t]*)?;")
PREFIX = re.compile(r"^((?:\$(?:024|023|022)'[^;\r\n\t]*;)+)")
for chunk in ('001', '002'):
    f = root / 'translation' / '04-thoai' / f'talkfigs__0eng__data__0020.{chunk}.jsonl'
    rows = [json.loads(ln) for ln in f.read_text(encoding='utf-8').splitlines()]
    translations = (root / f'manual_0020_{chunk}.txt').read_text(encoding='utf-8').splitlines()
    if len(rows) != len(translations) or len(rows) != 120:
        raise ValueError(f'Count mismatch {f.name}: {len(rows)} != {len(translations)}')
    for i, (r, vi) in enumerate(zip(rows, translations), 1):
        if r['vi'] is not None:
            raise ValueError(f'Would overwrite: {f.name} row {i}')
        match = PREFIX.match(r['en'])
        vi = unicodedata.normalize('NFC', (match.group(1) if match else '') + vi)
        src_tokens = TOKEN.findall(r['en'])
        if TOKEN.findall(vi) != src_tokens:
            raise ValueError(f'Token mismatch: {f.name} row {i}: {src_tokens} -> {TOKEN.findall(vi)}')
        if vi.count('▼') > max(2, r['en'].count('▼')):
            raise ValueError(f'Too many displayed lines {f.name} row {i}')
        if any(ch in vi for ch in ('\r', '\n', '\t')):
            raise ValueError(f'Newline/tab leaked into {f.name} row {i}')
        if 'max_utf8_bytes' in r and r['max_utf8_bytes'] is not None and len(vi.encode()) > r['max_utf8_bytes']:
            raise ValueError(f'Overflow: {f.name} row {i}')
        r['vi'] = vi
    f.write_text(''.join(json.dumps(row, ensure_ascii=False, separators=(',', ':')) + '\n' for row in rows), encoding='utf-8')
    print(f'Updated {len(rows)}: {f.name}')