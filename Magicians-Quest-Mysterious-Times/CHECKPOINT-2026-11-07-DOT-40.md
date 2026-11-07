# Magician’s Quest: Mysterious Times — Checkpoint 040

**Ngày:** 07/11/2026  
**Repository:** `ronvotri/VH-NDS`, thư mục `Magicians-Quest-Mysterious-Times/`  
**Baseline:** `MagiciansQuest-VietHoa-Checkpoint-039.zip` (**11.509** mục dịch)  
**Mốc mới:** **11.749 / 55.976 mục (20,99%)**, **+240** trang thoại NPC.

## Tiến độ

| Nhóm | Đã dịch | Tổng | Mới |
|---|---:|---:|---:|
| 00 — Mở đầu | 106 | 106 | 0 |
| 01 — Hệ thống | 1.086 | 1.087 | 0 |
| 02 — Vật phẩm | 1.501 | 1.501 | 0 |
| 03 — Sổ tay | 432 | 432 | 0 |
| 04 — Hội thoại NPC | 8.624 | 52.608 | +240 |
| 05 — Credit | 0 | 242 | 0 |
| **Tổng** | **11.749** | **55.976** | **+240** |

## Nội dung đợt 040

- `translation/04-thoai/talkfigs__0eng__data__0032.003.jsonl` — **120 trang**: lời chào năm mới; thông báo trước giờ học; thầy Vlad nghiêm khắc kể về Ngôn ngữ Phép thuật, luyện niệm chú, cách sống của người giáo viên, cô Strawe; lựa chọn đổi đồng phục và xem sổ điểm danh.
- `translation/04-thoai/talkfigs__0eng__data__0032.004.jsonl` — **120 trang**: câu chuyện của thầy Oakley về bà Malila, chuyện nghịch ngợm với bố hiệu trưởng Sol, thú cưng mèo đưa thư của thầy Vlad, học phép và đoạn mở nhiệm vụ tìm tiên.
- Giọng nói: thầy Vlad nghiêm túc dùng **thầy–em**; thầy Oakley lớn tuổi dùng **ta–em**, hóm hỉnh, hơi nghễnh ngãng. Không biến những lời giáo huấn thành meme.
- Giữ mã điều khiển; tên địa điểm **Bách Hóa Tổng Hợp**; menu/điều kiện game dịch sát nguồn. Không sửa mâu thuẫn giữa nhãn *seating chart* và đáp thoại *attendance sheet*.

## Tệp bàn giao

- `vi_0032_003_raw.txt`, `vi_0032_004_raw.txt`: bản dịch câu chữ, chưa tự ghép mã đầu/cuối.
- `vi_0032_003.txt`, `vi_0032_004.txt`: bản ghép mã và dấu ngắt dòng cuối.
- `manual_0032_003.tsv`, `manual_0032_004.tsv`: đối chiếu id/EN/VI/ctx từng trang.
- `apply_040.py`: áp lại bản dịch kiểm tra mã, không ghi đè bản dịch khác.
- `qa_040.py`, `QA-040.md`: kiểm tra dữ liệu với checkpoint 039.
- `DELTA-040.jsonl`: bản kê 240 thay đổi `vi`.

## QA

**PASS:** 501 tệp JSONL / 55.976 bản ghi, chỉ thêm đúng 240 trường `vi`, giữ nguyên 11.509 bản dịch cũ. Mã điều khiển, Unicode NFC, ngắt dòng và giới hạn ký tự tĩnh đã kiểm tra. **Chưa thử ROM NDS thực tế**.

## Đợt 041 tiếp theo

- `0032.005`: 120 trang chưa dịch, phần tiếp nhiệm vụ tiên.
- `0033.001`: 120 trang chưa dịch, mở nhóm thoại nhân vật mới.
- Tổng dự kiến **240 trang**. Hai tệp nguồn nguyên bản được đưa lên GitHub để nối tiếp thuận tiện.