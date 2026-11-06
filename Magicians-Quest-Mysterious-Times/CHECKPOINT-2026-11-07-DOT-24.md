# Magician’s Quest: Mysterious Times — Checkpoint 024

**Ngày:** 07/11/2026  
**Repository:** `ronvotri/VH-NDS`, thư mục `Magicians-Quest-Mysterious-Times/`  
**Baseline:** `MagiciansQuest-VietHoa-Checkpoint-023.zip` (7.828 mục)  
**Mốc mới:** **8.068/55.976 mục (14,41%)**, thêm **240 trang thoại NPC**.

## Tiến độ

| Nhóm | Đã dịch | Tổng | Mới |
|---|---:|---:|---:|
| 00 — Mở đầu | 106 | 106 | 0 |
| 01 — Hệ thống | 1.086 | 1.087 | 0 |
| 02 — Vật phẩm | 1.501 | 1.501 | 0 |
| 03 — Sổ tay | 432 | 432 | 0 |
| 04 — Hội thoại | 4.943 | 52.608 | +240 |
| 05 — Credit | 0 | 242 | 0 |
| **Tổng** | **8.068** | **55.976** | **+240** |

## Đợt 024

- `translation/04-thoai/talkfigs__0eng__data__0026.001.jsonl`: **120 trang**. NPC chăm học và trọng kỷ luật; ngày nghỉ, việc học, những lần giúp bạn/bố mẹ/thầy cô và các tình huống dở khóc dở cười.
- `translation/04-thoai/talkfigs__0eng__data__0026.002.jsonl`: **120 trang**. Lựa chọn nghề nghiệp, bài tập về nhà, tình cảm, phép lịch sự khi hẹn hò, lễ Bảy Loại Rau, lễ Tình nhân, Phục Sinh và Bảy Loài Hoa mùa thu.
- Bản dịch tay: `vi_0026_001.txt` và `vi_0026_002.txt` (120 dòng/tệp); tệp đối chiếu `manual_0026_001.tsv`, `manual_0026_002.tsv` lưu ID / English / Vietnamese.
- Công cụ: `apply_024.py`, `qa_024.py`; delta `DELTA-024.jsonl` (240 dòng); kiểm tra `QA-024.md`.

## Kiểm thử

- PASS: đối chiếu **501 JSONL / 55.976 bản ghi** với checkpoint 023.
- Chính xác **240 trường `vi` mới**, giữ nguyên tất cả trường khác và mọi bản dịch trước.
- Bảo toàn mã màu `$000`, mã lựa chọn `$019`, mã nhánh `$034`, biểu cảm `$024/$023/$022` và các mã điều khiển khác theo đúng thứ tự và giá trị.
- Unicode NFC, tối đa ba dấu `▼`; mỗi dòng ≤34 ký tự hiển thị (không tính mã); không chứa CR/LF/tab trong trường dịch; tuân thủ byte budget khi được khai báo.
- ZIP checkpoint được kiểm tra CRC, có đủ 501 JSONL, không chứa ROM thương mại.
- **Chưa kiểm thử thực tế trong ROM NDS / độ rộng pixel font tiếng Việt**. QA xác nhận cấu trúc, chưa phải hiển thị cuối cùng.

## Bước tiếp theo — đợt 025

- `0026.003` — 120 trang chưa dịch.
- `0026.004` — 120 trang chưa dịch.
- Tiếp tục giọng từng NPC, giữ mã điều khiển, chỉ sửa `vi`, lưu checkpoint GitHub và ZIP sau đợt.