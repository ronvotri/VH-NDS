#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract authentic J-Quiz CP047 Japanese source (no translations added).
Usage: python CHUAN_BI_NGUON_047.py JumpUltimateStars_Japan_BanGiao_Cloud.zip
"""
import argparse
import hashlib
import io
import json
from pathlib import Path
from zipfile import ZipFile

NAME = "06-jquiz-008.jsonl"
SHA = "48c26ae8eb63b3d3272741f93683312ff435ac8fc8995479f96a42045acd0dfc"
ROWS = 2012
START = 518
ANCHORS = {
    513: ("JUS-e1218705022517b32644", "紫龍が中国での修業時代、共に過ごした"),
    514: ("JUS-a8f7e58a4bbaeff42db6", "春麗"),
    515: ("JUS-b98cef068ac64392536b", "夏麗"),
    516: ("JUS-8a74e907afc2edb1c895", "秋麗"),
    517: ("JUS-9250794ffc0f5ee63d3d", "冬麗"),
}

def find(zf, depth=0):
    hits = []
    for info in zf.infolist():
        if info.is_dir() or info.file_size > 80 * 1024 * 1024:
            continue
        name = info.filename.replace("\\", "/")
        if name.rsplit("/", 1)[-1] == NAME:
            hits.append(zf.read(info))
        elif name.lower().endswith(".zip") and depth < 3:
            with ZipFile(io.BytesIO(zf.read(info))) as inner:
                hits.extend(find(inner, depth + 1))
    return hits

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("archive", type=Path)
    ap.add_argument("--limit", type=int, default=700)
    ap.add_argument("--out", type=Path, default=Path("JUS_CP047_NGUON_CHO_DICH.jsonl"))
    args = ap.parse_args()
    with ZipFile(args.archive) as zf:
        hits = find(zf)
    if len(hits) != 1:
        raise ValueError(f"Phải có đúng một {NAME}; tìm thấy {len(hits)}")
    raw = hits[0]
    actual = hashlib.sha256(raw).hexdigest()
    if actual != SHA:
        raise ValueError(f"SHA256 không khớp CP046: {actual}")
    lines = raw.decode("utf-8-sig").splitlines()
    if len(lines) != ROWS:
        raise ValueError(f"Sai số dòng: {len(lines)} thay vì {ROWS}")
    data, ids = [], set()
    for i, line in enumerate(lines):
        x = json.loads(line)
        if not x.get("id") or not x.get("ja") or x.get("row_index", i) != i:
            raise ValueError(f"Sai id/ja/row_index tại {i}")
        if x.get("file", NAME).split("/")[-1] != NAME or x["id"] in ids:
            raise ValueError(f"Sai file/trùng ID tại {i}")
        ids.add(x["id"])
        data.append(x)
    for i, expected in ANCHORS.items():
        if (data[i]["id"], data[i]["ja"]) != expected:
            raise ValueError(f"Điểm nối CP046 không khớp tại dòng {i}")
    if not 1 <= args.limit <= ROWS - START:
        raise ValueError("limit ngoài số dòng còn lại")
    end = START + args.limit
    def quizid(row):
        q = row.get("quiz_context") or []
        return q[0].get("question_index") if q else None
    while end < len(data) and quizid(data[end]) == quizid(data[end-1]):
        end += 1
    if args.out.exists():
        raise FileExistsError(args.out)
    selected = data[START:end]
    txt = "".join(json.dumps(x, ensure_ascii=False) + "\n" for x in selected)
    args.out.write_text(txt, encoding="utf-8")
    report = {
        "checkpoint": "047",
        "status": "SOURCE_ONLY_NOT_TRANSLATED",
        "new_translations": 0,
        "source_sha256": actual,
        "start_row_index": START,
        "last_row_index": end-1,
        "next_row_index": end,
        "selected_ids": len(selected),
        "source_rows": ROWS,
        "extracted_sha256": hashlib.sha256(txt.encode("utf-8")).hexdigest()
    }
    qa = args.out.with_suffix(".qa.json")
    qa.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Đã trích {len(selected)} dòng Nhật: {START}-{end-1}. Chưa dịch.")
    print("JSONL:", args.out, "QA:", qa)

if __name__ == "__main__":
    main()
