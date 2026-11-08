# -*- coding: utf-8 -*-
"""Bản biên tập thủ công đợt 069, tái dùng các câu trùng tuyệt đối từ checkpoint 068."""
import zipfile,json,re,collections,unicodedata,hashlib,pathlib,datetime,io,os
OLD=pathlib.Path('/mnt/data/MagiciansQuest-VietHoa-Checkpoint-068.zip')
OUT=pathlib.Path('/mnt/data/MagiciansQuest-VietHoa-Checkpoint-069.zip')
root_old='MagiciansQuest_068/'
root_new='MagiciansQuest_069/'
prefix_re=re.compile(r"^(?:\$\d{3}(?:[\d'-]+)?;)+")
token_re=re.compile(r"\$\d{3}(?:[\d'-]+)?;")

# Các chỉ số ứng với lần xuất hiện đầu của câu EN sau khi bỏ mã điều khiển mở đầu.
T={
0: 'Thích người khác là chuyện thường,▼nhưng lừa dối rồi làm▼người yêu đau lòng thì không.',
2: 'Có tin đồn rằng cậu▼đang lén qua lại▼với một người khác...',
3: 'Tớ luôn tin cậu, nhưng▼nếu tin đó là thật,▼chắc tớ phải nghĩ lại...',
4: 'Nghe nói hai cậu▼sắp chia tay. Thật à?',
5: 'Hai cậu có chia tay▼cũng chẳng liên quan▼đến tớ, nhưng...',
6: 'nếu cần người tâm sự,▼cứ tìm tớ nhé.',
7: 'Này, hai cậu vẫn ổn chứ?',
8: "Nghe nói $503'567;▼đang dỗi đấy.",
9: "Cậu làm gì $503'567;▼giận à? Nếu có thì▼mau xin lỗi đi!",
10: 'Nghe nói hai cậu cãi nhau.▼Đang giả vờ kiêu▼để làm giá đấy à?',
11: 'Làm giá chút thì được,▼nhưng lâu quá là▼phản tác dụng đấy!',
12: 'Vậy là hai cậu▼bất đồng ý kiến à...?',
13: 'Nếu cần tâm sự,▼cậu biết tìm tớ ở đâu rồi.',
14: 'Khoan, hai cậu bị cận à?▼Sao lại chẳng▼nhìn cùng một hướng?',
15: 'Hai cậu không còn▼là bạn nữa à?',
16: 'Hai cậu từng thân thế mà!▼Làm hòa đi chứ!',
17: 'Bỏ cái tôi xuống▼và chủ động làm hòa đi!▼Không là hối hận đấy!',
18: 'Có chuyện đồn vui lắm▼về hai cậu đấy!',
19: 'Nghe nói chuyện tình cảm▼của cậu dạo này▼lắm sóng gió nhỉ!',
20: 'Ít ra cũng thú vị hơn,▼đúng không?',
21: 'Hai cậu đính hôn rồi à?',
22: 'Thế là đám cưới này▼do người khác sắp đặt à?▼Mỗi người mỗi ý, nhưng...',
23: 'tớ chẳng đời nào để ai▼chọn bạn đời hộ đâu!',
24: 'Dạo này cậu bắt bọ▼đến toát mồ hôi hột nhỉ?',
25: 'Toát mồ hôi hột á?▼Nghe ngầu ghê!▼Tớ cũng muốn thử!',
26: 'Dạo này cậu câu cá▼đến toát mồ hôi hột nhỉ?',
27: 'Hai cậu tấu hài quá!▼Nghe đồn sắp lập▼hẳn nhóm hài đấy!',
28: 'Tớ ủng hộ hết mình!▼Nhớ cho tớ chữ ký,▼rồi nổi tiếng nhé!',
29: 'Hai cậu dạo này thân ghê!▼Có khi là anh em▼thất lạc đấy nhỉ?',
30: 'Ai cũng đang nói thế đấy.',
31: 'Dù là thật cũng đừng lo.▼Có anh chị em▼vẫn là chuyện tốt mà!',
32: 'Nghe đồn hai cậu▼định sống chung vì▼lúc nào cũng dính nhau.',
33: 'Sống chung nghe vui đó!▼Lúc nào cũng có▼người để trò chuyện.',
34: 'Bạn thân thì tốt,▼nhưng thiên hạ bảo▼hai cậu thân QUÁ mức.',
35: 'Họ còn bảo hai cậu▼giả vờ thân thiết,▼thật ra là đối thủ!',
36: "Có tin đồn dạo này▼cậu chỉ chơi với▼$503'567; thôi đấy.",
37: 'Dù thân nhau đến mấy,▼cũng nên chơi▼với bạn khác nữa nhé!',
38: 'Bảo sao trước đó▼tớ thấy cậu lạ lạ...',
39: 'Thế cậu bị đá▼vì cãi nhau to à?',
40: 'Dù ai cũng nghĩ cậu sai,▼tớ vẫn đứng▼về phía cậu!',
41: 'Nghe nói sau cú chia tay,▼cậu định đi xa▼một chuyến dài...',
42: 'Có gì chất chứa trong lòng,▼cứ kể tớ nghe nhé.',
43: 'Nghe đồn cậu▼sắp chuyển trường à?',
44: 'Tớ không cản đâu.▼Ai cũng phải tự chọn▼con đường của mình mà.',
45: 'Nghe nói cậu đang▼niệm chú để▼thống trị thế giới...',
46: 'Đến ngày đó nhớ cho tớ▼làm cánh tay phải nhé!',
47: 'Có lời đồn cậu▼thật ra là người ngoài hành tinh!',
48: 'Tớ luôn muốn lên vũ trụ!▼Cho tớ đi với!▼Lúc nào tớ cũng rảnh!',
49: 'Nghe nói cậu▼bị ma nhập rồi...!',
50: 'Không phải thật chứ?▼Cậu mà là ma thì▼tình bạn này căng đấy!',
51: 'Cậu... cậu không giấu▼tớ chuyện gì đấy chứ?',
52: 'Có lời đồn cậu là▼anh hùng bảo vệ công lý!',
53: 'Ừm... lúc tớ nghịch ngợm,▼cậu nhắm mắt▼cho qua được không?',
54: 'Nghe nói cậu thầm thích▼ai đó trong trường này...',
55: 'Chắc cậu chẳng đơn độc!▼Ở đây có khối▼người nổi tiếng mà!',
56: 'Có tin đồn cậu▼thật ra là loài côn trùng!',
57: 'Đừng lo! Dù là ong bắp cày▼hay nhện thì cậu▼vẫn là bạn tớ!',
58: 'Nghe nói cậu mộng du,▼rồi ngã xuống sông đấy.',
59: 'Cậu gặp chuyện gì buồn à?▼Nhớ là luôn có tớ▼để tâm sự nhé!',
60: 'Nghe nói cậu là▼người lãng mạn kín tiếng...',
61: 'Đừng bận tâm lời thiên hạ.▼Dù sao tớ vẫn▼luôn là bạn cậu!',
62: 'Nghe nói cậu▼sợ bị cù lắm, thật à?',
63: 'Đừng lo! Ai cù cậu,▼cứ hét lên là▼tớ chạy tới cứu ngay!',
64: 'Có thật cậu giàu đến mức▼tối nào cũng ngồi▼đếm tiền không?',
65: 'Nếu cậu giàu thế,▼tớ sẵn lòng giúp▼xài bớt tiền nhé...',
66: 'Nghe đồn cậu gom kho báu▼để trở thành hải tặc...',
67: 'Ừm... tớ hình dung ra▼cậu ra khơi dưới▼lá cờ đầu lâu rồi...',
68: 'Nghe đồn cậu đào hố▼trong rừng rồi khóc.',
69: 'Có chuyện gì vậy?',
70: 'Đừng ôm hết một mình!▼Có chuyện cứ▼tìm tớ nhé!',
71: 'Này! Tớ nghe danh▼cậu lâu rồi đấy!',
72: 'Cậu lại phá được án mới à?',
73: 'Có cậu ở đây thì▼thị trấn này còn▼vụ án nào bí ẩn nữa!',
74: 'Nghe nói cậu▼học chăm lắm nhỉ.',
75: 'Muốn luyện thêm▼thì làm bài tập▼hộ tớ nhé...',
76: 'Nghe nói cậu▼tốt bụng lắm...',
77: 'Có bạn bè được tiếng tốt▼làm tớ vui ghê!',
78: 'Cậu thành dân quậy▼từ khi nào vậy?',
79: 'Cậu bị sao thế?!▼Có chuyện khó nói▼cứ kể tớ nghe!',
80: 'Tớ nghe lời đồn▼trong trường rồi...',
95: 'Tớ nghĩ hai cậu nên▼giữ ý tứ hơn▼khi ở chỗ đông người.',
96: 'Đừng quên luôn có▼người đang nhìn đấy!',
101: 'Ít ra có chút kịch tính▼mới thú vị, nhỉ?',
102: 'Chắc cậu không cô đơn đâu!▼Trường này có mấy thầy cô▼được mến mộ lắm!',
103: 'Này, nghe chuyện này...',
105: 'Hai người đó gan thật,▼dám làm cả chuyện ấy.',
109: 'Tớ ghen... à không...▼Khụ khụ... Không có gì.',
}

def get_rows(z,suffix):
 return [json.loads(line) for line in z.read(f'{root_old}translation/04-thoai/talkfigs__0eng__data__{suffix}.jsonl').decode().splitlines()]

z=zipfile.ZipFile(OLD)
lookup=collections.defaultdict(collections.Counter)
for n in z.namelist():
 if n.startswith(root_old+'translation/') and n.endswith('.jsonl'):
  for line in z.read(n).decode('utf-8').splitlines():
   r=json.loads(line)
   if r['vi']:
    key=prefix_re.sub('',r['en'])
    val=prefix_re.sub('',r['vi'])
    lookup[key][val]+=1
new_rows={s:get_rows(z,s) for s in ('0041.013','0041.014')}
alltext={}
for s in new_rows:
 for r in new_rows[s]:
  k=prefix_re.sub('',r['en'])
  alltext.setdefault(k,[]).append(r)
keys=list(alltext.keys())
print('Unique',len(keys),'Manually translated',len(T))
assert len(keys)==111
missing=[i for i,k in enumerate(keys) if i not in T and k not in lookup]
assert not missing,missing
trans_map={}
for i,key in enumerate(keys):
 if i in T:v=T[i]
 else:v=lookup[key].most_common(1)[0][0]
 trans_map[key]=v
 assert unicodedata.normalize('NFC',v)==v,(i,v)
 old_tokens=token_re.findall(key)
 new_tokens=token_re.findall(v)
 if old_tokens != new_tokens:raise AssertionError(('Token mismatch',i,key,v,old_tokens,new_tokens))
 lens=[len(token_re.sub('',x)) for x in v.split('▼')]
 if max(lens)>34:raise AssertionError(('Overlength',i,lens,v))
 if len(lens)>4:raise AssertionError(('Too many page breaks',i,lens,v))
 if v.rstrip()!=v:raise AssertionError(('Trailing whitespace',i,v))

new_files={}
changes=[]
for suf,rows in new_rows.items():
 output=[]
 for r in rows:
  key=prefix_re.sub('',r['en']);pref=r['en'][:len(r['en'])-len(key)]
  vi=pref+trans_map[key]
  if token_re.findall(r['en'])!=token_re.findall(vi):
   raise AssertionError(('Token mismatch including prefix',suf,r['id'],r['en'],vi))
  v= dict(r);v['vi']=vi;output.append(v)
  changes.append(dict(v, file=f'translation/04-thoai/talkfigs__0eng__data__{suf}.jsonl'))
 n=f'translation/04-thoai/talkfigs__0eng__data__{suf}.jsonl'
 new_files[n]=''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in output)
 new_files[f'manual_{suf.replace(".","_")}.tsv']='id\ten\tvi\tctx\n'+''.join('\t'.join([r['id'],r['en'],r['vi'],str(r['ctx'])])+'\n' for r in output)
 new_files[f'vi_{suf.replace(".","_")}.txt']='\n'.join(r['vi'] for r in output)+'\n'
 print(suf,'rows',len(output),'new',len(output),'unique',len(set(prefix_re.sub('',r['en']) for r in rows)))

new_files['DELTA-069.jsonl']=''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in changes)
new_files['CHECKPOINT-2026-11-09-DOT-69.md']='''# Checkpoint 069 — Magician's Quest: Mysterious Times

- Ngày: 2026-11-09.
- Tiến độ: **18.612 / 55.976 (33,25%)**, +240 từ checkpoint 068.
- Thoại NPC: **15.487 / 52.608**.
- Tệp: `0041.013` (120 trang), `0041.014` (120 trang).
- Số mẫu câu phân biệt (bỏ mã tiền tố): 111; 24 mẫu câu từ cũ được tái dùng bằng EN khớp tuyệt đối, 87 mẫu còn lại được biên tập thủ công.
- Phong cách: bạn bè tớ–cậu; lời đồn, tình cảm, hẹn hò; mã `$...;`, `▼` và biến nhân vật giữ nguyên.
- QA: đối chiếu toàn bộ 501 tệp JSONL / 55.976 bản ghi với ZIP 068, chỉ cập nhật 240 `vi` từ null; không sửa ID, EN, CTX hoặc các `vi` đã có.
- Chưa kiểm thử trực tiếp trên ROM Nintendo DS.
- Đợt 070: `0041.015` và `0041.016` (nếu có; kiểm tra từ gói nguồn trước khi định số trang).
'''
new_files['README.md']=''
new_files['BAN_GIAO.md']=''
print('All new translated rows',len(changes))

# Gộp archive checkpoint mới từ gói cũ, giữ toàn bộ 501 JSONL và các tệp khác.
old_files={}
for info in z.infolist():
 if info.is_dir():continue
 rel=info.filename[len(root_old):] if info.filename.startswith(root_old) else info.filename
 old_files[rel]=z.read(info.filename)
assert len([p for p in old_files if p.startswith('translation/') and p.endswith('.jsonl')])==501
for path,s in new_files.items():
 if path not in ('README.md','BAN_GIAO.md'):
  old_files[path]=s.encode('utf-8')
readme=old_files['README.md'].decode('utf-8')
ban=old_files['BAN_GIAO.md'].decode('utf-8')
old_files['README.md']=('**Checkpoint mới nhất: 069 (09/11/2026): 18.612 / 55.976 (33,25%).** Bổ sung 240 trang thoại NPC `0041.013`–`0041.014`, QA toàn bộ 501 tệp nguồn; xem `CHECKPOINT-2026-11-09-DOT-69.md`, `QA-069.md`, `DELTA-069.jsonl`.\n\n'+readme).encode('utf-8')
old_files['BAN_GIAO.md']=('## Checkpoint 069 — 09/11/2026\n\n- Dịch 240/240 trang `0041.013` và `0041.014`, tiến độ 18.612/55.976 (33,25%).\n- Gói checkpoint đầy đủ, giữ nguyên các tệp nguồn và toàn bộ bản dịch trước. Kiểm tra QA toàn bộ; chưa kiểm thử trên ROM NDS.\n- Tiếp theo: hai tệp chưa dịch sau `0041.014`.\n\n'+ban).encode('utf-8')

# QA tĩnh toàn dự án + diff chuẩn với checkpoint 068
errors=[]; totals=[]; translated=0;old_translated=0;modified=[]
for name in sorted(p for p in old_files if p.startswith('translation/') and p.endswith('.jsonl')):
 old=[json.loads(x) for x in z.read(root_old+name).decode('utf-8').splitlines()]
 new=[json.loads(x) for x in old_files[name].decode('utf-8').splitlines()]
 if len(old)!=len(new):errors.append(f'row count changed: {name}')
 for i,(o,n) in enumerate(zip(old,new)):
  if any(o.get(k)!=n.get(k) for k in ('id','en','ctx')):errors.append(f'core changed {name}:{i}')
  old_translated+=o['vi'] is not None
  translated+=n['vi'] is not None
  if o['vi']!=n['vi']:
   modified.append((name,i))
   if o['vi'] is not None or not name.endswith(('0041.013.jsonl','0041.014.jsonl')):errors.append(f'unexpected change {name}:{i}')
  if n['vi'] is not None and not o['vi']:
   if token_re.findall(n['en'])!=token_re.findall(n['vi']):errors.append(f'token mismatch {name}:{i}')
   if unicodedata.normalize('NFC',n['vi'])!=n['vi']:errors.append(f'NFC mismatch {name}:{i}')
   if len(n['vi'].split('▼'))>4:errors.append(f'too many breaks {name}:{i}')
   if max(len(token_re.sub('',s)) for s in n['vi'].split('▼'))>34:errors.append(f'overflow {name}:{i}')
 totals.append(len(new))
assert sum(totals)==55976,(sum(totals),totals[:3])
assert old_translated==18372,(old_translated)
assert translated==18612,translated
assert len(modified)==240,len(modified)
assert not errors,errors[:10]

with zipfile.ZipFile(OUT,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as dst:
 for rel,data in old_files.items():
  dst.writestr(root_new+rel,data)
with zipfile.ZipFile(OUT) as test:
 assert test.testzip() is None
 print('ZIP entries',len(test.namelist()),'size',OUT.stat().st_size,'SHA256',hashlib.sha256(OUT.read_bytes()).hexdigest())

qa=f'''# QA checkpoint 069\n\n- PASS: {len(totals)} JSONL, {sum(totals)} bản ghi.\n- Checkpoint 068: {old_translated} trường `vi` có nội dung.\n- Checkpoint 069: {translated} trường `vi` có nội dung (+{translated-old_translated}).\n- Chỉ thay đổi 240 trường `vi` tại hai tệp `0041.013` và `0041.014`.\n- Tất cả ID, EN, CTX và 18.372 bản dịch cũ được giữ nguyên.\n- So khớp toàn bộ token `$...;`, chuẩn Unicode NFC, tối đa 34 ký tự tĩnh/đoạn và tối đa 3 dấu `▼` cho 240 bản dịch mới.\n- ZIP toàn vẹn: PASS (CRC).\n- Chưa kiểm thử thực tế trên ROM NDS hoặc kiểm tra độ rộng ký tự do biến động.\n'''
# đưa QA vào ZIP bằng cách cập nhật archive 1 lần.
with zipfile.ZipFile(OUT,'a',compression=zipfile.ZIP_DEFLATED) as dst:
 dst.writestr(root_new+'QA-069.md',qa)
assert zipfile.ZipFile(OUT).testzip() is None
print('FINAL',OUT.stat().st_size,'entries',len(zipfile.ZipFile(OUT).namelist()))
