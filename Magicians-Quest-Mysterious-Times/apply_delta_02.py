#!/usr/bin/env python3
"""Apply Batch 02 to an extracted MagiciansQuest-VietHoa-Checkpoint-001.
Requires only Python stdlib. Original en, id, ctx, limits and other fields stay unchanged.
"""
import sys, json, hashlib, base64, bz2
from pathlib import Path

root=Path(sys.argv[1] if len(sys.argv)>1 else '.').resolve()
source=Path(__file__).with_name('DOT-02-DELTA.bz2.b64')
if not source.is_file():
    source=root/'DOT-02-DELTA.bz2.b64'
raw=bz2.decompress(base64.b64decode(source.read_text(encoding='ascii').strip()))
data=json.loads(raw.decode('utf8'))
assert data['base']=='001'
for rel,(expected_sha,vis) in sorted(data['files'].items()):
    p=root/rel
    original=p.read_bytes()
    assert hashlib.sha256(original).hexdigest()==expected_sha, f'Checkpoint 001 SHA mismatch: {rel}'
    entries=[json.loads(x) for x in original.decode('utf8').splitlines()]
    assert len(entries)==len(vis), f'Row count mismatch: {rel}'
    for row, vi in zip(entries,vis):
        if vi is not None:
            assert row['vi'] is None, f'Overwrite not allowed: {row["id"]}'
            row['vi']=vi
    p.write_text(''.join(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n' for x in entries),encoding='utf8')
print('Đã áp dụng Batch 02: 636 mục ở 9 tệp. Chạy python qa_checkpoint.py để kiểm tra.')