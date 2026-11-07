#!/usr/bin/env python3
"""Verify 038 against 037, preserving all non-target fields and existing translations."""
from __future__ import annotations
import sys, json, re, zipfile, unicodedata
from pathlib import Path

ROOT=Path(__file__).resolve().parent
OLD_ZIP=Path(sys.argv[1] if len(sys.argv)>1 else '/mnt/data/MagiciansQuest-VietHoa-Checkpoint-037.zip')
OLD_ROOT='MagiciansQuest_037/'
TARGETS={
    'translation/04-thoai/talkfigs__0eng__data__0031.004.jsonl':120,
    'translation/04-thoai/talkfigs__0eng__data__0031.005.jsonl':101,
}
TOK=re.compile(r'\$\d{3}(?:\'[^;$]+)*;')

def parsed(source:str):
    return [json.loads(s) for s in source.splitlines() if s.strip()]

def fail(msg):
    raise AssertionError(msg)

with zipfile.ZipFile(OLD_ZIP) as z:
    assert z.testzip() is None,'Broken baseline ZIP'
    old_jsonls=sorted(n for n in z.namelist() if n.startswith(OLD_ROOT+'translation/') and n.endswith('.jsonl'))
    files=sorted(str(p.relative_to(ROOT)) for p in (ROOT/'translation').rglob('*.jsonl'))
    assert len(files)==len(old_jsonls)==501,(len(files),len(old_jsonls))
    assert files==[n[len(OLD_ROOT):] for n in old_jsonls],'Changed source file inventory'
    all_rows=translated=old_translated=new_entries=0
    per_group={}
    for filename in files:
        now=parsed((ROOT/filename).read_text('utf-8'))
        before=parsed(z.read(OLD_ROOT+filename).decode('utf-8'))
        assert len(now)==len(before),(filename,len(now),len(before))
        if filename in TARGETS:
            assert len(now)==TARGETS[filename]
        for index,(a,b) in enumerate(zip(before,now)):
            loc=f'{filename} item {index}'
            if a.get('vi'):
                assert a==b,f'Old translated record modified: {loc}'
                old_translated+=1
            else:
                assert all(a.get(k)==b.get(k) for k in a.keys() if k!='vi'),f'Non-VI field modified: {loc}'
                assert set(a)==set(b),f'Field layout modified: {loc}'
                if b.get('vi'):
                    assert filename in TARGETS,f'Unexpected translated record: {loc}'
                    v=b['vi']
                    assert isinstance(v,str) and v and unicodedata.is_normalized('NFC',v),f'Bad VI: {loc}'
                    assert TOK.findall(a['en'])==TOK.findall(v),f'Token mismatch: {loc}'
                    assert not any(ch in v for ch in '\r\n\t'),f'CR/LF/tab: {loc}'
                    assert v.count('▼')<=3,f'Too many breaks: {loc}'
                    assert all(len(TOK.sub('',ln))<=34 for ln in v.split('▼')),f'Overlong line: {loc}'
                    if a.get('max_utf8_bytes') is not None:
                        assert len(v.encode('utf-8')) <= a['max_utf8_bytes'],f'Byte overrun: {loc}'
                    new_entries+=1
            all_rows+=1
            translated+=bool(b.get('vi'))
            group=filename.split('/')[1]
            if group not in per_group:per_group[group]=[0,0]
            per_group[group][0]+=1
            per_group[group][1]+=bool(b.get('vi'))
    assert (all_rows,old_translated,new_entries,translated)==(55976,11048,221,11269),(all_rows,old_translated,new_entries,translated)
    assert per_group['04-thoai']==[52608,8144],per_group
    delta=parsed((ROOT/'DELTA-038.jsonl').read_text('utf-8'))
    assert len(delta)==221
    assert set(x['id'] for x in delta)==set(row['id'] for p in TARGETS for row in parsed((ROOT/p).read_text('utf-8')))
    for x in delta:
        assert not x['old_vi'] and x['vi']

print('PASS: 501 JSONL / 55,976 records. +221 vi, 11,048 preserved, total 11,269 (20.13%).')
print('Dialogue: 8,144 / 52,608. Tokens, ID, context, byte constraints and line lengths PASS.')