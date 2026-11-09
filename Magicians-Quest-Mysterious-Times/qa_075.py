#!/usr/bin/env python3
"""Validate checkpoint 075 against checkpoint 074, without running ROM emulator."""
from __future__ import annotations
import argparse,json,re,unicodedata,zipfile
from pathlib import Path
TOKEN=re.compile(r"\$\d{3}(?:'[-\d]+)*;")
OLD='MagiciansQuest_074/'
NEW='MagiciansQuest_075/'
BATCH=('0042.003','0042.004')
def verify(old:Path,new:Path):
    with zipfile.ZipFile(old) as za,zipfile.ZipFile(new) as zb:
        assert za.testzip() is None and zb.testzip() is None
        files=total=cnt_old=cnt_new=delta=affected=0
        for name in za.namelist():
            if not ('/translation/' in name and name.endswith('.jsonl')):continue
            files+=1
            updated=name.replace(OLD,NEW,1)
            raw_a=za.read(name);raw_b=zb.read(updated)
            active=any(name.endswith(f'{s}.jsonl') for s in BATCH)
            if active: affected+=1
            else:assert raw_a==raw_b,('Outside-batch change',name)
            a=[json.loads(x) for x in raw_a.decode().splitlines()]
            b=[json.loads(x) for x in raw_b.decode().splitlines()]
            assert len(a)==len(b)
            for x,y in zip(a,b):
                total+=1
                assert x.keys()==y.keys()
                assert all(x[k]==y[k] for k in x if k!='vi'),x['id']
                cnt_old+=x['vi'] is not None
                cnt_new+=y['vi'] is not None
                if x['vi'] is not None:assert x['vi']==y['vi']
                elif active:
                    delta+=1
                    assert y['vi'] and unicodedata.normalize('NFC',y['vi'])==y['vi']
                    assert TOKEN.findall(x['en'])==TOKEN.findall(y['vi']),y['id']
                    assert y['vi'].count('▼')<=3,y['id']
                    assert all(len(TOKEN.sub('',p))<=34 for p in y['vi'].split('▼')),y['id']
                else:assert y['vi'] is None
        assert (files,total,cnt_old,cnt_new,delta,affected)==(501,55976,19698,19938,240,2)
        print('PASS: 501 JSONL / 55,976 rows; 240 new VI; 19,698 old VI unchanged; token/NFC/line/CRC PASS')
if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('previous',nargs='?',type=Path,default=Path('/mnt/data/MagiciansQuest-VietHoa-Checkpoint-074.zip'))
    p.add_argument('current',nargs='?',type=Path,default=Path('/mnt/data/MagiciansQuest-VietHoa-Checkpoint-075.zip'))
    args=p.parse_args();verify(args.previous,args.current)
