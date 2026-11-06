# Magician’s Quest: Mysterious Times — Việt hóa Nintendo DS

**Checkpoint mới nhất: 026 (07/11/2026) — 8.528 / 55.976 mục (15,24%).** Đợt 026 dịch thêm **220 trang NPC** (`0026.005`: 100, `0027.001`: 120). Xem `CHECKPOINT-2026-11-07-DOT-26.md` và `QA-026.md`.

**Repository chung:** https://github.com/ronvotri/VH-NDS/tree/main/Magicians-Quest-Mysterious-Times

## Nguyên tắc

- Dịch tiếng Việt tự nhiên, vui nhộn vừa phải, không lạm dụng meme; nhất quán lời thoại NPC; bạn bè xưng **tớ–cậu**.
- Thuật ngữ: **The Emporium → Bách Hóa Tổng Hợp**, **Lovers' Point → Điểm Hẹn Hò**.
- Chỉ bổ sung trường `vi`; giữ nguyên `id`, `en`, `ctx`, mã biểu cảm, thứ tự và lựa chọn. Không thay đổi các biến tên `$500;`, `$515;` hay `$503'...;`.

## Đợt 026

- `translation/04-thoai/talkfigs__0eng__data__0026.005.jsonl`: 100 trang, các lời mời gặp nhau, kết bạn thân, chốt giờ hẹn, lời nhận xét về bạn bè.
- `translation/04-thoai/talkfigs__0eng__data__0027.001.jsonl`: 120 trang, NPC nữ hoạt bát kể chuyện nhà cửa, nấu ăn, học hành, đi chơi và mua sắm.
- `vi_0026_005.txt`, `vi_0027_001.txt`: bản dịch tay; `manual_0026_005.tsv`, `manual_0027_001.tsv`: ID / tiếng Anh / tiếng Việt.
- `apply_026.py`, `qa_026.py`, `DELTA-026.jsonl`, `QA-026.md`, `CHECKPOINT-2026-11-07-DOT-26.md` và `BAN_GIAO.md`.

**QA PASS:** 501 JSONL / 55.976 mục, đúng 220 trường `vi` mới. **Chưa thử trong ROM NDS**. ZIP không chứa ROM thương mại.

**Đợt 027:** tiếp tục `0027.002` (120 trang) và `0027.003` (120 trang).