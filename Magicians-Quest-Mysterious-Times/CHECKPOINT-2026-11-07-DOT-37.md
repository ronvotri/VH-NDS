# Magician’s Quest: Mysterious Times — Checkpoint 037

**Ngày:** 07/11/2026  
**Repository:** `ronvotri/VH-NDS`, thư mục `Magicians-Quest-Mysterious-Times/`  
**Baseline:** `MagiciansQuest-VietHoa-Checkpoint-036.zip` (10.808 mục đã dịch)  
**Mốc mới:** **11.048 / 55.976 mục (19,74%)**, thêm **240 trang NPC**.

## Tiến độ

| Nhóm | Đã dịch | Tổng | Mới |
| --- | ---: | ---: | ---: |
| 00 — Mở đầu | 106 | 106 | 0 |
| 01 — Hệ thống | 1.086 | 1.087 | 0 |
| 02 — Vật phẩm | 1.501 | 1.501 | 0 |
| 03 — Sổ tay | 432 | 432 | 0 |
| 04 — Hội thoại NPC | 7.923 | 52.608 | +240 |
| 05 — Credit | 0 | 242 | 0 |
| **Tổng** | **11.048** | **55.976** | **+240** |

## Nội dung đợt 037

- `translation/04-thoai/talkfigs__0eng__data__0031.002.jsonl` — **120 trang**: chuyến đi học ngoại khóa; học tập, thầy cô; sách, học hành; bối rối về tình yêu đầu đời; tỏ tình, hẹn hò, gu thời trang; mùa thu/mùa đông và cô bạn có phần nhút nhát, lo xa.
- `translation/04-thoai/talkfigs__0eng__data__0031.003.jsonl` — **120 trang**: lá thu, cỏ bốn lá, pháo hoa và bông tuyết; thói quen, sở thích; tâm lý rụt rè; ngưỡng mộ người hoạt bát và câu hỏi về tình bạn giữa các cô gái.
- Dịch thủ công: `vi_0031_002_raw.txt`, `vi_0031_003_raw.txt`; bản đầy đủ mã: `vi_0031_002.txt`, `vi_0031_003.txt`. Bảng song ngữ `manual_0031_002.tsv`, `manual_0031_003.tsv`.
- Mã áp dụng `apply_037.py`; QA `qa_037.py`; chênh lệch gốc/dịch `DELTA-037.jsonl` và `QA-037.md`.

## Kết quả kiểm tra

- **PASS:** 501 tệp JSONL / 55.976 bản ghi so với ZIP 036; chỉ hai tệp đích thay đổi trường `vi`, **240 mục** mới.
- Giữ nguyên **10.808** mục dịch cũ; bảo toàn mọi mã game và lựa chọn; tối đa 3 ngắt dòng/trang, 34 ký tự nhìn thấy/dòng, NFC.
- **Chưa kiểm thử trong ROM NDS** hoặc đo rộng pixel bằng font game; còn cần test các biến tên thay thế.
- ZIP này gồm bảng dịch và công cụ; **không chứa ROM thương mại**.

## Tiếp theo — đợt 038

- `0031.004`: 120 trang chưa dịch.
- `0031.005`: 101 trang chưa dịch.
- Tổng **221 trang**; cần đọc tiếp mạch NPC, tránh dịch trùng và giữ mã điều khiển.