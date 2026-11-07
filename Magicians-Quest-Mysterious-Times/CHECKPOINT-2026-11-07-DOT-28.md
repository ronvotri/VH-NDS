# Magician’s Quest: Mysterious Times — Checkpoint 028

**Ngày:** 07/11/2026  
**Repository:** `ronvotri/VH-NDS`, thư mục `Magicians-Quest-Mysterious-Times/`  
**Baseline:** `MagiciansQuest-VietHoa-Checkpoint-027.zip` (8.768 mục)  
**Mốc mới:** **8.969/55.976 mục (16,02%)**, thêm **201 trang thoại NPC**.

## Tiến độ

| Nhóm | Đã dịch | Tổng | Mới |
|---|---:|---:|---:|
| 00 — Mở đầu | 106 | 106 | 0 |
| 01 — Hệ thống | 1.086 | 1.087 | 0 |
| 02 — Vật phẩm | 1.501 | 1.501 | 0 |
| 03 — Sổ tay | 432 | 432 | 0 |
| 04 — Hội thoại | 5.844 | 52.608 | +201 |
| 05 — Credit | 0 | 242 | 0 |
| **Tổng** | **8.969** | **55.976** | **+201** |

## Nội dung đợt 028

- `translation/04-thoai/talkfigs__0eng__data__0027.004.jsonl`: **120 trang**, tình bạn, quà sinh nhật, tiệc ngủ, bối rối khi ghen, mời đi chơi, học nhóm, tỏ tình, hẹn nhau ở Điểm Hẹn Hò.
- `translation/04-thoai/talkfigs__0eng__data__0027.005.jsonl`: **81 trang**, lời đề nghị kết bạn thân, chọn giờ hẹn, giữ lời hứa, chuyện học hành, bạn bè, hẹn hò và các hoạt động chung.
- Bản dịch tay: `vi_0027_004.txt`, `vi_0027_005.txt`; bảng đối chiếu ID/EN/VI: `manual_0027_004.tsv`, `manual_0027_005.tsv`.
- Công cụ: `apply_028.py` (áp 201 bản dịch), `qa_028.py` (so với ZIP 027), `DELTA-028.jsonl` (201 thay đổi), `QA-028.md` (báo cáo).
- Ngôi xưng bạn bè **tớ–cậu**, hài hước theo đúng nhân vật. **Lovers' Point → Điểm Hẹn Hò** nhất quán với các đợt trước. Bảo toàn `$500;`, `$503'305;`, `$503'306;`, `$515;`, mã màu `$000'5;` và `$000'1;`, mã nhánh `$019'...;` cùng các mã biểu cảm.

## Kết quả QA

- **PASS:** 501 JSONL / 55.976 bản ghi, đối chiếu từng trường với checkpoint 027.
- Chỉ bổ sung **201 mục `vi`**; **8.768 bản dịch đã có** và toàn bộ trường nguồn được giữ nguyên.
- Các token kỹ thuật đúng **danh sách và thứ tự**; Unicode NFC; không CR/LF/tab trong VI; tối đa 3 `▼` và 34 ký tự nhìn thấy/dòng, kiểm tra byte budget nếu có.
- Gói ZIP có đủ toàn bộ 501 tệp JSONL và lịch sử các đợt trước; không chứa ROM thương mại hoặc patch ROM.
- **Chưa kiểm thử ROM NDS / độ rộng pixel thật.** QA mới xác nhận dữ liệu và ngưỡng ký tự.

## Tiếp theo — đợt 029

- `0028.001` — 120 trang chưa dịch.
- `0028.002` — 120 trang chưa dịch.
- Tổng **240 trang**, tiếp tục đúng giọng NPC, giữ nguyên mã lệnh và cập nhật GitHub sau QA.