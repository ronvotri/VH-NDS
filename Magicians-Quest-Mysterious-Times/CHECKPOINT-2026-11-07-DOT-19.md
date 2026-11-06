# Magician’s Quest: Mysterious Times — Checkpoint 019

**Ngày:** 07/11/2026  
**Repo:** `ronvotri/VH-NDS`, thư mục `Magicians-Quest-Mysterious-Times/`  
**Baseline:** `MagiciansQuest-VietHoa-Checkpoint-018.zip` (6.711 mục)  
**Mốc mới:** **6.951/55.976 mục (12,42%)**, thêm **240 trang NPC**.

## Tiến độ

| Nhóm | Đã dịch | Tổng | Mới |
|---|---:|---:|---:|
| 00 — Mở đầu | 106 | 106 | 0 |
| 01 — Hệ thống | 1.086 | 1.087 | 0 |
| 02 — Vật phẩm | 1.501 | 1.501 | 0 |
| 03 — Sổ tay | 432 | 432 | 0 |
| 04 — Hội thoại | 3.826 | 52.608 | +240 |
| 05 — Credit | 0 | 242 | 0 |
| **Tổng** | **6.951** | **55.976** | **+240** |

## Phạm vi đợt 019

- `translation/04-thoai/talkfigs__0eng__data__0024.001.jsonl`: **120 trang**, NPC yêu suy luận, từ nấu ăn luyện não, câu cá để nghỉ ngơi, dọn phòng, thư viện, trang phục cho tới giao tiếp xã hội.
- `translation/04-thoai/talkfigs__0eng__data__0024.002.jsonl`: **120 trang**, chuyện bài tập, trường học, nghề nghiệp tương lai, thể thao, hẹn hò, tình yêu, Halloween và kỷ niệm mùa đông.
- `vi_0024_001.txt`, `vi_0024_002.txt`: lời Việt viết tay, đúng thứ tự trang nguồn. `manual_0024_001.tsv`, `manual_0024_002.tsv`: bản đối chiếu ID / tiếng Việt.
- `apply_019.py`: công cụ chèn trường `vi` có giữ mã, tách dòng. `qa_019.py`: đối chiếu với checkpoint 018. `DELTA-019.jsonl` là nhật ký thay đổi toàn bộ 240 mục.

## QA

- **PASS:** đủ 501 JSONL và 55.976 bản ghi, 240 trường `vi` mới, các trường khác bất biến; không ghi đè lời Việt cũ.
- Bảo toàn mọi biến `$500;`, thẻ biểu cảm `$024`, `$023`, `$022`, vị trí theo đúng thứ tự; Unicode NFC, giới hạn tối đa 34 ký tự hiển thị/đoạn xuống dòng, không có CR/LF/tab. Số `▼` không quá 3.
- **Chưa thử nghiệm ROM thật**, cần QA font tiếng Việt, độ rộng pixel, xuống dòng biến tên người chơi và ngôi xưng trong từng nhánh tương tác.
- ZIP chứa văn bản, mã nguồn và tài liệu, không kèm ROM thương mại.

## Mốc đợt 020

Tiếp theo `0024.003` (120) và `0024.004` (120) chưa dịch. Tiếp tục bảo toàn `vi` cũ, thuật ngữ **Bách Hóa Tổng Hợp**, **Điểm Hẹn Hò** và văn phong **tớ–cậu** của NPC đồng trang lứa.