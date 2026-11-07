# Magician’s Quest: Mysterious Times — Checkpoint 052

**Ngày:** 08/11/2026  
**Repo:** `ronvotri/VH-NDS` → `Magicians-Quest-Mysterious-Times/`  
**Mốc trước:** checkpoint 051 — **14.352/55.976**  
**Mốc mới:** **14.592/55.976 (26,07%)**, +**240** bản dịch; thoại NPC **11.467/52.608**.

## Nội dung đợt 052

| Tệp JSONL | Số trang mới | Nội dung |
|---|---:|---|
| `translation/04-thoai/talkfigs__0eng__data__0040.001.jsonl` | 120 | Đối thoại khi tặng quà, hỏi thăm người ốm, chuyển trường, sinh nhật, nhận xét phòng, thưởng trà tại Nhà kính; rủ đi chơi, học phép Cầu Vồng và Pháo Giấy, giấc mơ xấu |
| `translation/04-thoai/talkfigs__0eng__data__0040.002.jsonl` | 120 | Dọn phòng giữa đêm, sợ gián, báo thức, học nhóm và hỏi đáp, chuyển trường, đổi nội thất, phản ứng khi trúng phép, ốm đau, uống nước ép và câu cá |
| **Tổng** | **240** | Giọng NPC lịch sự, có chút điệu và kiêu hãnh; bạn bè tớ–cậu, hạn chế meme |

## Bàn giao

- `vi_0040_001_raw.txt`, `vi_0040_002_raw.txt`: 120 dòng dịch tay/tệp, `¤` là vị trí của mã điều khiển còn lại sau phần tiền tố.
- `vi_0040_001.txt`, `vi_0040_002.txt`: bản cuối đã tự động ghép mã và ngắt dòng; `manual_0040_001.tsv`, `manual_0040_002.tsv`: bảng EN–VI cùng ID và context.
- `apply_052.py`: áp bản dịch từ checkpoint 051, idempotent khi cùng nội dung và từ chối ghi đè `vi` khác biệt; `qa_052.py`: so sánh 501 JSONL với ZIP checkpoint 051.
- `DELTA-052.jsonl` (240 mục) và `QA-052.md` lưu thay đổi và báo cáo QA.
- Bảo toàn mã `$...;`, các nhánh Có/Không, mã tên NPC và vật phẩm, thứ tự và bản dịch trước đó.

**QA PASS:** 501 JSONL / 55.976 mục; chỉ thêm 240 trường `vi`, 14.352 mục dịch cũ giữ nguyên. **Chưa thử trên ROM NDS**. ZIP không chứa ROM thương mại.

**Đợt 053:** `talkfigs__0eng__data__0040.003.jsonl` (120 trang) và `talkfigs__0eng__data__0040.004.jsonl` (120 trang). Nguồn của cả hai có sẵn trong ZIP checkpoint 052; nên lưu bản `vi:null` lên GitHub để nối tiếp.