# Magician’s Quest: Mysterious Times — Việt hóa Nintendo DS

**Checkpoint mới nhất: 019 (07/11/2026) — 6.951 / 55.976 mục (12,42%).** Thêm **240 trang NPC** (`0024.001` = 120, `0024.002` = 120). Xem `CHECKPOINT-2026-11-07-DOT-19.md`, `QA-019.md`.

**Repository chung:** https://github.com/ronvotri/VH-NDS/tree/main/Magicians-Quest-Mysterious-Times

## Nguyên tắc

- Ngôn ngữ tự nhiên, dí dỏm có chút tinh nghịch Gen Z nhưng không nhồi meme. Bạn đồng trang lứa **tớ–cậu**, giữ giọng từng nhân vật.
- Thuật ngữ: **The Emporium → Bách Hóa Tổng Hợp**, **Lovers Point → Điểm Hẹn Hò**.
- Chỉ sửa `vi`, giữ bất biến `en`, `id`, `ctx`, các mã lệnh (`$500;`, `$024`, `$023`, `$022`, v.v.), thứ tự tệp và nhánh lựa chọn.

## Đợt 019

- `translation/04-thoai/talkfigs__0eng__data__0024.001.jsonl` — 120 trang: giải đố, nấu ăn, đi câu cá, cách suy luận rất riêng.
- `translation/04-thoai/talkfigs__0eng__data__0024.002.jsonl` — 120 trang: trường học, bài tập, nghề nghiệp mơ ước, tình yêu, sự kiện theo mùa.
- `vi_0024_001.txt`, `vi_0024_002.txt`: bản dịch tay theo đúng thứ tự ID; `manual_0024_001.tsv`, `manual_0024_002.tsv` là bản đối chiếu ID và tiếng Việt.
- Công cụ/tài liệu: `apply_019.py`, `qa_019.py`, `DELTA-019.jsonl`, `QA-019.md`, `CHECKPOINT-2026-11-07-DOT-19.md`.

**QA: PASS**, đối chiếu đủ 501 JSONL và 55.976 bản ghi, thêm 240 trường `vi`, không ghi đè. **Chưa thử dựng và hiển thị trên ROM NDS**. ZIP không chứa ROM thương mại.

**Đợt 020:** tiếp tục `0024.003` và `0024.004` (120 + 120 trang chưa dịch).