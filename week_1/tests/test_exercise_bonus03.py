from io import StringIO
from unittest import TestCase
from unittest.mock import patch

class TestURLPrint(TestCase):
    def test_pattern_stdout(self):
        expected = '''{0:.17}
'''.format((9.5 * 4.5 - 2.5 * 3) / (45.5 - 3.5))

        with patch('sys.stdout', new=StringIO()) as fake_out:
            from week_1 import Exercise_bonus03
            self.assertEqual(fake_out.getvalue(), expected)
