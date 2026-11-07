#!/usr/bin/env python3
"""Apply reviewed checkpoint 043 delta to the two target JSONL files; only `vi` changes."""
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parent
TOK=re.compile(r"\$[0-9'\-]+;")
TARGET={'talkfigs__0eng__data__0033.004.jsonl','talkfigs__0eng__data__0033.005.jsonl'}

def main():
    delta=[json.loads(s) for s in (ROOT/'DELTA-043.jsonl').read_text('utf8').splitlines()]
    assert len(delta)==240
    grouped={}
    for d in delta:
        n=Path(d['file']).name
        assert n in TARGET
        grouped.setdefault(n,{})[d['id']]=d
    for n,table in grouped.items():
        p=ROOT/'translation'/'04-thoai'/n
        rows=[json.loads(s) for s in p.read_text('utf8').splitlines()]
        assert len(rows)==len(table)==120
        for row in rows:
            d=table[row['id']]
            assert row['en']==d['en']
            assert row.get('vi') in (None,'',d['vi']),'Refuse to overwrite conflicting VI'
            assert TOK.findall(row['en'])==TOK.findall(d['vi'])
            row['vi']=d['vi']
        p.write_text('\n'.join(json.dumps(row,ensure_ascii=False,separators=(',',':')) for row in rows)+'\n','utf8')
    print('Applied checkpoint 043: 240 verified VI fields, safe to rerun.')

if __name__=='__main__':main()