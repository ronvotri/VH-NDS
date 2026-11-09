#!/usr/bin/env python3
"""Build full Magician's Quest checkpoint 087 from 086 + manual unique_087.tsv.

Usage:
 python build_087.py --previous MagiciansQuest-VietHoa-Checkpoint-086.zip \
   --output MagiciansQuest-VietHoa-Checkpoint-087.zip
"""
from __future__ import annotations
import argparse, collections, csv, io, json, pathlib, re, unicodedata, zipfile, hashlib
BASE = pathlib.Path(__file__).resolve().parent
OLD, NEW = 'MagiciansQuest_086/', 'MagiciansQuest_087/'
TARGETS = ('0043.004', '0043.005')
NEXT = ('0043.006', '0043.007')
TOTAL, BEFORE, NPC_BEFORE = 55976, 22569, 19444
PREFIX = re.compile(r"^(?:\$(?:024|023|022|034|040|004)(?:'[-\d]+)*;)+")
TOKEN = re.compile(r"\$\d{3}(?:'[-\d]+)*;")
def body(s): return PREFIX.sub('', s)
def verify(en, vi, name):
    if not isinstance(vi, str) or not vi:
        raise ValueError(f'Empty vi: {name}')
    if vi != unicodedata.normalize('NFC', vi):
        raise ValueError(f'Unicode not NFC: {name}')
    if TOKEN.findall(en) != TOKEN.findall(vi):
        raise ValueError(f'Tokens mismatch: {name}: {TOKEN.findall(en)} != {TOKEN.findall(vi)}')
    if vi.count('▼') > 3:
        raise ValueError(f'Too many breaks: {name}')
    if any(len(TOKEN.sub('',segment)) > 34 for segment in vi.split('▼')):
        raise ValueError(f'Static segment > 34 characters: {name}')
    if any(ch in vi for ch in ('\t','\r','\n')):
        raise ValueError(f'Invalid separator: {name}')

def build(previous: pathlib.Path, output: pathlib.Path):
    lex={}
    with (BASE/'unique_087.tsv').open('r',encoding='utf-8',newline='') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            key=r['en_body']
            if key in lex:raise AssertionError('Duplicate body')
            lex[key]=r['vi_body']
            verify(key,r['vi_body'],'unique '+r['index'])
    assert len(lex)==55
    with zipfile.ZipFile(previous) as src:
        assert src.testzip() is None
        names=src.namelist()
        assert len(names)==len(set(names))
        assert all(n.startswith(OLD) for n in names)
        outfiles={n.replace(OLD,NEW,1):src.read(n) for n in names}
        english_pages=[]
        delta=[]
        for key in TARGETS:
            path=NEW+'translation/04-thoai/talkfigs__0eng__data__'+key+'.jsonl'
            rows=[json.loads(x) for x in outfiles[path].decode('utf-8').splitlines()]
            assert len(rows)==120 and all(x['vi'] is None for x in rows),key
            tsv=io.StringIO();wr=csv.writer(tsv,delimiter='\t',lineterminator='\n')
            wr.writerow(('id','en','vi','ctx'))
            for r in rows:
                en=r['en']; english_pages.append(body(en))
                v=(PREFIX.match(en).group() if PREFIX.match(en) else '')+lex[body(en)]
                verify(en,v,r['id'])
                r['vi']=v
                delta.append(r.copy())
                wr.writerow([r['id'],r['en'],r['vi'],r['ctx']])
            outfiles[path]=''.join(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n' for x in rows).encode('utf-8')
            outfiles[NEW+'manual_'+key.replace('.','_')+'.tsv']=tsv.getvalue().encode('utf-8')
            outfiles[NEW+'vi_'+key.replace('.','_')+'.txt']=''.join(r['id']+'\t'+r['vi']+'\n' for r in rows).encode('utf-8')
        assert len(delta)==240 and len(set(english_pages))==55
        outfiles[NEW+'DELTA-087.jsonl']=''.join(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n' for x in delta).encode('utf-8')
        outfiles[NEW+'unique_087.tsv']=(BASE/'unique_087.tsv').read_bytes()
        outfiles[NEW+'build_087.py']=pathlib.Path(__file__).read_bytes()
        for key in NEXT:
            path=NEW+'translation/04-thoai/talkfigs__0eng__data__'+key+'.jsonl'
            nxt=[json.loads(x) for x in outfiles[path].decode('utf-8').splitlines()]
            assert len(nxt)==120 and all(x['vi'] is None for x in nxt),key
        done=BEFORE+240
        npc=NPC_BEFORE+240
        pct=f'{done/TOTAL*100:.2f}'
        reuse=sum(1 for s in set(english_pages) if s not in {r['en_body'] for r in csv.DictReader(io.StringIO((BASE/'unique_087.tsv').read_text('utf-8')),delimiter='\t') if r['origin']=='new'})
        assert reuse==20
        qa=f'''# QA — Magician's Quest Checkpoint 087 (10/11/2026)

- **PASS:** 501 JSONL files / 55,976 records compared to checkpoint 086.
- **{BEFORE:,} → {done:,} / {TOTAL:,} ({pct}%)**: +240 NPC dialogue pages.
- `0043.004`: 120/120; `0043.005`: 120/120.
- 55 unique English body patterns; 20 prior patterns reused, 35 newly translated; 185 repeated pages within batch.
- 499 other JSONL byte-identical. Existing {BEFORE:,} translations unchanged.
- `id`, `en`, `ctx`, other fields, order unchanged in targets.
- Token sequence preserved for every modified line. Unicode NFC, max 3 `▼`, static segment ≤34 characters.
- ZIP CRC PASS; unique filenames; no files from other NDS games.
- **Not yet tested in-game:** dynamic expansion and actual font width require ROM/emulator checks.
- Next: `0043.006` and `0043.007` (120 untranslated pages each).
'''
        outfiles[NEW+'QA-087.md']=qa.encode('utf-8')
        checkpoint=f'''# Magician's Quest — Checkpoint 087

**Date:** 10/11/2026
**Repository:** `ronvotri/VH-NDS` / `Magicians-Quest-Mysterious-Times/`.

- Added **240 NPC pages**, `0043.004` (120) and `0043.005` (120).
- Total **{done:,}/55.976 ({pct}%)**; NPC **{npc:,}/52.608**.
- 55 unique EN patterns: 20 reused from prior translations; 35 newly localized (breakups, greetings, school tasks, rumours).
- Full 501 JSONL QA PASS; 499 files unchanged. Not yet tested on physical ROM.
- Handoff: `DELTA-087.jsonl`, `unique_087.tsv`, two EN–VI TSVs, `QA-087.md`, `build_087.py`, full ZIP.
- Next 088: `0043.006`, `0043.007` (120 pages each, untranslated and ready in ZIP).
'''
        outfiles[NEW+'CHECKPOINT-2026-11-10-DOT-87.md']=checkpoint.encode('utf-8')
        top=f'**Checkpoint mới nhất: 087 (10/11/2026) — {done:,}/55.976 ({pct}%).** +240 NPC (`0043.004`, `0043.005`); 35 mẫu thoại mới, 20 mẫu tái dùng; QA 501 JSONL PASS. Xem `CHECKPOINT-2026-11-10-DOT-87.md` và `QA-087.md`. Tiếp `0043.006`, `0043.007` (240 trang).\n\n'
        outfiles[NEW+'README.md']=(top+outfiles[NEW+'README.md'].decode('utf-8')).encode('utf-8')
        hand=f'''## Checkpoint 087 — 10/11/2026

- +240 trang thoại `0043.004` và `0043.005`; {done:,}/55.976 ({pct}%), NPC {npc:,}/52.608.
- 55 mẫu EN riêng: 35 dịch mới, 20 tái dùng. QA 501 JSONL PASS, giữ nguyên {BEFORE:,} bản dịch trước.
- Bàn giao ZIP đầy đủ, bản EN–VI, delta, script, QA. Chưa thử trong ROM NDS.
- Tiếp `0043.006` và `0043.007` (120 trang mỗi tệp).

'''
        outfiles[NEW+'BAN_GIAO.md']=(hand+outfiles[NEW+'BAN_GIAO.md'].decode('utf-8')).encode('utf-8')
        count=before=after=changed=0
        for oldname in names:
            if '/translation/' not in oldname or not oldname.endswith('.jsonl'):continue
            count+=1
            newname=oldname.replace(OLD,NEW,1)
            oldbytes=src.read(oldname);newbytes=outfiles[newname]
            target=any(newname.endswith(k+'.jsonl') for k in TARGETS)
            if target:changed+=1
            else:assert oldbytes==newbytes,f'Other file changed: {newname}'
            prior=[json.loads(x) for x in oldbytes.decode('utf-8').splitlines()]
            new=[json.loads(x) for x in newbytes.decode('utf-8').splitlines()]
            assert len(prior)==len(new)
            for a,b in zip(prior,new):
                count_fields=a.keys()==b.keys() and all(a[k]==b[k] for k in a if k!='vi')
                assert count_fields,a.get('id')
                if a['vi'] is not None:
                    assert a['vi']==b['vi'],a.get('id')
                before+=a['vi'] is not None
                after+=b['vi'] is not None
        total=sum(len(outfiles[n].decode('utf-8').splitlines()) for n in outfiles if '/translation/' in n and n.endswith('.jsonl'))
        assert (count,total,before,after,changed)==(501,TOTAL,BEFORE,done,2),(count,total,before,after,changed)
    output.parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(output,'w',zipfile.ZIP_DEFLATED,compresslevel=7) as dest:
        for path,payload in sorted(outfiles.items()):dest.writestr(path,payload)
    with zipfile.ZipFile(output) as zipped:
        assert zipped.testzip() is None
        assert len(zipped.namelist())==len(set(zipped.namelist()))
    print(f'PASS checkpoint 087: {count} JSONL; {after}/{TOTAL} ({pct}%); {len(outfiles)} files; {output.stat().st_size} bytes; SHA256 {hashlib.sha256(output.read_bytes()).hexdigest()}')

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--previous',type=pathlib.Path,required=True)
    ap.add_argument('--output',type=pathlib.Path,required=True)
    args=ap.parse_args()
    build(args.previous,args.output)