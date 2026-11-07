#!/usr/bin/env python3
"""Manually translated NPC dialogue batch 034: preserve command tokens, wrap text."""
from pathlib import Path
import re, json, unicodedata
ROOT=Path(__file__).resolve().parent
TOKEN=re.compile(r"\$\d+(?:'[-\d]+)*;")
ANIMATION=re.compile(r"^(?:(?:\$(?:034|024|023|022|040)'[-\d]+(?:'[-\d]+)*;))+")

def visible(s):return len(TOKEN.sub('',s))

def wrap(raw, width=32):
    # Raw manual translations carry all non-animation tokens in their intended position.
    lines=[]; line=''
    for word in raw.strip().split():
        trial=(line+' '+word).strip() if line else word
        if line and visible(trial)>width:
            lines.append(line);line=word
        else:line=trial
    if line: lines.append(line)
    return '▼'.join(lines)

if __name__=='__main__':
    for n,expected in [('0030.001',120),('0030.002',120)]:
        path=ROOT/'translation'/'04-thoai'/f'talkfigs__0eng__data__{n}.jsonl'
        rows=[json.loads(x) for x in path.read_text('utf8').splitlines()]
        if all(r.get('vi') for r in rows):
            print(n,'already translated, skipping');continue
        raw=(ROOT/f'vi_{n.replace(".","_")}_raw.txt').read_text('utf8').splitlines()
        assert len(rows)==len(raw)==expected,(n,len(rows),len(raw))
        issues=[];wrapped=[]
        for i,(row,vi) in enumerate(zip(rows,raw),1):
            en=row['en'];lead=ANIMATION.match(en);lead=lead.group(0) if lead else ''
            out=unicodedata.normalize('NFC',lead+wrap(vi))
            if TOKEN.findall(en)!=TOKEN.findall(out):issues.append((i,'Token mismatch',TOKEN.findall(en),TOKEN.findall(out)))
            if out.count('▼')>3:issues.append((i,'More than 3 breaks',out))
            for line in out.split('▼'):
                if visible(line)>34:issues.append((i,'Line too long',visible(line),line))
            cap=row.get('max_utf8_bytes')
            if cap and len(out.encode())>cap:issues.append((i,'Byte limit',cap,len(out.encode())))
            if any(c in out for c in '\r\n\t'):issues.append((i,'Unexpected newline',out))
            if not vi.strip():issues.append((i,'Empty translation'))
            wrapped.append(out)
        print(n,'issues:',len(issues),'max_breaks:',max(x.count('▼') for x in wrapped),'max_visible:',max(visible(y) for x in wrapped for y in x.split('▼')))
        for v in issues[:100]:print(v)
        if issues: continue
        (ROOT/f'vi_{n.replace(".","_")}.txt').write_text('\n'.join(wrapped)+'\n',encoding='utf8')
        for row,vi in zip(rows,wrapped):row['vi']=vi
        path.write_text(''.join(json.dumps(row,ensure_ascii=False,separators=(',',':'))+'\n' for row in rows),encoding='utf8')
        (ROOT/f'manual_{n.replace(".","_")}.tsv').write_text('id\ten\tvi\n'+''.join(f"{x['id']}\t{x['en']}\t{x['vi']}\n" for x in rows),encoding='utf8')