# Magician’s Quest: Mysterious Times — Checkpoint 036

**Ngày:** 07/11/2026  
**Repository:** `ronvotri/VH-NDS`, thư mục `Magicians-Quest-Mysterious-Times/`  
**Baseline:** `MagiciansQuest-VietHoa-Checkpoint-035.zip` (10.568 mục đã dịch)  
**Mốc mới:** **10.808/55.976 mục (19,31%)**, thêm **240 trang thoại NPC**.

## Tiến độ

| Nhóm | Đã dịch | Tổng | Mới |
| --- | ---: | ---: | ---: |
| 00 — Mở đầu | 106 | 106 | 0 |
| 01 — Hệ thống | 1.086 | 1.087 | 0 |
| 02 — Vật phẩm | 1.501 | 1.501 | 0 |
| 03 — Sổ tay | 432 | 432 | 0 |
| 04 — Hội thoại | 7.683 | 52.608 | +240 |
| 05 — Credit | 0 | 242 | 0 |
| **Tổng** | **10.808** | **55.976** | **+240** |

## Nội dung đợt 036

- `translation/04-thoai/talkfigs__0eng__data__0030.005.jsonl`: **120 trang**. Kết thúc cuộc dạo chơi, các câu rủ rê và đáp lại, hẹn gặp ở Điểm Hẹn Hò, chọn giờ 10h/12h/15h/18h/20h, tỏ tình và hẹn hò, ưu tiên giữ lời hứa; câu chuyện về người bạn `$515;`. Giữ sắc thái nữ NPC dịu dàng, lịch thiệp và ngôi tớ–cậu; không mất lựa chọn `$019'...;`.
- `translation/04-thoai/talkfigs__0eng__data__0031.001.jsonl`: **120 trang**. Nhân vật nhút nhát, hay lo âu kể chuyện đan len, thơ, vẽ tranh, gấp giấy, thư từ và các hiểu lầm khi trò chuyện với bạn; có cả các đoạn tự nhìn nhận cảm xúc, nên dịch nhẹ nhàng, hạn chế giễu cợt.
- Dịch thủ công: `vi_0030_005_raw.txt`, `vi_0031_001_raw.txt`; bản ngắt dòng tương ứng `.txt`, bảng đối chiếu `manual_0030_005.tsv`, `manual_0031_001.tsv`.
- Công cụ `apply_036.py`, `qa_036.py`; `DELTA-036.jsonl` chứa nguyên bản EN, VI, mã ID và ngữ cảnh; `QA-036.md` có kết quả kiểm tra.

## Kết quả QA

- **PASS:** 501 JSONL / 55.976 bản ghi, đối chiếu từng trường với checkpoint 035.
- Chỉ có **240 `vi` mới**, không ghi đè 10.568 mục đã dịch hoặc thay các trường khác.
- Bảo toàn toàn bộ mã điều khiển, mã biểu cảm và thứ tự lựa chọn; NFC, không có ký tự điều khiển bất hợp lệ; mỗi trang tối đa 3 dấu `▼`, mỗi dòng không quá 34 ký tự hiển thị theo cách đếm chưa tính độ rộng pixel của font game.
- **Chưa thử trực tiếp trên ROM NDS.** ZIP chứa bảng dịch và công cụ, **không chứa ROM thương mại**.

## Tiếp theo — đợt 037

- `0031.002` — 120 trang thoại chưa dịch.
- `0031.003` — 120 trang thoại chưa dịch.
- Giữ giọng NPC nhút nhát, ngôi xưng, tên người chơi/NPC và nhánh hội thoại; so sánh với checkpoint 036 trước khi cập nhật GitHub.