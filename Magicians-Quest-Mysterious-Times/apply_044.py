#!/usr/bin/env python3
"""Apply checkpoint 044 to target JSONL files, without editing metadata or English.

Safe to rerun. Refuses to overwrite a different Vietnamese translation.
"""
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parent
TOK=re.compile(r"\$[0-9'\-]+;")
TARGET={'talkfigs__0eng__data__0033.006.jsonl','talkfigs__0eng__data__0033.007.jsonl'}

def run():
    data=[json.loads(line) for line in (ROOT/'DELTA-044.jsonl').read_text('utf8').splitlines()]
    assert len(data)==240
    groups={}
    for item in data:
        name=Path(item['file']).name
        assert name in TARGET
        assert item['id'] not in groups.setdefault(name,{})
        groups[name][item['id']]=item
    assert set(groups)==TARGET
    for name,updates in groups.items():
        path=ROOT/'translation'/'04-thoai'/name
        rows=[json.loads(s) for s in path.read_text('utf8').splitlines()]
        assert len(rows)==len(updates)==120
        for row in rows:
            d=updates[row['id']]
            assert row['en']==d['en']
            assert row.get('vi') in (None,'',d['vi']),'Existing translation differs; refuse overwrite'
            assert TOK.findall(row['en'])==TOK.findall(d['vi'])
            row['vi']=d['vi']
        path.write_text('\n'.join(json.dumps(row,ensure_ascii=False,separators=(',',':')) for row in rows)+'\n','utf8')
    print('Applied 240 Vietnamese pages from checkpoint 044 safely.')

if __name__=='__main__':run()