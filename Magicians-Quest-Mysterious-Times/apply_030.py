#!/usr/bin/env python3
"""Apply manual Vietnamese translations to only the two designated JSONL files.
Preserve script tokens (including expression, branching, menu choices and variable ids).
"""
from pathlib import Path
import json
import re
import unicodedata

ROOT=Path(__file__).resolve().parent
TOK=re.compile(r"\$\d+(?:'[-\d]+)*;")
LEAD=re.compile(r"^(?:\$(?:034|024|023|022|040)'[-\d]+(?:'[-\d]+)*;)+")
TAIL=re.compile(r"(?:\$\d+(?:'[-\d]+)*;)+$")
TARGETS=(('0028.003',120),('0028.004',120))

for segment,expected in TARGETS:
    path=ROOT/f'translation/04-thoai/talkfigs__0eng__data__{segment}.jsonl'
    texts=(ROOT/f'vi_{segment.replace(".","_")}.txt').read_text('utf8').splitlines()
    rows=[json.loads(line) for line in path.read_text('utf8').splitlines()]
    assert len(rows)==len(texts)==expected,(segment,len(rows),len(texts))
    updated=[]
    manual=[]
    for index,(row,body) in enumerate(zip(rows,texts),1):
        src=row['en']
        lead=LEAD.match(src)
        prefix=lead.group(0) if lead else ''
        tail=TAIL.search(src)
        suffix=tail.group(0) if tail and tail.start()>len(prefix) else ''
        vi=unicodedata.normalize('NFC',prefix+body+suffix)
        if TOK.findall(vi)!=TOK.findall(src):
            raise ValueError((segment,index,'Control token order',TOK.findall(src),TOK.findall(vi)))
        if vi.count('▼')>3:
            raise ValueError((segment,index,'Too many line breaks'))
        if any(len(TOK.sub('',line))>34 for line in vi.split('▼')):
            raise ValueError((segment,index,'Line too long',vi))
        if any(c in vi for c in '\r\n\t'):
            raise ValueError((segment,index,'Unsupported whitespace'))
        if row.get('vi') not in (None,'',vi):
            raise ValueError((segment,index,'Previous translation cannot be overwritten'))
        if not body.strip():raise ValueError((segment,index,'Empty translation'))
        row['vi']=vi
        updated.append(json.dumps(row,ensure_ascii=False,separators=(',',':'))+'\n')
        manual.append('\t'.join((row['id'],src,vi))+'\n')
    path.write_text(''.join(updated),'utf8')
    (ROOT/f'manual_{segment.replace(".","_")}.tsv').write_text(''.join(manual),'utf8')
    print('APPLIED',segment,len(rows))