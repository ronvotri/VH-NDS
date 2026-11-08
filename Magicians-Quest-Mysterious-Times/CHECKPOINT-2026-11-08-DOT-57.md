# Magician’s Quest: Mysterious Times — Checkpoint 057

**Ngày:** 08/11/2026 · **Repo:** `ronvotri/VH-NDS` · `Magicians-Quest-Mysterious-Times/`

| Tệp | Trang mới | Nội dung |
|---|---:|---|
| `0040.011` | 120 | Tin đồn về hai người bạn, đi chơi cùng nhau, các hành động đáng ngờ, đối thoại biết/chưa biết tin |
| `0040.012` | 120 | Tin đồn tình yêu, pháo hoa, niềm tin, phép thuật, chuyện học và phản ứng giữ bí mật |

**Tiến độ:** **15.792/55.976 (28,21%)**, tăng 240 từ checkpoint 056 (15.552); hội thoại NPC **12.667/52.608**.

**Thành phẩm:** 2 JSONL có trường `vi`, 2 bảng `manual_0040_011.tsv` và `manual_0040_012.tsv`, `vi_0040_011.txt`, `vi_0040_012.txt`, `DELTA-057.jsonl`, `QA-057.md`, `build_057.py`, `qa_057.py`.

**QA:** Đối chiếu toàn bộ 501 JSONL/55.976 bản ghi với ZIP checkpoint 056, giữ 15.552 bản dịch cũ, chỉ bổ sung 240 trường `vi` mới; các trường `id/en/ctx` và token game không thay. Không thay hay gộp bản ghi lặp. Giới hạn tĩnh 34 ký tự/đoạn, tối đa 3 `▼`/trang.

**Chưa test trực tiếp trên ROM NDS**; cần kiểm width của tên/hành động động trong game. Tệp nguồn đợt 058: `0040.013` và `0040.014` đã giữ nguyên trong ZIP 057.
