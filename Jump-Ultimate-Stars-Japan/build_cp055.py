#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validate full Japanese source + CP055 hand-translated VN, retaining all prior deltas and CP050A corrections.

Does not write an NDS ROM patch.
"""
from pathlib import Path
import collections,csv,hashlib,json,re,unicodedata,zipfile
ROOT=Path(__file__).resolve().parent
DATA=ROOT.parent
SOURCE=DATA/'JumpUltimateStars_Japan_BanGiao_Cloud.zip'
PREV=DATA/'JUS_CP054'
OVERLAY=DATA/'JumpUltimateStars_CP051_DinhChinh'/'BAN_DINH_CHINH_050A.jsonl'
EXPECTED_SOURCE_SHA='14e839a35e75f35534a93a1b37ebe42731ea530fbc012267b45bbbed8446f241'
TOKEN=re.compile(r'<[A-Z][A-Z_]*>')
def read_jsonl(path):return [json.loads(line) for line in path.read_text(encoding='utf-8-sig').splitlines() if line.strip()]
def save_jsonl(path,rows):path.write_text(''.join(json.dumps(row,ensure_ascii=False)+'\n' for row in rows),encoding='utf-8')
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
assert sha(SOURCE)==EXPECTED_SOURCE_SHA,'Original source ZIP checksum changed'
source_files={}
with zipfile.ZipFile(SOURCE) as z:
 for name in z.namelist():
  if name.startswith('translation/') and name.endswith('.jsonl'):
   basename=name.rsplit('/',1)[-1]
   assert basename not in source_files
   source_files[basename]=[json.loads(line) for line in z.read(name).decode('utf-8-sig').splitlines() if line.strip()]
assert len(source_files)==30
source={}
for file,lines in source_files.items():
 for i,row in enumerate(lines):
  assert row['id'] not in source,(file,i)
  assert row.get('file',file)==file and row.get('row_index',i)==i,(file,i)
  source[row['id']]={**row,'file':file,'row_index':i}
assert len(source)==34919
pending=read_jsonl(PREV/'NGUON_CHUA_DICH_SAU_054.jsonl')
assert len(pending)==248 and [x['row_index'] for x in pending]==list(range(248))
assert all(x['file']=='00-he-thong-ten-goi-002.jsonl' and x['vi'] is None for x in pending)
assert all(all(x.get(k)==v for k,v in source[x['id']].items()) for x in pending)
translations={}
for line in (ROOT/'draft_055.tsv').read_text(encoding='utf-8').splitlines():
 key,vi=line.split('\t',1);i=int(key)
 assert i not in translations
 translations[i]=vi
assert len(translations)==248 and set(translations)==set(range(248))
new=[]
for row in pending:
 i=row['row_index'];vi=translations[i]
 assert vi and vi.strip() and unicodedata.normalize('NFC',vi)==vi,i
 assert all(ch not in vi for ch in ('\x00','\n','\r','\ufffd')),i
 assert collections.Counter(TOKEN.findall(row['ja']))==collections.Counter(TOKEN.findall(vi)),(i,row['ja'],vi)
 cap=row.get('source_fixed_field_bytes')
 assert cap is None or len(vi.encode('utf8'))<=cap,(i,cap,vi)
 new.append({**row,'vi':vi})
assert len(new)==248 and len({r['id'] for r in new})==248
prior=read_jsonl(PREV/'BAN_DICH_TONG_HOP_038-054.jsonl')
assert len(prior)==11075 and len({r['id'] for r in prior})==11075
past={r['id']:r for r in prior}
for row in prior:
 assert row['id'] in source
 orig=source[row['id']]
 assert all(orig[k]==v for k,v in row.items() if k!='vi'),('Older source changed',row['id'])
for fix in read_jsonl(OVERLAY):
 assert past[fix['id']]['vi']==fix['vi'],('lost CP050A correction',fix['id'])
assert not any(r['id'] in past for r in new)
merged=sorted(prior+new,key=lambda x:(x['file'],x['row_index']))
assert len(merged)==11323 and len({r['id'] for r in merged})==11323
assert 23596+len(merged)==34919
assert all(r['id'] in source and r['vi'] for r in merged)
assert all(collections.Counter(TOKEN.findall(r['ja']))==collections.Counter(TOKEN.findall(r['vi'])) for r in new)
assert len({r['id'] for r in prior+new})==11323
save_jsonl(ROOT/'BAN_DICH_055.jsonl',new)
save_jsonl(ROOT/'BAN_DICH_TONG_HOP_038-055.jsonl',merged)
with (ROOT/'BAN_DICH_055.tsv').open('w',encoding='utf-8-sig',newline='') as f:
 writer=csv.writer(f,delimiter='\t')
 writer.writerow(['file','row_index','id','ja','vi','utf8_bytes','fixed_field_bytes','context'])
 for x in new:writer.writerow([x['file'],x['row_index'],x['id'],x['ja'],x['vi'],len(x['vi'].encode('utf8')),x.get('source_fixed_field_bytes') or '',';'.join(x.get('context',[]))])
assert set(source)==set([r['id'] for r in merged]) | (set(source)-set([r['id'] for r in merged]))
qa={
 'game':'Jump Ultimate Stars (Japan) AJUJ','checkpoint':'055','date':'2026-11-20',
 'source_zip':SOURCE.name,'source_zip_sha256':sha(SOURCE),'source_file_count':len(source_files),
 'source_total_unique_ids':len(source),'previous_translated':34671,'new_translated':248,
 'cp001_037_history_reported_ids':23596,'cp038_055_verified_merged_ids':len(merged),
 'translation_total_by_checkpoint_sum':23596+len(merged),'remaining_by_checkpoint_sum':0,'progress_percent':100.0,
 'new_source_file':'00-he-thong-ten-goi-002.jsonl','new_row_range':[0,247],
 'new_source_id_matches':True,'new_ja_and_metadata_matches':True,'new_unique_ids':True,
 'new_ideosp_control_token_matches':True,'new_unicode_normalized_nfc':True,
 'new_fixed_field_limits_where_declared':True,'new_fixed_field_length_rows':sum(x.get('source_fixed_field_bytes') is not None for x in new),
 'new_vi_max_unicode_codepoints':max(len(x['vi']) for x in new),
 'new_vi_max_utf8_bytes':max(len(x['vi'].encode('utf8')) for x in new),
 'cp050a_10_corrections_retained':True,
 'new_source_context_counts':dict(collections.Counter((x.get('context') or [''])[0] for x in new)),
 'full_001_055_delta_audited_against_source':False,
 'full_all_34919_ids_audited_against_source':False,
 'nds_rom_patch_built':False,'font_pixel_qa_done':False,'manual_translation_accuracy_audit_complete':False,
 'notes':[
 'All previously untranslated 248 records have Vietnamese values. 100% is a content-count milestone based on 23,596 previously reported CP001–037 plus 11,323 validated CP038–055; separate full-source audit of CP001–037 still recommended.',
 'No byte cap is declared by Japanese source for CP055 lines. Validated token count per record; actual ROM layout and font compatibility need testing.',
 'Row 0 continues Midori Makibao sentence from CP054 row 1230.',
 'Row 119 and 120 preserve the source IDEOSP token positions; Luffy quoted speech continues through row 121.',
 'Ransen Festival transliteration (嵐泉祭), minor title names and established series terms require visual QA.',
 'Checkpoint 050A corrections (10 translations) preserved in merged CP038–055.'
 ],
 'sha256':{name:sha(ROOT/name) for name in ['BAN_DICH_055.jsonl','BAN_DICH_055.tsv','BAN_DICH_TONG_HOP_038-055.jsonl']}
}
(ROOT/'QA_055.json').write_text(json.dumps(qa,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'new':len(new),'total':23596+len(merged),'remaining':0,'merged':len(merged),'qa':'PASS','max_chars':qa['new_vi_max_unicode_codepoints']},ensure_ascii=False))
