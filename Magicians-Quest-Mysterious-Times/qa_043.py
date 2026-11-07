#!/usr/bin/env python3
"""Full checkpoint 043 QA against the checkpoint 042 ZIP."""
import json,re,sys,unicodedata,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent
TOK=re.compile(r"\$[0-9'\-]+;")
TARGET={'talkfigs__0eng__data__0033.004.jsonl','talkfigs__0eng__data__0033.005.jsonl'}

def main(source):
    files=sorted((ROOT/'translation').rglob('*.jsonl'))
    assert len(files)==501
    total_old=total_new=translated_old=translated_new=added=npc_total=npc_done=0
    with zipfile.ZipFile(source) as z:
        for p in files:
            rel=p.relative_to(ROOT).as_posix()
            previous=[json.loads(s) for s in z.read('MagiciansQuest_042/'+rel).decode('utf8').splitlines()]
            current=[json.loads(s) for s in p.read_text('utf8').splitlines()]
            assert len(previous)==len(current),(rel,'row count')
            total_old+=len(previous);total_new+=len(current)
            for index,(old,new) in enumerate(zip(previous,current),1):
                translated_old+=bool(old.get('vi'))
                translated_new+=bool(new.get('vi'))
                if '04-thoai/' in rel:
                    npc_total+=1;npc_done+=bool(new.get('vi'))
                if p.name not in TARGET:
                    assert old==new,(rel,index,'outside translation target modified')
                    continue
                assert set(old)==set(new)
                assert {k:v for k,v in old.items() if k!='vi'}=={k:v for k,v in new.items() if k!='vi'},(rel,index,'non-vi edited')
                assert not old.get('vi'),(rel,index,'was translated')
                vi=new.get('vi')
                assert isinstance(vi,str) and vi.strip()
                assert TOK.findall(old['en'])==TOK.findall(vi),(rel,index,'control codes')
                assert unicodedata.normalize('NFC',vi)==vi
                assert not any(c in vi for c in '\r\n\t')
                assert vi.count('▼')<=3,(rel,index,'breaks')
                assert all(len(TOK.sub('',v))<=34 for v in vi.split('▼')),(rel,index,'line length')
                if old.get('max_utf8_bytes') is not None:
                    assert len(vi.encode('utf8'))<=old['max_utf8_bytes']
                added+=1
    assert (total_old,total_new)==(55976,55976)
    assert (translated_old,translated_new,added)==(12229,12469,240)
    assert (npc_total,npc_done)==(52608,9344)
    print('QA PASS: 501 JSONL, 55,976 records; +240 VI; 12,229 existing translations unchanged.')
    print('Progress: 12,469/55,976 (22.28%); NPC: 9,344/52,608.')

if __name__=='__main__':
    main(Path(sys.argv[1]) if len(sys.argv)>1 else Path('/mnt/data/MagiciansQuest-VietHoa-Checkpoint-042.zip'))