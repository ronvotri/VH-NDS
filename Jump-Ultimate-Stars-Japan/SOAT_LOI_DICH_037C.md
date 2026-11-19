# Jump Ultimate Stars — QA bổ sung 037C (sửa 17 dòng)
 
**Ngày:** 2026-11-19. **Dữ liệu đọc thực tế:** `BAN_DICH_037.jsonl`, đủ 676 bản ghi Nhật–Việt ở CP037. `BAN_DINH_CHINH_037C.jsonl` là lớp đính chính mới, **không phải câu dịch mới**.

## Kết quả đối chiếu

| row_index | Việt ngữ trước | Việt ngữ đính chính | Căn cứ chỉnh |
|---|---|---|---|
| 1297 | Cậu ấy chiến thắng bằng cách nào? | Jotaro đã thắng bằng cách nào? | Chủ ngữ rõ ràng, không đổi nghĩa câu hỏi. |
| 1330 | dùng Stand cạo sạch mọi vật thể. | Stand của hắn nghiền nát mọi vật cản. | Diễn đạt tự nhiên hơn 「削りながら攻撃」. |
| 1332 | hai ai đã bỏ mạng? | hai người nào đã bỏ mạng? | Sửa kết cấu tiếng Việt 'hai ai'. |
| 1364 | Josuke và Koichi hoạt động tại | Phần 4 Diamond is Unbreakable có | Khôi phục nhan đề chương bị lược trong bản cũ. |
| 1365 | thị trấn hư cấu trong Phần 4, | Josuke và Koichi góp mặt. | Kết nối chủ thể trong câu hỏi. |
| 1366 | Thị trấn giả tưởng này tên gì? | Bối cảnh ở thị trấn hư cấu nào? | Giữ ý hỏi địa điểm giả tưởng của Phần 4. |
| 1412 | Vì đó là tóc của người cậu ngưỡng mộ | Vì giống kiểu tóc của thần tượng | Đúng ý về kiểu tóc của người Josuke ngưỡng mộ. |
| 1618 | Gyro Zeppeli, một tay đua | Gyro Zeppeli, tay đua Steel Ball Run, | Làm rõ Gyro tham gia giải đua. |
| 1619 | Steel Ball Run, khắc gì trên răng? | có dòng chữ nào khắc trên | Liên kết mệnh đề hỏi về dòng chữ. |
| 1620 | Dòng chữ nào sau đây? | chiếc răng vàng của mình? | Khôi phục chi tiết 'răng vàng' 「金歯」. |
| 1860 | (Tính đến tháng 11/<IDEOSP>2006) | (Tính tới 11/2006<IDEOSP>) | Sửa vị trí dấu ngắt, giữ thẻ điều khiển. |
| 1898 | Giải Tezuka đào tạo nhiều mangaka. | Giải Tezuka chắp cánh nhiều mangaka. | Không diễn đạt sai thành giải thưởng 'đào tạo' nghệ sĩ. |
| 1899 | Tiền thưởng giải chính là bao nhiêu? | Tác phẩm trúng tuyển nhận bao nhiêu? | Thể hiện nghĩa 「入選」 thay vì gọi tùy tiện 'giải chính'. |
| 1914 | bao nhiêu nước? (11/<IDEOSP>2006) | bao nhiêu nước? (11/2006)<IDEOSP> | Giữ đúng mốc lịch sử tháng 11/2006 và thẻ. |
| 1919 | Ở châu Âu, nước nào mua | Ở châu Âu, manga Jump bán chạy | Diễn đạt đúng ý sức bán, không phải ai đi mua. |
| 1920 | manga Jump nhiều nhất? | nhất tại quốc gia nào? | Hoàn chỉnh câu hỏi liên dòng. |
| 1929 | So với thời kỳ ra mắt, giá của | So với lúc mới ra mắt, giá của | Tự nhiên hơn và nối đúng câu hỏi sang tệp 005. |

## Kiểm tra

- 17/17 bản ghi có ID độc nhất, gắn đúng file `06-jquiz-004.jsonl`.
- Chỉ sửa thuộc tính `vi`; bảo toàn `id`, `ja`, `file`, `row_index`, `quiz_context` và các metadata còn lại.
- Tất cả các chuỗi mới có độ dài Unicode tối đa 37 ký tự (bao gồm thẻ điều khiển như chữ thường để tính bảo thủ).
- Thẻ điều khiển có trong bản Việt cũ vẫn khớp bản sửa (cùng số lượng, tên thẻ).
- **Không thay đổi** thứ tự hoặc nội dung các phương án trả lời.
- **Tiến độ không đổi:** 23.596/34.919 chuỗi. 037B có 3 sửa riêng; 037C có 17 sửa mới.
- QA này là **đối chiếu văn bản tĩnh**, chưa QA độ rộng pixel và chưa kiểm thử ROM NDS.

## Cách áp dụng

Sau khi khôi phục bản hợp nhất 001–037 theo `PHUC_HOI_TONG_HOP_037.md`, áp overlay 037B và sau đó 037C **theo `id`**. Không nối các tệp đính chính vào JSONL tổng hợp vì làm trùng ID.

```python
from pathlib import Path
import json
root = Path(".")
source = root / "BAN_DICH_TONG_HOP_001-037.jsonl"
rows = [json.loads(s) for s in source.read_text(encoding="utf-8").splitlines() if s.strip()]
assert len(rows) == 23596
index = {r["id"]: r for r in rows}
assert len(index) == len(rows)
for basename, expected in [("BAN_DINH_CHINH_037B.jsonl", 3), ("BAN_DINH_CHINH_037C.jsonl", 17)]:
    changes = [json.loads(line) for line in (root / basename).read_text(encoding="utf-8").splitlines() if line.strip()]
    assert len(changes) == expected
    assert len({r["id"] for r in changes}) == expected
    for patch in changes:
        row = index[patch["id"]]
        assert row["file"] == patch["file"] and row["row_index"] == patch["row_index"] and row["ja"] == patch["ja"]
        row["vi"] = patch["vi"]
out = root / "BAN_DICH_TONG_HOP_001-037_QA037C.jsonl"
out.write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in rows), encoding="utf-8")
print(f"QA overlay hoàn tất: {len(rows)} ID")
```

## Tiếp theo

**Checkpoint 038 vẫn cần nguồn Nhật:** `06-jquiz-005.jsonl`, từ row_index 4. ZIP `JumpUltimateStars_Japan_BanGiao_Cloud.zip` có trong danh mục tệp cũ nhưng hiện không thể đọc byte nguồn. GitHub chỉ có các bản dịch đã làm đến row_index 3; tra cứu công khai cũng không ra bản nguồn tương ứng. Không được chế câu hỏi/đáp án khi không có nguyên văn.
