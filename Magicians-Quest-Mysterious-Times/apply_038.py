import re,os,json,unicodedata,copy,collections,pathlib
ROOT=pathlib.Path(__file__).resolve().parent
HOME=ROOT
TOK=re.compile(r'\$\d{3}(?:\'[^;$]+)*;')
LEAD=re.compile(r'^(?:\$\d{3}(?:\'[^;$]+)*;)*')
TAIL=re.compile(r'(?:\$\d{3}(?:\'[^;$]+)*;)*$')
for suffix,total in [('0031.004',120),('0031.005',101)]:
 file=ROOT/f'translation/04-thoai/talkfigs__0eng__data__{suffix}.jsonl'
 rows=[json.loads(x) for x in file.read_text('utf-8').splitlines()]
 assert len(rows)==total
 lines=(HOME/f'vi_{suffix.replace(".","_")}_raw.txt').read_text('utf-8').splitlines()
 mapping={int(z.partition('|')[0]):z.partition('|')[2] for z in lines}
 assert len(mapping)==total and sorted(mapping)==list(range(total))
 notes=[]
 for i,r in enumerate(rows):
  original=r['en'];raw=mapping[i]
  pre=LEAD.match(original).group(); remaining=original[len(pre):]; suf=TAIL.search(remaining).group(); middle=remaining[:-len(suf)] if suf else remaining
  mids=TOK.findall(middle)
  if raw.count('§')!=len(mids):
   raise Exception(f'{suffix} {i}: middle tokens {mids} count {len(mids)} raw placeholders {raw.count("§")}: {original} -> {raw}')
  for token in mids:raw=raw.replace('§',token,1)
  vi=unicodedata.normalize('NFC',pre+raw+suf)
  if TOK.findall(original)!=TOK.findall(vi):raise Exception(f'{suffix} {i}: token mismatch {TOK.findall(original)} vs {TOK.findall(vi)}')
  if vi.count('▼')>3:notes.append((i,'over breaks',vi))
  if '\t' in vi or '\n' in vi or '\r' in vi:notes.append((i,'control bytes',vi))
  if len(vi.split('▼'))>4:notes.append((i,'over lines',vi))
  lens=[len(TOK.sub('',x)) for x in vi.split('▼')]
  if max(lens)>34:notes.append((i,'long line '+str(lens),vi))
  if 'max_utf8_bytes' in r and r['max_utf8_bytes'] is not None and len(vi.encode('utf-8'))>r['max_utf8_bytes']:
   notes.append((i,'utf8 bytes limit',vi))
  r['vi']=vi
 if notes:
  print('\nNOTES',suffix)
  for n in notes:print(*n,sep=' | ')
 else: print(suffix,'QA clean')
 file.write_text('\n'.join(json.dumps(x,ensure_ascii=False,separators=(',',':')) for x in rows)+'\n',encoding='utf-8')
 (HOME/f'vi_{suffix.replace(".","_")}.txt').write_text('\n'.join(x['vi'] for x in rows)+'\n',encoding='utf-8')