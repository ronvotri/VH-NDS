# Jump Ultimate Stars — Việt hóa Checkpoint 044

**Ngày 19/11/2026.** Đã dịch thêm **698 ID**, tiến độ **28497/34919 (81.61%)**, còn **6422 ID**.

## Phạm vi

- Nguồn: ZIP bàn giao `JumpUltimateStars_Japan_BanGiao_Cloud.zip`, tệp `translation/06-jquiz-007.jsonl`. Dịch row_index **325–1022**.
- Các câu đố về *One Piece* (manga_code=41) từ **325–944** (**620 ID**): băng Mũ Rơm, Arlong Park, Alabasta, Skypiea, Water Seven và Enies Lobby.
- *Pyu to Fuku! Jaguar* (manga_code=27) từ **945–1022** (**78 ID**).
- Đợt 044 kết thúc ở phương án cuối câu số 2240; **CP045 bắt đầu tại `06-jquiz-007.jsonl`, row_index 1023** (câu 2241).

## File bàn giao

- `BAN_DICH_044.jsonl`: 698 bản ghi Nhật–Việt, ID nguyên bản, metadata và `quiz_context`.
- `BAN_DICH_044.tsv`: dễ kiểm soát từng dòng.
- `BAN_DICH_TONG_HOP_038-044.jsonl`: bản nối CP038–044, **4.901 ID**, không phải CP001–044.
- `QA_044.json`: thống kê QA, SHA256 nguồn, các phương án giữ Hán tự và ký hiệu gốc cần xem lại.

## Kiểm tra đã thực hiện

- 698/698 mục có tiếng Nhật và Việt; 698 ID không trùng; không giao nhau với 4.203 ID của CP038–043.
- Các trường `ja`, `group`, `context`, `uses`, `quiz_context` giữ nguyên nguồn; số và thứ tự phương án không thay đổi.
- Thẻ điều khiển không thêm/bớt; tất cả câu Việt <= 37 ký tự Unicode.
- Một số câu hỏi dùng lại phương án ở câu khác, file nguồn có thể chỉ xuất vài đáp án. **Không tự bịa phương án bị thiếu**.
- Các chữ Hán trong phương án đánh lừa nhau được giữ nguyên; xem các dòng đặc biệt trong QA.
- **Chưa QA đáp án đúng, font rộng bao nhiêu pixel, bản ROM NDS hoặc gameplay thực tế.** Đây chỉ là dữ liệu dịch text, chưa có patch ROM chơi được.

## Cách phục hồi đầy đủ

1. Khôi phục 23.596 ID CP001–037 theo `PHUC_HOI_TONG_HOP_037.md`.
2. Nối CP038–044 (**4.901 ID**) theo ID, từ chối ID trùng → **28497 ID**.
3. Overlay sửa QA 037B và 037C bằng cách **thay giá trị `vi` theo ID**, không nối thêm bản ghi.
