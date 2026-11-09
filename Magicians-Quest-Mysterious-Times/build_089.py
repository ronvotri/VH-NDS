#!/usr/bin/env python3
"""Rebuild full MQ089 using the full MQ088 ZIP and unique_089.tsv."""
from pathlib import Path
import csv,zipfile,json,re,unicodedata,argparse
PREFIX=re.compile(r"^(?:\$(?:024|023|022|034|040|004)(?:'[-\d]+)*;)+")
TOK=re.compile(r"\$\d{3}(?:'[-\d]+)*;")
ROOT=Path(__file__).resolve().parent
TARGET=('0043.008','0043.009')
with (ROOT/'unique_089.tsv').open(encoding='utf-8',newline='') as f:
    MAP={r['en_body']:r['vi_body'] for r in csv.DictReader(f,delimiter='\t')}

def run(before,output):
    old='MagiciansQuest_088/';new='MagiciansQuest_089/'
    with zipfile.ZipFile(before) as zz:
        assert zz.testzip() is None
        data={n.replace(old,new,1):zz.read(n) for n in zz.namelist()}
    for key in TARGET:
        path=new+'translation/04-thoai/talkfigs__0eng__data__'+key+'.jsonl'
        rows=[json.loads(l) for l in data[path].decode('utf-8').splitlines()]
        assert len(rows)==120 and all(r['vi'] is None for r in rows)
        for r in rows:
            body=PREFIX.sub('',r['en'])
            assert body in MAP
            r['vi']=(r['en'][:len(r['en'])-len(body)])+MAP[body]
            assert TOK.findall(r['en'])==TOK.findall(r['vi'])
            assert r['vi']==unicodedata.normalize('NFC',r['vi'])
        data[path]=''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in rows).encode('utf-8')
    for n in ('README.md','BAN_GIAO.md','QA-089.md','CHECKPOINT-2026-11-10-DOT-89.md','DELTA-089.jsonl','unique_089.tsv','build_089.py','manual_0043_008.tsv','manual_0043_009.tsv','vi_0043_008.txt','vi_0043_009.txt'):
        data[new+n]=(ROOT/n).read_bytes()
    with zipfile.ZipFile(output,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=7) as zz:
        for n,blob in sorted(data.items()):zz.writestr(n,blob)
    with zipfile.ZipFile(output) as zz:assert zz.testzip() is None
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--previous',required=True,type=Path);p.add_argument('--output',required=True,type=Path);a=p.parse_args();run(a.previous,a.output)