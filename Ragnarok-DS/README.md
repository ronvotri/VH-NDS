# Ragnarok DS (USA) — Việt hóa NDS

Nhánh độc lập `vh/ragnarok-ds-usa` của kho `VH-NDS`. Không trộn với các dự án Ni no Kuni, Magician’s Quest hoặc Ragnarok Odyssey ACE.

## Nguồn dữ liệu
- Bàn giao: `RagnarokDS_USA_BanGiao_Cloud.zip` (ROM USA, mã YRBE).
- Tổng 14.616 mục trong 33 tệp JSONL: 14.597 chuỗi và 19 nhãn ảnh; không bao gồm ROM.
- Đợt 001: 304 mục đã điền `vi` (219 bản Việt khác nguồn, 85 mục giữ nguyên), 14.312 mục còn `null`.
- Kiểm tra bằng `tools/check_handoff.py`: 14.616 ID; **0 lỗi**, chưa bật `--require-complete` vì đây là bản dịch từng phần.

## Quy ước
- Giữ nguyên **tên riêng, tên Job, item, skill, quái, địa điểm, tên Guild, Zeny, HP, SP, ATK, DEF và thuật ngữ gameplay chủ chốt**. 
- Việt hóa thông báo, hội thoại, mô tả, hướng dẫn, credit và nhãn UI không phải thuật ngữ chính.
- Giọng tự nhiên, gần gũi, điểm hài vừa phải; cảnh bi kịch phải được tôn trọng. Không thêm meme làm sai tính cách.
- Giữ nguyên **ID, trường en, thứ tự JSONL và mọi thẻ <Cxxxx>**, biến dạng %s/%d và ngắt dòng mã hóa.
- Ngôi xưng dựa trên lời thoại lân cận, không đoán quan hệ/tuổi/giới tính.
- Không tự sửa/đăng ROM thương mại. Chưa có font Việt, chưa patch và chưa test giả lập/máy thật.

## Tập tin bàn giao

Bản ZIP đầy đủ của đợt 001 đã được xuất trong phiên ChatGPT, gồm toàn bộ 33 JSONL với `vi=null` cho phần chưa dịch, `THUAT_NGU.json`, `QUY_TAC_XUNG_HO.md`, `DANH_BA_NHAN_VAT.json`, `BAO_CAO.txt` và `PATCH-DOT001.jsonl`.


## Checkpoint 002 — 18/11/2026

- **Đợt 002 thêm 759 ID:** +669 hệ thống và +90 hội thoại đầu game.
- **Tổng cộng 1.063/14.616 mục:** 922 bản Việt khác nguồn, 141 mục giữ nguyên tiếng Anh, 13.553 mục chưa xử lý.
- **QA chính thức:** 0 lỗi ID và mã điều khiển, không thay `en` hoặc các trường ngữ cảnh; chưa test font/máy thật.
- Đợt 002 ở `translation/PATCH-DOT002.jsonl`; đợt 001 ở 5 tệp `PATCH-DOT001-*.jsonl`. Công cụ `tools/apply_patches.py` sẽ tự áp dụng **cả hai** theo ID.
- Bộ ZIP đủ 33 JSONL đã xuất riêng trong phiên trò chuyện, kèm `THUAT_NGU.json`, hồ sơ xưng hô, báo cáo QA. Không đưa ROM lên GitHub.

## Checkpoint 003 — 18/11/2026

- **+266 ID** mới trong `translation/PATCH-DOT003.jsonl`, hoàn thành **05-hoi-thoai-001.jsonl: 441/441**.
- **Tích lũy tại mốc 003: 1.329/14.616 mục (9,09%)**, 1.186 bản dịch khác EN và 143 mục giữ nguyên thuật ngữ; 13.287 mục đang `vi=null`.
- Cảnh: lập Guild, nhiệm vụ tại Prontera Culvert, gặp Lucifi, giúp ông Olav tìm Colm (10 tuổi), White Peach.
- Điều chỉnh xưng hô theo cặp: người chơi–Lucifi **tôi/anh** (Lucifi dùng **tôi/cậu**), Olav **ông/cháu**, Colm **em/tôi** khi nói chuyện với người chơi không xác định giới tính, chỉ huy–thuộc cấp trang trọng.
- `tools/check_handoff.py` báo **14.616 source rows, 1.329 translated, 13.287 unfinished, 0 errors**.
- Đây vẫn là bản dữ liệu JSONL, **chưa có font tiếng Việt và chưa patch ROM**.

## Checkpoint 004 — 18/11/2026

- **+489 ID**, hoàn thành toàn bộ `05-hoi-thoai-002.jsonl` (489/489, trước đó vi=null). Bản mới nằm tại `translation/PATCH-DOT004.jsonl`.
- **Tích lũy 1.818/14.616 mục (12,44%)**: 1.664 mục khác bản EN, 154 mục đã rà và giữ nguyên; còn 12.798 mục chưa xử lý.
- Ngữ cảnh: đoàn tụ Colm/Olav, săn kho báu ở Geffen, trò lừa của Lughill/Attar, hồn ma Aghill, Viselc trợ chiến, Dark Knight và ký ức về mẹ, tìm Emperium để lập Guild.
- Bảo toàn tên nhân vật, item/Job/skill/địa điểm, tiêu biểu: White Peach, Dog Tag, Emperium, Prontera, Geffen, Mjolnir Dead Pit, Order of Knights, Guild. Mã điều khiển, màu và tên động được giữ nguyên.
- **QA 0 lỗi:** kiểm 14.616 ID, giữ `en`, không thêm/bớt mã điều khiển. Chưa thử font Việt, hiển thị trên NDS hay patch ROM.
- Bộ ZIP checkpoint 004 tích lũy đủ 33 tệp JSONL, có patch mới và báo cáo QA.

## Checkpoint 005 — 18/11/2026

- **+550 ID** mới, hoàn thành `05-hoi-thoai-003.jsonl` (550/550). Patch tại `translation/PATCH-DOT005.jsonl`.
- **Tích lũy 2.368/14.616 mục (16,20%)**: 2.204 mục dịch khác EN, 164 mục được kiểm tra và giữ nguyên, 12.248 mục chưa dịch.
- Bao gồm cảnh Lucifi khuyên người chơi, đoàn buôn Viselc, Lisir, Popi/Yolanda, Golden Eagle Guild, Frione/Frione Tear, Aldo, Emperium và Order of Knights. Giữ nguyên tên, item, skill và thuật ngữ chính.
- QA chính thức: **14.616 ID, 2.368 mục có `vi`, 12.248 mục `vi=null`, 0 lỗi**. Đối chiếu với nguồn `RagnarokDS_USA_BanGiao_Cloud.zip`; không đổi `en`, ID, mã điều khiển.
- **Chưa kiểm tra font tiếng Việt, tràn dòng trên NDS, patch ROM hay máy thật**.

## Checkpoint 006 — 18/11/2026

- **+535 mục** (525 câu dịch khác EN, 10 mục chỉ có tên hoặc lời gọi được giữ nguyên), hoàn thành `05-hoi-thoai-004.jsonl` (535/535). Tệp GitHub: `translation/PATCH-DOT006.jsonl`.
- **Tích lũy 2.903/14.616 mục (19,86%)**, 2.729 bản khác tiếng Anh, 174 mục giữ nguyên sau rà, 11.713 mục `vi=null`.
- Cảnh truyện: Aldo–Rodia–Zane gặp rồng; Emperium ở Yusidra Caves; lập Guild và Kafra; Golden Eagle, Edwin, Fiona; món Rusty Legendary Sword; Dark Knight; mở đầu nhiệm vụ Yolanda/Popi.
- **QA nguồn chính thức** (bản `tools/check_handoff.py` từ bộ bàn giao): 14.616 ID, 2.903 mục có `vi`, 11.713 chưa dịch, **0 lỗi** điều khiển/placeholder/ID. Đã đối chiếu phiên bản JSONL tích lũy của checkpoint 005; không sửa `en`.
- Chưa build ROM, chưa thay font, chưa kiểm tra kích thước tiếng Việt trên NDS hoặc giả lập.

## Khôi phục bản dịch từ GitHub

Trong nhánh có **2.903 patch records** từ các đợt 001–006, không trùng ID. Công cụ kiểm tra của bộ nguồn xác nhận 0 lỗi cấu trúc; vẫn cần kiểm tra hiển thị sau khi bổ sung font.

```bash
python Ragnarok-DS/tools/apply_patches.py \
  --handoff RagnarokDS_USA_BanGiao_Cloud.zip \
  --patch-dir Ragnarok-DS/translation \
  --output RagnarokDS_VH_Checkpoint_006_GitHub.zip
```

Lệnh chỉ xuất ZIP dịch thuật, không chỉnh ROM hay font và không xóa dòng chưa dịch. Bản ZIP đã xuất trực tiếp trong phiên chat còn có danh bạ nhân vật và bảng thuật ngữ cập nhật.

## Kiểm tra khi nhận bản ZIP

```sh
python tools/check_handoff.py --source INPUT/translation --translation KET_QUA/translation
```

Không dùng `--require-complete` cho các đợt chưa dịch xong. Nhớ đối chiếu tên/mô tả và ảnh UI trước khi đóng gói vào game.
