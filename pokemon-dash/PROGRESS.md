# Pokémon Dash (USA) — checkpoint Việt hóa

Cập nhật: 2026-11-04. Dự án này độc lập với Ni no Kuni (DS) trong cùng repository.

## Trạng thái

- ROM: Nintendo DS USA, game ID **APDE**, 16 MiB. Người dùng phải tự sở hữu ROM gốc.
- Bản chơi thử ổn định mới nhất được dựng: **v0.6**; **chưa được kiểm thử gameplay đầy đủ trên máy DS hoặc giả lập**.
- NitroFS bên ngoài: **505** tệp, trong đó **242** ảnh NCG; **178** ảnh NCG khác ROM gốc ở v0.6.
- Kho con `archive.archive`: **318** tệp. Kho này **không đổi byte** giữa ROM gốc và v0.6.
- **91** mô hình `en/*.rel` (định dạng `NITRO RelocMod 1`) cần giải mã và kiểm chứng chữ 3D. **91 là số mô hình cần rà, KHÔNG phải số câu chưa dịch.**
- Các mô hình được phân nhóm: 7 Pause, 6 race-status, 25 stage-intro, 31 stage-title, 22 khác.
- Đã trích xuất 91 tệp và phân tích header, bảng vị trí thô, chuỗi metadata; **chưa giải mã mesh / texture** và **chưa sửa nội dung của kho 3D**.

## Phần 2D đã làm tới v0.6

Hướng dẫn luyện tập, tên đường đua, bảng xếp hạng/kỷ lục, tên cúp, menu, nút bấm; sửa một số chữ khó đọc. Chỉ kiểm chứng kết cấu ROM và IPS, chưa xác minh toàn bộ ngữ cảnh gameplay. Không tuyên bố 100% Việt hóa.

## Luật dịch đã được duyệt

- `Zigzag Road` → **Đường Zigzag** (không đổi thành Đường ngoằn ngoèo).
- Các cúp: **Cúp Xanh lá**, **Cúp Trắng**, **Cúp Xanh dương**, **Cúp Vàng**, **Cúp Đỏ**.
- Nút chọn cúp hiển thị **CÚP trên / tên màu dưới**.
- Nền đỏ: chữ sáng, viền đậm, ưu tiên đọc rõ hơn giữ màu gốc.
- Tên Pokémon, tên người trong credit để nguyên.
- Tiếng Việt **có dấu**, không làm vỡ kích thước/giới hạn palette của Nintendo DS.

## Đang chặn hoàn tất

`NITRO RelocMod 1` không phải tệp chứa chuỗi văn bản thông thường; tên ASCII cuối mô hình là metadata kỹ thuật, không phải bản dịch hiển thị. Không thay chuỗi này tùy tiện. Phải xác định hình chữ qua mesh/texture hoặc đối chiếu khi chạy game trước khi vá.

Ưu tiên: Pause → GOAL/TIME UP/REPLAY/BEST RECORD → giới thiệu cúp và đường đua → test trên melonDS/DS. Không phát hành v0.7 khi chưa có thay đổi đã xác minh.

## Tái lập kết quả kiểm kê

Chạy công cụ `tools/audit_dash_archive.py` trong thư mục dự án trên bản ROM USA của chính bạn. Công cụ chỉ đọc ROM, trích danh sách archive và đặc điểm đầu tệp mô hình; **không chỉnh ROM**.

## SHA-256 đối chiếu

- ROM gốc APDE: `d7b17c367c9bb9e3820d7862f237424cf2509c4f189e6a88fb299fc1cd521157`
- ROM v0.6: `2dd5d75336f3b3479e21bf795e7276b014d89e1fab59ec68c87760eeeba4018d`
- `archive.archive`: `052fdbb429ae539965329833f4189a75391762779fa7a7ceb74a0dba77d3a622`

**Không lưu file ROM có bản quyền lên repo; chỉ lưu công cụ, thuật ngữ và trạng thái kiểm thử.**

## Tiếp tục nghiên cứu 3D (04/11/2026 — lượt kế tiếp)

- Đã hiển thị **hình chữ có thể đọc** bằng cách xem một phần dữ liệu `NITRO RelocMod 1` ở dạng **8-bit grayscale, width 256, bắt đầu thử tại 0x400**. Đây là **cách xem thực nghiệm**, chưa phải bộ giải mã texture được chứng minh.
- Nhìn thấy được `Back to Title`, `Back to Course`, `GOAL!!`, `TIME'S UP!` và nhiều nhãn tên đường/cúp; đủ tạo bản kiểm kê hình ảnh của cả **91** mô hình 3D.
- Đã có bản **preview thử** đổi `Back to Title` → `Về menu` trong cùng chiều dài mẫu model (chỉ đổi vùng byte tương ứng hình nghi vấn), nhưng **chưa đóng vào ROM phát hành và chưa test emulator**.
- Đã lập hàng đợi dịch 91 model: **69 có gợi ý nhãn Việt**, **22 chưa xác định**; đây không phải 69 bản dịch đã vá vào ROM.
- Công cụ và ghi chú chi tiết: `3D_VISUAL_BREAKTHROUGH.md` và `tools/rel_visual_inventory.py`.

**Bản chơi thử mới nhất giữ nguyên v0.6**. Bước tiếp: xác minh điểm bắt đầu texture / định dạng palette / UV và kiểm thử trong giả lập trước khi xuất v0.7.

## Bản thử 3D A3I5 v0.7 Alpha (04/11/2026)

- Đã thử biên dịch bản ROM mới kế thừa v0.6, chỉ thay **một mô hình 3D** `en/mdl_pause_title.rel` (`Back to Title` → `Về menu`), bốn vùng chữ / hai trạng thái.
- Dữ liệu raster rất giống A3I5 (alpha 3-bit, palette index 5-bit); giả thuyết chưa được kiểm chứng trực tiếp bằng engine.
- Header, kích thước mô hình, 317 tệp archive khác giữ nguyên. **1872 byte** thay đổi trong đúng vùng thử.
- **IPS round-trip PASS; SHA-256 ROM Alpha:** `d592391af5d125c902545d143c3bca3bc65acc2986efdd1690c6248fd856a16d`.
- Bộ nguồn và bản vá thử: [3D_A3I5_ALPHA_TEST.md](3D_A3I5_ALPHA_TEST.md), `patches/v06_to_v07_alpha_pause_title.ips`, `tools/apply_v07_alpha.py`.
- **Chưa kiểm thử runtime trên melonDS/NDS**. Vẫn giữ v0.6 là bản dùng chính; v0.7 chỉ là **Alpha test**.
- Ưu tiên kế: xác minh nhãn Pause trong game trước, sau đó mới sửa `mdl_pause_course`, `mdl_t_goal`, `mdl_t_timesup`.

## v0.8 Alpha: Pause / Tiếp tục (04/11/2026)

- ROM mới từ v0.7 Alpha, dịch thêm **`Continue` → `Tiếp tục`** trong `en/mdl_pause_tudukeru.rel`.
- Vùng chữ chỉ cao 7 pixel, sử dụng bitmap pixel tự dựng; có bản preview, **chưa test trong DS/melonDS**.
- Chỉnh 1139 byte, chỉ trong raster trước relocation `0xB60`. 317 tệp archive khác không sửa; tổng cộng **2/91 mô hình 3D có bản vá thử nghiệm**, không phải 2 mô hình được chứng nhận hoàn tất.
- IPS từ v0.7 Alpha, công cụ SHA-verified: [3D_ALPHA_V08.md](3D_ALPHA_V08.md), `patches/v07_to_v08_alpha_pause_continue.ips`, `tools/apply_v08_alpha.py`.
- SHA-256 ROM test v0.8: `635353b74025daf83e9a4d0a121e24896696fa0c2e8cf644c444e60ab57f0b3b`.
- v0.6 vẫn là bản thử nghiệm chính. v0.8 là bản kiểm tra chữ 3D, còn nguy cơ khó đọc/không hiển thị và chưa kiểm thử runtime.

## v0.8.1 Alpha — sửa font 3D bị dính nét

- Phản hồi từ ảnh v0.8: chữ **Tiếp tục** dày, sát nét, khó đọc do font 3×7 bị kéo ngang.
- Thay bằng glyph **5×7 pixel native, không resize**, cách 1 pixel. Chỉ đổi 340 byte trong `mdl_pause_tudukeru.rel`; kiểm tra IPS round-trip PASS; chưa gameplay-test.
- ROM SHA-256 v0.8.1: `b9bc2094455c2316be263f31a05978f5949060241c1b802a9d18c16d9f023409`.
- Báo cáo và patch: [3D_ALPHA_V081_FONT_QA.md](3D_ALPHA_V081_FONT_QA.md), `patches/v08_to_v081_alpha_fontfix.ips`, `tools/continue_font_5x7.py`.
- **Giới hạn nguyên bản:** texture chỉ cao 7 pixel; font đã gọn hơn nhưng chữ có dấu vẫn cần xem thực tế trên màn DS. **v0.6 là bản ổn định để giữ lại.**
