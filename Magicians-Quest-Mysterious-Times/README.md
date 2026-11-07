# Magician’s Quest: Mysterious Times — Việt hóa Nintendo DS

**Checkpoint mới nhất: 032 (07/11/2026) — 9.900 / 55.976 mục (17,69%).** Đợt 032 dịch thêm **240 trang thoại NPC** (`0029.002`: 120; `0029.003`: 120). Xem `CHECKPOINT-2026-11-07-DOT-32.md` và `QA-032.md`.

**Repository chung:** https://github.com/ronvotri/VH-NDS/tree/main/Magicians-Quest-Mysterious-Times

## Nguyên tắc

- Tiếng Việt tự nhiên, tinh nghịch và hài theo tính cách nhân vật, không lạm dụng meme; bạn bè dùng **tớ–cậu**.
- Thuật ngữ: **The Emporium → Bách Hóa Tổng Hợp**; **Lovers' Point → Điểm Hẹn Hò**; tên riêng giữ nhất quán.
- Chỉ thêm trường `vi`; không đổi `id`, `en`, `ctx`, giới hạn byte hay thứ tự mục. Giữ nguyên mã biểu cảm, biến tên `$500;`, `$515;`, `$503'...;`, mã lựa chọn `$019'...;` và mã màu `$000'...;`.

## Đợt 032

- `translation/04-thoai/talkfigs__0eng__data__0029.002.jsonl`: 120 trang, quán cà phê, học hành, nghề nghiệp, tình yêu, các tình huống hài hước.
- `translation/04-thoai/talkfigs__0eng__data__0029.003.jsonl`: 120 trang, dã ngoại, bánh ngọt, gia đình, bạn bè, đời thường.
- `vi_0029_002_raw.txt`, `vi_0029_003_raw.txt`: bản dịch tay; `vi_0029_002.txt`, `vi_0029_003.txt`: bản ngắt dòng.
- `DELTA-032.jsonl`, `qa_032.py`, `QA-032.md`, `CHECKPOINT-2026-11-07-DOT-32.md`, `BAN_GIAO.md`.

**QA PASS:** 501 JSONL / 55.976 bản ghi, +240 mục `vi`, không ghi đè bản dịch cũ. **Chưa kiểm tra trực tiếp trong ROM NDS.** ZIP bàn giao không gồm ROM thương mại.

**Đợt 033:** dịch tiếp `0029.004` (120 trang), rồi `0029.005` (nếu phù hợp).