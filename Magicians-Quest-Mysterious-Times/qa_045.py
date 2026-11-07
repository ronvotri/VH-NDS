#!/usr/bin/env python3
"""Full checkpoint 045 regression QA against untouched checkpoint 044."""
from pathlib import Path
import json,re,sys,unicodedata,zipfile
ROOT=Path(__file__).resolve().parent
CODES=re.compile(r"\$[0-9'\-]+;")
TARGET={'talkfigs__0eng__data__0033.008.jsonl','talkfigs__0eng__data__0033.009.jsonl'}

def run(source):
    paths=sorted((ROOT/'translation').rglob('*.jsonl'))
    assert len(paths)==501,len(paths)
    old_done=new_done=total=npc_total=npc_done=changed=0
    with zipfile.ZipFile(source) as z:
        assert z.testzip() is None
        for p in paths:
            rel=p.relative_to(ROOT).as_posix()
            previous=z.read('MagiciansQuest_044/'+rel)
            current=p.read_bytes()
            if p.name not in TARGET:
                assert previous==current,(rel,'unchanged JSONL differs byte-for-byte')
            old=[json.loads(x) for x in previous.decode('utf8').splitlines()]
            new=[json.loads(x) for x in current.decode('utf8').splitlines()]
            assert len(old)==len(new),(rel,'record count changed')
            for line,(o,n) in enumerate(zip(old,new),1):
                total+=1
                old_done+=bool(o.get('vi'))
                new_done+=bool(n.get('vi'))
                if '04-thoai/' in rel:
                    npc_total+=1;npc_done+=bool(n.get('vi'))
                if p.name not in TARGET:continue
                assert set(o)==set(n),(rel,line,'keys changed')
                assert all(o[k]==n[k] for k in o if k!='vi'),(rel,line,'non-vi field changed')
                assert not o.get('vi'),(rel,line,'old field already translated')
                vi=n.get('vi')
                assert isinstance(vi,str) and vi.strip(),(rel,line,'translation missing')
                assert CODES.findall(o['en'])==CODES.findall(vi),(rel,line,'game token mismatch')
                assert unicodedata.normalize('NFC',vi)==vi,(rel,line,'NFC')
                assert '¤' not in vi and not any(x in vi for x in '\t\r\n'),(rel,line,'unescaped marker/newline')
                assert vi.count('▼')<=3,(rel,line,'more than 4 display lines')
                assert all(len(CODES.sub('',part))<=34 for part in vi.split('▼')),(rel,line,'line >34 characters')
                if o.get('max_utf8_bytes') is not None:
                    assert len(vi.encode('utf8'))<=int(o['max_utf8_bytes']),(rel,line,'byte limit')
                changed+=1
    assert total==55976,total
    assert (old_done,new_done,changed)==(12709,12949,240),(old_done,new_done,changed)
    assert (npc_total,npc_done)==(52608,9824),(npc_total,npc_done)
    delta=[json.loads(x) for x in (ROOT/'DELTA-045.jsonl').read_text('utf8').splitlines()]
    assert len(delta)==240
    assert len({(x['file'],x['id']) for x in delta})==240
    for d in delta:
        assert d.get('old_vi') is None
        assert any(d['file'].endswith(n) for n in TARGET)
    print('PASS: 501 JSONL / 55,976 records; +240 translated pages, 12,709 old records unchanged.')
    print('Progress 12,949/55,976 = {:.2f}%; NPC 9,824/52,608.'.format(100*new_done/total))

if __name__=='__main__':run(Path(sys.argv[1]) if len(sys.argv)>1 else Path('/mnt/data/MagiciansQuest-VietHoa-Checkpoint-044.zip'))