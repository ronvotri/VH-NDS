#!/usr/bin/env python3
"""Apply checkpoint 042's reviewed delta to checkpoint 041's source tree; only vi fields change."""
from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parent
TOK=re.compile(r"\$[0-9'\-]+;")
TARGET={'0033.002','0033.003'}
def run():
    delta=[json.loads(line) for line in (ROOT/'DELTA-042.jsonl').read_text('utf-8').splitlines()]
    assert len(delta)==240
    byfile={}
    for row in delta:
        name=Path(row['file']).name
        assert any(name.endswith(n+'.jsonl') for n in TARGET)
        byfile.setdefault(name,{})[row['id']]=row
    for name,items in byfile.items():
        p=ROOT/'translation'/'04-thoai'/name
        rows=[json.loads(line) for line in p.read_text('utf-8').splitlines()]
        assert len(rows)==len(items)==120
        for row in rows:
            d=items[row['id']]
            assert row['en']==d['en']
            assert row.get('vi') in (None,'',d['vi']),('conflicting translation',row['id'])
            assert TOK.findall(row['en'])==TOK.findall(d['vi']),row['id']
            row['vi']=d['vi']
        p.write_text('\n'.join(json.dumps(x,ensure_ascii=False,separators=(',',':')) for x in rows)+'\n','utf-8')
    print('Applied 240 vi translations (safe to run twice)')
if __name__=='__main__':run()