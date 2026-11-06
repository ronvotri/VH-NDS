# Magician’s Quest: Mysterious Times — Việt hóa Nintendo DS

Repo chung: [ronvotri/VH-NDS](https://github.com/ronvotri/VH-NDS/tree/main/Magicians-Quest-Mysterious-Times). Mỗi game có thư mục riêng.

**Checkpoint mới nhất: 015 (06/11/2026) — 6.045/55.976 mục (10,80%).** Đợt 015 dịch tay **240 trang thoại NPC**, `0022.003` và `0022.004` (mỗi tệp 120 trang). Đọc `CHECKPOINT-2026-11-06-DOT-15.md`.

## Phong cách đã duyệt

- Lời thoại ngộ nghĩnh, tự nhiên, hài đúng tình huống kiểu Gen Z; ví dụ: **“Em mê tụ tập, quẩy banh nóc với bạn bè!”**. Không nhồi meme.
- Người dẫn chuyện lớn tuổi **ta–em**; thầy/cô–em khi đúng vai; bạn bè **tớ–cậu**; thông báo hệ thống dùng **bạn**.
- NPC cụm `0022` có vẻ tự phụ, hay lý sự nhưng thường tự làm mình quê; giữ sắc thái đó khi dịch.
- Thuật ngữ: **The Emporium → Bách Hóa Tổng Hợp**, **Lovers’ Point → Điểm Hẹn Hò**.

## Dữ liệu checkpoint 015

- `translation/04-thoai/talkfigs__0eng__data__0022.003.jsonl` + `.004.jsonl`: 240 câu mới, chỉ thay `vi`.
- `manual_0022_003.txt` + `manual_0022_004.txt`: lời dịch tay theo thứ tự từng trang.
- `apply_015.py`, `qa_015.py`, `DELTA-015.jsonl`, `QA-015.md`: script áp, so sánh với checkpoint 014, bản chênh và báo cáo QA.
- `CHECKPOINT-2026-11-06-DOT-15.md`: tiến độ và chỉ dẫn nối phiên.

**QA cấu trúc: PASS**, 501 JSONL, 55.976 bản ghi, 0 lỗi mã điều khiển/giới hạn ký tự/byte/ghi đè. **Chưa QA hiển thị thực tế trên ROM NDS.** Không chứa ROM thương mại.

**Tiếp đợt 016:** dịch `0022.005` (120 trang), rồi `0023.001` (120 trang), giữ các quy ước trên.