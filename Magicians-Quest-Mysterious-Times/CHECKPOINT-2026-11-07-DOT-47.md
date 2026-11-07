# Magician’s Quest: Mysterious Times — Checkpoint 047

**Ngày:** 07/11/2026  
**Repository:** `ronvotri/VH-NDS` → `Magicians-Quest-Mysterious-Times/`  
**Nguồn:** `MagiciansQuest-VietHoa-Checkpoint-046.zip`  
**Kết quả:** **13.429 / 55.976 mục (23,99%)**, +240 trang thoại NPC.

## Tiến độ

| Nhóm | Đã dịch | Tổng | Tăng |
|---|---:|---:|---:|
| 00 — Mở đầu | 106 | 106 | 0 |
| 01 — Hệ thống | 1.086 | 1.087 | 0 |
| 02 — Vật phẩm | 1.501 | 1.501 | 0 |
| 03 — Sổ tay | 432 | 432 | 0 |
| 04 — Hội thoại NPC | 10.304 | 52.608 | +240 |
| 05 — Credit | 0 | 242 | 0 |
| **Tổng** | **13.429** | **55.976** | **+240** |

## Nội dung đã dịch

- `0033.012` — **120 trang**: nàng tiên cá kể vì sao từ bỏ hoàng tử; siren tự tin đến mức tự mê nhan sắc; Yeti nhờ học thần chú Mưa Hoa; Cerberus giữ cổng Âm Phủ; lời giới thiệu người bạn sống lẩn tránh dưới cống.
- `0033.013` — **120 trang**: tiếp diễn nhiệm vụ đưa người bạn đến chỗ Charlie mà không bị phát hiện; chia tay cảm động; du khách sống dưới lòng đất hiểu sai sách du lịch và muốn đến Cây Nấm, Điểm Hẹn Hò, phế tích; Cấm Thư nhờ tìm các trang bỏ trốn.
- Xưng hô theo vai: nàng tiên cá/siren “tôi–cậu”, Yeti “ta–cậu” nói ngắn, Cerberus “ta–nhóc”, bạn bị xa lánh “tôi–cậu”, du khách lòng đất “tui–cậu” mộc mạc.

## Các tệp bàn giao

- `translation/04-thoai/talkfigs__0eng__data__0033.012.jsonl`, `0033.013.jsonl`: 240 bản dịch hoàn chỉnh.
- `manual_0033_012.tsv`, `manual_0033_013.tsv`: bảng ID–EN–VI–ctx (mỗi tệp 120 câu + header).
- `vi_0033_012_raw.txt`, `vi_0033_013_raw.txt`: bản dịch từng trang với `¤` đánh dấu vị trí mã gốc; `vi_0033_012.txt`, `vi_0033_013.txt`: bản hoàn chỉnh với token và ngắt dòng.
- `apply_047.py`, `qa_047.py`, `QA-047.md`, `DELTA-047.jsonl`: chương trình áp bản dịch, QA và diff 240 mục.

## QA và giới hạn

**PASS:** so sánh theo trường toàn bộ 501 JSONL / 55.976 bản ghi với ZIP 046; chỉ điền `vi` trong hai tệp đích, giữ nguyên 13.189 bản dịch cũ, mã điều khiển và cấu trúc. Đã xác minh ZIP hoàn chỉnh, không có ROM thương mại.

**Chưa chạy game trên ROM NDS**, chưa đo độ rộng pixel bằng font thật hoặc kiểm tra chỗ thay tên động.

## Đợt 048 tiếp theo

`0033.014` và `0033.015`, mỗi tệp **120 trang**, tổng **240 trang**; nguồn có sẵn trong ZIP và dự kiến stage lên GitHub để dịch ở lần sau.