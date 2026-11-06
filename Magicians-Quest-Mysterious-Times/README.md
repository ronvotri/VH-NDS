# Magician's Quest: Mysterious Times — Việt hóa Nintendo DS

Dự án Việt hóa **Magician's Quest: Mysterious Times** (NDS / bản Mỹ) trong [VH-NDS](https://github.com/ronvotri/VH-NDS). Dữ liệu nằm trong thư mục riêng để không lẫn với **Ni no Kuni** và **Pokémon Dash**.

## Trạng thái ngày 06/11/2026 — Checkpoint 003

| Nhóm | Đã điền tiếng Việt | Tổng |
|---|---:|---:|
| Mở đầu | 106 | 106 |
| Hệ thống | 1.086 | 1.087 |
| Vật phẩm | 390 | 1.501 |
| Sổ tay | **432** | **432** |
| Hội thoại NPC | 0 | 52.608 |
| Credit | 0 | 242 |
| **Tổng** | **2.014** | **55.976** |

**Đợt 003:** +723 trường `vi` mới, biên tập lại 12 câu nhận xét tính cách. Số này bao gồm cả tên riêng/nhãn giữ nguyên nguồn sau khi rà duyệt, **không phải** số câu Việt hóa hoàn toàn đã test trong ROM.

### Văn phong được người dùng duyệt
> **Em mê tụ tập, quẩy banh nóc với bạn bè!**

Phong cách ngộ nghĩnh, lém lỉnh, thân thiện Gen Z nhưng không nói lóng vô tội vạ. **Ngôi xưng là luật:** người dẫn chuyện `ta–em`, giáo viên `thầy/cô–em`, bạn bè `tớ–cậu` khi đã biết quan hệ; menu/thông báo hệ thống viết trung tính.

## Tệp quan trọng
- [CHECKPOINT-2026-11-06-DOT-03.md](CHECKPOINT-2026-11-06-DOT-03.md) — tiến độ, hướng dẫn nối phiên.
- [QUY_UOC_DICH_VI.md](QUY_UOC_DICH_VI.md) — phong cách, ngôi xưng, yêu cầu kỹ thuật.
- [translation/THUAT_NGU-003.tsv](translation/THUAT_NGU-003.tsv) — 429 thuật ngữ sinh vật/vật phẩm duyệt ở đợt 003.
- `translation/00-mo-dau/` — lời mở đầu, kể cả 12 dòng sửa lần này.
- `translation/02-vat-pham/` — các trang tên vật phẩm 001–003 đã dịch (các trang còn lại chưa dịch).
- `translation/03-so-tay/` — đầy đủ 432 mục.
- [DELTA-003.jsonl](DELTA-003.jsonl) — 735 bản ghi thay đổi so với checkpoint 002 (723 mới + 12 sửa).
- [mq_translate_003.py](mq_translate_003.py), [mq_items_003.py](mq_items_003.py) — mã nguồn bảng dịch đợt 003, tái dựng được trên checkpoint 002.
- [qa_checkpoint.py](qa_checkpoint.py), [BAN_GIAO.md](BAN_GIAO.md) — QA và hướng dẫn build NDS.

**QA:** tái dựng từ checkpoint 002 cho kết quả trùng 100% các tệp JSONL; 0 lỗi mã điều khiển/NFC/giới hạn byte; sổ tay tối đa 3 dòng/150px (ước lượng font, không thay kiểm thử ROM). **Chưa có ROM build** vì chưa cung cấp ROM USA sạch; repo không lưu ROM thương mại.

### Dịch tiếp
Tiếp từ `translation/02-vat-pham/item__ItemName_e.ofs.004.jsonl` (quần áo, trang phục), sau đó rà NPC theo `ctx` để khóa ngôi xưng và tái sử dụng các thuật ngữ thống nhất. Mỗi đợt phải cập nhật checkpoint và GitHub.