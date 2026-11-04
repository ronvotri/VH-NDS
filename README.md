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
| 06 | `hoi_thoai_007` — Nghêu Bổ Dưỡng, Can Đảm, Mary–Suren và Sáo Clarion | 180 | Kiểm tra kỹ thuật đạt |
| 07 | `hoi_thoai_008` — Ichi no Kuni, Cowla, phô mai, Nhân Ái, Roy–Sophia | 180 | 1 nhãn nguồn nghi nội bộ cần rà |
| 08 | `hoi_thoai_009` — Roy–Sophia, Kiềm Chế, Tự Tin, nhà nghiên cứu Imagen Nellory | 180 | Kiểm tra kỹ thuật đạt |
| **Tổng** | | **2.210/17.935 (~12,3%)** | Chưa nhúng ROM |

Tệp dịch là JSONL, mỗi dòng `{"id":"...","translation":"..."}`. Sử dụng ID từ gói nguồn để nhập lại, không tự đổi mã điều khiển. **Không nhập cùng lúc bản gộp và các bản riêng**.

Bảng tiến độ: [TIEN_DO.md](TIEN_DO.md). Bảng thuật ngữ: [THUAT_NGU.md](THUAT_NGU.md). Kiểm tra số lượng và ID trùng: `tools/check_counts.py`.

Nguyên tắc: giữ đúng bối cảnh và ngôi xưng; Oliver chân thành; Shizuku dí dỏm; các đoạn cảm xúc vẫn tinh tế. Tên riêng theo bản DS, không tùy tiện đổi sang bản PS3. Lời thoại tự nhiên, hơi hài nhưng không phá chất truyện.

**Chưa kiểm tra:** font Việt, độ rộng ô thoại NDS, tái dựng kịch bản, nhúng vào ROM và thử chơi thật. 4 chuỗi nguồn nghi lỗi của `hoi_thoai_003` vẫn được để riêng, không dịch đoán.

**Tiếp theo:** `hoi_thoai_010`. Bản gộp `BAN_DICH_GOP_DOT_01_08.jsonl` nằm trong ZIP bàn giao đợt 8; không nhập đồng thời bản gộp và các tệp rời. Mục `HOI_d66c6b0d4ef33b` là nhãn NPC nghi nội bộ, cần xác minh khi nhúng. Mục `HOI_d66c6b0d4ef33b` là nhãn NPC nghi nội bộ, cần xác minh khi nhúng.
