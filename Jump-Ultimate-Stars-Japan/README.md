# Jump Ultimate Stars (Japan) — Việt hóa (AJUJ)

Checkpoint **001** — 18/11/2026. Dịch trực tiếp từ bản Nhật, **không chứa ROM**.

## Tiến độ thật
- Tổng dữ liệu nguồn: **34.919** chuỗi, chia 30 file JSONL.
- Đã dịch và lưu bằng ID: **316** chuỗi. Còn **34.603** chuỗi `vi=null`.
- Đợt 001: 126 dòng hướng dẫn, 75 dòng trợ giúp, 105 dòng luật/nhiệm vụ, 10 dòng Koma/kỹ năng.
- QA: công cụ `tools/check_translations.py` trong ZIP nguồn báo **0 lỗi** (kiểm tra cấu trúc/ID/thẻ điều khiển, không phải QA màn hình).

## Những gì đã lưu trên GitHub
- `BAN_DICH_001.jsonl`: **316 bản dịch** kèm `file`, `row_index`, `id`, `ja`, `vi` để đối chiếu nguồn, ghép vào 30 file gốc không mất ID.
- `THUAT_NGU.json`: thuật ngữ thống nhất.
- `XUNG_HO_NHAN_VAT.md`: quy tắc xưng hô, phần đã xác nhận và phần còn đề xuất.

**Lưu ý:** Kho này mới có **bản sai biệt 316 dòng**, chưa tải lên toàn bộ 30 file nguồn. ZIP bàn giao **JumpUltimateStars_VietHoa_Checkpoint_001.zip** ở cuộc chat chứa đủ 30 JSONL (`vi=null` cho phần còn lại) và báo cáo. Để tiếp tục, sử dụng ZIP bàn giao làm nền và đối chiếu ID trong `BAN_DICH_001.jsonl`.

## Quy tắc
Giữ tiếng Anh tên nhân vật/manga/Item/Skill, Koma, Deck, J-Soul, Dream Combo và ba thuộc tính **Strength / Knowledge / Laughter**. Việt hóa phần giải thích/hội thoại với giọng tự nhiên, hài vừa đủ, không sai chất manga. Giữ chính xác mọi `<B0A>`, `<IDEOSP>`, `<PERCENT_FULL>`, byte điều khiển và biến.

**Chưa hỗ trợ font Việt, ghi lại ROM và QA gameplay; đây chưa phải patch NDS có thể chơi.**
