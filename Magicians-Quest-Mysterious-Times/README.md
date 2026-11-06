# Magician’s Quest: Mysterious Times — Việt hóa Nintendo DS

Dự án Việt hóa tiếng Việt bản NDS USA thuộc kho [VH-NDS](https://github.com/ronvotri/VH-NDS). Giữ riêng dưới `Magicians-Quest-Mysterious-Times/`, không lẫn với Ni no Kuni hoặc Pokémon Dash.

## Tiến độ mới nhất · Checkpoint 009 (06/11/2026)

**4.690 / 55.976 mục (8,38%)**, trong đó hội thoại đạt **1.565/52.608** mục.

| Nhóm | Đã xử lý | Tổng |
|---|---:|---:|
| Mở đầu | 106 | 106 |
| Hệ thống | 1.086 | 1.087 |
| Vật phẩm | 1.501 | 1.501 |
| Sổ tay | 432 | 432 |
| Hội thoại | 1.565 | 52.608 |
| Credit | 0 | 242 |

Đợt 009 xử lý **240 trang thoại** thuộc `0020.001` và `0020.002`. Không có các nhóm `0013`–`0015` trong file bàn giao (nhảy từ `0012` sang `0020`).

## Tài liệu và kỹ thuật

- [CHECKPOINT-2026-11-06-DOT-09.md](CHECKPOINT-2026-11-06-DOT-09.md): kết quả, thống kê và hướng dẫn nối phiên.
- [QUY_UOC_DICH_VI.md](QUY_UOC_DICH_VI.md): giọng vui nhộn Gen Z, khóa ngôi xưng theo quan hệ nhân vật.
- [QA-009.md](QA-009.md), [qa_009.py](qa_009.py): kiểm tra 501 JSONL và chỉ thay `vi`.
- [DELTA-009.jsonl](DELTA-009.jsonl): ID, EN, VI, ctx của 240 mục mới.
- [manual_0020_001.txt](manual_0020_001.txt), [manual_0020_002.txt](manual_0020_002.txt), [apply_009.py](apply_009.py): nguồn dịch tay và công cụ áp bản dịch.
- `translation/04-thoai/`: chứa tất cả hội thoại đã cập nhật.

**Luật bắt buộc:** không sửa `id`, `en`, `ctx`, mã `$...;`, thứ tự dòng; giữ `▼` và hạn chế độ dài pixel màn hình NDS. Không đăng ROM thương mại lên GitHub. Bản hiện tại chưa được kiểm thử in-game.

**Bước sau:** nhóm `0020.003` trở đi, đồng bộ checkpoint 010 vào đúng thư mục này.