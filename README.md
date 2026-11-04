# Ni no Kuni (Nintendo DS) — Bản dịch tiếng Việt

Nơi lưu bản dịch và theo dõi tiến độ Việt hóa từ gói chữ xuất của trò chơi. **Đây chưa phải ROM đã vá và chưa nhúng tiếng Việt vào game.**

## Tiến độ 04/11/2026

| Đợt | Phần | Đã dịch | Ghi chú |
|---|---|---:|---|
| 01 | Hội thoại 001–002, hướng dẫn, nhiệm vụ, địa danh và UI | 954 | Kiểm tra kỹ thuật đạt |
| 02 | `hoi_thoai_003` | 176 | 4 chuỗi nguồn nghi hỏng, chưa dịch |
| 03 | `hoi_thoai_004` — Babanacia, NPC và nhiệm vụ | 180 | Kiểm tra kỹ thuật đạt |
| 04 | `hoi_thoai_005` — NPC, họa sĩ, bác sĩ và chuyện hôn nhân | 180 | Kiểm tra kỹ thuật đạt |
| 05 | `hoi_thoai_006` — Mirant, Nhẫn Qi, du lịch, tình mẹ và ẩm thực | 180 | Kiểm tra kỹ thuật đạt |
| **Tổng** | | **1.670/17.935 (~9,3%)** | Chưa nhúng ROM |

Tệp dịch là JSONL, mỗi dòng `{"id":"...","translation":"..."}`. Sử dụng ID từ gói nguồn để nhập lại, không tự đổi mã điều khiển. **Không nhập cùng lúc bản gộp và các bản riêng**.

Bảng tiến độ: [TIEN_DO.md](TIEN_DO.md). Bảng thuật ngữ: [THUAT_NGU.md](THUAT_NGU.md). Kiểm tra số lượng và ID trùng: `tools/check_counts.py`.

Nguyên tắc: giữ đúng bối cảnh và ngôi xưng; Oliver chân thành; Shizuku dí dỏm; các đoạn cảm xúc vẫn tinh tế. Tên riêng theo bản DS, không tùy tiện đổi sang bản PS3. Lời thoại tự nhiên, hơi hài nhưng không phá chất truyện.

**Chưa kiểm tra:** font Việt, độ rộng ô thoại NDS, tái dựng kịch bản, nhúng vào ROM và thử chơi thật. 4 chuỗi nguồn nghi lỗi của `hoi_thoai_003` vẫn được để riêng, không dịch đoán.
