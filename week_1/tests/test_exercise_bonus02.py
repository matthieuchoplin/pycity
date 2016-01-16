from io import StringIO
from math import pi
from unittest import TestCase
from unittest.mock import patch

class TestURLPrint(TestCase):
    def test_pattern_stdout(self):
        expected = '''{0:.2f}
{1:.2f}
'''.format(5.5 * 5.5 * pi, 2 * 5.5 * pi)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            from week_1 import Exercise_bonus02
            self.assertEqual(fake_out.getvalue(), expected)
