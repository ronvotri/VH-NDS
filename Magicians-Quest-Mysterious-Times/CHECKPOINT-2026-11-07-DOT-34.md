# Magician’s Quest: Mysterious Times — Checkpoint 034

**Ngày:** 07/11/2026  
**Repository:** `ronvotri/VH-NDS`, thư mục `Magicians-Quest-Mysterious-Times/`  
**Baseline:** `MagiciansQuest-VietHoa-Checkpoint-033.zip` (10.088 mục đã dịch)  
**Mốc mới:** **10.328/55.976 mục (18,45%)**, thêm **240 trang hội thoại NPC**.

## Tiến độ

| Nhóm | Đã dịch | Tổng | Mới |
| --- | ---: | ---: | ---: |
| 00 — Mở đầu | 106 | 106 | 0 |
| 01 — Hệ thống | 1.086 | 1.087 | 0 |
| 02 — Vật phẩm | 1.501 | 1.501 | 0 |
| 03 — Sổ tay | 432 | 432 | 0 |
| 04 — Hội thoại | 7.203 | 52.608 | +240 |
| 05 — Credit | 0 | 242 | 0 |
| **Tổng** | **10.328** | **55.976** | **+240** |

## Nội dung đợt 034

- `translation/04-thoai/talkfigs__0eng__data__0030.001.jsonl` — **120 trang**, những chuyện đời thường của một NPC học đường: bánh su kem, may đồ cho búp bê, hoa và gia đình, cầu vồng, bánh quy, truyện trinh thám, trường lớp, phép thuật, tình bạn và cách nói thẳng.
- `translation/04-thoai/talkfigs__0eng__data__0030.002.jsonl` — **120 trang**, nối tiếp chuyện bạn bè hiểu lầm vì đau răng, lời nói dối thiện ý, bài học về công việc và người giao thư, trắc nghiệm, tính trì hoãn, đi học, hôn nhân và những thắc mắc ngộ nghĩnh về tình yêu.
- Giữ lối xưng hô **tớ–cậu** giữa các bạn cùng tuổi. Đoạn nói đến giáo viên giữ vai thầy; câu chuyện hài được thể hiện tự nhiên, không bóp méo ý gốc.
- Chú ý lời đáp tương tác: giữ nguyên mã lựa chọn `$019'26;`, `$019'27;`, `$019'39;`, `$019'40;`, `$019'44;`, `$019'45;`, `$019'49;`, `$019'50;`, `$019'57;`, `$019'58;`, `$019'65;`, `$019'66;` và mọi mã điều khiển khác.
- Tên người chơi `$500;`, nhân vật `$503'307;` và `$503'305;`, mã màu `$000'...;` không thay đổi. Phần `Điểm Hẹn Hò` của các đợt trước được giữ nguyên.
- Bản dịch tay: `vi_0030_001_raw.txt`, `vi_0030_002_raw.txt`; đã ngắt dòng và gắn mã: `vi_0030_001.txt`, `vi_0030_002.txt`; bảng đối chiếu ID/EN/VI: `manual_0030_001.tsv`, `manual_0030_002.tsv`.
- Công cụ `apply_034.py`, `qa_034.py`; nhật ký delta `DELTA-034.jsonl`; kết quả `QA-034.md`.

## Kết quả QA

- **PASS:** đối chiếu với checkpoint 033 ở cấp trường trên **501 JSONL / 55.976 bản ghi**, chỉ 240 `vi` mới; tất cả 10.088 bản dịch trước vẫn bất biến.
- Không sửa ID, câu gốc EN, ctx, tên tệp hoặc thứ tự bản ghi; kiểm tra mã lệnh đúng danh sách/thứ tự; Unicode NFC; không có CR/LF/tab trong giá trị `vi`; mỗi trang tối đa 3 ký tự ngắt `▼`, mỗi dòng tối đa 34 ký tự hiển thị; byte-cap nếu có.
- **Chưa dựng hay kiểm thử trực tiếp trên ROM NDS; chưa đo độ rộng pixel bằng font game.** Kết quả QA chỉ xác nhận dữ liệu và giới hạn ký tự.
- ZIP đầy đủ chứa 501 JSONL, các tệp lịch sử, công cụ và tài liệu; **không chứa ROM thương mại**.

## Đợt 035 tiếp theo

- `0030.003` — 120 trang chưa dịch.
- `0030.004` — 120 trang chưa dịch.
- Tổng mục tiêu: **240 trang**. Sau dịch kiểm tra mã và QA trước khi cập nhật GitHub.