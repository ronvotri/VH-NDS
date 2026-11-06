# Magician’s Quest: Mysterious Times — Việt hóa Nintendo DS

Dự án riêng trong **[VH-NDS](https://github.com/ronvotri/VH-NDS)**, không lẫn với Ni no Kuni hoặc Pokémon Dash.

**Checkpoint mới nhất: 004 — ngày 06/11/2026.** Đã xử lý **3.382/55.976 mục** (+1.368 mục so với 003), trong đó có tên riêng/nhãn được duyệt để nguyên.

| Nhóm | Đã điền / tổng |
|---|---:|
| Mở đầu | 106/106 |
| Hệ thống | 1.086/1.087 |
| **Vật phẩm** | **1.501/1.501** |
| **Sổ tay** | **432/432** |
| Hội thoại | 257/52.608 |
| Credit | 0/242 |

## Giọng văn

> **“Em mê tụ tập, quẩy banh nóc với bạn bè!”**

Vui nhộn, đáng yêu, gần gũi Gen Z; tuyệt đối không xưng hô tùy tiện. Người dẫn chuyện `ta–em`, giáo viên `thầy/cô–em`, bạn bè `tớ–cậu` khi xác định quan hệ; phản ứng chung chưa xác định người nói giữ trung tính.

## File quan trọng

- [CHECKPOINT-2026-11-06-DOT-04.md](CHECKPOINT-2026-11-06-DOT-04.md): lô 004, hướng dẫn nối phiên, hạn chế hiện tại.
- [QUY_UOC_DICH_VI.md](QUY_UOC_DICH_VI.md): luật dịch và kỹ thuật.
- [QA-004.md](QA-004.md): xác minh chỉ trường `vi` thay đổi.
- `translation/02-vat-pham/`: toàn bộ 1.501 tên/lệnh vật phẩm đã điền.
- `translation/03-so-tay/`: toàn bộ 432 mục sổ tay đã điền.
- `translation/04-thoai/`: bắt đầu dịch 257 mục (99 câu cửa miệng theo `ctx` + 158 phản ứng ngắn).
- [DELTA-004.jsonl](DELTA-004.jsonl): danh sách 1.368 mục đợt mới.
- [translation/THUAT_NGU-004.tsv](translation/THUAT_NGU-004.tsv): 1.111 mục vật phẩm mới để tái sử dụng thuật ngữ.
- `mq_batch_004*.py`, `mq_check_004.py`, `qa_checkpoint.py`: nguồn bản dịch và công cụ QA.

**QA:** PASS cấu trúc, token và giới hạn byte; chưa test font/hiển thị trên ROM. Kho GitHub không chứa ROM thương mại.

**Tiếp theo:** phần hội thoại (`04-thoai`), ưu tiên ngữ cảnh NPC rõ ràng; cập nhật GitHub sau từng checkpoint.