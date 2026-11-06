# Magician’s Quest: Mysterious Times — Checkpoint 021

**Ngày:** 07/11/2026  
**Repo:** `ronvotri/VH-NDS`, thư mục `Magicians-Quest-Mysterious-Times/`  
**Baseline:** `MagiciansQuest-VietHoa-Checkpoint-020.zip` (7.191 mục)  
**Mốc mới:** **7.385/55.976 mục (13,19%)**, thêm **194 trang NPC**.

## Tiến độ

| Nhóm | Đã dịch | Tổng | Mới |
|---|---:|---:|---:|
| 00 — Mở đầu | 106 | 106 | 0 |
| 01 — Hệ thống | 1.086 | 1.087 | 0 |
| 02 — Vật phẩm | 1.501 | 1.501 | 0 |
| 03 — Sổ tay | 432 | 432 | 0 |
| 04 — Hội thoại | 4.260 | 52.608 | +194 |
| 05 — Credit | 0 | 242 | 0 |
| **Tổng** | **7.385** | **55.976** | **+194** |

## Phạm vi đợt 021

- `0024.005` — 74 trang: chọn giờ hẹn tại **Điểm Hẹn Hò**, nói về bạn bè, tin đồn, trò chuyện và hoạt động cùng người quen. Đặc biệt giữ `$515;` và `$500;` đúng ngữ cảnh khi tên người chơi/NPC đứng đầu hoặc giữa câu.
- `0025.001` — 120 trang: NPC nói chuyện xuề xòa, thích nằm dài, ngủ nướng, ăn uống, mua sắm, các trò nghịch ngợm và đối đáp hài; giữ nét tính cách mà không lạm dụng tiếng lóng.
- Bản dịch tay `vi_0024_005.txt`, `vi_0025_001.txt`; bản đối chiếu `manual_0024_005.tsv`, `manual_0025_001.tsv` (ID / EN / VI).
- `apply_021.py` để tái áp dụng bản dịch từ checkpoint 020 (chỉ sửa `vi`); `qa_021.py` để đối chiếu dữ liệu; `DELTA-021.jsonl` ghi đủ 194 thay đổi.

## QA

- **PASS:** 501 tệp JSONL và 55.976 bản ghi, đúng 194 trường `vi` mới trong hai tệp; không sửa metadata hoặc lời Việt cũ.
- Giữ nguyên thứ tự các mã biểu cảm, biến tên `$500;`, `$515;`, màu địa điểm `$000'5;` / `$000'1;`, mã lựa chọn/nhánh và ký tự cần bảo toàn.
- Chuẩn NFC, không CR/LF/tab, dòng không dài quá 34 ký tự thấy được, số `▼` tối đa 3, giới hạn byte nếu có.
- **Chưa kiểm thử font/pixel hoặc chạy ROM NDS thật**; cần kiểm tra trường hợp tên người chơi/NPC dài và tốc độ hiển thị câu ba dòng.
- ZIP chứa dữ liệu dịch, mã nguồn, QA và tài liệu; không chứa ROM thương mại.

## Tiếp theo — đợt 022

Dịch `0025.002` (120) và `0025.003` (120) theo cùng giọng NPC, bảo toàn mã và bối cảnh.