# Ragnarok DS — Checkpoint 039 (20/11/2026)

## Tổng quan
- File Quest: `04-nhiem-vu-001.jsonl`, tổng **545/545 ID**.
- Thành phần: 33 hội thoại về danh tiếng Guild, 97 nhãn NPC, 49 điều kiện Quest, 183 mô tả mục tiêu, 183 tiêu đề Quest.
- 469 bản Việt khác EN và 76 nhãn/tên riêng/thuật ngữ giữ nguyên nguồn.
- Nguồn toàn dự án: **14.616 ID** / 33 JSONL, gồm 14.597 chuỗi và 19 nhãn chữ trong ảnh.
- Trước đợt 039: 14.071 ID, thêm 545 = **14.616/14.616 ID đã xử lý (100% phạm vi dịch dữ liệu)**.
- Các patch trên GitHub: DOT001–029, DOT034–039; bỏ qua DOT030 (815 bản ghi trùng cũ).

## QA đã chạy trong phiên
- Source `RagnarokDS_Checkpoint038_HoanTat_JobSkill_475muc.zip` (545 Quest chưa dịch).
- Đối chiếu 545 Quest với cùng nguồn: **0 ID trùng**, **0 mã `<Cxxxx>` lệch thứ tự**, **0 placeholder `%s`/`%d` bị mất**, **0 trường EN/context/group/uses thay đổi**, **0 đoạn Unicode vượt 36 ký tự giữa mã ngắt**.
- Chạy `tools/check_handoff.py` trên đủ 33 tệp nguồn của ZIP: `source_rows=14616`, `translated=3230`, `unfinished=11386`, `errors=[]`. Con số 3230 chỉ tính các bản dịch bên trong ZIP địa phương; 11386 bản dịch cũ đang ở các patch GitHub 001–026.
- Đã điều chỉnh ngắt dòng tên Item/địa danh và chạy QA lần hai: **đạt**.
- Bản cuối: `translation/PATCH-DOT039.jsonl`, **545 bản ghi**, blob SHA **`8d3f2442bf2c7888d79a1147322509ae24410c45`** đối chiếu nội dung file đã xuất.
- Bản GitHub của patch 039 đã kiểm tra sau khi ghi: đủ 545 ID, không trùng bên trong.

## Những việc CHƯA làm
- Chưa chạy `apply_patches.py` kết hợp toàn bộ 14.616 patch trong cùng một ZIP và QA `--require-complete` trên bản đó. Con số 100% là tiến độ **patch hợp lệ theo phạm vi ID**, không khẳng định đã kiểm thử trên ROM.
- Chưa QA chất lượng bản dịch độc lập từng hội thoại trong game; chưa kiểm tra ngữ cảnh xưng hô bằng gameplay.
- Chưa kiểm tra kích thước ký tự theo pixel, font Unicode và các trường text nằm trong texture ảnh.
- Chưa nhúng font, chưa vá ROM, chưa tạo bản NDS chơi được, chưa test giả lập/máy thật.

## Cách ghép từ GitHub

```bash
python Ragnarok-DS/tools/apply_patches.py \
  --handoff RagnarokDS_USA_BanGiao_Cloud.zip \
  --patch-dir Ragnarok-DS/translation \
  --output RagnarokDS_VH_Checkpoint_039_GitHub.zip
```

Sau khi xuất, báo cáo `BAO_CAO_GHEP_PATCH.json` cần có `source_rows=14616`, `patch_records=14616`, `applied=14616`, `pending=0`. Nếu không, không được gắn nhãn full.
