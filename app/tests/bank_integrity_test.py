"""Regression tests for immutable published IDs and final-build validation."""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'authoring'))
from bank_integrity import history, validate
from rules import SKILLS
from dsl import LEVELS


class IntegrityTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.items = json.loads((ROOT / 'content/items.json').read_text())

    def test_final_bank(self):
        validate(self.items, SKILLS, LEVELS)

    def test_published_answer_cannot_be_replaced(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'published.json'
            old = copy.deepcopy(self.items[0])
            path.write_text(json.dumps([old]))
            changed = dict(old, correct='wrong')
            with self.assertRaisesRegex(ValueError, 'immutable'):
                history([changed], path, record=True)
            self.assertEqual(json.loads(path.read_text()), [old])
            changed['id'] = old['id'] + '-test-revision'
            self.assertEqual(history([changed], path, record=True), [old])
            self.assertEqual(history([changed], path), [old])

    def test_duplicate_ids_rejected(self):
        with self.assertRaisesRegex(ValueError, 'duplicate id'):
            validate(self.items + [self.items[0]], SKILLS, LEVELS)

    def test_missing_translation_rejected(self):
        items = copy.deepcopy(self.items)
        items[0].pop('why_lv')
        with self.assertRaisesRegex(ValueError, 'Latvian'):
            validate(items, SKILLS, LEVELS)

    def test_missing_or_unusable_cards_rejected(self):
        items = copy.deepcopy(self.items)
        gap = next(i for i in items if i.get('bank'))
        gap['bank'].remove(gap['answers'][0][0])
        with self.assertRaisesRegex(ValueError, 'bank'):
            validate(items, SKILLS, LEVELS)


if __name__ == '__main__':
    unittest.main()
