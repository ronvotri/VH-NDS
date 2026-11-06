# Magician’s Quest: Mysterious Times — Việt hóa Nintendo DS

**Checkpoint mới nhất: 025 (07/11/2026) — 8.308 / 55.976 mục (14,84%).** Đợt 025 dịch thêm **240 trang NPC** (`0026.003`: 120, `0026.004`: 120). Xem `CHECKPOINT-2026-11-07-DOT-25.md` và `QA-025.md`.

**Repository chung:** https://github.com/ronvotri/VH-NDS/tree/main/Magicians-Quest-Mysterious-Times

## Nguyên tắc

- Dịch tiếng Việt tự nhiên, hài hước vừa phải, không nhồi meme. Giữ phong cách riêng từng NPC; với bạn bè đồng trang lứa dùng **tớ–cậu**.
- Thuật ngữ thống nhất: **The Emporium → Bách Hóa Tổng Hợp**, **Lovers Point → Điểm Hẹn Hò**.
- Chỉ sửa trường `vi`; giữ nguyên `id`, `en`, `ctx`, mã điều khiển, thứ tự và nhánh lựa chọn. Giữ biến tên `$500;`, `$515;`, `$503;`.

## Đợt 025

- `translation/04-thoai/talkfigs__0eng__data__0026.003.jsonl`: 120 trang, ngày lễ, sở thích, ứng xử, lòng can đảm và sự tự lập.
- `translation/04-thoai/talkfigs__0eng__data__0026.004.jsonl`: 120 trang, tình bạn, rủ đi chơi, uống trà, học nhóm, tâm sự và lựa chọn hẹn hò.
- `vi_0026_003.txt`, `vi_0026_004.txt`: bản dịch tay; `manual_0026_003.tsv`, `manual_0026_004.tsv`: ID / tiếng Anh / tiếng Việt.
- `apply_025.py`, `qa_025.py`, `DELTA-025.jsonl`, `QA-025.md`, `CHECKPOINT-2026-11-07-DOT-25.md` và `BAN_GIAO.md`.

**QA PASS:** 501 JSONL / 55.976 mục, đúng 240 trường `vi` mới, không ghi đè dữ liệu cũ. **Chưa kiểm thử trong ROM NDS**. ZIP checkpoint không chứa ROM thương mại.

**Đợt 026:** tiếp tục `0026.005` (100 trang) và `0027.001` (120 trang).