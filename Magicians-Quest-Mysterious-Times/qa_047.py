#!/usr/bin/env python3
"""Checkpoint 047 data audit against prior checkpoint 046 ZIP."""
import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parent
OLD_ARCHIVE = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('/mnt/data/MagiciansQuest-VietHoa-Checkpoint-046.zip')
TOKEN = re.compile(r'\$[^;]*;')
TARGET = {'talkfigs__0eng__data__0033.012.jsonl':120, 'talkfigs__0eng__data__0033.013.jsonl':120}

old_count = new_count = delta = 0
old_trans = new_trans = 0
category = Counter()
with ZipFile(OLD_ARCHIVE) as z:
    paths = sorted(n for n in z.namelist() if '/translation/' in n and n.endswith('.jsonl'))
    assert len(paths) == 501, f'Expected 501 files, got {len(paths)}'
    for old_zip_name in paths:
        relative = old_zip_name.split('/translation/', 1)[1]
        name = Path(relative).name
        new_file = ROOT / 'translation' / relative
        assert new_file.is_file(), f'Missing {new_file}'
        prev_bytes = z.read(old_zip_name)
        new_bytes = new_file.read_bytes()
        old = [json.loads(s) for s in prev_bytes.decode('utf-8').splitlines() if s.strip()]
        new = [json.loads(s) for s in new_bytes.decode('utf-8').splitlines() if s.strip()]
        assert len(old) == len(new), f'Record count differs: {relative}'
        old_count += len(old)
        new_count += len(new)
        old_trans += sum(bool(rec.get('vi')) for rec in old)
        new_trans += sum(bool(rec.get('vi')) for rec in new)
        if name not in TARGET:
            assert prev_bytes == new_bytes, f'Non-target JSONL changed: {relative}'
            continue
        assert len(new) == TARGET[name], f'Target row count differs: {relative}'
        for i, (a,b) in enumerate(zip(old,new),1):
            assert set(a)==set(b), f'Field set changed {relative}:{i}'
            assert {k:v for k,v in a.items() if k!='vi'}=={k:v for k,v in b.items() if k!='vi'}, f'Non-vi changed {relative}:{i}'
            assert a.get('vi') in (None,''), f'Existing translation was overwritten {relative}:{i}'
            vi=b.get('vi')
            assert isinstance(vi,str) and vi.strip(), f'Empty translation {relative}:{i}'
            assert TOKEN.findall(a['en'])==TOKEN.findall(vi), f'Token mismatch {relative}:{i}'
            assert unicodedata.normalize('NFC',vi)==vi, f'Not NFC {relative}:{i}'
            assert '¤' not in vi and all(x not in vi for x in '\r\n\t'), f'Illegal char {relative}:{i}'
            text=TOKEN.sub('',vi)
            assert text.count('▼') <=3, f'Too many linebreaks {relative}:{i}'
            widths=[len(segment) for segment in text.split('▼')]
            assert max(widths)<=34, f'Over 34 visible chars {relative}:{i}, {widths}: {vi}'
            limit=b.get('max_utf8_bytes')
            if limit is not None:
                assert len(vi.encode('utf8'))<=int(limit), f'Byte limit overrun {relative}:{i}'
            delta+=1
        category['NPC']+=len(new)
assert old_count == new_count == 55976, f'Total row count wrong: {old_count}/{new_count}'
assert old_trans == 13189, f'Old translated !=12949: {old_trans}'
assert delta == 240, f'Expected exactly 240 modified translations, got {delta}'
assert new_trans == old_trans + delta == 13429, f'Total translated count inconsistent: {new_trans}'
print(f'PASS: {len(paths)} JSONL, {new_count:,} records; translated {old_trans:,} => {new_trans:,} (+{delta}).')
print('PASS: all old translations preserved; unchanged files byte-identical; only target vi updated.')
print('PASS: token order and values preserved; Unicode NFC; line breaks <=3 and width <=34; byte limits respected.')