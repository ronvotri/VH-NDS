# Source metadata anomaly — story|1486|0

English source `«\\n¢\\n*\\n%` contains 4 symbols and three literal newline escapes (`\\n`). Its raw CSV length is **10**, although the declared `toi_da_ky_tu` is **8**. The localized ASCII-compatible `-\\n-\\n*\\n%` likewise has raw length 10. After decoding the three newline escapes, the display contains **7** characters, which fits limit 8.

Removing a newline token to meet the raw limit would corrupt game data. Preserve the escaped newlines. Check in-game rendering when assembling the ROM. This is documented openly, not counted as zero strict length violations.
