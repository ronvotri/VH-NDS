from pathlib import Path
import zipfile,json,collections,re,unicodedata,copy,hashlib,shutil,csv,sys
BASE=Path('/mnt/data/MQ113'); data=json.loads((BASE/'unique.json').read_text())
uniq=data['uniq'];old=data['old'];z=zipfile.ZipFile('/mnt/data/MagiciansQuest-VietHoa-Checkpoint-112.zip')
pat=r"\$\d{3}(?:'[-\d]+)*;"
token=re.compile(pat)

def split_msg(en):
 prefix=re.match('^(?:'+pat+')*',en).group()
 rest=en[len(prefix):]
 m=re.search('(?:'+pat+')+$',rest)
 suffix=m.group() if m else ''
 if suffix: rest=rest[:-len(suffix)]
 return prefix,re.split(pat,rest),token.findall(rest),suffix

mapped={}
for j,line in enumerate((BASE/'translated.tsv').read_text().splitlines(),1):
 if not line.strip():continue
 try:
  i,s=line.split('\t',1); i=int(i)
 except Exception as e:raise ValueError(f'Bad row {j}: {line!r}') from e
 if i in mapped:raise ValueError(f'Duplicate {i}')
 mapped[i]=s
issues=[]
for i,en in enumerate(uniq):
 if en in old:
  if i in mapped:issues.append((i,'reused yet manually provided'))
  continue
 if i not in mapped:issues.append((i,'not translated'));continue
 prefix,parts,tok,suffix=split_msg(en)
 vi=mapped[i]
 if vi.count('¤')!=len(tok):issues.append((i, f'token marker count {vi.count("¤")} expected {len(tok)}',repr(vi),repr('¤'.join(parts))))
 if '¤' in vi and not tok:issues.append((i,'extra marker'))
print('Translation phrase count',len(mapped),'unique new expected',sum(x not in old for x in uniq))
if issues:
 for item in issues[:200]:print('MARKER FAIL',item)
 sys.exit(1)
print('All marker counts match.')

# Translate; never alter source control tokens or previously translated entries.
def tokens_of(s):return token.findall(s)
def visible_len(s):return len(token.sub('',s))

def wrap_smart(value,limit=34,max_lines=4):
 # Existing author-made page breaks are preferred. If some phrases exceed 34,
 # first try wrapping per authored segment. If that overflows four lines, reflow.
 def wrap_segment(raw):
  words=raw.split(' ')
  lines=[];line=''
  for w in words:
   if not w:continue
   proposal=(line+' '+w) if line else w
   if line and visible_len(proposal)>limit:
    lines.append(line);line=w
   else:line=proposal
  if line:lines.append(line)
  return lines
 if all(visible_len(p)<=limit for p in value.split('▼')) and value.count('▼')<=max_lines-1:return value
 attempt=[]
 for s in value.split('▼'):
  attempt.extend(wrap_segment(s))
 if len(attempt)>max_lines:
  attempt=wrap_segment(value.replace('▼',' '))
 if len(attempt)>max_lines:
  return value # FAIL on QA: manually shorten instead of discarding content.
 return '▼'.join(attempt)

vi_by_en={}; untranslated=0
for i,en in enumerate(uniq):
 if en in old:
  vi_by_en[en]=old[en]
  continue
 prefix,parts,tok,suffix=split_msg(en)
 vi_parts=mapped[i].split('¤')
 assert len(vi_parts)==len(tok)+1
 v=prefix+''.join(part+ (tok[j] if j<len(tok) else '') for j,part in enumerate(vi_parts))+suffix
 v=unicodedata.normalize('NFC',v)
 v=wrap_smart(v)
 vi_by_en[en]=v
 untranslated+=1

bads=[]
for i,e in enumerate(uniq):
 v=vi_by_en[e]
 if not v or not v.strip():bads.append((i,'empty'))
 if tokens_of(e)!=tokens_of(v):bads.append((i,'tokens',tokens_of(e),tokens_of(v)))
 if v.count('▼')>3:bads.append((i,'breaks',v.count('▼'),repr(v)))
 for segment in v.split('▼'):
  if visible_len(segment)>34:bads.append((i,'segment length',visible_len(segment),repr(v)))
 if v!=unicodedata.normalize('NFC',v):bads.append((i,'NFC'))
if bads:
 print('QA ISSUES:',len(bads))
 for e in bads[:130]:print(e)
 sys.exit(1)
print('All 580 unique strings pass token, length, NFC and break QA.')

names_in_zip=z.namelist();prefix='MagiciansQuest_112/translation/04-thoai/talkfigs__0eng__data__';targets={prefix+f'0046.{i:03}.jsonl' for i in range(17,23)}
assert len(targets)==6 and all(t in names_in_zip for t in targets)
modified={};changed=[];target_counts={}
for name in sorted(targets):
 rows=[json.loads(s) for s in z.read(name).decode('utf-8-sig').splitlines()]
 if len(rows)!=120:raise ValueError(f'Wrong count {name}: {len(rows)}')
 for row in rows:
  assert row['vi'] is None
  row['vi']=vi_by_en[row['en']]
  changed.append(row)
 modified[name]=('\n'.join(json.dumps(r,ensure_ascii=False) for r in rows)+'\n').encode()
 target_counts[name]=len(rows)
assert len(changed)==720

# Count all JSONL and translations, verifying that no existing translations change.
prior_tot=0;rows_total=0;all_jsonl=[];prior_v=0
for name in names_in_zip:
 if name.startswith('MagiciansQuest_112/translation/') and name.endswith('.jsonl'):
  all_jsonl.append(name)
  olddata=z.read(name)
  oldrows=[json.loads(s) for s in olddata.decode('utf-8-sig').splitlines()]
  rows_total+=len(oldrows)
  prior_v+=sum(bool(x.get('vi')) for x in oldrows)
  if name in modified:
   newrows=[json.loads(s) for s in modified[name].decode().splitlines()]
   assert len(oldrows)==len(newrows)
   for a,b in zip(oldrows,newrows):
    assert a['id']==b['id'] and a['en']==b['en'] and a.get('ctx')==b.get('ctx')
    assert a.get('vi') is None and b['vi']
  else:
   # outside target unchanged by byte-copy (ensured by ZIP writing below)
   pass
assert len(all_jsonl)==501,(len(all_jsonl),rows_total)
assert rows_total==55976,rows_total
assert prior_v==32055,prior_v
assert prior_v+len(changed)==32775
assert len(modified)==6
print('PASS records',rows_total,'JSONLs',len(all_jsonl),'previous',prior_v,'new',len(changed),'result',prior_v+len(changed))

# Process output files and handoff, then pack the FULL ZIP.
patid=re.compile(r'0046\.(\d{3})')
for name in sorted(modified):
 short=patid.search(name).group(0)
 lines=[json.loads(s) for s in modified[name].decode().splitlines()]
 (BASE/f'manual_{short.replace(".","_")}.tsv').write_text('id\ten\tvi\n'+'\n'.join(f'{x["id"]}\t{x["en"]}\t{x["vi"]}' for x in lines)+'\n')
 (BASE/f'vi_{short.replace(".","_")}.txt').write_text('\n'.join(x['id']+'\t'+x['vi'] for x in lines)+'\n')
 (BASE/f'{short}.jsonl').write_bytes(modified[name])

counts=collections.Counter(row['en'] for row in changed)
uniq_rows=[(i,en,vi_by_en[en],counts[en], 'reused' if en in old else 'new') for i,en in enumerate(uniq)]
with (BASE/'unique_113.tsv').open('w') as f:
 f.write('index\tcount\tstatus\ten\tvi\n')
 for i,e,v,c,s in uniq_rows:f.write(f'{i}\t{c}\t{s}\t{e}\t{v}\n')
(BASE/'manual_113.tsv').write_text('index\ttranslation_body\n'+'\n'.join(str(i)+'\t'+v for i,v in sorted(mapped.items()))+'\n')
(BASE/'DELTA-113.jsonl').write_text('\n'.join(json.dumps(x,ensure_ascii=False) for x in changed)+'\n')

# Progress is calculated from the 55,976 records. English source is retained.
percent=32775/55976*100
qa=f'''# Magician's Quest — QA checkpoint 113

- **PASS:** 501 tệp JSONL / 55.976 dòng; +720 trang thoại NPC.
- Tiến độ **32.055 → 32.775 / 55.976 ({percent:.2f}%)**.
- Tệp `0046.017`–`0046.022`: 120 trang/tệp, 720 trang đã có bản dịch.
- 580 mẫu tiếng Anh khác nhau; **538 mẫu dịch mới**, 42 mẫu tái sử dụng nguyên văn từ checkpoint 112.
- Bảo toàn 32.055 bản dịch trước; 495 tệp JSONL ngoài phạm vi không đổi byte.
- Token `$...;` và thứ tự: PASS; Unicode NFC: PASS; tối đa 3 dấu `▼`: PASS; tối đa 34 ký tự tĩnh/đoạn: PASS.
- `id`, `en`, `ctx` của tất cả mục giữ nguyên.
- ZIP: kiểm tra CRC sau đóng gói.
- **Chưa thử ROM NDS/giả lập:** tên nhân vật động có thể làm thay đổi độ rộng hiển thị.
'''
checkpoint=f'''# Magician's Quest — Checkpoint 113

**Ngày:** 11/11/2026  
**Repo:** `ronvotri/VH-NDS/Magicians-Quest-Mysterious-Times/`

- +720 trang NPC: `0046.017`–`0046.022`, 120 trang mỗi tệp.
- Tổng: **32.775/55.976 ({percent:.2f}%)**; NPC **29.650/52.608**.
- 580 mẫu tiếng Anh khác nhau, 538 mẫu dịch tay mới, 42 mẫu tái sử dụng; tất cả 720 trang có `vi`.
- Nội dung: chuyện trường học, Ông Kẹo, Nhà Ma, Nhân Sư, Cấm Thư, sinh vật huyền bí, ký túc xá, phiêu lưu cõi mơ.
- 501 JSONL QA PASS, giữ nguyên 32.055 bản dịch trước và 495 tệp ngoài phạm vi; token, ngắt dòng và NFC đạt.
- Bàn giao: ZIP đầy đủ, `DELTA-113.jsonl`, `unique_113.tsv`, `manual_113.tsv`, 6 bảng EN-VI và 6 tệp VI, `QA-113.md`, `build_113.py`.
- Kiểm thử hiển thị trên ROM NDS: chưa thực hiện.
- Tiếp đợt 114: kiểm kê các tệp thoại chưa dịch sau `0046.022`.
'''
(BASE/'QA-113.md').write_text(qa)
(BASE/'CHECKPOINT-2026-11-11-DOT-113.md').write_text(checkpoint)

# Existing notes are carried forward verbatim with a small new section.
namebase='MagiciansQuest_112/'
for name in ['BAN_GIAO.md','README.md']:
 oldnote=z.read(namebase+name).decode('utf-8')
 heading=f'## Cập nhật 113 — 11/11/2026\n\n+720 trang `0046.017`–`0046.022` (538 mẫu dịch mới, 42 tái sử dụng), tổng 32.775/55.976 ({percent:.2f}%). QA dữ liệu đạt; chưa test trực tiếp trên ROM. Xem `CHECKPOINT-2026-11-11-DOT-113.md` và `QA-113.md`.\n\n'
 (BASE/name).write_text(heading+oldnote)

output=Path('/mnt/data/MagiciansQuest-VietHoa-Checkpoint-113.zip')
with zipfile.ZipFile(output,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as out:
 for item in z.infolist():
  path=item.filename
  rel=path[len(namebase):] if path.startswith(namebase) else None
  newname=path.replace(namebase,'MagiciansQuest_113/',1) if rel is not None else path
  if path in modified: payload=modified[path]
  elif rel in ('BAN_GIAO.md','README.md'):payload=(BASE/rel).read_bytes()
  else:payload=z.read(item)
  out.writestr(newname,payload,compress_type=zipfile.ZIP_DEFLATED)
 for p in sorted(BASE.iterdir()):
  if p.name in ('prep.py','unique.json','translated.tsv','translate_source.txt','build_113.py','BAN_GIAO.md','README.md') or p.is_dir():continue
  if p.name.startswith('0046.') and p.name.endswith('.jsonl'):continue # already in translation dir
  out.write(p,'MagiciansQuest_113/'+p.name)
 out.write(BASE/'build_113.py','MagiciansQuest_113/build_113.py')
with zipfile.ZipFile(output) as check:
 assert check.testzip() is None
 check_names=check.namelist()
 assert len(check_names)==len(names_in_zip)+len([p for p in BASE.iterdir() if p.name not in ('prep.py','unique.json','translated.tsv','translate_source.txt','build_113.py','BAN_GIAO.md','README.md') and not(p.name.startswith('0046.') and p.suffix=='.jsonl')])+1
print('ZIP PASS',output,output.stat().st_size,'bytes,',len(check_names),'entries')
