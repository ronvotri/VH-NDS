#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rebuild CP054 translations from manually authored Japanese-to-Vietnamese mapping.
Do not treat as ROM patch or completed semantic/pixel font QA.
"""
from pathlib import Path
import collections, csv, hashlib, json, re, unicodedata, zipfile

ROOT=Path(__file__).resolve().parent
MNT=ROOT.parent
SOURCE=MNT/'JumpUltimateStars_Japan_BanGiao_Cloud.zip'
PREV=MNT/'JUS_CP053'
PENDING=PREV/'NGUON_CHUA_DICH_SAU_053.jsonl'
PREV_MERGED=PREV/'BAN_DICH_TONG_HOP_038-053.jsonl'
OVERLAY=MNT/'JumpUltimateStars_CP051_DinhChinh'/'BAN_DINH_CHINH_050A.jsonl'
EXPECTED_SHA='14e839a35e75f35534a93a1b37ebe42731ea530fbc012267b45bbbed8446f241'
TOKEN=re.compile(r'<[A-Z][A-Z_]*>')

def read_jsonl(p):
    return [json.loads(x) for x in p.read_text(encoding='utf-8-sig').splitlines() if x.strip()]
def write_jsonl(p,rows):
    p.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rows),encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(SOURCE)==EXPECTED_SHA,'Original ZIP not matching CP053 verified SHA256'
source_files={}
with zipfile.ZipFile(SOURCE) as archive:
    for name in archive.namelist():
        if name.startswith('translation/') and name.endswith('.jsonl'):
            base=name.rsplit('/',1)[-1]
            if base in source_files:raise ValueError('Duplicate source filename')
            source_files[base]=[json.loads(x) for x in archive.read(name).decode('utf-8-sig').splitlines()]
assert len(source_files)==30 and sum(map(len,source_files.values()))==34919
original={}
for f,group in source_files.items():
    for i,x in enumerate(group):
        assert x['id'] not in original and x.get('file',f)==f and x.get('row_index',i)==i,(f,i)
        original[x['id']]={**x,'file':f,'row_index':i}
assert len(original)==34919

pending=read_jsonl(PENDING)
assert len(pending)==732 and len({x['id'] for x in pending})==732
for x in pending:
    assert x['vi'] is None and x['id'] in original
    assert all(x.get(k)==v for k,v in original[x['id']].items())

mapping={}
for row in (ROOT/'draft_054.tsv').read_text(encoding='utf-8').splitlines():
    i,v=row.split('\t',1)
    i=int(i)
    assert i not in mapping
    mapping[i]=v
assert len(mapping)==484 and set(mapping)==set(range(747,1231))

new=[]
for x in pending:
    if x['file']!='00-he-thong-ten-goi-001.jsonl' or x['row_index'] not in mapping:
        continue
    vi=mapping[x['row_index']]
    assert vi.strip() and unicodedata.normalize('NFC',vi)==vi,(x['row_index'],vi)
    assert not any(c in vi for c in ('\x00','\n','\r','\ufffd'))
    assert collections.Counter(TOKEN.findall(x['ja']))==collections.Counter(TOKEN.findall(vi)),(x['row_index'],x['ja'],vi)
    cap=x.get('source_fixed_field_bytes')
    assert cap is None or len(vi.encode('utf-8'))<=cap,(x['row_index'],cap,len(vi.encode('utf-8')))
    new.append({**x,'vi':vi})
assert len(new)==484 and len({x['id'] for x in new})==484
assert [x['row_index'] for x in new]==list(range(747,1231))

previous=read_jsonl(PREV_MERGED)
assert len(previous)==10591 and len({x['id'] for x in previous})==10591
prior={x['id']:x for x in previous}
for row in previous:
    assert row['id'] in original
    src=original[row['id']]
    assert all(row[k]==src[k] for k in row if k!='vi')
for fix in read_jsonl(OVERLAY):
    assert prior[fix['id']]['vi']==fix['vi'],('Missing CP050A fix',fix['id'])
assert not any(x['id'] in prior for x in new)
merged=sorted(previous+new,key=lambda x:(x['file'],x['row_index']))
assert len(merged)==11075 and len({x['id'] for x in merged})==11075
remaining=[x for x in pending if x['id'] not in {o['id'] for o in new}]
assert len(remaining)==248 and {x['file'] for x in remaining}=={'00-he-thong-ten-goi-002.jsonl'}
assert [x['row_index'] for x in remaining]==list(range(248))
assert 34187+len(new)+len(remaining)==34919

write_jsonl(ROOT/'BAN_DICH_054.jsonl',new)
write_jsonl(ROOT/'BAN_DICH_TONG_HOP_038-054.jsonl',merged)
write_jsonl(ROOT/'NGUON_CHUA_DICH_SAU_054.jsonl',remaining)
with (ROOT/'BAN_DICH_054.tsv').open('w',encoding='utf-8-sig',newline='') as f:
    writer=csv.writer(f,delimiter='\t')
    writer.writerow(['file','row_index','id','ja','vi','utf8_bytes','source_fixed_field_bytes','context'])
    for x in new:
        writer.writerow([x['file'],x['row_index'],x['id'],x['ja'],x['vi'],len(x['vi'].encode()),x.get('source_fixed_field_bytes') or '', ';'.join(x.get('context',[]))])

qa={
 'game':'Jump Ultimate Stars (Japan) AJUJ', 'checkpoint':'054','date':'2026-11-20',
 'source_zip':SOURCE.name,'source_zip_sha256':sha(SOURCE),'source_files':len(source_files),
 'source_total_ids':len(original),'previous_total':34187,'new_translations':484,
 'from_file':'00-he-thong-ten-goi-001.jsonl','from_row_index':747,'to_row_index':1230,
 'context_counts':dict(collections.Counter(tuple(x['context'])[0] if x.get('context') else 'unknown' for x in new)),
 'translated_total':34187+len(new),'remaining':len(remaining),'progress_percent':round((34187+len(new))/34919*100,2),
 'id_uniqueness':True,'ja_metadata_exactly_match_source':True,'control_tokens_preserved':True,
 'unicode_nfc':True,'byte_limits_pass_where_declared':True,
 'source_fixed_field_bytes_rows':sum(x.get('source_fixed_field_bytes') is not None for x in new),
 'max_vi_chars':max(len(x['vi']) for x in new),'max_vi_utf8_bytes':max(len(x['vi'].encode('utf-8')) for x in new),
 'merged_038_054_ids':len(merged),'cp050a_10_corrections_retained':True,
 'nds_rom_patch_built':False,'font_pixel_qa_done':False,'manual_accuracy_review_complete':False,
 'notes':['Narrative descriptions have been translated as cohesive manga-specific paragraphs and redistributed to original fixed ordering of 484 IDs. The source does not specify a fixed per-record byte limit for this section.',
          'Row 1230 continues into 00-he-thong-ten-goi-002.jsonl row 0; its Vietnamese text intentionally lacks terminal punctuation to allow continuation.',
          'All 248 IDs left are in 00-he-thong-ten-goi-002.jsonl, from index 0 to 247.',
          'Text-only static QA; no ROM injection, NDS font width, or exhaustive human review yet.'],
 'output_sha256':{name:sha(ROOT/name) for name in ['BAN_DICH_054.jsonl','BAN_DICH_TONG_HOP_038-054.jsonl','NGUON_CHUA_DICH_SAU_054.jsonl','BAN_DICH_054.tsv']}
}
(ROOT/'QA_054.json').write_text(json.dumps(qa,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'new':len(new),'total':qa['translated_total'],'pending':len(remaining),'progress':qa['progress_percent'],'merged':len(merged),'max_chars':qa['max_vi_chars'],'QA':'PASS'},ensure_ascii=False))
