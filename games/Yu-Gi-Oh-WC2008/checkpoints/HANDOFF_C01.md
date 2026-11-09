# Yu-Gi-Oh! World Championship 2008 – C01 Duel dialogue (2026-11-09)

Repository: `ronvotri/VH-NDS`; project directory: `games/Yu-Gi-Oh-WC2008/` (separate from other NDS games).

- C01 covers **500/500** dialogue strings across `translations/duel_C01/C_THOAI_DUEL_01.csv` and `C_THOAI_DUEL_02.csv` (250 per file). New Vietnamese values occupy `tieng_Viet_MOI`.
- Of these, **206 strings differ from old machine Vietnamese**, and **294 existing Vietnamese strings were checked and retained**. The English text and all other columns are preserved.
- Technical QA: **500/500 PASS**; zero missing translations, max-length violations, game-token mismatches, or escaped linebreak differences.
- Running the supplied ZIP's `check_import.py` over A01–A26, B01–B11, and C01–C02 found **4.127 valid entries** and one pre-existing source-length warning from B05 at `story|1486|0` (three escaped `\\n`, displayed length 7/limit 8).
- Total project with new Vietnamese in result column: **4.127/8.156** (2.009 card descriptions A35 + 1.618 story B06 + 500 duel lines C01); **4.029** entries without new Vietnamese. Group C alone has **1.462** remaining.
- The complete ZIP checkpoint is `YGO_WC2008_CHECKPOINT_C01_THOAI_DUEL_500.zip` in ChatGPT handoff, containing 162 files, all earlier translations, glossary, QA logs and compiled `ket_qua_dich.json`.
- No ROM test performed; 'technical PASS' does not mean every line's voice and context has been finally approved.

**Next:** C02 translate `C_THOAI_DUEL_03.csv` and `C_THOAI_DUEL_04.csv` (500 lines); continue with the English original and commit without touching other games.
