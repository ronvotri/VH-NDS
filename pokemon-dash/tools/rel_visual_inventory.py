#!/usr/bin/env python3
"""Read-only visual inspection of NITRO RelocMod 1 byte patterns.

This is an *experimental* 8-bit grayscale preview, NOT a certified texture decoder.
Usage:
  python tools/rel_visual_inventory.py ./extracted/en --out ./preview
Needs: Pillow, numpy. Does not modify ROM or model data.
"""
from pathlib import Path
from PIL import Image, ImageDraw
import argparse, csv
import numpy as np


def grayscale_candidate(data: bytes, offset=0x400, width=256, height=32):
    if len(data) <= offset + width:
        return None
    count = min(width * height, len(data) - offset)
    count -= count % width
    raw = np.frombuffer(data[offset:offset+count], dtype=np.uint8)
    return Image.fromarray(raw.reshape(-1, width), "L").convert("RGB")


def run(model_dir: Path, out: Path):
    out.mkdir(parents=True, exist_ok=True)
    models = sorted(model_dir.rglob("*.rel"))
    inventory = []
    for page_no, first in enumerate(range(0, len(models), 36), 1):
        sheet = Image.new("RGB", (1800, 1296), "#202020")
        draw = ImageDraw.Draw(sheet)
        for j, path in enumerate(models[first:first+36]):
            data = path.read_bytes()
            if not data.startswith(b"NITRO RelocMod 1"):
                continue
            img = grayscale_candidate(data)
            entry = {
                "name": path.name, "size": len(data),
                "grayscale_offset_guess": "0x400",
                "grayscale_width_guess": 256,
                "texture_decoder_confirmed": False
            }
            inventory.append(entry)
            x, y = j % 3 * 600, j // 3 * 108
            draw.text((x + 8, y + 2), path.stem[:40], fill="#dddddd")
            if img is not None:
                img.thumbnail((580, 76), Image.Resampling.NEAREST)
                sheet.paste(img, (x + 8, y + 22))
        sheet.save(out / f"candidate_sheet_{page_no:02d}.png")
    with (out / "inventory.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(inventory[0]) if inventory else ["name"])
        writer.writeheader()
        writer.writerows(inventory)
    print(f"Created previews for {len(inventory)} model candidates")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("model_dir", type=Path)
    parser.add_argument("--out", type=Path, default=Path("rel_previews"))
    args = parser.parse_args()
    run(args.model_dir, args.out)
