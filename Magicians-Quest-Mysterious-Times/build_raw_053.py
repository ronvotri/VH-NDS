#!/usr/bin/env python3
"""Create hand-translated 0040.004 raw dialogue from reviewed phrases and explicit repeated blocks."""
from pathlib import Path
root = Path(__file__).resolve().parent
items = ['Vậy... Hẹn gặp lại nhé?¤¤']
items.extend(['Tớ chẳng hiểu mấy hoạt động▼ngoại khóa rắc rối này là gì.',
              ', cậu có biết họ đang▼bày trò gì không?¤'] * 10)
items.extend(['Cuối cùng giờ ngoại khóa▼cũng kết thúc! Bài nào cũng khó▼muốn xỉu!'] * 10)
items.extend([
    'Bọn mình làm bạn thân với nhau▼được một thời gian rồi...',
    'nhưng tớ nghĩ có lẽ nên▼xa nhau một thời gian.',
    'Đừng hiểu lầm! Không phải▼tớ hết quý cậu đâu...',
    'Chỉ là lúc nào cũng ở bên nhau,▼tớ sợ mình xem tình bạn▼là điều hiển nhiên.',
    'Xa nhau đôi chút, lại càng▼thấy quý nhau hơn mà!¤¤',
] * 10)
items.extend(['Này!¤¤'] * 20)
items.extend([
    'Mình đã yêu nhau▼được một thời gian rồi...',
    'nhưng tớ nghĩ nên kết thúc▼mấy chuyện yêu đương sến sẩm.',
    'Dù không còn là một đôi,▼tớ vẫn muốn đi chơi với cậu▼như hai người bạn!¤¤',
] * 6)
items.append('Mình đã yêu nhau▼được một thời gian rồi...')
assert len(items) == 120, len(items)
(root / 'vi_0040_004_raw.txt').write_text('\n'.join(items) + '\n', encoding='utf8')
print('Generated',len(items),'authored raw VI lines for 0040.004')