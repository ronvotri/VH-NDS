#!/usr/bin/env python3
"""Audit all translation records checkpoint 060→061, tokens, structure and archive integrity."""
import collections,json,re,sys,unicodedata,zipfile
OLD=sys.argv[1] if len(sys.argv)>1 else '/mnt/data/MagiciansQuest-VietHoa-Checkpoint-060.zip'
NEW=sys.argv[2] if len(sys.argv)>2 else '/mnt/data/MagiciansQuest-VietHoa-Checkpoint-061.zip'
TOKEN=re.compile(r"\$\d{3}(?:'[0-9-]+)*;")
with zipfile.ZipFile(OLD) as a,zipfile.ZipFile(NEW) as b:
    assert a.testzip() is None and b.testzip() is None
    old={n.split('/',1)[1]:a.read(n) for n in a.namelist() if not n.endswith('/')}
    new={n.split('/',1)[1]:b.read(n) for n in b.namelist() if not n.endswith('/')}
    paths=sorted(p for p in old if p.startswith('translation/') and p.endswith('.jsonl'))
    assert len(paths)==501,len(paths)
    targets={f'translation/04-thoai/talkfigs__0eng__data__0040.{i:03d}.jsonl' for i in (19,20)}
    total=before=after=count=0;changed=collections.Counter()
    for p in paths:
        assert p in new,p
        previous=[json.loads(x) for x in old[p].decode().splitlines()]
        current=[json.loads(x) for x in new[p].decode().splitlines()]
        assert len(previous)==len(current),(p,'row count')
        total+=len(previous)
        before+=sum(r.get('vi') is not None for r in previous)
        after+=sum(r.get('vi') is not None for r in current)
        for x,y in zip(previous,current):
            assert {k:v for k,v in x.items() if k!='vi'}=={k:v for k,v in y.items() if k!='vi'},(p,x['id'],'source mutated')
            if x.get('vi')!=y.get('vi'):
                assert p in targets and x.get('vi') is None and isinstance(y.get('vi'),str) and y['vi'],(p,x['id'],'unexpected change')
                assert TOKEN.findall(x['en'])==TOKEN.findall(y['vi']),(p,x['id'],'TOKENS')
                assert unicodedata.normalize('NFC',y['vi'])==y['vi'],(p,x['id'],'NFC')
                assert not any(c in y['vi'] for c in '\r\n\t'),(p,x['id'],'LINE CONTROL')
                assert y['vi'].count('▼')<=3,(p,x['id'],'BREAKS')
                assert all(len(TOKEN.sub('',piece))<=34 for piece in y['vi'].split('▼')),(p,x['id'],'WIDTH')
                count+=1;changed[p]+=1
        if p not in targets:assert old[p]==new[p],(p,'byte mismatch')
    assert (total,before,after,count)==(55976,16512,16752,240),(total,before,after,count)
    assert len(changed)==2 and sorted(changed.values())==[120,120],changed
    for name in ['DELTA-061.jsonl','QA-061.md','CHECKPOINT-2026-11-08-DOT-61.md','manual_0040_019.tsv','manual_0040_020.tsv','build_061.py','qa_061.py','vi_0040_019.txt','vi_0040_020.txt']:
        assert name in new,name
    delta=[json.loads(x) for x in new['DELTA-061.jsonl'].decode().splitlines()]
    assert len(delta)==240
    assert all(x['vi']==next(y['vi'] for p in targets for y in (json.loads(t) for t in new[p].decode().splitlines()) if y['id']==x['id']) for x in delta)
    print(f'QA PASS: {len(paths)} JSONL; {total} records; {before}->{after} translated; exactly {count} new; all tokens/NFC/width PASS; 499 other JSONL byte-identical; ZIP CRC PASS')
