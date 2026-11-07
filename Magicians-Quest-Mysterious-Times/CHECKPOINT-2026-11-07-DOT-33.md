# Magician’s Quest: Mysterious Times — Checkpoint 033

**Ngày:** 07/11/2026  
**Repo:** `ronvotri/VH-NDS`, thư mục `Magicians-Quest-Mysterious-Times/`  
**Baseline:** `MagiciansQuest-VietHoa-Checkpoint-032.zip` (9.900 mục đã dịch)  
**Mốc mới:** **10.088/55.976 mục (18,02%)**, thêm **188 trang hội thoại NPC**.

## Tiến độ

| Nhóm | Đã dịch | Tổng | Mới |
| --- | ---: | ---: | ---: |
| 00 — Mở đầu | 106 | 106 | 0 |
| 01 — Hệ thống | 1.086 | 1.087 | 0 |
| 02 — Vật phẩm | 1.501 | 1.501 | 0 |
| 03 — Sổ tay | 432 | 432 | 0 |
| 04 — Hội thoại | 6.963 | 52.608 | +188 |
| 05 — Credit | 0 | 242 | 0 |
| **Tổng** | **10.088** | **55.976** | **+188** |

## Nội dung đợt 033

- `translation/04-thoai/talkfigs__0eng__data__0029.004.jsonl`: **120 trang**. Nối tiếp nhân vật nữ hay tự trào: chuyện ăn bánh, hội bạn đi vệ sinh, rủ ra ngoài, học nhóm, nghỉ chơi và hẹn hò. Nhiều nhánh lời mời, từ chối và tỏ tình cần giữ nguyên mã lựa chọn.
- `translation/04-thoai/talkfigs__0eng__data__0029.005.jsonl`: **68 trang**. Lựa chọn giờ hẹn 10:00–20:00, những lời nhắc về lời hứa, cùng chuỗi lời kể về bạn bè: trò chuyện, học giỏi, đùa nghịch, câu cá, bắt côn trùng, cưỡi chổi, mua sắm, học bài, uống trà.
- Phần thoại trực tiếp duy trì ngôi **tớ–cậu**, hài hước gần gũi, không thay nghĩa những lời tình cảm. Giữ nguyên biến tên `$500;` và `$515;`, mã biểu cảm, mã màu Điểm Hẹn Hò `$000'5;...$000'1;` và mọi mã `$019'...;` điều hướng nhánh.
- Bản dịch tay: `vi_0029_004_raw.txt`, `vi_0029_005_raw.txt`; thành phẩm: `vi_0029_004.txt`, `vi_0029_005.txt`; đối chiếu EN/VI: `manual_0029_004.tsv`, `manual_0029_005.tsv`.
- `DELTA-033.jsonl`: đầy đủ 188 thay đổi theo ID; `wrap_033.py`: áp bản dịch thủ công và bảo toàn token; `qa_033.py` kiểm tra cấu trúc với ZIP 032; kết quả trong `QA-033.md`.

## QA và giới hạn

- **PASS 501 JSONL / 55.976 bản ghi**; chỉ thêm 188 trường `vi`, không ghi đè bất kỳ mục nào trong 9.900 bản dịch cũ.
- Bảo toàn ID, câu tiếng Anh, `ctx`, mọi trường khác và thứ tự bản ghi. Kiểm mã điều khiển theo danh sách/thứ tự, Unicode NFC, số ngắt dòng, độ dài từng dòng và giới hạn byte nếu có.
- **Chưa kiểm thử trực tiếp trong ROM NDS, chưa kiểm chứng độ rộng pixel thực tế.** Font và độ dài tên được thay từ `$500;`/`$515;` cần kiểm tra bằng game.
- ZIP checkpoint gồm dữ liệu và công cụ bàn giao, không gồm ROM thương mại.

## Tiếp theo — Đợt 034

- `0030.001`: 120 trang; `0030.002`: 120 trang. Dịch đúng mạch nhân vật mới, tiếp tục QA và lưu GitHub cùng ZIP checkpoint.