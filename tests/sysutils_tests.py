import unittest
from mypyutils import sysutils

class SysUtilsTests(unittest.TestCase):
    def test_chomp(self):
        test_str = 'blablabla\r\n'
        self.assertEqual(test_str, 'blablabla')
