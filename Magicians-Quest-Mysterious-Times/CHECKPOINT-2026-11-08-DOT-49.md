# Magician’s Quest: Mysterious Times — Checkpoint 049

**Ngày:** 08/11/2026  
**Repository:** `ronvotri/VH-NDS` → `Magicians-Quest-Mysterious-Times/`  
**Nguồn:** `MagiciansQuest-VietHoa-Checkpoint-048.zip`  
**Tiến độ:** **13.909 / 55.976 (24,85%)**, +240 trang NPC.

## Thống kê

| Nhóm | Đã dịch | Tổng | Tăng |
|---|---:|---:|---:|
| 00 — Mở đầu | 106 | 106 | 0 |
| 01 — Hệ thống | 1.086 | 1.087 | 0 |
| 02 — Vật phẩm | 1.501 | 1.501 | 0 |
| 03 — Sổ tay | 432 | 432 | 0 |
| 04 — Hội thoại NPC | 10.784 | 52.608 | +240 |
| 05 — Credit | 0 | 242 | 0 |
| **Tổng** | **13.909** | **55.976** | **+240** |

## Nội dung mới

- `0033.016` (**120 trang**): hoàn tất việc tìm chó săn hoang; hồn ma và đoàn **linh hồn không yên** biểu diễn tại Nhà Ma do **thầy Vlad** mời; phần thưởng theo số nghệ sĩ bị đánh bại; nhạc công lang thang muốn **hòa tấu với bạn bè**, sáng tác các bài nhạc rồi lên đường; cuối tệp bắt đầu hội thoại với những linh thể hiếm thấy.
- `0033.017` (**120 trang**): linh thể chỉ xuất hiện một lần; **ông già Noel** xin diêm, kể chuyện **Cô Bé Bán Diêm** và tuần lộc Prancer, giao quà trước bình minh; **Chồn Gió** bị bắt; một vị **hiệp sĩ mất thân mình** nhờ tìm lại thân và học Ngôn ngữ Phép thuật.
- Giọng nhân vật: người giới thiệu xiếc ma lịch thiệp nhưng thích đùa **ta–nhóc**; nhạc công phóng khoáng **tôi–cậu/bạn hiền**; Santa **ông–cháu**; linh thể **ta/chúng ta–em**; hiệp sĩ nóng nảy **ta–nhóc**.
- Lựa chọn **Có/Không** và các điều kiện phát quà được giữ nguyên mã nhánh và mã đếm; giữ tên riêng Prancer, Chồn Gió và các mã động.

## Dữ liệu bàn giao

- `translation/04-thoai/talkfigs__0eng__data__0033.016.jsonl`, `0033.017.jsonl`: 240 trang đã dịch, giữ nguyên ID, EN, ctx và mọi mã engine.
- `vi_0033_016_raw.txt`, `vi_0033_017_raw.txt`: bản dịch tay có placeholder cho mã điều khiển; `vi_0033_016.txt`, `vi_0033_017.txt`: bản thành phẩm có mã và ngắt dòng.
- `manual_0033_016.tsv`, `manual_0033_017.tsv`: bảng đối chiếu ID / EN / VI / ctx.
- `apply_049.py`, `qa_049.py`, `DELTA-049.jsonl`, `QA-049.md`: công cụ tái tạo, đối chiếu, thống kê và kiểm tra.

**QA PASS:** so sánh 501 JSONL/55.976 bản ghi với checkpoint 048, giữ nguyên 13.669 bản dịch cũ. ZIP tự chứa dữ liệu, không chứa ROM thương mại. Chưa test trong ROM Nintendo DS thật.

## Đợt 050 tiếp theo

`0033.018` (**120**) và `0033.019` (**120**), tổng 240 trang. Nguồn có trong ZIP 049 và được đưa trước lên GitHub để phiên sau tiếp tục thuận tiện.