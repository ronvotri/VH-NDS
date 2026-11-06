# Magician’s Quest: Mysterious Times — Việt hóa Nintendo DS

Dự án Việt hóa tiếng Việt bản NDS USA thuộc kho [VH-NDS](https://github.com/ronvotri/VH-NDS). Giữ riêng trong `Magicians-Quest-Mysterious-Times/`, không lẫn với Ni no Kuni hoặc Pokémon Dash.

## Tiến độ mới nhất · Checkpoint 010 (06/11/2026)

**4.930 / 55.976 mục (8,81%)**, trong đó hội thoại đạt **1.805/52.608** mục.

| Nhóm | Đã xử lý | Tổng |
|---|---:|---:|
| Mở đầu | 106 | 106 |
| Hệ thống | 1.086 | 1.087 |
| Vật phẩm | 1.501 | 1.501 |
| Sổ tay | 432 | 432 |
| Hội thoại | 1.805 | 52.608 |
| Credit | 0 | 242 |

Đợt 010 xử lý **240 trang thoại** thuộc `0020.003` và `0020.004`. Giọng văn dí dỏm Gen Z nhưng không lạm dụng meme; tên riêng, ngôi xưng và lựa chọn tình cảm được xử lý dựa trên `ctx`.

## Tài liệu và kỹ thuật

- [CHECKPOINT-2026-11-06-DOT-10.md](CHECKPOINT-2026-11-06-DOT-10.md): mốc, nội dung và cách nối phiên.
- [QUY_UOC_DICH_VI.md](QUY_UOC_DICH_VI.md): quy tắc giọng văn/ngôi xưng.
- [QA-010.md](QA-010.md), [qa_010.py](qa_010.py): so sánh 501 JSONL, bất biến mọi trường ngoài `vi`.
- [DELTA-010.jsonl](DELTA-010.jsonl): 240 ID + EN/VI + ctx.
- [manual_0020_003.txt](manual_0020_003.txt), [manual_0020_004.txt](manual_0020_004.txt), [apply_010.py](apply_010.py): dịch tay và công cụ áp bản dịch.
- `translation/04-thoai/`: hội thoại dịch đã cập nhật.

**Giới hạn:** Không sửa ID/EN/ctx, mã `$...;` và thứ tự; không đưa ROM thương mại lên repo. Chưa QA in-game; đã QA dữ liệu / token / số ký tự.

**Bước sau:** hoàn tất `0020.005` (87 trang), rồi chuyển các cụm thoại tiếp theo dựa trên tệp có thật.