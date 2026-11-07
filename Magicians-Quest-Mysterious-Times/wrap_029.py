#!/usr/bin/env python3
"""Word-wrap the authored Vietnamese lines for the NDS dialog constraints.
All content is authored in vi_*_raw.txt; this helper only inserts page separators.
"""
from pathlib import Path
import re,unicodedata
ROOT=Path(__file__).resolve().parent
TOK=re.compile(r"\$\d+(?:'[-\d]+)*;")

def wrap(s,width):
    lines=['']
    for word in s.split(' '):
        if not word:continue
        curr=lines[-1]
        candidate=curr+' '+word if curr else word
        if len(TOK.sub('',candidate))<=width:
            lines[-1]=candidate
        else:
            if len(TOK.sub('',word))>width:
                raise ValueError(('too long single word',word))
            lines.append(word)
    return lines

for seg,n in [('0028_001',120),('0028_002',120)]:
    raw=(ROOT/f'vi_{seg}_raw.txt').read_text('utf8').splitlines()
    assert len(raw)==n,(seg,len(raw))
    finished=[]
    for ix,s in enumerate(raw):
        s=unicodedata.normalize('NFC',s.strip())
        lines=wrap(s,32)
        if len(lines)>4:lines=wrap(s,34)
        if len(lines)>4:raise ValueError((seg,ix,len(lines),lines))
        assert max(len(TOK.sub('',x)) for x in lines)<=34
        finished.append('▼'.join(lines))
    (ROOT/f'vi_{seg}.txt').write_text('\n'.join(finished)+'\n','utf8')
    print('WRAPPED',seg,len(finished),'pages of 4 lines:',sum(x.count('▼')==3 for x in finished),'max visible',max(len(TOK.sub('',p)) for v in finished for p in v.split('▼')))