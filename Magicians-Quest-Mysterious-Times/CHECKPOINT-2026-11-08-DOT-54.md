# Magician’s Quest: Mysterious Times — Checkpoint 054

**Ngày:** 08/11/2026  
**Repository:** `ronvotri/VH-NDS`, `Magicians-Quest-Mysterious-Times/`  
**Mốc trước:** checkpoint 053 — **14.832/55.976 (26,50%)**  
**Mốc mới:** **15.072/55.976 (26,93%)**, +240 trang; NPC **11.947/52.608**.

## Nội dung Việt hóa

| Tệp | Số trang | Nội dung |
|---|---:|---|
| `translation/04-thoai/talkfigs__0eng__data__0040.005.jsonl` | 120 | Chia tay người yêu nhưng giữ tình bạn; giao diện nói chuyện, quà tặng, đi chơi và đi học; nhận xét tình cảm và sinh hoạt giữa các NPC |
| `translation/04-thoai/talkfigs__0eng__data__0040.006.jsonl` | 120 | Các biến thể tin đồn có tên NPC động: bạn bè đi chơi, niệm chú, câu cá, âm nhạc, nhặt rác, nghịch ngợm, hẹn hò và quà tặng |
| **Tổng** | **240** | Giữ kiểu xưng hô tớ–cậu; nhân vật có nét tự phụ về vẻ lịch lãm, nhưng vẫn dễ thương |

## Tệp bàn giao

- `vi_0040_005_raw.txt`, `vi_0040_006_raw.txt`: bản dịch đã biên tập. Mã `¤` được dùng làm chỗ trống cho token động rồi được lắp lại theo đúng thứ tự xuất hiện từ tiếng Anh.
- `build_raw_054.py` chứa 53 và 45 mẫu câu được soạn và nhân vào **đúng từng bản ghi** tương ứng; không gộp hoặc xóa trang trùng. `apply_054.py` ghép lại token, chia dòng giao diện và điền `vi`.
- `vi_0040_005.txt`, `vi_0040_006.txt`: chuỗi cuối đầy đủ mã NDS; `manual_0040_005.tsv` và `manual_0040_006.tsv`: bảng ID/EN/VI/CTX.
- `DELTA-054.jsonl` chỉ gồm 240 thay đổi; `qa_054.py` và `QA-054.md` chứa kiểm định so với bản 053.
- **QA PASS:** 501 JSONL / 55.976 bản ghi, trường dữ liệu khác không đổi; mã điều khiển đúng, Unicode và giới hạn dòng đạt.
- Nguồn **đợt 055**: `0040.007` và `0040.008` (120 + 120) vẫn chưa dịch; có trong ZIP và được chuẩn bị lên GitHub.

**Giới hạn kiểm thử:** chưa chạy game trên ROM NDS; chưa kiểm chiều rộng thực khi tên NPC động được thay vào đoạn tin đồn. ZIP không chứa ROM thương mại.