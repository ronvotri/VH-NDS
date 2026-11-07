# Magician’s Quest: Mysterious Times — Checkpoint 051

**Ngày:** 08/11/2026  
**Repo:** `ronvotri/VH-NDS` → `Magicians-Quest-Mysterious-Times/`  
**Mốc trước:** checkpoint 050 — 14.149/55.976  
**Mốc mới:** **14.352/55.976 (25.64%)**, tăng **203** bản dịch; NPC **11.227/52.608**.

## Nội dung đợt 051

| Tệp nguồn JSONL | Số trang mới | Mô tả |
|---|---:|---|
| `translation/04-thoai/talkfigs__0eng__data__0033.020.jsonl` | 120 | Cô bé bán diêm, Kraken tìm nhẫn đính hôn bị thuyền trưởng Dot lấy mất, Kappa tò mò về trường học và kết bạn |
| `translation/04-thoai/talkfigs__0eng__data__0033.021.jsonl` | 83 | Kappa khám phá trường, câu đố ba gã áo vàng/xanh/đỏ: một nói thật, hai nói dối, chỉ được hỏi **một người, một lần** về kho báu |
| **Tổng** | **203** | |

## Bàn giao

- `vi_0033_020_raw.txt`, `vi_0033_021_raw.txt`: bản dịch tay, mỗi dòng ứng với một trang của tệp gốc; placeholder `¤` giữ chỗ mã nhúng theo thứ tự.
- `vi_0033_020.txt`, `vi_0033_021.txt`: bản dịch hoàn thiện với mã game và ký tự `▼` để ngắt dòng.
- `manual_0033_020.tsv`, `manual_0033_021.tsv`: bản song ngữ EN–VI theo đúng ID, kèm `ctx`.
- `apply_051.py`: áp bản dịch mới trên nguồn gốc chưa điền `vi`; `qa_051.py`: so sánh đủ bộ với ZIP 050.
- `DELTA-051.jsonl`: log chính xác 203 trường mới; `QA-051.md`: báo cáo kiểm tra.

**QA PASS:** 501 tệp JSONL, 55.976 bản ghi, giữ nguyên 14.149 bản dịch cũ; không đổi nguồn tiếng Anh, ID, context hay token. **Chưa test trên ROM NDS thực tế.** ZIP không chứa ROM.

**Đợt 052:** `talkfigs__0eng__data__0040.001.jsonl` (120 trang) và `talkfigs__0eng__data__0040.002.jsonl` (120 trang). Nguồn gốc của cả hai đã có trong ZIP 051 và sẽ được đưa lên GitHub dưới dạng `vi: null`.