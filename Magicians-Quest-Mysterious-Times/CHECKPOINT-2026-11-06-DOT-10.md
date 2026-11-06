# Magician’s Quest: Mysterious Times — Checkpoint Việt hóa 010

**Ngày:** 06/11/2026  
**Repo:** `ronvotri/VH-NDS` → `Magicians-Quest-Mysterious-Times/`  
**Baseline:** Checkpoint 009 — 4.690/55.976 mục  
**Sau đợt 010:** **4.930/55.976 mục (8,81%)**, tăng **240 trang thoại**.

## Thống kê

| Nhóm | Đã xử lý | Tổng | Mới |
|---|---:|---:|---:|
| Mở đầu | 106 | 106 | 0 |
| Hệ thống | 1.086 | 1.087 | 0 |
| Vật phẩm | 1.501 | 1.501 | 0 |
| Sổ tay | 432 | 432 | 0 |
| Hội thoại | 1.805 | 52.608 | +240 |
| Credit | 0 | 242 | 0 |
| **Tổng** | **4.930** | **55.976** | **+240** |

Lưu ý: con số "đã xử lý" bao gồm cả tên riêng được duyệt giữ nguyên, không đồng nghĩa số tiếng Anh đã được dịch hoàn toàn. Bản chưa qua kiểm thử thực tế trong ROM.

## Lô 010

- `translation/04-thoai/talkfigs__0eng__data__0020.003.jsonl`: dịch 120/120 trang, bối cảnh 56–84 (cắm trại, mùa đông, đi bộ, cứu hộ, thời trang và chuyện bạn bè). Giọng tự nhiên, hài Gen Z; không đẩy trò đùa sang các câu nghiêm túc.
- `translation/04-thoai/talkfigs__0eng__data__0020.004.jsonl`: dịch 120/120 trang, bối cảnh 85–90 và 2300–4017 (mở rộng hội thoại, lời mời, làm bạn, hẹn hò). Các lựa chọn trả lời dùng giọng nhân vật phù hợp.
- Giữ nhất quán địa danh **Lovers Point → Điểm Hẹn Hò** theo đoạn mở đầu đã dịch; các thẻ định dạng màu `$000'5;` và `$000'1;` giữ nguyên.
- Khi vai giáo viên chưa rõ giới tính, dùng từ trung tính **giáo viên** thay vì tự gán thầy/cô. Khi giới tính xác định từ văn bản có thể dùng xưng hô tương ứng.

## Kiểm tra

- Đối chiếu đủ **501 tệp JSONL** với checkpoint 009, chỉ thay trường `vi` của 240 bản ghi trước đó còn trống.
- Không đổi `id`, `en`, `ctx`, trường kỹ thuật và thứ tự ID.
- Tất cả `$...;` đúng thứ tự, gồm mã tên `$500;`, nhánh trả lời `$019'...;`, mã biểu cảm và thẻ màu địa danh. Không thêm tab / CR / LF, Unicode NFC hợp lệ.
- Không vượt ngưỡng thử nghiệm 34 ký tự/trang-dòng sau khi bỏ mã lệnh; 0 lỗi / 0 cảnh báo theo `qa_010.py`.
- **Chưa kiểm thử độ rộng pixel thực tế, font dấu hay va chạm dòng trong game NDS.**

## Tệp nối phiên

- `manual_0020_003.txt`, `manual_0020_004.txt`: bản dịch tay tương ứng 120 trang mỗi tệp; dùng ký hiệu `¤` làm chỗ điền mã điều khiển đúng vị trí nguồn.
- `apply_010.py`: áp bản dịch lên checkpoint 009 mới giải nén; từ chối ghi đè phần đã có.
- `qa_010.py`: so sánh với checkpoint 009, sinh `DELTA-010.jsonl` và báo cáo `QA-010.md`.
- `DELTA-010.jsonl`: 240 ID mới + EN + VI + ctx.
- ZIP `MagiciansQuest-VietHoa-Checkpoint-010.zip`: bản đầy đủ nối từ checkpoint 009, giữ các đợt trước.

## Tiếp theo — Checkpoint 011

Ưu tiên `0020.005` (87 trang còn trống), sau đó khảo sát nhóm tiếp theo có thật. Không tự ý đổi ngôi xưng hoặc các lựa chọn tình cảm khi chưa đối chiếu `ctx` và mạch hội thoại.