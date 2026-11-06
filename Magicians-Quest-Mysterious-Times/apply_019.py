#!/usr/bin/env python3
"""Apply manually translated page text for checkpoint 019, only changing `vi`."""
from pathlib import Path
import json,re,unicodedata
ROOT=Path(__file__).resolve().parent
TOK=re.compile(r"\$\d+(?:'[-\d]+)*;")
LEAD=re.compile(r"^(?:(?:\$034(?:'[-\d]+)*;)|(?:\$024(?:'[-\d]+)*;)|(?:\$023(?:'[-\d]+)*;)|(?:\$022(?:'[-\d]+)*;))+")
TAIL=re.compile(r"(?:(?:\$019(?:'[-\d]+)*;)|(?:\$074;)|(?:\$079;)|(?:\$023(?:'[-\d]+)*;)|(?:\$034(?:'[-\d]+)*;))+$")

def wrap(text,cap=32):
    out=[]
    for segment in text.split('▼'):
        cur=''
        for word in segment.split():
            trial=(cur+' '+word) if cur else word
            if cur and len(TOK.sub('',trial))>cap:
                out.append(cur)
                cur=word
            else:cur=trial
        out.append(cur)
    return '▼'.join(out)

for seg in ('001','002'):
    p=ROOT/f'translation/04-thoai/talkfigs__0eng__data__0024.{seg}.jsonl'
    rows=[json.loads(l) for l in p.read_text('utf8').splitlines()]
    lines=(ROOT/f'vi_0024_{seg}.txt').read_text('utf8').splitlines()
    assert len(rows)==len(lines)==120,(seg,len(rows),len(lines))
    changed=0
    for i,(row,plain) in enumerate(zip(rows,lines)):
        en=row['en']
        leading=LEAD.match(en)
        trailing=TAIL.search(en)
        vi=unicodedata.normalize('NFC',(leading.group() if leading else '')+wrap(plain)+(trailing.group() if trailing else ''))
        assert TOK.findall(en)==TOK.findall(vi),(seg,i,'tokens',TOK.findall(en),TOK.findall(vi))
        assert vi.count('▼')<=3,(seg,i,'page breaks',vi.count('▼'),plain)
        lengths=[len(TOK.sub('',s)) for s in vi.split('▼')]
        assert max(lengths)<=34,(seg,i,'lengths',lengths,plain)
        assert row.get('vi') in ('',None,vi),(seg,i,'overwrite')
        assert '\n' not in vi and '\t' not in vi and '\r' not in vi
        row['vi']=vi;changed+=1
    p.write_text(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in rows),encoding='utf8')
    print(f'PASS: 0024.{seg} +{changed} entries')