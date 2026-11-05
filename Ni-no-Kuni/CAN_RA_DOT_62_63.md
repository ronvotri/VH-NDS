# Ni no Kuni DS — Điểm cần rà đợt 62–63

Nguồn: `hoi_thoai_063–064` (**359/360 câu dịch**, 1 nhãn thử nghiệm hoãn). Đã soát ID, cấu trúc JSONL, placeholder và giới hạn ngắt dòng sơ bộ 3 × 48 ký tự. Mã nguồn như `{3:4}`, `{1:2}` được giữ nguyên.

- **Colin/Corrin**: cùng người tiều phu, nguồn `hoi_thoai_063` dùng *Colin* (dòng 149/170) nhưng dòng 164 ghi *Corrin*; `hoi_thoai_064` dùng *Colin*. Bản dịch chuẩn hóa **Colin**, cần soát nhãn UI.
- **Phone Stone → Đá Liên Lạc**: tạm giữ tên đã chọn ở đợt trước; kiểm tra tên vật phẩm.
- **Dragon's Den → Hang Rồng**, **Glacier Grotto → Hang Băng**, **Mouth of Shadaar → Miệng Shadaar**: kiểm tra nhãn bản đồ. Chỉ dẫn hướng đông giữ đúng nguồn.
- **Grey**: tên riêng chó, giữ nguyên; cảnh chia tay được giữ giọng nghiêm túc.
- **Nguồn 064 dòng 40**: `(Chief's Schedule)`, dịch `(Lịch trình Trưởng Làng)`; có thể là nhãn nội bộ.
- **Nguồn 064 dòng 45**: `Temp text` (`HOI_7fdeb5909b7ee1`), **hoãn riêng**, không đưa vào JSONL.
- **Khớp kho 2024**: 1 câu nguồn trùng tiếng Anh nguyên văn (nguồn 063 dòng 162); chỉ đối chiếu, không chép đè.
- **Thuật ngữ**: Hollowed → Rỗng Tim; Love → Tình Yêu; Give Heart → Trao Tim; Arcane Stone → Ma Thạch; Great Sage → Đại Hiền Giả; Priestess → Nữ Tư Tế; Chief → Trưởng Làng; Hardwood → gỗ cứng.

**Chưa thực hiện**: nhúng ROM, kiểm tra font có dấu/byte, đo kích thước ô thoại thực tế và chơi thử trên NDS. QA dữ liệu không thay cho kiểm thử game.
