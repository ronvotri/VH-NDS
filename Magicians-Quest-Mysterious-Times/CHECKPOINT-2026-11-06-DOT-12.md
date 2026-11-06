# Magician’s Quest: Mysterious Times — Checkpoint 012

**Ngày:** 06/11/2026  
**Repo:** `ronvotri/VH-NDS` → `Magicians-Quest-Mysterious-Times/`  
**Nguồn:** `MagiciansQuest-VietHoa-Checkpoint-011.zip`, mốc 5.137/55.976  
**Mốc mới:** **5.377/55.976 (9,61%)**, thêm 240 trang thoại mới và 6 chỉnh thuật ngữ có chủ đích.

## Tiến độ tổng

| Phần | Đã điền `vi` | Tổng | Mới đợt 012 |
|---|---:|---:|---:|
| 00 · Mở đầu | 106 | 106 | 0 |
| 01 · Hệ thống | 1.086 | 1.087 | 0 (1 chỉnh tên hiển thị) |
| 02 · Vật phẩm | 1.501 | 1.501 | 0 |
| 03 · Sổ tay | 432 | 432 | 0 |
| 04 · Hội thoại | 2.252 | 52.608 | +240 (5 chỉnh tên đã dịch) |
| 05 · Credit | 0 | 242 | 0 |
| **Tổng** | **5.377** | **55.976** | **+240** |

*`vi` có nội dung nghĩa là đã xử lý, bao gồm một số tên riêng giữ nguyên; chưa có nghĩa đã xác nhận toàn bộ câu trong game/ROM.*

## Nội dung mới

- `translation/04-thoai/talkfigs__0eng__data__0021.002.jsonl`: **120/120** trang bối cảnh 31–59. Cốt chuyện bài tập, thầy giáo, tiệm hoa, cửa hàng đồ chơi, tình cảm bạn học, Giáng Sinh, trượt băng và các mùa.
- `translation/04-thoai/talkfigs__0eng__data__0021.003.jsonl`: **120/120** trang bối cảnh 59–87. Sưu tầm côn trùng, đồ cổ, kính râm, phi tiêu, thể thao, nghề nghiệp và một số trò nghịch ở trường.
- Văn phong: hoạt bát, tớ–cậu với bạn bè; chỗ nghiêm túc giữ nguyên tình cảm nhân vật. Không gán giới tính mới so với nội dung nguồn. Đặc biệt giữ nguyên mã biến tên `$500;` và `$503'...;`.

## Chuẩn hóa tên cửa hàng

**The Emporium → Bách Hóa Tổng Hợp**, đồng nhất thuật ngữ đã dùng trong hệ thống `0999.006`. Sửa **6** mục đã dịch từ các đợt trước: một nhãn menu, bốn trang cửa hàng `0012.001` và một trang NPC `0021.001`. Các chỉnh sửa cũ→mới lưu tại `TERM-CORRECTIONS-012.jsonl` và giải thích trong `THUAT-NGU-012.md`. Chỉ thay `vi`, giữ nguyên mọi thẻ màu `$000'...;`.

## Dữ liệu và kiểm tra

- `manual_0021_002.txt`, `manual_0021_003.txt`: mỗi dòng một trang theo thứ tự JSONL, giữ `▼` đúng nhịp.
- `apply_012.py`: áp 240 bản dịch mới lên checkpoint 011 đã giải nén.
- `normalize_terms_012.py`: cập nhật đúng 6 thuật ngữ cũ có kiểm tra mã/độ dài.
- `qa_012.py`: đối chiếu toàn bộ checkpoint 011; tạo `DELTA-012.jsonl` (246 mục) và `QA-012.md`.
- QA: **501 tệp**, **55.976 hàng**, **0 lỗi**; giữ đúng ID/EN/ctx/metadata, mã `$...;`, giới hạn byte nếu có, Unicode NFC, tối đa 34 ký tự nhìn thấy trên từng dòng và tối đa ba dấu `▼`.

**Giới hạn:** chưa có ROM Mỹ sạch YNNE để dựng vá và thử font. Phải kiểm tra độ rộng pixel thực sự (~160 px), ký tự có dấu, nhịp trang, danh xưng và độ dài bảng tên Bách Hóa Tổng Hợp trong giả lập/máy NDS.

## Nối phiên

- ZIP giao cho phiên sau: `MagiciansQuest-VietHoa-Checkpoint-012.zip`, có đủ dữ liệu dịch các đợt 001–012 và toàn bộ công cụ.
- Tệp tiếp theo: `translation/04-thoai/talkfigs__0eng__data__0021.004.jsonl` (**120 trang trống**); sau đó `0021.005` (**68 trang trống**).
- Cấm sửa trường khác `vi`; không viết đè bản dịch đã duyệt trừ khi ghi điều chỉnh có chủ đích với ID cụ thể và QA.
- Mỗi đợt tiếp phải cập nhật trực tiếp thư mục game trong repo `VH-NDS`, ghi commit và xác minh tệp thật trên GitHub.