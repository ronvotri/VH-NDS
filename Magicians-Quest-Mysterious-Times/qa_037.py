#!/usr/bin/env python3
"""Full strict QA for Magician's Quest checkpoint 037 vs 036 ZIP."""
import json, re, zipfile, unicodedata
from pathlib import Path
ROOT=Path(__file__).resolve().parent
BASE=Path(__file__).resolve().parents[2]/'MagiciansQuest-VietHoa-Checkpoint-036.zip'
TOK=re.compile(r"\$\d+(?:'\d+)*;")
TARGET={
  'translation/04-thoai/talkfigs__0eng__data__0031.002.jsonl':120,
  'translation/04-thoai/talkfigs__0eng__data__0031.003.jsonl':120,
}
assert BASE.is_file(), BASE
files=sorted((ROOT/'translation').rglob('*.jsonl'))
count=count_old=count_new=0;file_count=0;changes=[]
with zipfile.ZipFile(BASE) as z:
    root_names={n.split('/',1)[1]:n for n in z.namelist() if '/translation/' in n and n.lower().endswith('.jsonl')}
    current={p.relative_to(ROOT).as_posix():p for p in files}
    assert set(root_names)==set(current),(len(root_names),len(current),set(root_names)^set(current))
    for relative,p in current.items():
        base_lines=z.read(root_names[relative]).decode('utf-8').splitlines()
        new_lines=p.read_text('utf-8').splitlines()
        assert len(base_lines)==len(new_lines),(relative,len(base_lines),len(new_lines))
        for lineno,(b,n) in enumerate(zip(base_lines,new_lines),1):
            old=json.loads(b);cur=json.loads(n)
            assert list(old)==list(cur),(relative,lineno,'schema')
            assert all(old[k]==cur[k] for k in old if k!='vi'),(relative,lineno,'non-VI change')
            assert cur.get('en')==old.get('en')
            assert cur.get('id')==old.get('id')
            assert cur.get('ctx')==old.get('ctx')
            if old.get('vi') is not None:
                assert old['vi']==cur['vi'],(relative,lineno,'previous VI overwritten')
                count_old+=1
            elif cur.get('vi') is not None:
                assert relative in TARGET,(relative,lineno,'unexpected translation')
                count_new+=1
                changes.append((relative,lineno,old,cur))
            count+=1
            if cur.get('vi') is not None and cur.get('en') is not None:
                assert TOK.findall(cur['en'])==TOK.findall(cur['vi']),(relative,lineno,'token drift')
        file_count+=1
    assert count==55976,count
    assert file_count==501,file_count
    assert count_old==10808,count_old
    assert count_new==240,count_new
    for relative,want in TARGET.items():
        assert sum(x[0]==relative for x in changes)==want
    for relative,lineno,old,cur in changes:
        v=cur['vi']
        assert v==unicodedata.normalize('NFC',v),(relative,lineno,'non-NFC')
        assert not any(x in v for x in '\r\n\t'),(relative,lineno,'control chars')
        assert v.count('▼')<=3,(relative,lineno,'too many line breaks')
        for segment in v.split('▼'):
            assert len(TOK.sub('',segment))<=34,(relative,lineno,'too wide',segment)
        if cur.get('max_utf8_bytes') is not None:
            assert len(v.encode('utf-8'))<=int(cur['max_utf8_bytes']),(relative,lineno,'byte limit')
print(f'PASS {file_count} JSONL / {count} rows / old={count_old} / new={count_new} / total={count_old+count_new}')