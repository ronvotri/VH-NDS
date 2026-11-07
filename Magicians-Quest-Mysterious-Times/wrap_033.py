#!/usr/bin/env python3
"""Apply hand-authored Magician's Quest batch 033, preserve in-game tokens."""
from pathlib import Path
import re, json, unicodedata
ROOT=Path(__file__).resolve().parent
TOK=re.compile(r"\$\d+(?:'[-\d]+)*;")
LEAD=re.compile(r"^(?:\$(?:034|024|023|022|040)'(?:[-\d]+')*[-\d]+;)+")
TAIL=re.compile(r"(?:\$\d+(?:'[-\d]+)*;)+$")
VAR={'{N}':'$500;','{P}':'$515;','{LOC}':"$000'5;Điểm Hẹn Hò$000'1;"}

def vlen(txt):
    s=txt.replace('{N}', 'Người chơi').replace('{P}', 'Người ấy').replace('{LOC}','Điểm Hẹn Hò')
    return len(TOK.sub('',s))

def wrap(s, limit=32):
    words=s.split(); parts=[]; cur=''
    for word in words:
        trial=(cur+' '+word) if cur else word
        if cur and vlen(trial)>limit:
            parts.append(cur);cur=word
        else:cur=trial
    if cur:parts.append(cur)
    return '▼'.join(parts)

def process(segment, expected):
    fn=f'translation/04-thoai/talkfigs__0eng__data__{segment}.jsonl'
    rows=[json.loads(z) for z in (ROOT/fn).read_text('utf8').splitlines()]
    raw=(ROOT/f'vi_{segment.replace(".","_")}_raw.txt').read_text('utf8').splitlines()
    if len(rows)!=len(raw) or len(rows)!=expected:
        raise ValueError(f'{segment}: expected {expected}, got records={len(rows)} translations={len(raw)}')
    errors=[];out=[]
    for index,(row,src) in enumerate(zip(rows,raw),1):
        en=row['en'];m=LEAD.match(en);lead=m.group(0) if m else ''
        remain=en[len(lead):]
        # End control codes are action keys and leave page text unmodified.
        t=TAIL.search(remain);tail=t.group(0) if t else ''
        if '{' in src and any(v not in VAR for v in re.findall(r'\{[^{}]+\}',src)):
            errors.append((index,'unknown placeholder',src))
        vi=wrap(src)
        for var,token in VAR.items():vi=vi.replace(var,token)
        vi=unicodedata.normalize('NFC',lead+vi+tail)
        if TOK.findall(vi)!=TOK.findall(en):errors.append((index,'token mismatch',TOK.findall(en),TOK.findall(vi)))
        if vi.count('▼')>3:errors.append((index,'too many lines',vi.count('▼')+1,vi))
        if max(len(TOK.sub('',p)) for p in vi.split('▼'))>34:errors.append((index,'long line',vi))
        if any(c in vi for c in '\r\t\n'):errors.append((index,'bad whitespace',vi))
        if row.get('vi'):errors.append((index,'already translated',row.get('vi')))
        if row.get('max_utf8_bytes') and len(vi.encode('utf8'))>row['max_utf8_bytes']:errors.append((index,'too many bytes',vi))
        row['vi']=vi
        out.append(vi)
    if errors:
        print('ERRORS',segment,len(errors))
        for er in errors:print(er)
        raise SystemExit(1)
    (ROOT/fn).write_text(''.join(json.dumps(row,ensure_ascii=False,separators=(',',':'))+'\n' for row in rows),'utf8')
    (ROOT/f'vi_{segment.replace(".","_")}.txt').write_text('\n'.join(out)+'\n','utf8')
    return len(rows)

if __name__=='__main__':
    for seg,n in [('0029.004',120),('0029.005',68)]:
        print('PASS',seg,process(seg,n))