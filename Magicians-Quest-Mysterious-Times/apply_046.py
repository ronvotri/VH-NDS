#!/usr/bin/env python3
"""Apply hand-edited Vietnamese to Magician's Quest checkpoint 046.

Use ¤ as a positional placeholder for a non-prefix game token. Leading game
control codes remain attached automatically. Fails closed on count mismatch.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parent
TOKEN = re.compile(r'\$[^;]*;')
TARGETS = {'0033.010': 'vn_0033_010.txt', '0033.011': 'vn_0033_011.txt'}

def merge(en: str, translated: str) -> str:
    leading = ''
    tail = en
    while match := TOKEN.match(tail):
        leading += match.group()
        tail = tail[match.end():]
    codes = TOKEN.findall(tail)
    if translated.count('¤') != len(codes):
        raise ValueError(f'placeholder count differs: {en!r} => {translated!r}')
    res = translated
    for code in codes:
        res = res.replace('¤', code, 1)
    return leading + res

for suffix, txt in TARGETS.items():
    path = ROOT / 'translation' / '04-thoai' / f'talkfigs__0eng__data__{suffix}.jsonl'
    records = [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines() if line.strip()]
    translations = (SOURCE / txt).read_text(encoding='utf-8').splitlines()
    if len(records) != 120 or len(translations) != len(records):
        raise ValueError(f'Row count mismatch {suffix}: records={len(records)}, Vietnamese={len(translations)}')
    for idx, (record, vi) in enumerate(zip(records, translations), 1):
        if record.get('vi') is not None:
            raise ValueError(f'{suffix} row {idx} already translated, stop to prevent overwrite')
        record['vi'] = merge(record['en'], vi)
    path.write_text('\n'.join(json.dumps(rec, ensure_ascii=False, separators=(',', ':')) for rec in records)+'\n', encoding='utf-8')
    print(f'Applied {len(records)} pages to {path.name}')