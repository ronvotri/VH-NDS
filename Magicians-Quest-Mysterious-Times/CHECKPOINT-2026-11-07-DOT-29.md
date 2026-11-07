# Magician’s Quest: Mysterious Times — Checkpoint 029

**Ngày:** 07/11/2026  
**Repository:** `ronvotri/VH-NDS`, thư mục `Magicians-Quest-Mysterious-Times/`  
**Baseline:** `MagiciansQuest-VietHoa-Checkpoint-028.zip` (8.969 mục)  
**Mốc mới:** **9.209/55.976 mục (16,45%)**, thêm **240 trang thoại NPC**.

## Tiến độ

| Nhóm | Đã dịch | Tổng | Mới |
|---|---:|---:|---:|
| 00 — Mở đầu | 106 | 106 | 0 |
| 01 — Hệ thống | 1.086 | 1.087 | 0 |
| 02 — Vật phẩm | 1.501 | 1.501 | 0 |
| 03 — Sổ tay | 432 | 432 | 0 |
| 04 — Hội thoại | 6.084 | 52.608 | +240 |
| 05 — Credit | 0 | 242 | 0 |
| **Tổng** | **9.209** | **55.976** | **+240** |

## Nội dung đợt 029

- `translation/04-thoai/talkfigs__0eng__data__0028.001.jsonl`: **120 trang**. Nhân vật nữ mê thời trang, đam mê ngôi sao: ngày nghỉ, mua sắm, trang điểm, fan, chuyện mình mạnh bất ngờ, quần áo mặc trái, nhầm cách giao tiếp và các pha hài tự nhiên.
- `translation/04-thoai/talkfigs__0eng__data__0028.002.jsonl`: **120 trang**. Tán gẫu trong lớp, mẹo học số pi, sách thời trang, nghề nghiệp, chữ rune, mối quan hệ tình cảm, lý tưởng bạn trai, mùa thời trang và ca hát.
- Bản dịch tay trước khi ngắt dòng: `vi_0028_001_raw.txt`, `vi_0028_002_raw.txt`; thành phẩm: `vi_0028_001.txt`, `vi_0028_002.txt`; bảng đối chiếu ID/EN/VI: `manual_0028_001.tsv`, `manual_0028_002.tsv`.
- Công cụ: `wrap_029.py` (ngắt dòng), `apply_029.py` (áp 240 bản dịch), `qa_029.py` (đối chiếu ZIP 028), `DELTA-029.jsonl` (240 thay đổi), `QA-029.md` (báo cáo).
- Ngôi xưng **tớ–cậu**, giữ chất tự tin hơi lố và đáng yêu của nữ NPC, không lạm dụng meme. Không dịch sai giới tính người được nhắc đến. Giữ biến tên và mã tô màu nguyên thứ tự.

## Kết quả QA

- **PASS:** 501 JSONL / 55.976 bản ghi; đối chiếu từng trường với checkpoint 028.
- Chỉ bổ sung **240 mục `vi`**; toàn bộ **8.969 mục dịch cũ** và trường nguồn được giữ nguyên.
- Mã kỹ thuật đúng **danh sách và thứ tự**; Unicode NFC; không CR/LF/tab trong `vi`; mỗi trang tối đa 3 dấu `▼`, 34 ký tự nhìn thấy/dòng; kiểm tra byte budget nếu có.
- ZIP chứa toàn bộ 501 JSONL và lịch sử các đợt trước; không chứa ROM thương mại hoặc patch ROM.
- **Chưa kiểm thử ROM NDS / độ rộng pixel thật.** QA mới xác nhận dữ liệu và ngưỡng ký tự.

## Tiếp theo — đợt 030

- `0028.003` — 120 trang chưa dịch.
- `0028.004` — 120 trang chưa dịch.
- Tổng **240 trang**, bảo toàn mã lệnh, ngôi xưng, cập nhật GitHub sau QA.