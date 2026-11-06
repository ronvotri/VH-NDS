#!/usr/bin/env python3
"""Apply checkpoint 017 240 hand-reviewed lines; preserve source codes and metadata."""
from pathlib import Path
import json,re,unicodedata
ROOT=Path(__file__).resolve().parent
TOKEN=re.compile(r"\$\d+(?:'[-\d]+)*;")
FORMAT_PREFIX=re.compile(r"^(?:\$(?:024|023|022)(?:'[-\d]+)*;)+")

def softwrap(text,limit=33):
    # Respect explicitly supplied page breaks; never split control codes.
    out=[]
    for seg in text.split('▼'):
        cur=''
        for word in seg.split(' '):
            if not word:continue
            trial=f'{cur} {word}' if cur else word
            if cur and len(TOKEN.sub('',trial))>limit:
                out.append(cur);cur=word
            else:cur=trial
        if cur:out.append(cur)
    return '▼'.join(out)

for segment in ('0023.002','0023.003'):
    p=ROOT/f'translation/04-thoai/talkfigs__0eng__data__{segment}.jsonl'
    rows=[json.loads(s) for s in p.read_text('utf8').splitlines()]
    manual=ROOT/f'vi_{segment.replace(".","_")}.txt'
    translations=manual.read_text('utf8').splitlines()
    assert len(rows)==len(translations)==120,(segment,len(rows),len(translations))
    errors=[]
    for i,(row,text) in enumerate(zip(rows,translations)):
        en=row['en'];m=FORMAT_PREFIX.match(en)
        fmt=m.group() if m else ''
        assert row['vi'] in (None,''),(segment,i,'overwriting old VI')
        vi=unicodedata.normalize('NFC',fmt+softwrap(text))
        if TOKEN.findall(en)!=TOKEN.findall(vi):errors.append((i,'control',TOKEN.findall(en),TOKEN.findall(vi)))
        if vi.count('▼')>3:errors.append((i,'breaks',vi.count('▼'),vi))
        if any(len(TOKEN.sub('',line))>34 for line in vi.split('▼')):errors.append((i,'long',vi))
        if any(c in vi for c in '\t\r\n'):errors.append((i,'newline',vi))
        if vi!=unicodedata.normalize('NFC',vi):errors.append((i,'NFC',vi))
        if row.get('max_utf8_bytes') and len(vi.encode('utf8'))>row['max_utf8_bytes']:errors.append((i,'byte',vi))
        row['vi']=vi
    if errors:
        for e in errors[:100]:print('ERROR',segment,e)
        raise SystemExit('FAIL '+str(len(errors)))
    p.write_text(''.join(json.dumps(row,ensure_ascii=False,separators=(',',':'))+'\n' for row in rows),'utf8')
    print('TRANSLATED',segment,len(rows))