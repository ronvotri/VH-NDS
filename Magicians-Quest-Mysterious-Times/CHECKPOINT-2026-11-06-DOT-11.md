# Magician’s Quest: Mysterious Times — Checkpoint 011

**Ngày:** 06/11/2026  
**GitHub:** `ronvotri/VH-NDS` → `Magicians-Quest-Mysterious-Times/`  
**Baseline:** checkpoint 010 = 4.930/55.976  
**Sau đợt 011:** **5.137/55.976 (9,18%)**, tăng **207 trang thoại**.

## Tiến độ

| Nhóm | Đã xử lý | Tổng | Đợt này |
|---|---:|---:|---:|
| Mở đầu | 106 | 106 | 0 |
| Hệ thống | 1.086 | 1.087 | 0 |
| Vật phẩm | 1.501 | 1.501 | 0 |
| Sổ tay | 432 | 432 | 0 |
| Hội thoại | 2.012 | 52.608 | +207 |
| Credit | 0 | 242 | 0 |
| **Tổng** | **5.137** | **55.976** | **+207** |

*Đã xử lý là số mục có `vi`, bao gồm tên riêng được giữ sau rà; không hàm ý mọi chuỗi đã được bản địa hóa hoàn toàn hoặc đạt kiểm thử in-game.*

## Lô dịch mới

- `translation/04-thoai/talkfigs__0eng__data__0020.005.jsonl`: 87/87 trang, bối cảnh 4017–4034, 4376–4398 và 4700–4734. Lời mời hẹn hò, yêu cầu làm bạn thân, quyết định thời gian gặp, tự sự về người bạn tên `$515;`. Giữ chính xác mã lựa chọn `$019'...;`, mã biểu cảm và mã thẻ màu `Điểm Hẹn Hò`.
- `translation/04-thoai/talkfigs__0eng__data__0021.001.jsonl`: 120/120 trang, bối cảnh 1–31. Chuyện đời thường: buffet pizza, ngày nghỉ, bài tập, nghịch ngợm, thầy giáo, quà tặng, học hành. Giọng vui dí dỏm và tớ–cậu; giữ biến tên `$500;`, `$503'...;`, tên riêng và thẻ màu đúng thứ tự.
- Chưa sửa các câu đã được dịch ở các đợt trước; `The Emporium` được giữ theo các đoạn hội thoại cửa hàng đã dịch. Cần rà thống nhất toàn dự án với tên hệ thống `Bách Hóa Tổng Hợp` ở đợt thuật ngữ sau.

## Kiểm tra

Đã đối chiếu toàn bộ **501 JSONL / 55.976 bản ghi** với ZIP checkpoint 010. Kết quả: **0 lỗi**, chỉ trường `vi` thay đổi đúng 207 bản ghi còn trống, không ghi đè bản dịch cũ, mã điều khiển/thẻ màu thứ tự nguyên vẹn, Unicode NFC hợp lệ, không vượt ngưỡng kiểm tra 34 ký tự trên từng dòng hiển thị. Chi tiết: `QA-011.md`.

**Lưu ý:** chưa thử thực tế trên ROM NDS. Cần test độ rộng pixel, font dấu, ngắt dòng khi NPC nói, nhánh chọn giờ hẹn và cảnh tỏ tình để hoàn thiện bản vá.

## Hướng dẫn nối phiên

- File bàn giao: `MagiciansQuest-VietHoa-Checkpoint-011.zip`, đầy đủ dữ liệu từ trước đến nay.
- File dịch tay mới: `manual_0020_005.txt` và `manual_0021_001.txt` (mỗi dòng là một trang theo thứ tự JSONL; mã mở/đóng trang được bộ áp tự động giữ).
- `apply_011.py`: áp hai bản dịch vào bản checkpoint 010 mới giải nén; tự bảo vệ không ghi đè bản có nội dung khác.
- `qa_011.py`: so với checkpoint 010 để tạo `DELTA-011.jsonl` và QA; có thể cần đổi đường dẫn ZIP baseline khi chạy trong thư mục khác.
- **Tiếp theo:** `0021.002` (120 trang) rồi các tệp `0021.*` kế tiếp. Trước khi chốt các nhân vật, kiểm tra ngôi xưng theo từng `ctx` và quan hệ đã được thiết lập.