#!/usr/bin/env python3
"""Checkpoint 022: map Vietnamese hand translations onto source JSONL, preserving control codes."""
from pathlib import Path
import json, re, unicodedata
ROOT=Path(__file__).resolve().parent
TOK=re.compile(r"\$\d+(?:'[-\d]+)*;")
LEAD=re.compile(r"^(?:\$\d+(?:'[-\d]+)*;)+")
TAIL=re.compile(r"(?:\$\d+(?:'[-\d]+)*;)+$")

def wrap(s,cap=34):
    parts=[]; cur=''
    for word in s.split():
        cand=(cur+' '+word).strip()
        if cur and len(TOK.sub('',cand))>cap:
            parts.append(cur); cur=word
        else: cur=cand
    if cur:parts.append(cur)
    return '▼'.join(parts)

for seg,expected in [('0025.002',120),('0025.003',120)]:
    p=ROOT/f'translation/04-thoai/talkfigs__0eng__data__{seg}.jsonl'
    rows=[json.loads(s) for s in p.read_text('utf8').splitlines()]
    texts=(ROOT/f'vi_{seg.replace(".","_")}.txt').read_text('utf8').splitlines()
    assert len(rows)==len(texts)==expected,(seg,len(rows),len(texts))
    output=[]; manual=[]
    for i,(row,body) in enumerate(zip(rows,texts),1):
        src=row['en']
        m=LEAD.match(src)
        prefix=m.group() if m else ''
        srcend=TAIL.search(src)
        suffix=srcend.group() if srcend and srcend.start()>len(prefix) else ''
        # The source may place a player/NPC name at sentence start as part of
        # the leading token run. If translated in a different word position,
        # move the *same* source token rather than copying it twice.
        leading=TOK.findall(prefix)
        if leading and leading[-1] in body and leading[-1].startswith(('$500;', '$503')):
            prefix=prefix[:-len(leading[-1])]
        vi=unicodedata.normalize('NFC',prefix+wrap(body)+suffix)
        if TOK.findall(vi)!=TOK.findall(src):
            raise AssertionError((seg,i,'control tokens',TOK.findall(src),TOK.findall(vi),src,vi))
        assert vi.count('▼')<=3,(seg,i,'page breaks',vi)
        assert all(len(TOK.sub('',part))<=34 for part in vi.split('▼')),(seg,i,'length',vi)
        assert not any(x in vi for x in '\r\n\t'),(seg,i,'whitespace')
        assert row.get('vi') in (None,'',vi),(seg,i,'overwrite')
        row['vi']=vi
        output.append(json.dumps(row,ensure_ascii=False,separators=(',',':'))+'\n')
        manual.append(row['id']+'\t'+row['en']+'\t'+vi+'\n')
    p.write_text(''.join(output),'utf8')
    (ROOT/f'manual_{seg.replace(".","_")}.tsv').write_text(''.join(manual),'utf8')
    print('Applied',seg,len(output))