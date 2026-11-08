# Magician’s Quest: Mysterious Times — Checkpoint 060

**Ngày:** 08/11/2026 · **Repo:** `ronvotri/VH-NDS` · `Magicians-Quest-Mysterious-Times/`

| Tệp | Trang mới | Nội dung |
|---|---:|---|
| `0040.017` | 120 | Nessie, sinh vật dưới sông, Candyman, nhà ma, cây trắng, kỳ lân, Nhân sư, kho báu, rồng, người Sao Hỏa |
| `0040.018` | 120 | Người ngoài hành tinh, rác thải, người sói, Thom, tượng đá, Krampus, Minotaur, chuông trường, ma quậy phòng, quỷ thách đấu |

**Tiến độ:** **16.512/55.976 (29,50%)**, tăng 240 từ checkpoint 059 (16.272); hội thoại NPC **13.387/52.608**.

**Thành phẩm:** 2 JSONL dịch, 2 `manual_0040_*.tsv` EN–VI, 2 `vi_0040_*.txt`, `DELTA-060.jsonl`, `QA-060.md`, `build_060.py` và `qa_060.py`.

**QA:** so sánh toàn bộ 501 JSONL / 55.976 bản ghi giữa ZIP 059 và 060. Chỉ 240 trường `vi` đổi từ `null` sang tiếng Việt trong `0040.017` và `0040.018`. Giữ 16.272 bản dịch cũ, không đổi `id`, `en`, `ctx` hoặc byte dữ liệu của các JSONL còn lại. Tất cả mã `$...;` giữ đúng thứ tự; Unicode NFC, ≤3 `▼`, và ≤34 ký tự tĩnh mỗi đoạn.

**Chưa kiểm thử trên ROM NDS.** Các biến tên động cần kiểm tra khi hiển thị trong trò chơi. **Đợt 061 tiếp theo:** `0040.019` + `0040.020` có trong ZIP 060, chưa dịch.
