#!/usr/bin/env python3
"""Apply hand-written checkpoint 021 lines with immutable English/control codes."""
from pathlib import Path
import json,re,unicodedata
ROOT=Path(__file__).resolve().parent
TOK=re.compile(r"\$\d+(?:'[-\d]+)*;")
LEAD=re.compile(r"^(?:\$\d+(?:'[-\d]+)*;)+")
TAIL=re.compile(r"(?:\$\d+(?:'[-\d]+)*;)+$")

def wrap(s,cap=34):
    # Preserve in-line command order while splitting only between complete words.
    pieces=[];current=''
    for word in s.split():
        candidate=f'{current} {word}' if current else word
        if current and len(TOK.sub('',candidate))>cap:
            pieces.append(current);current=word
        else:current=candidate
    if current:pieces.append(current)
    return '▼'.join(pieces)

for seg,expected in [('0024.005',74),('0025.001',120)]:
    p=ROOT/f'translation/04-thoai/talkfigs__0eng__data__{seg}.jsonl'
    rows=[json.loads(line) for line in p.read_text('utf8').splitlines()]
    plain=(ROOT/f'vi_{seg.replace(".","_")}.txt').read_text('utf8').splitlines()
    assert len(rows)==len(plain)==expected,(seg,len(rows),len(plain))
    for i,(row,body) in enumerate(zip(rows,plain),1):
        en=row['en']
        prefix=LEAD.match(en);suffix=TAIL.search(en)
        vi=unicodedata.normalize('NFC',(prefix.group() if prefix else '')+wrap(body)+(suffix.group() if suffix else ''))
        assert TOK.findall(en)==TOK.findall(vi),(seg,i,'tokens',en,vi)
        assert vi.count('▼')<=3,(seg,i,'line_count',vi)
        assert all(len(TOK.sub('',piece))<=34 for piece in vi.split('▼')),(seg,i,'visible_length',vi)
        assert not any(c in vi for c in '\n\r\t'),(seg,i,'whitespace')
        assert row.get('vi') in (None,'',vi),(seg,i,'would overwrite')
        row['vi']=vi
    p.write_text(''.join(json.dumps(row,ensure_ascii=False,separators=(',',':'))+'\n' for row in rows),'utf8')
    print('PASS',seg,len(rows))