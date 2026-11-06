#!/usr/bin/env python3
"""Checkpoint 016 vs immutable 015. Check only vi changed; preserve all other metadata."""
import json,zipfile,pathlib,re,unicodedata,collections,sys
ROOT=pathlib.Path(__file__).resolve().parent
BASE=ROOT.parent/'MagiciansQuest-VietHoa-Checkpoint-015.zip'
TOKEN=re.compile(r"\$\d+(?:'[-\d]+)*;")
EXPECTED={'translation/04-thoai/talkfigs__0eng__data__0022.005.jsonl':120,
          'translation/04-thoai/talkfigs__0eng__data__0023.001.jsonl':120}
errors=[];changed=[];counter=collections.Counter();total=filled=0
with zipfile.ZipFile(BASE) as z:
    names=sorted(n for n in z.namelist() if n.startswith('MagiciansQuest_015/translation/') and n.endswith('.jsonl'))
    if len(names)!=501:errors.append(f'Expected 501 JSONL, got {len(names)}')
    for name in names:
        rel=name.split('/',1)[1]
        old=[json.loads(s) for s in z.read(name).decode('utf-8').splitlines()]
        p=ROOT/rel
        if not p.exists(): errors.append(f'Missing {rel}');continue
        new=[json.loads(s) for s in p.read_text('utf8').splitlines()]
        if len(old)!=len(new):errors.append(f'Row count {rel}');continue
        for a,b in zip(old,new):
            total+=1
            if set(a)!=set(b):
                errors.append(f'Unexpected fields {rel} {a.get("id")}')
            for key in set(a)|set(b):
                if key!='vi' and a.get(key)!=b.get(key):errors.append(f'Changed {key} {rel} {a["id"]}')
            value=b.get('vi')
            if value not in ('',None):filled+=1
            if a.get('vi')==value:continue
            if a.get('vi') not in ('',None):errors.append(f'Overwrote VI {rel} {a["id"]}')
            if not isinstance(value,str) or not value:errors.append(f'New blank {rel} {a["id"]}');continue
            if TOKEN.findall(a['en'])!=TOKEN.findall(value):errors.append(f'Control order {rel} {a["id"]}')
            if unicodedata.normalize('NFC',value)!=value:errors.append(f'NFC {rel} {a["id"]}')
            if any(char in value for char in '\t\n\r'):errors.append(f'Whitespace {rel} {a["id"]}')
            if value.count('▼')>3:errors.append(f'Too many breaks {rel} {a["id"]}')
            if any(len(TOKEN.sub('',line))>34 for line in value.split('▼')):
                errors.append(f'Line >34 {rel} {a["id"]}')
            cap=b.get('max_utf8_bytes')
            if cap and len(value.encode('utf-8'))>cap:errors.append(f'UTF8 bytes {rel} {a["id"]}')
            counter[rel]+=1
            changed.append({'file':rel.removeprefix('translation/'),'id':b['id'],'en':a['en'],'old_vi':a.get('vi'),'vi':value,'ctx':b.get('ctx')})
if total!=55976:errors.append(f'Total {total} instead of 55976')
if filled!=6285:errors.append(f'Filled {filled} instead of 6285')
if len(changed)!=240:errors.append(f'Changes {len(changed)} instead of 240')
if dict(counter)!=EXPECTED:errors.append(f'Changed paths {dict(counter)}')
if errors:
    print('FAIL',len(errors));print('\n'.join(errors[:120]));sys.exit(1)
(ROOT/'DELTA-016.jsonl').write_text(''.join(json.dumps(d,ensure_ascii=False,separators=(',',':'))+'\n' for d in changed),'utf8')
(ROOT/'QA-016.md').write_text('''# QA — Magician’s Quest checkpoint 016

- Đối chiếu checkpoint 015 bất biến: **501 tệp JSONL**, **55.976 bản ghi**.
- **240 trang thoại mới**, `0022.005` và `0023.001`, mỗi tệp 120 trang.
- **6.285 / 55.976** trường `vi` đã điền; nhóm hội thoại **3.160 / 52.608**.
- **PASS — 0 lỗi** khác biệt ngoài trường `vi`, ghi đè bản dịch, ID, tiếng Anh gốc, metadata, thứ tự mã điều khiển, NFC, TAB/CR/LF, ngắt dòng tối đa 3 và ký tự hiển thị tối đa 34/dòng.
- Bảo toàn `$500;`, `$503'327;`, `$503'309;`, `$515;`, các mã lựa chọn `$019'...;` và thẻ màu `$000'...;`.
- 240 bản ghi chi tiết tại `DELTA-016.jsonl`. Tất cả đều có bản tiếng Anh gốc + bản Việt đối chiếu.
- Ngôi xưng tớ–cậu với bạn bè, có phân biệt những câu tỏ tình/hẹn hò và nhân vật nóng tính.
- **Chưa kiểm thử độ rộng chữ theo font thực tế hoặc chạy trên ROM NDS**. Ngưỡng 34 ký tự chỉ là kiểm tra sơ bộ về bố cục.
''','utf8')
print('PASS',len(names),'files',total,'rows',filled,'filled',len(changed),'new',dict(counter))