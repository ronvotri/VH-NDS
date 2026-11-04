#!/usr/bin/env python3
"""Direct 5×7 pixel glyph mask for Pokémon Dash's 7px Pause/Continue model.

No stretching: each logical pixel maps to one model texel.
This only builds a mask, not a ROM. The original model remains necessary.
Requires numpy; project asset widths are per-state 54/54/54/55 pixels.
"""
import numpy as np

GLYPHS = {
    "T": ["11111", "00100", "00100", "00100", "00100", "00100", "00100"],
    "i": ["01000", "00000", "11000", "01000", "01000", "01000", "11100"],
    "ế": ["00100", "01010", "01110", "10001", "11111", "10000", "01111"],
    "p": ["00000", "00000", "11110", "10001", "11110", "10000", "10000"],
    " ": ["000", "000", "000", "000", "000", "000", "000"],
    "t": ["00100", "00100", "11110", "00100", "00100", "00101", "00010"],
    "ụ": ["00000", "10001", "10001", "10001", "10001", "01110", "00100"],
    "c": ["00000", "01110", "10001", "10000", "10000", "10001", "01110"],
}


def glyph_mask(text="Tiếp tục", width=54):
    if width < 50:
        raise ValueError("Model 3D Continue label expects 54+ pixels")
    letters = [
        np.array([[255 if bit == "1" else 0 for bit in line] for line in GLYPHS[ch]],
                 dtype=np.uint8)
        for ch in text
    ]
    ink_width = sum(letter.shape[1] for letter in letters) + len(letters) - 1
    out = np.zeros((7, width), dtype=np.uint8)
    x = (width - ink_width) // 2
    for letter in letters:
        out[:, x:x + letter.shape[1]] = letter
        x += letter.shape[1] + 1
    return out


if __name__ == "__main__":
    from PIL import Image
    mask = glyph_mask()
    Image.fromarray(mask, "L").resize((432, 56), Image.Resampling.NEAREST).save(
        "dash_continue_font_5x7_preview.png")
