# Tiến độ Việt hóa Ni no Kuni DS

**05/11/2026 — 37 đợt — 7.423 / 17.935 mục ưu tiên (41,39%). Còn 10.512 mục.**

## Đợt 34–37

| Đợt | Tệp nguồn | Đã dịch | Hoãn |
|---|---|---:|---:|
| 34 | `hoi_thoai_035` | 180 | 0 |
| 35 | `hoi_thoai_036` | 180 | 0 |
| 36 | `hoi_thoai_037` | 180 | 0 |
| 37 | `hoi_thoai_038` | 180 | 0 |
| **Mới** | | **720** | **0** |

## Kiểm tra dữ liệu

- Kiểm tra qua bộ `KIEM_TRA_BAN_DICH.py` đi kèm nguồn: **720/720 mục hợp lệ**, không lỗi ID, JSON hay placeholder.
- Bản gộp có **7.423 ID duy nhất**, không trùng với 6.703 mục trước đó.
- Câu mới tối đa **3 dòng**, mỗi dòng tối đa **48 ký tự** sau ngắt dòng ở khoảng trắng. Đây không đảm bảo vừa khung NDS, vì còn phụ thuộc font, độ rộng chữ và bố cục.
- Đối chiếu kho dịch tay Excel 2024: **16 câu nguồn trùng nguyên văn**, hầu hết là lời ngắn, dùng để tham khảo và rà ngôi xưng, không sao chép đè bản DS.
- Giữ nguyên **11 mục hoãn cũ**: 4 chuỗi lỗi đợt 2; 7 nhãn thử nghiệm đợt 29.

## Cảnh báo cần rà

1. `hoi_thoai_037`: các câu đố dựa trên ngôn ngữ tiếng Anh và hình minh họa. Cần thử đáp án, nhất là câu đối xứng 'racecar', câu đố số lượng cá/lá và hình đảo ngược.
2. `hoi_thoai_038`: câu nguồn dùng phép `Take Heart` để trao Tim cho Mark, có vẻ không khớp logic hệ kỹ năng. Bản dịch giữ `Thu Tim` theo nguồn, không tự sửa mã.
3. `hoi_thoai_037`: ghép Chìa Đỏ + Xanh tạo Chìa Trắng là logic của kịch bản nguồn, không tự đổi màu.
4. Vẫn cần kiểm thử font dấu tiếng Việt, độ rộng ô thoại, vị trí ROM, và ngữ cảnh khi chạy thật.

**Lưu ý nhập liệu:** chỉ dùng bản gộp hoặc các tệp rời, không nhập đồng thời.