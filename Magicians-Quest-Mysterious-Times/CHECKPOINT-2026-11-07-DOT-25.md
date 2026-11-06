# Magician’s Quest: Mysterious Times — Checkpoint 025

**Ngày:** 07/11/2026  
**Repository:** `ronvotri/VH-NDS`, thư mục `Magicians-Quest-Mysterious-Times/`  
**Baseline:** `MagiciansQuest-VietHoa-Checkpoint-024.zip` (8.068 mục)  
**Mốc mới:** **8.308/55.976 mục (14,84%)**, thêm **240 trang thoại NPC**.

## Tiến độ

| Nhóm | Đã dịch | Tổng | Mới |
|---|---:|---:|---:|
| 00 — Mở đầu | 106 | 106 | 0 |
| 01 — Hệ thống | 1.086 | 1.087 | 0 |
| 02 — Vật phẩm | 1.501 | 1.501 | 0 |
| 03 — Sổ tay | 432 | 432 | 0 |
| 04 — Hội thoại | 5.183 | 52.608 | +240 |
| 05 — Credit | 0 | 242 | 0 |
| **Tổng** | **8.308** | **55.976** | **+240** |

## Đợt 025

- `translation/04-thoai/talkfigs__0eng__data__0026.003.jsonl`: **120 trang**. NPC chăm chỉ/đề cao trách nhiệm bàn về bảy loài hoa mùa thu, ngày lễ, sức khỏe, thú vui lạ, nghị lực, lòng can đảm và tình bạn.
- `translation/04-thoai/talkfigs__0eng__data__0026.004.jsonl`: **120 trang**. Căn cứ bí mật, thư từ, tin đồn, rủ đi chơi, uống trà, học nhóm, chia tay khi hết buổi chơi và lời tỏ tình có lựa chọn.
- Bản dịch tay: `vi_0026_003.txt`, `vi_0026_004.txt`; tệp đối chiếu `manual_0026_003.tsv` và `manual_0026_004.tsv` gồm ID / English / Vietnamese.
- Script: `apply_025.py`, `qa_025.py`; delta `DELTA-025.jsonl` (240 dòng); báo cáo `QA-025.md`.
- **Lưu ý kỹ thuật:** mã tên nhân vật `$500;` nằm ngay đầu nội dung một trang (mã `0026#23.4#page:1`). Script chỉ tự thêm tiền tố biểu cảm / mã nhánh, không tự nhân đôi biến tên; `$514'1;` và mã màu `$000'5;` được bảo toàn tại đúng vị trí.

## QA

- PASS: đối chiếu đủ **501 JSONL và 55.976 bản ghi** với checkpoint 024.
- Chính xác **240 trường `vi` mới**, không sửa bất cứ trường còn lại hoặc bản dịch trước.
- Bảo toàn thứ tự mã lệnh, ID, biểu cảm, biến tên, mã lựa chọn và mã màu; Unicode NFC; tối đa 3 `▼`, 34 ký tự hiển thị/dòng; tôn trọng byte budget nếu khai báo.
- ZIP được kiểm tra CRC và có đủ 501 JSONL; **không chứa ROM thương mại**.
- **Chưa kiểm thử trong ROM NDS / độ rộng font tính theo pixel**; QA chỉ xác thực cấu trúc và ngưỡng ký tự.

## Tiếp theo — đợt 026

- `0026.005` — 100 trang chưa dịch.
- `0027.001` — 120 trang chưa dịch.
- Tổng 220 trang; giữ nguyên ngôi xưng, mã điều khiển và checkpoint GitHub sau mỗi đợt.