#!/usr/bin/env python3
"""Rebuild Magician's Quest checkpoint 090 from checkpoint 089 and unique_090.tsv.

Usage:
  python build_090.py --previous MagiciansQuest-VietHoa-Checkpoint-089.zip --output MagiciansQuest-VietHoa-Checkpoint-090.zip
"""
from pathlib import Path
import json,re,csv,zipfile,unicodedata,argparse,hashlib
ROOT=Path(__file__).resolve().parent
PREFIX=re.compile(r"^(?:\$(?:024|023|022|034|040|004)(?:'[-\d]+)*;)+")
TOKEN=re.compile(r"\$\d{3}(?:'[-\d]+)*;")
OLD='MagiciansQuest_089/'
NEW='MagiciansQuest_090/'
TARGET=('0043.010','0043.011')
ADDED=('README.md','BAN_GIAO.md','QA-090.md','CHECKPOINT-2026-11-10-DOT-90.md',
       'DELTA-090.jsonl','unique_090.tsv','build_090.py',
       'manual_0043_010.tsv','manual_0043_011.tsv','vi_0043_010.txt','vi_0043_011.txt')

def run(before:Path, output:Path):
    with (ROOT/'unique_090.tsv').open(encoding='utf-8',newline='') as f:
        mapping={r['en_body']:r['vi_body'] for r in csv.DictReader(f,delimiter='\t')}
    assert len(mapping)==48
    with zipfile.ZipFile(before) as z:
        assert z.testzip() is None
        items={n.replace(OLD,NEW,1):z.read(n) for n in z.namelist()}
    assert len(items)==1348
    allnew=[]
    for key in TARGET:
        path=NEW+'translation/04-thoai/talkfigs__0eng__data__'+key+'.jsonl'
        rows=[json.loads(l) for l in items[path].decode('utf-8').splitlines()]
        assert len(rows)==120 and all(r['vi'] is None for r in rows)
        for r in rows:
            body=PREFIX.sub('',r['en'])
            assert body in mapping
            prefix=r['en'][:len(r['en'])-len(body)]
            r['vi']=prefix+mapping[body]
            assert TOKEN.findall(r['en'])==TOKEN.findall(r['vi']), r['id']
            assert r['vi']==unicodedata.normalize('NFC',r['vi'])
            assert mapping[body].count('▼')<=3
            assert all(len(TOKEN.sub('',seg))<=34 for seg in mapping[body].split('▼'))
        allnew.extend(rows)
        items[path]=''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in rows).encode('utf-8')
    assert len(allnew)==240
    for n in ADDED:
        items[NEW+n]=(ROOT/n).read_bytes()
    output.parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(output,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=7) as z:
        for path in sorted(items):
            z.writestr(path,items[path])
    with zipfile.ZipFile(output) as z:
        assert z.testzip() is None
        assert len(z.namelist())==len(set(z.namelist()))==len(items)==1357
        translation_paths=[p for p in z.namelist() if '/translation/' in p and p.endswith('.jsonl')]
        assert len(translation_paths)==501
        count=done=0
        for p in translation_paths:
            for line in z.read(p).decode('utf-8').splitlines():
                r=json.loads(line)
                count+=1;done+=r['vi'] is not None
        assert count==55976 and done==23529,(count,done)
    print('BUILT',output,output.stat().st_size,'bytes','entries',len(items),'translated',done,'/',count)

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--previous',required=True,type=Path)
    p.add_argument('--output',required=True,type=Path)
    args=p.parse_args()
    run(args.previous,args.output)