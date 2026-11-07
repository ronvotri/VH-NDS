# Magician’s Quest: Mysterious Times — Checkpoint 032

**Ngày:** 07/11/2026  
**Repo:** `ronvotri/VH-NDS`, thư mục `Magicians-Quest-Mysterious-Times/`  
**Baseline:** `MagiciansQuest-VietHoa-Checkpoint-031.zip` (9.660 mục đã dịch)  
**Mốc mới:** **9.900/55.976 mục (17,69%)**, thêm **240 trang hội thoại NPC**.

## Tiến độ

| Nhóm | Đã dịch | Tổng | Mới |
| --- | ---: | ---: | ---: |
| 00 — Mở đầu | 106 | 106 | 0 |
| 01 — Hệ thống | 1.086 | 1.087 | 0 |
| 02 — Vật phẩm | 1.501 | 1.501 | 0 |
| 03 — Sổ tay | 432 | 432 | 0 |
| 04 — Hội thoại | 6.775 | 52.608 | +240 |
| 05 — Credit | 0 | 242 | 0 |
| **Tổng** | **9.900** | **55.976** | **+240** |

## Nội dung đợt 032

- `translation/04-thoai/talkfigs__0eng__data__0029.002.jsonl` — **120 trang**: NPC thích đồ ăn, những pha hậu đậu, ước mơ nghề nghiệp, trường học, thư tỏ tình và tình cảm tuổi học trò. Giữ ngôi xưng tớ–cậu và nét hài tự trào, không thay đổi ý gốc.
- `translation/04-thoai/talkfigs__0eng__data__0029.003.jsonl` — **120 trang**: ngắm hoa anh đào, đồ xinh, sự vụng về, tình bạn, quà tặng, bánh ngọt, gia đình và những suy ngẫm dịu dàng.
- `vi_0029_002_raw.txt`, `vi_0029_003_raw.txt`: bản dịch tay trước khi ngắt dòng; `vi_0029_002.txt`, `vi_0029_003.txt`: bản đã ngắt dòng ngắn cho khung thoại.
- `DELTA-032.jsonl`: 240 mục gồm ID, EN, VI và `ctx`. `qa_032.py` kiểm toàn bộ 501 JSONL với ZIP checkpoint 031; `QA-032.md` lưu kết quả.
- Giữ nguyên tên riêng `Piquard`, `Harrows`, `Vivian`, tên biến `$500;`, `$503'310;`, cùng mọi mã cảm xúc và màu `$000'...;`.

## QA và giới hạn

- **PASS 501 JSONL / 55.976 bản ghi** khi đối chiếu từng trường với ZIP 031.
- **Chỉ thêm 240 trường `vi`**, không ghi đè 9.660 mục đã dịch, không đổi `id`, `en`, `ctx`, khóa kỹ thuật và thứ tự bản ghi.
- Các chuỗi mới đúng token theo danh sách và thứ tự, Unicode NFC; không xuống dòng trong trường; tối đa 3 dấu `▼`, 34 ký tự nhìn thấy/dòng, kiểm byte budget khi có.
- **Chưa kiểm thử ROM NDS hoặc đo rộng pixel font thật.** Chỉ xác nhận cấu trúc và ngưỡng ký tự.
- ZIP checkpoint chỉ chứa dữ liệu văn bản và công cụ, **không gồm ROM thương mại**.

## Tiếp theo — đợt 033

- `0029.004` — 120 trang chưa dịch; sau đó `0029.005` nếu đủ nguồn.
- Tiếp tục dịch tay, giữ tính cách nhân vật, kiểm tra các nhánh lựa chọn, QA toàn bộ dữ liệu và lưu checkpoint GitHub.