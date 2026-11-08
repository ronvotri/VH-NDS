#!/usr/bin/env python3
"""Verify Magician's Quest checkpoint 063 (complete ZIP) against checkpoint 062."""
import collections, json, re, sys, unicodedata, zipfile
OLD=sys.argv[1] if len(sys.argv)>1 else '/mnt/data/MagiciansQuest-VietHoa-Checkpoint-062.zip'
NEW=sys.argv[2] if len(sys.argv)>2 else '/mnt/data/MagiciansQuest-VietHoa-Checkpoint-063.zip'
TOKEN=re.compile(r"\$\d{3}(?:'[0-9-]+)*;")
targets={f'translation/04-thoai/talkfigs__0eng__data__0041.{n}.jsonl' for n in ('001','002')}
with zipfile.ZipFile(OLD) as a,zipfile.ZipFile(NEW) as b:
    assert a.testzip() is None and b.testzip() is None
    old={n.split('/',1)[1]:a.read(n) for n in a.namelist() if not n.endswith('/')}
    new={n.split('/',1)[1]:b.read(n) for n in b.namelist() if not n.endswith('/')}
    paths=sorted(p for p in old if p.startswith('translation/') and p.endswith('.jsonl'))
    assert len(paths)==501,len(paths)
    total=before=after=count=0
    changed=collections.Counter()
    for p in paths:
        assert p in new,p
        ra=[json.loads(x) for x in old[p].decode().splitlines()]
        rb=[json.loads(x) for x in new[p].decode().splitlines()]
        assert len(ra)==len(rb),(p,'row count')
        total+=len(ra)
        before+=sum(r['vi'] is not None for r in ra)
        after+=sum(r['vi'] is not None for r in rb)
        for x,y in zip(ra,rb):
            assert {k:v for k,v in x.items() if k!='vi'}=={k:v for k,v in y.items() if k!='vi'},(p,x['id'],'metadata changed')
            if x['vi']!=y['vi']:
                assert p in targets and x['vi'] is None and isinstance(y['vi'],str) and y['vi'],(p,x['id'],'unexpected change')
                assert TOKEN.findall(x['en'])==TOKEN.findall(y['vi']),(p,x['id'],'tokens')
                assert unicodedata.normalize('NFC',y['vi'])==y['vi'],(p,x['id'],'NFC')
                assert not any(c in y['vi'] for c in '\r\n\t'),(p,x['id'],'newline/tab')
                assert y['vi'].count('▼')<=3,(p,x['id'],'breaks')
                assert all(len(TOKEN.sub('',segment))<=34 for segment in y['vi'].split('▼')),(p,x['id'],'width')
                count+=1; changed[p]+=1
        if p not in targets: assert old[p]==new[p],(p,'unrelated file modified')
    assert (total,before,after,count)==(55976,16932,17172,240),(total,before,after,count)
    assert sorted(changed.values())==[120,120] and len(changed)==2,changed
    extras=['DELTA-063.jsonl','QA-063.md','CHECKPOINT-2026-11-08-DOT-63.md','manual_0041_001.tsv','manual_0041_002.tsv','build_063.py','qa_063.py','vi_0041_001.txt','vi_0041_002.txt']
    for e in extras:assert e in new,e
    delta=[json.loads(x) for x in new['DELTA-063.jsonl'].decode().splitlines()]
    assert len(delta)==240
    idx={r['id']:r for r in delta}
    assert len(idx)==240
    for p in targets:
        for line in new[p].decode().splitlines():
            rec=json.loads(line)
            assert idx[rec['id']]==rec,rec['id']
    print(f'QA PASS: {len(paths)} JSONLs; {total} records; {before} -> {after} translated; 240 newly translated; 499 other JSONLs byte-identical, tokens, NFC, line length, IDs and ZIP CRC PASS')
