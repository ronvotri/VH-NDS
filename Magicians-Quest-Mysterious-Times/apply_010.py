#!/usr/bin/env python3
"""Apply manually translated 0020.003-004 to checkpoint 009, preserving engine tokens.
Use on an unmodified copy of the checkpoint 009 directory (all `vi` should be null in these files).
Manual lines use ¤ for source-position engine markers not part of leading NPC command prefix.
"""
from pathlib import Path
import json, re, unicodedata
ROOT=Path(__file__).resolve().parent
TOK=re.compile(r"\$\d{3}(?:'[^;\r\n\t]*)?;")
PREFIX=re.compile(r"^((?:\$(?:024|023|022|034)'[^;\r\n\t]*;)+)")
for chunk in ('003','004'):
    src=ROOT/'translation'/'04-thoai'/f'talkfigs__0eng__data__0020.{chunk}.jsonl'
    rows=[json.loads(x) for x in src.read_text(encoding='utf-8').splitlines()]
    lines=(ROOT/f'manual_0020_{chunk}.txt').read_text(encoding='utf-8').splitlines()
    if len(rows)!=120 or len(lines)!=120:raise ValueError(f'Expected 120: {chunk}: {len(rows)}, {len(lines)}')
    for i,(row,manual) in enumerate(zip(rows,lines),1):
        if row['vi'] is not None:raise ValueError(f'Nonempty VI at {chunk} row {i}')
        match=PREFIX.match(row['en']); prefix=match.group(1) if match else ''
        tail=row['en'][len(prefix):]
        needed=TOK.findall(tail)
        if manual.count('¤')!=len(needed):raise ValueError(f'Placeholders at {chunk} row {i}: {manual.count("¤")}/{len(needed)}')
        generated=manual
        for marker in needed:generated=generated.replace('¤',marker,1)
        generated=unicodedata.normalize('NFC',prefix+generated)
        if TOK.findall(generated)!=TOK.findall(row['en']):raise ValueError(f'Token mismatch {chunk} row {i}')
        if generated.count('▼')>max(2,row['en'].count('▼')):raise ValueError(f'Visual lines {chunk} row {i}')
        if any(c in generated for c in '\n\r\t'):raise ValueError(f'Bad whitespace {chunk} row {i}')
        if row.get('max_utf8_bytes') is not None and len(generated.encode('utf-8'))>row['max_utf8_bytes']:
            raise ValueError(f'Byte overflow {chunk} row {i}')
        lenses=[len(TOK.sub('',line).strip()) for line in generated.split('▼')]
        if max(lenses)>34: raise ValueError(f'Long line {chunk} row {i} len {max(lenses)}')
        row['vi']=generated
    src.write_text(''.join(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n' for x in rows),encoding='utf-8')
    print('Applied',src.name,len(rows))