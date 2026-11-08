#!/usr/bin/env python3
"""Validate entire 057 checkpoint against 056; static only, not a ROM play test."""
from pathlib import Path
from zipfile import ZipFile
import json,re,sys,unicodedata
OLD=Path(sys.argv[1] if len(sys.argv)>1 else '/mnt/data/MagiciansQuest-VietHoa-Checkpoint-056.zip')
NEW=Path(sys.argv[2] if len(sys.argv)>2 else '/mnt/data/MagiciansQuest-VietHoa-Checkpoint-057.zip')
TOKEN=re.compile(r"\$\d{3}(?:'[0-9-]+)*;")
TARGET={'04-thoai/talkfigs__0eng__data__0040.011.jsonl','04-thoai/talkfigs__0eng__data__0040.012.jsonl'}
def entries(z):return {n.split('/translation/',1)[1]:z.read(n) for n in z.namelist() if '/translation/' in n and n.endswith('.jsonl')}
def parse(b):return [json.loads(x) for x in b.decode('utf8').splitlines() if x.strip()]
with ZipFile(OLD) as a,ZipFile(NEW) as b:
    assert a.testzip() is None and b.testzip() is None
    before,after=entries(a),entries(b)
    assert before.keys()==after.keys() and len(before)==501
    counts={k:0 for k in TARGET}
    total=oldvi=newvi=0
    for key,raw in before.items():
        newraw=after[key]
        rr,xx=parse(raw),parse(newraw)
        assert len(rr)==len(xx),(key,len(rr),len(xx))
        total+=len(rr)
        if key not in TARGET:assert raw==newraw,('non-target file changed',key)
        for r,x in zip(rr,xx):
            oldvi+=r.get('vi') is not None
            newvi+=x.get('vi') is not None
            assert list(r)==list(x),('schema',key,r['id'])
            assert all(r[t]==x[t] for t in r if t!='vi'),('record changed',key,r['id'])
            if r['vi']!=x['vi']:
                assert key in TARGET and r['vi'] is None and x['vi'],('unexpected change',key,r['id'])
                counts[key]+=1
                assert TOKEN.findall(r['en'])==TOKEN.findall(x['vi']),('tokens',key,r['id'])
                assert unicodedata.normalize('NFC',x['vi'])==x['vi'],('NFC',key,r['id'])
                assert not any(y in x['vi'] for y in ['\n','\r','\t']),('control char',key,r['id'])
                segments=x['vi'].split('▼')
                assert len(segments)<=4 and all(len(TOKEN.sub('',y))<=34 for y in segments),('width',key,r['id'])
    assert (total,oldvi,newvi,sum(counts.values()))==(55976,15552,15792,240)
    assert set(counts.values())=={120},counts
    print(f'QA PASS: {len(before)} JSONL; {total} records; 15552 old kept, +240 new -> 15792 total; tokens/width/NFC/CRC PASS; zip entries: {len(b.namelist())}')
