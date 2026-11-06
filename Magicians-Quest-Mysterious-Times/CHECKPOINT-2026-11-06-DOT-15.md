# Magician’s Quest: Mysterious Times — Checkpoint 015

**Ngày:** 06/11/2026  
**Repository:** `ronvotri/VH-NDS`, thư mục `Magicians-Quest-Mysterious-Times/`  
**Nguồn:** ZIP checkpoint 014 (5.805/55.976)  
**Mốc mới:** **6.045/55.976 mục (10,80%)**, +240 trang thoại NPC mới.

## Phân bố

| Nhóm | Đã điền `vi` | Tổng | Mới |
|---|---:|---:|---:|
| 00 Mở đầu | 106 | 106 | 0 |
| 01 Hệ thống | 1.086 | 1.087 | 0 |
| 02 Vật phẩm | 1.501 | 1.501 | 0 |
| 03 Sổ tay | 432 | 432 | 0 |
| 04 Hội thoại | 2.920 | 52.608 | +240 |
| 05 Credit | 0 | 242 | 0 |
| **Tổng** | **6.045** | **55.976** | **+240** |

## Lô dịch 015

- `translation/04-thoai/talkfigs__0eng__data__0022.003.jsonl`: **120/120 trang**, chuyện đi suối nước nóng, săn ốc sên, giả ngủ trong lớp, bắt chuồn chuồn, làm bánh, sửa đồ điện thành đồ dùng ngược đời, sưu tập đá và mơ làm sao rock.
- `translation/04-thoai/talkfigs__0eng__data__0022.004.jsonl`: **120/120 trang**, NPC tự cho mình là quý tộc/thiên tài, ước làm người nổi tiếng, kế hoạch ăn gian marathon, chuyện bạn bè mượn tẩy, bánh quy mẹ gửi và các câu thoại lựa chọn đi chơi/uống trà/học nhóm.
- Bản dịch tay theo trang nằm ở `manual_0022_003.txt` và `manual_0022_004.txt`. `apply_015.py` ghép các mã biểu cảm đầu trang và bảo toàn toàn bộ biến tên `$500;`, `$503'307;`, `$503'309;`, lựa chọn `$019'...;`.
- Phong cách: dí dỏm kiểu Gen Z nhưng không lạm dụng meme. NPC hơi tự phụ, hay tự làm bản thân mất mặt; giữa bạn bè dùng **tớ–cậu**. Tên cửa hàng **The Emporium = Bách Hóa Tổng Hợp** như checkpoint 012.

## QA và tính toàn vẹn

- `qa_015.py` đối chiếu từng hàng của **501 tệp JSONL**, **55.976 bản ghi** với ZIP checkpoint 014.
- Kết quả **PASS: 240 thay đổi, chỉ trường `vi`; 0 lỗi** ghi đè bản dịch cũ, ID, EN, ctx, metadata, thứ tự mã điều khiển, Unicode NFC, TAB/CR/LF, hơn 3 dấu ngắt `▼`, giới hạn 34 ký tự hiển thị mỗi dòng hoặc giới hạn byte nếu có.
- Toàn bộ 240 bản ghi đổi được lưu trong `DELTA-015.jsonl` và tóm tắt `QA-015.md`.
- **Chưa kiểm thử ROM hoặc độ rộng pixel thực**. Checkpoint không chứa ROM thương mại. Cần ROM sạch USA `YNNE` nếu muốn dựng và test in-game.

## Bắt đầu checkpoint 016

- Nguồn: `MagiciansQuest-VietHoa-Checkpoint-015.zip`, hoặc lấy 2 tệp delta/JSONL mới nhất từ GitHub và phần data từ ZIP checkpoint.
- Mục kế tiếp có thật: `translation/04-thoai/talkfigs__0eng__data__0022.005.jsonl` (120 trang; còn null), sau đó `0023.001` (120 trang). Đọc ngữ cảnh trước khi dịch.
- Luôn chỉ sửa `vi`; bảo toàn chính xác control code, tên riêng và lựa chọn; QA checkpoint trước khi push.