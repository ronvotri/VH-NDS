# Magician’s Quest: Mysterious Times — Checkpoint 038

**Ngày:** 07/11/2026  
**Repository:** `ronvotri/VH-NDS`, thư mục `Magicians-Quest-Mysterious-Times/`  
**Baseline:** `MagiciansQuest-VietHoa-Checkpoint-037.zip` (11.048 mục đã dịch)  
**Mốc mới:** **11.269 / 55.976 mục (20,13%)**, thêm **221 trang thoại NPC**.

## Tiến độ

| Nhóm | Đã dịch | Tổng | Mới |
|---|---:|---:|---:|
| 00 — Mở đầu | 106 | 106 | 0 |
| 01 — Hệ thống | 1.086 | 1.087 | 0 |
| 02 — Vật phẩm | 1.501 | 1.501 | 0 |
| 03 — Sổ tay | 432 | 432 | 0 |
| 04 — Hội thoại NPC | 8.144 | 52.608 | +221 |
| 05 — Credit | 0 | 242 | 0 |
| **Tổng** | **11.269** | **55.976** | **+221** |

## Nội dung đợt 038

- `translation/04-thoai/talkfigs__0eng__data__0031.004.jsonl` — **120 trang**: cô bạn rụt rè suy nghĩ về tình bạn, những người chỉ giả vờ thân thiện, chuyện tâm sự, các nhánh rủ đi chơi, uống trà, học nhóm và cuộc hẹn lúc 6 giờ tối tại Điểm Hẹn Hò.
- `translation/04-thoai/talkfigs__0eng__data__0031.005.jsonl` — **101 trang**: thổ lộ, mối quan hệ bạn thân và bạn trai, lựa chọn giờ hẹn từ 10 giờ sáng tới 8 giờ tối, giữ lời hứa, các chuyện đi câu cá, mua sắm, học bài và cưỡi chổi với bạn bè.
- Bản dịch thủ công `vi_0031_004_raw.txt`, `vi_0031_005_raw.txt`; bản hoàn chỉnh giữ mã `vi_0031_004.txt`, `vi_0031_005.txt`; bảng song ngữ `manual_0031_004.tsv`, `manual_0031_005.tsv`.
- Tái tạo bằng `apply_038.py`; kiểm tra lại bằng `qa_038.py`; chênh lệch chi tiết `DELTA-038.jsonl`; biên bản `QA-038.md`.

## Kết quả QA

- **PASS:** đối chiếu 501 JSONL và 55.976 bản ghi so với ZIP checkpoint 037; chỉ hai tệp đích thay đổi trường `vi`; **221 mục mới**.
- Giữ nguyên 11.048 bản dịch cũ, `id`, `en`, `ctx`, thứ tự bản ghi và trường kỹ thuật.
- Mọi mã điều khiển, bao gồm `$019'...;`, `$000'...;`, `$500;`, `$515;`, `$074;`, `$079;`, được giữ đúng thứ tự/giá trị. UTF-8 NFC, tối đa 3 dấu ngắt `▼` mỗi trang và 34 ký tự nhìn thấy mỗi dòng.
- **Chưa kiểm thử trên ROM NDS** hoặc đo pixel bằng font game, nhất là khi tên nhân vật `$500;`/`$515;` dài sau khi game thay biến.

## Đợt 039 tiếp theo

- `0032.001` — 120 trang chưa dịch.
- `0032.002` — 120 trang chưa dịch.
- Tổng dự kiến **240 trang**, làm theo thứ tự và kiểm tra lại mạch nhân vật mới trong kho `0032`.