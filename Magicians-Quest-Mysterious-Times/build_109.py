#!/usr/bin/env python3
"""Magician's Quest 109 — 720 dialogue pages in 0045.015-0045.020.

Rebuilds the checkpoint 109 ZIP directly from checkpoint 108, preserving untouched
files byte-for-byte. The English text remains the source of truth.
"""
from pathlib import Path
import collections, hashlib, json, re, unicodedata, zipfile
from translate_109 import translations as MANUAL

ROOT=Path('/mnt/data'); SRC=ROOT/'MagiciansQuest-VietHoa-Checkpoint-108.zip'; OUT=ROOT/'MagiciansQuest-VietHoa-Checkpoint-109.zip'
STAGE=ROOT/'MQ109';STAGE.mkdir(exist_ok=True)
OLD='MagiciansQuest_108/';NEW='MagiciansQuest_109/'
TALK='translation/04-thoai/talkfigs__0eng__data__'
TARGETS=[f'0045.{i:03d}' for i in range(15,21)]
NEXT=['0045.021','0045.022']+[f'0046.{i:03d}' for i in range(1,5)]
TOK=re.compile(r"\$\d{3}(?:'[-\d]+)*;")
LEAD=re.compile(r"^(?:\$(?:024|023|022|034|040|004)(?:'[-\d]+)*;)+")
TAIL=re.compile(r"(?:\$(?:079|073|032|033)(?:'[-\d]+)*;)+$")

def gitsha(b):return hashlib.sha1(b'blob '+str(len(b)).encode('ascii')+b'\0'+b).hexdigest()
def static_len(s):return len(TOK.sub('',s))
def wrap(s):
    """Wrap into 1–4 lines of at most 34 static Unicode codepoints.

    Dynamic NDS tokens have zero static width; their runtime text width needs
    later in-ROM validation.
    """
    # Tokens may be adjacent to plain characters, for instance '$000'3;Name'.
    words=s.split()
    assert words,repr(s)
    assert all(static_len(w)<=34 for w in words),f'Overwide word: {s}'
    lines=[]; cur=''
    for w in words:
        candidate=(cur+' '+w if cur else w)
        if static_len(candidate)>34 and cur:
            lines.append(cur);cur=w
        else:cur=candidate
    if cur:lines.append(cur)
    if len(lines)>4:raise ValueError(f'{len(lines)} lines: {s}\n{lines}')
    return '▼'.join(lines)

with zipfile.ZipFile(SRC) as z:
    assert z.testzip() is None
    files={n.removeprefix(OLD):z.read(n) for n in z.namelist() if n.startswith(OLD) and not n.endswith('/')}
jsnames=[n for n in files if n.startswith('translation/') and n.endswith('.jsonl')]
rowsby={n:[json.loads(s) for s in files[n].decode('utf8').splitlines()] for n in jsnames}
assert len(jsnames)==501 and sum(map(len,rowsby.values()))==55976
prior_count=sum(sum(r.get('vi') is not None for r in rs) for rs in rowsby.values())
assert prior_count==29211,prior_count
keys=[TALK+n+'.jsonl' for n in TARGETS]
for k in keys:assert k in rowsby and len(rowsby[k])==120 and all(r.get('vi') is None for r in rowsby[k]),k
prior=collections.defaultdict(collections.Counter)
for n,rs in rowsby.items():
    if n in keys:continue
    for r in rs:
        if isinstance(r.get('en'),str) and isinstance(r.get('vi'),str):prior[r['en']][r['vi']]+=1
known={en:c.most_common(1)[0][0] for en,c in prior.items()}
targetrows=[r for k in keys for r in rowsby[k]]
unique=list(dict.fromkeys(r['en'] for r in targetrows if r['en'] not in known))
assert len(unique)==492,(len(unique),len(MANUAL))
assert set(MANUAL)==set(range(1,len(unique)+1))
manual={en:MANUAL[i] for i,en in enumerate(unique,1)}

def to_vi(en):
    if en in known:return known[en],'TÁI DÙNG'
    pre=LEAD.match(en).group() if LEAD.match(en) else ''
    end=TAIL.search(en).group() if TAIL.search(en) else ''
    translated=pre+wrap(manual[en])+end
    if TOK.findall(en)!=TOK.findall(translated):
        raise AssertionError(f'Mismatched token sequence:\nEN {en}\nVI {translated}\n'+str(list(zip(TOK.findall(en),TOK.findall(translated)))))
    assert unicodedata.normalize('NFC',translated)==translated,(en,translated)
    assert translated.count('▼')<=3,(en,translated)
    assert all(static_len(part)<=34 for part in translated.split('▼')),(en,translated)
    assert all(c not in translated for c in ['“','”','…','—','–',' ']),(en,translated)
    return translated,'DỊCH MỚI'

newfiles=dict(files);delta=[];usage=collections.Counter();changed_slices=[]
for x in TARGETS:
    n=TALK+x+'.jsonl';out=[]
    for original in rowsby[n]:
        r=dict(original)
        vi,origin=to_vi(r['en']);r['vi']=vi
        assert r['vi'] and all(r[field]==v for field,v in original.items() if field!='vi')
        assert TOK.findall(r['en'])==TOK.findall(r['vi'])
        assert r['vi'].count('▼')<=3 and all(static_len(y)<=34 for y in r['vi'].split('▼'))
        usage[origin]+=1;out.append(r)
        delta.append({'id':r['id'],'en':r['en'],'vi':r['vi'],'file':n,'origin':origin,'ctx':r.get('ctx')})
    newfiles[n]=(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in out)).encode('utf8')
    newfiles['manual_'+x.replace('.','_')+'.tsv']=('id\ten\tvi\tctx\torigin\n'+''.join('\t'.join(str(y) for y in [r['id'],r['en'],r['vi'],r.get('ctx',''),to_vi(r['en'])[1]])+'\n' for r in out)).encode('utf8')
    newfiles['vi_'+x.replace('.','_')+'.txt']=(''.join(r['id']+'\t'+r['vi']+'\n' for r in out)).encode('utf8')
    changed_slices.append(n)
assert len(delta)==720 and usage['TÁI DÙNG']==148 and usage['DỊCH MỚI']==572,usage
assert len(set(r['en'] for r in delta if r['origin']=='DỊCH MỚI'))==492
assert all(newfiles[n]==files[n] for n in jsnames if n not in keys)
newfiles['DELTA-109.jsonl']=(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in delta)).encode('utf8')
ct=collections.Counter(x['en'] for x in delta)
newfiles['unique_109.tsv']=('index\ten_body\tvi_body\torigin\tpages\n'+''.join('\t'.join(str(v) for v in [i,en,to_vi(en)[0],'DỊCH MỚI',ct[en]])+'\n' for i,en in enumerate(unique,1))).encode('utf8')
new_total=prior_count+720
assert new_total==29931
pc=new_total/55976*100
qa=f'''# QA — Magician's Quest Checkpoint 109 (11/11/2026)

- **PASS:** 501 JSONL files / 55,976 records checked against checkpoint 108.
- **29,211 → 29,931 / 55,976 ({pc:.2f}%)**: 720 new NPC pages in `0045.015`–`0045.020` (6 × 120).
- 148 pages reused with exact English match; **572 pages use 492 freshly localized distinct dialogue patterns**.
- Earlier 29,211 Vietnamese entries were preserved; 495 non-target JSONLs remained byte-identical.
- English source, row IDs, ctx, and other metadata preserved.
- Exact NDS control-token order, color spans, player-name placeholders, and selection codes preserved.
- Translations checked: NFC, <=3 `▼` line breaks, <=34 static Unicode codepoints per segment, regular punctuation.
- ZIP CRC, 501 JSONL parses and 55,976 record total checked again after build.
- **Not tested in ROM:** dynamic placeholder width, font glyph coverage and visual box layout require on-device QA.
- Next 110: remaining `0045.021` (120) + `0045.022` (84) and `0046.001`–`0046.004` (480), total 684 pages.
'''
cp=f'''# Magician's Quest — Checkpoint 109

**Date:** 11/11/2026
**Repository:** `ronvotri/VH-NDS` / `Magicians-Quest-Mysterious-Times/`.

- **+720 NPC pages**, files `0045.015`–`0045.020` (120 pages each).
- Total **29,931/55,976 ({pc:.2f}%)**; NPC **26,806/52,608**.
- **492 newly translated EN dialogue patterns** used on 572 pages; 148 pages reused from previous checkpoints.
- Topics: school gossip, Nessie, Haunted House, Candyman, Sphinx, treasure hunting, Dragon, Martian, werewolf, Death, Jack Frost, homunculus, mermaid, other worlds and nightmares.
- QA: all 501 JSONL files parse successfully, 55,976 records; previous 29,211 translations unchanged; 495 non-target JSONLs preserved exactly.
- Deliverables: complete ZIP, `DELTA-109.jsonl`, `unique_109.tsv`, 6 EN–VI TSVs, six VI sheets, `QA-109.md`, `build_109.py`, `translate_109.py`.
- Next: `0045.021`, `0045.022`, `0046.001`–`0046.004` (684 pages; English sources staged).
- **In-ROM NDS visual QA remains pending.**
'''
head=f'''## Checkpoint 109 — 11/11/2026

- +720 NPC pages, `0045.015`–`0045.020`; **29,931/55,976 ({pc:.2f}%)**.
- 492 newly localized distinct English dialogue patterns, applied to 572 pages; 148 source-exact reuses.
- 501 JSONL QA PASS; existing translations preserved; NDS layout untested.
- Next 110: `0045.021`, `0045.022`, `0046.001`–`0046.004` — 684 pages.

'''
newfiles['QA-109.md']=qa.encode('utf8')
newfiles['CHECKPOINT-2026-11-11-DOT-109.md']=cp.encode('utf8')
newfiles['BAN_GIAO.md']=(head+files['BAN_GIAO.md'].decode('utf8')).encode('utf8')
newfiles['README.md']=(f'**Checkpoint mới nhất: 109 (11/11/2026) — 29.931/55.976 ({pc:.2f}%).** +720 NPC pages `0045.015`–`0045.020`; QA 501 JSONL PASS. Xem `CHECKPOINT-2026-11-11-DOT-109.md` và `QA-109.md`.\n\n'+files['README.md'].decode('utf8')).encode('utf8')
newfiles['build_109.py']=Path(__file__).read_bytes()
newfiles['translate_109.py']=(ROOT/'translate_109.py').read_bytes()
for x in NEXT:
    n=TALK+x+'.jsonl'
    assert n in rowsby and len(rowsby[n])==(84 if x=='0045.022' else 120) and all(r['vi'] is None for r in rowsby[n]),x
with zipfile.ZipFile(OUT,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for k,v in sorted(newfiles.items()):z.writestr(NEW+k,v)
with zipfile.ZipFile(OUT) as z:
    assert z.testzip() is None
    rebuilt={n.removeprefix(NEW):z.read(n) for n in z.namelist()}
    names=[n for n in rebuilt if n.startswith('translation/') and n.endswith('.jsonl')]
    assert len(names)==501
    assert sum(len(rebuilt[n].decode('utf8').splitlines()) for n in names)==55976
    assert all(rebuilt[n]==files[n] for n in jsnames if n not in keys)
    assert sum(sum(json.loads(s).get('vi') is not None for s in rebuilt[n].decode('utf8').splitlines()) for n in names)==new_total
    for n in names:
        for s in rebuilt[n].decode('utf8').splitlines():json.loads(s)
    for x in NEXT:assert rebuilt[TALK+x+'.jsonl']==files[TALK+x+'.jsonl']
for n,v in newfiles.items():
    if n not in files or v!=files[n]:
        fn=STAGE/Path(n).name
        if n.startswith('translation/'): fn=STAGE/Path(n).name.replace('talkfigs__0eng__data__','')
        fn.write_bytes(v)
# Stage next source slices (not modified within bundle); for GitHub add them as source-only files.
for x in NEXT:
    n=TALK+x+'.jsonl'
    (STAGE/(x+'.jsonl')).write_bytes(newfiles[n])
modified=[]
for n,v in newfiles.items():
    if n not in files or v!=files[n]:
        modified.append({'path':'Magicians-Quest-Mysterious-Times/'+n,'name':Path(n).name.replace('talkfigs__0eng__data__','') if n.startswith('translation/') else Path(n).name,'sha':gitsha(v),'bytes':len(v),'newlines':len(v)-len(v.rstrip(b'\n'))})
for x in NEXT:
    n=TALK+x+'.jsonl';v=newfiles[n]
    modified.append({'path':'Magicians-Quest-Mysterious-Times/'+n,'name':x+'.jsonl','sha':gitsha(v),'bytes':len(v),'newlines':len(v)-len(v.rstrip(b'\n'))})
assert len(modified)==32,(len(modified),[m['path'] for m in modified])
(STAGE/'git-manifest.json').write_text(json.dumps(modified,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'output':str(OUT),'bytes':OUT.stat().st_size,'zip_files':len(newfiles),'jsonls':len(jsnames),'prior':prior_count,'total':new_total,'percent':round(pc,2),'unique_new':len(unique),'new_pages':usage['DỊCH MỚI'],'reused_pages':usage['TÁI DÙNG'],'github_changes':len(modified),'next':NEXT},ensure_ascii=False,indent=2))
