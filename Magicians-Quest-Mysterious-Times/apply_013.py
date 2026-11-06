#!/usr/bin/env python3
"""Apply hand-written translations for Magician's Quest NDS batch 013."""
from pathlib import Path
import json,re,unicodedata
ROOT=Path(__file__).resolve().parent
TOK=re.compile(r"\$\d+(?:'[-\d]+)*;")
FRONT=re.compile(r"^(?:\$(?:034|024|023|022|040)'[-\d]+(?:'[-\d]+)*;)+")
for part,count in [('004',120),('005',68)]:
    fname=f'talkfigs__0eng__data__0021.{part}.jsonl'
    p=ROOT/'translation'/'04-thoai'/fname
    data=[json.loads(s) for s in p.read_text(encoding='utf-8').splitlines()]
    lines=(ROOT/f'manual_0021_{part}.txt').read_text(encoding='utf-8').splitlines()
    assert len(data)==len(lines)==count,(part,len(data),len(lines))
    for i,(row,trans) in enumerate(zip(data,lines)):
        assert row.get('vi') is None,(part,i,'already translated')
        assert trans.strip() and not trans.startswith('▼') and not trans.endswith('▼'),(part,i,'empty')
        prefix=FRONT.search(row['en'])
        vi=unicodedata.normalize('NFC',(prefix.group() if prefix else '')+trans)
        assert TOK.findall(vi)==TOK.findall(row['en']),(part,i,TOK.findall(row['en']),TOK.findall(vi))
        assert vi.count('▼')<=3,(part,i,'pagebreak')
        assert all(len(TOK.sub('',line))<=34 for line in vi.split('▼')),(part,i,'line >34',vi)
        assert not any(x in vi for x in '\n\r\t'),(part,i,'newlines')
        if row.get('max_utf8_bytes') is not None:
            assert len(vi.encode('utf-8'))<=row['max_utf8_bytes'],(part,i,'UTF8')
        row['vi']=vi
    p.write_text(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in data),encoding='utf-8')
    print('DONE',fname,len(data))