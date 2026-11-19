# Jump Ultimate Stars (Japan) — Checkpoint 044 🇻🇳

**Tiến độ: 28.497 / 34.919 (81,61%)** — mới dịch thêm **698 ID**, còn **6.422 ID**.

## Mới nhất: Checkpoint 044 — 19/11/2026

- Nguồn gốc: `JumpUltimateStars_Japan_BanGiao_Cloud.zip` → `translation/06-jquiz-007.jsonl`.
- Đã dịch **row_index 325–1022** (**698 ID**), gồm 620 mục *One Piece* và 78 mục *Pyu to Fuku! Jaguar*.
- *One Piece*: Baratie, Arlong Park, Alabasta, Skypiea, Water Seven, Enies Lobby. Kết thúc phần One Piece ở row_index 944.
- *Pyu to Fuku! Jaguar*: 945–1022, kết thúc toàn bộ câu hỏi 2240 (đủ phương án).
- **Checkpoint 045 tiếp tục tại `06-jquiz-007.jsonl`, row_index 1023**, bắt đầu câu hỏi 2241 về nghề của cha Piyohiko.
- [BAN_DICH_044.jsonl](BAN_DICH_044.jsonl) — 698 bản ghi Nhật–Việt mới, giữ ID và metadata gốc.
- [QA_044.json](QA_044.json) — QA tĩnh đối chiếu ZIP nguồn, vai trò đáp án, SHA256, số ký tự.
- [BAN_GIAO_044.md](BAN_GIAO_044.md) — bàn giao và hướng dẫn phục hồi.
- [BAN_DICH_TONG_HOP_038-044.jsonl](BAN_DICH_TONG_HOP_038-044.jsonl) — **gộp riêng CP038–044, 4.901 ID**, không bao gồm CP001–037.

## Phục hồi đủ tiến độ

1. Khôi phục CP001–037 (**23.596 ID**) theo [PHUC_HOI_TONG_HOP_037.md](PHUC_HOI_TONG_HOP_037.md).
2. Nối CP038–044 (**4.901 ID**) theo ID, từ chối trùng ID → **28.497 ID**.
3. Áp bản sửa [BAN_DINH_CHINH_037B.jsonl](BAN_DINH_CHINH_037B.jsonl) và [BAN_DINH_CHINH_037C.jsonl](BAN_DINH_CHINH_037C.jsonl) bằng **ghi đè trường `vi` theo ID**, không thêm ID.
4. Giữ thuật ngữ nhất quán theo [THUAT_NGU.json](THUAT_NGU.json), ngôi xưng theo [XUNG_HO_NHAN_VAT.md](XUNG_HO_NHAN_VAT.md).

## QA và giới hạn

- **698/698** bản ghi có ID duy nhất, không trùng các checkpoint mới trước đó; nguyên văn tiếng Nhật, `group`, `context`, `uses` và `quiz_context` giữ nguyên theo ZIP.
- Không thay đổi thẻ điều khiển hoặc thứ tự đáp án. Không tự thêm đáp án bị thiếu do nguồn dùng chung chuỗi.
- Bản Việt không vượt **37 ký tự Unicode/dòng**; đây **không phải QA độ rộng font theo pixel**.
- Giữ Hán tự ở **14 dòng** để tránh mất phân biệt phương án/ tên riêng. Cần QA lại tên riêng trước khi ghép ROM.
- **Chưa kiểm thử đáp án đúng, độ rộng pixel, font Việt, ROM NDS hay gameplay.** Đây là dữ liệu bản dịch, chưa phải bản vá ROM đã chơi được.

Repository: `ronvotri/VH-NDS`, nhánh `vh/jump-ultimate-stars-japan`, thư mục `Jump-Ultimate-Stars-Japan/`.
