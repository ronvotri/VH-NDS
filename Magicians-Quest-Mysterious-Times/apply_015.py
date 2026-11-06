#!/usr/bin/env python3
"""Insert two hand-written 120-row NPC dialogue files. Keep immutable IDs and control codes."""
import json,re,unicodedata
from pathlib import Path
ROOT=Path(__file__).resolve().parent
TOKEN=re.compile(r"\$\d+(?:'[-\d]+)*;")
FRONT=re.compile(r"^(?:\$\d+(?:'[-\d]+)*;)+")
for part in ('003','004'):
    path=ROOT/f'translation/04-thoai/talkfigs__0eng__data__0022.{part}.jsonl'
    rows=[json.loads(line) for line in path.read_text(encoding='utf8').splitlines()]
    translations=(ROOT/f'manual_0022_{part}.txt').read_text(encoding='utf8').splitlines()
    assert len(rows)==len(translations)==120,(part,len(rows),len(translations))
    for i,(row,trans) in enumerate(zip(rows,translations)):
        assert trans and trans==trans.strip(),(part,i,'whitespace')
        m=FRONT.match(row['en'])
        vi=unicodedata.normalize('NFC',(m.group() if m else '')+trans)
        assert TOKEN.findall(vi)==TOKEN.findall(row['en']),(part,i,'control token',TOKEN.findall(vi),TOKEN.findall(row['en']))
        assert vi.count('▼')<=3,(part,i,'too many breaks')
        assert all(len(TOKEN.sub('',s))<=34 for s in vi.split('▼')),(part,i,'long visible line',vi)
        assert not any(c in vi for c in '\n\r\t'),(part,i,'raw whitespace')
        if row.get('max_utf8_bytes') is not None:
            assert len(vi.encode('utf8'))<=row['max_utf8_bytes'],(part,i,'too many bytes')
        assert row['vi'] in (None,'',vi),(part,i,'prior translation differs')
        row['vi']=vi
    path.write_text(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in rows),encoding='utf8')
    print('TRANSLATED',path.name,len(rows))