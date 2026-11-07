#!/usr/bin/env python3
"""Apply human-reviewed Vietnamese page translations for checkpoint 041.
Keeps every non-vi field byte-equivalent at JSON value level; no source or token changes.
"""
from pathlib import Path
import json,re,unicodedata,csv
BASE=Path(__file__).resolve().parent
TOKEN=re.compile(r"\$[0-9'\-]+;")
PFX=re.compile(r"^(?:\$[0-9'\-]+;)+")
SFX=re.compile(r"(?:\$[0-9'\-]+;)+$")
TARGETS=[('0032.005',120),('0033.001',120)]
def width(s):return len(TOKEN.sub('',s))
def wrap(s,limit=34):
    out=[]
    for part in s.split('▼'):
        cur=''
        protected=re.sub(r"\$000'[345];.*?\$000'1;",lambda m:m.group().replace(' ', '\uE000'),part)
        for word in protected.split():
            candidate=(cur+' '+word) if cur else word
            if width(candidate)<=limit:cur=candidate
            elif cur:
                out.append(cur)
                cur=word
            else:cur=word
        if cur:out.append(cur)
    return '▼'.join(out).replace('\uE000',' ')

def run():
    deltas=[]
    for f,count in TARGETS:
        p=BASE/'translation'/'04-thoai'/f'talkfigs__0eng__data__{f}.jsonl'
        raw=(BASE/f'vi_{f.replace(".","_")}_raw.txt').read_text('utf8').splitlines()
        assert len(raw)==count,(f,'translation lines',len(raw),count)
        rows=[json.loads(line) for line in p.read_text('utf8').splitlines()]
        assert len(rows)==count,(f,'source lines',len(rows),count)
        new_rows=[];vi_lines=[];table=[]
        for i,(row,vi) in enumerate(zip(rows,raw),1):
            assert row.get('vi') in (None,''),(f,i,'already translated')
            en=row['en']
            prefix=PFX.match(en).group() if PFX.match(en) else ''
            # If the translation intentionally places the final initial token itself, don't duplicate it.
            while prefix and vi.startswith(TOKEN.findall(prefix)[-1]):
                prefix=prefix[:-len(TOKEN.findall(prefix)[-1])]
            suffix=SFX.search(en).group() if SFX.search(en) else ''
            # Handle a pure token English string only once.
            if prefix and suffix and len(prefix)==len(en):suffix=''
            new=wrap(prefix+vi+suffix)
            expected=TOKEN.findall(en)
            observed=TOKEN.findall(new)
            if expected!=observed:
                print('TOKEN MISMATCH',f,i,'EN',expected,'VI',observed,'source:',en,'vi:',new)
                raise RuntimeError('Mismatch')
            if new.count('▼')>3:
                print('PAGE OVERFLOW',f,i,new)
                raise RuntimeError('Too many breaks')
            if any(width(line)>34 for line in new.split('▼')):
                print('LINE OVERFLOW',f,i,new)
                raise RuntimeError('Line too long')
            assert all(c not in new for c in ('\t','\r','\n'))
            assert unicodedata.normalize('NFC',new)==new,(f,i,'NFC')
            if row.get('max_utf8_bytes') and len(new.encode('utf8'))>row['max_utf8_bytes']:
                raise RuntimeError(f'Byte limit violation {f} row {i}')
            new_rows.append({**row,'vi':new})
            vi_lines.append(new)
            table.append((i,row['id'],en,new))
            deltas.append({'file':f'04-thoai/{p.name}','id':row['id'],'en':en,'old_vi':row.get('vi'),'vi':new,'ctx':row.get('ctx')})
        p.write_text('\n'.join(json.dumps(x,ensure_ascii=False,separators=(',',':')) for x in new_rows)+'\n','utf8')
        (BASE/f'vi_{f.replace(".","_")}.txt').write_text('\n'.join(vi_lines)+'\n','utf8')
        with (BASE/f'manual_{f.replace(".","_")}.tsv').open('w',encoding='utf8',newline='') as w:
            cw=csv.writer(w,delimiter='\t');cw.writerow(['index','id','en','vi']);cw.writerows(table)
        print('Translated',f,len(vi_lines),'lines', 'average visible chars',round(sum(width(s) for s in vi_lines)/count,1))
    (BASE/'DELTA-041.jsonl').write_text('\n'.join(json.dumps(x,ensure_ascii=False,separators=(',',':')) for x in deltas)+'\n','utf8')
if __name__=='__main__':run()