#!/usr/bin/env python3
"""Magician's Quest NDS: rebuild full checkpoint 086 from checkpoint 085 ZIP.

Usage: python build_086.py --previous MagiciansQuest-VietHoa-Checkpoint-085.zip --output MagiciansQuest-VietHoa-Checkpoint-086.zip

The two mq086_vi_*.txt files are manually edited dialogue bodies in source order.
No machine translation; all variable/control prefixes come verbatim from source.
"""
from __future__ import annotations
import argparse, collections, csv, io, json, pathlib, re, unicodedata, zipfile
BASE=pathlib.Path(__file__).resolve().parent
OLD='MagiciansQuest_085/'
NEW='MagiciansQuest_086/'
KEYS=('0043.002','0043.003')
NEXT=('0043.004','0043.005')
TOK=re.compile(r"\$\d{3}(?:'[-\d]+)*;")
PRE=re.compile(r"^(?:\$(?:024|023|022|034|040|004)(?:'[-\d]+)*;)+")
BASE_DONE=22329
TOTAL=55976
BASE_NPC=19204

def verify(en,vi,path):
    assert vi and isinstance(vi,str), (path,'missing')
    assert vi==unicodedata.normalize('NFC',vi), (path,'NFC')
    assert TOK.findall(en)==TOK.findall(vi), (path,'tokens',TOK.findall(en),TOK.findall(vi))
    assert vi.count('▼')<=3, (path,'breaks')
    assert all(len(TOK.sub('',part))<=34 for part in vi.split('▼')), (path,'too long')
    assert not any(c in vi for c in ('\t','\r','\n')), (path,'control chars')

def build(previous,output):
    with zipfile.ZipFile(previous) as prev:
        assert prev.testzip() is None
        names=prev.namelist()
        assert len(names)==len(set(names))
        assert all(n.startswith(OLD) for n in names)
        files={n.replace(OLD,NEW,1):prev.read(n) for n in names}
        delta=[]; distinct=set(); counts={}
        for key in KEYS:
            name=f'{NEW}translation/04-thoai/talkfigs__0eng__data__{key}.jsonl'
            raw=files[name]
            rows=[json.loads(l) for l in raw.decode('utf-8').splitlines()]
            vi=(BASE/f'mq086_vi_{key.replace(".","_")}.txt').read_text('utf-8').splitlines()
            assert len(rows)==len(vi)==120, (key,len(rows),len(vi))
            assert all(row['vi'] is None for row in rows)
            counts[key]=len(rows)
            tsv=io.StringIO(); w=csv.writer(tsv,delimiter='\t',lineterminator='\n'); w.writerow(('id','en','vi','ctx'))
            for row,text in zip(rows,vi):
                en=row['en'];prefix=PRE.match(en)
                row['vi']=(prefix.group() if prefix else '')+text
                verify(en,row['vi'],row['id'])
                distinct.add(PRE.sub('',en))
                w.writerow((row['id'],en,row['vi'],row['ctx']))
                delta.append(row.copy())
            files[name]=''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in rows).encode('utf-8')
            files[f'{NEW}manual_{key.replace(".","_")}.tsv']=tsv.getvalue().encode('utf-8')
            files[f'{NEW}vi_{key.replace(".","_")}.txt']=''.join(r['id']+'\t'+r['vi']+'\n' for r in rows).encode('utf-8')
            files[f'{NEW}mq086_vi_{key.replace(".","_")}.txt']=(BASE/f'mq086_vi_{key.replace(".","_")}.txt').read_bytes()
        assert len(delta)==240
        files[NEW+'DELTA-086.jsonl']=''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in delta).encode('utf-8')
        percent=round(100*(BASE_DONE+240)/TOTAL,2)
        assert percent==40.32
        report=f'''# QA — Magician's Quest Checkpoint 086 (10/11/2026)

- PASS: **501 JSONL / 55,976 records** compared against full checkpoint 085 ZIP.
- **22,329 → {BASE_DONE+240} / {TOTAL} ({percent:.2f}%)** translated; NPC **{BASE_NPC+240}/52,608**.
- Target files: `0043.002` 120/120, `0043.003` 120/120.
- **{len(distinct)} unique English body patterns** among 240 pages; {240-len(distinct)} duplicate pages.
- All 22,329 earlier translations remained unchanged; 499 other JSONL byte-identical.
- All IDs, English texts, context, keys and order preserved; all NDS tokens in exact order.
- Unicode NFC PASS; at most 3 breaks; max 34 static Unicode characters per segment; all ZIP CRC PASS.
- **Not tested in ROM**: dynamic field expansion and rendered font width remain to be checked.
- Next: `0043.004`, `0043.005` (both already in full ZIP).
'''
        files[NEW+'QA-086.md']=report.encode('utf-8')
        notes=f'''# Magician's Quest — Checkpoint 086

**Date:** 10/11/2026
**Repository:** ronvotri/VH-NDS / Magicians-Quest-Mysterious-Times/

- **+240 NPC pages** from `0043.002` (120), `0043.003` (120).
- Total **{BASE_DONE+240}/55,976 ({percent:.2f}%)**; NPC **{BASE_NPC+240}/52,608**.
- Themes: schooling, friendship, exchange, transfer, festivals and a mischievous student's dialogues.
- **{len(distinct)} unique English patterns** translated/reused; full QA PASS.
- Hand-off: `DELTA-086.jsonl`, `manual_0043_002.tsv`, `manual_0043_003.tsv`, `mq086_vi_*.txt`, `QA-086.md`, `build_086.py`, complete ZIP in Library.
- Next: `0043.004` and `0043.005`, 240 pages; source is in ZIP, not yet staged GitHub.
- UI-on-ROM testing remains open.
'''
        files[NEW+'CHECKPOINT-2026-11-10-DOT-86.md']=notes.encode('utf-8')
        files[NEW+'build_086.py']=pathlib.Path(__file__).read_bytes()
        top=f'**Checkpoint mới nhất: 086 (10/11/2026) — {BASE_DONE+240}/55.976 ({percent:.2f}%).** +240 NPC (`0043.002`, `0043.003`); QA 501 JSONL PASS. Xem `CHECKPOINT-2026-11-10-DOT-86.md`, `QA-086.md`. Tiếp `0043.004`, `0043.005` (240 trang).\n\n'
        files[NEW+'README.md']=(top+files[NEW+'README.md'].decode('utf-8')).encode('utf-8')
        hand=f'## Checkpoint 086 — 10/11/2026\n\n- +240 trang thoại (`0043.002` và `0043.003`); tổng {BASE_DONE+240}/55.976 ({percent:.2f}%), NPC {BASE_NPC+240}/52.608.\n- QA 501 JSONL PASS; giữ 22.329 bản dịch trước; 499 JSONL ngoài đợt không đổi byte.\n- ZIP đầy đủ, bản EN–VI, báo cáo QA, script tái tạo. Chưa thử trong ROM.\n- Đợt 087: `0043.004` và `0043.005` (240 trang).\n\n'
        files[NEW+'BAN_GIAO.md']=(hand+files[NEW+'BAN_GIAO.md'].decode('utf-8')).encode('utf-8')
        old_count=new_count=total=changed=0
        for path in names:
            if '/translation/' not in path or not path.endswith('.jsonl'): continue
            before=prev.read(path)
            newpath=path.replace(OLD,NEW,1)
            after=files[newpath]
            target=any(newpath.endswith(key+'.jsonl') for key in KEYS)
            if target:changed+=1
            else: assert before==after, ('unrelated JSONL modified',newpath)
            b=[json.loads(x) for x in before.decode('utf-8').splitlines()]
            a=[json.loads(x) for x in after.decode('utf-8').splitlines()]
            assert len(a)==len(b)
            for old,new in zip(b,a):
                assert old.keys()==new.keys()
                assert all(old[k]==new[k] for k in old if k!='vi')
                old_count+=old['vi'] is not None
                new_count+=new['vi'] is not None
                if old['vi'] is not None: assert old['vi']==new['vi']
                if target: verify(new['en'],new['vi'],new['id'])
                total+=1
        assert (total,old_count,new_count,changed)==(TOTAL,BASE_DONE,BASE_DONE+240,2),(total,old_count,new_count,changed)
        with zipfile.ZipFile(output,'w',zipfile.ZIP_DEFLATED,compresslevel=7) as z:
            for name in sorted(files):z.writestr(name,files[name])
        with zipfile.ZipFile(output) as z:
            assert z.testzip() is None
            assert len(z.namelist())==len(files)==len(set(z.namelist()))
        print('PASS',len(files),'ZIP files;',total,'JSONL rows;',new_count,'done;',len(distinct),'unique English patterns')
        print('ZIP:',output,output.stat().st_size)
if __name__=='__main__':
    a=argparse.ArgumentParser()
    a.add_argument('--previous',type=pathlib.Path,required=True)
    a.add_argument('--output',type=pathlib.Path,required=True)
    args=a.parse_args()
    build(args.previous,args.output)