#!/usr/bin/env python3
"""Apply exactly two hand-written 037 translation batches; leave all other fields intact."""
from pathlib import Path
import json, re, unicodedata
ROOT = Path(__file__).resolve().parent
TGT = ROOT/'translation'/'04-thoai'
TOKEN = re.compile(r"\$\d+(?:'\d+)*;")
PREFIX = re.compile(r"^(?:\$\d+(?:'\d+)*;)+")
SUFFIX = re.compile(r"(?:\$\d+(?:'\d+)*;)+$")

def merge(en: str, human: str) -> str:
    human=unicodedata.normalize('NFC',human)
    a=PREFIX.match(en)
    prefix=a.group() if a else ''
    remainder=en[len(prefix):]
    b=SUFFIX.search(remainder)
    suffix=b.group() if b else ''
    text_source=remainder[:-len(suffix)] if suffix else remainder
    assert TOKEN.findall(text_source)==TOKEN.findall(human), (en,human)
    result=prefix+human+suffix
    assert TOKEN.findall(result)==TOKEN.findall(en), (en,result)
    assert result.count('▼')<=3
    assert all(len(TOKEN.sub('',line))<=34 for line in human.split('▼'))
    assert result==unicodedata.normalize('NFC',result)
    assert not re.search(r'[\n\r\t]',result)
    return result

for suff in ('0031.002','0031.003'):
    source=TGT/f'talkfigs__0eng__data__{suff}.jsonl'
    lines=[json.loads(line) for line in source.read_text(encoding='utf-8').splitlines() if line.strip()]
    target=ROOT/f'vi_{suff.replace(".","_")}_raw.txt'
    human=target.read_text(encoding='utf-8').splitlines()
    assert len(lines)==len(human)==120
    for r,t in zip(lines,human):
        assert r['vi'] is None, (suff,r['id'],r['vi'])
        r['vi']=merge(r['en'],t)
        if 'max_utf8_bytes' in r and r['max_utf8_bytes'] is not None:
            assert len(r['vi'].encode('utf-8'))<=int(r['max_utf8_bytes'])
    with source.open('w',encoding='utf-8',newline='\n') as f:
        for r in lines:f.write(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n')
    (ROOT/f'vi_{suff.replace(".","_")}.txt').write_text('\n'.join([r['vi'] for r in lines])+'\n',encoding='utf-8')
    import csv
    with (ROOT/f'manual_{suff.replace(".","_")}.tsv').open('w',encoding='utf-8',newline='') as f:
        wr=csv.writer(f,delimiter='\t');wr.writerow(('index','id','ctx','EN','VI'))
        for i,r in enumerate(lines,1):wr.writerow((i,r['id'],r.get('ctx',''),r['en'],r['vi']))
    print(suff,'translated',len(lines))