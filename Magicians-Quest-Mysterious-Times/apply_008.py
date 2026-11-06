#!/usr/bin/env python3
"""Checkpoint 008: integrate 178 manually translated pages; only `vi` changes."""
from pathlib import Path
import json, re, unicodedata
ROOT=Path(__file__).resolve().parent
TOK=re.compile(r"\$\d{3}(?:'[^;\r\n\t]*)?;")
START=re.compile(r"^((?:\$(?:024|023|022)'[^;\r\n\t]*;)+)")
entries=[]
for group in ('0010','0011'):
    p=ROOT/'translation'/'04-thoai'/f'talkfigs__0eng__data__{group}.001.jsonl'
    rows=[json.loads(s) for s in p.read_text(encoding='utf-8').splitlines()]
    texts=(ROOT/f'manual_{group}.txt').read_text(encoding='utf-8').splitlines()
    assert len(rows)==len(texts),(group,len(rows),len(texts))
    for index,(row,vi) in enumerate(zip(rows,texts),1):
        assert row['vi'] is None,(group,index)
        leading=START.match(row['en'])
        prefix=leading.group(1) if leading else ''
        if "$503'??;" in vi:
            matching=[t for t in TOK.findall(row['en']) if t.startswith("$503'")]
            if len(matching)!=1:raise ValueError(f'Name token: {group} {index} {matching}')
            vi=vi.replace("$503'??;",matching[0])
        vi=unicodedata.normalize('NFC',prefix+vi)
        if TOK.findall(row['en'])!=TOK.findall(vi):
            raise ValueError(f'Token mismatch: {group} {index}: {TOK.findall(row["en"])} != {TOK.findall(vi)}')
        if vi.count('▼')>max(2,row['en'].count('▼')):
            raise ValueError(f'Too many newlines: {group} {index}')
        if any(x in vi for x in ('\r','\n','\t')):
            raise ValueError(f'Invalid whitespace control: {group} {index}')
        if row.get('max_utf8_bytes') is not None and len(vi.encode('utf-8'))>row['max_utf8_bytes']:
            raise ValueError(f'Overflow: {group} {index}')
        row['vi']=vi
        entries.append({'file':str(p.relative_to(ROOT/'translation')),'id':row['id'],'en':row['en'],'vi':vi,'ctx':row.get('ctx')})
    p.write_text(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in rows),encoding='utf-8')
(ROOT/'DELTA-008.jsonl').write_text(''.join(json.dumps(e,ensure_ascii=False,separators=(',',':'))+'\n' for e in entries),encoding='utf-8')
print('Updated',len(entries),'pages')