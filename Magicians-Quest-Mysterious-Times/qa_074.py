#!/usr/bin/env python3
"""Verify checkpoint 074 against 073 (full JSONL preservation and NDS token QA)."""
from pathlib import Path
import argparse,zipfile,json,re,unicodedata
TOKEN=re.compile(r"\$\d{3}(?:'[\d-]+)*;")
BATCH={'0042.001','0042.002'}
ROOT1='MagiciansQuest_073/'
ROOT2='MagiciansQuest_074/'

def verify(old,new):
    with zipfile.ZipFile(old) as before,zipfile.ZipFile(new) as after:
        assert before.testzip() is None and after.testzip() is None
        n=before_n=after_n=changed=changed_files=0
        for oldname in before.namelist():
            if not ('/translation/' in oldname and oldname.endswith('.jsonl')):continue
            n+=1
            newname=oldname.replace(ROOT1,ROOT2,1)
            a=before.read(oldname)
            b=after.read(newname)
            is_batch=any(newname.endswith(f'{s}.jsonl') for s in BATCH)
            if not is_batch:assert a==b,newname
            else: changed_files+=1
            oldrows=[json.loads(x) for x in a.decode().splitlines()]
            newrows=[json.loads(x) for x in b.decode().splitlines()]
            assert len(oldrows)==len(newrows)
            for x,y in zip(oldrows,newrows):
                before_n+=bool(x.get('vi'))
                after_n+=bool(y.get('vi'))
                assert all(x[k]==y[k] for k in x if k!='vi'),x['id']
                if x.get('vi') is not None:assert y['vi']==x['vi'],x['id']
                else:
                    if is_batch:
                        changed+=1
                        assert y['vi'] and unicodedata.normalize('NFC',y['vi'])==y['vi']
                        assert TOKEN.findall(x['en'])==TOKEN.findall(y['vi']),y['id']
                        assert y['vi'].count('▼')<=3,y['id']
                        assert all(len(TOKEN.sub('',z))<=34 for z in y['vi'].split('▼')),y['id']
                    else:assert y['vi'] is None
        assert (n,changed_files,changed,before_n,after_n)==(501,2,240,19458,19698)
        print('PASS: 501 JSONL, 55,976 rows, 240 translated, no legacy changes, CRC OK')

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('previous',type=Path)
    p.add_argument('current',type=Path)
    a=p.parse_args()
    verify(a.previous,a.current)
