#!/usr/bin/env python3
"""QA checkpoint 041 vs complete checkpoint 040: only 240 new vi allowed."""
from pathlib import Path
from collections import Counter
import json,re,sys,zipfile,unicodedata
BASE=Path(__file__).resolve().parent
TOKEN=re.compile(r"\$[0-9'\-]+;")
TARGET={'talkfigs__0eng__data__0032.005.jsonl':120,'talkfigs__0eng__data__0033.001.jsonl':120}
def audit(source):
    paths=sorted((BASE/'translation').rglob('*.jsonl'))
    assert len(paths)==501,('count source files',len(paths))
    old_total=new_total=old_done=new_done=changed=npc_done=npc_total=0
    for p in paths:
        rel=p.relative_to(BASE).as_posix()
        old=[json.loads(x) for x in source.read('MagiciansQuest_040/'+rel).decode('utf-8').splitlines()]
        new=[json.loads(x) for x in p.read_text('utf-8').splitlines()]
        assert len(old)==len(new),(rel,'record mismatch')
        old_total+=len(old);new_total+=len(new)
        for i,(a,b) in enumerate(zip(old,new),1):
            old_done+=bool(a.get('vi'));new_done+=bool(b.get('vi'))
            if '04-thoai/' in rel:npc_total+=1;npc_done+=bool(b.get('vi'))
            if p.name not in TARGET:
                assert a==b,(rel,i,'unintended edit')
                continue
            assert len(old)==TARGET[p.name],(rel,'unexpected file size')
            assert not a.get('vi'),(rel,i,'source already translated')
            assert set(a)==set(b),(rel,i,'field changed')
            assert {k:v for k,v in a.items() if k!='vi'}=={k:v for k,v in b.items() if k!='vi'},(rel,i,'source changed')
            v=b.get('vi')
            assert isinstance(v,str) and v.strip(),(rel,i,'missing vi')
            assert TOKEN.findall(a['en'])==TOKEN.findall(v),(rel,i,'token changed')
            assert unicodedata.normalize('NFC',v)==v,(rel,i,'Unicode not NFC')
            assert not any(q in v for q in '\r\n\t'),(rel,i,'unexpected control char')
            assert v.count('▼')<=3,(rel,i,'too many line breaks')
            assert all(len(TOKEN.sub('',ln))<=34 for ln in v.split('▼')),(rel,i,'overflow line')
            if b.get('max_utf8_bytes'):
                assert len(v.encode('utf-8'))<=b['max_utf8_bytes'],(rel,i,'over byte limit')
            changed+=1
    assert (old_total,new_total)==(55976,55976),(old_total,new_total)
    assert old_done==11749,old_done
    assert new_done==11989,new_done
    assert changed==240,changed
    assert (npc_total,npc_done)==(52608,8864),(npc_total,npc_done)
    print(f'QA PASS: {len(paths)} JSONL, {new_total:,} records; {changed} new vi; {old_done:,} prior vi untouched.')
    print(f'Progress: {new_done:,}/{new_total:,} ({new_done/new_total*100:.2f}%), NPC {npc_done:,}/{npc_total:,}.')
    return {'files':len(paths),'records':new_total,'added':changed,'translated':new_done,'npc':npc_done}
if __name__=='__main__':
    src=Path(sys.argv[1]) if len(sys.argv)>1 else Path('/mnt/data/MagiciansQuest-VietHoa-Checkpoint-040.zip')
    with zipfile.ZipFile(src) as z:audit(z)