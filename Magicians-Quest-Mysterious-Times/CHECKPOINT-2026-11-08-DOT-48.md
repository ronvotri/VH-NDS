# Magician’s Quest: Mysterious Times — Checkpoint 048

**Ngày:** 08/11/2026  
**Repo:** `ronvotri/VH-NDS` → `Magicians-Quest-Mysterious-Times/`  
**Nguồn:** `MagiciansQuest-VietHoa-Checkpoint-047.zip`  
**Tiến độ:** **13.669 / 55.976 (24,42%)**, +240 trang NPC.

## Thống kê

| Nhóm | Đã dịch | Tổng | Tăng |
|---|---:|---:|---:|
| 00 — Mở đầu | 106 | 106 | 0 |
| 01 — Hệ thống | 1.086 | 1.087 | 0 |
| 02 — Vật phẩm | 1.501 | 1.501 | 0 |
| 03 — Sổ tay | 432 | 432 | 0 |
| 04 — Hội thoại NPC | 10.544 | 52.608 | +240 |
| 05 — Credit | 0 | 242 | 0 |
| **Tổng** | **13.669** | **55.976** | **+240** |

## Nội dung mới

- `0033.014` (120 trang): **Cấm Thư** nhờ tìm lại các trang hóa thành trái cây, xương, đá; nhận quà Halloween, cho kẹo hay bị ghẹo; phần đầu vụ mở cánh cổng thế giới khác.
- `0033.015` (120 trang): **cánh cổng thời gian** và cuộc gặp giữa Hiệu trưởng Sol với người hiệu trưởng thời trước; **Ác Mộng** bày trò trong giấc ngủ; **lợn vòi** bị đau bụng do ăn giấc mơ thường thay vì ác mộng.
- Giữ phong cách **ta–em** cho Cấm Thư/hiệu trưởng, **ta–nhóc** cho Reginald, **ta–ngươi** cho Ác Mộng, **tôi–cậu** cho lợn vòi; dùng thuật ngữ đã có: Cấm Thư, Hiệu trưởng Sol, trường phép thuật, thị trấn.
- Giữ các mã động `$500;`, `$507'...;`, `$550'...;`, mã màu và biểu cảm, mã phân nhánh `Trick`/`Treat`.

## Bàn giao

- `translation/04-thoai/talkfigs__0eng__data__0033.014.jsonl`, `0033.015.jsonl`: 240 trang đã Việt hóa.
- `vi_0033_014_raw.txt`, `vi_0033_015_raw.txt`: bản dịch tay; `vi_0033_014.txt`, `vi_0033_015.txt`: thành phẩm có mã/ngắt dòng.
- `manual_0033_014.tsv`, `manual_0033_015.tsv`: đối chiếu ID/EN/VI/ctx, 120 trang + tiêu đề mỗi bảng.
- `apply_048.py`, `qa_048.py`, `DELTA-048.jsonl`, `QA-048.md`: tái tạo, kiểm tra và bảng thay đổi.

**QA PASS:** 501 tệp JSONL / 55.976 bản ghi, bảo toàn 13.429 bản dịch cũ; chỉ điền 240 trường `vi` mới. ZIP đủ dữ liệu không chứa ROM thương mại. Chưa test ROM NDS hay đo pixel font thật.

## Đợt 049 tiếp theo

`0033.016` (120) và `0033.017` (120), tổng **240 trang**. Tệp gốc có trong ZIP checkpoint và sẽ được đưa lên GitHub trước để phiên sau tự tiếp tục.