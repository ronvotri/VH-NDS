#!/usr/bin/env python3
"""Compare all Magician's Quest checkpoint 044 records with checkpoint 043."""
import json,re,sys,unicodedata,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent
TOKEN=re.compile(r"\$[0-9'\-]+;")
TARGET={'talkfigs__0eng__data__0033.006.jsonl','talkfigs__0eng__data__0033.007.jsonl'}

def run(source):
    paths=sorted((ROOT/'translation').rglob('*.jsonl'))
    assert len(paths)==501,len(paths)
    old_total=new_total=old_done=new_done=added=npc_total=npc_done=0
    with zipfile.ZipFile(source) as arc:
        for p in paths:
            rel=p.relative_to(ROOT).as_posix()
            name='MagiciansQuest_043/'+rel
            old_raw=arc.read(name)
            new_raw=p.read_bytes()
            if p.name not in TARGET:
                assert old_raw==new_raw,(rel,'old file bytes changed')
            before=[json.loads(s) for s in old_raw.decode('utf8').splitlines()]
            after=[json.loads(s) for s in new_raw.decode('utf8').splitlines()]
            assert len(before)==len(after),(rel,'row count')
            for index,(o,n) in enumerate(zip(before,after),1):
                old_total+=1;new_total+=1
                old_done+=bool(o.get('vi'));new_done+=bool(n.get('vi'))
                if '04-thoai/' in rel:
                    npc_total+=1;npc_done+=bool(n.get('vi'))
                if p.name not in TARGET:continue
                assert set(o)==set(n),(rel,index,'keys changed')
                assert all(o[k]==n[k] for k in o if k!='vi'),(rel,index,'original changed')
                assert not o.get('vi'),(rel,index,'previously translated')
                vi=n.get('vi')
                assert isinstance(vi,str) and vi.strip(),(rel,index,'vi empty')
                assert TOKEN.findall(o['en'])==TOKEN.findall(vi),(rel,index,'codes mismatch',TOKEN.findall(o['en']),TOKEN.findall(vi))
                assert unicodedata.normalize('NFC',vi)==vi,(rel,index,'not NFC')
                assert not any(c in vi for c in '\t\r\n'),(rel,index,'line break')
                assert vi.count('▼')<=3,(rel,index,'too many breaks')
                assert all(len(TOKEN.sub('',v))<=34 for v in vi.split('▼')),(rel,index,'line too long')
                if o.get('max_utf8_bytes') is not None:
                    assert len(vi.encode('utf8'))<=int(o['max_utf8_bytes']),(rel,index,'byte limit')
                added+=1
    assert (old_total,new_total)==(55976,55976),(old_total,new_total)
    assert (old_done,new_done,added)==(12469,12709,240),(old_done,new_done,added)
    assert (npc_total,npc_done)==(52608,9584),(npc_total,npc_done)
    print('PASS: 501 JSONL / 55,976 records; 240 new Vietnamese lines; 12,469 old translations unchanged.')
    print('Progress: 12,709/55,976 (22.70%); NPC: 9,584/52,608.')

if __name__=='__main__':
    run(Path(sys.argv[1]) if len(sys.argv)>1 else Path('/mnt/data/MagiciansQuest-VietHoa-Checkpoint-043.zip'))