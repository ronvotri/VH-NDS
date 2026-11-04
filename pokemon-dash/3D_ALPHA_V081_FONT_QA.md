# Pokémon Dash — sửa font 3D quá khó đọc (v0.8.1 Alpha)

Ngày 04/11/2026. Không thay thế v0.6 làm bản thử nghiệm chính.

## Phản hồi QA

Người chơi nhận xét ảnh trước/sau của v0.8 khó đọc. Nguyên nhân: script v0.8 vẽ từng chữ cao 7 pixel ở ma trận 3 cột rồi **kéo ngang lên gần 44 pixel**, khiến nét dày và dấu tiếng Việt dính nhau.

## Thay đổi đã thực hiện

- Vẽ `Tiếp tục` bằng font trực tiếp **5×7 pixel**, không kéo giãn; 1 pixel khoảng cách giữa ký tự.
- Giữ màu của 4 trạng thái chữ, thông qua A3I5 palette index 31/15 từ bản v0.8.
- Chỉ thay 340 byte trong `en/mdl_pause_tudukeru.rel`, ở vùng raster gốc. Giữ nguyên header/relocation và 317 tệp con archive còn lại.
- IPS từ **đúng v0.8 Alpha**: [patches/v08_to_v081_alpha_fontfix.ips](patches/v08_to_v081_alpha_fontfix.ips) (Git blob `fc6b0b14c36688640345e11c594b97565887fc17`).
- Source glyph: [tools/continue_font_5x7.py](tools/continue_font_5x7.py).
- IPS round-trip PASS, SHA đầu ra trùng bản dựng. **Chưa kiểm thử trên máy DS hay giả lập.**

## SHA-256 ROM

- Đầu vào v0.8 Alpha: `635353b74025daf83e9a4d0a121e24896696fa0c2e8cf644c444e60ab57f0b3b`
- Đầu ra v0.8.1 Alpha: `b9bc2094455c2316be263f31a05978f5949060241c1b802a9d18c16d9f023409`

## Giới hạn còn lại

Texture chỉ cao 7 pixel nên dấu phức tạp (như **ế**, **ụ**) vẫn nhỏ. Bản này sửa lỗi chữ bị *kéo giãn*, chưa chứng minh nét chữ dễ đọc khi model 3D được phối màu/thu phóng trong gameplay. Không xác nhận 100% Việt hóa, không phát hành là stable. Người chơi cần kiểm thử in-game; nếu vẫn khó đọc, cân nhắc dùng nhãn ngắn hơn sau khi xác định khả năng hiển thị thực tế.
