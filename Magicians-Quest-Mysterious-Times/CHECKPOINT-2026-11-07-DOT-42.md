# Magician’s Quest: Mysterious Times — Checkpoint 042

**Ngày:** 07/11/2026  
**Repository:** `ronvotri/VH-NDS` → `Magicians-Quest-Mysterious-Times/`  
**Checkpoint nguồn:** `MagiciansQuest-VietHoa-Checkpoint-041.zip`  
**Kết quả:** **12.229/55.976 mục (21,85%)**, tăng **240 trang thoại NPC**.

## Tiến độ

| Nhóm | Đã dịch | Tổng | Tăng |
|---|---:|---:|---:|
| 00 — Mở đầu | 106 | 106 | 0 |
| 01 — Hệ thống | 1.086 | 1.087 | 0 |
| 02 — Vật phẩm | 1.501 | 1.501 | 0 |
| 03 — Sổ tay | 432 | 432 | 0 |
| 04 — Hội thoại NPC | 9.104 | 52.608 | +240 |
| 05 — Credit | 0 | 242 | 0 |
| **Tổng** | **12.229** | **55.976** | **+240** |

## Hai tệp đã dịch

- `translation/04-thoai/talkfigs__0eng__data__0033.002.jsonl` — **120 trang**: đối chất với cướp biển, thu hồi rương ở nhà ma; lời tiên tri tình yêu của thần hoa; Nhân Sư ra câu đố và các thử thách Gọi Mưa, Cầu Vồng, gọi hoa.
- `translation/04-thoai/talkfigs__0eng__data__0033.003.jsonl` — **120 trang**: hoàn thành thử thách Nhân Sư, học phép Sao Băng, nhận Ngọc Xanh Biển/Ngọc Lam; quái rương ông M và bản đồ truy tìm kho báu; rồng bị thương cần thuốc chữa.
- Thống nhất tên với bản dịch hiện có: **Ngọc Xanh Biển, Ngọc Lam, Gọi Mưa, Cầu Vồng, Sao Băng, Săn Kho Báu, Ritch**. Cướp biển xưng **lão–nhóc**; Nhân Sư **ta–em**; thoại rồng có sắc thái cảnh giác, dứt khoát.
- Giữ nguyên câu đố nhân sư (sáng bốn chân, trưa hai, tối ba); giữ gợi ý **E10 S10 → Đông 10, Nam 10** và thông tin thời gian 100–200 năm. Không thay cơ chế nhận vật phẩm hoặc mã trao thưởng.

## Tệp hỗ trợ và QA

- `vi_0033_002_raw.txt`, `vi_0033_003_raw.txt`: bản dịch theo dòng trước khi ghép mã đầu/cuối; `vi_0033_002.txt`, `vi_0033_003.txt`: lời thoại đã ghép mã và ngắt dòng.
- `manual_0033_002.tsv`, `manual_0033_003.tsv`: bảng ID / EN / VI.
- `DELTA-042.jsonl`: 240 bản ghi thay đổi duy nhất trường `vi`.
- `apply_042.py`: áp bản dịch có kiểm tra, an toàn khi chạy lại; `qa_042.py` và `QA-042.md`: rà 501 JSONL và giới hạn kỹ thuật.

## QA

**PASS:** so sánh 501 JSONL và 55.976 mục với checkpoint 041, giữ nguyên 11.989 bản dịch cũ, chỉ điền 240 trường `vi` của hai tệp đích. Bảo toàn `id`, `en`, `ctx`, thứ tự, mã điều khiển `$...;`, mã lựa chọn/chuyển nhánh, biến tên, vật phẩm, tiền thưởng. Unicode NFC; tối đa ba dấu `▼` và 34 ký tự thấy được trên mỗi dòng, kiểm tra giới hạn byte khi có.

**Chưa kiểm thử trên ROM Nintendo DS** hoặc đo bề rộng pixel thực tế, nhất là tên biến động. ZIP là bộ dữ liệu và công cụ, không chứa ROM thương mại.

## Đợt 043

Tiếp tục **`0033.004` (120 trang)** và **`0033.005` (120 trang)**, tổng **240 trang**; bản nguồn chưa dịch có sẵn trong ZIP 042 và được stage lên GitHub.