# Magician’s Quest: Mysterious Times — Checkpoint 055

**Ngày:** 08/11/2026  
**Repository:** `ronvotri/VH-NDS` · `Magicians-Quest-Mysterious-Times/`.

**Mốc cũ:** 15.072/55.976 (26,93%) · NPC 11.947/52.608.  
**Mốc mới:** **15.312/55.976 (27.35%)**, +240 trang · NPC **12.187/52.608**.

## Phần đã dịch

- `translation/04-thoai/talkfigs__0eng__data__0040.007.jsonl` — 120 trang về tin đồn, chuyện hẹn hò, bạn bè cùng làm phép/câu cá/chơi nhạc; NPC tự phụ về phong cách lịch lãm nhưng tốt bụng.
- `translation/04-thoai/talkfigs__0eng__data__0040.008.jsonl` — 120 trang về đồn đoán, kiểm chứng tin đồn, lời hỏi đáp đúng/sai, phản ứng và lời đề nghị giúp đỡ.

Đầy đủ bảng EN–VI: `manual_0040_007.tsv`, `manual_0040_008.tsv`. Các câu lặp giữ nguyên từng ID. Nhật ký chính xác 240 bản ghi: `DELTA-055.jsonl`. Kiểm tra: `QA-055.md`.

**QA:** kiểm tra tĩnh từng bản ghi trên hai nguồn GitHub trước đợt 055: đúng 240 thay đổi `vi:null → bản dịch`, bảo toàn chuỗi mã động theo giá trị/thứ tự, tối đa 34 ký tự tĩnh mỗi dòng và 3 dấu `▼` mỗi trang. Chưa kiểm thử ROM NDS; chưa so sánh byte-to-byte toàn bộ 501 tệp vì bản ZIP checkpoint 054 không khả dụng trong môi trường hiện tại.

**Tiếp theo:** rà hai tệp `0040.009` và `0040.010` nếu đã có trong ZIP nguồn; đối chiếu bản gốc trước khi dịch. Không trộn dữ liệu với các game NDS khác.
