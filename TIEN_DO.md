# Tiến độ Việt hóa — Ni no Kuni (Nintendo DS)

Cập nhật: **04/11/2026**. Nguồn: gói chữ `Goi_dich_NiNoKuni.zip`. Chỉ cập nhật những câu đã thực sự dịch và kiểm tra.

| Đợt | Tệp | Số mục hợp lệ | Vướng mắc | Trạng thái |
|---|---|---:|---|---|
| 01 | `translations/dot_01/BAN_DICH_GUI_LAI.jsonl` | 954 | — | Kiểm tra kỹ thuật đạt |
| 02 | `translations/dot_02/hoi_thoai_003.jsonl` | 176 | 4 nguồn nghi lỗi, hoãn | Kiểm tra kỹ thuật đạt |
| 03 | `translations/dot_03/hoi_thoai_004.jsonl` | 180 | — | Kiểm tra kỹ thuật đạt |
| 04 | `translations/dot_04/hoi_thoai_005.jsonl` | 180 | — | Kiểm tra kỹ thuật đạt |
| 05 | `translations/dot_05/hoi_thoai_006.jsonl` | 180 | — | Kiểm tra kỹ thuật đạt |
| 06 | `translations/dot_06/hoi_thoai_007.jsonl` | 180 | — | Kiểm tra kỹ thuật đạt |
| 07 | `translations/dot_07/hoi_thoai_008.jsonl` | 180 | 1 nhãn NPC nghi nội bộ, cần kiểm tra | Kiểm tra kỹ thuật đạt |
| 08 | `translations/dot_08/hoi_thoai_009.jsonl` | 180 | — | Kiểm tra kỹ thuật đạt |
| 09 | `translations/dot_09/hoi_thoai_010.jsonl` | 180 | — | Kiểm tra kỹ thuật đạt |
| 10 | `translations/dot_10/hoi_thoai_011.jsonl` | 180 | — | Kiểm tra kỹ thuật đạt |
| 11 | `translations/dot_11/hoi_thoai_012.jsonl` | 180 | 3 thuật ngữ UI cần kiểm tra | Kiểm tra kỹ thuật đạt |
| **Tổng** | | **2.750** | **4 nguồn hoãn, 1 nhãn và 3 thuật ngữ cần rà** | Chưa nhập ROM |

**Mục ưu tiên trong gói nguồn: 17.935. Đã dịch: 2.750 (15,3%). Còn chưa dịch: 15.185.**

## Phạm vi từng đợt

- **Đợt 01:** `hoi_thoai_001` (180), `hoi_thoai_002` (180), `dia_danh_001` (30), `huong_dan_chien_dau_001` (139), `nhiem_vu_phu_001` (180), `lua_chon_thong_bao_002` (180), `noi_dung_bo_sung_001` (65).
- **Đợt 02:** `hoi_thoai_003` (176). Hoãn vị trí 123–126: `D`, `U`, `愈`, `!+f ﾆ`. Không suy đoán thành câu có nghĩa.
- **Đợt 03:** `hoi_thoai_004` (180), đoạn Babanacia, hội thoại NPC và sự kiện về Kiềm Chế/Niềm Tin.
- **Đợt 04:** `hoi_thoai_005` (180), NPC, họa sĩ, hôn nhân, ước mơ làm bác sĩ.
- **Đợt 05:** `hoi_thoai_006` (180), Mirant, chữ Astram trang 124, Nhẫn Qi, Đại sứ Du lịch, tình mẹ và sách ẩm thực.
- **Đợt 06:** `hoi_thoai_007` (180), nhiệm vụ Nghêu Bổ Dưỡng, người lính mất Can Đảm, Mary–Suren, Sáo Clarion, núi Dekarock và hai phép Thánh Tiễn/Xung Ba.
- **Đợt 07:** `hoi_thoai_008` (180), Ichi no Kuni, Nữ hoàng Cowla, Đài phun Sữa và phép Gia Vị Bí Mật, cô giáo thiếu Nhân Ái, Roy–Sophia thiếu Tình Yêu. Dùng tên **Sophia** thống nhất dù nguồn có một chỗ ghi Sofia.
- **Đợt 08:** `hoi_thoai_009` (180), Roy–Sophia đoàn tụ; Kiềm Chế và Tự Tin; ông Nellory, Sea Naiad, hai nhánh tiến hóa Teeny Bopper. Đã kiểm tra bằng công cụ nguồn `KIEM_TRA_BAN_DICH.py`.

- **Đợt 09:** `hoi_thoai_010` (180), Nellory nghiên cứu Imagen và Moya/Papa Sasquash; kẹo caramen sữa Babanacia; Kiềm Chế; người gửi quà cho pháp sư chống Jabou. Đã kiểm tra bằng `KIEM_TRA_BAN_DICH.py`.

- **Đợt 10:** `hoi_thoai_011` (180), Nữ hoàng Cowla và ông Kuran, Mảnh Tim Kiềm Chế, Imagen mắc chứng Nhớ Nhung, Alec và quái biển Blubber Bubbler. Đã kiểm tra bằng `KIEM_TRA_BAN_DICH.py`.

- **Đợt 11:** `hoi_thoai_012` (180), trả Mề Đay Bạc, thần nồi Al-Khemie, ghép Si-rô Vui Vẻ, Trứng Du Hành và luật đồ bơi tại Bikini. Đã chạy công cụ kiểm tra nguồn `KIEM_TRA_BAN_DICH.py`.

### ID nguồn đang hoãn

- `HOI_dd913e6676a5f6` — `D`
- `HOI_eef7e40c981caa` — `U`
- `HOI_b715c8861e9918` — `愈`
- `HOI_7ecf274c3ca2db` — `!+f ﾆ`

### Mục cần xác minh trước khi nhúng

- `HOI_d66c6b0d4ef33b`: `Recipe Distribution NPC (Temp)` có vẻ là nhãn phát triển, tạm dịch `NPC phát công thức (tạm)` nhưng chưa xác minh có hiển thị cho người chơi.

- `hoi_thoai_011`: nguồn có cả `Alex` và `Alec`; bản dịch thống nhất **Alec** theo tên đã dịch trong các nhiệm vụ. `Take Heart` dùng **Thu Tim** đối ứng với **Trao Tim**. Giữ nguyên tên **Blubber Bubbler**.

- `hoi_thoai_012`: thần nồi **Al-Khemie** tự xưng **thần**, gọi Oliver là **ngài/chủ nhân**. Dùng **Nồi Ghép**, **Ghép theo Công thức**, **Trứng Du Hành**. **Cống Imagen** là bản dịch tạm của `Imagen Manhole`, cần đối chiếu tên giao diện trong ROM.

## Luật để không sót, trùng hoặc lệch giọng

1. Mỗi `id` phải duy nhất trên toàn bộ các tệp dịch; **không nhập cùng lúc bản gộp và tệp riêng**.
2. Bản dịch phải giữ nguyên các mã trong nguồn như `{3:4}`, `{1:2}`, `<CTRL:01>`, `%s` và `[1000]`.
3. Tên riêng giữ theo bản DS. Oliver nói chân thành, tớ/cậu với bạn bè, con/mẹ và cháu/cô/chú với người lớn. Shizuku lanh lẹ, lém lỉnh nhưng không thô tục. NPC có ngữ cảnh riêng.
4. Xem `THUAT_NGU.md` trước khi dịch batch tiếp theo.
5. Chỉ ghi "đã dịch" cho file thực tế có trên repo và đã kiểm tra, không lấy số liệu từ nháp hoặc lời hứa.

**Chưa kiểm thử:** chất lượng bản dịch theo toàn tuyến truyện; font tiếng Việt; độ rộng ô thoại NDS; nhúng lại kịch bản, sửa offset/nhảy lệnh; chạy trong game thật. Các bước kiểm tra hiện tại chỉ xác minh ID/JSON/mã điều khiển. Đợt 11: 180/180 mục hợp lệ; tổng tích lũy 2.750 ID duy nhất.

**Đợt tiếp theo:** `hoi_thoai_013.jsonl`. Bản gộp sau đợt 11 nằm trong ZIP bàn giao, chỉ dùng **thay cho** chứ không nhập cùng lúc với các tệp riêng.
