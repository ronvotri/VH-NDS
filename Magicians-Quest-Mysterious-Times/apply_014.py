#!/usr/bin/env python3
"""Apply hand-written NPC translation batch 014, preserve all source control codes."""
from pathlib import Path
import json,re,unicodedata
ROOT=Path(__file__).resolve().parent
TOKEN=re.compile(r"\$\d+(?:'[-\d]+)*;")
FRONT=re.compile(r"^(?:\$\d+(?:'[-\d]+)*;)+")
for part,expected in [('001',120),('002',120)]:
    path=ROOT/f'translation/04-thoai/talkfigs__0eng__data__0022.{part}.jsonl'
    rows=[json.loads(line) for line in path.read_text(encoding='utf-8').splitlines()]
    manual=(ROOT/f'manual_0022_{part}.txt').read_text(encoding='utf-8').splitlines()
    assert len(rows)==len(manual)==expected,(part,len(rows),len(manual))
    for i,(row,trans) in enumerate(zip(rows,manual)):
        assert row.get('vi') is None,(part,i,'translation already filled')
        assert trans.strip() and not trans.startswith('▼') and not trans.endswith('▼'),(part,i,'empty')
        m=FRONT.match(row['en'])
        vi=unicodedata.normalize('NFC',(m.group() if m else '')+trans)
        assert TOKEN.findall(vi)==TOKEN.findall(row['en']),(part,i,'tokens',TOKEN.findall(row['en']),TOKEN.findall(vi))
        assert vi.count('▼')<=3,(part,i,'breaks')
        assert all(len(TOKEN.sub('',s))<=34 for s in vi.split('▼')),(part,i,'long line',vi)
        assert not any(x in vi for x in '\t\r\n'),(part,i,'bad whitespace')
        if row.get('max_utf8_bytes') is not None:
            assert len(vi.encode('utf-8'))<=row['max_utf8_bytes'],(part,i,'too many bytes')
        row['vi']=vi
    path.write_text(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in rows),encoding='utf-8')
    print('DONE',path.name,len(rows))