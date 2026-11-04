# Tiến độ Việt hóa — Ni no Kuni (Nintendo DS)

Cập nhật: **04/11/2026**. Nguồn: gói chữ `Goi_dich_NiNoKuni.zip`. Chỉ cập nhật những câu đã thực sự dịch và kiểm tra.

| Đợt | Tệp | Số mục hợp lệ | Vướng mắc | Trạng thái |
|---|---|---:|---|---|
| 01 | `translations/dot_01/BAN_DICH_GUI_LAI.jsonl` | 954 | — | Kiểm tra kỹ thuật đạt |
| 02 | `translations/dot_02/hoi_thoai_003.jsonl` | 176 | 4 nguồn nghi lỗi, hoãn | Kiểm tra kỹ thuật đạt |
| 03 | `translations/dot_03/hoi_thoai_004.jsonl` | 180 | — | Kiểm tra kỹ thuật đạt |
| **Tổng** | | **1.310** | **4 nguồn hoãn** | Chưa nhập ROM |

**Mục ưu tiên trong gói nguồn: 17.935. Đã dịch: 1.310 (7,3%). Còn chưa dịch: 16.625.**

## Phạm vi từng đợt

- **Đợt 01:** `hoi_thoai_001` (180), `hoi_thoai_002` (180), `dia_danh_001` (30), `huong_dan_chien_dau_001` (139), `nhiem_vu_phu_001` (180), `lua_chon_thong_bao_002` (180), `noi_dung_bo_sung_001` (65).
- **Đợt 02:** `hoi_thoai_003` (176). Hoãn vị trí 123–126: `D`, `U`, `愈`, `!+f ﾆ`. Không suy đoán thành câu có nghĩa.
- **Đợt 03:** `hoi_thoai_004` (180), đoạn Babanacia, hội thoại NPC và sự kiện về Kiềm Chế/Niềm Tin.

### ID nguồn đang hoãn

- `HOI_dd913e6676a5f6` — `D`
- `HOI_eef7e40c981caa` — `U`
- `HOI_b715c8861e9918` — `愈`
- `HOI_7ecf274c3ca2db` — `!+f ﾆ`

## Luật để không sót, trùng hoặc lệch giọng

1. Mỗi `id` phải duy nhất trên toàn bộ các tệp dịch; **không nhập cùng lúc bản gộp và tệp riêng**.
2. Bản dịch phải giữ nguyên các mã trong nguồn như `{3:4}`, `{1:2}`, `<CTRL:01>`, `%s` và `[1000]`.
3. Tên riêng giữ theo bản DS. Oliver nói chân thành, tớ/cậu với bạn bè, con/mẹ và cháu/cô/chú với người lớn. Shizuku lanh lẹ, lém lỉnh nhưng không thô tục. NPC có ngữ cảnh riêng.
4. Xem `THUAT_NGU.md` trước khi dịch batch tiếp theo.
5. Chỉ ghi "đã dịch" cho file thực tế có trên repo và đã kiểm tra, không lấy số liệu từ nháp hoặc lời hứa.

**Chưa kiểm thử:** chất lượng bản dịch theo toàn tuyến truyện; font tiếng Việt; độ rộng ô thoại NDS; nhúng lại kịch bản, sửa offset/nhảy lệnh; chạy trong game thật. Các bước kiểm tra hiện tại chỉ xác minh ID/JSON/mã điều khiển.
