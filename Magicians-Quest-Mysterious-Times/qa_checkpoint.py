"""Lightweight QA for translated JSONL without the clean USA NDS ROM.
Full ROM/font check still requires `python mqhandoff.py check` with MQ_ROM.
"""
from pathlib import Path
from collections import Counter
import json, re, unicodedata

root=Path(__file__).resolve().parent/'translation'
CONTROL=re.compile(r"\[\$[A-Za-z_][A-Za-z0-9_]*\]|\$[0-9]{3}(?:'[^;\r\n\t]*)?;|%(?:[0-9]+\$)?[-+0-9.]*[sdifux%]|[\r\n▼]")
counts=Counter(); errors=[]; ids=set()
for file in sorted(root.rglob('*.jsonl')):
    for n, line in enumerate(file.read_text(encoding='utf8').splitlines(),1):
        item=json.loads(line)
        id_=item['id']
        if id_ in ids:errors.append(f'{id_}: duplicated ID')
        ids.add(id_)
        en=item['en']; vi=item['vi']
        if vi is None:continue
        counts[file.parent.name]+=1
        if not isinstance(vi,str) or not vi.strip():errors.append(f'{id_}: blank translation')
        if unicodedata.normalize('NFC',vi)!=vi:errors.append(f'{id_}: not NFC')
        expected=CONTROL.findall(en); actual=CONTROL.findall(vi)
        if '#page:' in id_:
            expected=[x for x in expected if x!='▼']
            actual=[x for x in actual if x!='▼']
            if vi.count('▼')>max(2,en.count('▼')):
                errors.append(f'{id_}: too many visual lines')
        if expected!=actual:errors.append(f'{id_}: control codes changed')
        if item.get('max_utf8_bytes') is not None and len(vi.encode('utf8'))>item['max_utf8_bytes']:
            errors.append(f'{id_}: exceeded UTF-8 byte limit')
print(f'Populated Vietnamese fields: {sum(counts.values())}, by group: {dict(counts)}')
if errors:
    print(f'{len(errors)} errors:')
    for error in errors[:50]:print(' -',error)
    raise SystemExit(1)
print('PASS: controls, bytes, basic structure, Unicode NFC.')