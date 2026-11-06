# Magician’s Quest: Mysterious Times — Checkpoint 017

**Ngày:** 06/11/2026  
**Repository:** `ronvotri/VH-NDS`, thư mục `Magicians-Quest-Mysterious-Times/`  
**Nguồn:** ZIP checkpoint 016 (6.285/55.976 mục)  
**Mốc mới:** **6.525/55.976 mục (11,66%)**, thêm **240 trang thoại NPC**.

## Tiến độ

| Nhóm | Đã điền `vi` | Tổng | Mới |
|---|---:|---:|---:|
| 00 Mở đầu | 106 | 106 | 0 |
| 01 Hệ thống | 1.086 | 1.087 | 0 |
| 02 Vật phẩm | 1.501 | 1.501 | 0 |
| 03 Sổ tay | 432 | 432 | 0 |
| 04 Hội thoại | 3.400 | 52.608 | +240 |
| 05 Credit | 0 | 242 | 0 |
| **Tổng** | **6.525** | **55.976** | **+240** |

## Đợt 017 — thoại NPC nóng tính nhưng hài tự trào

- `translation/04-thoai/talkfigs__0eng__data__0023.002.jsonl`: **120/120 trang**. Chuyện thi cử, thầy cô, bài tập, nắm đấm, mối quan hệ và các mùa trong năm; một NPC mạnh miệng nhưng hay tự làm mình quê.
- `translation/04-thoai/talkfigs__0eng__data__0023.003.jsonl`: **120/120 trang**. Tiếp mạch ngắm sao, dã ngoại, sách vở, búp bê, ngôi sao điện ảnh, võ thuật, cảnh sát, chính trị và tình bạn. Giữ đoạn nối liền giữa các trang.
- Dịch từng trang tại `manual_0023_002.tsv`, `manual_0023_003.tsv`, bản thuần văn bản tại `vi_0023_002.txt`, `vi_0023_003.txt`.
- Chạy `python apply_017.py` từ bản đầy đủ checkpoint 016 để điền `vi`, sau đó `python qa_017.py` so nguyên gói với bản gốc 016.
- Dùng ngôi xưng **tớ–cậu**, giữ sự tự trào của nhân vật, không biến lời nghiêm túc về mẹ hoặc thất tình thành trò đùa. Giữ tên riêng và đúng các đoạn có biến tên người chơi/NPC.

## QA và bảo toàn

- **PASS** đối chiếu với ZIP checkpoint 016: **501 tệp JSONL, 55.976 bản ghi**.
- Chính xác **240 thay đổi** ở hai tệp kể trên, **chỉ sửa trường `vi`**; không thay ID, tiếng Anh gốc, metadata, mã biểu cảm, thứ tự các mã điều khiển, dấu Unicode NFC.
- Mọi dòng hiển thị mới tối đa 33 ký tự sau khi loại mã, tối đa 2 dấu `▼` mỗi trang. Không có trường nào vượt `max_utf8_bytes` nếu đã khai báo.
- Có file `DELTA-017.jsonl` đủ 240 dòng đối chiếu trước/sau và `QA-017.md`.
- **Chưa kiểm thử trên ROM NDS hoặc đo font thực tế**. Ngưỡng ký tự chỉ là kiểm tra sơ bộ.

## Tiếp checkpoint 018

- Nguồn: `MagiciansQuest-VietHoa-Checkpoint-017.zip` (đầy đủ) kết hợp kho GitHub `ronvotri/VH-NDS` để cập nhật nhánh chính.
- Ưu tiên `translation/04-thoai/talkfigs__0eng__data__0023.004.jsonl`, rồi `0023.005.jsonl`. Kiểm tra số hàng trước khi dịch, đối chiếu ngữ cảnh và giữ mọi mã `$503`, `$500`, `$000`, `$024`, `$023`, `$022`.
- Ghi log mốc 018, tạo ZIP đầy đủ, QA so 017, cập nhật repo. Không dựng ROM thương mại nếu chưa có bản ROM sạch USA YNNE do người dùng cung cấp.