# Magician’s Quest: Mysterious Times — Checkpoint 035

**Ngày:** 07/11/2026  
**Repository:** `ronvotri/VH-NDS`, thư mục `Magicians-Quest-Mysterious-Times/`  
**Baseline:** `MagiciansQuest-VietHoa-Checkpoint-034.zip` (10.328 mục đã dịch)  
**Mốc mới:** **10.568/55.976 mục (18,88%)**, thêm **240 trang hội thoại NPC**.

## Tiến độ

| Nhóm | Đã dịch | Tổng | Mới |
| --- | ---: | ---: | ---: |
| 00 — Mở đầu | 106 | 106 | 0 |
| 01 — Hệ thống | 1.086 | 1.087 | 0 |
| 02 — Vật phẩm | 1.501 | 1.501 | 0 |
| 03 — Sổ tay | 432 | 432 | 0 |
| 04 — Hội thoại | 7.443 | 52.608 | +240 |
| 05 — Credit | 0 | 242 | 0 |
| **Tổng** | **10.568** | **55.976** | **+240** |

## Nội dung đợt 035

- `0030.003`: **120 trang**, nối chuyện bố che ô, phép màu tình yêu, thiên nhiên bốn mùa, hoa bồ công anh, sở thích đọc sách, may vá, câu cá, bạn bè, tương lai và gia đình.
- `0030.004`: **120 trang**, chuyện kính trọng cha, nhà văn và ước mơ bay, lòng tốt, tình bạn, sinh nhật, các nhánh mời đi chơi / uống trà / học nhóm, các lựa chọn phản hồi.
- Văn phong vui và tự nhiên ở phần đời thường; các câu hỏi về lòng tốt và tình bạn giữ giọng chân thành. Xưng hô bạn bè mặc định **tớ–cậu**.
- Giữ nguyên biến tên `$500;`, `$503'306;`, `$503'307;`, `$503'309;`, `$503'310;`, `$503'327;` và mã điều hướng `$019'...;`.
- Bản dịch tay nguồn `vi_0030_003_raw.txt`, `vi_0030_004_raw.txt`; bản đã ngắt dòng và gắn token `vi_0030_003.txt`, `vi_0030_004.txt`; đối chiếu `manual_0030_003.tsv`, `manual_0030_004.tsv`.
- Nhật ký `DELTA-035.jsonl`, công cụ `wrap_035.py`, `apply_035.py`, `qa_035.py`, báo cáo `QA-035.md`.

## QA và trạng thái phát hành

- PASS 501 JSONL / 55.976 mục so với baseline 034; chỉ bổ sung 240 `vi`; 10.328 bản dịch trước giữ nguyên.
- Kiểm tra token, Unicode NFC, giới hạn dòng và số dấu `▼`, byte budget khi có.
- Chưa có kiểm thử thực tế với ROM NDS hoặc font hiển thị. ZIP chỉ gồm nguồn dịch và công cụ, **không gồm ROM thương mại**.

## Đợt 036 tiếp theo

- `0030.005`: 120 trang hội thoại.
- `0031.001`: dự kiến 120 trang; xác nhận lại trong checkpoint.
- Tiếp tục bảo toàn mã và cập nhật GitHub sau QA.