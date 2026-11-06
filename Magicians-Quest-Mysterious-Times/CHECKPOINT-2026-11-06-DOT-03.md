# Magician's Quest: Mysterious Times — Checkpoint 003

**Ngày:** 2026-11-06 · **Nhánh:** `ronvotri/VH-NDS/main` · **Thư mục:** `Magicians-Quest-Mysterious-Times/`

## Kết quả thực tế

| Nhóm | Có `vi` | Tổng | Thay đổi đợt 003 |
|---|---:|---:|---:|
| 00 · Mở đầu | 106 | 106 | 12 câu tính cách được biên tập lại theo giọng Gen Z |
| 01 · Hệ thống | 1.086 | 1.087 | Không đổi |
| 02 · Vật phẩm | 390 | 1.501 | +360 tên: 3 trang `ItemName` đầu tiên |
| 03 · Sổ tay | 432 | 432 | +363: **đã điền hết sổ tay** |
| 04 · Hội thoại | 0 | 52.608 | Chưa dịch |
| 05 · Credit | 0 | 242 | Chưa dịch |
| **Tổng** | **2.014** | **55.976** | **+723 mới, 12 câu chỉnh văn phong** |

**Lưu ý:** Số `vi` bao gồm nhãn/tên riêng được duyệt và giữ nguyên tiếng Anh. Các nhóm đã điền đầy đủ trường `vi` không đồng nghĩa đã kiểm thử mọi chữ trong ROM.

## Phong cách mới được người dùng duyệt
- Câu `120.25#page:1`: **`Em mê tụ tập,▼quẩy banh nóc với bạn bè!`** (▼ là dấu xuống dòng trong game).
- Người dẫn chuyện vẫn gọi học sinh là **em**, nhưng các dòng nhận xét tính cách được viết ngắn, hoạt bát, dí dỏm hơn; bỏ tiền tố lặp lại “Hô hô” tại 12 câu này theo mẫu người dùng đưa ra.
- Sổ tay được viết như một cuốn bách khoa đáng yêu, ví dụ **“To xác thế thôi, nhát gan lắm nhé!”**. Chỉ dùng câu đùa ở mô tả phù hợp, không làm lệch tính chất/luật của sinh vật.
- Tên vật phẩm/menu cô đọng, không cố nhồi tiếng lóng.
- Tôn trọng vai: người lớn **ta–em / thầy cô–em**, bạn bè **tớ–cậu** khi xác nhận được quan hệ, hệ thống trung tính.

## Tệp vừa thay đổi
- `translation/00-mo-dau/talkfigs__0eng__data__0999.001.jsonl` — 12 câu đã biên tập.
- `translation/03-so-tay/talkfigs__0eng__data__0999.001..004.jsonl` — 363 mục mới.
- `translation/02-vat-pham/item__ItemName_e.ofs.001..003.jsonl` — 360 tên vật phẩm mới.
- `translation/THUAT_NGU-003.tsv` — danh mục tên sinh vật/vật phẩm EN ↔ VI đã dùng, để tránh bất nhất về sau.
- `mq_translate_003.py`, `mq_items_003.py` — bảng dịch đợt 003 dạng mã nguồn để rà từng câu.
- `DELTA-003.jsonl` — danh sách tất cả 735 bản ghi đã chỉnh (723 mới + 12 sửa).

## QA
- `python qa_checkpoint.py`: **PASS** (mã điều khiển, NFC, giới hạn byte).
- So sánh từng JSONL với checkpoint 002: **735 thay đổi duy nhất ở trường `vi`**, không thay đổi `id`, `en`, `ctx`, các trường độ dài, thứ tự hay tệp nguồn.
- Tất cả dòng sổ tay mới có độ rộng ước lượng tối đa 160px (DejaVu Sans 11px, **không phải font ROM thực**). Giữ 3 dòng tối đa với trang sổ tay.
- **Chưa build ROM hoặc kiểm tra bằng máy NDS** vì chưa có bản ROM USA sạch trong đầu vào; cần kiểm tra font và ngắt dòng thực tế trên máy/emulator trước khi coi là hoàn thiện.

## Cách nối phiên
1. Giải nén `MagiciansQuest-VietHoa-Checkpoint-003.zip`, không ghi đè bằng checkpoint 001 hoặc 002.
2. Đọc `QUY_UOC_DICH_VI.md` và `translation/THUAT_NGU-003.tsv` để giữ ngôi xưng và tên riêng.
3. Dịch tiếp **tên vật phẩm** từ trang `item__ItemName_e.ofs.004.jsonl` (còn 1.111 mục của nhóm vật phẩm, bao gồm các bảng thao tác đã dịch); sau đó chuyển sang **NPC**, bắt đầu các tệp ngữ cảnh rõ ràng. Nếu tên nhân vật chưa rõ vai thì đừng tự gán ngôi xưng.
4. Chạy `qa_checkpoint.py`, so với checkpoint 003 để xác nhận chỉ thay `vi`; cập nhật progress và GitHub sau mỗi đợt.

**Không gồm ROM thương mại.** Mọi lần build phải dùng ROM USA sạch của người dùng (YNNE; SHA-256 ghi trong `BAN_GIAO.md`).