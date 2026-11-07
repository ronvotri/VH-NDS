# Magician’s Quest: Mysterious Times — Checkpoint 044

**Ngày:** 07/11/2026  
**Repository:** `ronvotri/VH-NDS` → `Magicians-Quest-Mysterious-Times/`  
**Checkpoint nguồn:** `MagiciansQuest-VietHoa-Checkpoint-043.zip`  
**Kết quả:** **12.709/55.976 mục (22,70%)**, +240 trang thoại NPC.

## Tiến độ

| Nhóm | Đã dịch | Tổng | Tăng |
|---|---:|---:|---:|
| 00 — Mở đầu | 106 | 106 | 0 |
| 01 — Hệ thống | 1.086 | 1.087 | 0 |
| 02 — Vật phẩm | 1.501 | 1.501 | 0 |
| 03 — Sổ tay | 432 | 432 | 0 |
| 04 — Hội thoại NPC | 9.584 | 52.608 | +240 |
| 05 — Credit | 0 | 242 | 0 |
| **Tổng** | **12.709** | **55.976** | **+240** |

## Phạm vi dịch

- `translation/04-thoai/talkfigs__0eng__data__0033.006.jsonl`: **120 trang**, đoạn ngắn Thần Chết, tượng quỷ đá gác sảnh trường ngủ gật, nhờ người chơi tìm món có vị kích thích để giữ tỉnh táo. Nhiều phản ứng hài với vị cay, đắng và món quá khó nuốt, thử cùng lúc **năm loại món khác nhau**, kết thúc bằng lời hứa giữ kín việc tượng biết nói.
- `translation/04-thoai/talkfigs__0eng__data__0033.007.jsonl`: **120 trang**, đoạn tê đầu lưỡi sau khi ăn, Krampus xét người chơi ngoan/hư qua bạn bè, học hành và phụ giúp việc nhà; quà phần thưởng và điều kiện hành trang đầy; Minotaur mở trại luyện thể lực, có lựa chọn Có/Không.
- Giữ rõ giọng điệu: tượng quỷ đá nhã nhặn tự ti; Krampus nghiêm nhưng có nét buồn cười, xưng **ta–nhóc**; Minotaur hô hào rèn luyện. Các câu nói ngọng khi lưỡi tê được cố ý Việt hóa theo âm nói lắp để giữ đặc trưng nguyên tác.
- Giữ nguyên mã ngắt trang `▼`, tên động như `$500;`, mã màu, mã biểu cảm `$024/$023/$022` và mã lựa chọn `$019`.

## Tệp bàn giao

- `DELTA-044.jsonl`: đúng **240** cập nhật `vi` theo ID, kèm `en` để đối chiếu.
- `manual_0033_006.tsv`, `manual_0033_007.tsv`: bảng EN–VI theo ID và `ctx`.
- `vi_0033_006_raw.txt`, `vi_0033_007_raw.txt`: bản nháp thuần chữ; `vi_0033_006.txt`, `vi_0033_007.txt`: bản đã giữ mã và ngắt dòng.
- `apply_044.py`: áp delta an toàn, từ chối ghi đè bản dịch khác; `qa_044.py`, `QA-044.md`: QA cả checkpoint.

## QA

**PASS:** đối chiếu 501 tệp JSONL / 55.976 bản ghi; 12.469 mục dịch cũ không thay đổi, 240 mục mới; chỉ sửa trường `vi` ở hai tệp mục tiêu. Mã game khớp theo đúng thứ tự và tham số; NFC, dấu `▼` và độ dài dòng đạt giới hạn. **Chưa thử trực tiếp trong ROM NDS.** ZIP không chứa ROM thương mại.

## Đợt 045 tiếp theo

Dịch `0033.008` và `0033.009`, mỗi tệp **120 trang** (tổng **240**). Nguồn EN có trong ZIP 044 và nên đưa sẵn lên GitHub để tiếp tục liền mạch.