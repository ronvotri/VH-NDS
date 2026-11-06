# Magician’s Quest: Mysterious Times — Việt hóa Nintendo DS

Repo chung: [ronvotri/VH-NDS](https://github.com/ronvotri/VH-NDS/tree/main/Magicians-Quest-Mysterious-Times). Dữ liệu của trò chơi này được tách trong thư mục riêng, không lẫn với Ni no Kuni hay Pokémon Dash.

**Checkpoint mới nhất: 013 (06/11/2026) — 5.565/55.976 mục (~9,94%).** Đợt này dịch thêm **188 trang hội thoại NPC**: `0021.004` (120) và `0021.005` (68).

## Giọng văn và ngôi xưng

- Vui nhộn, ấm áp, tự nhiên kiểu Gen Z; câu mở đầu đã duyệt: **“Em mê tụ tập, quẩy banh nóc với bạn bè!”**
- Người dẫn chuyện lớn tuổi: **ta–em**; thầy cô–em khi đúng vai; bạn bè **tớ–cậu**; thông báo hệ thống trung tính.
- Tình huống tỏ tình và lời thân tình phải có cảm xúc; không nhồi meme. Tên `Lovers Point` thống nhất là **Điểm Hẹn Hò**; `The Emporium` là **Bách Hóa Tổng Hợp**.

## Bàn giao hiện tại

- [CHECKPOINT-2026-11-06-DOT-13.md](CHECKPOINT-2026-11-06-DOT-13.md) — tiến độ và tệp sẽ dịch tiếp.
- [QA-013.md](QA-013.md) — QA toàn bộ 501 tệp và 55.976 hàng.
- `translation/04-thoai/talkfigs__0eng__data__0021.004.jsonl` và `.005.jsonl` — 188 trang mới.
- `manual_0021_004.txt`, `manual_0021_005.txt` — bản dịch tay trang-ứng-trang.
- `apply_013.py`, `qa_013.py`, `DELTA-013.jsonl` — áp, rà và truy xuất thay đổi từ checkpoint 012.

**Quy tắc kỹ thuật:** chỉ sửa `vi`, giữ nguyên `id`, `en`, `ctx`, mã `$...;`/`▼` và cấu trúc. Không đưa ROM thương mại lên repo. QA kỹ thuật đã đạt nhưng chưa test hiển thị với ROM NDS sạch.

**Việc tiếp theo:** dịch cụm `0022.001`, sau đó các tệp `0022.002` trở đi.