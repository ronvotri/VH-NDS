#!/usr/bin/env python3
"""Magician's Quest — manually translated dialogue batch 036.
Only fill previously-null vi fields. Control codes are preserved exactly.
"""
from pathlib import Path
import json, re, unicodedata
ROOT = Path(__file__).resolve().parent
SOURCE = ROOT  # Manually authored translations are bundled with this checkpoint
TOK = re.compile(r"\$\d+(?:'[-\d]+)*;")
LEAD = re.compile(r"^(?:\$(?:034|024|023|022|040)'[-\d]+(?:'[-\d]+)*;)+")
TAIL = re.compile(r"(?:\$(?:019|074|079|034)(?:'[-\d]+)*;|\$023'328'104'10;)+$")

def visible(s):
    return len(TOK.sub('', s))

def wrap(s, limit=32):
    lines, cur = [], ''
    for word in s.strip().split():
        trial = (cur + ' ' + word) if cur else word
        if cur and visible(trial) > limit:
            lines.append(cur)
            cur = word
        else:
            cur = trial
    if cur: lines.append(cur)
    return '▼'.join(lines)

for part, expected in [('0030.005', 120), ('0031.001', 120)]:
    src = ROOT / 'translation' / '04-thoai' / f'talkfigs__0eng__data__{part}.jsonl'
    lines = src.read_text(encoding='utf-8').splitlines()
    rows = [json.loads(line) for line in lines]
    raw = (SOURCE / f'vi_{part.replace(".", "_")}_raw.txt').read_text(encoding='utf-8').splitlines()
    assert len(rows) == len(raw) == expected, (part, len(rows), len(raw))
    output = []
    for n, (row, translation) in enumerate(zip(rows,raw),1):
        if row.get('vi') not in [None, '']:
            raise ValueError(f'Existing translation in {part}:{n}')
        en = row['en']; prefix_match = LEAD.match(en)
        prefix = prefix_match.group(0) if prefix_match else ''
        suffix_match = TAIL.search(en)
        suffix = suffix_match.group(0) if suffix_match and suffix_match.start() >= len(prefix) else ''
        vi = unicodedata.normalize('NFC', prefix + wrap(translation) + suffix)
        if TOK.findall(en) != TOK.findall(vi):
            raise ValueError(f'Token discrepancy in {part}:{n} {row["id"]}\nEN {TOK.findall(en)}\nVI {TOK.findall(vi)}\n{vi}')
        if vi.count('▼') > 3:
            raise ValueError(f'Too many wrapped lines: {part}:{n}: {vi}')
        if max(map(visible, vi.split('▼'))) > 34:
            raise ValueError(f'Line >34: {part}:{n}: {vi}')
        if any(c in vi for c in '\r\n\t'):
            raise ValueError(f'Illegal whitespace: {part}:{n}: {vi}')
        if row.get('max_utf8_bytes') is not None and len(vi.encode('utf-8')) > row['max_utf8_bytes']:
            raise ValueError(f'Byte limit: {part}:{n}')
        row['vi'] = vi
        output.append(vi)
    src.write_text(''.join(json.dumps(row, ensure_ascii=False, separators=(',', ':'))+'\n' for row in rows), encoding='utf-8')
    (ROOT / f'vi_{part.replace(".", "_")}.txt').write_text('\n'.join(output)+'\n', encoding='utf-8')
    (ROOT / f'vi_{part.replace(".", "_")}_raw.txt').write_text('\n'.join(raw)+'\n',encoding='utf-8')
    with (ROOT / f'manual_{part.replace(".", "_")}.tsv').open('w',encoding='utf-8') as f:
        f.write('id\ten\tvi\n')
        for row in rows:
            f.write('\t'.join(row[key].replace('▼',' / ').replace('\t',' ') for key in ('id','en','vi'))+'\n')
    print(f'PASS {part}: {len(rows)} translations; max line {max(visible(line) for v in output for line in v.split("▼"))}; max breaks {max(x.count("▼") for x in output)}')