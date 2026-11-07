# Magician’s Quest: Mysterious Times — Checkpoint 041

**Ngày:** 07/11/2026  
**Repository:** `ronvotri/VH-NDS`, thư mục `Magicians-Quest-Mysterious-Times/`  
**Baseline:** `MagiciansQuest-VietHoa-Checkpoint-040.zip` (11.749 mục dịch)  
**Mốc mới:** **11.989 / 55.976 mục (21,42%)**, **+240** trang thoại NPC.

## Tiến độ

| Nhóm | Đã dịch | Tổng | Mới |
|---|---:|---:|---:|
| 00 — Mở đầu | 106 | 106 | 0 |
| 01 — Hệ thống | 1.086 | 1.087 | 0 |
| 02 — Vật phẩm | 1.501 | 1.501 | 0 |
| 03 — Sổ tay | 432 | 432 | 0 |
| 04 — Hội thoại NPC | 8.864 | 52.608 | +240 |
| 05 — Credit | 0 | 242 | 0 |
| **Tổng** | **11.989** | **55.976** | **+240** |

## Nội dung đợt 041

- `translation/04-thoai/talkfigs__0eng__data__0032.005.jsonl` — **120 trang**: hướng dẫn tin vào tiên, đặt hoa huệ ban ngày, cô giáo ngượng ngùng vì quý mến thầy Vlad, thần chú tình yêu và lựa chọn thay đổi bàn/ghế/tường/thảm lớp học.
- `translation/04-thoai/talkfigs__0eng__data__0033.001.jsonl` — **120 trang**: sinh vật thác nước và nữ thần phục hồi hình dạng, hoa kẹo, hai vị hiệu trưởng cũ nói chuyện từ tranh, cướp biển đòi tiền để trả lời câu hỏi về Limelight và ngôi nhà ma.
- Cô giáo dùng **cô–em**, vị hiệu trưởng dùng **ta–em**, tên/cụm hư cấu và lời gầm của sinh vật được giữ gần nguyên văn, cướp biển xưng **lão–nhóc**. Tên riêng `Vlad`, `Marcy`, `Limelight`, `Harrows` giữ nguyên; tên tiền tệ `Ritch` không đổi.
- Bản dịch chỉ thêm trường `vi` và ngắt `▼`; mã lựa chọn, biểu cảm, màu chữ, mã item, giá tiền và chuyển nhánh được bảo toàn, không tự sửa logic trò chơi.

## Các tệp chính

- `vi_0032_005_raw.txt`, `vi_0033_001_raw.txt`: lời thoại tiếng Việt gốc (chưa gắn mã đầu/cuối và ngắt tự động).
- `vi_0032_005.txt`, `vi_0033_001.txt`: lời thoại đã chèn mã game và ngắt dòng.
- `manual_0032_005.tsv`, `manual_0033_001.tsv`: bảng đối chiếu 240 ID / EN / VI.
- `apply_041.py`: tái áp bản dịch vào đúng tệp JSONL từ checkpoint 040.
- `qa_041.py`, `QA-041.md`: kiểm tra dữ liệu bảo toàn và giới hạn kỹ thuật.
- `DELTA-041.jsonl`: 240 thay đổi trường `vi`.

## QA

**PASS:** 501 tệp JSONL / 55.976 bản ghi, +240 mục dịch mới, 11.749 mục trước không thay đổi; không sửa `id`, `en`, `ctx`, trường kỹ thuật, thứ tự hoặc mã game. Mỗi trang mới tối đa 3 dấu `▼`, mỗi dòng tối đa 34 ký tự (bỏ qua mã `$...;`), UTF-8 NFC. **Chưa chạy thử trong ROM NDS**, chưa xác minh bề rộng pixel/font hoặc tên động dài.

## Đợt 042 tiếp theo

- `0033.002` — 120 trang chưa dịch, nối tiếp các thoại đặc biệt.
- `0033.003` — 120 trang chưa dịch, kế tiếp.
- Tổng dự kiến **240 trang**. Hai tệp nguồn được đưa lên GitHub để tiện nối tiếp.