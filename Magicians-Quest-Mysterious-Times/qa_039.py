#!/usr/bin/env python3
"""Independent checkpoint 039 integrity QA against checkpoint 038."""
from __future__ import annotations
from pathlib import Path
import sys,re,json,zipfile,unicodedata
ROOT=Path(__file__).resolve().parent
BASE=Path(sys.argv[1] if len(sys.argv)>1 else '/mnt/data/MagiciansQuest-VietHoa-Checkpoint-038.zip')
BASE_ROOT='MagiciansQuest_038/'
TARGETS={'translation/04-thoai/talkfigs__0eng__data__0032.001.jsonl':120,
         'translation/04-thoai/talkfigs__0eng__data__0032.002.jsonl':120}
TOKEN=re.compile(r'\$\d{3}(?:\'[^;$]+)*;')
def parse(x): return [json.loads(line) for line in x.splitlines() if line.strip()]
with zipfile.ZipFile(BASE) as old:
    assert old.testzip() is None,'Baseline ZIP corrupt'
    prev=sorted(n[len(BASE_ROOT):] for n in old.namelist() if n.startswith(BASE_ROOT+'translation/') and n.endswith('.jsonl'))
    now=sorted(str(p.relative_to(ROOT)) for p in (ROOT/'translation').rglob('*.jsonl'))
    assert len(now)==len(prev)==501,(len(now),len(prev))
    assert now==prev,'Missing, added or renamed translation file'
    prior=total=changed=translated=0
    groups={}
    delta_expect={}
    for path in now:
        a=parse(old.read(BASE_ROOT+path).decode('utf-8'))
        b=parse((ROOT/path).read_text('utf-8'))
        assert len(a)==len(b),(path,len(a),len(b))
        if path in TARGETS: assert len(a)==TARGETS[path]
        group=path.split('/')[1]
        if group not in groups:groups[group]=[0,0]
        for idx,(x,y) in enumerate(zip(a,b),1):
            assert set(x)==set(y),(path,idx,'field inventory')
            assert all(x[k]==y[k] for k in x if k!='vi'),(path,idx,'non-vi modified')
            v=y.get('vi')
            if x.get('vi'):
                assert x==y,(path,idx,'prior translation overwritten')
                prior+=1
            elif v:
                assert path in TARGETS,(path,idx,'unexpected new translation')
                assert isinstance(v,str) and unicodedata.is_normalized('NFC',v),(path,idx,'unicode')
                assert TOKEN.findall(x['en'])==TOKEN.findall(v),(path,idx,'control code mismatch')
                assert not any(c in v for c in '\r\n\t'),(path,idx,'linebreaks')
                assert v.count('▼')<=3,(path,idx,'too many screen breaks')
                assert all(len(TOKEN.sub('',line))<=34 for line in v.split('▼')),(path,idx,'line width')
                if x.get('max_utf8_bytes') is not None:
                    assert len(v.encode('utf-8'))<=x['max_utf8_bytes'],(path,idx,'UTF-8 byte limit')
                changed+=1
                delta_expect[y['id']]=v
            translated+=bool(v);total+=1
            groups[group][0]+=1;groups[group][1]+=bool(v)
    assert (total,prior,changed,translated)==(55976,11269,240,11509),(total,prior,changed,translated)
    assert groups['04-thoai']==[52608,8384],groups
    ds=parse((ROOT/'DELTA-039.jsonl').read_text('utf-8'))
    assert len(ds)==240,len(ds)
    assert {d['id']:d['vi'] for d in ds}==delta_expect,'Delta file inconsistent'
    assert all(d.get('old_vi') is None for d in ds),'Delta overwrote prior translations'
    assert [d['file'] for d in ds].count('04-thoai/talkfigs__0eng__data__0032.001.jsonl')==120
    assert [d['file'] for d in ds].count('04-thoai/talkfigs__0eng__data__0032.002.jsonl')==120
print('PASS: all 501 JSONL files and 55,976 records checked against checkpoint 038.')
print('Added 240; old 11,269 unchanged. Total 11,509 (20.56%); NPC dialogues 8,384/52,608.')
print('PASS: IDs, source, context, field keys, control tokens, NFC, wrap and delta integrity.')
print('NOTE: ROM and in-game pixel/branch verification not performed.')