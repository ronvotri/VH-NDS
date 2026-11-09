#!/usr/bin/env python3
"""QA Yu-Gi-Oh! WC2008: xác minh 26 CSV và tạo ket_qua_dich.json.
Dùng: python check_import.py /thu_muc/A35
"""
import sys, csv, re, json, pathlib, collections
if len(sys.argv)!=2: sys.exit(__doc__)
root=pathlib.Path(sys.argv[1]); result={};errors=[];count=0
codes=lambda s:sorted(re.findall(r'@\d+|%(?:\d+)?[dsxc]|%%',s))
for i in range(1,27):
    file=root/f'A_MO_TA_LA_BAI_{i:02d}.csv'
    if not file.is_file(): raise SystemExit(f'Thiếu {file}')
    with file.open(encoding='utf-8-sig',newline='') as f:
        for row in csv.DictReader(f):
            key=row['key'];en=row['tieng_Anh'];vn=row['tieng_Viet_MOI'];mx=int(row['toi_da_ky_tu'])
            issues=[]
            if not vn.strip(): issues.append('trống')
            if len(vn)>mx: issues.append(f'quá dài {len(vn)}/{mx}')
            if codes(en)!=codes(vn): issues.append('sai mã game @/%')
            if any(en.count('\\'+c)!=vn.count('\\'+c) for c in 'nr'):
                issues.append('sai mã xuống dòng')
            if any(ord(x)>127 and x not in 'ĂăÂâĐđÊêÔôƠơƯưÁÀẢÃẠẤẦẨẪẬẮẰẲẴẶÉÈẺẼẸẾỀỂỄỆÍÌỈĨỊÓÒỎÕỌỐỒỔỖỘỚỜỞỠỢÚÙỦŨỤỨỪỬỮỰÝỲỶỸỴáàảãạấầẩẫậắằẳẵặéèẻẽẹếềểễệíìỉĩịóòỏõọốồổỗộớờởỡợúùủũụứừửữựýỳỷỹỵ' for x in vn):
                issues.append('ký tự lạ')
            if issues: errors.append((file.name,key,issues));continue
            g,n,c=key.split('|')
            val=vn.replace('\\r', '\r').replace('\\n','\n')
            result.setdefault(g,{}).setdefault(c,{})[n]=val
            count+=1
if errors:
    for name,key,issues in errors[:50]:print('LỖI',name,key,issues)
    raise SystemExit(f'FAIL: {len(errors)} lỗi')
assert count==2009, f'Sai tổng: {count}/2009'
(root/'ket_qua_dich.json').write_text(json.dumps(result,ensure_ascii=False),encoding='utf-8')
print('PASS 2009/2009; JSON:',root/'ket_qua_dich.json')
