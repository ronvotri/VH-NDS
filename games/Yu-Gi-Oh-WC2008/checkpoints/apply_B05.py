#!/usr/bin/env python3
"""Regenerate B09+B10 full translated CSVs from A35/B04 unmodified story sources.
Run: python apply_B05.py [path_to_repo_root_or_source_B_to_G] [output_directory]
"""
import csv, pathlib, json, bz2, base64, sys
if len(sys.argv)!=3: sys.exit(__doc__)
inp=pathlib.Path(sys.argv[1]);out=pathlib.Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=True)
here=pathlib.Path(__file__).resolve().parents[1]
if (inp/'games/Yu-Gi-Oh-WC2008/translations/source_B_to_G').is_dir():inp=inp/'games/Yu-Gi-Oh-WC2008/translations/source_B_to_G'
blob=(here/'translations/story_B05/B05_patch.json.bz2.b64').read_text(encoding='ascii').strip()
data=json.loads(bz2.decompress(base64.b64decode(blob)).decode('utf-8'))
assert len(data)==300, len(data)
applied=set()
for i in (9,10):
    src=inp/f'B_COT_TRUYEN_{i:02d}.csv'
    with src.open(encoding='utf-8-sig',newline='') as f: rows=list(csv.DictReader(f))
    assert len(rows)==150,(src,len(rows))
    fields=list(rows[0])
    for row in rows:
        k=row['key'];assert k in data,k
        assert not row['tieng_Viet_MOI'],k
        row['tieng_Viet_MOI']=data[k]
        applied.add(k)
    with (out/src.name).open('w',encoding='utf-8-sig',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=fields);writer.writeheader();writer.writerows(rows)
assert applied==set(data)
print('PASS: restored',len(applied),'translated B05 story rows to',out)
