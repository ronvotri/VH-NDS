#!/usr/bin/env python3
"""Reapply checkpoint 018 manual translations. Only change `vi`; idempotent."""
from pathlib import Path
import json,re,unicodedata
ROOT=Path(__file__).resolve().parent
TOK=re.compile(r"\$\d+(?:'[-\d]+)*;")
LEAD=re.compile(r"^(?:(?:\$034(?:'[-\d]+)*;)|(?:\$024(?:'[-\d]+)*;)|(?:\$023(?:'[-\d]+)*;)|(?:\$022(?:'[-\d]+)*;))+")
TAIL=re.compile(r"(?:(?:\$019(?:'[-\d]+)*;)|(?:\$074;)|(?:\$079;)|(?:\$023(?:'[-\d]+)*;)|(?:\$034(?:'[-\d]+)*;))+$")
def wrap(s,cap=32):
    o=[]
    for seg in s.split('▼'):
        cur=''
        for word in seg.split():
            trial=(cur+' '+word).strip() if cur else word
            if cur and len(TOK.sub('',trial))>cap:
                o.append(cur)
                cur=word
            else:
                cur=trial
        o.append(cur)
    return '▼'.join(o)
for segment,expected in [('0023.004',120),('0023.005',66)]:
    p=ROOT/f'translation/04-thoai/talkfigs__0eng__data__{segment}.jsonl'
    rows=[json.loads(x) for x in p.read_text(encoding='utf8').splitlines()]
    manual=(ROOT/f'vi_0023_{segment[-3:]}.txt').read_text(encoding='utf8').splitlines()
    assert len(rows)==len(manual)==expected
    for i,(r,plain) in enumerate(zip(rows,manual)):
        en=r['en'];lead=(LEAD.match(en).group() if LEAD.match(en) else '')
        tail=(TAIL.search(en).group() if TAIL.search(en) else '')
        vi=unicodedata.normalize('NFC',lead+wrap(plain)+tail)
        assert TOK.findall(en)==TOK.findall(vi),(segment,i,'mismatch codes')
        assert vi.count('▼')<=3,(segment,i,'too many page breaks')
        assert max(len(TOK.sub('',x)) for x in vi.split('▼'))<=34,(segment,i,'too long')
        assert r.get('vi') in (None,'',vi),(segment,i,'would overwrite existing translation')
        cap=r.get('max_utf8_bytes')
        assert not cap or len(vi.encode('utf8'))<=cap
        r['vi']=vi
    p.write_text(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in rows),encoding='utf8')
    print('PASS applied',segment,expected)