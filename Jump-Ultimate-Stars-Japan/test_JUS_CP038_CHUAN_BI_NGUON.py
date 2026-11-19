"""Checkpoint 038 source-loader regression tests.

Rows 0-3 use real CP037 anchors. Rows 4+ are SYNTHETIC TEST DATA,
not original Japanese text and must never be counted as translations.
Run: python -m unittest -v test_JUS_CP038_CHUAN_BI_NGUON.py
"""
import io
import json
import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile
from JUS_CP038_CHUAN_BI_NGUON import ANCHORS, TARGET, get_source, prepare

ORIGINAL_ANCHOR_JA = ('ジャンプの値段はいくら上がったか？', '１４０円', '１０円', '４０円')


def fixture():
    rows = [{'id': aid, 'ja': ja, 'row_index': i}
            for i, (aid, ja) in enumerate(zip(ANCHORS, ORIGINAL_ANCHOR_JA))]
    rows += [{'id': f'SYNTHETIC-TEST-{i}', 'ja': 'テスト文字列', 'row_index': i}
             for i in (4, 5)]
    return rows


def encode(rows):
    return ''.join(json.dumps(x, ensure_ascii=False) + '\n' for x in rows).encode('utf-8')


class ValidateSource(unittest.TestCase):
    def test_resume_row4(self):
        _, pending = prepare(encode(fixture()), 4, 650)
        self.assertEqual([x['row_index'] for x in pending], [4, 5])

    def test_limit_one(self):
        _, pending = prepare(encode(fixture()), 4, 1)
        self.assertEqual([x['row_index'] for x in pending], [4])

    def test_mismatched_anchor(self):
        rows = fixture()
        rows[0]['id'] = 'INVALID'
        with self.assertRaisesRegex(ValueError, '4 ID đầu'):
            prepare(encode(rows), 4, 650)

    def test_duplicate_id(self):
        rows = fixture()
        rows[5]['id'] = rows[4]['id']
        with self.assertRaisesRegex(ValueError, 'ID bị trùng'):
            prepare(encode(rows), 4, 650)

    def test_wrong_row_index(self):
        rows = fixture()
        rows[5]['row_index'] = 8
        with self.assertRaisesRegex(ValueError, 'row_index không khớp'):
            prepare(encode(rows), 4, 650)

    def test_archive_path(self):
        with tempfile.TemporaryDirectory() as d:
            file = Path(d) / 'source.zip'
            with ZipFile(file, 'w') as archive:
                archive.writestr('folder/translation/' + TARGET, encode(fixture()))
            label, data = get_source(file)
            self.assertIn(TARGET, label)
            self.assertEqual(len(prepare(data, 4, 650)[1]), 2)

    def test_nested_zip(self):
        nested = io.BytesIO()
        with ZipFile(nested, 'w') as archive:
            archive.writestr(TARGET, encode(fixture()))
        with tempfile.TemporaryDirectory() as d:
            file = Path(d) / 'outer.zip'
            with ZipFile(file, 'w') as archive:
                archive.writestr('inside.zip', nested.getvalue())
            label, data = get_source(file)
            self.assertIn('inside.zip', label)
            self.assertEqual(len(prepare(data, 4, 650)[1]), 2)

    def test_missing_source_file(self):
        with tempfile.TemporaryDirectory() as d:
            file = Path(d) / 'source.zip'
            with ZipFile(file, 'w') as archive:
                archive.writestr('other.jsonl', encode(fixture()))
            with self.assertRaisesRegex(ValueError, 'hiện tìm thấy 0'):
                get_source(file)

    def test_blank_line(self):
        payload = encode(fixture()).replace(b'\n', b'\n\n', 1)
        with self.assertRaisesRegex(ValueError, 'Dòng trống'):
            prepare(payload, 4, 650)


if __name__ == '__main__':
    unittest.main()
