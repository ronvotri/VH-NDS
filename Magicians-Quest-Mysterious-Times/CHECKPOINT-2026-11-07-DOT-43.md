# Magician’s Quest: Mysterious Times — Checkpoint 043

**Ngày:** 07/11/2026  
**Repository:** `ronvotri/VH-NDS` → `Magicians-Quest-Mysterious-Times/`  
**Checkpoint nguồn:** `MagiciansQuest-VietHoa-Checkpoint-042.zip`  
**Kết quả:** **12.469/55.976 mục (22,28%)**, tăng **240 trang thoại NPC**.

## Tiến độ

| Nhóm | Đã dịch | Tổng | Tăng |
|---|---:|---:|---:|
| 00 — Mở đầu | 106 | 106 | 0 |
| 01 — Hệ thống | 1.086 | 1.087 | 0 |
| 02 — Vật phẩm | 1.501 | 1.501 | 0 |
| 03 — Sổ tay | 432 | 432 | 0 |
| 04 — Hội thoại NPC | 9.344 | 52.608 | +240 |
| 05 — Credit | 0 | 242 | 0 |
| **Tổng** | **12.469** | **55.976** | **+240** |

## Phạm vi dịch

- `translation/04-thoai/talkfigs__0eng__data__0033.004.jsonl` — **120 trang**: rồng bình phục và tạm biệt; người sao Hỏa nói ngược chữ tìm hoa có thể sống trên sao Hỏa; kẻ thích vứt rác, thế giới gương, kẻ song trùng, điều tra vật phép.
- `translation/04-thoai/talkfigs__0eng__data__0033.005.jsonl` — **120 trang**: thu thập năm vật phép, chế bùa phản phép, bắt và đưa kẻ song trùng về gương; giải lời nguyền người sói; trao đổi linh hồn bằng giai điệu.
- Tên phép, màu, lựa chọn, vật phẩm (kể cả `$507'114;` và bộ đếm `$550'1012;`) giữ nguyên dạng token. Dùng **kẻ song trùng** nhất quán trong hai tệp; **người sói**, **thị trấn**, **thần chú**, **ma lực** đúng ngữ cảnh.
- **Đặc biệt:** lời người sao Hỏa trong tiếng Anh cố ý viết đảo ngược. Bản Việt cũng đảo ngược chữ có dấu theo cụm ký tự để giữ thủ pháp này; mã `$...;` và các lựa chọn Có/Không không đảo.

## Tệp bàn giao

- `DELTA-043.jsonl`: đúng 240 cập nhật trường `vi`.
- `manual_0033_004.tsv`, `manual_0033_005.tsv`: bảng đối chiếu EN–VI theo ID.
- `vi_0033_004_raw.txt`, `vi_0033_005_raw.txt`: bản dịch trước xử lý; `vi_0033_004.txt`, `vi_0033_005.txt`: bản Việt cuối theo từng trang.
- `apply_043.py`: áp delta có thể chạy lại an toàn; `qa_043.py`, `QA-043.md`: so sánh toàn bộ checkpoint.

## QA

**PASS:** 501 JSONL / 55.976 mục. **12.229 mục dịch cũ giữ nguyên**, chỉ có 240 trường `vi` ở hai tệp thay đổi; tất cả mã điều khiển giữ đúng tham số và thứ tự. Đạt NFC, giới hạn 34 ký tự hiển thị/dòng, tối đa 3 dấu `▼` và giới hạn UTF-8 khi có.

**Chưa thử hiển thị/điều khiển trực tiếp trong ROM Nintendo DS.** ZIP chỉ chứa bản dịch, mã và công cụ, không chứa ROM thương mại.

## Đợt 044 tiếp theo

Dịch `0033.006` (120 trang) và `0033.007` (120 trang), tổng **240 trang**. Hai tệp nguồn tiếng Anh đã có sẵn trong ZIP checkpoint 043 và được chuẩn bị để đưa lên GitHub.