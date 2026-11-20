# Jump Ultimate Stars (Japan) — Checkpoint 053 🇻🇳

**Ngày:** 20/11/2026. **Nhánh:** `vh/jump-ultimate-stars-japan`; thư mục `Jump-Ultimate-Stars-Japan/`.

## Lô đã dịch

- **507 dòng Nhật–Việt mới**, từ `00-he-thong-ten-goi-001.jsonl` `row_index` **240–746** (liền mạch).
- Nội dung theo tài nguyên: `bin/commwin.bin` **92 dòng** (DS, Wi-Fi, Friend Code, Deck); `bin/demo.bin` **60 dòng** (tựa manga/cảnh); `bin/infoname.bin` **42 dòng** (nhân vật); `bin/location.bin` **90 dòng** (địa danh); `bin/piece.bin` **223 dòng** (phần giới thiệu manga).
- Phần giới thiệu đã đi trọn nhóm **Eyeshield 21, I's, Ichigo 100%, Katekyo Hitman Reborn!, Captain Tsubasa, Gintama, Kinnikuman, Kochikame, Cobra, Otokojuku, Hell Teacher Nube**. Tên manga, tên nhân vật, Deck/Koma/J-Power và Skill giữ English/romanized theo bảng từ vựng.
- Phân biệt **Ichitaka Seto** (*I's*) với **Itsuki Akiba**; chuẩn hóa **Su Pu Shang** theo `THUAT_NGU.json`.

## Tiến độ

| Chỉ số | ID |
| --- | ---: |
| Trước CP053 | 33.680 |
| Mới CP053 | **507** |
| Đã dịch | **34.187 / 34.919 (97,90%)** |
| Chưa dịch | **732** |

**Hai dải còn lại:** `00-he-thong-ten-goi-001.jsonl` `row_index` 747–1230 (**484 dòng**), và `00-he-thong-ten-goi-002.jsonl` 0–247 (**248 dòng**). `NGUON_CHUA_DICH_SAU_053.jsonl` giữ chính xác ID, Nhật và metadata, `vi=null`.

## QA

- Nguồn: ZIP Nhật gốc `JumpUltimateStars_Japan_BanGiao_Cloud.zip`, SHA256 `14e839a35e75f35534a93a1b37ebe42731ea530fbc012267b45bbbed8446f241`, **30 tệp/34.919 ID**.
- **507/507 ID** duy nhất; khớp `id`, `ja`, `file`, `row_index`, `context` với nguồn; không ghi đè bản dịch cũ.
- **Giữ đủ token điều khiển**, Unicode NFC; không chuỗi trống.
- **10 sửa lỗi CP050A** vẫn hiện diện trong bản gộp `BAN_DICH_TONG_HOP_038-053.jsonl` (**10.591 ID**).
- Phần hệ thống của CP053 **không có** `source_fixed_field_bytes` trong JSONL. Vì vậy không thể xác nhận giới hạn byte thực tế, độ rộng pixel hay font NDS bằng QA tĩnh. Các tên phiên âm hiếm cần đọc soát thêm trước khi phát hành.
- **Chưa thử ROM NDS**, chưa chèn font, chưa vá ROM. Không khẳng định tương thích gameplay.

## Tệp bàn giao

- `BAN_DICH_053.jsonl` — 507 bản dịch, giữ nguyên metadata.
- `BAN_DICH_053.tsv` — bảng Nhật/Việt để duyệt.
- `BAN_DICH_TONG_HOP_038-053.jsonl` — bản gộp CP038–053, gồm đính chính CP050A. Không bao gồm CP001–037.
- `NGUON_CHUA_DICH_SAU_053.jsonl` — chính xác 732 chuỗi chưa dịch.
- `QA_053.json` — đối chiếu nguồn/ID/token và SHA256.
- `TAO_TONG_HOP_053.py` — script dựng full CP001–053 **từ các delta và đính chính trên GitHub** (khi có đủ tệp), tránh đếm trùng overlay.
- `build_cp053.py`, `dich_*.tsv` — nguyên liệu/reproducibility dùng ZIP gốc và bàn giao CP052. Không phải ROM patch.

## Điểm nối CP054

Tiếp `00-he-thong-ten-goi-001.jsonl` ở **dòng 747** (giới thiệu *Shaman King*), giữ nguyên mạch câu khi chuyển giữa nhiều ID. Sau hết 1230, xử lý 248 dòng cuối tệp 002. Tránh dịch rời một nửa đoạn manga; xưng hô của phần mô tả giữ giọng người kể trung tính.
