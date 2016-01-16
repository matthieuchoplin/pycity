from io import StringIO
from unittest import TestCase
from unittest.mock import patch

class TestURLPrint(TestCase):
    def test_pattern_stdout(self):
        expected = '''{0:.9}
{1:.9}
'''.format(5.5 * 5.5 * 3.14159, 2 * 5.5 * 3.14159)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            from week_1 import Exercise_bonus02
            self.assertEqual(fake_out.getvalue(), expected)
