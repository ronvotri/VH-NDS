# Magician’s Quest: Mysterious Times — Checkpoint 014

**Ngày:** 06/11/2026  
**Repo:** `ronvotri/VH-NDS` → `Magicians-Quest-Mysterious-Times/`  
**Nguồn:** ZIP checkpoint 013, mốc 5.565/55.976  
**Mốc mới:** **5.805/55.976 mục (~10,37%)**, +240 trang thoại NPC mới.

## Phân bố

| Nhóm | Đã điền `vi` | Tổng | Mới |
|---|---:|---:|---:|
| 00 Mở đầu | 106 | 106 | 0 |
| 01 Hệ thống | 1.086 | 1.087 | 0 |
| 02 Vật phẩm | 1.501 | 1.501 | 0 |
| 03 Sổ tay | 432 | 432 | 0 |
| 04 Hội thoại | 2.680 | 52.608 | +240 |
| 05 Credit | 0 | 242 | 0 |
| **Tổng** | **5.805** | **55.976** | **+240** |

## Dịch đợt 014

1. `translation/04-thoai/talkfigs__0eng__data__0022.001.jsonl`: **120/120 trang**. Tình huống đời thường của NPC kiêu kỳ nhưng hay tự làm mình quê: cha mẹ gửi thư, mượn vở, săn côn trùng, câu lên rác mình đã vứt, vô nhầm nhà vệ sinh, bí quyết nộp bài, phép lịch sự, tranh giành miếng pizza cuối cùng. Có hai lựa chọn `$019'29;` và `$019'30;` giữ đúng vị trí.
2. `translation/04-thoai/talkfigs__0eng__data__0022.002.jsonl`: **120/120 trang**. Chủ đề học tập, ước mơ làm pháp sư, trốn bài kiểm tra, yêu đương tuổi học trò, những màn tự tin thái quá và câu chuyện gia đình. Cố ý giữ ý nghĩa nguyên tác trong những câu nói phản ánh tính cách không dễ mến của NPC, không cổ vũ hành động đó.
3. `manual_0022_001.txt` và `manual_0022_002.txt` là **bản dịch tay theo thứ tự từng trang**. Script `apply_014.py` chèn y nguyên các mã biểu cảm đầu câu từ EN, và giữ mã tên riêng, màu chữ, lựa chọn ngay trong nội dung. Chỉ sửa `vi`.

## An toàn dữ liệu và QA

- `qa_014.py` so sánh từng bản ghi với ZIP checkpoint 013. Kiểm tra ID, EN, ctx, metadata, mã điều khiển theo thứ tự, NFC, giới hạn UTF-8 nếu có, độ dài từng dòng (34 ký tự hiển thị) và tránh ghi đè bản dịch cũ.
- Kết quả: **501 JSONL, 55.976 mục, 240 thay đổi chỉ ở `vi`, 0 lỗi cấu trúc**, có bản chênh lệch ở `DELTA-014.jsonl` và báo cáo `QA-014.md`.
- Tên giữ nguyên: **Reginald**, **Vivian**; tên cửa hàng **Tiệm Thời Trang Vivian**, tên trưởng thành từ nguồn; thẻ `$000'...;` bao quanh danh xưng được giữ đúng như nguồn.
- Chưa kiểm thử ROM và độ rộng pixel thực. Cần bản NDS sạch USA `YNNE` để build/QA in-game, không có trong checkpoint này.

## Nối phiên 015

- ZIP nguồn tiếp theo: `MagiciansQuest-VietHoa-Checkpoint-014.zip` (chứa toàn bộ file dịch và lịch sử đợt 001–014).
- Cụm có thật, còn trống: `translation/04-thoai/talkfigs__0eng__data__0022.003.jsonl` và `.004` (mỗi tệp 120 trang). Đọc mạch thoại theo `ctx` trước khi dịch; giữ giọng nhân vật hơi kiêu, dí dỏm.
- Chỉ sửa `vi`, không thay đổi `en` / `ctx` / `id` / mã `$...;`; sau mỗi batch cập nhật repo và xuất checkpoint mới để nối phiên.