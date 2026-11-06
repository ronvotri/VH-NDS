#!/usr/bin/env python3
"""Apply checkpoint 020 manually translated dialogue while retaining source metadata/control tokens.
Start from full checkpoint 019; safe to rerun on checkpoint 020 (idempotent).
"""
from pathlib import Path
import json, re, unicodedata
ROOT=Path(__file__).resolve().parent
TOK=re.compile(r"\$\d+(?:'[-\d]+)*;")
LEAD=re.compile(r"^(?:\$\d+(?:'[-\d]+)*;)+")
TAIL=re.compile(r"(?:\$\d+(?:'[-\d]+)*;)+$")

def wrap(s,cap=34):
    parts=[];cur=''
    for word in s.split():
        trial=(cur+' '+word) if cur else word
        if cur and len(TOK.sub('',trial))>cap:
            parts.append(cur);cur=word
        else:cur=trial
    if cur:parts.append(cur)
    return '▼'.join(parts)

for segment in ('003','004'):
    p=ROOT/f'translation/04-thoai/talkfigs__0eng__data__0024.{segment}.jsonl'
    rows=[json.loads(s) for s in p.read_text('utf8').splitlines()]
    vi_lines=(ROOT/f'vi_0024_{segment}.txt').read_text('utf8').splitlines()
    assert len(rows)==len(vi_lines)==120,(segment,len(rows),len(vi_lines))
    for i,(row,plain) in enumerate(zip(rows,vi_lines),1):
        en=row['en']
        prefix=LEAD.match(en);suffix=TAIL.search(en)
        vi=unicodedata.normalize('NFC',(prefix.group() if prefix else '')+wrap(plain)+(suffix.group() if suffix else ''))
        assert TOK.findall(en)==TOK.findall(vi),(segment,i,'tokens',en,vi)
        assert vi.count('▼')<=3,(segment,i,'line count',vi)
        assert all(len(TOK.sub('',s))<=34 for s in vi.split('▼')),(segment,i,'line length',vi)
        assert '\r' not in vi and '\n' not in vi and '\t' not in vi,(segment,i,'whitespace')
        assert row.get('vi') in (None,'',vi),(segment,i,'would overwrite a different existing translation')
        row['vi']=vi
    p.write_text(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in rows),'utf8')
    print('PASS',segment,len(rows),'entries')