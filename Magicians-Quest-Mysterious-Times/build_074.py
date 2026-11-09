#!/usr/bin/env python3
"""Magician's Quest checkpoint 074: strictly additive source-preserving Vietnamese localization.

Usage:
  python build_074.py --previous MagiciansQuest-VietHoa-Checkpoint-073.zip \
      --output MagiciansQuest-VietHoa-Checkpoint-074.zip

The two UTF-8 source tables mq074_vi_001_116.txt and mq074_vi_117_235.txt
must sit next to this script. Every numbered line is INDEX|VIETNAMESE_TEXT.
"""
import argparse
import collections
import csv
import io
import json
import pathlib
import re
import unicodedata
import zipfile

OLD = 'MagiciansQuest_073/'
NEW = 'MagiciansQuest_074/'
BATCH = ('0042.001', '0042.002')
TOKEN = re.compile(r"\$\d{3}(?:'[\d-]+)*;")
PREFIX = re.compile(r"^(?:\$(?:024|023|022|034|040)(?:'[\d-]+)*;)+")
BASE = pathlib.Path(__file__).resolve().parent


def load_translations():
    mapping = {}
    for name in ('mq074_vi_001_116.txt', 'mq074_vi_117_235.txt'):
        for line in (BASE / name).read_text(encoding='utf-8').splitlines():
            if not line.strip():
                continue
            idx, vi = line.split('|', 1)
            idx = int(idx)
            assert idx not in mapping, f'Duplicate index {idx}'
            mapping[idx] = vi
    assert list(sorted(mapping)) == list(range(1, 236)), 'Must have 235 translated patterns'
    return mapping


def line_content(raw):
    """Only remove the speaker-control prefix; never remove inline source tokens."""
    m = PREFIX.match(raw)
    return (m.group(0), raw[m.end():]) if m else ('', raw)


def verify_entry(src, vi, idx):
    if not vi or unicodedata.normalize('NFC', vi) != vi:
        raise ValueError(f'Index {idx}: empty or non-NFC Vietnamese')
    if TOKEN.findall(src) != TOKEN.findall(vi):
        raise ValueError(f'Index {idx}: token mismatch: {TOKEN.findall(src)} != {TOKEN.findall(vi)}')
    if vi.count('▼') > 3:
        raise ValueError(f'Index {idx}: too many dialogue breaks')
    for segment in vi.split('▼'):
        if len(TOKEN.sub('', segment)) > 34:
            raise ValueError(f'Index {idx}: static segment too long: {segment!r}')


def build(previous, output):
    mapping = load_translations()
    with zipfile.ZipFile(previous) as z:
        if z.testzip() is not None:
            raise ValueError('Source ZIP failed CRC verification')
        entries = {n.replace(OLD, NEW, 1): z.read(n) for n in z.namelist() if n.startswith(OLD)}
        source_contents = {}
        for s in BATCH:
            name = NEW + f'translation/04-thoai/talkfigs__0eng__data__{s}.jsonl'
            source_contents[s] = [json.loads(x) for x in entries[name].decode('utf-8').splitlines()]
        rows = [r for s in BATCH for r in source_contents[s]]
        keys = list(dict.fromkeys(TOKEN.sub('', r['en']) for r in rows))
        assert len(rows) == 240 and len(keys) == 235
        match = {key: i for i, key in enumerate(keys, 1)}
        corrections = 0
        delta = []
        for s in BATCH:
            rows_s = source_contents[s]
            assert len(rows_s) == 120
            manual = io.StringIO()
            writer = csv.writer(manual, delimiter='\t', lineterminator='\n')
            writer.writerow(['id', 'en', 'vi', 'ctx'])
            for r in rows_s:
                assert r['vi'] is None, f'Expected source translation blank: {r["id"]}'
                i = match[TOKEN.sub('', r['en'])]
                prefix, en_body = line_content(r['en'])
                vi_body = mapping[i]
                # One answer-option EN text occurs both with and without a branch tag.
                if i == 79 and not TOKEN.findall(en_body):
                    assert vi_body.endswith("$019'-1;")
                    vi_body = vi_body[:-len("$019'-1;")]
                    corrections += 1
                verify_entry(en_body, vi_body, i)
                r['vi'] = prefix + vi_body
                assert TOKEN.findall(r['en']) == TOKEN.findall(r['vi']), r['id']
                writer.writerow([r['id'], r['en'], r['vi'], r['ctx']])
                delta.append({k: r[k] for k in ('id', 'en', 'vi', 'ctx')})
            name = NEW + f'translation/04-thoai/talkfigs__0eng__data__{s}.jsonl'
            entries[name] = ('\n'.join(json.dumps({k:r[k] for k in ('id','en','vi','ctx')},ensure_ascii=False,separators=(',',':')) for r in rows_s)+'\n').encode('utf-8')
            entries[NEW + f'manual_{s.replace(".", "_")}.tsv'] = manual.getvalue().encode('utf-8')
        entries[NEW+'DELTA-074.jsonl'] = ('\n'.join(json.dumps(r,ensure_ascii=False,separators=(',',':')) for r in delta)+'\n').encode('utf-8')
        assert len(delta) == 240
        # Comprehensive source/diff QA for all localized JSONL records.
        translated_before=translated_after=total=nj=0
        modified=[]
        with zipfile.ZipFile(previous) as oldzip:
            for oldname in oldzip.namelist():
                if not ('/translation/' in oldname and oldname.endswith('.jsonl')):
                    continue
                nj+=1
                newname=oldname.replace(OLD,NEW,1)
                raw=oldzip.read(oldname)
                rows_old=[json.loads(r) for r in raw.decode('utf-8').splitlines()]
                rows_new=[json.loads(r) for r in entries[newname].decode('utf-8').splitlines()]
                assert len(rows_new)==len(rows_old), oldname
                if oldname.replace(OLD,'',1).endswith(tuple(f'{s}.jsonl' for s in BATCH)):
                    modified.append(newname)
                else:
                    assert raw==entries[newname], f'Unintended change outside batch: {oldname}'
                for old,new in zip(rows_old,rows_new):
                    total+=1
                    for field in set(old)|set(new):
                        if field != 'vi': assert old.get(field)==new.get(field), (field,old['id'])
                    translated_before+=bool(old.get('vi'))
                    translated_after+=bool(new.get('vi'))
                    if old.get('vi'): assert old['vi']==new['vi']
                    else: assert new['vi'] is None or new['id'] in {r['id'] for r in delta}
        assert (nj,total,translated_before,translated_after)==(501,55976,19458,19698),(nj,total,translated_before,translated_after)
        assert len(modified)==2
        assert corrections==1
        percent=round(100*translated_after/total,2)
        qp=f'''# QA — Checkpoint 074 (09/11/2026)

- **PASS: 501 tệp JSONL / 55.976 bản ghi** được đối chiếu checkpoint 073.
- Mục đã dịch: **19.458 → 19.698 / 55.976 ({percent:.2f}%)**; +240 trang mới.
- `0042.001`: **120/120**; `0042.002`: **120/120**.
- Có **235 mẫu EN riêng** trong 240 trang; chỉ **15 mẫu** có câu trùng tiếng Anh từng dịch, **220 mẫu** được biên tập mới. Tất cả 240 trang dịch thủ công hoặc đối chiếu.
- 499 JSONL ngoài phạm vi hai tệp đích giữ **byte-identical**; mọi `id`, `en`, `ctx` và các trường khác đều được bảo toàn.
- 19.458 trường `vi` đã có từ checkpoint trước không thay đổi; chỉ 240 `vi` từ `null` sang bản dịch tiếng Việt.
- Giữ đúng thứ tự và giá trị token `$...;`, bao gồm biến `$500;`, `$503;`, `$507;`, `$540;`, `$550;`, `$019;`, `$073;`.
- Phân biệt một lựa chọn `Yes, that's right.` có/không có `$019'-1;` để không chèn thêm mã không có trong nguồn.
- 240 câu mới đạt NFC, tối đa 3 dấu ngắt `▼`, tối đa 34 ký tự tĩnh trên từng phân đoạn.
- Kiểm tra CRC ZIP. **Chưa kiểm thử trực tiếp trên ROM NDS, chưa chứng thực độ rộng biến động sau khi thay thế token.**
'''
        hand=f'''# Magician’s Quest — Checkpoint 074 (09/11/2026)

**19.698 / 55.976 ({percent:.2f}%)** · hội thoại NPC: **16.573 / 52.608**.

- Đã dịch `talkfigs__0eng__data__0042.001.jsonl` và `0042.002.jsonl`: **240/240 trang**.
- Nội dung: quà sinh nhật, nhà cửa/nội thất, uống trà, huýt sáo, học nhóm, chuyển trường, bệnh tật, đổi vật dụng, tham vọng kiếm tiền.
- Có 235 mẫu EN riêng: 15 mẫu khớp dữ liệu cũ, 220 mẫu biên tập mới.
- Bàn giao: `DELTA-074.jsonl`, 2 `manual_0042_*.tsv`, bản đồ dịch `mq074_vi_*.txt`, `build_074.py`, `qa_074.py`, `QA-074.md`.
- QA: **PASS 501 JSONL / 55.976** bản ghi, chỉ thay đổi 240 trường `vi`; 499 JSONL còn lại giữ nguyên byte.
- Nguồn đợt 075: `0042.003` + `0042.004` (120 + 120, chưa dịch).
- ZIP đầy đủ: `/Dịch giả lập/MagiciansQuest-VietHoa-Checkpoint-074.zip`.
- **Chưa chạy thử trên ROM NDS**.
'''
        entries[NEW+'QA-074.md']=qp.encode('utf-8')
        entries[NEW+'CHECKPOINT-2026-11-09-DOT-74.md']=hand.encode('utf-8')
        readme='''**Checkpoint mới nhất: 074 (09/11/2026) — 19.698 / 55.976 (35,19%).** +240 trang thoại NPC (`0042.001`, `0042.002`). Có 235 mẫu EN riêng, 220 mẫu mới; QA 501 JSONL PASS. Xem `CHECKPOINT-2026-11-09-DOT-74.md`, `QA-074.md`, `DELTA-074.jsonl`. Đợt 075: `0042.003` + `0042.004`.\n\n'''
        newhandoff='''## Checkpoint 074 — 09/11/2026

- **19.698/55.976 (35,19%)**, thoại NPC **16.573/52.608**, tăng 240 trang từ 073.
- Hoàn thành `0042.001` + `0042.002` (120 trang/tệp), 235 mẫu EN riêng: 220 mẫu dịch mới, 15 mẫu có bản dịch trùng từ trước.
- QA toàn bộ 501 JSONL / 55.976: 19.458 bản dịch cũ nguyên vẹn; chỉ thêm 240 `vi`. Token NDS và giới hạn dòng tĩnh đạt.
- ZIP bàn giao: `MagiciansQuest-VietHoa-Checkpoint-074.zip` trong Thư viện `/Dịch giả lập`.
- Tiếp theo `0042.003` + `0042.004` (nguồn sẵn, mỗi tệp 120 trang).
- Chưa thử trực tiếp trên ROM NDS.

'''
        entries[NEW+'README.md']=(readme+entries[NEW+'README.md'].decode('utf-8')).encode('utf-8')
        entries[NEW+'BAN_GIAO.md']=(newhandoff+entries[NEW+'BAN_GIAO.md'].decode('utf-8')).encode('utf-8')
        for name in ('mq074_vi_001_116.txt','mq074_vi_117_235.txt','build_074.py','qa_074.py'):
            entries[NEW+name]=(BASE/name).read_bytes()
        with zipfile.ZipFile(output,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=7) as dst:
            for name,data in sorted(entries.items()): dst.writestr(name,data)
    with zipfile.ZipFile(output) as final:
        assert final.testzip() is None
        print(f'CHECKPOINT-074 PASS: {len(final.namelist())} archive entries, {nj} JSONL files, {total} records, {translated_before}->{translated_after} translated.')
    return output

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--previous',type=pathlib.Path,default=BASE/'MagiciansQuest-VietHoa-Checkpoint-073.zip')
    parser.add_argument('--output',type=pathlib.Path,default=BASE/'MagiciansQuest-VietHoa-Checkpoint-074.zip')
    args=parser.parse_args()
    build(args.previous,args.output)
