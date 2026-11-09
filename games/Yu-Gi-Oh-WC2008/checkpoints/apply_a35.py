#!/usr/bin/env python3
"""Phục hồi 26 CSV bản A35 từ 26 CSV nền A34 (thư mục hoặc ZIP).
Dùng: python apply_a35.py <duong_dan_nen_A34> <thu_muc_xuat>
"""
import sys, csv, io, zipfile, pathlib, base64, zlib, json
if len(sys.argv)!=3: sys.exit(__doc__)
inp=pathlib.Path(sys.argv[1]); out=pathlib.Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=True)
root=pathlib.Path(__file__).resolve().parents[1]
payload=(root/"translations/A35_patch.json.zlib.b64").read_text(encoding="ascii").strip()
patch=json.loads(zlib.decompress(base64.b64decode(payload)).decode("utf-8"))
applied=set()
for i in range(1,27):
    name=f"A_MO_TA_LA_BAI_{i:02d}.csv"
    if inp.is_dir():
        with (inp/name).open(encoding="utf-8-sig",newline="") as f: rows=list(csv.DictReader(f))
    else:
        with zipfile.ZipFile(inp) as z: rows=list(csv.DictReader(io.StringIO(z.read(name).decode("utf-8-sig"))))
    if not rows: raise ValueError("CSV rỗng: "+name)
    fields=list(rows[0].keys())
    for r in rows:
        if r["key"] in patch:
            r["tieng_Viet_MOI"]=patch[r["key"]]
            applied.add(r["key"])
        if not r["tieng_Viet_MOI"] or len(r["tieng_Viet_MOI"])>int(r["toi_da_ky_tu"]):
            raise ValueError("Dòng trống/quá dài: "+r["key"])
    with (out/name).open("w",encoding="utf-8-sig",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
assert applied==set(patch), f"Thiếu key cập nhật: {sorted(set(patch)-applied)}"
print(f"A35 hoàn thành: {len(applied)} cập nhật trong 26 CSV tại {out}")
