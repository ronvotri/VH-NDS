# Magician's Quest: Mysterious Times — Việt hóa Nintendo DS

Dự án con trong [ronvotri/VH-NDS](https://github.com/ronvotri/VH-NDS) — lưu mỗi game một thư mục, tránh lẫn với Ni no Kuni và Pokémon Dash.

## Checkpoint mới nhất: 006 (06/11/2026)

**4.082/55.976 mục đã có `vi` (7,29%)**, tăng **368 trang thoại NPC** so với checkpoint 005.

- Mở đầu 106/106; hệ thống 1.086/1.087; vật phẩm 1.501/1.501; sổ tay 432/432; hội thoại **957/52.608**; credit 0/242.
- Các tệp thoại dịch trong đợt này: `0002.001`, `0003.001`, `0006.001`, `0007.001`, `0008.001` (tổng 5 tệp).
- Chưa kiểm tra pixel-width/font trực tiếp trên ROM USA nên **chưa gọi bản vá là hoàn thành**.

## Phong cách đã duyệt

Lời thoại dễ thương, hài hước, gần gũi Gen Z mà giữ đúng nghĩa câu gốc; ví dụ **“Em mê tụ tập, quẩy banh nóc với bạn bè!”**. Giữa học sinh/bạn bè: **tớ – cậu**. Người dẫn chuyện lớn tuổi: **ta – em**. Giáo viên: theo vai **thầy/cô – em**. Không pha trộn ngôi xưng trong cùng nhân vật; chú ý mã `ctx` khi ghép kịch bản.

## Tài liệu

- [`CHECKPOINT-2026-11-06-DOT-06.md`](CHECKPOINT-2026-11-06-DOT-06.md): bảng tiến độ và thứ tự bước tiếp theo.
- [`QA-006.md`](QA-006.md): bằng chứng đối chiếu 501 JSONL và 368 dòng mới.
- [`DELTA-006.jsonl`](DELTA-006.jsonl): chỉ các bản ghi dịch mới, có ID/EN/VI.
- [`translation/`](translation/): toàn bộ 501 JSONL để tiếp nối khi chuyển phiên.
- [`manual_0002.txt`](manual_0002.txt), ... các file `manual_0003.txt`, `manual_0006.txt`, `manual_0007.txt`, `manual_0008.txt`: lời dịch theo thứ tự gốc.
- [`apply_006.py`](apply_006.py), [`qa_006.py`](qa_006.py): script áp dụng từ 005 và QA.
- [`QUY_UOC_DICH_VI.md`](QUY_UOC_DICH_VI.md): luật ngôi xưng, mã điều khiển và thuật ngữ.

**Tiếp theo:** đợt 007 chuyển sang nhóm NPC trong file `0004.001`, `0005.001` và các chuỗi hội thoại tiếp theo. Chỉ đưa bản dịch/tài liệu vào repo; không đưa ROM thương mại.