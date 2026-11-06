# Magician's Quest: Mysterious Times — Việt hóa Nintendo DS

Dự án con trong [ronvotri/VH-NDS](https://github.com/ronvotri/VH-NDS), lưu riêng theo game.

## Checkpoint mới nhất: 008 (06/11/2026)

**4.450/55.976 mục có `vi` (7,95%)** — +178 trang NPC từ checkpoint 007.

- Mở đầu 106/106; hệ thống 1.086/1.087; vật phẩm 1.501/1.501; sổ tay 432/432; hội thoại **1.325/52.608**; credit 0/242.
- Vừa dịch trọn hai tệp `talkfigs__0eng__data__0010.001.jsonl` (84 trang) và `talkfigs__0eng__data__0011.001.jsonl` (94 trang).
- **Chưa thử ROM/font pixel**, không gọi là bản hoàn thiện.

## Văn phong và ngôi xưng

Gen Z tinh nghịch, ngắn gọn, hài có duyên nhưng không lạm dụng meme. Câu mở đầu được duyệt: **“Em mê tụ tập, quẩy banh nóc với bạn bè!”**. Người dẫn chuyện lớn tuổi **ta – em**, giáo viên **thầy/cô – em** khi xác minh vai, bạn cùng lứa **tớ – cậu**, hệ thống trung tính. Giữ token, biến và trình tự gốc; không thêm giới tính/danh xưng khi thiếu ngữ cảnh.

## Tệp tiếp nối

- [`CHECKPOINT-2026-11-06-DOT-08.md`](CHECKPOINT-2026-11-06-DOT-08.md) — mốc, nhóm đã dịch và công việc tiếp theo.
- [`QA-008.md`](QA-008.md) — đối chiếu 501 JSONL, không có lỗi hay cảnh báo dòng dài.
- [`DELTA-008.jsonl`](DELTA-008.jsonl) — 178 bản dịch mới, có ID/EN/VI.
- [`manual_0010.txt`](manual_0010.txt), [`manual_0011.txt`](manual_0011.txt) — bản dịch được đánh số theo thứ tự hàng trong từng JSONL.
- [`apply_008.py`](apply_008.py), [`qa_008.py`](qa_008.py) — ghép vào baseline 007 và chạy QA (cần có checkpoint 007 ở thư mục sibling khi dùng trực tiếp).
- [`translation/`](translation/) — dữ liệu JSONL đã cập nhật, có thể dựng patch khi có ROM USA sạch hợp lệ.
- [`QUY_UOC_DICH_VI.md`](QUY_UOC_DICH_VI.md) — quy ước ngôi xưng, thuật ngữ, giữ byte/mã lệnh.

**Kế tiếp:** dịch các cụm NPC mới sau `0011`, bắt đầu rà `0013`–`0015`. Không đưa ROM thương mại lên GitHub.