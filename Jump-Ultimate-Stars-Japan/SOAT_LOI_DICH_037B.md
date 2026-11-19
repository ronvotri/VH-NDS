# Jump Ultimate Stars — Đính chính QA 037B

**Ngày:** 2026-11-19. **Nguồn:** \`BAN_DICH_037.jsonl\` (676 chuỗi), nhánh \`vh/jump-ultimate-stars-japan\`.

Rà đối chiếu Nhật–Việt trong \`06-jquiz-004.jsonl\`. Có **3 sửa diễn đạt** cần tách riêng làm overlay, không chạm bản checkpoint lịch sử:

| Dòng | Bản cũ | Bản sửa | Lý do |
| --- | --- | --- | --- |
| 1350 | Dịch chuyển đến mọi nơi thế giới | Dịch chuyển tới mọi nơi trên thế giới | Câu tiếng Việt thiếu giới từ |
| 1411 | cậu ta lại nổi điên như người khác. | cậu nổi điên như biến thành người khác. | Rõ sắc thái 「人が変わったように」 |
| 1458 | được nhóm Giorno giao hộ tống | được giao cho nhóm Giorno hộ tống | Đúng chủ thể được giao nhiệm vụ |

**QA:** Ba ID riêng biệt, giữ nguyên \`id\`, \`ja\`, \`file\`, \`row_index\` và \`quiz_context\`; chỉ thay trường \`vi\`. Tổng số bản dịch vẫn là **23.596/34.919**, không cộng 3 dòng sửa vào tiến độ.

### Cách áp dụng khi khôi phục bản hợp nhất

\`BAN_DINH_CHINH_037B.jsonl\` là **overlay thay thế** chứ không phải file thêm ID. Đừng nối nó trực tiếp vào bản hợp nhất (sẽ tạo ID trùng).

~~~python
from pathlib import Path
import json

root = Path(".")
base = root / "BAN_DICH_TONG_HOP_001-037.jsonl"
patch = root / "BAN_DINH_CHINH_037B.jsonl"
updates = {x["id"]: x for x in map(json.loads, patch.read_text(encoding="utf-8").splitlines())}
assert len(updates) == 3
data = [json.loads(s) for s in base.read_text(encoding="utf-8").splitlines() if s.strip()]
updated = set()
for row in data:
    if row["id"] in updates:
        change = updates[row["id"]]
        assert row["file"] == change["file"]
        assert row["row_index"] == change["row_index"]
        assert row["ja"] == change["ja"]
        row["vi"] = change["vi"]
        updated.add(row["id"])
assert updated == set(updates)
assert len(data) == 23596
assert len({row["id"] for row in data}) == len(data)
(root / "BAN_DICH_TONG_HOP_001-037_QA037B.jsonl").write_text(
    "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in data),
    encoding="utf-8",
)
print("Đã sửa", len(updated), "mục; tổng", len(data), "mục")
~~~

### Tình trạng checkpoint 038

**Chưa có câu Nhật mới để dịch.** Cần nguồn \`06-jquiz-005.jsonl\` dòng 4 trở đi từ ZIP bàn giao gốc. GitHub hiện có bản dịch dòng 0–3, không có nguồn Nhật dòng 4+. Không tạo giả câu đố/đáp án.
