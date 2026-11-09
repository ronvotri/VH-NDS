#!/usr/bin/env python3
"""Rebuild Magician's Quest checkpoint 088 from 087 ZIP + unique_088.tsv.
Usage: python build_088.py --previous MagiciansQuest-VietHoa-Checkpoint-087.zip --output MagiciansQuest-VietHoa-Checkpoint-088.zip
"""
from pathlib import Path
import argparse,zipfile,re,json,csv,unicodedata
P=Path(__file__).resolve().parent
PREFIX=re.compile(r"^(?:\$(?:024|023|022|034|040|004)(?:'[-\d]+)*;)+")
TOK=re.compile(r"\$\d{3}(?:'[-\d]+)*;")
TARGET=['0043.006','0043.007']
OLD='MagiciansQuest_087/'
NEW='MagiciansQuest_088/'
def build(previous,output):
    with (P/'unique_088.tsv').open(encoding='utf8',newline='') as f:
        mapping={row['en_body']:row['vi_body'] for row in csv.DictReader(f,delimiter='\t')}
    with zipfile.ZipFile(previous) as z:
        assert z.testzip() is None
        orig={n.replace(OLD,NEW,1):z.read(n) for n in z.namelist()}
    delta=[]
    for key in TARGET:
        name=NEW+f'translation/04-thoai/talkfigs__0eng__data__{key}.jsonl'
        rows=[json.loads(s) for s in orig[name].decode().splitlines()]
        assert len(rows)==120 and all(row['vi'] is None for row in rows)
        for row in rows:
            p=PREFIX.match(row['en'])
            head=p.group(0) if p else ''
            vi=head+mapping[PREFIX.sub('',row['en'])]
            assert vi==unicodedata.normalize('NFC',vi)
            assert TOK.findall(vi)==TOK.findall(row['en'])
            assert vi.count('▼')<=3
            assert all(len(TOK.sub('',s))<=34 for s in vi.split('▼'))
            row['vi']=vi
            delta.append(row.copy())
        orig[name]=''.join(json.dumps(row,ensure_ascii=False,separators=(',',':'))+'\n' for row in rows).encode()
    assert len(delta)==240
    orig[NEW+'DELTA-088.jsonl']=''.join(json.dumps(row,ensure_ascii=False,separators=(',',':'))+'\n' for row in delta).encode()
    for key in ('unique_088.tsv','QA-088.md','CHECKPOINT-2026-11-10-DOT-88.md','README.md','BAN_GIAO.md','build_088.py', 'manual_0043_006.tsv','manual_0043_007.tsv','vi_0043_006.txt','vi_0043_007.txt'):
        orig[NEW+key]=(P/key).read_bytes()
    with zipfile.ZipFile(output,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=7) as z:
        for n,blob in sorted(orig.items()):z.writestr(n,blob)
    with zipfile.ZipFile(output) as z:assert z.testzip() is None
if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--previous',type=Path,required=True);a.add_argument('--output',type=Path,required=True)
    args=a.parse_args();build(args.previous,args.output)