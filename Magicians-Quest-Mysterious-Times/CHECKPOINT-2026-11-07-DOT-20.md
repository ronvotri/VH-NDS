# Magician’s Quest: Mysterious Times — Checkpoint 020

**Ngày:** 07/11/2026  
**Repo:** `ronvotri/VH-NDS`, thư mục `Magicians-Quest-Mysterious-Times/`  
**Baseline:** `MagiciansQuest-VietHoa-Checkpoint-019.zip` (6.951 mục)  
**Mốc mới:** **7.191/55.976 mục (12,85%)**, thêm **240 trang NPC**.

## Tiến độ

| Nhóm | Đã dịch | Tổng | Mới |
|---|---:|---:|---:|
| 00 — Mở đầu | 106 | 106 | 0 |
| 01 — Hệ thống | 1.086 | 1.087 | 0 |
| 02 — Vật phẩm | 1.501 | 1.501 | 0 |
| 03 — Sổ tay | 432 | 432 | 0 |
| 04 — Hội thoại | 4.066 | 52.608 | +240 |
| 05 — Credit | 0 | 242 | 0 |
| **Tổng** | **7.191** | **55.976** | **+240** |

## Phạm vi đợt 020

- `0024.003`: **120 trang** về những nghiên cứu đáng yêu của NPC thích tính toán (bàn cờ, máy móc, tượng băng, sách, thiên tài, giáo sư, sưu tầm).
- `0024.004`: **120 trang** về bạn bè, quan hệ, lựa chọn đi chơi/học nhóm, uống trà, tỏ tình tại Điểm Hẹn Hò và làm bạn thân.
- `vi_0024_003.txt`, `vi_0024_004.txt`: bản dịch tay từng trang; `manual_0024_003.tsv`, `manual_0024_004.tsv`: đối chiếu ID / English / Vietnamese.
- `apply_020.py`: tái áp dụng bản dịch từ checkpoint 019 (chỉ sửa `vi`). `qa_020.py`: QA bất biến với checkpoint 019. `DELTA-020.jsonl`: toàn bộ 240 mục thay đổi.

## QA

- **PASS:** đủ 501 JSONL và 55.976 bản ghi; đúng 240 bản dịch mới trong đúng hai tệp, tất cả các trường ngoài `vi` bất biến.
- Không sửa lời Việt cũ, không mất mã biểu cảm, biến tên `$500;`, mã chọn `$019`, thẻ màu `$000'5;`/`$000'1;` và mã xuống dòng.
- Unicode NFC, không CR/LF/tab, tối đa 34 ký tự hiển thị/đoạn; số `▼` không quá 3; kiểm tra giới hạn byte nếu có.
- **Chưa kiểm thử ROM NDS thực tế**; cần QA độ rộng chữ theo pixel, font, và chỗ hiển thị biến tên dài.
- ZIP gồm văn bản, mã nguồn, QA, tài liệu; không kèm ROM thương mại.

## Mốc đợt 021

Tiếp tục `0024.005` (74 trang) rồi `0025.001` (120 trang), duy trì phong cách tự nhiên, xưng hô **tớ–cậu**, thuật ngữ nhất quán và mã điều khiển không đổi.