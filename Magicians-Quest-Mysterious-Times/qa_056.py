#!/usr/bin/env python3
"""Check 056 ZIP against 055 ZIP (no claims about ROM runtime)."""
from pathlib import Path
from zipfile import ZipFile
import json,re,sys,unicodedata
z1=Path(sys.argv[1] if len(sys.argv)>1 else '/mnt/data/MagiciansQuest-VietHoa-Checkpoint-055.zip')
z2=Path(sys.argv[2] if len(sys.argv)>2 else '/mnt/data/MagiciansQuest-VietHoa-Checkpoint-056.zip')
pat=re.compile(r"\$\d{3}(?:'[0-9-]+)*;")
def data(z):
    return {n.split('/translation/',1)[1]:z.read(n) for n in z.namelist() if '/translation/' in n and n.endswith('.jsonl')}
def parsed(b):return [json.loads(x) for x in b.decode('utf-8').splitlines() if x.strip()]
with ZipFile(z1) as a,ZipFile(z2) as b:
    assert a.testzip() is None and b.testzip() is None
    before=data(a);after=data(b)
    assert len(before)==len(after)==501 and before.keys()==after.keys()
    changes=[];nall=old_vi=new_vi=0
    for path,ba in before.items():
        bb=after[path]
        aa,rr=parsed(ba),parsed(bb)
        assert len(aa)==len(rr),(path,len(aa),len(rr))
        nall+=len(aa)
        if path not in ['04-thoai/talkfigs__0eng__data__0040.009.jsonl','04-thoai/talkfigs__0eng__data__0040.010.jsonl']:
            assert ba==bb, f'other file byte-different: {path}'
        for orig,now in zip(aa,rr):
            old_vi+=orig.get('vi') is not None
            new_vi+=now.get('vi') is not None
            assert list(orig)==list(now),path
            assert all(orig[k]==now[k] for k in orig if k!='vi'),(path,orig['id'])
            if orig.get('vi')!=now.get('vi'):
                assert ('0040.009' in path or '0040.010' in path) and orig.get('vi') is None and now.get('vi') is not None
                assert pat.findall(orig['en'])==pat.findall(now['vi']),(path,orig['id'],'token')
                assert now['vi']==unicodedata.normalize('NFC',now['vi'])
                assert not any(x in now['vi'] for x in ['\n','\r','\t'])
                segs=now['vi'].split('▼')
                assert len(segs)<=4 and all(len(pat.sub('',x))<=34 for x in segs)
                changes.append((path,now['id']))
    assert (nall,old_vi,new_vi,len(changes))==(55976,15312,15552,240),(nall,old_vi,new_vi,len(changes))
    assert len([x for x in changes if '0040.009' in x[0]])==120
    assert len([x for x in changes if '0040.010' in x[0]])==120
    print('QA PASS: 501 JSONL, 55,976 records, 15,312 old retained, 240 new, total 15,552; all control tokens / NFC / static widths preserved')
    print('ZIP files:',len(b.namelist()))
