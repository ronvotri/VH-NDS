# Magician's Quest: Mysterious Times — Việt hóa Nintendo DS

Dự án con trong [ronvotri/VH-NDS](https://github.com/ronvotri/VH-NDS) — mỗi game có thư mục riêng để không lẫn với Ni no Kuni, Pokémon Dash.

## Checkpoint mới nhất: 007 (06/11/2026)

**4.272/55.976 mục có `vi` (7,63%)**; **+190 trang hội thoại NPC** so với checkpoint 006.

- Mở đầu 106/106; hệ thống 1.086/1.087; vật phẩm 1.501/1.501; sổ tay 432/432; hội thoại **1.147/52.608**; credit 0/242.
- Đợt này dịch đủ `talkfigs__0eng__data__0004.001.jsonl` (90 trang) và `talkfigs__0eng__data__0005.001.jsonl` (100 trang).
- **Chưa kiểm tra hiển thị và độ rộng pixel trên NDS thực tế**, nên chưa gọi bản vá là hoàn thành.

## Phong cách đã được duyệt

Tinh nghịch, dễ thương, gần gũi Gen Z nhưng trung thành với cá tính nhân vật và ý nguyên bản. Ví dụ: **“Em mê tụ tập, quẩy banh nóc với bạn bè!”**. Bạn bè **tớ – cậu**; người dẫn chuyện lớn tuổi **ta – em**; giáo viên chỉ dùng **thầy/cô – em** khi nhận diện đúng vai. Không tự gán giới tính/danh xưng hay làm loạn ngôi xưng.

## Tài liệu nối phiên

- [`CHECKPOINT-2026-11-06-DOT-07.md`](CHECKPOINT-2026-11-06-DOT-07.md): tiến độ, nhóm đã dịch và việc kế tiếp.
- [`QA-007.md`](QA-007.md): kiểm tra 501 JSONL giữa checkpoint 006 và 007.
- [`DELTA-007.jsonl`](DELTA-007.jsonl): 190 bản ghi mới, có ID/EN/VI.
- [`translation/`](translation/): bản dịch được cập nhật. Repo cũng có các delta và dữ liệu checkpoint trước để tiếp tục.
- [`manual_0004.txt`](manual_0004.txt), [`manual_0005.txt`](manual_0005.txt): bản dịch theo thứ tự nguồn.
- [`apply_007.py`](apply_007.py), [`qa_007.py`](qa_007.py): script tái dựng và QA.
- [`QUY_UOC_DICH_VI.md`](QUY_UOC_DICH_VI.md): quy tắc ngôi xưng, mã điều khiển và thuật ngữ.

**Tiếp theo:** nhóm NPC `0010.001`, `0011.001`. Chỉ cập nhật bản dịch/checkpoint/công cụ, **không đưa ROM thương mại lên GitHub**.