#!/usr/bin/env python3
"""Apply checkpoint 113 translation delta to checkpoint 112's complete ZIP.

Usage:
 python replay_113.py MagiciansQuest-VietHoa-Checkpoint-112.zip DELTA-113.jsonl output.zip

Copies every non-target source byte unchanged; only 'vi' values of the six
0046.017-0046.022 JSONLs are updated, with English/ID/context checks.
"""
import argparse, zipfile, json, pathlib

SRC_PREFIX='MagiciansQuest_112/'
DST_PREFIX='MagiciansQuest_113/'
TARGETS={f'translation/04-thoai/talkfigs__0eng__data__0046.{i:03}.jsonl' for i in range(17,23)}

def apply(source, delta, output):
    updates={}
    with open(delta,encoding='utf-8') as f:
        for line in f:
            if not line.strip():continue
            row=json.loads(line)
            if row['id'] in updates:raise ValueError(f'Duplicate ID: {row["id"]}')
            updates[row['id']]=row
    if len(updates)!=720:raise ValueError(f'Expected 720 delta entries, got {len(updates)}')
    touched=set();counts={}
    with zipfile.ZipFile(source) as src, zipfile.ZipFile(output,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as out:
        if src.testzip() is not None:raise ValueError('Corrupted checkpoint 112 ZIP')
        for item in src.infolist():
            p=item.filename
            if not p.startswith(SRC_PREFIX):raise ValueError(f'Unexpected archive prefix: {p}')
            rel=p[len(SRC_PREFIX):]
            content=src.read(p)
            if rel in TARGETS:
                entries=[json.loads(line) for line in content.decode('utf-8').splitlines()]
                if len(entries)!=120:raise ValueError(f'Expected 120 lines: {rel}')
                counts[rel]=len(entries)
                for e in entries:
                    new=updates[e['id']]
                    if e['en']!=new['en'] or e.get('ctx')!=new.get('ctx') or e.get('vi') is not None:
                        raise ValueError(f'Source mismatch on {e["id"]}')
                    e['vi']=new['vi'];touched.add(e['id'])
                content=('\n'.join(json.dumps(e,ensure_ascii=False) for e in entries)+'\n').encode()
            out.writestr(DST_PREFIX+rel,content)
    if touched!=updates.keys() or len(counts)!=6:
        raise ValueError(f'Unexpected changed records: {len(touched)} / {len(counts)}')
    with zipfile.ZipFile(output) as check:
        bad=check.testzip()
        if bad:raise ValueError(f'Corrupt output: {bad}')
    print(f'PASS: {len(touched)} records in 6 files; other files byte-identical; output={output}')

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('checkpoint_112')
    p.add_argument('delta_113')
    p.add_argument('output_zip')
    a=p.parse_args()
    apply(a.checkpoint_112,a.delta_113,a.output_zip)
