#!/usr/bin/env python3
"""Build Magician's Quest checkpoint 039 from manual translations, preserving exact source control tokens."""
from pathlib import Path
import re,json,unicodedata,csv
ROOT=Path(__file__).resolve().parent
SRCDIR=ROOT
TGT=['0032.001','0032.002']
TOKEN=re.compile(r'\$\d{3}(?:\'[^;$]+)*;')
PREFIX=re.compile(r'^(?:\$(?:022|023|024|034)(?:\'[^;$]+)*;)+')

def visible(st): return TOKEN.sub('',st)

def wrap_vi(s,limit=34):
    # Keep invisible control sequences untouched. Break between whole words, never inside a token.
    # Existing page separators are honored when supplied by the translator.
    segs=s.split('▼')
    output=[]
    for seg in segs:
        words=seg.split(' ')
        line=''
        for w in words:
            cand=(line+' '+w) if line else w
            if line and len(visible(cand))>limit:
                output.append(line)
                line=w
            else:line=cand
        output.append(line)
    return '▼'.join(output)

all_delta=[]
for suf in TGT:
    p=ROOT/'translation'/'04-thoai'/f'talkfigs__0eng__data__{suf}.jsonl'
    records=[json.loads(s) for s in p.read_text('utf-8').splitlines() if s]
    raw=(SRCDIR/f'vi_{suf.replace(".","_")}_source.txt').read_text('utf-8').splitlines()
    assert len(records)==len(raw)==120,(suf,len(records),len(raw))
    vi=[];outrows=[]
    for i,(record,entry) in enumerate(zip(records,raw),1):
        num,divider,translation=entry.partition('|')
        assert divider and int(num)==i,(suf,i,entry)
        en=record['en']
        prefix=PREFIX.match(en)
        translated=unicodedata.normalize('NFC',(prefix.group(0) if prefix else '')+wrap_vi(translation.strip()))
        assert not record.get('vi') or record['vi']==translated,(suf,i,'conflicting translation')
        tokens_en=TOKEN.findall(en)
        tokens_vi=TOKEN.findall(translated)
        if tokens_vi!=tokens_en:
            print('BAD TOKENS',suf,i,'EN',tokens_en,'VI',tokens_vi)
        if any(len(visible(line))>34 for line in translated.split('▼')):
            print('BAD WIDTH',suf,i,translated,[(len(visible(line)),line) for line in translated.split('▼')])
        if translated.count('▼')>3:
            print('BAD BREAKS',suf,i,translated)
        if '▼' in en and en.count('▼')>=3 and translated.count('▼')>3:print('BREAK ISSUE',i)
        if len(visible(translated))>34*4:print('POTENTIAL OVER',suf,i)
        vi.append(translated)
        record['vi']=translated
        all_delta.append({'file':'04-thoai/'+p.name,'id':record['id'],'en':en,'old_vi':None,'vi':translated,'ctx':record.get('ctx')})
        outrows.append(record)
    p.write_text('\n'.join(json.dumps(r,ensure_ascii=False,separators=(',',':')) for r in outrows)+'\n','utf-8')
    (ROOT/f'vi_{suf.replace(".","_")}.txt').write_text('\n'.join(vi)+'\n','utf-8')
    (ROOT/f'vi_{suf.replace(".","_")}_raw.txt').write_text('\n'.join(x.partition('|')[2] for x in raw)+'\n','utf-8')
    with (ROOT/f'manual_{suf.replace(".","_")}.tsv').open('w',encoding='utf-8',newline='') as fp:
        w=csv.writer(fp,delimiter='\t');w.writerow(['index','id','en','vi','ctx']);w.writerows([[idx+1,r['id'],r['en'],r['vi'],r.get('ctx','')] for idx,r in enumerate(outrows)])
    print('WRITTEN',suf,'rows',len(outrows),'breaks',sum(x.count('▼') for x in vi))
(ROOT/'DELTA-039.jsonl').write_text('\n'.join(json.dumps(d,ensure_ascii=False,separators=(',',':')) for d in all_delta)+'\n','utf-8')