#!/usr/bin/env python3
"""Apply 240 hand-authored NPC translations, preserving control-token order and source metadata."""
import json,re,unicodedata,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
TOKEN=re.compile(r"\$\d+(?:'[-\d]+)*;")
PREFIX=re.compile(r"^(?:\$\d+(?:'[-\d]+)*;)+")
SUFFIX=re.compile(r"(?:\$\d+(?:'[-\d]+)*;)+$")

def softwrap(segment, limit=33):
    # Keep embedded control codes as indivisible tokens, count only glyphs.
    words=segment.split(' ')
    out=[]; cur=''
    for word in words:
        if word=='':continue
        trial=(cur+' '+word) if cur else word
        if len(TOKEN.sub('',trial))>limit and cur:
            out.append(cur);cur=word
        else:cur=trial
    if cur:out.append(cur)
    if any(len(TOKEN.sub('',x))>34 for x in out):
        raise ValueError(f'word too long {out}')
    return '▼'.join(out)

for segment in ('0022.005','0023.001'):
    p=ROOT/f'translation/04-thoai/talkfigs__0eng__data__{segment}.jsonl'
    rows=[json.loads(s) for s in p.read_text('utf8').splitlines()]
    lines=(ROOT/f'manual_{segment.replace(".","_")}.tsv').read_text('utf8').splitlines()
    assert len(rows)==len(lines)==120,(segment,len(rows),len(lines))
    result=[];errs=[]
    for i,(row,line) in enumerate(zip(rows,lines)):
        num,translated=line.split('\t',1)
        assert num==f'{i:03d}' and translated and translated==translated.strip(),(segment,i)
        en=row['en'];pre=PREFIX.match(en);suf=SUFFIX.search(en)
        front=pre.group() if pre else ''
        back=suf.group() if suf else ''
        # The entire English text is one prefix or suffix only in some edge cases.
        if front and len(front)==len(en):back=''
        parts=[softwrap(s) for s in translated.split('▼')]
        vi=unicodedata.normalize('NFC',front+(' ' if front.endswith('$515;') else '')+'▼'.join(parts)+back)
        coderef=TOKEN.findall(en);codevi=TOKEN.findall(vi)
        if coderef!=codevi:errs.append((i,'CONTROL',coderef,codevi))
        if vi.count('▼')>3:errs.append((i,'BREAKS',vi.count('▼'),vi))
        if any(len(TOKEN.sub('',s))>34 for s in vi.split('▼')):errs.append((i,'LONG',vi))
        if any(c in vi for c in '\n\r\t'):errs.append((i,'WHITESPACE',vi))
        if row.get('max_utf8_bytes') and len(vi.encode('utf8'))>row['max_utf8_bytes']:errs.append((i,'BYTES',len(vi.encode('utf8'))))
        if row['vi'] not in (None,'',vi):errs.append((i,'OVERWRITE',row['vi']))
        row['vi']=vi;result.append(row)
    if errs:
        print('FAIL',segment,'count',len(errs))
        for er in errs:print(er)
        sys.exit(1)
    p.write_text(''.join(json.dumps(row,ensure_ascii=False,separators=(',',':'))+'\n' for row in result),'utf8')
    print('TRANSLATED',segment,'120 pages')