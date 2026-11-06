# Magician’s Quest: Mysterious Times — Checkpoint 013

**Ngày:** 06/11/2026  
**Repo:** `ronvotri/VH-NDS` → `Magicians-Quest-Mysterious-Times/`  
**Nguồn:** ZIP checkpoint 012, mốc 5.377/55.976  
**Mốc mới:** **5.565/55.976 mục (~9,94%)**, +188 trang thoại NPC mới.

## Phân bố

| Nhóm | Đã điền `vi` | Tổng | Mới |
|---|---:|---:|---:|
| 00 Mở đầu | 106 | 106 | 0 |
| 01 Hệ thống | 1.086 | 1.087 | 0 |
| 02 Vật phẩm | 1.501 | 1.501 | 0 |
| 03 Sổ tay | 432 | 432 | 0 |
| 04 Hội thoại | 2.440 | 52.608 | +188 |
| 05 Credit | 0 | 242 | 0 |
| **Tổng** | **5.565** | **55.976** | **+188** |

## Dịch đợt 013

1. `translation/04-thoai/talkfigs__0eng__data__0021.004.jsonl`: 120/120 trang về tình bạn, lời mời đi chơi/học nhóm, hẹn hò và thổ lộ tình cảm; giữ `Điểm Hẹn Hò` cho `Lovers Point`.
2. `translation/04-thoai/talkfigs__0eng__data__0021.005.jsonl`: 68/68 trang về xác nhận giờ hẹn, NPC quá bận, tin đồn bạn bè và kỷ niệm bắt cá/bắt côn trùng/đi chổi/uống trà.

Cả hai tệp đều dịch theo bản gõ tay tại `manual_0021_004.txt` và `manual_0021_005.txt`, dùng lối nói tự nhiên/Gen Z đúng vai; mặc định tớ–cậu với bạn đồng lứa. Riêng lời tỏ tình giữ cảm xúc mộc mạc, không chen meme. Tránh gán giới tính khi trò chơi dùng biến tên tùy người chơi.

## An toàn dữ liệu

- Script `apply_013.py`: gắn lại chính xác mã biểu cảm đầu câu `$024;`, `$023;`, `$022;`, `$034;` và giữ nguyên các mã định dạng/biến còn lại. Chỉ sửa `vi`.
- Script `qa_013.py`: so từng hàng với ZIP checkpoint 012, ngăn ghi đè dịch cũ, đối chiếu mã token theo đúng thứ tự; kiểm tra NFC/giới hạn byte/độ dài/ngắt trang, tạo `DELTA-013.jsonl` và `QA-013.md`.
- Kết quả: **501 tệp JSONL, 55.976 hàng, 188 mục mới, 0 lỗi kiểm tra cấu trúc**. Giữ nguyên 5.377 mục đã xử lý trước đó.
- Không có ROM NDS thương mại trong ZIP. Chưa kiểm thử dựng ROM YNNE, độ rộng pixel/độ phủ ký tự có dấu và hiển thị trong game.

## Nối phiên 014

- ZIP mới: `MagiciansQuest-VietHoa-Checkpoint-013.zip` chứa đầy đủ dữ liệu/checkpoint 001–013.
- Tệp kế tiếp có thật: `translation/04-thoai/talkfigs__0eng__data__0022.001.jsonl`, rồi `.002` tiếp theo. Kiểm tra `ctx`, tên nhân vật và mã trước khi dịch.
- Tiếp tục chỉ sửa `vi`, không đổi `id` / `en` / `ctx` / thứ tự và không ghi đè bản dịch cũ nếu chưa ghi rõ lý do.
- Mỗi đợt sau phải cập nhật GitHub `ronvotri/VH-NDS` và lưu checkpoint/QA để nối phiên.