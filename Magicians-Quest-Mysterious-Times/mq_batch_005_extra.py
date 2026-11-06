#!/usr/bin/env python3
"""Cụm 005B — ngôn ngữ chào hỏi/đùa dí dỏm theo kiểu NPC tự tin, hơi khoe mẽ."""
import re,json,unicodedata
from pathlib import Path
f=Path(__file__).resolve().parent/'translation/04-thoai/talkfigs__0eng__data__0000.001.jsonl'
TOK=re.compile(r"\$\d{3}(?:'[^;\r\n\t]*)?;")
PFX=re.compile(r"^(?:(?:\$(?!500|503|000)\d{3}(?:'[^;\r\n\t]*)?;))*")
SLOT=re.compile(r'@(\d+)')
raw=r'''0|Xin chào! Hình như▼chúng ta chưa quen nhau nhỉ.
1|Cứ gọi tớ là @0.
2|À, mà nhớ nhé, nhà tớ▼giàu lắm đó. Tớ phải▼giữ phong độ chứ!
3|Chào người bạn mới!▼Tớ là @0. Vui quá được gặp cậu!
4|Hẹn gặp lại nha!
5|Này... hình như▼chúng ta chưa gặp nhau.
6|Tớ tên là @0.
7|Biết đâu chúng mình▼làm bạn được nhỉ.
8|Chào người lạ!▼Đã gặp nhau thì▼phải giới thiệu chứ!
9|Tên tớ là @0!▼Lần sau gặp nhớ▼chào tớ đó nhé!
10|Tớ có linh cảm tụi mình▼sẽ chơi với nhau cực vui!
11|Hừm... tớ chưa từng▼thấy cậu bao giờ thì phải.
12|Cậu tên gì nhỉ?▼@0 à?▼Tên nghe lạ ghê...
13|Tớ là @0.▼Từ giờ chúng mình▼làm bạn nhé!
14|Ê, cậu kia!▼Tên gì hả?!
15|@0 hả? Rõ rồi!
16|Tớ là @0!▼Được gặp tớ là may cho cậu!
17|Hửm? Hình như tớ▼chưa thấy cậu ở đây.
18|Tên tớ là @0.
19|Nếu gặp may, tớ sẽ▼cân nhắc kết bạn với cậu.
20|Ai đây ta?▼À, @0 chứ ai...
21|Lâu rồi không thấy cậu.▼Dạo này sao rồi?
22|Thôi, hẹn gặp lại nhé.
23|Chào @0!▼Lâu lắm mới gặp đó.
24|Tớ đây, @0 nè!
25|Đừng bảo cậu quên tớ nha!▼Nhà tớ giàu thế cơ mà!
26|Ê bạn hiền!▼Lâu lắm không thấy mặt!
27|Tớ đây, @0!
28|Thôi, gặp lại sau nhé!
29|Ồ, là cậu à.▼Lâu rồi nhỉ?
30|Tớ biết cậu đang muốn▼kể lắm rồi. Nói đi,▼cậu trốn đâu thế?
31|Chắc rồi mình cũng▼sớm gặp lại thôi...
32|Lại gặp cậu rồi!▼Lâu lắm rồi còn gì!
33|Dạo này mọi chuyện ổn chứ?
34|Ê! @0 đấy à!
35|Là tớ, @0 đây!▼Lâu quá không gặp, nhỉ?
36|Từ giờ gặp nhau trên▼hành lang nhớ chào đấy!
37|@0 đấy hả?!
38|Cậu lặn đâu thế, đồ lười!▼Và tên tớ là gì nào?!
39|Đừng nói cậu quên tớ nhé!▼Gọi tớ là @0!▼Rõ chưa? Giải tán!
40|Ê @0!▼Chúc mừng năm mới!
41|Năm nay tớ sẽ làm cả▼thế giới phải nhớ tên mình!▼Cứ chờ xem!
42|Ê hê!
43|Hú hú!
44|Này, @0.
45|Sao thế? Trông cậu▼lạc đường rồi kìa!
46|Ê! @0!
47|Chào @0.
48|Ê, @0!
49|Sao mặt ủ rũ thế?
50|Chào nhé, @0!
51|Đừng bảo cậu tới▼xin chữ ký tớ nha.
52|Ngôi sao cũng cần▼chút riêng tư chứ!
53|Ê, chào!
54|Có ngày nào mà tớ▼không ngầu được nhỉ?
55|Ối! Nhìn nắng kìa!
56|Chói lóa gần bằng tớ luôn!
57|Tớ mê trời mưa lắm...▼Nhất là vẻ ướt át▼đầy phong cách của mình!
58|Cả thế giới trắng xóa▼vì tuyết...
59|Quá hợp làm nền cho▼sự thuần khiết của tớ!
60|À... mặt trời vàng ghê.
61|Hê hê... Mặt trời▼còn mê tớ không rời nữa!
62|Chạng vạng rồi...▼Mặt trời đi ngủ,▼tớ lên đồ đi chơi!
63|Ban đêm mới là lúc▼tớ tỏa sáng rực rỡ!
64|Ngôi sao như tớ▼thì phải thế chứ!
65|Đừng quá kích động▼vì Giờ Bí Ẩn nhé!▼Trẻ con lắm đấy!
66|Ơ... Ừm...▼Ối vui quá! Hú hú!
67|Khoan, hôm nay là▼sinh nhật cậu đúng không?
68|Chúc mừng sinh nhật, @0!
69|Xin lỗi... hôm nay▼tớ muốn ở một mình...'''
M={}
for line in raw.splitlines():
 k,sep,v=line.partition('|'); assert sep and k.isdecimal();n=int(k);assert n not in M;M[n]=v
rows=[json.loads(s) for s in f.read_text().splitlines()]
assert set(M)==set(range(len(rows)))
for i,o in enumerate(rows):
 assert o['vi'] is None
 en=o['en'];pre=PFX.match(en).group();tok=TOK.findall(en[len(pre):]);v=M[i]
 assert [int(x) for x in SLOT.findall(v)]==list(range(len(tok))),(i,tok,v)
 vi=pre+SLOT.sub(lambda m:tok[int(m.group(1))],v)
 assert TOK.findall(en)==TOK.findall(vi)
 assert vi.count('▼')<=max(2,en.count('▼')),(i,'pages',vi)
 assert unicodedata.normalize('NFC',vi)==vi
 o['vi']=vi
f.write_text(''.join(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n' for x in rows),encoding='utf8')
print('Translated',len(rows),f.name)