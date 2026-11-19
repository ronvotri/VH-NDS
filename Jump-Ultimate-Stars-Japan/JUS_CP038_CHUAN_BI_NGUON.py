#!/usr/bin/env python3
"""Prepare the next untranslated J-Quiz batch from the original JUS handover.

Usage:
  python JUS_CP038_CHUAN_BI_NGUON.py JumpUltimateStars_Japan_BanGiao_Cloud.zip
  python JUS_CP038_CHUAN_BI_NGUON.py path/to/06-jquiz-005.jsonl --limit 650

Preparation only; this script NEVER translates or patches a ROM.
"""
import argparse
import hashlib
import io
import json
from pathlib import Path
from zipfile import ZipFile

TARGET = '06-jquiz-005.jsonl'
ANCHORS = (
    'JUS-aee2d23133ad709c8dea',
    'JUS-354ef70d9c6985abe4d6',
    'JUS-4ee9b3c3363174367764',
    'JUS-f219b7b67329d087a357',
)
MAX_INNER_BYTES = 70 * 1024 * 1024


def from_zip(archive, label, depth=0):
    matches = []
    with ZipFile(archive) as zf:
        for entry in zf.infolist():
            if entry.is_dir():
                continue
            name = entry.filename.replace('\\', '/')
            if name.rsplit('/', 1)[-1] == TARGET:
                if entry.file_size > MAX_INNER_BYTES:
                    raise ValueError('File nguồn vượt giới hạn an toàn: ' + name)
                matches.append((label + '::' + name, zf.read(entry)))
            elif depth < 2 and name.lower().endswith('.zip'):
                if entry.file_size <= MAX_INNER_BYTES:
                    matches.extend(from_zip(io.BytesIO(zf.read(entry)), label + '::' + name, depth + 1))
    return matches


def get_source(path):
    if path.is_dir():
        matches = [(str(p), p.read_bytes()) for p in path.rglob(TARGET)]
    elif path.name == TARGET:
        matches = [(str(path), path.read_bytes())]
    elif path.suffix.lower() == '.zip':
        matches = from_zip(path, str(path))
    else:
        raise ValueError('Dùng ZIP bàn giao, thư mục chứa JSONL, hoặc 06-jquiz-005.jsonl.')
    if len(matches) != 1:
        raise ValueError(f'Cần đúng một file {TARGET}, hiện tìm thấy {len(matches)}: {[m[0] for m in matches]}')
    return matches[0]


def prepare(raw, start, limit):
    source = raw.decode('utf-8-sig')
    rows = []
    seen = set()
    for physical_index, line in enumerate(source.splitlines()):
        if not line.strip():
            raise ValueError(f'Dòng trống tại vị trí {physical_index}: không tự đánh lại row_index.')
        record = json.loads(line)
        if not isinstance(record, dict) or not record.get('id') or not isinstance(record.get('ja'), str):
            raise ValueError(f'Bản ghi {physical_index} thiếu id hoặc ja.')
        index = record.get('row_index', physical_index)
        if not isinstance(index, int) or index != physical_index:
            raise ValueError(f'row_index không khớp thứ tự thật: {index} vs {physical_index}')
        if record['id'] in seen:
            raise ValueError(f'ID bị trùng: {record["id"]}')
        if not record['ja'].strip():
            raise ValueError(f'Câu Nhật trống tại row_index={index}')
        if record.get('file', TARGET).split('/')[-1] != TARGET:
            raise ValueError(f'Sai nguồn file tại row_index={index}')
        seen.add(record['id'])
        rows.append({**record, 'file': TARGET, 'row_index': index})
    if len(rows) <= start:
        raise ValueError('Không có dòng nào sau điểm nối. Kiểm tra ZIP nguồn.')
    if start != 4 or tuple(item['id'] for item in rows[:4]) != ANCHORS:
        raise ValueError('4 ID đầu không khớp CP037; từ chối nối nhầm phiên bản nguồn.')
    pending = rows[start:start + limit]
    return rows, pending


def main():
    ap = argparse.ArgumentParser(description='Khôi phục lô nguồn Nhật cho CP038, không dịch tự động.')
    ap.add_argument('source', type=Path, help='ZIP bàn giao gốc hoặc 06-jquiz-005.jsonl')
    ap.add_argument('--limit', type=int, default=650, help='Số dòng nguồn tối đa cho một lô (mặc định 650)')
    ap.add_argument('--out', type=Path, default=Path('JUS_CP038_NGUON_CHO_DICH.jsonl'))
    args = ap.parse_args()
    if not 1 <= args.limit <= 5000:
        ap.error('--limit phải từ 1 đến 5000')
    label, raw = get_source(args.source)
    all_rows, pending = prepare(raw, 4, args.limit)
    if args.out.exists():
        raise FileExistsError('Không ghi đè file đã tồn tại: ' + str(args.out))
    text = ''.join(json.dumps(rec, ensure_ascii=False) + '\n' for rec in pending)
    args.out.write_text(text, encoding='utf-8')
    report = {
        'game': 'Jump Ultimate Stars (Japan) AJUJ',
        'target_checkpoint': '038',
        'status': 'PREPARED_SOURCE_ONLY_NOT_TRANSLATED',
        'new_translations': 0,
        'source_file': TARGET,
        'source_location': label,
        'source_sha256': hashlib.sha256(raw).hexdigest(),
        'source_total_rows': len(all_rows),
        'resume_row_index': 4,
        'selected_count': len(pending),
        'selected_first_row_index': pending[0]['row_index'],
        'selected_last_row_index': pending[-1]['row_index'],
        'selected_sha256': hashlib.sha256(text.encode('utf-8')).hexdigest(),
        'anchors_from_cp037_verified': True,
        'notes': 'Không thêm chuỗi dịch hoặc tự xác nhận đáp án. Quiz có thể ngắt giữa nhóm; khi dịch cần mở rộng theo quiz_context.',
    }
    qa = args.out.with_suffix('.qa.json')
    if qa.exists():
        raise FileExistsError('Không ghi đè báo cáo QA đã tồn tại: ' + str(qa))
    qa.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'ĐÃ CHUẨN BỊ {len(pending)} câu nguồn Nhật (dòng {pending[0]["row_index"]}-{pending[-1]["row_index"]})')
    print('Nguồn:', label)
    print('JSONL:', args.out)
    print('QA:', qa)
    print('LƯU Ý: Chưa dịch thêm câu nào. Hãy đưa JSONL này vào phiên dịch.')


if __name__ == '__main__':
    main()
