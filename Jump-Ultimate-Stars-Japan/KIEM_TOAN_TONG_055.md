# Jump Ultimate Stars — kiểm toán toàn văn bản đến CP055

- Nguồn: `JumpUltimateStars_Japan_BanGiao_Cloud.zip` — SHA-256 `14e839a35e75f35534a93a1b37ebe42731ea530fbc012267b45bbbed8446f241`.
- `30` JSONL nguồn, `34.919` ID duy nhất.
- `CP001–037`: `23.596` chuỗi; GH audit `KIEM_TOAN_CP001_037_055.json` `PASS`, `22` nhóm nguồn, băm kép ID/JA/file/row_index/quiz_context theo thứ tự bản ghi.
- `CP038–055`: `11.323` chuỗi; so trực tiếp mọi metadata được lưu trong bản dịch với nguồn, trừ trường vi.
- Tổng 34.919 ID, 0 thiếu, không chồng lặp theo ID.
- Dữ liệu J-Quiz CP026 `651` dòng bị thiếu quiz_context, đã phục hồi nguồn trên GitHub và chạy lại kiểm toán `PASS`, không đổi nội dung Nhật/Việt.
- Đính chính CP050A `10` dòng vẫn tồn tại trong bản gộp 038–055.

## Phân biệt cấp nghiệm thu

| Hạng mục | Kết quả |
| --- | --- |
| Đủ 34.919 ID và có tiếng Việt | PASS |
| ID/câu Nhật/vị trí gốc | PASS |
| J-Quiz ngữ cảnh và thứ tự | PASS về metadata; chưa QA đáp án đúng |
| Token trong 248 dòng CP055 | PASS |
| Tương thích mã hóa ROM | CHƯA TEST |
| Font Việt, kích thước pixel NDS | CHƯA TEST |
| Đúng ngữ nghĩa và xưng hô toàn bộ game | CẦN RÀ THỦ CÔNG |

Thông tin chi tiết và tập tin ghi đè có trong `QA_055.json`, `BAN_GIAO_055.md` và nhánh `vh/jump-ultimate-stars-japan`.
