# Magician’s Quest: Mysterious Times — Việt hóa Nintendo DS

**Checkpoint mới nhất: 027 (07/11/2026) — 8.768 / 55.976 mục (15,66%).** Đợt 027 dịch thêm **240 trang thoại NPC** (`0027.002`: 120, `0027.003`: 120). Xem `CHECKPOINT-2026-11-07-DOT-27.md` và `QA-027.md`.

**Repository chung:** https://github.com/ronvotri/VH-NDS/tree/main/Magicians-Quest-Mysterious-Times

## Nguyên tắc

- Tiếng Việt tự nhiên, tinh nghịch và hài đúng tính cách nhân vật, không lạm dụng meme; bạn bè dùng **tớ–cậu**.
- Thuật ngữ: **The Emporium → Bách Hóa Tổng Hợp**; **Lovers' Point → Điểm Hẹn Hò**; tên riêng được giữ nhất quán.
- Chỉ thêm trường `vi`; không đổi `id`, `en`, `ctx` hay thứ tự mục. Giữ nguyên mã biểu cảm, biến tên `$500;`, `$515;`, `$503'...;` và mã màu `$000'...;`.

## Đợt 027

- `translation/04-thoai/talkfigs__0eng__data__0027.002.jsonl`: 120 trang, học hành, chuyện yêu đương, hoa và chuyến trốn tìm đáng sợ.
- `translation/04-thoai/talkfigs__0eng__data__0027.003.jsonl`: 120 trang, mùa lễ hội, thời trang, nấu ăn, tình bạn và ước mơ nghề nghiệp.
- `vi_0027_002.txt`, `vi_0027_003.txt`: văn bản dịch tay; `manual_0027_002.tsv`, `manual_0027_003.tsv`: bảng đối chiếu ID / nguồn EN / Việt.
- `apply_027.py`, `qa_027.py`, `DELTA-027.jsonl`, `QA-027.md`, `CHECKPOINT-2026-11-07-DOT-27.md`, `BAN_GIAO.md`.

**QA PASS:** 501 tệp JSONL / 55.976 bản ghi, đúng 240 trường `vi` mới; không ghi đè các mục đã dịch. **Chưa thử hiển thị trong ROM NDS**. ZIP không chứa ROM thương mại.

**Đợt 028:** tiếp tục `0027.004` (120 trang) và `0027.005` (81 trang).