# Magician’s Quest: Mysterious Times — Việt hóa Nintendo DS

**Checkpoint mới nhất: 028 (07/11/2026) — 8.969 / 55.976 mục (16,02%).** Đợt 028 dịch thêm **201 trang thoại NPC** (`0027.004`: 120; `0027.005`: 81). Xem `CHECKPOINT-2026-11-07-DOT-28.md` và `QA-028.md`.

**Repository chung:** https://github.com/ronvotri/VH-NDS/tree/main/Magicians-Quest-Mysterious-Times

## Nguyên tắc

- Tiếng Việt tự nhiên, tinh nghịch và hài đúng tính cách nhân vật, không lạm dụng meme; bạn bè dùng **tớ–cậu**.
- Thuật ngữ: **The Emporium → Bách Hóa Tổng Hợp**; **Lovers' Point → Điểm Hẹn Hò**; tên riêng nhất quán.
- Chỉ thêm trường `vi`; không đổi `id`, `en`, `ctx` hay thứ tự mục. Giữ nguyên mã biểu cảm, biến tên `$500;`, `$515;`, `$503'...;` và mã màu `$000'...;`.

## Đợt 028

- `translation/04-thoai/talkfigs__0eng__data__0027.004.jsonl`: 120 trang, chuyện ghen bạn, tặng quà, rủ đi chơi, học nhóm, tỏ tình và chọn câu trả lời.
- `translation/04-thoai/talkfigs__0eng__data__0027.005.jsonl`: 81 trang, bạn thân, giờ hẹn, lời hứa, tâm sự và hoạt động chung.
- `vi_0027_004.txt`, `vi_0027_005.txt`: văn bản dịch tay; `manual_0027_004.tsv`, `manual_0027_005.tsv`: bảng đối chiếu ID / nguồn EN / Việt.
- `apply_028.py`, `qa_028.py`, `DELTA-028.jsonl`, `QA-028.md`, `CHECKPOINT-2026-11-07-DOT-28.md`, `BAN_GIAO.md`.

**QA PASS:** 501 tệp JSONL / 55.976 bản ghi, đúng 201 trường `vi` mới; không ghi đè các mục đã dịch. **Chưa thử hiển thị trong ROM NDS**. ZIP không chứa ROM thương mại.

**Đợt 029:** tiếp tục `0028.001` (120 trang) và `0028.002` (120 trang).