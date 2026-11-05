# Ni no Kuni DS — Tiến độ Việt hóa

**05/11/2026 — 81 đợt — 15.046 / 17.935 mục ưu tiên (83,89%). Còn 2.889 mục.**

Giữ nguyên 14.831 mục từ checkpoint trước. Hai đợt 80–81 chuyển sang nhóm **lựa chọn và thông báo**. Phần `lua_chon_thong_bao_002` đã được dịch ở đợt 01, không dịch lại.

| Đợt | Nguồn | Tổng dòng | Dịch | Hoãn |
|---|---|---:|---:|---:|
| 80 | `lua_chon_thong_bao_001.jsonl` | 180 | 157 | 23 |
| 81 | `lua_chon_thong_bao_003.jsonl` | 90 | 58 | 32 |
| **Cộng mới** | | **270** | **215** | **55** |

Đã đối chiếu **215 ID mới**, JSONL hợp lệ, mã bảo vệ/placeholder không bị mất, giới hạn sơ bộ tối đa 3 dòng × 48 ký tự/dòng. 55 mục hoãn (chuỗi hỏng, nhãn debug, từ khóa đố BURN/FREEZE) được ghi tại `DEFERRED_SOURCE_80_81.json`.

**Còn lại:** 2.540 mục vật phẩm/kỹ năng, 236 mục nhiệm vụ phụ, 55 mục lựa chọn/thông báo hoãn, 58 mục hội thoại hoãn = **2.889**. Ngoài ra 1.860 mục tên riêng tùy chọn không thuộc mẫu số ưu tiên.

**Chưa kiểm thử:** ROM, font dấu tiếng Việt, byte/offset, độ rộng pixel và chạy thật trên NDS. Không nhập bản gộp cùng các tệp JSONL rời.
