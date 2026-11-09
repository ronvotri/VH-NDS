#!/usr/bin/env python3
"""Áp 47 cập nhật A35 vào 26 CSV nhóm A từ ZIP checkpoint A34.
Dùng: python apply_a35.py /duong-dan/A34.zip /thu-muc-xuat
Yêu cầu bản A34 nguồn có các tệp A_MO_TA_LA_BAI_01.csv ... 26.csv.
"""
import sys, csv, io, zipfile, pathlib, base64, zlib, json
if len(sys.argv) != 3:
    sys.exit(__doc__)
archive, outdir = sys.argv[1:]
root=pathlib.Path(__file__).resolve().parents[1]
data=(root/"translations/A35_patch.json.zlib.b64").read_text(encoding="ascii").strip()
patch=json.loads(zlib.decompress(base64.b64decode(data)).decode("utf-8"))
out=pathlib.Path(outdir);out.mkdir(parents=True,exist_ok=True)
updated=set()
with zipfile.ZipFile(archive) as z:
  for name in z.namelist():
    if not name.startswith("A_MO_TA_LA_BAI_") or not name.endswith(".csv"):continue
    rows=list(csv.DictReader(io.StringIO(z.read(name).decode("utf-8-sig"))))
    if not rows:continue
    headers=list(rows[0])
    for row in rows:
      if row["key"] in patch:
        row["tieng_Viet_MOI"]=patch[row["key"]]
        updated.add(row["key"])
    with (out/name).open("w",encoding="utf-8-sig",newline="") as f:
      writer=csv.DictWriter(f,fieldnames=headers);writer.writeheader();writer.writerows(rows)
missing=set(patch)-updated
assert not missing,f"Thiếu key: {sorted(missing)}"
print(f"Đã áp {len(updated)} bản sửa A35 vào 26 CSV tại {out}")
