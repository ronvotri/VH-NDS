# Tiến độ Việt hóa Ni no Kuni DS

**05/11/2026 — 45 đợt — 8.863 / 17.935 mục ưu tiên (49,42%). Còn 9.072 mục.**

## Đợt 42–45 (mới nhất)

| Đợt | Tệp nguồn | Đã dịch | Hoãn |
|---|---|---:|---:|
| 42 | `hoi_thoai_043` | 180 | 0 |
| 43 | `hoi_thoai_044` | 180 | 0 |
| 44 | `hoi_thoai_045` | 180 | 0 |
| 45 | `hoi_thoai_046` | 180 | 0 |
| **Mới** | | **720** | **0** |

- Mã điều khiển và ID đã kiểm tra qua công cụ nguồn: tổng cộng **8.863 bản dịch hợp lệ, 45 tệp, 0 lỗi**.
- Theo dõi thuật ngữ mới, câu đố Astram, mật lệnh bẫy và các câu của bản demo trong `CAN_RA_DOT_42_45.md`.
- Chưa nhúng ROM, kiểm thử font hoặc độ rộng ô thoại thực tế.

## Đợt 38–41

| Đợt | Tệp nguồn | Đã dịch | Hoãn |
|---|---|---:|---:|
| 38 | `hoi_thoai_039` | 180 | 0 |
| 39 | `hoi_thoai_040` | 180 | 0 |
| 40 | `hoi_thoai_041` | 180 | 0 |
| 41 | `hoi_thoai_042` | 180 | 0 |
| **Mới** | | **720** | **0** |

- Công cụ kiểm tra nguồn chấp nhận **720/720 mục**, không lỗi ID, JSON hay mã điều khiển.
- Bản tích lũy có **8.143 ID duy nhất**. Ngắt tối đa ba dòng/câu, 48 ký tự/dòng theo văn bản, **chưa xác minh độ rộng font thực**.
- Đối chiếu kho dịch tay 2024 có **6 câu trùng nguyên văn**, chủ yếu lời ngắn; chỉ dùng để tham khảo.
- Giữ nguyên **11 mục hoãn cũ** (4 chuỗi nguồn nghi lỗi, 7 nhãn thử nghiệm).
- Cần rà các tên phép Dò Rương/Tầm Bảo, ngữ cảnh hồi tưởng Alicia–Jabou, ba câu hỏi Lời Thề Pháp Sư và thuật ngữ mới. Xem `CAN_RA_DOT_38_41.md`.

**Chưa nhúng ROM hay kiểm thử trên NDS. Không nhập đồng thời bản gộp và tệp rời.**

## Lịch sử đợt 34–37


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