# Magician's Quest: Mysterious Times — Việt hóa Nintendo DS

Dự án Việt hóa **Magician's Quest: Mysterious Times** (NDS / bản Mỹ), lưu riêng trong [VH-NDS](https://github.com/ronvotri/VH-NDS) để không lẫn với Ni no Kuni hoặc Pokémon Dash.

## Trạng thái ngày 06/11/2026 — Checkpoint 002
- **Đã điền 1.291/55.976 mục `vi`** (đợt 02 mới dịch thêm 636 mục). Số này bao gồm chuỗi giữ nguyên tên riêng sau khi duyệt, không có nghĩa 1.291 câu tiếng Anh đều đã đổi sang tiếng Việt.
- **00 · Mở đầu:** 106/106, giữ bản đã thử trong game.
- **01 · Hệ thống:** 1.086/1.087, còn 1 chuỗi ký tự tiếng Nhật dự phòng chưa dịch.
- **02 · Vật phẩm:** 30/1.501.
- **03 · Sổ tay:** 69/432.
- **04 · Hội thoại:** 0/52.608.
- **05 · Credit:** 0/242.

## Dữ liệu trong repo
- `translation/01-he-thong/`: 5 tệp JSONL vừa dịch, mã kết nối, bạn bè, chuyển trường, trang phục và niệm chú.
- `translation/03-so-tay/`: 4 tệp JSONL danh mục bài học và phép thuật.
- [CHECKPOINT-2026-11-06-DOT-02.md](CHECKPOINT-2026-11-06-DOT-02.md): tiến độ, kiểm tra và cách nối phiên.
- [QUY_UOC_DICH_VI.md](QUY_UOC_DICH_VI.md): khóa ngôi xưng và phong cách.
- [BATCH_02_MAP.tsv](BATCH_02_MAP.tsv): 493 cặp dịch EN → VI (có thêm 3 mẫu đặc biệt cho bản rà).
- [DOT-02-DELTA.bz2.b64](DOT-02-DELTA.bz2.b64) + [apply_delta_02.py](apply_delta_02.py): phục dựng 9 tệp đã dịch từ ZIP checkpoint 001; đối chiếu SHA256 từng tệp.
- [qa_checkpoint.py](qa_checkpoint.py), [translation/GLOSSARY.tsv](translation/GLOSSARY.tsv), [translation/INDEX.tsv](translation/INDEX.tsv): công cụ QA, thuật ngữ và chỉ mục bản gốc.
- `BAN_GIAO.md`: hướng dẫn, kỹ thuật vá ROM.

## Luật dịch
- Vui nhộn, tinh nghịch, gần gũi Gen Z, không nhồi meme.
- Người dẫn chuyện lớn tuổi **ta–em**; giáo viên **thầy/cô–em**; bạn bè **tớ–cậu**; thông báo hệ thống trung tính.
- Chỉ thay `vi`, không sửa ID/EN/ctx/mã điều khiển/thứ tự/giới hạn byte.
- Chỉ dùng ROM sạch bản Mỹ hợp pháp để build. Không đăng ROM thương mại trên GitHub.

## Việc tiếp theo
Dịch nốt 363 chuỗi sổ tay, sau đó 1.471 tên vật phẩm chưa dịch. Hội thoại NPC phải xem `ctx`, khóa quan hệ nhân vật trước khi lựa chọn ngôi xưng. Mỗi đợt lưu checkpoint mới và cập nhật cùng thư mục này.