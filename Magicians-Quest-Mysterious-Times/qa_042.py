#!/usr/bin/env python3
"""Validate checkpoint 042 against user-provided checkpoint 041 (no ROM required)."""
import json,re,sys,unicodedata,zipfile
from pathlib import Path
BASE=Path(__file__).resolve().parent
TOK=re.compile(r"\$[0-9'\-]+;")
TARGET={"talkfigs__0eng__data__0033.002.jsonl":120,"talkfigs__0eng__data__0033.003.jsonl":120}
def validate(z):
    files=sorted((BASE/'translation').rglob('*.jsonl'))
    assert len(files)==501,len(files)
    old_total=new_total=old_done=new_done=added=npc_total=npc_done=0
    for path in files:
        rel=path.relative_to(BASE).as_posix()
        previous=[json.loads(s) for s in z.read('MagiciansQuest_041/'+rel).decode('utf-8').splitlines()]
        current=[json.loads(s) for s in path.read_text('utf-8').splitlines()]
        assert len(previous)==len(current),(rel,'count')
        old_total+=len(previous);new_total+=len(current)
        for index,(o,n) in enumerate(zip(previous,current),1):
            old_done+=bool(o.get('vi'));new_done+=bool(n.get('vi'))
            if '04-thoai/' in rel:
                npc_total+=1;npc_done+=bool(n.get('vi'))
            if path.name not in TARGET:
                assert o==n,(rel,index,'outside target modified')
                continue
            assert len(previous)==TARGET[path.name],(rel,'target length')
            assert not o.get('vi'),(rel,index,'source already translated')
            assert set(o)==set(n),(rel,index,'field set')
            assert {k:v for k,v in o.items() if k!='vi'}=={k:v for k,v in n.items() if k!='vi'},(rel,index,'source changed')
            vi=n.get('vi')
            assert isinstance(vi,str) and vi.strip(),(rel,index,'missing VI')
            assert TOK.findall(o['en'])==TOK.findall(vi),(rel,index,'control tokens changed')
            assert unicodedata.normalize('NFC',vi)==vi,(rel,index,'NFC')
            assert not any(c in vi for c in '\r\n\t'),(rel,index,'embedded tab/newline')
            assert vi.count('▼')<=3,(rel,index,'too many breaks')
            assert all(len(TOK.sub('',line))<=34 for line in vi.split('▼')),(rel,index,'line too wide')
            if n.get('max_utf8_bytes') is not None:
                assert len(vi.encode('utf-8'))<=n['max_utf8_bytes'],(rel,index,'max bytes')
            added+=1
    assert (old_total,new_total)==(55976,55976)
    assert (old_done,new_done,added)==(11989,12229,240),(old_done,new_done,added)
    assert (npc_total,npc_done)==(52608,9104),(npc_total,npc_done)
    print(f'QA PASS: {len(files)} JSONL, {new_total:,} records; +{added} vi; {old_done:,} prior translations unchanged')
    print(f'Total {new_done:,}/{new_total:,} ({100*new_done/new_total:.2f}%), NPC {npc_done:,}/{npc_total:,}')
if __name__=='__main__':
    z=Path(sys.argv[1]) if len(sys.argv)>1 else Path('/mnt/data/MagiciansQuest-VietHoa-Checkpoint-041.zip')
    with zipfile.ZipFile(z) as source:validate(source)