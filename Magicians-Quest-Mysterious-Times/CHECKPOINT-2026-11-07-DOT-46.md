# Magician’s Quest: Mysterious Times — Checkpoint 046

**Ngày:** 07/11/2026  
**Repository:** `ronvotri/VH-NDS` → `Magicians-Quest-Mysterious-Times/`  
**Nguồn:** `MagiciansQuest-VietHoa-Checkpoint-045.zip`  
**Kết quả:** **13.189 / 55.976 mục (23,56%)**, +240 trang thoại NPC.

## Tiến độ

| Nhóm | Đã dịch | Tổng | Tăng |
|---|---:|---:|---:|
| 00 — Mở đầu | 106 | 106 | 0 |
| 01 — Hệ thống | 1.086 | 1.087 | 0 |
| 02 — Vật phẩm | 1.501 | 1.501 | 0 |
| 03 — Sổ tay | 432 | 432 | 0 |
| 04 — Hội thoại NPC | 10.064 | 52.608 | +240 |
| 05 — Credit | 0 | 242 | 0 |
| **Tổng** | **13.189** | **55.976** | **+240** |

## Nội dung đã dịch

- `0033.010` — **120 trang:** lựa chọn đồ vật trong vụ điều tra, quỷ khổng lồ thách chơi đuổi bắt (bắt lén 3 lần trong thời gian quy định); Jack Frost đến thị trấn tìm ba đặc sản cho bữa tiệc tinh linh tuyết (vật phẩm dùng mã động `$507`). Giữ giọng thách thức **ta–nhóc**, giữ tên **Jack Frost**.
- `0033.011` — **120 trang:** hoàn tất nhiệm vụ ba món ăn, lời cảm ơn và món quà của Jack Frost; tiếng nói ngây ngô của sinh vật nhỏ; linh thú được triệu hồi quậy phá rồi xin về thế giới cũ; nàng tiên cá bị mất giọng và buồn chuyện tình cảm. Giữ đúng sắc thái từng nhân vật; không thêm điều kiện nhiệm vụ.

## Dữ liệu và công cụ

- `translation/04-thoai/talkfigs__0eng__data__0033.010.jsonl`, `0033.011.jsonl`: hai tệp đã dịch.
- `manual_0033_010.tsv`, `manual_0033_011.tsv`: bảng ID–EN–VI–ctx; `vi_0033_010_raw.txt`, `vi_0033_011_raw.txt`: bản dịch tay có chỗ đánh dấu mã; `vi_0033_010.txt`, `vi_0033_011.txt`: câu cuối cùng với mã game.
- `DELTA-046.jsonl`: 240 bản ghi thay đổi; `apply_046.py`, `qa_046.py`, `QA-046.md`: áp và đối chiếu.

## QA và giới hạn

**PASS:** kiểm tra đủ 501 tệp JSONL, 55.976 mục, giữ nguyên 12.949 bản dịch trước đó. Chỉ thêm `vi` mới, giữ đúng mã điều khiển, lựa chọn, ID, Unicode NFC và giới hạn ký tự. ZIP không chứa ROM thương mại.

**Chưa thử trong ROM NDS.** Cần kiểm tra chiều rộng pixel và đặc biệt các tên vật phẩm động khi game thay mã `$507`.

## Đợt 047

Tiếp `0033.012` và `0033.013`, mỗi tệp **120 trang**; nguồn chưa dịch đã có trong ZIP checkpoint 046 và nên đồng bộ trước lên GitHub.