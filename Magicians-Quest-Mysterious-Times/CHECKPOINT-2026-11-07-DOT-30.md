# Magician’s Quest: Mysterious Times — Checkpoint 030

**Ngày:** 07/11/2026  
**Repository:** `ronvotri/VH-NDS`, thư mục `Magicians-Quest-Mysterious-Times/`  
**Baseline:** `MagiciansQuest-VietHoa-Checkpoint-029.zip` (9.209 mục)  
**Mốc mới:** **9.449/55.976 mục (16,88%)**, thêm **240 trang thoại NPC**.

## Tiến độ

| Nhóm | Đã dịch | Tổng | Mới |
|---|---:|---:|---:|
| 00 — Mở đầu | 106 | 106 | 0 |
| 01 — Hệ thống | 1.086 | 1.087 | 0 |
| 02 — Vật phẩm | 1.501 | 1.501 | 0 |
| 03 — Sổ tay | 432 | 432 | 0 |
| 04 — Hội thoại | 6.324 | 52.608 | +240 |
| 05 — Credit | 0 | 242 | 0 |
| **Tổng** | **9.449** | **55.976** | **+240** |

## Nội dung đợt 030

- `translation/04-thoai/talkfigs__0eng__data__0028.003.jsonl`: **120 trang**. Nhân vật nữ mê thời trang, phối màu, quần bò cũ, đồ tái chế, bạn bè, tham vọng làm thần tượng và các câu chuyện hài do tự tin quá đà. Giữ phần suy tư về tình bạn, sự tự lập và tình cảm.
- `translation/04-thoai/talkfigs__0eng__data__0028.004.jsonl`: **120 trang**. Hiểu lầm khi che chiếc túi mới và khi soi gương trong giờ kiểm tra, các nhánh rủ đi chơi, uống trà, học bài, chia tay đi làm việc, lời hẹn ở Điểm Hẹn Hò lúc 18:00 và lời tỏ tình.
- Bản dịch tay trước khi ngắt dòng: `vi_0028_003_raw.txt`, `vi_0028_004_raw.txt`; thành phẩm: `vi_0028_003.txt`, `vi_0028_004.txt`; bảng đối chiếu ID/EN/VI: `manual_0028_003.tsv`, `manual_0028_004.tsv`.
- Công cụ: `wrap_030.py`, `apply_030.py`, `qa_030.py`, `DELTA-030.jsonl` (240 thay đổi), `QA-030.md`.
- Giọng nữ NPC tự tin hơi quá nhưng không châm biếm chuyện nghiêm túc; ngôi **tớ–cậu**; giữ nguyên token tên người chơi, nhân vật `$503'305;` và mã màu của `Điểm Hẹn Hò`.

## Kết quả QA

- **PASS:** 501 JSONL / 55.976 bản ghi; đối chiếu từng trường với checkpoint 029.
- Chỉ bổ sung **240 mục `vi`**; toàn bộ **9.209 mục dịch cũ** và các trường gốc giữ nguyên.
- Mã kỹ thuật đúng **danh sách và thứ tự**; Unicode NFC; không CR/LF/tab trong `vi`; mỗi trang tối đa 3 dấu `▼`, 34 ký tự nhìn thấy/dòng; kiểm tra byte budget nếu có.
- ZIP chứa toàn bộ 501 JSONL và lịch sử các đợt trước; không chứa ROM thương mại hoặc patch ROM.
- **Chưa kiểm thử ROM NDS / độ rộng pixel thật.** QA này chỉ xác nhận cấu trúc dữ liệu và ngưỡng ký tự.

## Tiếp theo — đợt 031

- `0028.005` — 91 trang chưa dịch.
- `0029.001` — 120 trang chưa dịch.
- Tổng **211 trang**, bảo toàn mã lệnh, ngôi xưng và cập nhật GitHub sau QA.