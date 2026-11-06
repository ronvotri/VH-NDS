# Magician’s Quest: Mysterious Times — Checkpoint 016

**Ngày:** 06/11/2026  
**Repository:** `ronvotri/VH-NDS`, thư mục `Magicians-Quest-Mysterious-Times/`  
**Nguồn:** ZIP checkpoint 015 (6.045/55.976 mục)  
**Mốc mới:** **6.285/55.976 mục (11,23%)**, thêm **240 trang thoại NPC**.

## Tiến độ

| Nhóm | Đã điền `vi` | Tổng | Mới |
|---|---:|---:|---:|
| 00 Mở đầu | 106 | 106 | 0 |
| 01 Hệ thống | 1.086 | 1.087 | 0 |
| 02 Vật phẩm | 1.501 | 1.501 | 0 |
| 03 Sổ tay | 432 | 432 | 0 |
| 04 Hội thoại | 3.160 | 52.608 | +240 |
| 05 Credit | 0 | 242 | 0 |
| **Tổng** | **6.285** | **55.976** | **+240** |

## Đợt 016

- `translation/04-thoai/talkfigs__0eng__data__0022.005.jsonl`: **120/120 trang**. Các nhánh hẹn hò, tỏ tình, đề nghị kết bạn thân, lựa chọn thời gian gặp, lời từ chối và tin đồn về NPC. Giữ nguyên tất cả các lựa chọn `$019'...;`, tên người chơi `$500;`, tên NPC `$515;` và màu địa danh **Điểm Hẹn Hò**.
- `translation/04-thoai/talkfigs__0eng__data__0023.001.jsonl`: **120/120 trang**. Một nhân vật nóng tính nhưng hài tự trào: đòi nhờ giặt đồ, ra vẻ học rộng, thích dọa bạn bè, chuyện câu cá, kiểm tra và các màn hiểu nhầm. Giữ nguyên màu tên **cô Strawe**, **Hiệu trưởng Sol**, **Ông Piquard** và **Harrows**, cùng các mã biến `$503'327;` và `$503'309;`.
- Dịch tay theo từng dòng tại `manual_0022_005.tsv` và `manual_0023_001.tsv` (mỗi file 120 dòng có chỉ số 000–119). Chạy `python apply_016.py` để tạo các tệp JSONL và `python qa_016.py` để đối chiếu.
- Phong cách gần gũi, có duyên, hài đúng tính cách; **tớ–cậu** giữa bạn cùng trang lứa, không chèn meme vào đoạn nghiêm túc. Giữ **The Emporium → Bách Hóa Tổng Hợp**, **Lovers’ Point → Điểm Hẹn Hò**.

## QA và bảo toàn dữ liệu

- **PASS:** so với ZIP checkpoint 015, đủ **501 tệp JSONL và 55.976 bản ghi**; **240 hàng thay đổi, chỉ trường `vi`**, hai file kể trên 120 hàng mỗi file.
- **0 lỗi** thay đổi ID, `en`, `ctx`, metadata, thứ tự mã điều khiển, ghi đè bản dịch cũ, NFC, ký tự xuống dòng vật lý, giới hạn 34 ký tự/dòng và giới hạn UTF-8 khi có.
- `DELTA-016.jsonl` giữ 240 thay đổi, văn bản Anh gốc, Việt mới và `ctx`. `QA-016.md` chứa báo cáo chi tiết.
- **Chưa kiểm thử trên ROM NDS, font hoặc chiều rộng pixel thực tế**. Không chứa ROM thương mại; dùng bản USA sạch `YNNE` nếu cần dựng.

## Tiếp checkpoint 017

- Nguồn: `MagiciansQuest-VietHoa-Checkpoint-016.zip` hoặc checkout GitHub mới nhất kết hợp bản đầy đủ.
- Ưu tiên tệp hội thoại `translation/04-thoai/talkfigs__0eng__data__0023.002.jsonl`, sau đó `0023.003.jsonl` (kiểm tra số bản ghi thực tế trước khi dịch).
- Chỉ thay `vi`, không đổi bất kỳ ID/mã lệnh nào; QA với checkpoint 016 rồi mới đưa lên repo và đóng ZIP.