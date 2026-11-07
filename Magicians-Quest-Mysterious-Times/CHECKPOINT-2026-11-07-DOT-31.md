# Magician’s Quest: Mysterious Times — Checkpoint 031

**Ngày:** 07/11/2026  
**Repo:** `ronvotri/VH-NDS`, thư mục `Magicians-Quest-Mysterious-Times/`  
**Baseline:** `MagiciansQuest-VietHoa-Checkpoint-030.zip` (9.449 mục đã dịch)  
**Mốc mới:** **9.660/55.976 mục (17,26%)**, +211 trang hội thoại NPC.

## Tiến độ

| Nhóm | Đã dịch | Tổng | Mới |
| --- | ---: | ---: | ---: |
| 00 — Mở đầu | 106 | 106 | 0 |
| 01 — Hệ thống | 1.086 | 1.087 | 0 |
| 02 — Vật phẩm | 1.501 | 1.501 | 0 |
| 03 — Sổ tay | 432 | 432 | 0 |
| 04 — Hội thoại | 6.535 | 52.608 | +211 |
| 05 — Credit | 0 | 242 | 0 |
| **Tổng** | **9.660** | **55.976** | **+211** |

## Nội dung đợt 031

- `translation/04-thoai/talkfigs__0eng__data__0028.005.jsonl`: **91 trang**; hoàn tất nhánh hẹn ở Điểm Hẹn Hò, các giờ hẹn, lời hứa, tin đồn và hồi tưởng về bạn cũ. Giữ chất hơi kiêu kỳ, hài duyên của NPC và ngôi xưng tớ–cậu.
- `translation/04-thoai/talkfigs__0eng__data__0029.001.jsonl`: **120 trang**; NPC mới kể những chuyện ngày nghỉ, giặt giũ, mua sắm, nấu ăn, đi học, trang điểm và những pha hậu đậu. Giọng tự nhiên, ấm áp, tinh nghịch.
- `vi_0028_005_raw.txt`, `vi_0029_001_raw.txt`: bản dịch tay chưa ngắt dòng; `vi_0028_005.txt`, `vi_0029_001.txt`: bản ngắt dòng gọn.
- `DELTA-031.jsonl`: đầy đủ ID, EN, VI và ngữ cảnh của 211 mục. `qa_031.py` kiểm tra toàn bộ bản gộp với ZIP checkpoint 030; `QA-031.md` lưu kết quả.

## QA

- **PASS** với **501 JSONL / 55.976 bản ghi**, toàn bộ 9.449 bản dịch cũ bất biến.
- Chỉ thêm `vi` vào 211 mục mới, giữ nguyên trường nguồn và thứ tự, token tên NPC, lựa chọn, màu sắc, ngắt dòng an toàn, NFC và byte budget khi có.
- **Chưa kiểm thử trực tiếp trong ROM NDS**, độ rộng pixel thực tế cần xác nhận sau.

## Tiếp theo — đợt 032

- `0029.002`: 120 trang chưa dịch; sau đó `0029.003` nếu đủ thời lượng.
- Giữ chính xác quy ước ngôi xưng, mã lệnh, màu và tên riêng. Tạo checkpoint ZIP đầy đủ và cập nhật GitHub.