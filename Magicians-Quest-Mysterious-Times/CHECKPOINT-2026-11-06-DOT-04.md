# Magician’s Quest: Mysterious Times — Checkpoint 004

**Ngày:** 06/11/2026 · **Kho:** `ronvotri/VH-NDS` · **Thư mục:** `Magicians-Quest-Mysterious-Times/`

## Kết quả

| Nhóm | Có `vi` | Tổng | Đợt 004 |
|---|---:|---:|---:|
| 00 — Mở đầu | 106 | 106 | +0; giữ câu “Em mê tụ tập, quẩy banh nóc với bạn bè!” |
| 01 — Hệ thống | 1.086 | 1.087 | +0 |
| 02 — Vật phẩm | **1.501** | **1.501** | **+1.111**, toàn bộ tên quần áo, nội thất, hình nền, sinh vật |
| 03 — Sổ tay | **432** | **432** | +0 |
| 04 — Hội thoại | 257 | 52.608 | **+257** (99 câu cửa miệng NPC và 158 đoạn phản ứng/phát ngôn ngắn) |
| 05 — Credit | 0 | 242 | +0 |
| **Tổng** | **3.382** | **55.976** | **+1.368** |

**Điểm cần hiểu:** “đã có `vi`” có thể bao gồm tên riêng hoặc nhãn được duyệt giữ nguyên tiếng Anh. Toàn bộ hội thoại dài vẫn chưa dịch; không được nói là đã Việt hóa toàn game.

## Phong cách đã khóa

- **“Em mê tụ tập, quẩy banh nóc với bạn bè!”** (giọng Gen Z dí dỏm, đúng lúc, không nhồi meme).
- Người dẫn chuyện lớn tuổi `ta–em`; giáo viên `thầy/cô–em`; bạn cùng lớp `tớ–cậu` **chỉ khi xác nhận vai**.
- Các đoạn phản ứng chung `onemsg00` không xác nhận được vai nói: dịch ngắn gọn **trung tính, tránh đoán ngôi xưng**; những câu cần thể hiện quan hệ sẽ rà lại khi có ngữ cảnh NPC.
- Tên vật phẩm theo một quy ước: **Sofa** cho ghế sofa, **Tủ Áo** cho wardrobe, **Váy** cho skirt, **Đầm** cho dress, **Trượng** cho staff; tên động vật đồng nhất với sổ tay ở đợt 003.

## Danh sách tệp dịch mới

- `translation/02-vat-pham/item__ItemName_e.ofs.004.jsonl` đến `item__ItemName_e.ofs.013.jsonl`: 1.111 mục.
- `translation/04-thoai/npc__NpcDataOfs_e.bin.001.jsonl`: 99 mục, đi cùng `ctx` ghi tên NPC.
- `translation/04-thoai/talk__msg__onemsg00_e.ofs.001.jsonl` và `.002.jsonl`: 158 mục (36 + 20 dòng tiếng Nhật dự phòng chưa điền; không giả vờ đã dịch).
- `DELTA-004.jsonl`: 1.368 dòng mới, dùng để kiểm tra/ghép tiến độ.
- `mq_batch_004.py`, `mq_batch_004_fashion.py`, `mq_batch_004_npc.py`, `mq_batch_004_chat.py`: mã bảng dịch và ánh xạ; chạy theo thứ tự trên checkpoint 003.
- `mq_check_004.py` và `QA-004.md`: kiểm tra chênh lệch 003 → 004.
- `translation/THUAT_NGU-004.tsv`: 1.111 tên vật phẩm mới, sử dụng cho hội thoại và tìm kiếm vật phẩm sau này.

## QA

1. `python qa_checkpoint.py`: PASS (mã điều khiển, giới hạn UTF-8 byte, Unicode NFC).
2. `python mq_check_004.py`: PASS. **1.368 bản ghi chỉ đổi trường `vi` trên 13 tệp, không sửa `id`, `en`, `ctx`, thứ tự hay mã cấu trúc**.
3. **Chưa có kiểm thử trong ROM máy thật/giả lập**; một số tên nội thất dài có thể cần rút gọn sau khi test UI. Chưa có bản ROM sạch USA trong đầu vào. Không lưu ROM thương mại trong kho.

## Bắt đầu đợt 005

1. Dùng chính ZIP checkpoint 004 hoặc dữ liệu nguồn trong GitHub làm mốc; **không quay lại checkpoint 001/002**.
2. Tập trung vào `translation/04-thoai/`, ưu tiên chuỗi có thể xác định vai và quan hệ trong cùng cụm. Xem `ctx` từ tệp NPC/nguồn; không tự đoán quan hệ khi thiếu ngữ cảnh.
3. Dịch các nhóm thoại, kiểm tra token `$500;`, `$503'...;` và ba cột tab; tránh dịch các dòng tiếng Nhật rõ ràng chỉ là chỗ dự phòng cho đến khi xác nhận chúng có hiển thị trong game.
4. QA → cập nhật checkpoint, delta và GitHub mỗi lô.