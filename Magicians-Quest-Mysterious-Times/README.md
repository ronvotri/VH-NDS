# Magician’s Quest: Mysterious Times — Việt hóa Nintendo DS

**Checkpoint mới nhất: 033 (07/11/2026) — 10.088 / 55.976 mục (18,02%).** Đợt 033 dịch thêm **188 trang thoại NPC** (`0029.004`: 120; `0029.005`: 68). Xem `CHECKPOINT-2026-11-07-DOT-33.md` và `QA-033.md`.

**Repository chung:** https://github.com/ronvotri/VH-NDS/tree/main/Magicians-Quest-Mysterious-Times

## Nguyên tắc

- Tiếng Việt tự nhiên, tinh nghịch và hài theo tính cách nhân vật, không lạm dụng meme; bạn bè dùng **tớ–cậu**.
- Thuật ngữ: **The Emporium → Bách Hóa Tổng Hợp**; **Lovers' Point → Điểm Hẹn Hò**; tên riêng giữ nhất quán.
- Chỉ thêm trường `vi`; không đổi `id`, `en`, `ctx`, giới hạn byte hay thứ tự mục. Giữ nguyên mã biểu cảm, biến tên `$500;`, `$515;`, `$503'...;`, mã lựa chọn `$019'...;` và mã màu `$000'...;`.

## Đợt 033

- `translation/04-thoai/talkfigs__0eng__data__0029.004.jsonl`: 120 trang, lời rủ đi chơi, uống nước, học nhóm, các nhánh hẹn hò và tỏ tình tại Điểm Hẹn Hò.
- `translation/04-thoai/talkfigs__0eng__data__0029.005.jsonl`: 68 trang, lựa chọn giờ hẹn, lời nhắc giữ lời và hồi tưởng về những người bạn thân, những buổi câu cá, bắt côn trùng, mua sắm, học nhóm, uống trà.
- `vi_0029_004_raw.txt`, `vi_0029_005_raw.txt`: bản dịch tay; `vi_0029_004.txt`, `vi_0029_005.txt`: phiên bản có token và ngắt dòng; `manual_0029_004.tsv`, `manual_0029_005.tsv`: bảng EN/VI/ID.
- `wrap_033.py`, `qa_033.py`, `DELTA-033.jsonl`, `QA-033.md`, `CHECKPOINT-2026-11-07-DOT-33.md`.

**QA PASS:** 501 JSONL / 55.976 bản ghi, +188 mục `vi`, không ghi đè bản dịch cũ. **Chưa kiểm tra trực tiếp trong ROM NDS.** ZIP bàn giao không gồm ROM thương mại.

**Đợt 034:** `0030.001` (120 trang) và `0030.002` (120 trang).