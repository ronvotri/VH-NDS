#!/usr/bin/env python3
"""Compare checkpoint 035 with checkpoint 034 ZIP; no edits to files."""
from pathlib import Path
import zipfile,json,re,unicodedata,collections
ROOT=Path(__file__).resolve().parent
BASE=ROOT.parent/'MagiciansQuest-VietHoa-Checkpoint-034.zip'
if not BASE.exists():BASE=ROOT.parent.parent/'MagiciansQuest-VietHoa-Checkpoint-034.zip'
TOK=re.compile(r"\$\d+(?:'[-\d]+)*;")
assert BASE.exists(), 'Place checkpoint 034 ZIP beside checkpoint 035 directory.'
with zipfile.ZipFile(BASE) as z:
 names=sorted(n for n in z.namelist() if n.startswith('MagiciansQuest_034/translation/') and n.endswith('.jsonl'))
 changes=collections.Counter();total=translated=0
 for name in names:
  rel=name.removeprefix('MagiciansQuest_034/')
  old=[json.loads(x) for x in z.read(name).decode('utf8').splitlines()]
  new=[json.loads(x) for x in (ROOT/rel).read_text('utf8').splitlines()]
  assert len(old)==len(new)
  for o,n in zip(old,new):
   total+=1
   assert set(o)==set(n)
   assert all(o.get(k)==n.get(k) for k in set(o)|set(n) if k!='vi')
   if n.get('vi'):translated+=1
   if o.get('vi')==n.get('vi'):continue
   assert o.get('vi') in (None,'')
   v=n['vi'];assert v and TOK.findall(v)==TOK.findall(o['en'])
   assert v==unicodedata.normalize('NFC',v)
   assert v.count('▼')<=3 and all(len(TOK.sub('',part))<=34 for part in v.split('▼'))
   assert not any(c in v for c in '\n\r\t')
   assert not n.get('max_utf8_bytes') or len(v.encode('utf8'))<=n['max_utf8_bytes']
   changes[rel]+=1
assert len(names)==501 and total==55976 and translated==10568
assert dict(changes)=={'translation/04-thoai/talkfigs__0eng__data__0030.003.jsonl':120, 'translation/04-thoai/talkfigs__0eng__data__0030.004.jsonl':120}
print('PASS 501 JSONL / 55976 rows / 10568 translations / +240 changes')