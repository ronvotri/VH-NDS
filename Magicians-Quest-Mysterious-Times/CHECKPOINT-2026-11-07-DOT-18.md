# Magician’s Quest: Mysterious Times — Checkpoint 018

**Ngày:** 07/11/2026  
**Repository:** `ronvotri/VH-NDS`, thư mục `Magicians-Quest-Mysterious-Times/`  
**Baseline:** `MagiciansQuest-VietHoa-Checkpoint-017.zip` (6.525 mục)  
**Mốc mới:** **6.711 / 55.976 mục (11,99%)**, thêm **186 trang NPC**.

## Tiến độ

| Nhóm | Đã dịch | Tổng | Mới |
|---|---:|---:|---:|
| 00 — Mở đầu | 106 | 106 | 0 |
| 01 — Hệ thống | 1.086 | 1.087 | 0 |
| 02 — Vật phẩm | 1.501 | 1.501 | 0 |
| 03 — Sổ tay | 432 | 432 | 0 |
| 04 — Hội thoại | 3.586 | 52.608 | +186 |
| 05 — Credit | 0 | 242 | 0 |
| **Tổng** | **6.711** | **55.976** | **+186** |

## Đợt 018

- `translation/04-thoai/talkfigs__0eng__data__0023.004.jsonl`: **120/120**, các câu rủ đi chơi, trà, học nhóm, từ chối, hẹn hò, tỏ tình, kết bạn và làm cộng sự. Ngôn ngữ giữ vẻ mạnh miệng hay ra lệnh của NPC nhưng không làm mất cảm xúc trong lời tỏ tình.
- `translation/04-thoai/talkfigs__0eng__data__0023.005.jsonl`: **66/66**, các lựa chọn giờ hẹn (10h, 12h, 15h, 18h, 20h) và lời NPC kể về mối quan hệ, các hoạt động chung, học tập, câu cá và uống trà.
- Bản dịch tay theo thứ tự từng tệp: `vi_0023_004.txt` và `vi_0023_005.txt`. Mã tạo trường `vi`: `apply_018.py`. Tệp bản ghi theo ID: `manual_0023_004.tsv`, `manual_0023_005.tsv`.
- Giữ nguyên mã nhánh `$019`, `$079`, biến `$500;`, `$515;`, tên địa điểm **Lovers Point → Điểm Hẹn Hò** và hai thẻ màu `$000'5;`, `$000'1;`.

## Đối chiếu và QA

- Chạy `python qa_018.py` với ZIP checkpoint 017 đặt cùng thư mục cha.
- **PASS** đối chiếu đủ **501 tệp JSONL**, **55.976 bản ghi**, chính xác **186 trường `vi` thêm mới**; mọi trường nguồn khác và bản dịch cũ giữ nguyên.
- Không lỗi mã kỹ thuật, Unicode NFC, CR/LF/tab, vượt số trang hoặc quá 34 ký tự thấy được/dòng; `DELTA-018.jsonl` lưu toàn bộ bản đối chiếu.
- **Giới hạn:** chưa kiểm thử bản ROM NDS, chưa kiểm tra pixel width theo font game. ZIP không chứa ROM thương mại.

## Mốc đợt 019

Tiếp tục `0024.001` và các tệp tiếp theo có thật trong thư mục `translation/04-thoai`, sau khi xác minh số dòng chưa dịch. Giữ xưng hô bạn bè **tớ–cậu**, nhất quán thuật ngữ **Bách Hóa Tổng Hợp** và **Điểm Hẹn Hò**. Mỗi đợt lưu bản ZIP đủ dữ liệu và cập nhật GitHub đúng thư mục game.