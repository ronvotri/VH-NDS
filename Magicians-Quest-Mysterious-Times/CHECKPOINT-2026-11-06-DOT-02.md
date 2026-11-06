# Magician’s Quest: Mysterious Times — Checkpoint Việt hóa đợt 02

**Ngày:** 2026-11-06  
**Repo:** `ronvotri/VH-NDS/Magicians-Quest-Mysterious-Times`  
**Nguồn:** ZIP bàn giao `MagiciansQuest_BanGiao_Cloud.zip` → checkpoint 001 → checkpoint 002.

## Tiến độ đã đối chiếu

| Nhóm | Đã có `vi` | Tổng | Đợt này |
|---|---:|---:|---:|
| 00-mo-dau | 106 | 106 | 0 (giữ nguyên trang đã test) |
| 01-he-thong | 1.086 | 1.087 | +567 (đã xong mọi chuỗi có nghĩa; 1 chuỗi ký tự Nhật dự phòng để trống) |
| 02-vat-pham | 30 | 1.501 | 0 |
| 03-so-tay | 69 | 432 | +69 (4 bảng menu lớp học; 363 mục còn lại chưa dịch) |
| 04-thoai | 0 | 52.608 | 0 |
| 05-credit | 0 | 242 | 0 |
| **Tổng** | **1.291** | **55.976** | **+636** |

**Lưu ý:** Một số tên riêng/nhãn đã được duyệt và đánh dấu `vi` giống nguyên văn `en`, nên số trường có `vi` không bằng số chuỗi thay chữ tiếng Anh.

### Phạm vi đợt 02
- Toàn bộ 5 trang tiếp của thông báo hệ thống `talkfigs/0eng/data/0999`, gồm kết nối Wi-Fi, mã bạn bè, lưu/tải, chuyển trường, trang phục, túi đồ, học bài/niệm chú, phép trên trượng, lưu tiến trình và thông báo tương tác.
- 4 bảng menu bài học của trường: `selmsg0..3_e.dat` (69 chuỗi).
- Đồng nhất thần chú, tên trường, tên địa điểm và quy tắc ngôi xưng theo `QUY_UOC_DICH_VI.md` và `translation/GLOSSARY.tsv`.

### QA đã kiểm tra
- Chạy `python qa_checkpoint.py`: PASS; **không sai mã lệnh, giới hạn byte, NFC hoặc ngắt trang**.
- So sánh **mọi JSONL với checkpoint 001**: tất cả trường ngoài `vi` (`id`, `en`, `ctx`, giới hạn, thứ tự, khóa) giữ nguyên; chỉ 636 `vi` mới được điền trong 9 tệp.
- Thử phục dựng 9 tệp từ ZIP checkpoint 001 + `DOT-02-DELTA.bz2.b64` bằng `apply_delta_02.py`: tất cả mục đối chiếu trùng bản vừa dịch.
- Đo xấp xỉ độ rộng bằng DejaVu Sans 11px, ngưỡng 155px. Chỉ còn một dòng có khoảng trắng đệm hệ thống gốc; không tự xóa đệm trước khi xác minh trên máy NDS.

### Vẫn cần kiểm thử thực tế
- **Chưa build ROM/IPS** do chưa có ROM sạch USA. Đích ROM YNNE, SHA-256: `5c1d3e9cb8a5351f9c949bc758d9aed94479abc17eb41b6d93cbe8d4e15cca36`.
- QA font NDS và dàn trang thực tế cần thử trên ROM, không thể khẳng định hoàn hảo chỉ từ ước lượng.
- Những bản nhạc mang tên riêng được dịch theo nghĩa tiếng Anh hoặc giữ tên riêng gốc; có thể rà lại khi thấy trong game.

### Khôi phục và nối phiên
1. Giải nén `MagiciansQuest-VietHoa-Checkpoint-002.zip` để làm tiếp trực tiếp.
2. Nếu chỉ có checkpoint 001, giải nén checkpoint 001 rồi chép `DOT-02-DELTA.bz2.b64` cùng `apply_delta_02.py` vào thư mục bất kỳ, chạy `python apply_delta_02.py <thu-muc-checkpoint-001>`; script đối chiếu SHA256 file cũ trước khi áp dụng, tránh vá nhầm.
3. Lần tiếp theo xử lý 363 chuỗi sổ tay còn lại (`03-so-tay/talkfigs...`) rồi 1.471 tên vật phẩm còn lại (`02-vat-pham/item...`); tiếp đó mở khóa NPC dựa `ctx` trước khi dịch thoại số lượng lớn.
4. Mỗi đợt thay mới checkpoint và cập nhật GitHub cùng thư mục; không ghi đè sai bản dịch đã test.