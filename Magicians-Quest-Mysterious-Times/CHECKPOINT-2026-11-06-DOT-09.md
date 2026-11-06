# Magician’s Quest: Mysterious Times — Checkpoint Việt hóa 009

**Ngày:** 06/11/2026  
**Kho GitHub:** `ronvotri/VH-NDS` → `Magicians-Quest-Mysterious-Times/`  
**Baseline:** checkpoint 008 — 4.450/55.976 mục  
**Hiện tại:** **4.690/55.976 mục (8,38%)**, thêm **240 trang thoại** ở cụm `0020`.

## Tiến độ

| Nhóm | Đã xử lý | Tổng | Đợt 009 |
|---|---:|---:|---:|
| 00 — Mở đầu | 106 | 106 | 0 |
| 01 — Hệ thống | 1.086 | 1.087 | 0 |
| 02 — Vật phẩm | 1.501 | 1.501 | 0 |
| 03 — Sổ tay | 432 | 432 | 0 |
| 04 — Hội thoại | **1.565** | 52.608 | **+240** |
| 05 — Credit | 0 | 242 | 0 |
| **Tổng** | **4.690** | **55.976** | **+240** |

**Lưu ý:** số "đã xử lý" bao gồm các tên riêng được quyết định giữ nguyên, không đồng nghĩa với số câu tiếng Anh đã được chuyển đổi. Chưa có ROM đã vá để thử trong game.

## Nội dung đợt 009

Tập trung vào `translation/04-thoai/talkfigs__0eng__data__0020.001.jsonl` và `...0020.002.jsonl`, mỗi tệp 120 trang. Các chủ đề: người thích thể hiện mình là người lớn, chuyện đi câu, nấu nướng, làm hỏng máy giặt, xem phim kinh dị, tình cảm và các tình huống hài ở trường phép thuật.

**Phát hiện về cấu trúc:** dữ liệu nguồn không có các nhóm `0013`, `0014`, `0015`. Sau `0012` chuyển sang `0020`; không tự tạo nhóm không tồn tại.

Văn phong: tự nhiên, gần gũi Gen Z, có duyên, không bóp méo ý gốc hoặc nhồi meme. Người bạn đồng lứa xưng **tớ–cậu**; các thông báo và tên riêng vẫn giữ đúng quy ước cũ. Không thêm giới tính/vai vế ở chỗ không có bằng chứng.

## Kiểm tra

- 501 tệp JSONL, 55.976 mục được đối chiếu với checkpoint 008.
- Đúng **240 thay đổi**, tất cả điền `vi` trước đây null; **không sửa** `id`, `en`, `ctx`, thứ tự hoặc trường kỹ thuật.
- Bảo toàn đúng thứ tự toàn bộ token `$...;` gồm các mã nhân vật `$500;`, `$503'318;`, tên có tag `$000'3;` và `$000'5;`.
- Kiểm tra Unicode NFC, dấu ngắt `▼`, số dòng, byte UTF-8 khi trường nguồn khai báo, không thêm tab/CR/LF cấu trúc.
- **0 lỗi, 0 cảnh báo** dòng hiển thị dài quá 34 ký tự sau khi loại bỏ token mã lệnh.
- **Chưa đo độ rộng font/pixel thực tế trong ROM**, không gọi đây là bản vá chơi được.

## Tệp nối phiên

- `manual_0020_001.txt`, `manual_0020_002.txt`: 120 câu mỗi tệp theo đúng thứ tự ID của nguồn.
- `apply_009.py`: áp bản dịch lên checkpoint 008; dừng nếu ghi đè câu đã có.
- `qa_009.py`: kiểm tra toàn bộ checkpoint, tạo `DELTA-009.jsonl`, `QA-009.md`.
- `DELTA-009.jsonl`: 240 bản ghi ID + EN + VI + ctx.
- ZIP `MagiciansQuest-VietHoa-Checkpoint-009.zip` là bản đầy đủ, gồm cả các đợt trước.

## Đợt 010

Tiếp tục `0020.003`–`0020.005` theo thứ tự, xem ngữ cảnh các trang trước/sau từng câu, giữ tớ–cậu và sắc thái nhân vật. Mỗi lần hoàn tất phải tạo ZIP, kiểm tra và cập nhật repo GitHub chung `VH-NDS` trong thư mục riêng của trò chơi.