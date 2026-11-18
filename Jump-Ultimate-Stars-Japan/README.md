# Jump Ultimate Stars (Japan) — Việt hóa NDS

**Checkpoint 021 — 18/11/2026** · ROM Nhật AJUJ · nhánh `vh/jump-ultimate-stars-japan`

## Tiến độ

- **13.085/34.919 chuỗi đã dịch (37,47%)**, còn **21.834** chuỗi `vi=null`.
- CP020: 12.452 chuỗi. **CP021: +633 chuỗi**, gồm:
  - `05-thu-vien-nhan-vat-005.jsonl`: 356 ID từ dòng 601–956 (file này hoàn thành).
  - `05-thu-vien-nhan-vat-006.jsonl`: 277 ID từ dòng 0–276.
- Nội dung: Muhyo & Roji, Naruto, Kakashi/Gaara/Jiraiya, Nube, Ninku.
- **Tiếp theo:** `05-thu-vien-nhan-vat-006.jsonl` từ dòng 277, mở đầu Neuro & Yako.

## Dữ liệu GitHub

- [BAN_DICH_021.jsonl](BAN_DICH_021.jsonl): 633 bản dịch mới, có `file`, `row_index`, `id`, `ja`, `vi`.
- [BAN_DICH_TONG_HOP_001-021.jsonl](BAN_DICH_TONG_HOP_001-021.jsonl): 13.085 bản dịch hợp nhất, không trùng ID.
- [THUAT_NGU.json](THUAT_NGU.json): 1.413 mục, tên chưa xác minh đánh dấu *provisional*.
- [XUNG_HO_NHAN_VAT.md](XUNG_HO_NHAN_VAT.md): quy tắc xưng hô theo vai và manga.
- [QA_021.json](QA_021.json): kiểm tra cấu trúc, mã và số lượng; **0 lỗi**, không ghi đè 12.452 bản dịch cũ.

ZIP bàn giao `JumpUltimateStars_VietHoa_Checkpoint_021.zip` trong ChatGPT bao gồm **30 file `translation/*.jsonl`**, toàn bộ câu tiếng Nhật cùng bản dịch tương ứng; câu chưa dịch giữ `vi=null`. GitHub lưu bản sai biệt 633 ID và bản hợp nhất để tiếp tục không sót.

## Quy tắc và giới hạn

Dịch trực tiếp từ nguồn Nhật. Giữ tên riêng, Item, Skill, thuật ngữ chính bằng tiếng Anh hoặc romaji; văn phong tự nhiên, có chất hài đúng lúc, nhất quán ngôi xưng. Không thay đổi `<IDEOSP>`, `<B0A>`, `<PERCENT_FULL>`, placeholder hay ID.

**QA hiện chỉ là kiểm tra tĩnh.** Có **4.658 đoạn trên 37 ký tự Unicode** cần soi độ rộng hiển thị; chưa có font Việt, bộ tạo patch, hay QA gameplay trên NDS. Chưa phải ROM chơi được.
