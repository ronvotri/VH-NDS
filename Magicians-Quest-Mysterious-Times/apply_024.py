#!/usr/bin/env python3
"""Apply 240 individually translated Vietnamese NPC pages; preserve original control tokens."""
from pathlib import Path
import json,re,unicodedata
ROOT=Path(__file__).resolve().parent
TOK=re.compile(r"\$\d+(?:'[-\d]+)*;")
LEAD=re.compile(r"^(?:\$\d+(?:'[-\d]+)*;)+")
TAIL=re.compile(r"(?:\$\d+(?:'[-\d]+)*;)+$")

def wrap(body,limit=34):
    """Respect hand-set page lines; wrap further if a line exceeds text-width cap."""
    pieces=[]
    for part in body.split('▼'):
        cur=''
        for word in part.split():
            cand=(cur+' '+word).strip()
            if cur and len(TOK.sub('',cand))>limit:
                pieces.append(cur);cur=word
            else:cur=cand
        pieces.append(cur)
    return '▼'.join(pieces)

for seg,expected in [('0026.001',120),('0026.002',120)]:
    p=ROOT/f'translation/04-thoai/talkfigs__0eng__data__{seg}.jsonl'
    rows=[json.loads(s) for s in p.read_text('utf8').splitlines()]
    texts=(ROOT/f'vi_{seg.replace(".","_")}.txt').read_text('utf8').splitlines()
    assert len(rows)==len(texts)==expected,(seg,len(rows),len(texts))
    output=[];manual=[]
    for i,(row,body) in enumerate(zip(rows,texts),1):
        src=row['en']
        m=LEAD.match(src)
        prefix=m.group() if m else ''
        srcend=TAIL.search(src)
        suffix=srcend.group() if srcend and srcend.start()>len(prefix) else ''
        leading=TOK.findall(prefix)
        if leading and leading[-1] in body and leading[-1].startswith(('$500;', '$503', '$515;')):
            prefix=prefix[:-len(leading[-1])]
        vi=unicodedata.normalize('NFC',prefix+wrap(body)+suffix)
        if TOK.findall(vi)!=TOK.findall(src):
            raise AssertionError((seg,i,'token mismatch',TOK.findall(src),TOK.findall(vi),src,vi))
        if vi.count('▼')>3:
            raise AssertionError((seg,i,'page breaks',vi))
        for piece in vi.split('▼'):
            if len(TOK.sub('',piece))>34:
                raise AssertionError((seg,i,'long line',len(TOK.sub('',piece)),vi))
        if any(c in vi for c in '\r\n\t'):raise AssertionError((seg,i,'bad whitespace'))
        if row.get('vi') not in (None,'',vi):raise AssertionError((seg,i,'overwrite'))
        row['vi']=vi
        output.append(json.dumps(row,ensure_ascii=False,separators=(',',':'))+'\n')
        manual.append(row['id']+'\t'+row['en']+'\t'+vi+'\n')
    p.write_text(''.join(output),'utf8')
    (ROOT/f'manual_{seg.replace(".","_")}.tsv').write_text(''.join(manual),'utf8')
    print('Applied',seg,len(output))