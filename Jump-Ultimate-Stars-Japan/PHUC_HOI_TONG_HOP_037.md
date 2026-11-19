# Khôi phục bản hợp nhất Jump Ultimate Stars — Checkpoint 037

Checkpoint 037 có **23.596 ID đã dịch**, thêm 676 câu so với Checkpoint 036. Bản ZIP đầy đủ được cung cấp trong cuộc trò chuyện; để tránh giới hạn tải tệp lớn trên GitHub, có thể khôi phục bản hợp nhất trực tiếp từ ba tệp đã có trên nhánh này:

- `BAN_DICH_TONG_HOP_001-035.jsonl.gz` (22.318 câu)
- `BAN_DICH_036.jsonl` (602 câu)
- `BAN_DICH_037.jsonl` (676 câu)

Chạy đoạn Python sau trong thư mục `Jump-Ultimate-Stars-Japan/`:

```python
from pathlib import Path
import gzip
import json
import hashlib

root = Path(".")
records = []
seen = set()

with gzip.open(root / "BAN_DICH_TONG_HOP_001-035.jsonl.gz", "rt", encoding="utf-8") as f:
    sources = [list(f)]
for filename in ("BAN_DICH_036.jsonl", "BAN_DICH_037.jsonl"):
    sources.append((root / filename).read_text(encoding="utf-8").splitlines())

for group in sources:
    for line in group:
        if not line.strip():
            continue
        item = json.loads(line)
        assert item["id"] not in seen, item["id"]
        seen.add(item["id"])
        records.append(item)

assert len(records) == 23596, len(records)
records.sort(key=lambda item: (item["file"], item["row_index"]))
output = "".join(json.dumps(item, ensure_ascii=False) + "\n" for item in records).encode("utf-8")
assert hashlib.sha256(output).hexdigest() == "5d4a212d62857c944d8b43c3194d225d82edebd0346bac7d93947351d0c4a51b"
(root / "BAN_DICH_TONG_HOP_001-037.jsonl").write_bytes(output)
print("OK", len(records))
```

Quy trình này đã được thử bằng đúng các JSONL bàn giao CP035, 036, 037 và khớp **từng byte** với bản hợp nhất trong ZIP CP037.

**Điểm tiếp theo:** `06-jquiz-005.jsonl` dòng **4**. Chưa có patch ROM NDS hoặc kiểm thử đáp án, ảnh hay font trực tiếp trong game.
