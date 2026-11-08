#!/usr/bin/env python3
"""Exhaustive checkpoint diff and static text controls check (064 -> 065)."""
import collections,json,re,sys,unicodedata,zipfile
OLD=sys.argv[1] if len(sys.argv)>1 else '/mnt/data/MagiciansQuest-VietHoa-Checkpoint-064.zip'
NEW=sys.argv[2] if len(sys.argv)>2 else '/mnt/data/MagiciansQuest-VietHoa-Checkpoint-065.zip'
TOKEN=re.compile(r"\$\d{3}(?:'[0-9-]+)*;")
TARGETS={f'translation/04-thoai/talkfigs__0eng__data__0041.{s}.jsonl' for s in ('005','006')}
with zipfile.ZipFile(OLD) as a,zipfile.ZipFile(NEW) as b:
    assert a.testzip() is None and b.testzip() is None,'zip CRC'
    old={p.split('/',1)[1]:a.read(p) for p in a.namelist() if not p.endswith('/')}
    new={p.split('/',1)[1]:b.read(p) for p in b.namelist() if not p.endswith('/')}
    paths=sorted(p for p in old if p.startswith('translation/') and p.endswith('.jsonl'))
    assert len(paths)==501,len(paths)
    before=after=total=changed=0; counts=collections.Counter()
    for p in paths:
        assert p in new,p
        ra=[json.loads(x) for x in old[p].decode('utf-8').splitlines()]
        rb=[json.loads(x) for x in new[p].decode('utf-8').splitlines()]
        assert len(ra)==len(rb),(p,'records count')
        total+=len(ra)
        for x,y in zip(ra,rb):
            before+=x['vi'] is not None;after+=y['vi'] is not None
            assert {k:v for k,v in x.items() if k!='vi'}=={k:v for k,v in y.items() if k!='vi'},(p,x['id'],'metadata')
            if x['vi']!=y['vi']:
                assert p in TARGETS and x['vi'] is None and isinstance(y['vi'],str) and y['vi'],(p,x['id'],'unexpected change')
                assert unicodedata.normalize('NFC',y['vi'])==y['vi'],(p,x['id'],'NFC')
                assert TOKEN.findall(x['en'])==TOKEN.findall(y['vi']),(p,x['id'],'token sequence')
                assert y['vi'].count('▼')<=3,(p,x['id'],'break count')
                assert all(len(TOKEN.sub('',seg))<=34 for seg in y['vi'].split('▼')),(p,x['id'],'width')
                assert all(x not in y['vi'] for x in '\r\n\t'),(p,y['id'],'newline/tab')
                changed+=1;counts[p]+=1
        if p not in TARGETS:assert old[p]==new[p],(p,'unexpected file change')
    assert (total,before,after,changed)==(55976,17412,17652,240),(total,before,after,changed)
    assert sorted(counts.values())==[120,120] and len(counts)==2,counts
    extras=['DELTA-065.jsonl','QA-065.md','CHECKPOINT-2026-11-08-DOT-65.md','manual_0041_005.tsv','manual_0041_006.tsv','build_065.py','qa_065.py','mq065_translate.py','vi_0041_005.txt','vi_0041_006.txt']
    for path in extras:assert path in new,path
    delta=[json.loads(x) for x in new['DELTA-065.jsonl'].decode('utf-8').splitlines()]
    assert len(delta)==240
    byid={r['id']:r for r in delta};assert len(byid)==240
    for p in TARGETS:
        for row in [json.loads(x) for x in new[p].decode('utf-8').splitlines()]:
            assert byid[row['id']]==row,(p,row['id'])
    print(f'QA PASS: {len(paths)} JSONLs / {total} records; {before} -> {after} translated; 240 new; 499 untouched JSONLs byte-identical; metadata, NDS tokens, NFC, width, delta and ZIP CRC PASS')
