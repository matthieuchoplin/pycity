from io import StringIO
from unittest import TestCase
from unittest.mock import patch

class TestURLPrint(TestCase):
    def test_pattern_stdout(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            from week_1 import Exercise_bonus05
            self.assertEqual(fake_out.getvalue(), '')
