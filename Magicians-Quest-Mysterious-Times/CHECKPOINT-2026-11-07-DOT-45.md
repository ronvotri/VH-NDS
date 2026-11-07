# Magician’s Quest: Mysterious Times — Checkpoint 045

**Ngày:** 07/11/2026  
**Repository:** `ronvotri/VH-NDS` → `Magicians-Quest-Mysterious-Times/`  
**Nguồn:** `MagiciansQuest-VietHoa-Checkpoint-044.zip`  
**Kết quả:** **12.949/55.976 mục (23,13%)**, tăng **240 trang NPC**.

## Thống kê

| Nhóm | Đã dịch | Tổng | Tăng |
|---|---:|---:|---:|
| 00 — Mở đầu | 106 | 106 | 0 |
| 01 — Hệ thống | 1.086 | 1.087 | 0 |
| 02 — Vật phẩm | 1.501 | 1.501 | 0 |
| 03 — Sổ tay | 432 | 432 | 0 |
| 04 — Hội thoại NPC | 9.824 | 52.608 | +240 |
| 05 — Credit | 0 | 242 | 0 |
| **Tổng** | **12.949** | **55.976** | **+240** |

## Nội dung

- `translation/04-thoai/talkfigs__0eng__data__0033.008.jsonl` — **120 trang**: buổi huấn luyện Minotaur (chào 10 lần, chạy vòng phế tích, bãi biển và rừng), Gremlin phá máy móc, hướng dẫn bấm nút X để bắt Gremlin, giáo viên đi tìm dụng cụ và hồn ma tại dinh thự bị mất đồ.
- `translation/04-thoai/talkfigs__0eng__data__0033.009.jsonl` — **120 trang**: ông cướp biển đòi tiền để trả lời câu hỏi; điều tra lời khai theo ngày, giờ, địa điểm, món đồ; vạch trần Thuyền trưởng Dot đã lấy trộm **tủ quần áo**; đưa vật chứng về cho hồn ma và xử lý hành trang đầy.
- Giọng nhân vật giữ riêng: Minotaur **ta–nhóc**; Gremlin **ta–ngươi**; cướp biển **lão–nhóc** với tiếng đệm Arrr; hồn ma **ta–ngươi**; người hướng dẫn cơ chế trung tính.
- Thuật ngữ địa danh đúng mạch trước: **Ngôi Nhà Ma**, **Limelight**, **Tiệm Thời Trang Vivian**; đơn vị tiền **Ritch**. Các lựa chọn 100/500/1000 Ritch, Không đưa gì, Trả tiền/Không trả và thời điểm được giữ nguyên thứ tự cùng mã `$019'-1;`.

## Tệp bàn giao

- `DELTA-045.jsonl`: 240 cập nhật theo ID, có nguồn EN và phần VI mới.
- `manual_0033_008.tsv`, `manual_0033_009.tsv`: đối chiếu ID, EN, VI, ctx.
- `vi_0033_008_raw.txt`, `vi_0033_009_raw.txt`: bản dịch tay nguyên câu với các vị trí chèn token `¤`; `vi_0033_008.txt`, `vi_0033_009.txt`: bản hoàn chỉnh có mã game và ngắt dòng.
- `apply_045.py`, `qa_045.py`, `QA-045.md`: công cụ áp bản dịch và kiểm tra toàn bộ tệp; `README.md` và `BAN_GIAO.md` cập nhật tiến độ.

## QA và giới hạn

**PASS:** đối chiếu cả 501 JSONL/55.976 bản ghi với ZIP 044; **12.709 bản dịch cũ được bảo toàn**, 240 bản mới; mã điều khiển không đổi thứ tự/tham số, Unicode NFC và giới hạn ngắt dòng đạt. Chưa thử thật trên ROM NDS hoặc đo pixel font trong game. ZIP không chứa ROM thương mại.

## Đợt 046

Tiếp `0033.010` và `0033.011`, mỗi tệp 120 trang; nguồn EN có trong ZIP và được đưa trước lên GitHub để tránh gián đoạn.