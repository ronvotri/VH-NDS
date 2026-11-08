#!/usr/bin/env python3
"""Build Magician's Quest checkpoint 068 from checkpoint 067.
Run: python build_068.py [checkpoint067.zip] [checkpoint068.zip]
Only 240 vi fields are new; all other localization JSONL bytes remain unchanged.
"""
import sys,json,zipfile,re,unicodedata,collections,hashlib
from pathlib import Path
from mq068_translate import MANUAL
HERE=Path(__file__).resolve().parent
OLD=Path(sys.argv[1]) if len(sys.argv)>1 else Path('/mnt/data/MagiciansQuest-VietHoa-Checkpoint-067.zip')
NEW=Path(sys.argv[2]) if len(sys.argv)>2 else Path('/mnt/data/MagiciansQuest-VietHoa-Checkpoint-068.zip')
ROOT_OLD='MagiciansQuest_067/'
ROOT_NEW='MagiciansQuest_068/'
TOKEN=re.compile(r"\$\d{3}(?:'[0-9-]+)*;")
PREFIX=re.compile(r"^(?:\$(?:034|024|023|022|004|040)(?:['0-9-]+)*;)+")
SUFFIX=re.compile(r"(?:\$(?:079|074|019|018|073|033|085|032)(?:['0-9-]+)*;)+$")
TARGETS=('0041.011','0041.012')

def split(s):
    m=PREFIX.match(s);p=m.group() if m else '';body=s[len(p):];m=SUFFIX.search(body)
    return p,body[:m.start()] if m else body,m.group() if m else ''

def validate(r,s):
    assert isinstance(s,str) and s and unicodedata.normalize('NFC',s)==s,(r['id'],'NFC/empty')
    assert TOKEN.findall(r['en'])==TOKEN.findall(s),(r['id'],'token order',TOKEN.findall(r['en']),TOKEN.findall(s))
    assert s.count('▼')<=3,(r['id'],'break count',s)
    assert all(c not in s for c in '\r\n\t'),(r['id'],'newline/tab')
    assert all(len(TOKEN.sub('',part))<=34 for part in s.split('▼')),(r['id'],'width',[(len(TOKEN.sub('',part)),part) for part in s.split('▼')])

with zipfile.ZipFile(OLD) as z:
    assert z.testzip() is None,'checkpoint 067 CRC error'
    sourcepaths=[p for p in z.namelist() if p.startswith(ROOT_OLD+'translation/') and p.endswith('.jsonl')]
    assert len(sourcepaths)==501,len(sourcepaths)
    previous=collections.defaultdict(collections.Counter)
    total=old_trans=0
    for p in sourcepaths:
        for line in z.read(p).decode('utf-8').splitlines():
            row=json.loads(line);total+=1
            if row['vi'] is not None:
                old_trans+=1
                previous[split(row['en'])[1]][split(row['vi'])[1]]+=1
    assert (total,old_trans)==(55976,18132),(total,old_trans)
    preexisting_en=set(previous)
    changes={};delta=[];stats=[];used_manual=set();used_reused=set()
    for suffix in TARGETS:
        rel=f'translation/04-thoai/talkfigs__0eng__data__{suffix}.jsonl'
        src=[json.loads(x) for x in z.read(ROOT_OLD+rel).decode('utf-8').splitlines()]
        assert len(src)==120 and all(r['vi'] is None for r in src),suffix
        unique=list(dict.fromkeys(split(r['en'])[1] for r in src))
        assert len(unique)==(35 if suffix=='0041.011' else 55),(suffix,len(unique))
        lookup={}
        for en in unique:
            if en in previous:
                lookup[en]=previous[en].most_common(1)[0][0]
                if en in preexisting_en: used_reused.add(en)
            elif en in MANUAL:
                lookup[en]=MANUAL[en]
                used_manual.add(en)
            else:raise AssertionError(('MISSING MANUAL',suffix,en))
        rows=[];tsv=['id\ten\tvi\tctx']
        for row in src:
            prefix,en,suffix_tokens=split(row['en'])
            vi=unicodedata.normalize('NFC',prefix+lookup[en]+suffix_tokens)
            validate(row,vi)
            rr={**row,'vi':vi};rows.append(rr);delta.append(rr)
            tsv.append('\t'.join(str(rr[k]) for k in ('id','en','vi','ctx')))
        changes[rel]=(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in rows)).encode('utf-8')
        changes[f'manual_{suffix.replace(".","_")}.tsv']=('\n'.join(tsv)+'\n').encode('utf-8')
        changes[f'vi_{suffix.replace(".","_")}.txt']=('\n'.join(r['vi'] for r in rows)+'\n').encode('utf-8')
        for en,vi in lookup.items():previous[en][vi]+=1
        stats.append((suffix,len(rows),len(unique)))
    assert len(used_manual)==len(MANUAL)==50,(len(used_manual),len(MANUAL),set(MANUAL)-used_manual)
    assert len(used_reused)==31,len(used_reused)
    assert len(delta)==240
    changes['DELTA-068.jsonl']=(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in delta)).encode('utf-8')
    after=old_trans+240;npc=15007+240;pct=100*after/total
    assert (after,npc)==(18372,15247)
    changes['QA-068.md']=f'''# QA — Magician's Quest · Đợt 068

- **PASS:** So sánh checkpoint 067 → 068 trên 501 JSONL / 55.976 bản ghi.
- **PASS:** Điền 240 trường `vi`: 0041.011 (120), 0041.012 (120). **18.132 → {after:,}/55.976 ({pct:.2f}%)**; hội thoại NPC **15.007 → {npc:,}/52.608**.
- **PASS:** Giữ nguyên 18.132 bản dịch cũ; 499 JSONL khác byte-identical; ID/EN/CTX không đổi.
- **PASS:** Mã `$...;` giữ nguyên thứ tự; Unicode NFC; ≤3 dấu `▼`/trang; ≤34 ký tự tĩnh/đoạn.
- **PASS:** 81 mẫu tiếng Anh riêng biệt, 31 mẫu tái dùng bản dịch có sẵn; 50 mẫu mới biên tập thủ công.
- **PASS:** `DELTA-068.jsonl`, hai bảng đối chiếu EN–VI, CRC ZIP, QA chéo hai checkpoint.
- **CHƯA THỬ:** Hiển thị trong ROM NDS và độ rộng thực khi các biến tên dài được thay thế.
'''.encode('utf-8')
    changes['CHECKPOINT-2026-11-09-DOT-68.md']=f'''# Magician's Quest — Checkpoint 068 (09/11/2026)

- **Tiến độ:** {after:,} / 55.976 ({pct:.2f}%); hội thoại NPC {npc:,} / 52.608.
- **Bổ sung:** 240 trang thoại trong `0041.011` và `0041.012` (120/tệp); 81 mẫu câu khác nhau.
- **Nội dung:** Tin đồn học đường, tình yêu đôi lứa, hẹn hò, những lời trêu ghẹo và cảnh báo về mối quan hệ; giọng tớ–cậu.
- **Thuật ngữ / kỹ thuật:** 50 mẫu biên tập thủ công, 31 mẫu tái dùng; bảo toàn token `$...;`, Unicode NFC, ngắt `▼`, chiều rộng 34 ký tự tĩnh.
- **Bảo toàn:** 18.132 bản dịch cũ, ID/EN/CTX, 499 tệp thoại JSONL khác byte-identical; QA toàn 501 JSONL.
- **Bàn giao:** `DELTA-068.jsonl`, `manual_0041_011.tsv`, `manual_0041_012.tsv`, `QA-068.md`, `build_068.py`, `qa_068.py`, `mq068_translate.py`.
- **ZIP:** `MagiciansQuest-VietHoa-Checkpoint-068.zip` trong thư viện `/Dịch giả lập`.
- **Lưu ý:** Chưa test hiển thị ROM NDS; độ dài biến động `$535`/`$538` cần kiểm thử trong game.
- **Tiếp 069:** `0041.013` và `0041.014` (120 trang/tệp) đã có nguồn trong ZIP.
'''.encode('utf-8')
    pre_readme=f'**Checkpoint mới nhất: 068 (09/11/2026) — 18.372/55.976 ({pct:.2f}%).** +240 trang NPC (`0041.011`, `0041.012`). QA 501 JSONL PASS; giữ 18.132 mục dịch trước. Xem `CHECKPOINT-2026-11-09-DOT-68.md`, `QA-068.md`, `DELTA-068.jsonl`. Tiếp `0041.013`, `0041.014` (120 trang/tệp).\n\n'
    pre_handoff=f'''## Checkpoint 068 — 09/11/2026

- **{after:,}/55.976 ({pct:.2f}%)**, thoại NPC **{npc:,}/52.608**; thêm 240 trang.
- Dịch xong `0041.011`/`0041.012` (120 trang/tệp): tin đồn, tình bạn, hẹn hò, ghen tuông, lời khuyên.
- QA 501 JSONL: chỉ điền 240 `vi`; 18.132 bản dịch cũ và ID/EN/CTX bảo toàn, 499 JSONL không đổi.
- ZIP: `/Dịch giả lập/MagiciansQuest-VietHoa-Checkpoint-068.zip`, đầy đủ dữ liệu và script build/QA, **chưa kiểm thử ROM NDS**.
- Đợt 069 tiếp `0041.013`/`0041.014` (120 trang/tệp), nguồn đã có trong ZIP.

'''
    changes['README.md']=(pre_readme+z.read(ROOT_OLD+'README.md').decode('utf-8')).encode('utf-8')
    changes['BAN_GIAO.md']=(pre_handoff+z.read(ROOT_OLD+'BAN_GIAO.md').decode('utf-8')).encode('utf-8')
    changes['build_068.py']=Path(__file__).read_bytes()
    changes['mq068_translate.py']=(HERE/'mq068_translate.py').read_bytes()
    qa_script=HERE/'qa_068.py'
    assert qa_script.exists(),'qa_068.py must exist'
    changes['qa_068.py']=qa_script.read_bytes()
    NEW.parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(NEW,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=7,allowZip64=True) as out:
        for old_name in z.namelist():
            assert old_name.startswith(ROOT_OLD),old_name
            relative=old_name[len(ROOT_OLD):]
            out.writestr(ROOT_NEW+relative,changes.pop(relative,z.read(old_name)))
        for relative,data in sorted(changes.items()):
            out.writestr(ROOT_NEW+relative,data)
print('WROTE',NEW,NEW.stat().st_size,'bytes; stats',stats,'manual',len(used_manual),'reuse',len(used_reused),'pct',f'{pct:.2f}')
print('SHA256',hashlib.sha256(NEW.read_bytes()).hexdigest())
