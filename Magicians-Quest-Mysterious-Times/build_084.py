#!/usr/bin/env python3
"""Build Magician's Quest (NDS) Vietnamese full checkpoint 084 from full checkpoint 083.

Run: python build_084.py --previous /mnt/data/MagiciansQuest-VietHoa-Checkpoint-083.zip \
         --output /mnt/data/MagiciansQuest-VietHoa-Checkpoint-084.zip
"""
from __future__ import annotations
import argparse, collections, csv, hashlib, io, json, pathlib, re, unicodedata, zipfile

BASE = pathlib.Path(__file__).resolve().parent
OLD, NEW = 'MagiciansQuest_083/', 'MagiciansQuest_084/'
TARGET = ('0042.021', '0042.022')
NEXT = {'0042.023': 111, '0043.001': 120}
TOTAL = 55976
BASE_COUNT = 21858
NPC_BASE = 18733
TOKEN = re.compile(r"\$\d{3}(?:'[-\d]+)*;")
PREFIX = re.compile(r"^(?:\$(?:024|023|022|034|040|004)(?:'[-\d]+)*;)+")

def body(value):
    return PREFIX.sub('', value)

def verify(en, vi, name):
    if not isinstance(vi, str) or not vi:
        raise ValueError(f'Vietnamese is empty at {name}')
    if vi != unicodedata.normalize('NFC', vi):
        raise ValueError(f'Non-NFC at {name}')
    if TOKEN.findall(en) != TOKEN.findall(vi):
        raise ValueError(f'NDS tokens changed at {name}: {TOKEN.findall(en)} != {TOKEN.findall(vi)}')
    if vi.count('▼') > 3:
        raise ValueError(f'Too many dialogue segment breaks at {name}')
    if any(len(TOKEN.sub('', part)) > 34 for part in vi.split('▼')):
        raise ValueError(f'Too many static characters in segment at {name}')
    if any(k in vi for k in ('\n', '\r', '\t')):
        raise ValueError(f'Unexpected control character at {name}')

def build(previous: pathlib.Path, output: pathlib.Path):
    manual = {}
    for line in (BASE/'mq084_new_translations.txt').read_text('utf-8').splitlines():
        if not line: continue
        num, vi = line.split('|', 1)
        idx = int(num)
        if idx in manual: raise ValueError(f'Duplicate translation index {idx}')
        manual[idx] = vi
    assert sorted(manual) == list(range(1, 232)), len(manual)
    with zipfile.ZipFile(previous) as original:
        assert original.testzip() is None
        names = original.namelist()
        assert len(set(names)) == len(names)
        assert all(name.startswith(OLD) for name in names)
        files = {name.replace(OLD, NEW, 1): original.read(name) for name in names}
        translations_before = collections.defaultdict(collections.Counter)
        for path, content in files.items():
            if '/translation/' not in path or not path.endswith('.jsonl'): continue
            for line in content.decode('utf-8').splitlines():
                row = json.loads(line)
                if isinstance(row['vi'], str) and TOKEN.findall(row['en']) == TOKEN.findall(row['vi']):
                    translations_before[body(row['en'])][body(row['vi'])] += 1
        sources = {}
        for key in TARGET:
            filename = NEW+f'translation/04-thoai/talkfigs__0eng__data__{key}.jsonl'
            rows = [json.loads(l) for l in files[filename].decode('utf-8').splitlines()]
            assert len(rows) == 120 and all(r['vi'] is None for r in rows), key
            sources[key] = rows
        unique = list(dict.fromkeys(body(r['en']) for key in TARGET for r in sources[key]))
        assert len(unique) == 231
        reuse_count = sum(bool(translations_before[text]) for text in unique)
        assert reuse_count == 0, f'The assumed source novelty changed: {reuse_count} matches'
        translations = {}
        for index, en in enumerate(unique, 1):
            vi = manual[index]
            verify(en, vi, f'pattern {index}')
            translations[en] = vi
        delta = []
        for key in TARGET:
            rows = sources[key]
            out = io.StringIO()
            writer = csv.writer(out, delimiter='\t', lineterminator='\n')
            writer.writerow(('id','en','vi','ctx'))
            for row in rows:
                english = row['en']
                prefix = english[:len(english)-len(body(english))]
                vietnamese = prefix + translations[body(english)]
                verify(english, vietnamese, row['id'])
                row['vi'] = vietnamese
                writer.writerow((row['id'], english, vietnamese, row['ctx']))
                delta.append(row.copy())
            assert len(rows) == 120
            files[NEW+f'translation/04-thoai/talkfigs__0eng__data__{key}.jsonl'] = ''.join(
                json.dumps(row, ensure_ascii=False, separators=(',',':'))+'\n' for row in rows
            ).encode('utf-8')
            files[NEW+f'manual_{key.replace(".","_")}.tsv'] = out.getvalue().encode('utf-8')
            files[NEW+f'vi_{key.replace(".","_")}.txt'] = ''.join(
                row['id']+'\t'+row['vi']+'\n' for row in rows
            ).encode('utf-8')
        files[NEW+'DELTA-084.jsonl'] = ''.join(
            json.dumps(row, ensure_ascii=False, separators=(',',':'))+'\n' for row in delta
        ).encode('utf-8')
        files[NEW+'mq084_new_translations.txt'] = (BASE/'mq084_new_translations.txt').read_bytes()
        files[NEW+'build_084.py'] = pathlib.Path(__file__).read_bytes()
        done = BASE_COUNT+240
        npc = NPC_BASE+240
        pct = f'{done/TOTAL*100:.2f}'
        qa=f'''# QA — Magician's Quest Checkpoint 084 (09/11/2026)

- **PASS:** 501 tệp JSONL / 55.976 bản ghi so với checkpoint 083.
- **{BASE_COUNT:,} → {done:,} / {TOTAL:,} ({pct}%)**: +240 trang thoại NPC, `0042.021` 120/120 và `0042.022` 120/120.
- **231 mẫu tiếng Anh riêng, 231 mẫu dịch mới**, 9 trang lặp trong batch.
- Chỉ hai JSONL đích thay đổi; 499 JSONL khác giữ nguyên từng byte.
- Không sửa {BASE_COUNT:,} bản dịch trước; `id`, `en`, `ctx`, thứ tự và metadata không đổi.
- Các mã NDS `$...;` đúng thứ tự, Unicode NFC, tối đa 3 dấu `▼`, không quá 34 ký tự tĩnh mỗi đoạn.
- Không trộn dữ liệu của các game khác; ZIP CRC PASS và không có tên tệp trùng.
- **Chưa kiểm thử ROM:** giới hạn ký tự tĩnh không bảo đảm kích thước hiển thị khi thay biến hoặc dùng font thực.
- **Nguồn đợt 085:** `0042.023` (111 trang) và `0043.001` (120 trang), trường `vi:null`.
'''
        files[NEW+'QA-084.md'] = qa.encode('utf-8')
        notes=f'''# Magician's Quest — Checkpoint 084

**Ngày:** 09/11/2026  
**Repository:** `ronvotri/VH-NDS` / `Magicians-Quest-Mysterious-Times/`.

- **+240 trang NPC**: `0042.021`, `0042.022` (120 trang mỗi tệp).
- Tổng **{done:,}/55.976 ({pct}%)**; riêng NPC **{npc:,}/52.608**.
- 231 mẫu EN mới, 9 trang lặp trong hai tệp. Nội dung: thế giới lòng đất, những giấc mơ, tiên, ma, người sói, rừng nấm, vòng tròn bí ẩn, sinh vật huyền thoại.
- Dịch có biên tập, ngôi xưng học sinh tớ-cậu; bảo toàn toàn bộ token `$000`, `$500`, `$507`, `$019`, `$073`, `$079` cùng biến tên và lựa chọn.
- Bàn giao: `DELTA-084.jsonl`, `manual_0042_021.tsv`, `manual_0042_022.tsv`, `mq084_new_translations.txt`, `QA-084.md`, `build_084.py`.
- QA 501 JSONL đạt; chưa kiểm thử ROM trực tiếp.
- **Đợt tiếp 085:** `0042.023` (111 trang) và `0043.001` (120 trang), đã có nguồn chưa dịch.
'''
        files[NEW+'CHECKPOINT-2026-11-09-DOT-84.md'] = notes.encode('utf-8')
        top=f'**Checkpoint mới nhất: 084 (09/11/2026) — {done:,}/55.976 ({pct}%).** +240 NPC (`0042.021`, `0042.022`); 231 mẫu thoại biên tập mới. Xem `CHECKPOINT-2026-11-09-DOT-84.md`, `QA-084.md`. Tiếp `0042.023` và `0043.001` (231 trang).\n\n'
        files[NEW+'README.md'] = (top+files[NEW+'README.md'].decode('utf-8')).encode('utf-8')
        hand=f'''## Checkpoint 084 — 09/11/2026

- +240 trang thoại `0042.021`, `0042.022`; tổng {done:,}/55.976 ({pct}%), NPC {npc:,}/52.608.
- 231 mẫu EN mới. QA 501 JSONL / 55.976 bản ghi đạt; 499 JSONL ngoài đợt không đổi byte.
- ZIP đầy đủ, TSV EN–VI, delta, script, QA và nguồn cho 085. Chưa kiểm thử ROM thực tế.
- Tiếp `0042.023` (111 trang) và `0043.001` (120 trang) — 231 trang chưa dịch.

'''
        files[NEW+'BAN_GIAO.md'] = (hand+files[NEW+'BAN_GIAO.md'].decode('utf-8')).encode('utf-8')
        num_files=total=old_done=new_done=changed_files=0
        for name in names:
            if '/translation/' not in name or not name.endswith('.jsonl'): continue
            num_files += 1
            new_name = name.replace(OLD, NEW, 1)
            old_bytes, new_bytes = original.read(name), files[new_name]
            target = any(new_name.endswith(key+'.jsonl') for key in TARGET)
            if target: changed_files += 1
            else: assert old_bytes == new_bytes, f'Changed unrelated translation file: {name}'
            old_rows = [json.loads(s) for s in old_bytes.decode('utf-8').splitlines()]
            new_rows = [json.loads(s) for s in new_bytes.decode('utf-8').splitlines()]
            assert len(old_rows)==len(new_rows), name
            for old, new in zip(old_rows, new_rows):
                total += 1
                assert old.keys() == new.keys() and all(old[k]==new[k] for k in old if k!='vi'), old['id']
                old_done += old['vi'] is not None
                new_done += new['vi'] is not None
                if old['vi'] is not None: assert old['vi'] == new['vi'], old['id']
                elif target: verify(old['en'], new['vi'], old['id'])
                else: assert new['vi'] is None, old['id']
        assert (num_files,total,old_done,new_done,changed_files) == (501,TOTAL,BASE_COUNT,done,2), (num_files,total,old_done,new_done,changed_files)
        for key, expected in NEXT.items():
            file = NEW+f'translation/04-thoai/talkfigs__0eng__data__{key}.jsonl'
            rows = [json.loads(line) for line in files[file].decode('utf-8').splitlines()]
            assert len(rows)==expected and all(row['vi'] is None for row in rows), key
        output.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(output,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=7,allowZip64=True) as zipout:
            for name, raw in sorted(files.items()): zipout.writestr(name, raw)
    with zipfile.ZipFile(output) as final:
        assert final.testzip() is None
        assert len(final.namelist())==len(set(final.namelist()))
        print(f'PASS: {num_files} JSONL, {total} rows, 499 files unchanged, +240 pages; ZIP {len(final.namelist())} entries')
    print('DONE',done,'/',TOTAL,'PERCENT',pct,'NPC',npc,'SIZE',output.stat().st_size,'SHA256',hashlib.sha256(output.read_bytes()).hexdigest())

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--previous',type=pathlib.Path,default=pathlib.Path('/mnt/data/MagiciansQuest-VietHoa-Checkpoint-083.zip'))
    parser.add_argument('--output',type=pathlib.Path,default=pathlib.Path('/mnt/data/MagiciansQuest-VietHoa-Checkpoint-084.zip'))
    args=parser.parse_args()
    build(args.previous,args.output)
