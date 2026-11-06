# Magician’s Quest: Mysterious Times — Việt hóa Nintendo DS

Repo chung: [ronvotri/VH-NDS](https://github.com/ronvotri/VH-NDS/tree/main/Magicians-Quest-Mysterious-Times). Dữ liệu từng trò chơi nằm trong thư mục riêng.

**Checkpoint mới nhất: 014 (06/11/2026) — 5.805/55.976 mục (~10,37%).** Đợt này dịch tay **240 trang NPC**: `0022.001` (120) và `0022.002` (120). Tham chiếu `CHECKPOINT-2026-11-06-DOT-14.md`.

## Phong cách đã duyệt

- Giọng văn ngộ nghĩnh, hài hước, tự nhiên kiểu Gen Z, không nhồi meme; ví dụ: **“Em mê tụ tập, quẩy banh nóc với bạn bè!”**
- Người dẫn chuyện lớn tuổi **ta–em**; thầy/cô–em khi đúng vai; bạn bè **tớ–cậu**; hệ thống trung tính.
- NPC `0022` có phong thái hơi kiêu, thích lý sự, tự tin quá đà, tạo nét hài từ chính lời nói và hoàn cảnh.
- Thuật ngữ: **The Emporium → Bách Hóa Tổng Hợp**, **Lovers' Point → Điểm Hẹn Hò**.

## Bàn giao đợt 014

- `CHECKPOINT-2026-11-06-DOT-14.md`: nội dung, tiến độ, bước tiếp.
- `QA-014.md`: kết quả kiểm tra toàn bộ 501 tệp / 55.976 trường.
- `translation/04-thoai/talkfigs__0eng__data__0022.001.jsonl`, `.002.jsonl`: bản dịch mới; chỉ thay `vi`.
- `manual_0022_001.txt`, `manual_0022_002.txt`: 240 câu dịch tay theo trang.
- `apply_014.py`, `qa_014.py`, `DELTA-014.jsonl`: công cụ áp bản dịch, QA và chênh lệch từ checkpoint 013.

**Chú ý:** QA đã đạt về cấu trúc, mã điều khiển, ngắt trang và byte. Chưa kiểm thử trên phần cứng/giả lập ROM NDS USA YNNE. ZIP là checkpoint dữ liệu, không chứa ROM thương mại.

**Bắt đầu đợt 015:** dịch `0022.003`, tiếp theo `0022.004`; ghi đè chỉ trường `vi`, không sửa bản cũ nếu chưa được duyệt.