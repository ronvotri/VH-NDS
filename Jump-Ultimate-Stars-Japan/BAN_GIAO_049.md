# Jump Ultimate Stars — Checkpoint 049 🇻🇳

Ngày 20/11/2026. **705 chuỗi Nhật–Việt mới**; tổng **32.011 / 34.919 (91,67%)**; còn **2.908 chuỗi**.

## Phạm vi và nguồn

- Nguồn gốc: `JumpUltimateStars_Japan_BanGiao_Cloud.zip`; SHA256 đã kiểm tra cho cả hai file J-Quiz.
- `06-jquiz-008.jsonl`: dòng **1923–2011**, **89 ID** — kết thúc file 008.
- `06-jquiz-009.jsonl`: dòng **0–615**, **616 ID** — nối giữa câu hỏi *10-Year Bazooka* và đi qua *Katekyo Hitman Reborn!*, *Taizō Mote King Saga*, đến đầu *Yu Yu Hakusho*.
- Manga code: 4 (*Reborn!*) **409**, 17 (*Taizō Mote King Saga*) **273**, 38 (*Yu Yu Hakusho*) **23**.
- QA đối chiếu từng `id`/`ja`/`quiz_context` với `reference/quiz-questions.jsonl` (3.006 câu hỏi).
- **CP050 tiếp từ `06-jquiz-009.jsonl`, `row_index=616`**, `question_index=2884` (*Yu Yu Hakusho*).

## Các tệp

- `BAN_DICH_049.jsonl`: đúng 705 ID nguồn, chỉ thêm trường `vi`.
- `BAN_DICH_049.tsv`: đối chiếu song ngữ kèm vị trí câu hỏi và đáp án.
- `BAN_DICH_TONG_HOP_038-049.jsonl`: **8.415 ID** của CP038–049 (không bao gồm CP001–037). Đã giữ sửa **Shunrei** từ CP046A.
- `QA_049.json`: SHA, kiểm kỹ thuật và các câu hỏi cần rà thủ công.

## Hạn chế QA

- Dòng Việt dài nhất **37 ký tự Unicode** (giới hạn 37); dữ liệu gốc không đổi mã điều khiển.
- Kiểm không trùng ID với CP038–048, không sai vị trí hỏi/đáp; không tự sửa JA.
- Tên riêng, chữ chơi chữ trong *Taizō Mote King Saga* và tên vũ khí ở *Yu Yu Hakusho* chưa hoàn tất đối chiếu tên Anh chính thức; xem `QA_049.json`.
- **Chưa xác minh đáp án đúng/sai, hiển thị ảnh trong quiz, font pixel, ROM patch hay gameplay NDS.** QA tĩnh không đồng nghĩa phát hành bản chơi được.

## Phục hồi tất cả bản dịch

1. Khôi phục CP001–037 từ `PHUC_HOI_TONG_HOP_037.md`: **23.596 ID**.
2. Ghép `BAN_DICH_TONG_HOP_038-049.jsonl`: **8.415 ID** theo ID, từ chối trùng. Tổng = **32.011 ID**.
3. Áp bản sửa QA 037B/037C bằng ghi đè trường `vi` theo ID. **Không cộng thêm ID**.
4. Không áp CP046A như bản mới: tên Shunrei **đã sửa trong bản gộp 038–049**.
