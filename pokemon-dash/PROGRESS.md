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
