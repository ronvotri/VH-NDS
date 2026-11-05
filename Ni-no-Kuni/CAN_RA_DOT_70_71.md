# Những điểm cần rà — đợt 70–71 (`hoi_thoai_071–072`)

- **Câu đố Mirant, `hoi_thoai_072` dòng 79:** 5 và 1 **xanh lá**; 6 **xanh dương**; 7 **xanh lá**; 4 và 3 **đỏ**; 2 **xanh dương**. Giữ các con số, màu và thứ tự chỉ dẫn.
- **Dòng 81:** giữ nguyên cụm đáp án tiếng Anh **"Huge Tower"**, kèm chú nghĩa "tòa tháp khổng lồ". Xác nhận cách nhập trên ROM, không đổi chuỗi nhận diện đáp án.
- **Thuật ngữ:** Hollowed → Rỗng Tim; Kindness → Nhân Ái; Faith → Niềm Tin; Love → Tình Yêu; Confidence → Tự Tin; Give Heart → Trao Tim; Tail Wrestling → Đấu Đuôi.
- **Địa danh và vật phẩm:** Corpse Lake → Hồ Tử Thi; Misleading Miasma → Chướng Khí Lạc Lối; Clarion → Sáo Clarion; giữ nguyên Astram, Rekka, Hotroit, Aylie, Obaba, Mirant, Mark, Marcel.
- **Kiểm tra xưng hô:** các vai dân Rekka không có tên người nói trực tiếp trong tệp JSONL nguồn; cần rà trên game các đoạn xưng hô "cậu", "ông", "cháu", "tớ"; nhất là khi người dân phản đối Oliver và phân cảnh cậu bé Aylie.
- **Đối chiếu dịch tay 2024:** 2 câu trùng nguyên văn tiếng Anh rất ngắn (Exactly!, Hey!); không tự động chép đè bản dịch hiện hành.
- **QA dữ liệu:** 360 câu mới, 0 nhãn nguồn hoãn, 0 trùng ID với 13.162 câu cũ, 0 sai mã bảo vệ, JSONL hợp lệ, mỗi câu tối đa 3 dòng × 48 ký tự.
- **Chưa được chứng minh:** chất lượng văn phong toàn tuyến, đủ pixel/byte trong hộp thoại DS, font dấu, tái đóng gói ROM hoặc thử trên giả lập.