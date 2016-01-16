from io import StringIO
from unittest import TestCase
from unittest.mock import patch

class TestURLPrint(TestCase):
    def test_pattern_stdout(self):
        expected = '''%d
%d
%d
%d
%d
''' % (
            64596800 + 365 * 24 * 60 * 60 // 40 - 365 * 24 * 60 * 60 // 60 + 365 * 24 * 60 * 60 // 100,
            64596800 + 2 * 365 * 24 * 60 * 60 // 40 - 2 * 365 * 24 * 60 * 60 // 60 + 2 * 365 * 24 * 60 * 60 // 100,
            64596800 + 3 * 365 * 24 * 60 * 60 // 40 - 3 * 365 * 24 * 60 * 60 // 60 + 3 * 365 * 24 * 60 * 60 // 100,
            64596800 + 4 * 365 * 24 * 60 * 60 // 40 - 4 * 365 * 24 * 60 * 60 // 60 + 4 * 365 * 24 * 60 * 60 // 100,
            64596800 + 5 * 365 * 24 * 60 * 60 // 40 - 5 * 365 * 24 * 60 * 60 // 60 + 5 * 365 * 24 * 60 * 60 // 100
        )

        with patch('sys.stdout', new=StringIO()) as fake_out:
            from week_1 import Exercise_bonus04
            self.assertEqual(fake_out.getvalue(), expected)
