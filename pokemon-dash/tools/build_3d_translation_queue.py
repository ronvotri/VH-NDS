#!/usr/bin/env python3
"""Generate a work queue from EXTRACTED Pokemon Dash en/*.rel files.
No ROM or game assets distributed; queue entries are proposals, NOT patches.
"""
from pathlib import Path
import argparse
import csv

COURSES = {
    "green": ["Đồng cỏ xanh", "Băng qua đồng", "Đường ven biển", "Dấu chân Mankey", "Đảo Pikachu"],
    "white": ["Miền tuyết trắng", "Đầm lầy thử thách", "Hồ bí ẩn", "Đồng bằng nứt nẻ", "Đảo Luvdisc"],
    "blue": ["Đường Zigzag", "Suối uốn lượn", "Cao nguyên bùn", "Hồ Sao", "Núi Jirachi"],
    "yellow": ["Dấu ấn Smeargle", "Đảo dung nham", "Đảo băng", "Đảo cát", "Đảo Pallet"],
    "red": ["Đồng cỏ lắt léo", "Vùng đất nóng", "Đầm xoáy", "Vòng xoáy băng", "Đảo Công viên Pokémon"],
    "battle": ["Đường đua hiểm hóc", "Đường thẳng sa mạc", "Đồng bằng gồ ghề", "Miền đất bằng phẳng", "Đầm lầy ô vuông"],
}
UI = {
    "mdl_pause_title": ("Back to Title", "Về menu"),
    "mdl_pause_course": ("Back to Course", "Trở lại đường đua"),
    "mdl_pause_retry": ("Retry", "Thử lại"),
    "mdl_pause_tudukeru": ("Continue", "Tiếp tục"),
    "mdl_pause_cup": ("Cup", "Cúp"),
    "mdl_pause_reverse": ("Reverse", "Đảo chiều"),
    "mdl_t_goal": ("GOAL!!", "VỀ ĐÍCH!"),
    "mdl_t_timesup": ("TIME'S UP!", "HẾT GIỜ!"),
    "mdl_t_replay": ("Replay", "Phát lại"),
    "mdl_t_best_record": ("Best Record", "Kỷ lục"),
    "mdl_t_speed_up": ("Speed Up", "Tăng tốc"),
    "mdl_pause_blt": ("Unknown pause label", "Chưa xác định"),
    "mdl_t_cp_x": ("Checkpoint number", "Số chốt kiểm tra"),
    "mdl_t_cp_atoko": ("Unknown checkpoint label", "Cần xem trực tiếp"),
}


def collect(directory):
    rows = []
    for p in sorted(directory.rglob("*.rel")):
        original, vietnamese = UI.get(p.stem, ("Unclassified", "Chưa đối chiếu"))
        source = "menu"
        for color, names in COURSES.items():
            for i, translation in enumerate(names, 1):
                if p.stem in (f"mdl_t_stage_st_{color}_{i}", f"mdl_t_stage_st_intro_{color}_{i}"):
                    original, vietnamese = "course name", translation
                    source = "approved 2D course name"
        rows.append({
            "model": p.name, "english_or_type": original,
            "suggested_vietnamese": vietnamese, "origin": source,
            "patch_status": "NOT_PATCHED", "in_game_test": "NOT_TESTED",
        })
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("model_dir", type=Path)
    ap.add_argument("--out", type=Path, default=Path("3D_TEXT_QUEUE.csv"))
    a = ap.parse_args()
    rows = collect(a.model_dir)
    with a.out.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Queued {len(rows)} models; proposed: {sum(r['suggested_vietnamese']!='Chưa đối chiếu' for r in rows)}")


if __name__ == "__main__":
    main()
