# Magician’s Quest: Mysterious Times — Việt hóa Nintendo DS

**Checkpoint mới nhất: 031 (07/11/2026) — 9.660 / 55.976 mục (17,26%).** Đợt 031 dịch thêm **211 trang thoại NPC** (`0028.005`: 91; `0029.001`: 120). Xem `CHECKPOINT-2026-11-07-DOT-31.md` và `QA-031.md`.

**Repository chung:** https://github.com/ronvotri/VH-NDS/tree/main/Magicians-Quest-Mysterious-Times

## Nguyên tắc

- Tiếng Việt tự nhiên, tinh nghịch và hài đúng tính cách nhân vật, không lạm dụng meme; bạn bè dùng **tớ–cậu**.
- Thuật ngữ: **The Emporium → Bách Hóa Tổng Hợp**; **Lovers' Point → Điểm Hẹn Hò**; tên riêng nhất quán.
- Chỉ thêm trường `vi`; không đổi `id`, `en`, `ctx` hay thứ tự mục. Giữ nguyên mã biểu cảm, biến tên `$500;`, `$515;`, `$503'...;`, mã lựa chọn `$019'...;` và mã màu `$000'...;`.

## Đợt 031

- `translation/04-thoai/talkfigs__0eng__data__0028.005.jsonl`: 91 trang, nhánh hẹn hò, lịch hẹn, mối quan hệ và chuyện với bạn cũ.
- `translation/04-thoai/talkfigs__0eng__data__0029.001.jsonl`: 120 trang, lời thoại NPC mới về ngày nghỉ, mua sắm, trà bánh, dọn dẹp và tình huống ngốc nghếch dễ thương.
- `vi_0028_005_raw.txt`, `vi_0029_001_raw.txt`, `vi_0028_005.txt`, `vi_0029_001.txt`: bản dịch tay và bản ngắt dòng.
- `DELTA-031.jsonl`, `qa_031.py`, `QA-031.md`, `CHECKPOINT-2026-11-07-DOT-31.md`, `BAN_GIAO.md`.

**QA PASS:** 501 tệp JSONL / 55.976 bản ghi, 211 `vi` mới, không ghi đè bản dịch cũ. **Chưa kiểm thử in-game.** ZIP checkpoint đầy đủ không chứa ROM.

**Đợt 032:** `0029.002` (120 trang); tiếp `0029.003` nếu có thể.