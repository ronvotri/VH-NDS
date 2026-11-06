# Magician’s Quest: Mysterious Times — Việt hóa Nintendo DS

**Checkpoint mới nhất: 024 (07/11/2026) — 8.068 / 55.976 mục (14,41%).** Đợt 024 dịch thêm **240 trang NPC** (`0026.001`: 120, `0026.002`: 120). Xem `CHECKPOINT-2026-11-07-DOT-24.md` và `QA-024.md`.

**Repository chung:** https://github.com/ronvotri/VH-NDS/tree/main/Magicians-Quest-Mysterious-Times

## Nguyên tắc

- Dịch tiếng Việt tự nhiên, hài hước vừa phải, không nhồi meme. Giữ phong cách riêng từng NPC; với bạn bè đồng trang lứa dùng **tớ–cậu**.
- Thuật ngữ thống nhất: **The Emporium → Bách Hóa Tổng Hợp**, **Lovers Point → Điểm Hẹn Hò**.
- Chỉ sửa trường `vi`; giữ nguyên `id`, `en`, `ctx`, mã điều khiển, thứ tự và nhánh lựa chọn. Giữ biến tên `$500;`, `$515;`, `$503;`.

## Đợt 024

- `translation/04-thoai/talkfigs__0eng__data__0026.001.jsonl`: 120 trang, nhân vật chăm học, kỷ luật, giúp đỡ bạn bè và những tình huống tự làm mình bẽ mặt.
- `translation/04-thoai/talkfigs__0eng__data__0026.002.jsonl`: 120 trang, học hành, định hướng nghề nghiệp, chuyện yêu đương, lễ hội và mùa màng.
- `vi_0026_001.txt`, `vi_0026_002.txt`: bản dịch tay từng trang; `manual_0026_001.tsv`, `manual_0026_002.tsv`: ID / tiếng Anh / tiếng Việt.
- `apply_024.py`, `qa_024.py`, `DELTA-024.jsonl`, `QA-024.md`, `CHECKPOINT-2026-11-07-DOT-24.md` và `BAN_GIAO.md`.

**QA PASS:** 501 JSONL / 55.976 mục, đúng 240 trường `vi` mới, không ghi đè dữ liệu cũ. **Chưa kiểm thử thực tế trên ROM NDS**. ZIP checkpoint không chứa ROM thương mại.

**Đợt 025:** tiếp tục `0026.003` (120 trang) và `0026.004` (120 trang).