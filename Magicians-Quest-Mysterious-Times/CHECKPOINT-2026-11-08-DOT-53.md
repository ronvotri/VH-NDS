# Magician’s Quest: Mysterious Times — Checkpoint 053

**Ngày:** 08/11/2026  
**Repository:** `ronvotri/VH-NDS`, thư mục `Magicians-Quest-Mysterious-Times/`  
**Mốc trước:** checkpoint 052 — **14.592/55.976 (26,07%)**  
**Mốc mới:** **14.832/55.976 (26,50%)** — +240 mục; hội thoại NPC **11.707/52.608**.

## Nội dung đợt 053

| Tệp | Số trang | Nội dung |
|---|---:|---|
| `translation/04-thoai/talkfigs__0eng__data__0040.003.jsonl` | 120 | Tâm sự về bạn học `$515;`, chuyện hẹn hò, Điểm Hẹn Hò, những hoạt động bạn bè, sự kiện mùa và thư điện tín xin lỗi |
| `translation/04-thoai/talkfigs__0eng__data__0040.004.jsonl` | 120 | Hoạt động ngoại khóa, chia tay bạn thân để trân trọng tình bạn, chào hỏi và đối thoại kết thúc hẹn hò |
| **Tổng** | **240** | Ngôi xưng bạn bè `tớ–cậu`; tính cách kiêu kỳ nhưng duyên dáng; giữ thoại lặp trong các nhánh |

## Bàn giao và kiểm chứng

- `vi_0040_003_raw.txt`, `vi_0040_004_raw.txt`: 120 dòng dịch có biên tập mỗi tệp; ký hiệu `¤` là vị trí của mã động không thuộc tiền tố biểu cảm.
- `build_raw_053.py` tái tạo những nhóm thoại lặp nguyên bản ở `0040.004`; `apply_053.py` gắn mã game, ngắt dòng và không ghi đè bản dịch không khớp.
- `vi_0040_003.txt`, `vi_0040_004.txt`: kết quả cuối; `manual_0040_003.tsv`, `manual_0040_004.tsv`: bảng đối chiếu ID/EN/VI/CTX.
- `DELTA-053.jsonl`: đúng 240 bản ghi mới; `QA-053.md`, `qa_053.py`: báo cáo và công cụ kiểm tra đối chiếu checkpoint 052.
- QA PASS: **501 JSONL, 55.976 bản ghi**, toàn bộ dữ liệu cũ giữ nguyên; mã điều khiển, Unicode, ngắt dòng và giới hạn byte (nếu có) được xác minh.
- Nguồn đợt **054**: `0040.005` và `0040.006` (120 trang mỗi tệp), có sẵn trong ZIP checkpoint 053 và đưa lên GitHub với trường `vi:null`.

Chưa test chạy ROM NDS; ZIP không chứa ROM thương mại.