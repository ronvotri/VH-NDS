# Magician’s Quest: Mysterious Times — Checkpoint 050

**Ngày:** 08/11/2026  
**Repository:** `ronvotri/VH-NDS` → `Magicians-Quest-Mysterious-Times/`  
**Nguồn:** `MagiciansQuest-VietHoa-Checkpoint-049.zip`  
**Tiến độ:** **14.149 / 55.976 (25.28%)**, +240 trang NPC.

## Thống kê

| Nhóm | Đã dịch | Tổng | Tăng |
|---|---:|---:|---:|
| 00 — Mở đầu | 106 | 106 | 0 |
| 01 — Hệ thống | 1.086 | 1.087 | 0 |
| 02 — Vật phẩm | 1.501 | 1.501 | 0 |
| 03 — Sổ tay | 432 | 432 | 0 |
| 04 — Hội thoại NPC | 11.024 | 52.608 | +240 |
| 05 — Credit | 0 | 242 | 0 |
| **Tổng** | **14.149** | **55.976** | **+240** |

## Nội dung mới

- `0033.018` (**120 trang**): đầu của một hiệp sĩ học Ngôn ngữ Phép thuật, dần thay cách cư xử với người chơi, học chào hỏi/khen/quở trách và đoàn tụ với thân; một người lớn nhờ đồ để bắt Manticore giữ nấm ngon; Griffin mất kho báu và nhờ truy tìm thủ phạm.
- `0033.019` (**120 trang**): gài lời khai cướp biển để tìm lại kho báu, an ủi Griffin; Harpy hát dở nhờ người chơi đệm nhạc và cuối cùng trưởng thành; cô bé bán diêm tìm tiền về thăm bà.
- Cách xưng hô: hiệp sĩ từ **ta–cậu/tiểu đồng**, nóng nảy dần lịch sự; cướp biển **lão–nhóc**; Griffin **ta–ngươi**; Harpy hơi đanh đá **ta–cậu**, cô bé bán diêm **tôi–cậu**.
- Bảo toàn mã vật phẩm động `$507'...;`, màu `$000`, nhánh câu thoại `$019`, tên người chơi `$500`, mã trừ tiền `$058'-100;`.

## Tệp bàn giao

- `translation/04-thoai/talkfigs__0eng__data__0033.018.jsonl` và `0033.019.jsonl`: 240 trang dịch mới, không thay `id`, `en`, `ctx`.
- `vi_0033_018_raw.txt`, `vi_0033_019_raw.txt`: bản dịch tay có placeholder `¤` cho token trung gian; `vi_0033_018.txt`, `vi_0033_019.txt`: bản hoàn chỉnh có mã game và ngắt dòng.
- `manual_0033_018.tsv`, `manual_0033_019.tsv`: bảng đối chiếu ID / EN / VI / ctx, 120 dòng mỗi tệp.
- `apply_050.py`, `qa_050.py`, `DELTA-050.jsonl`, `QA-050.md`: công cụ tái tạo và kết quả kiểm thử.

**QA PASS:** so sánh 501 JSONL / 55.976 bản ghi với checkpoint 049; bảo toàn 13.909 bản dịch cũ. ZIP tự chứa dữ liệu, không có ROM thương mại. Chưa kiểm thử NDS thực tế.

## Đợt 051 tiếp theo

`0033.020` (**120 trang**) và `0033.021` (**83 trang**), tổng **203 trang**. Cả hai tệp tiếng Anh đã nằm trong ZIP này; sẽ stage lên GitHub cùng commit 050.