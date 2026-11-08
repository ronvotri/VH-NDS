#!/usr/bin/env python3
"""Magician's Quest batch 058; reproducible from checkpoint 057.
Manually translated distinct EN dialogue templates; maintain NDS control codes,
records, archive integrity. Batch 059 source staged but remains untranslated.
"""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import json, re, unicodedata, hashlib

HOME=Path('/mnt/data')
OLD=HOME/'MagiciansQuest-VietHoa-Checkpoint-057.zip'
NEW=HOME/'MagiciansQuest-VietHoa-Checkpoint-058.zip'
ROOT='MagiciansQuest_058'
PREFIX=re.compile(r"^(?:\$(?:024|023|022|034|040)(?:['0-9-]+)*;)+")
TOKEN=re.compile(r"\$\d{3}(?:'[0-9-]+)*;")
TARGETS=('0040.013','0040.014')

def jd(x):return json.dumps(x,ensure_ascii=False,separators=(',',':'))
def parsed(blob):return [json.loads(x) for x in blob.decode('utf8').splitlines() if x.strip()]
def body(s):return PREFIX.sub('',s)
def relname(s):return ROOT+'/'+s.split('/',1)[1]
def pth(s):return f'{ROOT}/translation/04-thoai/talkfigs__0eng__data__{s}.jsonl'

# Numbering = 1-based EN-body unique order. All unique lines are manually
# translated except identical lines reused verbatim from previous checkpoints.
MANUAL_013={
 1:'Hôm nọ hai cậu lén▼đi hẹn hò phải không?',
 2:'Chuẩn bài! Cậu lịch thiệp▼hơn tớ tưởng đấy!',
 4:'Hai cậu cứ lén ngồi▼niệm bùa yêu với nhau à?',
 5:'Tuyệt! Cậu lịch thiệp▼hơn tớ tưởng đấy!▼Rồi kết quả sao?',
 6:'Hai cậu cứ suốt ngày▼tâm sự chuyện yêu đương▼sến súa ấy hả?',
 7:'Chà, cũng lãng mạn đấy!▼Nhưng tớ chịu không nổi▼mấy chuyện ngọt xớt đâu!',
 8:'Nghe nói giờ ăn trưa,▼hai cậu còn đút nhau ăn...',
 9:'Hay quá! Nhưng...▼cậu không ngượng à?',
 10:'Hai cậu định cưới nhau▼thật đấy à?!',
 11:'Đỉnh! Thế mới gọi là▼sành điệu chứ!▼Ôi, tuổi trẻ yêu đương!',
 12:'Hai cậu còn viết▼thư tình cho nhau à?',
 13:"Tình yêu của $503'567;▼làm cậu khổ sở rồi nhỉ?▼",
 14:'Cũng hay đấy, nhưng...▼tớ không thích bị▼ràng buộc đâu.',
 15:'Hai cậu tính cùng nhau▼đi du lịch thật hả?!',
 16:'Xịn! Nhưng hai cậu▼định đi đâu vậy?',
 17:'H-hai cậu đã...▼trao... nhẫn cho nhau rồi?!',
 18:'Tuyệt! Nhưng tiếp theo▼định trao nhau cái gì?',
 19:'Hai cậu ở bên nhau▼đến tận sáng hôm sau à?!',
 20:'Thế cả đêm hai cậu▼làm gì vậy?',
 21:'Nghe đồn hai cậu▼sắp chia tay...',
 22:'Ừ thì... yêu nhau▼đôi khi cũng vậy mà.',
 23:'Muốn tâm sự với người▼từng trải thì cứ tìm tớ.▼Tớ luôn sẵn lòng nghe.',
 24:'Hôm nọ tớ nghe▼một chuyện khó tin lắm.▼Cậu đoán ra chưa?',
 25:'Cả thị trấn đang bàn▼chuyện hai cậu đi hẹn hò▼kiểu người lớn đó.',
 26:'Đỉnh thật! Nhưng▼hẹn hò kiểu người lớn▼thì làm những gì nhỉ?',
 27:'Có tin đồn hai cậu▼đến một chỗ vắng vẻ...',
 28:'rồi làm chuyện gì đó▼đáng ngờ lắm.',
 29:'Rốt cuộc hai cậu▼đã làm gì thế?',
 30:'Lần tới cho tớ▼tham gia với nhé!',
 31:'Nghe đồn cậu đang▼bắt cá hai tay...',
 32:'Ôi, gan thật đấy!▼Nhưng tội người▼đang hẹn hò với cậu...',
 33:'Nghe đồn cậu đang▼bí mật hẹn hò với ai đó...',
 34:'Tuyệt mà! Nhưng sao▼lại phải giấu kín thế?',
 35:'Hai cậu sắp▼chia tay thật à?',
 36:'Tớ không hỏi lý do đâu.▼Nghe mà buồn quá...',
 37:'Hai cậu rồi sẽ▼ổn thôi, đúng không?',
 38:"Nghe nói $503'567;▼đang buồn bực lắm...",
 39:'Có chuyện gì cứ kể tớ nghe.▼Tớ sẵn lòng lắng nghe,▼nhưng cần cà phê đậm đấy!',
 40:'Nghe nói hai cậu cãi nhau.▼Chắc tại quý nhau quá,▼đúng không?',
 41:'Hả?! Hai cậu▼chia tay rồi sao?!',
 42:'Hai cậu đang▼chiến tranh lạnh à?',
 43:'Hmm... Hai cậu từng thân▼thế cơ mà. Không làm hòa▼thì tiếc lắm!',
 44:'Thị trấn đang râm ran▼một tin đồn thú vị về cậu...',
 45:'Nghe nói cậu đang▼tranh giành một người▼với ai đó, thật hả?',
 46:'Thế mới gọi là phiêu lưu!▼Tớ cũng muốn thử▼tranh giành ai đó xem!',
 47:'Hai cậu đính hôn▼thật rồi à?!',
 48:'Định cưới luôn như thế à?▼Nghe có vẻ vất vả quá...',
 49:'Dạo này cậu thi▼bắt côn trùng hăng lắm hả?',
 50:'Đem cả danh dự ra đấu,▼đáng nể thật!▼Nhưng ai thua thì sao?',
 51:'Dạo này cậu cũng▼thi câu cá à?',
 52:'Nghe nói hai cậu hợp cạ▼đến mức định lập▼cặp đôi tấu hài luôn!',
 53:'Tớ sẽ cổ vũ hết mình!▼Mong hai cậu nổi tiếng,▼để tớ xin chữ ký!',
 54:'Hai cậu thân nhau ghê!▼Cứ như anh em▼thất lạc lâu năm ấy...',
 55:'Có anh chị em thật tuyệt,▼dù đôi khi phải xa nhau.',
 56:'Nghe đồn vì quá thân▼nên hai cậu tính▼dọn về sống chung.',
 57:'Sống chung nghe vui đấy!▼Cậu thấy vậy không?',
 58:'Hai cậu thân thiết thật!▼Nhưng có người bảo▼là thân QUÁ mức ấy.',
 59:'Tớ thấy vui mà,▼có gì đâu nhỉ...',
 60:"Cả thị trấn bảo▼cậu chỉ thích chơi▼với $503'567; thôi.",
 61:"Tớ biết cậu rất quý▼$503'567;, nhưng thỉnh thoảng▼cũng chơi với bạn khác nhé!",
 62:'Cân bằng mới là▼bí quyết của mọi chuyện!',
 63:'Tớ đã thấy▼có gì đó sai sai mà...',
 64:'Bị đá vì cãi nhau▼thật đấy à?!',
 65:'Có người đồn cậu sẽ▼rời thị trấn vì quá▼đau khổ chuyện tình cảm...',
 66:'Ai cũng bảo học kỳ tới▼cậu định chuyển trường.',
 67:'Ừm... Mất một người bạn▼lúc nào cũng buồn.',
 68:'Nhưng cậu thật sự▼phải đi sao?',
 69:'Nghe đồn cậu đang▼niệm phép để chiếm▼cả thế giới...',
 70:'Hay là cậu cứ▼bình tĩnh lại một chút đi.',
 71:'Người ta bảo cậu▼thật ra là người ngoài hành tinh!',
 72:'Hấp dẫn ghê!▼Kể tớ nghe về▼hành tinh quê cậu đi!',
 73:'Có tin đồn cậu▼đang bị nhập hồn...',
 74:"Ghê nha! Kể tớ nghe▼về 'thế giới bên kia' đi!",
 75:'Ơ... cậu đang▼giấu chuyện gì à?',
 76:'Nghe đồn cậu là▼siêu anh hùng đi▼bảo vệ công lý!',
 77:'Ngầu quá! Cho tớ xem▼siêu năng lực của cậu đi!',
 78:'Nghe nói cậu phải lòng▼một người lớn tuổi hơn...',
 79:'Tớ thấy chẳng sao,▼miễn người đó tốt bụng!',
}
MANUAL_014={
 1:'Vụ này tớ ủng hộ cậu!',
 3:'Có người bảo cậu là▼loài côn trùng gì đó...',
 4:'Yên tâm! Dù cậu là▼sinh vật bé mọn cỡ nào,▼tớ vẫn là bạn cậu!',
 5:'Nghe nói đêm nọ▼cậu mộng du, rồi▼ngã xuống sông...',
 6:'Lạ đời ghê! Ước gì▼được nghiên cứu▼về cậu một lần!',
 7:'Ai cũng bảo cậu▼đa tình lắm...',
 8:'Không sao! Dù cậu▼có kém lịch thiệp đến đâu,▼tớ vẫn chơi với cậu.',
 9:'Cậu nhột lắm hả?',
 10:'Nghe nói cậu giàu▼đến mức tối nào cũng▼thức đếm tiền, đúng không?',
 11:'Giàu thế thì đầu tư▼vào người từng trải▼như tớ đây!',
 12:'Nghe đồn cậu là hải tặc,▼đi khắp thế giới▼săn kho báu...',
 14:'Người ta thấy cậu▼vừa đào hố trong rừng▼vừa khóc, thật sao?',
 16:'Dạo này tớ nghe▼thiên hạ bàn về cậu▼nhiều lắm đấy...',
 17:'Cậu LẠI giải quyết▼thêm vụ rắc rối nữa à?!',
 18:'Đáng nể! Có cậu ở đây,▼thị trấn này sẽ▼luôn yên bình!',
 19:'Cậu có chăm học không?',
 20:'Hê hê... Coi chừng nhé!▼Tớ không định thua đâu!',
 21:'Ai cũng bảo cậu▼là đứa trẻ ngoan...',
 22:'Từ khi nào cậu▼thành đứa trẻ hư thế?!',
 23:'Chà, nhóc quậy phá đây mà!▼Tớ mà là cậu thì▼bớt quậy chút đấy!',
 24:'Tớ nghe mấy lời đồn▼đang râm ran ở trường...',
 27:'Tớ muốn khen là ngầu,▼nhưng vụ này quá sức▼chịu đựng của tớ!',
}
assert len(MANUAL_013)==78, len(MANUAL_014)==22

with ZipFile(OLD) as old:
    assert old.testzip() is None
    prev={relname(n):old.read(n) for n in old.namelist() if not n.endswith('/')}
entries=dict(prev)
reuse={}
# Reuse only exact English wording from this checkpoint, and only where a
# single unambiguous prior Vietnamese translation exists. Some game phrases
# are context-dependent; use manual translations for all others.
for suf in ('0040.011','0040.012'):
    for r in parsed(prev[pth(suf)]):
        reuse[body(r['en'])]=body(r['vi'])
delta=[]
for suffix,manual in zip(TARGETS,(MANUAL_013,MANUAL_014)):
    rows=parsed(prev[pth(suffix)])
    assert len(rows)==120 and all(r['vi'] is None for r in rows),suffix
    unique=list(dict.fromkeys(body(r['en']) for r in rows))
    assert len(unique)==(79 if suffix.endswith('.013') else 56),len(unique)
    translations={}
    for i,en in enumerate(unique,1):
        if i in manual: vi=manual[i]
        elif en in reuse: vi=reuse[en]
        else: raise ValueError(f'Missing Vietnamese: {suffix} unique EN #{i}: {en}')
        assert vi==unicodedata.normalize('NFC',vi), (suffix,i,'NFC')
        assert TOKEN.findall(en)==TOKEN.findall(vi), (suffix,i,'token',en,vi)
        assert vi.count('▼')<=3, (suffix,i,'lines',vi)
        assert all(len(TOKEN.sub('',line))<=34 for line in vi.split('▼')), (suffix,i,'width',vi)
        translations[en]=vi
    assert len(translations)==len(unique)
    reuse.update(translations)
    out=[]
    for r in rows:
        match=PREFIX.match(r['en'])
        p=match.group(0) if match else ''
        vi=p+translations[body(r['en'])]
        assert TOKEN.findall(r['en'])==TOKEN.findall(vi), (suffix,r['id'],'token')
        assert vi==unicodedata.normalize('NFC',vi)
        assert '\n' not in vi and '\r' not in vi and '\t' not in vi
        assert vi.count('▼')<=3 and all(len(TOKEN.sub('',line))<=34 for line in vi.split('▼'))
        out.append({**r,'vi':vi})
        delta.append({'file':f'04-thoai/talkfigs__0eng__data__{suffix}.jsonl','id':r['id'],'en':r['en'],'old_vi':None,'vi':vi,'ctx':r['ctx']})
    entries[pth(suffix)]=('\n'.join(jd(r) for r in out)+'\n').encode('utf8')
    ident=suffix.replace('.','_')
    entries[f'{ROOT}/vi_{ident}.txt']=('\n'.join(r['vi'] for r in out)+'\n').encode('utf8')
    entries[f'{ROOT}/manual_{ident}.tsv']=('id\ten\tvi\tctx\n'+'\n'.join('\t'.join(map(str,(r['id'],r['en'],r['vi'],r['ctx']))) for r in out)+'\n').encode('utf8')
    print(f'{suffix}: 120 records, {len(unique)} unique EN bodies, manually translated {len(manual)} templates, reused {len(unique)-len(manual)}')
assert len(delta)==240
entries[f'{ROOT}/DELTA-058.jsonl']=('\n'.join(jd(r) for r in delta)+'\n').encode('utf8')

checkpoint=f'''# Magician’s Quest: Mysterious Times — Checkpoint 058

**Ngày:** 08/11/2026 · **Repo:** `ronvotri/VH-NDS` · `Magicians-Quest-Mysterious-Times/`

| Tệp | Trang mới | Nội dung |
|---|---:|---|
| `0040.013` | 120 | Tin đồn tình cảm, bùa yêu, hẹn hò, thi đấu côn trùng/câu cá, bí mật về siêu anh hùng |
| `0040.014` | 120 | Các câu chuyện về bạn bè, mộng du, tiền bạc, hải tặc và phản ứng với lời đồn |

**Tiến độ:** **16.032/55.976 (28,64%)**, tăng 240 từ checkpoint 057 (15.792); hội thoại NPC **12.907/52.608**.

**Thành phẩm:** 2 tệp JSONL dịch, 2 bảng `manual_0040_013.tsv` / `manual_0040_014.tsv`, `vi_0040_013.txt` / `vi_0040_014.txt`, `DELTA-058.jsonl`, `QA-058.md`, `build_058.py`, `qa_058.py`.

**QA:** kiểm 501 JSONL/55.976 bản ghi giữa checkpoint 057 và 058. Chỉ 240 trường `vi` mới được thay từ `null` sang tiếng Việt. Toàn bộ 15.792 bản dịch cũ, `id/en/ctx`, bản ghi lặp và các mã `$...;` được bảo toàn. Tối đa 3 `▼`, 34 ký tự tĩnh mỗi đoạn, Unicode NFC.

**Chưa kiểm thử trên ROM NDS.** Tên nhân vật động `$503'567;` cần kiểm giới hạn hiển thị khi chạy thật. Đợt 059: `0040.015` và `0040.016` giữ nguyên nguồn trong ZIP 058, sẵn sàng dịch.
'''
qa=f'''# QA — Magician’s Quest · Đợt 058

- **PASS:** 501 JSONL / 55.976 mục giữa checkpoint 057 và 058.
- **PASS:** đúng 240 bản dịch mới (`0040.013` và `0040.014`, 120 mục/tệp); **15.792 → 16.032/55.976 (28,64%)**; NPC **12.667 → 12.907/52.608**.
- **PASS:** không sửa 15.792 bản dịch cũ, id, en, ctx; các tệp JSONL khác giữ nguyên từng byte.
- **PASS:** tất cả token `$...;` và thứ tự của chúng giữ nguyên, gồm `$024` / `$023` / `$022` / `$503'567;` / các token biểu cảm.
- **PASS:** Unicode NFC, không có dấu CR/LF/TAB trong `vi`, tối đa 3 `▼` và 34 ký tự tĩnh mỗi đoạn (bỏ mã token).
- **PASS:** CRC của ZIP và tổng số tệp, mục không đổi.
- **CHƯA TEST:** ROM NDS / biến tên nhân vật mở rộng / font thực tế.

Tái kiểm: `python qa_058.py /mnt/data/MagiciansQuest-VietHoa-Checkpoint-057.zip /mnt/data/MagiciansQuest-VietHoa-Checkpoint-058.zip`.
'''
entries[f'{ROOT}/CHECKPOINT-2026-11-08-DOT-58.md']=checkpoint.encode()
entries[f'{ROOT}/QA-058.md']=qa.encode()
entries[f'{ROOT}/README.md']=(f'**Checkpoint mới nhất: 058 (08/11/2026) — 16.032 / 55.976 mục (28,64%).** Thêm 240 trang NPC (`0040.013`, `0040.014`): chuyện hẹn hò, lời đồn, bạn bè, thi đấu và những bí mật vui nhộn. Xem `CHECKPOINT-2026-11-08-DOT-58.md`, `QA-058.md`, `DELTA-058.jsonl`. Nguồn tiếp: `0040.015` và `0040.016` (chưa dịch).\n\n'+entries[f'{ROOT}/README.md'].decode('utf8')).encode('utf8')
entries[f'{ROOT}/BAN_GIAO.md']=(f'## Checkpoint 058 — 08/11/2026\n\n- **16.032/55.976 (28,64%)**, NPC **12.907/52.608**; thêm 240 trang của `0040.013` và `0040.014`.\n- Dịch mới 100 mẫu câu khác nhau và dùng lại 35 mẫu trùng trong hai tệp/đợt cũ; giữ nguyên toàn bộ ID, EN, CTX, mã NDS, bản ghi lặp.\n- Đã QA 501 JSONL / 55.976 bản ghi với checkpoint 057: chỉ điền 240 `vi`, giữ 15.792 bản dịch cũ, các tệp còn lại không đổi.\n- ZIP đầy đủ `MagiciansQuest-VietHoa-Checkpoint-058.zip` lưu Thư viện `Dịch giả lập`, có `DELTA-058.jsonl`, bảng EN–VI, QA và script build. Chưa test trực tiếp trên ROM.\n- Đợt 059 tiếp `0040.015` và `0040.016` (đã có trong ZIP).\n\n'+entries[f'{ROOT}/BAN_GIAO.md'].decode('utf8')).encode('utf8')
entries[f'{ROOT}/build_058.py']=Path(__file__).read_bytes()
entries[f'{ROOT}/qa_058.py']=(HOME/'qa_058.py').read_bytes()

with ZipFile(NEW,'w',ZIP_DEFLATED,compresslevel=6) as z:
    for n,data in sorted(entries.items()):z.writestr(n,data)
with ZipFile(NEW) as z:assert z.testzip() is None
print('CREATED',NEW, 'file count',len(entries),'size',NEW.stat().st_size,'sha256',hashlib.sha256(NEW.read_bytes()).hexdigest())
