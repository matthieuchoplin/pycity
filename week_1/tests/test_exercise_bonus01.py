from io import StringIO
from unittest import TestCase
from unittest.mock import patch

class TestURLPrint(TestCase):
    def test_pattern_stdout(self):
        expected = '''FFFFFFF   U     U   NN     NN
FF        U     U   NNN    NN
FFFFFFF   U     U   NN N   NN
FF         U   U    NN  N  NN
FF          UUU     NN    NNN
'''

        with patch('sys.stdout', new=StringIO()) as fake_out:
            from week_1 import Exercise_bonus01
            self.assertEqual(fake_out.getvalue(), expected)
