# Jump Ultimate Stars — Phục hồi bản hợp nhất Checkpoint 036

- Tổng nguồn: **34.919 ID**.
- Checkpoint 035: **22.318** bản dịch trong `BAN_DICH_TONG_HOP_001-035.jsonl.gz`.
- Checkpoint 036: **602** bản dịch mới trong `BAN_DICH_036.jsonl`.
- Tổng Checkpoint 036: **22.920** bản dịch, còn **11.999**.
- ZIP bàn giao 036 chứa đủ 30 JSONL và `BAN_DICH_TONG_HOP_001-036.jsonl` đã dựng sẵn.

## Tự tạo JSONL hợp nhất từ hai tệp đã có trên GitHub

```python
import gzip, json
from pathlib import Path

with gzip.open("BAN_DICH_TONG_HOP_001-035.jsonl.gz", "rt", encoding="utf-8") as f:
    prior = [json.loads(line) for line in f if line.strip()]
with open("BAN_DICH_036.jsonl", encoding="utf-8") as f:
    added = [json.loads(line) for line in f if line.strip()]

assert len(prior) == 22318 and len(added) == 602
rows = prior + added
assert len({row["id"] for row in rows}) == 22920
rows.sort(key=lambda row: (row["file"], row["row_index"]))
with open("BAN_DICH_TONG_HOP_001-036.jsonl", "w", encoding="utf-8") as f:
    for row in rows:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
```

**Lưu ý:** Vì giới hạn truyền tệp lớn của phiên đồng bộ này, file `BAN_DICH_TONG_HOP_001-036.jsonl.gz` chưa có trên GitHub. Không nên báo tệp đó đã được đồng bộ. Bản hợp nhất 036 có sẵn trong ZIP bàn giao tại cuộc trò chuyện.
