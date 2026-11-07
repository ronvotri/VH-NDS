#!/usr/bin/env python3
"""Translate batch 053 from manual Vietnamese lines without changing source fields."""
from pathlib import Path
import json,re,unicodedata
ROOT=Path(__file__).resolve().parent
TOKEN=re.compile(r'\$[^;]*;')
CONTROL_PREFIX=re.compile(r'\$(?:024|023|022|034|040)(?:[\'0-9-]+)*;')

def visible(s):return len(TOKEN.sub('',s))

def wrap(text,width=34):
    segments=text.split('▼'); lines=[]
    for segment in segments:
        words=segment.split(' ')
        cur=''
        for word in words:
            if not word: continue
            proposal=(cur+' '+word) if cur else word
            if visible(proposal)>width and cur:
                lines.append(cur);cur=word
            else:cur=proposal
            if visible(cur)>width:raise ValueError('Long indivisible token '+str((cur,visible(cur))))
        if cur:lines.append(cur)
    if len(lines)>4:raise ValueError('Too many visual lines: '+str((len(lines),text,lines)))
    return '▼'.join(lines)

for suffix in ('0040.003','0040.004'):
    p=ROOT/'translation/04-thoai'/f'talkfigs__0eng__data__{suffix}.jsonl'
    raw=(ROOT/f'vi_{suffix.replace(".","_")}_raw.txt').read_text(encoding='utf8').splitlines()
    src=[json.loads(s) for s in p.read_text(encoding='utf8').splitlines() if s.strip()]
    assert len(src)==len(raw)==120
    out=[]
    for i,(rec,translation) in enumerate(zip(src,raw),1):
        en=rec['en']
        try:
            tail=en;leading=''
            while m:=CONTROL_PREFIX.match(tail):
                leading+=m.group();tail=tail[m.end():]
            codes=TOKEN.findall(tail)
            if translation.count('¤')!=len(codes):raise ValueError('Token count mismatch')
            for code in codes:translation=translation.replace('¤',code,1)
            vi=leading+wrap(translation)
            vi=unicodedata.normalize('NFC',vi)
            if TOKEN.findall(en)!=TOKEN.findall(vi):raise ValueError('Token order mismatch')
            if max(map(visible,vi.split('▼')))>34:raise ValueError('Over width')
            if rec.get('vi') not in (None,'',vi):raise ValueError('Existing translation differs; refuse to overwrite')
            rec['vi']=vi;out.append(rec)
        except Exception as e:
            raise ValueError(f'{suffix} item {i}: {e}\nEnglish: {en}\nVietnamese: {translation}') from e
    p.write_text('\n'.join(json.dumps(rec,ensure_ascii=False,separators=(',',':')) for rec in out)+'\n',encoding='utf8')
    (ROOT/f'vi_{suffix.replace(".","_")}.txt').write_text('\n'.join(x['vi'] for x in out)+'\n',encoding='utf8')
    (ROOT/f'manual_{suffix.replace(".","_")}.tsv').write_text('id\ten\tvi\tctx\n'+ '\n'.join('\t'.join(str(x.get(k) or '') for k in ['id','en','vi','ctx']) for x in out)+'\n',encoding='utf8')
    print(suffix,'saved',len(out),'pages; longest:',max(max(map(visible,x['vi'].split('▼'))) for x in out))